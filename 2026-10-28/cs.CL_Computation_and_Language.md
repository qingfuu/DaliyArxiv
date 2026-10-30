# cs.CL | Computation and Language | 2026-10-28

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/强化学习/EnvSched_Environment-Aware_Scheduling_for_Rollout-Efficient_Agent_Reinforcement_Learning|EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning]]

![[assets/2610.37609_figure.png|800]]

- **arXiv**: [2610.37609](https://arxiv.org/abs/2610.37609)
- **PDF**: https://arxiv.org/pdf/2610.37609
- **详细分析**: [[20_Research/Papers/强化学习/EnvSched_Environment-Aware_Scheduling_for_Rollout-Efficient_Agent_Reinforcement_Learning|EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning]]
- **作者**: Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng, Tianyi Jiang, Renye Yan, Ning Ding, Yifan Zhang, Renrui Zhang, Yehui Tang, Wentao Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.77（加权：大模型 0.65，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACEBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Environment-aware Scheduling), an online scheduler that learns from rollout history. EnvSched assigns scheduling value through two complementary modeling choices: exploitation prioritizes tasks likely to provide informative reward differences, while coverage spreads each batch across underobserved environments and interaction patterns. EnvSched organizes environment--task pairs as nodes in a dual-relation graph, with within-environment edges capturing task semantics and shared tool, state, and verifier structure, and cross-environment edges capturing abstract execution and reward topology. By propagating historical rollout statistics along both edge types, it predicts within-task reward variance. These predictions guide a scheduler that allocates each batch to tasks with high predicted reward variance and underobserved environments and tasks. Environment quotas and a similarity penalty further limit concentration and redundancy, yielding informative and diverse batches without additional pilot rollouts. In RL on Qwen3-8B, EnvSched achieves an average score of 48.81 across BFCL-v3, tau-Bench, and ACEBench-Agent after 40 training steps, exceeding the highest score attained by random task selection after 120 steps. It also improves downstream performance across model sizes at the same training budget.

</details>

---

### [[20_Research/Papers/大模型/TrawMem_Reframing_Agent_Memory_as_Task-Oriented_Role-Adaptive_Workspaces|TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces]]

![[assets/2610.36918_figure.png|800]]

