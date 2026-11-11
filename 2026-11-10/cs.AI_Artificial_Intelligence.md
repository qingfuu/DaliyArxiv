# cs.AI | Artificial Intelligence | 2026-11-10

#arxiv #ComputerScience

**论文数**: 27

### [[20_Research/Papers/具身智能/$Σ$-LeWM_Learning_World_Models_via_S-Information_for_Robot_Control|$Σ$-LeWM: Learning World Models via S-Information for Robot Control]]

![[assets/2611.12732_figure.png|800]]

- **arXiv**: [2611.12732](https://arxiv.org/abs/2611.12732)
- **PDF**: https://arxiv.org/pdf/2611.12732
- **详细分析**: [[20_Research/Papers/具身智能/$Σ$-LeWM_Learning_World_Models_via_S-Information_for_Robot_Control|$Σ$-LeWM: Learning World Models via S-Information for Robot Control]]
- **作者**: Xinrui Zu, Michael Przystupa, Zhao Yang, Shujian Yu, Kevin Sebastian Luck
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习
- **相关性评分**: 3.52（加权：具身智能 0.9，强化学习 0.16，世界模型 1.16，机器人 1.3）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《$Σ$-LeWM: Learning World Models via S-Information for Robot Control》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have increasingly been applied as a model-based control method for robotics tasks such as manipulation and locomotion. While early world model architectures relied on decoders to prevent mode collapse and learn a predictable latent space, recent works on world models, such as Joint Embedding Predictive Architecture or LeWorldModel, increasingly aim to learn embeddings without a grounding decoder, utilising only a latent forward dynamics predictor and a stabilising entropy term. In this paper, we set out to demonstrate that the further introduction of two additional latent losses to LeWorldModel, a backward dynamics predictor and an inverse dynamics action predictor, enforces further structure on the latent embedding, leading to further gains in both performance and planning efficiency. These are critical properties for improving the applicability of such methods to real-time model-based control of real-world robots. We demonstrate these gains on standard world model benchmarks and two simulated robot manipulation tasks.

</details>

---

### [[20_Research/Papers/大模型/Safe_Reinforcement_Learning_for_Multi-Turn_Clinical_Agents_When_Dense_Rewards_Beat_Outcome_Rewards|Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards]]

![[assets/2611.12728_figure.png|800]]

- **arXiv**: [2611.12728](https://arxiv.org/abs/2611.12728)
- **PDF**: https://arxiv.org/pdf/2611.12728
- **详细分析**: [[20_Research/Papers/大模型/Safe_Reinforcement_Learning_for_Multi-Turn_Clinical_Agents_When_Dense_Rewards_Beat_Outcome_Rewards|Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards]]
- **作者**: Brendan P. Murphy, Agustina Saenz
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.97（加权：大模型 0.65，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Safe Reinforcement Learning for Multi-Turn Clinical Agents: When Dense Rewards Beat Outcome Rewards》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Pre-RL, SDBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards is increasingly used to improve language model reasoning, yet its effects on sequential decision procedures remain poorly understood. We study this problem in clinical multi-turn agents that must decide what information to request, when to stop gathering evidence, and which action to take. We introduce three controlled environments: medication refill triage, acute diagnostic work-up, and dosing titration, each with hidden clinical states, query costs, exact adaptive oracles, and deterministic outcome verifiers. Across these tasks, outcome-only group relative policy optimization often improves aggregate reward while producing undesirable procedures, including premature commitment, one-question collapse, and failures on rare high-risk cases. In diagnostics, assigning dense credit to questions that reduce uncertainty improves held-out value and moderate-case support across three training seeds relative to outcome-only reinforcement learning, without the high-risk seed collapse observed under outcome-only training. Separating exploration from exploitation further increases high-risk support at its best checkpoint, but at the cost of excessive information gathering on low-acuity cases. Additional experiments show that the optimal strength of process credit is task-dependent; that after a supervised warmup that already gathers carefully, reinforcement learning raises aggregate reward by trimming questions while degrading high-risk performance; and that reinforcement learning does not reliably repair rare behavior gaps inherited from biased supervised data. Verifiable final outcomes are therefore insufficient for training reliable multi-turn agents: reward design must account for the procedure used to reach an answer, and evaluation must distinguish adaptive information gathering from reward-exploiting shortcuts.

</details>

---

### [[20_Research/Papers/世界模型/Library_of_Hands_Fix_the_Hands,_Not_the_World_Model|Library of Hands: Fix the Hands, Not the World Model]]

![[assets/2611.12678_figure.jpg|800]]

- **arXiv**: [2611.12678](https://arxiv.org/abs/2611.12678)
- **PDF**: https://arxiv.org/pdf/2611.12678
- **详细分析**: [[20_Research/Papers/世界模型/Library_of_Hands_Fix_the_Hands,_Not_the_World_Model|Library of Hands: Fix the Hands, Not the World Model]]
- **作者**: Hasaan Ahmad, Qizhen Ying, Yuxuan Sun, Tianjin Huang, Guangming Wang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《Library of Hands: Fix the Hands, Not the World Model》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ShiftWM-Bench, SyncWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A world model predicts how a scene changes after an action, and a planner uses it to search for actions that reach a goal. If the camera moves or the controller changes, the same command moves the robot differently: when its commands are turned by 90 degrees, a frozen planner with the LeWM world model that succeeds in 77.5% of episodes succeeds in only 7.8%. Current fixes retrain the model, need training data, or forget a set-up when it returns. We propose Library of Hands (LoH), a training-free method that keeps the world model frozen and corrects only the map from commands to applied actions, which we call the hand. LoH reads the hand through the frozen model, with no extra sensor: it finds the action that best explains the change between two camera images (a reading). It stores every hand it identifies, so a returning set-up is recognised rather than re-learnt. In closed-loop tests, LoH more than doubles success on three simulated tasks, from 28.6% to 62.3%, and loses only 0.6 percentage points when nothing changes. It also works, unchanged, with two other world models and on two of three models pretrained on real robot data, and its gain grows with the quality of its readings.

</details>

---

### [[20_Research/Papers/大模型/UniOMA_Unified_Optimal-Transport_Multi-Modal_Structural_Alignment_for_Robot_Perception|UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception]]

![[assets/2611.12351_figure.png|800]]

- **arXiv**: [2611.12351](https://arxiv.org/abs/2611.12351)
- **PDF**: https://arxiv.org/pdf/2611.12351
- **详细分析**: [[20_Research/Papers/大模型/UniOMA_Unified_Optimal-Transport_Multi-Modal_Structural_Alignment_for_Robot_Perception|UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception]]
- **作者**: Xinrui Zu, Mark Hoogendoorn, Kevin Sebastian Luck, Shujian Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《UniOMA: Unified Optimal-Transport Multi-Modal Structural Alignment for Robot Perception》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MultiBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving generalizable and well-aligned multimodal representations remains a core challenge in robot learning. While recent approaches have attempted to align modalities by modeling conditional or higher-order statistical dependencies, they do not explicitly consider the structural coherence across modalities. In this work, we propose a novel multimodal alignment method that augments existing contrastive losses with a geometry-aware Gromov--Wasserstein (GW) distance-based regularization. To this end, we encode intra-modal geometry for each modality and reduce cross-modal structural discrepancies through a dynamically learned GW barycenter, thereby encouraging structural consistency in addition to instance-level contrastive alignment. We apply this optimal-transport-based alignment strategy to robot perception tasks involving underexplored modalities such as force and tactile signals, where modality data often exhibit varying sample densities. Extensive experiments on five robotic benchmarks show that our method improves structural alignment and downstream performance over state-of-the-art multimodal contrastive baselines across a wide range of downstream tasks, including robot and environment state prediction. Moreover, our GW-based regularization can be seamlessly integrated into most InfoNCE-like objectives.

</details>

---

### [[20_Research/Papers/世界模型/How_Many_Exposures_Does_a_World_Model_Need_Learning_Unseen_Game_Mechanics_at_Test_Time|How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time]]

![[assets/2611.12324_figure.png|800]]

- **arXiv**: [2611.12324](https://arxiv.org/abs/2611.12324)
- **PDF**: https://arxiv.org/pdf/2611.12324
- **详细分析**: [[20_Research/Papers/世界模型/How_Many_Exposures_Does_a_World_Model_Need_Learning_Unseen_Game_Mechanics_at_Test_Time|How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time]]
- **作者**: Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AdaWorld, AutumnBench, MechEval, ScratchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic that the model observes is one exposure. We ask how many exposures a world model needs to predict the effects of a new environment's mechanics. We address this question on ARC-AGI-3, a benchmark of interactive games defined by their programs. We introduce MechEval, which labels 69 recurring mechanics across 20 games from these programs. It scores each prediction on the cells the mechanic changes at each exposure. As a test bed, we build WARC (World model for ARC-AGI-3), a 35M-parameter vision transformer that is pretrained on other games and updates all of its parameters after each transition. On held-out games, WARC learns to predict four in five mechanics with at least 80% accuracy on the cells they change and keeps that accuracy to the end of the recordings. Half of them reach that accuracy within about 80 exposures, in a single play of the game, and without updates only one in seven does at all. In closed-loop play on the public games, WARC-Agent, which pairs WARC with a fixed graph explorer, triples the explorer's official efficiency score from 0.15 to 0.46, mostly through test-time training. On the hidden games of the Kaggle leaderboard, our entry scores 0.20.

</details>

---

### [[20_Research/Papers/具身智能/Be_My_Eye_Learning_to_See_Beyond_a_Robot's_Own_Perspective|Be My Eye: Learning to See Beyond a Robot's Own Perspective]]

![[assets/2611.12295_figure.jpeg|800]]

- **arXiv**: [2611.12295](https://arxiv.org/abs/2611.12295)
- **PDF**: https://arxiv.org/pdf/2611.12295
- **详细分析**: [[20_Research/Papers/具身智能/Be_My_Eye_Learning_to_See_Beyond_a_Robot's_Own_Perspective|Be My Eye: Learning to See Beyond a Robot's Own Perspective]]
- **作者**: Baifu Huang, Shilin Fang, Jianan Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Be My Eye: Learning to See Beyond a Robot's Own Perspective》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution. A key challenge is leveraging complementary observations from partner robots to support collaborative decision-making. We argue that information sharing should go beyond passively transmitting raw observations or generic visual features. Instead, robots should selectively encode task-relevant information according to task objectives and execution progress. To this end, we propose a task-oriented active context sharing framework that transforms robot observations into compact representations, preserving critical information under constrained communication budgets. The framework adopts a two-stage training paradigm. In the first stage, onboard observations and task instructions are jointly encoded into compact context representations. Task-oriented future prediction and soft task-progress correspondence learning guide this collaboration-agnostic compression, preserving information about task objectives and execution progress. In the second stage, the learned representations are integrated into a pretrained Vision-Language-Action (VLA) policy, enabling bidirectional context exchange. Each robot combines complementary partner information with local observations to guide action generation. Action supervision jointly refines the context representations and policy, aligning information sharing with collaborative decision-making. Controlled experiments demonstrate substantial performance gains under constrained communication budgets, while three real-world experiments validate the framework in complex dual-robot tasks. These results highlight a shift from passive visual transmission toward active, task-oriented context sharing that directly supports collaborative decision-making.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_First_Exam|Embodied First Exam]]

![[assets/2611.12177_figure.png|800]]

- **arXiv**: [2611.12177](https://arxiv.org/abs/2611.12177)
- **PDF**: https://arxiv.org/pdf/2611.12177
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_First_Exam|Embodied First Exam]]
- **作者**: Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui, Feishi Wang, Canyu Chen, Wenli Xiao, Xiaoyu Huang, Tonghe Zhang, Linjie Li, Zihan Wang...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied First Exam》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BiGym, DexToolBench, HumanoidBench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. We therefore introduce the Embodied First Exam, a unified, comprehensive, and agent-native evaluation framework where coding agents can choose their own control approach: direct control, code to control, or train a policy to control. We hope it serves as a first exam for coding agents before they enter the physical world, with 1,156 tasks in 35 suites on 47 robots, including 9 new suites that go beyond pick-and-place to spatial puzzles, dexterous manipulation, multi-robot interaction, dynamic whole-body control, and sim-to-sim engineering. Each task can be run in up to three evaluation settings. The Standard Setting mimics the real world: the agent receives only sensor observations and, by default, cannot reset the environment. Its Realtime variant keeps the environment running while the agent reasons. The Privileged Setting gives the agent access to the full simulator state and unlimited resets, allowing it to search for an oracle solution for training purposes. Success rates in this setting serve as an approximate upper bound. On the 456 core tasks, the strongest of eight agents, GPT-6 Astra in Codex, achieves a success rate of 34% in the Standard Setting, leaving much room for improvement. To see where agents fail, we label the stage at which failed attempts go wrong and compare failures across agents, settings, and stage categories.

</details>

---

### [[20_Research/Papers/具身智能/GeoMind_A_Benchmark_for_Spatial_Understanding_in_Robotic_Manipulation|GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation]]

![[assets/2611.12175_figure.png|800]]

- **arXiv**: [2611.12175](https://arxiv.org/abs/2611.12175)
- **PDF**: https://arxiv.org/pdf/2611.12175
- **详细分析**: [[20_Research/Papers/具身智能/GeoMind_A_Benchmark_for_Spatial_Understanding_in_Robotic_Manipulation|GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation]]
- **作者**: Jinghe Wang, Xinrui Cao, Duo Wu, Chenghao Gu, Yong Zhong, Linjia Kang, Tianyi Xiong, Zhi Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.8，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《GeoMind: A Benchmark for Spatial Understanding in Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ESI-Bench, InternVLA, MEMOBench, RMBench, VABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation has advanced rapidly in mapping visual observations and language instructions to actions. However, reliable manipulation in open-world environments requires robust spatial understanding: the ability to identify targets in complex layouts (spatial reasoning) and adapt to scenes that continuously evolve through interaction (spatial memory). Yet existing embodied benchmarks fall short in evaluating spatial understanding: they often introduce strong visual cues that bypass spatial reasoning, and focus on static scenes that offer little insight into an agent's capacity for spatial memory. To address this gap, we introduce GeoMind, a systematic benchmark for structured spatial understanding through tabletop manipulation. GeoMind comprises 54 evaluated task variants organized around spatial reasoning and spatial memory. It also incorporates a scalable pipeline that automates the generation and annotation of task instances with verified targets and executable interactions. Extensive evaluations across diverse embodied agents reveal their consistent weaknesses in spatial understanding. Our findings highlight that these agents struggle to track identities after spatial changes and convert relational or geometric constraints into executable actions. We release the GeoMind benchmark at https://github.com/Notfound-JH/GEOMIND-benchmark.git.

</details>

---

### [[20_Research/Papers/具身智能/Grasp-Taxonomy_Conditioning_as_a_Mode_Switch_for_Dexterous_Grasping_of_Climbing_Holds|Grasp-Taxonomy Conditioning as a Mode Switch for Dexterous Grasping of Climbing Holds]]

![[assets/2611.12017_figure.png|800]]

- **arXiv**: [2611.12017](https://arxiv.org/abs/2611.12017)
- **PDF**: https://arxiv.org/pdf/2611.12017
- **详细分析**: [[20_Research/Papers/具身智能/Grasp-Taxonomy_Conditioning_as_a_Mode_Switch_for_Dexterous_Grasping_of_Climbing_Holds|Grasp-Taxonomy Conditioning as a Mode Switch for Dexterous Grasping of Climbing Holds]]
- **作者**: Rumi Loghmani, Abraham George, Amir Barati Farimani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Grasp-Taxonomy Conditioning as a Mode Switch for Dexterous Grasping of Climbing Holds》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexGraspVLA, PointNet, T-Net, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous grasping in robotics relies on distinct hand configurations depending on object geometry. We introduce BetaGrasp, a 3D diffusion policy that conditions a DP3-style point-cloud policy on a four-class grasp label (crimp, sloper, pinch, and jug), running on a Franka arm with a 16-DoF LEAP hand. We also introduce a climbing-hold benchmark: a spring testbed whose ratchet gives a slip-force reading in newtons. In our analysis the policy's point-cloud encoder did not separate the four holds, so the scan alone gave it little to choose a grasp from. Without the label (a DP3-style baseline), simulated rollouts from the robot's reset pose all end in a jug grasp, whatever the hold (25% correct grasp type, versus 94% for BetaGrasp). The label works as a switch for which grasp the policy performs. On 80 paired hardware trials, BetaGrasp raises average slip force from 9.6 N to 14.3 N, and grasps slipping fully off the hold drop from 44% of trials to 10%.

</details>

---

### [[20_Research/Papers/具身智能/Thermo-VLA_A_Thermal-Aware_Vision-Language-Action_Model_with_Gated_Residual_Modulation_for_Robotic_Manipulation|Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation]]

![[assets/2611.11981_figure.png|800]]

- **arXiv**: [2611.11981](https://arxiv.org/abs/2611.11981)
- **PDF**: https://arxiv.org/pdf/2611.11981
- **详细分析**: [[20_Research/Papers/具身智能/Thermo-VLA_A_Thermal-Aware_Vision-Language-Action_Model_with_Gated_Residual_Modulation_for_Robotic_Manipulation|Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation]]
- **作者**: Jingxuan Chen, Junshi Luo, Chencheng Dong, Xiaojian Nie, Tongge Huang, Qiang Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.9（加权：具身智能 3.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Audio-VLA, DepthVLA, E-VLA, ForceVLA, MuseVLA, OmniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal images into cold and hot attribute representations and injects them into the RGB token through language-conditioned residual modulation, enabling temperature-driven target selection and continuous manipulation. We further construct six real-world robotic tasks on a dual-arm Unitree G1 platform, spanning basic grounding to relational reasoning. Experiments show that Thermo-VLA achieves an average success rate of 0.86 across four thermal-dependent tasks, outperforming a pi_0.5 baseline that directly incorporates RGB-thermal observations by 18 percentage points. Under unseen-object and scene variations, Thermo-VLA maintains an average success rate of 0.78, achieving the best generalisation performance among the compared methods. Beyond thermal sensing, we transfer the same residual modulation mechanism to colour attributes and observe consistent improvements in both simulation and real-robot experiments, indicating its potential to generalise beyond thermal attributes. Project website: https://j-x-chen.github.io/Thermo-VLA-web/

</details>

---

### [[20_Research/Papers/具身智能/An_Evaluation_of_Tabular_Foundation_Models_as_Training-Free_World_Models|An Evaluation of Tabular Foundation Models as Training-Free World Models]]

![[assets/2611.11921_first_page.png|800]]

- **arXiv**: [2611.11921](https://arxiv.org/abs/2611.11921)
- **PDF**: https://arxiv.org/pdf/2611.11921
- **详细分析**: [[20_Research/Papers/具身智能/An_Evaluation_of_Tabular_Foundation_Models_as_Training-Free_World_Models|An Evaluation of Tabular Foundation Models as Training-Free World Models]]
- **作者**: Xian Yeow Lee, Ryoichi Takase, Ahmed Farahat
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 具身智能, 机器人, 大模型
- **相关性评分**: 2.32（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 1.36，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《An Evaluation of Tabular Foundation Models as Training-Free World Models》归入 世界模型、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are widely considered to be a potential key component of model-based reinforcement learning and robot planning, but typically require task-specific training on substantial interaction data. We investigate whether a pretrained tabular foundation model (TabFM) can serve as a training-free dynamics model for world modeling by framing next-state prediction as in-context regression over transition pairs, and where such a model helps and where it breaks. Across synthetic dynamical systems and robot locomotion benchmarks, TabFM is more accurate than LSTM and MLP models trained from scratch on the same limited transitions in almost all settings, and among regressors fitted to the same data it is the most accurate on locomotion, while a Gaussian process is more accurate on smooth low-dimensional systems. However, models trained on the full dataset remain substantially better on most systems. When rolled out autoregressively over multiple steps, TabFM's accuracy depends strongly on how much context it is given. With a short context, its rollouts quickly degrade to the level of a trivial baseline, whereas with a long context they improve substantially and, on one locomotion task, exceed a trained LSTM. Inference is also about three orders of magnitude slower than an LSTM. Overall, in their current state, we find that training-free priors are useful as predictors when data are scarce and enough context is available, but they are not yet a substitute for trained world models in planning.

</details>

---

### [[20_Research/Papers/具身智能/Distilling_Instructions_into_Weights_Closed-Form_Edits_Fix_a_Robot_Policy's_Misreading|Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading]]

![[assets/2611.11894_figure.png|800]]

- **arXiv**: [2611.11894](https://arxiv.org/abs/2611.11894)
- **PDF**: https://arxiv.org/pdf/2611.11894
- **详细分析**: [[20_Research/Papers/具身智能/Distilling_Instructions_into_Weights_Closed-Form_Edits_Fix_a_Robot_Policy's_Misreading|Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading]]
- **作者**: Ali-Adeeb Abbas, Esmaeil Seraj
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Distilling Instructions into Weights: Closed-Form Edits Fix a Robot Policy's Misreading》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies often fail at one step of a task they can otherwise perform. We ask whether such a failure can be repaired by editing the policy's weights directly, without gradients, training data, or a change to the instruction. Told to put the cube then the banana in the bowl, a zero-shot $π_{0.5}$ vision-language-action policy in RoboLab releases the cube before it reaches the bowl. Replaying 21 of these decisions under rewordings shows that it binds "in the bowl" to the wrong object. Closed-form instruction distillation copies the per-layer effect of an explicit rewording into the language model's MLP weights. On 128 held-out seeds, success rises from 27 to 106 episodes, with 81 fixed and 2 broken ($p=7\times10^{-22}$), while an update of the same size in random directions leaves success unchanged. The edit also lifts two other tasks without detectable harm on the remaining 13, and a variant that stores 0.16% of the parameter count keeps most of its effect. Placed in the action expert or action head instead, the same distillation helps less or not at all. Our released tool reproduced the fix end to end on new held-out seeds, from 8/64 to 36/64. Edits aimed at perception, a missing grasp, contact physics, or the gripper threshold did not help, and of seven blind Claude Opus editors, only the one given the misread instruction produced an edit that passed held-out scoring. These results suggest that weight edits work best when a known-good input already exists to distil. Because reruns with unchanged weights flip about a third of paired outcomes, evaluations should pair seeds, rerun the unedited policy, and confirm gains on held-out seeds.

</details>

---

### [[20_Research/Papers/具身智能/Decoupled_Asynchronous_System_for_Humanoids_(DASH)_Latency-Agnostic_Scaling_of_Vision-Language-Action_Models_for_Humanoid_Manipulation|Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation]]

![[assets/2611.11854_figure.png|800]]

- **arXiv**: [2611.11854](https://arxiv.org/abs/2611.11854)
- **PDF**: https://arxiv.org/pdf/2611.11854
- **详细分析**: [[20_Research/Papers/具身智能/Decoupled_Asynchronous_System_for_Humanoids_(DASH)_Latency-Agnostic_Scaling_of_Vision-Language-Action_Models_for_Humanoid_Manipulation|Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation]]
- **作者**: Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiajin Zheng, Yin Zhang, Kehua Chen, Jian Yao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.8（加权：具身智能 3.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DP-VLA, FiS-VLA, OpenVLA, Real-World, ResNet, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy into a slow vision-language model (System 2) and a fast flow-matching action head (System 1) that run as concurrent processes over the LCM communication protocol, so the control rate is set by the action head alone, independent of backbone size. The action head fuses stale semantics from a frozen backbone with fresh vision from its own ResNet encoder, desynchronized training exposes it to the staleness it meets at deployment, and an adaptive temporal aggregator aligns overlapping action chunks under variable inference latency. On an asynchronous RoboTwin benchmark that charges inference latency in simulated time, DASH holds 20 Hz control rate from 0.8B to 8B backbones while the synchronous rate falls from 9.7 to 4.1 Hz, with higher success at every size. On a real humanoid with dexterous hands, DASH achieves clearly higher pick-and-place success than the synchronous pipeline.

</details>

---

### [[20_Research/Papers/机器人/A_Benchmark_and_Layered_Evaluation_Protocol_for_Evidence-Grounded_Shared_Belief_Updating_in_Connected_Robotics|A Benchmark and Layered Evaluation Protocol for Evidence-Grounded Shared Belief Updating in Connected Robotics]]

![[assets/2611.11842_figure.png|800]]

- **arXiv**: [2611.11842](https://arxiv.org/abs/2611.11842)
- **PDF**: https://arxiv.org/pdf/2611.11842
- **详细分析**: [[20_Research/Papers/机器人/A_Benchmark_and_Layered_Evaluation_Protocol_for_Evidence-Grounded_Shared_Belief_Updating_in_Connected_Robotics|A Benchmark and Layered Evaluation Protocol for Evidence-Grounded Shared Belief Updating in Connected Robotics]]
- **作者**: Ranulfo Bezerra, Kimitoshi Yamazaki
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Benchmark and Layered Evaluation Protocol for Evidence-Grounded Shared Belief Updating in Connected Robotics》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BayesBench, OpenEQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Connected physical systems fuse observations from robots, IoT sensors, and edge-AI modules into a shared account of the world, yet most evaluations score only the final answer or action and cannot tell whether a method attributed the evidence, updated its belief, handled contradictions, and justified its decision. We argue that shared reasoning in Connected Robotics should be evaluated as an evidence-to-belief trajectory, and introduce the Connected Robotics Evidence Graph (CREG) Benchmark to make that trajectory measurable. CREG comprises 350 deterministically generated scenarios across seven regimes (justified revision, belief preservation, relation association, contradiction onset and resolution, stale/delayed evidence, and source reliability), each exposing a normative posterior reference at every evidence prefix, validated by an independent log-odds checker and screened by a blinded expert audit. Nine representation conditions separate relation content from serialization, ordering, and metadata. Evaluating four open-weight instruction models and six transparent fusion baselines yields three findings. First, entity grounding accounts for a substantial part of the weak-model deficit. Second, deleting semantic relations costs 15.3 points of strict belief-state accuracy on relation-dependent scenarios (Holm-corrected p&lt;0.001), but an information-matched structured list outperforms the full graph and shuffling the graph does not hurt: relation content matters where required, while graph serialization confers no consistent advantage. Third, belief accuracy is strongly non-monotonic along the evidence sequence, with mid-trajectory failures that endpoint-only evaluation cannot detect. All scenarios, references, prompts, metrics, and analysis code are released for offline, hardware-free reproduction.

</details>

---

### [[20_Research/Papers/强化学习/HolidayFactory_1.0_Simulating,_Generating,_and_Evaluating_Industrial_Robot_Tasks|HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks]]

![[assets/2611.11789_figure.png|800]]

- **arXiv**: [2611.11789](https://arxiv.org/abs/2611.11789)
- **PDF**: https://arxiv.org/pdf/2611.11789
- **详细分析**: [[20_Research/Papers/强化学习/HolidayFactory_1.0_Simulating,_Generating,_and_Evaluating_Industrial_Robot_Tasks|HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks]]
- **作者**: Holiday Robotics, :, Jeongmin Lee, Taehyeon Kim, Dohyun Jang, Minji Lee, Seonghun Oh, Dongwoo Park, Geonhyup Lee, Jaehyung Kim, Jaemin Yoon, Jinseop Bok...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《HolidayFactory 1.0: Simulating, Generating, and Evaluating Industrial Robot Tasks》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Dex-Net, Holiday-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots are typically evaluated in episodes that begin from a reset, while industrial work consists of repeated jobs whose outcomes affect subsequent operations. Evaluating such work at scale requires simulation of task-critical physical interactions, construction of industrial environments, and measurements of performance as scene state persists. We present HOLIDAYFACTORY 1.0, a framework for simulating, generating, and evaluating industrial robot work. Given a human-specified workplace and task, the framework defines a world pairing a scenario of scene variants and process logic with an evaluation defining a job, metrics, and a rubric. HOLIDAYFACTORY 1.0 comprises three components. HOLIDAY-SIM extends Newton's SDF-based hydroelastic contact with additional constitutive laws and a semi-implicit primal-dual solver, couples stateful actuator dynamics to articulated motion, and derives tactile and joint observations from simulated states. Agentic world construction generates simulation-ready assets and scene variants using geometric and interaction checks, and proposes task-conditioned evaluations for human confirmation and executable checks. 24/7-BENCH introduces seven industrial tasks in which jobs are evaluated without resetting the scene, measuring completed, failed, and unfinished jobs, throughput, latency, and motor energy. Controlled studies characterize the proposed contact, actuator, and tactile models and examine the effectiveness of verification-guided world construction. Experiments on scene and evaluation generation further reveal the limitations of model critics and the difficulty of ensuring that generated evaluations faithfully capture task requirements. We examine job-level evaluations with scripted trajectories (e.g., code-as-policy) but have not yet compared policies over persistent runs.

</details>

---

### [[20_Research/Papers/强化学习/Accelerated_Reinforcement_Learning_for_Soft_Robotics_Hours_Instead_of_Years|Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years]]

![[assets/2611.11718_figure.png|800]]

- **arXiv**: [2611.11718](https://arxiv.org/abs/2611.11718)
- **PDF**: https://arxiv.org/pdf/2611.11718
- **详细分析**: [[20_Research/Papers/强化学习/Accelerated_Reinforcement_Learning_for_Soft_Robotics_Hours_Instead_of_Years|Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years]]
- **作者**: Roshan S. Kaundinya, Hehui Zheng, Robert K. Katzschmann, George Haller
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.72（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Accelerated Reinforcement Learning for Soft Robotics: Hours Instead of Years》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) requires large amounts of interaction data or a reliable simulator, both hard to obtain for nonlinear soft robotic hardware. Recent work shows that a time-scale separation inherent to soft robot dynamics justifies their reduction to low-dimensional invariant manifolds, known as adiabatic spectral submanifolds (aSSMs). We demonstrate that an aSSM-reduced model, a simple polynomial ordinary differential equation learned purely from pre-collected data, can serve as an RL training environment. On a pneumatically actuated soft arm, we train a trajectory-tracking policy in 3 hours on a six-dimensional aSSM-reduced model and deploy it without fine-tuning, whereas reproducing this policy training extrapolates to 3 years of hardware interaction. Our policy tracks dynamic targets with 40% lower error than otherwise identical policies trained on a 4.8-million-parameter recurrent neural network (RNN) or a 1.7-million-parameter transformer, which take 13 and 100 hours to identify, against 5 minutes for our mathematically justified 6,924-parameter model.

</details>

---

### [[20_Research/Papers/强化学习/Qubit-to-Motion_Traceable_Action_Provenance_in_Hybrid_QRL_for_Robotic_Bin-Packing_Sequencing|Qubit-to-Motion: Traceable Action Provenance in Hybrid QRL for Robotic Bin-Packing Sequencing]]

![[assets/2611.11580_figure.png|800]]

- **arXiv**: [2611.11580](https://arxiv.org/abs/2611.11580)
- **PDF**: https://arxiv.org/pdf/2611.11580
- **详细分析**: [[20_Research/Papers/强化学习/Qubit-to-Motion_Traceable_Action_Provenance_in_Hybrid_QRL_for_Robotic_Bin-Packing_Sequencing|Qubit-to-Motion: Traceable Action Provenance in Hybrid QRL for Robotic Bin-Packing Sequencing]]
- **作者**: Hassen Nigatu, Howard Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Qubit-to-Motion: Traceable Action Provenance in Hybrid QRL for Robotic Bin-Packing Sequencing》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：QRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hybrid quantum reinforcement learning has been explored for robotic decision-making, but evaluations often emphasize task success, return, or convergence, leaving unresolved whether quantum circuit outputs influence constrained actions and remain traceable through robot execution. We present \texttt{Qubit-to-Motion}, an evidence-centered framework for support-constrained sequencing and simulated robotic placement. Four Pauli-$Z$ readouts provide the sole learned input to the actor and critic, while a support mask enforces admissible object selection. Each decision is recorded and linked via step indices and SHA-256 fingerprints to a sealed route, deterministic Cartesian and inverse-kinematics waypoints, prescribed joint motion, and MuJoCo contact replay. A frozen checkpoint is evaluated across five deterministic 30-object scene variants. All 150 placements satisfy support, containment, and settling criteria. A fixed-state zero-readout intervention changes $90.0\pm0.0\%$ of decisions, demonstrating dependence on the joint circuit representation. Mean macro travel is $34.537\pm0.206$~m, inference requires $8.60\pm1.27$~ms per route, and replay achieves $8.764\pm0.220~μ$m mean final position error with 0.356~mm maximum interpenetration. These results establish reproducible decision-to-contact traceability. The implementation is available at \href{https://anonymous.4open.science/r/Qubit-to-Motion-Quantum-Reinforcement-Learning-F7DC}{\textcolor{linkpink}{the anonymous repository}}.

</details>

---

### [[20_Research/Papers/具身智能/Kimodo-Policy_Learning_Kinematic_Action_Models_for_Humanoid_Loco-Manipulation|Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation]]

![[assets/2611.11554_figure.png|800]]

- **arXiv**: [2611.11554](https://arxiv.org/abs/2611.11554)
- **PDF**: https://arxiv.org/pdf/2611.11554
- **详细分析**: [[20_Research/Papers/具身智能/Kimodo-Policy_Learning_Kinematic_Action_Models_for_Humanoid_Loco-Manipulation|Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation]]
- **作者**: Yunheng Wang, Jiaxi Zhang, Wei Lu, Yuetong Fang, Taowen Wang, Yixiao Feng, Shuning Zhang, Junzhe Xu, Yichi Wang, Zizhao Yuan, Kailun Huang, Lusong Li...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Kimodo-Policy: Learning Kinematic Action Models for Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, HumanVLA, Humanoid-VLA, Real-World, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires continuous coordination of high-dimensional whole-body motion to realize task objectives. While vision-language-action models and world action models transfer semantic and visual-dynamics priors to robot control, these priors do not necessarily capture the structure of robot motion. We introduce Kinematic Action Models (KAMs), a paradigm that treats whole-body motion as a direct pretraining target and uses a pretrained motion generator as the primary action-generation backbone. KAMs ground learned temporal and cross-body coordination priors through task conditioning, visual observations, and execution feedback. We present Kimodo-Policy as an initial instantiation, combining a frozen Kimodo text-to-motion backbone with lightweight ControlNet-based visual conditioning. A root-body-hand hierarchy coordinates locomotion and manipulation, while motion-history conditioning and repeated action-chunk prediction bridge motion synthesis and closed-loop control. Following large-scale loco-manipulation pretraining, the policy achieves the highest overall success among compared policies on multi-task HumanoidArena (72.14%), competitive performance on SIMPLE, and 60% mean success across eight real-world tasks, with 678M parameters (92M trainable). Ablations support the contribution of the pretrained motion backbone. Together, these results provide initial evidence for motion generation as a complementary foundation for humanoid action learning.

</details>

---

### [[20_Research/Papers/世界模型/K-PWM_Control-Oriented_Structured_Bilinear_World_Models_under_Partial_Observation|K-PWM: Control-Oriented Structured Bilinear World Models under Partial Observation]]

![[assets/2611.11521_figure.png|800]]

- **arXiv**: [2611.11521](https://arxiv.org/abs/2611.11521)
- **PDF**: https://arxiv.org/pdf/2611.11521
- **详细分析**: [[20_Research/Papers/世界模型/K-PWM_Control-Oriented_Structured_Bilinear_World_Models_under_Partial_Observation|K-PWM: Control-Oriented Structured Bilinear World Models under Partial Observation]]
- **作者**: Santosh Mohan Rajkumar, Sriram Narayanan, Samuel E. Otto, Debdipta Goswami
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.16，世界模型 1.36）
- **关联关键词**: Agent, WorldModel, Systems

#### 研究背景与动机

《K-PWM: Control-Oriented Structured Bilinear World Models under Partial Observation》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MBRL, MFRL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models learn internal simulators of environment dynamics for prediction, planning, and control, yet learning them from limited, noisy, and partial observations remains challenging. While much progress has focused on pixel-based observations, many physical systems instead provide vector-valued measurements that reveal only part of the underlying state. We introduce K-PWM, a probabilistic world model for prediction and control under partial observation. K-PWM couples Koopman-bilinear latent dynamics with a nonlinear observation decoder and performs probabilistic latent-state inference through the learned model via extended Kalman filtering and smoothing, without a separately trained inference network. Its bilinear structure enables exact propagation of the maintained Gaussian belief through the latent transition and efficient rollouts for uncertainty-aware model predictive path integral (MPPI) control. For training K-PWM, we present a generalized expectation conditional maximization (GECM) procedure with closed-form updates for the generators, noise covariances, and latent prior, complemented by gradient-based decoder learning. A Koopman-consistent initialization selects the latent dimension from data and initializes the action-dependent dynamics. With limited training data, K-PWM achieves lower long-horizon prediction error than the evaluated baselines on partially observed Gymnasium MuJoCo systems, while substantially reducing training time relative to the strongest prediction baseline. On high-dimensional MuJoCo Menagerie robots, it achieves competitive tracking accuracy with low per-step computation times, demonstrating potential for real-time deployment. These results support structured probabilistic dynamics as a data- and compute-efficient approach to world modeling and control under partial observation.

</details>

---

### [[20_Research/Papers/具身智能/Review_the_Episodes,_Refine_the_Lessons_Simple_Memory_Evolution_for_Embodied_Agents|Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents]]

![[assets/2611.11509_figure.png|800]]

- **arXiv**: [2611.11509](https://arxiv.org/abs/2611.11509)
- **PDF**: https://arxiv.org/pdf/2611.11509
- **详细分析**: [[20_Research/Papers/具身智能/Review_the_Episodes,_Refine_the_Lessons_Simple_Memory_Evolution_for_Embodied_Agents|Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents]]
- **作者**: Yifei Yao, Yude Zou, Xing Gao, Guanbo Jiao, Yukai Wang, Jianming Ma, Weinan Zhang, Chunhua Shen
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.6，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Review the Episodes, Refine the Lessons: Simple Memory Evolution for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies of embodied agents based on frontier multimodal large language models (MLLMs) develop harness engineering around the MLLM, such as harnesses with post-trained policies and recursive self-improvement loops. Yet whether these additions exceed the native capability of the MLLM remains unexplored. We introduce SimplEvo to explore how far an MLLM can improve under direct control when it retains its execution experience in self-written text memories. It requires no weight updates, post-trained policies, or privileged information. The MLLM writes a coordinate-free task memory once from a single demonstration. Under a strict train-test protocol, it then creates a bounded working memory on training episodes only and refines it after each episode with lessons on procedure, completion, and recovery. Both memories stay fixed at test time. On EBench, SimplEvo lifts the success rate (SR) of GPT-6-Astra under direct control from 46.7% to 81.7%, and tops the RoboDojo leaderboard with 69.63% SR and a score of 75.32. Compared with memories that also store past visual frames, SimplEvo reaches a similar SR with text memory alone while using fewer tokens. With its memories fixed, SimplEvo also generalizes to unseen layouts and randomized scene configurations. Moreover, the working memory transfers across models: written by GPT-6-Astra, it can be reused as is by weaker MLLMs and improve their performance without any adaptation of their own.

</details>

---

### [[20_Research/Papers/大模型/LLM-based_Multi-Criteria_Deep_Reinforcement_Learning_for_Dynamic_Efficient_5G_UPF_Selection|LLM-based Multi-Criteria Deep Reinforcement Learning for Dynamic Efficient 5G UPF Selection]]

![[assets/2611.11372_figure.png|800]]

- **arXiv**: [2611.11372](https://arxiv.org/abs/2611.11372)
- **PDF**: https://arxiv.org/pdf/2611.11372
- **详细分析**: [[20_Research/Papers/大模型/LLM-based_Multi-Criteria_Deep_Reinforcement_Learning_for_Dynamic_Efficient_5G_UPF_Selection|LLM-based Multi-Criteria Deep Reinforcement Learning for Dynamic Efficient 5G UPF Selection]]
- **作者**: Abdelrahman Soliman, Ahmed Refaey Hussein, Lei Lei
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.37（加权：大模型 0.45，强化学习 1.76，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《LLM-based Multi-Criteria Deep Reinforcement Learning for Dynamic Efficient 5G UPF Selection》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

User plane function (UPF) selection in 5G networks is an active area of research, with various limited approaches proposed to enhance network efficiency and manage resources effectively. In this paper, we address this gap in the related literature by proposing a Deep Reinforcement Learning (DRL) UPF selection method that utilizes a dynamic, multi-objective reward function and validating it on a real-world 5G emulation platform. The proposed method is based on the large language models' (LLMs) translation of network operator intents and the network data analytics function (NWDAF) abnormality alerts. The experimental results validated in the real-world experimental setup demonstrate that our dynamic DRL solution achieves an effective balance between latency, power consumption, and traffic distribution, outperforming the heuristic baselines and fixed DRL by 16.89%. These findings highlight the real-world applicability of our approach for dynamic, intent-driven UPF selection.

</details>

---

### [[20_Research/Papers/具身智能/Where_Should_Models_Run_A_Collaborative_Inference_Framework_for_Embodied_Intelligence_in_6G|Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G]]

![[assets/2611.11023_figure.png|800]]

- **arXiv**: [2611.11023](https://arxiv.org/abs/2611.11023)
- **PDF**: https://arxiv.org/pdf/2611.11023
- **详细分析**: [[20_Research/Papers/具身智能/Where_Should_Models_Run_A_Collaborative_Inference_Framework_for_Embodied_Intelligence_in_6G|Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G]]
- **作者**: Wanlu Sun, Zhenhui Yuan, Xiang Ji, Yi Han, Qing Li, Gan Zheng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.8，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, ResNet, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have significantly enhanced the capabilities of embodied agents in complex environments. However, deploying these models remains challenging due to the limited computational resources and energy budgets of robotic platforms. A fundamental question is where inference should be executed. Collaborative inference, which partitions models across end devices, edge servers, and the cloud, has emerged as a promising solution. Yet determining the optimal partitioning point remains an open problem, as it depends on wireless network conditions, model structure, and privacy requirements. This article reviews the state of the art in collaborative inference for embodied intelligence and proposes an edge-centric framework in which the edge coordinates model partitioning and execution. Through both simulation and real-world experiments over WiFi and 5G networks, we demonstrate that the optimal partitioning strategy varies with network conditions and model structure. We further identify latency-minimizing partition points for ResNet-101, Qwen2.5-VL-7B, and OpenVLA-7B in collaborative inference between NVIDIA Jetson Nano or AGX Xavier devices and an AGX Thor edge server under varying wireless conditions. Finally, we discuss the future directions for collaborative inference in 6G-empowered embodied intelligence systems.

</details>

---

### [[20_Research/Papers/具身智能/Zero-Shot_VLA_Adaptation_with_Retrieved_Guidance|Zero-Shot VLA Adaptation with Retrieved Guidance]]

![[assets/2611.10894_figure.png|800]]

- **arXiv**: [2611.10894](https://arxiv.org/abs/2611.10894)
- **PDF**: https://arxiv.org/pdf/2611.10894
- **详细分析**: [[20_Research/Papers/具身智能/Zero-Shot_VLA_Adaptation_with_Retrieved_Guidance|Zero-Shot VLA Adaptation with Retrieved Guidance]]
- **作者**: Subin Kim, Anh-Quan Pham, Dinesh Jayaraman
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.5（加权：具身智能 2.4，大模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Zero-Shot VLA Adaptation with Retrieved Guidance》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MetaWorld, RA-VLA, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pre-training large parametric "Vision-Language-Action" (VLA) models on large demonstration datasets has recently yielded promising results for general-purpose manipulation. However, these models still struggle under even small domain shifts relative to the training data, such as changes in camera viewpoint, background, object identity, or robot morphology. Motivated by the success of Retrieval-Augmented Generation (RAG) in language models, we pursue retrieval to boost VLA performance. Specifically, we seek to leverage retrieval from domain-mismatched, "in-the-wild" demonstration datasets like DROID to guide a VLA's behavior in a new target domain. To achieve this, we introduce RAGu, which overcomes robotics-specific challenges for RAG: (1) It incorporates simple geometric calibration to transform source demonstrations into the target setup and reduce cross-domain differences. (2) It uses a coarse-to-fine retrieval strategy that selects, from a large pool of pre-warped candidates, the trajectory most compatible with the base VLA. (3) It guides the VLA's flow-matching inference procedure rather than seeking to retrain the base model or expand its limited context window. We evaluate RAGu across real-world, simulation, sim-to-real transfer, and cross-embodiment humanoid manipulation. We find it improves real-world VLA success rates from 20% to 80% and outperforms the closest-related baselines in sim. Project website: raguvla.github.io

</details>

---

### [[20_Research/Papers/具身智能/Look_Ahead_Search-Driven_Reasoning_in_Embodied_AI|Look Ahead: Search-Driven Reasoning in Embodied AI]]

![[assets/2611.10769_figure.png|800]]

- **arXiv**: [2611.10769](https://arxiv.org/abs/2611.10769)
- **PDF**: https://arxiv.org/pdf/2611.10769
- **详细分析**: [[20_Research/Papers/具身智能/Look_Ahead_Search-Driven_Reasoning_in_Embodied_AI|Look Ahead: Search-Driven Reasoning in Embodied AI]]
- **作者**: Ahmed Zeer, Osama Shbib, Muzaffer Kaan Yuce, Himmet Toprak Kesgin, Mehmet Fatih Amasyali
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 2.1，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Look Ahead: Search-Driven Reasoning in Embodied AI》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Search allows a robotic policy to evaluate candidate futures before committing to an action. Motivated by test-time planning for vision-language action (VLA) models, we study selective search over action chunks in PushT using a frozen Action Chunking with Transformers (ACT) policy. Beam search generates perturbed alternatives around the policy prediction and scores them through rollouts from cloned simulator states. Across 50 evaluation episodes, beam search raises task success from 0% to 18% and increases average cumulative reward from 39.44 to 103.2. We introduce One Step Ahead (OSA), a gate that simulates the nominal policy chunk and invokes full search only when its predicted coverage drop exceeds a threshold. In the reported ablations, OSA preserves or improves success while reducing runtime by approximately 3x relative to full beam search. Ablations over tree depth, branching factor, beam width, and replanning frequency show that larger search budgets do not consistently improve performance. The results support selective test-time search for action-chunking policies; evaluation on language-conditioned VLAs and physical robots remains future work.

</details>

---

### [[20_Research/Papers/强化学习/SLA-Aware_Task_Offloading_in_the_IoT_Edge-Cloud_Continuum_Class-Weighted_Deep_Reinforcement_Learning_Against_an_Exact_Optimum|SLA-Aware Task Offloading in the IoT Edge-Cloud Continuum: Class-Weighted Deep Reinforcement Learning Against an Exact Optimum]]

![[assets/2611.10638_first_page.png|800]]

- **arXiv**: [2611.10638](https://arxiv.org/abs/2611.10638)
- **PDF**: https://arxiv.org/pdf/2611.10638
- **详细分析**: [[20_Research/Papers/强化学习/SLA-Aware_Task_Offloading_in_the_IoT_Edge-Cloud_Continuum_Class-Weighted_Deep_Reinforcement_Learning_Against_an_Exact_Optimum|SLA-Aware Task Offloading in the IoT Edge-Cloud Continuum: Class-Weighted Deep Reinforcement Learning Against an Exact Optimum]]
- **作者**: Shilpa Golla, Tharun Kumar Korine Palli, Urmila Bandaru
- **cs 子类**: cs.AI, cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.32（加权：大模型 0.2，强化学习 1.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《SLA-Aware Task Offloading in the IoT Edge-Cloud Continuum: Class-Weighted Deep Reinforcement Learning Against an Exact Optimum》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (RL) is often used to decide where Internet of Things (IoT) tasks with different latency limits run in the edge-cloud continuum, yet some methods give every missed task the same penalty and few compare their agents with an optimal policy. This benchmark study builds four offloading systems small enough to solve exactly by dynamic programming and measures reward and learner against the optimum. A bonus for a met limit makes each miss cost its penalty plus the bonus, which shifts the class weights of published per-class rewards. A class-blind penalty stays 65% to 118% above the optimal cost even with a perfect learner, while a corrected per-class penalty comes within 0.13% of the optimum. With a per-class reward, tuned proximal policy optimization (PPO) agents come within 9% to 11% of the optimum in the smallest system, and the corrected one beats a tuned reservation rule in 9 of 10 seeds. In larger systems the agents stay 41% to 76% above the optimum, and a tuned rule beats their mean. Training ten times longer does not close this gap, and a PPO-Lagrangian agent with reachable targets does no better than the per-class reward.

</details>

---

### [[20_Research/Papers/具身智能/CPNav_Calibrated_Vision-Language_Navigation_for_Object-Goal_Search_in_Unseen_Environments|CPNav: Calibrated Vision-Language Navigation for Object-Goal Search in Unseen Environments]]

![[assets/2611.10366_figure.png|800]]

- **arXiv**: [2611.10366](https://arxiv.org/abs/2611.10366)
- **PDF**: https://arxiv.org/pdf/2611.10366
- **详细分析**: [[20_Research/Papers/具身智能/CPNav_Calibrated_Vision-Language_Navigation_for_Object-Goal_Search_in_Unseen_Environments|CPNav: Calibrated Vision-Language Navigation for Object-Goal Search in Unseen Environments]]
- **作者**: Qizhao Chen, Yuanhong Zeng, Shoh Nishino, Anushri Dixit
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《CPNav: Calibrated Vision-Language Navigation for Object-Goal Search in Unseen Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Directing a robot to locate a target object in unseen environments remains a central challenge in embodied AI. Vision-Language Model (VLM)-based methods provide rich semantic reasoning but often produce uncalibrated and overconfident action decisions. We introduce CPNav, a navigation framework that combines collision-aware planning with statistically calibrated VLM action scoring for map-free object-goal navigation. From RGB-D input, CPNav constructs a navigability map, generates collision-free motion primitives, and queries two VLMs for goal detection and action scoring. The resulting scores are calibrated offline via conformal prediction (CP) using oracle actions obtained through a tree-structured exploration procedure with backtracking, providing finite-sample guarantees at a user-specified risk level. The CP layer is model-agnostic and can wrap any VLM policy. Online, calibrated VLM scores guide action selection, while a tree-structured exploration history records alternative actions and allows backtracking. We evaluate CPNav in both simulation and real-world hardware settings. In AI Habitat simulation, compared with the uncalibrated baseline method, CPNav achieves relative SR and SPL improvements of 6.2% and 11.4% on HM3D v0.2, and 12.4% and 8.8% on MP3D, respectively. In real-world deployment on a modified Hiwonder MentorPi robot, the corresponding improvements in SR and SPL are 24.9% and 15.2%, respectively. Code is available at https://github.com/practice-lab-ucla/CPnav.

</details>

---

### [[20_Research/Papers/强化学习/Transit-Oriented_Land_Use_Planning_Using_Deep_Reinforcement_Learning|Transit-Oriented Land Use Planning Using Deep Reinforcement Learning]]

![[assets/2611.10281_figure.png|800]]

- **arXiv**: [2611.10281](https://arxiv.org/abs/2611.10281)
- **PDF**: https://arxiv.org/pdf/2611.10281
- **详细分析**: [[20_Research/Papers/强化学习/Transit-Oriented_Land_Use_Planning_Using_Deep_Reinforcement_Learning|Transit-Oriented Land Use Planning Using Deep Reinforcement Learning]]
- **作者**: Bo Yang, Yuebing Liang, Zhan Zhao, Fangyi Ding, Yunhan Zheng, Shenhao Wang, Jinhua Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Transit-Oriented Land Use Planning Using Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transit-Oriented Development (TOD) is a key strategy for advancing sustainable urban development by promoting high-density, mixed-use land development within walking distance of public transit stations. However, traditional TOD planning often relies on heuristic methods, making it difficult to efficiently identify quantitatively optimized transit-oriented land use patterns. This paper presents DRL4TOD, a deep reinforcement learning framework that automatically optimizes land use types and floor area ratios (FARs) around transit stations in alignment with TOD principles. DRL4TOD incorporates a graph neural network to capture spatial interdependencies among land parcels, road networks, and metro stations, and uses a DRL-based optimization strategy to assign land-use types and FARs to selected parcels. It jointly optimizes multiple objectives, including land use density, land use diversity, and transit capacity utilization, while minimizing reconstruction costs to account for development feasibility. Applied to two real-world station areas in Shanghai, DRL4TOD consistently outperforms rule-based approaches and genetic algorithms, achieving more effective TOD outcomes with lower reconstruction costs. By adjusting objective weights, the framework enables flexible prioritization, such as placing greater emphasis on cost minimization when financial feasibility is a concern. These results demonstrate DRL4TOD's potential as a decision-support tool for generating coordinated land-use and FAR configurations under planner-specified priorities, rather than prescribing a single fixed design. For policymakers, the framework provides parcel-level, constraint-aware alternatives that make trade-offs among competing objectives explicit and support targeted decisions about development intensity and feasibility.

</details>

---
