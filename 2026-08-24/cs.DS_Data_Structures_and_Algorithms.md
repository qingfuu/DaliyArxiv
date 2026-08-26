# cs.DS | Data Structures and Algorithms | 2026-08-24

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Stochastic_Multi-Robot_Monitoring_on_Graphs_under_Markovian_Mobility|Stochastic Multi-Robot Monitoring on Graphs under Markovian Mobility]]

![[assets/2608.20618_figure.png|800]]

- **arXiv**: [2608.20618](https://arxiv.org/abs/2608.20618)
- **PDF**: https://arxiv.org/pdf/2608.20618
- **详细分析**: [[20_Research/Papers/机器人/Stochastic_Multi-Robot_Monitoring_on_Graphs_under_Markovian_Mobility|Stochastic Multi-Robot Monitoring on Graphs under Markovian Mobility]]
- **作者**: Walid Ben-Ameur, Tijani Chahed, Shamisa Nematollahi
- **cs 子类**: cs.DS
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Robotics

#### 研究背景与动机

《Stochastic Multi-Robot Monitoring on Graphs under Markovian Mobility》归入 机器人 方向。该论文围绕 Data Structures and Algorithms 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study a stochastic multi-robot monitoring problem on a connected graph $G=(V,E)$, where each robot moves according to a Markov chain on $G$ and monitors the closed neighborhood of its current vertex. The performance of $r$ robots is evaluated in steady state via two objectives: average-case coverage (the expected number of covered vertices) and worst-case coverage (the minimum coverage probability over all vertices). We consider three models: independent homogeneous strategies, where all robots share the same stationary distribution; independent heterogeneous strategies, where robots use different stationary distributions; and centralized strategies, allowing arbitrary correlations between robot locations. For the heterogeneous model, we prove that maximizing average coverage is NP-hard even for two robots, and that replicating an easy-to-compute optimal homogeneous strategy yields a \(\left(1-\left(1-\frac{1}{r}\right)^r\right)\)-approximation for both objective functions in the heterogeneous setting; moreover, no polynomial-time algorithm can achieve a ratio better than \(1-\nicefrac{1}{e}\) unless \(\text{P}=\text{NP}\). Centralized strategies can exploit correlations to reduce redundancy. We develop a hierarchy of approximation factors: for any positive integer \(r'\le r\), writing \(r=hr'+b\) with \(0\le b&lt;r'\), block coordination yields a \(1-\left(1-\frac{r'}{r}\right)^h\left(1-\frac{b}{r}\right)\) approximation for both objectives. We also establish NP-hardness and a tight \(1-\nicefrac{1}{e}\) inapproximability bound. Moreover, we prove diminishing-returns properties with respect to the number of robots: a non-increasing-ratio property holds for the average-case objective in all settings, but not for the heterogeneous worst-case objective.

</details>

---
