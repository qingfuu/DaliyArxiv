# cs.NI | Networking and Internet Architecture | 2026-08-10

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/LYRA_Label-Free_Structural_Synchronization_and_Resource_Allocation_for_UAV_Edge_Networks|LYRA: Label-Free Structural Synchronization and Resource Allocation for UAV Edge Networks]]

![[assets/2608.07392_figure.png|800]]

- **arXiv**: [2608.07392](https://arxiv.org/abs/2608.07392)
- **PDF**: https://arxiv.org/pdf/2608.07392
- **详细分析**: [[20_Research/Papers/强化学习/LYRA_Label-Free_Structural_Synchronization_and_Resource_Allocation_for_UAV_Edge_Networks|LYRA: Label-Free Structural Synchronization and Resource Allocation for UAV Edge Networks]]
- **作者**: Feng He, Alireza Furutanpey, Paolo Bellavista, Yu Qiu, Jiangchuan Liu, Jiannong Cao, Schahram Dustdar
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，机器人 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《LYRA: Label-Free Structural Synchronization and Resource Allocation for UAV Edge Networks》归入 机器人、强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While deploying hierarchical vision models to process mission-critical tasks, UAV edge systems must adaptively update the models to sustain inference reliability under low-level environmental corruption. However, existing work has overlooked the optimal timing for model updates, the impracticality of relying on real-time expert labels, and the significant bandwidth and energy constraints of UAVs. This paper proposes a joint model update scheduling and resource allocation framework, aiming to maximize long-term semantic fidelity and resource efficiency of UAV edge intelligence systems. To address the challenge of label-free semantic evaluation, we formulate the Online Semantic Disagreement Rate (OSDR) as a proxy for timely update triggering, thereby enabling fine-grained Sensitivity-Aware Structural Synchronization (SASS). Furthermore, to overcome the curse of dimensionality in hybrid action spaces and effectively bound long-term energy budgets, we propose a Lyapunov-guided discrete reinforcement learning algorithm that performs action space dimensionality reduction and transforms constraints into virtual queue stability problems. The reported experimental results, based on real traffic traces, demonstrate that the proposed framework consistently outperforms representative baselines in semantic recovery efficiency and update triggering precision, by satisfying long-term energy budget and by reducing average risk backlog by up to 33.3\% in the dynamic environmental corruption scenario.

</details>

---

### [[20_Research/Papers/大模型/EvoRIC_Reinforcement_Learning_Fine-Tuned_LLM-empowered_RAN_Intelligent_Control_Toward_Autonomous_O-RAN|EvoRIC: Reinforcement Learning Fine-Tuned LLM-empowered RAN Intelligent Control Toward Autonomous O-RAN]]

![[assets/2608.06789_first_page.png|800]]

- **arXiv**: [2608.06789](https://arxiv.org/abs/2608.06789)
- **PDF**: https://arxiv.org/pdf/2608.06789
- **详细分析**: [[20_Research/Papers/大模型/EvoRIC_Reinforcement_Learning_Fine-Tuned_LLM-empowered_RAN_Intelligent_Control_Toward_Autonomous_O-RAN|EvoRIC: Reinforcement Learning Fine-Tuned LLM-empowered RAN Intelligent Control Toward Autonomous O-RAN]]
- **作者**: Lingyan Bao, Jemin Lee, Tony Q.S. Quek
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EvoRIC: Reinforcement Learning Fine-Tuned LLM-empowered RAN Intelligent Control Toward Autonomous O-RAN》归入 强化学习、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite recent advances in applying artificial intelligence (AI) techniques to radio access network (RAN), critical challenges remain: traditional machine learning (ML) algorithms suffer from limited generalization across varying network topologies, whereas general-purpose large language models (LLMs) face high computational demands and lack domain-specific knowledge. To address these gaps, this article introduces the evolving RAN intelligent controller (RIC) (EvoRIC) framework, a hierarchical architecture that enables continuous evolution by leveraging a non-real-time RIC (non-RT RIC) for global model updates and a near-real-time RIC (near-RT RIC) for local execution, dynamically empowering LLMs with domain-specific decision-making capabilities. Within this framework, we employ a reinforcement learning-based fine-tuning (RLFT) mechanism where an LLM operates as an actor within a proximal policy optimization (PPO) agent. By leveraging the interaction tuples collected from the wireless environment, the LLM's parameters are iteratively updated to align semantic reasoning with rigorous network performance objectives. We evaluate the generalization and efficacy of the proposed EvoRIC framework within integrated access and backhaul (IAB) networks, and finally, discuss the open challenges and future directions of the EvoRIC framework toward realizing autonomous O-RAN.

</details>

---
