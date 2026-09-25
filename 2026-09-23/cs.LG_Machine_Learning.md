# cs.LG | Machine Learning | 2026-09-23

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/MAGIC_Mixed-Granularity_Agent_Graphs_via_Incremental_Construction_with_Dense-Reward_Reinforcement_Learning|MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning]]

![[assets/2609.26667_figure.png|800]]

- **arXiv**: [2609.26667](https://arxiv.org/abs/2609.26667)
- **PDF**: https://arxiv.org/pdf/2609.26667
- **详细分析**: [[20_Research/Papers/大模型/MAGIC_Mixed-Granularity_Agent_Graphs_via_Incremental_Construction_with_Dense-Reward_Reinforcement_Learning|MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning]]
- **作者**: Kairui Yang, Ziheng Yi, Xunkai Li, Minghao An, Zhanke Liu, Zekai Chen, Rong-Hua Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.6，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HumanEval, TAT-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granularity locally for each functional role, combining fine-grained control with reusable collaboration patterns within one organization. Learning such organizations requires exploring a combinatorial construction space with limited intermediate feedback from final-answer rewards. Therefore, we propose MAGIC, a dense-reward reinforcement learning framework for mixed-granularity graph generation. Specifically, MAGIC constructs a mixed-granularity agent graph by sequentially selecting a functional role, instantiating it as a single agent or reusable group, and connecting it to existing units. We directly optimize the construction policy using returns from trajectories sampled under the current policy and use potential-based reward shaping to provide intermediate feedback from probe-based utility and structural signals while preserving the cumulative task reward. MAGIC outperforms state-of-the-art baselines across eight benchmarks and demonstrates strong inference efficiency in our efficiency study.

</details>

---

### [[20_Research/Papers/强化学习/From_Risk_Scoring_to_Risk_Allocation_A_Density-Driven_Framework_for_Diverse_Monitoring_in_Multi-Agent_Systems|From Risk Scoring to Risk Allocation: A Density-Driven Framework for Diverse Monitoring in Multi-Agent Systems]]

![[assets/2609.26146_figure.png|800]]

- **arXiv**: [2609.26146](https://arxiv.org/abs/2609.26146)
- **PDF**: https://arxiv.org/pdf/2609.26146
- **详细分析**: [[20_Research/Papers/强化学习/From_Risk_Scoring_to_Risk_Allocation_A_Density-Driven_Framework_for_Diverse_Monitoring_in_Multi-Agent_Systems|From Risk Scoring to Risk Allocation: A Density-Driven Framework for Diverse Monitoring in Multi-Agent Systems]]
- **作者**: Zhaohui Wang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《From Risk Scoring to Risk Allocation: A Density-Driven Framework for Diverse Monitoring in Multi-Agent Systems》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Risk monitoring in multi-agent systems is commonly built on a per-state primitive that scores each state independently and selects the top K. Under crowding, where many agents share the same fragility, this approach picks redundant alerts whose risks are jointly correlated, a pattern we describe as ``herding in monitoring.'' We propose a paradigm shift from risk scoring to risk allocation, supported by two contributions. First, we identify the Crowding Paradox, namely that P(risk | x) $\propto$ p(x) rather than 1/p(x), so density rather than anomaly score is the operative risk signal; on financial data, density-based scoring reaches AUROC $\geq$ 0.94 at 5d/10d/20d crash horizons, while five anomaly baselines all fall below 0.80. Second, given a density-derived fragility score, we recast monitoring as combinatorial subset selection over interdependent states and map it to a QUBO objective with a $\lambda$-controlled risk--diversity tradeoff. The resulting Pareto frontier contains standard diverse-subset methods (MMR, k-DPP) as fixed operating points; the gain over greedy grows monotonically with scale, from +24% at n=15 to +66% at n=200; a learned $\lambda$ policy reaches 99.5% of an oracle grid-search objective; and the formulation transfers to traffic and multi-agent reinforcement learning. The same QUBO instances execute without modification on Rigetti superconducting QPUs (Ankaa-3 and Cepheus-1-108Q via Amazon Braket), which we report as a compatibility property of the formulation rather than a claim of quantum advantage at this scale.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Reconstruction_Error_Analytical_and_Data-Driven_Action_Tokenization_for_Autoregressive_Vision-Language-Action_Models|Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models]]

