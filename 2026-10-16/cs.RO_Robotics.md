# cs.RO | Robotics | 2026-10-16

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/强化学习/Value_as_Memory_Online_Value-Guided_Post-training_for_General_Robot_Policies|Value as Memory: Online Value-Guided Post-training for General Robot Policies]]

![[assets/2610.22368_figure.png|800]]

- **arXiv**: [2610.22368](https://arxiv.org/abs/2610.22368)
- **PDF**: https://arxiv.org/pdf/2610.22368
- **详细分析**: [[20_Research/Papers/强化学习/Value_as_Memory_Online_Value-Guided_Post-training_for_General_Robot_Policies|Value as Memory: Online Value-Guided Post-training for General Robot Policies]]
- **作者**: Wenye Yu, Yijin Chen, Kaiyi Xiong, Wenbo Han, Wendi Chen, Yang Jin, Han Xue, Jun Lv, Cewu Lu, Chuan Wen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.4，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Value as Memory: Online Value-Guided Post-training for General Robot Policies》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CFGRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world post-training of generalist robot policies faces two challenges: partial observability makes action selection ambiguous, while offline post-training methods delay feedback from deployment experience. We present Value as Memory (VaM), a framework that addresses these challenges through value caching and online real-world reinforcement learning (RL). Value caching conditions actions on recent value predictions as task-progress memory, while online updates enable timely policy improvement by combining offline demonstrations, off-policy interventions, and on-policy rollouts for sample-efficient adaptation. As a result, VaM transitions from offline RL warmup to online autonomous learning with sparse rewards. Across long-horizon tasks involving deformable objects and contact-rich manipulation, VaM yields a mean absolute success-rate gain of $29.4\%$ with value caching, while achieving a $32.8\%$ gain with online autonomous learning over matched offline training. The evaluated online schedule performs $8\times$ as many policy iterations under the same gradient-step budget, with more than $2\times$ lower recorded time per gradient step with concurrent data collection and training.

</details>

---

### [[20_Research/Papers/强化学习/Spark-0_Scaling_Spatially_Aligned_Tactile_Pretraining_for_Robot_Dexterous_Manipulation|Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation]]

![[assets/2610.22342_first_page.png|800]]

- **arXiv**: [2610.22342](https://arxiv.org/abs/2610.22342)
- **PDF**: https://arxiv.org/pdf/2610.22342
- **详细分析**: [[20_Research/Papers/强化学习/Spark-0_Scaling_Spatially_Aligned_Tactile_Pretraining_for_Robot_Dexterous_Manipulation|Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation]]
- **作者**: Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

</details>

---

### [[20_Research/Papers/具身智能/Sim-to-Real_Reinforcement_Learning_for_Path-Safe_Target_Reaching_in_Robotic_Harvesting_of_Hydroponic_Lettuce|Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce]]

![[assets/2610.22337_figure.png|800]]

- **arXiv**: [2610.22337](https://arxiv.org/abs/2610.22337)
- **PDF**: https://arxiv.org/pdf/2610.22337
- **详细分析**: [[20_Research/Papers/具身智能/Sim-to-Real_Reinforcement_Learning_for_Path-Safe_Target_Reaching_in_Robotic_Harvesting_of_Hydroponic_Lettuce|Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce]]
- **作者**: Al Bashir, Partho Ghose, Yibin Wang, Robert G. Hardin, Joshua Peeples, Genhua Niu, Azlan Zahid
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.4（加权：具身智能 1.5，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Sim-to-Real Reinforcement Learning for Path-Safe Target Reaching in Robotic Harvesting of Hydroponic Lettuce》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic harvesting requires precise manipulation to ensure accurate positioning of the end-effector, especially in a constraint workspace. This study introduces the Path-Safe Approach Proximal Policy Optimization (PSA-PPO), a target-conditioned local reaching framework designed for robotic harvesting of nutrient film technique (NFT)-hydroponic lettuce in greenhouses. The proposed PSA-PPO preserves the standard clipped PPO objective while introducing a harvesting-oriented policy formulation that integrates target-conditioned observations, corridor-aware spatial constraints, trajectory-history-based safety encoding, and task-specific success criteria for constrained robotic manipulation. PSAPPO was trained entirely in Isaac Lab and successfully transferred to a physical UR10e robotic arm without any real-world policy fine-tuning. In a controlled physical benchmark against 150 scheduled targets, PSA-PPO achieved the highest reaching rate of 94.7%, outperforming Cartesian+TOTG (86.0%), RRTConnect (88.0%), and RRT* (80.0%), while reducing median RMS jerk by 39.8 to 73.0% relative to the classical planners during the final approach segment. A formulation ablation evaluated over 200 simulation targets demonstrates that path-safety and side-corridor shaping are the principal drivers of harvesting-compatible performance: removing either term substantially degrades strict success even when terminal endpoint accuracy is preserved or improved, confirming that optimization toward the endpoint alone is an insufficient objective for constrained crop-proximal manipulation. Finally, PSA-PPO was integrated with an RGB-D vision module and an end-effector and evaluated as a complete greenhouse harvesting system across 144 lettuce harvesting attempts, achieving 94.4% vision-guided target reaching and 86.1% complete harvesting success.

</details>

---

### [[20_Research/Papers/具身智能/Mem4Act_Learning_Effective_Latent_Memory_for_Long-Horizon_Robotic_Manipulation|Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation]]

![[assets/2610.22323_figure.png|800]]

- **arXiv**: [2610.22323](https://arxiv.org/abs/2610.22323)
- **PDF**: https://arxiv.org/pdf/2610.22323
- **详细分析**: [[20_Research/Papers/具身智能/Mem4Act_Learning_Effective_Latent_Memory_for_Long-Horizon_Robotic_Manipulation|Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation]]
- **作者**: Yun Zhang, Zhiyu Huang, Tianhui Cai, Chen Tang, Wei Wang, Jiaqi Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Mem4Act: Learning Effective Latent Memory for Long-Horizon Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FurnitureBench, RMBench, ReMem-VLA, Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robotic manipulation fundamentally requires memory: agents must retain task-relevant information from past observations and interactions and use it to guide future actions. Existing approaches typically preserve raw historical observations, compressed visual tokens, or language summaries, but these representations either expose the action policy to increasingly long histories or risk discarding task-relevant temporal, semantic, and perceptual information. We introduce Mem4Act, a framework for learning effective latent memory as a fixed-size representation explicitly optimized for long-horizon robotic control. Mem4Act addresses three coupled challenges: how to efficiently cover long histories, what information memory should retain, and how to ensure the policy actually relies on memory. To this end, it organizes history via multi-granularity temporal aggregation, preserves complementary semantic and perceptual information through question-answering supervision and key-frame DINO feature reconstruction, and employs memory-first two-stage training to encourage greater use of memory by the action policy. The resulting memory captures both high-level task state and fine-grained perceptual evidence while providing a bounded interface to the action policy. Across RoboMME, RMBench, and four real-world manipulation tasks, Mem4Act achieves state-of-the-art performance on memory-dependent control, with success rates of 49.88%, 61.0%, and 81.5%, respectively. Extensive ablations further demonstrate the importance of temporal aggregation, complementary memory supervision, and memory-first training.

</details>

---

### [[20_Research/Papers/具身智能/Auditable_and_Deployable_Multi-Agent_Motion_Planning_via_Posetal_Games_from_Legal_Guidelines|Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines]]

![[assets/2610.22277_first_page.png|800]]

- **arXiv**: [2610.22277](https://arxiv.org/abs/2610.22277)
- **PDF**: https://arxiv.org/pdf/2610.22277
- **详细分析**: [[20_Research/Papers/具身智能/Auditable_and_Deployable_Multi-Agent_Motion_Planning_via_Posetal_Games_from_Legal_Guidelines|Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines]]
- **作者**: Florian Lercher, Karan Mahesh, Yujun Huang, Meshal Alharbi, Runyu Zhang, Hanna Krasowski, Michael R. Benjamin, Matthias Althoff, Gioele Zardini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable. We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). Scenario-independent legal guidelines order abstract legal concerns, from which we automatically derive agent preferences and a legal game for any concrete scenario. Agents may refine their legal preferences with private objectives, and regulators may refine the guideline as laws evolve. We prove that such customizations can only remove equilibria and thus preserve legality. To coordinate agents without explicitly communicating private preferences, we introduce belief play, which provably recovers the true equilibria from conservative local games, and a distributed iterative best-response protocol requiring less information. We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters. On seven encounters with up to four vessels, every rule violation of the committed equilibria is certified as forced by the legal hierarchy or unsatisfiable, and defectors are identified from public information in all tested cases. These results indicate that guideline-based posetal games offer an auditable route from partially specified laws to multi-agent motion planning.

</details>

---

### [[20_Research/Papers/机器人/Safe_and_Fuel-Efficient_Motion_Planning_for_Lunar_Propulsive_Drones|Safe and Fuel-Efficient Motion Planning for Lunar Propulsive Drones]]

![[assets/2610.22225_figure.png|800]]

- **arXiv**: [2610.22225](https://arxiv.org/abs/2610.22225)
- **PDF**: https://arxiv.org/pdf/2610.22225
- **详细分析**: [[20_Research/Papers/机器人/Safe_and_Fuel-Efficient_Motion_Planning_for_Lunar_Propulsive_Drones|Safe and Fuel-Efficient Motion Planning for Lunar Propulsive Drones]]
- **作者**: Elena Wittemyer, Graco Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Safe and Fuel-Efficient Motion Planning for Lunar Propulsive Drones》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Propulsive drones are a promising new technology for generating high-resolution terrain models of the Moon. In future lunar missions, propulsive drones will complete a series of hops across the lunar surface while capturing images with downward-facing cameras. We present an autonomous motion planning framework that uses a vision-guided optimal control strategy for performing safe, efficient hops between specified waypoints. The drone plans parabolic hops between waypoints generated by a global-level planner; if a nominal waypoint is unsafe or unreachable, the drone then completes a diversion maneuver to safely land. To evaluate the validity of potential landing sites, we develop a custom semantic segmentation model for identifying obstacles from aerial images, and we introduce an approach for rapidly calculating reachable terrain. We then use model predictive control (MPC) to robustly track hop trajectories that guide the drone towards safe landing sites. We test the optimal hop planner in a high-fidelity lunar simulation environment. Our results demonstrate that our unified motion planning framework yields safe, fuel-efficient hop trajectories which can be tracked rapidly and with low error via MPC.

</details>

---

### [[20_Research/Papers/具身智能/MOSS_Mode-Oriented_Source_Shaping_for_Robot_Flow_Matching_Policies|MOSS: Mode-Oriented Source Shaping for Robot Flow Matching Policies]]

![[assets/2610.22193_figure.png|800]]

- **arXiv**: [2610.22193](https://arxiv.org/abs/2610.22193)
- **PDF**: https://arxiv.org/pdf/2610.22193
- **详细分析**: [[20_Research/Papers/具身智能/MOSS_Mode-Oriented_Source_Shaping_for_Robot_Flow_Matching_Policies|MOSS: Mode-Oriented Source Shaping for Robot Flow Matching Policies]]
- **作者**: Zirun Ma, Jindou Jia, Tuo An, Jiaqi Bai, Jiahua Dong, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《MOSS: Mode-Oriented Source Shaping for Robot Flow Matching Policies》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotic manipulation, the same observation often admits multiple feasible actions. Generative policies such as diffusion and flow matching naturally capture such multimodal behaviors, yet which mode is executed is left to random sampling and cannot be actively controlled. We propose Mode-Oriented Source Shaping (MOSS), which turns mode selection into an explicit choice of where generation starts. We first reveal, both empirically and theoretically, that deterministic flow transport induces mode-dependent structure in the source space. Under ideal deterministic ODE transport, distinct behavioral modes have distinct source-space preimages, while practical approximation errors can blur their boundaries due to imbalanced data, limited model capacity, and few inference steps. Motivated by this source-space structure, MOSS constructs semantically aligned mode-specific Gaussian sources that encode mode identity in the initial noise. A modality-strength estimator predicts the local degree of multimodality, which adaptively controls the geometry of the mode-specific sources. It contracts them toward a shared Gaussian where behaviors are similar and separates them near behavioral branching points. During deployment, the desired behavior is selected at inference simply by sampling from the corresponding component. Across 6 simulated and 3 real-world manipulation tasks, MOSS steers to the target mode up to 100% of the time with high task success, recovers minority modes at over 90% guidance rate under a 10:90 imbalance dataset, and surpasses mode-conditioned flow policy by 43.3 points of guidance rate on real robots.

</details>

---

### [[20_Research/Papers/世界模型/Inertially_Significant_Humanoid_Teleoperation_via_Whole_Body_Model_Predictive_Control_and_Online_Parameter_Estimation|Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation]]

![[assets/2610.22176_figure.jpg|800]]

- **arXiv**: [2610.22176](https://arxiv.org/abs/2610.22176)
- **PDF**: https://arxiv.org/pdf/2610.22176
- **详细分析**: [[20_Research/Papers/世界模型/Inertially_Significant_Humanoid_Teleoperation_via_Whole_Body_Model_Predictive_Control_and_Online_Parameter_Estimation|Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation]]
- **作者**: James Foster, Beomyeong Park, Luigi Penco, Robert Griffin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.0（加权：具身智能 1.5，世界模型 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The effective deployment of humanoid robots in practical tasks of interest will require a capability of sensing and adapting to variations in inertial parameters, as occurs during heavy tool use or when carrying significant payload. Such payloads constitute a significant proportion of the combined payload-robot system, the effects of which cannot be ignored by delegating to feedback control. This paper showcases a general solution to this problem by integrating a whole body model predictive controller (WB-MPC) with an extended Kalman filter (EKF) for online estimation of fully physically consistent time-varying inertial parameters. These estimates are fed through to the WB-MPC's full rigid body dynamics model, resulting in more accurate feedforward torques for task demands under external load. Additionally, a virtual reality (VR) interface is provided that enables an operator to provide task-specific references without regard to payload while delegating dynamic balance to the WB-MPC. The framework is validated with simulation and hardware experiments on a humanoid system.

</details>

---

### [[20_Research/Papers/具身智能/FastVLA_Task-Conditioned_and_Temporally_Adaptive_Visual_Token_Compression_for_Efficient_Vision-Language-Action_Models|FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models]]

![[assets/2610.22146_figure.jpg|800]]

- **arXiv**: [2610.22146](https://arxiv.org/abs/2610.22146)
- **PDF**: https://arxiv.org/pdf/2610.22146
- **详细分析**: [[20_Research/Papers/具身智能/FastVLA_Task-Conditioned_and_Temporally_Adaptive_Visual_Token_Compression_for_Efficient_Vision-Language-Action_Models|FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models]]
- **作者**: Jiuyi Xu, Chengyuan Qian, Zhengzhong Tu, Yang Sui, Yangming Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression for Efficient Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EfficientVLA, FastVLA, FlashVLA, LightVLA, OpenVLA, SpecPrune-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models present a promising paradigm for general-purpose robot manipulation, but closed-loop deployment is often limited by inference efficiency: at each timestep, high-resolution, often multi-view images are encoded into hundreds of visual tokens that dominate transformer computation and latency. Token compression via attention is a natural solution but is challenging for VLA control because (1) decision-critical tokens are determined by the task, not generic visual saliency, and (2) the token budget varies substantially across steps, so static metrics and budgets waste computation or discard control-critical tokens. We introduce FastVLA, a training-free, task-aware, and temporally adaptive visual token compression framework. At each step, FastVLA scores token importance via task-to-vision attention and adaptively sets the compression rate from the importance-distribution uniformity, measured by an inverse-Simpson metric with online sliding-window calibration. We evaluate FastVLA on OpenVLA, OpenVLA-OFT, and CogACT across LIBERO and SIMPLER, and on a physical Franka Research 3 robot. In simulation, it reduces LLM-backbone FLOPs by 35-59\% and action latency by 9-32\% (a 1.09$\times$-1.46$\times$ speedup) while maintaining task success, achieving a comparable or better efficiency-performance trade-off than existing plug-and-play token compression/pruning/reuse baselines. On the real robot, it cuts end-to-end latency by 20\% (1.25$\times$ speedup) at comparable success. Code is available at https://github.com/jiuyixu25/FastVLA.

</details>

---

### [[20_Research/Papers/机器人/Compliant_GMT_Making_General_Motion_Tracking_Compliant_via_Residual_Reference_Adaptation|Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation]]

![[assets/2610.22119_figure.png|800]]

- **arXiv**: [2610.22119](https://arxiv.org/abs/2610.22119)
- **PDF**: https://arxiv.org/pdf/2610.22119
- **详细分析**: [[20_Research/Papers/机器人/Compliant_GMT_Making_General_Motion_Tracking_Compliant_via_Residual_Reference_Adaptation|Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation]]
- **作者**: Venki Parsuram, Michelle Wang, Jin-Hyuk Hong, Pulkit Agrawal
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose Compliant GMT (C-GMT), a modular framework for full-body compliant responses in general motion tracking. As humanoid robots move into real world deployment, they not only need to perform any motion but also respond safely and robustly to interaction forces. Existing general motion tracking policies can imitate diverse motions but are trained to be stiff, leading to unexpected and unsafe behaviors under disturbance. Prior work in compliant humanoid control trades off compliance and generality. There exist examples of full-body compliant responses, but these are heavily curated to single-reference policies. On the other hand, general motion trackers (GMT) are trained to rigidly imitate massive motion capture datasets. Our key insight is to leverage the generality of pretrained GMTs for motion tracking while introducing compliance from a residual adapter that conditions on a history of proprioception. This enables our approach, C-GMT, to achieve both general motion tracking and whole-body compliant responses. Compared to state-of-the-art general motion trackers and single-motion compliant policies, C-GMT demonstrates competitive performance in both motion tracking accuracy and compliance adherence. We further demonstrate improved safety, robustness, and error tolerance in simulation and real-world G1 experiments.

</details>

---

### [[20_Research/Papers/具身智能/Onboard_Lightweight_LLM_Reasoning_for_Human-Aware_Safe_UAV_Navigation|Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation]]

![[assets/2610.22092_figure.png|800]]

- **arXiv**: [2610.22092](https://arxiv.org/abs/2610.22092)
- **PDF**: https://arxiv.org/pdf/2610.22092
- **详细分析**: [[20_Research/Papers/具身智能/Onboard_Lightweight_LLM_Reasoning_for_Human-Aware_Safe_UAV_Navigation|Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation]]
- **作者**: Siwei Cai, Yuwei Wu, Vijay Kumar, Lifeng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Onboard Lightweight LLM Reasoning for Human-Aware Safe UAV Navigation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial robots operating near people must treat a pedestrian, a parked car, and a wall differently, yet conventional perception--planning stacks reduce all of them to occupied geometry---a \emph{human-aware safety gap} in which category-specific clearance is unavailable to the planner and temporary occlusions remove pedestrian-specific constraints from its map. We present a modular, fully onboard pipeline that closes this gap by turning visual observations into context-dependent safety constraints for real-time UAV navigation. A shared BLIP encoder drives scene captioning and text-conditioned segmentation, which is fused with depth to localize obstacles in 3D. Obstacle-specific risk is inferred by a lightweight LLM (Qwen-2.5-0.5B) stabilized with retrieval-augmented generation and grammar-constrained decoding that restricts its output to a planner-compatible JSON schema. The LLM reasons once per object category rather than per frame: its verdicts are cached per class, so previously seen categories are resolved without inference and new ones trigger a fresh retrieval-grounded query; detections are additionally given persistent identities and held in the map across occlusions. The perception pipeline runs at 10\,Hz on a Jetson Orin NX, while fallback LLM queries take approximately 0.8\,s and remain off the control-critical path. In Gazebo, low-altitude urban navigation among pedestrians and vehicles shows a roughly $3\times$ reduction in collision events over a geometric planner, and semantics-aware landing among moving actors raises success from 34\% to 96\%. The 224-pixel encoder input limits reliable small-object perception at range; conservative pedestrian margins and short-term persistence mitigate this limitation during navigation.

</details>

---

### [[20_Research/Papers/具身智能/VP-EVT_Active_Visibility_Preservation_for_Embodied_Visual_Tracking|VP-EVT: Active Visibility Preservation for Embodied Visual Tracking]]

![[assets/2610.21999_figure.png|800]]

- **arXiv**: [2610.21999](https://arxiv.org/abs/2610.21999)
- **PDF**: https://arxiv.org/pdf/2610.21999
- **详细分析**: [[20_Research/Papers/具身智能/VP-EVT_Active_Visibility_Preservation_for_Embodied_Visual_Tracking|VP-EVT: Active Visibility Preservation for Embodied Visual Tracking]]
- **作者**: Yanci Wen, Tianle Zeng, Jianwei Peng, Weixi Situ, Hanjing Ye, Hong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《VP-EVT: Active Visibility Preservation for Embodied Visual Tracking》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OccEVT-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Visual Tracking (EVT) is an essential capability for intelligent robots in human-robot collaboration, requiring an agent to follow a designated target person in dynamic environments relying solely on egocentric visual perception. However, persistent pedestrian occlusions in dynamic scenes pose critical challenges to existing EVT methods. Lacking proactive visibility preservation, reactive tracking methods frequently experience prolonged target loss under severe occlusions. Therefore, we propose VP-EVT, a framework that treats target visibility as an explicit objective of motion control rather than a by-product of following. Acting on this objective requires understanding both what obstructs the target and how robot motion can change that obstruction. VP-EVT therefore uses language-guided perception to extract separate target and pedestrian observations. When occlusion makes current observations incomplete, VP-EVT combines visual history with ego-motion to maintain estimates of their relative positions and motion. Using these estimates and the current following waypoints, VP-EVT predicts whether continued following will sustain the obstruction. When the predicted risk is low, the original following motion is retained; otherwise, a recurrent controller combines updated estimates with maneuver context from preceding decisions to coordinate viewpoint adjustment and the return to stable following. Moreover, we introduce OccEVT-Bench for closed-loop evaluation of persistent occlusion and collect expert demonstrations for training. On its Risk split, VP-EVT improves success rate by 121.4% relative to a competitive baseline and reduces visibility deficit and longest target-loss duration by 78.8% and 74.4%, respectively.

</details>

---

### [[20_Research/Papers/具身智能/VeriVLA_Adaptive_Test-Time_Verification_for_Flow-Based_VLAs_with_Latent_World_Models|VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models]]

![[assets/2610.21985_figure.png|800]]

- **arXiv**: [2610.21985](https://arxiv.org/abs/2610.21985)
- **PDF**: https://arxiv.org/pdf/2610.21985
- **详细分析**: [[20_Research/Papers/具身智能/VeriVLA_Adaptive_Test-Time_Verification_for_Flow-Based_VLAs_with_Latent_World_Models|VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models]]
- **作者**: Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.0（加权：具身智能 0.9，世界模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EVOLVE-VLA, TT-VLA, VeriVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the critical states. Once triggered, a JEPA-based latent world model ranks candidate action chunks by predicting action-conditioned future latent states and the corresponding changes in task progress. By operating in latent space, the verifier avoids pixel reconstruction and enables efficient and more accurate ranking. Across three real-world tasks, $\textit{i.e.,}$ pen insertion, pipetting, and apple placement), our method raises the average completion score from 50.8% to 65.5%, while adding 326 ms for sampling and verification per triggered decision on a single RTX 4090. Consistent gains are also observed in simulation, where the average success rate rises from 66.4% to 73.6% in the clean setting of RoboTwin 2.0, from 62.8% to 69.6% in its randomized setting, and from 96.9% to 97.6% on LIBERO.

</details>

---

### [[20_Research/Papers/机器人/De-Risking_Robotic_Welding_for_In-Space_Metal_Joining_Through_Physics-Grounded_Digital_Twins|De-Risking Robotic Welding for In-Space Metal Joining Through Physics-Grounded Digital Twins]]

![[assets/2610.21939_figure.png|800]]

- **arXiv**: [2610.21939](https://arxiv.org/abs/2610.21939)
- **PDF**: https://arxiv.org/pdf/2610.21939
- **详细分析**: [[20_Research/Papers/机器人/De-Risking_Robotic_Welding_for_In-Space_Metal_Joining_Through_Physics-Grounded_Digital_Twins|De-Risking Robotic Welding for In-Space Metal Joining Through Physics-Grounded Digital Twins]]
- **作者**: Zhou Daniel Hao, Umer Masood Chaudry, Robert Shaw, Andrew Cheney, Nick Ludford, Mark Sims, Hongbiao Dong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《De-Risking Robotic Welding for In-Space Metal Joining Through Physics-Grounded Digital Twins》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Growing interest in in-space servicing, manufacturing, and assembly has renewed attention on reliable metal joining for modular construction and on-orbit repair. Robotic welding is promising, but reduced-gravity and low-pressure operation remains poorly characterised and flight-like tests are limited. The UK Space Agency-supported ISPARK project is developing a physics-grounded digital twin for structured process de-risking. This paper evaluates a model-based prototype combining a finite-volume thermal weld-pool model, Gaussian-process (GP) and neural-network surrogates, and a simulated six-axis manipulator. The reduced model includes solid-liquid phase change, effective thermocapillary transport, and a local-pressure parameter. Gravity is assessed separately through a hydrostatic-to-capillary pressure ratio and does not enter the thermal energy equation. Across repeated five-fold cross-validation, the GP has lower normalised mean absolute error than the neural network for all eight outputs. In 10 held-out boundary cases, 74 of 80 solver responses fall within nominal 90% GP predictive intervals. A three-output GP query takes 249 microseconds, including scaling and predictive variance. In a simulated UR5 L-shaped-seam study, a proportional controller adjusts the synergic power-source setting as travel speed falls near the corner. Finite-volume re-evaluation finds all 12 closed-loop operating points and 9 of 12 open-loop points within an illustrative 1.0-3.0 mm root-side-width band. These simulation results support using the framework to screen welding conditions and control strategies before experimental tests. Thermal-vacuum, targeted reduced-gravity, and robotic hardware-in-the-loop studies are needed to assess the model and controller.

</details>

---

### [[20_Research/Papers/具身智能/TS-WAM_Temporal_Latent_Actions_and_World-Action_Coupling_for_Vision-Language_Robot_Control|TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control]]

![[assets/2610.21922_figure.png|800]]

- **arXiv**: [2610.21922](https://arxiv.org/abs/2610.21922)
- **PDF**: https://arxiv.org/pdf/2610.21922
- **详细分析**: [[20_Research/Papers/具身智能/TS-WAM_Temporal_Latent_Actions_and_World-Action_Coupling_for_Vision-Language_Robot_Control|TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control]]
- **作者**: Menghao Yin, Jiaju Yin, Xiyue Dong, Lixin Xu, Zhenhui Zhang, Ke Zhang, Yating Feng, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TS-WAM: Temporal Latent Actions and World-Action Coupling for Vision-Language Robot Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many vision-language-action policies rely on action-labeled robot demonstrations and lack an explicit mechanism for predicting future visual states. These limitations hinder learning from action-free videos and can encourage overfitting to demonstration conditions, weakening generalization and robustness. We present TS-WAM, a lightweight Teacher-Student World-Action Model that addresses these challenges through self-supervised temporal learning and explicit future prediction. Its vlm-jepa framework learns from heterogeneous data, including robot demonstrations and action-free human videos, using an EMA target branch without requiring a separately trained external teacher. By coupling vlm-jepa with delta-lwm, TS-WAM learns to predict latent actions from the current observation and instruction and uses them to predict future visual features that guide action generation at inference. A unified end-to-end training architecture jointly optimizes temporal representation learning, visual dynamics, and robot control without a separate latent-action or world-model pretraining stage. The EMA target branch is removed at inference, keeping the deployed policy lightweight. Experiments on LIBERO, LIBERO-Plus, and SimplerEnv, together with real-world manipulation experiments on Franka Research 3 and RevoTron, demonstrate that TS-WAM achieves strong manipulation performance, generalization, and robustness.

</details>

---

### [[20_Research/Papers/具身智能/What_Should_Robot_Policies_Learn_to_Predict_Rethinking_Supervision_Targets_in_Vision-Language-Action_Learning|What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning]]

![[assets/2610.21915_figure.png|800]]

- **arXiv**: [2610.21915](https://arxiv.org/abs/2610.21915)
- **PDF**: https://arxiv.org/pdf/2610.21915
- **详细分析**: [[20_Research/Papers/具身智能/What_Should_Robot_Policies_Learn_to_Predict_Rethinking_Supervision_Targets_in_Vision-Language-Action_Learning|What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning]]
- **作者**: Haitao Shen, Hanyu Liu, Yihan Lin, Huiping Liu, Junbo Cui, Daoheng Li, Yang Li, Jing Zhang, Wenxin Li, Yuan Yao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LARYBench, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies are typically trained with action prediction as the primary supervision signal, since robots ultimately execute actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV) prediction are often added to improve policy learning, yet they compete with action prediction for the same training budget. We ask whether, under a fixed budget, allocating a substantial share of training samples to such objectives, rather than to further action prediction, can improve policy learning. We build a unified VLA framework that couples a two-stream multimodal diffusion transformer (MMDiT) with a sample-level router, which assigns each training sample to either action prediction or an auxiliary objective and thus makes supervision allocation explicit. Within this framework, we instantiate three LA targets based on LAPA and its DINO-feature variants, and three FV targets based on DINOv3, V-JEPA 2, and Wan2.2 representations. Across LIBERO, CALVIN, and four real-robot tasks, suitable LA and FV supervision outperforms action-only training under the same budget, even when action prediction receives no more than half of the training samples. FV generally outperforms LA, although the strongest LA target remains competitive on CALVIN. Diagnostic analyses suggest that DINO-based LA targets emphasize relative motion, whereas FV targets emphasize absolute position and task identity. We therefore argue that what robot policies learn to predict, and how training is allocated among these targets, should be treated as explicit design choices rather than defaulting to action-dominant training.

</details>

---

### [[20_Research/Papers/机器人/Sub-Millisecond_Reflexes_for_Continuous_Physical_Human-Robot_Interaction|Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction]]

![[assets/2610.21913_figure.png|800]]

- **arXiv**: [2610.21913](https://arxiv.org/abs/2610.21913)
- **PDF**: https://arxiv.org/pdf/2610.21913
- **详细分析**: [[20_Research/Papers/机器人/Sub-Millisecond_Reflexes_for_Continuous_Physical_Human-Robot_Interaction|Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction]]
- **作者**: Jon Škerlj, Sami Haddadin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Sub-Millisecond Reflexes for Continuous Physical Human-Robot Interaction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous physical human-robot interaction requires robots to rapidly adapt their control behaviour without interrupting task execution. However, existing ROS 2 control architectures rely on stop-to-switch mechanisms that introduce substantial delays and interrupt execution. We present an open-source, sub-millisecond reflex engine based on an enhanced ROS 2-compatible multimode controller that enables deterministic switching between control modalities and integrates reflex behaviours for mitigating contact hazards and kinematic limit violations. Experiments on a Franka Robotics manipulator demonstrate switching delays below 0.1 ms, more than four orders of magnitude faster than conventional ros2_control, while maintaining continuous operation during safety-critical events. In a multi-stage manipulation task, the proposed framework reduced execution time by 3.5% and peak trajectory jerk by more than threefold. By eliminating runtime middleware overhead, controller transitions are implemented as lock-free pointer operations, enabling reflex-level responsiveness within an open-source robotics framework.

</details>

---

### [[20_Research/Papers/机器人/Time-Optimal_Ergodic_Retrieval|Time-Optimal Ergodic Retrieval]]

![[assets/2610.21823_figure.png|800]]

- **arXiv**: [2610.21823](https://arxiv.org/abs/2610.21823)
- **PDF**: https://arxiv.org/pdf/2610.21823
- **详细分析**: [[20_Research/Papers/机器人/Time-Optimal_Ergodic_Retrieval|Time-Optimal Ergodic Retrieval]]
- **作者**: Christian Sulana, Christian Hughes, Ian Abraham
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Time-Optimal Ergodic Retrieval》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval tasks are a form of search task where a robot must explore, find an object, and return with it as quickly as possible. Recent work in ergodic control has demonstrated time-optimal path planning for search tasks where visitation is proportionally matched, within some tolerance, to a given target distribution. However, these planners minimize the duration of a full deterministic search, while retrieval missions end their search at an unknown point in the trajectory and must return to a given base. In this work, we propose a new formulation of the time-optimal ergodic search problem that models detection as a Poisson process and minimizes total mission time by including the return phase in the objective. Experimental results show that time-optimal ergodic retrieval (TOER) achieves up to $19\%$ shorter mission durations relative to ergodic baselines and that this advantage grows as the return phase becomes more costly. Simulation and hardware implementations validate TOER's compatibility with environments of non-convex geometry as well as both 2D and 3D search domains.

</details>

---

### [[20_Research/Papers/具身智能/Uni-PNP_Unified_Prehensile_and_Non-prehensile_Policy_Learning_for_Generalizable_Object_Pose_Reaching|Uni-PNP: Unified Prehensile and Non-prehensile Policy Learning for Generalizable Object Pose Reaching]]

![[assets/2610.21735_figure.png|800]]

- **arXiv**: [2610.21735](https://arxiv.org/abs/2610.21735)
- **PDF**: https://arxiv.org/pdf/2610.21735
- **详细分析**: [[20_Research/Papers/具身智能/Uni-PNP_Unified_Prehensile_and_Non-prehensile_Policy_Learning_for_Generalizable_Object_Pose_Reaching|Uni-PNP: Unified Prehensile and Non-prehensile Policy Learning for Generalizable Object Pose Reaching]]
- **作者**: Wenxuan Zhu, Yuze Wang, Jiangran Lyu, Jiayi Chen, Yixin Zheng, Mi Yan, Li Yi, Zhizheng Zhang, He Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.1（加权：具身智能 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Uni-PNP: Unified Prehensile and Non-prehensile Policy Learning for Generalizable Object Pose Reaching》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DexGraspNet, PointNet, PointPatchRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object manipulation often requires combining non-prehensile actions with grasping. However, existing approaches typically develop these capabilities separately and integrate them by sequencing distinct primitives through prescribed intermediate objectives, limiting the coordination of contact motions and grasping. Their integration also remains sensitive to object and gripper geometry and depends on particular environmental supports, complicating real-world deployment. We present Uni-PNP, a unified policy that jointly learns prehensile and non-prehensile manipulation for object pose reaching across diverse objects and grippers. To achieve this, we first pretrain a geometry encoder to predict contact-induced object motion using a contact-dynamics dataset constructed from simulated interactions between diverse objects and grippers. We then train the policy in a two-stage reinforcement learning curriculum from graspable objects to ungraspable peers, encouraging the discovery of non-prehensile interactions and their integration with grasping. Experiments show 76.39% success on hundreds of seen objects with grippers, and 57.91% on unseen peers, outperforming the strongest pose-reaching baseline by 20.52 and 17.79 percentage points, respectively. We also analyze emergent behaviors, including nonprehensile and prehensile repositioning, grasp acquisition that requires grasping after tipping, and table-assisted reorientation while grasping, and transfer to the real-world scenario. Project page available at lgswdn.github.io/Uni-PNP.

</details>

---

### [[20_Research/Papers/大模型/MAIA_Anticipating_Interaction_Anomalies_in_Contact-Rich_Manipulation_via_Multimodal_World_Models|MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models]]

![[assets/2610.21686_figure.png|800]]

- **arXiv**: [2610.21686](https://arxiv.org/abs/2610.21686)
- **PDF**: https://arxiv.org/pdf/2610.21686
- **详细分析**: [[20_Research/Papers/大模型/MAIA_Anticipating_Interaction_Anomalies_in_Contact-Rich_Manipulation_via_Multimodal_World_Models|MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models]]
- **作者**: Yi Qiao, Maolin Zheng, Haoran Sun, Lujia Dong, Wenzhao Lian
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，世界模型 0.8）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models》归入 世界模型、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable contact-rich manipulation requires detecting execution deviations early enough for corrective action. Yet most monitoring methods are reactive, identifying anomalies only after they become observable. Anticipating such anomalies is challenging because visual observations only partially reveal physical interaction, while planned actions describe intended motion rather than their actual physical consequences. We address this problem with MAIA, a multimodal framework for anomaly anticipation. Its vision-action-force world model learns nominal interaction dynamics and predicts the visual and force responses of planned actions, while a lightweight anomaly head predicts impending interaction anomalies. To enable systematic evaluation, we introduce CRIA, a real-world multimodal dataset of 2,852 trajectories spanning 18 contact-rich manipulation tasks, with frame-level annotations of anomaly onset and evolution. Experiments on both seen and novel tasks show that MAIA achieves more accurate anomaly discrimination than representative baselines while providing earlier warnings, with bACC scores of 0.765 and 0.710 and median anticipation lead times of 28.0 and 25.1 steps, respectively. Moreover, using these predictions for anomaly-aware action selection improves end-to-end task success from 52.6% to 61.5% without retraining the underlying manipulation policy. These results highlight the value of modeling future physical consequences for proactive anomaly anticipation.

</details>

---

### [[20_Research/Papers/具身智能/SPEAR_Selective_Preference_Elicitation_with_Adaptive_Rewards_for_VLM-Guided_Robotic_Manipulation|SPEAR: Selective Preference Elicitation with Adaptive Rewards for VLM-Guided Robotic Manipulation]]

![[assets/2610.21621_figure.png|800]]

- **arXiv**: [2610.21621](https://arxiv.org/abs/2610.21621)
- **PDF**: https://arxiv.org/pdf/2610.21621
- **详细分析**: [[20_Research/Papers/具身智能/SPEAR_Selective_Preference_Elicitation_with_Adaptive_Rewards_for_VLM-Guided_Robotic_Manipulation|SPEAR: Selective Preference Elicitation with Adaptive Rewards for VLM-Guided Robotic Manipulation]]
- **作者**: Zewen Wu, Ruizhe Liu, Pei Zhou, Feng Chen, Yanchao Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SPEAR: Selective Preference Elicitation with Adaptive Rewards for VLM-Guided Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-World, PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Vision-Language Models (VLMs) enable automated preference labeling for robotic manipulation, yet their deployment remains impractical since each query incurs substantial inference cost, while VLMs frequently abstain on visually challenging comparisons. We propose SPEAR, a framework that transforms VLMs into efficient preference oracles via two synergistic mechanisms. First, we design distinguishability-aware query selection to reduce abstention rates by targeting only informative and distinguishable comparisons. Second, we deploy an adaptive reward transition that bootstraps exploration with VLM-synthesized guidance before preference-based refinement. Experiments on the manipulation benchmarks demonstrate that SPEAR achieves 88.9% average success, outperforming baselines by 23.3 percentage points, while significantly reducing abstention and wall-clock training time on contact-rich tasks. SPEAR learns three Mobile ALOHA manipulation tasks fully online on real hardware, demonstrating end-to-end real-world applicability. By addressing query efficiency and exploration challenges, SPEAR establishes VLMs as practical preference oracles for scalable robot learning without manual reward engineering.

</details>

---

### [[20_Research/Papers/大模型/A_Flow-Theoretic_Multimodal_Control_Framework_Fusing_Mental_and_Physical_Engagement_for_Upper-Limb_Rehabilitation|A Flow-Theoretic Multimodal Control Framework Fusing Mental and Physical Engagement for Upper-Limb Rehabilitation]]

![[assets/2610.21590_figure.jpg|800]]

- **arXiv**: [2610.21590](https://arxiv.org/abs/2610.21590)
- **PDF**: https://arxiv.org/pdf/2610.21590
- **详细分析**: [[20_Research/Papers/大模型/A_Flow-Theoretic_Multimodal_Control_Framework_Fusing_Mental_and_Physical_Engagement_for_Upper-Limb_Rehabilitation|A Flow-Theoretic Multimodal Control Framework Fusing Mental and Physical Engagement for Upper-Limb Rehabilitation]]
- **作者**: Jun Leng, Pengcheng Li, Hanze Wang, Shuxiang Guo, Junlin Jiang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《A Flow-Theoretic Multimodal Control Framework Fusing Mental and Physical Engagement for Upper-Limb Rehabilitation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Assist-as-Needed (AAN) control aims to maximize user participation in robot-assisted training, existing methods relying solely on physical metrics cannot distinguish muscular inability from mental disengagement, leading to suboptimal interventions. To address this ambiguity, a Flow-theoretic multimodal AAN framework is proposed, fusing EEG-based mental engagement and sEMG-based physical engagement into an adaptive impedance control strategy. A four-quadrant fuzzy decision engine translates these dual physiological metrics into continuous control policies. This enables the upper-limb exoskeleton to inject feedforward assistance during intent-execution mismatch (e.g., motor output attenuation despite mental focus) and escalate guiding stiffness to penalize mental distraction. The framework was validated with healthy participants against a state-of-practice sEMG-only AAN baseline. Kinematically and mechanically, the proposed framework reduced robotic energy expenditure by 71.9\% while maintaining precise trajectory tracking, confirming it elicited greater voluntary human effort. Physiologically, the system increased the time spent in the neuroplasticity zone (Flow State Ratio) from 4.6% to 42.8%. These results validate that decoupling and jointly regulating mental and physical states enhances the selectivity of robotic assistance, mitigating user passivity and sustaining the engagement crucial for motor learning.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Teacher_On-Policy_Distillation_for_Flow-Based_Vision-Language-Action_Models|Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models]]

![[assets/2610.21522_figure.png|800]]

- **arXiv**: [2610.21522](https://arxiv.org/abs/2610.21522)
- **PDF**: https://arxiv.org/pdf/2610.21522
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Teacher_On-Policy_Distillation_for_Flow-Based_Vision-Language-Action_Models|Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models]]
- **作者**: Lichao Ni, Yuhan Liu, Pengfei Li, Guanghuan Fang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DualVLA, MergeVLA, Meta-World, MetaWorld, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Specialized vision-language-action (VLA) policies acquire strong domain-specific skills, yet consolidating these skills into one shared policy remains challenging. On-policy distillation (OPD) transfers teacher knowledge on inputs induced by the student, addressing the distribution mismatch encountered during deployment. For flow-based VLAs, this mismatch arises at two levels: environment observations and intermediate action-generation states. We propose a two-level on-policy distillation framework that couples student-driven environment interaction with teacher velocity supervision along student-generated action flow trajectories. Frozen domain specialists jointly supervise one student. After each update, the student collects new environment experience and generates fresh action-flow trajectories. Starting from a joint supervised fine-tuning (SFT) initialization, Velocity Loss OPD yields absolute success-rate gains of 22.55% on LIBERO-40, 33.4% on CALVIN five-instruction sequences, and 22.6% on Meta-World MT50. Compared with Action Loss OPD and Teacher-rollout SFT, it achieves absolute success-rate gains of 6.4-9.5% on LIBERO-40, 9.7-18.3% on CALVIN, and 3.2-4.2% on Meta-World MT50. Analysis by sequence length further shows larger success-rate gains on longer CALVIN sequences. These results demonstrate effective multi-domain capability consolidation through two-level on-policy supervision, with a single student deployed across domains.

</details>

---

### [[20_Research/Papers/大模型/TRACE_Typed_Reference-Aware_Conversational_Editing_for_Humanoid_Motion_Diffusion|TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion]]

![[assets/2610.21515_figure.png|800]]

- **arXiv**: [2610.21515](https://arxiv.org/abs/2610.21515)
- **PDF**: https://arxiv.org/pdf/2610.21515
- **详细分析**: [[20_Research/Papers/大模型/TRACE_Typed_Reference-Aware_Conversational_Editing_for_Humanoid_Motion_Diffusion|TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion]]
- **作者**: Zejian Kang, Yifu Luo, Boyang Shen, Jingxuan Li, Zekai Chen, Zekun Shi, Yongxue Xu, Zhenyu Hou, Bingqian Wu, Shaolei Zhang, Wentao Yang, Xiangru Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-conditioned humanoid motion generation enables users to create and refine robot movements through natural language. The central challenge is to connect an underspecified request to concrete motion structure that can subsequently be revised relative to an accepted reference. We present TRACE, a generation and editing framework for the Unitree G1 humanoid robot built around typed, measurable kinematic quantities. Our insight is to ground generation conditions in paired training motions and editing goals in the current motion. A language model learns to predict support, root, and hand events from motion-derived supervision; their time-aligned encodings complement the original text in a diffusion generator. Gravity-referenced states and trajectory--contact objectives improve kinematic consistency. For editing, typed requests define body--time scopes and source-relative goals. A separate reference-conditioned diffusion editor uses these goals and revised events to realize changes, while sampling-time projection preserves protected state coordinates. Quantitative evaluation and human assessment show improved semantic alignment and motion quality over the compared methods. Controlled ablations support the value of motion-grounded conditioning and kinematic consistency, while multi-turn editing evaluations demonstrate more reliable execution of successive relative requests under shared preservation constraints. Together, these results support typed kinematic structure as a common basis for motion generation and reference-aware revision.

</details>

---

### [[20_Research/Papers/具身智能/Fast-VLA_You_Only_Think_Once_for_Robot_Manipulation|Fast-VLA: You Only Think Once for Robot Manipulation]]

![[assets/2610.21389_figure.png|800]]

- **arXiv**: [2610.21389](https://arxiv.org/abs/2610.21389)
- **PDF**: https://arxiv.org/pdf/2610.21389
- **详细分析**: [[20_Research/Papers/具身智能/Fast-VLA_You_Only_Think_Once_for_Robot_Manipulation|Fast-VLA: You Only Think Once for Robot Manipulation]]
- **作者**: Kehong Gong, Guanli Hou, Xiaoxu Zheng, Qi Wang, Mingxi Xu, Anbang Zhai, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.0（加权：具身智能 2.7，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Fast-VLA: You Only Think Once for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Fast-VLA, FastVLA, HyperVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies commonly place a multi-billion-parameter model inside the feedback loop, repeatedly recomputing task context whenever they predict a new action chunk. Yet task understanding changes far more slowly than the robot state. We introduce Fast-VLA, which invokes a frozen 4B VLM once per episode to contextualize the instruction and initial views as fixed, multi-layer key-value task memory. During execution, a lightweight online actor fuses learned time- and arm-indexed queries with current visual and proprioceptive feedback to form action queries. These queries retrieve task context from the fixed memory and predict action chunks without re-running the foundation model. Fast-VLA achieves 92.46% and 92.40% success on RoboTwin 2.0 Clean and Randomized, and 95.95% and 79.11% on LIBERO and LIBERO-Plus evaluation. Against three continually conditioned baselines on the same hardware, it reduces RoboTwin amortized policy inference time by 10.9-17.1x and requires 1.22 GiB of post-prefill online resident memory. Task-memory swaps further show that the actor relies on episode-matched task memory. These results show that task context can be established once while closed-loop control remains responsive throughout execution. Project page: https://garfield-kh.github.io/FastVLA

</details>

---

### [[20_Research/Papers/具身智能/From_Optical_Flow_to_Safety_Visual_Safety_Certification_via_Scale-Free_Relative_Motion|From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion]]

![[assets/2610.21374_figure.png|800]]

- **arXiv**: [2610.21374](https://arxiv.org/abs/2610.21374)
- **PDF**: https://arxiv.org/pdf/2610.21374
- **详细分析**: [[20_Research/Papers/具身智能/From_Optical_Flow_to_Safety_Visual_Safety_Certification_via_Scale-Free_Relative_Motion|From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion]]
- **作者**: Bazeela Banday, Jishnu Keshavan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.3，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《From Optical Flow to Safety: Visual Safety Certification via Scale-Free Relative Motion》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe autonomous navigation using monocular vision remains challenging because explicit obstacle states are not directly observable. This letter introduces a visual safety-certification paradigm that uses scale-free, depth-normalized relative motion encoded by monocular optical flow as the representation for collision-risk certification, without reconstructing obstacle position, velocity, geometry, or a metric world model. Unlike conventional optical-flow-based navigation approaches that rely on image motion to shape avoidance behavior, the proposed framework directly encodes collision-cone geometry and safety constraints in this relative-motion representation. An online Concurrent Learning observer estimates the normalized relative velocity and provides a computable estimation-error bound. This uncertainty is propagated into the collision cone through angular inflation and a monocular robot-footprint margin, yielding a Robust Vision-Based Collision Cone Control Barrier Function (RV-C$^3$BF). An optimal-decay CBF quadratic program minimally modifies the nominal control input to enforce the resulting robust safety constraint under the stated assumptions. Extensive simulation and real-world experiments on a TurtleBot3 in cluttered environments with static and dynamic obstacles demonstrate collision avoidance using only monocular vision and onboard proprioception, with the estimation-error bound containing the measured error in $98.3\%$ of simulation samples and the robot achieving collision-free navigation in $93$ of $100$ real-world trials.

</details>

---

### [[20_Research/Papers/具身智能/MR-MPCC_Model_Predictive_Contouring_Control_for_Robotic_Manipulator_Tracking_under_Moving_Reference_Frames|MR-MPCC: Model Predictive Contouring Control for Robotic Manipulator Tracking under Moving Reference Frames]]

![[assets/2610.21292_figure.png|800]]

- **arXiv**: [2610.21292](https://arxiv.org/abs/2610.21292)
- **PDF**: https://arxiv.org/pdf/2610.21292
- **详细分析**: [[20_Research/Papers/具身智能/MR-MPCC_Model_Predictive_Contouring_Control_for_Robotic_Manipulator_Tracking_under_Moving_Reference_Frames|MR-MPCC: Model Predictive Contouring Control for Robotic Manipulator Tracking under Moving Reference Frames]]
- **作者**: Chonghao Cheng, Tiancheng Li, Jonathan Woolfrey, Liang Zhao, Shoudong Huang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《MR-MPCC: Model Predictive Contouring Control for Robotic Manipulator Tracking under Moving Reference Frames》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maintaining small path-tracking errors under moving reference frames is essential for robotic manipulation tasks with tight execution tolerances, such as machining and surgical automation. Conventional time-indexed controllers, including tracking Model Predictive Control (MPC), rely on a fixed temporal correspondence with the reference trajectory and may therefore accumulate path-relative error under abrupt reference-frame motion or timing mismatch. This paper presents MR-MPCC, a Model Predictive Contouring Control (MPCC) framework for velocity-controlled robotic manipulators with 6-DoF end-effector pose regulation under Moving-Reference disturbances. A hierarchical control architecture is adopted, in which an upper-level MPCC optimizes path progress while penalizing contouring and orientation errors, and a constrained resolved motion rate control (RMRC) layer maps the commanded Cartesian twist to feasible joint velocities under joint-level and safety constraints. MR-MPCC is implemented in a ROS2--MuJoCo pipeline and validated on a UR5e platform under moving-reference disturbances, where the path frame is perturbed and tracked by electromagnetic sensors. Compared with PI control and time-indexed tracking MPC under matched disturbance, MR-MPCC achieves lower geometric path-following error and smaller deviations in the moving path frame, demonstrating improved path-following performance under reference-frame motion.

</details>

---

### [[20_Research/Papers/机器人/CLIS-MPPI_Closed-Loop_Model_Predictive_Path_Integral_Control_With_Initial-State_Sampling_Under_Execution_Delay|CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay]]

![[assets/2610.21239_figure.png|800]]

- **arXiv**: [2610.21239](https://arxiv.org/abs/2610.21239)
- **PDF**: https://arxiv.org/pdf/2610.21239
- **详细分析**: [[20_Research/Papers/机器人/CLIS-MPPI_Closed-Loop_Model_Predictive_Path_Integral_Control_With_Initial-State_Sampling_Under_Execution_Delay|CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay]]
- **作者**: Zidong Liu, Xu Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《CLIS-MPPI: Closed-Loop Model Predictive Path Integral Control With Initial-State Sampling Under Execution Delay》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sampling-based motion planning such as Model Predictive Path Integral (MPPI) control has become attractive for robotics due to its ability to handle nonlinear dynamics and non-smooth objectives without gradient information, while leveraging parallel rollout computation for real-time performance. However, in real-world robotic systems, the optimized control input is often applied after a non-negligible planning delay, causing a mismatch between the state used in forward simulation and the actual state at control execution, which can significantly degrade planning accuracy and may even lead to unsafe behavior such as collisions. This paper proposes Closed-Loop MPPI with Initial-State Sampling (CLIS-MPPI), which explicitly addresses execution-time state mismatch by modeling planning delay as a distribution over plausible execution-time initial states, performing rollout optimization from sampled initial states, and applying a rollout-based local feedback correction during control execution. The proposed method is validated through real-world experiments on a 6-DoF UR5e manipulator in a narrow-passage task involving obstacle avoidance and end-effector target reaching. Across 5 real-world runs of the same task, standard MPPI collided in 2 runs, whereas CLIS-MPPI remained collision-free in all 5 runs. Averaged over all collision-free runs for each method (3 for MPPI and 5 for CLIS-MPPI), CLIS-MPPI reduced the average task completion time from 25.4s to 24.4s and the average end-effector path length from 0.456 m to 0.425 m. It also reduced the overall joint-position and joint-velocity root mean square errors (RMSEs) from 0.100 rad and 0.108 rad/s to 0.017 rad and 0.011 rad/s, respectively. These results demonstrate improved safety, planning-execution consistency, and motion smoothness.

</details>

---

### [[20_Research/Papers/具身智能/An_Agentic_Framework_for_Proactive_Robots_with_Procedural_Assistance_Memory|An Agentic Framework for Proactive Robots with Procedural Assistance Memory]]

![[assets/2610.21211_figure.png|800]]

- **arXiv**: [2610.21211](https://arxiv.org/abs/2610.21211)
- **PDF**: https://arxiv.org/pdf/2610.21211
- **详细分析**: [[20_Research/Papers/具身智能/An_Agentic_Framework_for_Proactive_Robots_with_Procedural_Assistance_Memory|An Agentic Framework for Proactive Robots with Procedural Assistance Memory]]
- **作者**: Dohyun Lee, Minho Park, Jeonghoon Park, Dongyoon Hwang, Junha Hyung, Sungwon Hwang, Byungkun Lee, Jaegul Choo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《An Agentic Framework for Proactive Robots with Procedural Assistance Memory》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proactive robots should anticipate user needs and provide assistance before being explicitly asked. A straightforward approach is to infer human intentions from commonsense knowledge, but the same observed behavior can imply different needs across users, potentially leading to unwanted assistance. We observe that everyday routines in the real world exhibit recurring patterns, so learning these patterns can reduce ambiguity in proactive decisions. Based on this, we propose a memory-based agentic framework in which a VLM task predictor reads a Procedural Assistance Memory (PAM) alongside the current observation to decide when to assist and what task to perform, and a VLA executor performs the predicted task. PAM is structured as a finite-state machine over activity phases, per-state assistance rules, and event-driven transitions; a reflection VLM revises PAM from each day's interaction trace without weight updates or retraining. In our 5-day desk-assistance evaluation, memory-free baselines remain conservative, with limited recall on proactive tasks. Our system improves consistently with accumulated experience, achieving the highest precision, recall, and F1 and reducing first-fire delay from approximately 5 seconds on Day 1 to 1 second by Day 5. Our approach also adapts to changes in the user's routine through continued memory reflection, recovering from memory--routine misalignment after a single memory update. The project page is available at https://davian-robotics.github.io/PAM/

</details>

---

### [[20_Research/Papers/具身智能/LIN-SLAM_Lightweight_LiDAR--Inertial_Neural_SLAM_for_Real-Time_Onboard_Navigation|LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation]]

![[assets/2610.21199_figure.png|800]]

- **arXiv**: [2610.21199](https://arxiv.org/abs/2610.21199)
- **PDF**: https://arxiv.org/pdf/2610.21199
- **详细分析**: [[20_Research/Papers/具身智能/LIN-SLAM_Lightweight_LiDAR--Inertial_Neural_SLAM_for_Real-Time_Onboard_Navigation|LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation]]
- **作者**: Shiqi Che, Yijie Liu, Shuo Wang, Wenxin Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LIN-SLAM), a hybrid method that couples high-rate geometric LiDAR--inertial estimation with neural implicit tracking, continual mapping, and global refinement for accurate real-time onboard SLAM. Experiments on twelve representative sequences from three datasets spanning 32-, 64-, and 128-channel LiDAR configurations show that LIN-SLAM achieves the lowest overall mean absolute trajectory error (ATE) among the evaluated state-of-the-art geometric and neural implicit methods, while substantially reducing runtime compared with existing neural implicit SLAM methods. On a Unitree Go2 equipped with an NVIDIA Jetson Orin NX and a 16-channel LiDAR, LIN-SLAM sustains real-time localization and neural mapping over a 1.47-km indoor trajectory through challenging repetitive corridor environments, with an endpoint closure error of only 0.141~m. To the best of our knowledge, LIN-SLAM is the first LiDAR--inertial SLAM system with a neural implicit backend to achieve real-time online operation on a mobile robotic platform while maintaining state-of-the-art localization accuracy. The code will be released upon acceptance.

</details>

---

### [[20_Research/Papers/大模型/Evo-DexBench_Benchmarking_Generalization_across_Related_Tasks_for_Dexterous_Manipulation|Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation]]

![[assets/2610.21180_figure.png|800]]

- **arXiv**: [2610.21180](https://arxiv.org/abs/2610.21180)
- **PDF**: https://arxiv.org/pdf/2610.21180
- **详细分析**: [[20_Research/Papers/大模型/Evo-DexBench_Benchmarking_Generalization_across_Related_Tasks_for_Dexterous_Manipulation|Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation]]
- **作者**: Bing Cheng, Yiran Mao, Zewei Ye, Yifan Jin, Xinyi Chen, Ruifeng Tu, Shuhuai Wang, Tao Lin, Zhimu Zhou, Yuxin Du, Fangwei Zhong, Junchi Yan...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DexGraspVLA, DexVLA, Evo-DexBench, Meta-World, PartNet, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose dexterous manipulation requires policies to transfer knowledge from related tasks to new tasks with only a few target demonstrations. Existing benchmarks often provide too many target demonstrations. They also leave the differences between source and target tasks uncontrolled. As a result, they cannot clearly distinguish knowledge transfer from task memorization. Our key insight is the Core-Gen principle. Core tasks are related tasks that share a functional interaction and provide source knowledge, while a Gen task is a novel target within the same functional family that has only a few demonstrations. This setup tests whether a policy can reuse functional interaction knowledge. Based on this principle, we propose Evo-DexBench, which controls both source-task relatedness and target-task exposure. It comprises 30 tasks in six functional families and a VR teleoperation pipeline. The resulting dataset covers three everyday scenes per task. It contains 1,248 multimodal demonstrations collected with simulated Shadow Hands equipped with 123 taxels. Experiments show that even the best-performing method achieves an average success rate of only 38.5%, highlighting the challenges existing methods face in transferring functional interaction knowledge. Further analysis shows that, across the two tasks, joint Core+Gen training improves performance by 12% and 38%, respectively, over training on Core followed by fine-tuning on Gen. This indicates that joint training makes better use of Core knowledge and that functionally matched Core data yields greater gains in success rate than mismatched data. We release the Evo-DexBench dataset and benchmark to support the evaluation of dexterous manipulation policies' generalization across related tasks.

</details>

---

### [[20_Research/Papers/具身智能/When_to_Ask_for_Help_A_Decision-Theoretic_Account_and_Measurement_Standard_for_Slow-Module_Scheduling_in_Dual-System_Vision-Language-Action_|When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models]]

![[assets/2610.21160_first_page.png|800]]

- **arXiv**: [2610.21160](https://arxiv.org/abs/2610.21160)
- **PDF**: https://arxiv.org/pdf/2610.21160
- **详细分析**: [[20_Research/Papers/具身智能/When_to_Ask_for_Help_A_Decision-Theoretic_Account_and_Measurement_Standard_for_Slow-Module_Scheduling_in_Dual-System_Vision-Language-Action_|When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models]]
- **作者**: Shilin Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《When to Ask for Help: A Decision-Theoretic Account and Measurement Standard for Slow-Module Scheduling in Dual-System Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FiS-VLA, OneTwoVLA, OpenVLA, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dual-system vision-language-action (VLA) models pair a high-frequency fast policy with a slow, expensive module, and published trigger mechanisms for invoking it lack a shared objective, measured costs, and any standard separating schedule quality from module quality. We provide the missing account: invocation is formalized as a calibrated decision problem whose fixed-ratio, fixed-budget, and history-gated schedules are degenerate cases of one quantity, the Value of Intervention (VoI); a renewal baseline proves the optimal schedule periodic under state-independent collapse, with adaptive gains governed by the cost ratio $ρ$ and the dispersion of collapse. Measured systems span three orders of magnitude in $ρ$ (FiS-VLA $0.95$; RoboICL about $10^3$), and a direct test confirms the low-$ρ$ prediction: calibrated gains vanish under homogeneous collapse and grow with heterogeneity. Fourteen closed-loop arms on LIBERO test the contested middle of the continuum ($ρ=1.53$): the adaptive trigger allocates its queries exactly as the threshold rule predicts, yet the language-rewrite channel cannot convert them into success on either suite, and a revert actuator that undoes a failed rewrite is the only intervention with zero net downside on both LIBERO-Spatial and LIBERO-Goal, where the rewrite deficit deepens from thirteen to forty-two points. A four-measure leak-free protocol cuts apparent early-warning AUC from $0.93$ to $0.62$ on $929$ deployment traces, a detection-limited frontier theorem converts detection quality into a schedulability statement, and a compilation loop turns measured value functions into per-task refresh periods within $2.4\%$ of the closed-loop oracle. Together these results turn slow-module invocation from a design opinion into a measured decision.

</details>

---

### [[20_Research/Papers/具身智能/KODA_Kinematics--Observation_Data_Alignment_for_Humanoid_Learning_from_Human_Egocentric_Demonstration|KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration]]

![[assets/2610.21152_figure.png|800]]

- **arXiv**: [2610.21152](https://arxiv.org/abs/2610.21152)
- **PDF**: https://arxiv.org/pdf/2610.21152
- **详细分析**: [[20_Research/Papers/具身智能/KODA_Kinematics--Observation_Data_Alignment_for_Humanoid_Learning_from_Human_Egocentric_Demonstration|KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration]]
- **作者**: Zibo Zhou, Yueru Chen, Junsong Wu, Weiji Xie, Qingyao Xu, Sheng Yin, Shiqing Wang, Jiyuan Shi, Siheng Chen, Chenjia Bai, Xuelong Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training humanoid whole-body vision-language-action (VLA) policies requires costly robot demonstrations with aligned robot-view observations and controller-compatible whole-body state-action labels. Egocentric human demonstrations offer scalable supervision but have misaligned views and sparse motion cues. Existing approaches either pretrain policies that still require robot data for adaptation or generate controller-specific commands that limit reuse. Conversion also requires robot-view observations aligned with the generated whole-body motion. We present KODA (Kinematics-Observation Data Alignment), which converts egocentric RGB demonstrations into whole-body VLA training data using a reusable canonical trajectory to guide robot-view synthesis and generate controller-specific whole-body state-action supervision. KODA first generates a simulator-checked whole-body trajectory using a sparse tracker with sampling-based command optimization. This generated trajectory directly determines the onboard camera poses used to synthesize corresponding robot-view observations. The motion, observations, and task instruction form a canonical record. For each deployment controller, KODA optimizes commands to track the stored motion and records the corresponding action labels and proprioceptive states. When switching controllers, KODA retains this canonical record and regenerates whole-body state-action supervision for co-training with matching robot demonstrations. We evaluate KODA on four Unitree G1 loco-manipulation tasks using two whole-body controllers, SONIC and HEFT. With robot data held fixed, macro-average success on conditions covered by human demonstrations but absent from robot data improves by 45.0 and 46.25 percentage points, respectively. Under both controllers, this metric shows an upward trend across the evaluated human-data budgets, suggesting potential for further scaling.

</details>

---

### [[20_Research/Papers/强化学习/Manifold_Generative_Annealing_for_Contact_Constraint-aware_Impedance_Control_with_Reinforcement_Learning_Prior|Manifold Generative Annealing for Contact Constraint-aware Impedance Control with Reinforcement Learning Prior]]

![[assets/2610.21140_figure.png|800]]

- **arXiv**: [2610.21140](https://arxiv.org/abs/2610.21140)
- **PDF**: https://arxiv.org/pdf/2610.21140
- **详细分析**: [[20_Research/Papers/强化学习/Manifold_Generative_Annealing_for_Contact_Constraint-aware_Impedance_Control_with_Reinforcement_Learning_Prior|Manifold Generative Annealing for Contact Constraint-aware Impedance Control with Reinforcement Learning Prior]]
- **作者**: Zhilin He, Guoquan Qi, Changliu Liu
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.8，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Manifold Generative Annealing for Contact Constraint-aware Impedance Control with Reinforcement Learning Prior》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich robotic tasks require coordinated motion and impedance under uncertain interaction dynamics and physical constraints. While recent methods on learned policies provide useful interaction strategies, they may fail when contact conditions differ from those encountered during training. Model-based generative methods show promising receding-horizon trajectories optimization results, but often lack structured behavioral guidance and refinement that jointly accounts for constraint geometry and actual contact responses. To this end, we propose Manifold Generative Annealing (MGA), a joint model-free and model-based generative framework for motion--impedance optimization. MGA first organizes pretrained reinforcement learning policies into structured sequence proposals, retaining task-specific interaction strategies without committing to their execution. It then evaluates these proposals alongside exploratory samples through model-based rollouts for refinement or separate execution selection. Crucially, realization-aware manifold refinement aligns updates from the refinement bank with both task constraints and locally achievable physical responses, allowing learned experience to guide online adaptation under changing contact conditions. Experiments cover surface scanning, peg insertion, and humanoid pushing, with improved safety success rate of impedance control under nominal and sensing-shift conditions.

</details>

---

### [[20_Research/Papers/机器人/When_a_robot_can_trust_reversing_wind_to_find_an_odour_source|When a robot can trust reversing wind to find an odour source]]

![[assets/2610.20970_figure.png|800]]

- **arXiv**: [2610.20970](https://arxiv.org/abs/2610.20970)
- **PDF**: https://arxiv.org/pdf/2610.20970
- **详细分析**: [[20_Research/Papers/机器人/When_a_robot_can_trust_reversing_wind_to_find_an_odour_source|When a robot can trust reversing wind to find an odour source]]
- **作者**: Junlong Shen, Shunsuke Shigaki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《When a robot can trust reversing wind to find an odour source》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A wind-derived heading can guide a robot towards an odour source even after the wind reverses, but its reliability depends on the plume's transport history. On a quadruped initially facing the source, holding the initial heading reached it in every reversing-wind trial, whereas comparison controllers never settled there. An exact geometric condition links heading correctness to net odour transport, and simulations separate sensing error from departures from nominal flow. Where the alternating wind directions are too close for reversal alone to produce wrong-side headings, the wrong-side rate rises from 1.0% under uniform transport to 4.7% in a stochastic flow. Re-acquiring headings from new odour contact improves simulated search when contact is intermittent. These results identify distinct requirements for wind-guided search: a heading supported by the transport geometry and sufficient intermittent contact to replace it.

</details>

---

### [[20_Research/Papers/具身智能/LEAP_Gradient_Flow_Augmented_Lagrangian_Trajectory_Optimization_for_Contact_Constrained_Robots|LEAP: Gradient Flow Augmented Lagrangian Trajectory Optimization for Contact Constrained Robots]]

![[assets/2610.20936_figure.png|800]]

- **arXiv**: [2610.20936](https://arxiv.org/abs/2610.20936)
- **PDF**: https://arxiv.org/pdf/2610.20936
- **详细分析**: [[20_Research/Papers/具身智能/LEAP_Gradient_Flow_Augmented_Lagrangian_Trajectory_Optimization_for_Contact_Constrained_Robots|LEAP: Gradient Flow Augmented Lagrangian Trajectory Optimization for Contact Constrained Robots]]
- **作者**: César E. Ramos Chuquiure, Ryan Tsai, Yutong Zhou, Zihang Huang, Vansh Thakur, Akshunn Trivedi, Zachary Lin, Pearl Lin, Ruikai Yang, Challen Enninful Adu, Ram Vasudevan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《LEAP: Gradient Flow Augmented Lagrangian Trajectory Optimization for Contact Constrained Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating dynamically feasible motions for legged and manipulating robots requires solving a large, nonlinear, non-convex optimal control problem (OCP) in which contact wrenches must satisfy friction-cone constraints throughout the motion, not only at isolated instants. Existing solvers are sensitive to the initial guess and scale poorly with the number of joints. This paper introduces LEAP, which transcribes the OCP with pseudospectral collocation and, instead of a Newton or SQP solve, integrates a primal--dual gradient flow of a Powell--Hestenes--Rockafellar augmented Lagrangian to compute a solution. Because the flow is stiff, this paper designs a linearly implicit integrator with a Gauss--Newton metric, momentum, and a merit-based step controller that keeps the augmented Lagrangian monotone. Across locomotion benchmarks on five robot platforms, from planar hoppers to 32-joint humanoids, LEAP is the only method to solve every tested problem, achieves substantial speedups over Crocoddyl and Aligator on several benchmarks, and reaches trackable references at smaller compute budgets. The resulting trajectories are validated by tracking them in a high-fidelity simulator and on hardware. We will make the code public upon final acceptance of this paper.

</details>

---

### [[20_Research/Papers/具身智能/BubbleCBF_Constructive_Safety_for_Second-Order_Systems_and_Application_to_Autonomous_Robot_Navigation_in_Unknown_Environments|BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments]]

![[assets/2610.20895_figure.png|800]]

- **arXiv**: [2610.20895](https://arxiv.org/abs/2610.20895)
- **PDF**: https://arxiv.org/pdf/2610.20895
- **详细分析**: [[20_Research/Papers/具身智能/BubbleCBF_Constructive_Safety_for_Second-Order_Systems_and_Application_to_Autonomous_Robot_Navigation_in_Unknown_Environments|BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments]]
- **作者**: Mani Amani, Mohammed Alyaseen, Zhirui Dai, Ki Myung Brian Lee, Nikolay Atanasov, Jorge Cortes
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ARL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Satisfying safety constraints for systems with second-order dynamics is challenging because a position constraint may require infeasible deceleration. Higher-order control barrier functions (CBFs) provide an approach for expressing safety conditions for such systems but feasibility depends on the system dynamics and available control authority. We develop a constructive approach for designing feasible safety constraints for second-order control-affine systems. Starting from a signed distance function (SDF), we construct collision-free spheres, i.e., bubbles, in position space, and use their quadratic geometry and overlap to construct a velocity-dependent safety constraint. The associated safe set is represented as a union of intersections and enforced through a quadratic-program safety filter. Under mild assumptions on the dynamics, bubble overlap, and design parameters, we prove that the quadratic-program-based controller is well defined, continuous in the system state, and renders the set forward invariant. We also derive sufficient conditions for feasibility under bounded inputs. We demonstrate that our BubbleCBF, applied to a differential-drive robot, achieves safe autonomous navigation in unknown environments. Videos and results are available at: https://existentialrobotics.org/bubblecbf/.

</details>

---

### [[20_Research/Papers/机器人/Robotic-supported_Data_Loss_Detection_in_Android_Applications|Robotic-supported Data Loss Detection in Android Applications]]

![[assets/2610.20807_first_page.png|800]]

- **arXiv**: [2610.20807](https://arxiv.org/abs/2610.20807)
- **PDF**: https://arxiv.org/pdf/2610.20807
- **详细分析**: [[20_Research/Papers/机器人/Robotic-supported_Data_Loss_Detection_in_Android_Applications|Robotic-supported Data Loss Detection in Android Applications]]
- **作者**: Davi Freitas, Breno Miranda, Juliano Iyoda
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Robotic-supported Data Loss Detection in Android Applications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Smartphones have become integral to modern life due to their diverse applications. However, the development of applications for these devices faces significant challenges, primarily due to two factors: (i) the diverse hardware and operating system versions that require testing across multiple configurations; and (ii) the imperative activity of testing the smartphone in a non-invasive way (similar to an end-user interaction), which is expensive, tedious and error-prone as it is usually carried out manually. In this context, robotic automation has emerged as an effective solution for addressing the diversity of smartphone systems and versions, and in performing some testing tasks non-invasively. In addition, automated robots facilitate quick, accurate, and repetitive testing, thus enabling developers to validate their applications across various configurations effectively. This results in a less invasive verification and in a significant reduction in time spent on manual testing, thus accelerating the development cycle. Our work proposes R-DLD (Robotic-supported Data Loss Detection), a robot-assisted infrastructure for data loss detection in Android applications, offeringless invasive and more realistic tests by interacting directly with smartphone sensors. The robot is constructed using cost-effective materials, facilitating its adoption in testing environments. In our empirical evaluation R-DLD successfully identified 341 data loss issues in 77 randomly selected apps from an Android store. All reported bugs received responses from the developer, with 89.55% confirming the data loss problems, while 35.82% have being subsequently fixed.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Dimensional_Featurizers_Yield_Fine-Grained_Steering_and_Data_Shaping_in_Robot_Foundation_Models|Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models]]

![[assets/2610.20767_figure.png|800]]

- **arXiv**: [2610.20767](https://arxiv.org/abs/2610.20767)
- **PDF**: https://arxiv.org/pdf/2610.20767
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Dimensional_Featurizers_Yield_Fine-Grained_Steering_and_Data_Shaping_in_Robot_Foundation_Models|Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models]]
- **作者**: Aiden Swann, Mozes Jacobs, Mathilde Papillon, Siddharth Boppana, David Chanin, Dron Hazra, Usha Bhalla, Curt Tigges, Mac Schwager, Owen Lewis, Jack Merullo, Ekdeep Singh Lubana...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Multi-Dimensional Featurizers Yield Fine-Grained Steering and Data Shaping in Robot Foundation Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can better feature discovery improve control over robot behavior through internal interventions and training data? Recent work in vision and language models reveals multidimensional features, motivating block-sparse featurizers (BSFs), which represent each feature in a low-dimensional subspace. We investigate whether recovering this structure provides an interpretable interface for steering vision-language-action models and shaping the data from which they learn. We show that BSFs recover several multi-dimensional task-relevant features underlying the model's computation (e.g., perception, language, proprioceptive state, episode phase, and control variables). We causally validate these features through fine-grained steering: targeted changes in visual perception, semantic representation, and spatial localization produce predictable changes in downstream action prediction. Finally, we use feature-based data attribution to isolate where a specific behavior (failure recovery) arises in the training dataset, identifying fewer than $1.4\%$ of training tokens whose masking is sufficient to remove the targeted behavior. Overall, our results show how matching featurizers to representation geometry can provide more effective tools for understanding and changing robot behavior.

</details>

---

### [[20_Research/Papers/具身智能/Causal_Analysis_of_Robot_Foundation_Models_Enables_Efficiency_Gains|Causal Analysis of Robot Foundation Models Enables Efficiency Gains]]

![[assets/2610.20750_figure.png|800]]

- **arXiv**: [2610.20750](https://arxiv.org/abs/2610.20750)
- **PDF**: https://arxiv.org/pdf/2610.20750
- **详细分析**: [[20_Research/Papers/具身智能/Causal_Analysis_of_Robot_Foundation_Models_Enables_Efficiency_Gains|Causal Analysis of Robot Foundation Models Enables Efficiency Gains]]
- **作者**: Aiden Swann, Mathilde Papillon, Mozes Jacobs, Siddharth Boppana, Tal Haklay, Eric Bigelow, Andrew Lee, Conor Watts, Thomas Icard, Mac Schwager, Owen Lewis, Jack Merullo...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Causal Analysis of Robot Foundation Models Enables Efficiency Gains》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($π_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input image and the instruction shape actions. Across the three models, activation patching shows that causally relevant information influences the action expert (AE) through a narrow band of mid-to-late cross-attention layers, which we term the action-conditioning interface. The content of this information changes with token and layer within the model. Early-to-mid layer representations of the target noun token determine which object is selected, whereas mid-to-late layers carry the spatial information in text tokens that redirects the movement when patched. Where spatial information is stored in prompt tokens various based on the architecture. In MolmoAct2 the model forms task-conditioned representations at the text positions that follow the instruction, whereas $π_{0.5}$ additionally stores this information at image token positions. We show that these findings can be translated directly into improving model efficiency. We find that restricting MolmoBot's action expert conditioning to only 3 out of 36 layers reduces inference FLOPs by up to $33\%$ while maintaining comparable task success with the default model across 3,000 evaluation episodes ($46.7\%$ vs. $46.9\%$), and the same principle carries over to real-robot deployment of $π_{0.5}$.

</details>

---
