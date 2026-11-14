# cs.CL | Computation and Language | 2026-11-13

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Negative-Only_Policy_Optimization_for_One-Sided_Verifiable_Rewards|Negative-Only Policy Optimization for One-Sided Verifiable Rewards]]

![[assets/2611.17287_first_page.png|800]]

- **arXiv**: [2611.17287](https://arxiv.org/abs/2611.17287)
- **PDF**: https://arxiv.org/pdf/2611.17287
- **详细分析**: [[20_Research/Papers/大模型/Negative-Only_Policy_Optimization_for_One-Sided_Verifiable_Rewards|Negative-Only Policy Optimization for One-Sided Verifiable Rewards]]
- **作者**: Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.25，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Negative-Only Policy Optimization for One-Sided Verifiable Rewards》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry makes standard RLVR unreliable, because reinforcing verified positives can directly reward shortcuts that pass partial checks. To address this issue, we propose Negative-Only Policy Optimization (NOPO), which treats verified positives as unlabeled and updates the policy only by suppressing trusted verified negatives. Specifically, NOPO combines a reference-relative negative suppression loss with a group-level adapter that scales each update by the proportion of non-falsified responses. Across unit-test, constraint-check, and LLM self-verifiers, NOPO improves pass@k over baselines on code, logic, and math benchmarks when oracle rewards are unavailable. These gains persist under inference-time scaling and cross-benchmark transfer.

</details>

---

### [[20_Research/Papers/大模型/Outcome-Mass_Alignment_Controlling_Length-Dependent_Trajectory_Influence_in_Multi-Turn_LLM_Agent_Reinforcement_Learning|Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning]]

![[assets/2611.16816_figure.png|800]]

- **arXiv**: [2611.16816](https://arxiv.org/abs/2611.16816)
- **PDF**: https://arxiv.org/pdf/2611.16816
- **详细分析**: [[20_Research/Papers/大模型/Outcome-Mass_Alignment_Controlling_Length-Dependent_Trajectory_Influence_in_Multi-Turn_LLM_Agent_Reinforcement_Learning|Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning]]
- **作者**: Dawei Zhang, Yubin Huangfu, Jessica Fan, Boyu Wei, Likang Wu, Hongke Zhao, Ming He, Zhu Teng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.55（加权：大模型 0.95，强化学习 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assignment: row-based outcome statistics can count one episode outcome multiple times, while token-level reduction can assign unequal aggregate objective mass across trajectories. We term these effects outcome-statistics multiplicity and objective-mass imbalance. We introduce Outcome-Mass Alignment (OMA), a two-component method that makes both accounting choices explicit. Outcome Alignment computes outcome statistics over unique source trajectories, while Mass Alignment controls aggregate objective mass after within-trajectory aggregation of optimizer-native token objectives. Neither redesigns the base optimizer's credit assignment, importance ratios, or clipping. Across matched ALFWorld GRPO comparisons at two model scales, where failed trajectories typically expand much more than successful ones, OMA improves matched-horizon endpoint success by 7.0-9.4 percentage points. Ordinary WebShop exhibits weak or reversed expansion-outcome coupling and correspondingly mixed effects, whereas in a success-oriented WebShop setting, WebShop-SOL, OMA improves success nAUC from 0.399 to 0.511. Component ablations and GiGPO and GSPO comparisons further support component separability and cross-optimizer compatibility. These results show that trajectory expansion always defines an implicit weighting rule, but its practical effect depends on how expansion couples to outcomes and optimizer-native updates.

</details>

---

### [[20_Research/Papers/强化学习/Experience-Handoff_Reinforcement_Learning_for_Recursive_Self-Improvement|Experience-Handoff Reinforcement Learning for Recursive Self-Improvement]]

![[assets/2611.16409_first_page.png|800]]

- **arXiv**: [2611.16409](https://arxiv.org/abs/2611.16409)
- **PDF**: https://arxiv.org/pdf/2611.16409
- **详细分析**: [[20_Research/Papers/强化学习/Experience-Handoff_Reinforcement_Learning_for_Recursive_Self-Improvement|Experience-Handoff Reinforcement Learning for Recursive Self-Improvement]]
- **作者**: Doyoung Kim, Byeongguk Jeon, Kailin Zhang, Sherry Yang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Experience-Handoff Reinforcement Learning for Recursive Self-Improvement》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this rich information, recent works wrap the agent in a harness that refines its own inputs through reflection or compaction and hands past experience to future rollouts, but the construction of the handed-off artifacts (e.g., a playbook) is itself not learned. We want the best of both worlds: gradient updates from a scalar reward, while also utilizing environment information to hand off experience. As a concrete testbed, we fix the Agentic Context Engineering (\ace{}) harness and train one model to act, reflect, and curate task-local playbooks. Our method, \acerl{}, evaluates candidate experience-handoff artifacts by their downstream effect on future actor rollouts, and co-optimizes the role-specific behaviors (action generator, insight reflector, and playbook curator) under a fixed scaffold. Across agentic benchmarks, \acerl{} achieves higher held-out performance than baseline methods. The results suggest that agent training should optimize not only the actions in the current rollout, but also the model-written experience that future rollouts inherit.

</details>

---

### [[20_Research/Papers/大模型/AROMA_Adaptive_Representation-Oriented_Multimodal_Actuation_for_Vision-Language_Model_Control|AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control]]

![[assets/2611.15041_first_page.png|800]]

- **arXiv**: [2611.15041](https://arxiv.org/abs/2611.15041)
- **PDF**: https://arxiv.org/pdf/2611.15041
- **详细分析**: [[20_Research/Papers/大模型/AROMA_Adaptive_Representation-Oriented_Multimodal_Actuation_for_Vision-Language_Model_Control|AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control]]
- **作者**: Zhaoning Zhang
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mechanistic localization does not by itself yield usable control: causal sensitivity may occupy little activation energy, an accurate local direction may fail at finite scale, and a reachable numeral target may be wrong. We introduce AROMA (Adaptive Representation-Oriented Multimodal Actuation), a frozen-VLM control framework separating where to intervene, which geometry and gain to use, how to reach a target, which target to pursue, and when to act. In Llama-3.2-11B-Vision-Instruct, four dimensions of a causally validated cross-attention head explain 89.82% of cardinality sensitivity but only 9.52% of median activation energy; magnitude-normalized causal subspace actuation converts this mismatch into finite control, improving exact-count accuracy on untouched procedural data by +8.00 pp. Iterative Minimal-Effort Actuation (MEA) reaches 81.25% of oracle targets versus 15.18% for a frozen direction under matched step budgets. With target and gate frozen before evaluation, targeted MEA improves the previous frozen policy from 34.444% to 38.730% on a new natural Stage-2 cohort (N=630; paired p=4.63e-7) and yields 65.741% versus 65.153% over all 7,992 examples while editing only 63 inputs. Prospective routing, replication across heads and models, and comparisons with attribution-steering baselines further characterize each stage, separating localization, actuation, reachability, target quality, and selective deployment as distinct control problems.

</details>

---

### [[20_Research/Papers/大模型/Trait_Hitchhiking_in_LLM_Post-Training|Trait Hitchhiking in LLM Post-Training]]

![[assets/2611.14683_figure.png|800]]

- **arXiv**: [2611.14683](https://arxiv.org/abs/2611.14683)
- **PDF**: https://arxiv.org/pdf/2611.14683
- **详细分析**: [[20_Research/Papers/大模型/Trait_Hitchhiking_in_LLM_Post-Training|Trait Hitchhiking in LLM Post-Training]]
- **作者**: Adil Soubki, Elizabeth S. Z. Tan, Miles Cranmer
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Trait Hitchhiking in LLM Post-Training》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is now a standard stage of language model post-training, and the compute devoted to it is growing rapidly. While it has been shown to improve capabilities, particularly for tasks with verifiable rewards, it can also change behaviours and internal properties that the reward does not explicitly target. We present a formalism to describe the evolution of "traits" during RL post-training and, in doing so, recover the Price equation from evolutionary biology. We use this to develop a mathematical model for what we call "trait hitchhiking": the amplification or suppression of non-targeted traits as training redistributes probability across completions. We evaluate this Price update expression on language models trained with GRPO and show that the Price estimates closely track the sampled trait dynamics. These results identify trait hitchhiking as a mechanism by which RL post-training can silently amplify undesirable traits.

</details>

---
