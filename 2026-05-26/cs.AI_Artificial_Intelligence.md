# cs.AI | Artificial Intelligence | 2026-05-26

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/强化学习/Learning_in_Low-Dimensional_Subspaces_Orthogonal_Bottlenecks_for_Reinforcement_Learning|Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning]]

![[assets/2605.26012_figure.png|800]]

- **arXiv**: [2605.26012](https://arxiv.org/abs/2605.26012)
- **PDF**: https://arxiv.org/pdf/2605.26012
- **详细分析**: [[20_Research/Papers/强化学习/Learning_in_Low-Dimensional_Subspaces_Orthogonal_Bottlenecks_for_Reinforcement_Learning|Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning]]
- **作者**: Aleksandar Todorov, Matthia Sabatelli
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning in Low-Dimensional Subspaces: Orthogonal Bottlenecks for Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (RL) agents commonly rely on high-dimensional neural representations, despite growing evidence that task-relevant value and policy structure may be intrinsically low-dimensional. In this work, we present a simple yet effective representation-level prior that inserts a fixed orthonormal projection to constrain encoder features to a low-dimensional subspace, requiring no auxiliary objectives, pretraining, or changes to the underlying RL algorithm. Under a linear realizability assumption, we prove that when the bottleneck dimension exceeds the intrinsic rank of the optimal value function in feature space, the bottleneck preserves expressivity and leaves the induced gradient dynamics unchanged up to an equivalent low-dimensional parameterization. Empirically, we find that across both single and multi-task benchmarks, baseline performance is either matched or improved once the bottleneck dimension exceeds a small task-dependent threshold; in many cases, value representations can be compressed to extremely low dimensions without loss, and the minimal sufficient dimension depends far more on environment complexity than encoder width. In addition, we analyze representation geometry and find that orthogonal bottlenecks stabilize feature norms and are associated with higher effective rank. Together, these results support a representation-space interpretation of the manifold hypothesis in reinforcement learning and position orthogonal bottlenecks as a lightweight, architecture-agnostic mechanism for shaping RL representations.

</details>

---

### [[20_Research/Papers/大模型/Can_LLMs_Time_Travel_Enhancing_Temporal_Consistency_in_Legal_Agentic_Search_through_Reinforcement_Learning|Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning]]

![[assets/2605.25920_figure.png|800]]

- **arXiv**: [2605.25920](https://arxiv.org/abs/2605.25920)
- **PDF**: https://arxiv.org/pdf/2605.25920
- **详细分析**: [[20_Research/Papers/大模型/Can_LLMs_Time_Travel_Enhancing_Temporal_Consistency_in_Legal_Agentic_Search_through_Reinforcement_Learning|Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning]]
- **作者**: Wei Fan, Yining Zhou, Mufan Zhang, Yanbing Weng, Yiran HU, Tianshi Zheng, Baixuan Xu, Chunyang Li, Jianhui Yang, Haoran Li, Yangqiu Song
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.45，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search through Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DISC-LawEval, KQA, LawBench, LexEval, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While large language models (LLMs) augmented with agentic search capabilities show promise for legal reasoning, they overlook a fundamental constraint that applicable law must match the temporal context of each case, as retroactive application of statutes violates core legal principles and leads to erroneous conclusions. Our observations reveal that current legal LLMs suffer from temporal bias anchored to their training cutoff, while search agents rarely incorporate temporal constraints into queries, and that web search alone cannot provide the precise statute and precedent citations that legal reasoning demands. To address these challenges, we propose LegalSearch-R1, an end-to-end reinforcement learning framework that pairs local statute RAG for precise article matching with online web search for broader legal knowledge, trained on temporally-indexed data spanning multiple amendment periods to enforce temporal consistency. Extensive experiments on our benchmark covering 13 legal tasks demonstrate that our 7B-parameter agent outperforms state-of-the-art deep research frameworks and specialized legal LLMs by 12.9% to 29.8%, surpasses baselines by 57.7% to 80.3% on temporal consistency, and exhibits robust out-of-domain generalization. The code and data are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/TIAR_Trajectory-Informed_Advantage_Reweighting_for_LLM_Abstention_Learning|TIAR: Trajectory-Informed Advantage Reweighting for LLM Abstention Learning]]

![[assets/2605.25850_figure.png|800]]

- **arXiv**: [2605.25850](https://arxiv.org/abs/2605.25850)
- **PDF**: https://arxiv.org/pdf/2605.25850
- **详细分析**: [[20_Research/Papers/大模型/TIAR_Trajectory-Informed_Advantage_Reweighting_for_LLM_Abstention_Learning|TIAR: Trajectory-Informed Advantage Reweighting for LLM Abstention Learning]]
- **作者**: Muyu Pan, Shu Zhao, Nan Zhang, Philip Shin, Varun Parekh, Vijaykrishnan Narayanan, Rui Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.75，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《TIAR: Trajectory-Informed Advantage Reweighting for LLM Abstention Learning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AbstentionBench, TruthRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates large language model (LLM) abstention learning, specifically using ternary reward, which incentivize truthfulness in large language models. This paper extends that idea by moving from a ternary reward to a Trajectory-Informed advantage reweighting, dynamically re-weights the abstention reward during Group Relative Policy Optimization (GRPO) training. The objective of this work focuses on abstention learning instead of improving truthfulness, serving as an exploration into hallucination reduction. The novelty of this paper lies in methodological innovation, advantage re-weighting, and benchmark selection. Leveraging GRPO's multiple trajectories as a natural abstention signal, this method uses a reward signal to explore knowledge boundaries and encourage consistency. By demonstrating that trajectories can be used as a confidence indicator of the policy relative to the query, they are then used to dynamically calculate the abstention advantage. AbstentionBench is used as the evaluation benchmark, as this work aims to contribute to the field of abstention learning. All datasets on the benchmark were tested against this method and various baselines. Empirical results demonstrate that TIAR achieves state-of-the-art abstention F1 scores across five of six evaluation categories, outperforming the static ternary baseline on 17 of 31 benchmark datasets while fully preserving baseline accuracy.

</details>

---

### [[20_Research/Papers/具身智能/When_Search_Becomes_Memory_Turning_Robot_Design_Trials_into_Transferable_Skills|When Search Becomes Memory: Turning Robot Design Trials into Transferable Skills]]

![[assets/2605.25832_first_page.png|800]]

- **arXiv**: [2605.25832](https://arxiv.org/abs/2605.25832)
- **PDF**: https://arxiv.org/pdf/2605.25832
- **详细分析**: [[20_Research/Papers/具身智能/When_Search_Becomes_Memory_Turning_Robot_Design_Trials_into_Transferable_Skills|When Search Becomes Memory: Turning Robot Design Trials into Transferable Skills]]
- **作者**: Yunfei Wang, Xiaohao Xu, Yang Li, Xiaonan Huang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.15（加权：具身智能 0.6，大模型 0.45，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《When Search Becomes Memory: Turning Robot Design Trials into Transferable Skills》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EvoGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used as proposal generators for evolutionary robot design, yet most loops remain memoryless: simulator results shape the next population but are not preserved as reusable design knowledge. We present Auto-Robotist, a self-evolving LLM agent that distills morphology-search traces into an explicit natural-language skill library. Each skill stores a structural archetype, evidence-grounded positive and negative rules, and the evaluated designs that support them, making design memory inspectable rather than implicit in a population. During search, the agent retrieves skills to condition LLM edits of elite bodies while retaining a Genetic Algorithm (GA) mutation path for exploration; after evaluation, it updates the library through Add, Diagnose, and Merge. Across seven EvoGym tasks spanning locomotion, traversal, and object interaction, Auto-Robotist improves cold-start 5x5 search and transfers learned skills to 10x10 design spaces, where reference-conditioned transfer outperforms GA on every task. These results suggest that LLM agents can convert expensive physical evaluations into reusable, auditable design principles. Our code will be released upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/OASIS_Observation-Action_Space_Alignment_via_SE(3)_Trajectory_Prediction_for_Robotic_Manipulation|OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation]]

![[assets/2605.25829_figure.png|800]]

