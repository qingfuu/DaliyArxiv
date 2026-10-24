# cs.OH | cs.OH | 2026-10-23

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/强化学习/Cross-Region_Cooperation_of_UAV_Swarms_Towards_Air-Ground_ISAC_via_Hierarchical_Multi-Agent_Reinforcement_Learning|Cross-Region Cooperation of UAV Swarms Towards Air-Ground ISAC via Hierarchical Multi-Agent Reinforcement Learning]]

![[assets/2610.31054_figure.png|800]]

- **arXiv**: [2610.31054](https://arxiv.org/abs/2610.31054)
- **PDF**: https://arxiv.org/pdf/2610.31054
- **详细分析**: [[20_Research/Papers/强化学习/Cross-Region_Cooperation_of_UAV_Swarms_Towards_Air-Ground_ISAC_via_Hierarchical_Multi-Agent_Reinforcement_Learning|Cross-Region Cooperation of UAV Swarms Towards Air-Ground ISAC via Hierarchical Multi-Agent Reinforcement Learning]]
- **作者**: Linghui Miao, Nhan Thanh Nguyen, Shijian Gao
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型
- **相关性评分**: 2.0（加权：大模型 0.4，强化学习 0.8，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Cross-Region Cooperation of UAV Swarms Towards Air-Ground ISAC via Hierarchical Multi-Agent Reinforcement Learning》归入 强化学习、机器人、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, H-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The limited communication resources and sensing perspectives of a single uncrewed aerial vehicle (UAV) motivate UAV swarms for integrated sensing and communication (ISAC) in air-ground networks. However, in multi-region scenarios, regional UAV allocations may not match vehicle demand, while local observations may lack sufficient diversity for accurate sensing. To address these issues, this paper proposes a cross-region cooperation framework for UAV swarms. For communication, cross-region UAV reallocation reduces service disparities by matching resources to vehicle demand. For sensing, combining UAV observations from different regions increases observation diversity, while adaptive handshaking guided by marginal Cramér--Rao bound (CRB) utilities balances phase synchronization gains against handshaking energy consumption. Joint optimization of UAV positions and transmit power within each region then further improves communication service and sensing performance. These coupled decisions are coordinated by a hierarchical multi-agent reinforcement learning (H-MARL) approach through slow-timescale inter-region UAV reallocation and fast-timescale intra-region UAV control. Under the considered simulation settings, reallocation can improve quality of service (QoS) by over 20 percentage points compared with retaining the initial allocation under severe resource-demand mismatches. Cooperative sensing with adaptive handshaking incurs only about a 5.0% increase in mean CRB relative to perfect synchronization.

</details>

---

### [[20_Research/Papers/强化学习/Stability-Preserving_Reinforcement_Learning_for_Heterogeneity-Aware_Composite_Max-Pressure_Traffic_Signal_Control|Stability-Preserving Reinforcement Learning for Heterogeneity-Aware Composite Max-Pressure Traffic Signal Control]]

![[assets/2610.31037_figure.jpg|800]]

- **arXiv**: [2610.31037](https://arxiv.org/abs/2610.31037)
- **PDF**: https://arxiv.org/pdf/2610.31037
- **详细分析**: [[20_Research/Papers/强化学习/Stability-Preserving_Reinforcement_Learning_for_Heterogeneity-Aware_Composite_Max-Pressure_Traffic_Signal_Control|Stability-Preserving Reinforcement Learning for Heterogeneity-Aware Composite Max-Pressure Traffic Signal Control]]
- **作者**: Jichen Zhu, Chaopeng Tan
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Stability-Preserving Reinforcement Learning for Heterogeneity-Aware Composite Max-Pressure Traffic Signal Control》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) provides a flexible mechanism for adapting traffic signal control to heterogeneous traffic and sensing conditions, but directly learned signal actions do not automatically inherit the analytical properties of structured traffic-control methods. This paper proposes Com-MP, a theory-guided RL framework that learns a context-dependent composition of multiple max-pressure (MP) control preferences while retaining decentralized MP phase selection. The learned policy adapts the relative influence of constituent MP formulations according to local traffic and sensing conditions, allowing data-driven adaptation to operate within a structured traffic-control framework. We show that such intersection-specific and time-varying composition preserves strong queue stability for every demand in the strictly stabilizable region under any admissible non-anticipative composition policy, thereby separating the performance-adaptation role of learning from the stability property of the underlying controller. In a representative implementation combining detector-supported queue-based MP and connected-vehicle-supported travel-time MP, experiments on a real-world 45-intersection network show that Com-MP reduces average delay by 15.6\% and 8.6\% relative to the two constituent controllers, respectively, and by about 7.0\% relative to the best fixed composition. The learned composition responds systematically to local traffic and sensing conditions, remains effective under heterogeneous and degraded sensing, and can be transferred without retraining to an unseen network with an average delay only 2.4\% higher than that of a policy trained directly on the target network. These results show how learning-based adaptation can be introduced within a stability-preserving traffic-control structure, providing a theory-guided pathway toward trustworthy learning-enabled traffic signal control.

</details>

---

### [[20_Research/Papers/强化学习/Strategic_Arbitrage_in_Electricity_Markets_A_Multi-Agent_Policy_Optimization_Framework|Strategic Arbitrage in Electricity Markets: A Multi-Agent Policy Optimization Framework]]

![[assets/2610.30446_figure.png|800]]

- **arXiv**: [2610.30446](https://arxiv.org/abs/2610.30446)
- **PDF**: https://arxiv.org/pdf/2610.30446
- **详细分析**: [[20_Research/Papers/强化学习/Strategic_Arbitrage_in_Electricity_Markets_A_Multi-Agent_Policy_Optimization_Framework|Strategic Arbitrage in Electricity Markets: A Multi-Agent Policy Optimization Framework]]
- **作者**: Eli Brock, Srikar Babu Gadipudi, Somayeh Sojoudi, Javad Lavaei
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Strategic Arbitrage in Electricity Markets: A Multi-Agent Policy Optimization Framework》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Grid-scale storage and load aggregators are growing quickly in wholesale electricity markets. If highly consolidated, these new participants may distort the competitive market equilibrium through strategic withholding behavior. Traditional market power mitigation techniques are ill-suited to arbitrage-based participants. We provide a multi-agent policy optimization model to study game-theoretic equilibria for real-time markets with consolidated storage and/or aggregators. The model is designed to facilitate natural first-order equilibrium-seeking update rules. We analyze the theoretical properties of different supply functions and their implications on the convergence of the gradient dynamics. Finally, we train equilibrium policies for a modified version of the IEEE RTS-GMLC benchmark across different levels of storage fleet consolidation, to demonstrate the potential of the framework as a tool to characterize and quantify strategic arbitrage.

</details>

---

### [[20_Research/Papers/机器人/Dynamic_Active_Fleet_Sizing_of_Heterogeneous_UAV_Relays_for_Post-Disaster_Communication_Networks|Dynamic Active Fleet Sizing of Heterogeneous UAV Relays for Post-Disaster Communication Networks]]

![[assets/2610.30323_figure.png|800]]

- **arXiv**: [2610.30323](https://arxiv.org/abs/2610.30323)
- **PDF**: https://arxiv.org/pdf/2610.30323
- **详细分析**: [[20_Research/Papers/机器人/Dynamic_Active_Fleet_Sizing_of_Heterogeneous_UAV_Relays_for_Post-Disaster_Communication_Networks|Dynamic Active Fleet Sizing of Heterogeneous UAV Relays for Post-Disaster Communication Networks]]
- **作者**: Jimin Choi, Max Z. Li
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Systems

#### 研究背景与动机

《Dynamic Active Fleet Sizing of Heterogeneous UAV Relays for Post-Disaster Communication Networks》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FirstNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Uncrewed aerial vehicle (UAV) communication systems are increasingly used to provide temporary connectivity when ground communication infrastructure is damaged by disasters such as hurricanes and wildfires. However, the amount of aerial support required changes as ground networks recover and communication demand evolves. We focus on dynamically adjusting the number and allocation of actively deployed UAVs within a fixed available fleet. We develop a model predictive control (MPC) framework for dynamic fleet sizing of heterogeneous UAV relays during post-disaster communication recovery. The framework accounts for communication demand, ground network recovery, heterogeneous UAV operation, UAV energy availability, and backhaul capacity, which limits how much relayed traffic can be transmitted to the external communication network. The resulting formulation is a convex quadratic program that supports efficient online fleet sizing and deployment decisions. We evaluate the framework using seven historical disaster recovery case studies based on Federal Communications Commission reports, together with four backhaul scenarios and sensitivity analyses. Results show that required active UAV fleet size varies considerably throughout recovery, while backhaul capacity and fleet composition affect communication performance, highlighting the value of adapting active fleet size over time.

</details>

---