![[assets/2609.25820_first_page.png|800]]

- **arXiv**: [2609.25820](https://arxiv.org/abs/2609.25820)
- **PDF**: https://arxiv.org/pdf/2609.25820
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Reconstruction_Error_Analytical_and_Data-Driven_Action_Tokenization_for_Autoregressive_Vision-Language-Action_Models|Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models]]
- **作者**: Yuxin Yang, Gaohan He, Changxue Guan, Hangming Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discrete action tokenization is central to autoregressive vision-language-action (VLA) models, yet action representations are often evaluated primarily through reconstruction fidelity. We ask which representation properties actually matter for closed-loop control by comparing fixed analytical, data-driven linear, and nonlinear neural representations under a unified tokenization interface. Across rate-distortion analysis, sequence-modeling diagnostics, and 3,500 LIBERO rollouts, representation rankings change with the evaluation criterion. PCA achieves lower nominal reconstruction error than Temporal-DCT, but produces less predictable token sequences and 3.0 percentage points lower mean seen-task success across three policy-training seeds, with the policy ordering reversing in one seed. In a matched seed-42 ablation, an autoencoder further reduces reconstruction error yet does not yield the strongest policy and exhibits greater sensitivity to discrete token perturbations. These findings show that reconstruction fidelity alone cannot reliably select action representations for autoregressive control, motivating joint evaluation of geometric fidelity, sequence predictability, decoder stability, and closed-loop performance.

</details>

---

### [[20_Research/Papers/强化学习/Fully_Byzantine-Resilient_Multi-Agent_Reinforcement_Learning|Fully Byzantine-Resilient Multi-Agent Reinforcement Learning]]

![[assets/2609.25701_figure.png|800]]

- **arXiv**: [2609.25701](https://arxiv.org/abs/2609.25701)
- **PDF**: https://arxiv.org/pdf/2609.25701
- **详细分析**: [[20_Research/Papers/强化学习/Fully_Byzantine-Resilient_Multi-Agent_Reinforcement_Learning|Fully Byzantine-Resilient Multi-Agent Reinforcement Learning]]
- **作者**: Haejoon Lee, Dimitra Panagou
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 世界模型
- **相关性评分**: 2.02（加权：大模型 0.5，强化学习 1.16，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Fully Byzantine-Resilient Multi-Agent Reinforcement Learning》归入 强化学习、大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AC-MARL, FRAC-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear parameterizations of the value and team-reward functions and Byzantine edge attacks, where adversarial behavior is confined to the communication layer, we prove that agents' parameters converge almost surely to the same limit points as in the attack-free case over time-varying communication graphs. We introduce a novel topological condition for the convergence of our method, present a systematic method to construct such networks, and prove that this condition can be verified in polynomial time. Finally, we demonstrate our method on cooperative multi-robot formation control tasks.

</details>

---

### [[20_Research/Papers/具身智能/HABILIS_Brain_0_Geometry-Change_Supervision_for_Vision-Language-Action_and_Residual_Flow_Recovery|HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery]]

![[assets/2609.25558_figure.png|800]]

- **arXiv**: [2609.25558](https://arxiv.org/abs/2609.25558)
- **PDF**: https://arxiv.org/pdf/2609.25558
- **详细分析**: [[20_Research/Papers/具身智能/HABILIS_Brain_0_Geometry-Change_Supervision_for_Vision-Language-Action_and_Residual_Flow_Recovery|HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery]]
- **作者**: Jinu Pahk, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm, Jaejoon Kim, Byoung-Tak Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GC-VLA, OpenVLA, VideoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. Offline frame pairs define a nominal 0.5-second prediction horizon; future observations are used only to construct training targets. Stage 1 trains a geometry-change vision-language model (GC-VLM). Stage 2 introduces a continuous ActionExpert and aligns it with robot actions while stopping action-flow gradients at the VLM interface. Stage 3 enables these gradients to update the trainable VLM components jointly with the ActionExpert. Stage 4 freezes GC-VLA and applies Geometry-Conditioned Residual Flow (GCRF), using a binary intervention router and a single bounded residual velocity policy learned from closed-loop feedback. GC-VLA achieves 95.20% success on LIBERO, and GC-VLA with GCRF achieves 99.55%. Inference uses current observations and the learned GC representation without executing the offline target encoders.

</details>

---