- **arXiv**: [2605.25829](https://arxiv.org/abs/2605.25829)
- **PDF**: https://arxiv.org/pdf/2605.25829
- **详细分析**: [[20_Research/Papers/具身智能/OASIS_Observation-Action_Space_Alignment_via_SE(3)_Trajectory_Prediction_for_Robotic_Manipulation|OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation]]
- **作者**: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, QDepth-VLA, ReconVLA, SpatialVLA, URL, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent vision-language-action (VLA) models and world action models (WAMs) advance robotic manipulation by enriching intermediate representations with auxiliary spatial features or future visual-state prediction. However, these representations largely remain within the observation space and do not share the rigid-body geometry of the action space, forcing the action decoder to implicitly recover this geometry. We propose OASIS, a visuomotor policy that aligns the intermediate representation with the action space via $SE(3)$ end-effector trajectory prediction. OASIS couples a 3D-aware feature encoder that fuses vision-language and metric-depth features with an $SE(3)$ trajectory predictor that produces a camera-frame end-effector trajectory. Conditioned on the predictor's pose-supervised hidden states, the action decoder generates action chunks consistent with rigid-body motion. Across simulation and real-world experiments, OASIS outperforms VLA and WAM baselines in success rate and out-of-distribution generalization. Our project page is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/CUA-Gym_Scaling_Verifiable_Training_Environments_and_Tasks_for_Computer-Use_Agents|CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents]]

![[assets/2605.25624_first_page.png|800]]

- **arXiv**: [2605.25624](https://arxiv.org/abs/2605.25624)
- **PDF**: https://arxiv.org/pdf/2605.25624
- **详细分析**: [[20_Research/Papers/大模型/CUA-Gym_Scaling_Verifiable_Training_Environments_and_Tasks_for_Computer-Use_Agents|CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents]]
- **作者**: Bowen Wang, Dunjie Lu, Junli Wang, Tianyi Bai, Shixuan Liu, Zhipeng Zhang, Haiquan Wang, Hao Hu, Tianbao Xie, Shuai Bai, Dayiheng Liu, Que Shen...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.6，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CUA-Gym, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has driven breakthroughs in domains such as math, tool-use, and software engineering, yet its extension to computer-use agents (CUAs) has been bottlenecked by the scarcity of scalable training data with deterministic rewards. Constructing such data for CUAs requires consistent task instruction, executable environment, and verifiable reward. However, hand-curated benchmarks achieve high reward fidelity but cover few applications and LLM-as-judge-based datasets scale broadly but lack reliable verification. We present CUA-Gym, a scalable pipeline that co-generates task instructions, environment states, and reward functions. Concretely, a Generator agent constructs the initial and golden environment states, and a separate Discriminator agent writes the reward function from the task specification. An orchestrator agent drives the two through iterative rounds upon execution. Generated tuples then pass a final filter combining LLM majority voting and agent rollouts, ensuring quality beyond the per-task adversarial loop. To address the scarcity of training environments, we further synthesize CUA-Gym-Hub, a broad suite of high-fidelity mock web applications grounded in real-world software-use distributions, expanding the scale of CUA RLVR data by magnitude. Using this pipeline, we construct CUA-Gym, a dataset of 32,112 verified RLVR training tuples grounded in 110 environments. Trained with GSPO on CUA-Gym, our CUA-Gym-A3B and CUA-Gym-A17B achieve 62.1% and 72.6% on OSWorld-Verified, outperforming prior open-source CUAs at comparable scales, with performance scaling smoothly in both data volume and environment diversity. The same checkpoints also improve on the held-out WebArena benchmark, indicating transfer beyond the training environments. We will open-source the full synthesis pipeline, dataset, CUA-Gym-Hub environments, and models.

</details>

---

### [[20_Research/Papers/强化学习/Acting_on_the_Unseen_Communication-Free_Collaborative_Filtering_for_Decentralized_Multi-Robot_Task_Allocation|Acting on the Unseen: Communication-Free Collaborative Filtering for Decentralized Multi-Robot Task Allocation]]

![[assets/2605.25584_first_page.png|800]]

- **arXiv**: [2605.25584](https://arxiv.org/abs/2605.25584)
- **PDF**: https://arxiv.org/pdf/2605.25584
- **详细分析**: [[20_Research/Papers/强化学习/Acting_on_the_Unseen_Communication-Free_Collaborative_Filtering_for_Decentralized_Multi-Robot_Task_Allocation|Acting on the Unseen: Communication-Free Collaborative Filtering for Decentralized Multi-Robot Task Allocation]]
- **作者**: Alexander Apartsin, Yigal Meshulam, Yehudit Aperstein
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Acting on the Unseen: Communication-Free Collaborative Filtering for Decentralized Multi-Robot Task Allocation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot task allocation usually assumes some combination of communication, known task models, or a coordinator. We study the opposite extreme, a regime common in practice but overlooked in theory, which we name Zero-Knowledge MRTA (ZK-MRTA): a robot team with no prior knowledge (no task models, not even the latent rank), no communication (no messages, no parameter sharing, no coordinator), and only a partial and privately-noisy view of a public stream of teammates' outcomes. A hidden low-rank structure governs which robot suits which task, and there are far more tasks than rounds, so most (robot, task) pairs are never attempted. Yet each robot can act well on tasks it never attempted, and onboard new tasks, by running online low-rank collaborative filtering over the broadcast (SwarmCF). The advantage over any structure-free learner is categorical, not a constant factor: a structure-free learner is provably at the prior-mean error floor on unseen pairs. We prove a matching per-robot sample complexity ({\Theta}(d) versus {\Theta}(n), in the rank d and the task count n), an anytime (cumulative-reward) separation under task scarcity, and a deterministic condition under which decentralized recovery from the masked broadcast is exact (validated empirically). Experiments quantify the value of the broadcast, a positive scaling law (per-robot unseen-pair skill rises with team size), and the strongest masking-robustness and anytime profile among low-rank methods, recovering most (about 80% on earned skill) of a centralized full-communication ceiling, and holding under capacity-1 contention and in a robotics-grounded sensing instance.

</details>

---

### [[20_Research/Papers/具身智能/EXPO-FT_Sample-Efficient_Reinforcement_Learning_Finetuning_for_Vision-Language-Action_Models|EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models]]

![[assets/2605.25477_figure.png|800]]

- **arXiv**: [2605.25477](https://arxiv.org/abs/2605.25477)
- **PDF**: https://arxiv.org/pdf/2605.25477
- **详细分析**: [[20_Research/Papers/具身智能/EXPO-FT_Sample-Efficient_Reinforcement_Learning_Finetuning_for_Vision-Language-Action_Models|EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models]]
- **作者**: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The ability to efficiently and reliably learn new tasks has been a foundational challenge in robotics. Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse manipulation tasks, yet pretrained policies consistently fall short of the reliability required for real-world deployment. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches either train from scratch without fully leveraging pretrained priors, or fine-tune VLAs without achieving the sample efficiency and success rates that practical deployment demands. We present EXPO-FT, a system for stable, sample-efficient RL finetuning of pretrained VLA policies that closes this gap. Our system solves a suite of challenging manipulation tasks, including routing string lights and inserting the plug to light it up, striking a pool ball into a pocket, and inserting a flower into a wine bottle, each requiring combinations of high precision, dynamic actions, and robustness to varied initial states. Our system achieves perfect task performance (30/30 successes) across all evaluated tasks within an average of 19.1 minutes of online robot data, outperforming both prior RL-from-scratch and VLA finetuning approaches. We release an open-source codebase with the aim of facilitating broader adoption of RL finetuning of VLA models in robotics.

</details>

---

### [[20_Research/Papers/具身智能/SeqRoute_Global_Budget-Aware_Sequential_LLM_Routing_via_Offline_Reinforcement_Learning|SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning]]

![[assets/2605.25424_figure.png|800]]

- **arXiv**: [2605.25424](https://arxiv.org/abs/2605.25424)
- **PDF**: https://arxiv.org/pdf/2605.25424
- **详细分析**: [[20_Research/Papers/具身智能/SeqRoute_Global_Budget-Aware_Sequential_LLM_Routing_via_Offline_Reinforcement_Learning|SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning]]
- **作者**: Zhongling Xu, Shunan Zheng, Wei Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《SeqRoute: Global Budget-Aware Sequential LLM Routing via Offline Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing LLM routing frameworks treat queries as independent events, neglecting the sequential nature of real-world user sessions constrained by global computational budgets. This mismatch inevitably leads to budget bankruptcy: myopic routing policies exhaust resources on early interactions, forcing subsequent and often more complex queries onto inadequate models. We introduce SeqRoute, a framework that formulates multi-turn routing as a finite-horizon Markov Decision Process and solves it via offline reinforcement learning. By incorporating the remaining budget into the state space and training with Conservative Q-Learning (CQL), SeqRoute learns delayed gratification to strategically preserve resources for high-stakes turns later in the session. To overcome data starvation, we propose Hindsight Budget Relabeling (HBR). This technique retrospectively simulates historical trajectories under diverse hypothetical budgets, expanding 10,000 raw sessions into 2.38 million transitions enriched with critical bankruptcy signals. At deployment, a dynamic $\lambda$-sweep mechanism enables zero-shot navigation of the cost-quality Pareto frontier without retraining. Extensive evaluations demonstrate that SeqRoute reduces operational costs by 6.0-73.5% while maintaining or improving quality, and suppresses bankruptcy rates to under 1%, strictly dominating behavior cloning, budget-aware heuristics, and static baselines across the entire Pareto frontier.

</details>

---

### [[20_Research/Papers/大模型/Evo-Attacker_Memory-Augmented_Reinforcement_Learning_for_Long-Horizon_Tool_Attacks_on_LLM-MAS|Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS]]

![[assets/2605.25389_figure.png|800]]

- **arXiv**: [2605.25389](https://arxiv.org/abs/2605.25389)
- **PDF**: https://arxiv.org/pdf/2605.25389
- **详细分析**: [[20_Research/Papers/大模型/Evo-Attacker_Memory-Augmented_Reinforcement_Learning_for_Long-Horizon_Tool_Attacks_on_LLM-MAS|Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS]]
- **作者**: Bingyu Yan, Xiaoming Zhang, Jinyu Hou, Chaozhuo Li, Ziyi Zhou, Yiming Hei, Litian Zhang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 0.8，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. Existing tool attacks are limited by domain specificity or fixed and static templates. To address these challenges, we propose Evo-Attacker, which formulates the tool attack as a self-evolving, memory-augmented reinforcement learning process. Evo-Attacker constructs a dynamic attack memory and employs deliberative reasoning to retrieve adversarial patterns and strategize modifying interventions at critical moments. Furthermore, we introduce Attack-Flow GRPO to optimize intermediate reasoning steps via terminal outcomes, addressing the long-horizon credit assignment challenge. Comprehensive experiments demonstrate that Evo-Attacker consistently outperforms baselines, highlighting its generalization and evolutionary capabilities and the urgent need for defensive tool safeguards.

</details>

---

### [[20_Research/Papers/世界模型/UWM-JEPA_Predictive_World_Models_That_Imagine_in_Belief_Space|UWM-JEPA: Predictive World Models That Imagine in Belief Space]]

![[assets/2605.25313_figure.png|800]]

- **arXiv**: [2605.25313](https://arxiv.org/abs/2605.25313)
- **PDF**: https://arxiv.org/pdf/2605.25313
- **详细分析**: [[20_Research/Papers/世界模型/UWM-JEPA_Predictive_World_Models_That_Imagine_in_Belief_Space|UWM-JEPA: Predictive World Models That Imagine in Belief Space]]
- **作者**: Santosh Kumar Radha, Oktay Goktas
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《UWM-JEPA: Predictive World Models That Imagine in Belief Space》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for partially observed environments must imagine multiple compatible hidden futures and steer between them under counterfactual actions. Joint Embedding Predictive Architectures (JEPAs) do this in latent space, but a vector-valued latent has no internal structure for carrying the belief over hidden continuations through blind rollout. We introduce the Unitary World Model JEPA (UWM-JEPA), a JEPA world model with a density-matrix latent on a joint system-environment space and a learned unitary predictor. The construction preserves the joint-state spectrum exactly during rollout, so the predictor itself cannot dissipate the represented uncertainty. On a hidden-velocity indicator task requiring five-step forward simulation under a given action sequence with the target observation masked, UWM-JEPA reaches 0.77 accuracy and degrades monotonically as actions are perturbed; a parameter-matched LSTM-JEPA trained under the same counterfactual-target objective and action head collapses to majority-class accuracy (0.53) under every action condition. Under blind rollout, UWM-JEPA loses fewer than ten points of probe R^2 at short horizons while vector-latent baselines lose forty-one and sixty-eight; both nevertheless tie on a held-out context probe, locating the separation in the predictor rather than the encoder. Action sensitivity itself requires training against counterfactual rather than teacher-forced targets, a finding that applies beyond the unitary parameterisation. For JEPA world models to imagine under partial observability, latent geometry and predictor dynamics matter, not frozen context-encoding capacity alone.

</details>

---

### [[20_Research/Papers/强化学习/Latent_Q-Barrier_Shielding_for_Safe_In-Context_Reinforcement_Learning|Latent Q-Barrier Shielding for Safe In-Context Reinforcement Learning]]

![[assets/2605.25267_first_page.png|800]]

- **arXiv**: [2605.25267](https://arxiv.org/abs/2605.25267)
- **PDF**: https://arxiv.org/pdf/2605.25267
- **详细分析**: [[20_Research/Papers/强化学习/Latent_Q-Barrier_Shielding_for_Safe_In-Context_Reinforcement_Learning|Latent Q-Barrier Shielding for Safe In-Context Reinforcement Learning]]
- **作者**: Minjae Kwon, Amir Moeini, Shangtong Zhang, Lu Feng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Latent Q-Barrier Shielding for Safe In-Context Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ICRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe in-context reinforcement learning (ICRL) adapts online from interaction history without test-time parameter updates while controlling episode cost under a safety budget. Under out-of-distribution (OOD) deployment shifts, pretraining-only safe ICRL can give poor reward-safety tradeoffs because the remaining budget affects behavior only through frozen policy conditioning, not an explicit action-level check against predicted future cost. We propose a latent Q-Barrier shield that learns a context representation, latent dynamics, and an ensemble cost critic before deployment. Without parameter updates, the shield infers context from history and filters or softly reweights candidate actions using the remaining budget and predicted future cost. We prove a conditional, error-decomposed barrier-margin result: a Q-Barrier-satisfying action leaves the next latent-budget state with an approximately budget-safe continuation under the learned critic, up to Bellman and latent-prediction errors. Across five safe ICRL benchmarks, the shield improves deployment-time reward-safety tradeoffs over a strong safe-ICRL baseline: after a short context window, it achieves higher return in four of five benchmarks while matching or lowering average episode cost in all five.

</details>

---

### [[20_Research/Papers/具身智能/Grow-Prune-Freeze_Networks_Adaptive_&_Continual_Learning_Technique_for_Olfactory_Navigation|Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation]]

![[assets/2605.25170_figure.png|800]]

- **arXiv**: [2605.25170](https://arxiv.org/abs/2605.25170)
- **PDF**: https://arxiv.org/pdf/2605.25170
- **详细分析**: [[20_Research/Papers/具身智能/Grow-Prune-Freeze_Networks_Adaptive_&_Continual_Learning_Technique_for_Olfactory_Navigation|Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation]]
- **作者**: Kordel K. France, Ovidiu Daescu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 世界模型, 具身智能, 大模型
- **相关性评分**: 1.62（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 0.36，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Grow-Prune-Freeze Networks: Adaptive & Continual Learning Technique for Olfactory Navigation》归入 机器人、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MorphNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training data for olfaction is scattered through disparate, non-standardized datasets that limit the ability to build representative world models. Olfactory navigation is a highly dynamic and non-stationary task that benefits from real-time continual learning. We introduce an adaptive framework called Grow-Prune-Freeze (GPF) networks that enable an agent to continually learn through growing, pruning, and freezing early layers of its policy in response to world complexity. Grounding GPFs in non-linear random matrix theory, we show that the work of Pennington &amp; Worth (2017) can be extended from single hidden layers to n-layer continual-learning models, and that eigenvalue composition of network weights is preserved as successive layers are added. We show that GPFs based on Expected SARSA achieve a 94% success rate on turbulent plume navigation - a partially observable, non-stationary task representative of the "big world" challenges that motivate adaptive learning in robotics - and provide supporting methodology for applying GPFs in other world models. Further experiments amount evidence that GPFs may generalize well to other machine learning tasks such as reinforcement learning in Atari, image classification, and autoregressive language models. We open source all code and data to encourage improvements on and more research in olfactory robotics.

</details>

---

### [[20_Research/Papers/大模型/LLM_Agent_Based_Renewable_Energy_Forecasting_Using_Edge_and_IoT_Data_A_Review_of_Solar_Wind_Weather_and_Grid_Aware_Decision_Support|LLM Agent Based Renewable Energy Forecasting Using Edge and IoT Data A Review of Solar Wind Weather and Grid Aware Decision Support]]

![[assets/2605.25141_first_page.png|800]]

- **arXiv**: [2605.25141](https://arxiv.org/abs/2605.25141)
- **PDF**: https://arxiv.org/pdf/2605.25141
- **详细分析**: [[20_Research/Papers/大模型/LLM_Agent_Based_Renewable_Energy_Forecasting_Using_Edge_and_IoT_Data_A_Review_of_Solar_Wind_Weather_and_Grid_Aware_Decision_Support|LLM Agent Based Renewable Energy Forecasting Using Edge and IoT Data A Review of Solar Wind Weather and Grid Aware Decision Support]]
- **作者**: Pavan Manjunath, Thomas Pruefer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Agent Based Renewable Energy Forecasting Using Edge and IoT Data A Review of Solar Wind Weather and Grid Aware Decision Support》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable forecasting of renewable energy generation is a foundational requirement for grid stability energy trading battery scheduling and carbon aware operational planning Solar and wind resources are inherently intermittent their output fluctuates with cloud cover wind speed atmospheric turbulence seasonal patterns and local terrain The proliferation of IoT and edge devices spanning smart meters inverters anemometers pyranometers weather stations and grid interface sensors has created an unprecedented volume of real time operational data that conventional forecasting pipelines are ill equipped to exploit fully This review investigates how large language model LLM agents can enhance renewable energy forecasting by integrating heterogeneous sensor streams weather API data historical generation records grid constraints and contextual reasoning into unified decision support workflows We survey classical forecasting methods statistical time series models deep learning architectures physics hybrid approaches and emerging LLM agent frameworks for explanation uncertainty communication and operator guidance A six layer taxonomy is proposed covering data acquisition preprocessing feature engineering model inference uncertainty estimation and natural language reporting The review identifies twelve open challenges spanning real time deployment model drift under distribution shift uncertainty quantification hallucination control in LLM agents interoperability of edge hardware and integration with energy management systems The paper concludes by recommending a research agenda centred on open benchmarks physics informed LLM grounding and federated forecasting architectures

</details>

---

### [[20_Research/Papers/强化学习/Evolutionary_Enhanced_Multi-Agent_Reinforcement_Learning_for_Cooperative_Air_Combat|Evolutionary Enhanced Multi-Agent Reinforcement Learning for Cooperative Air Combat]]

![[assets/2605.25091_figure.png|800]]

- **arXiv**: [2605.25091](https://arxiv.org/abs/2605.25091)
- **PDF**: https://arxiv.org/pdf/2605.25091
- **详细分析**: [[20_Research/Papers/强化学习/Evolutionary_Enhanced_Multi-Agent_Reinforcement_Learning_for_Cooperative_Air_Combat|Evolutionary Enhanced Multi-Agent Reinforcement Learning for Cooperative Air Combat]]
- **作者**: Chengwei Li, Junlin Liu, Yang Gao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Evolutionary Enhanced Multi-Agent Reinforcement Learning for Cooperative Air Combat》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CEM-RL, DRL, ERL, MARL, PDERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As modern air combat evolves toward beyond-visual-range (BVR) multi-aircraft cooperative engagements, autonomous decision-making for unmanned combat aerial vehicles (UCAVs) faces significant challenges due to high-dimensional state spaces, discrete action commands, and strongly adversarial dynamic environments. To overcome the limitations of existing multi-agent reinforcement learning (MARL) methods in such settings, namely insufficient exploration efficiency, low sample utilization, and poor policy generalization, we propose Adversarial Curriculum and Evolutionary-enhanced Multi-agent Proximal Policy Optimization (ACE-MAPPO), a hybrid learning framework that integrates evolutionary algorithms with MAPPO. Specifically, a genetic soft update mechanism is introduced to enhance population diversity and mitigate convergence to local optima. An evolutionary-augmented prioritized trajectory replay strategy is further employed to improve the utilization of sparse high-value samples. In addition, an adversarial evolutionary curriculum learning mechanism is designed to enable adaptive training with progressively increasing difficulty. Extensive experimental results demonstrate that the proposed method outperforms MAPPO and other baseline algorithms in terms of training stability, convergence speed, and win rate, validating its effectiveness in multi-aircraft cooperative air combat scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Performance_Comparison_of_Classical_and_Neural_Sampling_Algorithms_for_Robotic_Navigation|Performance Comparison of Classical and Neural Sampling Algorithms for Robotic Navigation]]

![[assets/2605.25010_figure.png|800]]

- **arXiv**: [2605.25010](https://arxiv.org/abs/2605.25010)
- **PDF**: https://arxiv.org/pdf/2605.25010
- **详细分析**: [[20_Research/Papers/具身智能/Performance_Comparison_of_Classical_and_Neural_Sampling_Algorithms_for_Robotic_Navigation|Performance Comparison of Classical and Neural Sampling Algorithms for Robotic Navigation]]
- **作者**: Hichem Cheriet, Badra Khellat Kihel, Samira Chouraqui
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Performance Comparison of Classical and Neural Sampling Algorithms for Robotic Navigation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MPNet, ResNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrating artificial intelligence (AI) into sampling-based motion planning provides new possibilities for improving autonomous navigation efficiency. In this paper, three algorithms, namely RRT*, Neural RRT*, and Neural Informed RRT*, are implemented and evaluated on environments containing convex and concave obstacles with different obstacle densities. The obtained results indicate that neural-guided planners improve path quality, producing up to 14\% shorter paths and 55--75\% smoother trajectories compared with the conventional RRT* algorithm. Among the evaluated methods, Neural Informed RRT* achieves the best overall performance in terms of path length and trajectory smoothness. These results demonstrate the effectiveness of AI-guided sampling strategies for improving reliability and trajectory efficiency in robotic and UAV navigation, despite a slight increase in computation time. Overall, the study highlights the growing importance of artificial intelligence in real-time robotic path planning applications.

</details>

---

### [[20_Research/Papers/强化学习/Scaling_up_Energy-Aware_Multi-Agent_Reinforcement_Learning_for_Mission-Oriented_Drone_Networks_with_Individual_Reward|Scaling up Energy-Aware Multi-Agent Reinforcement Learning for Mission-Oriented Drone Networks with Individual Reward]]

![[assets/2605.24992_figure.png|800]]

- **arXiv**: [2605.24992](https://arxiv.org/abs/2605.24992)
- **PDF**: https://arxiv.org/pdf/2605.24992
- **详细分析**: [[20_Research/Papers/强化学习/Scaling_up_Energy-Aware_Multi-Agent_Reinforcement_Learning_for_Mission-Oriented_Drone_Networks_with_Individual_Reward|Scaling up Energy-Aware Multi-Agent Reinforcement Learning for Mission-Oriented Drone Networks with Individual Reward]]
- **作者**: Changling Li, Ying Li
- **cs 子类**: cs.AI, cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 世界模型
- **相关性评分**: 2.32（加权：大模型 0.4，强化学习 0.96，世界模型 0.16，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Scaling up Energy-Aware Multi-Agent Reinforcement Learning for Mission-Oriented Drone Networks with Individual Reward》归入 强化学习、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Li2022MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reinforcement learning (MARL) has shown wide applicability in collaborative systems such as autonomous driving and smart cities for its ability of learning through interaction. With the recent development of drone networks, researchers have also applied MARL to address the trajectory planning problems. However, the dynamic environment and the limited battery capacity are still challenging for using MARL to achieve efficient collaborative task execution. In this paper, we propose an energy-aware MARL model as an attempt to tackle these challenges, leveraging Deep Q-Networks (DQN) with \emph{individual reward functions} driven by the task execution progress and the remaining battery of drones. We conduct a set of simulation studies for the proposed mode and compare it with the shared reward MARL~\cite{Li2022MARL} to explore the impact of credit assignment in MARL. The results indicate that our proposed model can achieve at least 80\% success rate regardless of the task locations and lengths. Similar to the shared reward mode, the individual reward mode can achieve a better success rate when the task density is high, and it can hit nearly a 100\% success rate when task density gets close to 40\%. The true advantage of our proposed model with individual reward is revealed when scaling up the environment. The comparison to the shared reward MARL shows that the our proposed model is more robust towards the change of the environment size and agent numbers. It can achieve higher success rate with fewer steps due to the clarity of the goal which improves energy efficiency even better.

</details>

---

### [[20_Research/Papers/具身智能/Bridging_the_Gap_Enabling_Soft_Actor_Critic_for_High_Performance_Legged_Locomotion|Bridging the Gap: Enabling Soft Actor Critic for High Performance Legged Locomotion]]

![[assets/2605.24975_figure.png|800]]

- **arXiv**: [2605.24975](https://arxiv.org/abs/2605.24975)
- **PDF**: https://arxiv.org/pdf/2605.24975
- **详细分析**: [[20_Research/Papers/具身智能/Bridging_the_Gap_Enabling_Soft_Actor_Critic_for_High_Performance_Legged_Locomotion|Bridging the Gap: Enabling Soft Actor Critic for High Performance Legged Locomotion]]
- **作者**: Gianluca Sabatini, Chenhao Li, Marco Hutter
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.02（加权：具身智能 1.8，强化学习 0.56，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Bridging the Gap: Enabling Soft Actor Critic for High Performance Legged Locomotion》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RSL-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proximal Policy Optimization (PPO) has become the de facto standard for training legged robots, thanks to its robustness and scalability in massively parallel simulation environments like IsaacLab. However, its on-policy nature makes it inherently sample-inefficient, preventing its use for continuous adaptation and fine-tuning on real hardware. Soft Actor-Critic (SAC), by contrast, is an off-policy algorithm that can reuse past experience, making it a natural candidate for sim-to-real transfer workflows where the same algorithm can be used both in simulation and for online learning on the real robot. Despite these advantages, SAC has consistently failed to match PPO's empirical performance in massively parallel training settings. This work identifies the root causes of this gap and introduces targeted modifications, covering policy initialization, timeout-aware critic targets, and multi-step return estimation, that enable SAC to train stably at scale. Evaluated across multiple legged robot platforms and diverse locomotion tasks, our approach closes the performance gap with PPO entirely.

</details>

---

### [[20_Research/Papers/强化学习/HumanEgo_Zero-Shot_Robot_Learning_from_Minutes_of_Human_Egocentric_Videos|HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos]]

![[assets/2605.24934_figure.png|800]]

- **arXiv**: [2605.24934](https://arxiv.org/abs/2605.24934)
- **PDF**: https://arxiv.org/pdf/2605.24934
- **详细分析**: [[20_Research/Papers/强化学习/HumanEgo_Zero-Shot_Robot_Learning_from_Minutes_of_Human_Egocentric_Videos|HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos]]
- **作者**: Wang, Botao He, Kelin Yu, Seungjae Lee, Ruohan Gao, Furong Huang, Yiannis Aloimonos
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human egocentric video captures rich manipulation demonstrations without any robot hardware, yet transferring these skills to robots remains challenging due to the embodiment gap between human and robot in both visual appearance and kinematics. We present HumanEgo, a framework that bridges the embodiment gap by lifting each human demonstration to an entity-level representation of hand-object interaction, and training a flow matching policy with dense auxiliary objectives that amplify supervision from every trajectory. HumanEgo is robot-data-free, hardware-agnostic, data-efficient, and zero-shot human-to-robot transferable. With only 30 minutes of human videos per task, HumanEgo achieves 92.5% average success across four real-world tasks (75% with just 15 minutes), outperforms matched-time robot teleoperation by 41%, and robustly transfers zero-shot across novel robots, cameras, and environments.

</details>

---

### [[20_Research/Papers/强化学习/ProActor_Timing-Aware_Reinforcement_Learning_for_Proactive_Task_Scheduling_Agents|ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents]]

![[assets/2605.24900_figure.png|800]]

- **arXiv**: [2605.24900](https://arxiv.org/abs/2605.24900)
- **PDF**: https://arxiv.org/pdf/2605.24900
- **详细分析**: [[20_Research/Papers/强化学习/ProActor_Timing-Aware_Reinforcement_Learning_for_Proactive_Task_Scheduling_Agents|ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents]]
- **作者**: Lei Ding, Bin He, Chenguang Wang, Yang Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proactive task-oriented agents must autonomously anticipate user needs, identify actionable opportunities, and trigger software actions at appropriate moments - fundamentally shifting from reactive systems that await explicit instructions. However, existing approaches lack generalizable end-to-end solutions for measuring and optimizing such anticipatory behaviors. This paper introduces ProActor, a unified framework for conversational task scheduling that integrates: (1) a domain-agnostic automated annotation methodology that enables scalable proactiveness reinforcement learning (RL) by generating full opportunity time windows instead of rigid point labels, (2) systematic proactiveness metrics capturing both timing quality and reference action alignment, and (3) RL optimization using GRPO with various reward designs. Our insight is that RULER-based rewards with proactiveness rubrics are crucial for improving timing quality, and that proactiveness optimization enabled by stage-aware composite rewards is key to balancing timing quality and reference action alignment. Timing-aware RL requires extensive exploration, demanding efficient infrastructure. We develop ART-F, an adaptive framework combining request-adaptive inference clusters with DDP-based training on single-node multi-GPU systems, enabling LoRA training of 4-bit Qwen2.5-14B-ProActor-Q4 with 4-8x speedups. Experiments on two newly auto-annotated datasets demonstrate significant improvements in proactive timing while maintaining action consistency comparable to state-of-the-art (SOTA) baselines. Ablations validate the effectiveness of distinct composite reward variations.

</details>

---

### [[20_Research/Papers/大模型/CoRe-Code_Collaborative_Reinforcement_Learning_for_Code_Generation|CoRe-Code: Collaborative Reinforcement Learning for Code Generation]]

![[assets/2605.24812_figure.png|800]]

- **arXiv**: [2605.24812](https://arxiv.org/abs/2605.24812)
- **PDF**: https://arxiv.org/pdf/2605.24812
- **详细分析**: [[20_Research/Papers/大模型/CoRe-Code_Collaborative_Reinforcement_Learning_for_Code_Generation|CoRe-Code: Collaborative Reinforcement Learning for Code Generation]]
- **作者**: Zhihao Dou, Qinjian Zhao, Zhongwei Wan, Xiaoyu Xia, Sumon Biswas
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.3，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CoRe-Code: Collaborative Reinforcement Learning for Code Generation》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HumanEval, RECRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have achieved strong performance in code generation, but most methods rely on autoregressive decoding without global planning, often leading to locally coherent yet globally suboptimal solutions (e.g., failing test cases or inefficient complexity). While recent approaches such as Chain-of-Thought (CoT) and multi-agent systems (MAS) introduce planning, their limited role specialization and coordination hinder performance on complex tasks. To address the challenges of coordination and specialization in multi-agent code generation, we propose Collaborative Reinforcement Code (CoRe-Code), a framework for role specialized LLM agents that enhances inter-agent coordination to generate more accurate and efficient code. CoRe-Code adopts a simple Planner-Coder paradigm, where the Planner produces high-level plans and the Coder executes them to generate code. We further introduce a collaboration-aware reinforcement learning stage based on Group Relative Policy Optimization (GRPO) to enhance role specialization and alignment. Experiments show that CoRe-Code outperforms a wide range of existing RL-based and multi-agent methods. In addition, we demonstrate that CoRe-Code can generalize to other multi-agent frameworks (e.g., Retrieval and Debugging agents), highlighting its flexibility and scalability. We evaluate CoRe-Code on multiple benchmarks of varying difficulty using three base models. Compared to existing baselines, the results show consistent improvements in accuracy, while also achieving higher efficiency in terms of execution time and memory usage, demonstrating the effectiveness and practicality of CoRe-Code.

</details>

---

### [[20_Research/Papers/强化学习/Cross-Domain_Energy-Guided_Diffusion_Generation_for_Off-Dynamics_Reinforcement_Learning|Cross-Domain Energy-Guided Diffusion Generation for Off-Dynamics Reinforcement Learning]]

![[assets/2605.24810_figure.png|800]]

- **arXiv**: [2605.24810](https://arxiv.org/abs/2605.24810)
- **PDF**: https://arxiv.org/pdf/2605.24810
- **详细分析**: [[20_Research/Papers/强化学习/Cross-Domain_Energy-Guided_Diffusion_Generation_for_Off-Dynamics_Reinforcement_Learning|Cross-Domain Energy-Guided Diffusion Generation for Off-Dynamics Reinforcement Learning]]
- **作者**: Yu Yang, Yihong Guo, Anqi Liu, Pan Xu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Cross-Domain Energy-Guided Diffusion Generation for Off-Dynamics Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ODRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-dynamics offline reinforcement learning seeks to learn a target-domain policy from a large source dataset and a limited target dataset under mismatched transition dynamics. Existing approaches such as reward augmentation and data filtering are constrained to the source dataset and cannot synthesize new target behavior to improve coverage beyond the collected source trajectories. While recent model-based methods attempt to address this by learning target-aware dynamics, the generated experience is constructed only at the transition level, which leads to accumulated errors over long horizons. These limitations necessitate a shift toward trajectory-level generation for off-dynamics offline RL. We propose CEDGE, a Cross-domain Energy-guided Diffusion GEneration framework. CEDGE trains a trajectory diffusion model on source-domain trajectories and adapts the generated samples to the target domain through energy guidance. This guidance is derived by minimizing the distribution mismatch between the source and desired target-domain trajectories and is decomposed into return, domain, and behavior energy components. The resulting energy-guided trajectories are useful both for direct planning and as synthetic data for policy learning. Since target adaptation is achieved via energy guidance rather than retraining the diffusion model, CEDGE can be efficiently adapted to new target dynamics compared to previous methods. Experiments on the ODRL benchmark demonstrate that trajectory-level energy-guided generation improves diffusion planning under dynamics shifts and produces synthetic data that improves downstream target policy learning.

</details>

---

### [[20_Research/Papers/大模型/How_Many_Tools_Should_an_LLM_Agent_See_A_Chance-Corrected_Answer|How Many Tools Should an LLM Agent See? A Chance-Corrected Answer]]

![[assets/2605.24660_figure.png|800]]

- **arXiv**: [2605.24660](https://arxiv.org/abs/2605.24660)
- **PDF**: https://arxiv.org/pdf/2605.24660
- **详细分析**: [[20_Research/Papers/大模型/How_Many_Tools_Should_an_LLM_Agent_See_A_Chance-Corrected_Answer|How Many Tools Should an LLM Agent See? A Chance-Corrected Answer]]
- **作者**: Vyzantinos Repantis, Ameya Gawde, Harshvardhan Singh, Joey Blackwell II
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《How Many Tools Should an LLM Agent See? A Chance-Corrected Answer》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongFuncEval, ToolBench, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Before an LLM agent can use a tool, a retrieval system must decide which candidate tools to show to the agent. How long should that shortlist be? Show too many tools and the model struggles to choose. Show too few and the correct tool may not appear. Most systems apply a fixed shortlist size to every query, but no standard metric exists to evaluate whether that size was appropriate. We treat the number of tools shown to an LLM agent as the object of evaluation and we apply Bits-over-Random (BoR), a chance-corrected metric that asks whether success at a given depth is better than what random selection would achieve at that same depth. We evaluate BoR across three tool-selection benchmarks, multiple scorers, and registries ranging from 20 to 3,251 tools. We then turn the same principle into a reinforcement learning (RL) reward for choosing tool shortlist depth per query. The RL agent is deliberately simple, serving as a probe of the metric rather than a proposed system. As the shortlist grows, random chance of including the correct tool rises, so the reward naturally decreases, reducing the need for an engineered depth penalty. On BFCL (370 tools), the learned policy nearly matches the coverage of showing 50 tools ($90.3\%$ vs $90.8\%$) while presenting only 7 on average. On ToolBench (3,251 tools), a fixed shortlist of 5 tools achieves higher aggregate coverage ($64.7\%$ vs $61.9\%$) but finds nothing on hard queries (correct tool ranked 6th-20th). The BoR agent finds $16.7\%$ on those same queries by searching deeper. Downstream validation with Claude Sonnet 4.6 indicates that shorter adaptive lists also improve the LLM's ability to select the right tool: $93.1\%$ versus $87.1\%$ when always shown 5 tools, widening to $76.8\%$ vs $60.9\%$ on medium-difficulty queries where the correct tool is present but not ranked first.

</details>

---

### [[20_Research/Papers/大模型/Hera_Learning_Long-Horizon_Coordination_for_Device-Cloud_Collaborative_LLM_Agents|Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents]]

![[assets/2605.24598_figure.png|800]]

- **arXiv**: [2605.24598](https://arxiv.org/abs/2605.24598)
- **PDF**: https://arxiv.org/pdf/2605.24598
- **详细分析**: [[20_Research/Papers/大模型/Hera_Learning_Long-Horizon_Coordination_for_Device-Cloud_Collaborative_LLM_Agents|Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents]]
- **作者**: Yuxin Zhang, Mengxue Hu, Zheng Lin, Xiaoyi Fan, Fan Xie, Zihan Fang, Jing Yang, Wenjun Zhu, Zhiwen Chen, Chengfei Lv, Zhe Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.3（加权：大模型 1.1，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Hera: Learning Long-Horizon Coordination for Device-Cloud Collaborative LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents excel at solving complex long-horizon tasks through autonomous interaction with environments. However, their real-world deployment faces a fundamental device--cloud dilemma: on-device models are efficient but often brittle, while cloud models are stronger but costly in computation. State-of-the-art LLM device--cloud routers usually make coarse task-level decisions, which cannot adapt to the changing difficulty of multi-step agent interactions. To address this issue, we present Hera, a step-level device--cloud LLM agent coordinator for long-horizon tasks achieving a strong performance--cost Pareto frontier. Hera adopts a novel two-stage training paradigm: (1) imitation learning for cold-start, followed by (2) reinforcement learning that jointly optimizes task success and cloud usage efficiency. The first stage casts step-level routing as a supervised classification problem: the device agent is replayed on cloud trajectories, with each state labeled by the agreement between device and cloud actions. In the second stage, we perform cost-aware reinforcement learning by grouping identical states across trajectories and updating Hera with labels favoring higher expected return and fewer future cloud calls. We evaluate Hera on ALFWorld, WebShop, and AppWorld, where it consistently outperforms prior methods, achieving 92.5% of the cloud-only success rate with cloud use in only 46.3% of steps.

</details>

---

### [[20_Research/Papers/强化学习/Generative_OOD-regularized_Model-based_Policy_Optimization|Generative OOD-regularized Model-based Policy Optimization]]

![[assets/2605.24405_figure.png|800]]

- **arXiv**: [2605.24405](https://arxiv.org/abs/2605.24405)
- **PDF**: https://arxiv.org/pdf/2605.24405
- **详细分析**: [[20_Research/Papers/强化学习/Generative_OOD-regularized_Model-based_Policy_Optimization|Generative OOD-regularized Model-based Policy Optimization]]
- **作者**: Aysin Tumay, Jiahe Huang, Elise Jortberg, Rose Yu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Generative OOD-regularized Model-based Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL, OGSRL, SAMBO-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study sequential decision-making with offline reinforcement learning (RL). Traditional offline RL policies may result in out-of-distribution (OOD) actions when training relies only on sparse offline representations. To ensure safe offline policies in a sparse state-action space, we explore how density estimation models can be integrated into model-based RL methods to avoid the OOD regions. Generative models are capable of explicitly modeling the density in sparse state-action spaces. Building on this, we introduce Generative OOD-regularized Model-based Policy Optimization (GORMPO), a density-regularized offline RL algorithm that uses generative density modeling to restrict policy updates to high-density areas of the dataset. Furthermore, we examine whether better OOD detection corresponds to better model-based offline policies. We compare (1) the OOD detection capabilities of various density estimators and (2) their performance within the GORMPO framework on a real-world medical dataset and sparse offline RL datasets. We theoretically guarantee GORMPO's performance under mild assumptions. Empirically, GORMPO outperforms state-of-the-art baselines by 17% on a real-world medical dataset and enhances the base model on the offline RL datasets. Our empirical findings show that better OOD detection generally results in improved policies in environments with stable dynamics, while conservative penalties with poor density estimation are favored when dynamics are uncertain.

</details>

---

### [[20_Research/Papers/大模型/Agent-ToM_Learning_to_Monitor_Autonomous_LLM_Agents_via_Theory-of-Mind_Reasoning|Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning]]

![[assets/2605.24216_figure.png|800]]

- **arXiv**: [2605.24216](https://arxiv.org/abs/2605.24216)
- **PDF**: https://arxiv.org/pdf/2605.24216
- **详细分析**: [[20_Research/Papers/大模型/Agent-ToM_Learning_to_Monitor_Autonomous_LLM_Agents_via_Theory-of-Mind_Reasoning|Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning]]
- **作者**: Nesreen K. Ahmed, Nima Nafisi
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.55（加权：大模型 1.55）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monitoring autonomous large language model (LLM) agents for covert malicious behavior is challenging due to delayed, context-dependent, and long-horizon attack patterns. Agents may pursue hidden objectives while maintaining superficially benign behavior, making detection difficult even with full trajectory access. Prior monitoring approaches improve scaffolding or ensemble aggregation, but treat each trajectory independently and do not learn from prior monitoring experience. Moreover, standard reasoning methods explain observed behavior without explicitly reasoning about agent beliefs, intentions, and goal alignment required to distinguish benign task execution from covert deviation. We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents. Agent-ToM performs structured full-trajectory analysis by inferring beliefs, intent hypotheses with calibrated confidence, expected actions, and deviations from task-consistent behavioral baselines. At inference time, it employs a \textit{Reason-Verify-Refine} pipeline to construct and validate monitoring decisions. At training time, Agent-ToM distills critique signals into a persistent \textit{semantic guardrail memory}, enabling reusable belief- and intent-conditioned constraints across episodes. We evaluate Agent-ToM on adversarial agent monitoring benchmarks (SHADE-Arena and CUA-SHADE-Arena). Agent-ToM achieves strong precision-recall balance and outperforms state-of-the-art monitoring baselines, including ensemble methods, while using a coherent two-call reasoning pipeline. These results demonstrate that learning at the monitoring layer, combined with structured ToM reasoning and verification, provides an effective and deployable foundation for securing autonomous LLM agents.

</details>

---

### [[20_Research/Papers/大模型/When_Does_Multi-Agent_RL_Improve_LLM_Workflows_Workflow,_Scale,_and_Policy-Sharing_Tradeoffs|When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs]]

![[assets/2605.24202_figure.png|800]]

- **arXiv**: [2605.24202](https://arxiv.org/abs/2605.24202)
- **PDF**: https://arxiv.org/pdf/2605.24202
- **详细分析**: [[20_Research/Papers/大模型/When_Does_Multi-Agent_RL_Improve_LLM_Workflows_Workflow,_Scale,_and_Policy-Sharing_Tradeoffs|When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs]]
- **作者**: Yifan Zeng, Yiran Wu, Yaolun Zhang, Wentian Zhao, Kun Wan, Qingyun Wu, Huazheng Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.9，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MA-RL, SA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM workflows route inference through specialized roles to lift end-task accuracy, but jointly training those roles with reinforcement learning is unstable in ways that are poorly understood. We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters. Our experimental matrix spans Eval-Opt, Voting, and Orch-Workers workflows, math and code tasks, and three model scales (0.6B, 1.7B, 4B). We find that multi-agent RL usually improves over base models, but gains depend jointly on workflow, task, and scale, not on policy sharing alone. Isolated-Policy tends to reach higher peak accuracy yet more often falls off a terminal accuracy cliff, while Shared-Policy training does not eliminate failure; it redistributes failure into qualitatively different patterns. We then explain the strongest of these patterns through role-level gradient dynamics induced by workflow topology and policy routing: under Isolated-Policy, parallel same-role agents on shared prompts amplify per-role gradients and drive terminal degradation in Voting and Orch-Workers workflows; under Shared-Policy, asymmetric per-step gradient mass causes the shared policy to be captured by the dominant role, producing different failure signatures by task and workflow. Together, the empirical map and its underlying mechanisms show that policy sharing routes training pressure through different channels rather than offering uniform stability, making it a design choice with workflow- and task-conditional tradeoffs.

</details>

---

### [[20_Research/Papers/具身智能/ActQuant_Sub-4-bit_Action-Guided_Quantization_for_Vision-Language-Action_Models|ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models]]

![[assets/2605.24011_figure.png|800]]

- **arXiv**: [2605.24011](https://arxiv.org/abs/2605.24011)
- **PDF**: https://arxiv.org/pdf/2605.24011
- **详细分析**: [[20_Research/Papers/具身智能/ActQuant_Sub-4-bit_Action-Guided_Quantization_for_Vision-Language-Action_Models|ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models]]
- **作者**: Arash Akbari, Arman Akbari, Masih Eskandar, Qitao Tan, Yixiao Chen, Jingwu Luo, Bertha Pangaribuan, Liyun Zhang, Jennifer Dy, Geng Yuan, Xue Lin, Gaowen Liu...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.8，大模型 0.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BitVLA, OpenVLA, QVLA, QuantVLA, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models exhibit remarkable action generation for embodied intelligence, but their heavy compute make deployment on edge platforms impractical. Aggressive, sub-4-bit weight quantization is the natural solution, yet existing post-training quantization (PTQ) methods suffer severe performance degradation in this regime. To address this, we introduce ActQuant, an action-guided mixed-precision PTQ framework that operates in two stages: (1) an inter-tensor bit allocator that assigns each weight matrix a single bit-width based on how much it contributes to predicting the agent's actions; (2) an intra-tensor scale optimizer tunes per-block quantization scales using action-aware curvature, so that dynamic range is concentrated on the weights most influential for control. To deliver the on-device benefits of our aggressive quantization, we further introduce this http URL , an agentic conversion pipeline that ports architectures into a native C/C++ runtime with efficient low-bit kernels. We evaluate ActQuant both in simulation and on a real-world 6-DoF UR3 arm, with all models deployed through this http URL . On the LIBERO benchmark, ActQuant is the only method that operates at or below 3 bits-per-weight, retaining 95.0% on OpenVLA-OFT and 94.8% on $\pi_{0.5}$. Pushed further, ActQuant reaches 2.5 bpw at 90.1% on OpenVLA-OFT, compressing the backbone from 14.3 GB to 2.7 GB (5.3$\times$). On the physical UR3 arm, $\pi_{0.5}$ quantized with ActQuant retains the baseline's success rate while reducing the memory footprint by 2.5$\times$.

</details>

---

### [[20_Research/Papers/大模型/Reason--Imagine--Act_Closed-Loop_LLM_Decision_Making_with_World_Models_for_Autonomous_Driving|Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving]]

![[assets/2605.24004_figure.png|800]]

- **arXiv**: [2605.24004](https://arxiv.org/abs/2605.24004)
- **PDF**: https://arxiv.org/pdf/2605.24004
- **详细分析**: [[20_Research/Papers/大模型/Reason--Imagine--Act_Closed-Loop_LLM_Decision_Making_with_World_Models_for_Autonomous_Driving|Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving]]
- **作者**: Zhengqi Sun, Yiwen Sun, Boxuan Liu, Tailai Chen, Tianxu Guo, Jiabin Liu
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 0.16，世界模型 1.16）
- **关联关键词**: LLM, WorldModel

#### 研究背景与动机

《Reason--Imagine--Act: Closed-Loop LLM Decision Making with World Models for Autonomous Driving》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are promising for autonomous driving, but semantics-only decision policies can yield physically unsafe behavior in dynamic traffic. Existing methods either perform online language reasoning without explicit dynamics verification or use world models mainly in offline pipelines, leaving a gap between semantic intent and physical feasibility at decision time. We propose Reason--Imagine--Act (RIA), a closed-loop framework that couples an LLM reasoner with an action-conditioned world model for online safety verification. At each step, the LLM proposes an action template and candidate sub-actions, the world model performs short-horizon rollouts, and a safety scorer selects the safest executable action with feedback to the next reasoning step. Under a unified CARLA point-goal protocol (1000 episodes), RIA achieves 80.05% route completion, 51.10% arrival rate, and 0.20% collision rate. Under the same closed-loop interface, RIA consistently outperforms training-free baselines, including CARLA TM and MADA, on core closed-loop metrics. For reproducibility, code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/IVR-R1_Refining_Trajectories_through_Iterative_Visual-Grounded_Reasoning_in_Reinforcement_Learning|IVR-R1: Refining Trajectories through Iterative Visual-Grounded Reasoning in Reinforcement Learning]]

![[assets/2605.23997_figure.png|800]]

- **arXiv**: [2605.23997](https://arxiv.org/abs/2605.23997)
- **PDF**: https://arxiv.org/pdf/2605.23997
- **详细分析**: [[20_Research/Papers/大模型/IVR-R1_Refining_Trajectories_through_Iterative_Visual-Grounded_Reasoning_in_Reinforcement_Learning|IVR-R1: Refining Trajectories through Iterative Visual-Grounded Reasoning in Reinforcement Learning]]
- **作者**: Chenghao Li, Fusheng Hao, Xikai Zhang, Likang Xiao, Yanwei Ren, Fuxiang Wu, Quan Chen, Liu Liu
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《IVR-R1: Refining Trajectories through Iterative Visual-Grounded Reasoning in Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models via reinforcement learning (RL) have demonstrated remarkable capabilities in complex visual reasoning tasks, yet they remain limited in long-horizon multimodal scenarios, often suffering from visual hallucination and logical error. Current methods typically pre-encode high-dimensional visual scenes into discrete textual proxies to facilitate downstream reasoning. As the reasoning chain unfolds, however, the inherent information asymmetry between text and visual scenes tends to erode visual grounding, resulting in misguided reasoning and erroneous outputs. To address this issue, we introduce IVR-R1 (Iterative Visual-grounded Reasoning), a novel RL training framework that facilitates dynamic visual re-alignment that actively rectifies reasoning trajectories to guide policy optimization. Specifically, by leveraging a reward-driven screening mechanism to identify flawed rollouts, IVR-R1 executes a fine-grained, step-level error attribution within the multimodal context. By iteratively cross-referencing intermediate reasoning states against pristine visual priors, a Re-Reasoning Loop enables automated trajectory rectification, effectively synthesizing expert-level demonstrations that serve as high-fidelity reasoning templates for the policy model. Our experiments across diverse multimodal benchmarks demonstrate that IVR-R1 consistently outperforms existing reinforcement learning methods, establishing a superior paradigm for maintaining logical and visual consistency in complex multimodal reasoning.

</details>

---

### [[20_Research/Papers/世界模型/Nano_World_Models_A_Minimalist_Implementation_of_Future_Video_Prediction|Nano World Models: A Minimalist Implementation of Future Video Prediction]]

![[assets/2605.23993_figure.png|800]]

- **arXiv**: [2605.23993](https://arxiv.org/abs/2605.23993)
- **PDF**: https://arxiv.org/pdf/2605.23993
- **详细分析**: [[20_Research/Papers/世界模型/Nano_World_Models_A_Minimalist_Implementation_of_Future_Video_Prediction|Nano World Models: A Minimalist Implementation of Future Video Prediction]]
- **作者**: Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Omar Chehab, Fernando Moreno-Pino, Max Simchowitz
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 0.96，机器人 0.2）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Nano World Models: A Minimalist Implementation of Future Video Prediction》归入 世界模型、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have become a central paradigm for learning predictive simulators that support generation, planning, and decision-making. Yet, despite rapid progress in industry-scale interactive video generation, the broader research community still lacks compact, reproducible, and easily extensible implementations for studying the design choices underlying modern world models. We introduce Nano World Models, a minimalist codebase for future video prediction centered around diffusion forcing. Nano World Models provides a unified interface for generative objectives, model scales, action-conditioning mechanisms, latent observation spaces, datasets, evaluation protocols, and long-horizon rollout procedures. This design enables controlled studies of world-modeling components that are often entangled across separate implementations. Through experiments across simple control environments, game simulation, and real-robot data, we examine how prediction parameterization, architecture scale, action injection, sampling budget, and domain complexity affect video prediction quality and autoregressive rollout behavior. By releasing code, configurations, evaluation scripts, and pretrained checkpoints, Nano World Models aims to provide a compact yet extensible experimental substrate for open, reproducible, and scientific world-model research.

</details>

---

### [[20_Research/Papers/机器人/Beyond_Predefined_Learning_Objects_A_Thinking-Learning_Interaction_Model_for_Up-to-Date_Autonomous_Robot_Learning|Beyond Predefined Learning Objects: A Thinking-Learning Interaction Model for Up-to-Date Autonomous Robot Learning]]

![[assets/2605.23987_figure.png|800]]

- **arXiv**: [2605.23987](https://arxiv.org/abs/2605.23987)
- **PDF**: https://arxiv.org/pdf/2605.23987
- **详细分析**: [[20_Research/Papers/机器人/Beyond_Predefined_Learning_Objects_A_Thinking-Learning_Interaction_Model_for_Up-to-Date_Autonomous_Robot_Learning|Beyond Predefined Learning Objects: A Thinking-Learning Interaction Model for Up-to-Date Autonomous Robot Learning]]
- **作者**: Hong Su
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Beyond Predefined Learning Objects: A Thinking-Learning Interaction Model for Up-to-Date Autonomous Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots operating in open and changing environments cannot always rely on predefined inputs, outputs, and action routines. Although existing learning methods enable robots to improve their performance through environmental interaction, the objects of learning are often fixed in advance, such as input features, recognition outputs, network structures, task goals, or action sequences. This limits their ability to adapt when new features, new categories, or more efficient task routines appear during long-term operation. To address this problem, this paper proposes a thinking-learning interaction model for autonomous robots. The core idea is that thinking guides learning by identifying potential changes, selecting useful evidence, organizing training materials, and planning verification actions, while learning promotes thinking by updating task knowledge, feature-selection experience, action strategies, and future reasoning processes. Based on this bidirectional mechanism, the robot can gradually move beyond predefined learning settings and adapt its recognition relations and action relations through continuous interaction with the environment. Specifically, the proposed model supports adaptive input feature discovery, output category expansion, learning model update, and action routine reconstruction. Experimental results show that the proposed model improves the final recognition accuracy from 0.419 to 0.845 in feature adaptation, achieves higher new-category formation accuracy and model-update success rate, and reduces the average action length from 13.0 to 4.0 in action routine reconstruction. In learning-enhanced thinking, the useful evidence selection rate increases from 0.272 to 0.965, indicating that learning results can effectively improve future evidence selection and reasoning.

</details>

---

### [[20_Research/Papers/大模型/Why_We_Need_World_Models_for_AGI_Where_LLMs_Fail_and_How_World_Models_May_Outperform|Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform]]

![[assets/2605.23972_figure.png|800]]

- **arXiv**: [2605.23972](https://arxiv.org/abs/2605.23972)
- **PDF**: https://arxiv.org/pdf/2605.23972
- **详细分析**: [[20_Research/Papers/大模型/Why_We_Need_World_Models_for_AGI_Where_LLMs_Fail_and_How_World_Models_May_Outperform|Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform]]
- **作者**: Feisal Alaswad, Batoul Aljaddouh, Maher Alrahhal, Poovammal E, Talal Bonny
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.15（加权：大模型 0.35，世界模型 0.8）
- **关联关键词**: Multimodal, Agent, WorldModel

#### 研究背景与动机

《Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FLUX-RL, PlaNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models achieve strong performance in language generation and knowledge-intensive tasks, yet remain limited in settings requiring causal reasoning, persistent state tracking, and long-horizon planning. We argue that these limitations may arise from an objective-level mismatch between sequence prediction and reasoning over latent environment dynamics. To formalize this distinction, we introduce Latent Dynamics Inference (LDI), a conceptual perspective that interprets language and multimodal observations as partial evidence of underlying transition dynamics. To empirically investigate this perspective, we introduce Flux, a sequential reasoning environment specified entirely through natural-language rules. As a proof-of-concept case study, the rules are first compiled into an explicit state-transition simulator, illustrating that structured latent transition dynamics can, in some cases, be operationally extracted from textual rule descriptions. This enables a controlled comparison between the LLMs operating purely over textual observations and reinforcement-learning agents trained directly within the extracted latent state space. Within this case study, agents operating with explicit access to the latent state space exhibit substantially more stable behavior in long-horizon gameplay, achieving an aggregate win rate of approximately 79% versus 11% for LLMs. Qualitative analysis further reveals failure modes consistent with unstable persistent state tracking, including invalid actions, state-tracking errors, and short-horizon reasoning failures. The complete implementation of the Flux environment available at this https URL Within the evaluated setting, these results suggest that strong sequence prediction alone may struggle to support robust long-horizon dynamic reasoning without mechanisms for persistent state tracking and transition modeling

</details>

---

### [[20_Research/Papers/大模型/MEMOR-E_In-Context_and_Fine-Tuned_LLM_Personalization_for_Alzheimer's_Assistive_Robotics|MEMOR-E: In-Context and Fine-Tuned LLM Personalization for Alzheimer's Assistive Robotics]]

![[assets/2605.23941_figure.png|800]]

- **arXiv**: [2605.23941](https://arxiv.org/abs/2605.23941)
- **PDF**: https://arxiv.org/pdf/2605.23941
- **详细分析**: [[20_Research/Papers/大模型/MEMOR-E_In-Context_and_Fine-Tuned_LLM_Personalization_for_Alzheimer's_Assistive_Robotics|MEMOR-E: In-Context and Fine-Tuned LLM Personalization for Alzheimer's Assistive Robotics]]
- **作者**: Maissa Abir Smaili, Eren Sadikoglu, Ransalu Senanayake
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.6，大模型 0.4，机器人 1.5）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《MEMOR-E: In-Context and Fine-Tuned LLM Personalization for Alzheimer's Assistive Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Alzheimer's disease is a neurodegenerative disorder marked by progressive declines in memory and language that reduce independence in daily life, motivating socially assistive robotic support. This paper presents MEMOR-E, a mobile quadruped robot with an interactive tablet interface that assists patients and caregivers through medication reminders, routine guidance, memory oriented interactions, and companionship. We evaluated the feasibility of fine tuning large language models (LLMs) to emulate stage consistent cognitive behavior and interpret responses across standard neuropsychological language tasks, using audio transcriptions from 235 Alzheimer's patients and synthetically generated healthy controls. We also report findings on using in context learning (ICL) in LLMs, where a second LLM produced domain and severity level cognitive error summaries. Our results show that MEMOR-E can generate stage aware, non diagnostic cognitive summaries that support personalized assistive interactions, while explainable AI mechanisms translate model outputs into transparent, human readable evidence to enable caregiver oversight and trustworthy human robot interaction.

</details>

---
