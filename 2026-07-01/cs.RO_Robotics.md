# cs.RO | Robotics | 2026-07-01

#arxiv #ComputerScience

**论文数**: 31

### [[20_Research/Papers/具身智能/DVG-WM_Disentangled_Video_Generation_Enables_Efficient_Embodied_World_Model_for_Robotic_Manipulation|DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation]]

![[assets/2606.32028_figure.png|800]]

- **arXiv**: [2606.32028](https://arxiv.org/abs/2606.32028)
- **PDF**: https://arxiv.org/pdf/2606.32028
- **详细分析**: [[20_Research/Papers/具身智能/DVG-WM_Disentangled_Video_Generation_Enables_Efficient_Embodied_World_Model_for_Robotic_Manipulation|DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation]]
- **作者**: Ziyu Shan, Zhenyu Wu, Xiaofeng Wang, Zheng Zhu, Ziwei Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 4.8（加权：具身智能 2.7，世界模型 1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KeyWorld, Real-World, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos. Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled video generation can be an efficient embodied world model for robotic manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Human-as-Humanoid_Enabling_Zero-Shot_Humanoid_Learning_from_Ego-Exo_Human_Videos_with_Human-Aligned_Embodiments|Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments]]

![[assets/2606.32009_figure.png|800]]

- **arXiv**: [2606.32009](https://arxiv.org/abs/2606.32009)
- **PDF**: https://arxiv.org/pdf/2606.32009
- **详细分析**: [[20_Research/Papers/具身智能/Human-as-Humanoid_Enabling_Zero-Shot_Humanoid_Learning_from_Ego-Exo_Human_Videos_with_Human-Aligned_Embodiments|Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments]]
- **作者**: Xiaopeng Lin, Ruoqi Yang, Shijie Lian, Zhaolong Shen, Bin Yu, Changti Wu, Haibao Liu, Yuxiang Zhang, Hong Li, Qiyuan Su, Haochen Liu, Xuguo He...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Bridgedatav2_2023_CoRL, EgoVLA, OpenVLA, OpenVLA_2024_CoRL, RT2_2023_CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models across robot embodiments require high-quality observation--action supervision to learn deployable action distributions, yet scaling such robot data remains difficult, especially for high-DoF humanoids. Teleoperation provides controller-aligned supervision, while human egocentric videos capture diverse bimanual manipulation but do not directly provide executable robot actions. We introduce Human-as-Humanoid, a human-to-humanoid supervision framework that enables near-real-time human-centric action generation, making human demonstrations usable for high-DoF humanoid VLA training by jointly aligning the robot embodiment, the sensing setup, and the action-label interface. Built on PrimeU, a human-aligned 60-DoF upper-body humanoid, Human-as-Humanoid uses synchronized ego-exo videos to pair deployment-aligned egocentric observations with exocentric motion recovery, retargets the recovered human motion through staged Inverse Kinematics (IK) into controller-aligned 60-DoF action chunks, and trains the VLA model with Forward Kinematics (FK)-aware supervision to preserve wrist and fingertip task-space geometry. This converts large-scale human demonstrations from visual observations into executable observation--action supervision for the target humanoid. Experiments validate the conversion chain at the motion-recovery, robot-action-space, and real-robot deployment levels. Human-as-Humanoid yields a 4.8--7.2x raw demonstration-throughput gain over humanoid teleoperation in our data-collection analysis, and on several downstream tasks, policies post-trained only with the converted human labels generalize to real-robot deployment without target-task robot demonstrations. The official project website is available at https://zgc-embodyai.github.io/Human-as-Humanoid.

</details>

---

### [[20_Research/Papers/具身智能/OopsieVerse_A_Safety_Benchmark_with_Damage-Aware_Simulation_for_Robot_Manipulation|OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation]]

![[assets/2606.31993_figure.png|800]]

- **arXiv**: [2606.31993](https://arxiv.org/abs/2606.31993)
- **PDF**: https://arxiv.org/pdf/2606.31993
- **详细分析**: [[20_Research/Papers/具身智能/OopsieVerse_A_Safety_Benchmark_with_Damage-Aware_Simulation_for_Robot_Manipulation|OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation]]
- **作者**: Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, Roberto Martín-Martín
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.6（加权：具身智能 2.1，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DSRL, DamageSim, OopsieBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

</details>

---

### [[20_Research/Papers/具身智能/Adapting_Generalist_Robot_Policies_with_Semantic_Reinforcement_Learning|Adapting Generalist Robot Policies with Semantic Reinforcement Learning]]

![[assets/2606.31958_figure.png|800]]

- **arXiv**: [2606.31958](https://arxiv.org/abs/2606.31958)
- **PDF**: https://arxiv.org/pdf/2606.31958
- **详细分析**: [[20_Research/Papers/具身智能/Adapting_Generalist_Robot_Policies_with_Semantic_Reinforcement_Learning|Adapting Generalist Robot Policies with Semantic Reinforcement Learning]]
- **作者**: Jagdeep Singh Bhatia, Andrew Wagenmaker, William Chen, Sergey Levine
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Adapting Generalist Robot Policies with Semantic Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies learn a diverse repertoire of behaviors from large-scale pretraining. In principle, this makes them excellent priors for downstream adaptation via reinforcement learning (RL). In practice, however, standard RL methods leveraging this prior optimize directly over robot actions, requiring the base policy's action distribution to be close to that of a performant policy from the start. This assumption breaks down for complex or long-horizon tasks that fall outside the pretraining distribution. Our key insight is that, for sufficiently expressive generalist policies, language prompts are an effective alternative space for learning to solve such tasks: modulating language inputs elicits skills already within the policy's repertoire, which can be composed to solve tasks beyond its zero-shot capabilities. We propose Semantic Action Reinforcement Learning (SARL), which learns to optimize this prompt space through online interaction, treating the generalist policy as a controllable skill prior. Importantly, leveraging pretrained skills rather than learning new ones from scratch yields structured, semantically meaningful exploration and highly efficient online improvement, and learning to modulate prompts through experience grounds them in induced real-world behaviors for robust task-solving. Across real-world settings and simulated benchmarks, we show SARL unlocks fundamentally new capabilities -- adapting VLA behavior to solve complex, long-horizon tasks -- and significantly outperforms existing approaches for improving robot behavior in deployment.

</details>

---

### [[20_Research/Papers/机器人/RRT-Rope_A_deterministic_shortening_approach_for_fast_near-optimal_path_planning_in_large-scale_uncluttered_3D_environments|RRT-Rope: A deterministic shortening approach for fast near-optimal path planning in large-scale uncluttered 3D environments]]

![[assets/2606.31948_first_page.png|800]]

- **arXiv**: [2606.31948](https://arxiv.org/abs/2606.31948)
- **PDF**: https://arxiv.org/pdf/2606.31948
- **详细分析**: [[20_Research/Papers/机器人/RRT-Rope_A_deterministic_shortening_approach_for_fast_near-optimal_path_planning_in_large-scale_uncluttered_3D_environments|RRT-Rope: A deterministic shortening approach for fast near-optimal path planning in large-scale uncluttered 3D environments]]
- **作者**: Louis Petit, Alexis Lussier Desbiens
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《RRT-Rope: A deterministic shortening approach for fast near-optimal path planning in large-scale uncluttered 3D environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many path planning algorithms have been introduced so far, but most are costly, in path cost and in processing time, in large-scale uncluttered 3D environments such as underground mining stopes explored by an unmanned aerial vehicle (UAV). Rapidly-exploring Random Tree (RRT) algorithms are popular because of their probabilistic completeness and rapidity in finding a feasible path in single-query problems. Many of the algorithms (e.g. Informed RRT*, RRT#) developed to improve RRT need considerable time to converge in large environments. Shortcutting an RRT is an old idea that has been proven to outperform RRT variants. This paper introduces a new method, RRT-Rope, that aims at finding a near-optimal solution in a drastically shorter amount of time. The proposed approach benefits from fast computation of a feasible path with an altered version of RRT-connect, and post-processes it quickly with a deterministic shortcutting technique, taking advantage of intermediate nodes added to each branch of the tree. This paper presents simulations and statistics carried out to show the efficiency of RRT-Rope, which gives better results in terms of path cost and computation time than other popular RRT variations and shortening techniques in all our simulation environments, and is up to 70% faster than the next best algorithm in a representative stope.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Locomotion_on_Discrete_Terrain_via_Minimal_Proximity_Sensing|Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing]]

![[assets/2606.31912_figure.jpg|800]]

- **arXiv**: [2606.31912](https://arxiv.org/abs/2606.31912)
- **PDF**: https://arxiv.org/pdf/2606.31912
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Locomotion_on_Discrete_Terrain_via_Minimal_Proximity_Sensing|Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing]]
- **作者**: Jiale Fan, Connor Flynn, Tianao Xu, Junzhe He, Andrei Cramariuc, Marco Hutter, Robert Baines
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based control has revolutionized dynamic locomotion, yet navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact" feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home.

</details>

---

### [[20_Research/Papers/强化学习/CoDex_Learning_Compositional_Dexterous_Functional_Manipulation_without_Demonstrations|CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations]]

![[assets/2606.31909_figure.jpg|800]]

- **arXiv**: [2606.31909](https://arxiv.org/abs/2606.31909)
- **PDF**: https://arxiv.org/pdf/2606.31909
- **详细分析**: [[20_Research/Papers/强化学习/CoDex_Learning_Compositional_Dexterous_Functional_Manipulation_without_Demonstrations|CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations]]
- **作者**: Bowen Jiang, William Painter Reger, Roberto Martin-Martin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《CoDex: Learning Compositional Dexterous Functional Manipulation without Demonstrations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we study Compositional Dexterous Functional Object Manipulation (CD-FOM): tasks such as aiming and actuating a spray bottle on a plant or a glue gun on wood, which require both actuating an object's internal mechanism and controlling its pose to apply the object's function to the environment. These tasks pose significant challenges for robots due to the demanding integration of semantic understanding of the object's function, actuation mode, and application area with intricate physical dexterity to manage grasp stability, movement trajectory, and actuation. We introduce CoDex, a zero-demonstration framework that autonomously discovers CD-FOM manipulation strategies. CoDex uses vision-language models (VLMs) to infer semantic constraints from the task and scene. These constraints guide analytic constrained optimization to generate a short list of functional grasp candidates that can be efficiently refined with reinforcement learning to generate full grasp-move-actuate policies transferable from simulation to the real world. We evaluate CoDex on a 7-DoF robot arm with a 16-DoF multi-fingered hand across six CD-FOM tasks involving previously unseen objects with internal mechanisms, including spray bottles, hot glue guns, air dusters, flashlights, and pepper grinders, and their application to unseen target objects, showcasing its ability to autonomously discover and execute complex, physically viable dexterous behaviors without human demonstrations. More information at https://robin-lab.cs.utexas.edu/CoDex/.

</details>

---

### [[20_Research/Papers/机器人/Improving_path-tracking_performance_of_an_articulated_tractor-trailer_system_using_a_non-linear_kinematic_model|Improving path-tracking performance of an articulated tractor-trailer system using a non-linear kinematic model]]

![[assets/2606.31889_figure.jpg|800]]

- **arXiv**: [2606.31889](https://arxiv.org/abs/2606.31889)
- **PDF**: https://arxiv.org/pdf/2606.31889
- **详细分析**: [[20_Research/Papers/机器人/Improving_path-tracking_performance_of_an_articulated_tractor-trailer_system_using_a_non-linear_kinematic_model|Improving path-tracking performance of an articulated tractor-trailer system using a non-linear kinematic model]]
- **作者**: Marina Murillo, Guido Sanchez, Nestor Deniz, Lucas Genzelis, Leonardo Giovanini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Improving path-tracking performance of an articulated tractor-trailer system using a non-linear kinematic model》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a novel non-linear mathematical model of an articulated tractor-trailer system that can be used, in combination with receding horizon techniques, to improve the performance of path tracking tasks of articulated systems. Due to its dual steering mechanisms, this type of vehicle can be very useful in precision agriculture, particularly for seeding, spraying and harvesting in small fields. The articulated tractor-trailer system model was embedded within a non-linear model predictive controller and the trailer position was monitored. When the kinematic of the trailer was considered, the deviation of trailer's position was reduced substantially alongside not only straight paths but also in headland turns. Using the proposed mathematical model, we were able to control the trailer's position itself rather than the tractor's position. The Robot Operating System (ROS) framework and Gazebo simulator were used to perform realistic simulations examples.

</details>

---

### [[20_Research/Papers/具身智能/RoboTacDex_A_Dexterous_Visual-Tactile-Action_Dataset_for_Humanoid_Manipulation|RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation]]

![[assets/2606.31836_first_page.png|800]]

- **arXiv**: [2606.31836](https://arxiv.org/abs/2606.31836)
- **PDF**: https://arxiv.org/pdf/2606.31836
- **详细分析**: [[20_Research/Papers/具身智能/RoboTacDex_A_Dexterous_Visual-Tactile-Action_Dataset_for_Humanoid_Manipulation|RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation]]
- **作者**: Xinyi Wang, Donghan Li, Zi'Ang Chen, Chong Yu, Chen Xin, Peng Ye, Yingkai Sun, Tao Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.5（加权：具身智能 3，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback, and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative imitation learning models on our dataset, analyzing their performance as well as their respective strengths and limitations across different task categories. Successful trial results and a moderate level of generalization capabilities across a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.

</details>

---

### [[20_Research/Papers/具身智能/Reinforcement_Learning-Based_Control_for_an_Inline_Skating_Humanoid_Robot|Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot]]

![[assets/2606.31807_first_page.png|800]]

- **arXiv**: [2606.31807](https://arxiv.org/abs/2606.31807)
- **PDF**: https://arxiv.org/pdf/2606.31807
- **详细分析**: [[20_Research/Papers/具身智能/Reinforcement_Learning-Based_Control_for_an_Inline_Skating_Humanoid_Robot|Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot]]
- **作者**: Ethan Marot, Thomas Bi, Clemens Schwarke, Victor Klemm, Marco Hutter, Raffaello D'Andrea
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 4.5（加权：具身智能 1.8，强化学习 0.8，机器人 1.9）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Reinforcement Learning-Based Control for an Inline Skating Humanoid Robot》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As humanoid robots become increasingly dynamic, coupling them with reinforcement learning offers a promising approach to solving the complex, underactuated mechanics of passive inline skating. Equipping a humanoid robot with passive inline skating wheels presents an opportunity to combine the versatile agility of humanoids with the high-speed, energy-efficient locomotion strategies utilized by human skaters. In this paper, we train and deploy a reinforcement learning control policy that enables novel locomotion strategies for a humanoid robot modified to equip consumer inline skates instead of conventional feet. Unlike previous work limited to quadrupedal robots or actively driven wheels, our system allows for precise 6-DoF control of the skates to execute dynamic, edge-driven propulsion strategies. Our skating strategies emerge entirely from our reward structure, without reliance on human motion data, imitation learning, or kinematic priors. We overcome the inherent instability of passive wheels and simulation contact artifacts by utilizing different geometric wheel models (spherical and ellipsoidal) during training and validation, along with a custom success-based command curriculum and a specialized rolling reward. Consequently, our policy demonstrates up to a 50% reduction in Cost of Transport (CoT) compared to standard walking gaits. The resulting policy successfully transfers zero-shot to the physical Booster T1 hardware. Real-world deployments demonstrate dynamic balance, the ability to reject active physical perturbations, and agile locomotion strategies capable of turning at speed. A video of our results can be found at https://www.youtube.com/watch?v=-_APcOS7uFo.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_UAV_Navigation_for_Individual_Wildlife_Re-Identification|Autonomous UAV Navigation for Individual Wildlife Re-Identification]]

![[assets/2606.31772_figure.png|800]]

- **arXiv**: [2606.31772](https://arxiv.org/abs/2606.31772)
- **PDF**: https://arxiv.org/pdf/2606.31772
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_UAV_Navigation_for_Individual_Wildlife_Re-Identification|Autonomous UAV Navigation for Individual Wildlife Re-Identification]]
- **作者**: Claire Sun, Tanya Berger-Wolf, Jenna Kline
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: EmbodiedAI, RL, ComputerVision

#### 研究背景与动机

《Autonomous UAV Navigation for Individual Wildlife Re-Identification》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable individual re-identification (re-ID) of wildlife is essential for population monitoring, behavioral tracking, and conservation policy evaluation, yet large-scale data collection remains labor-intensive, relying on manual efforts by ecologists or citizen scientists. We propose an autonomous drone navigation system that actively optimizes image capture for downstream re-ID, moving beyond passive aerial sensing. The system combines YOLOv11 object detection with a DINOv2-based pose classifier to guide real-time flight decisions: detecting animals, orienting to expose the lateral flank (the surface of interest for pattern-based re-ID), and approaching until the subject meets a minimum bounding-box threshold. Unlike prior drone systems that optimize for group-level behavioral video, ours targets the specific image-quality requirements of individual-identification models. We demonstrate feasibility through a case study on zebra using footage collected in Kenya, and show the approach generalizes to other species with diagnostic surface patterns, including giraffes, tigers, and elephants. Our work establishes a framework for task-aware embodied AI for ecological data collection, in which downstream re-ID requirements drive real-time perception and control.

</details>

---

### [[20_Research/Papers/具身智能/UniTacVLA_Unified_Tactile_Understanding_and_Prediction_in_Vision_Language_Action_Models|UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models]]

![[assets/2606.31723_figure.png|800]]

- **arXiv**: [2606.31723](https://arxiv.org/abs/2606.31723)
- **PDF**: https://arxiv.org/pdf/2606.31723
- **详细分析**: [[20_Research/Papers/具身智能/UniTacVLA_Unified_Tactile_Understanding_and_Prediction_in_Vision_Language_Action_Models|UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models]]
- **作者**: Xidong Zhang, Yichi Zhang, Jiaxin Shi, Fucai Zhu, Siyu Zhu, Michael Yu Wang, Xiaojun Wu, Weihao Yuan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：UniTacVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction.

</details>

---

### [[20_Research/Papers/具身智能/FastDSAC_Enhancing_Policy_Plasticity_via_Constrained_Exploration_for_Scalable_Humanoid_Locomotion|FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion]]

![[assets/2606.31691_figure.png|800]]

- **arXiv**: [2606.31691](https://arxiv.org/abs/2606.31691)
- **PDF**: https://arxiv.org/pdf/2606.31691
- **详细分析**: [[20_Research/Papers/具身智能/FastDSAC_Enhancing_Policy_Plasticity_via_Constrained_Exploration_for_Scalable_Humanoid_Locomotion|FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion]]
- **作者**: Guanchen Lu, Yajuan Dun, Yi Zhou, Letian Tao, Jingliang Duan, Jie Li, Guofa Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.9（加权：具身智能 2.4，强化学习 0.4，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable Humanoid Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanoidBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

</details>

---

### [[20_Research/Papers/具身智能/HABIT_Human-Aware_Behavior_and_Interaction_Training_Dataset_for_Robot_Manipulation|HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation]]

![[assets/2606.31682_figure.png|800]]

- **arXiv**: [2606.31682](https://arxiv.org/abs/2606.31682)
- **PDF**: https://arxiv.org/pdf/2606.31682
- **详细分析**: [[20_Research/Papers/具身智能/HABIT_Human-Aware_Behavior_and_Interaction_Training_Dataset_for_Robot_Manipulation|HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation]]
- **作者**: Jaehwi Song, Suchae Jeong, Byeongguk Jeon, Sungdong Kim, Minjoon Seo, Hyungmok Son, Kimin Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale demonstration datasets have been central to recent progress in general-purpose robot policies. However, existing datasets are collected in human-absent settings, and policies trained on such data may perform tasks competently in isolation but fail to exhibit human-aware behaviors. To address this gap, we introduce HABIT, a large-scale robot demonstration dataset for human-present environments. We organize tasks into three roles capturing distinct modes of human-robot interaction: Collaborator, where human and robot jointly accomplish a task; Coworker, where they pursue separate tasks in a shared space; and Supervisor, where the human directs the robot. The dataset comprises over 10K episodes and over 160 hours across 60 tasks. Our experiments show that training on human-present data elicits human-aware behaviors that robot-only data fails to produce: spatiotemporal synchronization in Collaborator tasks, yielding in Coworker tasks, and gesture grounding in Supervisor tasks. Moreover, training on HABIT enables rapid adaptation to new human-robot interaction tasks. By introducing human presence as a new axis of dataset diversity, HABIT extends robot policies to environments shared with humans.

</details>

---

### [[20_Research/Papers/强化学习/Stabilization_Learning_A_Paradigm_Transition_Bridging_Control_Theory_and_Machine_Learning|Stabilization Learning: A Paradigm Transition Bridging Control Theory and Machine Learning]]

![[assets/2606.31562_figure.png|800]]

- **arXiv**: [2606.31562](https://arxiv.org/abs/2606.31562)
- **PDF**: https://arxiv.org/pdf/2606.31562
- **详细分析**: [[20_Research/Papers/强化学习/Stabilization_Learning_A_Paradigm_Transition_Bridging_Control_Theory_and_Machine_Learning|Stabilization Learning: A Paradigm Transition Bridging Control Theory and Machine Learning]]
- **作者**: Quan Quan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Stabilization Learning: A Paradigm Transition Bridging Control Theory and Machine Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Point-to-Set, Set-to-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stabilization learning is an interdisciplinary paradigm that bridges control theory and machine learning. Its core idea is to enable systems to adjust their policies under perturbations or environmental changes through real-time feedback and adaptive mechanisms. It takes stability as its primary goal, distinguishing itself from certificate learning, which focuses on formal proofs, and reinforcement learning, which pursues optimality. It encompasses a range of methods, including Lyapunov-based analysis and design, deep feature extraction, and data-driven feedback synthesis, and is applicable to complex high-dimensional, nonlinear systems. This paper elaborates on the two major categories of stability in stabilization learning, as well as three typical application scenarios: control, observation, and recognition. It constructs a unified mathematical framework based on a six-tuple, and expands into two types of seven-tuple models: constrained learning with barrier spaces and tracking problems with targets. It also analyzes the roles, meanings, and implementation choices of key elements such as state space, controlled system, metrics, and policy. Through the formal reformulation of 11 types of problems, including multi-agent cooperative tracking, visual servo robot position stabilization, chess games, and Push-T tasks, this paper illustrates the potential applicability of the framework across multiple domains. Finally, it points out that future stabilization learning will focus on two major directions: constructing a unified problem framework and achieving efficient and robust learning, providing solutions for complex system control that combine theoretical rigor with engineering practicality.

</details>

---

### [[20_Research/Papers/机器人/Communication-Aware_Robot_Execution_for_Cloud_Inference_under_Spatially_Heterogeneous_Connectivity|Communication-Aware Robot Execution for Cloud Inference under Spatially Heterogeneous Connectivity]]

![[assets/2606.31497_figure.png|800]]

- **arXiv**: [2606.31497](https://arxiv.org/abs/2606.31497)
- **PDF**: https://arxiv.org/pdf/2606.31497
- **详细分析**: [[20_Research/Papers/机器人/Communication-Aware_Robot_Execution_for_Cloud_Inference_under_Spatially_Heterogeneous_Connectivity|Communication-Aware Robot Execution for Cloud Inference under Spatially Heterogeneous Connectivity]]
- **作者**: Fengkai Liu, Yuichi Ohsita, Masayuki Murata, Hideyuki Shimonishi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Communication-Aware Robot Execution for Cloud Inference under Spatially Heterogeneous Connectivity》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cloud-hosted foundation models enable robots to use semantic reasoning beyond onboard computational limits. In this setting, the robot executes a currently available primitive generated by the cloud, and continued task progress requires the next cloud result before this primitive is exhausted. This execution becomes fragile under spatially heterogeneous connectivity, because the current primitive determines when the next result is needed, whereas the wireless environment determines where the next request can be submitted and where the response can be retrieved. Strategies that reduce latency or improve individual transmissions can shorten this dependency, but they do not determine a submission location that supports reliable upload and leaves a feasible opportunity for response retrieval. To address this problem, we introduce the request--response window, which characterizes the time required for the next cloud cycle, including uplink transmission, cloud inference, downlink retrieval, and inference uncertainty. Building on this window and an available communication map, the proposed framework treats the next request point as a motion decision during ongoing primitive execution, selecting it to provide sufficient communication quality for cloud request submission while preserving progress within the finite support of the current primitive. The selected request point is incorporated into a local planner, which guides the robot toward the request point before submission and then continues task execution while maintaining sufficient connectivity for retrieving the next cloud result. Experiments in an indoor wireless scenario built from measurements show that the proposed method achieves the best or tied-best task success among the compared methods, while using fewer request attempts and producing lower request failure rates.

</details>

---

### [[20_Research/Papers/机器人/Energy-Optimal_Spatial_Iterative_Learning_within_a_Virtual_Tube|Energy-Optimal Spatial Iterative Learning within a Virtual Tube]]

![[assets/2606.31487_figure.png|800]]

- **arXiv**: [2606.31487](https://arxiv.org/abs/2606.31487)
- **PDF**: https://arxiv.org/pdf/2606.31487
- **详细分析**: [[20_Research/Papers/机器人/Energy-Optimal_Spatial_Iterative_Learning_within_a_Virtual_Tube|Energy-Optimal Spatial Iterative Learning within a Virtual Tube]]
- **作者**: Chen Min, Shuli Lv, Pengda Mao, Huixin Cao, Li Hong, Quan Quan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Energy-Optimal Spatial Iterative Learning within a Virtual Tube》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Due to the limited endurance of embedded energy sources such as lithium-polymer (LiPo) batteries, the flight duration and operational range of unmanned aerial vehicles (UAVs) are severely constrained. Although energy-efficient trajectory planning and control have been widely studied, most existing approaches rely on accurate system models and computationally expensive optimization procedures. This paper proposes a model-free online iterative learning (IL) framework to minimize energy consumption. Without requiring explicit models of UAV dynamics or energy consumption, the proposed method improves energy efficiency while maintaining a low computational cost. The per-iteration computational complexity is O(n), where n denotes the number of path points. In the tested cases, the proposed method is approximately 50--60 times faster than the model-based IPOPT benchmark. Simulation results and real-world flight experiments across multiple UAV platforms validate the effectiveness, computational efficiency, and practical applicability of the proposed approach.

</details>

---

### [[20_Research/Papers/具身智能/Revisiting_Parameter_Redundancy_in_Vision-Language-Action_Models_Insights_from_VLM-to-VLA_Adaptation|Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation]]

![[assets/2606.31382_figure.png|800]]

- **arXiv**: [2606.31382](https://arxiv.org/abs/2606.31382)
- **PDF**: https://arxiv.org/pdf/2606.31382
- **详细分析**: [[20_Research/Papers/具身智能/Revisiting_Parameter_Redundancy_in_Vision-Language-Action_Models_Insights_from_VLM-to-VLA_Adaptation|Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation]]
- **作者**: Fengnian Zhang, Tao Huang, Siyu Xu, Zhong Jin, Chang Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, VLA_Parameter_Redundancy_VLM2VLA, VLM-VLA, VLM-to-VLA, VLM4VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and $π_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained environments.

</details>

---

### [[20_Research/Papers/机器人/Verification-Gated_Agentic_Mission-State_Governance_for_Intelligent_Industrial_Multi-Robot_Systems|Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems]]

![[assets/2606.31339_figure.png|800]]

- **arXiv**: [2606.31339](https://arxiv.org/abs/2606.31339)
- **PDF**: https://arxiv.org/pdf/2606.31339
- **详细分析**: [[20_Research/Papers/机器人/Verification-Gated_Agentic_Mission-State_Governance_for_Intelligent_Industrial_Multi-Robot_Systems|Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems]]
- **作者**: Guoqin Tang, Qingxuan Jia, Yichen Tan, Zeyuan Huang, Ning Ji, Gang Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PlanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic artificial intelligence is increasingly used to decompose industrial tasks, propose robot actions, and adapt execution plans in dynamic cyber-physical environments. However, autonomous proposal generation alone does not guarantee that multi-robot industrial systems preserve task dependencies, resource ownership, safety holds, or repair boundaries during long-horizon execution. This paper introduces a verification-gated agentic mission-state governance framework for intelligent industrial multi-robot systems. The framework maintains two synchronized state objects: an evolving task forest for persistent hierarchy, delayed grounding, and repairable substructures; and a governed blackboard for online execution state, robot traces, resource locks, world beliefs, proposals, verification records, and scene-temporary constraints. From each forest--blackboard snapshot, a derived execution coupling topology exposes cross-branch dependencies for proposal verification, parallel-commit eligibility, and bounded repair. Candidate assignments, repairs, deferrals, and constraint updates may be generated by heuristic, optimization, or agentic reasoning modules, but they can update the committed mission state only after deterministic verification and atomic commit. We evaluate the framework in an indoor factory multi-robot scenario, 30-seed remote-construction stress benchmarks, structural ablations, and scalability probes. The results show improved verified and safety-audited mission-state progress with fewer invalid commitments, lock conflicts, duplicate assignments, abandoned nodes, and disruptive repairs under modeled mission predicates. The study positions agentic AI as a proposal-generating layer governed by inspectable mission-state verification rather than as an unchecked execution authority.

</details>

---

### [[20_Research/Papers/具身智能/Plan_Right,_Then_Plan_Tight_Symbolic_RL_for_Efficient_Embodied_Reasoning|Plan Right, Then Plan Tight: Symbolic RL for Efficient Embodied Reasoning]]

![[assets/2606.31260_figure.png|800]]

- **arXiv**: [2606.31260](https://arxiv.org/abs/2606.31260)
- **PDF**: https://arxiv.org/pdf/2606.31260
- **详细分析**: [[20_Research/Papers/具身智能/Plan_Right,_Then_Plan_Tight_Symbolic_RL_for_Efficient_Embodied_Reasoning|Plan Right, Then Plan Tight: Symbolic RL for Efficient Embodied Reasoning]]
- **作者**: Xiangli Shi, Xiaomeng Zhu, Ye Tian, Yuchun Guo, Ziyang Sun, Lujie Yin, Yuxuan Zhou, Yufei Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.3，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Plan Right, Then Plan Tight: Symbolic RL for Efficient Embodied Reasoning》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Short-RL, WordNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied task planning asks an agent to turn a natural-language instruction into an executable sequence of actions in a physical scene, and is a building block for household, assistive, and service robots. Recent prompting-based and reinforcement-learning planners generate fluent action text but lack a cheap deterministic check that the produced plan is valid in the target world, while high-fidelity simulation is too slow to serve as an inner-loop training signal. The general problem is therefore how to obtain verifiable supervision and rewards for embodied planners without relying on string-level matching or full simulation. Here we show that a single BDDL specification, automatically constructed from open-world video evidence or curated tasks, can serve as a shared interface for data construction, plan verification, and reward design. A video-to-BDDL parser, an LLM verifier, and a lightweight symbolic engine together supply dense feedback at millisecond latency. We further introduce GroupAdapt, a difficulty-aware length schedule that uses the in-batch group pass rate as a zero-cost signal so that hard prompts get wider length tolerance and automatically tighten as their pass rate improves. Under the guidance of the proposed verifier and GroupAdapt schedule, the 8B planner attains a Strict-Pass score of 97.3 on BEHAVIOR-1000, yielding a 25.9 percent relative improvement over the Qwen3-8B baseline. This result exceeds the strongest large-model baseline by 3.5 percent, while simultaneously compressing the response length by 79 percent to 207 tokens, demonstrating both effectiveness and efficiency.

</details>

---

### [[20_Research/Papers/机器人/Diffusion-based_4D_Trajectory_Prediction_and_Distributed_Control_for_UAV_Swarms|Diffusion-based 4D Trajectory Prediction and Distributed Control for UAV Swarms]]

![[assets/2606.31197_figure.png|800]]

- **arXiv**: [2606.31197](https://arxiv.org/abs/2606.31197)
- **PDF**: https://arxiv.org/pdf/2606.31197
- **详细分析**: [[20_Research/Papers/机器人/Diffusion-based_4D_Trajectory_Prediction_and_Distributed_Control_for_UAV_Swarms|Diffusion-based 4D Trajectory Prediction and Distributed Control for UAV Swarms]]
- **作者**: Tianshun Li, Hongliang Lu, Haoang Li, Xinhu Zheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《Diffusion-based 4D Trajectory Prediction and Distributed Control for UAV Swarms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate 4D trajectory prediction and closed-loop tracking are essential for Unmanned Aerial Vehicle (UAV) swarms to achieve safe and efficient operations in complex low-altitude environments such as urban airspaces, industrial sites, and indoor facilities. However, this task remains challenging due to intrinsic nonlinearity of UAV swarm dynamics and strict real-time constraints of swarm formation control. To address these challenges, we propose a unified framework that couples coarse-to-fine trajectory forecasting with uncertainty-aware Distributed Nonlinear Model Predictive Control (DNMPC). Our approach features two key innovations: 1) a dimension-decoupled trajectory prediction module that reduces computational complexity by forecasting axis-wise motion, and 2) a diffusion-based residual dynamics refinement module that captures temporally correlated dynamic uncertainties. These refined predictions are then integrated into a DNMPC loop to ensure formation stability. We also introduce a synchronized multi-scenario 4D UAV swarm dataset spanning six representative airspace scenarios. The dataset contains over \textbf{7,900} frames of synchronized three-UAV trajectories with frame-level annotations of speed intention and target sector. Extensive experiments demonstrate that our approach outperforms state-of-the-art baselines, reducing trajectory tracking error by up to \textbf{10-15\%} and achieving sub-\textbf{0.07\,m} average tracking error in complex urban and industrial environments, while maintaining real-time inference speeds of 34 FPS (sub-30 ms latency) suitable for agile flight.

</details>

---

### [[20_Research/Papers/具身智能/ELASTIC_Efficiently_Learning_to_Adaptively_Scale_Test-Time_Compute_for_Generative_Control_Policies|ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies]]

![[assets/2606.31132_figure.png|800]]

- **arXiv**: [2606.31132](https://arxiv.org/abs/2606.31132)
- **PDF**: https://arxiv.org/pdf/2606.31132
- **详细分析**: [[20_Research/Papers/具身智能/ELASTIC_Efficiently_Learning_to_Adaptively_Scale_Test-Time_Compute_for_Generative_Control_Policies|ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies]]
- **作者**: Andrew Zou Li, Gokul Swamy, Yonatan Bisk, Andrea Bajcsy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative Control Policies》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP's training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at matched compute budgets. On real-world robot manipulation with the $π_{0.5}$ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.

</details>

---

### [[20_Research/Papers/具身智能/Efficient_Sim-to-Real_Transfer_of_World-Action_Models_from_Synthetic_Priors|Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors]]

![[assets/2606.31101_figure.jpg|800]]

- **arXiv**: [2606.31101](https://arxiv.org/abs/2606.31101)
- **PDF**: https://arxiv.org/pdf/2606.31101
- **详细分析**: [[20_Research/Papers/具身智能/Efficient_Sim-to-Real_Transfer_of_World-Action_Models_from_Synthetic_Priors|Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors]]
- **作者**: Zixing Wang, Kausik Sivakumar, Jinghuan Shang, Yafei Hu, Zhaoming Xie, Ran Gong, Xiaohan Zhang, Karl Schmeckpeper
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bridging the sim-to-real gap is a core challenge in deploying learned manipulation policies. Sim-to-real learning is attractive because it can replace expensive real robot demonstrations with scalable synthetic data, yet world-action models have not previously been shown to transfer from simulation to real robotic manipulation. We study whether a world-action model can be trained from synthetic priors and deployed zero-shot in the real world. To this end, we build upon Cosmos Policy, a video diffusion model adapted for visuomotor control. We construct simulation environments with extensive domain randomization and generate demonstrations using the AnyTask motion planning pipeline. We evaluate our approach across object lifting, drawer opening, and pick-and-place tasks using ${\sim}800$ synthetic demonstrations per task and no real demonstrations. When deployed zero-shot on a Franka Robot, our policy attains a 35\% average success rate. To our knowledge, this represents the first successful sim-to-real transfer of a world-action model for robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Labimus_A_Simulation_and_Benchmark_for_Humanoid_Dexterous_Manipulation_in_Chemical_Laboratory|Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory]]

![[assets/2606.31037_figure.png|800]]

- **arXiv**: [2606.31037](https://arxiv.org/abs/2606.31037)
- **PDF**: https://arxiv.org/pdf/2606.31037
- **详细分析**: [[20_Research/Papers/机器人/Labimus_A_Simulation_and_Benchmark_for_Humanoid_Dexterous_Manipulation_in_Chemical_Laboratory|Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory]]
- **作者**: Yuhan Wu, Zhao Jin, Tao Li, Yuheng Zhang, Zhengping Che, Jian Tang, Zhichao Wang, Shuo Wang, Jun Jiang, Xiaobo Li, Yanyong Zhang, Yan Xia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FurnitureBench, GenieSim, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

</details>

---

### [[20_Research/Papers/具身智能/Multisensory_Continual_Learning_Adapting_Pretrained_Visuomotor_Policies_to_Force|Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force]]

![[assets/2606.30988_figure.png|800]]

- **arXiv**: [2606.30988](https://arxiv.org/abs/2606.30988)
- **PDF**: https://arxiv.org/pdf/2606.30988
- **详细分析**: [[20_Research/Papers/具身智能/Multisensory_Continual_Learning_Adapting_Pretrained_Visuomotor_Policies_to_Force|Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force]]
- **作者**: Jaden Clark, Changhao Wang, Yihuai Gao, Seongheon Hong, Hojung Choi, Mark Cutkosky, Yifan Hou, Shuran Song
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Multisensory Continual Learning: Adapting Pretrained Visuomotor Policies to Force》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation often relies on sensory feedback beyond vision, particularly in contact-rich settings where force, tactile, or audio signals reveal interaction states that are not directly observable from images. However, these modalities are often hardware- and task-specific, and large-scale multisensory robot datasets remain scarce. As a result, it is impractical to pretrain policies with every sensor they may encounter. We study multisensory continual learning: adapting a pretrained robot policy to new tasks with newly introduced modalities while preserving performance under the original sensor suite. We propose MuSe, which incorporates limited multisensory data into pretrained vision-only policies through multi-stage fusion, multisensory future prediction, and experience replay over pretraining data. We instantiate MuSe by augmenting a pretrained vision-only policy with force-torque sensing and evaluate it on real-world manipulation tasks. Our experiments show that MuSe performs strongly on contact-rich finetuning tasks while preserving, and in some cases improving, performance on the original pretraining tasks. These results suggest that a modest multisensory dataset can improve general robot capabilities beyond the finetuning distribution. Project website: https://jadenvc.github.io/multisensory-continual-learning/

</details>

---

### [[20_Research/Papers/具身智能/The_Quadruped_Soft_Tail_Compliant_Grasping_and_Swabbing_for_Contamination_Surveys_in_Harsh_Environments|The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments]]

![[assets/2606.30900_figure.jpeg|800]]

- **arXiv**: [2606.30900](https://arxiv.org/abs/2606.30900)
- **PDF**: https://arxiv.org/pdf/2606.30900
- **详细分析**: [[20_Research/Papers/具身智能/The_Quadruped_Soft_Tail_Compliant_Grasping_and_Swabbing_for_Contamination_Surveys_in_Harsh_Environments|The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments]]
- **作者**: Harald Minde Hansen, Nandita Gallacher, Kristin Y. Pettersen, Jan Tommy Gravdahl, Mario di Castro
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.5（加权：具身智能 3，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《The Quadruped Soft Tail: Compliant Grasping and Swabbing for Contamination Surveys in Harsh Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Beryllium contamination surveys in radioactive areas are challenging for robots in environments cluttered with cables and electronics. To address this problem, we have developed a novel quadruped system augmentation: A lightweight, soft, and compliant tendon-actuated robotic tail mounted on a quadruped robot. The tail features a hollow, flexible backbone and a tendon-actuated soft gripper that enables the robot to pick up sampling tissues, swab contaminated surfaces, and release the tissues at designated collection locations for subsequent beryllium analysis. To enable intuitive teleoperation, a closed-form kinematic model and a singularity-robust task-space controller are developed. Experimental results demonstrate that gripper actuation has a negligible effect on robot shape, while common-mode tendon actuation provides an effective mechanism for stiffness modulation and preload control. Furthermore, experimental validation indicates that the proposed kinematic model provides a suitable basis for real-time task-space control. The proposed system combines the agility of legged locomotion with the compliance of soft robotic manipulation, enabling the complete contamination-survey procedure to be performed without human exposure. While motivated by beryllium contamination surveys at CERN, the proposed quadruped soft-tail concept is broadly applicable to legged robots operating in cluttered, confined, or hazardous environments where conventional rigid-link manipulators are undesirable.

</details>

---

### [[20_Research/Papers/强化学习/Sampling-Based_Coordination-Informed_Multi-Objective_Multi-Robot_Reinforcement_Learning|Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning]]

![[assets/2606.30893_figure.png|800]]

- **arXiv**: [2606.30893](https://arxiv.org/abs/2606.30893)
- **PDF**: https://arxiv.org/pdf/2606.30893
- **详细分析**: [[20_Research/Papers/强化学习/Sampling-Based_Coordination-Informed_Multi-Objective_Multi-Robot_Reinforcement_Learning|Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning]]
- **作者**: Antonio Marino, Esteban Restrepo, Soon-jo Chung, Paolo Robuffo Giordano, Claudio Pacchierotti
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.1，强化学习 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Sampling-Based Coordination-Informed Multi-Objective Multi-Robot Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CIMORL, MARL, MOMARL, MOPDERL, MORL, PGMORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot systems must simultaneously optimize competing objectives while maintaining coordinated behavior. Existing multi-agent reinforcement learning approaches often rely on fixed or centralized coordination, which limits adaptability and violates distributed constraints. This work introduces the Coordination-Informed Multi-Objective Reinforcement Learning (CIMORL) framework, integrating a distributed weight prediction mechanism, a privileged expert training strategy, and theoretical guarantees for Pareto-optimal solutions. We present the base CIMORL method alongside two sampling-based variants, CIMORL-TS (Tree Search) and CIMORL-MPPI (MPPI), which leverage privileged global information during training to enable fully decentralized deployment. Experimental validation in cooperative and adversarial scenarios demonstrates a $21.2\%$ hypervolume improvement and superior policy stability compared to state-of-the-art baselines. Real-world experiments with Crazyflie drones further validate the framework's robustness in resource allocation and multi-attacker multi-defend scenarios under partial observability.

</details>

---

### [[20_Research/Papers/机器人/TAPE_Tether-Aware_Path_Planning_for_Autonomous_Exploration_of_Unknown_3D_Cavities_Using_a_Tangle-Compatible_Tethered_Aerial_Robot|TAPE: Tether-Aware Path Planning for Autonomous Exploration of Unknown 3D Cavities Using a Tangle-Compatible Tethered Aerial Robot]]

![[assets/2606.30817_first_page.png|800]]

- **arXiv**: [2606.30817](https://arxiv.org/abs/2606.30817)
- **PDF**: https://arxiv.org/pdf/2606.30817
- **详细分析**: [[20_Research/Papers/机器人/TAPE_Tether-Aware_Path_Planning_for_Autonomous_Exploration_of_Unknown_3D_Cavities_Using_a_Tangle-Compatible_Tethered_Aerial_Robot|TAPE: Tether-Aware Path Planning for Autonomous Exploration of Unknown 3D Cavities Using a Tangle-Compatible Tethered Aerial Robot]]
- **作者**: Louis Petit, Alexis Lussier Desbiens
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《TAPE: Tether-Aware Path Planning for Autonomous Exploration of Unknown 3D Cavities Using a Tangle-Compatible Tethered Aerial Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This letter presents the first method for autonomous exploration of unknown cavities in three dimensions (3D) that focuses on minimizing the distance traveled and the length of tether unwound. Considering that the tether entanglements are little influenced by the global path, our approach employs a 2-level hierarchical architecture. The global frontier-based planning solves a Traveling Salesman Problem (TSP) to minimize the distance. The local planning attempts to minimize the path cost and the tether length using an adjustable decision function whose parameters play on the trade-off between these two values. The proposed method, TAPE, is evaluated through detailed simulation studies as well as field tests. On average, our method generates a 4.1% increase in distance traveled compared to the TSP solution without our local planner, with which the length of the tether remains below the maximum allowed value in 53% of the simulated cases against 100% with our method.

</details>

---

### [[20_Research/Papers/机器人/Wind_and_State_Estimation_on_SE(3)_Comparative_Evaluation_of_EKF_and_UKF_with_Continuous_and_Discrete_Quadrotor_Models|Wind and State Estimation on SE(3): Comparative Evaluation of EKF and UKF with Continuous and Discrete Quadrotor Models]]

![[assets/2606.30804_figure.png|800]]

- **arXiv**: [2606.30804](https://arxiv.org/abs/2606.30804)
- **PDF**: https://arxiv.org/pdf/2606.30804
- **详细分析**: [[20_Research/Papers/机器人/Wind_and_State_Estimation_on_SE(3)_Comparative_Evaluation_of_EKF_and_UKF_with_Continuous_and_Discrete_Quadrotor_Models|Wind and State Estimation on SE(3): Comparative Evaluation of EKF and UKF with Continuous and Discrete Quadrotor Models]]
- **作者**: Hiranya Udagedara, Adam Bigsby, Mahdis Bisheban
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Systems

#### 研究背景与动机

《Wind and State Estimation on SE(3): Comparative Evaluation of EKF and UKF with Continuous and Discrete Quadrotor Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Use of quadrotor UAVs for wind velocity estimation is gaining popularity in recent studies, leveraging their maneuverability, compact size and low cost. Among available approaches, model-based wind velocity estimation is most commonly used, since it relies only on onboard sensors. However, as the quadrotor is a highly nonlinear system, thus making this task challenging. This study evaluate the use of both discrete and continuous dynamic equations of the quadrotor UAV for wind velocity estimation on SE(3), rather than commonly adapted continuous or discretized form. Lie Group Variational Integrator, developed on discrete Lagrangian is used as the discrete model without any approximation or discritization. The study assess both the discrete and continuous form of the quadrotor dynamics on SE(3) using Extended Kalman filter (EKF), and Unscented Kalman filter (UKF). The quadrotor UAV performance is evaluated in both MATLAB-based numerical simulations and free outdoor flight. The numerical simulations are conducted during both hovering and trajectory-tracking flights. Results demonstrate that, by using discrete SE(3) dynamics coupled with UKF, the quadrotor achieves higher estimation accuracy while maintaining trajectory tracking, even with low-cost sensors. These findings highlight the potential of discrete quadrotor models with UKF not only for wind velocity estimation but also for other high-accuracy tasks, even when relying on low-cost onboard sensors.

</details>

---

### [[20_Research/Papers/强化学习/From_Grasps_to_Dexterity_Large-Scale_Grasp_Pretraining_for_Dexterous_Manipulation|From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation]]

![[assets/2606.30749_figure.png|800]]

- **arXiv**: [2606.30749](https://arxiv.org/abs/2606.30749)
- **PDF**: https://arxiv.org/pdf/2606.30749
- **详细分析**: [[20_Research/Papers/强化学习/From_Grasps_to_Dexterity_Large-Scale_Grasp_Pretraining_for_Dexterous_Manipulation|From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation]]
- **作者**: Ying Yuan, Xinyu Liu, Sriram Krishna, David Held
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PartNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

</details>

---

### [[20_Research/Papers/具身智能/Vision-Language_Procedural_Reasoning_for_Context-Aware_Reward_Modeling_of_Robotic_Endovascular_Guidewire_Navigation|Vision-Language Procedural Reasoning for Context-Aware Reward Modeling of Robotic Endovascular Guidewire Navigation]]

![[assets/2606.30698_figure.png|800]]

- **arXiv**: [2606.30698](https://arxiv.org/abs/2606.30698)
- **PDF**: https://arxiv.org/pdf/2606.30698
- **详细分析**: [[20_Research/Papers/具身智能/Vision-Language_Procedural_Reasoning_for_Context-Aware_Reward_Modeling_of_Robotic_Endovascular_Guidewire_Navigation|Vision-Language Procedural Reasoning for Context-Aware Reward Modeling of Robotic Endovascular Guidewire Navigation]]
- **作者**: Wentong Tian, Jiyuan Zhao, Tianliang Yao, Yuxiang Fan, Zhengyu Shi, Dong Liu, Peng Qi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Vision-Language Procedural Reasoning for Context-Aware Reward Modeling of Robotic Endovascular Guidewire Navigation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic-assisted endovascular interventions demand accurate, stable, and context-aware guidewire navigation in complex and patient-specific vascular anatomies. Despite recent advances in robotic precision and learning-based control, existing autonomous navigation methods remain limited by their reliance on static reward functions and the lack of explicit procedural reasoning regarding anatomical context and task progression. To address these challenges, this paper proposes a vision-language procedural reasoning (VL-PR) framework for autonomous guidewire navigation. The framework integrates a multimodal large language model (MLLM) as a procedural reasoning module that interprets real-time visual observations to infer high-level navigation contexts. Instead of generating low-level control commands, the inferred procedural insights enable context-aware reward adaptation by dynamically adjusting the importance of reward components across different navigation phases. This approach allows a single policy to resolve competing objectives and handle complex transitions while preserving a consistent global task goal. Experiments on a physical robotic platform across diverse vascular scenarios demonstrate enhanced task reliability and streamlined navigational efficiency, highlighting the advantages over static-reward methods and offering a scalable solution for complex and multi-task robotic endovascular procedures.

</details>

---
