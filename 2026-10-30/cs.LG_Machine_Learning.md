# cs.LG | Machine Learning | 2026-10-30

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/强化学习/world2vec_Mechanistic_world_models_through_latent_dynamics_learning|world2vec: Mechanistic world models through latent dynamics learning]]

![[assets/2610.40637_figure.png|800]]

- **arXiv**: [2610.40637](https://arxiv.org/abs/2610.40637)
- **PDF**: https://arxiv.org/pdf/2610.40637
- **详细分析**: [[20_Research/Papers/强化学习/world2vec_Mechanistic_world_models_through_latent_dynamics_learning|world2vec: Mechanistic world models through latent dynamics learning]]
- **作者**: Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger, Steffen Schneider
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.92（加权：强化学习 0.16，世界模型 1.76）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《world2vec: Mechanistic world models through latent dynamics learning》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly from observations and actions. World2vec learns latent dynamics that faithfully reproduce the true system over long prediction horizons, with at least one order of magnitude fewer parameters than DreamerV3, TD-MPC2 and LeWM. This enables state of the art performance in controlling continuous environments from pixels and accurate system identification across a benchmark of 71 attractors, demonstrating how world models are amenable to scientific discovery.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_learning_for_control_of_partial_differential_equations|Reinforcement learning for control of partial differential equations]]

![[assets/2610.40449_figure.png|800]]

- **arXiv**: [2610.40449](https://arxiv.org/abs/2610.40449)
- **PDF**: https://arxiv.org/pdf/2610.40449
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_learning_for_control_of_partial_differential_equations|Reinforcement learning for control of partial differential equations]]
- **作者**: Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Reinforcement learning for control of partial differential equations》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controlling dynamical systems governed by partial differential equations (PDEs) remains a challenging task in scientific computing, owing to high-dimensional state spaces, distributed actuation, nonlinear dynamics, and stringent real-time constraints. Reinforcement learning (RL) has emerged as a promising paradigm for synthesizing feedback controllers that adapt to varying operating conditions and can be deployed efficiently in real-time. This review provides a unified perspective on RL and PDE-constrained optimization, and surveys model-free, model-based, and multi-agent RL approaches to PDE control, with particular emphasis on sample efficiency, generalization across parametric variations, and scalability to high-dimensional problems. Two demonstrative examples, the stabilization of a chaotic system and a flow control problem, illustrate the performance and pitfalls of RL agents in practice. Finally, we discuss evaluation and benchmarking practices, current limitations, and open research directions toward reliable, data-efficient, and scalable RL for scientific computing.

</details>

---

### [[20_Research/Papers/具身智能/LLM-guided_Planar_Loco-Manipulation_for_Quadruped_Robots|LLM-guided Planar Loco-Manipulation for Quadruped Robots]]

![[assets/2610.40248_figure.png|800]]

- **arXiv**: [2610.40248](https://arxiv.org/abs/2610.40248)
- **PDF**: https://arxiv.org/pdf/2610.40248
- **详细分析**: [[20_Research/Papers/具身智能/LLM-guided_Planar_Loco-Manipulation_for_Quadruped_Robots|LLM-guided Planar Loco-Manipulation for Quadruped Robots]]
- **作者**: Georges Jetti, Michael Khayyat, Jean-Pierre Sleiman, Stefano Arrigoni, Francesco Braghin
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.2，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《LLM-guided Planar Loco-Manipulation for Quadruped Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic navigation typically assumes a collision-free route to the goal exists; in cluttered environments with movable obstacles, however, reaching the goal may require physical interaction. Classical solutions encode these behaviors through geometric rules and task-specific logic, while learning-based approaches often constrain the decision space to low-dimensional motion commands or predefined action sets. We instead consider a broader decision space, jointly selecting the skill, relevant object, and geometric target. Our language-conditioned task planner, fine-tuned with LoRA on synthetic data, maps natural-language tasks and a structured scene representation to variable-length sequences of parameterized actions, executed by low-level reinforcement-learning policies. The planner learns the geometric relations underlying interactive navigation and outperforms a classical planner and a prompted frontier model on interactive navigation tasks. Comparisons with models trained from scratch indicate that composition does not require pretraining when the representation is structured, whereas pretraining yields more reliable geometric targets. At the low level, we introduce an end-to-end whole-body planar pushing policy that achieves a 93.3% success rate in simulation, versus 83.5% for a hierarchical baseline, while reducing completion time by more than 60%. On hardware, the hierarchy yields the correct skill composition in 44/45 trials and end-to-end success in 34/45. Project website: https://anonymousprojects-dev.github.io/LLM-guided-LocoManipulation-Quadrupeds/

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_Under_Runtime_Confounding_Policy_Learning_and_Off-Policy_Evaluation|Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation]]

