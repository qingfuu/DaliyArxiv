# cs.NI | Networking and Internet Architecture | 2026-07-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/PHaul_A_PPO-based_forwarding_agent_for_Sub6_enhanced_Integrated_Access_and_Backhaul_networks|PHaul: A PPO-based forwarding agent for Sub6 enhanced Integrated Access and Backhaul networks]]

![[assets/2607.07584_figure.png|800]]

- **arXiv**: [2607.07584](https://arxiv.org/abs/2607.07584)
- **PDF**: https://arxiv.org/pdf/2607.07584
- **详细分析**: [[20_Research/Papers/强化学习/PHaul_A_PPO-based_forwarding_agent_for_Sub6_enhanced_Integrated_Access_and_Backhaul_networks|PHaul: A PPO-based forwarding agent for Sub6 enhanced Integrated Access and Backhaul networks]]
- **作者**: Jorge Pueyo, Daniel Camps-Mur and, Miguel Catalan-Cid
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.4，强化学习 0.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《PHaul: A PPO-based forwarding agent for Sub6 enhanced Integrated Access and Backhaul networks》归入 强化学习、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3GPP Integrated Access and Backhaul (IAB) allows operators to deploy outdoor mm-wave access networks in a cost-efficient manner, by reusing the same spectrum in access and backhaul. In IAB networks the performance bottleneck is the wireless backhaul segment, where efficient forwarding strategies are needed to effectively use the available capacity. In addition, the performance of the mm-wave IAB backhaul segment is contingent on the availability of line of sight (LoS) conditions in the selected deployment sites. To mitigate LoS dependence, in this paper, we propose to complement the mm-wave backhaul segment of IAB networks with additional Sub6 backhaul links, which contribute to the capacity and robustness of the backhaul network. We refer to IAB networks combining Sub6 and mm-wave links in the backhaul as Sub6 enhanced IAB networks. In this context, the main contribution of this paper is PHaul, a forwarding engine for Sub6 enhanced IAB networks that accomodates different traffic engineering criteria, and combines an offline path selection heuristic with an online Deep Reinforcement Learning (DRL) agent based on Proximal Policy Optimization (PPO). By leveraging a network digital twin of the IAB wireless backhaul, PHaul periodically samples the input traffic of the backhaul network and updates flow to path mappings, with execution times below 10 seconds in realistic backhaul topologies. We present an exhaustive performance evaluation, where we demonstrate that PHaul can achieve gains of up to 36\% in throughput efficiency and of up to 20\% in fairness, when compared against two alternative heuristics in a wide range of network configurations. We also demonstrate that PHaul is robust to differences between the network topologies considered in the training and inference phases, which can occur in practice due to link failures.

</details>

---
