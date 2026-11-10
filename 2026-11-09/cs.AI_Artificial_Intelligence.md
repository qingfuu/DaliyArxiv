# cs.AI | Artificial Intelligence | 2026-11-09

#arxiv #ComputerScience

**论文数**: 39

### [[20_Research/Papers/具身智能/On_Agentic_Manipulation_Policies|On Agentic Manipulation Policies]]

![[assets/2611.09892_figure.png|800]]

- **arXiv**: [2611.09892](https://arxiv.org/abs/2611.09892)
- **PDF**: https://arxiv.org/pdf/2611.09892
- **详细分析**: [[20_Research/Papers/具身智能/On_Agentic_Manipulation_Policies|On Agentic Manipulation Policies]]
- **作者**: Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi, Fahad Islam, Xueting Li, Jean-Baptiste Regli, Kejia Ren, Petr Švec, David J. Yoon, Matthias Müller...
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《On Agentic Manipulation Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CaP-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work on robot manipulation has focused on specialist policies trained on demonstrations. We show that generalist AI models can control manipulators more reliably than specialist policies such as vision-language-action models (VLAs) and world-action models (WAMs). We systematically analyze agentic manipulation policies (AMPs), in which a generalist AI model commands the manipulator directly, adapting its actions as the task unfolds. We present AMP1, a reference harness that runs unchanged across single-arm, bimanual, and mobile manipulation. AMP1 achieves state-of-the-art results on the RoboLab-120 and CaP-Gym benchmarks, with no demonstrations or task-specific training. On RoboLab-120, AMP1 reaches an 85.6\% success rate zero-shot, compared to 49.2\% and 42.9\% for leading VLA and WAM policies. The agent succeeds zero-shot in 104 of 108 real-world trials spanning twelve tasks and three robot instances, reducing failure rates by 20x and 15x relative to strong VLA and WAM baselines. The basic harness supplies no grasping, pushing, or placing skills; the agent develops its own strategies, such as searching for hidden objects, using objects as tools, and calibrating its cameras. With the addition of a persistent memory store, the agent can also learn from experience: an augmented harness with a memory representation that is carried across episodes lowers the failure rate on RoboDojo bimanual manipulation tasks by 4.6x relative to zero-shot deployment. Our analysis suggests that AMPs are substantially more general and robust than specialist manipulation policies, providing a promising foundation for robot manipulation.

</details>

---

### [[20_Research/Papers/强化学习/On_the_Reliability_of_Majority-Vote_Pseudo-Labels_in_Test-Time_Reinforcement_Learning|On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning]]

![[assets/2611.09872_figure.png|800]]

- **arXiv**: [2611.09872](https://arxiv.org/abs/2611.09872)
- **PDF**: https://arxiv.org/pdf/2611.09872
- **详细分析**: [[20_Research/Papers/强化学习/On_the_Reliability_of_Majority-Vote_Pseudo-Labels_in_Test-Time_Reinforcement_Learning|On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning]]
- **作者**: Haoyu Wang, Ru Wang, Yuanyuan Wang, Jiaxian Guo, Mingming Gong
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the downstream effects of finite-rollout variation. We propose \emph{Prompt-Conditional Distributionally Robust DPO (PC-Dr.DPO)}, which conditions within-prompt robust reweighting on observed vote reliability to make updates from sampling-sensitive prompts more conservative. We further introduce a cache-based mechanism to reduce self-supervised forgetting during online adaptation. Across six mathematical and knowledge-intensive reasoning benchmarks and five model backbones, PC-Dr.DPO matches or outperforms the strongest TTRL baseline in 24 of 30 settings.

</details>

---

### [[20_Research/Papers/具身智能/Grasp-TAGS_Task-Aware_Grasp_Selection_via_Critic_Distillation_for_Prehensile_Loco-Manipulation|Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation]]

![[assets/2611.09864_figure.png|800]]

- **arXiv**: [2611.09864](https://arxiv.org/abs/2611.09864)
- **PDF**: https://arxiv.org/pdf/2611.09864
- **详细分析**: [[20_Research/Papers/具身智能/Grasp-TAGS_Task-Aware_Grasp_Selection_via_Critic_Distillation_for_Prehensile_Loco-Manipulation|Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation]]
- **作者**: Xun Tu, Minghao Zou, Karthik Desingh
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Loco-manipulation, which requires mobile manipulators to coordinate locomotion and manipulation over long horizons, is a key capability for large-object rearrangement in applications such as service robotics and warehouse automation. Despite recent progress, reliably executing these tasks remains challenging because performance depends on complex robot-object and object-environment interaction dynamics. Existing approaches address this challenge either through model-based methods, which often require accurate dynamics models, or through learning-based methods, which reduce this requirement but typically assume a fixed or predefined initial grasp. However, different geometrically stable grasps can lead to substantially different downstream manipulation performance. Therefore, we propose Grasp-TAGS, a task-aware grasp selection framework for goal-conditioned large-object rearrangement. We train a unified PPO-based reinforcement learning policy across multiple initial grasp configurations and distill the learned critic into a lightweight grasp utility network that ranks candidate grasps using only the candidate grasp configuration and goal information. At inference time, we select the grasp with the highest predicted downstream utility for the downstream policy to complete the task, before even making a contact. Experiments demonstrate that Grasp-TAGS improves rearrangement success over both fixed single-grasp policies and random grasp selection, achieving an average success rate of 89.84% compared with 79.87% for the best-performing single-grasp policies, an improvement of 9.97 percentage points. Grasp-TAGS also reduces final orientation errors across all evaluated objects. For more qualitative results, refer to the supplementary webpage: https://rpm-lab-umn.github.io/Grasp-TAGS-web-page/

</details>

---

### [[20_Research/Papers/大模型/When_Instruction_Files_Go_Stale_Documentation_Debt_and_Hidden_Cost_in_Coding_Agents|When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents]]

![[assets/2611.09802_first_page.png|800]]

- **arXiv**: [2611.09802](https://arxiv.org/abs/2611.09802)
- **PDF**: https://arxiv.org/pdf/2611.09802
- **详细分析**: [[20_Research/Papers/大模型/When_Instruction_Files_Go_Stale_Documentation_Debt_and_Hidden_Cost_in_Coding_Agents|When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents]]
- **作者**: Tural Mehtiyev, Biruk Tadesse, Lawrence Arkoh, Wesley Assunção
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based coding agents such as Claude Code are guided by repository instruction files (also called context files or agent configuration files) like AGENTS.md and CLAUDE.md, which are read in every agent session. As any documentation artifact, these files can fall behind the code and become stale (e.g., a test folder moves, but the file still points to the old one). In technical debt terms, such a stale instruction is documentation debt, and its interest is the cost it adds to every later agent session. Evaluations that check only task success can miss this cost, and the stale file can persist. In this study, we ask what leads agents to act on a stale instruction, how it affects their behavior and at what cost, and how they recover. We study three real-world stale instructions from active open-source repositories in depth, each a different kind of guidance: a test command, a code location, and a procedure for adding a component. Agents fix 22 maintenance tasks under three versions of each instruction (left stale, corrected to the current path, and removed), with the code and the task held fixed, and we analyze 732 trajectories of two models at the level of individual tool calls. We find that agents follow stale guidance when it is relevant to their tasks, sometimes even when correct information is available elsewhere. On the stale test command, Claude Sonnet 5.5 needed about two extra tool calls per run, a third more than with the corrected command; in the other cases, we could not detect a difference. Although agents generally recovered from the immediate failures, none repaired the underlying instruction file. Correcting the instructions eliminated operations on obsolete paths, while removing them prevented most. Our findings show that task success alone can hide the costs of documentation debt, highlighting the need to evaluate agent behavior beyond final outcomes.

</details>

---

### [[20_Research/Papers/大模型/Language_as_Trait,_Politeness_as_Strategy_Controlled_Tests_of_Linguistic_Effects_in_LLM_Social-Deduction_Agents|Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents]]

![[assets/2611.09768_first_page.png|800]]

- **arXiv**: [2611.09768](https://arxiv.org/abs/2611.09768)
- **PDF**: https://arxiv.org/pdf/2611.09768
- **详细分析**: [[20_Research/Papers/大模型/Language_as_Trait,_Politeness_as_Strategy_Controlled_Tests_of_Linguistic_Effects_in_LLM_Social-Deduction_Agents|Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents]]
- **作者**: Yuchen Li, Lisa Liu, Runqi Zou, Shuxuan Kuang, Qingquan Zhang, Julian Togelius
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic Effects in LLM Social-Deduction Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents coordinate through conversation, and the same message can be phrased in simpler or more complex language, bluntly or politely. We test whether such differences change how other agents judge and act, using the LURK Werewolf framework, which separates each utterance's speech-act predicate from its natural-language realization. We rewrite only the realization, check that the game content is preserved, and replay each game day from saved checkpoints against a re-sampled control. We vary linguistic range consistently across a speaker's messages and politeness strategy per utterance. Across 30 games and 4,335 replays, neither manipulation changes the trust other agents place in the speaker, and no effect on votes or night actions survives correction for multiple comparisons; the largest uncorrected effect is that shifting range away from a neutral paraphrase changes about 4 percentage points more of the other players' votes. In natural play, 88% of face-threatening speech is bald on-record regardless of role.

</details>

---

### [[20_Research/Papers/大模型/MemoryDojo_Benchmarking_Poisoning_Through_LLM_Agent_Memory|MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory]]

![[assets/2611.09721_figure.png|800]]

- **arXiv**: [2611.09721](https://arxiv.org/abs/2611.09721)
- **PDF**: https://arxiv.org/pdf/2611.09721
- **详细分析**: [[20_Research/Papers/大模型/MemoryDojo_Benchmarking_Poisoning_Through_LLM_Agent_Memory|MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory]]
- **作者**: David H. Yang, Blake Bullwinkel, Amanda Minnich, Mohammad Mohammadi Amiri, Giorgio Severi
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning across different memory architectures, we introduce MemoryDojo, a benchmark for tracing the lifecycle of poisoned information through agent memory and measuring its influence on subsequent agent behavior. MemoryDojo is easily extensible, consists of 155 multi-session long-horizon trajectories covering four domains, and supports five different memory systems. Through our evaluation, we find that all memory systems are susceptible to memory poisoning, with substantial variation in downstream effects. We further propose a memory-aware poison optimization process that increases the poisoning efficacy, highlighting differences between memory architectures. We hope that MemoryDojo will support research on understanding and mitigating agentic memory risks.

</details>

---

### [[20_Research/Papers/具身智能/SURE_Spatiotemporal_Uncertainty_Representation_for_Efficient_Vision-Language-Action_Learning|SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning]]

![[assets/2611.09684_figure.png|800]]

- **arXiv**: [2611.09684](https://arxiv.org/abs/2611.09684)
- **PDF**: https://arxiv.org/pdf/2611.09684
- **详细分析**: [[20_Research/Papers/具身智能/SURE_Spatiotemporal_Uncertainty_Representation_for_Efficient_Vision-Language-Action_Learning|SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning]]
- **作者**: Jingye Zhang, Choo Sin Wai, Dake Zhong, Zhifang Liu, Yuhong Zhang, Siyao Xiao, Guorui Song, Guocun Wang, Dongbin Zhang, Peng Jiao, Haoqian Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《SURE:Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies have become a promising paradigm for end-to-end robot control, but their effectiveness still depends heavily on large volumes of demonstration data. In manipulation tasks, this dependence is compounded by structured spatiotemporal uncertainty in the action space: multiple nearby actions or trajectories may successfully solve the same task, while semantically equivalent demonstrations often unfold at different speeds. Standard pointwise supervision treats each demonstrated action as an exact target, imposing an unnecessary learning burden under such uncertainty. We present SURE, a data-efficient VLA training framework that explicitly models both spatial and temporal uncertainty. SURE augments a VLA backbone with a lightweight transposed-convolutional probabilistic action decoder that captures spatial uncertainty through local correlations among neighboring action bins. It further introduces Soft-DTW alignment supervision to accommodate local timing variations between predicted and demonstrated action chunks. Together, these two components reduce sensitivity to demonstrator-specific poses and execution timing, enabling more data-efficient action learning. We evaluate SURE on LIBERO, RoboTwin 2.0, and real-world manipulation tasks. Even with only 10% of the demonstration data or 20% of the training steps, SURE achieves manipulation success rates that match or surpass baseline VLAs.

</details>

---

### [[20_Research/Papers/大模型/Steerable_Multi-Objective_Group-Relative_Preference_Optimization_with_Jointly_Trained_Low-Rank_Adapters|Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters]]

![[assets/2611.09634_first_page.png|800]]

- **arXiv**: [2611.09634](https://arxiv.org/abs/2611.09634)
- **PDF**: https://arxiv.org/pdf/2611.09634
- **详细分析**: [[20_Research/Papers/大模型/Steerable_Multi-Objective_Group-Relative_Preference_Optimization_with_Jointly_Trained_Low-Rank_Adapters|Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters]]
- **作者**: Constantinos Karouzos, Nikolaos Aletras
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector selects the adapter mixture that generates responses and weights the separately normalized rewards used to update the adapters. A single training run supports changing preferences at inference without further optimization. We experiment with four models on helpfulness and harmlessness and on solving math problems while following instructions. We also evaluate the two largest models on rewriting comments to preserve wording while reducing clues about personal attributes. On the first two tasks, LambdaMix achieves higher hypervolume than all evaluated conditioned and policy merging baselines across all four models. LambdaMix uses fewer training completions and stores fewer adapter parameters than a set of GRPO specialist policies. With architecture and initialization fixed, varying adapter mixtures and objective weights together gives wider score ranges and higher coverage than varying either alone.

</details>

---

### [[20_Research/Papers/强化学习/Encoding_Memory_in_World_Models_with_Test-Time_Model-Based_Reinforcement_Learning|Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning]]

![[assets/2611.09625_figure.png|800]]

- **arXiv**: [2611.09625](https://arxiv.org/abs/2611.09625)
- **PDF**: https://arxiv.org/pdf/2611.09625
- **详细分析**: [[20_Research/Papers/强化学习/Encoding_Memory_in_World_Models_with_Test-Time_Model-Based_Reinforcement_Learning|Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning]]
- **作者**: Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 3.02（加权：大模型 0.1，强化学习 0.96，世界模型 1.96）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL, TT-MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning (MBRL) approaches have demonstrated strong performance across diverse domains in recent years, learning accurate world models from agent trajectories. However, despite this progress, current approaches still struggle to surpass human performance on tasks that require long-term memory and planning. In this work, we address the problem of long-term memory in MBRL by moving beyond the commonly studied paradigm of architecture design. We introduce Test-Time Model-Based Reinforcement Learning (TT-MBRL), using gradient descent at test time to encode the memory of episode observations into world model parameters. This enables the agent to learn a distinct world model for each episode, improving memory capabilities compared to traditional approaches that solely rely on contextual memory. We first establish a proof of concept on a simplified two-dimensional variant of the Memory Maze environment, which we refer to as Memory Maze 2D, showing consistent improvements across different world model architectures. We then demonstrate the effectiveness of TT-MBRL in the 3D domain, achieving new state-of-the-art results on the Memory Maze benchmark. Finally, we show that TT-MBRL maintains strong performance on non-memory benchmarks such as DeepMind Control and Atari 100k.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Training_with_Knowledge_Traction_for_Video_Anomaly_Detection|Multimodal Training with Knowledge Traction for Video Anomaly Detection]]

![[assets/2611.09536_figure.png|800]]

- **arXiv**: [2611.09536](https://arxiv.org/abs/2611.09536)
- **PDF**: https://arxiv.org/pdf/2611.09536
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Training_with_Knowledge_Traction_for_Video_Anomaly_Detection|Multimodal Training with Knowledge Traction for Video Anomaly Detection]]
- **作者**: Xiao Tan
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Multimodal Training with Knowledge Traction for Video Anomaly Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CURL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The task of weakly supervised video anomaly detection is challenging. Existing approaches mainly model video frame features and determine whether anomalies are present based on their magnitudes. In this work, we propose a novel method that incorporates external knowledge into training to improve model performance, robustness, and generalization. We leverage textual prompts and a large language model (LLM) to establish prior information for the specific task, and employ dictionary learning to normalize and compress this information. Moreover, during experiments, we observed inconsistencies in the textual descriptions extracted from similar video frames by image caption models. To address this, we devise a method that leverages an LLM and auxiliary information to ensure consistency in the textual descriptions of similar frames within a video. Finally, we introduce a feature processing approach that incorporates prior knowledge and cross-modal attention mechanisms. This approach learns the relationships and characteristics among different modalities to construct more accurate and reliable feature representations, thereby improving the accuracy and stability of downstream tasks. Experimental results demonstrate that our method surpasses other state-of-the-art approaches.

</details>

---

### [[20_Research/Papers/强化学习/Not_All_Entropy_Is_Equal_Reward-Conditioned_Entropy_Allocation_in_Reinforcement_Learning_with_Verifiable_Rewards|Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards]]

![[assets/2611.09448_figure.png|800]]

- **arXiv**: [2611.09448](https://arxiv.org/abs/2611.09448)
- **PDF**: https://arxiv.org/pdf/2611.09448
- **详细分析**: [[20_Research/Papers/强化学习/Not_All_Entropy_Is_Equal_Reward-Conditioned_Entropy_Allocation_in_Reinforcement_Learning_with_Verifiable_Rewards|Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards]]
- **作者**: Song Yu, Li Li, Zhenming Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy entropy is widely used to diagnose exploration and collapse in reinforcement learning with verifiable rewards (RLVR), yet its magnitude does not consistently track reasoning performance across optimization objectives. We argue that this ambiguity arises because global token entropy conflates uncertainty in successful and failed trajectories, diversity across correct solution strategies, and variation among realizations of the same strategy. We introduce \textbf{Reward-Conditioned Entropy Allocation (RCEA)}, a hierarchical diagnostic framework that separates complete-trajectory entropy from average token entropy, conditions uncertainty on verifier outcome and process validity, measures correct-solution-mode retention, and connects these population-level quantities to local covariance-driven updates. In controlled sweeps over six RLVR objectives at two model scales, entropy trajectories do not induce a stable ordering of reasoning accuracy. Token entropy is higher for verifier-failed than successful trajectories under both broad separately aggregated estimates and a common-question paired analysis, whose confidence intervals exclude equality at 10 of 12 displayed endpoints. A local covariance approximation predicts the direction of adjacent-checkpoint entropy change in 95.5\% of nonfailed transitions; a reward-stratified endpoint proxy further shows that positive chosen-token covariance is more tail-concentrated within failed prefixes. Every reportable trained endpoint exhibits some contraction in independently audited correct-solution-mode breadth, whose positive association with large-\(k\) coverage remains exploratory. These results show that entropy collapse should be diagnosed by which uncertainty is removed, rather than by global entropy alone.

</details>

---

### [[20_Research/Papers/具身智能/DexDICE_Reconciling_Safety_and_Performance_via_Dual-Expert_Offline_Imitation_Learning|DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning]]

![[assets/2611.09433_figure.png|800]]

- **arXiv**: [2611.09433](https://arxiv.org/abs/2611.09433)
- **PDF**: https://arxiv.org/pdf/2611.09433
- **详细分析**: [[20_Research/Papers/具身智能/DexDICE_Reconciling_Safety_and_Performance_via_Dual-Expert_Offline_Imitation_Learning|DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning]]
- **作者**: Seokin Seo, Sung Kuk Shyn, Minji Seo, Yisoo Lee, Jongmin Lee, Hongseok Yang, Kee-Eung Kim
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 0.6（加权：具身智能 0.3，大模型 0.1，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《DexDICE: Reconciling Safety and Performance via Dual-Expert Offline Imitation Learning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DSRL, OSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ensuring high returns while providing strong safety guarantees in offline imitation learning (IL) is a fundamental challenge: existing approaches either rely on explicitly specified cost functions, which are difficult to design for complex real-world safety constraints, or require expert demonstrations that are both safe and high-performing, which are often too costly to collect. We introduce dual-expert imitation learning, which leverages two complementary data sources: (i) safety-compliant demonstrations that faithfully follow safety guidelines but may be suboptimal, and (ii) performance-oriented demonstrations that achieve high returns but may violate safety guidelines. To address this problem, we propose DexDICE (Dual-expert offline imitation learning via stationary DIstribution Correction Estimation). Instead of conventional distribution constraints, DexDICE combines DICE-style offline learning with safe support constraints, enabling agents to exploit high-return behaviors while remaining within safety-compliant regions. We prove that the ideal solution satisfying this constraint exactly has zero unsafe-region visitation with high probability. We evaluate DexDICE on a re-curated DSRL benchmark and validate it on a real-world mobile-robot navigation task trained directly from human teleoperation demonstrations, where it substantially outperforms baselines and remains robust to data scarcity and quality degradation.

</details>

---

### [[20_Research/Papers/大模型/ROAM_Retrieval-Augmented_Optimization_for_Feasible_Multi-Day_Itinerary_Planning|ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning]]

![[assets/2611.09407_first_page.png|800]]

- **arXiv**: [2611.09407](https://arxiv.org/abs/2611.09407)
- **PDF**: https://arxiv.org/pdf/2611.09407
- **详细分析**: [[20_Research/Papers/大模型/ROAM_Retrieval-Augmented_Optimization_for_Feasible_Multi-Day_Itinerary_Planning|ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning]]
- **作者**: Ye Zihao, Lin Xiaoheng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) can draft plausible travel itineraries, but the plans they produce are frequently infeasible: attractions are grouped into days without regard for geography, opening hours are ignored, and a single generation pass cannot reliably organize a multi-day trip. We present ROAM, a retrieval-augmented agentic framework for spontaneous multi-day itinerary planning that couples semantic preference retrieval with explicit spatiotemporal optimization. ROAM embeds the natural-language request, retrieves a compact candidate set from a curated point-of-interest (POI) database, partitions candidates into day groups through maximal-clique analysis and K-means, orders each day with a quality-biased simulated-annealing TSP solver, and repairs hard opening-hour violations with greedy exchange. A spatiotemporal retrieval layer injects weather forecasts, real road distances and POI operating hours into the prompt, after which the LLM renders a structured, map-ready itinerary; an interactive ReAct-style replanning agent then supports natural-language edits while re-checking feasibility. Across four Chinese cities and 510 POIs, ROAM produces 27.5 POIs per three-day plan versus 19.3 for a bare LLM and 17.0 for a retrieval-only baseline (+42% and +62%), while reducing route dispersion from 2,101 to 677 (3.1x). Ablations show that spatial optimization is the dominant driver of route efficiency and that hard time-window repair prevents roughly 30% of attractions from violating operating hours.

</details>

---

### [[20_Research/Papers/强化学习/PhyCAD_Physics-Aware_Text-to-CAD_Generation_via_Hierarchical_Reinforcement_Learning|PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning]]

![[assets/2611.09401_figure.png|800]]

- **arXiv**: [2611.09401](https://arxiv.org/abs/2611.09401)
- **PDF**: https://arxiv.org/pdf/2611.09401
- **详细分析**: [[20_Research/Papers/强化学习/PhyCAD_Physics-Aware_Text-to-CAD_Generation_via_Hierarchical_Reinforcement_Learning|PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning]]
- **作者**: Yuxin Cui, Weijie Zheng, Zhengyang Li, Han Wang, Wenjie Feng, Qiyu Kang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-driven computer-aided design (CAD) generation enables the creation of editable parametric models from text, yet geometric correctness alone does not ensure physical feasibility. We present PhyCAD, a framework for physics-aware Text-to-CAD generation that trains language models to produce executable CadQuery programs under geometric and physical constraints. To support this setting, we construct a Text-to-CAD dataset that links parametric CAD models with geometric specifications, loading conditions, and physical constraints. We further develop an automated CAD--CAE verifier that combines program execution, geometric checks, and finite element analysis to provide feedback for model training. A key learning challenge is to prioritize joint satisfaction of geometric and physical constraints while retaining informative feedback on partial progress. A flat aggregation of heterogeneous rewards can obscure this priority, allowing improvements in individual criteria to compensate for unmet design requirements. We therefore introduce a Hierarchical Balanced Advantage for Group Relative Policy Optimization, grouping candidates into levels according to their verification status and combining between-level progress with objective-wise peer ranking within each level. This formulation preserves cross-level priority in the training signal while providing fine-grained feedback for satisfying constraints and improving feasible designs. Experiments across multiple language models show that PhyCAD consistently improves joint geometric and physical constraint satisfaction. These results demonstrate the value of verifiable engineering feedback for advancing language-driven CAD generation beyond geometric reconstruction toward physics-aware design.

</details>

---

### [[20_Research/Papers/具身智能/Can_LLMs_Debug_Robots_by_Editing_Their_Weights|Can LLMs Debug Robots by Editing Their Weights?]]

![[assets/2611.09376_figure.png|800]]

- **arXiv**: [2611.09376](https://arxiv.org/abs/2611.09376)
- **PDF**: https://arxiv.org/pdf/2611.09376
- **详细分析**: [[20_Research/Papers/具身智能/Can_LLMs_Debug_Robots_by_Editing_Their_Weights|Can LLMs Debug Robots by Editing Their Weights?]]
- **作者**: Jusheng Zhang, Keze Wang, Liang Lin
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Can LLMs Debug Robots by Editing Their Weights?》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A language model can repair a robot policy's lexical instruction grounding by editing just 65 token-embedding rows. We bring weight-space programming to robot foundation policies: GPT-6 Astra reads weights and uses a CPU workspace and budgeted simulator feedback, without gradient updates or new demonstrations. Three independent sessions on $π_{0.5}$ all improve success on 765 held-out paraphrases; the best raises success from 86.3\% to 92.0\% (48 repairs, four regressions; exact paired $p=1.31\times10^{-10}$). Among the 335 instructions containing edited tokens, success rises from 74.3\% to 87.5\%; the other 430 episodes have zero outcome changes. Matched random-direction edits do not help. Full replacement using the editor's own lexicon explains much of the gain but produces more regressions; its direct difference from the editor is not significant at 0.05. Across 13 further robot sessions, the editor declines 12 candidates; the sole retained edit does not show a significant held-out gain. Separately, benchmark metadata lowers FastWAM success from 70.0\% to 48.6\%, while the evaluated VLA's aggregate rate is unchanged. The evidence supports precise lexical repair, not general acquisition of missing robot capabilities.

</details>

---

### [[20_Research/Papers/具身智能/HiMEM_Hippocampus-Inspired_Memory_Consolidation,_Pruning,_and_Composition_for_Vision-Language-Action_Models_in_3D_Scenes|HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes]]

![[assets/2611.09355_figure.png|800]]

- **arXiv**: [2611.09355](https://arxiv.org/abs/2611.09355)
- **PDF**: https://arxiv.org/pdf/2611.09355
- **详细分析**: [[20_Research/Papers/具身智能/HiMEM_Hippocampus-Inspired_Memory_Consolidation,_Pruning,_and_Composition_for_Vision-Language-Action_Models_in_3D_Scenes|HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes]]
- **作者**: Boran Zhao, Yanbin Hu, Jun Ye, Zhenxian Hu, Yuxin Zhai, Jin Cui, Pengju Ren
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.5，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MAP-VLA, MemoryVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory plays a crucial role in long-horizon task execution and cross-task generalization for Vision-Language-Action (VLA) models operating in complex 3D scenes. However, existing VLA memory mechanisms suffer from memory noise, particularly in complex 3D scenes, as stored episodic memories contain extensive redundant details about scene layouts, object configurations, and robot-specific states, which obscure generalizable manipulation principles and hinder cross-task transfer. To address this challenge, we first introduce a hippocampus-inspired memory consolidation mechanism that synthesizes extensive episodic experiences into a compact set of essential semantic memories, enabling VLA models to derive generalizable principles from practical experience. Second, we propose an episodic memory pruning mechanism that removes redundant episodic memories whose contents are captured by consolidated semantic memories, thereby increasing effective memory capacity and improving long-horizon task execution. Finally, to handle complex task scenarios, we develop a flexible memory composition mechanism that jointly leverages multiple episodic and semantic memories to enhance cross-scenario generalization. Experiments on LIBERO, LIBERO-Plus demonstrate the effectiveness of HiMEM across different VLA backbones, improving the average success rate of pi_0 from 91.88% to 98.20% on LIBERO.

</details>

---

### [[20_Research/Papers/强化学习/RPEG_Training_Reasoning_Language_Models_Scalably_and_Cost-Effectively|RPEG: Training Reasoning Language Models Scalably and Cost-Effectively]]

![[assets/2611.09207_figure.png|800]]

- **arXiv**: [2611.09207](https://arxiv.org/abs/2611.09207)
- **PDF**: https://arxiv.org/pdf/2611.09207
- **详细分析**: [[20_Research/Papers/强化学习/RPEG_Training_Reasoning_Language_Models_Scalably_and_Cost-Effectively|RPEG: Training Reasoning Language Models Scalably and Cost-Effectively]]
- **作者**: Maciej Besta, Leonard Schmidt, Pierre Pang, Patrik Okanovic, Robert Gerstenberger, Torsten Hoefler
- **cs 子类**: cs.AI, cs.CL, cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《RPEG: Training Reasoning Language Models Scalably and Cost-Effectively》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is now central to training Reasoning Language Models (RLMs), but RLM pipelines are difficult to scale and costly to run because each RL step couples multiple large models, heterogeneous stages, cross-step state, and complex asynchronous dependencies. Existing systems typically optimize only parts of this design space. We address this complexity by jointly optimizing the pipeline structure as well as its execution using a novel data-centric graph intermediate representation called RLM Pipeline Execution Graph (RPEG). RPEG exposes structural choices such as bounded asynchrony and actor-critic sharing together with execution optimizations such as stage fusion, fine-grained scheduling, and multi-dimensional model parallelism. It is coupled with a comprehensive analytical performance model for RLM training, jointly capturing compute, communication, memory, and hierarchical rack-, node-, and GPU-level effects. Across systems with up to 256 GH200 GPUs, our distributed runtime engine implementing RPEG improves performance by up to 2x over ReaL and reduces step latency by up to 2.48x over verl, while increasing hardware utilization by up to 30%. Overall, RPEG provides a graph-driven foundation for next-generation training pipelines for frontier reasoning LLMs.

</details>

---

### [[20_Research/Papers/具身智能/Safe_Reinforcement_Learning_via_Probabilistic_Option_Shielding|Safe Reinforcement Learning via Probabilistic Option Shielding]]

![[assets/2611.09197_figure.png|800]]

- **arXiv**: [2611.09197](https://arxiv.org/abs/2611.09197)
- **PDF**: https://arxiv.org/pdf/2611.09197
- **详细分析**: [[20_Research/Papers/具身智能/Safe_Reinforcement_Learning_via_Probabilistic_Option_Shielding|Safe Reinforcement Learning via Probabilistic Option Shielding]]
- **作者**: Gian Luca Ascari, Isidoro Tamassia, Ying Jiao, Luc De Raedt, Giuseppe Marra
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Safe Reinforcement Learning via Probabilistic Option Shielding》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HRL, Safe-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shielding is a safe reinforcement learning technique that provides safety guarantees while learning, by blocking unsafe actions. Traditional shielding relies on a complete model of the environment to provide long-term guarantees. Probabilistic logic shielding (PLS) lifts the requirement of having such model, but only considers safety in the short term, typically looking only one or few steps ahead. We propose Probabilistic Option Shielding (POS), which extends PLS to the option level, recovering long-horizon safety without reintroducing the need for a complete environment model. POS learns a model-free critic directly from one-step PLS signals, to estimate the probability that an entire option will complete safely under uncertainty. We evaluate POS on safe navigation tasks in the LogiCity environment, and show that it achieves considerably safer training while matching the task performance of standard step-level PLS and other safety related reinforcement learning baselines.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_Consensus_and_Corpus-Adaptive_Topic_Modeling_for_Classifying_and_Mapping_Patent_Innovation|Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation]]

![[assets/2611.09194_first_page.png|800]]

- **arXiv**: [2611.09194](https://arxiv.org/abs/2611.09194)
- **PDF**: https://arxiv.org/pdf/2611.09194
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_Consensus_and_Corpus-Adaptive_Topic_Modeling_for_Classifying_and_Mapping_Patent_Innovation|Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation]]
- **作者**: Sercan Ozcan, Enes Ozgozler, C. Okan Sakar
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《Large Language Model Consensus and Corpus-Adaptive Topic Modeling for Classifying and Mapping Patent Innovation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Patent analytics increasingly relies on transformer representations and large language models (LLMs), yet linking conceptual classification, topic formation and interpretation requires explicit decisions about model roles and the evidence retained at each stage. In this design-oriented study, we propose and demonstrate a patent analytics pipeline that links these tasks and keeps each decision open to audit. Three LLMs separately classify each patent by novelty (radical or incremental) and innovation type (product, process, service). Radical and innovation-type labels each require two supporting votes, with Incremental used as the fallback novelty label. Topics are discovered by clustering PatentSBERTa embeddings, with parameter ranges scaled to corpus size. A patent-specific stopword list is applied only when topics are represented with class-based term frequency--inverse document frequency (c-TF-IDF), and a second embedding model supports inter-topic similarity, hierarchical refinement and visualization. An LLM then labels each topic from its ranked keywords and representative patents. We demonstrate the pipeline on 30,964 public-sector-related patents retrieved from Lens.org. Across five category corpora ranging from 591 to 29,215 patents, the pipeline produced 74 category-specific topic instances with a macro-average document coverage of 98.1% and topic diversity of 0.900--1.000, and fewer than 1% of classification outputs returned UNKNOWN. Because every model vote and the evidence behind each topic label are retained, analysts can audit and revise the outputs. The demonstration establishes the feasibility and traceability of the pipeline; testing its labels against expert coding and benchmarking it against alternative pipelines are identified as the next steps. The pipeline offers a reusable basis for LLM-assisted patent analysis in technology intelligence.

</details>

---

### [[20_Research/Papers/强化学习/CARGO_Causal_Attribution_and_Responsibility-Guided_Preventive_Safe_Multi-Agent_Reinforcement_Learning_for_Cooperative_Driving|CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving]]

![[assets/2611.09139_figure.png|800]]

- **arXiv**: [2611.09139](https://arxiv.org/abs/2611.09139)
- **PDF**: https://arxiv.org/pdf/2611.09139
- **详细分析**: [[20_Research/Papers/强化学习/CARGO_Causal_Attribution_and_Responsibility-Guided_Preventive_Safe_Multi-Agent_Reinforcement_Learning_for_Cooperative_Driving|CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving]]
- **作者**: Jingjia Teng, Yang Li, Wenjie Huang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior uncertainty propagated into interaction-edge selection. Complementary attribution mechanisms couple signed influence with marginal team utility for cooperative reward shaping and assign responsibility from positive excess tail risk relative to a safe reference policy. Conditional diffusion generates future responses for action-dependent risk estimation. Responsibility-guided preventive optimization calibrates agent-specific risk-reduction requirements to local capacity within a policy trust region, using reserved safety margins, adaptive requirement scaling, and joint feasibility verification. Theoretical analysis establishes risk monotonicity and sufficient local conditions for non-decreasing environmental return under explicit assumptions. Experiments in highway-env across three traffic densities, together with controlled graph-recovery and attribution studies, support the effectiveness of the framework. Under high-density traffic, CARGO increases the success rate by 66.04\% and reduces the crash rate by 56.23\% relative to the best evaluated baseline for each metric.

</details>

---

### [[20_Research/Papers/具身智能/AlienBench_A_Benchmark_of_Structural_Novelty_in_Language_Model_Outputs|AlienBench: A Benchmark of Structural Novelty in Language Model Outputs]]

![[assets/2611.09094_first_page.png|800]]

- **arXiv**: [2611.09094](https://arxiv.org/abs/2611.09094)
- **PDF**: https://arxiv.org/pdf/2611.09094
- **详细分析**: [[20_Research/Papers/具身智能/AlienBench_A_Benchmark_of_Structural_Novelty_in_Language_Model_Outputs|AlienBench: A Benchmark of Structural Novelty in Language Model Outputs]]
- **作者**: Jonas Oppenlaender, Johanna M. Silvennoinen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.85（加权：具身智能 0.3，大模型 0.55）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《AlienBench: A Benchmark of Structural Novelty in Language Model Outputs》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AlienBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used for creative tasks such as writing, design, and idea generation. For these uses, it matters whether a model's ideas depart from familiar examples or stay close to them. Novelty is one standard measure of creativity, and current creativity evaluations ask human experts or LLM judges to rate how novel an output is. However, these ratings have no fixed reference for what counts as novel (or, in other terms, departure from the familiar). Measuring this departure requires a task with known familiar defaults. The structured imagination task from cognitive psychology is such a task. In this creativity test, people imagine a creature from another planet. The departure from features of Earth animals, such as bilateral symmetry and legs as mode of locomotion, is used as measure of creativity. We introduce AlienBench, a benchmark that adapts the structured imagination task to language models. Models describe alien creatures, and a panel of three LLM judges extracts ten biological features from the description and labels them as either Earth-typical or a departure. The sum of feature departures is the score of a description, from 0 to 10. Each model describes alien creatures under six prompt conditions that vary the framing of the task and the planetary environment. Each model generates 30 descriptions per condition (180 in total), and its overall score is the mean across these descriptions. We evaluate 10 language models, from frontier to open-weight models. Overall scores range from 3.28 (GPT-6 Luna) to 6.55 (Ministral 3 14B). Interestingly, open-weight models score higher than proprietary models in this task (5.40 vs. 4.58). Under the baseline prompt, the models depart from Earth defaults more often on average than 100 human participants on every feature. We release all prompts, generations, judge outputs, and scores.

</details>

---

### [[20_Research/Papers/大模型/When_Routine_Operations_Break_Architectural_Pattern_Relationships_in_LLM_Agent_Harnesses|When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses]]

![[assets/2611.09088_first_page.png|800]]

- **arXiv**: [2611.09088](https://arxiv.org/abs/2611.09088)
- **PDF**: https://arxiv.org/pdf/2611.09088
- **详细分析**: [[20_Research/Papers/大模型/When_Routine_Operations_Break_Architectural_Pattern_Relationships_in_LLM_Agent_Harnesses|When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses]]
- **作者**: Boming Xia, Qinghua Lu, Dino Sejdinovic, Liming Zhu
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agent harnesses distribute tool mediation, state management and safety guardrails across native services, independently written plugins and configuration. Routine operations can change the runtime order or retained state that architectural pattern relationships require, without any code change. We study five relationships associated with the Guardrail Enforcement Point, Autonomy Controller and Blackboard patterns across five released harnesses, analysing a main sample of fourteen independently written plugins. Using PatternOps, our assessment procedure, we trace requirements from pattern descriptions, provider documentation and deployment profiles to the providers that realise them and the records that decide them. We then compare alternative allocations under supported operations. Such operations broke relationships silently: after a plugin was reapplied or an allow rule saved, policy stopped evaluating edits while every plugin stayed active, and a prohibited edit executed. Which alternatives qualified depended on the requirement. Allocations that kept the required order, or kept or rebuilt the needed state, held on their tested paths and operation sequences, while others prevented prohibited effects but missed edits rejected elsewhere. In these harnesses, a pattern relationship is a property of the running system and its history, so architects should evaluate it against the decision paths, state lifetimes and operation sequences their deployments use.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_Deployment_on_Resource-Constrained_Edge_Devices_A_Practitioners_Survey|Large Language Model Deployment on Resource-Constrained Edge Devices: A Practitioners Survey]]

![[assets/2611.09075_figure.png|800]]

- **arXiv**: [2611.09075](https://arxiv.org/abs/2611.09075)
- **PDF**: https://arxiv.org/pdf/2611.09075
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_Deployment_on_Resource-Constrained_Edge_Devices_A_Practitioners_Survey|Large Language Model Deployment on Resource-Constrained Edge Devices: A Practitioners Survey]]
- **作者**: Rahul Maliakkal, Yashasvi Makin, Plawan Rath, Rohit Jain, Ankur Sadhoo
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Large Language Model Deployment on Resource-Constrained Edge Devices: A Practitioners Survey》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have transformed many areas of artificial intelligence (AI), but their substantial resource requirements limit their deployment on mobile and edge devices. Although LLMs have demonstrated impressive capabilities in various applications, the next challenge is deploying these models on resource-limited edge devices. Recent innovations in software optimizations and specialized hardware have made it feasible to deploy LLMs on edge devices. Edge deployment offers benefits including local data processing, cost savings, reduced latency, and personalized responses. This paper reviews the latest techniques that make the deployment of LLMs on edge devices feasible.

</details>

---

### [[20_Research/Papers/具身智能/ToolDex_An_Ego-Exo_Human_Demonstration_Dataset_for_Creative_Physical_Tool_Use|ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use]]

![[assets/2611.09036_figure.png|800]]

- **arXiv**: [2611.09036](https://arxiv.org/abs/2611.09036)
- **PDF**: https://arxiv.org/pdf/2611.09036
- **详细分析**: [[20_Research/Papers/具身智能/ToolDex_An_Ego-Exo_Human_Demonstration_Dataset_for_Creative_Physical_Tool_Use|ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use]]
- **作者**: Mohamed Elmoghany, Kehan Li, Ruoqu Chen, Tarun Chiruvolu, Shutong Zhang, Ryan Wang, Stephen Tian, Yaru Niu, Michelle Guo, Ding Zhao, Weiyu Liu, Mengdi Xu...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PhysToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence. It requires agents to reason about object affordances, physical constraints, and manipulation strategies, especially when standard tools are unavailable. However, progress in this area is limited by the lack of real-world datasets that capture human tool-use behavior with sufficient scale, fidelity, and diversity. Existing benchmarks are often simulation-based, focus on simplified interactions, or lack detailed observations and annotations. We introduce ToolDex, a large-scale egocentric-exocentric (ego-exo) human demonstration dataset for creative physical tool use. ToolDex captures scenarios in which humans select, adapt, and repurpose available objects as tools. Using synchronized egocentric cameras and eight exocentric cameras, the dataset provides high-fidelity multi-view observations and rich annotations for hands, tools, target objects, and their deformable interactions. Beyond data collection, we establish a benchmark suite characterizing three core capabilities: physical tool-use reasoning, sparse-view 3D and 4D reconstruction, and robot policy learning. ToolDex provides a foundation for studying human tool-use behavior and developing embodied agents that can adaptively use tools in complex real-world environments. Dataset visualizations and benchmarking results are available at https://tooluse-dataset.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/A_Controlled_Study_of_Models,_Skills,_Feedback,_and_Curriculum_in_Agentic_Robotics|A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics]]

![[assets/2611.09030_figure.png|800]]

- **arXiv**: [2611.09030](https://arxiv.org/abs/2611.09030)
- **PDF**: https://arxiv.org/pdf/2611.09030
- **详细分析**: [[20_Research/Papers/强化学习/A_Controlled_Study_of_Models,_Skills,_Feedback,_and_Curriculum_in_Agentic_Robotics|A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics]]
- **作者**: Kaiyuan Chen, Xinyue Zhu, Shuangyu Xie, Uksang Yoo, Thi Thu Phuong Luong, Marcus Gualtieri, Christian Juette, Liu Ren, Spencer Huang, Ken Goldberg
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic robotics asks coding agents to implement and iteratively improve robot policies from simulated and real-world physical interactions. We study the self-learning loop of agentic robotics through a controlled simulation study spanning nine manipulation tasks, 631 different experiment configurations, and 28K coding agent rollouts, systematically varying model capability, skill priors, feedback structure, and curriculum. The experiment data suggests that the bottleneck is often not the access to sufficient information, but interpreting it into the right policy update. Across these factors, a successful self-learning loop depends on how effectively agents attribute failures, reason task-relevant spatial and geometric structure, and selectively restructure code to improve policies.

</details>

---

### [[20_Research/Papers/大模型/Seeing_vs._Counting_Complexity_Twins_Show_Where_Multimodal_LLMs_Fail_on_Diagrams|Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams]]

![[assets/2611.08998_figure.png|800]]

- **arXiv**: [2611.08998](https://arxiv.org/abs/2611.08998)
- **PDF**: https://arxiv.org/pdf/2611.08998
- **详细分析**: [[20_Research/Papers/大模型/Seeing_vs._Counting_Complexity_Twins_Show_Where_Multimodal_LLMs_Fail_on_Diagrams|Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams]]
- **作者**: Yin Liu
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AlgoPuzzleVQA, CountBench, CountQA, GraphQA, IsoBench, NPHardEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a multimodal LLM miscounts in a diagram, does it fail at seeing or at counting? Existing visual graph and puzzle benchmarks vary visual density and algorithmic hardness together, confounding the two. We pair counting questions about the same drawing that sit in different counting-complexity classes, such as its spanning trees (a determinant) and its simple paths (#P-complete), and use a transcription probe and a text-only control to separate reading from computing. We test Gemini, Gemma and Qwen3-VL models; for the Gemini models, the answer depends on how the model computes. In chain of thought, most of them read small drawings correctly and then fail at counting, at a rate set far more by the size of the answer than by its complexity class (for the primary model, the odds of an exact answer fall 2.38-fold per decade of the answer). Given code and an exact transcription, the primary model counts correctly even on 10x10 grids, and reading becomes the bottleneck: a single view misses horizontal edges, and a second reading of a rotated copy with crop checks reads 86/96 large grids exactly, against 57/96 when the upright reading is simply repeated.

</details>

---

### [[20_Research/Papers/大模型/Phantom_Consensus_Measuring_Social_Reasoning_in_Multi-Agent_LLM_Decision-Making|Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making]]

![[assets/2611.08971_figure.jpg|800]]

- **arXiv**: [2611.08971](https://arxiv.org/abs/2611.08971)
- **PDF**: https://arxiv.org/pdf/2611.08971
- **详细分析**: [[20_Research/Papers/大模型/Phantom_Consensus_Measuring_Social_Reasoning_in_Multi-Agent_LLM_Decision-Making|Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making]]
- **作者**: Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, Tirthankar Dasgupta
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, MultiAgentBench, PHANTOM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately judged, even when the group's recorded private judgments do not support the apparent consensus. We call this failure phantom consensus and study it as a pluralistic-ignorance-style pattern in controlled LLM collectives. To measure this phenomenon, we introduce PHANTOM-Bench, a benchmark that separates isolated private judgments, public decisions after ambiguous social signals, elicited estimates of the group's private judgment, transparency-based recovery, and controls for neutral public text and explicit vote-following. Across nine closed- and open-weight models, ambiguous public signals consistently degrade decision quality and can turn correct private group judgments into incorrect public collective outcomes. Public accuracy drops by as much as 47.8 percentage points, and collective rationality failures reach 47.3% in the most susceptible setting. We observe substantial errors in reported group-private beliefs alongside public-stage failures, while control conditions reveal model-dependent differences in susceptibility to ambiguous and explicit peer signals. Revealing the agents' recorded private decisions repairs many failures without revealing the gold label, although recovery varies across models. Our results show that evaluating multi-agent LLM systems requires measuring not only final agreement, but whether that agreement reflects independently measured private judgments or an apparent consensus.

</details>

---

### [[20_Research/Papers/机器人/Flex-RSI_Benchmarking_Recursive_Self-Improvement_of_Frontier_Agents|Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents]]

![[assets/2611.08946_figure.png|800]]

- **arXiv**: [2611.08946](https://arxiv.org/abs/2611.08946)
- **PDF**: https://arxiv.org/pdf/2611.08946
- **详细分析**: [[20_Research/Papers/机器人/Flex-RSI_Benchmarking_Recursive_Self-Improvement_of_Frontier_Agents|Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents]]
- **作者**: Jingdong Zhang, Jionghao Wang, Zhengming Yu, Yancheng Cai, Wei Chow, Chris Choy, Zhiyang Dou, Hang Hua, Jiachen Li, Zhixuan Liu, Chen Wang, Songlin Wei...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.5，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedCLBench, EvoAgentBench, EvolveTool-Bench, PAST-Bench, PaperBench, RE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier language models are increasingly deployed as agents, and how well an agent performs depends not only on its model but also on its harness: the prompts, tools, memory, and control loop through which the model acts. When an agent is applied to a new problem, a natural question is whether it can use the feedback of the task to improve the way it works, and not merely its answer. Most existing benchmarks keep the agent's harness fixed and score the solution it produces, or target large-scale model training. We introduce Flex-RSI, a benchmark for the recursive self-improvement of agents on vision and robotics tasks under a fixed budget. In each round, an executor improves the task solution, which is kept only if it scores higher on held-out validation data, and an improver then revises the harness, including the executor and itself. Every run starts from the same general-purpose harness, and the final solution is scored on hidden test data. Evaluating closed-source and open-weight models on tasks spanning perception, reasoning, robot action, 3D reconstruction, visual creation, and infrastructure, we find that self-improvement helps most when the agent builds its own solution, that feedback recording only success or failure holds back open-weight models, and that open-weight models fall furthest behind where outputs must pass strict checks of physical stability or exact correctness. Paired runs further show that editing the harness itself contributes to the gains.

</details>

---

### [[20_Research/Papers/强化学习/Ordered_Policy_Optimization|Ordered Policy Optimization]]

![[assets/2611.08936_figure.png|800]]

- **arXiv**: [2611.08936](https://arxiv.org/abs/2611.08936)
- **PDF**: https://arxiv.org/pdf/2611.08936
- **详细分析**: [[20_Research/Papers/强化学习/Ordered_Policy_Optimization|Ordered Policy Optimization]]
- **作者**: Dongkyu Derek Cho, Pan Xu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Ordered Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proximal Policy Optimization (PPO) stabilizes policy updates by clipping the importance ratio between the new policy and the data-collecting policy. The standard rule uses one fixed clipping range for all samples. While this choice offers simplicity and effectiveness, it fails to distinguish statistically harmful extreme ratio values from large, yet tolerable changes. We study how to adapt the clipping radius to the reliability of the induced importance ratio distribution. Our case study demonstrates that reliable updates require controlling these extreme ratios, rather than merely verifying that individual ratios fall within a fixed interval. Motivated by this observation, we propose Ordered Policy Optimization (\textsc{OPO}). In each minibatch, \textsc{OPO} sorts the importance ratios, selects the extreme ratios that potentially have the largest effect on the update, and assigns them adaptive sample-wise radii instead of using the fixed clipping radius. These radii are derived from a prescribed tail profile, which specifies desired target values for the selected extreme ratios. The resulting objective remains first-order and requires only minibatch sorting and a modified policy loss. Experiments conducted on MuJoCo and Atari benchmarks demonstrate that this simple modification achieves strong performance relative to established baselines.

</details>

---

### [[20_Research/Papers/具身智能/HomeLoop_A_Simulation_Framework_and_Benchmark_for_Robot-IoT_Coordination_in_Everyday_Domestic_Assistance_and_Safety|HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety]]

![[assets/2611.08914_figure.jpg|800]]

- **arXiv**: [2611.08914](https://arxiv.org/abs/2611.08914)
- **PDF**: https://arxiv.org/pdf/2611.08914
- **详细分析**: [[20_Research/Papers/具身智能/HomeLoop_A_Simulation_Framework_and_Benchmark_for_Robot-IoT_Coordination_in_Everyday_Domestic_Assistance_and_Safety|HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety]]
- **作者**: Ramy ElMallah, Marc Bishara, Hyegang Kim, Yuxi Zhang, Chongyu Zhu, Chi-Guhn Lee
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.6，大模型 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HomeBench, HomeSafeBench, IS-Bench, PersonalHomeBench, SMH-Bench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress in embodied robotics is bringing robots closer to deployment in homes, as vision-language models (VLMs) are demonstrating significant advances in reasoning, making VLM-driven robots promising home assistant agents. These agents will often be introduced into homes that already have cameras, Internet of Things (IoT) devices, and residents with wearables. To fulfill their potential, they need to integrate with existing smart infrastructure and reason through ambiguous scenarios: a smoke alarm may come from a pan about to ignite, a pan already on fire, a resident cooking or a faulty sensor, and each calls for a different response. To that end, we introduce HomeLoop, a simulation framework and benchmark built on Isaac Sim that combines robot bodies, networked devices and wearables, simulated residents and visitors, faulty sensors, and hazards that evolve over time. Our benchmark is composed of 20 tasks across five families grounded in real-world household hazards and needs, and designed so that the same alert can have different causes. A runtime monitor scores each episode with temporal-logic checks on the final outcome and the actions along the way, and every action carries a predefined cost. We evaluate six open-weight and proprietary VLMs. The best achieves a family-balanced score of 61.9%, and across models we see a pattern of over-reaction: failed episodes involving prohibited interventions outnumber those involving missed required interventions by more than two to one, with models often shutting off the stove before investigating the alarm's cause. HomeLoop is an extensible foundation intended for use in research on robot-IoT coordination, long-term memory, proactive assistance, and privacy-safety trade-offs. HomeLoop will be released with 2,100 home layouts that can be automatically furnished in diverse configurations, five robot bodies and 20 networked device types.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Scheduling_Pipeline_for_Multi-Instance_Asynchronous_Reinforcement_Learning|Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning]]

![[assets/2611.08864_figure.png|800]]

- **arXiv**: [2611.08864](https://arxiv.org/abs/2611.08864)
- **PDF**: https://arxiv.org/pdf/2611.08864
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Scheduling_Pipeline_for_Multi-Instance_Asynchronous_Reinforcement_Learning|Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning]]
- **作者**: Salah Chikhi, Luis Zuin, Entong Li, Zeng Li
- **cs 子类**: cs.AI, cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Adaptive Scheduling Pipeline for Multi-Instance Asynchronous Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MindSpeed-RL, StreamRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present the Adaptive Scheduling Pipeline (ASP), an offline rollout scheduler for multi-instance asynchronous reinforcement learning (RL) of large language models (LLMs). ASP jointly reduces three sources of rollout underutilization - padding bubbles from intra-minibatch length heterogeneity, skewness bubbles from long-tail outputs, and sorting bubbles from fluctuations in training-queue occupancy induced by length-sorted dispatch - through a single offline preprocessing pass. This enables efficient multi-instance rollout that overcomes the early scaling plateau of single-instance inference while smoothing the arrival of generated samples at the trainer. We integrate the scheduler into an asynchronous architecture that decouples rollout from training while keeping policy lag observable and bounded. Complete ASP improves end-to-end throughput by up to 3.22 times and reduces iteration time by up to 76.8% relative to MindSpeed-RL, while reducing iteration time by up to 62.5% relative to verl. Within ASP, scheduling reduces mean iteration time by 10.9%. ASP also scales more robustly with additional generation resources than these baselines and shows no visible convergence degradation in the measured bounded-lag regime. ASP has since been used in an internal telecom-domain RL post-training workflow, reducing the reported training period from more than three months to about two months and producing a domain-enhanced model for knowledge answering and tool calling.

</details>

---

### [[20_Research/Papers/大模型/Mind_the_Divergence_Divergence-Guided_Reliability-Aware_Fusion_and_Adaptive_LLM_Prompting_for_Conversational_Emotion_Recognition|Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition]]

![[assets/2611.08860_figure.png|800]]

- **arXiv**: [2611.08860](https://arxiv.org/abs/2611.08860)
- **PDF**: https://arxiv.org/pdf/2611.08860
- **详细分析**: [[20_Research/Papers/大模型/Mind_the_Divergence_Divergence-Guided_Reliability-Aware_Fusion_and_Adaptive_LLM_Prompting_for_Conversational_Emotion_Recognition|Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition]]
- **作者**: Jingwen Wang, Jiao Li, Yuhang Qian, Yuyin Wang, Min Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal emotion recognition in conversations (MERC) integrates textual, acoustic, and visual cues to identify utterance-level emotions. However, existing approaches generally do not explicitly adapt multimodal processing to the degree of inter-modal predictive disagreement. In real conversations, semantic incongruity, concealed emotion, noisy observations, and ambiguity can affect modality-specific emotional evidence differently, while the reliability of individual modalities varies across samples. Rather than identifying each source of inconsistency separately, we model their common consequence for emotion recognition as predictive disagreement among unimodal emotion distributions over the same emotion-label set. Such disagreement makes indiscriminate fusion prone to propagating unreliable or competing evidence. Inspired by the Brunswik Lens Model, we propose MiD-ERC, a divergence-centric framework that quantifies inter-modal predictive disagreement using a normalized divergence score and estimates sample-specific modality reliability. MiD-ERC uses these signals to coordinate divergence-guided cross-modal gating, divergence-modulated reliability weighting, and divergence-conditioned adaptive LLM prompting. The framework is trained end-to-end using only standard emotion annotations, without requiring additional conflict labels, auxiliary data construction, or external retrieval modules. Experiments on IEMOCAP and MELD demonstrate that MiD-ERC achieves state-of-the-art performance, with particularly pronounced improvements on high-divergence samples.

</details>

---

### [[20_Research/Papers/强化学习/Training_Stability_under_Adaptive_Curricula|Training Stability under Adaptive Curricula]]

![[assets/2611.08787_first_page.png|800]]

- **arXiv**: [2611.08787](https://arxiv.org/abs/2611.08787)
- **PDF**: https://arxiv.org/pdf/2611.08787
- **详细分析**: [[20_Research/Papers/强化学习/Training_Stability_under_Adaptive_Curricula|Training Stability under Adaptive Curricula]]
- **作者**: Johan Obando-Ceron, Walter Mayor, Michael Dennis, Aaron Courville, Pablo Samuel Castro
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Training Stability under Adaptive Curricula》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unsupervised Environment Design (UED) approaches train reinforcement learning (RL) agents on diverse curricula that may evolve with their capabilities. While prior work has largely focused on how these curricula are constructed, we study whether their students remain trainable under the resulting distributions. Across multiple UED mechanisms, environment complexities, and extended training horizons, we identify recurring learner-side pathologies, including parameter growth, degraded value--outcome ordering, and loss of representational diversity, that accompany stagnation and performance degradation. These findings connect limitations in UED to optimization failures previously identified in conventional deep RL, while showing how adaptive curricula couple the learner's optimization state to its future training distribution. Controlled interventions show that mitigating selected pathologies improves learning. Stabilizing the learner improves long-horizon performance and zero-shot generalization without changing the curriculum rule or increasing environment interaction. Our results establish learner trainability as a complementary design principle for UED. Effective curricula require students that remain capable of learning from the distributions they produce.

</details>

---

### [[20_Research/Papers/大模型/Debate_to_Deceive_Poisoning_LLM's_Fact-Checking_via_Game-Theoretic_Multi-Agent_Debate|Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate]]

![[assets/2611.08756_figure.png|800]]

- **arXiv**: [2611.08756](https://arxiv.org/abs/2611.08756)
- **PDF**: https://arxiv.org/pdf/2611.08756
- **详细分析**: [[20_Research/Papers/大模型/Debate_to_Deceive_Poisoning_LLM's_Fact-Checking_via_Game-Theoretic_Multi-Agent_Debate|Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate]]
- **作者**: Liting Huang, Huizhi Liang, Yi Lei, Xingjun Ma, Varun Ojha
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge attacks on Large Language Models, such as manipulating fact-checking judgments, pose significant risks to AI reliability. Existing approaches -- adversarial suffix/template injection and single-agent self-reflection -- lack robustness across diverse defenses and are prone to confirmation bias and costly trial-and-error, respectively. We propose Debate-to-Deceive (D2D), a multi-agent debate framework grounded in human debate structure and rhetorical style, enabling agents to generate adversarial passages that are semantically coherent, rhetorically effective, and resistant to early confirmation bias. D2D formalizes the adversarial process as an evolutionary game in which agents adaptively evolve their rhetorical strategies (Logos, Pathos, Ethos) through competition. To manage the intractably large LLM output space, we decouple agent behavior into a strategic layer, which selects a rhetorical action from a compact strategy space via evolutionary-inspired learning dynamics, and a generation layer, where the LLM produces a concrete passage conditioned on that strategy and the debate context. On four fact-checking benchmarks (FEVER, HealthVer, CLIMATE-FEVER, and SciFact), D2D substantially outperforms existing attacks and evades most defenses.

</details>

---

### [[20_Research/Papers/大模型/Memory-Aware_Multi-Agent_Architecture_with_LLM-based_Orchestration_for_Conversational_Recommendation|Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation]]

![[assets/2611.08718_figure.png|800]]

- **arXiv**: [2611.08718](https://arxiv.org/abs/2611.08718)
- **PDF**: https://arxiv.org/pdf/2611.08718
- **详细分析**: [[20_Research/Papers/大模型/Memory-Aware_Multi-Agent_Architecture_with_LLM-based_Orchestration_for_Conversational_Recommendation|Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation]]
- **作者**: Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno, Marcus Santos, Bruno Ferraz do Amaral, Marcelo Nogueira, Lucas Francisco Pellicer, Lucas Lanaro, Pedro Augusto Luiz, João Renato Ribeiro Manesco, Giovanni Carbinatti, Isabela de Lima Santos...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system level. In this work, we propose a memory-aware multi-agent architecture for conversational recommendation, in which LLMs act as orchestration layers that coordinate intent refinement, query construction, and interaction flow. A key design principle is the integration of long-term memory as a first-class component, influencing both routing decisions and semantic query formation. We evaluate the system through cross-session memory experiments, multi-turn conversational simulations, and supervisor-driven interaction studies on the Amazon Reviews dataset. Results show that memory-enabled interactions recover up to 63\% of the gap toward explicit-query scenarios and prevent semantic degradation in extended dialogues. In addition, supervisory orchestration increases user acceptance by +28.9 percentage points, highlighting the importance of structured orchestration in guiding interaction and output quality. We also observe an exposure bottleneck between retrieved candidates and displayed recommendations. While LLM-reranking does not improve Hit@K, it consistently enhances semantic consistency and diversity. To capture these effects, we introduce the Semantic Consistency Score (SCS), a complementary evaluation measure. Overall, the results emphasize the importance of system-level design choices, suggesting that effective conversational recommendation benefits from explicit memory integration, orchestration, and evaluation beyond traditional ranking metrics.

</details>

---

### [[20_Research/Papers/大模型/Dual-Stream_LLM-Guided_Reward_Design_for_Reject-Inference-Aware_Reinforcement_Learning_in_E-Commerce_Payment_Fraud_Detection|Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection]]

![[assets/2611.08706_first_page.png|800]]

- **arXiv**: [2611.08706](https://arxiv.org/abs/2611.08706)
- **PDF**: https://arxiv.org/pdf/2611.08706
- **详细分析**: [[20_Research/Papers/大模型/Dual-Stream_LLM-Guided_Reward_Design_for_Reject-Inference-Aware_Reinforcement_Learning_in_E-Commerce_Payment_Fraud_Detection|Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection]]
- **作者**: Bo Qu, Zhurong Wang, Frank Zahradnik, Ming Ouyang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.65，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production fraud-detection models learn from a censored slice of their own traffic: transactions a legacy system blocked never receive fraud labels, so models train on a biased, approved-only distribution. We extend LLM-guided reward design, the framework of Qu et al. (2025) in which an LLM evolves the reward of a two-step REINFORCE fraud-blocking policy, to attack this reject-inference problem inside the reward. A single LLM designs a dual-stream reward: stream 1 applies the standard dollar-weighted precision objective to labeled transactions; stream 2 scores legacy-blocked, unlabeled transactions by contrasting the newest gradient-boosted risk signal against the legacy scores that drove the original block. Rather than prescribe which signals matter, we expose a superset of evidence and let the LLM decide for itself which to use, guided by evaluation feedback alone; because it writes the reward as code, that choice is directly auditable. On a held-out four-month out-of-time test, the dual-stream agent beats the prior labeled-only agent at every target recall, by +4.7, +2.4 and +3.0 points of dollar-weighted precision at 80%, 85% and 90% recall, and the production baseline by +6.8 points on average. The resulting policy is architecturally identical to that of Qu et al. (2025) and adds no inference cost.

</details>

---

### [[20_Research/Papers/强化学习/s$^3$_Simple_Scaling_of_Swarms_via_Cooperative_Multi-agent_RL|s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL]]

![[assets/2611.08615_first_page.png|800]]

- **arXiv**: [2611.08615](https://arxiv.org/abs/2611.08615)
- **PDF**: https://arxiv.org/pdf/2611.08615
- **详细分析**: [[20_Research/Papers/强化学习/s$^3$_Simple_Scaling_of_Swarms_via_Cooperative_Multi-agent_RL|s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL]]
- **作者**: Kunal Jha, Gonçalo Faria, Shuyue Stella Li, Scott Geng, Faeze Brahman, Noah A. Smith, Yulia Tsvetkov, Max Kleiman-Weiner, Natasha Jaques
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Groups can achieve more than individuals in the same amount of time, but only if their members coordinate: they must decide who works on what and what to share. However, this organization in multi-agent systems today usually comes from arbitrary, static harnesses designed a priori without adapting to agent behaviors or task specifications. We ask whether agents can instead learn to organize themselves. We introduce s$^3$, the first multi-agent reinforcement learning method in which agents decide for themselves how long to work alone and when to share findings or read teammates' messages, with no predefined organization or roles. Our s$^3$ agents learn to take different approaches, read each other's work, exhibit emergent roles that complement each other in the swarm, and generalize to bigger teams. We study both coordination, where agents must combine private information, and parallel exploration, where sharing discoveries can make search more efficient. With matched training and inference budgets, s$^3$, swarms evaluated with twice as many agents as in training solve over 25$\times$ more coordination problems than the strongest baseline, and in exploration, communicating agents reduce repeated work by nearly 50% and outperform best-of-N by up to 9.4 percentage points. Rather than being designed in advance, s$^3$ enables organization to emerge from a shared goal. This opens the door to capable systems built from many models that learn to work together.

</details>

---

### [[20_Research/Papers/强化学习/Q-OIL_Optimistic_Exploration_in_Learning_from_Human_Interventions|Q-OIL: Optimistic Exploration in Learning from Human Interventions]]

![[assets/2611.08576_figure.png|800]]

- **arXiv**: [2611.08576](https://arxiv.org/abs/2611.08576)
- **PDF**: https://arxiv.org/pdf/2611.08576
- **详细分析**: [[20_Research/Papers/强化学习/Q-OIL_Optimistic_Exploration_in_Learning_from_Human_Interventions|Q-OIL: Optimistic Exploration in Learning from Human Interventions]]
- **作者**: Pranav Teegavarapu, Sriyash Poddar, Rico Qi, Cleah Winston, Krisha Khandelwal, Aykut Onyol, Natasha Jaques, Abhishek Gupta
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Q-OIL: Optimistic Exploration in Learning from Human Interventions》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robots are deployed in the real world, they will inevitably make mistakes. Human interventions provide valuable feedback for improving their behavior, enabling them to adapt online to new scenarios. However, studying human-in-the-loop robot learning is difficult: real-world experiments are slow and expensive, so most algorithm development relies on simulated human models. We show that common human modeling assumptions do not match how real people intervene in practice. Through analyzing intervention data from human participants, we find that humans tend to intervene when agent progress stalls, and that their corrective actions are often suboptimal. Motivated by these findings, we introduce a progress-based model of human intervention that achieves higher rank correlation with real-user algorithm rankings, enabling realistic algorithm benchmarking and development in simulation. Building on these insights, we propose Q-OIL, a method that adds optimistic bonuses to intervention transitions in reinforcement learning and softly guides exploration toward human corrections. We find that decoupled critics are critical for stability because they prevent the bonuses from backing up to pre-intervention states. As a result, Q-OIL learns more efficiently than competitive baselines, achieving 10-50% higher success in simulation and on real robots, and improving pretrained VLAs on two bimanual manipulation tasks. As we ground both evaluation and algorithms in realistic human behavior, this work provides a practical path toward scalable robot learning from interventions.

</details>

---

### [[20_Research/Papers/大模型/LLM-Enhanced_Self-Evolving_Reinforcement_Learning_for_Multi-Step_E-Commerce_Payment_Fraud_Risk_Detection|LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection]]

![[assets/2509.18719_figure.png|800]]

- **arXiv**: [2509.18719](https://arxiv.org/abs/2509.18719)
- **PDF**: https://arxiv.org/pdf/2509.18719
- **详细分析**: [[20_Research/Papers/大模型/LLM-Enhanced_Self-Evolving_Reinforcement_Learning_for_Multi-Step_E-Commerce_Payment_Fraud_Risk_Detection|LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection]]
- **作者**: Bo Qu, Zhurong Wang, Daisuke Yagi, Zhen Xu, Yang Zhao, Yinan Shan, Frank Zahradnik
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.87（加权：大模型 0.55，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a novel approach to e-commerce payment fraud detection by integrating reinforcement learning (RL) with Large Language Models (LLMs). By framing transaction risk as a multi-step Markov Decision Process (MDP), RL optimizes risk detection across multiple payment stages. Crafting effective reward functions, essential for RL model success, typically requires significant human expertise due to the complexity and variability in design. LLMs, with their advanced reasoning and coding capabilities, are well-suited to refine these functions, offering improvements over traditional methods. Our approach leverages LLMs to iteratively enhance reward functions, achieving better fraud detection accuracy and demonstrating zero-shot capability. Experiments with real-world data confirm the effectiveness, robustness, and resilience of our LLM-enhanced RL framework through long-term evaluations, underscoring the potential of LLMs in advancing industrial RL applications.

</details>

---
