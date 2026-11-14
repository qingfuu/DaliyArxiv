# cs.OH | cs.OH | 2026-11-13

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Sim-to-Real_Powertrain_Vibration_Control_via_Model-Based_Assisted_Domain-Randomized_Reinforcement_Learning|Sim-to-Real Powertrain Vibration Control via Model-Based Assisted Domain-Randomized Reinforcement Learning]]

![[assets/2611.15133_figure.png|800]]

- **arXiv**: [2611.15133](https://arxiv.org/abs/2611.15133)
- **PDF**: https://arxiv.org/pdf/2611.15133
- **详细分析**: [[20_Research/Papers/强化学习/Sim-to-Real_Powertrain_Vibration_Control_via_Model-Based_Assisted_Domain-Randomized_Reinforcement_Learning|Sim-to-Real Powertrain Vibration Control via Model-Based Assisted Domain-Randomized Reinforcement Learning]]
- **作者**: Heisei Yonezawa, Ansei Yonezawa, Itsuro Kajiwara
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.2，大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Sim-to-Real Powertrain Vibration Control via Model-Based Assisted Domain-Randomized Reinforcement Learning》归入 强化学习、具身智能、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controllers designed from nominal models often degrade on mechanical systems with nonlinearities and parametric variations, such as automotive powertrains with backlash. Deep reinforcement learning (DRL) with domain randomization can acquire robustness to such model discrepancies, but wide randomization destabilizes training and yields conservative policies, and experimental transfer of such policies has rarely been demonstrated in vibration control. This paper presents model-based controller assisted domain randomization (MBCADR), a framework that integrates model-based control into domain-randomized DRL. An $H_{2}$ controller designed from the nominal model supplies a baseline action, while a residual policy trained with twin delayed deep deterministic policy gradient under randomized dynamics compensates for nonlinearities and uncertainties. This model-based assistance relieves the agent of synthesizing the entire control input, thereby stabilizing training under extensive randomization. For each realization of the uncertain parameters, the augmented plant--controller state is shown to be a Markov state of the closed loop, so that domain-randomized training is rigorously formulated as policy optimization over a parameterized family of Markov decision processes. A Lyapunov-based stability analysis further derives a forward-invariant set and an explicit ultimate bound, in which the learned action enters only through its saturation level. Monte Carlo simulations with multiple training seeds show that MBCADR reduces performance variability compared with either component alone. Experiments on a powertrain test bench with backlash, using the simulation-trained policy on an embedded processor without further tuning, confirm successful sim-to-real transfer.

</details>

---

### [[20_Research/Papers/强化学习/Inverse-Optimal_Fixed-Time_Integral_Reinforcement_Learning_for_Unknown_Nonlinear_Leader-Follower_Multi-Agent_Systems|Inverse-Optimal Fixed-Time Integral Reinforcement Learning for Unknown Nonlinear Leader-Follower Multi-Agent Systems]]

![[assets/2611.14927_figure.png|800]]

- **arXiv**: [2611.14927](https://arxiv.org/abs/2611.14927)
- **PDF**: https://arxiv.org/pdf/2611.14927
- **详细分析**: [[20_Research/Papers/强化学习/Inverse-Optimal_Fixed-Time_Integral_Reinforcement_Learning_for_Unknown_Nonlinear_Leader-Follower_Multi-Agent_Systems|Inverse-Optimal Fixed-Time Integral Reinforcement Learning for Unknown Nonlinear Leader-Follower Multi-Agent Systems]]
- **作者**: Tien Dat Vu, Minh Doan
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Inverse-Optimal Fixed-Time Integral Reinforcement Learning for Unknown Nonlinear Leader-Follower Multi-Agent Systems》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper develops a distributed inverse-optimal fixed-time integral reinforcement learning framework for unknown nonlinear leader-follower multi-agent systems. The proposed method first reconstructs the unknown agent dynamics from finite integral data. Based on the identified dynamics, a distributed inverse-optimal formulation is constructed by prescribing a desired fixed-time value function and recovering a compatible running cost. A critic-only integral reinforcement learning architecture is then developed using current integral data and finitely informative experience-replay data, thereby avoiding the persistent-excitation requirement. Practical fixed-time convergence of the critic-weight errors is established in the presence of identification and function-approximation residuals. Finally, a network-level composite Lyapunov analysis proves practical fixed-time leader-following consensus of the true unknown nonlinear multi-agent system. Numerical simulations are provided to validate the developed theory.

</details>

---
