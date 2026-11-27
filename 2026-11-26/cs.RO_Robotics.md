# cs.RO | Robotics | 2026-11-26

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/强化学习/DexLink_Synthesizing_Dexterous_Behaviors_from_Chained_Hand-object_Poses|DexLink: Synthesizing Dexterous Behaviors from Chained Hand-object Poses]]

![[assets/2611.34936_figure.png|800]]

- **arXiv**: [2611.34936](https://arxiv.org/abs/2611.34936)
- **PDF**: https://arxiv.org/pdf/2611.34936
- **详细分析**: [[20_Research/Papers/强化学习/DexLink_Synthesizing_Dexterous_Behaviors_from_Chained_Hand-object_Poses|DexLink: Synthesizing Dexterous Behaviors from Chained Hand-object Poses]]
- **作者**: Meenal Parakh, Deep Patel, Beining Han, Jia Deng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexLink: Synthesizing Dexterous Behaviors from Chained Hand-object Poses》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synthesizing diverse dexterous manipulation policies is challenging: existing simulation-based approaches rely on human demonstrations which are difficult to scale, or use generic reward functions, which provide limited control over the hand-object interactions. We propose DexLink, which addresses these limitations by synthesizing diverse dexterous behaviors from sparse, reusable hand-object interaction templates. Given key task waypoints, DexLink retargets static interaction templates to target objects using an optimization that preserves spatial hand-object relationships. It then links the retargeted poses into an approximate reference trajectory and uses residual reinforcement learning to refine this reference into a closed-loop policy in simulation. Experiments spanning single-hand, bimanual, articulated, and dynamic tasks demonstrate that DexLink provides fine-grained control over task timing, grasp types, and high-level execution. The modular interaction templates transfer reliably across object scales, instances, and categories; without object-specific human demonstrations, the framework also matches the performance of dense reference-tracking methods. Finally, zero-shot deployment of policies trained purely in simulation shows promise for the simulation-based framework.

</details>

---

### [[20_Research/Papers/具身智能/MERLoc_Robust_Robot_Localization_in_Dynamic_Environments_with_Pose-Based_Retrieval_over_3D_Gaussian_Splatting_References|MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References]]

![[assets/2611.34932_figure.png|800]]

- **arXiv**: [2611.34932](https://arxiv.org/abs/2611.34932)
- **PDF**: https://arxiv.org/pdf/2611.34932
- **详细分析**: [[20_Research/Papers/具身智能/MERLoc_Robust_Robot_Localization_in_Dynamic_Environments_with_Pose-Based_Retrieval_over_3D_Gaussian_Splatting_References|MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References]]
- **作者**: Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in previously mapped spaces must localize accurately despite moving people and rearranged objects. Most localization pipelines match the query against a sparse set of captured reference images retrieved by appearance, which is brittle under scene change and repeating structures. We present MERLoc, which turns a single metric 3D Gaussian Splatting scan into a dense Functional Reference Memory. Reference views are sampled over the navigable space for the robot's morphology and sensors at a target density and rendered offline. Pre-encoding them for the chosen off-the-shelf localizer removes the reference encoder from inference. A pose-based retrieval strategy then selects references by spatial proximity and viewing direction rather than appearance, sidestepping visual ambiguities whenever a prior exists. Across one classical and four learned localizers in simulated and real dynamic scenes, pose-based retrieval matches or outperforms appearance retrieval in most cases, even when the latter is gated by the same prior. On real data, it lowers position RMSE by 15-60 % in nine of ten backend/split combinations, and the rendered memory outperforms real-image caches posed by Structure-from-Motion. The system runs onboard a Jetson Orin NX at 5 Hz, enabling a navigation policy to successfully traverse a hallway with people roaming and rearranging objects.

</details>

---

### [[20_Research/Papers/具身智能/One_Ocean,_Many_Tasks_A_Data-Grounded_Simulation_Suite_and_Benchmark_for_Marine_Robotics|One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics]]

![[assets/2611.34925_figure.png|800]]

- **arXiv**: [2611.34925](https://arxiv.org/abs/2611.34925)
- **PDF**: https://arxiv.org/pdf/2611.34925
- **详细分析**: [[20_Research/Papers/具身智能/One_Ocean,_Many_Tasks_A_Data-Grounded_Simulation_Suite_and_Benchmark_for_Marine_Robotics|One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics]]
- **作者**: Shuaijun Liu, Qifu Wen, Xingwei Chen, Xinwen Hu, Feiyang You, Sijia Chen, Ningxin Su
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL, MarineGym, OCPNet, OceanGym, OceanSim, UWSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation is essential for marine robotics, yet existing platforms often trade off between visually realistic worlds, high-throughput experimentation, and ocean-condition realism grounded in real data. We present OneOcean, a data-grounded simulation suite and benchmark built around a unified spatiotemporal ocean-environment product that harmonizes bathymetry with data-driven currents and tides, with optional pollution fields for cleanup-related evaluation. On top of this environment representation, OneOcean defines a task ladder spanning navigation and station-keeping under currents, waypoint and route following, depth-profile tracking, area scanning, pipeline inspection, and multi-agent coordination, including formation transit, fish protection and patrol (herding), and surface pollution localization, containment, and cleanup. The suite supports multi-agent settings with 2-10 vehicles. Our simulator supports three to six Degrees of Freedom (DoF) and produces standardized metrics and reproducible run manifests, enabling consistent aggregation across tasks, difficulties, and scaling settings. Experiments across dataset variants and scenes systematically stress planning and control under data-grounded disturbances and reveal trade-offs among heuristic baselines, Behavior Cloning (BC), and a Large Language Model (LLM)-based planner.

</details>

---

### [[20_Research/Papers/具身智能/Toward_Agentic_Robotics_A_Large-Scale_Study_of_Harness_Design_for_Robot-Use_Agents|Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents]]

![[assets/2611.34778_figure.png|800]]

- **arXiv**: [2611.34778](https://arxiv.org/abs/2611.34778)
- **PDF**: https://arxiv.org/pdf/2611.34778
- **详细分析**: [[20_Research/Papers/具身智能/Toward_Agentic_Robotics_A_Large-Scale_Study_of_Harness_Design_for_Robot-Use_Agents|Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents]]
- **作者**: Yuxiang Lai, Jike Zhong, Yu-Jhe Li, Lan Wang, Chengzhi Liu, Youbao Tang, Ming Li, Xi Xiao, Xiaofeng Yang, Liang Zhao, Zheda Mai, Ruixi Fan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.1（加权：具身智能 0.9，大模型 0.5，机器人 1.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MME-VLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent vision-language models (VLMs) can act as robot-use agents that understand diverse scenes and control robots through policy code and tools. However, they predict 3D gripper poses poorly even with extended reasoning, struggling with precise manipulation. Vision-language-action (VLA) and world-action (WAM) models are the opposite: they execute fast, smooth control on trained tasks, yet fail under domain shifts or when tasks require long-horizon memory and reasoning. Agentic robots therefore combine VLM reasoning and perception with precise VLA/WAM control through a policy harness. Yet harness design spans thousands of configurations, shifting success by tens of points with the same models. Moreover, testing even one design takes thousands of rollouts at high API and GPU cost, so prior works often commit to a single design chosen from few alternatives. To guide harness design, we evaluate over 470,000 rollouts across eight simulation benchmarks, six VLMs, and 15 VLA/WAM checkpoints. Seven controlled studies show effective harnesses must adapt to both VLM and VLA/WAM capabilities. Our findings specify what structure the VLM's policy code needs, where VLA manipulation needs help from tools and policy code, and when to involve the VLM at test time. The reference recipe X-Harness shows that these findings compose without weight updates, lifting base policies up to $+42.8$ points across memory, reasoning, and domain shifts.

</details>

---

### [[20_Research/Papers/具身智能/Anytime-Valid_Sequential_Verification_for_Sensing-Efficient_Robot_Navigation_under_Perception_Uncertainty|Anytime-Valid Sequential Verification for Sensing-Efficient Robot Navigation under Perception Uncertainty]]

![[assets/2611.34764_figure.png|800]]

- **arXiv**: [2611.34764](https://arxiv.org/abs/2611.34764)
- **PDF**: https://arxiv.org/pdf/2611.34764
- **详细分析**: [[20_Research/Papers/具身智能/Anytime-Valid_Sequential_Verification_for_Sensing-Efficient_Robot_Navigation_under_Perception_Uncertainty|Anytime-Valid Sequential Verification for Sensing-Efficient Robot Navigation under Perception Uncertainty]]
- **作者**: Saad Korchi, Abderrahim Waga
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Anytime-Valid Sequential Verification for Sensing-Efficient Robot Navigation under Perception Uncertainty》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a robot navigates an unfamiliar grid, noisy sensor readings can make it hard to tell whether the cells along its next move are free. Additional scans can reduce that uncertainty, but a fixed scan count spends the same sensing effort at every position. In a static-grid simulation, a sequential rule uses a Gaussian likelihood ratio to determine when the cells newly covered by the robot's footprint have enough evidence of free space. On 324 held-out scenarios from 18 public maps, the sequential gate and a four-scan reference chosen on validation data both completed every mission without an observed collision. With their respective validation-selected routing weights, the gate averaged 123.15 scans per episode versus 224.13 for the reference, a reduction of 45.05% (95% map-stratified bootstrap interval: 42.21--48.95%). In a retrospective check on the same scenarios with routing weights held equal, the reductions were 43.91% and 43.37% at the two tested weights, with all missions completed. On 216 scenarios from 12 previously unused maps, allocating more of the same certification error budget near the initial start--goal rectangle cut the sequential gate's scan count by a further 11.58%. The spatial variant completed 206 missions versus 208 for the original gate and increased computation time. The collision bound depends on the assumed observation model and footprint geometry. In a stress test with persistent per-cell bias, the original gate completed 0 of 54 missions.

</details>

---

### [[20_Research/Papers/具身智能/ELMO_Emergent_Representations_In_Imitation_Learning_Via_Dynamic_Hierarchical_Action_Chunking|ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking]]

![[assets/2611.34741_figure.png|800]]

- **arXiv**: [2611.34741](https://arxiv.org/abs/2611.34741)
- **PDF**: https://arxiv.org/pdf/2611.34741
- **详细分析**: [[20_Research/Papers/具身智能/ELMO_Emergent_Representations_In_Imitation_Learning_Via_Dynamic_Hierarchical_Action_Chunking|ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking]]
- **作者**: Jasper Gerigk, Yang Xu, Nicholas Rhinehart, Igor Gilitschenski
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：H-Net, Real-World, SA-VLA, SmolVLA, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot trajectories naturally decompose into variable-length phases with distinct semantic intents, such as reaching, grasping, and lifting. However, training policies to minimize MSE treats all actions as equal, obscuring their semantic structure. While latent action models attempt to create a structured prediction target by compressing action chunks into latent representations, existing approaches rely on two-stage training and context-blind decoders. Consequently, their representations are context-agnostic motion codes (e.g., "move down") which fail to capture behavioural intent (e.g., "pick up the block"). To overcome these bottlenecks, we introduce the Emergent Latent-action MOdel (ELMO), an end-to-end framework that encodes robot trajectories as grounded semantic codes -- representations that ground task-level behavioural intent in the current environment. ELMO jointly trains a VLA planner and an observation-conditioned decoder over dynamically chunked trajectories, learning a semantically grounded action space without separate pretraining. Across standard benchmarks, ELMO outperforms comparable prior methods by 9.6 percentage points on LIBERO-Plus and by 0.75 in average task length on CALVIN. Furthermore, on Blocks -- our shortcut-free simulation and real-world generalization benchmark -- ELMO reaches a 38.6% success rate while all baselines remain below 5%, demonstrating its ability to capture the semantic structure of demonstrations. Website: https://uoft-isl.github.io/elmo.github.io/

</details>

---

### [[20_Research/Papers/机器人/Autonomous_Ergodic_Robotic_Palpation_for_Elastic_Mapping_of_Curved_Soft_Tissues|Autonomous Ergodic Robotic Palpation for Elastic Mapping of Curved Soft Tissues]]

![[assets/2611.34670_figure.png|800]]

- **arXiv**: [2611.34670](https://arxiv.org/abs/2611.34670)
- **PDF**: https://arxiv.org/pdf/2611.34670
- **详细分析**: [[20_Research/Papers/机器人/Autonomous_Ergodic_Robotic_Palpation_for_Elastic_Mapping_of_Curved_Soft_Tissues|Autonomous Ergodic Robotic Palpation for Elastic Mapping of Curved Soft Tissues]]
- **作者**: Luca Beber, Cem Bilaloglu, Edoardo Lamon, Matteo Saveriano, Daniele Fontanelli, Luigi Palopoli, Sylvain Calinon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Autonomous Ergodic Robotic Palpation for Elastic Mapping of Curved Soft Tissues》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robotic palpation offers repeatable, quantitative estimates of tissue properties for stiff inclusion localization. However, existing methods often rely on prior mesh models or planar surface assumptions that do not generalize to complex human anatomy. We propose an ergodic palpation framework that operates directly on curved soft surfaces using point cloud data. Central to our approach is the Laplace--Beltrami operator, which grounds both online estimation and exploration in the surface intrinsic geometry. We estimate local viscoelastic parameters using an Unscented Kalman Filter (UKF) and fuse them into a surface-aware Gaussian Process (GP). This probabilistic model drives a diffusion-based ergodic motion planner, generating a continuous exploration trajectory that feeds the new informative samples back to the GP in a closed loop. Throughout this process, a hybrid force-impedance controller regulates interaction forces to maintain contact. We evaluate the approach against existing methods in simulation and validate it in physical experiments on tissue-mimicking silicone phantoms with varying geometries and viscoelastic properties, demonstrating geometry-consistent mapping and stiff inclusion localization under contact-rich conditions.

</details>

---

### [[20_Research/Papers/具身智能/Nav4Manip_From_Navigation_to_Dexterous_Mobile_Manipulation_through_Co-Evolution|Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution]]

![[assets/2611.34655_figure.png|800]]

- **arXiv**: [2611.34655](https://arxiv.org/abs/2611.34655)
- **PDF**: https://arxiv.org/pdf/2611.34655
- **详细分析**: [[20_Research/Papers/具身智能/Nav4Manip_From_Navigation_to_Dexterous_Mobile_Manipulation_through_Co-Evolution|Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution]]
- **作者**: Yusen Feng, Zixi Kang, Zhijun Yin, Changxiao Liu, Tianhong Gao, Jiazhao Zhang, Jiahang Liu, Libin Liu, Zhizheng Zhang, He Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Nav4Manip: From Navigation to Dexterous Mobile Manipulation through Co-Evolution》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BaSeNet, EQA, InternVLA, OmniVLA, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous mobile manipulation is essential for robots to perform useful tasks in complex, unstructured environments. However, existing systems face two challenges. First, navigation remains too coarse for downstream manipulation, which often requires a precise base position and approach orientation rather than merely reaching a meter-scale goal region. Second, navigation and manipulation are commonly trained in isolation, lacking a feedback loop that enables the two capabilities to co-evolve. These limitations prevent current systems from reliably executing long-horizon dexterous mobile-manipulation tasks in real-world environments. To address them, we introduce Nav4Manip, a bidirectionally coupled co-evolution system for long-horizon dexterous mobile manipulation. It comprises two complementary architectures: Nav4Manip-N learns long-horizon navigation and refines its policy through manipulation feedback, while Nav4Manip-M trains a world-action model (WAM) for downstream dexterous manipulation. We train Nav4Manip-N in three stages: multi-task co-tuning learns navigation behavior and manipulation-aware affordance prediction; rejection sampling fine-tuning (RFT) rejects low-quality policy-generated paths and fine-tunes the model on retained trajectories; and reinforcement learning from AI feedback (RLAIF) uses counterfactual preferences to further improve navigation decisions. To support this framework, we establish the Nav-N-Manip benchmark and construct Nav4Manip-Pairs from benchmark rollouts, providing large-scale paired navigation--manipulation trajectories and affordance supervision. Extensive experiments on public vision-language navigation (VLN) benchmarks and Nav-N-Manip demonstrate state-of-the-art performance, while real-world evaluations show that Nav4Manip completes diverse dexterous mobile-manipulation tasks. Project website: https://nav4manip.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Geometric_Acceleration_Obstacles_Physical_Boundary_Structure_and_Affine_Safety_Certificates|Geometric Acceleration Obstacles: Physical Boundary Structure and Affine Safety Certificates]]

![[assets/2611.34586_figure.png|800]]

- **arXiv**: [2611.34586](https://arxiv.org/abs/2611.34586)
- **PDF**: https://arxiv.org/pdf/2611.34586
- **详细分析**: [[20_Research/Papers/具身智能/Geometric_Acceleration_Obstacles_Physical_Boundary_Structure_and_Affine_Safety_Certificates|Geometric Acceleration Obstacles: Physical Boundary Structure and Affine Safety Certificates]]
- **作者**: Xuheng Gao, Yuhan Pang, Bi-Ke Zhu, Ronghao Chen, Lingxiao Meng, Jiankun Wang, Max Q. -H. Meng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Geometric Acceleration Obstacles: Physical Boundary Structure and Affine Safety Certificates》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Collision-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe robot navigation in dynamic environments requires collision avoidance that respects motion constraints while remaining computationally efficient. Conventional velocity-obstacle (VO) methods characterize collision-inducing motions in velocity space. Although some formulations account for acceleration-limited velocity transitions, their collision constraints remain tied to specific velocity-tracking models. Acceleration obstacles (AO) address this limitation by representing collision-inducing inputs directly in acceleration space. However, existing AO methods either rely on conservative approximations or derive analytical structure expressions without verifying their geometric correspondence. To address this gap, this paper presents Geometric Acceleration Obstacles (GAO), which provides, to the best of our knowledge, the first unified and physically validated characterization of AO geometry and its supporting structure. Specifically, we derive configuration-dependent half-planes that globally support the collision set and establish their tightness, thereby separating certified collision-free acceleration inputs from collision-inducing parts. These geometric results yield unified affine safety constraints. Combined with actuator limits, these constraints define a quadratic program (QP) for real-time navigation. Extensive experiments demonstrate that GAO achieves competitive success rates and the lowest control effort among the evaluated methods, with millisecond-level computational latency. Further circle-interchange simulations demonstrate scalability to 1,000 agents. Physical experiments validate the approach in pedestrian encounters, reciprocal multi-agent navigation, and high-speed maneuvering.

</details>

---

### [[20_Research/Papers/强化学习/Riding_the_Wave_Sim-to-Real_Humanoid_Control_on_Elastic_Terrain|Riding the Wave: Sim-to-Real Humanoid Control on Elastic Terrain]]

![[assets/2611.34569_figure.png|800]]

- **arXiv**: [2611.34569](https://arxiv.org/abs/2611.34569)
- **PDF**: https://arxiv.org/pdf/2611.34569
- **详细分析**: [[20_Research/Papers/强化学习/Riding_the_Wave_Sim-to-Real_Humanoid_Control_on_Elastic_Terrain|Riding the Wave: Sim-to-Real Humanoid Control on Elastic Terrain]]
- **作者**: Yinglei Zhu, Qin Li, Honghao Pan, Bozhao Wang, Binghui Xu, Jie Lu, Wentao Song, Xiyu Wang, Xinyu Zhu, Wei Liu, Xinjun Liu, Kai Lu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 2.4，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《Riding the Wave: Sim-to-Real Humanoid Control on Elastic Terrain》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots on deformable elastic terrains face a surface whose position and motion are coupled in space and time: deflection and rebound persist between contacts, and load at one foothold alters the support at others, so training must capture how each contact changes the support that follows. We present RIPPLE (Robust Interaction via Proprioceptive Policies on Large-deformation Elastic terrain), a simulation-to-real learning framework for humanoid control on such terrains. RIPPLE integrates ElasticMembrane, a pretensioned mass-spring mesh that models spatially coupled deflection, energy storage, and rebound, together with deformable contact into MJLab for GPU-parallel policy learning. Staged training then transfers rigid-ground skills to balance and jumping on these terrains using only proprioception, without vision or force sensing. Deployed zero-shot, the policies enable a MagicBot Z1 humanoid to balance, jump consecutively, and enter a trampoline from a rigid platform. In simulation, ElasticMembrane training holds standing success of at least 98.7% (mean over three seeds) on ElasticMembrane, IndependentSprings, and BouncyPlate under 0.3 m/s perturbations, whereas rigid-ground or contact-compliance training transfers poorly to the first two. A fixed policy tolerates stiffness from 0.35 to 2.8 times the training value, beds up to 7 m wide, and seven further simulated support scenarios, so transfer needs no calibration to the trampoline's stiffness. We plan to release the code soon. The interactive browser demo, videos, and scene configurations are available on the project page: https://fly-pigTH.github.io/wave_rider/

</details>

---

### [[20_Research/Papers/机器人/Reference-Model-Guided_Distributed_MPC_for_UAV_Swarm_Formation_Flying_Under_Switching_Directed_Graphs|Reference-Model-Guided Distributed MPC for UAV Swarm Formation Flying Under Switching Directed Graphs]]

![[assets/2611.34540_figure.png|800]]

- **arXiv**: [2611.34540](https://arxiv.org/abs/2611.34540)
- **PDF**: https://arxiv.org/pdf/2611.34540
- **详细分析**: [[20_Research/Papers/机器人/Reference-Model-Guided_Distributed_MPC_for_UAV_Swarm_Formation_Flying_Under_Switching_Directed_Graphs|Reference-Model-Guided Distributed MPC for UAV Swarm Formation Flying Under Switching Directed Graphs]]
- **作者**: Yiming Wang, Yenan Wu, Junda Wu, Yanke Sun, Huizhe Li, Ke Yu, Youmin Gong, Guangfu Ma, Jie Mei
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Reference-Model-Guided Distributed MPC for UAV Swarm Formation Flying Under Switching Directed Graphs》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distributed formation control of unmanned aerial vehicle (UAV) swarms in complex environments faces several challenges, including switching inter-agent connectivity, limited communication, external disturbances, and collision avoidance. To address these challenges, we propose a reference-model-guided distributed model predictive control (MPC) framework for UAV swarm formation. Each UAV uses relative-position information from its neighbors as input to a local reference model, whose output serves as the formation guidance for the onboard MPC controller. Meanwhile, a Kalman filter is utilized to predict neighboring UAV motions, enabling the construction of inter-UAV collision-avoidance constraints solely from instantaneous relative-state information. By decoupling MPC optimization from distributed coordination, this control architecture preserves the look-ahead planning and constraint-handling capabilities of MPC while enhancing the swarm's adaptability to switching directed graphs. Moreover, eliminating the exchange of neighbors' predicted trajectories reduces communication bandwidth demands, offering strong scalability for large-scale UAV swarms. To improve robustness and safety, disturbance-observer-based feedforward compensation is employed, while the bounded residual disturbance is explicitly considered in the control barrier function (CBF)-based obstacle-avoidance constraints. Finally, the proposed framework is validated through both simulations and real-world flight experiments. Specifically, the flight verification is conducted on a fully distributed multi-UAV platform without external global localization.

</details>

---

### [[20_Research/Papers/具身智能/Dynamic_Task_Update_Benchmark_(DTU-Bench)_Evaluating_Runtime_Task_Adaptation_in_Robotic_Manipulation|Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation]]

![[assets/2611.34538_figure.png|800]]

- **arXiv**: [2611.34538](https://arxiv.org/abs/2611.34538)
- **PDF**: https://arxiv.org/pdf/2611.34538
- **详细分析**: [[20_Research/Papers/具身智能/Dynamic_Task_Update_Benchmark_(DTU-Bench)_Evaluating_Runtime_Task_Adaptation_in_Robotic_Manipulation|Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation]]
- **作者**: Yanran Jiang, Cécile Paris, Dana Kulić, Leimin Tian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Dynamic Task Update Benchmark (DTU-Bench): Evaluating Runtime Task Adaptation in Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DTU-Bench, DynamicVLA, OpenVLA, RynnVLA, SwitchVLA, TIC-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies perform well on fixed-instruction robotic manipulation benchmarks, but their ability to adapt to instruction changes during execution remains understudied. We introduce the Dynamic Task Update Benchmark (DTU-Bench), evaluating 40 task revisions across seven update types and three execution stages using LIBERO, a simulated robotic manipulation benchmark. We compare performance when a new instruction is given before execution starts versus during execution, and examine whether the new task instructions are followed. Across 13 representative VLA configurations, average task success is 95.8% on the original object-manipulation tasks, compared with only 1.6% when the instruction changes which object to manipulate during execution. Controlled diagnostics show that policies often complete the original task before the updated one, and that their responses depend on the robot's physical state. We further test whether a simple scripted controller that releases the grasped object and moves the arm back helps robots respond to instruction changes. This improves success from 2% to 38% for π0.5 and from 8% to 48% for DM0.5, but can cause unwanted object motion. These findings reveal limitations that fixed-instruction benchmarks and task-success metrics alone can overlook in evaluating robotic manipulation. Project page: https://dtu-bench.github.io/

</details>

---

### [[20_Research/Papers/机器人/AGLR_Attribute-Guided_Latent_Refinement_for_Fine-Grained_Humanoid_Motion_Generation_and_Editing|AGLR: Attribute-Guided Latent Refinement for Fine-Grained Humanoid Motion Generation and Editing]]

![[assets/2611.34519_figure.png|800]]

- **arXiv**: [2611.34519](https://arxiv.org/abs/2611.34519)
- **PDF**: https://arxiv.org/pdf/2611.34519
- **详细分析**: [[20_Research/Papers/机器人/AGLR_Attribute-Guided_Latent_Refinement_for_Fine-Grained_Humanoid_Motion_Generation_and_Editing|AGLR: Attribute-Guided Latent Refinement for Fine-Grained Humanoid Motion Generation and Editing]]
- **作者**: Shuai Yuan, Yuwei Gui, Mingshuang Luo, Zhuo Li, Siyuan Meng, Wenhao Cui, RuiBing Hou, Bingpeng Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《AGLR: Attribute-Guided Latent Refinement for Fine-Grained Humanoid Motion Generation and Editing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion generation must accommodate evolving task requirements, where localized adjustments should satisfy new geometric constraints without disrupting desired motion details. However, language-based control lacks geometric precision, while joint-level constraints require explicit spatial targets. Local geometric constraints are also underdetermined, complicating target satisfaction and source preservation. We present AGLR (Attribute-Guided Latent Refinement), a unified framework for fine-grained humanoid motion generation and editing through source-anchored refinement. A compact geometric interface supports composable, time-varying control of limb extents, torso orientation, and root trajectories. Given a generated or encoded base latent, an Attribute Residual Adapter predicts a single-pass correction, with dual-level supervision enforcing target matching and selective preservation across attributes and motion coordinates. On HumanML3D-G1, AGLR achieves the highest controllable-generation and preservation-constrained editing success rates among evaluated methods. Editing take only 9.1 ms for a cached 500-frame motion, without additional sampling or test-time optimization. Zero-shot evaluation on BONES-SEED-G1 further demonstrates transfer without fine-tuning.

</details>

---

### [[20_Research/Papers/具身智能/HoloBrain-0.5_Technical_Report|HoloBrain-0.5 Technical Report]]

![[assets/2611.34449_figure.png|800]]

- **arXiv**: [2611.34449](https://arxiv.org/abs/2611.34449)
- **PDF**: https://arxiv.org/pdf/2611.34449
- **详细分析**: [[20_Research/Papers/具身智能/HoloBrain-0.5_Technical_Report|HoloBrain-0.5 Technical Report]]
- **作者**: Xuewu Lin, Jiahao Wang, Jiawei Li, Mengdi Li, Zhengmao Sun, Yiwei Jin, Hongyu Xie, Zhengyang Feng, Kun Wu, Zihao Chen, Lianzhou Zhang, Lichao Huang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HoloBrain-0.5 Technical Report》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA, SmolVLA, SpatialVLA, TinyVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present HoloBrain-0.5, a family of vision-language-action (VLA) models for manipulation across robot embodiments. The policies plan in a shared action space using robot state, kinematic structure, and calibrated camera observations. We standardize joint axes, coordinate frames, and tool-center points in robot descriptions (URDFs) and encode their kinematic graphs in a shared 3D representation. HoloBrain-0.5-Continuous generates action chunks by diffusion, while HoloBrain-0.5-Discrete uses residual finite scalar quantization (FSQ) and delayed autoregression. We pretrain both policies on over 10,000 hours of real-robot, simulation, and human-manipulation data spanning 15 embodiment categories. Across six closed-loop simulation settings, the discrete policy converges faster and reaches a higher mean success rate than the continuous policy (56.77% vs. 49.71%). On seven real-robot tasks, it achieves a mean progress score of 87.76% without task-specific post-training. After post-training, the continuous policy outperforms $π_{0.5}$ on the seven-task benchmark (94.52% vs. 86.25%) and an 11-task dual-arm benchmark (79.07% vs. 69.41%). The discrete-initialized continuous policy transfers five tasks zero-shot from Piper to Piper-X, scoring 63.28% on average. With target-robot demonstrations, the continuous policy scores 89.2% on Franka Panda and 92.94% on a mobile dual-arm platform. Although pretraining includes no Unitree G1 data, post-training with limited G1 demonstrations yields a mean progress score of 70.24% across three humanoid tasks, compared with 11.00% for $π_{0.5}$.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Lower-limb_Exoskeleton_Assistance_Survey,_Challenges,_and_Perspectives|Embodied Lower-limb Exoskeleton Assistance: Survey, Challenges, and Perspectives]]

![[assets/2611.34408_figure.png|800]]

- **arXiv**: [2611.34408](https://arxiv.org/abs/2611.34408)
- **PDF**: https://arxiv.org/pdf/2611.34408
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Lower-limb_Exoskeleton_Assistance_Survey,_Challenges,_and_Perspectives|Embodied Lower-limb Exoskeleton Assistance: Survey, Challenges, and Perspectives]]
- **作者**: Xiao-Yin Liu, Guotao Li, Robert Riener, Zeng-Guang Hou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Lower-limb Exoskeleton Assistance: Survey, Challenges, and Perspectives》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Over the past decade, artificial intelligence (AI) has enabled lower-limb exoskeletons to adapt to complex tasks and assist diverse users. Existing reviews, however, are organized around mechanical design, control strategies, or individual AI algorithms, and provide little systematic coverage of embodied lower-limb exoskeletons and their enabling technologies. This review defines embodied lower-limb exoskeletons and organizes the literature around four dimensions: structural self-adaptation, task adaptation, user-specific adaptation, and control self-regulation. In each dimension, state-of-the-art and representative studies are classified and discussed in terms of the associated challenges, including lightweight and compliant design, data acquisition and fusion, optimization of complex policies, and robust, compliant control. The review then identifies the principal limitations of current research and outlines future directions along these dimensions. From an embodied perspective, this review sets out the closed-loop relationship among mechanical structure, sensing, and control as a framework for analyzing lower-limb exoskeleton performance and for research on human-robot interaction. The directions it identifies point toward lightweight, comfortable, and practical physical assistance.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Natural-Language_Instructions_Temporal_Logic_as_a_Task_Language_for_VLA_Models_with_Visual-Logical_Fusion|Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion]]

![[assets/2611.34352_figure.png|800]]

- **arXiv**: [2611.34352](https://arxiv.org/abs/2611.34352)
- **PDF**: https://arxiv.org/pdf/2611.34352
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Natural-Language_Instructions_Temporal_Logic_as_a_Task_Language_for_VLA_Models_with_Visual-Logical_Fusion|Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion]]
- **作者**: Zezhi Liu, Jingwen Sun, Hongjin Chen, Shaojie Ren, Peiyan Tu, Xin Jin, Zhibo Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Beyond Natural-Language Instructions: Temporal Logic as a Task Language for VLA Models with Visual-Logical Fusion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Logic-VLA, OpenVLA, StarVLA, TL-VLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic tasks combine object relations, logical dependencies, and temporal requirements, which robot planning and industrial control commonly specify in temporal logic (TL). We introduce TL-VLA, a vision--language--action framework that replaces natural-language task instructions with temporal logic, making this spatiotemporal structure explicit. A typed graph encoder and visual--logical fusion condition continuous actions on the task specification and the current observations. To prepare a general vision--language backbone for this interface, we develop TL-aware robot pretraining with separate semantic and structural readouts: a frozen language teacher aligns task semantics, the structural readout encodes TL syntax to support complex, long-horizon tasks, and autoregressive action prediction connects the graph representation to robot behavior. Downstream policies inherit the pretrained backbone and TL encoder and learn new fusion and action modules. On CALVIN ABC$\rightarrow$D, our TL-aware initializer reaches \textbf{3.800} average chain length and \textbf{62.3\%} five-task success, compared with 3.578 and 54.5\% for a FAST initializer pretrained on the same data and 3.485 average chain length for a Qwen+NL baseline. On LIBERO-10, TL-aware initialization improves success from \textbf{91.2\% to 95.8\%}. On LIBERO-Mem, our policy reaches \textbf{65.0\%} success without observation history, compared with 45.0\% for a Qwen+NL reference. On held-out Panda planning specifications, it reaches \textbf{59.6\%} at Success@256 over three generation seeds, versus 48.4\% for Qwen+TL and 37.0\% for Qwen+NL. These results support explicit logical task conditioning and transferable TL-aware representations for robot action learning.

</details>

---

### [[20_Research/Papers/世界模型/Co-World_Model_for_Human-Video-to-Robot_Transfer_via_Co-Constructed_Shared_Latent_Dynamics|Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics]]

![[assets/2611.34302_figure.png|800]]

- **arXiv**: [2611.34302](https://arxiv.org/abs/2611.34302)
- **PDF**: https://arxiv.org/pdf/2611.34302
- **详细分析**: [[20_Research/Papers/世界模型/Co-World_Model_for_Human-Video-to-Robot_Transfer_via_Co-Constructed_Shared_Latent_Dynamics|Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics]]
- **作者**: Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling, Hui Wang, Sheng Liu, Miao Li
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 3.0（加权：具身智能 0.3，世界模型 1.6，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Co-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning. Existing methods, however, either retarget human-specific geometry or match only static visual goals, and thus stumble over the cross-embodiment dynamics mismatch and the ungrounded action execution. We present the Co-World Model (CoWM), a predictive framework jointly optimized from paired yet unsynchronized human and robot streams. To bridge the cross-embodiment dynamics gap, CoWM disentangles each observation into a shared object-relation state and embodiment-specific context. It aligns latent actions across embodiments using effect-swap and action-sensitivity objectives,such that actions are matched by their predicted effects on the manipulated objects rather than by embodimentdependent kinematics. For grounded execution, a phase-aware receding-horizon controller estimates demonstration progress, projects the inferred human action prior onto the robot action-support density, and translates the resulting latent dynamics into executable robot commands. Extensive experiments in simulation and on two physical robot platforms demonstrate the effectiveness of CoWM, its cross-platform generalizability, and the contribution of each component. See the demo video in the supporting information for details.

</details>

---

### [[20_Research/Papers/具身智能/BOT-Scale_A_Traceable_Evaluation_Methodology_for_Robotic_Manipulation|BOT-Scale: A Traceable Evaluation Methodology for Robotic Manipulation]]

![[assets/2611.34297_figure.png|800]]

- **arXiv**: [2611.34297](https://arxiv.org/abs/2611.34297)
- **PDF**: https://arxiv.org/pdf/2611.34297
- **详细分析**: [[20_Research/Papers/具身智能/BOT-Scale_A_Traceable_Evaluation_Methodology_for_Robotic_Manipulation|BOT-Scale: A Traceable Evaluation Methodology for Robotic Manipulation]]
- **作者**: Yunfei Xue, Kemi Chen, Weiling Chen, Wei Gao, Tiesong Zhao, Zheng-Jun Zha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《BOT-Scale: A Traceable Evaluation Methodology for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoEval, HealthBench, RoboEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A successful manipulation rollout can still involve a mid-task object drop or a placement deviation. Existing evaluators reduce such deviations to a single score or attach explanations computed separately; the score itself explains neither its basis nor what to fix. We show that a manipulation score becomes traceable when defined as the sum of outcome-conditioned penalties over retained behavioral-factor records. Explanation and score share the same computation, so each factor-level deduction names an inspectable deviation. BOT-Scale applies this principle by adapting behavioral assessment scales from medicine. It organizes twelve candidate factors into four assessment layers; each factor is tied to observable evidence and an explicit decision criterion. Reference calibration fixes a penalty per factor, and a closed-form rule aggregates the factor records into a score with per-factor contributions. We developed BOTScorer, an automatic scoring system based on the seven factors retained by data-driven screening, to validate this methodology. We provide BOT-Events, a dataset with eight-rater quality scores and factor-event annotations, alongside the traceable, interpretable score. The code will be released publicly.

</details>

---

### [[20_Research/Papers/具身智能/DataForgeVLA_Fully_Synthetic_Manipulation_Demonstrations_for_Vision-Language-Action_Training|DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training]]

![[assets/2611.34287_figure.png|800]]

- **arXiv**: [2611.34287](https://arxiv.org/abs/2611.34287)
- **PDF**: https://arxiv.org/pdf/2611.34287
- **详细分析**: [[20_Research/Papers/具身智能/DataForgeVLA_Fully_Synthetic_Manipulation_Demonstrations_for_Vision-Language-Action_Training|DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training]]
- **作者**: Sergei Kurchev, Iaroslav Kolomiets, Filipp Maksimov, Elizaveta Semenyakina, Miguel Altamirano Cabrera, Artem Lykov, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DataForgeVLA: Fully Synthetic Manipulation Demonstrations for Vision-Language-Action Training》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DataForgeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a dataset of 340 fully synthetic manipulation demonstrations generated from real seed data for Vision-Language-Action (VLA) training. The corpus contains 32,340 frames with synchronized RGB and actions across eight object categories, represented as LeRobot v2.1 episodes with H.264 video, per-frame robot states and pose-valued action labels, language task annotations, summary statistics and quality decisions. Each synthetic demonstration is produced without additional teleoperation: a LoRA-fine-tuned Cosmos-3 model generates a manipulation video, and RoboHaMeR recovers the corresponding robot trajectory from RGB. Quality screening accepted 300 of 340 episodes for policy fine-tuning. As preliminary evidence of feasibility, a pretrained GR00T N1.6 policy fine-tuned exclusively on the 300 accepted episodes reaches 16/20 (80%) real-world pick-and-place success on the Oreo-package task. A policy fine-tuned on 105 real teleoperated episodes achieved 18/20 (90%) under the same protocol. These results are based on one object and 20 trials per policy and are therefore reported as preliminary evidence rather than a general performance claim.

</details>

---

### [[20_Research/Papers/具身智能/Escapingthe_instruction_blackhole_of_vision-language-action_policies_via_optimal-transport_wormholes|Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes]]

![[assets/2611.34280_figure.png|800]]

- **arXiv**: [2611.34280](https://arxiv.org/abs/2611.34280)
- **PDF**: https://arxiv.org/pdf/2611.34280
- **详细分析**: [[20_Research/Papers/具身智能/Escapingthe_instruction_blackhole_of_vision-language-action_policies_via_optimal-transport_wormholes|Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes]]
- **作者**: Xuetao Li, Chen Liu, Jing Wu, Sheng Liu, Miao Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Escapingthe instruction blackhole of vision-language-action policies via optimal-transport wormholes》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SwitchVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies are trained to follow a fixed instruction, yet people change their minds while the robot acts. We identify the instruction black hole: once a VLA policy commits to a task, new instructions are absorbed and the robot completes the old task or freezes. We quantify it with a transmission ratio and an event horizon and prove it is a blind spot of static imitation, which cannot distinguish a policy that listens from a deaf one once the execution state reveals the task. We propose Wormhole, a training-free plug-in that relocates the robot instead of re-instructing it: optimal transport selects an approach-phase state of the new task, a rate-limited traversal carries the robot there, and the unmodified policy takes over. On LIBERO,Wormhole raises committed-switch success of pi to and pi0.5 from at most 1.2% to 93.1%, matching or exceeding scripted retreat-and-restart with one fifth of its action discontinuity.

</details>

---

### [[20_Research/Papers/具身智能/CamAct_Learning_Robotic_Manipulation_from_In-the-Wild_Videos_via_Camera_Motion|CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion]]

![[assets/2611.34257_figure.png|800]]

- **arXiv**: [2611.34257](https://arxiv.org/abs/2611.34257)
- **PDF**: https://arxiv.org/pdf/2611.34257
- **详细分析**: [[20_Research/Papers/具身智能/CamAct_Learning_Robotic_Manipulation_from_In-the-Wild_Videos_via_Camera_Motion|CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion]]
- **作者**: Haoming Gu, Yunpeng Qing, Zhi Hou, Weinan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CamAct: Learning Robotic Manipulation from In-the-Wild Videos via Camera Motion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Qwen-VLA, Real-World, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models benefit from large, diverse datasets for robotic manipulation, yet collecting robot demonstrations remains costly. Recent work has explored egocentric videos as a source of supervision, primarily drawing on demonstrations of human-object interaction. We show that in-the-wild videos can improve robotic manipulation even when they contain no demonstrations of object manipulation. Specifically, camera motion recovered from these videos provides an additional source of motion supervision that complements robot demonstrations. Building on this finding, we introduce CamAct, which incorporates this camera-motion supervision into VLA policies alongside robot demonstrations, extending the use of human videos for manipulation learning beyond object interactions. Experiments show that incorporating this video supervision during fine-tuning improves success rates from 96.40% to 98.10% on LIBERO and from 22.96% to 29.32% on RoboCasa 365. The resulting policy also demonstrates strong results in out-of-distribution generalization on LIBERO-Plus and real-world manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Vineyard_Exploration_using_LiDAR_Sensing_A_Field_Evaluation_on_Legged-Wheeled_Quadruped_Robot|Autonomous Vineyard Exploration using LiDAR Sensing: A Field Evaluation on Legged-Wheeled Quadruped Robot]]

![[assets/2611.34246_figure.jpeg|800]]

- **arXiv**: [2611.34246](https://arxiv.org/abs/2611.34246)
- **PDF**: https://arxiv.org/pdf/2611.34246
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Vineyard_Exploration_using_LiDAR_Sensing_A_Field_Evaluation_on_Legged-Wheeled_Quadruped_Robot|Autonomous Vineyard Exploration using LiDAR Sensing: A Field Evaluation on Legged-Wheeled Quadruped Robot]]
- **作者**: Spencer Sweeney, Hongbo Li, Michael Ziegltrum, Dimitra Koumoutsou, Andromachi Maria Delfaki, Taskin Padir, Dimitrios Kanoulas
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Autonomous Vineyard Exploration using LiDAR Sensing: A Field Evaluation on Legged-Wheeled Quadruped Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous navigation in vineyards presents significant challenges due to uneven terrain, sparse vegetation, and the repetitive geometric nature of vineyard rows. This paper evaluates a LiDAR-based autonomous exploration system deployed on a Unitree Go2 Wheeled quadruped robot. Our approach utilizes an iterative RANSAC-based line detection pipeline to identify vineyard rows and a finite-state navigation strategy to govern row selection and traversal. Field evaluations conducted at Denbies Vineyard (UK) demonstrate the system's ability to perform sustained autonomous row following, completing a 370m up-and-down traversal without intervention. We analyze the failure modes encountered, specifically focusing on line detection instability in sparse vegetation and the trade-offs of spatial filtering. The results suggest that, while RANSAC provides a robust geometric primitive, additional temporal filtering and adaptive perception are required for reliable lane-to-lane transitions in commercial vineyard environments. A video of the experimental results is available at: youtu.be/1om1HFGF4ps

</details>

---

### [[20_Research/Papers/机器人/Ground_Your_Steps_Optimizing_Sampling_Schedules_in_Flow_Matching_Robot_Policies|Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies]]

![[assets/2611.34148_figure.png|800]]

- **arXiv**: [2611.34148](https://arxiv.org/abs/2611.34148)
- **PDF**: https://arxiv.org/pdf/2611.34148
- **详细分析**: [[20_Research/Papers/机器人/Ground_Your_Steps_Optimizing_Sampling_Schedules_in_Flow_Matching_Robot_Policies|Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies]]
- **作者**: Licheng Yang, Yonghao He, Lingfeng Qian, Xin Shi, Wei Sui, Hu Su
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Ground Your Steps: Optimizing Sampling Schedules in Flow Matching Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching robot policies generate action chunks by integrating a learned velocity field at inference. However, under a fixed budget of neural function evaluations (NFEs), the integration result depends on the sampling schedule. This motivates optimizing the schedule to bring the generated action distribution closer to the demonstrations and improve task success. We propose Ground Your Steps (GYS), a training-free method that optimizes the sampling schedule by matching the generated and demonstrated chunk distributions at each observation. GYS applies truncated fractional differencing along each arm joint's action sequence and compares two types of pairwise differences between action chunks at each observation: differences of a generated chunk against a demonstration, and differences of two independent generated chunks against each other. After fractional differencing, these two pairwise-difference distributions coincide exactly when the distributions of generated and demonstrated action chunks match. GYS minimizes the energy distance between these distributions to obtain an improved schedule for each task and NFE budget. Compared with the uniform grid, GYS brings the generated chunk distribution closer to the demonstrated distribution and raises the success rate through the sampling schedule alone. On RoboTwin 2.0 benchmarks, GYS improves success rates at nearly every budget, with gains of 2.8 percentage points for both $π_{0.5}$ and GR00T N1.7. The gains also transfer to three real-world manipulation tasks, reaching up to 3.3 percentage points. Code is available at https://github.com/D-Robotics-AI-Lab/GroundYourSteps.

</details>

---

### [[20_Research/Papers/具身智能/WAtcher_Watching_Ahead_for_Safe_Robotic_Manipulation_with_Efficient_World-Action_Models|WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models]]

![[assets/2611.34124_figure.png|800]]

- **arXiv**: [2611.34124](https://arxiv.org/abs/2611.34124)
- **PDF**: https://arxiv.org/pdf/2611.34124
- **详细分析**: [[20_Research/Papers/具身智能/WAtcher_Watching_Ahead_for_Safe_Robotic_Manipulation_with_Efficient_World-Action_Models|WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models]]
- **作者**: Ziyu Shan, Xiao Ma, Kangrui Yu, Changjie Wang, Gaoyuan Wu, Zaijia Yang, Chuanrui Zhang, Qirui Li, Yanbo Zhang, Duomin Wang, Ziwei Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《WAtcher: Watching Ahead for Safe Robotic Manipulation with Efficient World-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamVLA, Real-World, SafeVLA, VideoVLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) couple future imagination with action generation, but they execute every action chunk while ignoring the potential risk. To fill this gap, we present WAtcher, a safety-aware world-action framework in which the policy imagines the outcome of the candidate chunk before execution. For fast future preview, WAtcher builds on a compact WAM whose video expert imagines the visual outcome in only two denoising steps. In addition, we propose Safe-Guard, a lightweight module kept outside the WAM that scores each candidate chunk from its imagined outcome and triggers a bounded retreat when the risk is high. Safe-Guard is detachable and can be applied to other WAMs. To train Safe-Guard, we build an autonomous pipeline to collect hazard data from RoboTwin, LIBERO, and a real robot. Specifically, the pipeline perturbs expert demonstrations and labels each candidate chunk from the physical events recorded when it is executed, such as contacts and losses of support. Using the ~25,000 labeled windows from this pipeline, Safe-Guard reaches 92.1% balanced accuracy on a blind set, and cuts hazardous closed-loop trials on training tasks from 27.0% to 10.8% without lowering task success. On a held-out 300-question benchmark, it scores 94.2%, against 72.5% and 63.3% for zero-shot GPT-6-Astra and Claude Opus 5.5. WAtcher also reaches 90.4% and 82.4% average success on RoboTwin 2.0 and ManiSkill3, on par with or above leading WAMs, and 74.0% on five real-world tasks with Safe-Guard on, against 59.5% for $π_{0.5}$. Project page: https://zyshan0929.github.io/WAtcher

</details>

---

### [[20_Research/Papers/具身智能/CoTacWAM_Joint_Modeling_of_Vision_and_Touch_for_Robotic_Manipulation|CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation]]

![[assets/2611.34117_figure.png|800]]

- **arXiv**: [2611.34117](https://arxiv.org/abs/2611.34117)
- **PDF**: https://arxiv.org/pdf/2611.34117
- **详细分析**: [[20_Research/Papers/具身智能/CoTacWAM_Joint_Modeling_of_Vision_and_Touch_for_Robotic_Manipulation|CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation]]
- **作者**: Lei Jin, Yiding Ma, Zhuohang Li, Jiachen Liu, Zibo Zhu, Kairui Liu, Chen Gao, Wei Wu, Yong Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CoTacWAM: Joint Modeling of Vision and Touch for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present CoTacWAM, a world-action model that learns shared contact semantics between wrist vision and touch, achieving the best observed performance in our nominal manipulation and missing-input evaluations. The two modalities observe the same local interaction through different signals: wrist images reveal nearby geometry, while touch records physical contact. Our approach connects their common contact meaning while preserving the evidence unique to each modality, giving the policy a joint description of interaction across available input combinations. This representation supports predictive action learning alongside head-view scene context and conditions corrections after an independent detector confirms a failed attempt. Experiments across four real-world tasks demonstrate improved manipulation performance over the evaluated baselines, robustness to missing local observations, and further gains from autonomous retries.

</details>

---

### [[20_Research/Papers/强化学习/WISER-RL_A_Wake-Sleep_Learning_Mechanism_for_Robot_Reinforcement_Learning_from_One_Demonstration|WISER-RL: A Wake-Sleep Learning Mechanism for Robot Reinforcement Learning from One Demonstration]]

![[assets/2611.34043_figure.png|800]]

- **arXiv**: [2611.34043](https://arxiv.org/abs/2611.34043)
- **PDF**: https://arxiv.org/pdf/2611.34043
- **详细分析**: [[20_Research/Papers/强化学习/WISER-RL_A_Wake-Sleep_Learning_Mechanism_for_Robot_Reinforcement_Learning_from_One_Demonstration|WISER-RL: A Wake-Sleep Learning Mechanism for Robot Reinforcement Learning from One Demonstration]]
- **作者**: Kwunhang Wong, Yang Bai, Qingyang Bao, Liudi Yang, Chenzhi Liu, Jiehong Lin, Wei Huang, Lin Li, Ziyuan Liu, Yujie Yang, Gitta Kutyniok, Zhongrui Wang...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《WISER-RL: A Wake-Sleep Learning Mechanism for Robot Reinforcement Learning from One Demonstration》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, IBRL, MemoryVLA, Real-World, WISER-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot learning from one human demonstration may rarely succeed on its own, leaving reinforcement learning (RL) with little reward feedback. We introduce WISER-RL ({W}ake--sleep policy improvement loop, {I}mitation, and {S}elective {E}xperience {R}eplay), a composite reinforcement learning framework that turns assisted practice into autonomous control. During wake, GPTDAgger monitors disagreement among actions sampled by a diffusion policy. When disagreement crosses a threshold, a frozen GPT controller uses retrieved experience to continue the episode. During sleep, Conflict-Aware Experience Reweighting (CAER) compares visually matched successful trajectories and downweights conflicting action windows with more steps remaining to success. The policy imitates the reweighted successes and learns from both successes and failures through offline advantage-guided RL before collecting the next round. After final online PPO refinement, the autonomous policy succeeded in 100% evaluations on each of six LIBERO tasks and 100% trials on each of two real-robot tasks.

</details>

---

### [[20_Research/Papers/机器人/X-World_Transferring_Video_Priors_to_Cross-Embodiment_Robot_Control|X-World: Transferring Video Priors to Cross-Embodiment Robot Control]]

![[assets/2611.33914_figure.png|800]]

- **arXiv**: [2611.33914](https://arxiv.org/abs/2611.33914)
- **PDF**: https://arxiv.org/pdf/2611.33914
- **详细分析**: [[20_Research/Papers/机器人/X-World_Transferring_Video_Priors_to_Cross-Embodiment_Robot_Control|X-World: Transferring Video Priors to Cross-Embodiment Robot Control]]
- **作者**: Chun Gu, Xiaofei Wei, Yiming Chen, Juntong Zhang, Li Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《X-World: Transferring Video Priors to Cross-Embodiment Robot Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgiBotWorld, OpenVLA, X-VLA, X-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-instructed manipulation requires robust closedloop policies, yet action-labeled robot trajectories are costly and limited in coverage. Human and robot videos provide complementary spatiotemporal priors for crossembodiment control. We propose X-World, which adapts pretrained video diffusion to variable views. A Q-Former compresses hidden states into tokens for a shared flowmatching expert that predicts action chunks. Datasetspecific projections map native states and actions. We adapt the backbone on large-scale robot and human videos, freeze it for action-only pretraining of the Q-Former and action expert, then post-train on the target platform. At inference, X-World responds at 20 Hz and overlaps updates with execution via asynchronous real-time chunking. X-World performs strongly on LIBERO and under zero-shot shifts on LIBERO-Plus. On hardware, it averages 81.7% success across six bimanual tasks on the side-mounted dual-arm UR5e, one of three real-robot configurations presented.

</details>

---

### [[20_Research/Papers/大模型/CoTAMP_Cooperative_Task_and_Motion_Planning_for_Quadruped_Robots_with_Large_Language_Models|CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models]]

![[assets/2611.33911_figure.png|800]]

- **arXiv**: [2611.33911](https://arxiv.org/abs/2611.33911)
- **PDF**: https://arxiv.org/pdf/2611.33911
- **详细分析**: [[20_Research/Papers/大模型/CoTAMP_Cooperative_Task_and_Motion_Planning_for_Quadruped_Robots_with_Large_Language_Models|CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models]]
- **作者**: Woojin Kim, Jemin Hwangbo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.9（加权：具身智能 1.5，大模型 0.3，机器人 2.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CoTAMP: Cooperative Task and Motion Planning for Quadruped Robots with Large Language Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Some environments cannot be traversed by a single quadruped robot, for example a ledge that one robot can climb only from its partner's back or a gap that must be bridged with boxes. Solving them requires cooperative task and motion planning (TAMP). Previous works are limited to the motions of a single robot or only select actions from a predefined set of skills. We propose a framework with two parts: task planning that invents motions not defined in advance, and motion generation that realizes the invented motions. Both parts consist of large language model (LLM)-based modules and code-based modules. Task planning divides the trajectory of the whole task into steps and fixes the robot poses at the step boundaries. Motion generation produces keyframes that describe the motion of each step and turns them into a continuous trajectory through kinematic synthesis. The code-based modules check every plan and motion and return failures to the LLM-based modules for correction. The whole trajectory is then refined by trajectory optimization to satisfy the dynamics. On three simulated courses with two RAIBO2 robot models, our framework produced kinematically valid references in all 30 trials, all of which converged in trajectory optimization. Compared with several baselines, our framework showed advantages in success rate, dynamic feasibility, execution time, and generation time and cost. Project page: https://woojin8098.github.io/CoTAMP/

</details>

---

### [[20_Research/Papers/具身智能/Integration_of_Vision-Language-Action_Control_for_Autonomous_Forklift_Unloading_with_Limited_Real-World_Data|Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data]]

![[assets/2611.33880_figure.png|800]]

- **arXiv**: [2611.33880](https://arxiv.org/abs/2611.33880)
- **PDF**: https://arxiv.org/pdf/2611.33880
- **详细分析**: [[20_Research/Papers/具身智能/Integration_of_Vision-Language-Action_Control_for_Autonomous_Forklift_Unloading_with_Limited_Real-World_Data|Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data]]
- **作者**: Koshi Oishi, Seigo Ito
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Integration of Vision-Language-Action Control for Autonomous Forklift Unloading with Limited Real-World Data》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forklifts play a critical role in warehousing and distribution, but existing automation systems remain limited in handling complex tasks that require sequential decision-making. Recently, vision--language--action (VLA) models have emerged as a promising approach for multi-step decision-making by directly generating control actions from visual observations and language prompts. Although VLA-based control has been extensively researched for manipulators, to the best of our knowledge, its application to forklifts remains unexplored. Therefore, this study demonstrates the integration of VLA control for an autonomous forklift unloading task with limited real-world data. Moreover, training VLA models typically requires large-scale datasets. As there is currently no public dataset for forklift operations, we use a VLA model pretrained primarily on robotic manipulator data and construct a training dataset via simulation, which can be scaled up at low cost. We then adapt the pretrained VLA model to forklift control using 9.38 h of simulation data and 0.8 h of real-world demonstrations, with the latter accounting for approximately 8% of the collected forklift data by duration. The integrated system was validated through 72 real-world trials across four model variants. The results show that the proposed system can accomplish an unloading task even with limited real-world data.

</details>

---

### [[20_Research/Papers/具身智能/$_widetilde{_varepsilon}$_Does_Initial_Noise_Induce_Directional_Bias_in_Vision-Language-Action_Models|$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?]]

![[assets/2611.33816_figure.png|800]]

- **arXiv**: [2611.33816](https://arxiv.org/abs/2611.33816)
- **PDF**: https://arxiv.org/pdf/2611.33816
- **详细分析**: [[20_Research/Papers/具身智能/$_widetilde{_varepsilon}$_Does_Initial_Noise_Induce_Directional_Bias_in_Vision-Language-Action_Models|$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?]]
- **作者**: Junmyeong Lee, Dongmin Shin, Wooseok Jeon, JunGyu Lee, Seunghyun Shin, Hae-Gon Jeon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《$\widetilde{\varepsilon}$: Does Initial Noise Induce Directional Bias in Vision-Language-Action Models?》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BehaviorVLA, DSRL, ResVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) have widely adopted diffusion-based action generation for continuous robot motions, enabling fine-grained control across diverse tasks. However, recent studies have shown that their performance is highly sensitive to initial noise, with resulting action errors that make recovery difficult during execution. Existing approaches search for favorable noise initializations to improve performance, yet the action expert itself remains sensitive to noise. In this work, we reveal that initial noise induces a consistent directional bias in action space that closely aligns with the noise's temporal mean. We thus introduce a simple yet effective framework that improves robustness to initial noise through interventions during both training and inference. During training, we enforce consistent action predictions from antithetic noise pairs $(ε, -ε)$ and, at inference, remove the noise's temporal mean. Our method substantially reduces action deviation and improves task performance across simulation benchmarks. In real-robot experiments, our method increases the average task success rate of $π_{0.5}$ from 40% to 68%, with more stable and consistent execution.

</details>

---

### [[20_Research/Papers/具身智能/FailPoint-X_A_Policy-Matched,_Failure-Anchored_Benchmark_for_Offline_VLA_Post-Training_from_Human_Takeovers|FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers]]

![[assets/2611.33769_figure.png|800]]

- **arXiv**: [2611.33769](https://arxiv.org/abs/2611.33769)
- **PDF**: https://arxiv.org/pdf/2611.33769
- **详细分析**: [[20_Research/Papers/具身智能/FailPoint-X_A_Policy-Matched,_Failure-Anchored_Benchmark_for_Offline_VLA_Post-Training_from_Human_Takeovers|FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers]]
- **作者**: Zirui Li, Yujie Yan, Jingxuan Qian, Yangang Ren, Haizhou Yin, Haoran Xu, Chen Lv
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《FailPoint-X: A Policy-Matched, Failure-Anchored Benchmark for Offline VLA Post-Training from Human Takeovers》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FRBench, Kintsugi-VLA, RePO-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human takeovers offer corrective supervision for vision-language-action (VLA) policies, but their contribution to offline post-training must be separated from that of continued optimization. We introduce FailPoint-X, a benchmark for offline VLA post-training with human takeovers. To represent uncertainty in failure onset, an annotator marks an interval for each failure, and training takeovers start at seeded frames sampled within it. From one fixed $π_{0.5}$ checkpoint, which also initializes post-training, we assemble 629 natural failures across 10 LIBERO-X task families at up to five difficulty levels. All 2,823 takeover attempts are logged; 2,400 are accepted recoveries, of which 2,320 are used for post-training. Evaluation restarts every method from the fixed midpoints of 384 held-out failure intervals. Under matched actor-update counts, we compare behavior cloning of recoveries, value-based offline learning on recoveries and failed rollouts, and continued training on existing demonstrations. Within 1,200 steps on the 240 L1-L3 held-out failures, cloning improves recovery by 29.4 percentage points (pp) over the demonstration-only control; the value-based learner does not establish a further gain (1.5 pp). In exploratory evaluation from L1-L5 nominal starts at the same horizon, cloning loses 30.0 pp of success relative to the base policy; mixing in demonstrations reduces the loss to 16.5 pp, a reduction that shrinks under a stricter, pre-specified horizon. Restorable failure states and a shared evaluator let all methods be compared from identical starts.

</details>

---

### [[20_Research/Papers/具身智能/RegHarness_Regulating_What_Code-as-Policy_Agents_Keep_from_Steps_to_Skills|RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills]]

![[assets/2611.33739_figure.png|800]]

- **arXiv**: [2611.33739](https://arxiv.org/abs/2611.33739)
- **PDF**: https://arxiv.org/pdf/2611.33739
- **详细分析**: [[20_Research/Papers/具身智能/RegHarness_Regulating_What_Code-as-Policy_Agents_Keep_from_Steps_to_Skills|RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills]]
- **作者**: Shengming Liu, Yunyi Gao, Xinyi Wang, Jianyong Sun, Shuai Wang, Yi Deng, Li Chenye, Mingcai Zhou, Sim Kuan Goh
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.0（加权：具身智能 0.9，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RURL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code-as-Policy agents generate, execute, and revise robot programs, but often lack explicit mechanisms to govern what persists across executions: which actions are retained within a trial and which code modifications carry over to subsequent runs. This leaves two critical aspects of agent behavior insufficiently controlled: step-level execution and cross-run adaptation. We present RegHarness, a two-level harness that governs both forms of persistence for the RATs agent team, without relying on a vision-language-action (VLA) policy or demonstrations. Within each trial, run-time governance evaluates each proposed step from a reset scene, replaying the committed steps, while a fixed-rule controller commits the step only when both RATs' verifier and a task-long LLM auditor approve it. Between runs, a coding agent uses logged failures to develop and test revisions to skills, primitives, and rules, which remain disabled by default until explicitly enabled by the authors. Using a single low-cost model across all run-time roles, RegHarness achieves an 87.8% success rate (158/180) on paired LIBERO-PRO trials, compared with 39.4% for RATs, and a 72.0% success rate on MolmoSpaces trials. A $2\times2$ ablation study of RegHarness's two levels shows that its skill refinement alone increases RATs' successful trials from 71 to 135, whereas run-time governance alone achieves 105 and RATs' native stepwise reset-and-replay mode achieves only 46. These findings suggest that, for Code-as-Policy agents operating with low-cost models, task success depends not only on how generated programs are executed, but also on the quality of the reusable skills they invoke and how those skills evolve across runs.

</details>

---

### [[20_Research/Papers/具身智能/A_general-purpose_safe_manipulator_planning_framework_for_diverse_environments_without_retraining|A general-purpose safe manipulator planning framework for diverse environments without retraining]]

![[assets/2611.33721_figure.png|800]]

- **arXiv**: [2611.33721](https://arxiv.org/abs/2611.33721)
- **PDF**: https://arxiv.org/pdf/2611.33721
- **详细分析**: [[20_Research/Papers/具身智能/A_general-purpose_safe_manipulator_planning_framework_for_diverse_environments_without_retraining|A general-purpose safe manipulator planning framework for diverse environments without retraining]]
- **作者**: Mingkang Long, Rong Su, Luhang Hong, Qingqing Wang, Ruochen Tai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《A general-purpose safe manipulator planning framework for diverse environments without retraining》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nowadays, robots need to be retrained whenever their operating environment changes, and this prohibitive training cost keeps them far from daily use. The community is calling for innovations that bestow on a robot the ability to safely grasp different objects under different conditions without excessive training data and computing power. In response to this call, we present a general-purpose manipulator mission-planning framework, allowing a robot to safely perform manipulation tasks, such as grasping objects that fit in its gripper, across different operating environments without retraining its controllers. The framework rests on two innovations: a finite-state abstracted model, bisimilar to the original system dynamics, that describes accessibility of the space in front of the robot under its given arm and gripper, and a block-conservative specification generation method that turns each manipulation task under any specific operational environment into specifications about state accessibility of the abstracted model. A task proven feasible and safe on the abstracted model is guaranteed to be safe and achievable by the robot. Real-world case studies conducted on a Unitree G1 U1 humanoid show that manipulation tasks commonly encountered in daily life, such as grasping an object, pressing an elevator button or picking up a berry, can be handled within this framework, where an abstracted model of the G1 U1 robot is built only once to avoid costly model reconstructions, and different tasks are simply captured by specific block-conservative specifications, achievable by a generic mission planner with vision-based feedback control.

</details>

---

### [[20_Research/Papers/具身智能/FreshVLA_Frequency-Regularized_Time_Scale_Hierarchical_Latent_Actions_for_Vision-Language-Action_Models|FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models]]

![[assets/2611.33635_figure.png|800]]

- **arXiv**: [2611.33635](https://arxiv.org/abs/2611.33635)
- **PDF**: https://arxiv.org/pdf/2611.33635
- **详细分析**: [[20_Research/Papers/具身智能/FreshVLA_Frequency-Regularized_Time_Scale_Hierarchical_Latent_Actions_for_Vision-Language-Action_Models|FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models]]
- **作者**: Jiaming Liang, Yifeng Zhan, Rongyi He, Mu Li, Jiaqi Fan, Zhiyuan Zhang, Qiwei Liang, Zhengjie Zhang, Boyang Cai, Ningyuan Zhang, Xingjian Jing, Qiang Nie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《FreshVLA: Frequency-Regularized Time Scale Hierarchical Latent Actions for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FreshVLA, OpenVLA, Real-World, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning reusable latent actions from action-free videos offers an effective route to improving Vision-Language-Action (VLA) policies. However, reconstruction-oriented latent actions do not necessarily benefit policy learning: as they may encode task-irrelevant static appearance with scene identity, or entangle slowly varying task progress with fine-grained execution dynamics in limited discrete code. We propose FreshVLA, a VLA framework built on a frequency-guided, dynamics-sensitive learning paradigm for acquiring temporally hierarchical continuous latent actions. FreshVLA uses a high-pass prior to guide visual transition encoding toward dynamical regions, thereby reducing reliance on static appearance cues. It further organizes latent actions into coarse-grained task progress and fine-grained execution dynamics through cross-timescale sampling and frequency-domain regularization, enhancing their capacity to represent long-horizon behaviors. During policy training, we freeze the pretrained latent action encoder and transfer its representations to robot control through joint flow-matching of latent and robot actions. FreshVLA achieves 98.2% average success on LIBERO and 98.0% on LIBERO-Long, exceeding GR00T-N1.6 on the latter by 3.6%. It also reaches an average sequence length of 4.52 on CALVIN and strong overall success rate of 80.4% in the zero-shot LIBERO-PLUS evaluation. Furthermore, FreshVLA exhibits greater robustness to visual perturbations and a more distinct division of roles between two branches in modeling low- and high-frequency motion, respectively. In 35-step action regression, it achieves a 51.3-percentage-point higher relative error reduction than its hierarchical discrete counterpart. Real-world experiments demonstrate that FreshVLA improves the average success rate over $π_{0.5}$ by 7.5%. The FreshVLA project page is available at https://freshvla.github.io/.

</details>

---

### [[20_Research/Papers/大模型/Skeptic_Grounding_Failure_Diagnosis_for_Robot_Skill_Discovery|Skeptic: Grounding Failure Diagnosis for Robot Skill Discovery]]

![[assets/2611.33560_figure.png|800]]

- **arXiv**: [2611.33560](https://arxiv.org/abs/2611.33560)
- **PDF**: https://arxiv.org/pdf/2611.33560
- **详细分析**: [[20_Research/Papers/大模型/Skeptic_Grounding_Failure_Diagnosis_for_Robot_Skill_Discovery|Skeptic: Grounding Failure Diagnosis for Robot Skill Discovery]]
- **作者**: Wenfang Sun, Jianghao Deng, Wenzhe Yin, Yingjun Du, Cees G. M. Snoek
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Skeptic: Grounding Failure Diagnosis for Robot Skill Discovery》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CaP-RL, Contact-GraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot agents discover reusable skills by revising programs from execution feedback and retaining experience for later tasks. This process can fail when an agent treats an unsuccessful program as evidence that the task is physically impossible, ending exploration with revision budget remaining. We study this failure in Qwen3.8-27B and examine two decisions that shape skill discovery: I) how execution failures are diagnosed, and II) which lessons enter the shared skill library. Failure diagnosis requires the agent to reconstruct physical action effects from multimodal traces, while independent reproduction of a proposed repair does not require adequate task performance from its source program. We introduce Skeptic, a training-free protocol that uses measured action outcomes to guide repair and measured task success to govern skill admission. A grounded event log reports action effects and object end states from depth images and proprioception, separating sensor observations from inferred diagnoses. Verified promotion adds a development-success requirement on the source program to the existing independent reproduction check. Across 60 audited tasks, the mean number of tasks with false impossibility judgments decreases from 19.5 to 8.5 per campaign. On 80 LIBERO-Pro tasks and seven Robosuite tasks, Skeptic improves held-out success by 14.9 and 11.7 percentage points, with frozen model weights and the same program-revision budget.

</details>

---
