# cs.OH | cs.OH | 2026-07-01

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/强化学习/On_the_Comparison_of_Reinforcement_Learning_and_Adaptive_Control_for_Linear_Systems_under_Packet_Loss_and_Uncertainty|On the Comparison of Reinforcement Learning and Adaptive Control for Linear Systems under Packet Loss and Uncertainty]]

![[assets/2606.32003_figure.png|800]]

- **arXiv**: [2606.32003](https://arxiv.org/abs/2606.32003)
- **PDF**: https://arxiv.org/pdf/2606.32003
- **详细分析**: [[20_Research/Papers/强化学习/On_the_Comparison_of_Reinforcement_Learning_and_Adaptive_Control_for_Linear_Systems_under_Packet_Loss_and_Uncertainty|On the Comparison of Reinforcement Learning and Adaptive Control for Linear Systems under Packet Loss and Uncertainty]]
- **作者**: Moh Kamalul Wafi
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《On the Comparison of Reinforcement Learning and Adaptive Control for Linear Systems under Packet Loss and Uncertainty》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a comparative study between Adaptive Quantized Control (AQC) and Deep Deterministic Policy Gradient (DDPG) reinforcement learning for uncertain linear systems with input quantization over communication channels subject to packet loss. The considered setting also includes dynamic switching from a nominal unstable system to a more unstable one during operation. The AQC is designed for unknown system dynamics using acknowledgment messages to compensate for packet losses, whereas the DDPG controller is trained using the nominal system model without acknowledgment messages. Numerical results show that the DDPG controller achieves faster transient responses and improved damping within its training environment. However, under model uncertainty, packet loss, and dynamic switching, the AQC consistently demonstrates superior robustness owing to its rigorous Lyapunov stability guarantees. These results highlight the trade-off between data-driven performance and model-based robustness, and provide insight into the applicability of reinforcement learning and adaptive control for networked uncertain systems.

</details>

---

### [[20_Research/Papers/强化学习/Dynamic_Scheduling_for_Flexible_Manufacturing_Systems_Based_on_Multi-Agent_Deep_Reinforcement_Learning_and_Petri_Nets|Dynamic Scheduling for Flexible Manufacturing Systems Based on Multi-Agent Deep Reinforcement Learning and Petri Nets]]

![[assets/2606.31737_figure.png|800]]

- **arXiv**: [2606.31737](https://arxiv.org/abs/2606.31737)
- **PDF**: https://arxiv.org/pdf/2606.31737
- **详细分析**: [[20_Research/Papers/强化学习/Dynamic_Scheduling_for_Flexible_Manufacturing_Systems_Based_on_Multi-Agent_Deep_Reinforcement_Learning_and_Petri_Nets|Dynamic Scheduling for Flexible Manufacturing Systems Based on Multi-Agent Deep Reinforcement Learning and Petri Nets]]
- **作者**: Zhou He, Ning Li, Ning Ran, Liang Li, Carla Seatzu
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.0（加权：大模型 0.4，强化学习 1.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Dynamic Scheduling for Flexible Manufacturing Systems Based on Multi-Agent Deep Reinforcement Learning and Petri Nets》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates dynamic scheduling for flexible manufacturing systems (FMSs) subject to dynamic events, such as new order arrivals, temporary order cancellations, and machine failures. Traditional methods often face significant challenges in achieving real-time responsiveness under such conditions. To address this issue, the scheduling problem is formulated as a Markov decision process (MDP) with timed Petri nets, where the future evolution of the system depends exclusively on the current marking and the subsequently executed transitions, independent of historical trajectories. The state space and action space of the MDP are constructed using the notion of basis reachability graph (a compact state space representation) of Petri nets to alleviate the state explosion problem, thereby accelerating model training convergence. Meanwhile, a hierarchical dense reward function is constructed by integrating stepwise guidance with terminal evaluation. Then, a multi-agent proximal policy optimization algorithm is employed for model training under the centralized training and decentralized execution paradigm to improve scheduling efficiency. Numerical experiments are conducted involving typical dynamic events, and the results demonstrate that the proposed method can effectively handle dynamic events and achieve superior scheduling performance compared with conventional approaches.

</details>

---

### [[20_Research/Papers/大模型/A_Novel_Method_for_Differential-Algebraic_Dynamic_Model_Discovery_in_Power_Systems_An_LLM-Based_Multi-Agent_Collaborative_Framework|A Novel Method for Differential-Algebraic Dynamic Model Discovery in Power Systems: An LLM-Based Multi-Agent Collaborative Framework]]

![[assets/2606.31314_figure.png|800]]

- **arXiv**: [2606.31314](https://arxiv.org/abs/2606.31314)
- **PDF**: https://arxiv.org/pdf/2606.31314
- **详细分析**: [[20_Research/Papers/大模型/A_Novel_Method_for_Differential-Algebraic_Dynamic_Model_Discovery_in_Power_Systems_An_LLM-Based_Multi-Agent_Collaborative_Framework|A Novel Method for Differential-Algebraic Dynamic Model Discovery in Power Systems: An LLM-Based Multi-Agent Collaborative Framework]]
- **作者**: Xinming Wang, Fan Tang, Yingli Wei, Yakun He, Zhe Liu, Ping Jiang, Haoyu Wu, Zihan Guo, Chao Shen
- **cs 子类**: 
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《A Novel Method for Differential-Algebraic Dynamic Model Discovery in Power Systems: An LLM-Based Multi-Agent Collaborative Framework》归入 大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With large-scale integration of emerging power electronic devices represented by grid-forming inverters, power system dynamics increasingly exhibit strong nonlinearity, multi-timescale coupling, and black-box control logic. These features hinder conventional parameter identification requiring known model structures and structure identification based on predefined function libraries, making complete differential-algebraic dynamic model recovery difficult under weak prior information. To address this challenge, this paper proposes an LLM-based multi-agent collaborative framework for differential-algebraic dynamic model discovery in power systems. It integrates heterogeneous exploratory agents, individual candidate model memories, parameter fitting and evaluation, and a coordinator agent. Under unified measurement-data constraints, agents generate candidate equation structures in parallel, while candidates are optimized, evaluated, retained, and summarized to provide closed-loop search guidance. The task is decomposed into differential equation structure discovery and algebraic closure discovery, enabling joint recovery of state dynamics, algebraic constraints, and key intermediate variables with incomplete prior information. Case studies on synchronous generators and grid-forming inverters show that the proposed method outperforms single-agent LLM-based discovery and conventional symbolic regression in reconstruction accuracy, generalization, search efficiency, and noise robustness. In the generator case, OOD MAPE reaches 0.19\%; in the inverter case, discovery time is reduced by 25.7\% compared with the single-agent LLM baseline.

</details>

---
