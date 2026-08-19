# cs.LG | Machine Learning | 2026-08-17

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/强化学习/Offline_Deep_Q_Estimation_with_Diffusion_Models|Offline Deep Q* Estimation with Diffusion Models]]

![[assets/2608.14401_figure.png|800]]

- **arXiv**: [2608.14401](https://arxiv.org/abs/2608.14401)
- **PDF**: https://arxiv.org/pdf/2608.14401
- **详细分析**: [[20_Research/Papers/强化学习/Offline_Deep_Q_Estimation_with_Diffusion_Models|Offline Deep Q* Estimation with Diffusion Models]]
- **作者**: Xiaohong Chen, Yuling Jiao, Lican Kang, Jerry Zhijian Yang, Chen Zhong
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Offline Deep Q* Estimation with Diffusion Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, IRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In offline RL, estimating the optimal action-value function $Q^*$ can be formulated as solving the optimal Bellman equation based solely on offline observations. A fundamental challenge is that the reward function and transition kernel are unknown, so the optimal Bellman operator is not directly observable from data. To address this issue, we propose a novel framework that decouples operator estimation from value function learning. In this approach, we first formulate conditional diffusion models to estimate the reward law and transition kernel, which induces a data-driven approximation of the optimal Bellman operator. We then plug these estimators into the Bellman equation and obtain a deep estimator of $Q^*$ by minimizing the empirical Bellman residual over a neural network function class. Theoretically, we first establish sharp nonasymptotic convergence rates for learning the optimal Bellman operator through an end-to-end analysis of conditional diffusion estimation in total variation distance. We then establish the oracle value-stage rate $\widetilde{\mathcal O}\bigl(n^{-\frac{2β}{d_x+d_a+2β}}\bigr)$ for the excess Bellman residual risk. Finally, under a concentrability condition, we translate this residual bound into an $L^2$ convergence rate of $\widetilde{\mathcal O}\bigl(n^{-\fracβ{d_x+d_a+2β}}\bigr)$ for the resulting deep estimator of $Q^*$, where $d_x$ and $d_a$ denote the dimensions of the state and action spaces, respectively, and $β$ denotes the Hölder smoothness index of $Q^*$. Importantly, our theoretical analysis does not rely on completeness assumptions commonly used in deep RL theory. Extensive numerical experiments demonstrate the effectiveness of the proposed method and its strong empirical performance.

</details>

---

### [[20_Research/Papers/大模型/ATLAS_Discovering_Agent_Strategies_through_LLM-Guided_Abstraction_and_Automata_Learning|ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning]]

![[assets/2608.14352_first_page.png|800]]

- **arXiv**: [2608.14352](https://arxiv.org/abs/2608.14352)
- **PDF**: https://arxiv.org/pdf/2608.14352
- **详细分析**: [[20_Research/Papers/大模型/ATLAS_Discovering_Agent_Strategies_through_LLM-Guided_Abstraction_and_Automata_Learning|ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning]]
- **作者**: Ignacio D. Lopez-Miguel, Andreas Happe, Jürgen Cito, Ezio Bartocci, Bettina Könighofer, Martin Tappler
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based agents are increasingly used for complex tasks such as software testing and cybersecurity assessment. While these agents demonstrate impressive capabilities, their behavior is difficult to understand, explain, and analyze. Existing evaluations focus mainly on task success and execution traces, offering limited insight into the strategies employed by the agent. We present ATLAS (Automata Learning for Agent Trajectory Analysis and Strategy Discovery), an approach for recovering interpretable behavioral models from agent trajectories. ATLAS combines trace abstraction with automata learning to infer finite-state models that capture observed agent-environment interaction strategies. These models provide human-interpretable insights and support automated analyses of recurring behaviors, decision points, successful task-completion paths, and failure loops. As a proof of concept, we apply ATLAS to trajectories generated by an LLM-based penetration-testing agent. The resulting models expose high-level behavioral strategies for exploiting vulnerable machines that are difficult to identify from raw execution traces alone. We discuss how learned behavioral models can support explainability, model-guided exploration, auditing, and analysis of agentic systems. We further demonstrate symbolic model-based knowledge transfer from powerful frontier models to compact language models. In addition, we show how model transformations can derive concise explanations of agent behavior in a penetration-testing case study comprising 12 vulnerable machines. ATLAS highlights a new opportunity for model-driven engineering: transforming agent trajectories into explicit behavioral models that enable systematic understanding and analysis of otherwise opaque AI agents.

</details>

---

### [[20_Research/Papers/具身智能/CORAL_Curriculum-Optimized_Reward_Adaptation_for_LiDAR-Based_Goal-Directed_Urban_Driving|CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving]]

![[assets/2608.14332_figure.png|800]]

- **arXiv**: [2608.14332](https://arxiv.org/abs/2608.14332)
- **PDF**: https://arxiv.org/pdf/2608.14332
- **详细分析**: [[20_Research/Papers/具身智能/CORAL_Curriculum-Optimized_Reward_Adaptation_for_LiDAR-Based_Goal-Directed_Urban_Driving|CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving]]
- **作者**: Anisa Saleem, Duksu Kim
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL, Systems

#### 研究背景与动机

《CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet, VoxelNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning is promising for autonomous urban driving, but long-horizon goal-directed navigation asks a policy to acquire several competing behaviors at once--reaching a distant goal, tracking a route, avoiding obstacles, obeying signals--and a fixed objective gives no order in which to learn them. This paper presents CORAL, which advances two schedules together: a five-stage curriculum that progressively lengthens routes and tightens behavioral constraints, and a stage-aware reward whose component weights shift emphasis from mission progress toward route following, safety, smoothness, and rule compliance as the task hardens. The policy is a multi-stream actor-critic network trained with Proximal Policy Optimization (PPO) in CARLA on a compact 99-dimensional state pairing a polar LiDAR histogram with vehicle telemetry, ego-frame route geometry, and traffic-rule indicators--no point-cloud encoder, no bird's-eye-view rasterization. Against two PPO baselines under an identical protocol, CORAL reaches the goal in all twenty evaluation episodes on the longest routes under the full set of behavioral constraints, where the baselines reach 5% and 10%; a factorial ablation shows that neither schedule alone matches their combination: removing either lowers both success and route completion, and disabling both drops success to 55%. Trained in one town, the policy transfers zero-shot to seven unseen towns, succeeding in 68-98% of episodes on routes of the same 100-150 m length, with mean lateral deviation below 0.35 m.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_solution_for_pickup_and_delivery_routing_problems_with_time_window_and_capacity_constraints|Deep Reinforcement Learning solution for pickup and delivery routing problems with time window and capacity constraints]]

![[assets/2608.14156_figure.png|800]]

- **arXiv**: [2608.14156](https://arxiv.org/abs/2608.14156)
- **PDF**: https://arxiv.org/pdf/2608.14156
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_solution_for_pickup_and_delivery_routing_problems_with_time_window_and_capacity_constraints|Deep Reinforcement Learning solution for pickup and delivery routing problems with time window and capacity constraints]]
- **作者**: Andrew Soroka, Alex Meshcheryakov, Sergey Gerasimov
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Deep Reinforcement Learning solution for pickup and delivery routing problems with time window and capacity constraints》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PtrNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The task of constructing vehicles optimal routes for pickup and delivery of goods is one of most promising tasks in the context of global urban population growth. Although this kind of problems with small size can be solved by various classical approaches, a fast (or realtime) route optimizer under the constraints of the real world (such as capacity and time windows constraints) for medium-large size problems still remains a highly challenging task. In this work we, for the first time, successfully applied a deep Reinforcing Learning approach (modified JAMPR model) to solve Pickup and Delivery problem with Capacity and Time Window constraints (CPDPTW). We obtained a robust model that gives a fast optimal solution for problems of small and medium size, and gives fast suboptimal solution for problems of larger (&gt; 200) size.

</details>

---

### [[20_Research/Papers/强化学习/AgilePE_Autonomous_UAV_Pursuit-Evasion_via_Self-Play_Reinforcement_Learning|AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning]]

![[assets/2608.14135_figure.jpg|800]]

- **arXiv**: [2608.14135](https://arxiv.org/abs/2608.14135)
- **PDF**: https://arxiv.org/pdf/2608.14135
- **详细分析**: [[20_Research/Papers/强化学习/AgilePE_Autonomous_UAV_Pursuit-Evasion_via_Self-Play_Reinforcement_Learning|AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning]]
- **作者**: Wenhao Tang, Tianyang Chen, Zhejun Cui, Boyuan An, Jiayu Chen, Ruize Zhang, Huidong Liu, Tianyue Wu, Qingmin Liao, Fei Gao, Yu Wang, Chao Yu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 大模型, 世界模型
- **相关性评分**: 3.22（加权：具身智能 0.6，大模型 0.2，强化学习 1.16，世界模型 0.16，机器人 1.1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous pursuit-evasion is a fundamental challenge for Unmanned Aerial Vehicles (UAVs), requiring rapid decision-making under tightly coupled dynamics and continuously changing opponent behaviors. Traditional rule-based or differential-game approaches often struggle with high-dimensional aerial interactions and agile maneuvering. We present AgilePE, a complete system for autonomous UAV pursuit-evasion via self-play reinforcement learning. AgilePE integrates agile low-level control, competitive policy optimization, and sim-to-real deployment in a unified framework. The policy directly maps onboard state observations to Collective Thrust and Body Rates (CTBR) commands, enabling end-to-end agile maneuvering without intermediate trajectory planners or waypoint controllers. For training, we use competitive self-play with Prioritized Fictitious Self-Play (PFSP) and a diversified opponent pool, enabling agents to improve against historical policies while stabilizing optimization and reducing policy oscillation. This process leads to the emergence of sophisticated pursuit and evasion strategies. For real-world deployment, we develop a hardware-aligned simulation pipeline that models actuator-response dynamics, communication latency, and domain randomization. The learned policies transfer zero-shot to real quadrotors without task-specific tuning. Real-world experiments reproduce pursuit-evasion tactics observed in simulation, including rapid dodging and flanking, and demonstrate interactive two-agent zero-shot deployment.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Run_Power_Networks_Effective_AlphaZero-inspired_Topological_Control|Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control]]

![[assets/2608.14114_first_page.png|800]]

- **arXiv**: [2608.14114](https://arxiv.org/abs/2608.14114)
- **PDF**: https://arxiv.org/pdf/2608.14114
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Run_Power_Networks_Effective_AlphaZero-inspired_Topological_Control|Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control]]
- **作者**: Lukas Zetto, Benjamin Schäfer, Qiong Huang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As the integration of volatile renewable energy sources increases the strain on modern power grids, the use of Reinforcement Learning (RL) for autonomous topological reconfiguration has emerged as a promising research field to keep strained grids stable and operational. Compared to traditional redispatching measures, topological actions offer a cheaper and more cost-effective way to manage grid congestion. However, their implementation is hindered by a vast combinatorial action space and strict operational constraints. This paper investigates the effectiveness of model-based AlphaZero-inspired approaches that utilize Monte Carlo Tree Search (MCTS) for proactive grid management. We systematically evaluate how reward functions, observation density, and search guidance influence an agent's survivability. Our results demonstrate that the optimized AlphaZero approach achieves a peak survivability of 98.43%, significantly outperforming the proximal policy optimization (PPO) variant. We find that conducting the MCTS without guidance from a prior learned policy or value function can enhance training efficiency, and that a straightforward binary survival reward provides more effective search guidance than complex, multi-objective functions. Our findings demonstrate that while AlphaZero is a powerful framework for topological control, pure reinforcement learning is not sufficient; rather, an effective and reliable system requires a 'minimalist' integration of domain-specific heuristics, binary rewards, and a restricted observation space of line loads.

