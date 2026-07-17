# cs.RO | Robotics | 2026-07-15

#arxiv #ComputerScience

**论文数**: 21

### [[20_Research/Papers/具身智能/DenseReward_Dense_Reward_Learning_via_Failure_Synthesis_for_Robotic_Manipulation|DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation]]

![[assets/2607.13033_figure.png|800]]

- **arXiv**: [2607.13033](https://arxiv.org/abs/2607.13033)
- **PDF**: https://arxiv.org/pdf/2607.13033
- **详细分析**: [[20_Research/Papers/具身智能/DenseReward_Dense_Reward_Learning_via_Failure_Synthesis_for_Robotic_Manipulation|DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation]]
- **作者**: Yu Fang, Wanxi Dong, Jiaqi Liu, Yue Yang, Mingxiao Huo, Yao Mu, Huaxiu Yao, Li Erran Li, Daniel Szafir, Mingyu Ding
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.2，强化学习 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, GraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However, its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward signals beyond sparse trajectory-level success labels. Collecting failure trajectories typically requires laborious human effort, while pseudo-failures constructed by relabeling successful demonstrations fail to capture the diverse physical failure modes that arise during robot execution. Meanwhile, existing reward models often predict sparse binary or trajectory-level rewards, which provide limited guidance for efficient policy optimization. We introduce DenseReward, a dense robotic reward model that addresses both challenges. To train DenseReward, we develop an automated failure data generation pipeline that synthesizes physically realistic failure trajectories in simulation without human labeling, covering diverse failure modes such as collisions, missed grasps, object drops, and recovery behaviors. DenseReward predicts dense frame-level reward scores from visual observations and language instructions, enabling fine-grained estimation of task progress throughout an episode. Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation. We further demonstrate that DenseReward provides effective reward guidance for downstream model predictive control and reinforcement learning. We release the dataset, trained reward models, and evaluation suite to support the development of failure-aware dense reward modeling for robot learning.

</details>

---

### [[20_Research/Papers/具身智能/ChunkFlow_Towards_Continuity-Consistent_Chunked_Policy_Learning|ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning]]

![[assets/2607.12992_figure.png|800]]

- **arXiv**: [2607.12992](https://arxiv.org/abs/2607.12992)
- **PDF**: https://arxiv.org/pdf/2607.12992
- **详细分析**: [[20_Research/Papers/具身智能/ChunkFlow_Towards_Continuity-Consistent_Chunked_Policy_Learning|ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning]]
- **作者**: Zhao Yang, Yinan Shi, Mingyuan Yao, Wenyao Xue, Yawei Jueluo, Longjun Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Imitation-and-RL, OpenVLA, TraceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. We propose ChunkFlow, a seam-aware training-and-execution framework for chunked policies that aligns chunk structure with boundary execution. It partitions each chunk into frozen, editable, and future zones, applies deterministic overlap blending at execution, and trains raw predictions with seam and first- and second-order continuity losses. History corruption and scheduled sampling improve robustness to executed-history errors, while an AWAC fine-tuning stage adapts the policy without removing these structural regularizers. Under mild smoothness assumptions, pre-blending seam discrepancies provably decay with increasing overlap. Experiments on CALVIN, LIBERO, and real robots show an improved success-stability trade-off with low-latency inference. Project page: https://cytoderm-ai.github.io/chunkflow.

</details>

---

### [[20_Research/Papers/具身智能/MAMMOTH_A_Multi-Modal_End-to-End_Policy_for_Off-Road_Mobility_Robust_to_Missing_Modality|MAMMOTH: A Multi-Modal End-to-End Policy for Off-Road Mobility Robust to Missing Modality]]

![[assets/2607.12965_figure.png|800]]

- **arXiv**: [2607.12965](https://arxiv.org/abs/2607.12965)
- **PDF**: https://arxiv.org/pdf/2607.12965
- **详细分析**: [[20_Research/Papers/具身智能/MAMMOTH_A_Multi-Modal_End-to-End_Policy_for_Off-Road_Mobility_Robust_to_Missing_Modality|MAMMOTH: A Multi-Modal End-to-End Policy for Off-Road Mobility Robust to Missing Modality]]
- **作者**: Ahaan Kotian, Shivani Subramanyan, Suresh Sundaram
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MAMMOTH: A Multi-Modal End-to-End Policy for Off-Road Mobility Robust to Missing Modality》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OmniVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable autonomous navigation in unstructured off-road environments remains a critical unsolved challenge due to extreme terrain diversity, drastic illumination variations and acute sensor degradation. Recent developments have approached the problem as a traversability costmap estimation or visual navigation task. However, many exhibit heavy reliance on RGB modality, leading to poor performance in varied illumination such as glares, shadows or low ambient light. Achieving robust generalization in such conditions requires integrating modalities that provide supplementary scene information. Such multi-modal methods suffer from a rigid dependency on the presence of near-perfect sensor inputs, leaving them unable to robustly handle sensor degradation or individual modality failure. To address these limitations, we introduce MAMMOTH (MAsking Multi-Modal inputs for Off-road Traversability Heuristic-informed navigation), a unified end-to-end navigation policy for robust off-road visual-goal-conditioned navigation and undirected exploration. Specifically, MAMMOTH efficiently fuses multi-modal observations (RGB, Thermal, 3D Pointcloud and Ego Velocity) and is trained with a modality dropout scheme, enabling it to generalize to missing modalities at inference time. Furthermore, we employ a diffusion policy to learn the joint conditional probability distribution of physically-grounded trajectories and a intrinsic traversability heuristic. MAMMOTH utilizes this heuristic to prefer safer, smoother trajectories. We validate MAMMOTH through extensive real-world robot experiments in distinct off-road environments, including night-time operation. Our results demonstrate superior performance, with significant improvements in collision avoidance, terrain-aware planning and generalization to missing modalities. The code and dataset used for this work will be made publicly available.

</details>

---

### [[20_Research/Papers/具身智能/ExToken_Structured_Exploration_for_Efficient_Vision-Language-Action_Reinforcement_Fine-tuning|ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning]]

![[assets/2607.12931_figure.png|800]]

- **arXiv**: [2607.12931](https://arxiv.org/abs/2607.12931)
- **PDF**: https://arxiv.org/pdf/2607.12931
- **详细分析**: [[20_Research/Papers/具身智能/ExToken_Structured_Exploration_for_Efficient_Vision-Language-Action_Reinforcement_Fine-tuning|ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning]]
- **作者**: Yilun Kong, Yunpeng Qing, Guozheng Ma, Haoyu Wang, Li Shen, Zhi Hou, Dacheng Tao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. In this work, we first investigate the exploration stagnation bottleneck in current VLA-RL frameworks and reveal that trajectory diversity is fundamentally more important to sample efficiency than the sheer quantity of collected rollouts. Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration. By conditioning the policy on different tokens during rollout collection, ExToken encourages the agent to explore diverse behavioral modes, substantially improving state-action coverage and exploration efficiency. To bridge exploration during training with deterministic inference at deployment, ExToken further incorporates a state-conditioned token selector that adaptively predicts effective behavioral modes for unseen scenarios. Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.

</details>

---

### [[20_Research/Papers/大模型/Globalized_Constrained_Stein_Variational_Inference_for_Diverse_Feasible_Robot_Motion_Planning|Globalized Constrained Stein Variational Inference for Diverse Feasible Robot Motion Planning]]

![[assets/2607.12732_figure.png|800]]

- **arXiv**: [2607.12732](https://arxiv.org/abs/2607.12732)
- **PDF**: https://arxiv.org/pdf/2607.12732
- **详细分析**: [[20_Research/Papers/大模型/Globalized_Constrained_Stein_Variational_Inference_for_Diverse_Feasible_Robot_Motion_Planning|Globalized Constrained Stein Variational Inference for Diverse Feasible Robot Motion Planning]]
- **作者**: Jiayun Li, Georgia Chalvatzaki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.3，大模型 0.1，机器人 2.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Globalized Constrained Stein Variational Inference for Diverse Feasible Robot Motion Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot motion planning is inherently multimodal, yet classical planners typically return only a single solution. Probabilistic formulations address this limitation by maintaining a distribution over motions, allowing the planner to reason over multiple low-cost alternatives. In robotics, however, motion samples must also satisfy strict constraints, including collision avoidance, joint limits, contact conditions, and dynamics consistency. These hard requirements make motion sampling substantially more challenging: within a limited planning budget, the ensemble must cover diverse low-cost motions while ensuring that every sample remains feasible under the relevant constraints. We propose SteinSQP (Stein Variational Sequential Quadratic Programming), a constrained Stein variational inference method for diverse feasible robot motion sampling. SteinSQP evolves an interacting particle ensemble, as in Stein variational methods, while embedding constraints directly into a kernel-space SQP subproblem. We solve the resulting constrained Stein-Newton subproblem with a GPU-friendly matrix-free primal-dual algorithm, enabling efficient batched ensemble updates. To globalize the method, we introduce an ensemble-level merit function that jointly balances objective value, constraint violation, and particle diversity. Across five constrained motion-planning tasks, SteinSQP returns fully feasible ensembles while preserving diverse motion alternatives. Compared with first-order constrained Stein baselines and serial multistart nonlinear programming, SteinSQP shows faster and more robust ensemble convergence in terms of iterations, improves particle-wise feasibility, and achieves faster batched time-to-solution on challenging robot-scale tasks.

</details>

---

### [[20_Research/Papers/强化学习/Vision-Based_Dribbling_for_Humanoid_Soccer_via_Privileged_Representation_Learning|Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning]]

![[assets/2607.12702_figure.png|800]]

- **arXiv**: [2607.12702](https://arxiv.org/abs/2607.12702)
- **PDF**: https://arxiv.org/pdf/2607.12702
- **详细分析**: [[20_Research/Papers/强化学习/Vision-Based_Dribbling_for_Humanoid_Soccer_via_Privileged_Representation_Learning|Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning]]
- **作者**: Flavio Maiorana, Valerio Spagnoli, Eugenio Bugli, Flavio Volpi, Daniele Affinita, Vincenzo Suriani, Daniele Nardi, Luca Iocchi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.2（加权：具身智能 1.5，强化学习 0.2，机器人 1.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in humanoid robotics have highlighted the importance of deployable loco-manipulation skills. Dribbling a soccer ball while evading active opponents requires simultaneous balance, precise ball control, and awareness of a dynamic adversary under onboard sensing and real-time constraints. Existing approaches typically separate perception and motion, which can be effective in controlled settings but may fail under occlusions, fast ball movements, and complex opponent interactions, since perception is not directly optimized for control. We propose an integrated approach in which a temporal depth encoder is embedded into a reinforcement learning policy through a task-specific projection layer. We apply this framework to a simulated Booster T1 humanoid robot and show that it is possible to learn vision-based, opponent-aware dribbling directly from depth observations, without explicit state estimation or privileged scene information. The learned policy achieves 100% success in nominal target-driven dribbling and 96% success with a single static obstacle, while reaching 46% success against an actively moving ball-attacker opponent. These results demonstrate that the proposed framework supports robust vision-based dribbling in nominal and moderately dynamic settings, and provides a strong foundation for handling more challenging moving-adversary scenarios.

</details>

---

### [[20_Research/Papers/机器人/Streamlining_stereo_differentiable_rendering_for_marker-free_real-time_tracking_of_surgical_robots|Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots]]

![[assets/2607.12604_figure.png|800]]

- **arXiv**: [2607.12604](https://arxiv.org/abs/2607.12604)
- **PDF**: https://arxiv.org/pdf/2607.12604
- **详细分析**: [[20_Research/Papers/机器人/Streamlining_stereo_differentiable_rendering_for_marker-free_real-time_tracking_of_surgical_robots|Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots]]
- **作者**: Yanghe Hao, Martin Huber, Christos Bergeles, Tom Vercauteren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Streamlining stereo differentiable rendering for marker-free real-time tracking of surgical robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CtRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Purpose: Marker-based tracking of surgical robots is occlusion-prone in cluttered operating rooms. We evaluate stereo differentiable rendering for marker-free, real-time robot pose tracking, potentially improving safety, reducing setup time, and enabling multi-robot interaction. Methods: We extend the markerless pose estimation framework roboreg to online dynamic tracking via (i) sequential optimisation that propagates pose estimates across frames with motion-adaptive hyperparameter tuning, and (ii) CUDA stream parallelisation of segmentation and optimisation, combined with CUDA-graph accelerated segmentation. We evaluate on 38 unobstructed and 5 occluded displacement sequences with static start/end ground-truth calibrations and dynamic marker-based reference tracking. Results: We achieve real-time 1080p tracking at 30 fps (up from 14 fps for vanilla roboreg), matching the camera frame rate. Accuracy reaches 1.7 cm / 0.6 deg against static ground truth and 1.2 cm mean 3D error over 27,460 frames against the marker-based reference (1.53 cm over 1,242 occluded frames). Our method outperforms FoundationPose by 11% in dynamic estimation (63% under occlusion) and 250% in static estimation, with 6x faster inference. Conclusions: Stereo differentiable rendering enables real-time, high-resolution marker-free surgical robot tracking, on par with marker-based approaches and surpassing foundation-model baselines.

</details>

---

### [[20_Research/Papers/具身智能/Improving_Autonomous_Nano-drones_Performance_via_Automated_End-to-End_Optimization_and_Deployment_of_DNNs|Improving Autonomous Nano-drones Performance via Automated End-to-End Optimization and Deployment of DNNs]]

![[assets/2607.12593_figure.png|800]]

- **arXiv**: [2607.12593](https://arxiv.org/abs/2607.12593)
- **PDF**: https://arxiv.org/pdf/2607.12593
- **详细分析**: [[20_Research/Papers/具身智能/Improving_Autonomous_Nano-drones_Performance_via_Automated_End-to-End_Optimization_and_Deployment_of_DNNs|Improving Autonomous Nano-drones Performance via Automated End-to-End Optimization and Deployment of DNNs]]
- **作者**: Vlad Niculescu, Lorenzo Lamberti, Francesco Conti, Luca Benini, Daniele Palossi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Improving Autonomous Nano-drones Performance via Automated End-to-End Optimization and Deployment of DNNs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The evolution of energy-efficient ultra-low-power (ULP) parallel processors and the diffusion of convolutional neural networks (CNNs) are fueling the advent of autonomous driving nano-sized unmanned aerial vehicles (UAVs). These sub-10 cm robotic platforms are envisioned as next-generation ubiquitous smart-sensors and unobtrusive robotic-helpers. However, the limited computational/memory resources available aboard nano-UAVs introduce the challenge of minimizing and optimizing vision-based CNNs -- which to date require error-prone, labor-intensive iterative development flows. This work explores methodologies and software tools to streamline and automate all the deployment of vision-based CNN navigation on a ULP multicore system-on-chip acting as a mission computer on a Crazyflie 2.1 nano-UAV. We focus on the deployment of PULP-Dronet, a state-of-the-art CNN for autonomous navigation of nano-UAVs, from the initial training to the final closed-loop evaluation. Compared to the original hand-crafted CNN, our results show a 2x reduction of memory footprint and a speedup of 1.6x in inference time while guaranteeing the same prediction accuracy and significantly improving the behavior in the field, achieving: i) obstacle avoidance with a peak braking-speed of 1.65 m/s and improving the speed/braking-space ratio of the baseline, ii) free flight in a familiar environment up to 1.96 m/s (0.5 m/s for the baseline), and iii) lane following on a path featuring a 90 deg turn -- all while using for computation less than 1.6% of the drone's power budget. To foster new applications and future research, we open-source all the software design in a ready-to-run project compatible with the Crazyflie 2.1

</details>

---

### [[20_Research/Papers/具身智能/TrustVLA_Mechanism-Guided_Inference-Time_Defense_Against_Vision-Language-Action_Backdoors|TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors]]

![[assets/2607.12571_figure.png|800]]

- **arXiv**: [2607.12571](https://arxiv.org/abs/2607.12571)
- **PDF**: https://arxiv.org/pdf/2607.12571
- **详细分析**: [[20_Research/Papers/具身智能/TrustVLA_Mechanism-Guided_Inference-Time_Defense_Against_Vision-Language-Action_Backdoors|TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors]]
- **作者**: Pinhan Fu, Xianda Guo, Xuetao Li, Wenke Huang, Ruilin Wang, Weiheng Zhao, Wei Sui, Mang Ye
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BadVLA, OpenVLA, TrustVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. We study this gap through two independently proposed VLA attacks from groups with distinct injection strategies, BadVLA and INFUSE; the latter persists after downstream clean adaptation. Across the evaluated poisoned models, we identify a recurring internal mechanism: a \emph{compact causal footprint}, namely a small visual support that is attention-seeded, spatially compact, and \emph{causal} in a precise sense -- masking it returns a clean-calibrated evidence-evolution score to the normal operating region. This footprint motivates TrustVLA, a mechanism-guided inference-time defense that adapts the Dirichlet evidence framework from trusted classification to monitor per-token, per-layer epistemic uncertainty in VLA policies. With only a small clean calibration set, TrustVLA (i)~detects abnormal evidence evolution, (ii)~localizes the compact support by counterfactual mechanism-score drop, and (iii)~recovers the observation by localized inpainting. Across OpenVLA/LIBERO and $π_{0.5}$ transfer evaluations, TrustVLA reduces attack success while preserving clean-task performance, providing a retraining-free, mechanism-guided defense for visual-triggered VLA backdoors.

</details>

---

### [[20_Research/Papers/机器人/Infra-Swarm_Robust_Vision-Based_Multi-Robot_Swarming_via_Near-Infrared_Spectral_Vision|Infra-Swarm: Robust Vision-Based Multi-Robot Swarming via Near-Infrared Spectral Vision]]

![[assets/2607.12489_figure.png|800]]

- **arXiv**: [2607.12489](https://arxiv.org/abs/2607.12489)
- **PDF**: https://arxiv.org/pdf/2607.12489
- **详细分析**: [[20_Research/Papers/机器人/Infra-Swarm_Robust_Vision-Based_Multi-Robot_Swarming_via_Near-Infrared_Spectral_Vision|Infra-Swarm: Robust Vision-Based Multi-Robot Swarming via Near-Infrared Spectral Vision]]
- **作者**: Haoyu Chen, Qijin Li, Wanyu Xiang, Xiuxiu Lin, Zian Ning, Shiyu Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Infra-Swarm: Robust Vision-Based Multi-Robot Swarming via Near-Infrared Spectral Vision》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distributed swarms typically rely on either active wireless communication or passive vision, and they are frequently hindered by bandwidth constraints or environmental sensitivity. This paper proposes Infra-Swarm, a robust vision-based swarm. Each robot is equipped with a near-infrared light source and four ordinary gray-scale cameras. The Infra-Swarm system directly measures the centimeter-level 3D position of neighbors based on the position (bearing) and intensity (strength) of optical flares in the captured images. By utilizing 940 nm narrow-band filters to physically reject 99.2% of ambient light interference, the perception front-end achieves hardware-level robustness against illumination variations. Furthermore, its minimal computational overhead provides a resilient foundation for the massive scalability of robotic collectives on resource-constrained hardware.

</details>

---

### [[20_Research/Papers/具身智能/Deployable_Human_Preference_Alignment_in_Robotics_Learning_Representative_Rewards_from_Diverse_Human_Preferences|Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences]]

![[assets/2607.12466_figure.png|800]]

- **arXiv**: [2607.12466](https://arxiv.org/abs/2607.12466)
- **PDF**: https://arxiv.org/pdf/2607.12466
- **详细分析**: [[20_Research/Papers/具身智能/Deployable_Human_Preference_Alignment_in_Robotics_Learning_Representative_Rewards_from_Diverse_Human_Preferences|Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences]]
- **作者**: Taehyung Kim, Gwangmo Lee, Minjun Chang, Sunghyun Lim, Jongeun Choi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.9（加权：具身智能 0.6，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Deployable Human Preference Alignment in Robotics: Learning Representative Rewards from Diverse Human Preferences》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aligning robot policies with human preferences is essential for deployment to diverse end users. In per-user alignment approach, preference feedback is often sparse, so learning becomes unstable and vulnerable to human preference noise, and a growing number of individualized policies makes validation difficult before deployment. A single shared policy approach to user alignment avoids this cost but fails to capture heterogeneous preferences and often neglects minority preferences. To address these challenges, we introduce Preference-based REward Clustering (PREC), a novel framework that learns a compact set of policies from binary preference labels provided by diverse users. From a dataset of user trajectories and their preference labels, PREC first sets the labels aside and aggregates trajectories across users to learn a population-level shared trajectory encoder, alleviating limited per-user coverage and avoiding label noise during representation learning. Using this representation, PREC jointly assigns users to preference-coherent clusters and learns a representative reward model per cluster using preference labels, from which a policy is optimized for each cluster. Clustering similar users compensates for the limited number of labels available from each user and mitigates the effect of label noise. At the same time, maintaining a manageable number of reward models reduces the validation burden at deployment. Experiments across diverse simulated locomotion environments show that PREC groups users who label different trajectory subsets into preference-coherent clusters more accurately than baseline methods. Under sparse and noisy feedback, policies trained with PREC improve all three social welfare metrics over an existing single shared-policy user-alignment approach and even outperform per-user alignment approaches.

</details>

---

### [[20_Research/Papers/机器人/Model-Based_Diffusion_Optimal_Control_for_Multi-Robot_Motion_Planning|Model-Based Diffusion Optimal Control for Multi-Robot Motion Planning]]

![[assets/2607.12423_figure.png|800]]

- **arXiv**: [2607.12423](https://arxiv.org/abs/2607.12423)
- **PDF**: https://arxiv.org/pdf/2607.12423
- **详细分析**: [[20_Research/Papers/机器人/Model-Based_Diffusion_Optimal_Control_for_Multi-Robot_Motion_Planning|Model-Based Diffusion Optimal Control for Multi-Robot Motion Planning]]
- **作者**: Zhilin He, Yorai Shaoul, Jiaoyang Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Model-Based Diffusion Optimal Control for Multi-Robot Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Robot Motion Planning in continuous environments, where robots must generate dynamically feasible, collision-free trajectories, is challenging due to the combinatorial growth of the joint trajectory space and the difficulty of enforcing dynamic feasibility and hard safety constraints. Recent approaches recast trajectory planning as probabilistic inference, sampling from a posterior over trajectories using diffusion models whose score functions are learned from demonstration data. While showing promising performance, these approaches are limited: they often rely on sizable demonstration datasets and struggle to rigorously enforce dynamics and hard safety constraints during sampling. To this end, we introduce Model-Based Diffusion Optimal Control (MDOC), a model-based diffusion planner that efficiently produces dynamically feasible trajectories without relying on data. Crucially, we show that MDOC's safety mechanism -- combining known dynamics models with Control Barrier Function-constrained projections -- naturally scales to multi-robot planning settings through Conflict-Based Search. Across simulation experiments, this integrated method consistently outperforms representative baseline planners in sample efficiency, geometric smoothness, and success rate, while reducing computation time and producing collision-free trajectories.

</details>

---

### [[20_Research/Papers/具身智能/StratMamba_Strategic_and_Reactive_Stream_Partitioning_for_Path-Efficient_LiDAR-Based_Obstacle_Avoidance|StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance]]

![[assets/2607.12370_figure.jpg|800]]

- **arXiv**: [2607.12370](https://arxiv.org/abs/2607.12370)
- **PDF**: https://arxiv.org/pdf/2607.12370
- **详细分析**: [[20_Research/Papers/具身智能/StratMamba_Strategic_and_Reactive_Stream_Partitioning_for_Path-Efficient_LiDAR-Based_Obstacle_Avoidance|StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance]]
- **作者**: Hung-Chieh Wu, Xiaopan Zhang, Kasra Sinaei, Ryan Abnavi, Kasun Weerakoon, Christopher Bradley, Seyed Fakoorian, Jiachen Li, Donald Ebeigbe
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes StratMamba, a dual-stream Mamba-based temporal modeling architecture, to more efficiently capture long-horizon temporal dependencies required for robot navigation in complex and obstacle-rich environments. StratMamba leverages a combination of fast-decay and slow-decay memory architectures, where the fast-decay component processes high-frequency LiDAR data for reactive obstacle avoidance, while the slow-decay component maintains longer-horizon goal information for strategic planning. We perform extensive evaluations of different obstacle avoidance scenarios in IsaacLab and Gazebo, while also validating successful sim-to-real deployment on a Unitree GO1 quadruped robot navigating in the presence of static/dynamic obstacles. Comparisons with other temporal RL baselines, such as LSTM, Transformer, and Vanilla-Mamba, show that our StratMamba achieves exceptional temporal reasoning efficiency with a lower timeout rate, while maintaining the fastest navigation speed (576 median steps, 5.0% better than Vanilla-Mamba). It also achieves the highest path optimality (0.915 path efficiency) across all baselines. Real-world evaluation reveals that StratMamba maintains more robust performance across extended LiDAR ranges compared to vanilla Mamba and the Transformer, demonstrating that dual-stream partitioning effectively balances reactive safety with strategic navigation under challenging sensing conditions.

</details>

---

### [[20_Research/Papers/具身智能/VistaVLA_Geometry-_and_Semantic-Aware_3D_Gaussian-Grounded_VLA_for_Robotic_Manipulation|VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation]]

![[assets/2607.12356_figure.png|800]]

- **arXiv**: [2607.12356](https://arxiv.org/abs/2607.12356)
- **PDF**: https://arxiv.org/pdf/2607.12356
- **详细分析**: [[20_Research/Papers/具身智能/VistaVLA_Geometry-_and_Semantic-Aware_3D_Gaussian-Grounded_VLA_for_Robotic_Manipulation|VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation]]
- **作者**: Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.1（加权：具身智能 3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, VistaVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures and lack high-level semantic grounding in 3D space. In human cognition, interaction with the physical world relies on a 3D semantic cognitive map - an internal mental model that integrates spatial layouts with semantic context to enable persistent, viewpoint-invariant reasoning. In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning. Specifically, VistaVLA lifts multi-view vision-language features into 3D Gaussian primitives, forming geometry-anchored semantic tokens that align view-consistent spatial grounding with 2D visual feature spaces. To make this 3D representation computationally tractable for effective VLA control, we introduce Merge-then-Query (MtQ), a token summarization mechanism. MtQ compresses dense Gaussian primitives into a highly compact set of spatially informative tokens, achieving a 99% token reduction while preserving action-relevant 3D layouts and semantic context. Extensive evaluations in both simulated and real-world environments demonstrate the effectiveness of VistaVLA. Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA-Adapter baseline on challenging out-of-distribution tasks.

</details>

---

### [[20_Research/Papers/具身智能/Reducing_Temporal_Redundancy_for_Efficient_Vision-Language-Action_Inference|Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference]]

![[assets/2607.12287_figure.png|800]]

- **arXiv**: [2607.12287](https://arxiv.org/abs/2607.12287)
- **PDF**: https://arxiv.org/pdf/2607.12287
- **详细分析**: [[20_Research/Papers/具身智能/Reducing_Temporal_Redundancy_for_Efficient_Vision-Language-Action_Inference|Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference]]
- **作者**: Yuzhou Wu, Yuxin Zheng, Muchun Niu, Yishan Yang, Tianhao Liu, hanwen kang, Jiajian Jing, Linfeng Zhang, Chuan Wen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeeR-VLA, OpenVLA, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies. To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation. On the perception side, we incrementally update only tokens corresponding to dynamic scene regions instead of re-encoding entire frames. On the policy side, we compress diffusion sampling into a compact 2-step schedule through efficiency oriented training while preserving action precision. Experiments on Libero, RobotWin, and Real Robot Platforms demonstrate over 2 times speedup while maintaining high performance, achieving up to 98% success rate on general manipulation benchmarks. Our codes will be released on Github.

</details>

---

### [[20_Research/Papers/机器人/DiffRadar_Differentiable_Physics-Aware_Radar_SLAM_with_Gaussian_Fields|DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields]]

![[assets/2607.12265_figure.png|800]]

- **arXiv**: [2607.12265](https://arxiv.org/abs/2607.12265)
- **PDF**: https://arxiv.org/pdf/2607.12265
- **详细分析**: [[20_Research/Papers/机器人/DiffRadar_Differentiable_Physics-Aware_Radar_SLAM_with_Gaussian_Fields|DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields]]
- **作者**: Gaurav Bagwe, Xiaoyong Yuan, Yongji Wu, Lan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Security, Systems

#### 研究背景与动机

《DiffRadar: Differentiable Physics-Aware Radar SLAM with Gaussian Fields》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Radar sensing is increasingly used in mobile systems because it operates reliably under poor lighting, adverse weather, and privacy-sensitive settings where cameras and LiDAR often fail. However, most existing radar SLAM systems estimate motion through scan matching on discretized radar heatmaps, which breaks geometric continuity and fails to capture key radar sensing properties, often leading to unstable pose estimation and degraded mapping in regenerate or dynamically changing environments. We present DiffRadar, a real-time radar SLAM system that models radar observations as a differentiable, physics-aware Gaussian field rather than discrete scans. DiffRadar represents the scene as anisotropic Gaussian primitives and renders radar measurements in range-azimuth and Doppler-azimuth spaces through a differentiable radar forward model, enabling joint optimization of robot pose and scene structure directly from radar measurements. We implement DiffRadar on commodity FMCW radar hardware and evaluate it on both the public Radarize benchmark and a controlled stress-test suite that targets common radar SLAM failure modes, including corridor degeneracy, motion regime transitions, dynamic clutter, and long-horizon loop closures. DiffRadar achieves substantial reductions in trajectory error on the benchmark, with especially large gains under feature-poor corridor motion, while more than doubling map consistency and maintaining real-time performance at 70 FPS. These results show that modeling radar observations directly in the signal domain enables substantially more robust and consistent radar-only SLAM for mobile platforms.

</details>

---

### [[20_Research/Papers/大模型/Contract-Grounded_Behavior_Tree_Synthesis_via_Coding_Agents|Contract-Grounded Behavior Tree Synthesis via Coding Agents]]

![[assets/2607.12220_figure.png|800]]

- **arXiv**: [2607.12220](https://arxiv.org/abs/2607.12220)
- **PDF**: https://arxiv.org/pdf/2607.12220
- **详细分析**: [[20_Research/Papers/大模型/Contract-Grounded_Behavior_Tree_Synthesis_via_Coding_Agents|Contract-Grounded Behavior Tree Synthesis via Coding Agents]]
- **作者**: Jonathan Salfity, Robert Blake Anderson, Mitch Pryor
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Contract-Grounded Behavior Tree Synthesis via Coding Agents》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PyRoboSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synthesizing deployable robot behavior trees (BTs) from natural language (NL) requires grounding to ensure every generated BT references only skills a robot can actually execute. Existing LLM-based BT synthesis approaches often place this grounding responsibility on the prompt author. This makes deployment brittle when the author does not know which skills the robot can execute, how those skills are parameterized, or how the robot runtime software constrains valid BT structure. This paper proposes a contract-grounded BT synthesis architecture in which a coding agent queries a robot-side Model Context Protocol (MCP) server to retrieve an explicit contract consisting of a skill library, permitted BT operators, and optional BT composition templates, before synthesizing a BT for validation and execution. In our framework, non-expert operators issue NL commands without knowledge of robot implementation details, while a robot runtime validation gate enforces correctness before execution. We evaluate two LLMs, a closed model (Sonnet 4.6) and a smaller open-source model (Gemma4:31b), across 110 simulated tasks in PyRoboSim and 14 tasks on a physical Husarion Panther robot. Results show that contract grounding enables near-perfect BT validation and high task success, that BT composition templates substantially recover success on reactive control-flow tasks for the smaller model, and that the architecture transfers to physical hardware running a Nav2 stack opaque to both operator and agent.

</details>

---

### [[20_Research/Papers/机器人/LQG_solution_for_POMDP_without_estimating_states_A_minimum_variance_approach|LQG solution for POMDP without estimating states: A minimum variance approach]]

![[assets/2607.12135_figure.png|800]]

- **arXiv**: [2607.12135](https://arxiv.org/abs/2607.12135)
- **PDF**: https://arxiv.org/pdf/2607.12135
- **详细分析**: [[20_Research/Papers/机器人/LQG_solution_for_POMDP_without_estimating_states_A_minimum_variance_approach|LQG solution for POMDP without estimating states: A minimum variance approach]]
- **作者**: Ranjan Sarkar, Prabhat K. Mishra
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: RL

#### 研究背景与动机

《LQG solution for POMDP without estimating states: A minimum variance approach》归入 强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates the control of discrete-time linear time-invariant (LTI) systems subject to incomplete and corrupted measurements. Specifically, we focus on designing a Linear Quadratic Gaussian (LQG) controller without relying on explicit state estimation. By leveraging minimum variance duality, our approach allows the current control input to be represented as a linear function of available measurements and previously applied inputs, successfully reducing the task to a tractable deterministic optimization problem. We provide theoretical justification for this framework and demonstrate its practical effectiveness through numerical experiments.

</details>

---

### [[20_Research/Papers/具身智能/More_than_a_Manipulator_Planning_Propellant-Free_Attitude_Maneuvers_for_Free-Floating_Spacecraft|More than a Manipulator: Planning Propellant-Free Attitude Maneuvers for Free-Floating Spacecraft]]

![[assets/2607.12130_figure.png|800]]

- **arXiv**: [2607.12130](https://arxiv.org/abs/2607.12130)
- **PDF**: https://arxiv.org/pdf/2607.12130
- **详细分析**: [[20_Research/Papers/具身智能/More_than_a_Manipulator_Planning_Propellant-Free_Attitude_Maneuvers_for_Free-Floating_Spacecraft|More than a Manipulator: Planning Propellant-Free Attitude Maneuvers for Free-Floating Spacecraft]]
- **作者**: Harsh G. Bhundiya, Avi Soval, Keenan Albee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《More than a Manipulator: Planning Propellant-Free Attitude Maneuvers for Free-Floating Spacecraft》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spacecraft attitude control is traditionally achieved using momentum exchange devices or propellant-consuming thrusters. Meanwhile, a growing number of missions require robotic manipulators, which are typically treated as disturbance sources to be rejected rather than as actuators for spacecraft reorientation. This work investigates the use of manipulator motions for propellant-free attitude control by formulating a trajectory optimization problem with critical joint and collision avoidance constraints. Using an interior point solver for the resulting nonlinear program, complex slew and detumble trajectories are demonstrated for a range of spacecraft-manipulator systems with varying kinematic complexity and mass properties. The achievable control authority is compared directly with that of reaction wheel arrays via momentum and torque envelopes, demonstrating the potential for manipulators to serve as redundant or even primary attitude control systems. This work provides a framework for using manipulators as multipurpose attitude control actuators, with particularly promising applications in in-space assembly and manufacturing when grasping payloads with high relative mass fractions.

</details>

---

### [[20_Research/Papers/具身智能/A_Behavioral_State_Vocabulary_in_Sony_ERS-111_R-CODE|A Behavioral State Vocabulary in Sony ERS-111 R-CODE]]

![[assets/2607.12115_figure.png|800]]

- **arXiv**: [2607.12115](https://arxiv.org/abs/2607.12115)
- **PDF**: https://arxiv.org/pdf/2607.12115
- **详细分析**: [[20_Research/Papers/具身智能/A_Behavioral_State_Vocabulary_in_Sony_ERS-111_R-CODE|A Behavioral State Vocabulary in Sony ERS-111 R-CODE]]
- **作者**: Christopher A. Tucker
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《A Behavioral State Vocabulary in Sony ERS-111 R-CODE》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a corpus-level analysis of generated behavior diagrams derived from Sony's R-CODE sample distribution for the ERS-111 AIBO. Rather than reading each script in isolation, the study compares named states across the corpus to identify the recurring control vocabulary that structures the sample set. The resulting aggregate shows that many superficially different routines are built from a compact embodied grammar centered on initialization, sensing, iterative action, synchronization, and recovery. In addition to historical analysis, the paper argues that this form of state-based abstraction is useful as an intermediate representation for constructing new encapsulated behavior routines, especially on constrained native robotic systems where deterministic control, direct hardware access, and modular behavioral composition remain important.

</details>

---

### [[20_Research/Papers/具身智能/EFLUX_Elastic_Multi-Robot_Formation_Navigation_and_Adaptation_with_Agentic_LLMs|EFLUX: Elastic Multi-Robot Formation Navigation and Adaptation with Agentic LLMs]]

![[assets/2607.12050_figure.png|800]]

- **arXiv**: [2607.12050](https://arxiv.org/abs/2607.12050)
- **PDF**: https://arxiv.org/pdf/2607.12050
- **详细分析**: [[20_Research/Papers/具身智能/EFLUX_Elastic_Multi-Robot_Formation_Navigation_and_Adaptation_with_Agentic_LLMs|EFLUX: Elastic Multi-Robot Formation Navigation and Adaptation with Agentic LLMs]]
- **作者**: Jinyuan Zhang, Yuwei Wu, Guangyao Shi, Jonathan Diller, Gaurav S. Sukhatme, Vijay Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《EFLUX: Elastic Multi-Robot Formation Navigation and Adaptation with Agentic LLMs》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LAMARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot teams operating in confined or cluttered environments must adapt both their formation geometry and group topology to navigate through complex obstacles. This adaptation requires two complementary behaviors: deformation, where the team continuously reshapes its geometry while remaining connected, and reconfiguration, where robots split into subgroups or merge back into a single formation. Existing methods often model these behaviors independently, connect them through handcrafted rules, or lack explicit geometric criteria for determining when each behavior should be invoked. However, challenging environments may require online changes in formation shape, connectivity, and effective team composition, making decoupled or rule-based approaches prone to suboptimal trajectories and deadlock. We propose EFLUX, a geometry-grounded LLM agentic framework for automatic and elastic multi-robot formation navigation. EFLUX extracts a structured scene representation and uses an LLM to reason jointly over both deformation actions, such as scaling and shearing, and reconfiguration actions, such as splitting and merging. These strategies are then translated into executable per-robot waypoints through a closed-loop generation, verification, and correction pipeline. Simulation and hardware experiments show that EFLUX enables safe, continuous, and elastic formation navigation in constrained environments, reducing deadlock and navigation failures compared with baselines while maintaining coherent multi-robot coordination.

</details>

---
