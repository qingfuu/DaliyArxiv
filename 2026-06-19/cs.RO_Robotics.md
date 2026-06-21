# cs.RO | Robotics | 2026-06-19

#arxiv #ComputerScience

**论文数**: 28

### [[20_Research/Papers/具身智能/MemoryWAM_Efficient_World_Action_Modeling_with_Persistent_Memory|MemoryWAM: Efficient World Action Modeling with Persistent Memory]]

![[assets/2606.20562_figure.png|800]]

- **arXiv**: [2606.20562](https://arxiv.org/abs/2606.20562)
- **PDF**: https://arxiv.org/pdf/2606.20562
- **详细分析**: [[20_Research/Papers/具身智能/MemoryWAM_Efficient_World_Action_Modeling_with_Persistent_Memory|MemoryWAM: Efficient World Action Modeling with Persistent Memory]]
- **作者**: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《MemoryWAM: Efficient World Action Modeling with Persistent Memory》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GigaWorld, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling. World action models (WAMs) possess these capabilities by jointly modeling visual foresight and actions conditioned on both current and historical observations, making them a promising paradigm for robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of recent observations and therefore struggle in non-Markovian environments, whereas methods that preserve long histories incur time and space costs that grow substantially with sequence length. To address this challenge, we introduce MemoryWAM, a world action model with efficient persistent memory. MemoryWAM uses a hybrid memory design that combines recent frames, event-boundary anchor frames, and compact gist tokens that summarize long-range history. A tailored attention mechanism enables retrieval of both detailed short-term context and compressed long-term context, supporting memory-dependent decision-making with reduced inference latency and GPU memory usage. Across long-horizon, memory-dependent manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong vision-language-action (VLA) and WAM baselines while maintaining favorable computational efficiency.

</details>

---

### [[20_Research/Papers/强化学习/Generating_Robot_Hands_from_Human_Demonstrations|Generating Robot Hands from Human Demonstrations]]

![[assets/2606.20549_figure.png|800]]

- **arXiv**: [2606.20549](https://arxiv.org/abs/2606.20549)
- **PDF**: https://arxiv.org/pdf/2606.20549
- **详细分析**: [[20_Research/Papers/强化学习/Generating_Robot_Hands_from_Human_Demonstrations|Generating Robot Hands from Human Demonstrations]]
- **作者**: Sha Yi, Nicklas Hansen, Xueqian Bai, Carmelo Sferrazza, Michael T. Tolley, Xiaolong Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Generating Robot Hands from Human Demonstrations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning has advanced rapidly in learning control, but learning the physical body of a robot remains much more difficult because jointly searching over design and control creates a very large combinatorial problem. Here, we present a data-driven framework for generating robot hands from human demonstrations. Instead of learning a complex controller together with each candidate design, we generate robot hand designs using the same simple control policy used after fabrication: matching fingertip positions through inverse kinematics. Using more than 4 million frames of human fingertip motion from everyday manipulation, our algorithm optimizes tree-structured robot hands to reproduce desired target motions. The framework produced both a 6-degree-of-freedom (DoF) general-purpose hand and lower-DoF task-specific hands with spatial four-bar mimic joints. To accelerate the search over designs, we trained a reinforcement-learning (RL) actor to propose good hand designs and joint angles, reducing search time from hours to minutes. We fabricated the mechanisms directly as one-piece articulated structures with print-in-place joints. In real-world experiments, the 6-DoF hand achieved highly accurate teleoperated fingertip tracking better than available commercial robot hands, whereas the specialized 3-DoF hands reproduced structured human and synthetic trajectories with reduced mechanical complexity. These results showed that large-scale human motion data can be used not only to train robot controllers but also as a reference for optimizing and generating the physical embodiment of robots.

</details>

---

### [[20_Research/Papers/机器人/Increasing_Resilience_of_Continuum_Robots_via_Motion_Planning_Algorithms|Increasing Resilience of Continuum Robots via Motion Planning Algorithms]]

![[assets/2606.20495_first_page.png|800]]

- **arXiv**: [2606.20495](https://arxiv.org/abs/2606.20495)
- **PDF**: https://arxiv.org/pdf/2606.20495
- **详细分析**: [[20_Research/Papers/机器人/Increasing_Resilience_of_Continuum_Robots_via_Motion_Planning_Algorithms|Increasing Resilience of Continuum Robots via Motion Planning Algorithms]]
- **作者**: Oxana Shamilyan, Ievgen Kabin, Zoya Dyka, Oleksandr Sudakov, Peter Langendoerfer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Increasing Resilience of Continuum Robots via Motion Planning Algorithms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an experimental study of motion planning for resilient continuum robots. In this study we mainly focused on multi-criteria decision-making, its application for path-planning algorithms, impact on the generated path and execution time. To do this, we used two well-known algorithms for path planning, namely Genetic algorithm and A star algorithm, and modified them by adding the Analytical Hierarchy Process algorithm to evaluate the quality of the paths generated. In our experiment the Analytical Hierarchy Process considers four different criteria, i.e. distance, motors damage, mechanical damage of the robot's arm and accuracy, each considered to contribute to the resilience of a continuum robot. The use of different criteria is necessary to increase the time to maintenance operations of the continuum robot. We conducted the experiments using two different simulated environments of the robot. Although we significantly simplified the robot's model and its environment, we still implemented some of the features of the environment based on the real robot prototype. In particular, one of the environments has single- as well as multi-path points, and other consists of the multi-path points only. The results show that, in contrast to A star, the performance time of Genetic algorithm does not depend on the environment's cardinality. It generates more diverse paths, which increases the robot's resilience.

</details>

---

### [[20_Research/Papers/具身智能/Slow_Brain,_Fast_Planner_Latency-Resilient_VLM-Augmented_Urban_Navigation|Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation]]

![[assets/2606.20458_figure.png|800]]

- **arXiv**: [2606.20458](https://arxiv.org/abs/2606.20458)
- **PDF**: https://arxiv.org/pdf/2606.20458
- **详细分析**: [[20_Research/Papers/具身智能/Slow_Brain,_Fast_Planner_Latency-Resilient_VLM-Augmented_Urban_Navigation|Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation]]
- **作者**: Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based planners for sidewalk navigation can generate diverse candidate trajectories in real time, yet their scoring functions often fail to select the best trajectory in challenging situations, outputting trajectories that make the mobile robot drive onto grass, toward pedestrians, or in the wrong direction, even when better candidates exist in the same set. We call this the trajectory scoring gap: in real-world sidewalk navigation, the gap between an anchor-based planner's top choice and the best possible candidate is substantial, likely due to limited high-level scene understanding capability of the planner. Rather than replacing the planner with an end-to-end Vision-Language-Action model, we propose a VLM-Planner interface that uses a VLM to select a candidate index from the planner's proposal set and then fuse it with the planner's initial output. However, VLMs take 1--3s per query and so cannot directly drive a 5--20Hz control loop. We contribute a training-free, latency-resilient trajectory-level fusion layer that turns a stale VLM selection into real-time planner scoring via geometric similarity with exponential decay. On $\sim$2,000 challenging real-world scenarios (e.g., junctions, pedestrian encounters), VLM selection achieves 30% ADE reduction versus the planner's best selection, while the planner remains competitive in routine situations. In simulation, Score Fusion maintains &gt;80% success rate with delays up to 5s. We demonstrate the full system on a mobile robot navigating challenging campus sidewalks with varied network latency.

</details>

---

### [[20_Research/Papers/具身智能/TaCauchy_An_Extensible_FEM_Framework_for_Vision-Based_Tactile_Simulation|TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation]]

![[assets/2606.20426_figure.png|800]]

- **arXiv**: [2606.20426](https://arxiv.org/abs/2606.20426)
- **PDF**: https://arxiv.org/pdf/2606.20426
- **详细分析**: [[20_Research/Papers/具身智能/TaCauchy_An_Extensible_FEM_Framework_for_Vision-Based_Tactile_Simulation|TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation]]
- **作者**: Hengfei Zhao, Yifan Xie, Junhao Gong, Yue Sun, Kai Zhu, Weihua He, Shoujie Li, Haohuan Fu, Wenbo Ding
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TaCauchy: An Extensible FEM Framework for Vision-Based Tactile Simulation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based tactile sensors require high-fidelity simulation for reinforcement learning, yet existing approaches struggle to provide accurate mechanical stress fields within GPU-accelerated robotics platforms. We present TaCauchy, an extensible Finite Element Method (FEM) framework that integrates rigorous physics-based force computation into Isaac Sim. Built on the Unified Incremental Potential Contact (UIPC) solver, TaCauchy directly computes Cauchy stress tensors from hyperelastic constitutive laws and projects them onto contact surfaces to obtain traction forces and pressure distributions, providing mechanical ground truth from first principles rather than empirical estimation. Our framework features automatic mesh generation with geometry-aware adaptive refinement and a modular sensor interface enabling rapid integration of diverse sensors (GelSight Mini, DIGIT, 9DTact) with minimal configuration. Performance benchmarks demonstrate 33.40 FPS for single environments and 555 FPS aggregate throughput across 60 parallel environments, with stress extraction overhead under 1 ms. Physical validation experiments show strong agreement between simulated and real tactile responses across force ranges from 1.2556 N to 4.7332 N, achieving SSIM above 0.93, confirming the framework's capability to provide accurate, physically-grounded force supervision for downstream robotic manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/Agentic_AutoResearch_forSpace_Autonomy_An_Auditable,_LLM-Driven_Research_Agent_for_Aerospace_Control_Problems|Agentic AutoResearch forSpace Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems]]

![[assets/2606.20394_figure.png|800]]

- **arXiv**: [2606.20394](https://arxiv.org/abs/2606.20394)
- **PDF**: https://arxiv.org/pdf/2606.20394
- **详细分析**: [[20_Research/Papers/具身智能/Agentic_AutoResearch_forSpace_Autonomy_An_Auditable,_LLM-Driven_Research_Agent_for_Aerospace_Control_Problems|Agentic AutoResearch forSpace Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems]]
- **作者**: Amit Jain, Richard Linares
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Agentic AutoResearch forSpace Autonomy: An Auditable, LLM-Driven Research Agent for Aerospace Control Problems》归入 大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MLAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spacecraft guidance, navigation, and control functions are increasingly realized as learned policies distilled from expert solvers. Developing such a policy is itself a research process: an investigator selects an architecture and hyperparameters, runs experiments, and must determine whether an apparent improvement is genuine or merely seed noise. This paper presents AutoResearch, a framework in which a large language model autonomously drives that loop for aerospace control problems, coupled with a credibility layer, built into the loop, that certifies each reported result against the problem's own measured seed noise. The language model serves only as the offline research agent that develops the control policy; the trained policy it produces is then deployed onboard the spacecraft, while the model itself never operates the vehicle. At each iteration the agent reads a plain-language problem description and the run history, proposes a single edit to the training script, executes it, and logs the outcome. No reported result is credited until it passes the same three checks: measured per-problem seed noise, reseeded verification of the best configuration, and leave-one-out pruning of the agent's edits. The same loop is applied, unchanged, to two aerospace control problems: a Clohessy-Wiltshire relative rendezvous and a safety-constrained collision-avoidance docking past a keep-out zone, each calibrated against a known optimal control benchmark. In both, the audited policy clears the measured seed noise by many standard deviations; an undirected search over the same parameters does not. On the docking problem the gap becomes categorical: undirected search yields no feasible policy, while the learned policy stays outside the keep-out zone on every seed.

</details>

---

### [[20_Research/Papers/机器人/CoLI_A_Reproducible_Platform_for_Continuum_Robot_Learning_via_Monolithic_3D_Printing_and_Isomorphic_Teleoperation|CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation]]

![[assets/2606.20389_figure.jpg|800]]

- **arXiv**: [2606.20389](https://arxiv.org/abs/2606.20389)
- **PDF**: https://arxiv.org/pdf/2606.20389
- **详细分析**: [[20_Research/Papers/机器人/CoLI_A_Reproducible_Platform_for_Continuum_Robot_Learning_via_Monolithic_3D_Printing_and_Isomorphic_Teleoperation|CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation]]
- **作者**: Ziyuan Tang, Chenxi Xiao*
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuum robots offer strong potential for manipulation tasks due to their high degrees of freedom, compliant structures, and operational safety. However, their adoption in both research and practical applications has been hindered by reproducibility issues arising from complex fabrication and assembly processes, challenging kinematic modeling, and a lack of intuitive control interfaces. To address these challenges, we present a novel open-source continuum robot design. The platform features a simplified fabrication pipeline enabled by multi-material 3D printing, allowing the arm to be fabricated as a monolithic compliant structure with minimal assembly. Control is achieved through an isomorphic teleoperation interface that establishes a direct actuator-level mapping, eliminating the need for explicit kinematic modeling and providing a singularity-free mapping. Building on this hardware design, the platform further supports imitation-learning-based autonomous control. The proposed system is evaluated through hardware characterization and a set of manipulation tasks. Experimental results demonstrate that the platform provides a reproducible, learning-ready continuum robot system, accelerating algorithmic development and systematic benchmarking for the continuum robotics community.

</details>

---

### [[20_Research/Papers/具身智能/An_Infrastructure-less,_Control-Independent_Solution_to_Relative_Localisation_of_a_Team_of_Mobile_Robots_using_Ranging_Measurements|An Infrastructure-less, Control-Independent Solution to Relative Localisation of a Team of Mobile Robots using Ranging Measurements]]

![[assets/2606.20365_figure.png|800]]

- **arXiv**: [2606.20365](https://arxiv.org/abs/2606.20365)
- **PDF**: https://arxiv.org/pdf/2606.20365
- **详细分析**: [[20_Research/Papers/具身智能/An_Infrastructure-less,_Control-Independent_Solution_to_Relative_Localisation_of_a_Team_of_Mobile_Robots_using_Ranging_Measurements|An Infrastructure-less, Control-Independent Solution to Relative Localisation of a Team of Mobile Robots using Ranging Measurements]]
- **作者**: Paolo Golinelli, Tommaso Faraci, Daniele Fontanelli
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《An Infrastructure-less, Control-Independent Solution to Relative Localisation of a Team of Mobile Robots using Ranging Measurements》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The ability to localise teams of robots is essential for applications ranging from robotic fleets in unstructured environments to cooperative control and navigation tasks. In such contexts, fixed infrastructure is often unavailable, deployments must be fast and flexible, and system requirements must be minimal. We present a decentralised cooperative localisation algorithm that addresses all these challenges at once. The method is anchor-less, fully decentralised, and, unlike most existing approaches, does not require controlling the robots motion to ensure team observability. It relies only on local odometry, sparse inter-agent ranging measurements, and short-range communication, all of which are widely available in practice. The algorithm adopts a multi-hypothesis Bayesian framework that maintains the entire set of feasible solutions, ensuring robustness under transient unobservable conditions. Moreover, through information sharing, each agent benefits from the estimates of the entire group, even in partially connected conditions.

</details>

---

### [[20_Research/Papers/具身智能/Towards_3D_karst_underwater_scene_reconstruction_from_rotating_sonar_data|Towards 3D karst underwater scene reconstruction from rotating sonar data]]

![[assets/2606.20322_figure.png|800]]

- **arXiv**: [2606.20322](https://arxiv.org/abs/2606.20322)
- **PDF**: https://arxiv.org/pdf/2606.20322
- **详细分析**: [[20_Research/Papers/具身智能/Towards_3D_karst_underwater_scene_reconstruction_from_rotating_sonar_data|Towards 3D karst underwater scene reconstruction from rotating sonar data]]
- **作者**: Georgios Evangelos Margaritis, Lionel Lapierre, Simon Rohou, Zhi Yan, Andreas Nüchter, François Goulette
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《Towards 3D karst underwater scene reconstruction from rotating sonar data》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Karst aquifers provide critical freshwater resources but pose significant hazards due to their complex and poorly understood subsurface geometry. Mapping these environments is challenging because sonar data from underwater exploration is sparse and noisy, while navigation estimates suffer from drift limiting standard 3D reconstruction methods. We present a pipeline for reconstructing underwater karst conduits from a sonar profiler. We combine a continuous-time SLAM approach to correct trajectory drift with a novel two-stage deep learning method for surface reconstruction, producing an immersive and navigable 3D mesh for hydrogeological analysis.

</details>

---

### [[20_Research/Papers/具身智能/Co-VLA_Coordination-Aware_Structured_Action_Modeling_for_Dual-Arm_Vision-Language-Action_Systems|Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems]]

![[assets/2606.20285_figure.png|800]]

- **arXiv**: [2606.20285](https://arxiv.org/abs/2606.20285)
- **PDF**: https://arxiv.org/pdf/2606.20285
- **详细分析**: [[20_Research/Papers/具身智能/Co-VLA_Coordination-Aware_Structured_Action_Modeling_for_Dual-Arm_Vision-Language-Action_Systems|Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems]]
- **作者**: Yandong Wang, Jiaqian Yu, Xiongfeng Peng, Lu Xu, Yamin Mao, Weiming Li, Jaewook Yoo, Dongwook Lee, Daehyun Ji, Mingbo Zhao, Chao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Co-VLA: Coordination-Aware Structured Action Modeling for Dual-Arm Vision-Language-Action Systems》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Co-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models show strong capabilities in single and dual-arm robotic manipulation. Prior works show coordinated bimanual behaviors can emerge from end-to-end learning, leveraging large vision-language backbones with continuous action prediction. However, as bimanual tasks become tightly coupled and execution constraints become critical, implicit coordination alone is insufficient to ensure reliable, interpretable, and stable behavior. In this work, we propose Co-VLA, a coordination-aware bimanual manipulation framework introducing explicit structural priors into VLA models. We instantiate our method on a state-of-the-art vision-language backbone by replacing its monolithic action head with a Structured Action Expert (SAE) designed for bimanual coordination. Specifically, we introduce explicit structure at the action generation level with a modular coordination-aware loss that shapes shared and residual latents according to task-specific structures. The shared latent encodes task-level coordination intent, while residual latents capture execution adjustments for each arm. At deployment, a Latent-Aware Controller (LAC) interprets the learned representations to modulate synchronization strength, execution asymmetry, smoothness, and safety constraints in real time. LAC operates at the joint-command level and remains compatible with standard control pipelines without requiring force or impedance control. Experiments across simulation and real-world benchmarks show Co-VLA significantly outperforms monolithic baselines, achieving a 27% success rate gain in tight-coordination tasks, more than doubling performance in OOD real-world scenarios (from 13% to 27%), and reducing task completion time by up to 25%.

</details>

---

### [[20_Research/Papers/强化学习/Stable_Transformer-Actor-Critic_Model_Predictive_Control_A_Contraction_Analysis_Approach|Stable Transformer-Actor-Critic Model Predictive Control: A Contraction Analysis Approach]]

![[assets/2606.20197_first_page.png|800]]

- **arXiv**: [2606.20197](https://arxiv.org/abs/2606.20197)
- **PDF**: https://arxiv.org/pdf/2606.20197
- **详细分析**: [[20_Research/Papers/强化学习/Stable_Transformer-Actor-Critic_Model_Predictive_Control_A_Contraction_Analysis_Approach|Stable Transformer-Actor-Critic Model Predictive Control: A Contraction Analysis Approach]]
- **作者**: Antonio Marino, Valerio Modugno, Marco Cognetti
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《Stable Transformer-Actor-Critic Model Predictive Control: A Contraction Analysis Approach》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actor-Critic Model Predictive Control (MPC) effectively addresses complex, non-convex control problems, but guaranteeing the closed-loop stability of sequence-based learning models within these pipelines remains challenging. This paper introduces a novel Transformer-Actor-Critic MPC architecture with formal robustness guarantees. First, we prove that Transformer networks can satisfy global incremental Input-to-State Stability ($δ$ISS). We then leverage Riemannian contraction theory to analyze the interconnected dynamics between the physical plant and the predictive neural network. Finally, we integrate these theoretical bounds as a training regularizer to yield a certifiably robust policy. The framework is validated on a nonlinear 3D drone model executing target-reaching and obstacle-avoidance maneuvers.

</details>

---

### [[20_Research/Papers/机器人/Belt-Finger_An_Affordable_Soft_Belt-Driven_Gripper_for_Dexterous_In-Hand_Manipulation|Belt-Finger: An Affordable Soft Belt-Driven Gripper for Dexterous In-Hand Manipulation]]

![[assets/2606.20193_figure.png|800]]

- **arXiv**: [2606.20193](https://arxiv.org/abs/2606.20193)
- **PDF**: https://arxiv.org/pdf/2606.20193
- **详细分析**: [[20_Research/Papers/机器人/Belt-Finger_An_Affordable_Soft_Belt-Driven_Gripper_for_Dexterous_In-Hand_Manipulation|Belt-Finger: An Affordable Soft Belt-Driven Gripper for Dexterous In-Hand Manipulation]]
- **作者**: Boya Zhang, Andreas Zell, Georg Martius
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Belt-Finger: An Affordable Soft Belt-Driven Gripper for Dexterous In-Hand Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Parallel-jaw grippers are the default manipulator choice in robotics because they are simple, robust, and inexpensive. Their limited in-hand mobility, however, often forces large arm motions and restricts dexterous manipulation in confined workspaces. We present a parallel-gripper upgrade: a double-soft-belt-based finger module that preserves standard opening/closing while adding three in-hand degrees of freedom (DoF): translation, pitch, and roll. The mechanism is deliberately kept simple and engineered for inexpensive manufacturing and straightforward integration, preserving the reliability and precise control of traditional parallel grippers while greatly broadening the range of manipulation capabilities. To demonstrate the utility of the added DoFs, we integrate the gripper in two control pipelines. First, we adapt a model predictive controller for in-hand manipulation of known objects. Second, we introduce a lightweight teleoperation interface that enables simultaneous control of the robot arm and gripper (10 DoFs total) with minimal hardware. Across a suite of challenging manipulation tasks executed via teleoperation, MPC, and trained policies, the proposed gripper consistently improves dexterity and task feasibility compared to a conventional parallel gripper

</details>

---

### [[20_Research/Papers/机器人/Robust_Assembly_State_Reasoning_from_Action_Recognition_for_Human-Robot_Collaboration|Robust Assembly State Reasoning from Action Recognition for Human-Robot Collaboration]]

![[assets/2606.20150_figure.png|800]]

- **arXiv**: [2606.20150](https://arxiv.org/abs/2606.20150)
- **PDF**: https://arxiv.org/pdf/2606.20150
- **详细分析**: [[20_Research/Papers/机器人/Robust_Assembly_State_Reasoning_from_Action_Recognition_for_Human-Robot_Collaboration|Robust Assembly State Reasoning from Action Recognition for Human-Robot Collaboration]]
- **作者**: James Fant-Male, Roel Pieters
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Robust Assembly State Reasoning from Action Recognition for Human-Robot Collaboration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet, SMIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human Action Recognition (HAR) is frequently investigated in Human-Robot Collaboration (HRC) research to understand what actions have been performed and hence the state of a collaborative task. Accurately tracking an assembly state from HAR is however not fully investigated, and in realistic scenarios is not a trivial task. This research systematically investigates and compares methods for tracking assembly state using action recognition inputs. Investigations using two diverse datasets and five state tracking approaches, including logic-based, Hidden Markov Model (HMM), and neural network (NN) methods, show that optimal approaches are not uniform across different tasks and that different methods fail under different circumstances. Testing is performed using both simulated inputs with varying noise levels and realistic inputs from a HAR model. Results show NN and HMM methods can perform well in tasks with limited variability, but for other scenarios logic-based approaches can be more robust. Methods which model expected action duration are also important for tasks with repeated actions where no additional sensing is provided.

</details>

---

### [[20_Research/Papers/具身智能/Evaluation_of_Augmented_Reality-based_Intuitive_Interface_for_Robot-Assisted_Transesophageal_Echocardiography_A_User_Study|Evaluation of Augmented Reality-based Intuitive Interface for Robot-Assisted Transesophageal Echocardiography: A User Study]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2606.19971](https://arxiv.org/abs/2606.19971)
- **PDF**: https://arxiv.org/pdf/2606.19971
- **详细分析**: [[20_Research/Papers/具身智能/Evaluation_of_Augmented_Reality-based_Intuitive_Interface_for_Robot-Assisted_Transesophageal_Echocardiography_A_User_Study|Evaluation of Augmented Reality-based Intuitive Interface for Robot-Assisted Transesophageal Echocardiography: A User Study]]
- **作者**: Xiu Zhang*, Matteo Di Mauro*, Sofia Breschi, Angela Peloso, Emiliano Votta, Arianna Menciassi, Elena De Momi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Evaluation of Augmented Reality-based Intuitive Interface for Robot-Assisted Transesophageal Echocardiography: A User Study》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

TransEsophageal Echocardiography (TEE) is essential for diagnosing and guiding Structural Heart Disease (SHD) interventions. However, manual TEE manipulation demands significant operator expertise, is physically demanding, and exposes clinicians to radiation when performed alongside fluoroscopy. Robotic-assisted TEE systems have been introduced to improve probe handling and reduce operator fatigue, yet the design of intuitive and effective user interfaces remains an open challenge. This study presents and evaluates a model-enhanced, Augmented Reality (AR)-based intuitive interface for robot-assisted TEE, designed to improve spatial awareness and control intuitiveness. A robotic TEE platform integrated with electromagnetic tracking and a virtual simulator was used to compare three user interfaces differing in visualization and interaction modalities: 2D jointlevel (2D-JI), 3D joint-level (3D-JI), and 3D tip-level (3D-TI). Thirty six participants performed standardized navigation tasks to reproduce target echocardiographic views, with performance assessed via position and orientation errors, completion time, and NASA-TLX workload scores. Results show that 3D visualization significantly improved spatial accuracy, reducing median position error from 13 mm to 3 mm and halving the orientation error compared with the 2D interface. Tip-level interaction yielded a further 50% reduction in orientation error and reduced interuser variability relative to joint-level control. Overall, the 3D-TI configuration, combining immersive visualization with direct tip-level control, proved the most effective and ergonomic interface, supporting the integration of AR-based visualization and intuitive control paradigms into next-generation robotic TEE systems to enhance operator performance and procedural safety.

</details>

---

### [[20_Research/Papers/机器人/Motor_Angular_Speed_Preintegration_for_Multirotor_UAV_State_Estimation|Motor Angular Speed Preintegration for Multirotor UAV State Estimation]]

![[assets/2606.19929_first_page.png|800]]

- **arXiv**: [2606.19929](https://arxiv.org/abs/2606.19929)
- **PDF**: https://arxiv.org/pdf/2606.19929
- **详细分析**: [[20_Research/Papers/机器人/Motor_Angular_Speed_Preintegration_for_Multirotor_UAV_State_Estimation|Motor Angular Speed Preintegration for Multirotor UAV State Estimation]]
- **作者**: Matěj Petrlík, Filip Novák, Robert Pěnička, Martin Saska
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Motor Angular Speed Preintegration for Multirotor UAV State Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A precise state estimate is crucial for a tight feedback control that enables agile and near-obstacle flights of UAVs. The state-of-the-art methods fuse slow pose measurements with high-frequency inertial measurements to obtain a precise state estimate. However, the inertial measurements from the IMU onboard the UAV are degraded by vibrations from spinning propellers and the precision of the estimated state suffers. We propose a novel approach based on the preintegration of accelerations obtained from motor speeds. We show that the accelerations obtained in this manner can be used for state propagation on their own to achieve better precision without including the IMU. Further, we propose a factor composed of the preintegrated motor speeds that can be directly employed in factor graph optimization frameworks. We combine our factor with LiDAR measurements into the proposed Motor Angular Speed LiDAR Odometry (MAS-LO) algorithm for precise state estimation, which we open-source. Lastly, we evaluate the estimation precision against a state-of-the-art inertial algorithm LIO-SAM to show 28% improvement in position and 65% in velocity estimation accuracy, 14% lower measurement lag, and high robustness to wrong parameter values.

</details>

---

### [[20_Research/Papers/具身智能/SWAP_Symmetric_Equivariant_World-Model_for_Agile_Robot_Parkour|SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour]]

![[assets/2606.19928_figure.png|800]]

- **arXiv**: [2606.19928](https://arxiv.org/abs/2606.19928)
- **PDF**: https://arxiv.org/pdf/2606.19928
- **详细分析**: [[20_Research/Papers/具身智能/SWAP_Symmetric_Equivariant_World-Model_for_Agile_Robot_Parkour|SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour]]
- **作者**: Kaixin Lan, Ze Wang, Hongyi Li, Lei Jiang, Chaojie Fu, Chengkai Su, Choi Lam Wong, Yongbin Jin, Hongtao Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 强化学习
- **相关性评分**: 2.8（加权：具身智能 0.9，强化学习 0.2，世界模型 0.4，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MFRL, PlaNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns. This inflates the learning burden and hinders the capture of geometric regularities, restricting the latent space's efficiency for downstream policies. To address this, we propose SWAP, an end-to-end equivariant symmetric world model. This framework embeds symmetry directly into both the world model and the actor-critic networks. In real-world tests, the robot leaps across a 2.13 m gap and climbs a 1.63 m platform, breaking records for quadruped parkour. Furthermore, the framework exhibits robust geometric generalization to unseen mirrored terrains and exceptional zero-shot transferability across diverse outdoor environments. These results demonstrate that symmetry equivariance is an effective structural prior for pushing the physical boundaries of learned legged locomotion.

</details>

---

### [[20_Research/Papers/大模型/One-to-Two_Acting_A_Novel_Framework_for_Single-arm_Agent_Action_Expansion_to_Dual_Arms|One-to-Two Acting: A Novel Framework for Single-arm Agent Action Expansion to Dual Arms]]

![[assets/2606.19897_figure.png|800]]

- **arXiv**: [2606.19897](https://arxiv.org/abs/2606.19897)
- **PDF**: https://arxiv.org/pdf/2606.19897
- **详细分析**: [[20_Research/Papers/大模型/One-to-Two_Acting_A_Novel_Framework_for_Single-arm_Agent_Action_Expansion_to_Dual_Arms|One-to-Two Acting: A Novel Framework for Single-arm Agent Action Expansion to Dual Arms]]
- **作者**: Youbin Yao, Nieqin Cao, Mingyan Li, Yan Ding, Fuqiang Gu, Chao Chen
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《One-to-Two Acting: A Novel Framework for Single-arm Agent Action Expansion to Dual Arms》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dual-arm manipulation can improve throughput via parallel execution, but collecting bimanual demonstrations for training is costly and difficult. We present ExS2D, a hierarchical action expansion framework that enables dual-arm manipulation from single-arm supervision. ExS2D first generates structured subtasks from textual instructions while explicitly capturing temporal precedence. It then grounds each subtask into executable actions through subtask-guided action mapping in observation. Finally, precedence-aware action allocation and synchronized planning are performed by a multimodal large language model driven coordinator to select collision-free dual-arm executions. Simulation experiments demonstrate that ExS2D reduces the average execution steps by 54.4% while maintaining a comparable success rate to a single-arm baseline. Real-robot experiments on four tasks further demonstrate the reliability of ExS2D for dual-arm execution under few-shot single-arm samples, while using zero bimanual demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/EquiVLA_A_General_Framework_for_Rotationally_Equivariant_Vision-Language-Action_Models|EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models]]

![[assets/2606.19784_figure.png|800]]

- **arXiv**: [2606.19784](https://arxiv.org/abs/2606.19784)
- **PDF**: https://arxiv.org/pdf/2606.19784
- **详细分析**: [[20_Research/Papers/具身智能/EquiVLA_A_General_Framework_for_Rotationally_Equivariant_Vision-Language-Action_Models|EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models]]
- **作者**: Thien-Loc Ha, Quang-Tan Nguyen, Trong-Bao Ho, Long Dinh, Minh Duc Nguyen, Gia-Binh Nguyen, Pham Tri Quang, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《EquiVLA: A General Framework for Rotationally Equivariant Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EquiVLA, RLBench, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for generalist robot manipulation, yet they lack geometric inductive biases: policies trained at specific orientations require substantially more data to generalize across rotational configurations. We present \textsc{EquiVLA}, the first general framework for end-to-end $\mathrm{SO}(2)$-equivariant VLA models, applicable to any architecture coupling a frozen vision-language backbone with a flow-matching Diffusion Transformer action head. \textsc{EquiVLA} introduces \textsc{EquiPerceptor}, which produces approximately $\mathrm{SO}(2)$-equivariant visual representations from frozen ViT features; and \textsc{EquiActor}, an exactly $\mathrm{SO}(2)$-equivariant flow-matching Diffusion Transformer action head. Together, they establish an approximate $\mathrm{SO}(2)$ equivariance chain from camera observations to predicted action sequences. Instantiated on GR00T~N1.5 and evaluated across four LIBERO suites, CALVIN ABCD$\to$D, and five real-robot tasks on Mobile ALOHA, \textsc{EquiVLA} achieves $92.6\%$ average success on LIBERO (vs. $78.1\%$ baseline), an average sequence length of $4.03$ on CALVIN (vs. $3.45$), and improves real-robot success from $54\%$ to $72\%$.

</details>

---

### [[20_Research/Papers/强化学习/Start_Right,_Arrive_Right_Asynchronous_Execution_via_Initial_Noise_Selection|Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection]]

![[assets/2606.19774_figure.png|800]]

- **arXiv**: [2606.19774](https://arxiv.org/abs/2606.19774)
- **PDF**: https://arxiv.org/pdf/2606.19774
- **详细分析**: [[20_Research/Papers/强化学习/Start_Right,_Arrive_Right_Asynchronous_Execution_via_Initial_Noise_Selection|Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection]]
- **作者**: Trong-Bao Ho, Quang-Tan Nguyen, Thien-Loc Ha, Gia-Binh Nguyen, Viet-Thanh Nguyen, Long Dinh, Minh N. Vu, Duy M. H. Nguyen, An Thai Le, Ngo Anh Vien
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Start Right, Arrive Right: Asynchronous Execution via Initial Noise Selection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action chunking enables robot policies to produce temporally coherent behavior, but generating multi-step action sequences with flow-based policies incurs latency that is incompatible with real-time control. Under asynchronous execution, the robot continues executing the current chunk while the next one is generated, causing even minor delays to create inconsistencies at chunk boundaries. Existing methods address this problem by steering generation toward the already executed action prefix. We instead show that prefix consistency can be achieved by selecting an appropriate initial noise before generation begins, allowing the unmodified flow ODE to produce a coherent next chunk. This reframes asynchronous inference as a noise selection problem rather than a trajectory steering problem. We introduce \textbf{PAINT}, a training-free method that finds this noise via backward Euler inversion and constructs the final chunk through a repainting rule. In summary, \texttt{PAINT} requires no gradients, retraining, or policy modification; yet it improves execution consistency and task performance across \textit{12 simulated benchmarks} and \textit{6 real-world manipulation tasks} spanning single-arm, bimanual, and humanoid embodiments. Website: ~\href{https://paint-action-chunking.github.io}{\texttt{https://paint-action-chunking.github.io}}.

</details>

---

### [[20_Research/Papers/机器人/ForEnt_A_Multi-Modal_Dataset_for_Characterizing_Quadruped_Robot_Entrapments_in_Forest_Environments|ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments]]

![[assets/2606.19675_figure.jpg|800]]

- **arXiv**: [2606.19675](https://arxiv.org/abs/2606.19675)
- **PDF**: https://arxiv.org/pdf/2606.19675
- **详细分析**: [[20_Research/Papers/机器人/ForEnt_A_Multi-Modal_Dataset_for_Characterizing_Quadruped_Robot_Entrapments_in_Forest_Environments|ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments]]
- **作者**: Natapat Kirdwichai, Danesh Tarapore
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots are increasingly deployed in forests for ecological surveying and monitoring, yet their autonomy is often interrupted consequent to the challenges posed in traversing forest environments. Forest entrapments, for example, when a robot's legs are ensnared in vines or other vegetation, result in loss of stability and toppling. Such events not only disrupt the mission and require manual intervention, but also risk damage to the robot hardware. To address the absence of a dedicated dataset to investigate these failure modes in forest environments, we present ForEnt, a multi-modal dataset collected with the low-cost Unitree Go2 quadruped across eight forest sites in the Southampton Common Woodlands, UK. For our dataset, over approximately 1.7 km of traversals in 11 sequences were conducted, yielding 69 recorded entrapment events. ForEnt includes time-synchronized RGB-D images, LiDAR scans, proprioceptive data, and third-person video, enabling analysis of terrain factors contributing to entrapment and providing labeled sensor streams for reproducible benchmarking. By supporting the evaluation of entrapment detection strategies, ForEnt lowers the barrier to developing robust quadruped robot deployments in challenging forest environments.

</details>

---

### [[20_Research/Papers/具身智能/Fail-RAG_A_Retrieval_Augmented_Generation_Informed_Framework_for_Robot_Failure_Identification|Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification]]

![[assets/2606.19598_figure.jpg|800]]

- **arXiv**: [2606.19598](https://arxiv.org/abs/2606.19598)
- **PDF**: https://arxiv.org/pdf/2606.19598
- **详细分析**: [[20_Research/Papers/具身智能/Fail-RAG_A_Retrieval_Augmented_Generation_Informed_Framework_for_Robot_Failure_Identification|Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification]]
- **作者**: Ameya Salvi, Jie Hu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.6，大模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Fail-RAG : A Retrieval Augmented Generation Informed Framework for Robot Failure Identification》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industry automation is witnessing an evolution in robotics driven by both technological breakthroughs and societal changes: progress towards generalist robots, embodied and physical artificial intelligence (AI), and increasing labor shortage in manufacturing.An intelligent autonomous robot needs to not only act according to planned motions but also react to any unexpected events. In this study, we focus on such unexpected events in warehouses where robots are used for material handling. Specifically, we refer to any unexpected events as failures and develop methods to detect robot operations related failures. Rule-based detection methods may break since the form of failures could change due to the dynamic nature of both environments and tasks. We propose 'Fail-RAG', a Retrieval Augmented Generation (RAG)-based failure detection framework where failure images and context information are embedded and queried against a failure database by calculating their similarities. Vision-Language Models (VLMs) are further used to analyze failures and provide details by following our instruction template. We evaluated the performance of Fail-RAG by conducting both simulation and physical experiments using fixed robot arms and a mobile manipulator for multiple tasks that are common in warehouse automation. Fail-RAG achieved 25 percentage point higher failure detection accuracy on average across five types of robot operations compared to using off-the-shelf VLMs, indicating its effectiveness for real-world failure detection.

</details>

---

### [[20_Research/Papers/具身智能/Safe,_Real-Time_Active_Model_Discrimination_and_Fault_Diagnosis_for_Nonlinear_Systems_via_Differentiable_Reachability|Safe, Real-Time Active Model Discrimination and Fault Diagnosis for Nonlinear Systems via Differentiable Reachability]]

![[assets/2606.19590_figure.png|800]]

- **arXiv**: [2606.19590](https://arxiv.org/abs/2606.19590)
- **PDF**: https://arxiv.org/pdf/2606.19590
- **详细分析**: [[20_Research/Papers/具身智能/Safe,_Real-Time_Active_Model_Discrimination_and_Fault_Diagnosis_for_Nonlinear_Systems_via_Differentiable_Reachability|Safe, Real-Time Active Model Discrimination and Fault Diagnosis for Nonlinear Systems via Differentiable Reachability]]
- **作者**: Xinpei Ni, Melkior Ornik, Glen Chou, Samuel Coogan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.2（加权：具身智能 0.3，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Safe, Real-Time Active Model Discrimination and Fault Diagnosis for Nonlinear Systems via Differentiable Reachability》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a safe, real-time algorithm for active fault diagnosis and model discrimination for uncertain continuous-time nonlinear systems with process and measurement disturbances. Given a finite set of candidate models representing nominal and faulty modes, including actuator and sensor faults, we formulate an output-feedback, time-varying policy optimization problem that (i) robustly enforces state-input safety constraints over a finite horizon and (ii) drives the system to produce sampled measurements consistent with at most one model, enabling deterministic diagnosis. To solve this problem in real time, we develop a tractable approximation using interval over-approximations of reachable state and output sets, and encode diagnosability via a differentiable objective that penalizes overlap between the reachable output sets of possible models. The resulting optimization is solved efficiently online with gradient-based methods using JAX and differentiable reachability primitives. We evaluate our method on sensor and actuator fault diagnosis (up to 11 fault modes) in several high-dimensional nonlinear robotic systems, including a simulated quadrotor and fighter-jet model, a hardware differential-drive robot, and quadrupedal navigation. Across these case studies, our approach achieves reliable model discrimination in under 50 ms, outperforming baselines in discrimination success rate and speed while providing formal safety guarantees.

</details>

---

### [[20_Research/Papers/机器人/One_Demo_is_Worth_a_Thousand_Trajectories_Action-View_Augmentation_for_Visuomotor_Policies|One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies]]

![[assets/2606.19586_figure.png|800]]

- **arXiv**: [2606.19586](https://arxiv.org/abs/2606.19586)
- **PDF**: https://arxiv.org/pdf/2606.19586
- **详细分析**: [[20_Research/Papers/机器人/One_Demo_is_Worth_a_Thousand_Trajectories_Action-View_Augmentation_for_Visuomotor_Policies|One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies]]
- **作者**: Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies for manipulation have demonstrated remarkable potential in modeling complex robotic behaviors, yet minor alterations in the robot's initial configuration and unseen obstacles easily lead to out-of-distribution observations. Without extensive data collection effort, these result in catastrophic execution failures. In this work, we introduce an effective data augmentation framework that generates visually realistic fisheye image sequences and corresponding physically feasible action trajectories from real-world eye-in-hand demonstrations, captured with a portable parallel gripper with a single fisheye camera. We introduce a novel Gaussian Splatting formulation, adapted to wide FoV fisheye cameras, to reconstruct and edit the 3D scene with unseen objects. We utilize trajectory optimization to generate smooth, collision-free, view-rendering-friendly action trajectories and render visual observations from corresponding novel views. Comprehensive experiments in simulation and the real world show that our augmentation framework improves the success rate for various manipulation tasks in both the same scene and the augmented scene with obstacles requiring collision avoidance.

</details>

---

### [[20_Research/Papers/具身智能/SCAN-Planner_Spatial_Collision-Aware_Local_Planning_for_Route-Guided_Long-Range_Quadruped_Navigation|SCAN-Planner: Spatial Collision-Aware Local Planning for Route-Guided Long-Range Quadruped Navigation]]

![[assets/2606.19555_figure.jpg|800]]

- **arXiv**: [2606.19555](https://arxiv.org/abs/2606.19555)
- **PDF**: https://arxiv.org/pdf/2606.19555
- **详细分析**: [[20_Research/Papers/具身智能/SCAN-Planner_Spatial_Collision-Aware_Local_Planning_for_Route-Guided_Long-Range_Quadruped_Navigation|SCAN-Planner: Spatial Collision-Aware Local Planning for Route-Guided Long-Range Quadruped Navigation]]
- **作者**: Han Zheng, Zhe Chen, Yiwen Fu, Ming Yang, Tong Qin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SCAN-Planner: Spatial Collision-Aware Local Planning for Route-Guided Long-Range Quadruped Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots are increasingly expected to navigate through narrow passages, cluttered indoor scenes, and large-scale 3D unstructured environments. Existing local planners commonly approximate the robot using isotropic geometric inflation or rely on planar and elevation-map representations, leading to conservative motion in tight spaces and limited reasoning about overhanging structures. This letter presents SCAN-Planner, a spatial collision-aware local planning framework for long-range quadruped navigation. A yaw-aware twin-cylinder footprint is used to model the elongated robot body, enabling whole-body collision evaluation through sparse queries in an inflated 3D occupancy map. We further introduce a projected A* search that generates collision-free guidance on an interpolated ground-following surface, with z-gradient suppression to avoid obstacles horizontally while maintaining vertical stability. For large-scale deployment, a robot-centric sliding map with boundary fallback provides high-resolution local collision checking and recovery from local dead ends. Simulation and real-world experiments demonstrate that SCAN-Planner generates safe, smooth, and efficient trajectories in dense clutter, 3D unstructured scenes, stair traversal, and long-range navigation tasks.

</details>

---

### [[20_Research/Papers/机器人/Proprioceptive_Invariant_State_Estimation_for_Humanoid_Robots_on_Non-Inertial_Ground|Proprioceptive Invariant State Estimation for Humanoid Robots on Non-Inertial Ground]]

![[assets/2606.19512_figure.png|800]]

- **arXiv**: [2606.19512](https://arxiv.org/abs/2606.19512)
- **PDF**: https://arxiv.org/pdf/2606.19512
- **详细分析**: [[20_Research/Papers/机器人/Proprioceptive_Invariant_State_Estimation_for_Humanoid_Robots_on_Non-Inertial_Ground|Proprioceptive Invariant State Estimation for Humanoid Robots on Non-Inertial Ground]]
- **作者**: Falak Mandali, Zijian He, Yan Gu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Proprioceptive Invariant State Estimation for Humanoid Robots on Non-Inertial Ground》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an invariant extended Kalman filtering (InEKF) approach for real-time state estimation of humanoid robots operating on non-inertial ground using only onboard proprioceptive sensing. The proposed approach estimates the robot's base position and velocity relative to the moving ground frame without requiring direct measurements of ground motion or externally mounted sensors. By exploiting kinematic constraints at the stance foot through foot-mounted IMUs, the filter accounts for ground-induced nonlinearities in the process and measurement models while remaining fully proprioceptive. The estimator is formulated to admit a right-invariant measurement model, enabling favorable error dynamics under large initial uncertainties. Observability analysis establishes conditions under which the robot's relative base position and velocity are observable with respect to the non-inertial ground frame. Experiments with the Digit humanoid robot standing and squatting atop a swaying and pitching ground showcase a 96% speedup in convergence rate and an 80% reduction in position estimate errors over existing InEKFs. Walking experiments on a uni-axially rotating ground achieve an average estimation error of less than 9 cm for an initial error of up to 1 m.

</details>

---

### [[20_Research/Papers/具身智能/Simulating_Robotic_Locomotion_in_Sand_Resistive_Force_Theory_in_an_Open-Source_Physics_Engine|Simulating Robotic Locomotion in Sand: Resistive Force Theory in an Open-Source Physics Engine]]

![[assets/2606.19504_figure.png|800]]

- **arXiv**: [2606.19504](https://arxiv.org/abs/2606.19504)
- **PDF**: https://arxiv.org/pdf/2606.19504
- **详细分析**: [[20_Research/Papers/具身智能/Simulating_Robotic_Locomotion_in_Sand_Resistive_Force_Theory_in_an_Open-Source_Physics_Engine|Simulating Robotic Locomotion in Sand: Resistive Force Theory in an Open-Source Physics Engine]]
- **作者**: Ryan Walker Brown, Laura K. Treers, Kathryn A. Daltorio
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Simulating Robotic Locomotion in Sand: Resistive Force Theory in an Open-Source Physics Engine》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in Resistive Force Theory (RFT) enable approximation of ground reaction forces for locomotion in sand without the computational expense of modeling interactions with individual grains. However, these tools have been absent in 3D physics engines commonly used for robot simulation. We explore if resistive force approximations are sufficient, when integrated with standard dynamics calculations, to provide a stable substrate for a freely walking robot. To determine this, we implement 3D Granular Resistive Force Theory (3D RFT) in a physics simulation engine, MuJoCo. We verify simulations in multiple scenarios to demonstrate that key trends due to end effector shape, speed, and loading are preserved. Our implementation predicts walking distance and foot sinkage of a 12-Degree of Freedom hexapod robot within 20\% of experiments in sand. While RFT has inherent approximations, the open source tool described here has potential to help develop new and improved robot designs to traverse granular media substrates.

</details>

---

### [[20_Research/Papers/具身智能/DiffusionVS_A_Generative_Framework_for_Robust_Visual_Servoing_Based_on_Diffusion_Policy|DiffusionVS: A Generative Framework for Robust Visual Servoing Based on Diffusion Policy]]

![[assets/2606.19397_figure.png|800]]

- **arXiv**: [2606.19397](https://arxiv.org/abs/2606.19397)
- **PDF**: https://arxiv.org/pdf/2606.19397
- **详细分析**: [[20_Research/Papers/具身智能/DiffusionVS_A_Generative_Framework_for_Robust_Visual_Servoing_Based_on_Diffusion_Policy|DiffusionVS: A Generative Framework for Robust Visual Servoing Based on Diffusion Policy]]
- **作者**: Hongkang Cui, Rui He, Haoyao Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DiffusionVS: A Generative Framework for Robust Visual Servoing Based on Diffusion Policy》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual servoing is a fundamental technique in robotic manipulation and navigation. Regression-based visual servoing frequently experiences trajectory jitter as a result of noise-sensitive single-step mappings and the accumulation of errors during distribution shifts. In contrast, Diffusion Policy maintains temporal consistency by predicting action sequences and improves robustness through implicit data augmentation. This paper presents a novel diffusion-based servoing method. Based on Diffusion Policy, the proposed approach uses normalized image coordinates of observed tag corners as input and generates camera velocity through conditional denoising. To overcome the generalization limitations of models trained on static datasets, an online training paradigm is adopted, continuously expanding the diversity of training data through interactive experience collection. This strategy substantially enhances both the performance and generalization capability of the model. Comprehensive simulations and real-world experiments demonstrate the effectiveness of the proposed method, achieving success rates of nearly 100\% in simulation and 93\% in physical experiments. Beyond the specific pipeline, we further validate the generality of the diffusion mechanism. Experiments show that existing visual servoing networks consistently achieve improved performance when integrated with our diffusion-based module. These results indicate that the proposed strategy possesses broad applicability and can enhance various visual servoing systems beyond the specific architecture presented here.

</details>

---

### [[20_Research/Papers/具身智能/WorkBenchMark_A_LEGO-Based_Assembly_Benchmark_with_an_Assembly-by-Disassembly_Baseline_for_the_Smart_Manufacturing_League|WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League]]

![[assets/2606.19358_figure.png|800]]

- **arXiv**: [2606.19358](https://arxiv.org/abs/2606.19358)
- **PDF**: https://arxiv.org/pdf/2606.19358
- **详细分析**: [[20_Research/Papers/具身智能/WorkBenchMark_A_LEGO-Based_Assembly_Benchmark_with_an_Assembly-by-Disassembly_Baseline_for_the_Smart_Manufacturing_League|WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League]]
- **作者**: Wenbo Ma, Daniel Swoboda, Matteo Tschesche, Till Hofmann
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BlocksWorld, FurnitureBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduceWorkBenchMark, a LEGO Duplo-based robotic assembly benchmark motivated by the RoboCup Smart Manufacturing League. Robotic assembly couples low-level manipulation with task-level symbolic reasoning under physical constraints, a combination that current end-to-end learning methods do not yet solve reliably. The benchmark provides 400 tasks across four complexity tiers. We provide an open-vocabulary perception, Assembly-by-Disassembly baseline solution. Our planning-based pipeline outperforms a modern vision-language-action approach across all tiers. The benchmark, simulation environment, and baseline implementation will be released openly to support the broader robotic assembly community.

</details>

---
