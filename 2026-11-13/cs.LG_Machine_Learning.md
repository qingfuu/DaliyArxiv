# cs.LG | Machine Learning | 2026-11-13

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/强化学习/HALight_Heterogeneous_Multi-Agent_Reinforcement_Learning_for_Traffic_Signal_Control_under_Lane-Level_Missing_Observations|HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations]]

![[assets/2611.16574_figure.png|800]]

- **arXiv**: [2611.16574](https://arxiv.org/abs/2611.16574)
- **PDF**: https://arxiv.org/pdf/2611.16574
- **详细分析**: [[20_Research/Papers/强化学习/HALight_Heterogeneous_Multi-Agent_Reinforcement_Learning_for_Traffic_Signal_Control_under_Lane-Level_Missing_Observations|HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations]]
- **作者**: Chenkai Hu, Yingqian Zhang, Ming Xie, Yi Fang, Chengxiang Jin, Chao Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MARL, TeDA-GCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reinforcement learning has shown great promise for traffic signal control. However, most existing methods rely on two key assumptions: (i) agents are assumed to be homogeneous with unified observation/action spaces; (ii) full and reliable lane-level traffic observations are available to all agents. In practice, urban road networks exhibit substantial structural heterogeneity (e.g., lane configurations and phase designs), while sensor failures and incomplete detector coverage often result in missing incoming lane measurements. Such issues can severely impair coordination and destabilize learning. To address these challenges, we propose HALight, a communication-enhanced heterogeneous multi-agent reinforcement learning framework for traffic signal control under lane-level missing observations. HALight supports intersection-specific observation and action modeling to accommodate heterogeneous intersections, and incorporates a lightweight one-hop neighborhood communication module to enrich spatial context when lane-level observations are partially unavailable. Moreover, HALight adopts a sequential policy update scheme to improve coordination among heterogeneous agents. Experimental results on two real-world road networks demonstrate that HALight outperforms representative homogeneous and heterogeneous baselines in terms of traffic efficiency and convergence behavior. The code and datasets used in this work are available at https://github.com/Huchenkaii/HALight.

</details>

---

### [[20_Research/Papers/强化学习/BlinkMimic_Training_a_Humanoid_Motion_Tracker_in_Minutes_on_a_Single_GPU|BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU]]

![[assets/2611.16422_figure.png|800]]

- **arXiv**: [2611.16422](https://arxiv.org/abs/2611.16422)
- **PDF**: https://arxiv.org/pdf/2611.16422
- **详细分析**: [[20_Research/Papers/强化学习/BlinkMimic_Training_a_Humanoid_Motion_Tracker_in_Minutes_on_a_Single_GPU|BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU]]
- **作者**: Fuyi Chen
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 3.32（加权：具身智能 1.5，强化学习 0.16，世界模型 0.36，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU》归入 具身智能、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DAWNBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body motion tracking lets a humanoid robot follow reference motions, but training a tracking policy for a library of motions has usually taken hours of GPU time. SuperMimic showed that the policy can instead be trained by backpropagating through a world model learned from parallel simulation, and InstantTrack added Muon updates, a residual policy around the reference and an averaged deployed policy. We build on both and present BlinkMimic, a recipe that makes this training faster. On a simulated Unitree G1, BlinkMimic trains one policy for all 40 LAFAN1 clips in 3.4 minutes on a single RTX 4090, measured until three consecutive checkpoints reach a normalized return of at least 0.82 with no failed clip (mean of three seeds). We split training time into the cost of an iteration, the iterations needed to fit the motions, and the iterations needed to remove the last failures, and assign each component, inherited or new, to one of these terms. The new components are a step size that decreases once training has progressed, resets directed by failures of the deployed policy under deployment conditions, and GPU graph capture of the whole iteration. A leave-one-out ablation with three seeds per component shows which term each component affects, and further measurements of the gradient, the update rule and the failure cases explain these effects. Code and per-seed results are available at https://github.com/fuyichen0725/blinkmimic.

</details>

---

### [[20_Research/Papers/强化学习/StateAlign_Internalizing_State-Aware_Decision-Making_for_Reliable_Multi-Turn_Tool_Agents_via_Reinforcement_Learning|StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning]]

![[assets/2611.16304_first_page.png|800]]

- **arXiv**: [2611.16304](https://arxiv.org/abs/2611.16304)
- **PDF**: https://arxiv.org/pdf/2611.16304
- **详细分析**: [[20_Research/Papers/强化学习/StateAlign_Internalizing_State-Aware_Decision-Making_for_Reliable_Multi-Turn_Tool_Agents_via_Reinforcement_Learning|StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning]]
- **作者**: Zhexi Lu, Subhajit Chaudhury, Tejaswini Pedapati, Keerthiram Murugesan, Lei Yu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SimpleToolHalluBench, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has improved the tool-use capabilities of large language models. However, better task performance can coincide with increased tool hallucination. Reliable tool use requires decisions to follow the current task state: available information, tool capabilities, and task progress. Our analysis shows that agents sometimes execute when they should ask for information, retrieve it, or decline an infeasible request, even when reasoning identifies missing information. We introduce StateAlign, combining task-state construction with state-contrastive reinforcement learning. The data cover five task conditions and pair states with different action requirements. Outcome rewards guide task completion; token-level contrasts compare the same generated reasoning and actions under paired states to train outputs that fit the current state. Experiments across five base models from three families show improvements on BFCL v4 multi-turn, ToolSandbox, and When2Call. Ablations show that state construction improves performance and reliability under different reward designs. The complete method further reduces tool hallucination across three Qwen3 sizes. On Qwen3-8B, StateAlign improves BFCL v4 multi-turn accuracy from 45.5% to 55.2% and reduces no-tool hallucination on SimpleToolHalluBench from 62.2% under outcome-only training to 56.1%. Behavioral analyses show more consistent decisions, more complete multi-call execution, and stronger recovery after tool errors.

</details>

---

### [[20_Research/Papers/具身智能/What_Can_a_VLA_Learn_from_the_Agent_That_Calls_It_Task-Level_Experience_Distillation_for_Embodied_Navigation|What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation]]

![[assets/2611.16246_figure.png|800]]

- **arXiv**: [2611.16246](https://arxiv.org/abs/2611.16246)
- **PDF**: https://arxiv.org/pdf/2611.16246
- **详细分析**: [[20_Research/Papers/具身智能/What_Can_a_VLA_Learn_from_the_Agent_That_Calls_It_Task-Level_Experience_Distillation_for_Embodied_Navigation|What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation]]
- **作者**: Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu, Bokui Chen, Houde Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，大模型 0.8，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation》归入 具身智能、大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test time. Agent sessions are not VLA demonstrations. They include motions driven by planner tools and sub-instructions, along with detours. We present H2E, a task-level experience distillation method that converts these sessions into VLA training data. Every motion becomes a VLA action under the original task instruction, with the resulting poses as targets. H2E masks the loss on steps that move away from the goal. It labels every visited state within 1 m of the goal as a stop. We then update the VLA with low-rank adaptation. The VLA learns to stop at the goal and find goals the base model never reaches. On all 3,189 REVERIE-CE val-unseen episodes, H2E raises the success rate of an 8B VLA from 35.0% to 44.9%.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Inventory_Control_under_Regime-Switching_Demand_A_Controlled_Comparison_of_LSTM,_MLP,_and_(s,S)_Policies|Reinforcement Learning for Inventory Control under Regime-Switching Demand: A Controlled Comparison of LSTM, MLP, and (s,S) Policies]]

![[assets/2611.15945_figure.png|800]]

- **arXiv**: [2611.15945](https://arxiv.org/abs/2611.15945)
- **PDF**: https://arxiv.org/pdf/2611.15945
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Inventory_Control_under_Regime-Switching_Demand_A_Controlled_Comparison_of_LSTM,_MLP,_and_(s,S)_Policies|Reinforcement Learning for Inventory Control under Regime-Switching Demand: A Controlled Comparison of LSTM, MLP, and (s,S) Policies]]
- **作者**: Alex Haines, Nathanael L. Baisa
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reinforcement Learning for Inventory Control under Regime-Switching Demand: A Controlled Comparison of LSTM, MLP, and (s,S) Policies》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Classical inventory policies such as (s,S) are provably optimal under stationary demand but cannot adapt when demand switches between hidden regimes, and memoryless deep reinforcement learning policies, confined to a fixed observation window, cannot maintain a belief over latent demand structure. We ask whether a recurrent policy offers a measurable advantage over both a memoryless policy and a classical baseline under regime-switching demand, and how that advantage scales with supply-chain lead time. We build a custom Gymnasium environment in which daily demand is generated by a two-state hidden Markov process with Poisson emissions, so that the regime is known at evaluation time but hidden from the agent. An optimised (s,S) heuristic, an MLP PPO agent, and an LSTM Recurrent PPO agent are trained under matched compute and evaluated at lead times of 0, 3, 6, and 10 days over 30 deterministic episodes each. The recurrent policy outperforms both alternatives at every lead time, and its margin over the MLP widens monotonically with lead time, from parity at lead time 0 to 2.17$\times$ at lead time 10. Principal component analysis of the LSTM hidden state explains the widening gap: the representation shifts from encoding a binary regime indicator at short lead times to encoding multi-step pipeline state at long lead times. Recurrent memory becomes the decisive architectural factor as the credit-assignment horizon lengthens.

</details>

---

### [[20_Research/Papers/强化学习/Understanding_the_Asymptotic_Transience_of_Q-Learning_via_Distributional_Expansion|Understanding the Asymptotic Transience of Q-Learning via Distributional Expansion]]

![[assets/2611.14926_figure.png|800]]

- **arXiv**: [2611.14926](https://arxiv.org/abs/2611.14926)
- **PDF**: https://arxiv.org/pdf/2611.14926
- **详细分析**: [[20_Research/Papers/强化学习/Understanding_the_Asymptotic_Transience_of_Q-Learning_via_Distributional_Expansion|Understanding the Asymptotic Transience of Q-Learning via Distributional Expansion]]
- **作者**: Shengbo Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Understanding the Asymptotic Transience of Q-Learning via Distributional Expansion》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Q-learning has been empirically observed to exhibit substantial transient error. This transient remains uncaptured by the leading Gaussian limit because the central-limit normalization removes the smaller-scale displacement generated by the initial nonlinear evolution. On the other hand, worst-case finite-sample guarantees, while accounting for transient effects, can obscure the mechanisms responsible for the error on a particular problem instance. We develop a finer asymptotic analysis that gives an asymptotically exact characterization of this transient for a fixed instance. Specifically, for synchronous Q-learning in finite discounted Markov decision processes, we separate the last-iterate error into an optimal-policy temporal-difference (TD) component and a nonnegative displacement caused by maximization. The centered TD component has Gaussian fluctuations at scale $n^{-1/2}$, whereas the maximization transient is of order $n^{-1}$ and converges almost surely, after rescaling by $n$, to a random limit. This limit represents the propagated effect of maximization errors generated before the greedy policy stabilizes. We combine this characterization with an Edgeworth expansion of the TD component to identify the corrections to its Gaussian approximation, separating the effects of initialization, non-Gaussian TD fluctuations, and maximization. The results reveal how transient errors arise for individual Q-learning instances and how their effects persist below the central-limit scale.

</details>

---

### [[20_Research/Papers/强化学习/Epigraph_Form_Reinforcement_Learning-based_Safe_Trajectory_Tracking_Control_for_Connected_and_Autonomous_Vehicles|Epigraph Form Reinforcement Learning-based Safe Trajectory Tracking Control for Connected and Autonomous Vehicles]]

![[assets/2611.14903_figure.png|800]]

- **arXiv**: [2611.14903](https://arxiv.org/abs/2611.14903)
- **PDF**: https://arxiv.org/pdf/2611.14903
- **详细分析**: [[20_Research/Papers/强化学习/Epigraph_Form_Reinforcement_Learning-based_Safe_Trajectory_Tracking_Control_for_Connected_and_Autonomous_Vehicles|Epigraph Form Reinforcement Learning-based Safe Trajectory Tracking Control for Connected and Autonomous Vehicles]]
- **作者**: Xiaoke Yang, Jin Chen, Yafei Wang, Qi Zhang, Ming Li, Haiwen Wu, Chengliang Yin, Yong Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Epigraph Form Reinforcement Learning-based Safe Trajectory Tracking Control for Connected and Autonomous Vehicles》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, EFRL, STTC-EFRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe trajectory tracking (STT) aims to enable autonomous vehicles to follow a reference trajectory accurately while avoiding collisions. This problem is particularly challenging for Connected and Autonomous Vehicles (CAVs) in highly dynamic environments. Existing non-learning-based STT methods often use simplified vehicle and interaction models to meet real-time requirements, which may result in suboptimal tracking accuracy. Although Deep Reinforcement Learning (DRL) can help address this limitation, widely used Lagrangian DRL methods often suffer from unstable training because increasing Lagrange multipliers amplify policy-gradient magnitudes. To address these issues, we propose a novel reinforcement learning framework for STT, called STT Control Epigraph Form RL (STTC-EFRL). In this framework, the STT problem is formulated as an epigraph-form min-max optimization problem. Based on this formulation, we develop a learning mechanism that uses a decreasing scalar related to the epigraph to adjust the policy gradient descent direction without increasing the gradient magnitude, thereby improving training stability. We also develop a computationally efficient ray-casting method to compute a polyhedron scaling factor for safety quantification. Experimental results, including Vehicle-in-the-Loop tests, show that STTC-EFRL achieves higher tracking accuracy than the considered non-learning-based baseline and more stable training than widely used Lagrangian DRL methods, while satisfying safety requirements in connected environments.

</details>

---

### [[20_Research/Papers/具身智能/SPIRE_Task-agnostic_embodied_continual_learning_through_autonomous_situation_inference_and_causal_motor-primitive_reuse|SPIRE: Task-agnostic embodied continual learning through autonomous situation inference and causal motor-primitive reuse]]

![[assets/2611.14840_figure.png|800]]

- **arXiv**: [2611.14840](https://arxiv.org/abs/2611.14840)
- **PDF**: https://arxiv.org/pdf/2611.14840
- **详细分析**: [[20_Research/Papers/具身智能/SPIRE_Task-agnostic_embodied_continual_learning_through_autonomous_situation_inference_and_causal_motor-primitive_reuse|SPIRE: Task-agnostic embodied continual learning through autonomous situation inference and causal motor-primitive reuse]]
- **作者**: Yiyang Jia, Mingyang Lyu, Gongce Cao, Feifei Zhao, Yinqian Sun, Yi Zeng
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《SPIRE: Task-agnostic embodied continual learning through autonomous situation inference and causal motor-primitive reuse》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied continual learning requires controllers to infer changing situations, retain prior behavior and reuse motor skills without task labels or known boundaries. The challenge is deciding when to recover earlier behavior and which skills can support new learning. We introduce Situation-guided Primitive Integration for Recurrent Embodiment (SPIRE), a recurrent-spiking system that infers latent contexts from action-outcome evidence and learns context-specific motor actors online. Mature actors become protected sources that combine with a target-context residual to drive recurrent-spiking motor populations. Across coordinate, three-joint and hidden-force control, SPIRE maintained control, autonomously inferred situations, retained prior behavior and accelerated acquisition of an unseen source composition, reducing mean interactions to criterion by approximately 40% relative to matched fresh controllers. Rewinding compatible source actors impaired early acquisition in every matched intervention, demonstrating causal reuse. Against seven recurrent continual-learning and modular-control comparators, SPIRE achieved 2.4 times the mean prior-learning advantage of the strongest eligible task-free alternative selected for each paired stream. These results demonstrate autonomous recovery and causal reuse of motor skills for new learning in continuous embodied control.

</details>

---

### [[20_Research/Papers/强化学习/A_New_Framework_for_Quantum_Reinforcement_Learning|A New Framework for Quantum Reinforcement Learning]]

![[assets/2611.14731_first_page.png|800]]

- **arXiv**: [2611.14731](https://arxiv.org/abs/2611.14731)
- **PDF**: https://arxiv.org/pdf/2611.14731
- **详细分析**: [[20_Research/Papers/强化学习/A_New_Framework_for_Quantum_Reinforcement_Learning|A New Framework for Quantum Reinforcement Learning]]
- **作者**: Alireza Tavakoli, Mohsen Heidari
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《A New Framework for Quantum Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：QRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantum reinforcement learning (QRL) has emerged as a promising approach for controlling quantum systems and accelerating learning tasks with quantum resources. However, most existing QRL formulations still retain a classical reinforcement learning interface: states and actions are often encoded in computational bases and rewards are extracted through measurements. This interface is restrictive for genuinely quantum environments: choosing a measurement can discard entanglement information, while repeated intermediate measurements collapse the evolving state and require costly re-preparation. This motivates a fully QRL framework in which the agent, environment, rewards, and return accumulation are all quantum. In this paper, we take a step toward this goal and introduce a new QRL framework in which both the policy and the environment are modeled by conditional quantum channels. We then propose a quantum policy-gradient algorithm for parameterized conditional quantum channels with a trainable control basis. We also derive finite- and infinite-horizon gradient estimators using a new parameter-shift rule. This rule is needed because policy parameters are shared across repeated interaction blocks and the infinite-horizon objective is not a finite circuit; rather than shifting every occurrence and evaluating the whole trajectory, our estimator shifts only one sampled policy block. Sampling this block from a geometric distribution yields an unbiased gradient estimator under bounded rewards. Finally, we establish convergence of the resulting stochastic gradient-ascent procedure to stationary points under standard smoothness and step-size assumptions.

</details>

---

### [[20_Research/Papers/强化学习/StructRL_Model-Free_Reinforcement_Learning_with_Replay_Graphs|StructRL: Model-Free Reinforcement Learning with Replay Graphs]]

![[assets/2611.14599_figure.png|800]]

- **arXiv**: [2611.14599](https://arxiv.org/abs/2611.14599)
- **PDF**: https://arxiv.org/pdf/2611.14599
- **详细分析**: [[20_Research/Papers/强化学习/StructRL_Model-Free_Reinforcement_Learning_with_Replay_Graphs|StructRL: Model-Free Reinforcement Learning with Replay Graphs]]
- **作者**: Ivo Nowak
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《StructRL: Model-Free Reinforcement Learning with Replay Graphs》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：StructRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

StructRL turns the experience collected during reinforcement learning into an explicit replay graph. Once the graph contains a path to the task goal, dynamic programming selects actions on the observed part of the state space; these actions form a graph policy that is defined only where the required transitions have been observed. StructRL transfers these actions to model-free learners: as action preferences for a DQN Q-model and as target directions along shortest observed paths for a SAC actor. For DQN on three sparse-reward MiniGrid tasks, final success rises from 0.10 to 0.90 (DoorKey), 0.10 to 0.80 (KeyCorridor) and 0 to 0.50 (ObstructedMaze); plain DQN does not catch up with three times the budget. For SAC on continuous PointMaze, graph-derived direction labels raise final success from 0.17 to 1.0 on seven matched runs that reached the goal. Distilling the graph policy into a fresh Q-model gives a DoorKey 6x6 controller that reaches the goal from 91% of reachable states, against 38% for plain DQN. Scaling experiments identify three bottlenecks: incomplete graph support, structural aliasing, and loss of graph information in high-dimensional inputs.

</details>

---
