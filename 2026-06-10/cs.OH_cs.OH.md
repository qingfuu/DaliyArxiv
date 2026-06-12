# cs.OH | cs.OH | 2026-06-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/LLM-Mediated_Demand_Response_Coordination_in_Smart_Microgrids|LLM-Mediated Demand Response Coordination in Smart Microgrids]]

![[assets/2606.11050_figure.png|800]]

- **arXiv**: [2606.11050](https://arxiv.org/abs/2606.11050)
- **PDF**: https://arxiv.org/pdf/2606.11050
- **详细分析**: [[20_Research/Papers/大模型/LLM-Mediated_Demand_Response_Coordination_in_Smart_Microgrids|LLM-Mediated Demand Response Coordination in Smart Microgrids]]
- **作者**: J. de Curtò, I. de Zarzà
- **cs 子类**: 
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《LLM-Mediated Demand Response Coordination in Smart Microgrids》归入 大模型、强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective demand response in smart microgrids requires prosumers to cooperate voluntarily under strategic self-interest, a coordination problem structurally equivalent to a repeated Prisoner's Dilemma on a social network. This paper presents a multi-agent simulation in which a Large Language Model (LLM) Influence Compiler issues structured demand-response directives to a population of heterogeneous prosumer agents, each governed by a hybrid decision architecture combining game-theoretic base probability (derived from payoff history, neighbour imitation, and exploitation memory) with LLM narrative evaluation of incoming coordination signals. The hybrid architecture resolves a key methodological challenge: LLMs aligned via Reinforcement Learning from Human Feedback (RLHF) exhibit strong cooperation bias when used as direct decision-makers, producing flat dynamics regardless of grid conditions. By separating strategic reasoning from grounded narrative evaluation, the model generates realistic prosumer behaviour across six personality archetypes, with baseline cooperation near 50% and clear differentiation under influence. Compiled structured directives achieve 33.3% demand-curtailment cooperation versus 27.0% for unstructured messaging and 28.0% for a no-intervention baseline ($Δ_\mathrm{comp} = +0.063$), with the advantage preserved across both grounded and idealized agent substrates ($Δ= +0.083$) and across all resistance levels ($R = 0.1$ to $0.7$). Hub-targeted dissemination via high-centrality network nodes outperforms peripheral or random targeting, confirming that grid topology provides mechanistic amplification independent of message content. These results suggest that structured LLM compilation, grounded agent reasoning, and network-aware targeting are complementary design principles for scalable, interpretable demand-response coordination in smart-city energy systems.

</details>

---
