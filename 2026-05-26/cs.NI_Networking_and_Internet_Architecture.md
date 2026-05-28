# cs.NI | Networking and Internet Architecture | 2026-05-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/K8S_Power_Irrigation_Deep_Reinforcement_Learning_for_Performance-Aware_Power_Efficiency_of_Kubernetes_Cloud-Native_Microservices|K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices]]

![[assets/2605.25218_figure.png|800]]

- **arXiv**: [2605.25218](https://arxiv.org/abs/2605.25218)
- **PDF**: https://arxiv.org/pdf/2605.25218
- **详细分析**: [[20_Research/Papers/强化学习/K8S_Power_Irrigation_Deep_Reinforcement_Learning_for_Performance-Aware_Power_Efficiency_of_Kubernetes_Cloud-Native_Microservices|K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices]]
- **作者**: Zouhir Bellal, Laaziz Lahlou, Nadjia Kara, Timothy Murphy, Tan Phat Nguyen
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices》归入 强化学习、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HRL, Non-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern cloud platforms are facing a sharp increase in power demand driven by the rapid adoption of AI-powered applications, making power optimization urgent under net-zero commitments and sustainability goals. Yet, reducing power in production remains challenging for latency-sensitive microservices, where performance violations directly affect user experience and operational risk. Such services exhibit heterogeneous workload characteristics and dynamic load patterns. In multi-tenant environments, contention on shared uncore resources, including last-level cache and memory bandwidth, can degrade performance, especially for memory-intensive workloads. As a safeguard, providers often run servers in performance mode, fixing core and uncore frequencies at high levels. Existing power governors largely ignore application-level performance requirements and uncore interference, leading to systematic power over-provisioning. To address this, we introduce K8SPI, a hierarchical reinforcement learning controller that jointly optimizes CPU core and uncore frequencies for cloud-native deployments. K8SPI uses a two-stage architecture: a coarse-grained agent rapidly mitigates performance violations, while a fine-grained agent minimizes power once requirements are satisfied. Using telemetry from hardware, Kubernetes, and application layers, K8SPI adapts to workload heterogeneity and cross-microservice interference. We evaluate K8SPI on a Kubernetes testbed across multiple scenarios. Results show that K8SPI reduces node-level power by 23--30\% compared with the Linux performance governor while keeping performance requirement violations below 2--3\%, even under severe uncore contention and dynamic load fluctuations.

</details>

---
