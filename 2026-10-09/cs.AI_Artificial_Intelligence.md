# cs.AI | Artificial Intelligence | 2026-10-09

#arxiv #ComputerScience

**论文数**: 28

### [[20_Research/Papers/机器人/RoboRSI_Stable,_efficient,_and_reusable_robot_self-evolution_in_complex_real-world_environments|RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments]]

![[assets/2610.12424_figure.png|800]]

- **arXiv**: [2610.12424](https://arxiv.org/abs/2610.12424)
- **PDF**: https://arxiv.org/pdf/2610.12424
- **详细分析**: [[20_Research/Papers/机器人/RoboRSI_Stable,_efficient,_and_reusable_robot_self-evolution_in_complex_real-world_environments|RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments]]
- **作者**: Zimo Wen, Yijin Chen, Yuxuan Cao, Wendi Chen, Yanwen Zou, Wenye Yu, Fuhang Kuang, Han Xue, Jun Lv, Chuan Wen, Cewu Lu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A generalist robot should not only perform diverse tasks but also improve through experience, turning what it learns during execution into capabilities that later tasks can reuse. Robot agents that act through code can already repair programs from execution feedback, yet it remains a central challenge to organize this experience around the task structure that gives it meaning, so that each repair is attributed to the responsible capability, supported by execution evidence, and validated before it is reused. We introduce RoboRSI, a robot self-improvement system built on Top-Down Skill Refinement (TSR). TSR decomposes tasks into compound, atomic, and base skills with scoped responsibilities and explicit input--output contracts, attributes each execution outcome to the responsible branch, and confines revision to that branch. Building upon this structure, a Manager, Planner, Engineer, and Reviewer coordinate planning, execution, diagnosis, and the validated release of new skills, while people steer the process through objectives and corrections; stable skill sequences are further consolidated into reusable compound skills. On a mobile manipulator, RoboRSI develops multi-object household cleanup over 104 rounds. In simulation, it achieves the highest success rate on LIBERO, LIBERO-PRO, LIBERO-Plus, and RoboTwin, exceeding the strongest baseline by 2.7 to 11.0 percentage points.

</details>

---

### [[20_Research/Papers/强化学习/ARC_A_Reasoning_Recipe_for_Robot_Foundation_Models|ARC: A Reasoning Recipe for Robot Foundation Models]]

![[assets/2610.12386_figure.png|800]]

- **arXiv**: [2610.12386](https://arxiv.org/abs/2610.12386)
- **PDF**: https://arxiv.org/pdf/2610.12386
- **详细分析**: [[20_Research/Papers/强化学习/ARC_A_Reasoning_Recipe_for_Robot_Foundation_Models|ARC: A Reasoning Recipe for Robot Foundation Models]]
- **作者**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li, Fabio Ramos, Ankit Goyal, Jenai Xuning Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ARC: A Reasoning Recipe for Robot Foundation Models》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARC-Trace-DROID, TRACE-DROID, Trace-DROID。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces should be grounded in the robot's next action and explain its causal structure: why the action is appropriate and what effect it should produce. Second, we show that these traces can be generated automatically from existing demonstrations, enabling us to construct ARC-Trace-DROID from DROID without collecting new robot data. Third, we show how state-of-the-art VLAs such as $π_{0.5}$ and WAMs such as Cosmos3-Nano-Policy can learn to use these traces for control, with fine-tuning and inference tailored to each model's architecture and capabilities. Using ARC, we obtain gains in zero-shot RFM performance that, to our knowledge, are unprecedented without additional robot demonstrations or foundation-scale training. The adapted models establish a new state of the art on RoboLab-120 and MolmoSpaces, with gains of up to 50 percentage points on RoboLab-Reasoning-50. On real robots, ARC improves $π_{0.5}$'s task success by 82.2 percentage points. Project website: https://arc-robot-reasoning.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Multi-Agent_Egocentric_World_Model_with_Fine-Grained_Embodied_Interaction|Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction]]

![[assets/2610.12299_figure.png|800]]

- **arXiv**: [2610.12299](https://arxiv.org/abs/2610.12299)
- **PDF**: https://arxiv.org/pdf/2610.12299
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Agent_Egocentric_World_Model_with_Fine-Grained_Embodied_Interaction|Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction]]
- **作者**: Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.5，大模型 0.5，世界模型 1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction》归入 具身智能、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ME-World, Shared-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric world models predict first-person observations conditioned on an agent's actions, but most focus on a single agent. Real embodied settings often involve multiple agents that act and interact within a shared environment. Existing multi-agent world models rely on coarse actions like locomotion, camera control, or discrete commands, leaving fine-grained embodied interactions underexplored. We formulate multi-agent egocentric world modeling as synchronized ego-stream generation for multiple agents interacting through fine-grained actions in a shared world. This requires cross-view action consistency, shared-environment consistency, and consistent propagation of interaction-induced state updates. We propose Multi-agent Egocentric World Model (ME-World), which jointly denoises multiple ego streams in a shared token sequence, conditions each stream on all agents' target-view poses, and grounds generation with shared environment memory. We train and evaluate on real and synthetic multi-agent data and introduce shared-world consistency metrics for environment, update, and identity consistency. Experiments show ME-World improves shared-world consistency, action control, identity preservation, and video quality over existing methods.

</details>

---

### [[20_Research/Papers/机器人/Real-Time_Motion_Planning_with_Dynamic_Hazards_Classical_vs._Learning-Based_Methods|Real-Time Motion Planning with Dynamic Hazards: Classical vs. Learning-Based Methods]]

![[assets/2610.12249_first_page.png|800]]

- **arXiv**: [2610.12249](https://arxiv.org/abs/2610.12249)
- **PDF**: https://arxiv.org/pdf/2610.12249
- **详细分析**: [[20_Research/Papers/机器人/Real-Time_Motion_Planning_with_Dynamic_Hazards_Classical_vs._Learning-Based_Methods|Real-Time Motion Planning with Dynamic Hazards: Classical vs. Learning-Based Methods]]
- **作者**: Eran Iceland, Alexander Tuisov, Oren Gal, Ariel Barel, Alfred M. Bruckstein
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Real-Time Motion Planning with Dynamic Hazards: Classical vs. Learning-Based Methods》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study real-time motion planning in dynamic hazard fields through a controlled comparison between classical planning and learning-based methods. Rather than introducing a new planner, we construct a unified benchmark in which representative classical and learning-based methods face the same environments, motion constraints, information assumptions, and evaluation metrics. The test environment consists of planar domains populated with rotating sprinkler-like hazards that generate time-varying forbidden regions via sweeping angular sectors. Our results show a clear regime shift. In deterministic environments, classical planners achieve near-perfect success and higher-quality paths, though sometimes at the cost of substantial planning or replanning time. Under stochastic obstacle dynamics, however, online search becomes strongly budget-sensitive: low budgets lead to frequent failure, while high budgets improve success at the cost of latency and longer trajectories. PPO-based policies, trained under the same scenario distribution, consistently outperform in latency, success rate, and path quality in these stochastic regimes. Overall, the results indicate that uncertainty in obstacle evolution, more than partial observability, is the dominant factor determining which planning paradigm is practically effective for the problem at hand.

</details>

---

### [[20_Research/Papers/具身智能/Q-Shaped_Options_for_Hierarchical_Reinforcement_Learning|Q-Shaped Options for Hierarchical Reinforcement Learning]]

![[assets/2610.12135_first_page.png|800]]

- **arXiv**: [2610.12135](https://arxiv.org/abs/2610.12135)
- **PDF**: https://arxiv.org/pdf/2610.12135
- **详细分析**: [[20_Research/Papers/具身智能/Q-Shaped_Options_for_Hierarchical_Reinforcement_Learning|Q-Shaped Options for Hierarchical Reinforcement Learning]]
- **作者**: Clarisse Wibault, Antoine Gorceix, Antonio Léon Villares, Alexey Zakharov, Evangelos Chatzaroulas, Michael Matthews, Eduardo Pignatelli, Jakob Foerster
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Q-Shaped Options for Hierarchical Reinforcement Learning》归入 强化学习、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning to tackle long-horizon, goal-conditioned tasks requires an agent to reason over extended timescales and act across a broad range of states. In principle, Hierarchical Reinforcement Learning (HRL) addresses both challenges through the interaction between action (temporal) and state (spatial) abstraction. First, using an action abstraction to represent temporally extended behaviour as options reduces the effective decision horizon. Second, enabling different state abstractions at each level of the decision process permits greater data aggregation for learning. However, realising these two benefits of a hierarchical policy depends on learning an appropriate action abstraction. Current HRL algorithms fail in one of two ways. Some discard distinctions between options needed for optimal control, undermining hierarchy altogether. Others retain unnecessary distinctions, preserving horizon reduction, but forfeiting coarser state abstraction. In this work, we characterise three desiderata for an action abstraction. We introduce Q-Shaped Options (QSO) to address all three. QSO builds on an architecture with distinct state-value functions, Q functions and policies at each level of the hierarchy. It learns the action abstraction between consecutive levels as a shared encoder shaped by their respective Q functions. The low-level Q function uses the option as a goal, encouraging the abstraction to retain distinctions necessary for optimal control. The high-level Q function uses it as an action, encouraging unnecessary distinctions to be discarded. Across offline goal-conditioned locomotion and manipulation environments, QSO learns semantically meaningful option spaces and outperforms baselines, achieving non-zero performance in tasks where all other evaluated algorithms fail.

</details>

---

### [[20_Research/Papers/具身智能/A_Geometric_Approach_to_Soft_Actor-Critic_with_Zonotopes_for_Locomotion_Learning|A Geometric Approach to Soft Actor-Critic with Zonotopes for Locomotion Learning]]

![[assets/2610.12113_figure.png|800]]

- **arXiv**: [2610.12113](https://arxiv.org/abs/2610.12113)
- **PDF**: https://arxiv.org/pdf/2610.12113
- **详细分析**: [[20_Research/Papers/具身智能/A_Geometric_Approach_to_Soft_Actor-Critic_with_Zonotopes_for_Locomotion_Learning|A Geometric Approach to Soft Actor-Critic with Zonotopes for Locomotion Learning]]
- **作者**: Panagiotis Roditis, Panagiotis P. Filntisis, Petros Maragos
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.12（加权：具身智能 1.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《A Geometric Approach to Soft Actor-Critic with Zonotopes for Locomotion Learning》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-policy actor--critic methods control overestimation bias by taking the minimum of two critics. This uses the same aggregation rule everywhere, regardless of how the critics disagree. We propose \textbf{GeZo-SAC}, which uses auxiliary geometric representations to adapt critic pessimism to the state and action. Alongside its scalar value, each critic predicts a set of generators defining a zonotope. Probing this zonotope along sampled directions provides a geometric width, "subtracted from each critic value as a pessimistic offset, and a measure of disagreement between the two critics, aggregated with log-sum-exp. This disagreement controls how the critics are combined, moving from a width-weighted average toward the usual minimum as disagreement increases. At inference, the deployed policy is an unmodified SAC actor, since the generators are used only on the critic side during training.Across four MuJoCo-v5 locomotion benchmarks and six off-policy baselines, GeZo-SAC achieves the highest mean return on Ant-v5 and Hopper-v5 and remains competitive with other methods on the remaining tasks. Our analysis further shows that GeZo-SAC achieves the lowest average actuator work and action effort per metre among the evaluated methods, while maintaining near-zero measured overestimation frequency across all four environments.

</details>

---

### [[20_Research/Papers/具身智能/Recompose_and_Refine_Latent_Reasoning_Flows_for_Vision-Language-Action_Models|Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models]]

![[assets/2610.12090_figure.png|800]]

- **arXiv**: [2610.12090](https://arxiv.org/abs/2610.12090)
- **PDF**: https://arxiv.org/pdf/2610.12090
- **详细分析**: [[20_Research/Papers/具身智能/Recompose_and_Refine_Latent_Reasoning_Flows_for_Vision-Language-Action_Models|Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models]]
- **作者**: Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou, Xinyu He, Xu Zhang, Qinghua Zhang
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.8，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LaRA-VLA, RD-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and recomposes compatible latent fragments as the embodied context evolves, forming a reasoning route that follows the temporal structure and progress of successful computation. The route is then refined using current visual and proprioceptive evidence before it conditions action generation. Experiments on RoboMME and LIBERO-Plus show that FLOWMEM attains 48.0% and 77.3% success, outperforming memory-free policies by 1.7 and 4.1 percentage points, respectively. These results demonstrate the value of reusing successful latent computation for closed-loop VLA control.

</details>

---

### [[20_Research/Papers/机器人/Traceable_World_State_A_Provenance-Aware_State_Representation_and_Deterministic_Replay_Framework_for_Robotic_Systems|Traceable World State: A Provenance-Aware State Representation and Deterministic Replay Framework for Robotic Systems]]

![[assets/2610.12033_first_page.png|800]]

- **arXiv**: [2610.12033](https://arxiv.org/abs/2610.12033)
- **PDF**: https://arxiv.org/pdf/2610.12033
- **详细分析**: [[20_Research/Papers/机器人/Traceable_World_State_A_Provenance-Aware_State_Representation_and_Deterministic_Replay_Framework_for_Robotic_Systems|Traceable World State: A Provenance-Aware State Representation and Deterministic Replay Framework for Robotic Systems]]
- **作者**: Zoe Li
- **cs 子类**: cs.AI, cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Traceable World State: A Provenance-Aware State Representation and Deterministic Replay Framework for Robotic Systems》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic systems operating over extended tasks must maintain a world state assembled from observations arriving at different times, with varying confidence and potential revisions. Conventional representations emphasize latest estimates, hindering fact provenance, decision reproduction, or execution auditing. We present Traceable World State (TWS), a middleware-neutral semantic representation and reference runtime for provenance-aware robot world state. A TWS snapshot captures entities, relations, observations, confidence, and revision metadata. Validated update operations transform snapshots immutably, ordered updates support deterministic replay, and a canonical SHA-256 hash chain ensures tamper-evident logs. We evaluate TWS through schema conformance, complete state lifecycles, deterministic replay, and fault injection. Passing 38 tests across Python 3.10-3.14, the framework detects record corruptions, broken hash links, sequence discontinuities, and world mismatches. Across ten public BEHAVIOR-1K task definitions, TWS imported 153 entities and 146 relations with successful validation. On 103 NVIDIA Unitree G1 simulated trajectories containing 78,369 frames, TWS achieved exact terminal-state replay in all episodes and detected 412/412 injected corruptions with a 1.72% storage overhead over Plain JSONL.

</details>

---

### [[20_Research/Papers/具身智能/Humanoid_World_Action_Model_With_Joint_State--Action_Generation|Humanoid World Action Model With Joint State--Action Generation]]

![[assets/2610.12026_figure.png|800]]

- **arXiv**: [2610.12026](https://arxiv.org/abs/2610.12026)
- **PDF**: https://arxiv.org/pdf/2610.12026
- **详细分析**: [[20_Research/Papers/具身智能/Humanoid_World_Action_Model_With_Joint_State--Action_Generation|Humanoid World Action Model With Joint State--Action Generation]]
- **作者**: Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu, Zihan Lan, Weixin Mao, Yinhao Li, Zhen Fu, Hua Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.5（加权：具身智能 2.1，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Humanoid World Action Model With Joint State--Action Generation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robot. Without explicitly modeling the realized body state, future visual prediction must jointly explain scene evolution and discrepancies between reference actions and executed motion, making it difficult to associate an action with its physical outcome. We propose HWAM, a Humanoid World Action Model with joint state--action generation, which makes the robot's post-execution proprioceptive state an explicit prediction target. By jointly generating reference actions and their realized body states, HWAM directly incorporates supervision of executed motion into action learning. HWAM is trained through three complementary conditional paths. The Policy path jointly denoises state--action trajectories conditioned only on current observations, matching deployment conditions. Forward Dynamics Modeling (FDM) predicts future visual observations conditioned on actions and post-execution states, while Inverse Dynamics Modeling (IDM) reconstructs the joint trajectory from visual transitions. Together, these paths connect policy references, realized body motion, and visual outcomes. HWAM achieves the highest success rate among evaluated baselines on three real-robot tasks on the LimX OLI humanoid. On Candy Picking, HWAM achieves a 70.6% success rate, compared with 43.3% for Fast-WAM.

</details>

---

### [[20_Research/Papers/具身智能/REACT_Rolling_Denoising_and_Dual_Decoupling_for_Reactive_Robot_Control_with_VLA_Models|REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models]]

![[assets/2610.12007_figure.png|800]]

- **arXiv**: [2610.12007](https://arxiv.org/abs/2610.12007)
- **PDF**: https://arxiv.org/pdf/2610.12007
- **详细分析**: [[20_Research/Papers/具身智能/REACT_Rolling_Denoising_and_Dual_Decoupling_for_Reactive_Robot_Control_with_VLA_Models|REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models]]
- **作者**: Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren, Wanting Xu, Hongfei Niu, Chengyang He, Ge Sun, Ran Cheng, Qian Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon is denoised using the latest observation, the cleanest action block is executed, partially refined future blocks are shifted forward, and fresh noise is appended to the tail. As a result, each executed action block is refined across multiple recent observations before deployment. To support real-time control, we further introduce dual decoupling, which separates sensing, VLM encoding, DiT denoising, and action execution, enabling high-frequency observation updates and action streaming under practical compute constraints. Across the RoboTwin 2.0 simulation benchmark and real-world tasks spanning bimanual manipulation and dynamic control on multiple robot platforms, REACT improves task success and reduces reaction latency while producing smoother trajectories than frequent-replanning and asynchronous baselines.

</details>

---

### [[20_Research/Papers/大模型/Forms_of_LLM-Integrated_Applications_from_LLM-Chats_to_Autonomous_AI_Agent_System|Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System]]

![[assets/2610.11899_figure.png|800]]

- **arXiv**: [2610.11899](https://arxiv.org/abs/2610.11899)
- **PDF**: https://arxiv.org/pdf/2610.11899
- **详细分析**: [[20_Research/Papers/大模型/Forms_of_LLM-Integrated_Applications_from_LLM-Chats_to_Autonomous_AI_Agent_System|Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System]]
- **作者**: Irene Weber
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically. In the sources surveyed, labels do carry architectural content, most clearly in vendor usage: copilot denotes a router-worker architecture operating a host application under step-by-step user confirmation, while the more recent shift to the label agent coincides with AI-planned multi-step execution of which the user sees only the outcome. The coding agents of four major providers share one architecture, a reason-and-act loop delegating to subagents. This survey describes seven recurring forms---LLM chats, custom agents, retrieval-augmented generation (RAG), AI-enhanced workflows, copilots, coding agents, and, in part, agentic RAG---in a common vocabulary of agents and tools. Each is characterized along four structural dimensions (agentic RAG only partially): the architectural pattern, the control of execution and the point of user intervention, the number of agent calls per task, and tool use. An illustrative corpus of 22 systems from research publications and vendor documentation grounds the descriptions and shows where they reach their limit.

</details>

---

### [[20_Research/Papers/大模型/GRPODropout_Less_is_More_for_Online_Reinforcement_Learning_Rollouts|GRPODropout: Less is More for Online Reinforcement Learning Rollouts]]

![[assets/2610.11854_first_page.png|800]]

- **arXiv**: [2610.11854](https://arxiv.org/abs/2610.11854)
- **PDF**: https://arxiv.org/pdf/2610.11854
- **详细分析**: [[20_Research/Papers/大模型/GRPODropout_Less_is_More_for_Online_Reinforcement_Learning_Rollouts|GRPODropout: Less is More for Online Reinforcement Learning Rollouts]]
- **作者**: Hexuan Deng, Zihao Yan, Xuebo Liu, Shuo Nie, Yue Wang, Chen Wang, Zhaohua Zhang, Tianwen Jiang, Qiuyong Xiao, Jihong Zhang, Min Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《GRPODropout: Less is More for Online Reinforcement Learning Rollouts》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SCOPE-RL, UloRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) methods such as GRPO substantially improve large language model reasoning but often suffer from policy entropy collapse: the loss of sampling diversity weakens exploration and limits further improvement. Existing methods address this issue either through algorithm-level interventions, such as reward modification and entropy/KL regularization, or through token-level reweighting. We investigate a complementary perspective: entropy collapse can also be mitigated by changing which generated rollouts contribute to policy updates. Under the same sampling budget, not all rollouts contribute positively to an update, and selectively excluding some can improve learning. To address this, we propose GRPODropout: before the standard update, we use a simple strategy that selectively removes a small number of high-probability positive-advantage rollouts and recenters the retained advantages. To motivate this design, we develop a rollout-level theoretical analysis that guides method design and threshold selection. The method changes only rollout usage, and adds negligible computational overhead. Experiments show higher accuracy than original GRPO and higher actor entropy while using fewer rollout samples for updates, illustrating "less is more." This work provides insight into RL rollout usage: removing some rollouts can improve performance. Code is available at https://github.com/hexuandeng/GRPODropout/.

</details>

---

### [[20_Research/Papers/强化学习/Constrained_Command-Conditioned_Reinforcement_Learning_with_Bandit_Strategy_Selection_in_Real-Time_Strategy_Games|Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games]]

![[assets/2610.11663_figure.png|800]]

- **arXiv**: [2610.11663](https://arxiv.org/abs/2610.11663)
- **PDF**: https://arxiv.org/pdf/2610.11663
- **详细分析**: [[20_Research/Papers/强化学习/Constrained_Command-Conditioned_Reinforcement_Learning_with_Bandit_Strategy_Selection_in_Real-Time_Strategy_Games|Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games]]
- **作者**: Nick Leenders, Roy Lindelauf, Joost van Oijen, Boris Cule
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.1，强化学习 1.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GridNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning agents reach strong performance in real-time strategy games but can be brittle against opponents outside their training distribution. Separating strategic command selection from learned unit control allows different strategies to be selected for different opponents while reusing the same execution policy. This requires an executor that can follow different commands and measurable criteria for assessing whether it does so. We introduce a constrained command-conditioned Proximal Policy Optimization (PPO) policy, the executor, for MicroRTS, a real-time strategy environment. Discrete commands specify strategic objectives and behavioral requirements for economy, army composition, military posture, and worker policy over multiple environment steps; the executor determines the unit-level actions used to fulfill them. A Thompson-sampling bandit acts as the strategist, selecting command tuples from an estimate of the opponent's strategy built from in-game observations rather than opponent identity. In a controlled comparison with a flat PPO baseline trained with the same architecture, budget, curriculum and self-play league, the strategist-executor system wins significantly more often against three of the four strongest opponents on a training map, including the two strongest held-out ones (0.55 to 0.97 and 0.01 to 0.34), with no significant difference against the others.

</details>

---

### [[20_Research/Papers/机器人/Neural_Networks_for_Temporal_Pattern_Recognition_and_Dynamic_Arm_Gesture_Speed_Estimation_for_Robot_Control|Neural Networks for Temporal Pattern Recognition and Dynamic Arm Gesture Speed Estimation for Robot Control]]

![[assets/2610.11631_figure.png|800]]

- **arXiv**: [2610.11631](https://arxiv.org/abs/2610.11631)
- **PDF**: https://arxiv.org/pdf/2610.11631
- **详细分析**: [[20_Research/Papers/机器人/Neural_Networks_for_Temporal_Pattern_Recognition_and_Dynamic_Arm_Gesture_Speed_Estimation_for_Robot_Control|Neural Networks for Temporal Pattern Recognition and Dynamic Arm Gesture Speed Estimation for Robot Control]]
- **作者**: Milán Zsolt Bagladi, László Gulyás
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Neural Networks for Temporal Pattern Recognition and Dynamic Arm Gesture Speed Estimation for Robot Control》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying intelligent robotic systems that interact with humans through gestures requires neural networks capable of recognizing diverse temporal patterns. We present a systematic benchmark of ten abstract sequential tasks--five permutation-invariant (set) and five order-dependent (sequence) problems--evaluated across eighteen neural network architectures spanning recurrent, convolutional, attention-based, and set-function families. Beyond the core architecture-task grid, we explore numerous preprocessing and target-variable transformations, yielding more than 250 distinct experimental configurations. All variants are trained and tested under strictly identical conditions (fixed random seeds, shared hyperparameters, shared data splits) to ensure fair and reproducible comparison. Ranking across all ten tasks reveals four consistently top-performing architectures--BiGRU, TCN, Conv1D, and GRUReLU--all compact enough for real-time deployment (under 2,000 parameters in the benchmark setting). Based on this ranking, we apply three architecturally diverse top models (BiGRU, TCN, and GRUReLU) to a practical robotics problem: estimating the execution speed of dynamic arm gestures from skeletal keypoint sequences. Three speed interpretations (peak count, period time, and mean spike spacing) are evaluated on a custom dataset of eight traffic-related gesture classes comprising 256,710 frames recorded via OpenPose. The best configuration achieves a mean absolute error of 0.198 on the peak-count interpretation, corresponding to roughly 5% relative error, while the period-time interpretation reaches approximately 4% relative error, and the mean spike spacing interpretation approximately 8% relative error. These results demonstrate that neural networks can reliably estimate gesture speed from skeletal data, opening a path toward speed-aware gesture-controlled robotic systems.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Orchestrate_Evolutionary_Search_Progression-Aware_Deep_Reinforcement_Learning_for_Dynamic_DE-CMA-ES_Coordination_in_Optimization|Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating]]

![[assets/2610.11546_figure.png|800]]

- **arXiv**: [2610.11546](https://arxiv.org/abs/2610.11546)
- **PDF**: https://arxiv.org/pdf/2610.11546
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Orchestrate_Evolutionary_Search_Progression-Aware_Deep_Reinforcement_Learning_for_Dynamic_DE-CMA-ES_Coordination_in_Optimization|Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating]]
- **作者**: Lechen Li, Rongye Shi, Wanhuan Zhou
- **cs 子类**: cs.AI, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.1（加权：大模型 0.1，强化学习 2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Learning to Orchestrate Evolutionary Search: Progression-Aware Deep Reinforcement Learning for Dynamic DE-CMA-ES Coordination in Optimization and Structural Model Updating》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, ERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Solving high-dimensional structural model updating problems requires an algorithm capable of navigating complex, non-convex landscapes with correlated parameters. Existing hybrid evolutionary algorithms typically rely on static architectures or fixed switching rules, resulting in disjointed search phases. To address this, this study proposes a Deep Reinforcement Learning-governed dynamic DE-CMAES Orchestration (DRL-DCO) algorithm, in which a Deep Deterministic Policy Gradient (DDPG)-based actor-critic agent continuously governs the evolutionary process as a single, unified system rather than a mechanical concatenation of algorithms. Guided by a progression-aware state representation and a diversity-informed reward, the agent fluidly reallocates computational resources between the differencevector-based exploration of Differential Evolution (DE) and the covariance-guided exploitation of CMA-ES, while jointly regulating population size, elite preservation, and a restart mechanism to escape local optima. This allows DRL-DCO to autonomously transition between exploration-dominant, exploitation-dominant, and mixed-strategy regimes across generations. Beyond the training phase, the trained actor can operate in a supervision-free inference mode, where the internalized policy autonomously orchestrates DE and CMA-ES control from observed search states through forward inference alone, without critic evaluation or weight updates, enabling faster deployment while retaining full effectiveness. Validated on high-dimensional single-objective optimization benchmarks and the IASC-ASCE structural health monitoring benchmark, DRL-DCO achieves superior convergence accuracy and robustness compared to state-of-the-art adaptive and hybrid evolutionary algorithms, as well as single-operator DRL-governed baselines.

</details>

---

### [[20_Research/Papers/具身智能/RoboAware_Learning_to_Coordinate_Embodied_Skills_from_Counterfactual_Outcomes|RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes]]

![[assets/2610.11480_figure.png|800]]

- **arXiv**: [2610.11480](https://arxiv.org/abs/2610.11480)
- **PDF**: https://arxiv.org/pdf/2610.11480
- **详细分析**: [[20_Research/Papers/具身智能/RoboAware_Learning_to_Coordinate_Embodied_Skills_from_Counterfactual_Outcomes|RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes]]
- **作者**: Bohan Zhou, Xingbei Chen, Emily Huang, Weilin Ruan, Haojian Huang, Yehang Zhang, Zexi Li, Wenqian Li, Qize Yu, Zetian Song, Leyi Wu, Jinghao Li...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.2，强化学习 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboAware: Learning to Coordinate Embodied Skills from Counterfactual Outcomes》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Harness-VLA, NeuGraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied coding agents can combine modular robot skills with frozen end-to-end policies, yet effective composition requires anticipating which policy family will succeed in the current physical state. We present RoboAware, which builds on coding agents' skill orchestration by learning only a state-conditioned responsibility coordinator from counterfactual outcomes. Inspired by the success of REPL, we propose the $P^5$ schema and formulate a hierarchical MDP based on it. $P^5$ organizes skills uniformly into five semantic stages, defining where responsibility can be compared. To address the lack of counterfactual branch outcomes in existing work, we introduce State-Locked Counterfactual Branching (SCB), which restores the same training state to generate and execute a code block from each admissible family, exposing outcomes that selected-branch experience leaves unobserved. Building on this, we propose Execution-Aware Learning (EAL), which combines Monte Carlo tree search with Q-learning to distill these outcomes into family-conditioned values. At deployment, the coordinator selects the policy family according to observable context, and the frozen coding agent generates the next local code block. Comprehensive single-episode evaluations on 100 tasks show that RoboAware reaches a 77.0% overall success rate, with SOTA averages of 90.0% on RoboSuite, 73.8% on diverse LIBERO-Pro task clusters, and 90.0% on challenging RoboTwin bimanual tasks, outperforming existing code-as-policy and VLA-harness baselines.

</details>

---

### [[20_Research/Papers/具身智能/Rewiring_Semantics,_Dynamics,_and_Control_A_Simple_yet_Effective_Action-Centric_Tri-Stream_Transformer|Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer]]

![[assets/2610.11416_figure.png|800]]

- **arXiv**: [2610.11416](https://arxiv.org/abs/2610.11416)
- **PDF**: https://arxiv.org/pdf/2610.11416
- **详细分析**: [[20_Research/Papers/具身智能/Rewiring_Semantics,_Dynamics,_and_Control_A_Simple_yet_Effective_Action-Centric_Tri-Stream_Transformer|Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer]]
- **作者**: Shuang Luo, Yilun Kong, Yunpeng Qing, Yihang Jiao, Zhi Hou, Shunyu Liu, Xiaogang Wang, Dacheng Tao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，世界模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Rewiring Semantics, Dynamics, and Control: A Simple yet Effective Action-Centric Tri-Stream Transformer》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BagelVLA, InternVLA, Real-World, TriVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a prominent framework for complex robotic manipulation, building on the strong semantic understanding of pretrained Vision-Language Models (VLMs). However, such VLM backbones offer insufficient physical dynamics priors, which limits the generalization capabilities of robot policies. Recent efforts therefore integrate video-generation World Models (WMs) into robot policies through various strategies, using predictive dynamics to facilitate action generation. Despite these advances, harnessing semantic understanding and dynamics prediction as complementary guidance for action generation remains challenging. In this paper, we introduce $\mathrm{ACT}^3$, a simple yet effective Action-Centric Tri-Stream Transformer that fuses semantic and dynamics information into control actions while preserving the distinct roles of context streams. Specifically, $\mathrm{ACT}^3$ enables the dedicated action expert to access VLM and WM representations through layerwise attention, with each backbone attending only within its own stream. This straightforward interaction design maintains independent forward propagation in the context streams while allowing both backbones to be updated through control supervision. Experiments on both simulated and real-world robotic manipulation benchmarks show that the proposed $\mathrm{ACT}^3$ yields results superior to its counterparts.

</details>

---

### [[20_Research/Papers/大模型/SynCo_Data_Synthesis_Co-Training_for_Self-Evolving_LLMs_via_Multi-Agent_Reinforcement_Learning|SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning]]

![[assets/2610.11345_figure.png|800]]

- **arXiv**: [2610.11345](https://arxiv.org/abs/2610.11345)
- **PDF**: https://arxiv.org/pdf/2610.11345
- **详细分析**: [[20_Research/Papers/大模型/SynCo_Data_Synthesis_Co-Training_for_Self-Evolving_LLMs_via_Multi-Agent_Reinforcement_Learning|SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning]]
- **作者**: Wei Yang, Shawn Li, Yuehan Qin, Yawei Wang, Mingxi Wang, Shixuan Li, Tiankai Yang, Jiate Li, Jesse Thomason, Xuezhe Ma, Yue Zhao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Agent-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving LLM agents promise to improve autonomously through continual interaction and learning, reducing their dependence on manually curated supervision. Realizing this promise requires not only updating the agent, but also evolving its training experience as its capabilities change. However, most existing pipelines rely on static datasets or separately updated synthesis models, causing previously useful tasks to become trivial while overly difficult tasks remain uninformative. This growing mismatch between agent capability and training experience limits sustained self-improvement. To address this problem, we propose SynCo, an agentic data synthesis co-training framework for self-evolving LLMs based on multi-agent reinforcement learning. SynCo jointly optimizes two independently parameterized agents: a Synthesizer that constructs training tasks from the Reasoner's evolving capability state, and a Reasoner that learns from the resulting experience. Each synthesized task induces multiple Reasoner rollouts whose outcomes provide complementary rewards to both agents. Correctness feedback improves the Reasoner, while task quality, answer reliability, and outcome-grounded teachability guide the Synthesizer. Their updates are fed back into subsequent synthesis rounds, allowing the task-solving policy and its training distribution to evolve together. Extensive experiments across eight mathematical reasoning benchmarks demonstrate that SynCo substantially outperforms a broad range of existing synthetic-data methods and controlled baselines, achieving the strongest overall performance while deriving most of its gains from previously unsolved problems.

</details>

---

### [[20_Research/Papers/大模型/LLM-IDEA_Identifiability-Driven_Experimental_Agent_for_Autonomous_Discovery_of_Mechanistic_World_Models|LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models]]

![[assets/2610.11253_first_page.png|800]]

- **arXiv**: [2610.11253](https://arxiv.org/abs/2610.11253)
- **PDF**: https://arxiv.org/pdf/2610.11253
- **详细分析**: [[20_Research/Papers/大模型/LLM-IDEA_Identifiability-Driven_Experimental_Agent_for_Autonomous_Discovery_of_Mechanistic_World_Models|LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models]]
- **作者**: Surya Shetty, Ulisses Braga-Neto
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 1.9（加权：大模型 1.1，世界模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ActiveSciBench, AstaBench, BoxingGym, Gravity-Bench, LLM-SRBench, NewtonBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents are being increasingly deployed as autonomous scientists, designing experiments and inferring mechanistic world models with minimal human oversight. Yet identifiability is often overlooked: when a plateau is reached, the agent needs to know whether it is not yet capable enough or the model simply is not identifiable from the data, in which case no amount of further experimentation of the same kind can help. We propose the Identifiability-Driven Experimental Agent (LLM-IDEA) for closed-loop discovery with an identifiability engine that returns a three-way plateau verdict: capability limit, resolvable within the design class, or certified exhausted. On ODEBench, 60 of the 62 systems with free constants are identifiable at round 0; the RC circuit is certified exhausted for every experiment that protocol can run, and a harvesting model is resolvable by one added initial condition. The identifiability engine reproduces known verdicts on Lotka-Volterra, Van der Pol, Lorenz, and a pharmacokinetic model, where it recommends the intravenous arm pharmacologists use, and it ranks the depth scorer of our own benchmark last among four observation designs. On the DiscoverPhysics benchmark, it finds two public worlds whose explanation rubric rewards a distinction no legal experiment can make, and every model there with accurate trajectories failed the explanation grade (15 of 15, against 5 of 9 in identifiable worlds, p = 0.012). On the Alien Universe, a two-body testbed we propose in which a force law switches between a provably non-identifiable and an identifiable protocol, LLM-IDEA on the identifiable protocol reaches discovery depth at least three on 8/8 seeds versus 1/8 without it. An autonomous discovery agent can thus compute, rather than guess, whether a plateau calls for more search, a better experiment of the same kind, or a different kind of experiment.

</details>

---

### [[20_Research/Papers/机器人/SafeInferCom_Safe_Inference-Time_Compute_via_Verifier-Guided_Mid-Generation_Intervention_for_Robotic_Task_Planning|SafeInferCom: Safe Inference-Time Compute via Verifier-Guided Mid-Generation Intervention for Robotic Task Planning]]

![[assets/2610.11223_figure.png|800]]

- **arXiv**: [2610.11223](https://arxiv.org/abs/2610.11223)
- **PDF**: https://arxiv.org/pdf/2610.11223
- **详细分析**: [[20_Research/Papers/机器人/SafeInferCom_Safe_Inference-Time_Compute_via_Verifier-Guided_Mid-Generation_Intervention_for_Robotic_Task_Planning|SafeInferCom: Safe Inference-Time Compute via Verifier-Guided Mid-Generation Intervention for Robotic Task Planning]]
- **作者**: Weizhe Xu, Jialiang Fan, Mengyu Liu, Fanxin Kong
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《SafeInferCom: Safe Inference-Time Compute via Verifier-Guided Mid-Generation Intervention for Robotic Task Planning》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Reasoning Language Models (LRLMs) enable multi-step reasoning for robotic task planning, but continued reasoning can overwrite valid intermediate plans or leave constraint violations unresolved, reducing planning reliability and wasting inference-time computation. We develop an inference-time monitor that exposes and verifies intermediate plans without disrupting the original decoding trajectory. Building on this monitor, we propose SafeInferCom, a formal verifier-guided framework that preserves valid intermediate plans and directs error correction during generation. Experiments across multiple LRLMs and planning domains reveal reasoning-response inconsistency and limited self-correction under one-shot inference. SafeInferCom improves planning success and accelerates error correction relative to one-shot inference. When combined with iterative refinement, it further improves success while reducing token usage compared with refinement alone. We additionally evaluate SafeInferCom in VirtualHome and provide a real-world robotic-arm demonstration.

</details>

---

### [[20_Research/Papers/大模型/RAG-Stress_Probing_the_Limits_of_Evidence_Reliance_in_Retrieval-Augmented_Generation|RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation]]

![[assets/2610.11183_figure.png|800]]

- **arXiv**: [2610.11183](https://arxiv.org/abs/2610.11183)
- **PDF**: https://arxiv.org/pdf/2610.11183
- **详细分析**: [[20_Research/Papers/大模型/RAG-Stress_Probing_the_Limits_of_Evidence_Reliance_in_Retrieval-Augmented_Generation|RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation]]
- **作者**: Shunyuan Zhou, Hao Chen, Tianyu Wang, Goose Lin, Zaiyuan Wang, Haiying Zhao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HotpotQA, MedQA, SearchQA, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Following retrieved evidence does not guarantee factual correctness: misleading evidence can induce a model to replace an answer it previously gave correctly. Standard accuracy measures obscure this behavior by combining answer replacement with preexisting errors. We introduce RAG-Stress, a controlled diagnostic protocol for examining the limits of evidence reliance in retrieval-augmented generation. The protocol holds the question and reference answer fixed, edits one assertion to support a designated incorrect answer, and crosses two source priority policies with three positions of the answer span within the evidence text. We measure misleading rate (MR) on each model's subset of questions answered correctly without retrieval, alongside clean accuracy on the full evaluation set. We evaluate fifteen systems spanning API models, open models, and search agents trained with reinforcement learning on TriviaQA-RC, HotpotQA, and SearchQA, with additional English and Chinese MedQA evaluations. Instructions that prioritize documents consistently produce higher MR than those permitting reliance on prior knowledge. Averaged over models and positions, the gap ranges from 10.9 to 13.5 percentage points across the three QA datasets. Mean MR follows End $&gt;$ Beginning $&gt;$ Middle under both policies, although individual models do not uniformly follow this ordering. A separate paired audit of 500 questions and two checkpoints supports increased harmful override without establishing a corresponding improvement in beneficial correction. These findings distinguish evidence adherence from factual reliability and motivate evaluating whether retrieved evidence preserves, replaces, or corrects a model's answers.

</details>

---

### [[20_Research/Papers/强化学习/Higher-Order_Action_Supervision_Makes_A_Strong_Policy_Class|Higher-Order Action Supervision Makes A Strong Policy Class]]

![[assets/2610.11175_figure.png|800]]

- **arXiv**: [2610.11175](https://arxiv.org/abs/2610.11175)
- **PDF**: https://arxiv.org/pdf/2610.11175
- **详细分析**: [[20_Research/Papers/强化学习/Higher-Order_Action_Supervision_Makes_A_Strong_Policy_Class|Higher-Order Action Supervision Makes A Strong Policy Class]]
- **作者**: Peng Cheng, Yunxian Hou, Zhi Zhou, Qian Zhang, Chang Huang, Xianyuan Zhan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，强化学习 0.4，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Higher-Order Action Supervision Makes A Strong Policy Class》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, LipsNet, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern data-driven decision-making methods, such as imitation learning (IL) and reinforcement learning (RL), have achieved great success in solving many complex tasks. However, these methods often suffer from serious control instability and robustness issues when applied in real-world applications such as robotics and autonomous driving, posing notable challenges for their practical deployment. We argue that this instability issue stems largely from their limitations in solely supervising and optimizing zeroth-order actions (i.e., the action labels), failing to account for higher-order action dynamics and temporal consistency. In this paper, we show that simultaneously supervising both zeroth- and first-order actions can dramatically enhance policies' performance and control robustness. To achieve this, we introduce a novel and elegant loss scheme supported by formal theoretical guarantees that can equip any off-the-shelf policy model (e.g., deterministic, stochastic, or flow policies) with the capability for higher-order action supervision, without requiring any structural modifications. Moreover, our proposed method can serve as a lightweight plug-and-play module that seamlessly integrates with a broad spectrum of existing offline RL frameworks. Extensive evaluations on OGBench and D4RL demonstrate that our approach yields substantial performance and robustness improvements across a wide range of continuous control environments. Notably, our method can also enhance policies' out-of-distribution (OOD) generalization capability in the challenging low-data regime, making it an ideal tool in tackling many real-world control problems.

</details>

---

### [[20_Research/Papers/具身智能/PMTRM_Pseudo-Memory_Temporal_Re-encoding_Module_for_Embodied_Policy_Learning|PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning]]

![[assets/2610.11168_figure.png|800]]

- **arXiv**: [2610.11168](https://arxiv.org/abs/2610.11168)
- **PDF**: https://arxiv.org/pdf/2610.11168
- **详细分析**: [[20_Research/Papers/具身智能/PMTRM_Pseudo-Memory_Temporal_Re-encoding_Module_for_Embodied_Policy_Learning|PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning]]
- **作者**: Changchuan Yang, Haoxuan Xu, Wenbo Chen, Shuai Ren, Jianlong Zheng, Huarui Zhang, Tianfu Li, Guanzhong Tian
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PMTRM: Pseudo-Memory Temporal Re-encoding Module for Embodied Policy Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation often contains repeated motions whose local observations look similar at different phases. When these phases require different actions, a policy that relies mainly on the current observation may repeat completed motions or switch phases at the wrong time. To address this phase ambiguity, we present the Pseudo-Memory Temporal Re-encoding Module (PMTRM), a lightweight plug-in module with only 7.61M parameters that encodes a bounded history of executed states and actions into a latent sequence for existing policies. To help distinguish phases, a temporal heterogeneity objective penalizes positive similarity between distant positions in this sequence, while anchor and reconstruction losses preserve information needed for action prediction. The reconstruction decoder is used only during training, leaving the temporal re-encoder to supply history to the policy at inference. We train the module progressively on synthetic sequences and robot data, then jointly with the policy, using temporal masking to accommodate partial histories. This integration retains the original action head and action space and adds auxiliary losses to the original policy loss. Experiments with multiple policy backbones in simulation and on a real robot show improved task success on tasks with phase ambiguity, with little additional computation.

</details>

---

### [[20_Research/Papers/具身智能/iAm.md_Robot_Skill_Self-Assessment_through_Agentic_Introspection_for_Unknown_Open-Vocabulary_Domains|iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains]]

![[assets/2610.10962_figure.png|800]]

- **arXiv**: [2610.10962](https://arxiv.org/abs/2610.10962)
- **PDF**: https://arxiv.org/pdf/2610.10962
- **详细分析**: [[20_Research/Papers/具身智能/iAm.md_Robot_Skill_Self-Assessment_through_Agentic_Introspection_for_Unknown_Open-Vocabulary_Domains|iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains]]
- **作者**: Vincenzo Guarino, Emanuele Musumeci, Vincenzo Suriani, Daniele Nardi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.3，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《iAm.md: Robot Skill Self-Assessment through Agentic Introspection for Unknown Open-Vocabulary Domains》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PlanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic AI based on Large Language Model generalization capabilities offers a wide range of potential applications, including planning for embodied tasks. For example, embodied agents based on Foundation models can generate plausible plans in autonomous robotics scenarios. Due to limited context windows or hallucinatory phenomena in the next-token prediction formulation, behaviors may be generated without establishing whether the deployed robot and the observed environment actually support the requested operation, in what we call a "grounding failure". Thanks to the recent improvements in reasoning capabilities of foundation models, autonomous robot behavior generation problem can be formulated as a code generation problem. We present iAm.md, a Markdown standard and generation framework, that allows anchoring this process in complementary forms of deployment evidence. Through open-vocabulary semantic mapping, we combine local vision-language detections and object segmentation and refer them to persistent object records in this intermediate standardized representation, allowing agentic introspection. We then study this new technique on a simulated TIAGo, on navigation-and-manipulation tasks, showing how this standardized representation jointly supports skill self-assessment and executable task generalization.

</details>

---

### [[20_Research/Papers/大模型/StoreBench_A_Live-Commerce_Environment_for_Evaluating_and_Training_Autonomous_Operator_Agents|StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents]]

![[assets/2610.10942_first_page.png|800]]

- **arXiv**: [2610.10942](https://arxiv.org/abs/2610.10942)
- **PDF**: https://arxiv.org/pdf/2610.10942
- **详细分析**: [[20_Research/Papers/大模型/StoreBench_A_Live-Commerce_Environment_for_Evaluating_and_Training_Autonomous_Operator_Agents|StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents]]
- **作者**: Daksh Raghuvanshi, Ved Vedere, Yifan Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.85，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MerchantBench, StoreBench, Vending-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning environments are now a primary lever for improving large language model (LLM) capabilities in post-training, yet most agentic benchmarks remain static: the world moves only when the agent acts, the reward is a terminal verdict, and the pass bar is set arbitrarily. We introduce StoreBench, a live-commerce environment in which an agent runs a mid-size online apparel store on a production-grade commerce backend, testing long-horizon planning and economic judgment under uncertainty. Customers order around the clock, suppliers reprice and fail, and market shocks arrive with partial or no warning. The agent acts through the same 29 merchant tools a human operator would use, under a windowed operation budget that makes simulated time a function of actions taken, so model latency cannot influence simulated time. Pass thresholds are calibrated against scripted anchor policies, the reward is hardened against a catalogue of reward hacks, and every episode replays identically given a sequence of actions. We evaluate seven frontier LLMs on 11 scenarios of 30 to 45 days and a full simulated year, over three world seeds at matched reasoning effort. No model matches the scripted smart-triage policy on average: the best, DeepSeek-V4-Pro, passes 49% of task-seed cells against the heuristic's 97%. Human experts working through the same tools and budgets outscore every model (mean composite 0.708 vs. 0.700). Over a full simulated year under the Claude Code harness, most models show dramatic performance improvement. In a GRPO post-training run, Qwen3.5-27B trained on only five disjoint tasks raises its mean composite on the held-out evaluation tasks from 0.136 to 0.373. We release five example training-split tasks, ten sample trajectories, and the scoring and verification tooling; the full environment and evaluation suite are withheld to keep the benchmark uncontaminated.

</details>

---

### [[20_Research/Papers/具身智能/NavGPT-3_Harnessing_Context_in_a_Hierarchical_Navigation_Runtime|NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime]]

![[assets/2610.10787_figure.png|800]]

- **arXiv**: [2610.10787](https://arxiv.org/abs/2610.10787)
- **PDF**: https://arxiv.org/pdf/2610.10787
- **详细分析**: [[20_Research/Papers/具身智能/NavGPT-3_Harnessing_Context_in_a_Hierarchical_Navigation_Runtime|NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime]]
- **作者**: Gengze Zhou, Yicong Hong, Jiazhao Zhang, Xunyi Zhao, Jian Zhou, Zixing Lei, Zun Wang, Chongyang Zhao, Xionghui Chen, Stephen Gould, Anton van den Hengel, Qi Wu
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型, 世界模型
- **相关性评分**: 2.17（加权：具身智能 0.9，大模型 0.25，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InternVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language models trained with long-horizon agentic reinforcement learning can generalize knowledge through reasoning, express precise actions, and pursue goals over many steps, raising the ceiling on what an embodied agent can understand and decide. Physical interaction, however, remains the domain of action policies, which provide dense, low-latency control. We present NavGPT-3, a harness that connects the two models, with an OS-like runtime built above it: reasoning, acting, and monitoring run as threads with their own context, tools, and permissions, while the runtime schedules them and decides which thread controls the robot's motion, so that the robot can react to sudden real-world events through interruption and thread switching. Beneath it, our action policy NavGPT VLA, trained on 19.28M examples, allocates visual tokens using codec allocation, in proportion to scene change; its 8B model alone reaches 74.51 SR on R2R-CE and leads RxR-CE with 78.19 SR. With the complete harness, NavGPT-3 sets the state of the art on R2R-CE (81.51 SR) and, for the first time, brings an autonomous agent to human level: on RxR-CE it matches human followers in success (90.43 vs. 90.4 SR) and path fidelity (78.47 vs. 77.7 nDTW) at 1 min 22 s per episode, versus roughly 3 min for a human. We comprehensively ablate the harness design and the interaction between the two models, showing how tools and the action policy shape the path from language-model reasoning to physical control: when NavGPT VLA executes the route, the reasoning loop shortens and the system's minimum reaction time falls from 3-19 s per language-model decision to 0.5-1 s per action-policy step (1-2 Hz). These results show that designing this embodied interface is central to connecting frontier language-model intelligence with low-level physical control. We will release all models, code, and evaluation records.

</details>

---

### [[20_Research/Papers/世界模型/MemoWM_How_World_Models_Change_What_Agents_Need_to_Remember|MemoWM: How World Models Change What Agents Need to Remember]]

![[assets/2610.10778_figure.png|800]]

- **arXiv**: [2610.10778](https://arxiv.org/abs/2610.10778)
- **PDF**: https://arxiv.org/pdf/2610.10778
- **详细分析**: [[20_Research/Papers/世界模型/MemoWM_How_World_Models_Change_What_Agents_Need_to_Remember|MemoWM: How World Models Change What Agents Need to Remember]]
- **作者**: Bingfan Zeng, Zhisheng Chen, Chenbo Sang, Zhengwei Xie, Jinpeng Wang, Xiangchen Guan, Rui Qian, Zheng Lu, Jingwei Song
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《MemoWM: How World Models Change What Agents Need to Remember》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term agents face growing storage demands as they accumulate experience. World models capture reusable regularities that can reduce the information stored for each experience. We formulate the problem of memory allocation conditioned on a world model and introduce MemoWM, a framework that uses shared predictions to compress retained information and reconstruct omitted content. Its task-aware allocation rule balances the expected impact of reconstruction errors against storage cost, retaining information with downstream value beyond the predictive prior. Across five long-term agent-memory benchmarks, MemoWM achieves 42.42\% average answer accuracy, exceeding the strongest baseline by 2.62 percentage points, while reducing average experience-specific storage by 53.9\% relative to MIRIX, the most storage-efficient baseline. Further analysis shows that stronger world models reduce per-experience storage at comparable task quality. Accounting for model parameters reveals a trade-off between shared model capacity and recurring storage costs, with the capacity that minimizes total storage increasing as more interactions are retained. Our code is available at https://github.com/Feld-maxiu/MemoWM.

</details>

---

### [[20_Research/Papers/机器人/Masked_Generative_Motion_Planning_with_Geometry-Guided_Token_Search|Masked Generative Motion Planning with Geometry-Guided Token Search]]

![[assets/2610.10646_figure.png|800]]

- **arXiv**: [2610.10646](https://arxiv.org/abs/2610.10646)
- **PDF**: https://arxiv.org/pdf/2610.10646
- **详细分析**: [[20_Research/Papers/机器人/Masked_Generative_Motion_Planning_with_Geometry-Guided_Token_Search|Masked Generative Motion Planning with Geometry-Guided Token Search]]
- **作者**: Lipeng Zhuang, Yingdong Ru, Shiyu Fan, Edmond S. L. Ho, Gerardo Aragon Camarasa, Paul Henderson
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Masked Generative Motion Planning with Geometry-Guided Token Search》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative motion planners typically use learned trajectory priors for initial generation, while leaving test-time repair to local continuous refinement. We introduce Masked Generative Motion Planning (MGMP), which extends the learned prior from efficient parallel generation to structural repair. A masked generative transformer generates discrete trajectory candidates in parallel, and Geometry-Guided Token Search (GGTS) uses scene geometry to target where to edit and which prior-supported alternatives to evaluate. This turns refinement into an efficient search over discrete motion alternatives, enabling route-level restructuring beyond local trajectory deformation. MGMP achieves 96% success on Ring Maze and 82% repair success on Controlled Route Invalidation on Kuka, exceeding the strongest external baselines by 23 and 25 percentage points, respectively. It further generalizes to unseen layouts, additional obstacles, unseen geometries, single- and dual-arm planning, and real-world Baxter tasks.

</details>

---