- **arXiv**: [2610.36918](https://arxiv.org/abs/2610.36918)
- **PDF**: https://arxiv.org/pdf/2610.36918
- **详细分析**: [[20_Research/Papers/大模型/TrawMem_Reframing_Agent_Memory_as_Task-Oriented_Role-Adaptive_Workspaces|TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces]]
- **作者**: Mingyu Zhang, Zixu Li, Zhiheng Fu, Zhiwei Chen, Jinhe Bi, Yupeng Hu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TrawMem: Reframing Agent Memory as Task-Oriented Role-Adaptive Workspaces》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents rely on memory systems to leverage long-term interactions, yet existing systems typically retrieve memories based on their relevance to the current query and use them as contextual evidence. However, relevance alone does not characterize how a memory contributes to task solving: the same memory may serve different roles across tasks, such as directly supporting the answer or linking to complementary memories with weaker semantic relevance but necessary information. We therefore reframe agent memory systems as Task-Oriented Role-Adaptive Workspaces, where memories are selected and organized by their task-oriented roles and relations. Based on this view, we propose TrawMem, which organizes interaction histories into local threads and constructs task-oriented workspaces by assigning roles and jointly selecting complementary memories. Experiments on LoCoMo and MemGallery with four open- and closed-source backbones show consistent improvements over representative memory systems, with macro-F1 gains of 2.23-3.14 points. On LoCoMo, TrawMem improves the LLM-Judge score over SimpleMem by 4.07 and 4.31 percentage points on Qwen3.5-9B and DeepSeek-V4-Flash, respectively, while requiring approximately 12.8% and 5.1% fewer context tokens, respectively.

</details>

---

### [[20_Research/Papers/大模型/CONCUR_Concordant_Auxiliary_Rewards_for_Multi-Task,_Multi-Reward_Reinforcement_Learning|CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning]]

![[assets/2610.36437_figure.png|800]]

- **arXiv**: [2610.36437](https://arxiv.org/abs/2610.36437)
- **PDF**: https://arxiv.org/pdf/2610.36437
- **详细分析**: [[20_Research/Papers/大模型/CONCUR_Concordant_Auxiliary_Rewards_for_Multi-Task,_Multi-Reward_Reinforcement_Learning|CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning]]
- **作者**: Jixuan Leng, Si Si, Fei Wang, Cho-Jui Hsieh, Jiong Zhang, Hsiang-Fu Yu, Inderjit S. Dhillon
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.45，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a Large Language Model (LLM) is trained with Reinforcement Learning (RL) on multiple tasks, a task's primary reward can gate auxiliary rewards such as a length reward: on a failing response, an auxiliary cannot exceed the primary. However, group-relative advantage estimators treat a gated auxiliary like any other component, so it can reverse the primary's order, and at the primary's ceiling only auxiliaries order responses. Keeping gated auxiliaries hurts some tasks, while dropping them hurts others. We propose CONCUR, an advantage estimator that replaces the standardized scores of each gated auxiliary with the closest scores that satisfy two conditions: responses with higher primary rewards cannot receive lower scores, and responses at the primary's ceiling receive equal scores. CONCUR-T applies both conditions throughout training, and CONCUR-A lifts the second for an auxiliary that agrees with the primary's order more often than it reverses it among passing responses. On three models from two families and across math, code, instruction following, and writing, both variants score higher on average than all baselines and than when all the gated auxiliaries are dropped.

</details>

---

### [[20_Research/Papers/具身智能/OmniBrain-0_A_Unified_Agentic_Model_for_Embodied_Intelligence|OmniBrain-0: A Unified Agentic Model for Embodied Intelligence]]

![[assets/2610.36013_figure.png|800]]

- **arXiv**: [2610.36013](https://arxiv.org/abs/2610.36013)
- **PDF**: https://arxiv.org/pdf/2610.36013
- **详细分析**: [[20_Research/Papers/具身智能/OmniBrain-0_A_Unified_Agentic_Model_for_Embodied_Intelligence|OmniBrain-0: A Unified Agentic Model for Embodied Intelligence]]
- **作者**: Xiaomi Embodied Intelligence Team, Yuechen Luo, Chong He, Fang Li, Shaoqing Xu, Jingkai Wang, Menglun Su, Jiaxin Liu, Shengyin Jiang, Zhiyi Lai, Long Chen, Longlong Wang...
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.65（加权：具身智能 1.2，大模型 0.45）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《OmniBrain-0: A Unified Agentic Model for Embodied Intelligence》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbSpatial-Bench, InternVLA, LingBot-VLA, RefSpatial-Bench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose embodied intelligence requires robots to coordinate diverse skills over long horizons, track task progress, and recover from failures. Specialist policies alone do not ensure task-level reliability, while powerful multimodal agents rely on costly reasoning and external experience that compact models struggle to reproduce. We introduce OmniBrain-0, a lightweight unified embodied agent that coordinates manipulation and navigation through a shared high-level decision model, integrating task understanding, planning, progress tracking, and feedback-driven recovery. Our progressive training framework combines embodied pretraining, domain-specialized agent distillation, and multi-teacher on-policy distillation (MOPD). It distills powerful teachers' interaction experience into manipulation and navigation experts, then consolidates their decision capabilities into OmniBrain-0. Unification therefore occurs within the learned decision model rather than only at the tool interface. We further introduce Rubric-Guided Recursive Self-Improvement (RSI), a data flywheel in which a Meta-Agent turns execution evidence into refined rubrics, step-level reminders, and verified trajectories for domain-expert updates before their reconsolidation into OmniBrain-0 through MOPD. We evaluate OmniBrain-0 on LIBERO-Pro, LIBERO-Plus, RoboCasa365, RoboTwin 2.0, and R2R-CE Val-Unseen, as well as multiple real-world manipulation tasks. OmniBrain-0 combines strong cross-domain task performance with substantially lower inference and execution overhead than its closed-source teacher, demonstrating efficient transfer and consolidation of embodied capabilities into a compact unified agent.

</details>

---
