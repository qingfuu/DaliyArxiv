# cs.AI | Artificial Intelligence | 2026-10-16

#arxiv #ComputerScience

**论文数**: 32

### [[20_Research/Papers/具身智能/LIBERO-PeRM_Benchmarking_Personalized_Robotic_Manipulation|LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation]]

![[assets/2610.22372_figure.png|800]]

- **arXiv**: [2610.22372](https://arxiv.org/abs/2610.22372)
- **PDF**: https://arxiv.org/pdf/2610.22372
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-PeRM_Benchmarking_Personalized_Robotic_Manipulation|LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation]]
- **作者**: Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang, Tianze Xu, Zehao Wang, Yuping Wang, Junge Zhang, Jiachen Li
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InternVLA, RLBench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings; 2) how they learn single preferences from demonstrations; 3) how efficiently they acquire preferences as demonstrations increase; 4) how learned preferences generalize across layouts and tasks; and 5) how policies compose preferences and behave under conflicts. We propose a controlled formulation and taxonomy of observable preferences in simulation, covering motion, skill, and user-profile choices. This formulation is restricted to language-expressible preferences that can be instantiated in LIBERO without changing the task goal, evaluated automatically, and reused across tasks. Building on LIBERO, our procedural pipeline generates paired demonstrations with and without preferences. We create five task suites (312 tasks) with high-quality demonstrations, rich metadata, and preference-satisfaction metrics. Experiments show that current VLA policies struggle with zero-shot personalization, while SFT makes preferences learnable. Mixed training achieves better no-preference retention than sequential adaptation and improves performance with contextual prompts compared with preference-only training, but can weaken motion-preference learning; preference generalization, decomposition, and conflict handling remain difficult. The code, datasets, and demos can be found on the project website: https://libero-perm.github.io/.

</details>

---

### [[20_Research/Papers/世界模型/T2-z_Test-Time_Optimization_of_Environment_Latents_for_Robotic_World_Models|T2-z: Test-Time Optimization of Environment Latents for Robotic World Models]]

![[assets/2610.22364_figure.png|800]]

- **arXiv**: [2610.22364](https://arxiv.org/abs/2610.22364)
- **PDF**: https://arxiv.org/pdf/2610.22364
- **详细分析**: [[20_Research/Papers/世界模型/T2-z_Test-Time_Optimization_of_Environment_Latents_for_Robotic_World_Models|T2-z: Test-Time Optimization of Environment Latents for Robotic World Models]]
- **作者**: Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang, David Held, Vitor Campagnolo Guizilini, Yue Wang, Li Fei-Fei, Jiajun Wu, Leonidas Guibas, Yejin Choi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《T2-z: Test-Time Optimization of Environment Latents for Robotic World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z for test-time optimization of environment latents, which augments a robotic world model with a learnable environment latent to condition world predictions. This compact latent captures underlying environmental variation without supervision of what environmental factors exist or what values they take. During training, T2-Z alternates between two stages: a world-model optimization stage that fixes the latents and learns general action-conditioned dynamics across environments; and an environment-latent optimization stage that freezes the world model and optimizes the conditioning latents, allowing latent structure to emerge purely through world prediction. At test time, the world model remains frozen and a newly initialized environment latent is optimized from one or more test-time interactions, adapting the model to previously unseen environmental configurations. Across 7 simulated settings and 4 real-world robotic tasks, T2-Z reduces object prediction error metric from 15.20 to 7.00 and raises action success from 33.73% to 72.96%. Its emergent latents capture structured representations of individual and compounded factors across diverse visual scenes. Ablations further show that T2-Z can efficiently infer environment latents from as little as a single test-time interaction trajectory.

</details>

---

### [[20_Research/Papers/强化学习/Dexterity_from_Supervised_Play|Dexterity from Supervised Play]]

![[assets/2610.22340_figure.png|800]]

- **arXiv**: [2610.22340](https://arxiv.org/abs/2610.22340)
- **PDF**: https://arxiv.org/pdf/2610.22340
- **详细分析**: [[20_Research/Papers/强化学习/Dexterity_from_Supervised_Play|Dexterity from Supervised Play]]
- **作者**: Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma, Ruoshi Liu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.9，强化学习 0.2，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Dexterity from Supervised Play》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-conditioned policy through self-play within the learned world model. We evaluate this framework on underactuated pushing and any-to-any in-hand pose reorientation with a multifingered hand, in simulation and real world. In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data. These results demonstrate that supervised play can autonomously collect interaction data, guide model-based planning, and enable policy learning without any task-specific demonstrations or sim-to-real transfer.

</details>

---

### [[20_Research/Papers/强化学习/KnowGPO_Knowledge-Grouped_Policy_Optimization_for_Search_Agents|KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents]]

![[assets/2610.22331_figure.png|800]]

- **arXiv**: [2610.22331](https://arxiv.org/abs/2610.22331)
- **PDF**: https://arxiv.org/pdf/2610.22331
- **详细分析**: [[20_Research/Papers/强化学习/KnowGPO_Knowledge-Grouped_Policy_Optimization_for_Search_Agents|KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents]]
- **作者**: Siqi Chen, Zhengxi Lu, Yuchen Yan, Xingyu Wu, Qipeng Chen, Xin Zhang, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Weiming Lu, Jun Xiao...
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unreliable in deep search where observations are heterogeneous and retrieved contexts are long and noisy. We propose KnowGPO, a reinforcement learning framework that aligns trajectories by the task-relevant knowledge they have acquired rather than by their surface observations. For each query, KnowGPO decomposes the information required to derive the answer into atomic knowledge conditions, and represents the state of a trajectory at each step by the subset of conditions it has satisfied. Trajectories sharing the same knowledge state are grouped for within-group comparison, and the incremental knowledge gain between consecutive steps serves as an environment-grounded process reward. Experiments on Xbench, BrowseComp-ZH, and GAIA show KnowGPO consistently outperforms outcome-only (GRPO) and process-supervision baselines (GiGPO, IGPO) by 3.8 to 4.2 points, with our 8B model rivaling or exceeding most 32B open-source systems.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Self-Orchestration_in_Decentralized_Agent_Swarms|Learning Self-Orchestration in Decentralized Agent Swarms]]

![[assets/2610.22322_figure.png|800]]

- **arXiv**: [2610.22322](https://arxiv.org/abs/2610.22322)
- **PDF**: https://arxiv.org/pdf/2610.22322
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Self-Orchestration_in_Decentralized_Agent_Swarms|Learning Self-Orchestration in Decentralized Agent Swarms]]
- **作者**: Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.45（加权：具身智能 0.6，大模型 0.65，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning Self-Orchestration in Decentralized Agent Swarms》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt together without a central coordinating agent. We evaluate MPT on embodied crafting, robot navigation, and deep research. Results show gains over monolithic post-training and confirm that agent participation indeed evolves with learning. With the same post-trained action policies, learned self-orchestration outperforms alternative coordination strategies. Ablations show that both action and bidding benefit from learning, and that learned bids provide more effective action-training signals. Beyond the original training objectives, trained swarms adapt faster to related tasks and achieve better performance with larger populations at inference time. Larger populations also suffer smaller performance losses under agent dropout, demonstrating that learned self-orchestration supports reuse, scaling, and robustness in decentralized agent swarms. Code and trained models are available at https://github.com/Embodied-Minds-Lab/MPT.

