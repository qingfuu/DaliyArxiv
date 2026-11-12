# cs.LG | Machine Learning | 2026-11-11

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/大模型/Pyrite_Building_and_Benchmarking_Protein-Ligand_Pose_Ranking_Agents|Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents]]

![[assets/2611.14511_figure.png|800]]

- **arXiv**: [2611.14511](https://arxiv.org/abs/2611.14511)
- **PDF**: https://arxiv.org/pdf/2611.14511
- **详细分析**: [[20_Research/Papers/大模型/Pyrite_Building_and_Benchmarking_Protein-Ligand_Pose_Ranking_Agents|Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents]]
- **作者**: Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical signals. To investigate automated ranking, we introduce PyriteRep, a structured representation of molecular geometry, protein-ligand interactions, and physicochemical scores, and develop two LLM-based agents: PyriteReasoner, which directly compares poses through text-based reasoning, and PyriteFeaturizer, which generates executable code to construct features for logistic regression, optionally incorporating features derived from LLM subcalls. These agents achieve up to 67% and 74% accuracy, respectively, exceeding observed expert performance. LLM-guided feature discovery generally outperforms direct reasoning, while Group Relative Policy Optimization (GRPO) improves open-weight models, enabling them to match or surpass closed-source frontier models in our evaluations. These results establish Pyrite as a challenging test of pose-ranking ability and highlight LLM-guided feature discovery as a promising approach to interpret and combine the outputs of computational chemistry tools.

</details>

---

### [[20_Research/Papers/大模型/A_Theory_of_Policy_Optimization_in_Post-Training_Coverage_Collapse_and_Reference_Resets|A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets]]

![[assets/2611.14467_figure.png|800]]

- **arXiv**: [2611.14467](https://arxiv.org/abs/2611.14467)
- **PDF**: https://arxiv.org/pdf/2611.14467
- **详细分析**: [[20_Research/Papers/大模型/A_Theory_of_Policy_Optimization_in_Post-Training_Coverage_Collapse_and_Reference_Resets|A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets]]
- **作者**: Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ProRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy optimization is central to language model post-training, yet principled guidance remains limited. We revisit its theoretical foundations to identify algorithms that learn near-optimal policies using total samples and gradient steps governed by the base model's response coverage, a measure of how readily it generates optimal responses. We call such algorithms coverage-preserving. This guarantee captures the goal of amplifying capabilities accessible through sampling from the base model. (1) Coverage collapse. REINFORCE, the basis for PPO and GRPO, can drive the probability of optimal responses to near zero, even as reward improves. This coverage collapse stalls optimization, and convergence can require exponentially many steps despite good initial coverage. The failure arises even with exact gradients and persists under KL regularization to the base model. (2) Reference resets. We show that repeatedly resetting the KL reference to the most recent policy mitigates coverage collapse. We formalize this intervention in Approximate Policy Mirror Descent (APMD), a meta-algorithm that approximately solves a sequence of KL-regularized RL subproblems. APMD enables stronger regularization, making each subproblem easier to solve, while reference resets allow convergence to global optimality. (3) Coverage-preserving algorithms. For softmax linear policies over pretrained features, we use APMD to establish the first global convergence guarantees showing that widely used families of post-training algorithms are coverage-preserving. These include stylized PPO and GRPO variants with explicit KL regularization and reference resets, and squared-loss algorithms that implement them implicitly, including those used to train the Kimi models. These results clarify how regularization, clipping, and objective choice affect the sampling and optimization costs of post-training.

</details>

---

### [[20_Research/Papers/强化学习/Uncertainty-Aware_Hybrid_Offline_Reinforcement_Learning_with_Online_Action_Selection_Enabled_by_Sparse_Gaussian-Process_Critics|Uncertainty-Aware Hybrid Offline Reinforcement Learning with Online Action Selection Enabled by Sparse Gaussian-Process Critics]]

![[assets/2611.14374_figure.png|800]]

- **arXiv**: [2611.14374](https://arxiv.org/abs/2611.14374)
- **PDF**: https://arxiv.org/pdf/2611.14374
- **详细分析**: [[20_Research/Papers/强化学习/Uncertainty-Aware_Hybrid_Offline_Reinforcement_Learning_with_Online_Action_Selection_Enabled_by_Sparse_Gaussian-Process_Critics|Uncertainty-Aware Hybrid Offline Reinforcement Learning with Online Action Selection Enabled by Sparse Gaussian-Process Critics]]
- **作者**: Marco Chan, Christos Evripidou, Liqiu Dong, Benoit Chachuat, Mehmet Mercangöz
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《Uncertainty-Aware Hybrid Offline Reinforcement Learning with Online Action Selection Enabled by Sparse Gaussian-Process Critics》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Start-ups and grade changes remain largely operator-driven, while developing and maintaining dynamic models for model-based control requires substantial engineering effort. Hybrid Offline Learning and Online Optimisation (HOFLON) uses one-step offline reinforcement learning to select actions from historical transition data. In its original implementation, the online objective combines the predicted return from a tree-ensemble critic with an adversarial-autoencoder (AAE) penalty for unfamiliar state-action pairs. We examine the effect of this penalty and replace the critic and AAE with a sparse variational Gaussian-process (sGP) critic. Actions maximise $μ- κσ$, an uncertainty-adjusted estimate of the return from one action followed by the historical operating practice. On the HOFLON polymerisation-reactor benchmark, removing the AAE from HOFLON led to 4 failed start-ups in 15 runs over five critics. At its published weight, the variation in the AAE penalty is four orders of magnitude smaller than the variation in the tree-ensemble critic. Nevertheless, it changes actions when the predicted returns of competing candidates are nearly equal, and paired runs with and without the penalty diverged from the first move. With a Matérn-5/2 sGP critic, $κ= 0$ led to failure in 13 of 15 runs, whereas with $κ= 3$ none of 15 runs (five critics, three noise realisations) failed. The median and lowest returns were 13,464 and 13,398 (HOFLON: 13,393 and 12,411). A squared-exponential sGP critic with learned inducing inputs needed $κ\geq 3$ to remain within the empirical data support in steady state, and then settled with a temperature offset of 2.0 K.

</details>

---

### [[20_Research/Papers/大模型/Chain_of_Physics_Supporting_Fault_Diagnosis_with_Engineering-Inspired_Large_Language_Model_Reasoning|Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning]]

![[assets/2611.14263_first_page.png|800]]

- **arXiv**: [2611.14263](https://arxiv.org/abs/2611.14263)
- **PDF**: https://arxiv.org/pdf/2611.14263
- **详细分析**: [[20_Research/Papers/大模型/Chain_of_Physics_Supporting_Fault_Diagnosis_with_Engineering-Inspired_Large_Language_Model_Reasoning|Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning]]
- **作者**: Wenqi Zhou, Leonardo Baldo, Kai Goebel, Manuel Arias Chao
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fault diagnosis in complex systems requires linking observed changes in physical quantities to the failure mechanisms that produce them. Experienced engineers perform this task by combining sensor information with knowledge of system behavior and fault propagation. Large Language Models (LLMs) can support this process, but their diagnostic reasoning depends on the availability of asset-specific engineering knowledge and on how this knowledge is represented and used during inference. This work introduces Chain of Physics (CoP), an LLM-based fault-diagnosis framework built around a Constrained Knowledge Graph (CKG) generated automatically from asset-specific reference documentation. CoP addresses failure-sensor association from textual engineering knowledge. The CKG stores diagnostic chains connecting failure modes, changes in physical quantities, and monitoring sensors. During inference, semantically similar graph paths are retrieved for each question and used as both information and in-context examples for the reasoning process. Candidate failure modes are extracted from the question and analysed independently through dedicated LLM calls, which generate plausible failure-to-observation chains. A final decision module compares these chains with the available answer choices. CoP is evaluated on the FailureSensorIQ benchmark across four industrial asset classes and three LLMs. Compared with direct prompting and conventional Retrieval-Augmented Generation (RAG), CoP improves diagnostic accuracy across all evaluated models, with gains ranging from 7.8 to 19.6 percentage points and from 11.7 to 18.2 percentage points, respectively. The results show that structured engineering knowledge can improve LLM-based diagnostic reasoning when graph retrieval is combined with in-context examples of fault propagation.

</details>

---

### [[20_Research/Papers/强化学习/Opportunity-Cost_Option-Critic_Adaptive_Switching_Costs_for_Robust_Hierarchical_Reinforcement_Learning|Opportunity-Cost Option-Critic: Adaptive Switching Costs for Robust Hierarchical Reinforcement Learning]]

![[assets/2611.14099_figure.png|800]]

- **arXiv**: [2611.14099](https://arxiv.org/abs/2611.14099)
- **PDF**: https://arxiv.org/pdf/2611.14099
- **详细分析**: [[20_Research/Papers/强化学习/Opportunity-Cost_Option-Critic_Adaptive_Switching_Costs_for_Robust_Hierarchical_Reinforcement_Learning|Opportunity-Cost Option-Critic: Adaptive Switching Costs for Robust Hierarchical Reinforcement Learning]]
- **作者**: Khaled Ammoura, Aya Kayal, Naseem Daher
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Opportunity-Cost Option-Critic: Adaptive Switching Costs for Robust Hierarchical Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deliberation costs are commonly used in hierarchical reinforcement learning (HRL) to prevent options from collapsing to primitive actions. Existing approaches rely on fixed penalties or duration-based adaptations, both of which are indirect proxies for an option's utility. This paper argues that option persistence should instead depend on the opportunity cost of abandoning the current behavior. We propose the Opportunity-Cost Option-Critic ($OC^2$) framework, which defines a state-dependent deliberation cost using the positive value gap between the active option and its best alternative. This encourages persistence when the current option is clearly preferable and allows rapid switching when a better option emerges. We show that directly learning such costs leads to a degenerate zero-cost solution and introduces an auxiliary objective that aligns the learned cost with the value-gap target. The approach is evaluated in Four Rooms and Pinball domains under stationary, goal-shift, and geometry-shift conditions. In the Pinball goal-shift task, the $OC^2$ framework achieves a 52\% first-ten-episode success rate compared with 18\% for a fixed-cost baseline. The results suggest that opportunity-cost-based persistence improves adaptation in non-stationary environments.

</details>

---

### [[20_Research/Papers/强化学习/Temporal_Behavior_Trees_for_Reinforcement_Learning_Specifications_as_Rewards,_Curricula,_and_Diagnostics|Temporal Behavior Trees for Reinforcement Learning: Specifications as Rewards, Curricula, and Diagnostics]]

![[assets/2611.13993_first_page.png|800]]

- **arXiv**: [2611.13993](https://arxiv.org/abs/2611.13993)
- **PDF**: https://arxiv.org/pdf/2611.13993
- **详细分析**: [[20_Research/Papers/强化学习/Temporal_Behavior_Trees_for_Reinforcement_Learning_Specifications_as_Rewards,_Curricula,_and_Diagnostics|Temporal Behavior Trees for Reinforcement Learning: Specifications as Rewards, Curricula, and Diagnostics]]
- **作者**: Vladimir Krsmanovic, Bernd Finkbeiner
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Temporal Behavior Trees for Reinforcement Learning: Specifications as Rewards, Curricula, and Diagnostics》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from formal specifications often separates task definition, reward shaping, curriculum design, and policy diagnostics into different mathematical objects. This fragmentation requires additional conversion steps and discards structure already present in the specification, such as subtask boundaries, ordering constraints, and quantitative measures. We introduce TBTCL (Temporal Behavior Tree Centric Learning), a framework that uses Temporal Behavior Trees (TBTs) as a unified interface for specification-guided reinforcement learning. A single TBT specifies the task, induces dense robustness-based rewards, defines a curriculum, and supports better understanding of learned policies. By adapting TBT syntax and semantics for specification-guided reinforcement learning, we provide a formalism that is more expressive than popular specification languages such as LTL and inherently hierarchical. We present algorithms to automatically extract a curriculum DAG and derive dense, robustness-based rewards directly from TBT semantics. Furthermore, we utilize TBT trace segmentation to build understandable competence profiles and automatically adapt the reward toward bottlenecks. We evaluate TBTCL on six specifications across discrete and continuous domains and show that Temporal Behavior Trees can serve as a specification, a reward, a curriculum, and a diagnostic.

</details>

---

### [[20_Research/Papers/强化学习/Weighted-AoI-Driven_UAV_Trajectory_and_Reporting_for_Dynamic_CKM_Tracking|Weighted-AoI-Driven UAV Trajectory and Reporting for Dynamic CKM Tracking]]

![[assets/2611.13726_first_page.png|800]]

- **arXiv**: [2611.13726](https://arxiv.org/abs/2611.13726)
- **PDF**: https://arxiv.org/pdf/2611.13726
- **详细分析**: [[20_Research/Papers/强化学习/Weighted-AoI-Driven_UAV_Trajectory_and_Reporting_for_Dynamic_CKM_Tracking|Weighted-AoI-Driven UAV Trajectory and Reporting for Dynamic CKM Tracking]]
- **作者**: Zeyu Zhao, Yueling Che, Sheng Luo
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Weighted-AoI-Driven UAV Trajectory and Reporting for Dynamic CKM Tracking》归入 机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing channel knowledge map (CKM) construction assumes quasi-static environments, failing when channels rapidly decorrelate. This paper investigates continuous online dynamic CKM tracking over an airborne 2D plane via a UAV fleet. We formulate a long-term error minimization problem under UAV mobility and reporting constraints. This problem, however, is intractable with unobservable errors for unmeasured cells. To tackle this, we propose a metric-driven scheduling approach featuring the Weighted-Age of Information (W-AoI). W-AoI evaluates cells by combining exact temporal staleness with spatial uncertainty predicted by a 2D U-Net. We prove that top-$K$ W-AoI selection maximizes the one-slot error reduction bound. Guided by this guarantee, we develop a lightweight greedy trajectory policy incorporating continuous along-path sensing. Simulations demonstrate our method reduces steady-state error by 3.8 dB$^2$ and 4.8 dB$^2$ over AoI-only and FIFO baselines, closely approaching an idealized oracle.

</details>

---

### [[20_Research/Papers/强化学习/TRUER_Test-Time_Reward_Correction_Using_an_Error-Aware_Rectifier_for_Reinforcement_Learning|TRUER: Test-Time Reward Correction Using an Error-Aware Rectifier for Reinforcement Learning]]

![[assets/2611.13714_figure.png|800]]

- **arXiv**: [2611.13714](https://arxiv.org/abs/2611.13714)
- **PDF**: https://arxiv.org/pdf/2611.13714
- **详细分析**: [[20_Research/Papers/强化学习/TRUER_Test-Time_Reward_Correction_Using_an_Error-Aware_Rectifier_for_Reinforcement_Learning|TRUER: Test-Time Reward Correction Using an Error-Aware Rectifier for Reinforcement Learning]]
- **作者**: Mingxiang Shen, Jinhao Li, Jiaming Xu, Yibo Han, Guohao Dai, Yijia Zhang, Ningyi Xu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《TRUER: Test-Time Reward Correction Using an Error-Aware Rectifier for Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoVerRL, SCRL, SR-TTRL, TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time reinforcement learning enables language models to adapt using rewards derived from their own answers. However, majority voting can reinforce incorrect solutions even when correct alternatives are available. Our training audit shows that false positives (incorrect responses receiving positive rewards) dominate reward errors. We focus on a practical regime where ground-truth rewards are difficult to obtain at scale, while a limited labeled source set is available. We introduce TRUER, a framework that uses limited supervision to train a reward rectifier that distinguishes correctness from consensus. To achieve this goal, we train the rectifier with an emphasis on incorrect majorities and correct minorities, targeting cases where consensus and correctness disagree. After that, we freeze the rectifier and use it to correct rewards during subsequent test-time adaptation. By improving reward accuracy and thereby model performance, TRUER consistently outperforms naive TTRL in both metrics across all evaluated configurations.

</details>

---

### [[20_Research/Papers/强化学习/Unified_Optimization_of_Traffic_Signal_and_Lane_Channelization_for_an_Isolated_Intersection_Using_Reinforcement_Learning|Unified Optimization of Traffic Signal and Lane Channelization for an Isolated Intersection Using Reinforcement Learning]]

![[assets/2611.13599_first_page.png|800]]

- **arXiv**: [2611.13599](https://arxiv.org/abs/2611.13599)
- **PDF**: https://arxiv.org/pdf/2611.13599
- **详细分析**: [[20_Research/Papers/强化学习/Unified_Optimization_of_Traffic_Signal_and_Lane_Channelization_for_an_Isolated_Intersection_Using_Reinforcement_Learning|Unified Optimization of Traffic Signal and Lane Channelization for an Isolated Intersection Using Reinforcement Learning]]
- **作者**: Jiwon Kang, Jiyoung Kim, Hyunseok Jun, Keemin Sohn
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Unified Optimization of Traffic Signal and Lane Channelization for an Isolated Intersection Using Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Optimizing traffic signal control has been a long-lasting critical issue in traffic engineering, and a number of robust methodologies have emerged to solve the problem so far. On the other hand, the road design for lane channelization is a static problem that is difficult to solve jointly with the real-time traffic signal control. If traffic volume does not vary, it is possible that both problems can be solved in an integrated manner as a single static optimization problem. Recently, researchers have devised a mixed integer linear problem (MILP) to jointly determine the traffic signal and road width designs. However, this joint optimization problem must be solved repeatedly whenever the traffic flow pattern varies. Solving the MILP may also take impractical computing time as the problem size gets larger. We present a robust methodology for solving the joint optimization problem using reinforcement learning (RL) on a real-time basis. Abrupt changes in lane markings with an incompatible signal phase can jeopardize drivers. To sidestep such a dangerous action change, we train a model with human feedback to filter infeasible action transitions in a rule-based manner. We devised a deep Q-network that can accommodate joint actions for traffic signal and lane marking plans. To ensure the implementation of the proposed operation, a variable sign for lane markings is necessary at each stop line of an intersection. The experimental results confirm that the proposed methodology enhances the intersection performance by increasing throughput.

</details>

---

### [[20_Research/Papers/强化学习/Discrete_Model-Based_Diffusion_for_Combinatorial_Optimization_in_Multi-Robot_Task_Allocation|Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation]]

![[assets/2611.13382_figure.png|800]]

- **arXiv**: [2611.13382](https://arxiv.org/abs/2611.13382)
- **PDF**: https://arxiv.org/pdf/2611.13382
- **详细分析**: [[20_Research/Papers/强化学习/Discrete_Model-Based_Diffusion_for_Combinatorial_Optimization_in_Multi-Robot_Task_Allocation|Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation]]
- **作者**: Haejoon Lee, Thomas Marshall Vielmetti, Xinyi Wang, Dimitra Panagou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.02（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Discrete Model-Based Diffusion for Combinatorial Optimization in Multi-Robot Task Allocation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decision making in multi-agent and multi-robot systems often involves discrete decision variables, leading to NP-hard combinatorial optimization problems that must be solved within seconds for near real-time implementation. Denoising diffusion has emerged as a powerful tool for such problems, but existing approaches face a trade-off: Model-Based Diffusion (MBD) incorporates diffusion in sampling-based optimization (SBO) without training but only over continuous spaces, while existing diffusion-based combinatorial solvers operate over discrete spaces but require offline training. To this end, we propose Discrete Model-Based Diffusion (Discrete MBD), a training-free SBO method that directly optimizes discrete variables by approximating categorical reverse transition distributions through Monte Carlo sampling. We establish a finite-step lower bound on the probability of finding a global minimizer and show that this bound converges to one as the number of denoising steps increases. Extensive experiments on generic integer programs and heterogeneous multi-robot coalition formation and scheduling demonstrate that Discrete MBD outperforms SBO baselines in nearly all settings while achieving solution quality competitive with that of mixed-integer programming and reinforcement learning methods at a fraction of their computational cost.

</details>

---

### [[20_Research/Papers/强化学习/Audited_Gradients,_Anchored_Policies_Model-Based_Reinforcement_Learning_for_Efficient_Flow_Control|Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control]]

![[assets/2611.13203_figure.png|800]]

- **arXiv**: [2611.13203](https://arxiv.org/abs/2611.13203)
- **PDF**: https://arxiv.org/pdf/2611.13203
- **详细分析**: [[20_Research/Papers/强化学习/Audited_Gradients,_Anchored_Policies_Model-Based_Reinforcement_Learning_for_Efficient_Flow_Control|Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control]]
- **作者**: Ruige Kong, Stefania Fresca
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 0.96，世界模型 0.76）
- **关联关键词**: RL

#### 研究背景与动机

《Audited Gradients, Anchored Policies: Model-Based Reinforcement Learning for Efficient Flow Control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SINDy-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Feedback controllers for flows are expensive to design, since each candidate must be evaluated with a high-fidelity solver. Differentiable surrogates reduce that cost, but they also introduce a failure mode that prediction error cannot detect. Policy optimization uses the derivative of the objective with respect to the action, which we call the action gradient and which can be computed either through the surrogate or through the high-fidelity solver. Optimization through the surrogate uses only its action gradient, and a surrogate can follow the flow trajectory closely while misestimating this derivative. The surrogate action gradient is compared against a central finite-difference estimate from the high-fidelity solver on held-out states, under acceptance criteria fixed before the comparison, and we call that comparison an audit. A low-dimensional feedback law is then fitted to the surrogate action gradient when the surrogate passes the audit, and to the solver estimate when it does not. This law initializes a neural policy, and a quadratic penalty holds the policy near it during optimization. The proposed approach is validated on four test cases. The resulting controllers outperform or match a model-free baseline, while using 3 to 156 times fewer high-fidelity solver interactions across the four test cases. One surrogate predicts the objective at correlation 0.9996 but its action gradient at only 0.459, so prediction accuracy does not identify a usable surrogate. Another surrogate, whose action gradient agrees with the solver estimate at correlation 0.996, makes the objective 0.52% worse when the policy is optimized through it without the anchor penalty, so an accurate gradient alone does not provide a working controller. Finally, a surrogate that passes the audit at one fixed action fails it around the actions the deployed controller applies, so a pass is local.

</details>

---

### [[20_Research/Papers/具身智能/FaST_Factored_Synthesis_of_Transitions_for_Offline_Reinforcement_Learning|FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning]]

![[assets/2611.13013_first_page.png|800]]

- **arXiv**: [2611.13013](https://arxiv.org/abs/2611.13013)
- **PDF**: https://arxiv.org/pdf/2611.13013
- **详细分析**: [[20_Research/Papers/具身智能/FaST_Factored_Synthesis_of_Transitions_for_Offline_Reinforcement_Learning|FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning]]
- **作者**: Daniel Campa, Spandan Das, Srinjoy Das
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.52（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《FaST: Factored Synthesis of Transitions for Offline Reinforcement Learning》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：D4RL, MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synthetic data augmentation promises to scale offline reinforcement learning beyond fixed logged datasets, but leading diffusion-based generators model the transition tuple (state, action, next state, reward, terminal) as a monolith: no single factor can be natively redrawn in isolation. We present FaST (Factored Synthesis of Transitions), which factors transitions via the chain rule into state, action, dynamics, reward, and terminal stages, fitting each with an estimator matched to its statistical properties. Across twelve D4RL locomotion and maze benchmarks, TD3+BC and IQL agents trained on FaST transitions match the SynthER diffusion baseline while generating transitions over 90x faster. The explicit action-given-state conditional can also be re-queried for a fixed state, enabling targeted action synthesis: drawing N candidate actions per generated state and keeping the highest-advantage one under a value function fit to the same data, thereby synthesizing improved behavior during generation rather than filtering for it post-hoc. Best-of-10 synthesis beats training on real data on 11 of 12 medium and medium-replay settings (+8.9 D4RL points on average, up to +28.4), and is competitive with advantage-filtered SynthER at a fraction of its generation cost. On expert mixtures both mechanisms degrade identically, tracing the failure to the advantage estimate itself rather than to either targeting mechanism.

</details>

---

### [[20_Research/Papers/强化学习/Branch-and-Commit_for_Frozen_RL_Agents_When_and_Where_to_Spend_Test-Time_Compute|Branch-and-Commit for Frozen RL Agents: When and Where to Spend Test-Time Compute]]

![[assets/2611.13003_first_page.png|800]]

- **arXiv**: [2611.13003](https://arxiv.org/abs/2611.13003)
- **PDF**: https://arxiv.org/pdf/2611.13003
- **详细分析**: [[20_Research/Papers/强化学习/Branch-and-Commit_for_Frozen_RL_Agents_When_and_Where_to_Spend_Test-Time_Compute|Branch-and-Commit for Frozen RL Agents: When and Where to Spend Test-Time Compute]]
- **作者**: Sahar Admoni, Assaf Hallak, Yftah Ziser, Ofra Amir
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Branch-and-Commit for Frozen RL Agents: When and Where to Spend Test-Time Compute》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Selection-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning agents are often deployed with policies that cannot be retrained or modified. In digital environments whose states can be copied and resumed, an operator has another option: sample several continuations from the current state, evaluate them, and continue from the endpoint of the selected branch. We call this procedure branch-and-commit. We study when it improves return, what produces the improvement, and where its computational budget should be spent. Across four environments, two frozen policies, five continuation verifiers, and a model-free selection rule, we find that the benefit of branching depends on dispersion: the difference between the best candidate return and the mean candidate return. Branching provides no benefit in low-dispersion settings, while increasing return by 12.8% in our main Craftax-Medium setting. Most of this gain comes not from selecting better actions, but from selecting among different stochastic realizations of the same action. Several competent verifiers achieve similar episode returns, suggesting that verifier quality is not the main constraint at our operating budget. Instead, computation is better allocated to states where useful dispersion is likely. On held-out seeds, gating branching using predicted dispersion retains 69% of the improvement from uniform branching while using 48% as many branching calls. These results characterize when branch-and-commit is useful and clarify what its gains represent.

</details>

---
