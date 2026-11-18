# cs.NI | Networking and Internet Architecture | 2026-11-16

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Resource_Management_and_Trajectory_Optimization_for_UAV-IRS_Assisted_Maritime_Edge_Computing_Networks|Resource Management and Trajectory Optimization for UAV-IRS Assisted Maritime Edge Computing Networks]]

![[assets/2611.17803_figure.png|800]]

- **arXiv**: [2611.17803](https://arxiv.org/abs/2611.17803)
- **PDF**: https://arxiv.org/pdf/2611.17803
- **详细分析**: [[20_Research/Papers/强化学习/Resource_Management_and_Trajectory_Optimization_for_UAV-IRS_Assisted_Maritime_Edge_Computing_Networks|Resource Management and Trajectory Optimization for UAV-IRS Assisted Maritime Edge Computing Networks]]
- **作者**: Chaoyue Zhang, Bin Lin, Xu Hu, Shuang Qi, Liping Qian, Yuan Wu
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.2，机器人 0.6）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Resource Management and Trajectory Optimization for UAV-IRS Assisted Maritime Edge Computing Networks》归入 机器人、强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the exponential growth of maritime wireless devices and the rapid development of maritime applications, traditional maritime communication networks encounter communication and computation limitations in supporting computation-intensive and latency-critical tasks. Edge computing and Intelligent Reflecting Surface (IRS) have emerged as promising techniques to improve communication and computation services for maritime devices with limited computation capabilities and battery capacity. This paper studies an IRS Mounted on Unmanned Aerial Vehicle (UIRS) assisted maritime edge computing network, in which the UIRS is deployed to assist the transmission from Unmanned Surface Vehicles (USVs) to the edge server via Non-Orthogonal Multiple Access (NOMA) protocol. We propose a resource management and trajectory optimization scheme by jointly optimizing subslot duration, offloading ratios, transmit power, edge computation capability allocation, UIRS phase shifts and UIRS trajectory, aiming at minimizing the overall energy consumption. Since the non-convex nature of the optimization problem, we propose a two-layered method by decomposing the original problem into two subproblems. The top-layered subproblem is solved by the Semi-Definite Relaxation (SDR) method and the underlying-layered subproblem is solved by the Deep Deterministic Policy Gradient (DDPG) algorithm. Numerical results demonstrate that our proposed scheme can effectively and efficiently reduce overall energy consumption.

</details>

---

### [[20_Research/Papers/强化学习/Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks|Mobile Edge Deployment and Resource Management for Maritime Wireless Networks]]

![[assets/2611.17779_figure.png|800]]

- **arXiv**: [2611.17779](https://arxiv.org/abs/2611.17779)
- **PDF**: https://arxiv.org/pdf/2611.17779
- **详细分析**: [[20_Research/Papers/强化学习/Mobile_Edge_Deployment_and_Resource_Management_for_Maritime_Wireless_Networks|Mobile Edge Deployment and Resource Management for Maritime Wireless Networks]]
- **作者**: Chaoyue Zhang, Bin Lin, Ziru Chen, Lin X. Cai, Jianli Duan
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: RL

#### 研究背景与动机

《Mobile Edge Deployment and Resource Management for Maritime Wireless Networks》归入 强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DLRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile Edge Computing (MEC) has been envisioned as one of the key technologies for supplying computation and storage resources in Internet of Vessels (IoV) networks. Due to its flexible deployment, low cost and agile maneuverability, Unmanned Surface Vehicle (USV) has emerged as a promising solution, to provide communication and computation services for maritime users. In this paper, we study mobile edge deployment and resource management for MEC-assisted maritime wireless networks where USVs with diverse computation resources are deployed to provide edge computing services that complement the cloud-based services. To this end, we formulate an optimization problem to minimize the expected response time by jointly optimizing the deployment of mobile USVs and computation offloading decisions. To solve the mixed-integer nonlinear program problem, we propose a Dual-Layer Reinforcement Learning (DLRL) framework to attain a near-optimal solution. Specifically, a Deep Deterministic Policy Gradient (DDPG) algorithm is designed to obtain the best USV deployment in the outer layer learning, and a Q-learning algorithm is designed to determine the best computation offloading decisions in the inner layer learning. Numerical results demonstrate that the proposed solution outperforms some literature algorithms by effectively handling both continuous and discrete variables.

</details>

---
