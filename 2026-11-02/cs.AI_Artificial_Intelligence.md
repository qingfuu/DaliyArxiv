# cs.AI | Artificial Intelligence | 2026-11-02

#arxiv #ComputerScience

**论文数**: 24

### [[20_Research/Papers/具身智能/Hierarchical_World_Models_with_Implicit_Dynamics|Hierarchical World Models with Implicit Dynamics]]

![[assets/2610.42146_figure.png|800]]

- **arXiv**: [2610.42146](https://arxiv.org/abs/2610.42146)
- **PDF**: https://arxiv.org/pdf/2610.42146
- **详细分析**: [[20_Research/Papers/具身智能/Hierarchical_World_Models_with_Implicit_Dynamics|Hierarchical World Models with Implicit Dynamics]]
- **作者**: Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，世界模型 1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Hierarchical World Models with Implicit Dynamics》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning with world models enables test-time adaptation for embodied agents, offering superior generalization over direct policy learning. However, long-horizon tasks remain hindered by cumulative errors and search complexity. Existing hierarchical methods often use rigid macro-actions or latent skills, leading to brittle representations and limited fine-grained control. We introduce ID-WM (Implicit Dynamics World Models), a hierarchical world model that decouples state-space reachability from local control. Our framework utilizes a high-level model to sample feasible transitions across the state manifold and a low-level world model as an inverse dynamics solver to ground these transitions into precise actions. This allows the planner to identify reachable subgoals without being constrained by low-level execution details. By prioritizing local physical feasibility over global behavioral patterns, ID-WM synthesizes novel long-horizon plans from short segments, transcending the specific behavioral modes seen during training. We demonstrate its effectiveness across three navigation and manipulation suites, achieving a 38.5% improvement over state-of-the-art policy and diffusion-based planners. Crucially, by leveraging this hierarchical structure to mitigate compounding errors, our approach yields a 135% performance gain over single-level world model MPC, particularly in complex, unseen configurations for long-horizon tasks. Videos can be viewed at https://id-wm.github.io

</details>

---

### [[20_Research/Papers/具身智能/RoboArchitect_Automating_the_Design_of_Robotic_Agents_with_Persistent_Memory|RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory]]

![[assets/2610.42141_figure.png|800]]

- **arXiv**: [2610.42141](https://arxiv.org/abs/2610.42141)
- **PDF**: https://arxiv.org/pdf/2610.42141
- **详细分析**: [[20_Research/Papers/具身智能/RoboArchitect_Automating_the_Design_of_Robotic_Agents_with_Persistent_Memory|RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory]]
- **作者**: Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu, Serena Yeung-Levy
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.6，大模型 0.4，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA, VLABench, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises the harness around the frozen policy. The harness evolves on a set of episodes for its optimization and is evaluated on held-out scenes and tasks. Without updating any model weights, RoboArchitect raises average success from 9.7% to 43.3% on unseen scenes (4.5x) and from 12.7% to 40.2% on unseen tasks (3.2x), across multiple benchmarks and policies. The gains are largest where the benchmark is far from the policy's training data: wrapping a general-purpose policy, the evolved harness yields a specialist that often outperforms even the finetuned version. Intuitive control strategies are automatically designed, such as lifting a jammed arm clear or reaching in horizontally when an obstacle blocks the way from above. The harness also evolves its own persistent memory, carrying learned experience, such as effective grasp depths, into later decisions. These results suggest that substantial headroom in robotic manipulation lies in the agent harness, and its design can be effectively automated and optimized without weight updates.

</details>

---

### [[20_Research/Papers/大模型/TradeWar_A_Benchmark_for_Execution-Grounded_Trade_Negotiation_with_Adaptive_LLM_Agents|TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents]]

![[assets/2610.42004_figure.png|800]]

- **arXiv**: [2610.42004](https://arxiv.org/abs/2610.42004)
- **PDF**: https://arxiv.org/pdf/2610.42004
- **详细分析**: [[20_Research/Papers/大模型/TradeWar_A_Benchmark_for_Execution-Grounded_Trade_Negotiation_with_Adaptive_LLM_Agents|TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents]]
- **作者**: Xiangyu Kong, Ruirui Yang, Xia Hou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoffeeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-turn negotiation remains a challenging problem for large language model (LLM) agents. While LLMs can conduct natural-language dialogue, existing benchmarks predominantly assess only agreement rates, overlooking whether negotiated commitments actually create value once executed. To address this gap, we introduce TradeWar, a multi-country simulation benchmark that translates negotiation dialogues into concrete tariff and trade-share policies, enforces capacity and network constraints during settlement, and evaluates outcomes via an Economic Health Index (EHI). To solve this execution-grounded task, we propose TACTIC (Trade-aware Adaptive Consolidation and Theory-of-mind for International Commerce), an agent that iteratively refines its negotiation strategy across episodes-without updating base LLM weights-by leveraging prior experience, opponent behavior, and past settlement outcomes. Despite using zero-shot chain-of-thought (CoT) prompting, PromptLLM attains a 75% agreement rate but only 57.1 final EHI (*100), whereas TACTIC reaches 68.8. Across 20 sequential episodes and three seeds, TACTIC's final EHI improves from 58.2 to 73.2, compared with 65.2 for an ablation without cross-episode updates. Under technology-controls and energy-crisis shocks, TACTIC also exhibits smaller performance degradation than PromptLLM and MemoryLLM. These results indicate that CoT deliberation and interaction memory alone do not fully address delayed execution feedback, whereas settlement-grounded adaptation improves long-horizon negotiation in TradeWar.

</details>

---

### [[20_Research/Papers/强化学习/Optimizing_Stochastic_Policy_Geometry_for_Few-Step_Flow_Reinforcement_Learning|Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning]]

![[assets/2610.41949_figure.png|800]]

- **arXiv**: [2610.41949](https://arxiv.org/abs/2610.41949)
- **PDF**: https://arxiv.org/pdf/2610.41949
- **详细分析**: [[20_Research/Papers/强化学习/Optimizing_Stochastic_Policy_Geometry_for_Few-Step_Flow_Reinforcement_Learning|Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning]]
- **作者**: Zhuguanyu Wu, Congjia Chen, Ruihao Gong, Yang Yong, Shiqiao Gu, Yi Xu, Xianglong Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Geo-FSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Few-step flow models generate samples through a handful of large denoising transitions. Applying GRPO to such models requires introducing stochasticity into the denoising transitions, and when a single transition spans a wide range of noise levels, the choice of the resulting stochastic policy becomes a major factor in optimization. Recent constructions constrain the policy to preserve the target flow coefficients, but this constraint admits a family of policies and offers no criterion for choosing among them. We introduce Geo-FSRL (Geometry-Optimized Few-Step Reinforcement Learning), built on a selection principle: at a fixed conditioning state and timestep pair, choose the admissible policy that minimizes the conditional KL divergence induced by any given nonzero velocity-output update. Within a coefficient-preserving family of isotropic Gaussian transitions, this criterion reduces to minimizing a single scalar geometry factor that determines the conditional KL for every velocity-output update. The same factor governs velocity-space Fisher information and conditional transition log-likelihood-ratio variance. We derive the unique closed-form optimizer within this family, shared across all nonzero update magnitudes and directions, with transition coefficients determined by both the source and target noise levels. Because the minimized geometry factor still varies across timesteps, we further adopt gradient-scale matching from prior work and derive closed-form policy-gradient and KL weights that normalize explicit score scales and reference-KL curvature. Geo-FSRL trains on the original few-step schedule and retains the deterministic solver at inference. Our method achieves higher final reward scores than Flow-GRPO and Flow-CPS on both image generation and video generation models under the 4-step setting. Code is available at https://github.com/ModelTC/LightX2V/tree/main/lightx2v_rl

</details>

---

### [[20_Research/Papers/具身智能/Sensorium_An_Open-Source_Multimodal_Data_Collection_and_Curation_Library_for_Embodied_Surgical_AI|Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI]]

![[assets/2610.41946_figure.png|800]]

- **arXiv**: [2610.41946](https://arxiv.org/abs/2610.41946)
- **PDF**: https://arxiv.org/pdf/2610.41946
- **详细分析**: [[20_Research/Papers/具身智能/Sensorium_An_Open-Source_Multimodal_Data_Collection_and_Curation_Library_for_Embodied_Surgical_AI|Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI]]
- **作者**: Lorenzo Mazza, Ariel Rodriguez, Stefanie Speidel
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Sensorium: An Open-Source Multimodal Data Collection and Curation Library for Embodied Surgical AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied surgical AI requires reliable multimodal data, yet surgical data collection remains costly, difficult to repeat, and strongly dependent on the hardware setup. We present Sensorium, an open-source Python library for recording, processing, annotating, and curating multimodal surgical data from configurable robot and sensor streams using the Robot Operating System (ROS) and ROS2 middleware. The library combines operator-facing data acquisition, configurable processing, semantic annotation, and episodic dataset generation. We evaluate Sensorium across 1516 recordings of phantom, ex vivo, and in vivo porcine experiments involving multiple surgical tasks and sensing configurations, and report preliminary usability feedback.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_In-Context_Learning_with_Explicit_Rule_Induction|Multimodal In-Context Learning with Explicit Rule Induction]]

![[assets/2610.41754_figure.png|800]]

- **arXiv**: [2610.41754](https://arxiv.org/abs/2610.41754)
- **PDF**: https://arxiv.org/pdf/2610.41754
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_In-Context_Learning_with_Explicit_Rule_Induction|Multimodal In-Context Learning with Explicit Rule Induction]]
- **作者**: Yuquan Li, Xinyang Jiang, Yuhao Xue, Cairong Zhao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Multimodal In-Context Learning with Explicit Rule Induction》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IconQA, OCR-VQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A central challenge in multimodal in-context learning (MICL) arises from tasks that are ill-defined without context and require uncovering the underlying rules from demonstrations. Existing methods predominantly treat MICL as direct input-output mapping, overlooking the importance of explicitly inducing and reasoning over such rules, limiting both performance and interpretability. We propose ERIM, Explicit Rule-Induction for Multimodal In-Context Learning, a unified framework that enhances MICL by explicitly inducing the latent rules governing demonstration samples. Leveraging the reasoning ability of multi-modal large language model (MLLM), ERIM constructs rule-centric MICL datasets, introduces explicit supervision for rule induction, and fine-tunes MLLM to perform explicit rule-induction via a two-stage training strategy that combines mixed cold-start supervised fine-tuning with reinforcement learning. Extensive experiments show consistent performance improvements across diverse MICL settings and demonstrate that correctly inducing underlying rules directly leads to stronger and more stable performance.

</details>

---

### [[20_Research/Papers/强化学习/TSBPO_Tree-Structured_Branching_for_Policy_Optimization_in_Interactive_Language_Agents|TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents]]

![[assets/2610.41697_first_page.png|800]]

- **arXiv**: [2610.41697](https://arxiv.org/abs/2610.41697)
- **PDF**: https://arxiv.org/pdf/2610.41697
- **详细分析**: [[20_Research/Papers/强化学习/TSBPO_Tree-Structured_Branching_for_Policy_Optimization_in_Interactive_Language_Agents|TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents]]
- **作者**: Rui Yu, Chong Mu, Jinchuan Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.55，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training interactive language agents from terminal outcomes poses three coupled problems: which task and state continuations to sample, how to assign delayed feedback to decisions, and how to aggregate token losses for multi-token actions. We present TSBPO, a tree-structured sampling-to-update paradigm that addresses these problems within one training loop. A likelihood-fitted Root/Branch allocator uses retained task and state evidence to target continuations likely to produce contrasting terminal outcomes under fixed rollout budgets. On the resulting replayed physical trees, trajectory advantages compare immediate sibling segments, while observation-group step advantages compare outcomes at matched task/observation states. The actor then sums clipped token surrogates over each complete response and normalizes across active turns, avoiding response-length averaging in the policy-gradient term. With a Qwen2.5-1.5B actor, fixed checkpoints obtain 97.79% seen and 96.64% unseen stochastic success on ALFWorld and an 81.07% per-episode success rate over six stochastic episodes for each of the 500 WebShop test goals. A WebShop step-term ablation yields 75.93% at the same update-100 evaluation; an ALFWorld aggregation comparison shows higher observed command validity with complete-turn weighting. These results support the evaluated training configuration on two interactive benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/When_the_Past_Shapes_Action_Understanding_Embodied_Memory|When the Past Shapes Action: Understanding Embodied Memory]]

![[assets/2610.41688_figure.png|800]]

- **arXiv**: [2610.41688](https://arxiv.org/abs/2610.41688)
- **PDF**: https://arxiv.org/pdf/2610.41688
- **详细分析**: [[20_Research/Papers/具身智能/When_the_Past_Shapes_Action_Understanding_Embodied_Memory|When the Past Shapes Action: Understanding Embodied Memory]]
- **作者**: Siqi Li, Ziyi Bai, Xinrun Xu, Tinglei Huang, Börje F. Karlsson
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《When the Past Shapes Action: Understanding Embodied Memory》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EMem-Bench, OpenVLA, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in generative foundation models have expanded the capabilities of embodied AI, enabling increasingly general navigation, manipulation, and long-horizon task execution. However, effective interaction with dynamic environments requires more than only strong perception and reasoning: agents must act with partial knowledge and retain, retrieve, and update information from past observations, actions, and experiences. This survey examines embodied memory as a mechanism for preserving decision-relevant information beyond the current observation. We organize existing approaches along two complementary dimensions: six fundamental memory requirements, spanning world-state persistence, task progress, belief maintenance, and experiential learning; and eight architectural categories, including recurrent states, fast weights, visual and symbolic representations, spatial memory, and experience-based systems. We analyze their capabilities and limitations, and examine how existing benchmarks evaluate memory-dependent behavior, distinguishing genuine use of historical information from general task performance. Finally, we identify open challenges in selecting relevant experiences, maintaining consistent beliefs in changing environments, and consolidating knowledge across episodes. Our analysis provides a framework for understanding memory as an essential component of reliable, adaptive, and lifelong-horizon embodied intelligence.

</details>

---

### [[20_Research/Papers/强化学习/Risk-Sensitive_Mission_Planning_for_Multi-Target_On-Orbit_Inspection_via_Distributional_Reinforcement_Learning|Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning]]

![[assets/2610.41647_first_page.png|800]]

- **arXiv**: [2610.41647](https://arxiv.org/abs/2610.41647)
- **PDF**: https://arxiv.org/pdf/2610.41647
- **详细分析**: [[20_Research/Papers/强化学习/Risk-Sensitive_Mission_Planning_for_Multi-Target_On-Orbit_Inspection_via_Distributional_Reinforcement_Learning|Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning]]
- **作者**: Adam Abdin
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-target on-orbit servicing missions require planning tools that can adapt to evolving operational conditions while accounting for the outcome variability inherent to safety-critical spaceflight. This paper presents an adaptive planning approach for multi-target servicing campaigns in low Earth orbit and applies it to inspection missions flown by a low-thrust servicer. The approach is based on Distributional Reinforcement Learning, which learns the full distribution of mission returns and thereby supports explicit risk-sensitive decision-making at each planning step. Specifically, a Quantile-Regression Deep Q-Network (QR-DQN) agent selects which target to inspect next by jointly considering the expectation and the variance of the predicted return through a mean-variance criterion. The mission environment models circular orbits with a spread in inclination and uses Edelbaum's combined-manoeuvre low-thrust transfer estimates. The observation comprises the orbital elements, the visit history, the observed risk state of each target and the remaining mission-time budget. The risk state of each target changes stochastically during the campaign, making the outcome of an inspection uncertain and creating operationally meaningful distinctions between risk-neutral and risk-averse planning strategies. Because the mission-time budget generally admits only a subset of the candidate targets, the planner must also select which targets to inspect. Numerical experiments on scenarios with five target satellites show that one risk-aversion weight moves the policy across a range of mean return and return variance, over an unchanged environment and reward. Risk-averse agents reduce the variance of the episodic return by approximately one half relative to risk-neutral agents and lower the probability of a mission loss, at a cost in mean return. To validate the learned policies, the efficient frontier, which gives the highest mean return attainable at each level of return variance, is computed exactly by enumerating the admissible visit orders. At equal variance, the learned policies lie close to this frontier in mean return, and the risk-averse policies have a lower probability of a mission loss than the frontier policies.

</details>

---

### [[20_Research/Papers/具身智能/VLA_Policies_Do_Not_Know_When_Not_to_Act_Unintended_Task_Execution_and_Start_Suppression|VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression]]

![[assets/2610.41609_first_page.png|800]]

- **arXiv**: [2610.41609](https://arxiv.org/abs/2610.41609)
- **PDF**: https://arxiv.org/pdf/2610.41609
- **详细分析**: [[20_Research/Papers/具身智能/VLA_Policies_Do_Not_Know_When_Not_to_Act_Unintended_Task_Execution_and_Start_Suppression|VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression]]
- **作者**: Minsu Jang, Jae-Woo Choi, Youngwoo Yoon, Dohyung Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ICBench, OpenVLA, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot should act only on an instruction from a person or on an intent that the robot explicitly represents and generates. Unintended actions taken without such an instruction can cause risk or inconvenience to people and the environment. We examine how recent vision-language-action (VLA) policies respond when the instruction is missing or meaningless. We apply a paired protocol with empty, neutral, nonsense, infeasible, and wrong-task instructions to six model checkpoints in LIBERO-Goal simulation. Holding the initial state fixed and varying only the instruction, we ask three questions: whether the robot starts to move, which task it completes, and what the instruction determines. Even when the instruction was empty, the robot started moving in every episode with all six checkpoints, and with five of them it often completed a task that the instruction had not specified. On two GR00T checkpoints, the instruction determined which task was executed but not whether the robot started moving; the robot moved even on infeasible instructions. We then tested three methods for suppressing the start: prepending "if no task is given do not move" to the instruction; a gate that holds the robot when the first action chunk for the given instruction nearly equals that for an empty instruction; and fine-tuning the policy to hold still on non-task inputs. The prefix stopped the robot in none of the six checkpoints, and the gate held it on non-task inputs in five of the six checkpoints. The fine-tuned policy never completed a task on non-task inputs, but it did not reliably keep the robot still, and it failed to suppress the start on infeasible instructions.

</details>

---

### [[20_Research/Papers/大模型/KEEPER_Learning_Control-Sufficient_Textual_Memory_for_Long-Horizon_LLM_Agents|KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents]]

![[assets/2610.41482_figure.png|800]]

- **arXiv**: [2610.41482](https://arxiv.org/abs/2610.41482)
- **PDF**: https://arxiv.org/pdf/2610.41482
- **详细分析**: [[20_Research/Papers/大模型/KEEPER_Learning_Control-Sufficient_Textual_Memory_for_Long-Horizon_LLM_Agents|KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents]]
- **作者**: Jinkyeong Choi, Chaebin Jeong, Junsung Jeon, Donghyeon Park
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.05（加权：大模型 0.85，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《KEEPER: Learning Control-Sufficient Textual Memory for Long-Horizon LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, STEP-HRL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recursive textual memory can carry earlier errors into later updates, yet task performance alone does not establish memory reliability. We define self-consistency bias as the persistence of incorrect claims already present in the incoming memory. We present KEEPER, a comparative analysis of four auxiliary objectives along information-content and update-sensitivity axes within a shared recursive interface, examining how supervision targets relate to agent performance. Among evaluated conditions, reward-related prediction achieve the highest task performance before and after offline reinforcement learning, outperforming joint supervision. A claim-level analysis of one baseline trajectory documents error persistence despite corrective observations. Together, these analyses motivate evaluating error persistence and valid-information retention alongside task outcomes.

</details>

---

### [[20_Research/Papers/大模型/When_Safety_Checks_Become_Privacy_Risks_A_Privacy-Preserving_Paradigm_for_LLM_Agent_Safety_Auditing|When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing]]

![[assets/2610.41401_figure.png|800]]

- **arXiv**: [2610.41401](https://arxiv.org/abs/2610.41401)
- **PDF**: https://arxiv.org/pdf/2610.41401
- **详细分析**: [[20_Research/Papers/大模型/When_Safety_Checks_Become_Privacy_Risks_A_Privacy-Preserving_Paradigm_for_LLM_Agent_Safety_Auditing|When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing]]
- **作者**: Yixiang Luo, Ziheng Ma, Ke Chang, Jian Wang, Jiqiang Liu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《When Safety Checks Become Privacy Risks: A Privacy-Preserving Paradigm for LLM Agent Safety Auditing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents interact with online services through tool calls that may access private data or perform sensitive actions. Specialized providers can supply and maintain pre-execution safety auditing capabilities for agent operators. However, sending task descriptions, call arguments, and interaction histories to an external auditor may expose sensitive user information. In this work, we propose a paradigm for privacy-preserving safety auditing that separates delegated audit computation from plaintext access and execution authority. Grounded in a three-domain auditing model, the paradigm connects trusted representation construction, encrypted audit computation, and trusted decision and execution through explicit interfaces. These interfaces accommodate alternative representations and scorers, while encrypted computation protects audit inputs from a semi-honest auditor. We instantiate this paradigm in SealCall, a framework combining learned audit representations, CKKS-based encrypted similarity computation, and execution control bound to audited tool calls. Evaluated on 1,252 public binary candidates, SealCall achieves a mean F1 score of 0.840 under grouped nested evaluation, while preserving plaintext audit decisions in all measured cases. A representative configuration completes each encrypted scoring operation in 0.176 s.

</details>

---

### [[20_Research/Papers/大模型/In-Model_Context_Compression_with_Agentic_Soft_Tokens_for_Long-Horizon_LLM_Agents|In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents]]

![[assets/2610.41291_figure.png|800]]

- **arXiv**: [2610.41291](https://arxiv.org/abs/2610.41291)
- **PDF**: https://arxiv.org/pdf/2610.41291
- **详细分析**: [[20_Research/Papers/大模型/In-Model_Context_Compression_with_Agentic_Soft_Tokens_for_Long-Horizon_LLM_Agents|In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents]]
- **作者**: Xuning He, Kai Fan, Runyu Zhang, Binghuan Wang, Yuxiang Zhang, Xue Jiang, Yihong Dong
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《In-Model Context Compression with Agentic Soft Tokens for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents play an important role in solving complex and sustained tasks, with ever-growing interaction contexts. However, these accumulated contexts will raise substantial computational cost and obscure key decision-relevant evidence. Existing methods typically train external compressors or context-management agents to rewrite context as shorter hard-token sequences, but such external selection may not align with the LLM's evolving representation and is necessarily lossy. In this paper, we introduce Agentic Soft-Token Compression (ASTC), a training-free compression method using soft tokens within LLM agent for long-horizon tasks. Specifically, ASTC uses the model's native recurrent dynamics to determine the already absorbed information, leveraging the commonly-used hybrid Gated Delta Network (GDN)-attention. It then carries this information forward as agentic soft tokens while retaining exact values as hard tokens. The resulting compact sequence reduces later-layer computation and yields reusable KV caches, extending the savings across the agent's trajectory. Extensive experiments on long-horizon tasks show that ASTC matches or exceeds the uncompressed agent's accuracy with up to 50.68% fewer end-to-end Attention Pairs, while trained compressors require 15.4 to 103.7 times more Attention Pairs per successful task. These findings highlight agentic soft tokens as a model-native way to carry absorbed context forward as the task representation evolves.

</details>

---

### [[20_Research/Papers/大模型/When_Disclosure_Is_Compulsory_Evaluating_Ride-Hailing_Rebalancing_Policies_with_Self-Interested_LLM_Driver_Agents|When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents]]

![[assets/2610.41132_figure.png|800]]

- **arXiv**: [2610.41132](https://arxiv.org/abs/2610.41132)
- **PDF**: https://arxiv.org/pdf/2610.41132
- **详细分析**: [[20_Research/Papers/大模型/When_Disclosure_Is_Compulsory_Evaluating_Ride-Hailing_Rebalancing_Policies_with_Self-Interested_LLM_Driver_Agents|When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents]]
- **作者**: Xinyu Wang, Andres Fielbaum
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Disclosure Is Compulsory: Evaluating Ride-Hailing Rebalancing Policies with Self-Interested LLM Driver Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The EU Platform Work Directive, to be transposed by December 2026, requires ride-hailing platforms to state in plain language the main parameters of their automated decisions and how a worker's behaviour affects them. Such rules are exactly what a large language model (LLM) can read, so drivers will be able to let one decide for them. We compare two main families of rebalancing policy once their rules are public: a reactive policy (R) that sends idle drivers to cover requests just lost, and an anticipatory policy (A) that plans moves on a demand forecast. Each driver is an LLM agent maximizing its own net income, given no rules (N) or the rules at the directive's level of detail (L). We test two LLMs, Claude Haiku 5.5 and Jev, which understand the rules equally well, in a three-zone model and in Manhattan. With the rules disclosed, drivers follow the platform more closely: in Manhattan, the share of relocation offers they decline falls from about four in five to one in four under both policies. Yet the effects differ by policy. For the platform, disclosure costs R 3.7% of its profit in Manhattan, as R now pays for moves drivers used to make for free, while A's profit is unchanged; the two policies, which tie on profit under full compliance, end 6.1% apart. For drivers, disclosure raises income in the small model under both policies and LLMs; for users, it raises the service rate there by 10 to 18 percentage points. In Manhattan, self-interested drivers also make A a win-win-win against full compliance, raising driver income, platform profit and service rate by 10 to 12% each. Rebalancing policies that perform equally well under full compliance can thus show opposite results under mandatory disclosure. The study offers a framework to evaluate such policies under the new requirement and is, to our knowledge, the first to do so with LLM agents.

</details>

---

### [[20_Research/Papers/大模型/MUON-RT_Reusing_the_Teacher's_Trajectory_for_Momentum-Free_Muon_for_LLM_Self-Distillation|MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation]]

![[assets/2610.41104_figure.png|800]]

- **arXiv**: [2610.41104](https://arxiv.org/abs/2610.41104)
- **PDF**: https://arxiv.org/pdf/2610.41104
- **详细分析**: [[20_Research/Papers/大模型/MUON-RT_Reusing_the_Teacher's_Trajectory_for_Momentum-Free_Muon_for_LLM_Self-Distillation|MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation]]
- **作者**: Aryan Das, Vinay Kumar Verma, Aakansha Mishra
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.97（加权：大模型 0.45，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-distillation methods for large language models with an exponential moving average (EMA) teacher already retain a history of student updates. Muon nevertheless stores a separate momentum buffer, increasing persistent training memory. We propose Muon with Reused Teacher (Muon-RT), which reuses the teacher-student displacement to eliminate momentum buffers for hidden weight matrices. We show that this displacement encodes an exponentially weighted history of applied updates and smooths temporally uncorrelated noise under a local model. Muon-RT removes its radial component, normalizes it spectrally, and mixes it with the current gradient after Newton-Schulz (NS) orthogonalization. Under explicit regularity and alignment assumptions, we establish linear contraction of an expected objective-gap bound toward a residual error level. With Self-Distillation Fine-Tuning (SDFT) on Qwen2.5-7B-Instruct, Muon-RT improves average accuracy over AdamW by 2.6 points with 42% less persistent memory, and over momentum Muon by 5.4 points with 27% less persistent memory. With Self-Distillation Policy Optimization (SDPO) on Olmo-3-7B-Instruct, it improves average accuracy over AdamW by 2.0 points.

</details>

---

### [[20_Research/Papers/大模型/Accept_Changes,_Reject_Attacks_Robust_Memory_Management_for_LLM_Agents|Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents]]

![[assets/2610.41056_first_page.png|800]]

- **arXiv**: [2610.41056](https://arxiv.org/abs/2610.41056)
- **PDF**: https://arxiv.org/pdf/2610.41056
- **详细分析**: [[20_Research/Papers/大模型/Accept_Changes,_Reject_Attacks_Robust_Memory_Management_for_LLM_Agents|Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents]]
- **作者**: Runze Zhao, Dongruo Zhou, Sumit Kumar Jha, Nathaniel D. Bastian, Ankit Shah
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later. A memory manager decides how each input changes this memory and which records the agent acts on. It can fail in two ways: keeping a fact that has since changed (outdated memory), or storing a planted passage or injected instruction (memory poisoning). Most prior work studies them separately, yet they call for opposite write decisions, so no fixed write rule handles both. We therefore formalize memory robustness as handling both without doing worse on other inputs. Since accuracy checks only the answer, we measure robustness with evidence-conditioned accuracy (ECA), which also checks that the records the manager selects include all the evidence the answer needs, updated and free of attacks. However, existing memory systems and defenses are not more robust than an untuned manager on our test sets. We improve robustness with a simple one-shot recipe that fine-tunes the manager on episodes synthesized around a single conversation with inserted changes and attacks. On three backbones, it improves every category score on our test sets and more than doubles the untuned manager's overall ECA, though robustness remains incomplete.

</details>

---

### [[20_Research/Papers/具身智能/STAR_Steering_Action_Representations_during_Inference|STAR: Steering Action Representations during Inference]]

![[assets/2610.41009_figure.png|800]]

- **arXiv**: [2610.41009](https://arxiv.org/abs/2610.41009)
- **PDF**: https://arxiv.org/pdf/2610.41009
- **详细分析**: [[20_Research/Papers/具身智能/STAR_Steering_Action_Representations_during_Inference|STAR: Steering Action Representations during Inference]]
- **作者**: Guangyu Zhao, Yongchang Zhang, Haoxuan Ru, Kaichen He, Haoran Wen, Kun Zhan, Zeyu Zhang, Yin Li, Yiwu Zhong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《STAR: Steering Action Representations during Inference》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, ReconVLA, UniVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) map language instructions and visual observations to robot actions, showing strong capabilities across robotic manipulation tasks. However, in our probing experiment, we find that action representations near the action output do not fully preserve task-relevant visual grounding. Motivated by this late-layer grounding gap, we introduce STAR, for STeering Action Representations, a training-free inference method for pre-trained VLAs. STAR applies an exponential moving average over late-layer residual updates, allowing later action representations to inherit object-aware update directions from earlier layers without model updates or architectural changes. It further uses recent proprioceptive states to adapt the mixing strength, using conservative mixing when execution dynamics change rapidly. Experiments on robot manipulation benchmarks show that STAR improves late-layer object awareness and increases average task success rates by 4.0 percentage points. Our code is available at https://github.com/PKU-VaLuE-Lab/STAR.

</details>

---

### [[20_Research/Papers/大模型/Steering_Vectors_as_a_Training_Signal_in_LLM_Post-Training|Steering Vectors as a Training Signal in LLM Post-Training]]

![[assets/2610.40998_figure.png|800]]

- **arXiv**: [2610.40998](https://arxiv.org/abs/2610.40998)
- **PDF**: https://arxiv.org/pdf/2610.40998
- **详细分析**: [[20_Research/Papers/大模型/Steering_Vectors_as_a_Training_Signal_in_LLM_Post-Training|Steering Vectors as a Training Signal in LLM Post-Training]]
- **作者**: Tiejin Chen, Maunil Vyas, Huaiyuan Yao, Hua Wei
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Steering Vectors as a Training Signal in LLM Post-Training》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Steering vectors (SVs) are residual-stream directions that shift the behavior of LLMs when added to hidden states at inference time. While prior work has mainly used SVs as post-hoc controls, we ask whether the same directions can also guide parameter updates during post-training. We study this question across supervised learning, including SFT and distillation, and reinforcement learning with verifiable rewards (RLVR). Our framework considers two intervention regimes: a hidden-state hook during teacher-forced supervised training, and an advantage-repair mechanism on wrong rollouts in GRPO. For each regime, we analyze three design axes, which are the steering direction, its placement, and the operation used to combine it with training. In supervised settings, SV injection improves over plain SFT and distillation, with gains scaling with the off-policy gap and reaching up to a $12\%$ improvement when distilling from thinking-mode teachers. These gains hold across three random seeds. In RL settings, applying a correctness-contrast direction as advantage repair on wrong rollouts, including otherwise zero-gradient all-wrong groups, recovers a learning signal that transfers to held-out math benchmarks and acts as a composable auxiliary signal that adds to existing zero-variance remedies such as entropy-aware advantage shaping. We further identify three failure boundaries. In detail, code generation can break the direction, cross-family layer transfer can break the placement, and inference-time application on an SV-trained checkpoint can break the intervention regime. Together, these results establish steering vectors as a conditional but effective training signal for LLM post-training. Our code is available here.

</details>

---

### [[20_Research/Papers/大模型/On_the_Origin_and_Evolution_of_Training-Inference_Mismatch_in_LLM_Reinforcement_Learning|On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning]]

![[assets/2610.40945_figure.png|800]]

- **arXiv**: [2610.40945](https://arxiv.org/abs/2610.40945)
- **PDF**: https://arxiv.org/pdf/2610.40945
- **详细分析**: [[20_Research/Papers/大模型/On_the_Origin_and_Evolution_of_Training-Inference_Mismatch_in_LLM_Reinforcement_Learning|On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning]]
- **作者**: Yu Li, Yufa Zhou, Tian Lan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PipelineRL, QaRL, QeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy reinforcement learning for large language models assumes that training responses are sampled from the current policy. In practice, an inference engine samples the responses and a separate trainer computes the gradients, and the \textbf{training-inference mismatch} between the two makes the training data off-policy. The mismatch has two sources, the numerics of the engine and the stale weights of asynchronous sampling, and a correction that stabilizes training under one source can fail under the other. \textit{We ask which property of a mismatch source decides the correction it needs.} Evaluating the trainer at the sampler's weights splits each sampled-token error exactly into a \textit{numerical discrepancy} of the engine and a \textit{policy lag} of the trainer, and we follow both through training. The numerical discrepancy stays approximately constant, so it biases the updates by a nearly fixed amount, and centering the score at each prefix removes its leading bias. The policy lag is produced by the trainer's own updates: the bias it leaves enters the next update, which enlarges the next lag and closes a feedback loop. Importance weighting cuts this loop only while the lag ratio stays concentrated, and on Qwen3-1.7B it fails at the step where the effective sample size of the ratio falls below one half. From this account we derive the \textbf{discrepancy-lag correction} (DLC), which centers the numerical discrepancy, clips the lag ratio against the sampler's weights and resynchronizes the sampler when this effective sample size falls below one half. Under a stale sampler, DLC keeps the KL divergence from on-policy training within twice the KL between two independent on-policy trainings on Qwen3-0.6B and Qwen3-1.7B, and its resynchronization prevents collapses that the per-token corrections leave and that a KL measured on the sampler's prefixes does not detect.

</details>

---

### [[20_Research/Papers/大模型/Agentic_World_Modeling_for_Agent_Test-time_Scaling_without_Environment_Replica|Agentic World Modeling for Agent Test-time Scaling without Environment Replica]]

![[assets/2610.40927_first_page.png|800]]

- **arXiv**: [2610.40927](https://arxiv.org/abs/2610.40927)
- **PDF**: https://arxiv.org/pdf/2610.40927
- **详细分析**: [[20_Research/Papers/大模型/Agentic_World_Modeling_for_Agent_Test-time_Scaling_without_Environment_Replica|Agentic World Modeling for Agent Test-time Scaling without Environment Replica]]
- **作者**: Wendi Li, Huseyin A. Inan, Wei-Ning Chen, Yanzhi Chen, Chetan Bansal, Saravan Rajmohan, Sharon Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 0.95（加权：大模型 0.75，世界模型 0.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agentic World Modeling for Agent Test-time Scaling without Environment Replica》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：AppWorld, OfficeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time scaling (TTS) improves large language model agents by sampling and selecting among multiple candidate trajectories, but common realizations assume that these trajectories can be executed in parallel. This assumption breaks in realistic deployments, where enterprise workspaces and cloud services are shared and persistent, costly or infeasible to replicate, and actions may introduce irreversible side effects or cross-trajectory interference. Existing generative world models avoid direct execution, but typically compress environment state into a single prompt, limiting their ability to reliably simulate transitions under partial observability. Instead, we introduce Agentic World Modeling (AWM), which reformulates next-observation prediction as a multi-turn evidence-acquisition task. For each hypothetical action, an agentic simulator adaptively queries the real environment through safe read-only interfaces, reasons over the returned evidence, and uses executable computation to construct the resulting observation without mutating shared state. Integrated with trajectory-level TTS, AWM enables parallel exploration over a single shared environment. Across $τ$-bench, AppWorld, and OfficeBench, AWM outperforms a single-shot simulation baseline by 40.07% on average, and surpasses a trained world-model baseline by 12.36% on average. These results establish interactive, read-grounded simulation as a practical foundation for safe and scalable agentic test-time scaling in shared, non-resettable environments.

</details>

---

### [[20_Research/Papers/大模型/The_Generative_Gap_Between_Speculative_Drafter_and_Continuous_Diffusion_Language_Model|The Generative Gap Between Speculative Drafter and Continuous Diffusion Language Model]]

![[assets/2610.40847_first_page.png|800]]

- **arXiv**: [2610.40847](https://arxiv.org/abs/2610.40847)
- **PDF**: https://arxiv.org/pdf/2610.40847
- **详细分析**: [[20_Research/Papers/大模型/The_Generative_Gap_Between_Speculative_Drafter_and_Continuous_Diffusion_Language_Model|The Generative Gap Between Speculative Drafter and Continuous Diffusion Language Model]]
- **作者**: Yujian Chen, Hao Jiang, Guang Cheng, Weijian Luo, Tianyang Hu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《The Generative Gap Between Speculative Drafter and Continuous Diffusion Language Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous diffusion language models (CDLMs) and speculative drafters offer efficient language generation but are typically evaluated differently: CDLMs generate independently through iterative refinement, whereas drafters propose text for target-model verification and correction. We compare their architectures without verification, using LangFlow for CDLMs and adapting DSpark's Markov and recurrent-head architectures for standalone generation. All models are trained from scratch for unconditional, single-block OpenWebText generation at lengths 16, 128, and 1024, without target features or verification, using common preprocessing, backbone dimensions, and training-update budgets. We evaluate generation perplexity (GenPPL) with an external language model and distributional similarity to reference text with MAUVE. With default denoising steps equal to sequence length, LangFlow outperforms both DSpark variants on both metrics at lengths 128 and 1024, while DSpark-RNN leads at 16. A conditional KL analysis characterizes dependencies excluded by the Markov head's previous-token conditioning. Recurrent memory removes this restriction and improves both metrics, but the longer-sequence gap persists. Teacher probability matching further lowers Markov GenPPL without observed MAUVE gains. Increasing LangFlow's denoising steps at fixed weights improves both metrics at lengths 16 and 128, changing the length-128 ordering relative to DSpark-RNN. These results establish LangFlow's longer-sequence advantage under the evaluated budgets and highlight iterative full-sequence refinement as a route to improving standalone generation beyond gains from recurrent head memory.

</details>

---

### [[20_Research/Papers/具身智能/From_Teleoperation_to_Long-Horizon_Dexterity_Evaluating_Visuomotor_Skills_and_Offline_Proxies_for_Dexterous_Manipulation|From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation]]

![[assets/2610.40828_figure.png|800]]

- **arXiv**: [2610.40828](https://arxiv.org/abs/2610.40828)
- **PDF**: https://arxiv.org/pdf/2610.40828
- **详细分析**: [[20_Research/Papers/具身智能/From_Teleoperation_to_Long-Horizon_Dexterity_Evaluating_Visuomotor_Skills_and_Offline_Proxies_for_Dexterous_Manipulation|From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation]]
- **作者**: Ammar N. Abbas, Aayush Jain, Prashanth Viswanath, Nivesh Gadipudi, Giulia Vilone, Jim Gibbons
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL, ImageNet, PointNet, ResNet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered robotic hand. Controlled ablations showed that observation and action representations dominated conventional optimizer and sampling choices. For point-cloud policies, region-of-interest cropping, representation in the robot-base frame, and normalization within the point encoder each improved success by 70-100 percentage points. For the vision-language-action policy, absolute rather than relative action prediction improved insertion success by up to 70 percentage points. Skill decomposition, multi-view perception, and recovery demonstrations were associated with the strongest-performing systems, although their effects were not independently isolated. Of 67 offline metrics evaluated, only five measures of predicted-motion smoothness and directness reliably correlated with insertion success (r = -0.70 to -0.80), and only within a single policy family. These results identify representation choices as key determinants of real-world imitation-learning performance and show that offline metrics can shortlist policies, but cannot replace real-robot evaluation.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Plausible_Prediction_Safety_Sufficiency_in_Web_World_Models|Beyond Plausible Prediction: Safety Sufficiency in Web World Models]]

![[assets/2610.40798_figure.png|800]]

- **arXiv**: [2610.40798](https://arxiv.org/abs/2610.40798)
- **PDF**: https://arxiv.org/pdf/2610.40798
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Plausible_Prediction_Safety_Sufficiency_in_Web_World_Models|Beyond Plausible Prediction: Safety Sufficiency in Web World Models]]
- **作者**: Zhifei Hu, Alexandra I. Cristea, Adel Bibi, Jialin Yu
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Beyond Plausible Prediction: Safety Sufficiency in Web World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SafeWebWorld, WebWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web world models increasingly predict the consequences of candidate actions before agents act, yet a plausible predicted future does not necessarily support the correct safety decision. In a matched human evaluation of 3,000 predictions from ten frozen open models, 86.1% are judged semantically plausible. However, several models exhibit highly asymmetric authorisation behaviour, combining low false-safe execution with poor recall of clarifiable ASK cases and a strong preference for BLOCK. This motivates safety sufficiency: whether a predictive interface preserves and exposes the policy-decisive information required to distinguish actions that may be EXECUTED, require clarification through ASK, or should be BLOCKED. We introduce SafeWebWorld, a benchmark for evaluating safety sufficiency across five web-safety domains through action-conditioned futures, policy-decisive evidence, and policy-conditioned decisions. Under a controlled Security-Aligned Supervised Fine-Tuning protocol, evidence preservation can improve substantially while authorisation-sensitive decisions deteriorate. To determine whether this deterioration reflects loss of authorisation-sensitive score structure or a failure of the decision readout, we introduce Latent Authorisation Recovery (LAR). Frozen-score recalibration reveals substantial but backbone-dependent recovery, while paired recovery provides only a modest additional gain. Yet within-family and matched-authorisation evaluations remain poor, showing that aggregate recoverability does not imply robust fine-grained authorisation behaviour. Overall, plausible prediction, evidence preservation, and aggregate recovery are each insufficient on their own to establish robust authorisation.

</details>

---

### [[20_Research/Papers/大模型/Characterizing_LLM_Agent_Behaviors_in_Module_Shadowing_Environments|Characterizing LLM Agent Behaviors in Module Shadowing Environments]]

![[assets/2610.40716_first_page.png|800]]

- **arXiv**: [2610.40716](https://arxiv.org/abs/2610.40716)
- **PDF**: https://arxiv.org/pdf/2610.40716
- **详细分析**: [[20_Research/Papers/大模型/Characterizing_LLM_Agent_Behaviors_in_Module_Shadowing_Environments|Characterizing LLM Agent Behaviors in Module Shadowing Environments]]
- **作者**: Shuai Yang, Enmeng Lu, Jinyu Fan, Gongce Cao, Yu Chen, Jiawei Xie, Feifei Zhao, Zhangsheng Wang, Yongyu Jiang, Yi Zeng
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Characterizing LLM Agent Behaviors in Module Shadowing Environments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents operating in untrusted workspaces face the risk of untrusted code execution during routine tasks, yet final reports and workspace states alone cannot reliably establish whether execution occurred. We introduce an evaluation framework that codes observation, reasoning, execution, and response behaviors from agent trajectories and aligns them with independent environmental records to reconstruct execution histories and verify final reports. We apply this framework to module shadowing, in which a local file is loaded in place of a trusted module during import, enabling untrusted code execution without adversarial prompts. Across 90 trials with 15 models, the payload executed in 51% of direct shadowing trials and 87% of indirect shadowing trials. Even explicit recognition of the shadowing mechanism did not ensure prevention, as the payload ran in 10 of the 29 trials with recorded recognition. These failures were often omitted from final reports, as 49 of the 62 triggered trials ended without mention of the security issue. Three reports even denied execution, including one from a trial in which independent logs recorded 19 payload executions. Final workspace states also obscured prior execution when agents deleted or overwrote the payload marker in 10 triggered trials. These findings demonstrate that combining behavioral coding with independent environmental auditing enables rigorous and transparent evaluation of agent safety.

</details>

---
