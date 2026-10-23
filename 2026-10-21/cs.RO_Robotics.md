# cs.RO | Robotics | 2026-10-21

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/具身智能/Physical_Canvas_A_Vision_Tactile_World_Model_For_Robot_Policy_Evaluation_And_Learning|Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning]]

![[assets/2610.28613_figure.png|800]]

- **arXiv**: [2610.28613](https://arxiv.org/abs/2610.28613)
- **PDF**: https://arxiv.org/pdf/2610.28613
- **详细分析**: [[20_Research/Papers/具身智能/Physical_Canvas_A_Vision_Tactile_World_Model_For_Robot_Policy_Evaluation_And_Learning|Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning]]
- **作者**: Zebin Xing, Yuhang Zheng, Yupeng Zheng, Yichen Zhang, Zichen Li, Shangqing Zhou, Yujie Zang, Yuchen Liu, Zhongpu Xia, Haoran Li, Qichao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习, 大模型
- **相关性评分**: 3.0（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，世界模型 1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FeelWorld, GigaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators. However, visually plausible predictions can misrepresent contact dynamics, providing unreliable feedback for policy evaluation and learning. We introduce PhysCanvas, a state-consistent visuo-tactile world model for contact-rich robot manipulation. PhysCanvas unifies multi-view RGB, tactile images, marker displacement, task state, and actions within a unified vision space. All modalities share a video VAE and pretrained generative backbone, allowing optical touch to reuse visual and temporal priors. Motion images derived through forward kinematics and camera projection provide spatially aligned action conditioning, while an initial RGB anchor and updated reference observations guide sequential generation. Our consistency-aware post-training uses the frozen Scene Reward Model, Modality Reward Model, and State Reward Model to supervise scene preservation, visual-tactile compatibility, and agreement with real task outcomes. The resulting world model supports closed-loop policy rollouts for evaluation and provides imagined interactions and rewards for GRPO policy updates. Across four real-world manipulation tasks, when policies are rolled out in the world model, State Reward Model supervision increases the arithmetic mean of task-wise Pearson correlations between world-model and real-world success rates from 0.602 to 0.885. Policy post-training in the reward-guided world model further increases $π_{0.5}$'s mean real-world success rate from a 59.1% SFT baseline to 70.8%. These results demonstrate the value of unified multimodal modeling and consistency-aware post-training for robot policy evaluation and learning. Project page: https://zebinx.github.io/PhysCanvas_HomePage/.

</details>

---

### [[20_Research/Papers/具身智能/AgenticRoboRL_Bringing_Coding-Agent_Post-Training_to_Agentic_Robotics|AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics]]

![[assets/2610.28589_figure.png|800]]

- **arXiv**: [2610.28589](https://arxiv.org/abs/2610.28589)
- **PDF**: https://arxiv.org/pdf/2610.28589
- **详细分析**: [[20_Research/Papers/具身智能/AgenticRoboRL_Bringing_Coding-Agent_Post-Training_to_Agentic_Robotics|AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics]]
- **作者**: Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao, Chen Chen, Yuzhang Shang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 强化学习
- **相关性评分**: 2.5（加权：具身智能 0.6，大模型 0.4，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgenticRoboRL, CaP-RL, LEGO-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic robotics systems combine planners with robot harnesses to perform complex manipulation tasks. Recent work improves these systems through better harnesses and external memory, but relies on powerful closed-source models as planners and does not improve the planners' own capabilities. In contrast, coding agents have improved substantially by post-training the model itself. We therefore investigate whether post-training can also improve robot planners. However, applying it across robot harnesses requires accommodating different execution mechanisms, including VLA skill invocation and control-code generation. To this end, we introduce AgenticRoboRL, a framework for post-training robot planners across different harnesses. The training recipe combines supervised fine-tuning with multi-turn reinforcement learning. To accommodate different execution mechanisms, harness-specific adapters connect recorded planner interactions with task outcomes, enabling a common RL training pipeline while keeping execution components fixed. On LIBERO-PRO, AgenticRoboRL raises the success rate of a 9B-parameter planner from 18.1% to 71.0% without external memory, approaching the 72.1% achieved by Codex (GPT-5.5) with external memory. These results demonstrate post-training as an effective approach for improving robot planners. We will release the framework and trained planner checkpoints.

</details>

---

### [[20_Research/Papers/强化学习/SuperMimic_Scaling_Humanoid_Whole-Body_Control_with_One_Differentiable_World_Model|SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model]]

![[assets/2610.28480_first_page.png|800]]

- **arXiv**: [2610.28480](https://arxiv.org/abs/2610.28480)
- **PDF**: https://arxiv.org/pdf/2610.28480
- **详细分析**: [[20_Research/Papers/强化学习/SuperMimic_Scaling_Humanoid_Whole-Body_Control_with_One_Differentiable_World_Model|SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model]]
- **作者**: Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz, Pieter Abbeel, Koushil Sreenath
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 3.6（加权：具身智能 1.5，强化学习 0.2，世界模型 0.8，机器人 1.1）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tracking large human-motion datasets has become the dominant route to general, expressive humanoid whole-body control, but scaling across many motions is expensive. Current pipelines use model-free reinforcement learning, either merging per-motion specialists through lossy distillation, or brute-forcing a single policy with cluster-scale compute. SuperMimic amortizes learning across all motions with one differentiable world model of their shared dynamics, fit from logged transitions of a standard rigid-body simulator. The world model and the tracking policy train together in one loop, and backpropagation-through-time over short imagined rollouts gives the policy analytic gradients. Fast imagined rollouts and analytic gradients make policy learning efficient. In 3 hours on a single GPU, SuperMimic surpasses the return of a state-of-the-art motion tracker baseline trained for 7 days on 128 GPUs. It reduces GPU-hours by more than $1000\times$ and fails on only 25 of 129,514 benchmark motions, versus 179 failures for the baseline. After 9.8 hours on two GPUs, SuperMimic achieves zero failures. From 1 to 264 hours of motion, the world model's prediction error stays stable, and GPU-hours to a target return grow slowly. Our policy transfers to a physical Unitree G1 across diverse and acrobatic motions. SuperMimic removes compute as the bottleneck to scaling humanoid whole-body control, making it practical to measure motion-tracking scaling laws.

</details>

---

### [[20_Research/Papers/强化学习/Fast_Motion_Retargeting_Pipeline_for_Scalable_Humanoid_Robot_Learning|Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning]]

![[assets/2610.28470_figure.png|800]]

- **arXiv**: [2610.28470](https://arxiv.org/abs/2610.28470)
- **PDF**: https://arxiv.org/pdf/2610.28470
- **详细分析**: [[20_Research/Papers/强化学习/Fast_Motion_Retargeting_Pipeline_for_Scalable_Humanoid_Robot_Learning|Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning]]
- **作者**: Daniel Marew, Sangjun Park, Nisal Perera, Donghyun Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.9（加权：具身智能 1.8，强化学习 0.2，机器人 1.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning, retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV (Fast Retargeting with Dynamics Validation), a scalable framework consisting of rapid constrained kinematic retargeting and an additional dynamics validation pipeline. Its kinematic stage integrates a custom Sequential Quadratic Programming solver, Real-Time Iteration, and parallel chunk-based processing, achieving up to 9,156 frames per second, approximately up to 136 times faster than GMR and ProtoMotions, while robot-specific constraints are incorporated into the optimization to reduce common retargeting artifacts, such as ground penetration and self-collision. For motions requiring additional verification, a contact implicit iLQR controller is utilized to test the retargeted reference under full rigid body dynamics. This dynamics-based validation identifies dynamically infeasible motions and refines contact-related artifacts such as foot floating and foot skating. We evaluate retargeting quality by training motion tracking reinforcement learning policies using several state-of-the-art pipelines and comparing their tracking fidelity and success rates. Furthermore, sim-to-real transfer is demonstrated on a Unitree G1 humanoid. Videos and code are available at: https://daroslab.github.io/frdv/.

</details>

---

### [[20_Research/Papers/具身智能/Physical_AI_for_Intralogistics_Benchmarking_the_NVIDIA_Sim-to-Real_Ecosystem_for_Cosmos-Enhanced_COMPASS_Navigation_on_Industrial_Mobile_Rob|Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots]]

![[assets/2610.28432_figure.png|800]]

- **arXiv**: [2610.28432](https://arxiv.org/abs/2610.28432)
- **PDF**: https://arxiv.org/pdf/2610.28432
- **详细分析**: [[20_Research/Papers/具身智能/Physical_AI_for_Intralogistics_Benchmarking_the_NVIDIA_Sim-to-Real_Ecosystem_for_Cosmos-Enhanced_COMPASS_Navigation_on_Industrial_Mobile_Rob|Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots]]
- **作者**: Charbel Abi Hana, Rayan Zaitouni, Kameel Amareen, Mohamad Mostafa, Hasan Sayour, Wei Liu, Yan Chang, Mihir Acharya, Anthony Rizk
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Classical robot navigation stacks are reliable but often require re-engineering for each new robot type and site. Learning-based navigation shifts this effort from hand-tuned parameters to data generation and training, where a policy adapts to each new embodiment or facility by fine-tuning in simulation. Whether policies adapted this way stay reliable on real industrial robots has seen little systematic testing. We study this for NVIDIA's X-Mobility and COMPASS workflow for training learned navigation policies on Idealworks robots. In simulation, we extend the COMPASS benchmark with two embodiments, the differential-drive iw.hub and an omnidirectional Humanoid Mobile Platform (HMP), and with a digital twin of the Idealworks R&amp;D center. For the real world, we fine-tune X-Mobility on data from this digital twin, with and without sim-to-real variants generated by NVIDIA Cosmos, train COMPASS on top of it from scratch in the digital twin, deploy the resulting policies on the iw.hub's onboard Jetson AGX Xavier, and benchmark them in the Idealworks R&amp;D center against COMPASS trained only on NVIDIA's environments and the existing Idealworks navigation stack on task success, efficiency, safety, smoothness and onboard compute. Running every static scenario both in a digital-twin replica and in the real facility measures the sim-to-real gap and how far Cosmos-augmented data closes it. Training in the digital twin with Cosmos sim-to-real augmentation raises the real-world success rate of learned navigation from 65.3% to 91.7% across four scenarios and nearly halves its weighted travel time compared with simulation-only training, bringing it within 8.3 points of the production navigation stack, fully onboard; with an integrated global planner, it also reaches far, occluded goals in every trial.

</details>

---

### [[20_Research/Papers/强化学习/Reinforced_Iterative_Learning_Control_for_elastic_joint_arms_Guaranteed_cross-trajectory_generalization_under_model_uncertainties|Reinforced Iterative Learning Control for elastic joint arms: Guaranteed cross-trajectory generalization under model uncertainties]]

![[assets/2610.28329_figure.png|800]]

- **arXiv**: [2610.28329](https://arxiv.org/abs/2610.28329)
- **PDF**: https://arxiv.org/pdf/2610.28329
- **详细分析**: [[20_Research/Papers/强化学习/Reinforced_Iterative_Learning_Control_for_elastic_joint_arms_Guaranteed_cross-trajectory_generalization_under_model_uncertainties|Reinforced Iterative Learning Control for elastic joint arms: Guaranteed cross-trajectory generalization under model uncertainties]]
- **作者**: Yuri De Santis, Michele Pierallini, Franco Angelini, Manolo Garabini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reinforced Iterative Learning Control for elastic joint arms: Guaranteed cross-trajectory generalization under model uncertainties》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trajectory tracking for compliant robots is challenging due to nonlinear dynamics and modeling uncertainties, often requiring learning-based methods to avoid explicit parameter identification. Iterative Learning Control (ILC) ensures theoretically high precision and preserves the passive compliance of the robot. However, traditional ILC requires a separate learning phase for each new trajectory. Conversely, Reinforcement Learning (RL) generalizes to new trajectories, but practically suffers from high sample complexity and limited tracking precision. This work proposes Reinforced Iterative Learning Control (RILC) that combines the strengths of both approaches to achieve fast adaptation and guaranteed tracking convergence across diverse trajectories. By establishing a concurrent coupling between the two controllers, RILC overcomes the high initial errors and slow adaptation of traditional ILC, enabling high-performance tracking from the very first trials. In this architecture, ILC provides high-quality samples, while RL contributes as a generalizing best-effort policy across iterations. Additionally, a theoretical proof is presented to show that the RL component preserves ILC stability and, under specific conditions, can also reduce the error bound asymptotically. The efficacy of this framework is demonstrated through simulation and experiments on an underactuated 4-degree-of-freedom serial elastic robot using different trajectories and modeling mismatches.

</details>

---

### [[20_Research/Papers/具身智能/Large_Multimodal_Models_for_Direct_Robot_Control_GPT-6_as_a_Beginning|Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning]]

![[assets/2610.28259_figure.png|800]]

- **arXiv**: [2610.28259](https://arxiv.org/abs/2610.28259)
- **PDF**: https://arxiv.org/pdf/2610.28259
- **详细分析**: [[20_Research/Papers/具身智能/Large_Multimodal_Models_for_Direct_Robot_Control_GPT-6_as_a_Beginning|Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning]]
- **作者**: Youwei Zhou, Bohan Hou, Yankai Fu, Yaoxu Lyu, Yifan Ye, Shilin Shan, Chen Guo, Jiaming Liu, Ran He, Caifeng Shan, Shanghang Zhang, Jianfei Yang...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.9，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in visuospatial understanding and agentic reasoning enable direct robotic manipulation with general-purpose multimodal models, but their embodied capabilities remain poorly understood. This paper systematically evaluate GPT-6 Astra for closed-loop robotic manipulation using a lightweight agent execution framework. We first probe three fundamental embodied capabilities-depth perception, embodied in-context learning, and tactile understanding-and demonstrate that the model can exploit depth information, acquire simple manipulation strategies from contextual demonstrations, and use tactile feedback to correct its actions. We then evaluate GPT-6 Astra across five established manipulation benchmarks along six capability dimensions. Despite competitive performance on several benchmarks-26.92\% success on RoboDojo and 76.0\% on RoboTwin 2.0-our analysis reveals a pronounced gap between semantic reasoning and physical execution, particularly in consequence-aware action planning, precision, and complex motion coordination. To further examine these limitations, we introduce LIBERO-GeoMotion, a new benchmark of geometry-constrained tasks that require precise pose alignment, coordinated translation and rotation, and anticipation of physical action consequences. GPT-6 Astra achieves only 11.1\% zero-shot success, exposing the difficulty of translating spatial understanding into physically feasible motion. Real-world experiments corroborate these findings: zero-shot execution is feasible for simple tasks, yet persistent deficits remain in motion feasibility, precise control, and physical safety, while substantial inference latency further hinders practical deployment. Overall, our results characterize the emerging embodied capabilities of general-purpose multimodal models and delineate the key challenges toward safe, efficient, and reliable robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Safe_Multi-Robot_Collaboration_With_Uniform_Exclusion_Using_Trust|Safe Multi-Robot Collaboration With Uniform Exclusion Using Trust]]

![[assets/2610.28251_figure.png|800]]

- **arXiv**: [2610.28251](https://arxiv.org/abs/2610.28251)
- **PDF**: https://arxiv.org/pdf/2610.28251
- **详细分析**: [[20_Research/Papers/机器人/Safe_Multi-Robot_Collaboration_With_Uniform_Exclusion_Using_Trust|Safe Multi-Robot Collaboration With Uniform Exclusion Using Trust]]
- **作者**: Thomas Kaminsky, Áron Vékássy, Hammad Izhar, Angelia Nedić, Stephanie Gil
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Safe Multi-Robot Collaboration With Uniform Exclusion Using Trust》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot swarms coordinate through directed, time-varying local communication links, some of which may be compromised to allow the transmission of arbitrary malicious data. We provide an algorithm that acts as a wrapper around robot communication---when a robot seeks to update its state using data from some incoming links, our wrapper provides a subset of trusted links whose data can be safely incorporated. It selects these links by testing a stream of trust values---data collected from an anomaly detector on each robot---using Safe Anytime-Valid Inference. We require only that the detector be better than chance. This wrapper ensures safe and performant autonomy by providing two powerful statistical guarantees: it uniformly excludes all compromised links for all time with high user-chosen probability, but nevertheless quickly learns to trust legitimate links. Both guarantees are vital to secure generic tasks, but no previous work provides them simultaneously without restrictive assumptions on connectivity structure or the number of compromised links that are not guaranteed in practice. We study our Safe Wrapper's performance in hardware for two contrasting tasks---neural implicit mapping and heading consensus---deploying on 3 LoCoBots and 8 GoPiGos, respectively. We provide simulations using trust values sampled from hardware to validate that our approach scales well to swarms of hundreds of robots.

</details>

---

### [[20_Research/Papers/具身智能/Reasoning_as_a_Distribution_Generative_Plan_Latents_for_Vision-Language-Action_Models|Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models]]

![[assets/2610.28166_figure.png|800]]

- **arXiv**: [2610.28166](https://arxiv.org/abs/2610.28166)
- **PDF**: https://arxiv.org/pdf/2610.28166
- **详细分析**: [[20_Research/Papers/具身智能/Reasoning_as_a_Distribution_Generative_Plan_Latents_for_Vision-Language-Action_Models|Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models]]
- **作者**: Matteo Cercola, Katie Z Luo, Milan Ganai, John Alora, Simone Formentin, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Reasoning as a Distribution: Generative Plan Latents for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, ECoT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies increasingly reason before acting, but existing reasoning models compress this intermediate decision into a single representation. When several plans are valid, this commitment hides alternatives that could otherwise be selected or revised. We introduce the Generative Plan Latent (GPL), which represents the reasoning state as a low-dimensional conditional distribution over plans, such as which object, grasp, or route to use. This makes the reasoning state addressable: without retraining the VLA, plans can be sampled (coverage), selected on request (steering), and reweighted by deployment outcomes (outcome adaptation). We test all three on SimplerEnv manipulation with $π_0$, and extend the analysis to RoboCasa, LIBERO, and a maze domain. Steering the plan raises the fraction of executions that follow the request from 0.48 to 0.94, while the same guidance on the native action distribution shows no reliable gain. Finally, we show that an explicit plan is most useful when it carries decision information not already determined by the observation.

</details>

---

### [[20_Research/Papers/具身智能/From_Predictive_Geometry_to_Action_Learning_Complementary_Predictive_Representations_for_Embodied_Manipulation|From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation]]

![[assets/2610.28164_figure.png|800]]

- **arXiv**: [2610.28164](https://arxiv.org/abs/2610.28164)
- **PDF**: https://arxiv.org/pdf/2610.28164
- **详细分析**: [[20_Research/Papers/具身智能/From_Predictive_Geometry_to_Action_Learning_Complementary_Predictive_Representations_for_Embodied_Manipulation|From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation]]
- **作者**: Xiaoxu Xu, Hao Li, Hongtao Zhang, Yili Tang, Jiafei Cao, Junhao Cai, Haoxiang Ma, Weixin Li, Weinan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《From Predictive Geometry to Action: Learning Complementary Predictive Representations for Embodied Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective manipulation requires a policy to capture not only about the current scene geometry, but also about how that geometry will evolve under interaction. Existing approaches either augment policies with geometric information from current observations or introduce future prediction as auxiliary supervision, leaving open how predictive geometry should be represented for action generation. Therefore, we propose a two-stage framework, which learns complementary predictive representations from multi-view video clips. During pretraining, a frozen 3D foundation model provides dense geometric features that are compressed into predictive geometric representations and optimized to preserve scene structure and its temporal evolution. Action supervision is then applied to geometric transitions to extract a complementary motor representation that emphasizes action-relevant transitions. During downstream post-training, predictive geometry is transferred through geometry queries, while the motor representation guides intermediate features along the action-generation pathway. Future observations are used only as privileged supervision during training and are not required at inference time. Across LIBERO, LIBERO-Plus, SimplerEnv, and real-world bimanual and single-arm tasks, our approach consistently improves downstream policies, including an absolute gain of 10.4 percentage points on the WidowX evaluation. We further demonstrate transfer across multiple VLA architectures and WAMs, with improvements in both future-world and action prediction. The code will be available at https://github.com/xuxiaoxxxx/CPR.

</details>

---

### [[20_Research/Papers/具身智能/FIT-MAC_A_Closed-Loop_Multi-Agent_Framework_for_Robust_Vision-Language-Action_Models|FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models]]

![[assets/2610.28109_figure.png|800]]

- **arXiv**: [2610.28109](https://arxiv.org/abs/2610.28109)
- **PDF**: https://arxiv.org/pdf/2610.28109
- **详细分析**: [[20_Research/Papers/具身智能/FIT-MAC_A_Closed-Loop_Multi-Agent_Framework_for_Robust_Vision-Language-Action_Models|FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models]]
- **作者**: Jiatong Li, Jisheng Dang, Qiangqiang Ma, Bimei Wang, Jingwen Zhao, Wenjun Ma, Juncheng Li, Hong Peng, Bin Hu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.4，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AtomVLA, GTA-VLA, OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have achieved strong performance on standard robotic manipulation benchmarks. However, their reliability can degrade substantially when task conditions deviate from the nominal setting. Perturbations in object positions and task instructions may lead to complete task failure. Existing VLA policies generally lack an explicit runtime mechanism for distinguishing these failure modes and selecting an appropriate recovery strategy. To systematically mitigate this issue, we propose FIT-MAC, a failure-aware, closed-loop multi-agent control framework for improving the robustness of VLA policies at inference time. FIT-MAC augments a VLA policy with an inference-time control layer. First, the Planner Agent parses the language instruction into a structured task specification that captures the manipulation goal and spatial constraints, and the Grounder Agent resolves each instruction-level reference to a visual target. Next, the Verifier Agent tracks phase-specific execution progress, distinguishes target-binding errors from local execution failures, and determines whether intervention is warranted. The Correction Agent then routes permitted interventions to target rebinding or bounded grasping or placement recovery, depending on the failure type. When no intervention is required, the pretrained VLA remains the default action generator. Extensive experiments on LIBERO-PRO demonstrate that FIT-MAC improves robustness across multiple VLA backbones, consistently increasing success rates and achieving state-of-the-art performance under diverse perturbations.

</details>

---

### [[20_Research/Papers/具身智能/PACT-VLA_Speculative_Action-Chunk_Verification_with_Pre-Commit_Observations|PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations]]

![[assets/2610.28019_figure.png|800]]

- **arXiv**: [2610.28019](https://arxiv.org/abs/2610.28019)
- **PDF**: https://arxiv.org/pdf/2610.28019
- **详细分析**: [[20_Research/Papers/具身智能/PACT-VLA_Speculative_Action-Chunk_Verification_with_Pre-Commit_Observations|PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations]]
- **作者**: Yixiang Zhu, Ruilong Wu, Yonghao Chen, Jiaxiang Zou, Yusong Hu, Xinyu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PACT-VLA: Speculative Action-Chunk Verification with Pre-Commit Observations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PACT-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies are commonly deployed with asynchronous inference in real-world settings, where the next action chunk is generated while the robot is still executing the previous one. By the time the new chunk is committed, the robot and scene have changed, so the chunk is conditioned on a stale observation and task success drops sharply as this inference delay grows. Generating multiple candidate chunks could let newer observations inform the final choice, but existing multi-candidate methods either rank candidates with the stale inference-start observation or repeatedly switch between candidates during execution, which can make the executed action sequence discontinuous. Our key insight is that inference delay can be used as decision time. While candidate generation is still underway, candidate selection can reuse the VLA itself to choose the complete action chunk that best fits a later observation. We propose PACT-VLA, a training-free framework that generates candidates from the inference-start observation and selects one using this pre-commit observation. Its scoring function, FlowRes, measures the residual between each candidate's implied flow direction and the velocity predicted by the frozen policy under the pre-commit observation, requiring no separate verifier. A pipelined implementation overlaps observation processing with candidate generation and batches scoring, so selection adds no control-step delay on the evaluated hardware. At a four-step delay, PACT-VLA improves average success by 15.0 percentage points over RTC on Kinetix and by 5.2 points over single-candidate asynchronous execution with GR00T N1.7 on LIBERO, and it further improves existing delay-robust methods. On three real-robot tasks, it raises average success from 60% to 82% over naive asynchronous execution with the same frozen $π_{0.5}$ checkpoint.

</details>

---

### [[20_Research/Papers/大模型/LocoPilot_Single-Operator_Bilateral_Teleoperation_for_Loco-Manipulation_Policy_Learning|LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning]]

![[assets/2610.27998_figure.png|800]]

- **arXiv**: [2610.27998](https://arxiv.org/abs/2610.27998)
- **PDF**: https://arxiv.org/pdf/2610.27998
- **详细分析**: [[20_Research/Papers/大模型/LocoPilot_Single-Operator_Bilateral_Teleoperation_for_Loco-Manipulation_Policy_Learning|LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning]]
- **作者**: Antonio Langella, Giovanni Minelli, Giovanni B. Dessy, Lorenzo Amatucci, Giulio Turrisi, Victor Barasuol, Claudio Semini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation allows to capture these signals directly, but requires an interface capable of commanding the complete system concurrently. This paper presents LocoPilot, a single-operator bilateral teleoperation and data-collection framework implemented on a 12-DoF Unitree Go2 quadruped equipped with a 6-DoF AgileX Piper L manipulator, an Intel RealSense D435 wrist camera, and an Intel RealSense D405 head camera. A second 6-DoF Piper L arm, used as the leader and two handheld controllers provide simultaneous control of the base, body posture, manipulator, and gripper. The follower arm interaction forces are estimated without a dedicated force/torque sensor and rendered to the operator through a passivity-constrained haptic channel. A ROS~2 pipeline records synchronized multimodal observations together with a unified 11D action shared by teleoperation and policy deployment. Compared to prior work, LocoPilot uniquely unifies robot-in-the-loop legged data collection, force feedback without motion-capture instrumentation, and the same action interface at deployment. We evaluate the interface across multiple loco-manipulation tasks and validate the complete collection-to-deployment pipeline by fine-tuning MolmoAct2 \cite{MOLMO} on pick-and-place demonstrations and deploying on the physical robot without action retargeting or additional inverse kinematics. Code available at: https://github.com/iit-DLSLab/LocoPilot

</details>

---

### [[20_Research/Papers/具身智能/EventSync_Event-Driven_Memory_Updates_for_History-Dependent_Manipulation|EventSync: Event-Driven Memory Updates for History-Dependent Manipulation]]

![[assets/2610.27917_figure.png|800]]

- **arXiv**: [2610.27917](https://arxiv.org/abs/2610.27917)
- **PDF**: https://arxiv.org/pdf/2610.27917
- **详细分析**: [[20_Research/Papers/具身智能/EventSync_Event-Driven_Memory_Updates_for_History-Dependent_Manipulation|EventSync: Event-Driven Memory Updates for History-Dependent Manipulation]]
- **作者**: Jingjiao Zhao, Dong Jing, Mingyu Cao, Ruochuan Shi, Xiansheng Chen, Pengwei Wang, Zhiwu Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.9，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《EventSync: Event-Driven Memory Updates for History-Dependent Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

History-dependent robotic manipulation requires task context and interaction history, as the current observation alone is insufficient to determine the next action. Hierarchical frameworks use task memory for high-level subgoal reasoning and low-level policies for execution. However, memory updates require accurate completion assessment: similar observations may correspond to different execution phases, and prematurely recording completion can mislead subsequent subgoal reasoning. We present EventSync, a hierarchical framework that coordinates task reasoning and action execution through event-driven memory updates. A vision-language model generates subgoals from task plans and interaction history, while a vision-language-action model executes them. A lightweight Event Monitor combines visual observations with end-effector trajectories to determine whether the current subgoal is complete. The framework records the current subgoal in its completed-subgoal history and triggers subsequent reasoning only after obtaining completion evidence. With visual history in the executor, EventSync achieves 64.5% overall success on RoboMME, exceeding the best baseline reported in the benchmark by 20.0 percentage points. Further analysis shows that this update mechanism helps build a reliable completed-subgoal history. Experiments on four real-robot tasks with different memory requirements validate the framework's effectiveness in real-world robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/High-Precision_RCM_Motion_for_Ophthalmic_Robotics_via_Hierarchical_QP_Control_and_Authority-Guided_Recovery_Planning|High-Precision RCM Motion for Ophthalmic Robotics via Hierarchical QP Control and Authority-Guided Recovery Planning]]

![[assets/2610.27905_figure.png|800]]

- **arXiv**: [2610.27905](https://arxiv.org/abs/2610.27905)
- **PDF**: https://arxiv.org/pdf/2610.27905
- **详细分析**: [[20_Research/Papers/机器人/High-Precision_RCM_Motion_for_Ophthalmic_Robotics_via_Hierarchical_QP_Control_and_Authority-Guided_Recovery_Planning|High-Precision RCM Motion for Ophthalmic Robotics via Hierarchical QP Control and Authority-Guided Recovery Planning]]
- **作者**: Huanyu Tian, Adriana Namour, Lingyun Zeng, Zicong Wu, Sebastien Ourselin, Lyndon da Cruz, Christos Bergeles
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《High-Precision RCM Motion for Ophthalmic Robotics via Hierarchical QP Control and Authority-Guided Recovery Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose manipulators can position ophthalmic instruments under a software Remote Centre of Motion (RCM). However, at some reachable configurations that are nonsingular for the tip task alone, the RCM and tip-tracking objectives conflict and the servo oscillates. We formalise this failure as a constraint-induced task singularity: the RCM-projected tip Jacobian loses rank while the unprojected tip Jacobian stays well conditioned. Thus, the effective tip authority collapses although the target remains reachable. We present a high-precision RCM servo architecture with built-in singularity recovery: for each commanded target, an authority-guided planner selects a well-conditioned arm configuration that reaches it and plans an RCM-consistent route, executed by a fixed hierarchical-QP controller. On a 200-scenario kinematic benchmark, the complete nominal-and-recovery protocol reaches 128/128 near-singular targets and 71/72 near-joint-limit targets (100% and 99%, respectively), with the software-RCM residual below 0.142 mm. On a physical 6-DOF arm it executes across four RCM entry points, with a worst-case kinematically reconstructed RCM residual of 178 μm and a median tip-regulation error of 32μm, within the 200μm control requirement adopted for the ophthalmic task.

</details>

---

### [[20_Research/Papers/具身智能/Frontier_LLMs_Enter_the_World_of_Robotics_A_Cross-Model_Evaluation_on_RoboColiseum|Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum]]

![[assets/2610.27865_figure.png|800]]

- **arXiv**: [2610.27865](https://arxiv.org/abs/2610.27865)
- **PDF**: https://arxiv.org/pdf/2610.27865
- **详细分析**: [[20_Research/Papers/具身智能/Frontier_LLMs_Enter_the_World_of_Robotics_A_Cross-Model_Evaluation_on_RoboColiseum|Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum]]
- **作者**: Da Huang, Jichao Wang, Junhui Wu, Tong Ran, Linting Guo, Siying Zhang, Chuang Men, Sukai Wang, Yue Zhou, Maoqing Yao, Mo Wu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.9，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies have explored the potential of multimodal large language models for robot control, yet the models' embodied capabilities remain insufficiently characterized across models, tasks, and execution settings. We conduct a multidimensional comparative evaluation on RoboColiseum across four tracks: Instruction Following, Spatial Reasoning, General Manipulation, and Robustness. We implement Agent2Act, a control harness that integrates GPT-6 Astra, GPT-6.1 Sol, Claude Opus 5.5, and Gemini 4 Argon into the evaluation environment through shared observation, action execution, and feedback interfaces. Under common task settings and scoring criteria, all four models exhibit a consistent capability profile: high instruction-following scores, with three approaching perfect performance; strong spatial reasoning; and general manipulation scores below those of the other three tracks. Within the evaluated configurations, Astra leads instruction following and robustness, while Opus leads spatial reasoning, general manipulation, and overall performance. These results reveal complementary strengths across models and a persistent gap between task understanding and reliable physical execution. Component comparisons on selected tasks further show that harness design affects task success, planning cost, and execution time. Additionally, case studies with Astra examine whole-body coordination, manipulation across robot embodiments, precision manipulation, dexterous-hand manipulation, and real-robot tasks, providing further insight into the model's capabilities and limitations across embodied tasks.

</details>

---

### [[20_Research/Papers/具身智能/RoboCasa-Shift_Stage-Aware_Robustness_Evaluation_of_Vision-Language-Action_Policies_in_Long-Horizon_Household_Manipulation|RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation]]

![[assets/2610.27861_figure.png|800]]

- **arXiv**: [2610.27861](https://arxiv.org/abs/2610.27861)
- **PDF**: https://arxiv.org/pdf/2610.27861
- **详细分析**: [[20_Research/Papers/具身智能/RoboCasa-Shift_Stage-Aware_Robustness_Evaluation_of_Vision-Language-Action_Policies_in_Long-Horizon_Household_Manipulation|RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation]]
- **作者**: Haocheng Wang, Youquan Liu, Weiyu Guo, Aokai Zhang, Donghang Wu, Hongyu Liu, Sha Zhang, Weidong Yang, Ben Fei
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) robustness is commonly summarized by aggregate task success, which obscures how individual executions change under distribution shifts and where failures emerge in long-horizon tasks. We introduce \textbf{RoboCasa-Shift}, a diagnostic robustness benchmark built on RoboCasa365 that combines controlled single-factor shifts, matched clean-perturbed rollouts in which each pair shares the same underlying settings and differs only in the target shift, and simulator-grounded stage-aware diagnostics. We evaluate GR00T N1.5 on four long-horizon tasks that pass a predefined clean-performance gate under four perturbation factors and three calibrated severity levels, including conditions that drive the evaluated policy to complete task failure, totaling 1,040 formal rollouts. Robustness responses vary substantially across factors and tasks, and increasing severity does not always produce monotonic degradation. For example, one camera condition yields $Δ\mathrm{SR}=0$ despite 8 of 80 matched episodes changing outcome. Stage-aware analysis further shows that the same end-to-end degradation can correspond to different execution-depth profiles. Camera $L_2$ and Gaussian blur $L_1$ both yield $Δ\mathrm{SR}=0.188$, yet their first-stage failure rates are 19.0\% and 36.4\%, respectively. Our findings suggest that VLA robustness should be viewed as a multi-dimensional property of execution rather than a single end-to-end performance measure, motivating evaluation protocols that jointly capture outcome degradation, paired outcome sensitivity, and failure progression. The code is publicly available at https://github.com/HaochengWang23/RoboCasa-Shift.

</details>

---

### [[20_Research/Papers/强化学习/Multi-View_Latent_Action_Pretraining_for_Cross-Embodiment_Robot_Learning_from_Videos|Multi-View Latent Action Pretraining for Cross-Embodiment Robot Learning from Videos]]

![[assets/2610.27794_figure.png|800]]

- **arXiv**: [2610.27794](https://arxiv.org/abs/2610.27794)
- **PDF**: https://arxiv.org/pdf/2610.27794
- **详细分析**: [[20_Research/Papers/强化学习/Multi-View_Latent_Action_Pretraining_for_Cross-Embodiment_Robot_Learning_from_Videos|Multi-View Latent Action Pretraining for Cross-Embodiment Robot Learning from Videos]]
- **作者**: Oliver Hausdörfer, Felix Minzenmay, Mani Majd, Maximilian P. Christof, Shiyuan Zhang, Angela P. Schoellig
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Multi-View Latent Action Pretraining for Cross-Embodiment Robot Learning from Videos》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-free videos are an appealing substitute for costly teleoperated data. Latent action models (LAMs) turn videos into a supervision signal by inferring abstract actions between frames. Existing LAMs observe a single camera view, which resolves 6D robot actions only ambiguously missing out-of-plane movements and potential occlusions. We propose a LAM that ingests synchronized multi-camera views using cross-attention to resolve depth and occlusions before compressing them into latent actions. The latent actions are fed into a policy in which a latent expert and an action expert are coupled by sequential flow matching around a frozen VLM backbone. We further evaluate in strict cross-embodiment settings where task-specific demonstrations come from other embodiments. We show that dual-view LAM pretraining improves the decodability of ground-truth 6D actions by 17% compared to single-view, while scaling single-view data by two orders of magnitude is not sufficient to fully recover out-of-plane motions. The downstream policy improves success rate by +13.5% compared to +6.2% for single-view LAM. A single cross-embodiment is sufficient for skill transfer, and adding a second viewpoint outperforms adding up to four further embodiments. The results transfer to hardware where demonstrations come from a human hand improving success rate by +20% over action-only policies in 850 rollouts. We show that video and robot data are complementary, and that benefits of learning from video are task-dependent. Website: https://learnsyslab.github.io/multiview_latent_action_pretraining/

</details>

---

### [[20_Research/Papers/具身智能/AWLS_Advantage-Weighted_Latent_Steering_for_One-Step_Generative_Robotic_Manipulation_Policies|AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies]]

![[assets/2610.27736_figure.png|800]]

- **arXiv**: [2610.27736](https://arxiv.org/abs/2610.27736)
- **PDF**: https://arxiv.org/pdf/2610.27736
- **详细分析**: [[20_Research/Papers/具身智能/AWLS_Advantage-Weighted_Latent_Steering_for_One-Step_Generative_Robotic_Manipulation_Policies|AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies]]
- **作者**: Jiahong Tang, Jiaju He, Zhiyuan Yang, Ruyang Han, Haiyue Zhu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《AWLS: Advantage-Weighted Latent Steering for One-Step Generative Robotic Manipulation Policies》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-collected real-world robotic manipulation demonstrations often contain mixed-quality trajectories, including hesitant, indirect, or inefficient action segments. While diffusion- and flow-based policies can model such multimodal data, standard behavior cloning (BC) assigns equal likelihood to all demonstrated actions and may therefore reproduce suboptimal modes. Offline RL value estimates offer a natural signal for biasing policies toward higher-value behavioral modes, but directly fine-tuning the generative policy or using critic gradients for policy steering can amplify critic errors and induce prior drift. We propose Advantage-Weighted Latent Steering (AWLS), an offline post-training method for improving frozen one-step generative manipulation policies without updating their decoders. AWLS learns a residual noise shaper, an observation-conditioned residual correction to the policy's latent noise, and trains it with an advantage-weighted action reconstruction objective. The advantages are detached, scale-normalized, and used only as supervised weights on demonstrated actions, avoiding critic-gradient policy updates while preserving fast single-step inference. We further introduce a rollout-free decoder-sensitivity criterion for selecting pretrained checkpoints that remain responsive to latent-noise perturbations. Experiments on simulated and real-world robotic manipulation tasks with clean and mixed-quality demonstrations show that AWLS improves over the frozen base policy while limiting drift from the pretrained behavior prior. Project page: https://awls-corl2026.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Adaptive_Traversal_Tubes_for_Posture-Aware_Navigation_of_Bipedal_Humanoids|Adaptive Traversal Tubes for Posture-Aware Navigation of Bipedal Humanoids]]

![[assets/2610.27688_figure.png|800]]

- **arXiv**: [2610.27688](https://arxiv.org/abs/2610.27688)
- **PDF**: https://arxiv.org/pdf/2610.27688
- **详细分析**: [[20_Research/Papers/具身智能/Adaptive_Traversal_Tubes_for_Posture-Aware_Navigation_of_Bipedal_Humanoids|Adaptive Traversal Tubes for Posture-Aware Navigation of Bipedal Humanoids]]
- **作者**: Zijian Ge
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Adaptive Traversal Tubes for Posture-Aware Navigation of Bipedal Humanoids》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bipedal humanoids can change their effective footprint by adjusting body yaw, enabling both narrow-passage traversal and socially aware yielding. This paper presents a posture-aware navigation framework centered on \emph{Adaptive Traversal Tubes} (ATT), \emph{Interval Velocity--Heading} (IVH) control, and a sidestep-enhanced AMP locomotion prior. ATT represents a behavior-feasible corridor width field along a reference path, unifying geometric clearance and social comfort into a continuous signal. IVH maps this width to a continuous frontal-to-sidestep posture schedule and omnidirectional velocity commands. A velocity-conditioned AMP policy, trained with GVHMR-retargeted frontal/sidestep motions and coupled \((v_x,v_y)\) tracking rewards, is designed to improve transition stability over a generic locomotion controller while remaining interchangeable with the default onboard policy. This preprint presents the full method; a planned evaluation protocol on a Unitree G1 is outlined, with quantitative results to follow. Demo videos of MuJoCo simulation and real-robot deployment are available at: github.com/lborogzj997/Humanoid-Navigation-in-Crowds-and-Narrow-Spaces.

</details>

---

### [[20_Research/Papers/具身智能/JARVIS_From_Visual_Manuals_to_Autonomous_Robotic_Assembly|JARVIS: From Visual Manuals to Autonomous Robotic Assembly]]

![[assets/2610.27618_figure.png|800]]

- **arXiv**: [2610.27618](https://arxiv.org/abs/2610.27618)
- **PDF**: https://arxiv.org/pdf/2610.27618
- **详细分析**: [[20_Research/Papers/具身智能/JARVIS_From_Visual_Manuals_to_Autonomous_Robotic_Assembly|JARVIS: From Visual Manuals to Autonomous Robotic Assembly]]
- **作者**: Fan Ding, Fucai Ke, Kevin Yuchen Ma, Xuewen Luo, Wenyu Liang, Vishnu Monn Baskaran, Hamid Rezatofighi, Yan Wu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《JARVIS: From Visual Manuals to Autonomous Robotic Assembly》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AssemblyBench, MEPNet, ManualVLA, Training-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual manuals communicate procedural knowledge through stepwise diagrams, but translating these instructions into reliable long-horizon robotic execution remains challenging. We introduce JARVIS, a method-agnostic benchmark for autonomous visual-manual-guided execution without additional language instructions. JARVIS comprises 236,679 LEGO assembly tasks across 8,987 scenes, with a carefully curated JARVIS-v1 suite of 50 tasks for interactive robotic evaluation. Tasks span varying initial structural complexities and assembly horizons, requiring agents to interpret manuals, ground actions in an evolving workspace, and execute the intended procedure. A structure-aware evaluation protocol captures geometric accuracy, structural relations, construction order, partial progress, and completion. We further introduce JARVIS-agentic, a tool-grounded embodied agent that composes robot primitives into executable programs and uses execution feedback for verification and recovery, without task-specific action trajectories or model parameter updates. Across nine multimodal and reasoning models, task-oriented primitives increase the average assembly score. Performance nevertheless declines sharply with assembly horizon, and execution errors remain difficult to correct. Prior-task experience improves initial performance, while repeated reflection provides inconsistent benefits, highlighting persistent limitations in connecting visual procedural reasoning with reliable physical execution.

</details>

---

### [[20_Research/Papers/具身智能/EchoNav_Evidential_BEV_Completion_from_Historical_Observations_for_Visual_Navigation|EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation]]

![[assets/2610.27616_figure.png|800]]

- **arXiv**: [2610.27616](https://arxiv.org/abs/2610.27616)
- **PDF**: https://arxiv.org/pdf/2610.27616
- **详细分析**: [[20_Research/Papers/具身智能/EchoNav_Evidential_BEV_Completion_from_Historical_Observations_for_Visual_Navigation|EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation]]
- **作者**: Diwen Liu, Yiyang Shao, Borui Wang, Chi Zhang, Yunhui Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega features and combines historical residual proposals using cellwise weights and a learned no-update option. The BEV predictor produces a local map in the latest ego frame without depth or camera-pose inputs or explicit geometric warping. The evidential model treats observed free space separately and predicts occupancy with associated confidence across the remaining supported region. We train the predictor on simulated RGB sequences paired with complete and visibility-masked occupancy annotations. Our experiments evaluate navigation in simulation and on a wheeled robot, with additional demonstrations on quadruped and humanoid robots. In simulated sequential two-goal navigation, our system achieves 89.6% success, outperforming the strongest evaluated baseline by 32.5 percentage points. Across 60 wheeled-robot trials in 20 scenes, it achieves 73.3% success, compared with 33.3% for the strongest evaluated baseline.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Task_Agents_Can_Perform_Fine_Manipulation_through_Tactile_In-Context_Learning|Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning]]

![[assets/2610.27613_figure.png|800]]

- **arXiv**: [2610.27613](https://arxiv.org/abs/2610.27613)
- **PDF**: https://arxiv.org/pdf/2610.27613
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Task_Agents_Can_Perform_Fine_Manipulation_through_Tactile_In-Context_Learning|Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning]]
- **作者**: Yubang Wang, Zezheng Huai, Yifei Zhang, Jinhao Wu, Yitong Chen, Haozhe Zhang, Sixian Li, Jingjing Gong, Zhenyang Lin, Ziyang Chen, Xipeng Qiu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can embodied task agents use tactile experience to perform fine manipulation without task-specific model training? We investigate this capability through Tactile-ETA, a system that incorporates tactile experience into an embodied task agent through in-context learning. Successful expert demonstrations show how contact changes during manipulation. We pair each recorded robot movement with its camera views and bilateral tactile observations. We keep tactile observations at the start and end of each movement and add two neighboring time points when the tactile images change markedly in between. The agent combines these demonstrations with current vision, tactile observations, and proprioception to select actions through general-purpose robot tools, without updating model parameters. Across four simulated manipulation tasks, adding tactile observations to the same two expert demonstrations increases average success from 15.75% to 24.00%, with current sensing and execution interfaces held fixed. Further experiments show that performance depends on the sensory content and representation of demonstrations, while comparing agent models on Lift Bottle reveals substantial differences under the same system configuration. On the real-robot tasks, demonstrations with aligned visual and tactile observations increase the task success rate from 0% to 60%. These findings demonstrate the feasibility of using tactile experience in context for fine manipulation and suggest a path toward extending embodied task agents to additional sensory inputs.

</details>

---

### [[20_Research/Papers/大模型/Robot-Task_Suitability_in_Heterogeneous_Multi-Robot_Task_Allocation|Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation]]

![[assets/2610.27504_figure.png|800]]

- **arXiv**: [2610.27504](https://arxiv.org/abs/2610.27504)
- **PDF**: https://arxiv.org/pdf/2610.27504
- **详细分析**: [[20_Research/Papers/大模型/Robot-Task_Suitability_in_Heterogeneous_Multi-Robot_Task_Allocation|Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation]]
- **作者**: Daniel Weiner, Raj Korpan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, Systems

#### 研究背景与动机

《Robot-Task Suitability in Heterogeneous Multi-Robot Task Allocation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Heterogeneous multi-robot task allocation depends on estimates of how suitable individual robots are for candidate tasks, yet suitability can be defined in substantially different ways. We compare ten deterministic methods and two LLM-based variants spanning rule-based, similarity-based, requirement-oriented, fuzzy, and semantic approaches. Using common robot and task profiles, we compare how the methods score and rank candidate robots, identify feasibility, and select a top robot, while examining how these outcomes change with team composition, scale, spatial context, capability uncertainty, and task representation. The methods frequently disagree despite operating on identical scenarios. Generic similarity measures can violate properties expected under a one-sided requirement-satisfaction interpretation of suitability, while LLM-based scoring introduces additional stochastic and linguistic sensitivity. These results show that robot--task suitability should be treated as an explicit modeling choice whose assumptions, robustness, and decision-level consequences should be considered before allocation.

</details>

---

### [[20_Research/Papers/具身智能/HATCH_Hardware-Attested_Task_Chains_for_Verifiable_Manipulation|HATCH: Hardware-Attested Task Chains for Verifiable Manipulation]]

![[assets/2610.27485_first_page.png|800]]

- **arXiv**: [2610.27485](https://arxiv.org/abs/2610.27485)
- **PDF**: https://arxiv.org/pdf/2610.27485
- **详细分析**: [[20_Research/Papers/具身智能/HATCH_Hardware-Attested_Task_Chains_for_Verifiable_Manipulation|HATCH: Hardware-Attested Task Chains for Verifiable Manipulation]]
- **作者**: Shiza Charania
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《HATCH: Hardware-Attested Task Chains for Verifiable Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoRL, ImageNet, RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Capability claims in robot manipulation are unverifiable, and existing leaderboards are each closed, simulated, or gameable. We propose HATCH, a robot escape room: an openly specified, physically replicable, sensor-scored, and unrehearsable benchmark. Tasks span five skill categories at three difficulty levels and are chained so that the sensor confirming one task's completion unlocks the next, turning a room into a single long-horizon evaluation. Success is confirmed by instrumentation rather than human judgment, scoring is embodiment-agnostic, and object placements are randomized by a run-day seed. Entrants submit attested self-runs (uncut video, sensor logs, and the seed), with occasional organized events for calibration. Task specifications, build guide, bill of materials, and scoring rubrics are released under an open license.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Autonomous_Bricklaying_Using_Boston_Dynamics_Spot|Towards Autonomous Bricklaying Using Boston Dynamics Spot]]

![[assets/2610.27472_figure.png|800]]

- **arXiv**: [2610.27472](https://arxiv.org/abs/2610.27472)
- **PDF**: https://arxiv.org/pdf/2610.27472
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Autonomous_Bricklaying_Using_Boston_Dynamics_Spot|Towards Autonomous Bricklaying Using Boston Dynamics Spot]]
- **作者**: Karl-Johan Sorensen, Nico vom Hofe, Frank H. P. Fitzek
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Towards Autonomous Bricklaying Using Boston Dynamics Spot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile legged robots offer unique advantages for on-site construction, including the ability to traverse unstructured terrain, climb stairs, and operate independently between spatially separated work zones. This paper presents a proof-of-concept system for autonomous brick stacking using a Boston Dynamics Spot quadrupedal robot equipped with a manipulator arm. The system operates between a supply area and an assembly area, using AprilTag fiducials for localization and autowalk missions for navigation. Target brick positions and orientations are specified in CAD software and exported directly for robotic execution. We evaluate placement accuracy through ten repeated assemblies of a curved four-layer wall comprising 14 wooden bricks. Results show mean translation errors below 10 mm and mean yaw errors below 1.5 degrees, while the overall RMSE across all runs is 27.72 mm (translation) and 2.06 degrees (rotation). The system was also tested outdoors with stairs between the two areas. The workflow is modular and easily extendable to different wall geometries.

</details>

---

### [[20_Research/Papers/机器人/Determination_of_the_Human-Robot_Interaction_Workspace_for_Robot_Assisted_Head_Stabilization_Control|Determination of the Human-Robot Interaction Workspace for Robot Assisted Head Stabilization Control]]

![[assets/2610.27336_figure.png|800]]

- **arXiv**: [2610.27336](https://arxiv.org/abs/2610.27336)
- **PDF**: https://arxiv.org/pdf/2610.27336
- **详细分析**: [[20_Research/Papers/机器人/Determination_of_the_Human-Robot_Interaction_Workspace_for_Robot_Assisted_Head_Stabilization_Control|Determination of the Human-Robot Interaction Workspace for Robot Assisted Head Stabilization Control]]
- **作者**: Xinmin Liu, Alexander L. Van Slyke, Destinee Holloman, Ahmad Sakaamini, Rodney D. Wiersma
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Determination of the Human-Robot Interaction Workspace for Robot Assisted Head Stabilization Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate head immobilization is critical for medical procedures such as neuroimaging and intracranial radiation therapy, where even minor motion can compromise precision. Traditional methods, such as rigid stereotactic frames and thermoplastic face masks, are invasive, uncomfortable for patients, and require a time-consuming setup. To overcome these limitations, a novel approach employs a 6-degree-of-freedom (6DoF) robotic head holder that is integrated with real-time optical motion tracking, enabling dynamic compensation for head movements without physical restraint. However, implementing this system requires a detailed biomechanical understanding of skull-cervical spine interactions to define safe and effective motion limits. In this study, we conduct a human volunteer investigation using a 6DoF Stewart platform robot to characterize biokinematic workspace of the head-neck system and establish foundational data for human-robot interaction in precision head stabilization.

</details>

---

### [[20_Research/Papers/具身智能/Design_and_Control_of_a_Multimodal_Legged-Aerial_Robot_Through_Separate_Control_Contraction_Metrics|Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics]]

![[assets/2610.27315_figure.png|800]]

- **arXiv**: [2610.27315](https://arxiv.org/abs/2610.27315)
- **PDF**: https://arxiv.org/pdf/2610.27315
- **详细分析**: [[20_Research/Papers/具身智能/Design_and_Control_of_a_Multimodal_Legged-Aerial_Robot_Through_Separate_Control_Contraction_Metrics|Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics]]
- **作者**: Kaushik Venkatesh Krishnamurthy, Eric Sihite, Alireza Ramezani, Morteza Gharib
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.6，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Design and Control of a Multimodal Legged-Aerial Robot Through Separate Control Contraction Metrics》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of dynamic legged locomotion and aerial mobility offers versatility that is deterred by challenges in payload distribution, actuation, and the contrasting requirements of both domains. In this paper, we present the design and operation of a multimodal quadrupedal aerial-legged robot. The presence of legged aerial systems also allows for thruster-assisted legged locomotion, which we make possible with a unified control framework using Control Contraction Metrics (CCM). We search for separate domain-specific contraction metrics for walking and flight independently offline and unify them using an online energy-based Control Lyapunov Function Quadratic Program (CLF QP). This enables optimal, cross-domain control allocation, which we show using simulations. We also show experimental results that validate the mechanical viability of our hardware and the paradigm of thruster-assisted trotting. The stability of said experiments motivates the deployment of the control framework for multimodal operations.

</details>

---

### [[20_Research/Papers/强化学习/EmbodyHOI_Embodiment-Aware_Generation_of_Hand-Object_Interactions_for_Humanoid_Dexterous_Manipulation|EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation]]

![[assets/2610.27242_figure.png|800]]

- **arXiv**: [2610.27242](https://arxiv.org/abs/2610.27242)
- **PDF**: https://arxiv.org/pdf/2610.27242
- **详细分析**: [[20_Research/Papers/强化学习/EmbodyHOI_Embodiment-Aware_Generation_of_Hand-Object_Interactions_for_Humanoid_Dexterous_Manipulation|EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation]]
- **作者**: Chaitanya Chawla, Kartik Sharma, Ananya Bal, Laszlo A. Jeni, Guanya Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid dexterous manipulation needs reference motions that are both semantically rich and kinematically feasible for the target robot. Text-conditioned hand-object interaction (HOI) generators supply diverse, language-specified demonstrations, but they synthesize motion in human (MANO) space. The embodiment gap is therefore deferred to post-hoc retargeting, where trajectories deployed on the robot can fail to maintain contact with objects and also degrade policy learning. Our key idea is that robot reachability should constrain the interaction trajectories while they are being generated. We present EmbodyHOI, which runs a differentiable inverse-kinematics (IK) solver for a specific humanoid embodiment inside the sampling loop of a frozen flow-matching HOI trajectory generator. We feed back gradients from the embodiment-aware IK solver into the HOI sampler and jointly optimize the position of the humanoid with respect to the object. Because guidance acts only at inference, one HOI trajectory generator trained on human hand poses transfers across humanoid embodiments without retraining. On ARCTIC trajectories with two contrasting humanoids (Unitree G1 and H1-2), our proposed guidance-based method cuts the retargeted wrist error from 8.9 cm to 0.6 cm while leaving text-to-HOI generation quality intact, and raises task success from 68% to 79% on 50 random G1 tasks and from 62% to 76% on a four-task H1-2 suite. Critically, cheaper alternatives for bridging the embodiment gap fail to beat EmbodyHOI. Post-hoc wrist refinement and compute-matched best-of-N selection both reach lower IK energy than our guidance yet train worse policies. For simulation results, see our website: https://embodyhoi.github.io/

</details>

---

### [[20_Research/Papers/机器人/Learning_to_Be_Different_Component_Specialization_for_Compositional_Diffusion_Policies|Learning to Be Different: Component Specialization for Compositional Diffusion Policies]]

![[assets/2610.27194_figure.png|800]]

- **arXiv**: [2610.27194](https://arxiv.org/abs/2610.27194)
- **PDF**: https://arxiv.org/pdf/2610.27194
- **详细分析**: [[20_Research/Papers/机器人/Learning_to_Be_Different_Component_Specialization_for_Compositional_Diffusion_Policies|Learning to Be Different: Component Specialization for Compositional Diffusion Policies]]
- **作者**: Alec Laprevotte, Haonan Chen, Xiaoshen Han, Yilun Du
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Learning to Be Different: Component Specialization for Compositional Diffusion Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies with linearly composed scores have emerged as a promising approach to multitask robotic learning by combining separate factors to enable modular, task-wise adaptation, compositional generalization, and interpretable functional decomposition. However, current training objectives do not encourage factor specialization, often resulting in uninterpretable denoisers whose composed prediction is an average over identical copies, undermining their architectural premise. To address this, we propose a drop-in score-decorrelation auxiliary loss, motivated by projective composition theory. Our approach encourages specialization by penalizing overlap directly between component noise predictions, with little architectural change or computational overhead. We demonstrate across multiple benchmarks that our decorrelation loss consistently reduces measurable double-counting between components, improves task decomposition, and produces behaviorally meaningful specialization without compromising multitask performance. Website: https://al3cl1.github.io/robotics-score-decorrelation.

</details>

---

### [[20_Research/Papers/具身智能/ACE-Brain-0.6_Scaling_Spatial_Grounding_for_Physical_Foundation_Models|ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models]]

![[assets/2610.27040_figure.png|800]]

- **arXiv**: [2610.27040](https://arxiv.org/abs/2610.27040)
- **PDF**: https://arxiv.org/pdf/2610.27040
- **详细分析**: [[20_Research/Papers/具身智能/ACE-Brain-0.6_Scaling_Spatial_Grounding_for_Physical_Foundation_Models|ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models]]
- **作者**: Yinhe Wang, Tao Tao, Zexin He, Shuang Luo, Wei Mao, Yao Mu, Feng Pan, Hanming Deng, Lewei Lu, Zhi Hou, Xingang Pan, Dahua Lin...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate scaling visual grounding to strengthen the perceptual foundation of general embodied operation. We develop a unified data pipeline that combines robot manipulation recordings with complementary visual data from diverse sources. After automatically annotating the robot recordings, the pipeline converts the collected data into verifiable grounding supervision. Fine-tuning Qwen3.5-9B on approximately 1.5 million samples produced by this pipeline yields ACE-Brain-0.6. The model outperforms GPT-6 Astra on four of seven public grounding benchmarks, with an overall average score of 75.41 compared with Astra's 73.68. Under a fixed Qwen3.5-9B fine-tuning setup, aggregate grounding performance improves steadily as successive data releases expand the training collection to cover a broader range of grounding scenarios. These results show that scaling verifiable grounding supervision from diverse sources can strengthen the spatial perception of an open 9B model for general embodied operation.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Playground_A_Long-Horizon_Agentic_Robotics_Benchmark_for_Physical,_Strategic,_and_Spatial_Reasoning|Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning]]

![[assets/2610.27039_figure.png|800]]

- **arXiv**: [2610.27039](https://arxiv.org/abs/2610.27039)
- **PDF**: https://arxiv.org/pdf/2610.27039
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Playground_A_Long-Horizon_Agentic_Robotics_Benchmark_for_Physical,_Strategic,_and_Spatial_Reasoning|Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning]]
- **作者**: Feng Chen, Pei Zhou, Lixuan He, Yunchao Yao, Li Sun, Shenghua Gao, Mingyu Ding, Kaifeng Zhang, Kaichen Zhou, Yi Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.5，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CodeActionBench, EmbodiedBench, EmbodiedEval, LoTa-Bench, Meta-World, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models offer a promising basis for robotic agents, but long-horizon tasks require them to sustain coherent reasoning and reliable physical execution across interdependent stages. We introduce Embodied Playground, a benchmark for evaluating how foundation-model agents coordinate physical, strategic, and spatial reasoning throughout such tasks. Agents must track task progress, satisfy intermediate constraints, and revise their plans using execution feedback as earlier actions shape subsequent decisions. The playground comprises 410 task environments spanning basic manipulation, sequential puzzles, and multi-stage household activities, with variations in planning depth, geometric constraints, and physical execution demands. We curate EP-100, a representative selection of 100 tasks across five suites and 16 task types, together with the EP-Easy and EP-Hard difficulty splits and the compact EP-20 selection. A shared protocol specifies observation and tool access, resource budgets, repeated trials, and independent checks of goal completion, task-rule compliance, and physical validity. Embodied Playground provides a unified framework for studying whether foundation-model agents can sustain effective reasoning and action over extended task horizons. https://winniechen2002.github.io/Agent-bench-website/

</details>

---

### [[20_Research/Papers/具身智能/Replan_for_Error_Recovery_Training_Embodied_VLMs_through_Verifiable_Interaction_with_Action-Grouped_Turn-GSPO|Replan for Error Recovery: Training Embodied VLMs through Verifiable Interaction with Action-Grouped Turn-GSPO]]

![[assets/2610.27003_figure.png|800]]

- **arXiv**: [2610.27003](https://arxiv.org/abs/2610.27003)
- **PDF**: https://arxiv.org/pdf/2610.27003
- **详细分析**: [[20_Research/Papers/具身智能/Replan_for_Error_Recovery_Training_Embodied_VLMs_through_Verifiable_Interaction_with_Action-Grouped_Turn-GSPO|Replan for Error Recovery: Training Embodied VLMs through Verifiable Interaction with Action-Grouped Turn-GSPO]]
- **作者**: Zhuoran Wang, Keqing Fan, Yang Li, Jinbo Su, Ke Wang, Sijia Luo, Yuanzheng Tan, Junken Peng, Jing Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Replan for Error Recovery: Training Embodied VLMs through Verifiable Interaction with Action-Grouped Turn-GSPO》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ERR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied VLMs can execute increasingly complex manipulation tasks, yet execution errors can leave the environment in states that require replanning for recovery. Existing recovery methods either rely on inference-time mechanisms with fixed policies or learn from failure examples and reference corrections rather than verified action outcomes. To enable recovery learning through verifiable interaction, we introduce the Embodied Replanning for Recovery Environment (ERR-Env), which provides feedback on task progress and execution errors. We further construct ERR-Bench, a benchmark with held-out tasks spanning nominal, intermediate, and error states for evaluating recovery capability and execution reliability. We then propose Action-Grouped Turn-GSPO (AGT-GSPO), an online reinforcement learning method combining turn-level rewards for task progress and error states with action-grouped advantage estimation, and use it to train ERR-VLM, a compact 2B embodied VLM. Evaluation on ERR-Bench reveals a mismatch between task progress and execution reliability across diverse VLMs. AGT-GSPO improves ERR-VLM by 10.25 percentage points in Strict Success Rate for error-free completion and 22.95 percentage points in Recovery Rate, while ablations and zero-shot transfer further validate the effectiveness of our method.

</details>

---

### [[20_Research/Papers/具身智能/DexGraspFlow_Topology-Aware_SE(3)_Flow_Matching_for_Cross-Embodiment_Dexterous_Grasp_Generation|DexGraspFlow: Topology-Aware SE(3) Flow Matching for Cross-Embodiment Dexterous Grasp Generation]]

![[assets/2610.26962_figure.png|800]]

- **arXiv**: [2610.26962](https://arxiv.org/abs/2610.26962)
- **PDF**: https://arxiv.org/pdf/2610.26962
- **详细分析**: [[20_Research/Papers/具身智能/DexGraspFlow_Topology-Aware_SE(3)_Flow_Matching_for_Cross-Embodiment_Dexterous_Grasp_Generation|DexGraspFlow: Topology-Aware SE(3) Flow Matching for Cross-Embodiment Dexterous Grasp Generation]]
- **作者**: Bin Zhou, Boyu Ma, Xinyu Zhou, Jiahua Dong, Chuhao Zhou, Yizhou Liu, Hao Wan, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DexGraspFlow: Topology-Aware SE(3) Flow Matching for Cross-Embodiment Dexterous Grasp Generation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DexGraspNet, FFHNet, GraspGraphNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Differences in hand geometry, joint parameterization, and kinematic topology pose challenges for cross-embodiment dexterous grasp generation. However, spatial relations among links alone are insufficient to fully capture the hand's kinematic topology. We propose DexGraspFlow, a conditional link-level $\mathrm{SE}(3)$ flow-matching framework integrating geometric relations and kinematic topology. The framework encodes local object geometry, link geometry, and current poses. A dual-stream DiT models link--link coordination and link--object interaction, while attention biases derived from kinematic-tree distances provide explicit structural information for modeling evolving geometric interactions. The model jointly learns translational and rotational velocity fields, integrates them to generate link poses, and recovers joint configurations through inverse kinematics. Additionally, inference-time palm-orientation guidance enables controllable grasp generation without retraining. Across three robotic hands and 30 object--hand pairs, DexGraspFlow achieves a 95.33\% average simulation success rate, with an average generation latency, including inverse kinematics, approximately 49\% lower than that of a state-of-the-art baseline. Further experiments demonstrate zero-shot adaptability to seven finger-removal variants and palm-orientation control. A model trained on demonstrations for the deployed hand achieves a 91\% success rate over 100 real-robot grasping trials, supporting the framework's applicability to physical grasp execution.

</details>

---
