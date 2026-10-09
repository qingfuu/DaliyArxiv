# cs.CV | Computer Vision and Pattern Recognition | 2026-10-08

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/强化学习/Agentic_RSR_Real-to-Sim-to-Real_through_Scene_Reconstruction_and_Execution-Grounded_Robot_Policies|Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies]]

![[assets/2610.10479_figure.png|800]]

- **arXiv**: [2610.10479](https://arxiv.org/abs/2610.10479)
- **PDF**: https://arxiv.org/pdf/2610.10479
- **详细分析**: [[20_Research/Papers/强化学习/Agentic_RSR_Real-to-Sim-to-Real_through_Scene_Reconstruction_and_Execution-Grounded_Robot_Policies|Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies]]
- **作者**: Yihan Li, Yating Feng, Shengjiu Sun, Jianing Chen, Hao Ren, Bowen Yang, Weisheng Xu, Qiwei Wu, Hui Cheng, Renjing Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GSWorld, Gen2Sim, OpenVLA, Real-to-Sim, Real2Sim, SimWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an agent recovers metric scale, iteratively refines the scene using visual feedback, and checks task-relevant interactions in MuJoCo. A coding agent then develops an executable policy, progressing from privileged object poses to visual observations and randomized simulation. The policy can interleave multiple observations and actions within one invocation, while the agent uses execution feedback to continue, retry, or revise its approach. A shared task-level interface carries the policy and accumulated experience to the real robot, where fresh observations and safety checks guide execution. Across 18 reconstructed scenes involving two robots, the mean four-view Depth MAE against reference depth estimates is 0.1057 m, the mean Lab $ΔE_{76}$ is 11.04, and the mean grayscale SSIM is 0.6990. In real-robot experiments, the aggregate task success rate reaches 80% of the simulation task success rate, indicating substantial retention of simulated performance on hardware. Code and reconstructed scene data will be made publicly available.

</details>

---

### [[20_Research/Papers/具身智能/ECHO_Embodied_Camera_Observations_of_Human_Object_Carrying|ECHO: Embodied Camera Observations of Human Object Carrying]]

![[assets/2610.10438_first_page.png|800]]

- **arXiv**: [2610.10438](https://arxiv.org/abs/2610.10438)
- **PDF**: https://arxiv.org/pdf/2610.10438
- **详细分析**: [[20_Research/Papers/具身智能/ECHO_Embodied_Camera_Observations_of_Human_Object_Carrying|ECHO: Embodied Camera Observations of Human Object Carrying]]
- **作者**: Xuefei Sun, Lorin Achey, Kali Hamilton, Alberto Speranzon, Gregory Grebe, Yonatan Bisk, Christoffer Heckman
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《ECHO: Embodied Camera Observations of Human Object Carrying》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied and assistive agents must do more than recognize objects: they must reason about where an object belongs given the layout of an environment and the habits of the people who live in it. Progress on this problem has been limited, in part because no dedicated benchmark or dataset exists to define and evaluate it. Existing RGB-D scan datasets reconstruct static rooms without human activity, while human-object-interaction datasets capture motion without a navigable, fully reconstructed scene or a ground-truth notion of an object's natural destination. We introduce contextual object placement as a benchmark task: predicting an object's destination during an observed object-carrying episode. To support this task, we present Embodied Camera observations of Human Object carrying (ECHO), a large-scale synthetic dataset that pairs dense RGB-D scans of indoor scenes with recordings of an embodied human carrying everyday objects to context-appropriate destinations. ECHO is the first publicly available dataset to combine reconstructed scenes, human activity, natural language, and contextual-placement annotations. It comprises 3,805 human-annotated episodes across 159 floors of 115 HM3D scenes, involving 198 distinct objects. Each floor includes a complete RGB-D scan with human-annotated room labels and a surface list. Each episode provides synchronized RGB-D encounter clips; 6-DoF camera, human, and object trajectories; start and destination surfaces; an action caption; and a human-written context: a single sentence describing the inhabitant's routine that implies the destination without naming it. We evaluate contextual object placement using input-masked probes and an end-to-end baseline. Results show that no single input modality is sufficient, highlighting the need to jointly reason over scene structure, human activity, and contextual knowledge.

</details>

---

### [[20_Research/Papers/具身智能/Explicit_Geometric_Chain-of-Thought_for_Vision-Language-Action_in_Autonomous_Driving|Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving]]

![[assets/2610.10390_figure.png|800]]

- **arXiv**: [2610.10390](https://arxiv.org/abs/2610.10390)
- **PDF**: https://arxiv.org/pdf/2610.10390
- **详细分析**: [[20_Research/Papers/具身智能/Explicit_Geometric_Chain-of-Thought_for_Vision-Language-Action_in_Autonomous_Driving|Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving]]
- **作者**: Xingtai Gui, Yucheng Zhou, Dongqian Guo, Jiahao Gong, Feiyang Tan, Jianbing Shen
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.5，大模型 0.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LaST-VLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, drive with dedicated 3D priors paradigm. It first grounds 2D regions corresponding to decision-critical cues, and then retrieves localized 3D priors by sampling features from a geometric foundation model within the grounded regions. These localized geometric features are interleaved into the autoregressive context to support the trajectory generation. To supervise this process, we introduce planning-relevant grounding, a new region-level grounding task that focuses on local spatial cues directly affecting ego planning decisions, and construct the PlanningGrounding dataset to endow VLAs with planning-oriented grounding capability. Experiments across multiple end-to-end autonomous driving benchmarks show that GeoCoTDrive consistently improves safety-critical planning performance, demonstrating the effectiveness of the explicit geometric chain-of-thought process for VLA-based planning.

</details>

---

### [[20_Research/Papers/大模型/MultiFly_A_Real-World_Multimodal_Aerial_Dataset_with_Annotation-Efficient_Label_Transfer_and_Cross-Modal_Semantic_Consistency|MultiFly: A Real-World Multimodal Aerial Dataset with Annotation-Efficient Label Transfer and Cross-Modal Semantic Consistency]]

![[assets/2610.10359_figure.jpg|800]]

- **arXiv**: [2610.10359](https://arxiv.org/abs/2610.10359)
- **PDF**: https://arxiv.org/pdf/2610.10359
- **详细分析**: [[20_Research/Papers/大模型/MultiFly_A_Real-World_Multimodal_Aerial_Dataset_with_Annotation-Efficient_Label_Transfer_and_Cross-Modal_Semantic_Consistency|MultiFly: A Real-World Multimodal Aerial Dataset with Annotation-Efficient Label Transfer and Cross-Modal Semantic Consistency]]
- **作者**: Markus Gross, Andreas Greiner, Taehyoung Kim, Sivasubiramaniam Subbiah, Tomaž Cotič, Sai Bharadwaj Matha, Conrad Christoph, Oussema Dhaouadi, Simon Zieher, Surya Vijaya Kumar, Gordon Elger, Henri Meeß...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《MultiFly: A Real-World Multimodal Aerial Dataset with Annotation-Efficient Label Transfer and Cross-Modal Semantic Consistency》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce MultiFly, a real-world, low-altitude UAV dataset for semantic perception across RGB, thermal, LiDAR, and radar modalities. MultiFly provides 17,272 synchronized samples from four suburban scenes with frame-wise annotations for 15 semantic classes, together with calibration and GNSS-RTK/IMU measurements. To avoid costly and inconsistent modality-specific annotation, we propagate labels from only 115 manually annotated RGB images through shared geometric representations to all four modalities. This approach generates semantic labels for 17,157 additional RGB images, 17,272 thermal images, 840M LiDAR points, and 3.4M radar points. Transferred annotations achieve 89.93% average agreement with held-out manual annotations, and 90.94% average semantic consistency across all six modality pairs. We further establish semantic segmentation benchmarks for all four modalities, revealing distinct architectural behavior for dense LiDAR and sparse radar data. Taken together, MultiFly provides a scalable foundation for multimodal aerial perception and, to the best of our knowledge, the first public real-world low-altitude aerial benchmark that combines consistent frame-wise semantic annotations for RGB, thermal, LiDAR, and radar. Data at https://github.com/markus-42/multifly.

</details>

---

### [[20_Research/Papers/强化学习/From_Digital_Human_Interactions_to_Physics-Based_Humanoid_Skills_Physics-Grounded_Post-Training_of_Interaction_Generators|From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators]]

![[assets/2610.10322_figure.png|800]]

- **arXiv**: [2610.10322](https://arxiv.org/abs/2610.10322)
- **PDF**: https://arxiv.org/pdf/2610.10322
- **详细分析**: [[20_Research/Papers/强化学习/From_Digital_Human_Interactions_to_Physics-Based_Humanoid_Skills_Physics-Grounded_Post-Training_of_Interaction_Generators|From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators]]
- **作者**: Kerui Chen, Jianrong Zhang, Kai Lv, Hehe Fan
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，机器人 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent methods have made promising progress in generating interactions between two humanoids, largely relying on physics-based tracking policies to convert digital reference motions into executable trajectories. However, limited tracking capabilities restrict the range of reference motions that can be successfully executed, reducing data utilization. Moreover, even successful tracking does not guarantee physically plausible responses or faithful realization of the intended interactions. In this paper, we introduce DIGHT, a co-adaptive framework that couples a Digital human Interaction Generator with a Humanoid Tracking policy. Our DIGHT first executes multiple text-conditioned interaction candidates in simulation using a fixed tracker. It then constructs physics-grounded preferences from the resulting rollouts, covering both general executability and interaction fidelity. Rather than collapsing these signals into a single scalar reward for candidate ranking, we align the pretrained generator using physics-decoupled diffusion direct preference optimization (DPO), preserving criterion-specific supervision without differentiating through the simulator. To improve executability, preference pairs are derived from tracking error, friction, and floating. Additionally, to improve interaction fidelity, we propose to incorporate force feedback from simulator as a measure of contact fidelity and construct preferences over contact occurrence, location, duration, and force magnitude. The aligned generator then supplies reference motions for fine-tuning the tracker, improving compatibility between generation and physical execution. Extensive experiments demonstrate that our approach not only improves the physical plausibility of generated motions but also enables more reliable and faithful humanoid interactions in simulation.

</details>

---

### [[20_Research/Papers/具身智能/Temporal_Visuo-Tactile_Learning_for_Dexterous_Grasp_Stability|Temporal Visuo-Tactile Learning for Dexterous Grasp Stability]]

![[assets/2610.10283_figure.png|800]]

- **arXiv**: [2610.10283](https://arxiv.org/abs/2610.10283)
- **PDF**: https://arxiv.org/pdf/2610.10283
- **详细分析**: [[20_Research/Papers/具身智能/Temporal_Visuo-Tactile_Learning_for_Dexterous_Grasp_Stability|Temporal Visuo-Tactile Learning for Dexterous Grasp Stability]]
- **作者**: Ken Nakahara, Aleksei Buvailik, Prokhor Kotov, Roberto Calandra
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Temporal Visuo-Tactile Learning for Dexterous Grasp Stability》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans can grasp everyday objects with almost perfect success rates using fingertip tactile feedback, yet much of the robotic grasping literature emphasizes vision-based grasp selection with parallel grippers. In this work, we systematically investigate how high-resolution, dynamic tactile sensing contributes to grasp stability prediction and model-guided grasping in dexterous robotic hands. To this end, we collected a dataset of 10,000 grasp trials across 200 objects using a multi-fingered robotic hand equipped with four Digit 360 tactile sensors, recording external vision, proprioception, and tactile streams throughout each grasp. With this dataset, we trained end-to-end temporal multimodal models to predict post-lift stability from pre-lift grasp observations and compared sensing modalities and encoding backbones. Experimental results and controlled input ablations show that incorporating touch, and particularly high-resolution, dynamic touch, improves grasp stability prediction. Finally, we deployed the learned predictor as an online stability gate on the real robot, where visuo-tactile model-guided regrasping improved the success rate among executed lifts by 10.5 percentage points over a non-tactile gate. These results show how rich fingertip sensing and expressive temporal models that capture the dynamics of touch can support learned grasping with multi-fingered hands without explicit contact or force modeling, providing a scalable data-driven path from tactile experience toward stable dexterous manipulation. The dataset is publicly available at https://lasr-lab.github.io/dexterous-grasp-stability/.

</details>

---

### [[20_Research/Papers/具身智能/Lifelong_small-object_navigation_in_changing_object_layouts_a_benchmark_and_method|Lifelong small-object navigation in changing object layouts: a benchmark and method]]

![[assets/2610.10125_figure.png|800]]

- **arXiv**: [2610.10125](https://arxiv.org/abs/2610.10125)
- **PDF**: https://arxiv.org/pdf/2610.10125
- **详细分析**: [[20_Research/Papers/具身智能/Lifelong_small-object_navigation_in_changing_object_layouts_a_benchmark_and_method|Lifelong small-object navigation in changing object layouts: a benchmark and method]]
- **作者**: Jiagan Huang, Zikun Zhou, Zijian Ni, Hongpeng Wang, Guangming Lu, Jun Yu, Wenjie Pei
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Lifelong small-object navigation in changing object layouts: a benchmark and method》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LMEE-Bench, LiSoNav-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Household robots need to continually navigate to different objects in the same environment, many of which are small and portable, such as tools and toys. Their small visual footprint and frequent occlusion make reliable observation difficult, and they may be moved by people without the robot observing the changes. We formulate this challenging task as Lifelong Small-object Navigation in Changing Object Layouts (LiSoNav-COL). Agents must seek suitable viewpoints for reliable observation, accumulate and reuse scene knowledge to efficiently locate subsequent targets, and update outdated memory after object relocation. To eliminate the need for prior scene scanning, we also require agents to start navigation with empty scene memory. Although practical, this task still lacks benchmarks designed around its defining assumptions. To bridge this gap, we introduce LiSoNav-Eval, a dedicated benchmark spanning 28 indoor scenes with 45 small-object categories. Its lifelong navigation sequences include both unchanged and relocated targets to evaluate memory reuse and adaptation to object relocation. To address this challenging task, we propose a navigation method based on multi-view Inspection with Viewpoint-Anchored Memory, dubbed IVAM-Nav. IVAM-Nav actively observes supporting surfaces from complementary viewpoints for reliable small-object perception and anchors the resulting memory to their observation viewpoints, supporting relational memory reuse and revalidation under similar viewing conditions. Extensive experiments on LiSoNav-Eval demonstrate favorable performance of IVAM-Nav against representative methods. Benchmark analyses also show that smaller objects, larger environments, and longer relocation distances pose greater challenges. The dataset and code are available here.

</details>

---

### [[20_Research/Papers/具身智能/Juno_Taming_Predictive_Latents_for_Vision-Language-Action_Models|Juno: Taming Predictive Latents for Vision-Language-Action Models]]

![[assets/2610.09940_figure.png|800]]

- **arXiv**: [2610.09940](https://arxiv.org/abs/2610.09940)
- **PDF**: https://arxiv.org/pdf/2610.09940
- **详细分析**: [[20_Research/Papers/具身智能/Juno_Taming_Predictive_Latents_for_Vision-Language-Action_Models|Juno: Taming Predictive Latents for Vision-Language-Action Models]]
- **作者**: Yuchen Zhu, Chenyi Xu, Yulin Zhang, Gang Xu, Wentao Zhu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.7（加权：具身智能 1.8，世界模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Juno: Taming Predictive Latents for Vision-Language-Action Models》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predictive teacher, and an adaptable dynamics model. During pretraining, we train it on embodiment-matched trajectories and use a dynamic CLS loss to transfer motion-weighted patch dynamics to a compact global state. During policy learning, we fuse current-frame JEPA patches into VLA perception and use a decoupled reasoning branch with separate transformation parameters to distill future latent states for action generation. During deployment, we adapt the world model on all observed transitions, including failed rollouts, freeze the adapted teacher, and re-align the policy on verified executions using LoRA adapters and a trainable action head, without expert corrections or task rewards. On SimplerEnv, Juno raises average success from $60.9\%$ to $68.5\%$ over Qwen3GR00T, the strongest baseline, and test-time adaptation further reaches $72.7\%$; on a real robot, it retains $70\%$--$75\%$ success under background, height, and object shifts where the base policy collapses to $0\%$.

</details>

---

### [[20_Research/Papers/具身智能/YUBI-STAG_Contact_and_Semantic-Rich_Alignment_for_VLAs_via_Automated_Video-Language_Grounding|YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding]]

![[assets/2610.09718_figure.png|800]]

- **arXiv**: [2610.09718](https://arxiv.org/abs/2610.09718)
- **PDF**: https://arxiv.org/pdf/2610.09718
- **详细分析**: [[20_Research/Papers/具身智能/YUBI-STAG_Contact_and_Semantic-Rich_Alignment_for_VLAs_via_Automated_Video-Language_Grounding|YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding]]
- **作者**: Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu, Hanlong Li, Tatsuya Matsushima, Yoichi Sato, Kei Ota
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：YUBI-STAG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grounding that automatically enriches manipulation demonstrations with interaction-rich semantics to align pretrained VLAs with fine-grained manipulation language. Combining contact-object segmentation with vision-language models, YUBI-STAG annotates object identities, attributes and states, per-gripper actions, bimanual coordination, and spatially grounded interactions. To address YUBI-STAG's reliance on localized sequences and multi-stage VLM inference, we distill it into YUBI-VLM. YUBI-VLM directly recovers action structure and annotations from raw, unsegmented video in few inference calls and operates from wrist views alone. We evaluate both frameworks on YUBI-STAG-Bench across temporal, semantic, and spatial grounding tasks. YUBI-VLM retains much of YUBI-STAG's annotation accuracy with fewer inference calls and shorter runtime while generalizing to unseen manipulations. Finally, post-training VLA policies on these annotations aligns them with fine-grained language and contact-aware structure. Bimanual experiments demonstrate improved performance and instruction following, including control over object identity, acting gripper, target location, and spatial relations absent from original labels.

</details>

---

### [[20_Research/Papers/大模型/RLHND_Video_Foundation_Models_as_Physically_Grounded_Hand_Trackers_for_Robot_Learning|RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning]]

![[assets/2610.09455_figure.png|800]]

- **arXiv**: [2610.09455](https://arxiv.org/abs/2610.09455)
- **PDF**: https://arxiv.org/pdf/2610.09455
- **详细分析**: [[20_Research/Papers/大模型/RLHND_Video_Foundation_Models_as_Physically_Grounded_Hand_Trackers_for_Robot_Learning|RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning]]
- **作者**: Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy training. To this end, we propose RLHND, a video foundation model-based hand tracking model that jointly estimates hand pose and realistic tactile information from monocular egocentric videos. RLHND turns the pre-trained Cosmos 3 video diffusion backbone into a deterministic clip-level feature extractor via clean-latent conditioning, carrying its learned priors on hand motion and hand-object interaction into tracking. For pose estimation, RLHND (i) predicts hand poses with anatomically plausible joint angles and (ii) enables optional conditioning on the shape parameter to maintain consistent hand shape within the same video and even across videos recorded by the same actor. For tactile estimation, a separate tactile expert stream, trained with the pose stream frozen, predicts dense contact and force over the hand surface. We further adopt LBS-based feature spreading to enable vertex-wise feature extraction without costly per-vertex attention. RLHND achieves state-of-the-art performance across various benchmark datasets for pose estimation, while also achieving state-of-the-art performance in contact and force estimation. Moreover, we demonstrate the utility of RLHND for robot learning through retargeting results and real-world robot experiments. The code will be publicly available at https://seungjun-moon.github.io/rlhnd/.

</details>

---

### [[20_Research/Papers/机器人/GUARD_Geometric_Uncertainty-Aware_Point_Cloud_Denoising_and_Segmentation_for_Robotic_Hard_Disk_Drive_Disassembly|GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly]]

![[assets/2610.09068_figure.png|800]]

- **arXiv**: [2610.09068](https://arxiv.org/abs/2610.09068)
- **PDF**: https://arxiv.org/pdf/2610.09068
- **详细分析**: [[20_Research/Papers/机器人/GUARD_Geometric_Uncertainty-Aware_Point_Cloud_Denoising_and_Segmentation_for_Robotic_Hard_Disk_Drive_Disassembly|GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly]]
- **作者**: Zuoxu Wang, Xiao Liang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointCleanNet, PointNet, SOE-Net, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic disassembly requires part-level representations that distinguish genuine component geometry from scanning and reconstruction artifacts. In point clouds of hard disk drives (HDDs), structured ghost artifacts can resemble valid components locally while remaining inconsistent with the overall geometry, allowing erroneous measurements to receive plausible semantic labels. This creates an engineering information problem: semantic prediction confidence alone does not establish whether the underlying geometry is reliable. We propose \textbf{GUARD}, a geometric uncertainty-aware framework that performs point filtering and segmentation within a single forward pass by modeling the reliability of learned geometric representations. GUARD combines a multi-scale geometric transformer with a multi-bandwidth random Fourier feature Gaussian Process to estimate per-point geometric uncertainty, complemented by predictive entropy to suppress unreliable measurements while preserving informative structures. Evaluation on 2,745 real HDD point clouds shows that GUARD improves PointNet++ segmentation mean intersection over union from 0.7739 to 0.8318. Additional experiments on ShapeNetPart and ScanNet examine robustness across corruption types, point-cloud domains, and segmentation backbones. On manually annotated ScanNet samples, geometric uncertainty achieves a corrupted-point detection F1 score of 0.7931, compared with 0.2212 for predictive entropy. The results demonstrate the value of distinguishing geometric reliability from semantic confidence and reveal a tradeoff between artifact suppression and preservation of informative structures. GUARD contributes a reliability-aware approach to interpreting imperfect 3D measurements for component identification and subsequent robotic handling. Project website: https://001-wang.github.io/GUARD_Point_denoiser/.

</details>

---

### [[20_Research/Papers/具身智能/SPW-Nav_A_Streaming_Panoramic_World_Model_for_Language-Guided_Navigation|SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation]]

![[assets/2610.08941_figure.png|800]]

- **arXiv**: [2610.08941](https://arxiv.org/abs/2610.08941)
- **PDF**: https://arxiv.org/pdf/2610.08941
- **详细分析**: [[20_Research/Papers/具身智能/SPW-Nav_A_Streaming_Panoramic_World_Model_for_Language-Guided_Navigation|SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation]]
- **作者**: Yunheng Liu, Ziqi Cai, Siqi Yang, Yimu Wang, Minggui Teng, Jiaming Tan, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.1，世界模型 1）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation》归入 世界模型、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PanoWorld, SPW-NavBench, SPW-NavSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement instructions and streams one minute of 2K 360-degree video in real time from a single panorama. SPW-Nav interprets each instruction in the previously generated panorama as camera motion. Spherical rotation decoupling applies rotation exactly on the sphere, pose-aligned conditioning keeps translation inputs bounded over long streams, and a multi-term memory with a few-step generator continues the scene as instructions change. We also build SPW-NavSet, panoramic videos with camera trajectories and verified instructions. Driven by language, SPW-Nav outperforms prior panoramic generators in camera-following accuracy and video quality, and supports on-the-fly instruction switching.

</details>

---

### [[20_Research/Papers/具身智能/CIRRA_Dual-Level_Continual_Instruction_Reconciliation_with_Ongoing_Execution_for_Embodied_Robot_Agents_in_Interactive_Household_Tasks|CIRRA: Dual-Level Continual Instruction Reconciliation with Ongoing Execution for Embodied Robot Agents in Interactive Household Tasks]]

![[assets/2610.08862_figure.png|800]]

- **arXiv**: [2610.08862](https://arxiv.org/abs/2610.08862)
- **PDF**: https://arxiv.org/pdf/2610.08862
- **详细分析**: [[20_Research/Papers/具身智能/CIRRA_Dual-Level_Continual_Instruction_Reconciliation_with_Ongoing_Execution_for_Embodied_Robot_Agents_in_Interactive_Household_Tasks|CIRRA: Dual-Level Continual Instruction Reconciliation with Ongoing Execution for Embodied Robot Agents in Interactive Household Tasks]]
- **作者**: Ci Zhang, Enfu Nan, Arman Akbari, Lin Zhao, Li Wang, Chen Wang, Weiwei Chen, Yanzhi Wang, Geng Yuan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.5，大模型 0.5，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CIRRA: Dual-Level Continual Instruction Reconciliation with Ongoing Execution for Embodied Robot Agents in Interactive Household Tasks》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Household robots must accommodate new user instructions while executing ongoing tasks. Existing agents often regenerate or extensively revise the remaining task sequence, introducing plan ambiguity, logical inconsistency, and redundant execution. We formulate continual instruction reconciliation and propose CIRRA (Continual Instruction Reconciliation for Robot Agents), a dual-level framework combining LLM-based semantic reasoning with rule-constrained structural integration. CIRRA first grounds incoming instructions to unique executable skills and resolves underspecified actions and execution locations. It then preserves the ongoing subtask sequence as an execution backbone and generates integration candidates by inserting incoming subtasks into location-matched segments. The semantic reasoner evaluates only modified segments to identify dependencies and conflicts and select the most logically coherent local integration. This structure-preserving process maintains alignment with ongoing execution, mitigates ambiguity and inconsistency, and reuses shared subtasks to reduce redundant execution. We also introduce CHIRP (Continual Household Instruction Reconciliation and Planning), a text-based benchmark of 120 episodes across eight household environments and six categories of everyday activities. On CHIRP, CIRRA achieves 74.2% decision agreement, exceeding the strongest replanning baseline by 30 percentage points; every correct fusion decision yields a correctly placed, conflict-free schedule. On a Unitree G1 humanoid, CIRRA interrupts ongoing skills at the correct moment in every trial and significantly outperforms all baselines on every metric.

</details>

---

### [[20_Research/Papers/多模态技术/PanoPed_Beyond_Bounding_Boxes_for_Sim-to-Real_Panoramic_Pedestrian_Tracking|PanoPed: Beyond Bounding Boxes for Sim-to-Real Panoramic Pedestrian Tracking]]

![[assets/2610.08826_figure.png|800]]

- **arXiv**: [2610.08826](https://arxiv.org/abs/2610.08826)
- **PDF**: https://arxiv.org/pdf/2610.08826
- **详细分析**: [[20_Research/Papers/多模态技术/PanoPed_Beyond_Bounding_Boxes_for_Sim-to-Real_Panoramic_Pedestrian_Tracking|PanoPed: Beyond Bounding Boxes for Sim-to-Real Panoramic Pedestrian Tracking]]
- **作者**: Qinfeng Zhu, Weiguang Zhao, Yunxi Jiang, Anh Nguyen, Lei Fan
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.5，机器人 0.4）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《PanoPed: Beyond Bounding Boxes for Sim-to-Real Panoramic Pedestrian Tracking》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Full-sphere panoramic cameras let fixed monitoring systems and mobile robots track people in every direction, but a planar bounding box does not fully describe where a person is on the sphere. We introduce PanoPed, a sim-to-real benchmark for pedestrian tracking on the full sphere. PanoPed-S contains 108,000 frames from fixed, quadruped-mounted, and drone-mounted cameras, with synchronized masks, depth, camera poses, and 3D pedestrian states. PanoPed-R adds 28,002 real frames from fixed cameras, 16,247 of them densely annotated. We find that an ERP rectangle cannot uniquely determine the spherical center and angular extent of the visible person, while the detector's visual query still carries information about them. Inspired by the sextant's use of angular measurements to locate objects, we propose Sextant, a plug-and-play angular localization head with only about 0.035M parameters. It reuses a frozen detector, keeps track identities unchanged, and needs no extra image encoder. Sextant gives the best result in our PanoPed-S test comparison, raising the strongest baseline, MOTIP, from 47.30 to 49.49 HOTA, with gains on all eight test sequences. Without fine-tuning on real data, the same synthetic-trained heads improve MOTIP and HAT by 0.96-1.14 HOTA on real video, and both seeds improve every real sequence. HAT+Sextant scores best among the compared systems that add no localization image encoder.

</details>

---

### [[20_Research/Papers/世界模型/A_Review_Of_Robotic_World_Models_For_Dynamic_Environments_Based_On_Factor_And_Scene_Graphs|A Review Of Robotic World Models For Dynamic Environments Based On Factor And Scene Graphs]]

![[assets/2610.08800_first_page.png|800]]

- **arXiv**: [2610.08800](https://arxiv.org/abs/2610.08800)
- **PDF**: https://arxiv.org/pdf/2610.08800
- **详细分析**: [[20_Research/Papers/世界模型/A_Review_Of_Robotic_World_Models_For_Dynamic_Environments_Based_On_Factor_And_Scene_Graphs|A Review Of Robotic World Models For Dynamic Environments Based On Factor And Scene Graphs]]
- **作者**: Marco Giberna, Miguel Fernandez-Cortizas, Jose Luis Sanchez Lopez, Holger Voos
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 0.8，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Review Of Robotic World Models For Dynamic Environments Based On Factor And Scene Graphs》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Models based on graphs have emerged in robotics as a powerful foundation for internal world representations, where factor and scene graphs are among the most prominent model types found in the related literature and in successful robotic solutions. Initially, many of these models were assuming static environments as a simplification. Herein, factor graphs mainly provide uncertainty-aware geometric estimations while scene graphs enable a structured semantic abstraction. However, real-world robotic environments are often dynamic, posing severe challenges for purely static world representations. Therefore, this review presents a comprehensive view on how dynamic aspects of real-world environments can be addressed in such graph-based world models. We organize our assessments around three main aspects: (I) suitable representations, (II) pipelines to construct and update the representations, and (III) their exploitation for downstream tasks. We review approaches that are either based on factor or scene graphs, but put special emphasis on novel approaches that combine both types to form hybrid models. We mainly analyze how different types of dynamics can be modeled herein, and categorize common architectural patterns. Finally, emerging trends and open challenges are identified, including uncertainty propagation from learned perception through the representation layers, the observability of dynamic-entity motion and scale under minimal sensing, scalable lifelong maintenance, and the lack of datasets and evaluation protocols that ground world-model quality in downstream task performance under dynamics.

</details>

---
