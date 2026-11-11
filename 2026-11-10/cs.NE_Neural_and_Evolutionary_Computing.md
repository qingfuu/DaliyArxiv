# cs.NE | Neural and Evolutionary Computing | 2026-11-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Maximizing_Detection_Probability_in_UAV_Search_Missions_using_Random-Key_Optimizers|Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers]]

![[assets/2611.12317_figure.png|800]]

- **arXiv**: [2611.12317](https://arxiv.org/abs/2611.12317)
- **PDF**: https://arxiv.org/pdf/2611.12317
- **详细分析**: [[20_Research/Papers/机器人/Maximizing_Detection_Probability_in_UAV_Search_Missions_using_Random-Key_Optimizers|Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers]]
- **作者**: Antonio Dantas, Elcio Shiguemori, Antonio Chaves
- **cs 子类**: cs.NE, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers》归入 机器人、具身智能 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper focuses on the stochastic and real-time constraints of Unmanned Aerial Vehicle (UAV) path planning in Search and Rescue (SAR) missions. We introduce a configurable data-driven and intelligent routing architecture that combines a closed-loop probability update with the Random-Key Optimizers (RKO). Our problem is mathematically modeled as a dynamic probabilistic variant of the Open Vehicle Routing Problem (OVRP), enabling the solver to switch adaptively between two objectives, thereby balancing probability maximization and resource minimization. The framework degrades elegantly under noisy priors but not under biased ones: a systematically biased map performs about half as well as flying with no prior at all. Computational tests show that the proposed scheme is scalable and competitive with single-path scenarios in terms of solution performance and serves as a strong decision guide for intelligent planning in SAR operations in unstable environments

</details>

---
