# cs.IT | Information Theory | 2026-10-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Mission-critical_spectrum_sharing_with_decentralized_Multi-Agent_Reinforcement_Learning|Mission-critical spectrum sharing with decentralized Multi-Agent Reinforcement Learning]]

![[assets/2610.09213_figure.png|800]]

- **arXiv**: [2610.09213](https://arxiv.org/abs/2610.09213)
- **PDF**: https://arxiv.org/pdf/2610.09213
- **详细分析**: [[20_Research/Papers/强化学习/Mission-critical_spectrum_sharing_with_decentralized_Multi-Agent_Reinforcement_Learning|Mission-critical spectrum sharing with decentralized Multi-Agent Reinforcement Learning]]
- **作者**: Dimitrios Pylorof, Imtiaz Nasim, Humberto E. Garcia, Vivek Agarwal, Jasni A. Mannil, Mingyue Ji
- **cs 子类**: cs.IT
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Mission-critical spectrum sharing with decentralized Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motivated by emerging mission-critical applications and an increasingly congested spectrum, we develop a decentralized multi-agent reinforcement learning (MARL) model for dynamic spectrum access. The model enables secondary users to learn effective transmission strategies across shared frequency bands while minimizing collisions with high-priority primary users and among themselves. We design the agent-level learners following a Markov potential game approach, connecting independent local updates to system-level improvement. We instantiate this design using lightweight linear actor-critic learners suitable for resource-constrained edge devices, rather than computationally intensive centralized or deep multi-agent architectures. Across spectrum environments with different incumbent activities, the learned policies adapt their transmission policy and waiting behavior to preserve throughput while greatly reducing transmission collisions relative to random and forecast-aware heuristic baselines. The results establish the value of decentralized MARL and shows up to 96.8% reduction in overall collisions.

</details>

---
