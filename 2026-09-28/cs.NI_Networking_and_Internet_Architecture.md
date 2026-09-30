# cs.NI | Networking and Internet Architecture | 2026-09-28

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/强化学习/Solution_for_Interference_in_Hotspot_Scenarios_Applying_Q-Learning_on_FFR-Based_ICIC_Techniques|Solution for Interference in Hotspot Scenarios Applying Q-Learning on FFR-Based ICIC Techniques]]

![[assets/2609.31405_figure.png|800]]

- **arXiv**: [2609.31405](https://arxiv.org/abs/2609.31405)
- **PDF**: https://arxiv.org/pdf/2609.31405
- **详细分析**: [[20_Research/Papers/强化学习/Solution_for_Interference_in_Hotspot_Scenarios_Applying_Q-Learning_on_FFR-Based_ICIC_Techniques|Solution for Interference in Hotspot Scenarios Applying Q-Learning on FFR-Based ICIC Techniques]]
- **作者**: Iago Diógenes do Rego, Vicente A. de Sousa
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Solution for Interference in Hotspot Scenarios Applying Q-Learning on FFR-Based ICIC Techniques》归入 强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HetNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work explores interference coordination techniques (inter-cell interference coordination, ICIC) based on fractional frequency reuse (FFR) as a solution for a multi-cellular scenario with user concentration varying over time. Initially, we present the problem of high user concentration along with their consequences. Next, the use of multiple-input multiple-output (MIMO) and small cells are discussed as classic solutions to the problem, leading to the introduction of fractional frequency reuse and existing ICIC techniques that use FFR. An exploratory analysis is presented in order to demonstrate the effectiveness of ICIC techniques in reducing co-channel interference, as well as to compare different techniques. A statistical study was conducted using one of the techniques from the first analysis in order to identify which of its parameters are relevant to the system performance. Additionally, another study is presented to highlight the impact of high user concentration in the proposed scenario. Because of the dynamic aspect of the system, this work proposes a solution based on machine learning. It consists of changing the ICIC parameters automatically to maintain the best possible signal-to-interference-plus-noise ratio (SINR) in a scenario with hotspots appearing over time. All investigations are based on ns-3 simulator prototyping. The results show that the proposed Q-Learning algorithm increases the average SINR from all users and hotspot users when compared with a scenario without Q-Learning. The SINR from hotspot users is increased by 11.2% in the worst case scenario and by 180% in the best case

</details>

---

### [[20_Research/Papers/强化学习/Dynamic_Sampling_for_Telemetry_in_Microservices_A_Reinforcement_Learning_and_Entropy-Based_Approach|Dynamic Sampling for Telemetry in Microservices: A Reinforcement Learning and Entropy-Based Approach]]

![[assets/2609.31292_figure.png|800]]

- **arXiv**: [2609.31292](https://arxiv.org/abs/2609.31292)
- **PDF**: https://arxiv.org/pdf/2609.31292
- **详细分析**: [[20_Research/Papers/强化学习/Dynamic_Sampling_for_Telemetry_in_Microservices_A_Reinforcement_Learning_and_Entropy-Based_Approach|Dynamic Sampling for Telemetry in Microservices: A Reinforcement Learning and Entropy-Based Approach]]
- **作者**: Renan Martins Alves, Jéferson Campos Nobre, Juliano Araujo Wickboldt
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Dynamic Sampling for Telemetry in Microservices: A Reinforcement Learning and Entropy-Based Approach》归入 强化学习、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Microservices architectures are increasingly deployed in cloud-based distributed environments, making application development and maintenance more dynamic, but also increasing the complexity of troubleshooting and observability. Distributed tracing tools are therefore essential for request analysis and debugging, despite introducing additional overhead that can be amplified by excessive and inefficient data collection. This article proposes RADAR (Reinforcement Learning Agent for Dynamic And Relevant trace sampling), an agent that combines reinforcement learning with a data entropy assessment to achieve more efficient capture of traces relevant to system monitoring, based on the OpenTelemetry standard. RADAR tests different sampling rules to discover which combination is most efficient. A test environment simulating a minimalist online store with several microservices distributed across a Kubernetes cluster served as the basis for the experiments, which evaluated the agent's convergence and the system's performance in terms of resource consumption and collected data quality. Results showed that RADAR reduced network bandwidth consumption by 97.4% and CPU usage by 99.0% compared to full data collection, also outperforming a fixed-rate sampling baseline. Beyond these resource savings, the approach preserved observability of critical scenarios, retaining approximately 85.6% of rare trace patterns and increasing the average entropy of the stored information by approximately 25%, validating the feasibility of using entropy to orchestrate telemetry autonomously and efficiently.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Misbehavior_Detection_Under_Partially_Observable_V2X_Data|Deep Reinforcement Learning for Misbehavior Detection Under Partially Observable V2X Data]]

![[assets/2609.31217_first_page.png|800]]

- **arXiv**: [2609.31217](https://arxiv.org/abs/2609.31217)
- **PDF**: https://arxiv.org/pdf/2609.31217
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Misbehavior_Detection_Under_Partially_Observable_V2X_Data|Deep Reinforcement Learning for Misbehavior Detection Under Partially Observable V2X Data]]
- **作者**: Roshan Sedar, Charalampos Kalalas
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《Deep Reinforcement Learning for Misbehavior Detection Under Partially Observable V2X Data》归入 强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Misbehavior detection in vehicle-to-everything (V2X) systems is essential for ensuring the semantic correctness of exchanged messages and preventing the dissemination of falsified information. Existing data-centric misbehavior detection approaches largely rely on statistical validation or supervised machine learning models under the implicit assumption of fully observable V2X streams. In practice, however, vehicular environments are inherently partially observable due to hardware failures, intermittent connectivity, and environmental occlusions. Moreover, missingness itself can be strategically exploited by adversaries to evade detection. In this paper, we study misbehavior detection under incomplete V2X observations and propose a deep reinforcement learning (DRL)-based detection framework that learns adaptive policies with incomplete data. We further introduce an adversarial threat model in which attackers exploit or deliberately induce missingness to evade detection, including evasion via natural occlusions and adversarial feature suppression. Extensive experiments conducted on the VeReMi dataset under various missingness patterns demonstrate that DRL significantly outperforms a powerful XGBoost baseline under natural partial observability. However, results also reveal a critical vulnerability: DRL policies can be highly susceptible to evasion attacks that strategically exploit natural missingness. In contrast, DRL exhibits more gradual degradation under direct feature suppression compared to static tree-based models.

</details>

---