</details>

---

### [[20_Research/Papers/大模型/Model-agnostic_Retrieval-Augmented_Extended_Forecasting_for_time_series|Model-agnostic Retrieval-Augmented Extended Forecasting for time series]]

![[assets/2608.14054_first_page.png|800]]

- **arXiv**: [2608.14054](https://arxiv.org/abs/2608.14054)
- **PDF**: https://arxiv.org/pdf/2608.14054
- **详细分析**: [[20_Research/Papers/大模型/Model-agnostic_Retrieval-Augmented_Extended_Forecasting_for_time_series|Model-agnostic Retrieval-Augmented Extended Forecasting for time series]]
- **作者**: Juan Pablo Villa Serna, Rohan Asthana, Vasileios Belagiannis
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: cs.LG

#### 研究背景与动机

《Model-agnostic Retrieval-Augmented Extended Forecasting for time series》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time series forecasting with pretrained foundation models has demonstrated strong zero-shot capabilities. However, achieving optimal performance on time series with short or negligible historical data in domain-specific applications typically requires adaptation via either fine-tuning or RAG. While fine-tuning is effective, it incurs substantial computational costs. This work explores RAG within univariate time series (Retrieval Augmented Generation) as a more efficient alternative, in particular RAF (Retrieval Augmented Forecasting), and introduces RAEF (Retrieval-Augmented Extended Forecasting), a model-agnostic method built upon RAF. RAEF incorporates key refinements to the retrieval and aggregation mechanisms: (1) direct retrieval in input-space rather than embedding-space, reducing inference overhead, and (2) concatenation-based aggregation that preserves temporal structure instead of averaging. Empirical evaluation across multiple benchmark datasets demonstrates that RAEF outperforms RAF in both accuracy and inference overhead. Furthermore, comprehensive comparisons with zero-shot and fine-tuned foundation models show that RAEF achieves competitive or superior performance to fine-tuning while avoiding its computational burden, establishing it as a practical and scalable approach for domain adaptation in time series forecasting.

</details>

---

### [[20_Research/Papers/强化学习/Dynamic_Multi-Depot_Vehicle_Routing_with_Online_Requests_Event-Driven_Transformer--DRL_and_Rolling-Horizon_Benchmarking|Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking]]

![[assets/2608.13799_figure.png|800]]

- **arXiv**: [2608.13799](https://arxiv.org/abs/2608.13799)
- **PDF**: https://arxiv.org/pdf/2608.13799
- **详细分析**: [[20_Research/Papers/强化学习/Dynamic_Multi-Depot_Vehicle_Routing_with_Online_Requests_Event-Driven_Transformer--DRL_and_Rolling-Horizon_Benchmarking|Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking]]
- **作者**: Faezeh Ardali, Gerald M. Knapp
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an event-driven learning and benchmarking framework for the Dynamic Multi-Depot Vehicle Routing Problem with progressively revealed requests and evolving vehicle states. Masked MLP and Transformer policies are trained through behavior cloning and proximal policy optimization. Deterministic feasibility masking prevents invalid vehicle--request assignments, while fixed-prefix/flexible-suffix route commitments protect completed, active, and near-term decisions and separately measure vehicle reassignment and resequencing. The learned policies are compared with dynamic insertion heuristics and time-limited rolling-horizon optimization. In a 20-scenario policy benchmark, all methods completed every request without invalid actions, but nearest feasible achieved the lowest mean objective and outperformed the learned policies in routing quality, waiting time, stability, makespan, and runtime. Across five independent training runs, PPO had little average effect on the MLP and improved the Transformer on average, although with greater seed variability. Under the common protocol, nearest feasible achieved the lowest combined objective and route disruption, whereas rolling horizon achieved the lowest waiting times and makespan at substantially higher computational cost. The learned policies retained millisecond-level decisions and transferred to instances with up to 80 requests without retraining, but did not outperform the strongest heuristic. No single method was best across routing efficiency, service responsiveness, stability, and online computation.

</details>

---

### [[20_Research/Papers/世界模型/hint$^2$_Hierarchical_World_Models_for_Inference-Time_Temporal_Logic_Guidance|hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance]]

![[assets/2608.13678_figure.png|800]]

- **arXiv**: [2608.13678](https://arxiv.org/abs/2608.13678)
- **PDF**: https://arxiv.org/pdf/2608.13678
- **详细分析**: [[20_Research/Papers/世界模型/hint$^2$_Hierarchical_World_Models_for_Inference-Time_Temporal_Logic_Guidance|hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance]]
- **作者**: Moritz Zoellner, Anastasios Manganaris, Ahmed H. Qureshi, Rohan Paleja
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.32（加权：具身智能 0.3，强化学习 0.16，世界模型 1.36，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A central goal of robot learning is to enable robots to execute rich instructions specified at runtime. Large-scale language-conditioned policies have made substantial progress toward this goal, yet still struggle with temporal structure and safety constraints. Linear Temporal Logic (LTL) provides a powerful language to express complex, non-Markovian instructions. However, guiding learned manipulation policies toward LTL satisfaction remains challenging because modern policies generate short-horizon action chunks and replan in closed loop, while almost all LTL specifications are evaluated over long-horizon trajectories. In this paper, we introduce hint$^2$, a method for guiding short-horizon policies toward satisfying complex LTL specifications at inference time using hierarchical world models. Our key idea is to derive two separate guidance objectives using each world model's abstraction level. A high-level model predicts future action-induced transitions in task-relevant atomic propositions to guide progress through the LTL automaton, while a low-level dynamics model predicts immediate state evolution for accurate local safety guidance. Our results show that hint$^2$ overcomes the limitations of current LTL-guided diffusion methods, outperforms existing inference-time steering methods in CALVIN, and successfully completes instructions with complex liveness and safety constraints more elegantly than language-conditioned alternatives. Finally, we demonstrate that hint$^2$ can handle complex instructions on a real UR5e manipulator.

</details>

---

### [[20_Research/Papers/机器人/Adjacency-Based_Spectral_Proxy_Control_of_Mobile_Communication_Agents|Adjacency-Based Spectral Proxy Control of Mobile Communication Agents]]

![[assets/2608.13616_first_page.png|800]]

- **arXiv**: [2608.13616](https://arxiv.org/abs/2608.13616)
- **PDF**: https://arxiv.org/pdf/2608.13616
- **详细分析**: [[20_Research/Papers/机器人/Adjacency-Based_Spectral_Proxy_Control_of_Mobile_Communication_Agents|Adjacency-Based Spectral Proxy Control of Mobile Communication Agents]]
- **作者**: Mariana del Castillo, Federico Larroca
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Adjacency-Based Spectral Proxy Control of Mobile Communication Agents》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider a heterogeneous mobile-agent network composed of uncontrolled task agents and controllable communication agents. The objective is to reposition communication agents online as task agents move. Since throughput-based objectives are generally unsuitable for real-time control, spectral graph metrics such as algebraic connectivity are commonly adopted as surrogate objectives. However, controlling algebraic connectivity relies on the eigenvector corresponding to the second-smallest eigenvalue of a graph's Laplacian matrix (i.e., the Fiedler vector), whose distributed estimation requires an unbounded number of communication rounds to converge. In this work, we identify a structural decomposition of this Fiedler-gradient controller into a local interaction rule and a graph embedding component, suggesting the use of alternative embeddings that are easier to estimate distributively than the Fiedler vector. As a particular instance, we propose A-Fiedler, which replaces the Fiedler embedding with the dominant eigenvector of the adjacency matrix, commonly used as a graph embedding of nodes into a latent geometry. This representation is more naturally suited for distributed implementation under local communication constraints. We evaluate A-Fiedler against the classical Fiedler-gradient controller. Results show comparable network performance in the absence of communication constraints and improved robustness under distributed estimation. For instance, under the same number of communication rounds, the Fielder-gradient may even converge to disconnected configurations whereas our proposition maintains performance. We believe our contribution provides a simpler path toward distributed network control.

</details>

---
