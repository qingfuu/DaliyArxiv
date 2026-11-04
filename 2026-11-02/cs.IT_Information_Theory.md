# cs.IT | Information Theory | 2026-11-02

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/具身智能/Embodied_Movable_Antennas|Embodied Movable Antennas]]

![[assets/2610.42078_first_page.png|800]]

- **arXiv**: [2610.42078](https://arxiv.org/abs/2610.42078)
- **PDF**: https://arxiv.org/pdf/2610.42078
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Movable_Antennas|Embodied Movable Antennas]]
- **作者**: Yewen Cao, Dengke Wei, Yulin Shao
- **cs 子类**: cs.IT
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.1，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Movable Antennas》归入 具身智能、机器人、大模型 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces embodied movable antennas (MAs), a new MA architecture that rethinks the source of antenna mobility. Unlike conventional MAs that rely on dedicated antenna actuators, embodied MAs harness the mechanical degrees of freedom already present in physical agents to reconfigure antenna position and orientation. We distinguish two modes of embodied MAs: task-coupled and task-preserving. Focusing on the latter, we show how wireless channels can be reconfigured by exploiting task-equivalent host configurations without altering the prescribed physical task. Using a redundant robotic manipulator as a canonical realization, we characterize the intrinsically coupled antenna translation and orientation induced by task-preserving self-motion and derive an exact Fourier representation of the resulting multipath channel. Our analysis reveals that the wireless value of embodied mobility depends not merely on how far an antenna can move, but on which configurations remain feasible under the physical task and how their coupled motion interacts with polarization and multipath propagation. Building on this insight, we develop a cross-task antenna mounting design that enables wireless adaptation with a fixed physical installation. Numerical results demonstrate substantial communication gains through task-preserving motion. These findings establish mechanical redundancy as a new, quantifiable resource for wireless channel reconfiguration.

</details>

---

### [[20_Research/Papers/强化学习/Statistical_Foundations_of_Reinforcement_Learning_A_Non-Asymptotic_Perspective|Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective]]

![[assets/2610.41903_first_page.png|800]]

- **arXiv**: [2610.41903](https://arxiv.org/abs/2610.41903)
- **PDF**: https://arxiv.org/pdf/2610.41903
- **详细分析**: [[20_Research/Papers/强化学习/Statistical_Foundations_of_Reinforcement_Learning_A_Non-Asymptotic_Perspective|Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective]]
- **作者**: Yuxin Chen, Yuejie Chi, Jianqing Fan, Gen Li, Yuting Wei, Yuling Yan
- **cs 子类**: cs.IT, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective》归入 强化学习、世界模型、大模型 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) embodies a foundational paradigm for sequential decision-making in the face of uncertainty. The rapid growth of model complexity in emerging applications has significantly amplified the challenges of achieving data-efficient RL, particularly in sample-starved scenarios where data collection may be costly, time-consuming, or even high-stakes. Consequently, understanding and improving the data efficiency of RL algorithms has become a central problem of both fundamental theoretical interest and practical importance. Despite decades of research, the statistical underpinnings of RL remained remarkably underdeveloped until relatively recently, particularly in the finite-sample regimes most relevant to modern practice. Over the past few years, there has been a surge of activity advancing the frontiers of non-asymptotic statistical RL theory, drawing on ideas from high-dimensional statistics and probability, information theory, and statistical learning theory. In this monograph, we present a non-asymptotic treatment for RL based on tabular Markov decision processes, focusing on three canonical sampling mechanisms --- RL with a generative model, online RL, and offline RL --- together with two algorithmic paradigms: model-based and model-free approaches. Centered around non-asymptotic sample complexity analysis, our treatment emphasizes minimax-optimal algorithm design, particularly methods that attain statistical optimality without significant burn-in costs, as well as sharp statistical characterizations of several widely used RL algorithms. Whenever possible, we provide largely self-contained analyses together with intuitive explanations. We also briefly discuss several extensions, such as robust RL, competitive multi-agent RL, federated RL, uncertainty quantification, and RL from human feedback.

</details>

---
