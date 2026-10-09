# cs.LG | Machine Learning | 2026-10-08

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/具身智能/RobotWorld_Benchmarking_Multimodal_Agents_for_Robot_Use_Across_Diverse_Tasks_and_Embodiments|RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments]]

![[assets/2610.10409_figure.png|800]]

- **arXiv**: [2610.10409](https://arxiv.org/abs/2610.10409)
- **PDF**: https://arxiv.org/pdf/2610.10409
- **详细分析**: [[20_Research/Papers/具身智能/RobotWorld_Benchmarking_Multimodal_Agents_for_Robot_Use_Across_Diverse_Tasks_and_Embodiments|RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments]]
- **作者**: Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang, Jiankai Sun, Haitao Li, Zijian Wu, Yuzhi Huang, Fanding Huang, Hanwen Sun, Jiashun Liu...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.6，大模型 0.7，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments》归入 机器人、大模型、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, EmbodiedEval, EmbodiedSWE-Bench, OpenVLA, RLBench, RLE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose agents increasingly write code, use tools, and complete complex digital tasks, raising the question of how far these capabilities carry into the physical world. To investigate this, we introduce RobotWorld, a challenging simulation testbed for robot use: turning instructions and observations into physical task execution through robot interfaces. Its 84 tasks span manipulation, mobile manipulation, locomotion, driving, and aerial control, with explicit interaction budgets and executable success checks. By analysing task outcomes alongside execution traces, we identify both the capabilities that transfer and the gaps that prevent reliable completion. Furthermore, we find that current agents can construct sophisticated perception and control workflows, including image segmentation, camera calibration, spatial estimation, and dynamics-based computation. These capabilities, however, do not consistently compose into successful behaviour: agents lose task-relevant object states despite reaching commanded poses, fail to correct ineffective actions, recover too late, or mistake unfinished tasks for completion. This uneven transfer also differs across models: Astra succeeds more often on spatial and constrained-contact goals, whereas Opus 5.5 succeeds more often on continuous-balance and timed-interaction goals. By linking these outcomes to execution behaviour, RobotWorld provides both a rigorous proving ground and an empirical account of the remaining capability gaps, thereby establishing concrete targets for training and designing more reliable physical-world agents.

</details>

---

### [[20_Research/Papers/强化学习/Average-Reward_Reinforcement_Learning_for_Multichain_MDPs_A_Hierarchical_Decomposition_Approach|Average-Reward Reinforcement Learning for Multichain MDPs: A Hierarchical Decomposition Approach]]

![[assets/2610.10326_figure.png|800]]

- **arXiv**: [2610.10326](https://arxiv.org/abs/2610.10326)
- **PDF**: https://arxiv.org/pdf/2610.10326
- **详细分析**: [[20_Research/Papers/强化学习/Average-Reward_Reinforcement_Learning_for_Multichain_MDPs_A_Hierarchical_Decomposition_Approach|Average-Reward Reinforcement Learning for Multichain MDPs: A Hierarchical Decomposition Approach]]
- **作者**: Huizhen Yu, Isaiah Heidt
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Average-Reward Reinforcement Learning for Multichain MDPs: A Hierarchical Decomposition Approach》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study learning optimal policies in average-reward multichain Markov decision processes (MDPs), where the optimal gain may depend on the initial state and recurrence structures vary across policies, creating challenges for reinforcement learning (RL) methods. We propose an asynchronous value-iteration-based RL algorithm that requires no model knowledge beyond the MDP's transition graph and leverages Bather's decomposition to hierarchically partition the state space into communicating subsystems and transient states. This decomposition induces a recasting of the global decision problem into structured subproblems, which our algorithm exploits. We show that the algorithm converges to the optimal gain and produces gain-optimal policies after finite time. Building on this base algorithm, we develop two further algorithms: one approximately solves the multichain average optimality equations to obtain near gain-optimal policies, and another targets near bias-optimality by approximating the optimal bias function and solving an induced average-reward multichain MDP using the base algorithm. We provide almost-sure convergence guarantees for all three algorithms and empirically compare their tradeoffs, showing that the latter two also consistently improve transient performance relative to the base algorithm. To our knowledge, these are the first essentially model-free average-reward RL algorithms for general multichain MDPs without reductions to discounted problems.

</details>

---

### [[20_Research/Papers/强化学习/Continual_Graph_Multi-Agent_Reinforcement_Learning|Continual Graph Multi-Agent Reinforcement Learning]]

![[assets/2610.10302_first_page.png|800]]

- **arXiv**: [2610.10302](https://arxiv.org/abs/2610.10302)
- **PDF**: https://arxiv.org/pdf/2610.10302
- **详细分析**: [[20_Research/Papers/强化学习/Continual_Graph_Multi-Agent_Reinforcement_Learning|Continual Graph Multi-Agent Reinforcement Learning]]
- **作者**: Tommaso Marzi, Ahmed Hendawy, Jan Peters, Carlo D'Eramo, Andrea Cini, Cesare Alippi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Continual Graph Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CGMARL, CMARL, CRL, InforMARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack dedicated mechanisms to leverage this structural information when learning new tasks, failing to promote transfer and mitigate forgetting. To fill this gap, we propose Continual Graph Multi-Agent Reinforcement Learning (CGMARL), a novel framework for CMARL problems in which task sequences are mapped into a series of attributed graphs, each modeling a task-specific structure. In CGMARL, each graph determines the environment dynamics (next states and/or rewards) and the number of agents for the corresponding task. Then, we present Graph-based Formation (GRAFO), the first CGMARL benchmark, and show how forgetting arises in this setting. Finally, to address this limitation, we propose Frozen Graph Encoder (FROG), a method that relies on a frozen graph backbone to preserve past structural information in graph-based CMARL policies. Experiments on GRAFO show that pairing FROG with existing CL methods substantially improves performance on multiple CGMARL scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Energy-Efficient_Gait_Adaptation_via_Hierarchical_Reinforcement_Learning_for_Quadrupedal_Locomotion_Across_Diverse_Terrains|Energy-Efficient Gait Adaptation via Hierarchical Reinforcement Learning for Quadrupedal Locomotion Across Diverse Terrains]]

![[assets/2610.10297_figure.jpg|800]]

- **arXiv**: [2610.10297](https://arxiv.org/abs/2610.10297)
- **PDF**: https://arxiv.org/pdf/2610.10297
- **详细分析**: [[20_Research/Papers/具身智能/Energy-Efficient_Gait_Adaptation_via_Hierarchical_Reinforcement_Learning_for_Quadrupedal_Locomotion_Across_Diverse_Terrains|Energy-Efficient Gait Adaptation via Hierarchical Reinforcement Learning for Quadrupedal Locomotion Across Diverse Terrains]]
- **作者**: Ammar Issa, Anubhav Singh, Anton Tsaritsin, Sergey Kolyubin
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.92（加权：具身智能 2.1，强化学习 0.96，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Energy-Efficient Gait Adaptation via Hierarchical Reinforcement Learning for Quadrupedal Locomotion Across Diverse Terrains》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While energy efficiency is a critical objective for legged-robot locomotion control, achieving low energy consumption while maintaining robust performance across different velocity ranges and terrain conditions remains a key challenge. This is particularly true for end-to-end RL policies, where gait generation, motion execution, and energy optimization are tightly coupled, leading to high sensitivity to reward design. In this work, we propose a hierarchical reinforcement learning (HRL) framework that separates a high-frequency policy for stable and robust joint-level motion execution from low-frequency gait adaptation that explicitly minimizes the cost of transport (CoT). The three-stage Isaac-based training procedure enables zero-shot sim-to-real transfer with improved tracking accuracy, robustness, and energy efficiency. The learned hierarchy exhibits automatic speed-dependent gait adaptation, transitioning from pacing at low speeds to trotting at higher speeds. We validate the proposed approach in simulation against representative single-policy and hierarchical locomotion baselines, demonstrating reduced CoT over a broad range of commanded velocities, while maintaining robust locomotion across flat, uneven rough, and inclined terrains. We further demonstrate its practical feasibility through zero-shot deployment on a physical Unitree AlienGo quadruped.

</details>

---

### [[20_Research/Papers/具身智能/Many_Ways_to_Succeed_Diversity-Driven_RL_Fine-Tuning_for_VLA_Generalization|Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization]]

![[assets/2610.09943_figure.jpg|800]]

- **arXiv**: [2610.09943](https://arxiv.org/abs/2610.09943)
- **PDF**: https://arxiv.org/pdf/2610.09943
- **详细分析**: [[20_Research/Papers/具身智能/Many_Ways_to_Succeed_Diversity-Driven_RL_Fine-Tuning_for_VLA_Generalization|Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization]]
- **作者**: Haoru Li, Jinmei Liu, Zhiyong Wang, Xiaoming Li, Zhenhong Sun, Daoyi Dong, Chunlin Chen, Zhi Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.62（加权：具身智能 1.8，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternative strategies under distribution shifts. Inspired by this, we introduce DRIVE (Diversity-driven RL fIne-tuning for VLA gEneralization), which turns successful-behavior diversity into an explicit RL objective. DRIVE groups rollouts under matched task conditions, compares their trajectories with temporal alignment, and derives a success-conditioned intrinsic reward from relative behavioral diversity. This design encourages broader coverage of feasible solutions without rewarding diverse failures or superficial timing differences. Across LIBERO-Plus, ManiSkill3, and RoboTwin 2.0, DRIVE improves the average out-of-domain (OOD) performance over vanilla RL fine-tuning by 5.3 points on $π_0$ and 2.0 points on $π_{0.5}$. On a dual-arm AgileX PiPER-X platform, DRIVE further increases average OOD success from 64.1% to 73.3% (+9.2 points), demonstrating gains that persist under physical deployment.

</details>

---

### [[20_Research/Papers/强化学习/Boundary-aware_Reinforcement_Learning_for_Hypercube_State_Spaces_via_Deterministic_Policy_Gradient|Boundary-aware Reinforcement Learning for Hypercube State Spaces via Deterministic Policy Gradient]]

![[assets/2610.09712_figure.png|800]]

- **arXiv**: [2610.09712](https://arxiv.org/abs/2610.09712)
- **PDF**: https://arxiv.org/pdf/2610.09712
- **详细分析**: [[20_Research/Papers/强化学习/Boundary-aware_Reinforcement_Learning_for_Hypercube_State_Spaces_via_Deterministic_Policy_Gradient|Boundary-aware Reinforcement Learning for Hypercube State Spaces via Deterministic Policy Gradient]]
- **作者**: Lijun Bo, Yijie Huang, Chenhao Lu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Boundary-aware Reinforcement Learning for Hypercube State Spaces via Deterministic Policy Gradient》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We develop a continuous-time deterministic policy gradient framework for reinforcement learning with reflected state dynamics, where the state process is governed by a controlled reflected stochastic differential equation on a hypercube. Under suitable regularity assumptions, we establish the connection between the value function and the Neumann Bellman equation, introduce an advantage-rate function that yields a deterministic policy gradient formula, and prove the martingale characterization theorem. Motivated by these theoretical results, we propose a continuous-time deep deterministic policy gradient algorithm for reflected stochastic systems, in which the Neumann boundary condition is imposed via either soft penalization or hard architectural constraint. We further quantify the discrepancy between the ideal continuous-time dynamics and the discretely sampled exploratory dynamics executed in practice, showing that the error decays as the time grid is refined and exploration noise vanishes. Our experiments on reservoir control problems illustrate the effectiveness of the RL framework, highlighting that boundary-aware methods substantially reduce Neumann boundary residuals and enhance learning stability.

</details>

---

### [[20_Research/Papers/大模型/COPC_Coupled_Off-Policy_Correction_for_Asynchronous_LLM_Reinforcement_Learning|COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning]]

![[assets/2610.09597_figure.png|800]]

- **arXiv**: [2610.09597](https://arxiv.org/abs/2610.09597)
- **PDF**: https://arxiv.org/pdf/2610.09597
- **详细分析**: [[20_Research/Papers/大模型/COPC_Coupled_Off-Policy_Correction_for_Asynchronous_LLM_Reinforcement_Learning|COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning]]
- **作者**: Zicheng Hu, Zhijian Zhou, Xuan Zhang, Yuchen Liu, Cheng Chen, Yuan Li, Qi Gu, Yan Feng, Hongyan Hao, Chao Qu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.5，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LLM-RL, LlamaRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous RL accelerates large language model post-training by decoupling rollout generation from optimization, but trains on stale trajectories. Existing methods primarily correct token-level policy mismatch through importance-ratio control in the actor objective. We show that this \emph{policy-side correction} alone is insufficient: advantage estimates also inherit mismatch from behavior-policy continuations, which we term \emph{advantage staleness}. We derive exact bias and variance decompositions for a general two-channel actor update, revealing nonseparable coupling between policy-weight and advantage-estimation errors: their interaction induces multiplicative bias terms, while squared policy weights amplify advantage uncertainty in gradient variance. This motivates the hypothesis that policy- and advantage-side correction should be coordinated. We introduce Coupled Off-Policy Correction (COPC), an actor--critic method combining token-level ratio masking with two-sided clipped-ratio weighting of TD residuals for return and advantage estimation. Joint parameter sweeps across staleness levels support this hypothesis: the effect of one correction parameter depends on, and can reverse with, the other. COPC achieves the highest reported performance on tool-integrated mathematical reasoning and search, outperforming the strongest reported asynchronous baseline in each setting. It also offers a broad high-performing parameter region and improved training stability. In search, COPC remains stable throughout training, while most evaluated asynchronous baselines collapse late in training. These gains persist at 64-step policy staleness. COPC adds minimal step-time overhead over asynchronous PPO and retains a $1.7\times$ step-time speedup over synchronous PPO.

</details>

---

### [[20_Research/Papers/大模型/Immiscible_Diffusion_Policy_Preserving_Multimodal_Robot_Actions_through_Label-Free_Noise_Assignment|Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment]]

![[assets/2610.09369_figure.png|800]]

- **arXiv**: [2610.09369](https://arxiv.org/abs/2610.09369)
- **PDF**: https://arxiv.org/pdf/2610.09369
- **详细分析**: [[20_Research/Papers/大模型/Immiscible_Diffusion_Policy_Preserving_Multimodal_Robot_Actions_through_Label-Free_Noise_Assignment|Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment]]
- **作者**: Xiao Zhang, Yuxin Chen, Zhixuan Liang, Guojian Zhan, Chenran Li, Chenfeng Xu, Masayoshi Tomizuka, Yiheng Li
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Immiscible Diffusion Policy: Preserving Multimodal Robot Actions through Label-Free Noise Assignment》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When diffusion policies were first introduced, they were expected to recover multi-modal action distributions. However, we find this expectation does not always hold, as diffusion policies often collapse to a single modality even when we guarantee the balance of dataset modalities and exact within-batch symmetry. Our analysis indicates that independent action-noise pairing contributes to this failure by increasing mixing and crossing among diffusion paths, which can produce averaged denoising responses and suppress modality-specific behavior. This issue is especially severe in robot planning, where action spaces are dense and low-dimensional, significantly increasing such mixing and crossing. To alleviate this problem, we propose Immiscible Diffusion Policy, a label-free training-time add-on to diffusion policy that uses action-noise assignment to preserve relatively distinct noise-to-action routes without modifying the policy architecture or inference procedure. Across five simulated and two real-world humanoid manipulation tasks spanning state, RGB, and point-cloud observations, our method significantly improves the policy's preservation of action modalities while maintaining strong task performance. It increases the proportion of the non-dominant modality by 6.0x-14.6x across three two-modality tasks and recovers demonstrated modalities that are entirely absent from vanilla policy rollouts on both four-modality tasks. These results demonstrate that Immiscible Diffusion Policy provides a simple yet robust approach to preserving action multi-modality in general robot learning tasks.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Unknown_Constraints_without_Unsafe_Data_via_Optimality_and_Counterfactual_Regularization|Learning Unknown Constraints without Unsafe Data via Optimality and Counterfactual Regularization]]

![[assets/2610.09350_figure.png|800]]

- **arXiv**: [2610.09350](https://arxiv.org/abs/2610.09350)
- **PDF**: https://arxiv.org/pdf/2610.09350
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Unknown_Constraints_without_Unsafe_Data_via_Optimality_and_Counterfactual_Regularization|Learning Unknown Constraints without Unsafe Data via Optimality and Counterfactual Regularization]]
- **作者**: Zhouyu Zhang, Chih-Yuan Chiu, Glen Chou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 世界模型, 具身智能
- **相关性评分**: 1.52（加权：具身智能 0.3，强化学习 0.36，世界模型 0.36，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Learning Unknown Constraints without Unsafe Data via Optimality and Counterfactual Regularization》归入 机器人、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FCRL, ICRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from demonstrations (LfD) provides a framework for inferring unknown constraints from locally optimal, constraint-satisfying expert behavior. Existing approaches largely fall into two paradigms, constrained inverse optimal control (CIOC) and inverse constrained reinforcement learning (ICRL). CIOC exploits optimality conditions such as the Karush--Kuhn--Tucker (KKT) conditions but typically assumes known dynamics and structured constraint representations. Meanwhile, ICRL accommodates complex unknown constraints and unknown transition dynamics but often requires extensive online exploration, during which unsafe constraint violations may occur. In this work, we introduce Counterfactual KKT (CF-KKT), a constraint learning framework that leverages learned dynamics and locally optimal demonstrations to recover unknown constraints without requiring known dynamics or additional risky exploration, thereby combining the data efficiency and safety advantages of CIOC with the flexibility of ICRL. First, we use a locally learned differentiable dynamics model to impose KKT-inspired optimality conditions directly on the demonstrations. Second, we use the learned dynamics to generate reward-improving counterfactual behaviors near the demonstrations, revealing behaviors that would be preferable in the absence of the unknown constraint and thus providing synthetic infeasible data. When the constraint parameterization is known, the same learned-dynamics framework enables direct CIOC-based parameter recovery, and we characterize its sensitivity to dynamics misspecification. Across high-dimensional robotic control tasks, our approach learns neural constraint representations with improved safety and data efficiency relative to state-of-the-art offline ICRL baselines.

</details>

---

### [[20_Research/Papers/强化学习/FLoRa_Flight-Assisted_Data_Collection_from_Duty_Cycling_LoRa_Nodes_under_Energy_Constraints|FLoRa: Flight-Assisted Data Collection from Duty Cycling LoRa Nodes under Energy Constraints]]

![[assets/2610.09226_first_page.png|800]]

- **arXiv**: [2610.09226](https://arxiv.org/abs/2610.09226)
- **PDF**: https://arxiv.org/pdf/2610.09226
- **详细分析**: [[20_Research/Papers/强化学习/FLoRa_Flight-Assisted_Data_Collection_from_Duty_Cycling_LoRa_Nodes_under_Energy_Constraints|FLoRa: Flight-Assisted Data Collection from Duty Cycling LoRa Nodes under Energy Constraints]]
- **作者**: Naresh Babu Kakarla, V. Mahendran
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.76，世界模型 0.16，机器人 0.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《FLoRa: Flight-Assisted Data Collection from Duty Cycling LoRa Nodes under Energy Constraints》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data collection using Unmanned Aerial Vehicles (UAVs) is challenging when LoRa IoT Devices (IoTDs) duty-cycle to conserve battery. Under energy constraints, a UAV must decide which IoTDs to visit, in what order, where to hover, and how many times to probe each node, while time-based data freshness decays. Tractably solving this problem requires a multi-level optimization architecture: discrete combinatorial optimization for routing, continuous global optimization for spatial positioning, and sequential decision-making under uncertainty. We propose FLoRa, a Flight-assisted LoRa data collection architecture using Simulated Annealing (SA) for path planning, Covariance Matrix Adaptation Evolution Strategy (CMA-ES) for hover positioning, and Partially Observable Markov Decision Processes (POMDPs) for probing IoTDs. To quantify collection utility from duty-cycling nodes, we introduce the Value of Information for Pull-based systems (VIP), a metric that rewards fresh data and penalizes failed probes, imposing well-posedness and preventing indefinite probing when an IoTD is off. Tracking hard battery constraints on every POMDP sample path requires state augmentation, worsening the curse of dimensionality. For tractability, SA and CMA-ES work on the hard battery constraints, while at the POMDP layer we relax them into soft average constraints via Lagrangian relaxation. Since solving the network-wide POMDP is computationally complex, we decompose it into node-level POMDPs by approximating inter-node time dependency using a forward-decomposition technique. Evaluation shows FLoRa outperforms metaheuristic, greedy, and deep reinforcement learning baselines by 30.6%, 27.8%, and 15.2% in total expected VIP, while increasing node coverage by 24.5%, 29.2%, and 8.8%, and successful collections by 24.3%, 25.6%, and 15.2%, respectively.

</details>

---

### [[20_Research/Papers/强化学习/Workhorse_Learning_Robust_Whole-Body_Humanoid_Loco-Manipulation_from_Human_Data|Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data]]

![[assets/2610.09117_first_page.png|800]]

- **arXiv**: [2610.09117](https://arxiv.org/abs/2610.09117)
- **PDF**: https://arxiv.org/pdf/2610.09117
- **详细分析**: [[20_Research/Papers/强化学习/Workhorse_Learning_Robust_Whole-Body_Humanoid_Loco-Manipulation_from_Human_Data|Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data]]
- **作者**: Songbo Hu, Qiayuan Liao, Yufeng Chi, Kevin Zakka, Yakun Sophia Shao, Pieter Abbeel, Koushil Sreenath
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots still struggle to plan contact-rich whole-body manipulation from egocentric RGB and proprioception. Workhorse learns such manipulation from robot-free human demonstrations. A visual planner predicts five-link targets: the poses of the torso, both wrists, and both feet. A reinforcement-learning whole-body tracker follows them on the robot. Both policies train separately on the same recorded human poses, without retargeting. We augment the training data of each policy to imitate the errors that the other makes at deployment. On a real Unitree G1, Workhorse sorts boxes with its hands and a kick, catches a thrown box, and topples and climbs a suitcase. During box sorting, we show recoveries after a person pushes the robot or takes the box away. In a simulated copy of the demonstration room, the system completes box sorting in 77% of episodes, and in 64% under 40 N.s pushes. With both policies retrained from the same demonstrations, a simulated second humanoid completes box sorting in 83% of episodes without pushes.

</details>

---

### [[20_Research/Papers/强化学习/HULK_Learning_Whole-Body_Forceful_Loco-Manipulation_for_Humanoids|HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids]]

![[assets/2610.08970_figure.png|800]]

- **arXiv**: [2610.08970](https://arxiv.org/abs/2610.08970)
- **PDF**: https://arxiv.org/pdf/2610.08970
- **详细分析**: [[20_Research/Papers/强化学习/HULK_Learning_Whole-Body_Forceful_Loco-Manipulation_for_Humanoids|HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids]]
- **作者**: An Dang, Arturo Flores Alvarez, Yu-Ming Chen, Conor Mc Gartoll, Helen Sun, Aaron Ames, Nima Fazeli, Manikantan Nambi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.62（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CBF-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation of large, heavy objects demands forceful interaction across the entire body. However, such payloads shift a humanoid's center of mass and impose sustained loads across the upper body, challenging balance and command tracking. We present HULK, a whole-body control framework for forceful loco-manipulation. Using model predictive control (MPC) to guide reinforcement learning with predictions of the loaded dynamics, we train two teachers: one tracks arm motions under wrist forces, and the other locomotes while holding large objects against the body. A capture-point control barrier function augments the wrist-force teacher during training to improve balance under load. We distill both teachers into a single policy. Evaluation spans simulation and the Unitree G1. In simulation, the teacher with the barrier function achieves the lowest forward and lateral velocity tracking errors at 10 kg per arm among evaluated controllers and reduces aggregate divergent component of motion (DCM) excursion magnitude by 35.7% relative to MPC-guided reinforcement learning alone. Our wrist-force teacher withstands torso push disturbances of up to 130 N.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Droplet_Navigation_via_Model-Based_Reinforcement_Learning_Zero-Shot_Transfer_and_Emergent_Dynamics|Autonomous Droplet Navigation via Model-Based Reinforcement Learning: Zero-Shot Transfer and Emergent Dynamics]]

![[assets/2610.08852_figure.png|800]]

- **arXiv**: [2610.08852](https://arxiv.org/abs/2610.08852)
- **PDF**: https://arxiv.org/pdf/2610.08852
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Droplet_Navigation_via_Model-Based_Reinforcement_Learning_Zero-Shot_Transfer_and_Emergent_Dynamics|Autonomous Droplet Navigation via Model-Based Reinforcement Learning: Zero-Shot Transfer and Emergent Dynamics]]
- **作者**: Rajneesh Anand, Mayuresh V. Kothare
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 机器人, 具身智能
- **相关性评分**: 2.72（加权：具身智能 0.3，强化学习 0.96，世界模型 0.96，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Autonomous Droplet Navigation via Model-Based Reinforcement Learning: Zero-Shot Transfer and Emergent Dynamics》归入 强化学习、世界模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-driving laboratories (SDLs) are transforming chemical and materials discovery through closed-loop automation, yet automated infrastructure for physical manipulation of soft, deformable matter remains beyond current robotic platforms. A critical instance is autonomous droplet transport on an open surface, where contact-angle hysteresis, capillary pinning, and surface heterogeneity produce partially observable dynamics that pose significant challenges for classical model-based controllers. We introduce the first robotic platform for closed-loop autonomous liquid droplet navigation on an open, unconfined surface using model-based reinforcement learning. A two-axis tilting board coated with a thin silicone oil film drives the droplet, while an overhead camera provides real-time feedback. A learned policy was trained on just 50 to 150 physical episodes depending on geometric complexity, without simulation or analytical models. Beyond performance alone, the platform demonstrates three capabilities of interest to the SDL community: it robustly transfers zero-shot to unseen geometries; it autonomously discovers an oscillatory depinning strategy to free the droplet when it sticks; and it completes its full training pipeline in under 90 minutes. These results extend reinforcement-learning manipulation from rigid microrobots to deformable soft-matter systems for next-generation SDLs.

</details>

---
