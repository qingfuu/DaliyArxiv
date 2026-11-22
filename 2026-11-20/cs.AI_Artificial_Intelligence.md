# cs.AI | Artificial Intelligence | 2026-11-20

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/具身智能/One_Prior,_Two_Dynamics_Repurposing_Video_Diffusion_Transformers_for_Self-Supervised_Latent_Action_Learning|One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning]]

![[assets/2611.26617_figure.png|800]]

- **arXiv**: [2611.26617](https://arxiv.org/abs/2611.26617)
- **PDF**: https://arxiv.org/pdf/2611.26617
- **详细分析**: [[20_Research/Papers/具身智能/One_Prior,_Two_Dynamics_Repurposing_Video_Diffusion_Transformers_for_Self-Supervised_Latent_Action_Learning|One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning]]
- **作者**: Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Olaf-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics. By controlling information access and optimizing both dynamics end-to-end through a compact bottleneck, O$^{2}$LaF learns transferable actions from unlabeled videos. Across navigation and robotic manipulation, O$^{2}$LaF sets a new state of the art in few-shot action probing and enables stronger zero-shot action transfer across visual contexts and embodiments. Beyond generative video priors, we further extend our framework to predictive representation priors such as V-JEPA2, achieving competitive performance. Our findings suggest a broader paradigm for latent-action learning: repurposing pretrained video models to discover transferable actions and predict their consequences.

</details>

---

### [[20_Research/Papers/具身智能/PGX_Physically_Grounded_Execution_for_Long-Horizon_Humanoid_Loco-Manipulation|PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation]]

![[assets/2611.26596_figure.png|800]]

- **arXiv**: [2611.26596](https://arxiv.org/abs/2611.26596)
- **PDF**: https://arxiv.org/pdf/2611.26596
- **详细分析**: [[20_Research/Papers/具身智能/PGX_Physically_Grounded_Execution_for_Long-Horizon_Humanoid_Loco-Manipulation|PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation]]
- **作者**: Kai Lu, Chenyang Ma, Ioannis Havoutis
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.6（加权：具身智能 2.1，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using physical predicates to gate phase transitions, trigger recovery, and coordinate navigation and waiting. Shared predicate semantics connect offline demonstration segmentation, online execution, and stage-wise evaluation; (ii) VLA skills operate within active manipulation phases, with flat or stage-trained models concentrating on task-relevant actions; and (iii) world-coordinate locking (WCL) maintains spatial consistency through base station keeping, object-relative positioning, and world-anchored contact targets. We demonstrate the effectiveness of PGX with extensive experiments conducted on three simulated tasks and one real-world task using a Unitree G1 humanoid robot for long-horizon loco-manipulation, showing improvements in stage progression and task success rates. Project page is available at: https://kl-research.github.io/pgx

</details>

---

### [[20_Research/Papers/具身智能/Mind2Act_World_A_Diagnostic_Benchmark_for_Embodied_Mind,_Physical_Action,_and_Mind-Action_Composition_in_Robotic_Manipulation|Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation]]

![[assets/2611.26444_first_page.png|800]]

- **arXiv**: [2611.26444](https://arxiv.org/abs/2611.26444)
- **PDF**: https://arxiv.org/pdf/2611.26444
- **详细分析**: [[20_Research/Papers/具身智能/Mind2Act_World_A_Diagnostic_Benchmark_for_Embodied_Mind,_Physical_Action,_and_Mind-Action_Composition_in_Robotic_Manipulation|Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation]]
- **作者**: Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, Ziyi Xiong, Yang Li, Zhengwei Xie, Zhimin Wang, Zhen Liu, Jiazhen Huang, Yuzheng Zhang...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 2.7，大模型 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a failure comes from reasoning, execution, or their composition. We introduce Mind2Act World, a diagnostic benchmark of 30 simulated manipulation tasks from five real-world application domains. Each task has three difficulty levels and two scene settings (Clean and Random), yielding 180 configurations. The tasks form three views: Mind tests decisions based on past observations, Act tests precise and timely execution, and Mind2Act combines both in closed-loop tasks where action outcomes guide later decisions. Comparing the three views shows whether a system lacks a capability or fails to compose capabilities it already has. A diagnosis harness further attributes the failed episodes of three representative systems to Mind, Act, or their composition and summarizes each system in a profile card. Our evaluation of multimodal agents, vision-language-action models (VLAs), and world-action models (WAMs) shows that competence in a single view does not carry over to Mind2Act tasks. Even the strongest agent succeeds in 52.7% of Mind and 39.0% of Act episodes but in only 12.0% of Mind2Act episodes. The strongest agent retains task state but struggles with sustained contact, whereas end-to-end policies execute practiced motions but retain little task state. These findings point to composing reasoning and execution through environmental feedback as the main open problem.

</details>

---

### [[20_Research/Papers/具身智能/Awaken-HI_Scaling_Humanoid_Intelligence_with_Whole-Body_Human_Experience|Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience]]

![[assets/2611.26420_figure.png|800]]

- **arXiv**: [2611.26420](https://arxiv.org/abs/2611.26420)
- **PDF**: https://arxiv.org/pdf/2611.26420
- **详细分析**: [[20_Research/Papers/具身智能/Awaken-HI_Scaling_Humanoid_Intelligence_with_Whole-Body_Human_Experience|Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience]]
- **作者**: EngineAI
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.3（加权：具身智能 1.8，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A central goal of humanoid robotics is for robots to perform the everyday work people do in homes and workplaces. Existing egocentric video datasets cover many of these activities but provide little synchronized whole-body motion data for learning loco-manipulation at scale. We build Awaken-Human, which pairs approximately 50,000 hours of egocentric stereo video with synchronized whole-body human motion and covers more than 100 skills. Building on this, we also introduce Awaken-HI (Humanoid Intelligence), a vision-language-action model for humanoid loco-manipulation that jointly predicts original human motion and retargeted robot actions through a shared action expert. We show that loco-manipulation skills transfer more effectively from people to humanoids when human trajectories directly supervise the shared action expert. Increasing human pretraining data reduces held-out robot action prediction error according to an empirical scaling law and raises the mean success rate on downstream real-robot tasks. After full-corpus pretraining and T800 adaptation, Awaken-HI achieves a mean success rate of 93.75% across eight individual tasks and outperforms GR00T N1.7 and $π_{0.5}$ in both individual and long-horizon evaluations. The same policy generalizes to objects unseen during robot post-training and to new pairings of familiar objects and destinations.

</details>

---

### [[20_Research/Papers/大模型/How_Much_Should_an_Agent_Remember_Deployment_Lessons_from_Self-Distilled_Memory_for_LLM_Agents|How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents]]

![[assets/2611.26361_figure.png|800]]

- **arXiv**: [2611.26361](https://arxiv.org/abs/2611.26361)
- **PDF**: https://arxiv.org/pdf/2611.26361
- **详细分析**: [[20_Research/Papers/大模型/How_Much_Should_an_Agent_Remember_Deployment_Lessons_from_Self-Distilled_Memory_for_LLM_Agents|How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents]]
- **作者**: K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan, Vinod Muthusamy, Punleuk Oum, Gaodan Fang, Michal Ulewicz, Gegi Thomas, Evelyn Duesterwald
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent receives either all guidelines or a selected subset. The pipeline ships in the open-source altk-evolve library and is deployed in IBM's CUGA agent and watsonx Orchestrate platform. We report what we learned building, measuring, and productizing it. Our primary instrument is the AppWorld benchmark, across models spanning 40--92\% baseline task completion. The central finding is that the right amount of memory is a property of the model, not the memory. A strong model keeps improving as guidelines are added. DeepSeek-V3.2 gains +9.5 points of task completion and +16.1 points of scenario completion with its full 191-guideline set. A weak model gains less from the same full set than from a small selected subset. gpt-oss-120b starts at 39.9\% task completion. It reaches 51.2\% with all 199 of its guidelines but 55.4\% (mean of two runs) with a selected subset of about 29. Around that result we report what went wrong: a high-support guideline that backfired, provenance silently dropped during consolidation, a swallowed API error that failed every task while producing a plausible log, and a baseline confound that nearly produced a misleading comparison with a prior method. We distill these into recommendations for teams deploying agent memory.

</details>

---

### [[20_Research/Papers/强化学习/Actor-Predictor_Architecture_for_Reinforcement_Learning_with_Formal_Specification_Objectives|Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives]]

![[assets/2611.26313_figure.jpg|800]]

- **arXiv**: [2611.26313](https://arxiv.org/abs/2611.26313)
- **PDF**: https://arxiv.org/pdf/2611.26313
- **详细分析**: [[20_Research/Papers/强化学习/Actor-Predictor_Architecture_for_Reinforcement_Learning_with_Formal_Specification_Objectives|Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives]]
- **作者**: Josef Brozovich, Qining Zhang, Lei Ying
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人
- **相关性评分**: 1.0（加权：强化学习 0.8，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives》归入 强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

One fundamental challenge in reinforcement learning (RL) is enforcing temporal safety constraints, such as satisfying formal specifications. Existing methods often transform logic formulas into automata for state augmentation and reward shaping. However, this approach assumes that automaton construction is both feasible and tractable, which limits its applicability to small specifications and linear temporal logic (LTL). This paper proposes Actor-Predictor, a framework that learns a surrogate representation of logic progress without explicitly constructing an automaton. The predictor continuously estimates whether a partial trajectory will satisfy the formal specification in a later step, and its learned features are provided as auxiliary inputs to the actor, which is then optimized using GRPO and RWR. We show theoretically that, under sufficient predictive accuracy, the learned representation is equivalent to the automaton state. Experiments on grid world and robotic tasks in Isaac Lab demonstrate that Actor-Predictor outperforms automaton-based baselines on LTL-constrained tasks. It also performs well on non-regular formal specifications, such as $(a^n b^n)$, for which finite-automaton-based approaches are not applicable.

</details>

---

### [[20_Research/Papers/强化学习/The_Stability_Gap_in_Continual_Reinforcement_Learning|The Stability Gap in Continual Reinforcement Learning]]

![[assets/2611.26252_figure.png|800]]

- **arXiv**: [2611.26252](https://arxiv.org/abs/2611.26252)
- **PDF**: https://arxiv.org/pdf/2611.26252
- **详细分析**: [[20_Research/Papers/强化学习/The_Stability_Gap_in_Continual_Reinforcement_Learning|The Stability Gap in Continual Reinforcement Learning]]
- **作者**: Sebastian Pusch, Matthia Sabatelli, Gido M. van de Ven
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《The Stability Gap in Continual Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual reinforcement learning (CRL) aims to enable agents to adapt to changing tasks while preserving previously acquired capabilities. Evaluation often relies on final aggregate metrics that can hide temporary performance degradation during adaptation. This work introduces a simple CRL benchmark that varies observation representations while preserving environment dynamics and rewards, supporting proof-of-concept demonstrations, inexpensive experimentation, and easily reproducible sanity checks. Using this benchmark, we demonstrate the stability gap in CRL: a substantial drop in prior-task performance after the introduction of new tasks, followed by partial or complete recovery. This pattern occurs despite the agent having complete access to past tasks.

</details>

---

### [[20_Research/Papers/具身智能/FastRoverVLA_Fast_Vision-Language-Action_Execution_for_Off-Road_Autonomous_Driving|FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving]]

![[assets/2611.26242_figure.png|800]]

- **arXiv**: [2611.26242](https://arxiv.org/abs/2611.26242)
- **PDF**: https://arxiv.org/pdf/2611.26242
- **详细分析**: [[20_Research/Papers/具身智能/FastRoverVLA_Fast_Vision-Language-Action_Execution_for_Off-Road_Autonomous_Driving|FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving]]
- **作者**: Changtao Zhao, Yingxue Guan, Li Wang, Shijie Zhao, Yuhang Zhang, Shengkai Zhang, Qing Wang, Ziying Song
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoVLA, ColaVLA, DriveWorld-VLA, FastRoverVLA, GraphWorld, MomWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference. Reusing a prediction reduces this demand while leaving its commands exposed to changes in vehicle motion. FastRoverVLA addresses this mismatch by decoupling visual plan generation from motion-conditioned execution. Its training-free interface maintains decoded plans between visual predictions. A speed-curvature action buffer is aligned with measured motion at each update, integrated into a local trajectory, and advanced by consuming the current action. The corrected remainder is written back to the buffer, preserving motion corrections across successive updates. A bounded refresh rule normalizes speed and curvature variations within a newly decoded plan and assigns a short or long reuse budget according to the resulting plan-roughness score. The interface requires neither backbone features nor an additional learned driving policy. Over a 3 s horizon, independent real-request evaluation achieves average displacement error (ADE) and final displacement error (FDE) of 0.328/0.596 m on ORAD-3D and 0.266/0.526 m on RELLIS-3D, reducing FDE by 18.0% and 36.7% at request rates of 6.0% and 4.8%, respectively. These runs retain lower errors across four backbones and both datasets and reduce Qwen3-VL request-processing cost by factors of 16.6 and 20.8 under serial replay, while mechanism and motion-only controls identify persistent state correction as the main source of the observed accuracy benefit. The source code and evaluation materials are publicly available at https://github.com/ADEPT-ORG/FastRoverVLA.

</details>

---

### [[20_Research/Papers/具身智能/Controlling_the_Humanoid_Robot_H1-2_With_a_Simulated_Biologically_Plausible_Network|Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network]]

![[assets/2611.26074_first_page.png|800]]

- **arXiv**: [2611.26074](https://arxiv.org/abs/2611.26074)
- **PDF**: https://arxiv.org/pdf/2611.26074
- **详细分析**: [[20_Research/Papers/具身智能/Controlling_the_Humanoid_Robot_H1-2_With_a_Simulated_Biologically_Plausible_Network|Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network]]
- **作者**: Fatima Atwi, Constant Roux, Christian Bergaud, Olivier Stasse
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.7（加权：具身智能 1.8，强化学习 0.2，机器人 1.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial Spiking Neural Networks have gained remarkable attention in the last few years due to their proven ability in simulating biological neural cultures and producing similar activity and trends. Nevertheless, whether they can be trained for humanoid locomotion while retaining biological plausibility and robust performance at once remains an open question. We study this problem by proposing a biologically inspired spiking network, trained by different learning schemes and tested on the H1-2 Unitree Humanoid. These schemes differ in how recurrent weights are trained. Ordered from most to least biologically faithful, they are: a fixed reservoir mimicking an in-vitro neural culture, where recurrent weights are kept frozen and only a linear readout is trained, the same network but with its synapses trained by reward-modulated spike timing dependent plasticity and eligibility propagation, and finally backpropagation through time as a non biological baseline for comparison. All schemes relied on distillation of a reinforcement learning expert policy with dataset aggregation. We show that e-prop reached 100% survival rate matching backpropagation through time, whereas both the fixed reservoir and the reward-modulated STDP, though the closest to biological cultures, plateaued at a much lower performance (~43.7% and ~11% survival). We explore in further detail which trends a real culture could and could not produce until now. Finally we demonstrate brief bipedal stepping on a full size humanoid H1-2.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Improvement-Guided_Replay_for_Continual_Reinforcement_Learning|Policy Improvement-Guided Replay for Continual Reinforcement Learning]]

![[assets/2611.25989_figure.png|800]]

- **arXiv**: [2611.25989](https://arxiv.org/abs/2611.25989)
- **PDF**: https://arxiv.org/pdf/2611.25989
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Improvement-Guided_Replay_for_Continual_Reinforcement_Learning|Policy Improvement-Guided Replay for Continual Reinforcement Learning]]
- **作者**: Qin-Wen Luo, Haoxuan Gao, Sheng Ren, Xiang Chen, Sheng-Jun Huang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Policy Improvement-Guided Replay for Continual Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual reinforcement learning (CRL) requires models to acquire new capabilities while retaining performance on previous tasks. A stability-oriented perspective common in conventional continual learning emphasizes knowledge preservation and interference mitigation. Complementing this perspective, we revisit CRL for vision-language models through policy improvement, a fundamental principle of RL, to preserve acquired performance gains. Using the performance difference lemma, we characterize historical performance changes through the current policy's expected advantages on historical task distributions, motivating replay of historical prompts with the current policy. To allocate limited replay memory, we propose Contrastive Likelihood Replay (CoLiR), which contrasts likelihood gains on correct responses from the final task policy with likelihood reductions on incorrect responses from the initial policy. Our analysis links correct-response likelihood gains to reference-policy advantages under an idealized KL-regularized optimal update and provides an endogenous-reward interpretation for general policy updates. CoLiR estimates scores from finite training rollouts and cached log-likelihoods, selects prompts at task boundaries, and replays them uniformly during subsequent training, with KL regularization restricted to replayed prompts. Memory construction only requires a small amount of additional cross-policy scoring but no additional response generation. Across three Qwen3-VL model sizes on MRCL, CoLiR achieves the highest mean final accuracy and mean task accuracy among the compared methods while maintaining competitive new-task performance.

</details>

---

### [[20_Research/Papers/世界模型/Fast-JEPA_Advancing_the_Success-Latency_Frontier_for_Latent_World_Models|Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models]]

![[assets/2611.25927_figure.png|800]]

- **arXiv**: [2611.25927](https://arxiv.org/abs/2611.25927)
- **PDF**: https://arxiv.org/pdf/2611.25927
- **详细分析**: [[20_Research/Papers/世界模型/Fast-JEPA_Advancing_the_Success-Latency_Frontier_for_Latent_World_Models|Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models]]
- **作者**: Yao Zhang, Bin Yu, Shijie Lian, Haishan Liu, Changti Wu, Yu Wu, Kai Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models predict the outcomes of action sequences, but comparing candidate plans through recursive rollout remains expensive at test time. We introduce Fast-JEPA, a latent world model planning framework that advances the success-latency Pareto frontier of predictive search. Fast-JEPA reorganizes predictive computation to support effective action-sequence search at low planning cost. It constructs a goal-directed plan to guide search and directly predicts the outcomes of complete candidates for efficient comparison, avoiding recursive state rollout during refinement. Across PushT, Reacher, Cube, and TwoRoom, Fast-JEPA achieves 96.50% average success rate with 2.41x faster planning than INTACT. Search-budget sweeps show that its competitive success and low latency extend across candidate counts and refinement depths. We further introduce DynaGoal, a benchmark for evaluating world-model planning under dynamic out-of-distribution conditions, execution deadlines, and controlled response delays. Fast-JEPA achieves average success rates of 73.83% on DynaGoal-Shift and 87.67% on DynaGoal-Deadline, demonstrating the practical value of low-latency predictive planning under changing control conditions and execution-time constraints. Our code is available at https://github.com/Sofilyzia/Fast-JEPA.

</details>

---

### [[20_Research/Papers/具身智能/Collision-Free_Is_Not_Enough_Passage-Conditioned_Navigation_for_Wheeled-Legged_Robots|Collision-Free Is Not Enough: Passage-Conditioned Navigation for Wheeled-Legged Robots]]

![[assets/2611.25788_figure.png|800]]

- **arXiv**: [2611.25788](https://arxiv.org/abs/2611.25788)
- **PDF**: https://arxiv.org/pdf/2611.25788
- **详细分析**: [[20_Research/Papers/具身智能/Collision-Free_Is_Not_Enough_Passage-Conditioned_Navigation_for_Wheeled-Legged_Robots|Collision-Free Is Not Enough: Passage-Conditioned Navigation for Wheeled-Legged Robots]]
- **作者**: Wai Ka Sun, Waiyiu Pong, Bowen Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Collision-Free Is Not Enough: Passage-Conditioned Navigation for Wheeled-Legged Robots》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A collision-free detour can still bring a legged robot to the next stair or ledge a few centimetres or degrees off, and a fixed locomotion skill, factory or learned, can stall or fall. Existing methods prevent this with a robot model or extensive trial and error, but on a new site with unknown skills neither is available, so they cannot be used. We find that a single 27-minute teaching session already supplies what these methods have to derive or learn: for every stair and ledge, one crossing the skill has completed. Our method, passage-conditioned navigation, makes the route remember how each transition was entered, not only where the path went. It stores each taught crossing as an event and, without training or a robot model, enforces it after every local replan: before each ledge, an entry gate makes the robot turn or back up and retry if it is more than 10 cm or 10° off the taught crossing. Under localization noise, with path, gait schedule, and sensing unchanged, this raises the share of disturbed ledge crossings that stay within these limits from 24.1% to 88.6%. In contact simulation with our learned policies, a robot pushed off course before stairs never falls in 180 climbs, against 9 falls when the stored direction is ignored; pushed 1.2 m away, it rejoins the route, ending on average 0.14 m from it (1.10 m without rejoining), and finishes as often as an undisturbed robot. This suits any robot with fixed skills that repeats a route over terrain transitions, as in inspection and patrol, where one wrong entry can end the task. We deployed it in competition on a real wheeled-legged robot: over 271 m of multi-obstacle terrain spanning 7.0 m of elevation, it completed all six runs, won third place at the 2026 Global Open-source AI Challenge, which drew 2,999 submissions, and was the only finalist in its task to finish fully autonomously.

</details>

---

### [[20_Research/Papers/具身智能/DMT-Attack_Diffusion-Prior_Texture_Search_for_Closed-Loop_Vision-Language-Action_Policies|DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies]]

![[assets/2611.25695_figure.png|800]]

- **arXiv**: [2611.25695](https://arxiv.org/abs/2611.25695)
- **PDF**: https://arxiv.org/pdf/2611.25695
- **详细分析**: [[20_Research/Papers/具身智能/DMT-Attack_Diffusion-Prior_Texture_Search_for_Closed-Loop_Vision-Language-Action_Policies|DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies]]
- **作者**: Jun Xia, Shangwen Wang, Jun Ma, Ruichao Ren, Zhouyang Jia, Xin Zhao, Huijun Liu, Jie Yu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks. However, optimized patterns can stand out from their surroundings, making an attack easier to notice and its carrier more likely to be inspected or removed. To address this limitation, our key insight is to search the structured image distribution of a diffusion model for natural-looking textures while using closed-loop feedback to identify task-disruptive candidates. Based on this idea, we propose DMT-Attack, a gradient-free gray-box attack that generates textures for ordinary scene objects such as tablecloths. A frozen text-conditioned diffusion model defines the search space, and an eight-expert latent proposal network is initialized from evaluated teacher latents and refined using rollout feedback. We evaluate DMT-Attack against pi_0.5 and OpenVLA-OFT across four LIBERO suites. DMT-Attack achieves a macro clean-conditioned attack success rate (cASR) of 57.9%, compared with 44.7% for UPA-RFAS and 19.7% for random natural textures. It also attains higher scene similarity and a lower clean-calibrated detector flag rate (45% versus 97.5-100% for optimized patch baselines). These results demonstrate that natural-looking textures can disrupt VLA visual feedback and closed-loop decision-making, motivating defenses that jointly assess visual appearance and task behavior.

</details>

---

### [[20_Research/Papers/强化学习/TipDex-VTLA_Learning_When_to_Refine_Actions_with_Touch_for_Dexterous_Manipulation|TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation]]

![[assets/2611.25683_figure.png|800]]

- **arXiv**: [2611.25683](https://arxiv.org/abs/2611.25683)
- **PDF**: https://arxiv.org/pdf/2611.25683
- **详细分析**: [[20_Research/Papers/强化学习/TipDex-VTLA_Learning_When_to_Refine_Actions_with_Touch_for_Dexterous_Manipulation|TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation]]
- **作者**: Xudi Ge, Yepeng Liu, Haifeng Liu, Enze Shi, Liangqi Zhang, Yongchao Xu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《TipDex-VTLA: Learning When to Refine Actions with Touch for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AT-VLA, BAS-VLA, E-VLA, ForceVLA, ForeTac-VLA, ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Changes in illumination can induce action drift in dexterous manipulation even when the physical state remains unchanged. Although existing vision--tactile--language--action (VTLA) policies incorporate tactile feedback, when and how touch refines actions under changing visual conditions remains challenging. We introduce \textbf{TipDex-VTLA}, a VTLA policy that combines estimated visual action reliability and tactile forecast verification to regulate execution-time refinement. Specifically, Visual Action Sensitivity Estimation (VASE) learns visual reliability from a frozen reference policy's action sensitivity to illumination perturbations. Tactile Anticipation and Correction during Execution (TACE) compares predicted and measured touch at matched times and combines the resulting discrepancy with visual reliability to gate bounded feature corrections for unexecuted actions. This effectively helps to refine actions under challenging unseen visual conditions. We evaluate TipDex-VTLA on four real-world dexterous manipulation tasks and the UniVTAC simulation benchmark. TipDex-VTLA trained on data collected under normal visual conditions, achieves average full-task success rates of 87.5% (resp. 73.8%) under normal (resp. challenging unseen) lighting in real-world tasks, significantly outperforming some state-of-the-art methods. We will release the collected data and source code.

</details>

---

### [[20_Research/Papers/强化学习/SiliconGym_A_Versatile_Reinforcement_Learning_Environment_for_Agentic_EDA|SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA]]

![[assets/2611.25658_first_page.png|800]]

- **arXiv**: [2611.25658](https://arxiv.org/abs/2611.25658)
- **PDF**: https://arxiv.org/pdf/2611.25658
- **详细分析**: [[20_Research/Papers/强化学习/SiliconGym_A_Versatile_Reinforcement_Learning_Environment_for_Agentic_EDA|SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA]]
- **作者**: Hejia Zhang, Sheng Lu, Yitong Ma, Zhongming Yu, Zhijing Wu, Wentao Ni, Chia-Tung Ho, Jishen Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ArchGym, CompilerGym, CorrectBench, EDA-RL, EDAFlowQA, HWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) with electronic design automation (EDA) feedback is advancing large language models for hardware design and verification. Extending these gains to hardware-engineering agents requires environments that span tasks, preserve state across tool calls, and support large hierarchies alongside parallel rollouts. We present SiliconGym, the first versatile, cross-task and cross-toolchain RL environment for hardware design and verification. By decoupling versioned workspaces, budgeted execution, and acceptance-gated scoring, SiliconGym scales from module-level RTL, testbench, and PPA tasks to multi-round repository repair and full-hierarchy SoC flows. Streaming dispatch overlaps tool checks with generation, finishing a 256-answer RL batch 21.9% faster than native ChipSeek. Using interchangeable open-source and commercial backends, we show that open-source-trained functional correctness transfers cleanly to commercial simulation, while paired netlist evaluation reveals when open-source PPA gains survive commercial synthesis.

</details>

---

### [[20_Research/Papers/具身智能/A$^2$-VLA_Adapting_Vision-Language-Action_Policies_to_New_Tools_through_Agentic_Affordance_Discovery|A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery]]

![[assets/2611.25656_figure.png|800]]

- **arXiv**: [2611.25656](https://arxiv.org/abs/2611.25656)
- **PDF**: https://arxiv.org/pdf/2611.25656
- **详细分析**: [[20_Research/Papers/具身智能/A$^2$-VLA_Adapting_Vision-Language-Action_Policies_to_New_Tools_through_Agentic_Affordance_Discovery|A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery]]
- **作者**: Chenyuan Zhou, Chaoyi Huang, Zibo Wang, Zhiyuan Li, Yong-Lu Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.7，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：A2-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with a VLA policy. It treats tool affordances as hypotheses the agent can construct, test, and revise. Given teleoperated demonstrations with a few source tools, the agent reconstructs the scenes in simulation and autonomously determines task-relevant affordance features: functional regions and their key geometric properties. It develops affordance-extraction skills and refines both the features and skills through autonomous experiments in the reconstructed scenes. Validated extraction skills accumulate in a reusable skill library for unseen tools. Finally, A$^2$-VLA uses encoded functional-region features as conditioning inputs to a $π_{0.5}$ backbone during training and inference. Evaluation examines affordance reliability in reconstructed scenes and real-robot task success on unseen tools. Our method achieves 86.1% success in simulated cross-tool trajectory retargeting based on affordances. On three real-robot tool-use tasks, A$^2$-VLA improves task success by 30.7 percentage points over $π_{0.5}$.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Easy_Clients_Difficulty-_and_Improvement-Aware_Aggregation_for_Federated_Reinforcement_Learning_in_Robot_Navigation|Beyond Easy Clients: Difficulty- and Improvement-Aware Aggregation for Federated Reinforcement Learning in Robot Navigation]]

![[assets/2611.25637_figure.png|800]]

- **arXiv**: [2611.25637](https://arxiv.org/abs/2611.25637)
- **PDF**: https://arxiv.org/pdf/2611.25637
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Easy_Clients_Difficulty-_and_Improvement-Aware_Aggregation_for_Federated_Reinforcement_Learning_in_Robot_Navigation|Beyond Easy Clients: Difficulty- and Improvement-Aware Aggregation for Federated Reinforcement Learning in Robot Navigation]]
- **作者**: Ye Lin Tun, Chu Myaet Thwal, Eui-Nam Huh, Choong Seon Hong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 1.2，强化学习 0.8，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Beyond Easy Clients: Difficulty- and Improvement-Aware Aggregation for Federated Reinforcement Learning in Robot Navigation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FGRL, FRL, LFRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated reinforcement learning enables a fleet of robots to jointly learn a shared navigation policy without exchanging raw experience. In practice, however, the robots rarely operate in the same conditions: an open aisle is far easier to navigate than a cluttered room, and takes less learning to master. Standard federated aggregation rules ignore this. Uniform averaging weights every client equally, whether or not it is still learning, and weighting by episode return is worse, since easy environments permit high returns by construction. Both failures stem from what we call the \emph{plateau problem}: once a client masters its environment, its updates carry little new information even though its reported return remains high. We propose \emph{FedDIA}, which scores each client by how much its local training improves the global model it received, amplified by the difficulty of its environment. Difficulty is inferred from the model's own performance, without requiring any description of the environment. Both signals are measured against the global model, so they are comparable across clients. On a mapless navigation task with eight heterogeneous clients, FedDIA reaches a mean success rate of $75.5\%$ across training and held-out environments, against $68.7\%$ for the strongest federated baseline. Its advantage holds when the models are transferred to hand-authored warehouse and living-space layouts, or when one of the clients is defective.

</details>

---

### [[20_Research/Papers/大模型/Decision-Focused_Reinforcement_Learning_for_LLM_Post-Training|Decision-Focused Reinforcement Learning for LLM Post-Training]]

![[assets/2611.25597_figure.png|800]]

- **arXiv**: [2611.25597](https://arxiv.org/abs/2611.25597)
- **PDF**: https://arxiv.org/pdf/2611.25597
- **详细分析**: [[20_Research/Papers/大模型/Decision-Focused_Reinforcement_Learning_for_LLM_Post-Training|Decision-Focused Reinforcement Learning for LLM Post-Training]]
- **作者**: Haotian Zhai, Leqi Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Decision-Focused Reinforcement Learning for LLM Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DFRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have shown promise as predictors across various tasks, benefiting from their ability to use information from unstructured context. However, when predictions serve as parameters of downstream optimization problems, higher prediction accuracy does not necessarily translate into lower decision costs. We propose decision-focused reinforcement learning (DFRL), a framework for post-training LLMs to predict optimization parameters using negative downstream decision regret as reward. DFRL trains LLM predictors to minimize the costs of the decisions induced by their predictions, without requiring downstream convexity or differentiability, and integrates readily into existing RL post-training frameworks. To address expensive reward evaluation, we develop two approaches. Heuristic warm-starting uses inexpensive approximate rewards during an initial phase before switching to refinement with exact rewards. Reward correction combines inexpensive estimates with randomized exact evaluations, preserving the expected policy gradient while reducing the expected number of exact solves per update. Experiments on three synthetic optimization problems demonstrate improvements over prediction-loss baselines, while a larger knapsack experiment shows faster early improvement under short training budgets. On inventory planning with H&amp;M transactions and product descriptions, our best configuration, in which the LLM reasons before predicting, reduces regret by 31.4% relative to the SFT baseline and 12.4% relative to the strongest evaluated conventional forecasting baseline.

</details>

---

### [[20_Research/Papers/世界模型/Bradley-Terry_Training_Can_Distort_Outcome_Probabilities_of_Initially_Accurate_Language_World_Models|Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models]]

![[assets/2611.25594_figure.png|800]]

- **arXiv**: [2611.25594](https://arxiv.org/abs/2611.25594)
- **PDF**: https://arxiv.org/pdf/2611.25594
- **详细分析**: [[20_Research/Papers/世界模型/Bradley-Terry_Training_Can_Distort_Outcome_Probabilities_of_Initially_Accurate_Language_World_Models|Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models]]
- **作者**: Xinze Shi, Litian Zhang, Zhenjie Su, Zelong Yu, Yuting Zhang, Qihua Feng, Zifeng Kang, Chaozhuo Li, Zhengxuan Hu
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 0.96，机器人 0.2）
- **关联关键词**: Robotics

#### 研究背景与动机

《Bradley-Terry Training Can Distort Outcome Probabilities of Initially Accurate Language World Models》归入 世界模型、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Comparative feedback, in which a judge says which of two candidate outcomes is closer to what happened, is a practical way to train language world models that assign probabilities to an action's outcomes. We show that, fitted with a Bradley-Terry objective, it need not teach the true outcome probabilities and can distort accurate ones. On a simulated robot push with enumerated outcome distributions, this objective takes a model that is accurate on unseen layouts (hazard error 2.4 percentage points, pp) and moves 33 to 43 pp of its probability onto outcomes that none of a condition's enumerated branches produces. The cause is the objective, not the comparisons: its optimum, computed before training, predicts where the model ends up, and a likelihood that knows the judge's rule learns from the same comparisons without the shift. The shift is robust: it recurs on unseen conditions, under five candidate laws and a three-fold denser enumeration, and about 29 pp remain without the physically impossible events. Its cost is conditional: with those events it inflates hazard probabilities, and a threshold inherited from the pre-feedback model costs about 3 pp of utility per decision on trained and 1 to 2 pp on unseen conditions, through false rejects; without them the utility loss averages below 1 pp over six seeds, though a small regret in action choice remains. Audits of readout, response and decision trace the effect from probabilities to actions.

</details>

---

### [[20_Research/Papers/大模型/DriftGuard_Online_Memory-Drift_Detection_via_Causal_Attribution_for_LLM_Agents|DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents]]

![[assets/2611.25583_figure.png|800]]

- **arXiv**: [2611.25583](https://arxiv.org/abs/2611.25583)
- **PDF**: https://arxiv.org/pdf/2611.25583
- **详细分析**: [[20_Research/Papers/大模型/DriftGuard_Online_Memory-Drift_Detection_via_Causal_Attribution_for_LLM_Agents|DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents]]
- **作者**: Licheng Pan, Yuzhou Chen, Zhixuan Chu, Yichen Sun, Han Zheng, Zhiyu Wang, Hao Wang, Yan Wang, Bingyu Zhu, Haiwen Hong, Longtao Huang, Kui Ren
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HarmBench, MPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attribution, as perplexity or retrieval relevance alone cannot determine which retrieved memory would change agent behavior if neutralized; (2) Counterfactual attribution is prohibitively expensive for online detection, as it requires replaying downstream agent and tool execution for each candidate memory, exceeding real-time serving budgets. To address these challenges, we propose DriftGuard, a two-stage framework that decouples offline causal supervision from online estimation. Specifically, DriftGuard first constructs causal supervision through repeated paired counterfactual replays, continuing the original and single-memory neutralized trajectory suffixes from a shared pre-action state. The resulting annotations are aggregated by component-wise majority voting into a memory drift score (MDS) that captures action change, attack removal, violation removal, and task recovery. Guided by this supervision, DriftGuard then learns an online risk model that estimates MDS from pre-action information and flags drift-inducing memories via its maximum component risk, without online counterfactual rollouts. Extensive experiments demonstrate that DriftGuard accurately identifies drift-inducing memories and enables efficient online defense. Code is available at https://anonymous.4open.science/r/DriftGuard-7F0B.

</details>

---

### [[20_Research/Papers/大模型/AutoRAGBench_A_Benchmark_for_LLM_Agents_Automating_RAG_System_Development|AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development]]

![[assets/2611.25582_figure.png|800]]

- **arXiv**: [2611.25582](https://arxiv.org/abs/2611.25582)
- **PDF**: https://arxiv.org/pdf/2611.25582
- **详细分析**: [[20_Research/Papers/大模型/AutoRAGBench_A_Benchmark_for_LLM_Agents_Automating_RAG_System_Development|AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development]]
- **作者**: Hang Zhang, Yuzhi Pan, Ziyao Zhong, Chaokun Wang, Shuo Cao, Zeyu Huang, Yue Xue, Fang Niu, Bofan Xie, Guanchen Ge, Zecheng Li, Leqi Zheng...
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.55（加权：大模型 1.55）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AutoRAGBench, HotpotQA, PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.

</details>

---

### [[20_Research/Papers/具身智能/FlashX_Scaling_Robotic_Experience_Reuse_for_Embodied_Agents_with_CBA-Based_NAND_Flash|FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash]]

![[assets/2611.25580_figure.png|800]]

- **arXiv**: [2611.25580](https://arxiv.org/abs/2611.25580)
- **PDF**: https://arxiv.org/pdf/2611.25580
- **详细分析**: [[20_Research/Papers/具身智能/FlashX_Scaling_Robotic_Experience_Reuse_for_Embodied_Agents_with_CBA-Based_NAND_Flash|FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash]]
- **作者**: Yuseon Choi, Sanghyeon Park, Eunjong Lee, Hanseo Lee, Sangjin Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.6（加权：具身智能 2.1，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《FlashX: Scaling Robotic Experience Reuse for Embodied Agents with CBA-Based NAND Flash》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents are emerging as a promising paradigm for complex robotic tasks, leveraging Vision-Language-Action (VLA) and World Action Models (WAMs) to generate actions through Diffusion Transformer (DiT)-based iterative denoising. However, existing models often struggle to generalize to out-of-distribution (OOD) environments. We observe that retrieving successful experiences and using them to warm-start denoising enables agents to better adapt to unfamiliar situations while reducing computational overhead. This creates a new opportunity to improve task accuracy and inference efficiency simultaneously, in contrast to conventional acceleration techniques that trade accuracy for computation. However, realizing this opportunity requires scaling experience banks, introducing substantial storage and search overhead that challenges the capacity, bandwidth, and power constraints of edge systems. We propose FlashX, a CMOS Directly Bonded to Array (CBA)-based NAND flash architecture for scalable experience reuse in embodied agents. FlashX exploits CBA's high internal bandwidth for parallel pSLC key search, employing interleaved Compute-in-Flash (CIF) engines to sustain sensing throughput while retaining dense TLC latent storage. Proprioception-aware clustering further reduces search overhead and enables incremental experience acquisition without global reclustering. Evaluations across VLA and WAM workloads demonstrate up to 12.24\%p and 7.43\%p improvements in task success under dense and compute-efficient configurations, respectively. FlashX achieves 2.57$\times$ higher search throughput than the strongest prior NAND search architecture under pSLC sensing, with a further 9.7$\times$ search reduction through clustering. This delivers 1.29--3.95$\times$ end-to-end speedup and 1.12--2.34$\times$ energy efficiency improvement over SSD-based retrieval.

</details>

---

### [[20_Research/Papers/具身智能/Efficient_Multimodal_Agents_for_Auditing_3D_Worlds|Efficient Multimodal Agents for Auditing 3D Worlds]]

![[assets/2611.25543_figure.png|800]]

- **arXiv**: [2611.25543](https://arxiv.org/abs/2611.25543)
- **PDF**: https://arxiv.org/pdf/2611.25543
- **详细分析**: [[20_Research/Papers/具身智能/Efficient_Multimodal_Agents_for_Auditing_3D_Worlds|Efficient Multimodal Agents for Auditing 3D Worlds]]
- **作者**: Jingbo Yang, Ziyan Jiang, Li An, Jiabao Ji, Yujian Liu, Tommi Jaakkola, Yang Zhang, Shiyu Chang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Efficient Multimodal Agents for Auditing 3D Worlds》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：A-EQA, GBQA, WorldAuditBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal agents can now build interactive 3D worlds and games, yet these worlds, like those built by people, often contain glitches such as floating objects, walls that can be walked through, or objects that change when no one is looking. An automatic auditor could check such worlds at scale and provide rewards for agents that build them, but only if it is both accurate and cheap. Auditing requires three abilities, namely navigating to the objects that may contain a glitch, triggering glitches that appear only after a specific behavior, and recognizing what is wrong. Current auditors are either accurate but slow and expensive or cheap but unreliable. We study how much of the audit small models can take on. A 4B vision language model fine-tuned end to end on verified trajectories of a frontier teacher guided by Bayesian search learns to navigate and trigger, and six such explorers together match a frontier model on both, but recognition stays far behind. We therefore build an auditor in which a swarm of small explorers navigates and triggers, and a frontier model reviews what they record and report. On WorldAuditBench, our auditor succeeds on 55.9% of 213 tasks in Unreal Engine 5 and Three.js worlds, 13.6 points above the strongest auditor reported, at less than a quarter of its cost. It matches the frontier reviewer exploring on its own at 4.6 times lower cost and about half the latency. Without further training, it also answers embodied questions about real-world scans, matching the frontier reviewer exploring on its own and surpassing four other frontier models by 6.4 to 16.6 points.

</details>

---

### [[20_Research/Papers/具身智能/CoachSI_Self-Improvement_of_Robot_Policies_with_a_Language_Coach|CoachSI: Self-Improvement of Robot Policies with a Language Coach]]

![[assets/2611.25529_figure.png|800]]

- **arXiv**: [2611.25529](https://arxiv.org/abs/2611.25529)
- **PDF**: https://arxiv.org/pdf/2611.25529
- **详细分析**: [[20_Research/Papers/具身智能/CoachSI_Self-Improvement_of_Robot_Policies_with_a_Language_Coach|CoachSI: Self-Improvement of Robot Policies with a Language Coach]]
- **作者**: Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《CoachSI: Self-Improvement of Robot Policies with a Language Coach》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies execute atomic skills reliably but fail when the same skills are composed into long-horizon tasks. Self-improvement from the policy's own experience does not close this gap: experience collected by the policy alone stays within its own distribution and reproduces what it can already do. We show that what the policy lacks is not a skill but the next step. We present CoachSI, a self-improvement method in which a frozen, off-the-shelf vision-language model (VLM) coaches the policy in language: it watches the robot and names the next step in the format of the policy's atomic instructions, and never outputs an action. Successful coached rollouts are relabeled in hindsight with the original task instruction and used to fine-tune the policy. The fine-tuned policy is then deployed on its own. On states where a World Action Model and a Vision-Language-Action model have stalled, naming the next step raises subgoal completion by 4.6x over the unchanged task instruction, and the frozen VLM supplies it from the same camera images the policy sees. After fine-tuning, unassisted success on long-horizon tasks in unseen scenes rises from 47.4% to 59.3%, 9.8 points above fine-tuning on human demonstrations and 7.3 points above fine-tuning on self-collected successes at an equal data budget. With a coach that sees only camera images, it reaches 56.8%, above both baselines. The gain is obtained with the action backbone frozen: language coaching teaches the policy what should happen next, and the skills it already has do the rest.

</details>

---

### [[20_Research/Papers/具身智能/Demonstration-Free_Skill_Composition_for_Navigation_and_Manipulation|Demonstration-Free Skill Composition for Navigation and Manipulation]]

![[assets/2611.25462_figure.png|800]]

- **arXiv**: [2611.25462](https://arxiv.org/abs/2611.25462)
- **PDF**: https://arxiv.org/pdf/2611.25462
- **详细分析**: [[20_Research/Papers/具身智能/Demonstration-Free_Skill_Composition_for_Navigation_and_Manipulation|Demonstration-Free Skill Composition for Navigation and Manipulation]]
- **作者**: Madeleine Nouri, Gelareh Mohammadi, Francisco Cruz
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Demonstration-Free Skill Composition for Navigation and Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical reinforcement learning enables sequential tasks to be represented as compositions of separately trained skills. This paper evaluates demonstration-free hierarchical pipelines for MiniGrid navigation and robotic manipulation, comparing their training requirements and task performance with flat reinforcement learning baselines. The evaluation concerns complete pipelines with task-specific observation, reward and control structures. In navigation, two parameterised skills are reused across unseen FourRooms layouts under manually specified high-level plans. In manipulation, reaching, grasp alignment and lifting are trained separately, with downstream skills initialised from states collected during predecessor rollouts. Across unseen navigation layouts, the hierarchical pipeline substantially outperforms the evaluated flat DQN baselines while requiring fewer training interactions. In manipulation, the hierarchical chain requires fewer training steps than flat SAC and exhibits lower observed variation across seeds. The frozen Pick and Lift skills are further reused for stacking by training an additional Place skill.

</details>

---

### [[20_Research/Papers/具身智能/LoongForge-Embodied_A_Unified_Framework_for_Training_Heterogeneous_Embodied_Models|LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models]]

![[assets/2611.25460_figure.png|800]]

- **arXiv**: [2611.25460](https://arxiv.org/abs/2611.25460)
- **PDF**: https://arxiv.org/pdf/2611.25460
- **详细分析**: [[20_Research/Papers/具身智能/LoongForge-Embodied_A_Unified_Framework_for_Training_Heterogeneous_Embodied_Models|LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models]]
- **作者**: LoongForge Team
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.8，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LoongForge-Embodied: A Unified Framework for Training Heterogeneous Embodied Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training Vision-Language-Action (VLA) models and World-Action Models (WAMs) is computationally expensive, while their heterogeneous architectures and fragmented training stacks make system optimizations difficult to reuse across models. To address these challenges, we present LoongForge-Embodied, a native-PyTorch framework that unifies and accelerates the training of heterogeneous embodied models. At its core, LoongForge-Embodied introduces a common abstraction layer that decouples model-specific implementations from shared training infrastructure, enabling cross-model reuse without constraining individual architectures or execution requirements. Buildingon this unified infrastructure, the framework combines reusable acceleration mechanisms with model-specific and hardware-aware optimization strategies across computation, execution, memory, data I/O, and distributed communication, including FP8-based communication optimizations for DDP and FSDP. Beyond training acceleration, LoongForge-Embodied integrates a unified data infrastructure with a pipeline for synthesizing robot data from egocentric data, and an efficient evaluation framework that supports concurrency and optimized computation in simulator. Experiments across representative VLA and WAM models demonstrate 1.47x-4.38x end-to-end training throughput improvements over their corresponding open-source baselines, as well as 4.1x-23.2x faster evaluation under the same protocols.

</details>

---

### [[20_Research/Papers/具身智能/Dune_A_Zeroth-Order_Optimizer_with_Time-Conditioned_Historical_Error_Regression_for_VLA_Test-Time_Adaptation|Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation]]

![[assets/2611.25400_figure.png|800]]

- **arXiv**: [2611.25400](https://arxiv.org/abs/2611.25400)
- **PDF**: https://arxiv.org/pdf/2611.25400
- **详细分析**: [[20_Research/Papers/具身智能/Dune_A_Zeroth-Order_Optimizer_with_Time-Conditioned_Historical_Error_Regression_for_VLA_Test-Time_Adaptation|Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation]]
- **作者**: Chengyang Dong, Ze Chen, Kai Ye, Chutian Wang, Heng Xu, Wei Mo, Maomao Li, Jiayan Xu, Jiayuan Wu, Yihao Xiao, Linhua Ye, Zhonghua Peng...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-Time Adaptation (TTA) enables Vision-Language-Action (VLA) models to handle distribution shifts during deployment without source-domain retraining. However, backpropagation-based adaptation incurs heavy memory overhead on resource-constrained robots, whereas zeroth-order (ZO) methods suffer from high estimation variance under limited perturbation budgets. We observe that while ZO estimation enables low-memory adaptation with rapid initial gains, it often stalls or degrades over long-horizon updates due to noisy gradient estimates. To address these limitations, we propose Dune, a zeroth-order optimizer that stabilizes long-horizon adaptation by coupling online historical error prediction with current perturbation observations. Specifically, Dune learns a lightweight, time-conditioned error predictor from past optimization dynamics and fuses its predictions with instantaneous ZO estimates, achieving effective variance reduction without backpropagation or extra forward passes. Additionally, we theoretically characterize how estimation variance restricts convergence in high-dimensional, small-population regimes, motivating the use of historical statistics. Extensive experiments on LIBERO and real-world robots demonstrate that Dune achieves superior success rates under a low memory footprint, with ablations confirming improved closed-loop stability and post-disturbance recovery.

</details>

---

### [[20_Research/Papers/大模型/Pro$^2$_Agent_Scientific_Problem_Probing_for_Autonomous_AI_R&D|Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D]]

![[assets/2611.25357_figure.png|800]]

- **arXiv**: [2611.25357](https://arxiv.org/abs/2611.25357)
- **PDF**: https://arxiv.org/pdf/2611.25357
- **详细分析**: [[20_Research/Papers/大模型/Pro$^2$_Agent_Scientific_Problem_Probing_for_Autonomous_AI_R&D|Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D]]
- **作者**: Yixiong Chen, Liqian Peng, Tian Tan, Ziqian Lin, Blake Jianhang Chen, Chao Zhao, Yaojie Liu, Alec Go, Alan Yuille
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MLE-Bench, PostTrainBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents can now autonomously conduct AI research by writing code and running experiments. They typically do so by iteratively optimizing a codebase, while ignoring the problem structure behind the task. This formulation is effective on simpler tasks, but on difficult problems it often gets stuck in the wrong solution region because the agent never explicitly represents its understanding of the problem. We introduce Pro$^2$ Agent, which shifts the primary state of autonomous AI research from a codebase state to a Problem State: an explicit structure of what problems prevent success and which solutions are likely to address them. Pro$^2$ Agent initializes the Problem State through comprehensive analysis of available resources and constraints. It then performs targeted research to relate the identified problems to candidate solutions. Through controlled hypothesis testing, the agent updates the importance of a suspected problem or the benefit brought by a candidate solution. On the complete MLE-Bench, Pro$^2$ Agent matches the best reported medal rate (70.7%) under the standard 24-hour budget and reaches 76.0% with a 48-hour budget, the highest medal rate reported on the complete benchmark. It also achieves competitive performance on PostTrainBench. In addition, it produces research notes for each task that make the research process transparent and reusable by human researchers.

</details>

---

### [[20_Research/Papers/大模型/Keel_A_Frontier_Model_Teaches_a_Vision-Language_Model_by_Rewriting_Its_Weights|Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights]]

![[assets/2611.25257_figure.png|800]]

- **arXiv**: [2611.25257](https://arxiv.org/abs/2611.25257)
- **PDF**: https://arxiv.org/pdf/2611.25257
- **详细分析**: [[20_Research/Papers/大模型/Keel_A_Frontier_Model_Teaches_a_Vision-Language_Model_by_Rewriting_Its_Weights|Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights]]
- **作者**: Jiajun Fan, Neil He, Bangji Yang, Qinglong Zheng, Ziwen Wang, Chaoran Cheng, Changyi Yang, Hanqi Mao, Ge Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Keel: A Frontier Model Teaches a Vision-Language Model by Rewriting Its Weights》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HallBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can a frontier model repair a vision-language model (VLM) by rewriting its weights? Small reasoning VLMs such as Qwen3.5 need such a repair: in thinking mode they fall into loops on many image questions, repeating themselves until the token limit, spending the whole budget and losing the answer. The usual remedies act on the decoding, leaving the looping model as it was, or must be told what to change. Yet the cause is written in the weights. Keel, the first agentic weight-editing method for VLMs on image tasks, finds and removes it there. Told only the symptom, an editor, a frontier multimodal LLM acting as an agent, locates the cause, edits the weights and tests them, with a failure census and instruments showing it the failing images and where the VLM attends; among several editors, the harness keeps only edits that clearly reduce the failure without lowering accuracy on questions no editor saw. The repair needs no training, keeps the model's size and per-token cost, and applies to already-edited weights. The editors expose where the loops live: from the original weights, independent editors on both models trace them to the attention outputs of the middle layers, and the smaller VLM stops consulting the image inside a loop. On Qwen3.5-0.8B and Qwen3.5-2B, across six image benchmarks from visual mathematics to GUI grounding, the edit removes most loops on every benchmark and shortens answers, and the edited models are significantly more accurate than the thinking models on average; the larger one gains most on GUI grounding, a task absent from the practice questions. Because the repair lives in the weights, it combines with budget forcing where held-out questions favor it: on the best available weights, Keel has the best average accuracy on both models, significantly above every training-free baseline we compare on the larger one.

</details>

---

### [[20_Research/Papers/具身智能/Plan_your_Self-Adaptation!_Ontology-Mediated_Task_and_Architecture_Co-adaptation_Planning_for_Robots|Plan your Self-Adaptation! Ontology-Mediated Task and Architecture Co-adaptation Planning for Robots]]

![[assets/2611.25254_first_page.png|800]]

- **arXiv**: [2611.25254](https://arxiv.org/abs/2611.25254)
- **PDF**: https://arxiv.org/pdf/2611.25254
- **详细分析**: [[20_Research/Papers/具身智能/Plan_your_Self-Adaptation!_Ontology-Mediated_Task_and_Architecture_Co-adaptation_Planning_for_Robots|Plan your Self-Adaptation! Ontology-Mediated Task and Architecture Co-adaptation Planning for Robots]]
- **作者**: Gustavo Rezende Silva, Tobias John, Francisco Martín, EinarR Broch Johnsen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Plan your Self-Adaptation! Ontology-Mediated Task and Architecture Co-adaptation Planning for Robots》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots may need to adapt both their task plans and architectural configurations as operating conditions change. These decisions are interdependent: architectural configurations determine which actions a robot can perform, while task plans determine which capabilities are required. This paper presents PLANTA, an ontology-mediated approach to task and architecture co-adaptation that considers these dependencies during mission planning. PLANTA uses an ontology expressed in the Web Ontology Language to represent architectural alternatives and their associated functional and quality requirements, while the Planning Domain Definition Language defines task actions and mission goals. By automatically translating and integrating these models, PLANTA enables joint planning of task and reconfiguration actions. The approach uses satisficing planning and replans when changes during execution invalidate the current plan. PLANTA is evaluated in two robotic scenarios involving underwater inspection and ground navigation. The results support the feasibility of runtime co-adaptation and show lower planning time and memory consumption compared with optimal-policy generation in the evaluated navigation scenario, while producing plans of similar quality.

</details>

---

### [[20_Research/Papers/具身智能/Bridging_vision-language_reasoning_and_learned_control_for_legged_navigation_in_the_wild|Bridging vision-language reasoning and learned control for legged navigation in the wild]]

![[assets/2611.25215_figure.png|800]]

- **arXiv**: [2611.25215](https://arxiv.org/abs/2611.25215)
- **PDF**: https://arxiv.org/pdf/2611.25215
- **详细分析**: [[20_Research/Papers/具身智能/Bridging_vision-language_reasoning_and_learned_control_for_legged_navigation_in_the_wild|Bridging vision-language reasoning and learned control for legged navigation in the wild]]
- **作者**: Takahiro Miki, Robin Schmid, Manthan Patel, Turcan Tuna, Julia Richter, Julian Nubert, Joonho Lee, Matthias Müller, Marco Hutter
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.3，强化学习 0.2，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Bridging vision-language reasoning and learned control for legged navigation in the wild》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous navigation in diverse real-world environments remains one of the greatest challenges in robotics. It demands both robust low-level motion control to handle diverse terrain and high-level reasoning to interpret environmental cues. We present ROAM (Robust Open-world Autonomous Mobility), a system that enables legged robots to perform kilometer-scale navigation in complex alpine and urban settings. ROAM combines the world knowledge of a Vision-Language Model (VLM), pre-trained on internet-scale data, with robust locomotion and local planning policies learned in simulation via reinforcement learning (RL). The VLM provides common-sense reasoning and semantic interpretation of the scene, assessing risks, interpreting signs, and producing semantic labels with associated navigation costs. An open-vocabulary segmentation module converts these labels into a dense, real-time risk map, which conditions two pre-trained RL policies responsible for agile locomotion and local navigation, effectively coupling high-level VLM reasoning with low-level physical control. Real-world experiments showed the system's ability to autonomously navigate a wide range of complex real-world environments. The robot completes kilometer-long hikes with minimal intervention, interprets signs to avoid danger, and evaluates its environment to identify safe areas on which to step. This work represents a step toward the reliable deployment of systems in unstructured environments. However, it also underscores the challenges that remain in VLM reliability and spatial reasoning, indicating that foundational models are a crucial component but not yet a complete solution for navigation in the wild.

</details>

---

### [[20_Research/Papers/强化学习/VG-Steer_Visual-Geometric_Policy_Steering_from_In-Context_Aligned_Abstractions|VG-Steer: Visual-Geometric Policy Steering from In-Context Aligned Abstractions]]

![[assets/2611.25199_figure.png|800]]

- **arXiv**: [2611.25199](https://arxiv.org/abs/2611.25199)
- **PDF**: https://arxiv.org/pdf/2611.25199
- **详细分析**: [[20_Research/Papers/强化学习/VG-Steer_Visual-Geometric_Policy_Steering_from_In-Context_Aligned_Abstractions|VG-Steer: Visual-Geometric Policy Steering from In-Context Aligned Abstractions]]
- **作者**: Arthur Bucker, Pramod Anantharam, Jonathan Francis, Jean Oh
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VG-Steer: Visual-Geometric Policy Steering from In-Context Aligned Abstractions》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting robot policies to out-of-distribution (OOD) settings with limited real-world data remains a key bottleneck to generalist robots. The multimodality and scarcity of robotics data lead end-to-end approaches to overfit and break under small distribution shifts. Test-time adaptation can alleviate this by correcting frozen policies at inference, but most methods ground their correction in a signal learned implicitly from robotic datasets, making it susceptible to the same shifts as the policy it corrects. Recent methods that instead exploit explicit spatial information are typically limited to coarse corrections, missing the nuanced, task-relevant motion most manipulation tasks require. We propose VG-Steer, which corrects existing policies by transferring the nuanced motion of successful in-distribution rollouts, captured along meaningful geometric axes, known here as object-relational distance pairs. VG-Steer leverages the semantic understanding of Large Vision Models (LVMs) and Vision-Language Models (VLMs) reasoning, which combines the task-relevant entity pairs and their object-relational distance projections into a single tailored visual-geometric guidance signal. In a simulation benchmark, it efficiently corrects flow-matching policies under pose and task-goal shifts; on a real robot experiment, it widens the region of the workspace the frozen policy covers, more than doubling its success rate on cable placements one grid step outside the training positions, and steers a single-task policy toward objects it was never trained on while nearly eliminating object confusion. Project website: https://arthurfenderbucker.github.io/VG-Steer/

</details>

---

### [[20_Research/Papers/大模型/Forget_Freely,_Grep_Later_Lossless,_Index-Free_Memory_for_Long-Horizon_LLM_Agents|Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents]]

![[assets/2611.25123_first_page.png|800]]

- **arXiv**: [2611.25123](https://arxiv.org/abs/2611.25123)
- **PDF**: https://arxiv.org/pdf/2611.25123
- **详细分析**: [[20_Research/Papers/大模型/Forget_Freely,_Grep_Later_Lossless,_Index-Free_Memory_for_Long-Horizon_LLM_Agents|Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents]]
- **作者**: Ziyan Yang, Taiwei Shi, Jieyu Zhao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AMA-Bench, ContextBench, LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents often exceed their context windows, forcing them to discard information that may be needed later. Existing context management strategies rely on summarization, masking, or structured memory, requiring decisions about what to preserve or how to retrieve it before future needs are known. However, these methods can introduce lossy compression, potentially discarding details needed for future tasks. To address this limitation, we introduce GrepMem, a simple, lossless, and index-free memory mechanism built on two components: an append-only plain-text log of the agent's complete history and a regular-expression search tool for on-demand recall. Unlike structured memory systems, GrepMem requires no embeddings, retrieval index, memory extraction, or additional models. We train Qwen3.5-9B with reinforcement learning under five context management strategies and evaluate on multi-question research sessions, long-stream recall, and agent-trajectory question answering. GrepMem achieves 95-97% accuracy on ContextBench, versus at most 21% for lossy baselines, and outperforms SUPO's summarization by 8.8 percentage points on BCP-Multi. GrepMem scales effectively to increasingly long input streams while remaining on the accuracy-token-cost Pareto frontier across all five evaluation tasks. Our results show that a plain-text log and grep provide a simple but competitive approach to long-horizon agent memory, without requiring complex structured memory infrastructure.

</details>

---

### [[20_Research/Papers/具身智能/MAWAM_A_Multi-Agent_World-Action_Model_for_Coordinated_Manipulation|MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation]]

![[assets/2611.25105_figure.png|800]]

- **arXiv**: [2611.25105](https://arxiv.org/abs/2611.25105)
- **PDF**: https://arxiv.org/pdf/2611.25105
- **详细分析**: [[20_Research/Papers/具身智能/MAWAM_A_Multi-Agent_World-Action_Model_for_Coordinated_Manipulation|MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation]]
- **作者**: Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu, Yu-Cheng Chou, Johan Bjorck, Linxi "Jim" Fan, Jan Kautz, Yu-Chiang Frank Wang, Zhiding Yu, Hengshuang Zhao...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Gamma-World, MA-VLA, MultiWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the highest success on all three real-robot tasks (laundry-bag collection, bath-towel folding, and umbrella handover), with 67.8% mean success, 18.9 percentage points above MA-VLA trained on the same demonstrations and cameras. In simulation, MAWAM reaches 90.3% mean success on eight tasks with teams of up to four arms. Ablations show that cross-agent attention and team-stage future-video supervision both improve coordinated control: without attention, a four-arm relay falls from 95.0% to 39.0%, and without this supervision, Place Food falls from 78.0% to 47.0%.

</details>

---

### [[20_Research/Papers/大模型/LLM_Complexity_Towards_a_Computational_Complexity_View_of_Large_Language_Model_Inference|LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference]]

![[assets/2611.24943_figure.png|800]]

- **arXiv**: [2611.24943](https://arxiv.org/abs/2611.24943)
- **PDF**: https://arxiv.org/pdf/2611.24943
- **详细分析**: [[20_Research/Papers/大模型/LLM_Complexity_Towards_a_Computational_Complexity_View_of_Large_Language_Model_Inference|LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference]]
- **作者**: Yu-Hung Wu, Shao-Xiang Yuan, Chan-Hung Yu, Zih-Ching Chen, Kuan-Hao Huang, Shao-Hua Sun
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computational complexity theory offers a principled framework for characterizing the efficiency of computational problems, and Large Language Models (LLMs) can similarly be viewed as computational systems executing a structured process of input, inference-time compute, and output. In this context, the number of generated tokens emerges as a natural and directly observable proxy for inference-time compute. However, we show that the tempting analogy between LLM token length and classical time complexity does not hold. We disprove the hypothesis that inference-time token usage aligns monotonically with classical time complexity, demonstrating a fundamental divergence grounded in how LLMs actually allocate computation during inference. To this end, we introduce LLM Complexity, a new metric designed to quantify problem complexity from the perspective of LLMs by characterizing the area bounded above by the accuracy-token curve. We find that diverse LLMs induce highly consistent task rankings under LLM Complexity, indicating that the metric captures stable notions of difficulty across models. We leverage this property to construct an easy-to-hard curriculum for supervised fine-tuning, which improves accuracy while reducing token consumption. Finally, we demonstrate that LLM Complexity generalizes to real-world tasks, producing more stable cross-model correlations than human-annotated difficulty labels.

</details>

---