</details>

---

### [[20_Research/Papers/大模型/Learning_to_Steer_LLM_Agents_and_Multi-Agent_Systems|Learning to Steer LLM Agents and Multi-Agent Systems]]

![[assets/2610.22316_first_page.png|800]]

- **arXiv**: [2610.22316](https://arxiv.org/abs/2610.22316)
- **PDF**: https://arxiv.org/pdf/2610.22316
- **详细分析**: [[20_Research/Papers/大模型/Learning_to_Steer_LLM_Agents_and_Multi-Agent_Systems|Learning to Steer LLM Agents and Multi-Agent Systems]]
- **作者**: Leyang Shen, Yaxin Gong, Yang Zhang, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Fuli Feng, Chun Kai Ling, Tat-Seng Chua
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 2.12（加权：大模型 1.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Learning to Steer LLM Agents and Multi-Agent Systems》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed goal drift. In this work, we propose a steering agent that supervises execution on the fly and steers the system back on track when drift occurs. The steering agent observes the execution context, deciding when to intervene with a low-cost fast path and how to intervene with a high-cost slow path. To unlock its steering intelligence, the ability to assess goal drift and generate effective interventions, we jointly train the two paths with reinforcement learning, combining a pairwise ranking objective with group-relative policy optimization (GRPO). Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency. The learned steering intelligence generalizes to out-of-domain tasks, transfers to unseen executors, and supports controllable intervention frequency without retraining.

</details>

---

### [[20_Research/Papers/大模型/Librarian_Agents_Training_LLMs_to_Curate_Long-Context_Workspaces_that_Anticipate_Future_Queries|Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries]]

![[assets/2610.22273_figure.png|800]]

- **arXiv**: [2610.22273](https://arxiv.org/abs/2610.22273)
- **PDF**: https://arxiv.org/pdf/2610.22273
- **详细分析**: [[20_Research/Papers/大模型/Librarian_Agents_Training_LLMs_to_Curate_Long-Context_Workspaces_that_Anticipate_Future_Queries|Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries]]
- **作者**: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.75，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

</details>

---

### [[20_Research/Papers/强化学习/Whole-Body_Dexterity|Whole-Body Dexterity]]

![[assets/2610.22184_figure.png|800]]

- **arXiv**: [2610.22184](https://arxiv.org/abs/2610.22184)
- **PDF**: https://arxiv.org/pdf/2610.22184
- **详细分析**: [[20_Research/Papers/强化学习/Whole-Body_Dexterity|Whole-Body Dexterity]]
- **作者**: Conor Mc Gartoll, An Dang, Pranay Thangeda, Arjun Gupta, Carolina Higuera, Nima Fazeli, Mustafa Mukadam, Manikantan Nambi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Whole-Body Dexterity》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current humanoid dexterous manipulation remains largely confined to end-effectors and simple grasps, falling short of humans' ability to engage the entire body by bracing and sliding bulky objects against the arms and torso. We introduce Whole-Body Dexterity (WBD), a general framework that uses the robot's body and appendages as contact surfaces to grasp and manipulate objects. Our sim-to-real pipeline first generates a dataset of feasible whole-body grasps, then trains reinforcement-learning experts on a general any-to-any repositioning objective by sampling initial and goal grasps from the dataset, and distills these experts into a single policy that uses proprioception and object geometry. We show that the distilled policy transfers zero-shot to a real Unitree G1, where it repositions a basketball and a cardboard box to regions around the torso and completes a long-horizon task that stows a box under one arm, carries it from a shelf to a table, and places it. The controller operates interactively, steered by coarse motion references from a human teleoperator. Across real-world whole-body manipulation tasks, the distilled controller completes 90% of trials, compared with 18% for direct retargeting and 4% for a generalist whole-body controller.

</details>

---

### [[20_Research/Papers/强化学习/Mosaic_Multi-Session_Agentic_Reinforcement_Learning|Mosaic: Multi-Session Agentic Reinforcement Learning]]

![[assets/2610.22174_figure.png|800]]

- **arXiv**: [2610.22174](https://arxiv.org/abs/2610.22174)
- **PDF**: https://arxiv.org/pdf/2610.22174
- **详细分析**: [[20_Research/Papers/强化学习/Mosaic_Multi-Session_Agentic_Reinforcement_Learning|Mosaic: Multi-Session Agentic Reinforcement Learning]]
- **作者**: Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan, Zhijiang Guo
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Mosaic: Multi-Session Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple sessions, creating a mismatch between the single-session training assumption and inference-time execution. Therefore, we introduce Multi-Session Agentic Reinforcement Learning, a more general setting that supports an arbitrary number of sessions within a trajectory. Under this setting, a widely adopted method is to broadcast trajectory-level advantages to all sessions, but this does not distinguish contributions from various sessions or guide session allocation within trajectories. To address this issue, we propose Mosaic, a multi-session agentic RL method with critic-free hierarchical optimization. At the trajectory level, it incorporates session-usage signals into advantage estimation. At the session level, it shapes each session's advantage according to the estimated marginal contribution. Experiments on BrowseComp with Qwen3.5-4B show that Mosaic outperforms broadcasting in both context compaction and subagent forking scenarios while using fewer sessions on average. Further analyses show that our method achieves improvements in session utility and allocation, which we suggested is a promising target for future advances in multi-session agentic RL.

</details>

---

### [[20_Research/Papers/强化学习/Specification_Gaming_and_a_Constrained_Reinforcement_Learning_Mitigation_in_a_Cleaning_Gridworld|Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld]]

![[assets/2610.22152_figure.png|800]]

- **arXiv**: [2610.22152](https://arxiv.org/abs/2610.22152)
- **PDF**: https://arxiv.org/pdf/2610.22152
- **详细分析**: [[20_Research/Papers/强化学习/Specification_Gaming_and_a_Constrained_Reinforcement_Learning_Mitigation_in_a_Cleaning_Gridworld|Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld]]
- **作者**: Hilda Adwubi Osei
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Specification Gaming and a Constrained Reinforcement Learning Mitigation in a Cleaning Gridworld》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CleaningGridWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning agents optimize exactly the reward signal they are given, which can diverge sharply from an intended true objective when that signal is only a proxy for it; this failure mode is known as specification gaming. Existing evidence for this failure mode is largely observational, with comparatively few demonstrations pairing a controlled, deliberately constructed proxy/true gap with a mitigation that carries a verifiable guarantee rather than only an empirical improvement. We construct a minimal gridworld in which a cleaning-robot agent can either genuinely remove dirt or conceal it from a cheap sensor, and show that a standard deep Q-network trained only on the sensor's proxy reward converges to a policy that games it completely, reaching near-maximal proxy reward while never achieving the true objective. We then introduce a constrained reinforcement learning fix, penalizing the specific behaviors through which the agent exploits the gap, and show that it eliminates the gaming behavior from the final policy while substantially recovering true-objective performance. We further derive and empirically verify an exact accounting identity relating the proxy reward, true reward, and our cost signal for this environment, showing that the cost signal measures the proxy/true gap exactly rather than merely tracking it, and yields a deterministic guarantee under a hard-constrained variant of the method.

</details>

---

### [[20_Research/Papers/大模型/Believed_but_Not_Said_Measuring_Hidden_Belief_Collapse_in_Multi-Agent_LLM_Discussions|Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions]]

![[assets/2610.22138_figure.png|800]]

- **arXiv**: [2610.22138](https://arxiv.org/abs/2610.22138)
- **PDF**: https://arxiv.org/pdf/2610.22138
- **详细分析**: [[20_Research/Papers/大模型/Believed_but_Not_Said_Measuring_Hidden_Belief_Collapse_in_Multi-Agent_LLM_Discussions|Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions]]
- **作者**: Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：PopQA, SQA, SimpleQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round we probe each benign agent's private answer through a separate call whose response is hidden from its peers, and we separately label its public stance toward the claim. Across six models and three factual-QA datasets, groups remain stable without an attacker: only 0.6% of benign agents finish with the false answer. A single adversarial agent increases this rate to 44.8% and three to 60.5%. Studies of conformity typically report public agreement without private change; we find the reverse. With three adversarial agents present, benign agents hold the false answer in 51.6% of exposed turns but publicly endorse it in only 19.7%. Much of the influence therefore remains invisible in the discussion, and the false answers persist when agents are asked for their own views. Agents that retain the true answer often fail to defend it; once adopted, the false answer spreads among benign agents, and baseline knowledge does not predict robustness.

</details>

---

### [[20_Research/Papers/大模型/Progress_Reward_Model_for_Reinforcement_Learning_via_Large_Language_Models|Progress Reward Model for Reinforcement Learning via Large Language Models]]

![[assets/2610.22056_figure.png|800]]

- **arXiv**: [2610.22056](https://arxiv.org/abs/2610.22056)
- **PDF**: https://arxiv.org/pdf/2610.22056
- **详细分析**: [[20_Research/Papers/大模型/Progress_Reward_Model_for_Reinforcement_Learning_via_Large_Language_Models|Progress Reward Model for Reinforcement Learning via Large Language Models]]
- **作者**: Xiuhui Zhang, Ning Gao, Xingyu Jiang, Yihui Chen, Yuheng Pan, Mohan Zhang, Yue Deng
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型
- **相关性评分**: 2.1（加权：大模型 0.1，强化学习 1.8，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Progress Reward Model for Reinforcement Learning via Large Language Models》归入 强化学习、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PRM4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional reinforcement learning (RL) algorithms face significant limitations in handling long-term tasks with sparse rewards. Recent advancements have leveraged large language models (LLMs) to enhance RL by utilizing their world knowledge for task planning and reward generation. However, planning-based approaches often depend on pre-defined skill libraries and fail to optimize low-level control policies, while reward-based methods require extensive human feedback or exhaustive searching due to the complexity of tasks. In this paper, we propose the Progress Reward Model for RL (PRM4RL), a novel framework that integrates task planning and dense reward to enhance RL. For high-level planning, a complex task is decomposed into a series of simple manageable subtasks, with a subtask-oriented, fine-grained progress function designed to monitor task execution progress. For low-level reward generation, inspired by potential-based reward shaping, we use the progress function to construct a Progress Reward Model (PRM), providing theoretically grounded optimality and convergence guarantees, thereby enabling effective policy optimization. Experimental results on robotics control tasks demonstrate that our approach outperforms both LLM-based planning and reward methods, achieving state-of-the-art performance. Code is available at https://github.com/deng-ai-lab/PRM4RL.

</details>

---

### [[20_Research/Papers/大模型/GraphACM_Graph-based_Action_Consistency_Measurement_for_Uncertainty_Quantification_in_LLM_Agents|GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents]]

![[assets/2610.22031_figure.png|800]]

- **arXiv**: [2610.22031](https://arxiv.org/abs/2610.22031)
- **PDF**: https://arxiv.org/pdf/2610.22031
- **详细分析**: [[20_Research/Papers/大模型/GraphACM_Graph-based_Action_Consistency_Measurement_for_Uncertainty_Quantification_in_LLM_Agents|GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents]]
- **作者**: Yaxin Ma, Wenbo Zhang, Satya Krishna Pothapragada, Alina Zare
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Action-Set, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavioral consistency across repeated executions provides an informative signal for assessing the reliability of large language model (LLM) agents. However, existing approaches typically summarize consistency with a single task-level score, without identifying where behavioral differences occur or whether actions are compared under equivalent decision contexts. We propose a graph-based framework for fine-grained behavioral consistency measurement and uncertainty quantification. Given multiple rollouts of the same task, we merge equivalent states into a directed, action-labeled graph, enabling action comparisons at shared decision states. We introduce node-level and global measures of action consistency, using the global consistency score as a proxy for uncertainty to predict task success or failure. Experiments across three LLMs on ALFWorld, AppWorld, and WebShop demonstrate that our measure is positively associated with task success and achieves an average AUROC of 0.811 for task-success prediction, outperforming the strongest behavioral-consistency baseline (0.729) and verbalized confidence (0.769). These results highlight the effectiveness of state-conditioned behavioral consistency and pinpoint where agent actions agree.

</details>

---

### [[20_Research/Papers/大模型/CoWorld_Reasoner_Agentic_Multimodal_Reasoning_with_the_Evolving_Video_World_Model-Driven_Harness|CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness]]

![[assets/2610.21910_first_page.png|800]]

- **arXiv**: [2610.21910](https://arxiv.org/abs/2610.21910)
- **PDF**: https://arxiv.org/pdf/2610.21910
- **详细分析**: [[20_Research/Papers/大模型/CoWorld_Reasoner_Agentic_Multimodal_Reasoning_with_the_Evolving_Video_World_Model-Driven_Harness|CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness]]
- **作者**: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，世界模型 1）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoWorld, ERQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual content as additional evidence. However, existing approaches typically invoke a VWM through fixed pipelines centered on a predefined form of visual imagination, such as novel-view synthesis. To support flexible visual imagination for diverse reasoning tasks, we introduce CoWorld Reasoner, an agentic framework that uses a VWM as a unified visual reasoning engine. Its Video World Model-Driven Harness exposes multiple visual operations through tools and uses skills to guide the VLM in deciding whether to imagine, selecting an operation, constructing a generation request, and interpreting the resulting visual evidence. We further introduce VLM-VWM Harness Co-Evolution, which jointly revises tools, skills, and execution code based on execution feedback while keeping both model weights fixed. Across seven benchmarks spanning spatial intelligence, temporal and causal reasoning, and perceptual reasoning, CoWorld Reasoner outperforms direct reasoning with the same VLM. The strongest variant improves on all seven benchmarks, including relative accuracy gains of 11.8% on MMSI and 13.0% on ERQA, and outperforms all five evolving baselines using the same backbone across five benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Anvil_Scaling_Embodied_Spatial_Intelligence_through_Knowledge_Recirculation|Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation]]

![[assets/2610.21882_figure.png|800]]

- **arXiv**: [2610.21882](https://arxiv.org/abs/2610.21882)
- **PDF**: https://arxiv.org/pdf/2610.21882
- **详细分析**: [[20_Research/Papers/具身智能/Anvil_Scaling_Embodied_Spatial_Intelligence_through_Knowledge_Recirculation|Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation]]
- **作者**: Weilin Ruan, Bohan Zhou, Jinghao Li, Yangkai Wei, Wenqian Li, Peiran Dong, Yingjie Xu, Leyi Wu, Haojian Huang, Binghui Xie, Han Yang, Kaiwen Zhou...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Anvil-Eval, VABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied spatial intelligence requires more than visual recognition: models must localize entities, reason about their relations, and express this knowledge in action-relevant forms. Yet joint training can conflate the knowledge needed at different stages because supervision is fragmented across incompatible geometric and semantic outputs. We introduce Anvil, a unified framework for data generation, training, and benchmarking for embodied spatial intelligence. (1) Anvil-Gen is a heterogeneous data flywheel that combines form-specific generation, cross-stage consistency verification, and failure-driven recollection across 11 Ground--Relation--Act forms. (2) Anvil-Ben provides scene-aligned supervision for learning diverse embodied spatial capabilities and scene-linked assessments that distinguish stage competence from error propagation. (3) Anvil-MOPD is a 9B student that consolidates heterogeneous spatial knowledge through distillation from specialist teachers. Semantic-first-fault routing targets teacher supervision to the student's earliest decisive failure, while stage normalization controls the loss scale across native outputs of different lengths. We construct 5.8M source-grounded records spanning 160K images, reserving 580K spatial records for held-out evaluation and using the remaining 5.22M records for training. On average across seven public benchmarks, Anvil-MOPD outperforms Qwen3.5-9B and RynnBrain-8B by 9.29 and 11.03 percentage points, respectively, while reaching 80.67% on VABench-Point. Controlled studies support targeted coverage, selective transfer, and feedback-guided repair as complementary framework components.

</details>

---

### [[20_Research/Papers/强化学习/Provably_Efficient_Risk-Sensitive_Offline_Reinforcement_Learning_via_Optimized_Certainty_Equivalents|Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents]]

![[assets/2610.21870_first_page.png|800]]

- **arXiv**: [2610.21870](https://arxiv.org/abs/2610.21870)
- **PDF**: https://arxiv.org/pdf/2610.21870
- **详细分析**: [[20_Research/Papers/强化学习/Provably_Efficient_Risk-Sensitive_Offline_Reinforcement_Learning_via_Optimized_Certainty_Equivalents|Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents]]
- **作者**: Hanzhen Wang, Boxiang Lyu, Zhongxiang Dai, Siyang Gao, Dake Zhang, Shuang Qiu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Provably Efficient Risk-Sensitive Offline Reinforcement Learning via Optimized Certainty Equivalents》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CVaR-RL, OCE-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Risk-sensitive reinforcement learning (RL) addresses decision-making under uncertainty and adverse outcomes. Learning risk-sensitive policies from fixed datasets is important when additional interaction with the environment is costly. Existing work on risk-sensitive RL focuses on online settings or specific risk measures, leaving a general theoretical understanding of its offline setting underdeveloped. In this work, we investigate efficient offline risk-sensitive RL using the optimized certainty equivalent (OCE), a general class of risk measures. We consider two formulations: dynamic-OCE RL, which applies OCE recursively at each step, and static-OCE RL, which applies a single OCE to the cumulative rewards. Under the tabular setting, we develop pessimistic value-iteration algorithms for both formulations and establish tight sublinear suboptimality bounds, explicitly capturing how risk sensitivity, encoded by utility functions, affects learning difficulty. Moreover, we establish minimax suboptimality lower bounds to characterize the problem's fundamental limits. To handle large state spaces, we further develop pessimistic least-squares value-iteration algorithms that incorporate the general OCE risk criterion into linear function approximation. We establish utility-dependent sublinear guarantees with explicit dependence on the feature dimension $d$. To our knowledge, we provide the first offline algorithms along with the first upper and lower suboptimality bounds for both dynamic- and static-OCE RL.

</details>

---

### [[20_Research/Papers/具身智能/Cross-Embodiment_Causal_Transfer_from_Human_Videos_to_Robot_Manipulation|Cross-Embodiment Causal Transfer from Human Videos to Robot Manipulation]]

![[assets/2610.21798_figure.png|800]]

- **arXiv**: [2610.21798](https://arxiv.org/abs/2610.21798)
- **PDF**: https://arxiv.org/pdf/2610.21798
- **详细分析**: [[20_Research/Papers/具身智能/Cross-Embodiment_Causal_Transfer_from_Human_Videos_to_Robot_Manipulation|Cross-Embodiment Causal Transfer from Human Videos to Robot Manipulation]]
- **作者**: Xingyu Zhang, Yingchao Li, Peizheng Guo, Jie Hu, Changwen Zheng, Wenwen Qiang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Cross-Embodiment Causal Transfer from Human Videos to Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRASim, OpenVLA, PlaNet, Real-World, WHIRL, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling robot manipulation models requires large amounts of interaction data, yet collecting diverse real-robot experience remains costly. Human manipulation videos, in contrast, provide abundant and diverse task experience that could potentially benefit robot learning. However, differences in morphology, action spaces, and control mechanisms make human motions unsuitable as direct supervision for robot actions, raising a scientific question: what knowledge in human videos should be transferred across embodiments to robot manipulation? To address this question, we analyze subtask transfer through the lens of causal beams, focusing on which contextual conditions and interaction dependencies should be retained to support local task effects. Based on this perspective, we propose Causal-Beam-Guided Subtask Transfer (CBST). CBST learns manipulation-related representations from human videos and grounds them in task-level semantic variables using robot demonstrations. Within a predefined manipulation model, causal-beam constraints guide contextual information selection by requiring retained assignments to sustain local mechanism outputs while preserving nontrivial responsiveness to retained inputs. The selected semantic information conditions a world-action model, allowing the robot to generate actions from its own observations without requiring human-robot motion correspondence. Experiments on robot manipulation benchmarks show improvements in task success over the corresponding world-action model baselines.

</details>

---

### [[20_Research/Papers/大模型/DeciCAD_Harness-Grounded_Learning_of_Action_Policies_for_CAD_Agents|DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents]]

![[assets/2610.21755_figure.png|800]]

- **arXiv**: [2610.21755](https://arxiv.org/abs/2610.21755)
- **PDF**: https://arxiv.org/pdf/2610.21755
- **详细分析**: [[20_Research/Papers/大模型/DeciCAD_Harness-Grounded_Learning_of_Action_Policies_for_CAD_Agents|DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents]]
- **作者**: Yufeng Peng, Yixin Zhang, Ziyi Liu, Zhikun Xu, Jiarong Yang, Sijie Wang, Wenjie Feng, Qiyu Kang
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.85，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model agents operate through closed-loop action policies whose decision space is defined by an agent harness. We investigate how this operating space shapes agent behavior and policy learning in computer-aided design (CAD), a professional domain characterized by persistent state, geometric constraints, and long-horizon procedures. We instantiate this perspective in DeciCAD, a domain-native harness that exposes semantic CAD actions, decision-oriented observations, environment feedback, and persistent state transitions. Building on this harness, we develop a learning pipeline that extracts causal decision supervision from interaction trajectories and improves the policy through supervised fine-tuning (SFT) and geometry-grounded online reinforcement learning (RL). Across four CAD benchmarks, DeciCAD achieves the best F1 and intersection over union (IoU) while reducing model-output tokens by 45--88% relative to a general-purpose coding harness. Under matched supervision, its SFT policy improves F1 from 0.6883 to 0.7437 and outperforms the coding policy; subsequent online RL further raises geometry availability from 66.5% to 73.5% and F1 to 0.7880. These results demonstrate that the decision space induced by a harness materially affects both agent execution and policy learning in CAD.

</details>

---

### [[20_Research/Papers/大模型/Router_Drift_Control_Mitigating_Off-Policy_Degradation_in_Mixture-of-Experts_Reinforcement_Learning|Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning]]

![[assets/2610.21682_figure.png|800]]

- **arXiv**: [2610.21682](https://arxiv.org/abs/2610.21682)
- **PDF**: https://arxiv.org/pdf/2610.21682
- **详细分析**: [[20_Research/Papers/大模型/Router_Drift_Control_Mitigating_Off-Policy_Degradation_in_Mixture-of-Experts_Reinforcement_Learning|Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning]]
- **作者**: Liangyao Jin, Zhixin Wang, Liming Liu, Mingjun Zhang, Zhengzhou Zhu, Fangcheng Fu, Jinlong Hou, Yuan Cheng, Xiaohe Hu, Ping Zhang, Siyuan Feng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) can become off-policy due to training-inference mismatch, mini-batch updates, and asynchronous training.The resulting mismatch is especially harmful in Mixture-of-Experts (MoE) models, where rollout--training discrepancies can change routing decisions and lead to router drift. Rollout Routing Replay (R3) mitigates this mismatch by reusing expert selections from the rollout stage during training. Our analysis shows that routing replay introduces gradient bias by losing contributions from experts selected by the training router but not the rollout router. To address this, we propose Router Drift Control (RDC), which uses routing disagreement between rollout and training as a signal of off-policy staleness and selectively rejects high-drift responses. The sequence-level filtering avoids gradient bias introduced by replay while preserving native expert selection and the associated learning signals for retained responses. Experiments show that RDC achieves larger gains as policy staleness increases and remains effective in asynchronous RL. In asynchronous training, RDC combined with Truncated Importance Sampling (TIS) improves the average peak validation accuracy across AIME 2024 and AIME 2025 by 5.5 points over TIS and 4.5 points over R3.

</details>

---

### [[20_Research/Papers/具身智能/AVALON_Zero-Shot_Indoor_Navigation_with_Human-Seeded_Topological_Memory|AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory]]

![[assets/2610.21586_figure.png|800]]

- **arXiv**: [2610.21586](https://arxiv.org/abs/2610.21586)
- **PDF**: https://arxiv.org/pdf/2610.21586
- **详细分析**: [[20_Research/Papers/具身智能/AVALON_Zero-Shot_Indoor_Navigation_with_Human-Seeded_Topological_Memory|AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory]]
- **作者**: Jing Xia, Changyan Li, Yuduo Wang, Guiyin Tian, Bo Wang, Yifan Liao, Mingjun Li, Shiyan Hu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《AVALON: Zero-Shot Indoor Navigation with Human-Seeded Topological Memory》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Indoor service robots often enter unmapped buildings whose layouts and task constraints are already familiar to users. We address this human-familiar, robot-unseen setting with AVALON, a topological navigation framework organized around human-seeded layered spatial memory, node-verified topological execution, and task-triggered, evidence-gated human--robot memory co-updating. The robot has no prior on-site traversal or site-specific training. Deployment requires only a floor plan, place clues, and an initial topology-odometry alignment. Visual depth point-goal navigation leverages verified node arrivals to perform translational re-anchoring, without requiring a robot-constructed global SLAM map. Human--robot memory co-updating fuses complementary sources of information. Human operators specify task constraints that are unobservable via vision and report offline environmental modifications, whereas the robot provides physical-state evidence through active in-situ validation. Task relevance governs whether human-reported environmental changes undergo robot validation during the active mission. Field-collected perceptual evidence gates memory updates, maintaining an explicit separation between human-specified permissions and robot-observed traversability. Our experiments on a Unitree Go2 show that AVALON with X-NavDP completes a 12.81 m Intersection-to-Dining mission in 46.4 s (5/5) with no mapping, 40.9% less robot time than DimOS-Go2 (78.5 s, 4/5), while policy-only X-NavDP times out in all of the 5 runs. These demonstrate the superiority of the proposed topological navigation framework.

</details>

---

### [[20_Research/Papers/大模型/ISW-Agent_Integrating_LLM-Driven_Dialogue_with_n8n_Workflow_for_Internal_Solitary_Wave_Remote_Sensing_Image_Processing|ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing]]

![[assets/2610.21502_figure.png|800]]

- **arXiv**: [2610.21502](https://arxiv.org/abs/2610.21502)
- **PDF**: https://arxiv.org/pdf/2610.21502
- **详细分析**: [[20_Research/Papers/大模型/ISW-Agent_Integrating_LLM-Driven_Dialogue_with_n8n_Workflow_for_Internal_Solitary_Wave_Remote_Sensing_Image_Processing|ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing]]
- **作者**: Hao Zhang, Hengrui Liu, Lina Sun, Junmin Meng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IWE-Net, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Internal solitary wave (ISW) remote sensing requires task parameters and spatial information to be transferred across image acquisition, detection, stripe extraction, and propagation prediction. Here, we present ISW-Agent, which integrates large language model (LLM) interpretation with n8n workflows and independent scientific models through structured task constraints, geospatial transformations, and stage-specific output validation. In tests of 120 Chinese instructions per backend, GPT-5.6 Sol and DeepSeek both achieved a strict task-match rate of 94.2%, with all intents and execution decisions matching the reference. Sentinel-1 cases demonstrated continuous processing from dialogue requests to wavefront prediction for the specified scene. Of 50 timed scenes, 39 completed detection, extraction, and prediction with a median turnaround time of 48.04 s; 11 stopped after empty extraction. Across 3,408 controlled fault-injection runs, retries recovered 234 transient-failure conditions and output validation rejected 234 structural defects, while 61 provenance or completeness errors indicated the need for content-consistency checks. Overall, ISW-Agent thus connects natural-language requests to traceable spatial processing chains for multimodel ISW analysis.

</details>

---

### [[20_Research/Papers/大模型/Incentivizing_Tool-Use_Reinforcement_Learning_for_Post-Arrival_Emergency_Care_Prediction|Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction]]

![[assets/2610.21449_figure.png|800]]

- **arXiv**: [2610.21449](https://arxiv.org/abs/2610.21449)
- **PDF**: https://arxiv.org/pdf/2610.21449
- **详细分析**: [[20_Research/Papers/大模型/Incentivizing_Tool-Use_Reinforcement_Learning_for_Post-Arrival_Emergency_Care_Prediction|Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction]]
- **作者**: Pengfei Hu, Chenwei Wu, Qiao Jin, Jun Deng, Zhiyong Lu, Liyue Shen, Yue Ning
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) can reason over both structured measurements and free-text records, which makes them attractive for emergency department (ED) prediction. However, most existing LLMs still fall short of conventional ML methods like trees on EHR-based prediction tasks. Our controlled analysis traces this gap to two weaknesses: LLMs do not select informative features, and they misjudge what numerical values imply for risk even when given the right features. We propose TIR-EC, a tool-integrated reinforcement learning framework that addresses both. TIR-EC exposes EHR feature groups as tools the LLM can call. It trains the LLM with rewards from a gradient-boosted tree teacher, which provides a reference set of informative tools and a graded risk target. TIR-EC also distills task-specific clinical skills into the model weights through a reverse curriculum that gradually removes the skills from the prompt during RL process. Evaluation on three clinical prediction tasks shows that our 4B agent achieves the highest macro F1 of all compared models, outperforms conventional ML baselines, and is competitive with much larger frontier LLMs. Further analysis shows that TIR-EC selects more useful evidence with fewer tool calls and combines measurements more effectively.

</details>

---

### [[20_Research/Papers/大模型/MemCut_Every_Secret_Leaves_a_Trail_in_the_Long-Term_Memory_of_LLM_Agents|MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents]]

![[assets/2610.21405_figure.png|800]]

- **arXiv**: [2610.21405](https://arxiv.org/abs/2610.21405)
- **PDF**: https://arxiv.org/pdf/2610.21405
- **详细分析**: [[20_Research/Papers/大模型/MemCut_Every_Secret_Leaves_a_Trail_in_the_Long-Term_Memory_of_LLM_Agents|MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents]]
- **作者**: Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ForgetEval, LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this capability, we introduce MemCut, a systematic benchmark for user-requested forgetting. Its 456 hand-designed secrets in long-horizon conversations have fully annotated evidence trails to test recovery after deletion, including from messages that never state the secrets directly. We propose two recovery metrics. Native recovery measures reader success through the system's retrieval, whereas residual recovery measures the same reader's success when directly given surviving objects traced to annotated disclosures or evidence. We establish three reference deletion baselines to test how far existing retrievers and write models support forgetting across five memory designs and four LLMs. Disclosure removal reduces native recovery far more than residual recovery. LLM-guided deletion of ten additional turns from twenty retrieval candidates leaves 39-76% residual recovery. Subset sweeps (144 facts, three systems, two models) show that widening the pool at a fixed budget reduces residual recovery more than deleting all original candidates. These sweeps identify candidate coverage as a bottleneck in the reference baselines.

</details>

---

### [[20_Research/Papers/具身智能/LTM_Latent_Transition_Based_In-Context_Memory_for_Vision-Language-Action_Models|LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models]]

![[assets/2610.21362_figure.png|800]]

- **arXiv**: [2610.21362](https://arxiv.org/abs/2610.21362)
- **PDF**: https://arxiv.org/pdf/2610.21362
- **详细分析**: [[20_Research/Papers/具身智能/LTM_Latent_Transition_Based_In-Context_Memory_for_Vision-Language-Action_Models|LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models]]
- **作者**: Qixin Sun, WenLong Gao, Xiansheng Chen, Zhongyuan Wang, Si Liu, Pengwei Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LTM: Latent Transition Based In-Context Memory for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HiF-VLA, LaMem-VLA, LingBot-VLA, MemoryVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation often requires remembering interactions that are no longer visible. We introduce Latent Transition Memory (LTM), which stores history as compact latent transitions between consecutive observations. Instantiated on $π_{0.5}$ as LTM-$π$, our method uses a frozen latent action encoder, a lightweight adapter, and causal KV caching for incremental inference without memory-specific semantic annotations or external reasoning-model calls. With DreamDojo transitions, LTM-$π$ achieves 58.54% success on RoboMME and 80.5% on LIBERO-Mem, performing best among baselines without external reasoning models or memory-specific annotations. Ablations support the contribution of transition content beyond temporal cues and the efficiency of delayed memory admission. Scaling RoboMME demonstrations tenfold improves success from 57.67% to 87.50%, while a Cup Swap diagnostic highlights the role of process supervision in temporal composition. Under a 200-token memory budget, success remains 84.00%, versus 87.50% without compression. Finally, real-robot counting success improves from 11.25% to 82.50%. Together, these results demonstrate the effectiveness, scalability, and efficiency of latent transition memory, highlighting its capacity for complex temporal information, bounded-context operation, and real-world robotic control.

</details>

---

### [[20_Research/Papers/强化学习/Constrained_Multi-Agent_Reinforcement_Learning_in_Imagination|Constrained Multi-Agent Reinforcement Learning in Imagination]]

![[assets/2610.21319_figure.png|800]]

- **arXiv**: [2610.21319](https://arxiv.org/abs/2610.21319)
- **PDF**: https://arxiv.org/pdf/2610.21319
- **详细分析**: [[20_Research/Papers/强化学习/Constrained_Multi-Agent_Reinforcement_Learning_in_Imagination|Constrained Multi-Agent Reinforcement Learning in Imagination]]
- **作者**: Raz Shmueli, Shahaf S. Shperberg
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.6，世界模型 0.2）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Constrained Multi-Agent Reinforcement Learning in Imagination》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting cost in a multi-agent world model moves most constrained policy updates into imagination: the stronger model-free baseline needs $10$ to $20$ times CA-MAMBA's interactions on the median SMAC configuration, and CA-MAMBA earns $2.8$ to $12$ times the baselines' MAMuJoCo reward at equal budget. In controlled tests on one task per benchmark, pricing the model's cost advantages at parity more than halves a cost-blind learner's cost and meets a tight continuous-control limit the learned multiplier misses, suggesting the model's cost estimates are not the bottleneck.

</details>

---

### [[20_Research/Papers/大模型/Loud_and_Clear_Making_Visual_Evidence_Count_in_Multimodal_Document_RAG|Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG]]

![[assets/2610.21318_figure.png|800]]

- **arXiv**: [2610.21318](https://arxiv.org/abs/2610.21318)
- **PDF**: https://arxiv.org/pdf/2610.21318
- **详细分析**: [[20_Research/Papers/大模型/Loud_and_Clear_Making_Visual_Evidence_Count_in_Multimodal_Document_RAG|Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG]]
- **作者**: Eunchan Jo, Seounghyun Jang, Sangwoo Mo
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Loud and Clear: Making Visual Evidence Count in Multimodal Document RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MDocRAG-RL, MMLongBench, SciEGQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal document retrieval-augmented generation (RAG) has focused largely on retrieval, yet its answers depend on how well a vision-language model reads the retrieved pages. We find that evidence in retrieved pages remains underused even when the correct pages are retrieved. On SciEGQA oracle pages, five prior methods give the generator 0.7K to 2.7K visual tokens per query on average under a common image processor, yet raising the page-only budget from 1K to 32K improves accuracy by 15.22 points. At a fixed 16K budget, adding ground-truth crops improves accuracy by 3.75 points over page-only input. We study what the generator needs from retrieved pages through two requirements: Loud, making full use of visual token capacity, and Clear, refining the page so that its evidence becomes prominent. For Loud, increasing either the visual token budget or visual fidelity, the image resolution those tokens preserve, improves accuracy with the other held fixed, and full-page scaling outperforms repetition and tiling at matched budgets. For Clear, suppressing surrounding content improves accuracy without enlarging selected regions, and adding OCR of these regions to page images outperforms either input alone. We implement both as Loud and Clear (LoC), which combines higher-resolution pages with OCR from query-relevant regions without ground-truth annotations or additional training. LoC outperforms eight prior methods on SciEGQA, ViDoRe-v3, and MMLongBench-Doc, improving over the strongest, ColQwen3, by 8.88, 3.09, and 4.22 points with the same retriever and generator. It also outperforms its page-only variant under the same visual token budget. These results locate a bottleneck beyond retrieval: how the retrieved pages are given to the generator.

</details>

---

### [[20_Research/Papers/强化学习/All-in-One_Memory_Process-Rewarded_Reinforcement_Learning_for_Memory_Agents|All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents]]

![[assets/2610.21147_figure.png|800]]

- **arXiv**: [2610.21147](https://arxiv.org/abs/2610.21147)
- **PDF**: https://arxiv.org/pdf/2610.21147
- **详细分析**: [[20_Research/Papers/强化学习/All-in-One_Memory_Process-Rewarded_Reinforcement_Learning_for_Memory_Agents|All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents]]
- **作者**: Bingbing Wang, Jingjie Lin, Weiming Qiao, Jing Li, Ruifeng Xu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models increasingly rely on external memory to answer queries grounded in long-horizon histories such as multi-session dialogues and lengthy documents. However, existing memory methods often optimize retrieval and memory construction separately, without a shared reward space for evaluating search, writing, and stopping decisions. To address this, we propose All-in-One Memory (AiO-Mem), which organizes these operations as transitions over a shared evidence state and directly evaluates the semantic quality of each action in a unified reward space. AiO-Mem compiles heterogeneous histories into source-traceable multi-view events, providing a shared substrate for retrieval and memory writing. A unified memory policy actor then rolls out complete interaction trajectories over this shared evidence state. A separate trajectory-conditioned process reward model is trained through evidence-grounded supervised fine-tuning and trajectory-level DPO to assign process scores to the collected trajectories. These scores are aggregated into an action-balanced trajectory reward and used by Process-Aligned DAPO (PA-DAPO) to optimize the memory policy. Across long-context memory benchmarks, AiO-Mem consistently improves answer accuracy over both static memory systems and RL-trained memory agents.

</details>

---

### [[20_Research/Papers/大模型/SSR_Structural_Signal_Retriever_for_Scalable_Agent_Discovery_in_LLM-Orchestrated_Multi-Agent_Systems|SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems]]

![[assets/2610.21113_figure.png|800]]

- **arXiv**: [2610.21113](https://arxiv.org/abs/2610.21113)
- **PDF**: https://arxiv.org/pdf/2610.21113
- **详细分析**: [[20_Research/Papers/大模型/SSR_Structural_Signal_Retriever_for_Scalable_Agent_Discovery_in_LLM-Orchestrated_Multi-Agent_Systems|SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems]]
- **作者**: Giancarlo Maldonado Cárdenas, Carlos A. Astudillo, Nelson L. S. da Fonseca
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SSR-AgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale multi-agent ecosystems require mechanisms for discovering suitable agents without exposing entire registries to a large language model (LLM) orchestrator. The challenge is not only to retrieve relevant Agent Cards from a growing registry, but also to maintain a compact candidate context, since each additional candidate increases prompt size, inference cost, latency, and the risk of exceeding the model context window. We formulate this problem as candidate-context scalability and propose the Structural Signal Retriever (SSR), our deterministic and training-free retrieval method designed for Agent Card discovery. SSR derives structural lexical signals from capability-bearing Agent Card fields, weights them using inverse document frequency (IDF), and uses an Inverted Signal Index (ISI) for selective candidate scoring. We evaluate SSR using a synthetic agent benchmark, a public MS MARCO adaptation, and end-to-end LLM orchestration. At 1,000 agents, SSR reduces LLM input by 98.8% and orchestration latency by 70.9% relative to full-catalog orchestration. On MS MARCO, IDF improves retrieval effectiveness within the structural representation, while the ISI preserves retrieval effectiveness and reduces explicitly scored passages by 96.8%. End-to-end experiments show that candidate pre-selection maintains a compact candidate context as registry size grows and avoids the operational failures observed with full-catalog orchestration. These results support SSR as an Agent-Card-native, traceable retrieval mechanism for candidate-context scalability.

</details>

---

### [[20_Research/Papers/大模型/MemComposer_Learning_to_Assemble_Memories_for_LLM_Agents_via_Reinforcement_Learning|MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning]]

![[assets/2610.21091_figure.png|800]]

- **arXiv**: [2610.21091](https://arxiv.org/abs/2610.21091)
- **PDF**: https://arxiv.org/pdf/2610.21091
- **详细分析**: [[20_Research/Papers/大模型/MemComposer_Learning_to_Assemble_Memories_for_LLM_Agents_via_Reinforcement_Learning|MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning]]
- **作者**: Yixuan Xie, Xueqiang Xu, Xinyi Fan, Xinxi Lyu, Tao Feng, Xing Fan, Chenlei Guo, Jie Hao, Shaowen Wang, Jiashuo Sun, Jiawei Han
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 2.05（加权：大模型 1.25，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent memory enables large language model (LLM) agents to reuse past experiences without updating their parameters. However, semantic similarity alone does not guarantee memory usefulness: downstream performance depends on how memories are selected and presented to the agent. We propose MemComposer, a memory composer that jointly examines the current query and retrieved candidates to decide which experiences to include, how many to select, and how to order them. We train the composer using Experience Policy Optimization (ExPO), a GRPO-based framework that evaluates assembled memory contexts through complete agent interactions and uses task-success feedback to optimize the assembly policy. Across three $τ^2$-bench domains with two frozen executors, MemComposer outperforms the strongest baseline for each executor while reducing average memory-token usage by 16.9% and 4.9%, respectively. The learned policy also transfers to unseen domains, executors, and memory banks, and benefits from memories generated by stronger models without further training. These results demonstrate the value of learning query-specific memory assembly using downstream task feedback.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_HPC_Job_Scheduling_A_Statistical_Evaluation|Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation]]

![[assets/2610.21008_first_page.png|800]]

- **arXiv**: [2610.21008](https://arxiv.org/abs/2610.21008)
- **PDF**: https://arxiv.org/pdf/2610.21008
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_HPC_Job_Scheduling_A_Statistical_Evaluation|Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation]]
- **作者**: Justin M. Cheney, Clement N. Nyirenda
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 2.0（加权：强化学习 2）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, HPCSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Reinforcement Learning (DRL) offers learned job selection for High-Performance Computing (HPC), but performance against heuristics alone does not establish value beyond action masking. Six DRL treatments are compared: Proximal Policy Optimization (PPO), Advantage Actor-Critic (A2C), and Deep Q-Network (DQN), each with and without masking. Three heuristics and a seed-paired masked uniform random control provide baselines across ten seeds on two real Slurm (Simple Linux Utility for Resource Management) workload traces, one homogeneous and one heterogeneous, under a common non-parametric framework. All masked treatments complete evaluation, whereas unmasked treatments are truncated. On the homogeneous trace, no masked DRL treatment significantly improves average waiting time or average and maximum bounded slowdown over the control. On the heterogeneous trace, MaskablePPO improves all three metrics relative to the control. Its average waiting time is equivalent to that of the three heuristics within a 10% margin, and its maximum bounded slowdown is 22% lower than that of Last-Come, First-Served (LCFS). MaskablePPO has the leading average waiting-time rank among complete treatments on both traces, but Nemenyi comparisons detect no significant difference from MaskableA2C. Among masked variants, MaskablePPO has the lowest recorded mean training time, while MaskableDQN has the lowest mean decision latency. These findings distinguish completion from baseline-specific scheduling gains and support including a masked random control when assessing the value of learned selection.

</details>

---

### [[20_Research/Papers/具身智能/SOMA_Stack-of-Objects_Manipulation_using_a_Quadruped_Robot|SOMA: Stack-of-Objects Manipulation using a Quadruped Robot]]

![[assets/2610.20968_figure.png|800]]

- **arXiv**: [2610.20968](https://arxiv.org/abs/2610.20968)
- **PDF**: https://arxiv.org/pdf/2610.20968
- **详细分析**: [[20_Research/Papers/具身智能/SOMA_Stack-of-Objects_Manipulation_using_a_Quadruped_Robot|SOMA: Stack-of-Objects Manipulation using a Quadruped Robot]]
- **作者**: Stergios E. Bachoumas, Panagiotis Artemiadis
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.1，强化学习 0.2，机器人 1.9）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《SOMA: Stack-of-Objects Manipulation using a Quadruped Robot》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Executing heavy-duty physical manipulation in unpredictable environments remains a major challenge for quadrupedal robots lacking dedicated manipulators. This paper presents SOMA, a hierarchical reinforcement learning framework for whole-body non-prehensile manipulation of multi-object stacks using a quadruped robot. Unlike traditional methods restricted to two-dimensional planar pushing, SOMA integrates explicit robot base-height control, unlocking full three-dimensional pushing strategies. This capability enables the quadruped to manipulate complex payload stacks as a unified system while preventing relative sliding or tipping of upper layers. The architecture factorizes control into a high-level manipulation policy using a Simplified Structured State Space Sequence (S5) encoder to reason over long-horizon temporal history and predict bounded target tracking commands via Beta distributions, and a low-level locomotion policy that dynamically adapts leg stance configurations. In extensive simulation benchmarks, SOMA achieves a $90.3\%$ success rate for single-object reposing and up to $90.1\%$ for dynamic two-box stacks under stringent error margins ($0.05\text{ m}$ position error, $1^\circ$ orientation error). Finally, we validate zero-shot sim-to-real transfer on a Unitree Go1 quadruped robot across diverse payload masses and geometries, demonstrating active base-height adjustments to maintain traction and balance during heavy pushing tasks.

</details>

---

### [[20_Research/Papers/具身智能/TGrasp6D_Task-Informed_Vision-Language_Priors_and_Pose_Refinement_enable_Zero-Shot_Task-Oriented_6DoF_Grasping|TGrasp6D: Task-Informed Vision-Language Priors and Pose Refinement enable Zero-Shot Task-Oriented 6DoF Grasping]]

![[assets/2610.20901_figure.png|800]]

- **arXiv**: [2610.20901](https://arxiv.org/abs/2610.20901)
- **PDF**: https://arxiv.org/pdf/2610.20901
- **详细分析**: [[20_Research/Papers/具身智能/TGrasp6D_Task-Informed_Vision-Language_Priors_and_Pose_Refinement_enable_Zero-Shot_Task-Oriented_6DoF_Grasping|TGrasp6D: Task-Informed Vision-Language Priors and Pose Refinement enable Zero-Shot Task-Oriented 6DoF Grasping]]
- **作者**: Manav Kulshrestha, Apoorva Vashisth, Damon Conover, Aniket Bera
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《TGrasp6D: Task-Informed Vision-Language Priors and Pose Refinement enable Zero-Shot Task-Oriented 6DoF Grasping》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-Oriented Grasping (TOG) has emerged as an important skill for purposeful robotic manipulation. Given the task of using a knife to "slice bread," a robot must choose to grasp from the handle, whereas for "hand[ing] the knife over," it is preferable for the handle to remain unobstructed for safe handoff. Current approaches for TOG either focus on 2D planar grasping, remain limited by their reliance on task-agnostic grasp generators, or are constrained by reliance on finite, manually-annotated, task-specific grasp datasets that cannot cover all possible grasp-task pairs. To that end, we present TGrasp6D, a vision-language based approach for generating task-oriented 6DoF grasps in a zero-shot manner. Given a task and a single RGB-D image of an associated object, TGrasp6D reasons about the appropriate semantic affordance for the given task and object geometry to produce an initial task- informed prior. This generated prior is further refined via 6DoF pose optimization for collision avoidance while preserving task consistency. Our approach achieves state-of-the-art success rate of 94% on the TaskGrasp dataset, with the best baseline at 74%. We also deploy our approach on a Franka Research 3 robot to demonstrate zero-shot generalization to real world objects

</details>

---
