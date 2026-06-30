# cs.RO | Robotics | 2026-06-29

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/强化学习/WARP-RM_A_Warp-Augmented_Relative_Progress_Reward_Model_for_Data_Curation|WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation]]

![[assets/2606.28320_figure.png|800]]

- **arXiv**: [2606.28320](https://arxiv.org/abs/2606.28320)
- **PDF**: https://arxiv.org/pdf/2606.28320
- **详细分析**: [[20_Research/Papers/强化学习/WARP-RM_A_Warp-Augmented_Relative_Progress_Reward_Model_for_Data_Curation|WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation]]
- **作者**: Justin Yu, Andrew Goldberg, Kavish Kondap, Karim El-Refai, Ethan Ransing, Qianzhong Chen, Mac Schwager, Fred Shentu, Philipp Wu, Ken Goldberg
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，强化学习 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《WARP-RM: A Warp-Augmented Relative Progress Reward Model for Data Curation》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling imitation learning requires large datasets, yet human teleoperation inevitably produces mixed-quality demonstrations containing hesitations and recoveries. Prior frame-level progress reward models supervise on absolute temporal progress proxies that suffer from label noise, or require costly human annotations to define subtask boundaries. We present WARP (Warp-Augmented Relative Progress), a novel fully self-supervised algorithm for learning dense, signed relative progress magnitudes directly from successful demonstrations. WARP generates per-frame progress targets via time-warp augmentations of demonstrations (variable playback speeds and reversals) and we train WARP-RM to predict the normalized elapsed time between input frames. Aggregating these predictions across overlapping windows yields a dense frame-level progress signal. We then introduce WARP-BC, which leverages these scalar reward estimates to upweight high-advantage action chunks during behavior cloning, where chunk-level advantage is obtained by aggregating per-frame rewards. We evaluate our approach on a physical bimanual robot system performing a long-horizon deformable object manipulation task: folding T-shirts from a random crumpled start. To evaluate policy robustness against suboptimal data, we construct training datasets of varying quality using episode length as a proxy for teleoperation sub-optimality. As the dataset is widened to admit more inefficiencies, WARP-BC maintains a 19/20 success rate compared to vanilla BC's collapse to 2/20, improving throughput by up to 18x.

</details>

---

### [[20_Research/Papers/具身智能/CacheMPC_Certified_Cached_Model_Predictive_Control_for_Quadruped_Locomotion|CacheMPC: Certified Cached Model Predictive Control for Quadruped Locomotion]]

![[assets/2606.28300_figure.png|800]]

- **arXiv**: [2606.28300](https://arxiv.org/abs/2606.28300)
- **PDF**: https://arxiv.org/pdf/2606.28300
- **详细分析**: [[20_Research/Papers/具身智能/CacheMPC_Certified_Cached_Model_Predictive_Control_for_Quadruped_Locomotion|CacheMPC: Certified Cached Model Predictive Control for Quadruped Locomotion]]
- **作者**: Nimesh Khandelwal, Mehul Anand, Shakti S. Gupta, Mangal Kothari
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 2.4，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《CacheMPC: Certified Cached Model Predictive Control for Quadruped Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Active-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model Predictive Control (MPC) is the standard predictive layer in hierarchical quadruped controllers, but the per-cycle QP solve limits the update rate achievable on embedded processors. Because legged gaits revisit a bounded region of state space, MPC solutions admit caching and reuse. This paper proposes \emph{Certified CacheMPC}: a Locality-Sensitive-Hashed cache of horizon contact-force trajectories, partitioned by contact mode, retrieved at query time and accepted only when an a-posteriori per-query certificate confirms primal feasibility and a Lagrangian dual-gap upper bound on cost suboptimality. A bounded-budget controller schedule combines top-$K$ certified retrieval, a deadline-bounded QP solve, and a shifted last-certified fallback. The framework is evaluated on a Unitree Go2 across $2{,}038$ usable cold-controller MuJoCo trials, including a $600$-trial $n\!=\!50$ campaign at three failure-boundary cells, and a first-deploy session on the on-robot NVIDIA Orin NX. The un-gated cache delivers a $25\times$ median solve-time speedup in simulation and an $18.7\times$ median speedup on hardware. At $n\!=\!50$ no statistically significant difference in closed-loop stable rate is detected between the cache variants and the no-cache baseline at any tested cell. The certificate's contribution to closed-loop safety is not resolvable at the present sample size.

</details>

---

### [[20_Research/Papers/强化学习/SimFoundry_Modular_and_Automated_Scene_Generation_for_Policy_Learning_and_Evaluation|SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation]]

![[assets/2606.28276_figure.png|800]]

- **arXiv**: [2606.28276](https://arxiv.org/abs/2606.28276)
- **PDF**: https://arxiv.org/pdf/2606.28276
- **详细分析**: [[20_Research/Papers/强化学习/SimFoundry_Modular_and_Automated_Scene_Generation_for_Policy_Learning_and_Evaluation|SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation]]
- **作者**: Nadun Ranawaka, Josiah Wong, Wei-Lin Pai, Wei-Teng Chu, Tianyuan Dai, Masoud Moghani, Hang Yin, Yunfan Jiang, Wesley Durbano, Brandon Huynh, Yu Fang, Linxi Fan...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GSWorld, GenieSim, Real-to-Sim, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training and evaluating robot policies in the real world is costly and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction from a video. SimFoundry generates sim-ready digital twins and supports object, scene, and task editing, enabling the automated generation of diverse digital cousins: affordance-preserving variations of reconstructed real-world scenes. Policies trained on SimFoundry data transfer zero-shot to challenging real tasks involving multi-step manipulation, articulated object interaction, and bimanual interaction, and its digital cousins (variations of the original scene, objects, and tasks) facilitate generalization to new real-world conditions. Across 7 manipulation tasks and 5 policy architectures, SimFoundry simulation evaluations strongly predict real-world performance, with mean Pearson correlation 0.911 and mean maximum ranking violation 0.018. When evaluating sim-trained policies zero-shot in the real world, policies trained with object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively. Additional details at https://research.nvidia.com/labs/gear/simfoundry/ .

</details>

---

### [[20_Research/Papers/具身智能/Unleashing_Infinite_Motion_Scaling_Expressive_Quadrupedal_Motion_via_Generative_Video_Priors|Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors]]

![[assets/2606.28237_figure.png|800]]

- **arXiv**: [2606.28237](https://arxiv.org/abs/2606.28237)
- **PDF**: https://arxiv.org/pdf/2606.28237
- **详细分析**: [[20_Research/Papers/具身智能/Unleashing_Infinite_Motion_Scaling_Expressive_Quadrupedal_Motion_via_Generative_Video_Priors|Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors]]
- **作者**: Youzhi Liu, Li Gao, Yifei Qian, Liu Liu, Yang Cai, Ziqiao Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，机器人 0.9）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PhysWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots have achieved remarkable locomotion, yet their behavioral repertoire remains confined to a few gaits--far from the expressive, companion-like presence long envisioned for them. Attempts to import the humanoid recipe of large-scale motion data have inherited one tacit assumption: that robot motion must first pass through an animal body, making data collection dependent on cooperative animals, reconstruction fragile across species, and retargeting ill-posed across incompatible morphologies. We propose Uni-Mo, a fully automated pipeline that removes the animal from the loop by reframing data scarcity as a generation problem: an LLM proposes motion prompts, a video diffusion model synthesizes the corresponding robot behaviors, and the generated videos are lifted into 3D reference trajectories used to train tracking policies deployed on a real Unitree Go2. To make naively-drifting generations reliably extractable, we introduce an Identity Consistency Loss that enforces appearance coherence across frames. We release Quad-Imaginarium at https://github.com/GaoLii/Quad-Imaginarium.git, the resulting open-source dataset of 7,488 language-annotated quadruped motions (18.5 hours) spanning acrobatic and performative behaviors. We validate 392 randomly sampled motions on a real Unitree Go2 with a 96.7% deployment success rate, complemented by a 97.6% success rate across the full dataset in simulation.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Stable_In-Grasp_Manipulation_in_a_Non-Dropping_Action_Space|Learning Stable In-Grasp Manipulation in a Non-Dropping Action Space]]

![[assets/2606.28196_figure.png|800]]

- **arXiv**: [2606.28196](https://arxiv.org/abs/2606.28196)
- **PDF**: https://arxiv.org/pdf/2606.28196
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Stable_In-Grasp_Manipulation_in_a_Non-Dropping_Action_Space|Learning Stable In-Grasp Manipulation in a Non-Dropping Action Space]]
- **作者**: Ha Thang Long Doan, Hikaru Arita, Kazuto Nakashima, Kenji Tahara
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.1（加权：具身智能 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Stable In-Grasp Manipulation in a Non-Dropping Action Space》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditionally, dexterous manipulation controllers are designed using analytic models constrained by strong assumptions about the hand and the objects being manipulated. Reinforcement learning (RL) has become another common approach in which skills are explored openly in an end-to-end manner but is inefficient because of unnoticeable instability and conflicts in learning objectives. This paper attempts to efficiently explore stable and accurate manipulation skills by decomposing dexterous skills into multiple simpler/analyzable components. Each skill component is subsequently learned with constraints and guidance from classical physics and control theory. Our work shows that for stable grasp, in-grasp reposition/reorientation with different objects, sensor/motor noise, latency, and frictional conditions, skill learning becomes efficient and stable with prior knowledge from theory.

</details>

---

### [[20_Research/Papers/机器人/PA-BiCoop_A_Primary-Auxiliary_Cooperative_Framework_for_General_Bimanual_Manipulation|PA-BiCoop: A Primary-Auxiliary Cooperative Framework for General Bimanual Manipulation]]

![[assets/2606.28192_figure.png|800]]

- **arXiv**: [2606.28192](https://arxiv.org/abs/2606.28192)
- **PDF**: https://arxiv.org/pdf/2606.28192
- **详细分析**: [[20_Research/Papers/机器人/PA-BiCoop_A_Primary-Auxiliary_Cooperative_Framework_for_General_Bimanual_Manipulation|PA-BiCoop: A Primary-Auxiliary Cooperative Framework for General Bimanual Manipulation]]
- **作者**: Bai Qicheng, Wang Ziru, Ma Teli, Dai Guang, Wang Jingdong, Wang Mengmeng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《PA-BiCoop: A Primary-Auxiliary Cooperative Framework for General Bimanual Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual manipulation is essential for advanced robotic systems because it offers higher efficiency and flexibility compared to single-arm configurations. However, existing approaches either lack inter-arm interaction or ignore the need for a dynamic division of labor, treating the arms as functionally equivalent. To address these limitations, this paper draws inspiration from human bimanual manipulation where one arm handles core operations and the other provides auxiliary support, and proposes PA-BiCoop, a new single-model bimanual cooperation framework with dynamic primary-auxiliary arm differentiation. PA-BiCoop categorizes robotic arms into primary and auxiliary arms with adaptively adjustable roles across task stages, employs two specialized decoders that share a global feature encoder: the primary decoder generates the primary arm's base-coordinate pose and core-task affordance heatmaps, and the auxiliary decoder outputs the auxiliary arm's relative pose in the primary arm's coordinate system. Moreover, we design a dynamic role assignment module to automatically map roles to left/right arms without manual pre-definition. This design facilitates inter-arm knowledge sharing and coordinated manipulation. Extensive experiments demonstrate that our PA-BiCoop achieves superior performance: it outperforms state-of-the-art baselines by 48% on average in RLBench2 simulation tasks and by over 50% on average in real world tasks, thereby verifying its effectiveness and advancement in bimanual manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Building_a_Scalable,_Reproducible,_Evaluatable,_and_Closed-Loop_Simulation_Environment_Foundation_for_Embodied_Intelligence_Cloud-Native_Sim|Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection]]

![[assets/2606.27962_first_page.png|800]]

- **arXiv**: [2606.27962](https://arxiv.org/abs/2606.27962)
- **PDF**: https://arxiv.org/pdf/2606.27962
- **详细分析**: [[20_Research/Papers/具身智能/Building_a_Scalable,_Reproducible,_Evaluatable,_and_Closed-Loop_Simulation_Environment_Foundation_for_Embodied_Intelligence_Cloud-Native_Sim|Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection]]
- **作者**: Junwu Xiong, Yongjian Guo, Mingxi Luo, Ning Qiao, Lei Kang, Song Wang, Yince Gao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：D-VLA, Pre-VLA, RL-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a cloud-native simulation infrastructure framework for embodied intelligence that supports large-scale training, standardized evaluation, and simulation-based data collection. The framework unifies simulation environment generation, task execution, trajectory collection, model evaluation, data management, and cloud services into a scalable and reproducible platform. To address the high cost, limited scalability, and poor reproducibility of real-world robotic data collection, the framework adopts cloud-native technologies including elastic resource scheduling, containerized simulation, unified data management, and service-oriented system design, enabling efficient large-scale simulation for multi-model and multi-task workloads. Built on a four-layer architecture, the framework provides standardized environment assets, automated task generation, trajectory collection, benchmark evaluation, and closed-loop data optimization. It further integrates representative systems including D-VLA, RL-VLA3, Sword, and Pre-VLA to support scalable simulation, dynamic scheduling, visual augmentation, and real-time data filtering. We argue that cloud-native simulation infrastructure provides a unified foundation for data generation, model training, standardized evaluation, and real-world deployment, and will play a key role in the future development of embodied intelligence.

</details>

---

### [[20_Research/Papers/具身智能/When_Multi-Robot_Systems_Meet_Agentic_AI_Towards_Embodied_Collective_Intelligence|When Multi-Robot Systems Meet Agentic AI:Towards Embodied Collective Intelligence]]

![[assets/2606.27929_figure.png|800]]

- **arXiv**: [2606.27929](https://arxiv.org/abs/2606.27929)
- **PDF**: https://arxiv.org/pdf/2606.27929
- **详细分析**: [[20_Research/Papers/具身智能/When_Multi-Robot_Systems_Meet_Agentic_AI_Towards_Embodied_Collective_Intelligence|When Multi-Robot Systems Meet Agentic AI:Towards Embodied Collective Intelligence]]
- **作者**: Yuxuan Yan, Yuanyuan Jia, Qianqian Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.8，大模型 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《When Multi-Robot Systems Meet Agentic AI:Towards Embodied Collective Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied AI is increasingly becoming agentic, shifting robots from perception--control pipelines towards closed-loop systems that can retrieve context, deliberate during execution, monitor feedback, and refine future behavior. In parallel, robotics research has also moved from single-robot autonomy towards multi-robot systems, driven by the need for wider sensing, distributed action, heterogeneous capabilities, and fault tolerance. As AI agents move from single-agent use towards multi-agent collaboration, robotics faces a parallel challenge: robot teams must move beyond sharing maps, task assignments, and datasets towards sharing the state produced by embodied agent loops. This article explores Embodied Collective Intelligence (ECI), a future multi-robot paradigm in which a robot team accumulates and uses world context, task progress, and skill experience as shared resources. Specifically, we first review how embodied AI is becoming agentic and how multi-robot cooperation has evolved. We then present Embodied Collective Intelligence through Co-Perception, Co-Action, and Co-Evolution. Finally, we use an illustrative navigation study to examine one concrete component of the concept: shared world-memory inheritance. The study shows that a newly added robot can benefit from merged team memory, but it is not intended as a full evaluation of the ECI framework. Taken together, the review and conceptual framework motivate Embodied Collective Intelligence as a direction for embodied multi-agent intelligence, while the case study grounds one measurable part of the concept.

</details>

---

### [[20_Research/Papers/机器人/Swarm_sign_language_motion-based_communication_between_drones|Swarm sign language: motion-based communication between drones]]

![[assets/2606.27883_figure.png|800]]

- **arXiv**: [2606.27883](https://arxiv.org/abs/2606.27883)
- **PDF**: https://arxiv.org/pdf/2606.27883
- **详细分析**: [[20_Research/Papers/机器人/Swarm_sign_language_motion-based_communication_between_drones|Swarm sign language: motion-based communication between drones]]
- **作者**: Thomas Rey, Julien Moras, Alexandre Eudes, Antoine Manzanera
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Swarm sign language: motion-based communication between drones》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In stealth-constrained swarm robotics, visual communication provides a critical alternative to active radio transmissions, which might be jammed. This research investigates motion-based communication for non-active information exchange, utilizing modular, dynamically feasible planar trajectories as visual cues. On the receiver drone end, a pose estimator tracks the transmitting drone's pose, feeding it into our custom 3DTrajDecoder. The decoder is designed to classify and segment the spatiotemporal sequence while simultaneously regressing its size and normal vector. To robustly train the decoder on both communicative and non-communicative trajectories, we developed a configurable online procedural generation pipeline. We validate our system through real-world testing and simulation to define its operating domain, supported by an extensive ablation study detailing our architectural choices and system limitations.

</details>

---

### [[20_Research/Papers/具身智能/LocalNav_Distilling_Frontier_VLMs_and_Embodied_RL_for_On-Device_Object_Goal_Navigation|LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation]]

![[assets/2606.27871_figure.png|800]]

- **arXiv**: [2606.27871](https://arxiv.org/abs/2606.27871)
- **PDF**: https://arxiv.org/pdf/2606.27871
- **详细分析**: [[20_Research/Papers/具身智能/LocalNav_Distilling_Frontier_VLMs_and_Embodied_RL_for_On-Device_Object_Goal_Navigation|LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation]]
- **作者**: Nicolas Baumann, Liam Boyle, Pu Deng, Edoardo Ghignone, Boyang Sun, Marc Pollefeys, Luca Benini, Michele Magno
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《LocalNav: Distilling Frontier VLMs and Embodied RL for On-Device Object Goal Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Language Models (VLMs) have emerged in the robotic domain as a powerful tool that enables environmental perception with language context, serving as a catalyst for open-vocabulary tasks like ObjectNav. Yet, their computational footprint typically confines them to cloud execution, hindering low-latency inference with local deployment on resource-constrained robots. To address this challenge, we present a distillation strategy that transfers complex spatial-semantic reasoning from large frontier models into a lightweight, 4B-parameter local VLM for edge execution on embedded GPU devices (e.g., Jetson Orin). We first establish a State of the Art (SotA), Scene Graph (SG)-based pipeline using Claude Sonnet 4.6, achieving a 39.7% Success Rate (SR) on the HM3D OVON benchmark. We then demonstrate that fine-tuning Qwen3.5-4B on just 500 frontier reasoning traces effectively enables navigation capabilities, yielding a SR of 34.5%, narrowing the gap to the performance of large cloud models. Finally, we introduce E-RLVR with Token Generation (TG) regularization to compress output sequence lengths for physical deployment while grounding the agent in its task. This downstream optimization reduces TG overhead by 72.1% and latency by 71.8%. Combined with quantization, this joint strategy yields a cumulative 82.8% reduction in overall inference latency without significantly sacrificing performance, presenting a viable paradigm for local, low-latency VLM execution on mobile robots.

</details>

---

### [[20_Research/Papers/具身智能/PPO-EAL_Exact_Augmented_Lagrangian_Proximal_Policy_Optimization_for_Safe_Robotic_Control|PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control]]

![[assets/2606.27861_figure.png|800]]

- **arXiv**: [2606.27861](https://arxiv.org/abs/2606.27861)
- **PDF**: https://arxiv.org/pdf/2606.27861
- **详细分析**: [[20_Research/Papers/具身智能/PPO-EAL_Exact_Augmented_Lagrangian_Proximal_Policy_Optimization_for_Safe_Robotic_Control|PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control]]
- **作者**: Jiatao Ding, Songqun Gao, Andrea Del Prete, Matteo Saveriano
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 3.0（加权：具身智能 0.9，强化学习 1，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《PPO-EAL: Exact Augmented Lagrangian Proximal Policy Optimization for Safe Robotic Control》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has emerged as a promising solution to accomplish complex robotic control tasks; however, most of the current work ignores the safety requirements. Safe RL seeks to maximize task performance while satisfying explicit physical constraints, but current algorithms struggle to learn the policy efficiently with precise constraint satisfaction. This work proposes PPO-EAL, a novel first-order constrained policy optimization framework that integrates exact augmented Lagrangian optimization into proximal policy optimization for safe robotic control. By combining clipped policy updates with exact quadratic penalty terms, PPO-EAL achieves theoretically grounded constraint enforcement without requiring impractically large penalty factors. A momentum-regulated multiplier update further improves dual-variable stability, reducing constraint oscillation and unsafe behavior while preserving task performance. We provide exactness and convergence analysis under standard stochastic approximation assumptions. Extensive validation across diverse GPU-accelerated robotic benchmarks-including cart-pole balancing, cart-double-pendulum stabilization, 7-DoF Franka end-effector reaching, and quadrupedal locomotion-demonstrates superior safety precision and reward performance compared with state-of-the-art first-order safe RL baselines. Finally, we demonstrate zero-shot sim-to-real deployment in a contact-rich gear assembly task, where PPO-EAL substantially improves task success, reduces peak contact force, and enhances operational robustness. These results establish PPO-EAL as a general and practically deployable safe RL framework for diverse safety-critical robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Booster_Lab_A_Data-Centric_Pipeline_for_Learning_Deployable_Humanoid_Locomotion_Policies|Booster Lab: A Data-Centric Pipeline for Learning Deployable Humanoid Locomotion Policies]]

![[assets/2606.27813_first_page.png|800]]

- **arXiv**: [2606.27813](https://arxiv.org/abs/2606.27813)
- **PDF**: https://arxiv.org/pdf/2606.27813
- **详细分析**: [[20_Research/Papers/具身智能/Booster_Lab_A_Data-Centric_Pipeline_for_Learning_Deployable_Humanoid_Locomotion_Policies|Booster Lab: A Data-Centric Pipeline for Learning Deployable Humanoid Locomotion Policies]]
- **作者**: Penghui Chen, Tinglong Zheng, Yufeng Zhang, Mingguo Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Booster Lab: A Data-Centric Pipeline for Learning Deployable Humanoid Locomotion Policies》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Humanoid-Gym, Isaac-Gym, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robot motion learning requires not only task-oriented control policies but also physically feasible and natural behaviors that can be transferred to real robots. However, robot-feasible motion data are often scarce: raw human demonstrations may be incompatible with the robot morphology, open-source clips vary in quality, and simulation-collected robot trajectories still require feasibility checking. To address these challenges, we propose a data-centric training and deployment pipeline that integrates motion data curation, real-to-sim model adaptation, AMP-based reinforcement learning, and sim-to-real deployment. We validate the framework on the Booster T1 robot and further provide preliminary cross-platform validation on Booster K1.

</details>

---

### [[20_Research/Papers/机器人/LXD-SLAM_LiDAR+X_Dense_SLAM_with_$_sum_{i=0}^{5}C_5^i$_Configurable_Sensor_Combinations|LXD-SLAM: LiDAR+X Dense SLAM with $\sum_{i=0}^{5}C_5^i$ Configurable Sensor Combinations]]

![[assets/2606.27811_figure.png|800]]

- **arXiv**: [2606.27811](https://arxiv.org/abs/2606.27811)
- **PDF**: https://arxiv.org/pdf/2606.27811
- **详细分析**: [[20_Research/Papers/机器人/LXD-SLAM_LiDAR+X_Dense_SLAM_with_$_sum_{i=0}^{5}C_5^i$_Configurable_Sensor_Combinations|LXD-SLAM: LiDAR+X Dense SLAM with $\sum_{i=0}^{5}C_5^i$ Configurable Sensor Combinations]]
- **作者**: Zhong Wang, Lin Zhang, Linfei Li, Ying Shen, Shaoming Zhang, Pengcheng Shi, Shengjie Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《LXD-SLAM: LiDAR+X Dense SLAM with $\sum_{i=0}^{5}C_5^i$ Configurable Sensor Combinations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simultaneous Localization and Mapping (SLAM) is essential for autonomous systems, yet achieving reliable, globally consistent pose estimation and dense mapping in complex environments remains challenging due to geometric degeneracy and sensor drift. While multi-sensor fusion addresses these issues, existing systems often lack the modularity to adapt to diverse platforms and rely on mathematically inconsistent fusion or suboptimal map representations. To address these limitations, we propose LXD-SLAM (LiDAR+X Dense SLAM), a highly versatile and unified multi-sensor fusion framework. Centered around 3D LiDAR, our system allows for the plug-and-play integration of LiDAR, Camera, IMU, Wheel Encoder, and GNSS, supporting up to 32 distinct sensor combinations. We employ a mathematically unified Iterative Error-Sate Kalman Filter with an adaptive hierarchical prediction strategy and an update step that minimizes point-to-mesh distances and visual reprojection errors. To support this, the environment is modeled using continuous multi-layered Gaussian Process (GP) sub-meshes, which enables efficient ray-to-mesh depth recovery for visual features. For global consistency, we introduce an Extended Scan Context (ESC) descriptor derived from the GP sub-meshes alongside a Bidirectional PnP optimization for robust multi-modal loop closure within a hybrid pose graph. Extensive evaluations on public datasets and real-world experiments demonstrate that LXD-SLAM matches or exceeds state-of-the-art specialized odometry solutions across various configurations while generating high-fidelity, globally consistent dense meshes in real-time. The relevant codes and data will be made available at https://github.com/peterWon/LXD-SLAM upon publication.

</details>

---

### [[20_Research/Papers/具身智能/SpikeVLA_Vision-Language-Action_Models_with_Spiking_Neural_Networks|SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks]]

![[assets/2606.27807_figure.png|800]]

- **arXiv**: [2606.27807](https://arxiv.org/abs/2606.27807)
- **PDF**: https://arxiv.org/pdf/2606.27807
- **详细分析**: [[20_Research/Papers/具身智能/SpikeVLA_Vision-Language-Action_Models_with_Spiking_Neural_Networks|SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks]]
- **作者**: Ruiqi Song, Dujun Nie, Siyu Teng, Baiyong Ding, Xiaotong Zhang, Dong Li, Chenming Zhang, Yuchen Li, Hangbin Wu, Long Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 2.1，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SpikeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have become a dominant paradigm for embodied intelligence. However, most existing approaches are built on large-scale transformers, resulting in substantial inference latency and energy consumption that limit their practical deployment in low-power, real-time scenarios. We propose SpikeVLA, a spiking VLA architecture for embodied navigation with energy-efficient inference, consisting of three key components. (i) A spiking vision encoder, Spike-V, that replaces dense continuous layers with event-driven spiking layers to reduce the energy consumption of visual representation learning. (ii) A multi-modal spiking large language model, Spike-L, that reformulates cross-modal reasoning with spiking dynamics and token-level event-driven sparsity to further lower computational cost. (iii) A spiking action policy network, Spike-A employs Laplacian-kernel population coding with a multi-layer fully connected SNN, and decodes spiking activities into stable and robust continuous control with energy-efficient inference under low-power constraints. Experiments on navigation and robotic control tasks show that SpikeVLA significantly reduces energy consumption and computational cost while maintaining competitive performance, highlighting its potential for low-power, real-time embodied intelligence.

</details>

---

### [[20_Research/Papers/具身智能/CWI_Composite_Humanoid_Whole-Body_Imitation_System_for_Loco-manipulation|CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation]]

![[assets/2606.27676_figure.png|800]]

- **arXiv**: [2606.27676](https://arxiv.org/abs/2606.27676)
- **PDF**: https://arxiv.org/pdf/2606.27676
- **详细分析**: [[20_Research/Papers/具身智能/CWI_Composite_Humanoid_Whole-Body_Imitation_System_for_Loco-manipulation|CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation]]
- **作者**: Wenqi Ge, Junde Guo, Zhen Fu, Shunpeng Yang, Jiayu Chen, Hua Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《CWI: Composite Humanoid Whole-Body Imitation System for Loco-manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving everyday tasks with humanoid robots requires coordinating stable locomotion with versatile manipulation. However, existing whole-body controllers still face significant challenges. Methods trained solely via command sampling, without motion-capture (MoCap) data, often struggle with sparse rewards and require carefully tuned curricula to converge. This is especially problematic for upper-body control, where the resulting motions deviate from human-like statistics and degrade whole-body coordination. Conversely, approaches that imitate full-body MoCap data suffer from dataset imbalance, as many locomotion trajectories are overly aggressive for stable-locomotion scenarios, necessitating extensive data filtering and augmentation. To address this, we present Composite Whole-Body Imitation (CWI), a framework that decouples the use of MoCap data for upper-body manipulation and lower-body locomotion. This decoupling allows us to exploit the full MoCap dataset of diverse manipulation references, while stable, command-conditioned lower-body locomotion is guided by dual discriminators trained on curated expert-quality walking and squatting clips via an Adversarial Motion Prior (AMP). A multi-critic architecture reduces conflicts among locomotion, manipulation, and motion-style objectives, and a teacher--student distillation stage yields a whole-body policy conditioned only on bimanual hand poses and velocity/height commands. We evaluate CWI through simulation experiments and real-world deployment on a full-size LimX Oli humanoid. The results show competitive loco-manipulation performance, robust whole-body coordination, and practical teleoperation without full-body motion-capture equipment. A project page with supplementary material can be found at https://cwi-ral.github.io/CWI-RAL-Webpage.

</details>

---

### [[20_Research/Papers/具身智能/Direct_Action-Head_Injection_of_A_Grounded_3D_Point_Unlocks_Spatial_and_Task_Generalization|Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization]]

![[assets/2606.27663_figure.png|800]]

- **arXiv**: [2606.27663](https://arxiv.org/abs/2606.27663)
- **PDF**: https://arxiv.org/pdf/2606.27663
- **详细分析**: [[20_Research/Papers/具身智能/Direct_Action-Head_Injection_of_A_Grounded_3D_Point_Unlocks_Spatial_and_Task_Generalization|Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization]]
- **作者**: Shiang-Feng Tsai, Jin-Cheng Jhang, Yen-Ling Tai, Jia-Hong Lai, Shih-Yun Wong, KangTung-Hsu, Yi-Ting Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Direct Action-Head Injection of A Grounded 3D Point Unlocks Spatial and Task Generalization》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models leverage large-scale vision-language pretraining for flexible robot manipulation, yet at test time they remain brittle along two axes: spatial generalization, when object positions differ from those seen during training, and task generalization, when a familiar scene is paired with a different language instruction than the one seen in training. A growing family of methods addresses this brittleness by endowing a policy with the spatial and task-aware information such as 2D pixel-coordinate for object localization and placement. However, we find that existing representation through language prompting or visual prompting does not address the limitations; in contrast, exploiting a 3D point-based representation and feeding it directly to the action head leads to substantial improvements-revealing that how the grounding signal is represented and injected into the VLA is the true game changer. Thus, we propose a lightweight, model-agnostic module that represents the grounding signal in 3D, computes its relative displacement to the gripper, and injects the resulting spatial embedding directly into the action head through adaptive layer normalization. The entire module is a two-layer MLP that requires no changes to the VLA backbone or pretraining pipeline. On LIBERO-PRO, our method improves the average success rate of GR00T-N1.6 from 31.2 to 77.5 points under task perturbation and from 28.1 to 60.2 points under position perturbation (gains of 46.3 and 32.1 points). Comparable gains are achieved for $π_{0.5}$ as well, demonstrating that the mechanism is backbone-agnostic. Together, these results support our central finding: given adequate grounding lifted into 3D, injecting it directly into the action head is what unlocks both spatial and task generalization in VLAs-achievable with nothing more than a lightweight module on top of a pretrained backbone.

</details>

---

### [[20_Research/Papers/机器人/Spacecraft_Fiducial_Marker_for_Autonomous_Rendezvous,_Proximity_Operations,_and_Docking|Spacecraft Fiducial Marker for Autonomous Rendezvous, Proximity Operations, and Docking]]

![[assets/2606.27566_figure.jpg|800]]

- **arXiv**: [2606.27566](https://arxiv.org/abs/2606.27566)
- **PDF**: https://arxiv.org/pdf/2606.27566
- **详细分析**: [[20_Research/Papers/机器人/Spacecraft_Fiducial_Marker_for_Autonomous_Rendezvous,_Proximity_Operations,_and_Docking|Spacecraft Fiducial Marker for Autonomous Rendezvous, Proximity Operations, and Docking]]
- **作者**: Ravi Kumar Thakur, Matouš Vrba, Martin Saska
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Spacecraft Fiducial Marker for Autonomous Rendezvous, Proximity Operations, and Docking》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic operations in space are challenging due to the harsh environment and the high cost of failure. Fiducial markers provide visual references that aid autonomous rendezvous, proximity operations, and docking for space robots. However, existing fiducial markers are mostly single-scale and largely designed for terrestrial robotics. Such markers leave the camera's field of view at close range, precisely during the proximity and docking phases where reliable tracking is most critical. This paper presents AstraTag, a fiducial marker designed for autonomous on-orbit robotic operations. The marker template is based on a square Spidron pattern whose recursive, self-similar structure enables detection across multiple spatial scales. Marker identification uses a 48-bit signature derived from triangular sub-regions of the template and encoded with a Generalised Reed-Solomon (GRS) code. The detection pipeline performs contour-based quadrilateral localisation, perspective normalisation, and signature matching against a pre-computed dictionary. To handle markers affixed to curved spacecraft surfaces, it incorporates a Thin-Plate Spline (TPS) re-warp fallback that exploits the marker's internal rectangular borders as additional geometric correspondences. We benchmark AstraTag against three-layer Fractal ArUco and AprilTag on spacecraft mockups with flat and curved surfaces. On curved surfaces, AstraTag achieves a higher detection rate than both baselines, offering a robust recursive-marker option for space robotics.

</details>

---

### [[20_Research/Papers/机器人/AO-ARC_Almost-Surely_Asymptotically_Optimal_Multi-Robot_Motion_Planning_with_ARC|AO-ARC: Almost-Surely Asymptotically Optimal Multi-Robot Motion Planning with ARC]]

![[assets/2606.27495_figure.png|800]]

- **arXiv**: [2606.27495](https://arxiv.org/abs/2606.27495)
- **PDF**: https://arxiv.org/pdf/2606.27495
- **详细分析**: [[20_Research/Papers/机器人/AO-ARC_Almost-Surely_Asymptotically_Optimal_Multi-Robot_Motion_Planning_with_ARC|AO-ARC: Almost-Surely Asymptotically Optimal Multi-Robot Motion Planning with ARC]]
- **作者**: James D. Motes, Marco Morales, Nancy M. Amato
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《AO-ARC: Almost-Surely Asymptotically Optimal Multi-Robot Motion Planning with ARC》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present AO-ARC, an anytime multi-robot motion planning (MRMP) method that achieves initial solution times on par with state-of-the-art MRMP feasibility solvers while converging faster and more reliably than existing anytime MRMP methods as the number of robots increases. AO-ARC adapts the AO-x meta-algorithm for converting feasibility solvers into anytime algorithms by iteratively calling the original ARC method on bounded MRMP instances under a makespan cost metric. This exploits the adaptive (de)coupling of ARC while maintaining the consistent cost bound across robot (de)compositions needed for AO-x. We provide theoretical analysis proving the asymptotic optimality properties of AO- ARC and conduct empirical evaluation on a set of 2D scenarios with different levels of coordination complexity and a 3D manipulator scenario representative of real-world applications.

</details>

---
