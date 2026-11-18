# cs.OH | cs.OH | 2026-11-16

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Null-Space_Exploitation_in_Pseudo-Inverse_Control_Allocation|Reinforcement Learning for Null-Space Exploitation in Pseudo-Inverse Control Allocation]]

![[assets/2611.18364_figure.png|800]]

- **arXiv**: [2611.18364](https://arxiv.org/abs/2611.18364)
- **PDF**: https://arxiv.org/pdf/2611.18364
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Null-Space_Exploitation_in_Pseudo-Inverse_Control_Allocation|Reinforcement Learning for Null-Space Exploitation in Pseudo-Inverse Control Allocation]]
- **作者**: Umut Demir, Torbjørn Cunis, Aamir Ahmad, Walter Fichter
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Reinforcement Learning for Null-Space Exploitation in Pseudo-Inverse Control Allocation》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pseudo-inverse methods are widely used to solve control allocation problems for overactuated aircraft with redundant control effectors. These methods reliably satisfy the primary command tracking objective, while the remaining null-space degrees of freedom are in principle available for secondary objectives such as drag reduction or actuator wear balancing. However, exploiting this freedom in practice requires hand-tuned weighting matrices or a priori preferred deflections that are difficult to specify across a wide flight envelope with nonlinear, state-dependent dynamics. This paper presents a hybrid architecture in which a reinforcement learning agent operates exclusively within the null space of the control effectiveness matrix, learning secondary objective strategies directly from interaction with the flight dynamics. The null-space projector guarantees by construction that primary command tracking remains invariant regardless of the agent output, providing a principled separation between certified primary control and adaptive secondary optimization. The approach is demonstrated on a nonlinear six-degree-of-freedom distributed electric propulsion aircraft model with aero-propulsive effects across diverse mission scenarios, achieving measurable drag reduction compared to the baseline allocation while preserving tracking integrity and respecting actuator constraints. The proposed architecture forms a foundation for future extensions toward multi-objective, mission-conditioned policies.

</details>

---

### [[20_Research/Papers/强化学习/A_Reinforcement_Learning_Approach_to_Space-Filling_Input_Design_for_Nonlinear_System_Identification|A Reinforcement Learning Approach to Space-Filling Input Design for Nonlinear System Identification]]

![[assets/2611.18229_figure.png|800]]

- **arXiv**: [2611.18229](https://arxiv.org/abs/2611.18229)
- **PDF**: https://arxiv.org/pdf/2611.18229
- **详细分析**: [[20_Research/Papers/强化学习/A_Reinforcement_Learning_Approach_to_Space-Filling_Input_Design_for_Nonlinear_System_Identification|A Reinforcement Learning Approach to Space-Filling Input Design for Nonlinear System Identification]]
- **作者**: Charly Witmeur, Gonçalo G. Cruz, Maarten Schoukens, Mark C. Runacres, Jan Decuyper
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《A Reinforcement Learning Approach to Space-Filling Input Design for Nonlinear System Identification》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose a reinforcement learning (RL) approach to space-filling input design for nonlinear system identification, in which an agent learns a control policy that actively drives the system to explore its state space. Classical input design, developed mainly for linear models, minimises the covariance of the estimated parameters. For nonlinear black-box models, however, the dominant error is the bias induced by the model structure over the region of interest, which motivates space-filling strategies that seek to cover the system state space. Existing space-filling approaches rely on predefined input signal classes and require solving explicit optimisation problems. Unlike these methods, the proposed approach requires no input class to be selected and no frequency band to be tuned for the system at hand, satisfies an amplitude bound by construction, and adapts to varying initial conditions through its observation-based policy without re-optimisation. The learned excitation signals exhibit physically meaningful behaviours, such as resonance excitation and amplitude modulation. The approach is evaluated against tuned swept sine and crest-factor-optimised multisine excitations, and against a state-of-the-art space-filling multisine design, on two nonlinear benchmark systems: a mass-spring-damper with nonlinear stiffness and a Van der Pol oscillator. Under the same amplitude bound, the learned policy achieves the best overall space-filling performance on both systems and distributes its samples more uniformly than the state-of-the-art design.

</details>

---

### [[20_Research/Papers/强化学习/Battery_Energy_Storage_Sizing_in_PV_Ramp-Rate_Smoothing_using_Constraint-Aware_Reinforcement_Learning-Based_Controller|Battery Energy Storage Sizing in PV Ramp-Rate Smoothing using Constraint-Aware Reinforcement Learning-Based Controller]]

![[assets/2611.17612_figure.png|800]]

- **arXiv**: [2611.17612](https://arxiv.org/abs/2611.17612)
- **PDF**: https://arxiv.org/pdf/2611.17612
- **详细分析**: [[20_Research/Papers/强化学习/Battery_Energy_Storage_Sizing_in_PV_Ramp-Rate_Smoothing_using_Constraint-Aware_Reinforcement_Learning-Based_Controller|Battery Energy Storage Sizing in PV Ramp-Rate Smoothing using Constraint-Aware Reinforcement Learning-Based Controller]]
- **作者**: Arash Omidi, Tanmay Mishra, Mads R. Almassalkhi
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Battery Energy Storage Sizing in PV Ramp-Rate Smoothing using Constraint-Aware Reinforcement Learning-Based Controller》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CARL, RRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a constraint-aware reinforcement learning (CARL) controller for battery energy storage system (BESS) sizing and photovoltaic (PV) ramp-rate smoothing. Rapid PV power fluctuations caused by cloud transitions can introduce operational and stability challenges in power systems. To mitigate these impacts, grid codes impose ramp-rate limits (RRL) on PV power injected to the grid. BESSs can support such grid codes by absorbing or supplying power during rapid variations. However, the extent to which BESSs can reduce PV-induced variability depends on (i) the BESS power and energy capacities; and (ii) the adopted controller. Thus, BESS sizing and controller design are coupled. Conventional moving-average control can increase battery usage due to filter-induced lag, while ramp-rate control is reactive and does not account for the long-term impact of actions on battery state of charge and future ramp events. Optimization-based methods can reduce BESS requirements by anticipating future PV variations, but their performance depends on accurate PV forecasts. To address these limitations, the CARL controller learns a causal state-feedback policy from historical PV data without requiring forecasts during deployment. Ramp-rate, converter-power, and state-of-charge constraints are incorporated into a causal feasibility interval that guarantees feasible actions by definition. A full-horizon input-convex neural network (ICNN)-based optimization is developed as a noncausal benchmark for the minimum achievable BESS requirements. Evaluation using three real-world PV datasets shows that, at a 10\%/min ramp-rate limit, CARL reduces peak BESS power by 8.7--10.4\% and energy capacity by 47.5--62.6\% relative to conventional ramp-rate control while maintaining the grid-codes compliance.

</details>

---
