# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-16

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/强化学习/TIDE_Reclaiming_Lost_Performance_In_On-Policy_Reinforcement_Learning|TIDE: Reclaiming Lost Performance In On-Policy Reinforcement Learning]]

![[assets/2611.17924_figure.png|800]]

- **arXiv**: [2611.17924](https://arxiv.org/abs/2611.17924)
- **PDF**: https://arxiv.org/pdf/2611.17924
- **详细分析**: [[20_Research/Papers/强化学习/TIDE_Reclaiming_Lost_Performance_In_On-Policy_Reinforcement_Learning|TIDE: Reclaiming Lost Performance In On-Policy Reinforcement Learning]]
- **作者**: Mathew Jacob, Morgan Borjigin-Wang, Kan Zhu, Po Hao Chen, Yi Pan, Andy Ruan, Nayani Modugula, Ethan Lavi, Luis Ceze, Malte Schwarzkopf, Akshay Narayan, Deepti Raghavan...
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《TIDE: Reclaiming Lost Performance In On-Policy Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：StreamRL, ThunderSyncRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synchronous, colocated RL post-training of large language models (LLMs) today suffers from severe under-utilization due to long-tail rollouts. Inference engines fall idle waiting for long-tail rollouts or decode at low, inefficient batch sizes. To address this, we present TIDE, an RL training system that preserves on-policy training semantics while recovering resource utilization. TIDE does so by two complementary techniques: (1) dynamically repurposing rollout GPUs for training while long-tail rollouts complete and (2) dynamically migrating rollouts between inference engines to boost decoding throughput. TIDE automatically determines the right time to repurpose rollout resources through an adaptive migration policy, obtaining performance improvements that generalize across multiple applications and hardware configurations without requiring bespoke configuration. In our evaluation, TIDE provides end-to-end speedups of up to 1.36x over colocated systems, outperforming all evaluated on-policy baselines and achieving up to 97% of optimal throughput.

</details>

---

### [[20_Research/Papers/大模型/OrbitWeaver_LLM_Agent_Planning_with_Simulation_Feedback_for_Optically_Interconnected_Orbital_GPU_Clusters|OrbitWeaver: LLM Agent Planning with Simulation Feedback for Optically Interconnected Orbital GPU Clusters]]

![[assets/2611.17850_figure.png|800]]

- **arXiv**: [2611.17850](https://arxiv.org/abs/2611.17850)
- **PDF**: https://arxiv.org/pdf/2611.17850
- **详细分析**: [[20_Research/Papers/大模型/OrbitWeaver_LLM_Agent_Planning_with_Simulation_Feedback_for_Optically_Interconnected_Orbital_GPU_Clusters|OrbitWeaver: LLM Agent Planning with Simulation Feedback for Optically Interconnected Orbital GPU Clusters]]
- **作者**: Pengcheng Luo, Bowen Zhang
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《OrbitWeaver: LLM Agent Planning with Simulation Feedback for Optically Interconnected Orbital GPU Clusters》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KernelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Space-based data-center designs increasingly consider GPU computing formations connected by inter-satellite optical links. With limited neighboring connections, jobs assigned disjoint GPUs can still contend on shared relay paths. Rank placement and communication priorities jointly affect this contention and the readiness of downstream computation. We present OrbitWeaver, an offline large language model (LLM) agent planner that jointly optimizes rank placement and communication order. Guided by communication structure, execution dependencies, and simulation feedback, the agent constructs and refines plans that coordinate shared-link access with computation progress. This coordination reduces contention and dependency blocking, shortening mean job completion time (JCT). Simulation experiments on optically interconnected orbital GPU clusters show that OrbitWeaver reduces aggregate mean JCT by 6.2-33.5% relative to the state-of-the-art baselines CASSINI, Crux, and Symphony. These results demonstrate the value of LLM-guided planning for efficient concurrent computing in orbital GPU clusters.

</details>

---

### [[20_Research/Papers/机器人/INC-SRv6_In-Network_Route_Exploration_and_Fast_Failover_Using_Segment_Routing_Headers_in_Dynamic_UAV_Networks|INC-SRv6: In-Network Route Exploration and Fast Failover Using Segment Routing Headers in Dynamic UAV Networks]]

![[assets/2611.17659_first_page.png|800]]

- **arXiv**: [2611.17659](https://arxiv.org/abs/2611.17659)
- **PDF**: https://arxiv.org/pdf/2611.17659
- **详细分析**: [[20_Research/Papers/机器人/INC-SRv6_In-Network_Route_Exploration_and_Fast_Failover_Using_Segment_Routing_Headers_in_Dynamic_UAV_Networks|INC-SRv6: In-Network Route Exploration and Fast Failover Using Segment Routing Headers in Dynamic UAV Networks]]
- **作者**: Zhiyuan Ren, Zhao Li
- **cs 子类**: cs.DC, cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《INC-SRv6: In-Network Route Exploration and Fast Failover Using Segment Routing Headers in Dynamic UAV Networks》归入 机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Distributed, Parallel, and Cluster Computing 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) networks require a network provisioning mechanism that guarantees delivery and latency quality of service (QoS) under dynamic conditions in next-generation airborne mesh networks by continuously learning and repairing multi-hop paths under rapid link turnover without flooding the control plane. This paper presents INC-SRv6, an in-network computing routing mechanism that repurposes the IPv6 Segment Routing Header (SRH) and its Segments Left (SL) pointer into a self-learning, fast-failover distributed control plane. Rather than treating the SRH as a static source-committed vector, INC-SRv6 uses the active SL pointer to partition the segment list in flight: slots ahead of SL provide capacity for hop-by-hop next-hop recording, while the suffix behind SL serves as an in-band multi-destination reachability vector. Through this dual-zone header discipline, transit routers extract distance-weighted reachability updates from arriving suffixes, gate admission by single-pass confidence with bounded binary probing, advance or reverse SL deterministically, and restore pre-transmission SRH state for local failover upon link loss. Simulations across 200-node 3D UAV networks show that under high-speed flight and repeated 20% relay outages, INC-SRv6 improves packet delivery over reactive routing (92.12% versus 89.12%) while cutting 95th-percentile tail delay from 121.26 to 8.84 ms and control packets by 35.8%, with a 4-byte compact uSID stride model reducing SRv6 control bytes by over 52%.

</details>

---
