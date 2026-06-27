# cs.OH | cs.OH | 2026-06-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Reference-Free_Heterogeneous_Multi-Agent_Reinforcement_Learning_for_Grid-Friendly_Tie-Line_Power_Shaping_in_Industrial_Microgrids|Reference-Free Heterogeneous Multi-Agent Reinforcement Learning for Grid-Friendly Tie-Line Power Shaping in Industrial Microgrids]]

![[assets/2606.25599_figure.png|800]]

- **arXiv**: [2606.25599](https://arxiv.org/abs/2606.25599)
- **PDF**: https://arxiv.org/pdf/2606.25599
- **详细分析**: [[20_Research/Papers/强化学习/Reference-Free_Heterogeneous_Multi-Agent_Reinforcement_Learning_for_Grid-Friendly_Tie-Line_Power_Shaping_in_Industrial_Microgrids|Reference-Free Heterogeneous Multi-Agent Reinforcement Learning for Grid-Friendly Tie-Line Power Shaping in Industrial Microgrids]]
- **作者**: Daniyaer Paizulamua, Lin Cheng, Fashun Shi, Haoyu Zheng, Pengfei He, Haiwang Zhong
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.5，强化学习 0.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reference-Free Heterogeneous Multi-Agent Reinforcement Learning for Grid-Friendly Tie-Line Power Shaping in Industrial Microgrids》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HARL, MADRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tie-line power (TLP) shaping is a key requirement for the grid-friendly operation of industrial microgrids (IMGs). This paper studies the coordination of multi-timescale heterogeneous adjustable resources in a steel IMG to shape a grid-friendly TLP trajectory considering multiple objectives. A sequential heterogeneous-agent coordination (SHAC) framework is proposed, where process loads, hydrogen storage, and battery storage are modeled as functionally heterogeneous agents with cross-role observations, asynchronous decision intervals, role-specific rewards and critics. This design captures the heterogeneous temporal effects of different resources on the TLP trajectory and alleviates ambiguous credit assignment and weak inter-agent coordination. To ensure feasible real-time execution, process-knowledge-based action masking and feasibility projection are embedded into policy execution, and a role-aware multi-timescale actor--critic training scheme is developed for agents with different action structures and decision intervals. Numerical studies using real renewable generation and electricity market data show that SHAC effectively eliminates the dependence on predefined reference trajectories and enables adaptive 1-min online decision-making, achieving zero production failures with an average computational time of only 0.4 ms per step. Compared with the original operation, SHAC reduces the total grid purchase cost, contract-demand exceedance time, and cumulative ramp excess by 91.27\%, 98.64\%, and 96.91\%, respectively. These results demonstrate that the proposed framework improves the economic efficiency and grid friendliness of industrial microgrid operation while satisfying strict process-safety constraints and real-time computational requirements.

</details>

---
