# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-09-23

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/WeightBridge_An_Efficient_Weight_Transfer_Library_for_Reinforcement_Learning|WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning]]

![[assets/2609.25442_first_page.png|800]]

- **arXiv**: [2609.25442](https://arxiv.org/abs/2609.25442)
- **PDF**: https://arxiv.org/pdf/2609.25442
- **详细分析**: [[20_Research/Papers/强化学习/WeightBridge_An_Efficient_Weight_Transfer_Library_for_Reinforcement_Learning|WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning]]
- **作者**: Xuanlin Jiang, Samuel Hsia, Michael Kuchnik, Zachary DeVito, Minlan Yu, Carole-Jean Wu
- **cs 子类**: cs.DC, cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Weight transfer - the propagation of updated parameters from trainers to rollout generators - is becoming an important performance bottleneck in reinforcement learning (RL) systems for LLMs. The central challenge is supporting the diverse trainer and rollout layouts and synchronization requirements of modern RL workloads without sacrificing efficiency. Existing solutions are efficient under some configurations but perform poorly or lack support under others. We present WeightBridge, a flexible, efficient weight-transfer library designed to deliver high performance across diverse RL configurations. WeightBridge first automatically extracts the correspondence between trainer and rollout weight layouts, then plans and executes redundancy-free and load-balanced weight transfer. It exposes a small, general API while coordinating workers across diverse synchronization modes. Across configurations spanning different models, parallelization layouts, and synchronization modes, WeightBridge reduces average GPU stall time by up to 42$\times$ over the state-of-the-art open-source RL framework and achieves high performance in all settings. A coding agent was able to integrate WeightBridge into two different RL frameworks without manual guidance, demonstrating the generality and ease of use of its APIs.

</details>

---

### [[20_Research/Papers/大模型/Cloud,_Edge,_or_Split_Profiling_Onboard_and_Split_Vision-Language_Model_Deployment_for_Drone_AI|Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI]]

![[assets/2609.25415_figure.png|800]]

- **arXiv**: [2609.25415](https://arxiv.org/abs/2609.25415)
- **PDF**: https://arxiv.org/pdf/2609.25415
- **详细分析**: [[20_Research/Papers/大模型/Cloud,_Edge,_or_Split_Profiling_Onboard_and_Split_Vision-Language_Model_Deployment_for_Drone_AI|Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI]]
- **作者**: Zoha Azimi, Reza Farahani, Schahram Dustdar, Christian Timmerer
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.3（加权：大模型 0.7，机器人 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI》归入 大模型、机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Models (VLMs) enable edge devices like unmanned aerial vehicles (UAVs) to interpret visual observations and reason about complex environments using natural-language instructions. However, their practical deployment remains challenging as onboard inference is constrained by limited computational, memory, and energy resources, whereas cloud-based inference introduces communication latency, bandwidth overhead, and dependence on network connectivity. To address these limitations, split computing offers a promising alternative by partitioning VLM inference between the resource-constrained UAVs and more capable remote servers. However, the performance trade-offs among fully onboard, cloud-based, and split-computing architectures for lightweight VLMs have not yet been systematically profiled. This paper benchmarks these three deployment paradigms using SmolVLM-256M as a representative lightweight VLM. We quantify their inference latency, computational resource utilization, communication overhead, and energy consumption across varying image resolutions and network conditions. Our results show that no deployment strategy is universally optimal; instead, the preferred strategy depends on the interaction between network conditions and input image resolution.

</details>

---