![[assets/2610.40056_first_page.png|800]]

- **arXiv**: [2610.40056](https://arxiv.org/abs/2610.40056)
- **PDF**: https://arxiv.org/pdf/2610.40056
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_Under_Runtime_Confounding_Policy_Learning_and_Off-Policy_Evaluation|Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation]]
- **作者**: Raphael Kim, Michele Santacatterina, Ramin Zabih, Keith Barnatchez
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is increasingly used to train robust, adaptable systems across healthcare, e-commerce, and robotics. In these settings, legal, ethical, or logistical concerns may preclude certain key variables that drive decisions from being collected during deployment time. This gives rise to a setting known as runtime confounding: the logged data hold full observability, but deployment time lacks knowledge of certain variables, known as runtime confounders. Unlike single timepoint and non-adaptive settings, runtime confounding under reinforcement learning has the potential to propagate over time, as earlier decisions affect future states, observations, and action assignments, leading to biased learning. We address these problems with three contributions: we (1) develop policy learning algorithms under runtime-confounding, (2) develop semi-parametric efficient off-policy estimation procedures, and (3) provide diagnostics for understanding the price of runtime confounding.

</details>

---

### [[20_Research/Papers/强化学习/H$^2$R_Hierarchical_Hint-Based_Reward_for_Mathematical_Reasoning_via_Reinforcement_Learning|H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning]]

![[assets/2610.39934_figure.png|800]]

