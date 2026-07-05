# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-07-03

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/The_Rollout_Infrastructure_Tax_in_Coding-Agent_Reinforcement_Learning|The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning]]

![[assets/2607.01415_figure.png|800]]

- **arXiv**: [2607.01415](https://arxiv.org/abs/2607.01415)
- **PDF**: https://arxiv.org/pdf/2607.01415
- **详细分析**: [[20_Research/Papers/强化学习/The_Rollout_Infrastructure_Tax_in_Coding-Agent_Reinforcement_Learning|The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning]]
- **作者**: Daniel Thi Graviet, Lovre Pesut, Ivan Dagelic, Vedran Jukic, Ivan Burazin
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding-agent reinforcement learning treats execution infrastructure as a background implementation detail, despite relying on large numbers of interactive software rollouts. This is a missed opportunity: measuring infrastructure overhead can reveal practical efficiency gains for RL post-training, where small per-rollout savings compound at scale. We present a comparative study of four execution substrates: single containers, hosted sandboxes, Kubernetes-orchestrated containers, and cloud virtual machines. We find up to $110\times$ variation in cold-start latency and a $1.8\times$ spread in projected worker-hours for one million 150-step trajectories. Our results suggest that future coding-agent RL systems should optimize execution substrates as part of the training system itself, not merely as deployment plumbing.

</details>

---

### [[20_Research/Papers/机器人/The_Three_Dimensions_of_ROS_2_Middleware|The Three Dimensions of ROS 2 Middleware]]

![[assets/2607.01304_figure.png|800]]

- **arXiv**: [2607.01304](https://arxiv.org/abs/2607.01304)
- **PDF**: https://arxiv.org/pdf/2607.01304
- **详细分析**: [[20_Research/Papers/机器人/The_Three_Dimensions_of_ROS_2_Middleware|The Three Dimensions of ROS 2 Middleware]]
- **作者**: Sanghoon Lee, Taehun Kim, Angelo Corsaro, Kyung-Joon Park
- **cs 子类**: cs.DC, cs.NI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《The Three Dimensions of ROS 2 Middleware》归入 机器人、具身智能 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：WaitSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

ROS 2 (Robot Operating System 2) has emerged as the de facto standard for modern robot software development, with middleware implementations such as the Data Distribution Service (DDS) and Zenoh forming the core infrastructure for distributed robotic communication. Despite their architectural flexibility, these middleware systems exhibit structural limitations, particularly under dynamic and resource-constrained wireless environments. This paper presents a systematic survey of ROS 2 middleware and introduces a conceptual framework to examine its architectural limits through three structural dimensions required by distributed robotic systems, namely Space, Time, and State. We first provide a structured analysis of middleware architecture and operational dynamics, including discovery, data exchange, and state management mechanisms. Building on this foundation, we formalize Time as temporal predictability for control loops, Space as spatial abstraction from physical topology to enable modular deployment, and State as contextual continuity despite dynamic node participation and intermittent connectivity. Through a comprehensive review of existing implementations and prior studies, we organize middleware research according to the structural trade-offs that arise among these dimensions. Under constrained wireless conditions, spatial abstraction can obscure network variability and weaken temporal guarantees, while mechanisms that preserve state continuity introduce computational and network overhead that competes with time-critical communication. These interactions reveal structural trade-offs that characterize the practical limits of contemporary robot middleware. By synthesizing architectural patterns and identifying gaps in current modeling and analysis approaches, this survey outlines a principled research roadmap for robust and scalable robotic middleware architectures.

</details>

---
