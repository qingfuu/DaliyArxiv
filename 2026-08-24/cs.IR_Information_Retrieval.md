# cs.IR | Information Retrieval | 2026-08-24

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Towards_Faithful_Simulation_of_Human_Shopping_Behavior|Towards Faithful Simulation of Human Shopping Behavior]]

![[assets/2608.20707_figure.png|800]]

- **arXiv**: [2608.20707](https://arxiv.org/abs/2608.20707)
- **PDF**: https://arxiv.org/pdf/2608.20707
- **详细分析**: [[20_Research/Papers/大模型/Towards_Faithful_Simulation_of_Human_Shopping_Behavior|Towards Faithful Simulation of Human Shopping Behavior]]
- **作者**: Jiakai Tang, Yan Mi, Jing Yu, Yang Zhang, See-Kiong Ng, Qi Cao, Fei Sun, Xu Chen, Wen Chen, Jian Wu, Han Zhu, Bo Zheng
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Towards Faithful Simulation of Human Shopping Behavior》归入 大模型、强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulating realistic user shopping behavior underpins offline evaluation and reinforcement learning in e-commerce scenarios. While recent LLM- and VLM-based simulators have made encouraging progress, reproducing a real browsing session remains difficult for two reasons. (i) Memory Challenge: a shopping session spans dozens of pages, yet existing agents either discard long-range observation histories, losing the evolving user state, or naively concatenate them, overwhelming the context window and even degrading simulation quality. (ii) Optimization Challenge: current user simulators are typically supervised to match each logged action via imitation or step-level rewards; the resulting sessions often display unrealistic patterns, such as over-exploration or excessive passivity, which per-step supervision can neither detect nor correct. To address the above challenges, we present RecVerse, a GUI-grounded simulation agent that perceives pages through screenshots and produces faithful multi-turn trajectories. For the memory challenge, RecVerse adopts a cognitive-inspired hierarchical memory: Working Memory for short-term focus, Episodic Memory for in-session traces, and Preference Memory for high-level intent, with memory updates treated as actions so that the agent adaptively learns when and what to memorize. For the optimization challenge, RecVerse is optimized with a trajectory-level RL objective that scores entire sessions, aligning both macro-level action-type distributions and micro-level shopping intent with real users. We further release USB (User Simulation Benchmark), an interactive e-commerce GUI trajectory dataset for multi-turn user simulation. Experiments show that RecVerse significantly outperforms existing baselines in both behavioral fidelity and intent consistency.

</details>

---
