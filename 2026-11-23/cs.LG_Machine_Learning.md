# cs.LG | Machine Learning | 2026-11-23

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/具身智能/Efficient_VLA_Reinforcement_Learning_via_Subchunk_Rollouts_in_Latent_World_Models|Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models]]

![[assets/2611.27645_figure.png|800]]

- **arXiv**: [2611.27645](https://arxiv.org/abs/2611.27645)
- **PDF**: https://arxiv.org/pdf/2611.27645
- **详细分析**: [[20_Research/Papers/具身智能/Efficient_VLA_Reinforcement_Learning_via_Subchunk_Rollouts_in_Latent_World_Models|Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models]]
- **作者**: Nan Tang, Han-Tao Zhang, Jing-Cheng Pang, Hao-Nan Wang, Hao-Xiang Ren, Yi-Fei Sheng, Jun-Yin Ye, Tian Xu, Fan-Ming Luo, Hao-Xin Lin, Yang Yu
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 强化学习, 机器人
- **相关性评分**: 3.82（加权：具身智能 1.5，强化学习 0.96，世界模型 1.16，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models》归入 具身智能、世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, Latent-RL, MBRL, PlaNet, RLT-RL, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences. However, existing VLA-MBRL methods primarily rely on large-scale image or video generation world models, incurring large computational overhead. Latent world models offer a more efficient alternative but face two challenges: compounding errors during recursive prediction and incompatibility with VLAs' visual input interfaces. In this work, we propose LS-MBPO, a lightweight residual MBRL framework that leverages latent world models to improve upon pretrained VLAs. LS-MBPO introduces two key techniques: (1) Hierarchical Forcing, which combines dense causal supervision with autoregressive feedback to mitigate compounding prediction errors; and (2) Latent Subchunk Rollouts, which leverage action chunks from a frozen VLA policy and a latent residual policy for successive subchunk refinement, bridging the gap between latent imagination and VLA policy execution. We further introduce a Progress-Conditioned Branch-Start Curriculum that progressively shifts rollout starting points from later to earlier task stages, enabling effective policy learning from short imagined rollouts. Extensive experiments on LIBERO, RoboTwin, and a real-world ALOHA robot show that LS-MBPO achieves superior task performance and training efficiency compared to existing methods.

</details>

---

### [[20_Research/Papers/大模型/WEIR_Watershed_Exploration_and_Drift-Aware_Prefix_Shrinkage_for_Multi-Turn_Agent_Reinforcement_Learning|WEIR: Watershed Exploration and Drift-Aware Prefix Shrinkage for Multi-Turn Agent Reinforcement Learning]]

![[assets/2611.27570_first_page.png|800]]

- **arXiv**: [2611.27570](https://arxiv.org/abs/2611.27570)
- **PDF**: https://arxiv.org/pdf/2611.27570
- **详细分析**: [[20_Research/Papers/大模型/WEIR_Watershed_Exploration_and_Drift-Aware_Prefix_Shrinkage_for_Multi-Turn_Agent_Reinforcement_Learning|WEIR: Watershed Exploration and Drift-Aware Prefix Shrinkage for Multi-Turn Agent Reinforcement Learning]]
- **作者**: Pixel Nomand, Elena Voss, Marcus Hale, Sofia Reyes
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《WEIR: Watershed Exploration and Drift-Aware Prefix Shrinkage for Multi-Turn Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, CoBA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-turn language model agents often receive only a single binary reward at the end of a long interaction trajectory, making it difficult to separate decisive decisions from routine steps or estimate accurate intermediate values. Prefix-tree methods improve sample efficiency by merging trajectories that share action histories, yet two structural flaws remain: naive pooling mixes stale off-policy outcomes into critic targets with fixed weights, and uniform or entropy-driven branching wastes continuations on dead-end states whose outcome is already settled. We introduce WEIR (Watershed Exploration and Intrinsic-Drift Shrinkage), an actor-critic reinforcement learning framework grounded in a Doob turn-variance conservation identity. WEIR maintains a cross-iteration canonical action-prefix tree with exponentially discounted visit counts and trains a prefix-conditioned critic toward a minimax drift-aware shrinkage target that adapts from single-trajectory returns at rare nodes to pooled empirical means at dense nodes. Using the same pre-update critic, WEIR allocates rollout budgets across tasks via Neyman stratification $B_q \propto \sqrt{\hat{p}_q(1-\hat{p}_q)}$ and directs within-task branches to watershed forks where high survival-headroom uncertainty coincides with steep value cliffs. Across four multi-hop QA benchmarks, ALFWorld, and WebShop on Qwen2.5-3B/7B-Instruct, WEIR achieves $32.18\%$ and $37.85\%$ average QA exact match and $84.83\%$ and $87.81\%$ ALFWorld success rates, outperforming CAPO by $1.50$--$3.74$ points while generating $28$--$29\%$ fewer rollout tokens than chain sampling.

</details>

---

### [[20_Research/Papers/强化学习/TITAN_DRL-Based_Dynamic_Scheduling_and_Resource_Allocation_for_Tactile_Internet|TITAN: DRL-Based Dynamic Scheduling and Resource Allocation for Tactile Internet]]

![[assets/2611.27560_figure.png|800]]

- **arXiv**: [2611.27560](https://arxiv.org/abs/2611.27560)
- **PDF**: https://arxiv.org/pdf/2611.27560
- **详细分析**: [[20_Research/Papers/强化学习/TITAN_DRL-Based_Dynamic_Scheduling_and_Resource_Allocation_for_Tactile_Internet|TITAN: DRL-Based Dynamic Scheduling and Resource Allocation for Tactile Internet]]
- **作者**: Qingrui Fan, Vineet Gokhale, Jayakrishnan Nair, Johannes Cottyn
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《TITAN: DRL-Based Dynamic Scheduling and Resource Allocation for Tactile Internet》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile Internet (TI) applications require ultra-reliable, low-latency tactile communication alongside video traffic. However, tactile Quality of Service (QoS) requirements vary with the interaction context, making fixed resource allocation inefficient. In this paper, we propose TITAN (Two-Timescale Integrated Tactile Internet over 5G Access Networks), a dynamic scheduling and resource allocation (SRA) scheme. TITAN receives time-varying tactile QoS profiles from a higher-layer module and adapts SRA to the current QoS profile and network state. A deep reinforcement learning-based agent splits the available network bandwidth between tactile and video streams at a slow timescale, while a fast-timescale scheduler allocates resource blocks among active user equipment. Through simulations, we show that TITAN simultaneously satisfies both tactile and video QoS targets and achieves a performance gain of 7.64 percentage points (pp) in the joint satisfaction rate over the best-performing static SRA baseline.

</details>

---

### [[20_Research/Papers/大模型/Latent_Jacobian_Steer_Eliciting_Contact-Rich_Out-of-Distribution_Behaviors_from_Pretrained_Humanoid_Controllers|Latent Jacobian Steer: Eliciting Contact-Rich Out-of-Distribution Behaviors from Pretrained Humanoid Controllers]]

![[assets/2611.27338_figure.png|800]]

- **arXiv**: [2611.27338](https://arxiv.org/abs/2611.27338)
- **PDF**: https://arxiv.org/pdf/2611.27338
- **详细分析**: [[20_Research/Papers/大模型/Latent_Jacobian_Steer_Eliciting_Contact-Rich_Out-of-Distribution_Behaviors_from_Pretrained_Humanoid_Controllers|Latent Jacobian Steer: Eliciting Contact-Rich Out-of-Distribution Behaviors from Pretrained Humanoid Controllers]]
- **作者**: S K Swaminathan, Shivam Sood, Shreyansh Kansal, Chengyang He, Guillaume Adrien Sartoretti
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《Latent Jacobian Steer: Eliciting Contact-Rich Out-of-Distribution Behaviors from Pretrained Humanoid Controllers》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DEP-RL, OpenVLA, Real2Sim, SPiRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Given a pretrained general latent-conditioned whole-body humanoid controller, say a behavioral foundation model (BFM), how can we elicit complex and contact-rich out-of-distribution behaviors? Raw joint-action exploration enables direct, task-specific adjustments but can disrupt coordination learned by the pretrained controller, whereas latent exploration retains that coordination but is difficult to steer toward desired physical effects. To combine the complementary strengths of these exploration spaces, we propose Latent Jacobian Steer (LJS), which couples sampling in direct joint-action space with the semantics of the learned frozen controller's input latent space. For a task specified through desired physical effects, we sample task-relevant joint-action perturbations and map them through a damped local inverse of the policy Jacobian to obtain candidate latent ($z$) commands. These commands are executed through the frozen pretrained policy, while exploration is directed toward the physical outcomes required by the new task. Candidate outcomes are evaluated in simulation and composed into latent-command sequences that accomplish the task. Ablations show that neither action-space nor latent-space exploration alone provides the same capability as their coupling. Across diverse out-of-distribution tasks, simulation-based searching using this method produces contact-rich behaviors, including hurdling, manipulating articulated objects, and opening doors through non-prehensile contact. Over ten seeds, LJS completes more of each humanoid task than when searching in either space alone. Beyond humanoids, it also steers a goal-conditioned dexterous hand policy through four assembly tasks better than searching in goal space directly.

</details>

---

### [[20_Research/Papers/具身智能/Mind_World_Models_Joint_Learning_of_Motor_EEG_Representations_and_Action-Conditioned_World_Dynamics|Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics]]

![[assets/2611.27029_figure.png|800]]

- **arXiv**: [2611.27029](https://arxiv.org/abs/2611.27029)
- **PDF**: https://arxiv.org/pdf/2611.27029
- **详细分析**: [[20_Research/Papers/具身智能/Mind_World_Models_Joint_Learning_of_Motor_EEG_Representations_and_Action-Conditioned_World_Dynamics|Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics]]
- **作者**: Weikang Qiu, Zheng Huang, Tinglin Huang, Yujun Yan, Rex Ying
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 强化学习
- **相关性评分**: 1.72（加权：具身智能 0.6，强化学习 0.16，世界模型 0.96）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics》归入 世界模型、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motor decoding from electroencephalography (EEG) supports non-invasive brain-computer interfaces, yet existing methods either rely on costly cue-based trials and coarse categorical labels or use pretraining objectives that do not directly capture how movement unfolds, limiting their ability to learn transferable motor representations. To this end, we propose the Mind World Model (MWM), a framework that learns motor EEG representations from scalable naturalistic EEG and egocentric video without action annotations. MWM treats EEG observed up to the current frame as the latent action of a world model: a mind model encodes the EEG, and a world model uses it to predict the representation of a future frame, yielding a movement-grounded pretraining objective. We further introduce the Lateralization-Aware Transformer (LAT), which uses frame averaging to separate shared bilateral from side-specific lateral features, encoding hemispheric correspondence to reduce the burden of learning left-right relationships from data. MWM pretraining produces two models: a mind model for downstream motor decoding and a world model that can be adapted to prediction conditioned on real actions, opening a scalable and flexible path to collect egocentric data for embodied AI. Across 9 classification and 7 regression tasks, the mind model improves task-averaged balanced accuracy by 5.9% and Pearson correlation by 16.2% relative to the strongest baseline in each task family. Compared with an inverse-dynamics latent-action baseline, the world model achieves lower prediction error and benefits 3.3 times more from matched real actions within recordings and 4.7 times more on held-out subjects.

</details>

---

### [[20_Research/Papers/具身智能/Skill-JEPA_Learning_Planner-Aligned_Action_Spaces_for_World_Models|Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models]]

![[assets/2611.26825_figure.png|800]]

- **arXiv**: [2611.26825](https://arxiv.org/abs/2611.26825)
- **PDF**: https://arxiv.org/pdf/2611.26825
- **详细分析**: [[20_Research/Papers/具身智能/Skill-JEPA_Learning_Planner-Aligned_Action_Spaces_for_World_Models|Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models]]
- **作者**: Tomás Couso Coddou, Christ Devia, Rex G. Liu, Rodrigo Toro Icarte
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.72（加权：具身智能 0.9，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models based on Joint-Embedding Predictive Architectures (JEPAs) learn from pixels to predict the outcome of actions in a latent space. To reach a goal, a planner samples many candidate action sequences, uses the model to predict where each one leads, and executes the best one. However, standard planners draw their candidates from a Gaussian, while the model has only seen the structured, state-dependent actions of its training data. Its predictions for such candidates are unreliable, and planning fails more often as goals move farther away. We propose Skill-JEPA, which learns an action space aligned with the planner. A variational autoencoder conditioned on the current state encodes short action sequences into latent skills with a standard Gaussian prior, and decodes them back into actions. The world model predicts the effect of skills rather than raw actions, and the planner searches over skills starting from that same Gaussian, so its candidates resemble the model's training data. Skill-JEPA adds a single module, trained end-to-end with the world model, and leaves the planner untouched, with no subgoals, hierarchy, or hand-designed skills. Across three JEPA world models and four benchmarks, average success on goals 80 steps away rises from 42% with raw actions to 62%; the gains grow with goal distance and hold across four planners. On AntMaze, a quadruped locomotion task, success on goals two maze cells away rises from 0.4% to 38%. This suggests that part of the difficulty of reaching distant goals lies in the action space, and can be removed without changing the planner.

</details>

---