- **arXiv**: [2610.39934](https://arxiv.org/abs/2610.39934)
- **PDF**: https://arxiv.org/pdf/2610.39934
- **详细分析**: [[20_Research/Papers/强化学习/H$^2$R_Hierarchical_Hint-Based_Reward_for_Mathematical_Reasoning_via_Reinforcement_Learning|H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning]]
- **作者**: He Tu, Siye Li, Hongyi Wen
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BIG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards has shown great promise in enhancing mathematical reasoning in large language models. However, existing approaches provide limited intermediate supervision for complex, multi-step reasoning tasks. To bridge this gap, we propose \textbf{Hierarchical Hint-based Reward}, a framework that leverages the intrinsic sub-question structure of mathematical problems as structured intermediate conditioning signals during RLVR training. Unlike chain-of-thought prompting, these hierarchical hints serve as logically grounded intermediate milestones that effectively reduce the reasoning horizon toward the final answer. To validate this framework, we introduce \textbf{HiMath}, a benchmark of hierarchically structured mathematical problems. Across diverse LLMs, hierarchical hints consistently improve reasoning performance even without task-specific training. When integrated into RL training via H$^2$R, they boost Qwen2.5-Math-7B accuracy on HiMath from 30.4\% to 39.1\% using hierarchical hints, and up to 45.6\% with Oracle Hierarchical Hints. This pronounced improvement demonstrates that incorporating reliable intermediate checkpoints into reward design is essential for sustaining complex mathematical reasoning.

</details>

---

### [[20_Research/Papers/强化学习/Event2Reward_Learning_Robotic_Rewards_from_Progress_Relations|Event2Reward: Learning Robotic Rewards from Progress Relations]]

![[assets/2610.39212_first_page.png|800]]

- **arXiv**: [2610.39212](https://arxiv.org/abs/2610.39212)
- **PDF**: https://arxiv.org/pdf/2610.39212
- **详细分析**: [[20_Research/Papers/强化学习/Event2Reward_Learning_Robotic_Rewards_from_Progress_Relations|Event2Reward: Learning Robotic Rewards from Progress Relations]]
- **作者**: Junnan Nie, Zitian Fan, Jiachen Zhang, Junyi Lao, Likui Zhang, Chenghao Liu, Xiaoyang Lu, Yunbo Wang, Yixue Zhang, Linbo Zhai, Jiayi Li, Mengzhe Wang...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Event2Reward: Learning Robotic Rewards from Progress Relations》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, Real-World, SERL, Suboptimal-Value-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning task progress from robot demonstrations provides a practical way to construct dense shaping rewards for robotic reinforcement learning. A common approach uses normalized demonstration time as progress labels, implicitly assuming monotonically increasing task progress. During policy exploration, however, actual task progress can stall or even regress. Such models may mistake regressions for progress, assigning positive shaping rewards to actions that cause progress loss. Real suboptimal and failed executions offer corrective experience, but assigning absolute progress values to their states is difficult. Our key observation is that stalls, regressions, and recoveries establish local relative progress relations even when absolute progress is unknown. We introduce Event2Reward, which uses normalized temporal labels to anchor the progress scale and these within-trajectory relations to constrain local changes, combining absolute and relative progress supervision. Its progress predictions serve as potentials for reward shaping. We curate an event-annotated dataset from approximately 100K raw real-robot execution records, covering successful, suboptimal, and failed executions, without requiring framewise absolute progress labels. Under the same training budgets, Event2Reward improves average policy success by 18.16 percentage points over a baseline using only sparse task rewards across 40 tasks in four LIBERO suites. On real robots, average success after 30 minutes of wall-clock training reaches 60.0% on three precise insertion tasks and 90.0% on three object manipulation tasks, exceeding the sparse-reward baseline under the same budget by 36.7 and 23.3 percentage points, respectively. Ablation studies further show that absolute progress supervision and relative progress relations are complementary, with joint supervision yielding better downstream policy learning.

</details>

---

### [[20_Research/Papers/具身智能/Geometric_Time_Score_Estimators_Bridging_Self-Predictive_Representations_and_Generative_Occupancy_Models_For_Reinforcement_Learning|Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning]]

![[assets/2610.38901_figure.png|800]]

- **arXiv**: [2610.38901](https://arxiv.org/abs/2610.38901)
- **PDF**: https://arxiv.org/pdf/2610.38901
- **详细分析**: [[20_Research/Papers/具身智能/Geometric_Time_Score_Estimators_Bridging_Self-Predictive_Representations_and_Generative_Occupancy_Models_For_Reinforcement_Learning|Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning]]
- **作者**: Aravind Venugopal, Grace Liu, Jeff Schneider, Benjamin Eysenbach
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In reinforcement learning (RL), temporal reasoning is essential for estimating the density of future outcomes under a policy's occupancy measure. While self-predictive representations have been a dominant paradigm for occupancy density estimation, we find that they yield surprisingly poor estimates. On the other hand, generative occupancy models can produce remarkably accurate samples from the occupancy measure. Yet, they cannot easily recover occupancy densities, limiting their use for control despite their expressivity. In this paper, we propose Geometric Time Score Estimators (GTSE), a framework that bridges the two paradigms by learning occupancy density estimators along probability paths. We analyze how GTSE implicitly induces better occupancy estimators through improved representation learning and show how to directly extract self-predictive representations from this framework. Through experiments across several locomotion and manipulation tasks, we show that GTSE improves performance over state-of-the-art methods by $2\times$ to $6\times$ in goal-conditioned RL settings, and that the representations learned using our framework transfer effectively to downstream RL tasks. Website: https://aravindvenu7.github.io/website/gtse/

</details>

---

### [[20_Research/Papers/具身智能/CSO_Refining_Robotic_Policies_via_Skill_Distribution_Alignment_and_Skill-Grained_Optimization|CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization]]

![[assets/2610.38357_figure.png|800]]

- **arXiv**: [2610.38357](https://arxiv.org/abs/2610.38357)
- **PDF**: https://arxiv.org/pdf/2610.38357
- **详细分析**: [[20_Research/Papers/具身智能/CSO_Refining_Robotic_Policies_via_Skill_Distribution_Alignment_and_Skill-Grained_Optimization|CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization]]
- **作者**: Zhiyuan Xiang, Xiang Deng, Wanjie Tao, Xu Chen, Zhao Jielun, Weili Guan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.42（加权：具身智能 0.6，强化学习 0.56，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization》归入 机器人、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MetaWorld, OpenVLA, RIPT-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discretizing continuous actions into discrete skills using methods like VQ-VAE has emerged as a powerful paradigm for robotic manipulation. However, quantization errors yield a suboptimal distribution for the skill prior, degrading its performance. While reinforcement learning offers a path for refinement, its direct application faces unstable encoder updates and a granularity dilemma in importance sampling. To address these challenges, we introduce Cascaded Skills Optimization (CSO), a two-stage post-training framework. First, Rejection-Sampling Supervised Fine-tuning aligns the model's observation-to-skill mapping with the distribution of successful online trajectories via supervised fine-tuning. Second, with the observation encoder frozen, Skills Policy Optimization computes an independent, clipped importance ratio for each complete skill, enabling stable and efficient updates. With a lightweight QueST-style policy, CSO raises overall LIBERO success from 80.1% to 97.5%, improves performance on RoboTwin2.0, and achieves 61.0% success across five physical single-arm tasks. Additional comparisons with FAST, discrete BEAST, and fixed-buffer IQL further validate the effectiveness of our two-stage post-training strategy.

</details>

---

### [[20_Research/Papers/强化学习/Transportable_Offline_Reinforcement_Learning_in_Presence_of_Unmeasured_Confounding|Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding]]

![[assets/2610.38253_first_page.png|800]]

- **arXiv**: [2610.38253](https://arxiv.org/abs/2610.38253)
- **PDF**: https://arxiv.org/pdf/2610.38253
- **详细分析**: [[20_Research/Papers/强化学习/Transportable_Offline_Reinforcement_Learning_in_Presence_of_Unmeasured_Confounding|Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding]]
- **作者**: Junyi Liao, Hangqi Ren, Zhuoran Yang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning seeks to learn decision policies from previously collected data, but deployment environments may differ from the domains in which the data were collected, and logged variables may omit confounders that affected both historical actions and outcomes. We study offline policy learning under the joint challenges of domain discrepancy and unmeasured confounding, where multiple heterogeneous source datasets provide complementary information about a target domain. We develop a causally adjusted transportability framework combining transportability theory with instrumental variables, negative controls, and proxies to identify target-domain causal quantities. For confounded contextual bandits, identification reduces to systems of bridge-function integral equations, enabling minimax estimation from finite samples. Confidence sets for the identified quantities are then used for pessimistic policy optimization, yielding CAT-CCB. We extend the framework to episodic confounded Markov decision processes, where complementary sources identify target reward and transition mechanisms under structural and completeness conditions. Under Gaussian dynamics and linear function approximation, this yields CAT-CMDP. We establish high-probability finite-sample suboptimality guarantees that quantify the effects of approximation, estimation, source-to-target shift, offline coverage, and sample size. For bounded finite-dimensional linear classes, the contextual-bandit guarantee recovers the standard $\widetilde{\mathcal O}(N^{-1/2})$ rate. Numerical experiments support the effectiveness of the framework for learning target-domain policies from heterogeneous confounded data. Together, the results provide a principled approach when no single source dataset suffices for causal identification and policy optimization.

</details>

---

### [[20_Research/Papers/强化学习/Variational_Consequence-Driven_Offline_Reinforcement_Learning|Variational Consequence-Driven Offline Reinforcement Learning]]

![[assets/2610.38238_figure.png|800]]

- **arXiv**: [2610.38238](https://arxiv.org/abs/2610.38238)
- **PDF**: https://arxiv.org/pdf/2610.38238
- **详细分析**: [[20_Research/Papers/强化学习/Variational_Consequence-Driven_Offline_Reinforcement_Learning|Variational Consequence-Driven Offline Reinforcement Learning]]
- **作者**: Wen Jiang, Ke Jiang, Xiaoyang Tan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.16，世界模型 0.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Variational Consequence-Driven Offline Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning (RL) typically mitigates distribution shift by imposing divergence constraints on the action distributions of the learned and behavior policies. However, this paradigm cannot ensure the underlying dynamic consistency structure: even minor action deviations can lead to drastically different transitions, inadvertently driving the agent away from the offline dataset. To address this, we explore policy constraints through their induced state-consequence distributions rather than relying on pure action-distribution matching. Nevertheless, directly enforcing such consequence-aware constraints is computationally intractable without access to the true underlying dynamics model. To bypass this issue, we propose Structural Behavior Regularization (StBR), which replaces the intractable objective with a closed-form latent divergence. Structuring this latent space to reflect transition dynamics renders the latent divergence a theoretically bounded surrogate for the true consequence-distribution divergence. By regularizing the learned policy with this latent divergence, StBR adaptively tightens the behavior constraint in dynamics-sensitive regions, effectively preventing deviations outside the offline dataset. Empirically, we demonstrate that StBR achieves superior performance across diverse offline RL benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_at_Sea_Imitation_Learning_for_Multi-Task_Underwater_Manipulation|Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation]]

![[assets/2610.38199_figure.png|800]]

- **arXiv**: [2610.38199](https://arxiv.org/abs/2610.38199)
- **PDF**: https://arxiv.org/pdf/2610.38199
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_at_Sea_Imitation_Learning_for_Multi-Task_Underwater_Manipulation|Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation]]
- **作者**: Greta Perez-Haiek, Luca Macesanu, Kevin Angers, Mohammed Imam, Timothy Gambin, Christopher Clark
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirVLA, DynamicVLA, OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavior Cloning has demonstrated promising generalization capabilities for robotic manipulation in terrestrial environments. However, marine visual distortions and dynamic currents create a severe domain shift that remains a key bottleneck in adapting generalist architectures to underwater field manipulation. To address this, 1616 episodes of underwater manipulation data were collected in calm and turbulent waters and were used to train 14 generalist Vision-Language-Action (VLA) models (DynamicVLA) with varying proprioception observation configurations. Across three tasks on 1260 gradable on-hardware rollouts in a pool, 10 models outperformed the baseline, with the highest-performing model achieving a 93.3% overall success rate, including partial successes. Results are also introduced from a case study evaluating the performance of a single-task Action Chunking Transformer (ACT) and a generalist VLA (SmolVLA) policy for two tasks in marine archaeology and conservation: grasping and mooring. Experiments are performed on an ROV on and around the WWII wreck Coralita X127 and at Manoel Island Marina, Malta. Across 748 collected episodes and 508 gradable on-hardware rollouts, the ACT policy substantially outperformed SmolVLA (47.9% vs. 7.9% pooled success rate), earning a 66.7% success rate on the most successful task at the marine archaeological site. To enable further contributions to embodied intelligence in marine field robotics, the BLUEMBODIED KIT used to collect data, train models, and deploy policies on the ROV has been open sourced.

</details>

---

### [[20_Research/Papers/强化学习/Same_Label,_Different_Interface_Beyond_Action-Space_Labels_in_Robot_Learning|Same Label, Different Interface: Beyond Action-Space Labels in Robot Learning]]

![[assets/2610.38104_figure.png|800]]

- **arXiv**: [2610.38104](https://arxiv.org/abs/2610.38104)
- **PDF**: https://arxiv.org/pdf/2610.38104
- **详细分析**: [[20_Research/Papers/强化学习/Same_Label,_Different_Interface_Beyond_Action-Space_Labels_in_Robot_Learning|Same Label, Different Interface: Beyond Action-Space Labels in Robot Learning]]
- **作者**: Arshia Sangwan, Zhongyang Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Same Label, Different Interface: Beyond Action-Space Labels in Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-learning studies often compare position and velocity actions as though each label identified a single experimental treatment, yet the label alone does not determine what the robot executes. Before affecting robot motion, bounded policy output passes through filtering, physical scaling, reference construction, feedback, timing, and effort limits. We study how these omitted properties affect attribution under one shared learner and training budget. Across three contact-rich Factory tasks (PegInsert, GearMesh, and NutThread), we compare five joint-space interfaces, with ten independently trained policies per condition. We first remain within the same position-feedback law and vary the executed interface: substituting only the physical action scale as the directly modified component changes sample-median evaluation success by 0.645-1.000 across tasks, while removing an exponential moving average produces task-dependent changes. We then move to a cross-law comparison and choose a velocity scale that exactly matches the position interface's local raw-torque command gain. This calibration raises the sample median on GearMesh and NutThread, with no median change on PegInsert. Yet clear residual sample-median gaps remain on PegInsert and GearMesh, while the NutThread interval includes zero. Thus, even this explicit equality leaves feedback and held-action dynamics unmatched and does not establish position-velocity trained-outcome equivalence. Action-interface comparisons should therefore report the executed pathway and state the physical quantity they match.

</details>

---

### [[20_Research/Papers/强化学习/Cooperative_EV_Charging_Assignment_Using_Multi-Agent_Reinforcement_Learning_A_Comparison_of_QMIX_and_Independent_Q-Learning_Under_Urban_Traf|Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty]]

![[assets/2610.38053_figure.png|800]]

- **arXiv**: [2610.38053](https://arxiv.org/abs/2610.38053)
- **PDF**: https://arxiv.org/pdf/2610.38053
- **详细分析**: [[20_Research/Papers/强化学习/Cooperative_EV_Charging_Assignment_Using_Multi-Agent_Reinforcement_Learning_A_Comparison_of_QMIX_and_Independent_Q-Learning_Under_Urban_Traf|Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty]]
- **作者**: Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.22（加权：大模型 0.3，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The allocation of electric vehicles to public charging stations is increasingly constrained by the fact that several heterogeneous facilities often serve the same stream of requests while observing only partial local information. An accept/reject decision that is defensible for one station may nevertheless reduce the efficiency of the charging district as a whole. We formulate this operational problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) and examine whether Centralized Training with Decentralized Execution (CTDE), instantiated through QMIX, improves assignment performance relative to a cooperative Independent Q-Learning baseline (IQL). The evaluation uses a six-station urban network simulated with SUMO, five independent random seeds, 200 training episodes, and four traffic flux scenarios ranging from 100 to 250 vehicles/hour. Under this protocol, QMIX reaches a mean reward per evaluated decision of +0.776, versus +0.578 for IQL (delta = +0.198, seed-paired Cohens dz = 2.98, exact two-sided Wilcoxon p = 0.0625, the minimum attainable value at this sample size), and raises the acceptance rate from 72.4% to 94.0% (delta = +21.6 pp, dz = 5.24, Wilcoxon p = 0.0625). A five-variant ablation suggests this gain is primarily attributable to the CTDE architecture when holding cooperative reward terms fixed, though not formally isolated with a single seed. By contrast, cooperative reward shaping and experience sharing show no clear descriptive benefit and may slightly reduce performance. These findings support the view that, for multi-station charging assignment, coordination should be embedded in the learning architecture rather than added only through heuristic cooperation terms.

</details>

---

### [[20_Research/Papers/具身智能/FORGE_Feasible_Online_Reduced-Order_Reference_Generation_and_Whole-Body_Execution_for_Agile_Humanoid_Locomotion|FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion]]

![[assets/2610.37974_figure.jpg|800]]

- **arXiv**: [2610.37974](https://arxiv.org/abs/2610.37974)
- **PDF**: https://arxiv.org/pdf/2610.37974
- **详细分析**: [[20_Research/Papers/具身智能/FORGE_Feasible_Online_Reduced-Order_Reference_Generation_and_Whole-Body_Execution_for_Agile_Humanoid_Locomotion|FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion]]
- **作者**: Adrian B. Ghansah, Yujin An, Jeeseop Kim, Soon-Jo Chung
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 4.52（加权：具身智能 2.7，强化学习 0.16，世界模型 0.36，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion》归入 具身智能、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a two-stage learning framework for versatile and agile humanoid locomotion that couples online reduced-order model (ROM) reference generation with whole-body tracking control. In the first stage, we train a command-conditioned whole-body reference generator using single rigid body dynamics combined with full humanoid kinematics. In the second stage, the frozen ROM policy is rolled out online to generate references for training a whole-body tracking policy on the full-order dynamics model. Learning a kino-dynamically consistent reference generator in the simplified ROM space enables us to generate references over a broad command space and over multiple locomotion strategies using a single unified framework. We demonstrate the approach on a Unitree G1 humanoid robot, achieving longitudinal velocities from -2.0 m/s to 2.8 m/s, lateral velocities up to +-1.0 m/s, angular velocities up to +-3.0 rad/s, one-legged hopping, and continuous transitions across the commands, all using one unified reference policy and one whole-body tracking policy.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Global_Climate_Policy_Cooperation|Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation]]

![[assets/2610.37870_figure.png|800]]

- **arXiv**: [2610.37870](https://arxiv.org/abs/2610.37870)
- **PDF**: https://arxiv.org/pdf/2610.37870
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Global_Climate_Policy_Cooperation|Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation]]
- **作者**: Anne Moll-Elsborg, Oskar Bohn Lassen, Francisco Camara Pereira
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

International climate policy requires coordination among countries whose mitigation decisions impose local costs but generate global benefits. Classical game-theoretic and integrated assessment approaches can study these incentives, but typically rely on prescribed behavioural assumptions or equilibrium concepts. Recent work has therefore explored Multi-Agent Reinforcement Learning as a way to model climate-policy cooperation as an emergent outcome of repeated strategic interaction. We extend an existing MARL climate framework with a multi-stage negotiation mechanism in which agents propose agreements, accept or reject commitments, and face penalties for non-compliance. This allows us to study how agreement design affects learned mitigation behaviour, compliance, and climate outcomes. In an idealized setting with four homogeneous agents, we find that non-binding agreements do little to overcome free-riding, while moderate non-compliance penalties improve cooperation and reduce warming. However, excessively strong penalties discourage ambitious commitments, revealing a trade-off between enforcement and participation. We position the framework as a methodological contribution for testing agreement design rather than a predictive model of real negotiations.

</details>

---
