# cs.LG | Machine Learning | 2026-10-19

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/强化学习/CocoRNA_Collective_RNA_Design_with_Cooperative_Multi-agent_Reinforcement_Learning|CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning]]

![[assets/2610.23820_figure.png|800]]

- **arXiv**: [2610.23820](https://arxiv.org/abs/2610.23820)
- **PDF**: https://arxiv.org/pdf/2610.23820
- **详细分析**: [[20_Research/Papers/强化学习/CocoRNA_Collective_RNA_Design_with_Cooperative_Multi-agent_Reinforcement_Learning|CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning]]
- **作者**: Tianmeng Hu, Biao Luo, Ke Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design task by decomposing it into smaller sub-problems, each solved collaboratively by multiple agents. This approach reduces the complexity of the problem and improves the exploration of design policies. During training, a centralized critic uses global structural information to guide the agents, enabling them to jointly optimize their design strategies. As a result, CocoRNA learns high-quality RNA design policies that generalize effectively to unseen structures without additional training. Experiments on the Rfam dataset demonstrate that CocoRNA substantially outperforms state-of-the-art methods in both success rate and design speed. Further experiments on other biological sequence design tasks highlight the effectiveness and broad potential of CocoRNA for complex design tasks.

</details>

---

### [[20_Research/Papers/强化学习/JAXtari_High-Throughput_and_Easy-to-Modify_Arcade_Learning_Environment|JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment]]

![[assets/2610.23650_figure.png|800]]

- **arXiv**: [2610.23650](https://arxiv.org/abs/2610.23650)
- **PDF**: https://arxiv.org/pdf/2610.23650
- **详细分析**: [[20_Research/Papers/强化学习/JAXtari_High-Throughput_and_Easy-to-Modify_Arcade_Learning_Environment|JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment]]
- **作者**: Quentin Delfosse, Raban Emunds, Paul Seitz, Sebastian Wette, Jannis Blüml, Daniel Kirn, Dominik Mandok, Kristian Kersting
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CleanRL, D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Arcade Learning Environment (ALE) has been a cornerstone of Deep Reinforcement Learning research, providing a standardized benchmark for evaluating general agents. However, its lack of native support for object-extraction and environment modification restricts research into evaluating whether agents learn robust causal models or rely on brittle visual heuristics. Furthermore, the ALE's dependence on CPU-based emulation creates a significant bottleneck in modern GPU-accelerated training pipelines, limiting both experimental scale and iteration frequency. In this work, we introduce JAXtari, an open-source, high-performance reimplementation of Atari 2600 environments. By leveraging massive GPU parallelization, JAXtari allows PPO agents to finish training on 100M environment steps on a single A100-GPU in under an hour. Beyond speed, it provides object-centric observations and a flexible modification system, allowing researchers to, e.g. develop neuro-symbolic methods or discover novel shortcuts and subsequently train and adapt their agents rapidly, sometimes in only minutes.

</details>

---

### [[20_Research/Papers/大模型/Contracting_with_an_Agent_under_Model_Mismatch|Contracting with an Agent under Model Mismatch]]

![[assets/2610.23402_figure.png|800]]

- **arXiv**: [2610.23402](https://arxiv.org/abs/2610.23402)
- **PDF**: https://arxiv.org/pdf/2610.23402
- **详细分析**: [[20_Research/Papers/大模型/Contracting_with_an_Agent_under_Model_Mismatch|Contracting with an Agent under Model Mismatch]]
- **作者**: Elif Yılmaz, Jakub Tłuczek, Victor Villin, Christos Dimitrakakis
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Contracting with an Agent under Model Mismatch》归入 大模型、世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the classical principal-agent setting, the principal delegates some task to the agent, who receives a payment conditioned on the outcome of the task, which in turn benefits the principal. To align their objectives, the principal designs a contract that incentivizes the agent to take actions beneficial to the principal. In practice, however, the agent may act under misspecified beliefs about the underlying environment, leading to systematically suboptimal decisions. In this work, we study this problem through a principal-agent Markov Decision Process (PAMDP), in which the principal repeatedly interacts with an agent whose transition model may differ from the true environment dynamics. The principal has access to the true transition model and designs contracts that account for the agent's belief and incentives. We characterize contract design under model mismatch and develop a framework that enables the principal to induce desirable long-term benefits even though the agent has a potentially inaccurate understanding of the environment.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Success_Rate_Interventional_Evaluation_of_Memory_in_Vision-Language-Action_Systems|Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems]]

![[assets/2610.23372_figure.png|800]]

- **arXiv**: [2610.23372](https://arxiv.org/abs/2610.23372)
- **PDF**: https://arxiv.org/pdf/2610.23372
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Success_Rate_Interventional_Evaluation_of_Memory_in_Vision-Language-Action_Systems|Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems]]
- **作者**: Keyuan Luo, Yi Xie, Wanyun Ling, Yuanzhe Li, Ziyue Li, Zhuoqi Zeng
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChainBench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When we say that a robot uses memory, does that memory actually play a role? Success-rate ablations alone cannot establish the use of task-relevant facts: they change information and computation together, while aggregate rates can hide offsetting gains and losses. We propose an Interventional Memory Evaluation Protocol (IMEP) for vision-language-action (VLA) systems to address four questions: (1) Does memory provide a net benefit? (2) Under what conditions does memory help? (3) Do changes to memory alter task outcomes? (4) Are these effects specific to task-relevant facts? At the retrieval interface, we compare target-fact substitutions with fact-preserving replacements, minimal numerical perturbations, and exact replicas, while assessing decision correctness separately from motor execution success. We evaluate within-episode, cross-episode, and agentic memory. In cross-episode learned-bank experiments, a one-unit-in-the-last-place (ULP) intervention, including its installation procedure, changes 11.9% of seed-paired outcomes, while changing key facts produces no clear additional effect over fact-preserving replacements. To examine when memory helps, we introduce ChainBench, where correct decisions require historical information unavailable in current observations. The full memory configuration raises task success from 39.1% to 74.3%, matching the oracle-decision condition under shared recorded executions. These results show that correct history can support robot decisions, but establishing whether a memory system realizes this benefit requires fact-specific evidence beyond aggregate success rates.

</details>

---

### [[20_Research/Papers/具身智能/NestedVLA_Learning_to_Consolidate_and_Generate_Skills_for_Vision-Language-Action_Models|NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models]]

![[assets/2610.23271_figure.png|800]]

- **arXiv**: [2610.23271](https://arxiv.org/abs/2610.23271)
- **PDF**: https://arxiv.org/pdf/2610.23271
- **详细分析**: [[20_Research/Papers/具身智能/NestedVLA_Learning_to_Consolidate_and_Generate_Skills_for_Vision-Language-Action_Models|NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models]]
- **作者**: Guodong Du, Wanyu Lin
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MergeVLA, MetaWorld, NestedVLA, NeurIPS2026-NestedVLA, OpenVLA, ReVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc. To this end, we propose NestedVLA, which replaces parameter aggregation with parameter generation: a nested hypernetwork, conditioned on the target task, synthesizes task-adaptive action-expert parameters that compose with a frozen base VLA. Task-specific compressed VLM residuals are retained separately. This formulation enables flexible task-conditioned skill reuse while mitigating interference. Across three RL benchmarks (MetaWorld, ManiSkill, CALVIN), NestedVLA outperforms the strongest model-merging baseline by 41 pp on average, matches per-task fine-tuning within 1 pp on ManiSkill, and substantially closes the gap on CALVIN, pointing toward a storage-efficient route to skill consolidation. Code is available at https://github.com/WanyuGroup/NeurIPS2026-NestedVLA.

</details>

---

### [[20_Research/Papers/强化学习/Grounded_Credit_Assignment_in_Reinforcement_Learning_for_Multi-Turn_Search_Agents|Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents]]

![[assets/2610.23148_figure.png|800]]

- **arXiv**: [2610.23148](https://arxiv.org/abs/2610.23148)
- **PDF**: https://arxiv.org/pdf/2610.23148
- **详细分析**: [[20_Research/Papers/强化学习/Grounded_Credit_Assignment_in_Reinforcement_Learning_for_Multi-Turn_Search_Agents|Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents]]
- **作者**: Qirui Liu, Hao Chen, Yi Wen, Weijie Shi, Yao Zhao, Xianhe Chen, Hao Zhao, Xing Tang, Weihong Luo, Yuyu Luo
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Outcome-reward reinforcement learning such as GRPO gives every token of a search-agent rollout the same advantage, although the rollout exercises two capabilities: finding evidence and using it. We show that accuracy improves without grounding: Search-R1 raises accuracy on all seven QA benchmarks, yet on Bamboogle the evidence-supported share of correct answers falls from 84.0% to 42.9%. We attribute this to GRPO's credit assignment: rollouts that retrieve answer-bearing evidence are favoured in aggregate only in proportion to their accuracy gain over the rest, a grounding gap that answering from memory or misusing evidence shrinks or reverses. To address this, we propose Grounded Credit Assignment (GCA), which uses verifiable sub-outcomes (evidence retrieval and answer correctness) to correct search and answer credit separately: a wrong answer is blamed more than the search that found the evidence, and a correct answer that bypasses retrievable evidence is credited less. Never negative on evidence-finding search, the correction does not shrink with the grounding gap; capped at 10% of each token's advantage, it never overrides the outcome signal. Without extra models, rollouts, or training stages, GCA improves average EM over Search-R1 by 5.7 (Qwen2.5-3B) and 6.3 points (Qwen3-30B-A3B) and raises this share from 76.9% to 93.4%.

</details>

---

### [[20_Research/Papers/机器人/Shape-Aware_Neural_Time_Fields_for_Rigid-Body_Motion_and_Manipulation_Planning|Shape-Aware Neural Time Fields for Rigid-Body Motion and Manipulation Planning]]

![[assets/2610.22762_figure.png|800]]

- **arXiv**: [2610.22762](https://arxiv.org/abs/2610.22762)
- **PDF**: https://arxiv.org/pdf/2610.22762
- **详细分析**: [[20_Research/Papers/机器人/Shape-Aware_Neural_Time_Fields_for_Rigid-Body_Motion_and_Manipulation_Planning|Shape-Aware Neural Time Fields for Rigid-Body Motion and Manipulation Planning]]
- **作者**: Yanming Zhou, Yuchen Liu, Ahmed H. Qureshi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Shape-Aware Neural Time Fields for Rigid-Body Motion and Manipulation Planning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rigid-body motion planning is fundamental to robotic transport and manipulation, where both object position and orientation determine whether a body can move through cluttered environments. This coupling makes planning chal- lenging because translation and rotation can be constrained very differently by surrounding geometry. We propose Shape- Aware Neural Time Fields, a physics-informed neural motion planning framework that learns a reusable travel-time, or cost- to-go, representation for rigid-body motion while explicitly accounting for these distinct geometric restrictions. The learned field captures local motion difficulty in translation and rotation and is paired with a sampling-based planner that balances progress toward the goal with the cost of reaching nearby poses. We evaluate the framework across 2D and 3D rigid- body planning tasks and non-prehensile manipulation through object pushing in diverse environments. Results show substantial improvements in planning success and inference efficiency over physics-informed neural planning baselines, while remaining competitive with classical sampling-based planners at significantly lower planning times. Ablation studies further validate the contributions of both the learned representation and the proposed planning strategy. Finally, closed-loop pushing experiments under execution deviations and external disturbances demonstrate that fast replanning enables reactive and adaptive task execution.

</details>

---

### [[20_Research/Papers/机器人/Embodiment-Classifier_Guidance_Transferring_Frozen_VLAs_Across_Robot_Dynamics_without_Demonstrations|Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations]]

![[assets/2610.22576_figure.png|800]]

- **arXiv**: [2610.22576](https://arxiv.org/abs/2610.22576)
- **PDF**: https://arxiv.org/pdf/2610.22576
- **详细分析**: [[20_Research/Papers/机器人/Embodiment-Classifier_Guidance_Transferring_Frozen_VLAs_Across_Robot_Dynamics_without_Demonstrations|Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations]]
- **作者**: Devin Han, Hershraj Niranjani
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based policies such as $π_0$ are trained on a fixed set of embodiments, and transferring them to new ones is an open problem. To adapt a frozen $π_0$ to a new embodiment without additional demonstrations or parameter updates, we train a lightweight embodiment classifier to distinguish successful action chunks on the source body from those on the target body, using a few calibration tasks. On transfer tasks that $π_0$ saw on its source body but the classifier was never trained on, we nudge each denoising step of $π_0$ with the classifier's gradient, which estimates the direction from the distribution of successful actions on the source body toward that on the target body. On the LIBERO simulation benchmark with four modified controllers, embodiment-classifier guidance raises $π_0$'s average success on the target bodies from 72% to 80% across 12 suite-controller pairs, with a 31% relative reduction in failures (11 of 12 gain; 5 significant after Holm correction). In simulation, guidance is data-efficient, needing few target-body rollouts per task, which makes it promising for sim-to-real transfer, where rollouts are costly. Guidance is mixed on weak wrists and harmful on a locked wrist, when the classifier lacks data or favors infeasible motions. Collecting more target-body data with guided $π_0$ can fill such gaps: on one weak-wrist arm, guided $π_0$ solved a task on which unguided $π_0$ had zero successes in the original data, and retraining the classifier on the guided successes raised success from 52.5% to 70.7%.

</details>

---

### [[20_Research/Papers/具身智能/When_Plans_Change,_Remember_Replanning-Guided_Visual_Memory_for_Vision-Language-Action_Models|When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models]]

![[assets/2610.22556_figure.png|800]]

- **arXiv**: [2610.22556](https://arxiv.org/abs/2610.22556)
- **PDF**: https://arxiv.org/pdf/2610.22556
- **详细分析**: [[20_Research/Papers/具身智能/When_Plans_Change,_Remember_Replanning-Guided_Visual_Memory_for_Vision-Language-Action_Models|When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models]]
- **作者**: Victoria Smelova, Daniil Kazachkov, Georgiy Kazantsev, Iuliia Tsvetkova, Egor Cherepanov, Nikita Kachaev, Artem Latyshev, Aleksandr I. Panov, Alexey K. Kovalev
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MIKASA-Robo-VLA, OpenVLA, RePlanMem-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation. Retaining the complete observation history is computationally expensive and highly redundant, motivating selective visual memory. We introduce RePlanMem-VLA (Replanning-Guided Keyframe Memory for VLA), which turns a policy's own plan revisions into an online memory-write signal. Under receding-horizon execution, consecutive action chunks predict some of the same future actions. RePlanMem-VLA treats unusually large disagreement between these temporally aligned predictions as evidence of a task-relevant event. We first compare 35 disagreement measures across single-task autoregressive decoder-only and Flow-Matching Transformers trained from scratch, then validate the selected signals on pretrained OpenVLA-OFT and $π_{0.5}$ policies over MIKASA-Robo-VLA tasks. The resulting detectors achieve ROC-AUC of 0.981-0.997. We then use the selected signals in RePlanMem-VLA to trigger updates to a bounded visual memory, with a robot-masked write filter suppressing redundant frames. In the evaluated memory-retention experiments, RePlanMem-VLA preserves task-relevant observations until the later decision point in 100% of episodes. Real-robot replay data further show that event selection and redundancy suppression extend beyond simulation. These results establish plan revision as a policy-internal signal for controlling what a VLA remembers. Website: https://vika787.github.io/RePlanMem/.

</details>

---
