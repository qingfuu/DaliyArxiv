# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-25

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/世界模型/Reliability-aware_AI_Agent_Execution_in_Collaborative_Edge_Computing_A_World_Model_Approach|Reliability-aware AI Agent Execution in Collaborative Edge Computing: A World Model Approach]]

![[assets/2611.32520_figure.jpg|800]]

- **arXiv**: [2611.32520](https://arxiv.org/abs/2611.32520)
- **PDF**: https://arxiv.org/pdf/2611.32520
- **详细分析**: [[20_Research/Papers/世界模型/Reliability-aware_AI_Agent_Execution_in_Collaborative_Edge_Computing_A_World_Model_Approach|Reliability-aware AI Agent Execution in Collaborative Edge Computing: A World Model Approach]]
- **作者**: Xiangchun Chen, Jiannong Cao, Longxiang Gao, Xiaoming Wu, Yusheng Ji
- **cs 子类**: cs.DC
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，世界模型 0.8）
- **关联关键词**: Agent, WorldModel, Systems

#### 研究背景与动机

《Reliability-aware AI Agent Execution in Collaborative Edge Computing: A World Model Approach》归入 世界模型、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaborative edge computing supports AI agent applications by distributing execution across heterogeneous user-controlled devices with limited resources. This paper studies reliability-aware AI agent execution under node failures and wireless disruptions. These disruptions can make agent execution state unavailable or inconsistent, forcing recovery or recomputation that consumes the remaining deadline budget. Maintaining recoverable execution states can therefore improve request completion before deadlines. We formulate an online AI agent execution management problem that jointly selects resource allocations, state protection actions, and recovery targets to maximize the expected task success rate subject to resource, compatibility, and deadline constraints. We develop a world model that jointly captures evolving agent workflows and recoverable execution state under candidate management actions, accounting for node reliability, network conditions, and resource availability. The model enables the controller to simulate future execution and recovery trajectories under candidate actions and estimate their effects on execution progress and task completion before deadlines. We then employ world model-based model predictive control (WorldMPC) with Monte Carlo rollouts to jointly optimize resource allocation, state protection, and recovery decisions for long-term reliable agent execution under the dynamic environment. We evaluate the proposed approach on the simulation and real-world testbed using real-world and synthetic datasets. Experimental results show that WorldMPC improves task success rate over baselines in both simulation and real-world testbed.

</details>

---

### [[20_Research/Papers/强化学习/Multi_Agent_Reinforcement_Learning_enhanced_Federated_Learning_for_Predicting_Remaining_Useful_Lifetime|Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime]]

![[assets/2611.31880_figure.png|800]]

- **arXiv**: [2611.31880](https://arxiv.org/abs/2611.31880)
- **PDF**: https://arxiv.org/pdf/2611.31880
- **详细分析**: [[20_Research/Papers/强化学习/Multi_Agent_Reinforcement_Learning_enhanced_Federated_Learning_for_Predicting_Remaining_Useful_Lifetime|Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime]]
- **作者**: Rajarshi Chattopadhyay, Chen-Khong Tham
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Multi Agent Reinforcement Learning enhanced Federated Learning for Predicting Remaining Useful Lifetime》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Remaining useful life (RUL) prediction is central to Prognostics and Health Management (PHM). The growth of industrial IoT has unlocked large multivariate sensor streams and enabled deep models - especially Transformers - for long-horizon sequence learning. However, transformers are parameter-heavy and data-hungry, while operational datasets are often siloed and privacy-sensitive. Federated Learning (FL) addresses this by training across clients without raw data sharing, but in practice many clients connect over lossy wireless links where UDP is preferred for low latency, making model exchange vulnerable to packet drops. We present a cooperative multi-agent reinforcement learning (MARL) framework that adapts FL to lossy channels by selecting per-client layer subsets to transmit and capping retransmissions. This framework is trained with QMIX value-function factorization for scalability. We instantiate the approach with a Graph Convolution Position-Aware Transformer (GCPATr) for RUL forecasting. On the CMAPSS dataset, our MARL-enhanced FL (RL-FL) consistently improves mean square error over standard FL, with the largest gains at high packet loss (e.g., up to 18% improvement on FD003 at 50% loss). These results show that MARL is an effective countermeasure to wireless degradation in FL-based RUL prediction.

</details>

---
