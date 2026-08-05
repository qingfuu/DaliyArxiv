# cs.AI | Artificial Intelligence | 2026-08-03

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/大模型/AgentHPOBench_A_Benchmark_For_Evaluating_LLM_Agents_as_Sequential_Hyperparameter_Optimizers|AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers]]

![[assets/2607.29626_first_page.png|800]]

- **arXiv**: [2607.29626](https://arxiv.org/abs/2607.29626)
- **PDF**: https://arxiv.org/pdf/2607.29626
- **详细分析**: [[20_Research/Papers/大模型/AgentHPOBench_A_Benchmark_For_Evaluating_LLM_Agents_as_Sequential_Hyperparameter_Optimizers|AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers]]
- **作者**: Tianyu Huai, Tingshuo Fan, Xinchi Chen, Yining Zheng, Yuxin Wang, Shuang Chen, Jie Zhou, Xuanjing Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentHPOBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions. To address this gap, we introduce AgentHPOBench, a sequential benchmark comprising 30 executable machine learning tasks across seven research categories. Each task begins with a validated baseline run, after which an agent performs several sequential interventions. At each step, the agent observes the accumulated configurations, metrics, and logs before proposing the next valid configuration. We evaluate 12 widely used agents and conventional HPO baselines under a unified protocol. The results show that current agents exhibit measurable experimental optimization ability across domains, but still face clear limitations in sustained iterative refinement, complex log diagnosis, and consistent progress toward reported reference performance.

</details>

---

### [[20_Research/Papers/强化学习/LEMUR_Learning_to_Align_with_Multi-Objective_Reinforcement_Learning_from_Preference_Feedback|LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback]]

![[assets/2607.29559_figure.png|800]]

- **arXiv**: [2607.29559](https://arxiv.org/abs/2607.29559)
- **PDF**: https://arxiv.org/pdf/2607.29559
- **详细分析**: [[20_Research/Papers/强化学习/LEMUR_Learning_to_Align_with_Multi-Objective_Reinforcement_Learning_from_Preference_Feedback|LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback]]
- **作者**: Manith Adikari, Bei Peng, Samuele Vinanzi, Angelo Cangelosi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FPbRL, MO-MetaWorld, MORL, PbMORL, PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) systems are typically trained using a single, well-specified scalar reward function. However, real-world decision-making tasks often involve multiple, competing objectives, such as performance versus efficiency, where ground-truth reward functions are difficult to specify or inaccessible. While Multi-Objective RL (MORL) addresses such trade-offs by modeling rewards as vectors, existing approaches typically assume access to a well-specified reward function for each objective, inheriting the same challenges faced by single-objective RL. Meanwhile, Preference-based RL (PbRL) has shown great potential in solving complex tasks without access to a pre-defined reward function through reward learning from human feedback, yet has largely been studied in single-objective settings. In this work, we bridge this gap with LEMUR: Learning to Align with Multi-Objective Reinforcement Learning with Preference feedback, a novel framework where an agent interactively learns from the preferences of multiple humans to learn optimal multi-objective policies. Our approach jointly learns policies and multiple objective-specific reward models from human feedback, enabling agents to effectively balance competing objectives during learning. We evaluate LEMUR on a variety of benchmark multi-objective tasks, and empirical results demonstrate its superior performance over baseline methods. Our method presents a promising direction for solving multi-objective decision-making tasks without pre-defined reward functions.

</details>

---

### [[20_Research/Papers/强化学习/DreamQAS_Learning_a_Decision-Useful_World_Model_for_VQE-Efficient_Quantum_Architecture_Search|DreamQAS: Learning a Decision-Useful World Model for VQE-Efficient Quantum Architecture Search]]

![[assets/2607.29491_figure.png|800]]

- **arXiv**: [2607.29491](https://arxiv.org/abs/2607.29491)
- **PDF**: https://arxiv.org/pdf/2607.29491
- **详细分析**: [[20_Research/Papers/强化学习/DreamQAS_Learning_a_Decision-Useful_World_Model_for_VQE-Efficient_Quantum_Architecture_Search|DreamQAS: Learning a Decision-Useful World Model for VQE-Efficient Quantum Architecture Search]]
- **作者**: Jiayang Niu, Yan Wang, Jie Li, Ke Deng, Azadeh Alavi, Muhammad Usman, Yongli Ren
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《DreamQAS: Learning a Decision-Useful World Model for VQE-Efficient Quantum Architecture Search》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement-learning-based quantum architecture search (RL-QAS) repeatedly optimizes a variational quantum eigensolver (VQE) after extending a circuit, although circuit construction and action legality are deterministic and known. We introduce DreamQAS, a model-based RL framework that preserves these exact circuit dynamics and learns only the expensive post-VQE feedback. A recurrent randomized-prior ensemble predicts an oracle-free score relative to an empirical energy frontier and supports multi-step imagined policy learning over explicit legal circuits. Ranking-based activation, uncertainty-aware pessimism and truncation, and selective real-VQE verification form a reliability-controlled learning loop. Under a common 15,000-episode budget and frozen evaluation for the RL methods, DreamQAS has the lowest mean frozen-policy energy error on four of five molecular tasks and the second-lowest on one. At fine-error targets reached by all seeds of both methods, it uses 1.6x to 2.0x fewer real VQE calls on four tasks and 10.6x fewer on BeH2-8q. Counterfactual action-ranking utility increases across all five tasks, with a mean increase of 0.346 and a 95 percent confidence interval of [0.185, 0.507], while direct greedy and beam use of the same model does not recover the gains of imagined policy learning. Ensemble disagreement also improves risk-coverage over random rejection on all three probed tasks. These results establish a world-model design for QAS whose value lies in decision-useful feedback rather than exact energy prediction.

</details>

---

### [[20_Research/Papers/强化学习/Self-Play_Meets_Skill_Evolution_Self-Evolving_Search_Agents_that_Pose,_Solve,_and_Remember|Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember]]

![[assets/2607.29468_figure.png|800]]

- **arXiv**: [2607.29468](https://arxiv.org/abs/2607.29468)
- **PDF**: https://arxiv.org/pdf/2607.29468
- **详细分析**: [[20_Research/Papers/强化学习/Self-Play_Meets_Skill_Evolution_Self-Evolving_Search_Agents_that_Pose,_Solve,_and_Remember|Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember]]
- **作者**: Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Haoyu Wu, Minghui Wu, Chenxu Zhao, Ante Wang, Guannan He, Changwei Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-play agents can generate training problems without questions from target benchmarks, but their curricula lack persistent state: failures affect gradients yet do not explicitly shape future practice. External skill memories preserve procedural experience but are typically learned from fixed task distributions. We introduce \textbf{SESA} (Self-Evolving Skill-Augmented Agent), which makes procedural memory an evolving state of tool-augmented search self-play. A challenger poses problems, while a separately parameterized solver alone retrieves skills. Informative failures are distilled into reusable skills and written back to memory. The updated memory changes solver behavior and success, which changes the challenger's reward and the distribution of future problems; the resulting frontier produces new failures that rewrite memory. This bidirectional loop makes task generation and skill memory co-evolve. Because retrieved skills shape on-policy training trajectories, their benefits can enter the model parameters as well as remain in the external bank, enabling memory-free deployment and optional inference-time retrieval. Across seven open-domain and multi-hop question-answering benchmarks, SESA improves average accuracy over SSP by 1.2--3.2 points across multiple backbones and surpasses the skill-augmented SkillRL baseline by 0.9 points under a unified evaluation protocol. On Qwen3 models, SESA-Off retains 1.8--2.2 points of improvement over SSP, while the final skill bank adds a further 0.5--1.0 points. These results show that evolving skill memory is not merely an inference-time plug-in: it changes policy learning and the future training distribution while retaining value as optional external memory. Our code is available at https://github.com/Zenghuang-Fu/SESA-Self-Evolving-Search-Agents.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Retrieval_Analytic_Memory_for_Multimodal_Agents|Beyond Retrieval: Analytic Memory for Multimodal Agents]]

![[assets/2607.29440_figure.png|800]]

- **arXiv**: [2607.29440](https://arxiv.org/abs/2607.29440)
- **PDF**: https://arxiv.org/pdf/2607.29440
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Retrieval_Analytic_Memory_for_Multimodal_Agents|Beyond Retrieval: Analytic Memory for Multimodal Agents]]
- **作者**: Zhoujin Tian, Yao Tian, Hao Zhang, Cheng Chen, Yakun Li, Lei Zhang, Xiaofang Zhou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Beyond Retrieval: Analytic Memory for Multimodal Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions. Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant information at multiple granularities, from high-level abstractions to underlying records. In this paper, we formulate \emph{analytic memory} as a complementary abstraction that organizes recurring multimodal observations into queryable structures supporting filtering, aggregation, ranking, and temporal comparison. We present AdaMM, a framework that jointly supports retrieval and analytic memory. Rather than relying on application-defined schemas, AdaMM extracts provenance-linked attribute-value observations from dialogue, images, and contextual metadata, discovers recurring field structures, and materializes them for analytical access. At inference time, a memory-aware planner decomposes queries into retrieval and analytic operations and routes each operation to the appropriate tools. Experiments on two long-term multimodal memory benchmarks, MemEye and MemGallery, show that AdaMM improves performance by up to 11.3\% and 7.3\%, respectively.

</details>

---

### [[20_Research/Papers/强化学习/Explore_Beyond_the_Boundary_Using_Entropic_Information|Explore Beyond the Boundary Using Entropic Information]]

![[assets/2607.29419_figure.png|800]]

- **arXiv**: [2607.29419](https://arxiv.org/abs/2607.29419)
- **PDF**: https://arxiv.org/pdf/2607.29419
- **详细分析**: [[20_Research/Papers/强化学习/Explore_Beyond_the_Boundary_Using_Entropic_Information|Explore Beyond the Boundary Using Entropic Information]]
- **作者**: Bumgeun Park, Donghwan Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Explore Beyond the Boundary Using Entropic Information》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In reinforcement learning, exploration with sparse and delayed rewards presents a significant challenge due to the limited feedback available for guiding the learning process. Addressing this issue requires extensive exploration in the state space to discover valuable reward signals. In this paper, we propose Entropic Information for Exploration (ENTINEX), a novel method that enhances exploration by incentivizing agents to explore beyond the boundaries of the state distribution. ENTINEX achieves this by assigning intrinsic rewards to these boundaries, leveraging entropic information to identify them effectively. Through extensive experimentation, we demonstrate that ENTINEX consistently improves exploration performance in environments characterized by sparse and delayed rewards. Our experimental results show that ENTINEX outperforms existing exploration methods, highlighting its effectiveness in both sparse and delayed reward scenarios.

</details>

---

### [[20_Research/Papers/大模型/SeekBrain_An_Autonomous_Multi-Agent_System_for_Accelerating_Neuroscience_Discovery|SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery]]

![[assets/2607.29347_figure.png|800]]

- **arXiv**: [2607.29347](https://arxiv.org/abs/2607.29347)
- **PDF**: https://arxiv.org/pdf/2607.29347
- **详细分析**: [[20_Research/Papers/大模型/SeekBrain_An_Autonomous_Multi-Agent_System_for_Accelerating_Neuroscience_Discovery|SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery]]
- **作者**: Jiamin Wu, Peishan Xiang, Jingyang Chen, Yuqing Zhu, Yuxi Li, Ling Luo, Qihao Zheng, Jialiang Zu, Yongchao Wu, Mindong Liu, Haitao Wu, Chaofan Hu...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《SeekBrain: An Autonomous Multi-Agent System for Accelerating Neuroscience Discovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern neuroscience relies on integrating multi-scale, multimodal datasets to uncover the neural principles underlying intelligence. However, analytical challenges posed by highly heterogeneous data and fragmented workflows increasingly constrain discoveries. Here we introduce SeekBrain, an autonomous multi-agent framework designed to accelerate neuroscience discovery through domain-grounded hierarchical planning and cross-modal data analysis. SeekBrain dynamically constructs a repertoire of analysis recipes extracted from code-paper pairs. By coupling this codified expertise with agentic planning and execution engines, the framework scalably generates hypotheses and analytical pipelines on demand. Systematic evaluation on the expert-annotated BrainArena benchmark demonstrates that SeekBrain substantially outperforms state-of-the-art agent baselines across various analysis tasks. Crucially, when deployed in real-world research, SeekBrain integrated behavioral, neural, and anatomical data to reveal structured, distributed neural representations of larval zebrafish behavior and a shared axis of regional decoding strength across the brain in a mouse decision-making task. These results establish SeekBrain as a scalable and practical tool for accelerating data-driven discoveries in neuroscience.

</details>

---

### [[20_Research/Papers/强化学习/MAGA_Multi-Platform_Self-Fusion_of_GUI_Agents_via_Structured_Action_Distillation|MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation]]

![[assets/2607.29320_figure.png|800]]

- **arXiv**: [2607.29320](https://arxiv.org/abs/2607.29320)
- **PDF**: https://arxiv.org/pdf/2607.29320
- **详细分析**: [[20_Research/Papers/强化学习/MAGA_Multi-Platform_Self-Fusion_of_GUI_Agents_via_Structured_Action_Distillation|MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation]]
- **作者**: Hang Yan, Zhangxuan GU, Beitong Zhou, Jiaxuan Chen, Runze Li, Yusong Hu, Shuheng Shen, Changhua Meng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MobileWorld, OSWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graphical user interface (GUI) agents based on large language models are increasingly deployed across mobile, web, and desktop environments. However, existing agents are typically domain-specific, limiting the deployment and user experience. This motivates the consolidation of specialized models into a single cross-environment policy. Weight merging directly merges domain-specific experts but can corrupt executable actions under expert disagreement, while on-policy distillation (OPD) avoids conflicting teacher supervision yet still treats all response tokens equally during distillation, ignoring that action tokens are the only interface between the environment and the agent. To address this, We introduce MAGA that re-allocates training signal according to the structured action. Based on the correctness of the generated action, it suppresses unnecessary or invalid distillation signals and focuses learning on erroneous actions. Besides, a training-only hint optimizes the supervision signal provided by domain-specific teachers without changing the student input. Across two model scales, MAGA achieves the highest mean success rate, outperforming the strongest baseline by 2.0% at 8B and achieves almost the same average performance with teachers.

</details>

---

### [[20_Research/Papers/强化学习/Translation_with_Thought_Difficulty-Adaptive_Reasoning_via_Reinforcement_Learning_for_Multi-Domain_Machine_Translation|Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation]]

![[assets/2607.29287_figure.png|800]]

- **arXiv**: [2607.29287](https://arxiv.org/abs/2607.29287)
- **PDF**: https://arxiv.org/pdf/2607.29287
- **详细分析**: [[20_Research/Papers/强化学习/Translation_with_Thought_Difficulty-Adaptive_Reasoning_via_Reinforcement_Learning_for_Multi-Domain_Machine_Translation|Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation]]
- **作者**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement Learning for Multi-Domain Machine Translation》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-domain machine translation (MDMT) poses a unique challenge due to varying levels of linguistic complexity across domains. Inspired by human translators' ability to adapt reasoning effort based on difficulty, we propose TwT (Translation with Thought), a resource-rational framework that learns to modulate inference between intuitive and deliberate reasoning. TwT is trained in two stages: (1) supervised fine-tuning on difficulty-aware long chain-of-thought traces distilled from DeepSeek-R1 and rewritten by GPT-4o to reflect human-like reasoning economy, and (2) reinforcement learning with a hybrid reward to optimize translation quality and reasoning efficiency. Evaluated on 15 benchmarks spanning in-domain and out-of-domain settings, as well as 3 seen and 59 unseen languages, with ablations across three backbone models, TwT-7B and TwT-14B outperform much larger SOTA reasoning models in translation quality, while reducing token usage by 32--60\%. These results confirm that aligning translation behavior with cognitive principles enables robust generalization, high translation quality, and efficient reasoning in MDMT.

</details>

---

### [[20_Research/Papers/其他/Tool_Specifications_Matter_Uncovering_and_Mitigating_Safety_Risks_in_AI_Agents|Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents]]

![[assets/2607.29254_figure.png|800]]

- **arXiv**: [2607.29254](https://arxiv.org/abs/2607.29254)
- **PDF**: https://arxiv.org/pdf/2607.29254
- **详细分析**: [[20_Research/Papers/其他/Tool_Specifications_Matter_Uncovering_and_Mitigating_Safety_Risks_in_AI_Agents|Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents]]
- **作者**: Minghui Pan, Jiayuxuan Yang, Yuanyuan Yuan, Yu Jiang, Zhenpeng Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood. In this paper, we identify schema-formatted tool specifications as a primary source of agent safety degradation and show, through white-box representation analysis, that they weaken the model's internal refusal signals and contribute to unsafe tool execution. Building on this finding, we propose SafeKeep, an inference-time safeguard that decouples safety judgment from tool execution: it assesses requests using flattened textual tool specifications while retaining the original schema-formatted specifications for execution. Across two representative benchmarks and four LLMs, including both white-box and black-box models, SafeKeep increases the average refusal rate for harmful requests from 23.8% to 70.6% and reduces the average attack success rate under observation-level prompt injection from 25.6% to 2.5%. It also outperforms existing safeguards and preserves task-handling capability. We release the code and data at https://github.com/snowcatsmoking/SafeKeep .

</details>

---

### [[20_Research/Papers/大模型/CalibratedRubric_Task-Adaptive_Rubric_Banks_for_Open-Ended_LLM_Evaluation|CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation]]

![[assets/2607.29252_figure.png|800]]

- **arXiv**: [2607.29252](https://arxiv.org/abs/2607.29252)
- **PDF**: https://arxiv.org/pdf/2607.29252
- **详细分析**: [[20_Research/Papers/大模型/CalibratedRubric_Task-Adaptive_Rubric_Banks_for_Open-Ended_LLM_Evaluation|CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation]]
- **作者**: Mengting Chen, Yanshu Sun, Wanting Liang, Beidi Luan, Rui Sun, Dezhi Chen, Jing Li, Zuo Bai
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FinResearchBench, JudgmentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable evaluation of open-ended LLM outputs requires fine-grained rubrics, yet expert curation is costly and difficult to scale. Existing automated pipelines rely on strict judge unanimity and binary variance filters, which cannot distinguish measurable rubrics from informative ones. We introduce CalibratedRubric, a task-adaptive framework that combines type-specific scoring, Bayesian rubric-measurability filtering, and item response theory (IRT)-based bank assembly. CalibratedRubric estimates each rubric's measurability with a Beta--Bernoulli agreement posterior and uses a submodular information-coverage objective to construct compact rubric banks over the observed capability range. Across financial, healthcare, general, and legal benchmarks, measurability filtering improves human-gold agreement on JudgmentBench from $κ=0.604$ to $0.743$. IRT-based greedy selection improves cross-fitted rank fidelity over random selection across all six evaluated response blocks and requires only 49 rather than 131 rubrics to reach the target correlation on FinResearchBench decision-support tasks. Task-label perturbations further reduce system separation, confirming the practical relevance of task-adaptive scoring. These results support CalibratedRubric as an efficient, uncertainty-aware approach to open-ended LLM evaluation, with calibration gains depending on sufficient judge redundancy.

</details>

---

### [[20_Research/Papers/机器人/FBFM_A_Training-Free_Asynchronous_Feedback_Mechanism_for_Flow-Matching_in_World-Action_Models_Execution|FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution]]

![[assets/2607.29235_figure.png|800]]

- **arXiv**: [2607.29235](https://arxiv.org/abs/2607.29235)
- **PDF**: https://arxiv.org/pdf/2607.29235
- **详细分析**: [[20_Research/Papers/机器人/FBFM_A_Training-Free_Asynchronous_Feedback_Mechanism_for_Flow-Matching_in_World-Action_Models_Execution|FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution]]
- **作者**: Peize Li, Ruimeng Zhang, Ru Zhang, Cong Huang, Kai Chen, Shanghang Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although world-action models (WAMs) enhance long-horizon robot control by predicting visual evolution before acting, long-horizon reliability demands repeated re-grounding in real observations--not recursive rollout. Existing WAMs address this by refreshing history or KV cache with ground-truth data between chunks. However, such chunk-wise feedback operates at a coarse temporal granularity and thus fails to correct prediction errors at the individual time-step level. To address this, we propose Feedback Flow Matching (FBFM), a training-free inference mechanism that pushes re-grounding inside the actively generated chunk. During flow matching, FBFM applies a masked pseudoinverse correction to the conditional velocity field: it leverages the preceding action chunk to guide generation of the next action chunk, and uses the image observed after executing that preceding chunk to guide the next frame prediction. This cross-chunk pairing--where feedback from one chunk arrives in time to shape the next--creates an asynchronous loop that corrects errors without waiting for chunk boundaries. Being training-free, the mechanism improves responsiveness to unexpected events and suppresses drift in long-horizon tasks. We evaluate FBFM on both a joint-generation WAM (DreamZero) and a stage-wise WAM (LingBot-VA). On selected LIBERO and RoboTwin2.0 tasks, it improves success rates by over 5% in favorable settings, and real-world robot observation-prediction diagnostics show notably better tracking. We argue that FBFM offers a new paradigm for fine-grained online correction, bridging open-loop flow generation with closed-loop real-world dynamics.

</details>

---

### [[20_Research/Papers/强化学习/SAF-OPD_Stable_Advantage_Fusion_for_On-Policy_Distillation|SAF-OPD: Stable Advantage Fusion for On-Policy Distillation]]

![[assets/2607.29209_figure.png|800]]

- **arXiv**: [2607.29209](https://arxiv.org/abs/2607.29209)
- **PDF**: https://arxiv.org/pdf/2607.29209
- **详细分析**: [[20_Research/Papers/强化学习/SAF-OPD_Stable_Advantage_Fusion_for_On-Policy_Distillation|SAF-OPD: Stable Advantage Fusion for On-Policy Distillation]]
- **作者**: Yifan Ding, Xincheng Wei, Yoshua Y. Li, Ziheng Li, Yuquan Lu, Siyu Zhang, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Yun Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SAF-OPD: Stable Advantage Fusion for On-Policy Distillation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) broadcasts a single response-level reward to every token, while on-policy distillation (OPD) scores each token against a stronger teacher for a dense advantage but caps performance at teacher quality and discourages exploration beyond it. Their complementarity makes combining RLVR and OPD promising, but we find that fusing the two advantages with a fixed coefficient triggers entropy collapse from two miscalibrations: a magnitude mismatch, where token-level OPD advantages can spike far beyond the bounded RLVR advantage and erase its signal, and a temporal mismatch, where sustained full-strength OPD keeps pulling the student toward the teacher and limits exploration needed to surpass it. We propose SAF, a Stable Advantage Fusion framework that resolves both issues via a lightweight, four-stage pipeline applied only to the OPD advantage: a sparsify-then-compress mechanism for magnitude control paired with a warm-up-then-anneal mechanism for temporal control, with each stage independently switchable and adding negligible overhead. Instantiating RLVR with GRPO, we evaluate SAF across seven mathematical reasoning and code generation benchmarks with Qwen3-1.7B/4B/8B: SAF avoids entropy collapse and consistently outperforms fixed-coefficient GRPO+OPD fusion, improving the aggregate score by 0.51-2.70% across all six model-domain settings while achieving more stable training.

</details>

---

### [[20_Research/Papers/具身智能/CLIFT_Turning_Gemini_Robotics_On-Device_into_Humanoid_Specialists_via_Non-Invasive_Closed-Loop_Iterative_Fine-Tuning|CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning]]

![[assets/2607.29172_figure.png|800]]

- **arXiv**: [2607.29172](https://arxiv.org/abs/2607.29172)
- **PDF**: https://arxiv.org/pdf/2607.29172
- **详细分析**: [[20_Research/Papers/具身智能/CLIFT_Turning_Gemini_Robotics_On-Device_into_Humanoid_Specialists_via_Non-Invasive_Closed-Loop_Iterative_Fine-Tuning|CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning]]
- **作者**: Yuxin Chen, Hari Srikanth, Nathan Jew, Menglin Wu, Pengcheng Wang, Junli Ren, Masayoshi Tomizuka, Peng Xu, Jinyu Xie, Thomas Tian
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 4.2（加权：具身智能 1.8，大模型 0.1，强化学习 0.2，机器人 2.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While robot foundation models are growing increasingly capable, the strongest models are typically trained on proprietary data and remain closed-source, limiting downstream users' ability to adapt them to new tasks, embodiments, and deployment settings. Following the LLM community, an emerging access paradigm for closed-weight robot foundation models is the managed supervised fine-tuning (SFT) API, where users submit training data and receive a tuned policy without access to model weights, gradients, or training internals. While such APIs let downstream users leverage powerful proprietary foundation models, they restrict policy improvement to pure imitation, ruling out reinforcement learning and other closed-loop methods that rely on internal training signals. This limitation is particularly acute for agile, contact-rich humanoid manipulation, where the gap between policy outputs and deployed behavior is large due to novel states, action tracking dynamics, latency, and controller-specific failure modes. We study how effective this managed-API regime is for humanoid adaptation, and how closed-loop improvement can be realized within it to push policies toward task mastery. We conduct one of the first empirical studies of managed-API adaptation on a real humanoid, instantiated on Gemini Robotics On-Device (GROD). We find that direct SFT through the API substantially outperforms a leading open-weight VLA trained on the same demonstrations, yet still falls short of deployment-level mastery on agile, contact-rich tasks. To close this gap, we introduce CLIFT: Closed-Loop Iterative Fine-Tuning, which turns deployment-time reward feedback into API-compatible supervised data and enables closed-loop policy improvement without accessing weights, gradients, likelihoods, or losses-pushing GROD to near-perfect success after two flywheel cycles, all without "opening the model box."

</details>

---

### [[20_Research/Papers/具身智能/ActFovea_Runtime_Safeguarding_for_VLA_Policies_via_Spatiotemporal_Visual-Action_Consistency|ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency]]

![[assets/2607.29169_figure.png|800]]

- **arXiv**: [2607.29169](https://arxiv.org/abs/2607.29169)
- **PDF**: https://arxiv.org/pdf/2607.29169
- **详细分析**: [[20_Research/Papers/具身智能/ActFovea_Runtime_Safeguarding_for_VLA_Policies_via_Spatiotemporal_Visual-Action_Consistency|ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency]]
- **作者**: Wenda Yu, Tianshi Wang, Fengling Li, Xin Li, Jingjing Li, Lei Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AttackVLA, BYOVLA, FreezeVLA, OpenVLA, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying the underlying VLA policy. ActFovea uses robot kinematics, proprioceptive states, and recent actions to construct action-conditioned foveated regions that retain contact-relevant areas and predicted motion corridors while suppressing task-irrelevant visual content. It detects runtime risks by evaluating whether visual motion and observation freshness remain consistent with geometric, proprioceptive, and action transitions. For recoverable disturbances, ActFovea constructs disturbance-specific candidate observations and accepts a recovery only after verifying the resulting action chunk. When stale or replayed observations make reliable recovery impossible, it invokes a bounded safe-failure procedure. In closed-loop evaluations of $π_0$ across multiple LIBERO suites, ActFovea increases success under localized visual overlays from 49.3\% to 90.3\%, closing 93.7\% of the gap to clean performance. It further improves success under action drift and visual delay by 7.0 and 9.8 percentage points, respectively, while preserving clean-task performance. Under frozen-observation replay, ActFovea triggers timely safe failure in all trials, with no unprotected failures. These results demonstrate that spatiotemporal visual-action consistency provides an effective basis for runtime safeguarding of VLA policies.

</details>

---

### [[20_Research/Papers/大模型/Memory_Provenance_Laundering_in_LLM_Agents_A_Non-Amplification_Firewall_for_Persistent_Memory|Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory]]

![[assets/2607.29167_first_page.png|800]]

- **arXiv**: [2607.29167](https://arxiv.org/abs/2607.29167)
- **PDF**: https://arxiv.org/pdf/2607.29167
- **详细分析**: [[20_Research/Papers/大模型/Memory_Provenance_Laundering_in_LLM_Agents_A_Non-Amplification_Firewall_for_Persistent_Memory|Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory]]
- **作者**: Jinghan Xu, Yiyong Xiao, Wanru Shao, Hankai Liu, Xinjin Li
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authority. Existing prompt filters, content sanitizers, and tool guards do not enforce source-authority non-amplification after lossy memory consolidation. We formalize this boundary and instantiate it as Provenance-Preserving Memory Fire wall (PPMF), a lightweight memory middleware that preserves platform-maintained provenance and authorizes tool calls by matching action risk to the authority of action-relevant memories. In our schema-grounded evaluation with fixed risk policies, vulnerable consolidated memories reach up to 1.000 attack success rate(ASR); with intact platform-maintained provenance, confirmation, and risk labels, no evaluated unauthorized high-risk action passes the PPMF gate while confirmed benign actions and targeted low-risk memory use remain executable.

</details>

---

### [[20_Research/Papers/大模型/Semantics_of_Subterfuge_Benchmarking_Legal_Deception_Detection_Against_General-domain_State-of-the-Art|Semantics of Subterfuge: Benchmarking Legal Deception Detection Against General-domain State-of-the-Art]]

![[assets/2607.29066_figure.png|800]]

- **arXiv**: [2607.29066](https://arxiv.org/abs/2607.29066)
- **PDF**: https://arxiv.org/pdf/2607.29066
- **详细分析**: [[20_Research/Papers/大模型/Semantics_of_Subterfuge_Benchmarking_Legal_Deception_Detection_Against_General-domain_State-of-the-Art|Semantics of Subterfuge: Benchmarking Legal Deception Detection Against General-domain State-of-the-Art]]
- **作者**: Theekshana Samaradiwakara, Nisansa de Silva, George C. Lobb
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《Semantics of Subterfuge: Benchmarking Legal Deception Detection Against General-domain State-of-the-Art》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FakeNewsNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deception detection has critical implications for legal proceedings, law enforcement, and online security. Although human judgment is limited in accuracy and scalability, Natural Language Processing (NLP) offers a data-driven alternative. We present a survey and comparative analysis of NLP-based Automatic Deception Detection (ADD) focusing on the legal domain, reviewing the evolution from feature-based machine learning to Large Language Model (LLM) approaches. We conduct a unified empirical evaluation across seven datasets (two legal, five general-domain), comparing six fine-tuned transformer models and seven LLMs under four prompting strategies. The results show strong domain sensitivity, with fine-tuned models excelling in data-rich general domains and few-shot LLMs remaining competitive in low-resource legal settings. Chain-of-Thought prompting often underperforms direct classification. These findings highlight the need for domain adaptation and interpretable systems in high-stakes legal contexts.

</details>

---

### [[20_Research/Papers/具身智能/Auto-JEPA_A_Latent_World_Model_of_Continuous_Intent_for_End-to-End_Autonomous_Driving|Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving]]

![[assets/2607.29031_figure.png|800]]

- **arXiv**: [2607.29031](https://arxiv.org/abs/2607.29031)
- **PDF**: https://arxiv.org/pdf/2607.29031
- **详细分析**: [[20_Research/Papers/具身智能/Auto-JEPA_A_Latent_World_Model_of_Continuous_Intent_for_End-to-End_Autonomous_Driving|Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving]]
- **作者**: Jiwei Yang, Zhengxian Chen, Chaosheng Huang, Jun Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DriveWorld-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing autonomous-driving world models typically perform dense prediction of future videos, occupancy states, BEV representations, or agent motion. We argue that planning need not reconstruct the complete future world, but only focus on scene features that affect future ego action. Based on this perspective, we propose Auto-JEPA, an action-oriented latent world model that learns continuous future driving intent through joint-embedding prediction. Given visual observations, egomotion history, and navigation commands, Auto-JEPA predicts an intent embedding aligned with the latent representation of the future ego trajectory. The predicted intent retrieves executable trajectories from a fixed trajectory memory, which are then ranked by a scene-conditioned candidate selection module. Auto-JEPA keeps the visual encoder frozen, requires no explicit perception annotations, and uses no learned trajectory generator. By optimizing only task-specific modules for trajectory representation, intent prediction, and candidate selection, Auto-JEPA achieves 91.3 PDMS on NAVSIM v1 and 89.1 EPDMS on NAVSIM v2. Semantic occlusion experiments show that masking dynamic-agent regions induces an average intent change 2.97x that of equal-area random masking. Moreover, occluding vehicles that affect future driving substantially changes the predicted intent and selected trajectory, whereas both remain essentially unchanged when non-influential vehicles are occluded. These results show that future-intent prediction encourages the model to focus on planning-relevant visual features and supports high-quality planning without dense future-world modeling.

</details>

---

### [[20_Research/Papers/大模型/MMShopBench_A_Real-Log_Benchmark_for_Multimodal,_Multi-Turn_Shopping_Agents|MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents]]

![[assets/2607.29002_figure.png|800]]

- **arXiv**: [2607.29002](https://arxiv.org/abs/2607.29002)
- **PDF**: https://arxiv.org/pdf/2607.29002
- **详细分析**: [[20_Research/Papers/大模型/MMShopBench_A_Real-Log_Benchmark_for_Multimodal,_Multi-Turn_Shopping_Agents|MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents]]
- **作者**: Zeying Hao, Hao Guo, Mengtao Xu, Yimin Hu, Yuheng Song, Zesheng Zhou, Jinsong Lan, Xiaoyong Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《MMShopBench: A Real-Log Benchmark for Multimodal, Multi-Turn Shopping Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EComAgentBench, MMShopBench, ShoppingBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online shoppers increasingly turn to AI shopping assistants, using images and multi-turn dialogue to express and refine product needs that are difficult to articulate in text alone. However, existing benchmarks largely rely on text-only or synthetic requests, underrepresenting complex real-world shopping requirements jointly expressed through images and language. We introduce MMShopBench, the first real-log benchmark for multimodal, multi-turn shopping agents. Built from carefully cleaned and manually annotated shopping logs, MMShopBench provides ground-truth annotations of each request's purchase intent and mandatory product requirements. Agents must infer these requirements jointly from user images and multi-turn dialogue, retrieve candidate products through image and text search, and verify that each candidate satisfies all requirements using its product images and structured attributes. We evaluate representative open-source and proprietary models using an evidence-grounded multimodal protocol and construct a companion training set for fine-tuning an open-source model. To ensure reproducible experimentation, we build an offline shopping sandbox, where fine-tuning substantially narrows the performance gap between our open-source model and leading proprietary models, demonstrating the effectiveness of our training data.

</details>

---

### [[20_Research/Papers/大模型/Adjudicated_Captioning_Multi-Agent_Alignment_Scoring_and_Consensus-Distilled_Beam_Arbitration_for_Strict_Zero-Shot_Image_Captioning|Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning]]

![[assets/2607.28986_figure.png|800]]

- **arXiv**: [2607.28986](https://arxiv.org/abs/2607.28986)
- **PDF**: https://arxiv.org/pdf/2607.28986
- **详细分析**: [[20_Research/Papers/大模型/Adjudicated_Captioning_Multi-Agent_Alignment_Scoring_and_Consensus-Distilled_Beam_Arbitration_for_Strict_Zero-Shot_Image_Captioning|Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning]]
- **作者**: Duy Tran Thanh, Thien-Phuc Doan, Long Nguyen-Vu, Ngo Tan Vu Khanh
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ListNet, PCM-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot image captioning (ZIC) describes images without paired image-caption supervision during captioner training, relying on text-only corpora and frozen pretrained image-text scorers. Existing retrieval-augmented methods score image-text alignment once, at retrieval, then commit the captioner's autoregressive beam under language-model probability alone, leaving the decoder without further visual grounding feedback. Progress has stalled, with no method improving on the strict-regime best since 2024. We propose Adjudicated Captioning, an inference-time multi-agent framework that restores grounding feedback at multiple checkpoints over an unchanged IFCap captioner. First, we install a stronger frozen Retrieval Encoder at the input. Second, between retrieval and decoding we insert a frozen Cross-Attention Verifier that re-ranks the top-9 retrievals to top-5. Third, at the output beam we attach a learned Reranker pairing TriFuse, a multilayer perceptron, with MemAttend, a memory-attended transformer, the pipeline's only learned components; both are trained self-supervised by Borda-consensus distillation across the three frozen scorers, using no paired image-caption labels and no reference captions. Under the inductive headline protocol, with rerankers fit on the disjoint COCO Karpathy validation beam and applied frozen to test, the framework reaches CIDEr 117.6 and SPICE 21.9 on COCO Karpathy, up from 108.0 and 20.3 for IFCap, a +9.6 CIDEr gain, and +7.7 above NES, the strongest synthetic-image-augmented method at 109.9, without retraining the captioner. A training-free fixed-fusion baseline reaches 115.8 CIDEr, so +7.8 of the +9.6 gain comes from the non-learned architectural intervention and the remaining +1.8 from the learned rerankers. The same recipe transfers off-COCO without captioner retraining: +8.1 CIDEr on Flickr30k Karpathy and +5.7 on NoCaps overall.

</details>

---

### [[20_Research/Papers/大模型/MerchantBench_Benchmarking_LLM_Agents_for_Long-Term_Coherence_in_E-Commerce_Operations|MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations]]

![[assets/2607.28956_figure.png|800]]

- **arXiv**: [2607.28956](https://arxiv.org/abs/2607.28956)
- **PDF**: https://arxiv.org/pdf/2607.28956
- **详细分析**: [[20_Research/Papers/大模型/MerchantBench_Benchmarking_LLM_Agents_for_Long-Term_Coherence_in_E-Commerce_Operations|MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations]]
- **作者**: Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang, Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu, Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Market-Bench, MerchantBench, Real-World, RetailBench, Vending-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents are increasingly evaluated as autonomous tool users, yet most benchmarks focus on bounded tasks with immediate success criteria. Real-world deployments often require Long-Term Coherence, the capacity to preserve purposeful behavior across extended horizons while adapting decisions to accumulated evidence. Evaluating this capacity requires a persistent environment in which actions constrain future choices, feedback arrives at heterogeneous delays, and incoherent behavior produces measurable cumulative effects. Seller-side e-commerce provides a suitable setting for this evaluation through recurrent and interdependent decisions over Product Sourcing, Listing and Pricing Control, Cash-Flow Management, and Mixed-Latency Feedback Adaptation. We introduce MerchantBench, a 365-day order-level simulation grounded in 98,843 real e-commerce product records and equipped with 26 tools for agent interaction. MerchantBench couples promptly observable Upstream Supplier Events with delayed Downstream Order Outcomes, requiring agents to follow individual order lifecycles and revisit earlier decisions. We evaluate eight LLMs under two agent frameworks in 48 runs, each spanning 365 simulated days. Our results reveal a substantial gap between even the latest LLMs and human participants, with the best LLM configuration attaining only 27.3\% of the mean final net assets achieved by human participants.

</details>

---

### [[20_Research/Papers/大模型/NeSyFS_A_Neuro-symbolic_Fast-Slow_Thinking_Framework_for_LLM_Agent_under_Partial_Observability|NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability]]

![[assets/2607.28942_figure.png|800]]

- **arXiv**: [2607.28942](https://arxiv.org/abs/2607.28942)
- **PDF**: https://arxiv.org/pdf/2607.28942
- **详细分析**: [[20_Research/Papers/大模型/NeSyFS_A_Neuro-symbolic_Fast-Slow_Thinking_Framework_for_LLM_Agent_under_Partial_Observability|NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability]]
- **作者**: Duo Xu, Faramarz Fekri
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently Large Language Models (LLMs) have been increasingly deployed as autonomous agents in applications such as self-reflection, retrieval-augmented generation, and scientific discovery. In these settings, agents must act based on limited observations rather than full environmental states, leading to partial observability. This introduces several key challenges: belief state inference, task objective misalignment, and planning under uncertainty. Prior approaches typically condition actions on full or summarized action-observation histories whose redundant and irrelevant information can mislead the decision making of LLM agent. Inspired by human cognition, we propose a novel neuro-symbolic fast-slow thinking (NeSyFS) framework for LLM agent, addressing the challenges introduced by partial observability in a unified approach. We use a knowledge graph (KG) to represent the belief state, providing triplets as context for every module of NeSyFS. The fast-thinking module performs reactive action, while slow-thinking conducts a new uncertainty-aware planning by following the high-level structure of twisted sequential Monte Carlo (TSMC) algorithm. To mitigate the misalignment of task objective, a reflection module is used to reflect fast-thinking actions, and also switches to the slow-thinking module whenever reactive actions repeatedly fail. Experiments on three representative benchmarks, i.e. ALFWorld, Webshop, and ScienceWorld, demonstrate significant advantages over previous methods.

</details>

---

### [[20_Research/Papers/大模型/FairFund-Bench_Evaluating_Distributive_Bias_in_LLM_Resource_Allocation|FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation]]

![[assets/2607.28934_figure.png|800]]

- **arXiv**: [2607.28934](https://arxiv.org/abs/2607.28934)
- **PDF**: https://arxiv.org/pdf/2607.28934
- **详细分析**: [[20_Research/Papers/大模型/FairFund-Bench_Evaluating_Distributive_Bias_in_LLM_Resource_Allocation|FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation]]
- **作者**: Martin Lukk
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《FairFund-Bench: Evaluating Distributive Bias in LLM Resource Allocation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FairFund-Bench, StereoSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly involved in the distribution of scarce resources, raising concerns about biased allocations based on characteristics like race and gender. Recent LLM audits have produced inconsistent results, however, finding evidence of both positive and negative discrimination towards women and ethnic minorities, even for the same models. We show that this disagreement can arise from differences in audit format and introduce FairFund-Bench, a benchmark that systematically varies key features of previous audit designs: the evaluation task (rating, ranking, or allocation), comparison context (single or multi-stimulus), and whether the audit is transparent or disguised. The benchmark comprises 600 requests for financial assistance created from human-authored templates (calibrated against 1.3M real GoFundMe campaigns) across three domains, four race and two gender categories, and five causal framings of need derived from welfare deservingness theory. Across 14 models, audit format changes the direction of bias: models advantage minorities when rating claimants individually but penalize some groups when ranking them side by side. Bias magnitude, though small overall, is several times greater in disguised audits than in transparent ones, where, faced with appeals differing only in claimants' names, models overwhelmingly split funds equally. Causal framing effects, by contrast, exceed demographic effects by roughly an order of magnitude and are consistent across models and audit formats, indicating that current LLMs robustly reproduce human deservingness evaluations. The benchmark scores models on four criteria (demographic bias, deservingness alignment, cross-task consistency, and cross-context consistency), is publicly available, and can be readily adapted to other substantive domains.

</details>

---

### [[20_Research/Papers/强化学习/Gated_Q-learning_Add_Off-Policy_Bias_to_Taste|Gated Q-learning: Add Off-Policy Bias to Taste]]

![[assets/2607.28916_figure.png|800]]

- **arXiv**: [2607.28916](https://arxiv.org/abs/2607.28916)
- **PDF**: https://arxiv.org/pdf/2607.28916
- **详细分析**: [[20_Research/Papers/强化学习/Gated_Q-learning_Add_Off-Policy_Bias_to_Taste|Gated Q-learning: Add Off-Policy Bias to Taste]]
- **作者**: Brett Daley
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Gated Q-learning: Add Off-Policy Bias to Taste》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multistep credit assignment is critical for sample-efficient reinforcement learning, yet managing off-policy bias in Q-learning remains a fundamental challenge. For 30 years, practitioners have been limited to a binary choice: eliminate the bias at the cost of severely truncated eligibility traces (Watkins' Q($λ$)), or ignore the bias to learn faster while injecting detrimental errors into the value estimates (Peng's Q($λ$)). Modern off-policy estimators fail to resolve this tension, as importance-sampling ratios collapse under Q-learning's greedy target policy. We introduce Gated Q-learning, a novel algorithmic framework that ends this dilemma by smoothly interpolating between the two historical extremes. Rather than relying on importance sampling, our approach employs a continuous, state-action-dependent gating mechanism to selectively attenuate eligibility traces in an exploration-aware manner. We provide a rigorous theoretical foundation for this mechanism, proving that the expected operator remains a contraction mapping and deriving its exact fixed point. Empirical evaluations verify that intermediate gating safely enables longer credit-assignment horizons, yielding faster initial learning than either extreme. Gated Q-learning offers a simple alternative to importance sampling while enabling customization of the effective multistep horizon and the amount of off-policy bias in Q-learning agents.

</details>

---

### [[20_Research/Papers/大模型/Validation_Evidence_in_LLM_Repair_Agents_How_Much_of_What_Passes_Actually_Tests_the_Bug|Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?]]

![[assets/2607.28871_figure.png|800]]

- **arXiv**: [2607.28871](https://arxiv.org/abs/2607.28871)
- **PDF**: https://arxiv.org/pdf/2607.28871
- **详细分析**: [[20_Research/Papers/大模型/Validation_Evidence_in_LLM_Repair_Agents_How_Much_of_What_Passes_Actually_Tests_the_Bug|Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?]]
- **作者**: Xiaonan Xu, Wenjing Wu
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a repair agent runs a test and sees it pass, the result is treated as evidence about the reported defect. We measure how often that treatment is warranted. BSG-VA (buggy-state/candidate-state/gold-fix validation analysis) captures each validation command at its exact working-tree state, extracts a test-only patch, and replays the command on the original buggy code (B), the candidate state (S), and the developer gold fix (G). The captured outcome and the replay results assign every event an evidence role, from gold-aligned bug-discriminating through regression-only to misleading. Across 3,730 events in 643 rollouts on 110 tasks, 46.0% of positive comparable events carry no bug-discriminating information; 23.8% of baseline rollouts, with no feedback injected, close with a patch whose entire positive evidence base is of this kind. A three-arm experiment tests whether returning the B-replay outcome to the agent changes this pattern. Bug-contrast feedback reduces evidence-inadequate closure by 7.8 percentage points relative to an attention-matched reminder (p = 0.0029) and raises bug-discriminating evidence by 7.4 points (p = 0.011), with no detectable cost to repair success. Both estimates fall below the prespecified 10-percentage-point smallest effect size of interest, so practical magnitude remains uncertain. Roughly a third of the improvement traces to the reminder alone; across two exploratory replications, varying the scaffold and the model, the B-replay content adds a detectable increment only with gpt-5.6-sol under the unconstrained tool-use loop. BSG-VA applies post hoc to any replayable repair trajectory that preserves the required code states and execution environment. Keywords: program repair agents, validation evidence, test adequacy, large language models, software quality, controlled experiment.

</details>

---

### [[20_Research/Papers/大模型/TextCloak_Thwarting_Unauthorized_LLM_Exploitation_via_RL-Driven_Unlearnable_Text|TextCloak: Thwarting Unauthorized LLM Exploitation via RL-Driven Unlearnable Text]]

![[assets/2607.28862_figure.png|800]]

- **arXiv**: [2607.28862](https://arxiv.org/abs/2607.28862)
- **PDF**: https://arxiv.org/pdf/2607.28862
- **详细分析**: [[20_Research/Papers/大模型/TextCloak_Thwarting_Unauthorized_LLM_Exploitation_via_RL-Driven_Unlearnable_Text|TextCloak: Thwarting Unauthorized LLM Exploitation via RL-Driven Unlearnable Text]]
- **作者**: Chengshuai Zhao, Pingchuan Ma, Dawei Li, Bohan Jiang, Zhiyuan Yu, Zhen Tan, Huan Liu
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《TextCloak: Thwarting Unauthorized LLM Exploitation via RL-Driven Unlearnable Text》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid development of Large Language Models (LLMs) has led to significant advances across a wide range of language tasks, while simultaneously raising growing concerns about unauthorized data exploitation and privacy leakage. Unlearnable examples (UEs) offer a promising defense by introducing carefully designed perturbations into data such that models trained on them exhibit degraded utility. However, existing methods for text protection are primarily designed for classification tasks (e.g., sentiment analysis) in discriminative language models and often rely on injecting class-specific linguistic cues, which limits their effectiveness in the open-ended generation settings of LLMs. In this work, we propose TextCloak, an RL-driven framework for protecting textual data against unauthorized LLM exploitation. TextCloak employs a generative policy that transforms batches of clean text into unlearnable examples while preserving semantic fidelity and linguistic naturalness. To optimize the policy, we introduce GRPO-UE, which rewards generated unlearnable text based on the downstream degradation they induce in fine-tuned surrogate LLMs and updates the generator parameters via group-relative policy optimization. This bi-level optimization enables the generator to discover generalizable protective patterns beyond class-specific cues. Comprehensive experiments on six publicly available datasets and nine state-of-the-art LLMs demonstrate that TextCloak consistently impairs unauthorized fine-tuning while maintaining text utility for legitimate use. Further analyses establish its transferability and robustness across model architectures, training configurations, and adaptive attacks, highlighting its broad applicability as a practical defense against unauthorized LLM exploitation.

</details>

---

### [[20_Research/Papers/强化学习/Hypergradient-based_Bilevel_Reinforcement_Learning_with_Improved_Sample_Complexity|Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity]]

![[assets/2607.28849_first_page.png|800]]

- **arXiv**: [2607.28849](https://arxiv.org/abs/2607.28849)
- **PDF**: https://arxiv.org/pdf/2607.28849
- **详细分析**: [[20_Research/Papers/强化学习/Hypergradient-based_Bilevel_Reinforcement_Learning_with_Improved_Sample_Complexity|Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity]]
- **作者**: Naman Saxena, Mudit Gaur, Vaneet Aggarwal
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Hypergradient-based Bilevel Reinforcement Learning with Improved Sample Complexity》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bilevel reinforcement learning (RL) is an important framework within the literature of RL that can be used to formalize various categories of problems, such as meta-learning, hierarchical task decomposition, and reinforcement learning from human feedback (RL-HF). Most of the bilevel RL algorithms are either not scalable because of using hypergradient with Hessian, or they suffer from high sample complexity because of using penalty-based approximation methods. In this work, we propose a hypergradient-based bilevel RL algorithm using the optimality of the Boltzmann policy for the entropy regularized discounted RL objective function. Our proposed algorithm is Hessian-free and obtains an iteration complexity of $O(ε^{-1})$ and state-of-the-art sample complexity of $\tilde{O}(ε^{-2})$ under mild regularity conditions. Further, in our convergence analysis, we are able to remove the assumption of the Polyak-Lojasiewicz (PL) condition on the outer-level objective function present in the prior state-of-the-art sample complexity work.

</details>

---

### [[20_Research/Papers/大模型/SciToolAgent-Evo_An_Ontology-Aware_Self-Evolving_Agent_for_Open-World_Scientific_Tool_Acquisition|SciToolAgent-Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition]]

![[assets/2607.28692_figure.png|800]]

- **arXiv**: [2607.28692](https://arxiv.org/abs/2607.28692)
- **PDF**: https://arxiv.org/pdf/2607.28692
- **详细分析**: [[20_Research/Papers/大模型/SciToolAgent-Evo_An_Ontology-Aware_Self-Evolving_Agent_for_Open-World_Scientific_Tool_Acquisition|SciToolAgent-Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition]]
- **作者**: Yuqi Tang, Chenyi Zhou, Libin Wang, Keyan Ding, Qiang Zhang, Huajun Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SciToolAgent-Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld, Open-World, OpenSciToolBench, RESTBench, SciToolBench, SciToolEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have been increasingly adopted in scientific research for organizing and invoking specialized computational tools. However, their reliance on predefined tool spaces with static semantics limits their applicability to open-world scientific workflows, where tool requirements, capabilities, and boundaries evolve dynamically. To this end, we propose SciToolAgent-Evo, an ontology-aware self-evolving agent for open-world scientific tool acquisition. Driven by an evolving memory of skills, experiences, and an ontologized tool graph, it distills generalizable knowledge from contrastive trajectories during accumulation, whereas during inference, it formulates active requests and utilizes a LinUCB-based bandit gate to dynamically balance exploration and exploitation. Once a novel tool is acquired, its scientific ontology is completed online for seamless integration into the known graph. Moreover, we introduce OpenSciToolBench, a benchmark containing 900 realistic tasks across four difficulty levels. Extensive evaluations show that SciToolAgent-Evo achieves state-of-the-art performance, validating its robustness and generalization.

</details>

---

### [[20_Research/Papers/机器人/Multi-Agent_Planning_with_Spatio-Temporal_and_Topological_Constraints_using_STL-GO|Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO]]

![[assets/2607.28679_figure.png|800]]

- **arXiv**: [2607.28679](https://arxiv.org/abs/2607.28679)
- **PDF**: https://arxiv.org/pdf/2607.28679
- **详细分析**: [[20_Research/Papers/机器人/Multi-Agent_Planning_with_Spatio-Temporal_and_Topological_Constraints_using_STL-GO|Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO]]
- **作者**: Sheryl Paul, Vidisha Kudalkar, Anand Balakrishnan, Lars Lindemann, Alberto Speranzon, Jyotirmoy V. Deshmukh
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.9（加权：大模型 0.5，机器人 0.4）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Multi-Agent Planning with Spatio-Temporal and Topological Constraints using STL-GO》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HypRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent planning problems arise in a variety of engineering applications, such as multi-robot wildfire fighting and unmanned aerial inspection in factories. A particular challenge is the existence of spatio-temporal (i.e., when and/or where an agent should do what) and topological constraints (i.e., how agents should interact), as typically formalized via the notion of graphs. Over the last years, various frameworks have been proposed that can capture such constraints via spatio-temporal logics. We focus here on spatio-temporal logic with graph operators (STL-GO), a recent formalism that supports reasoning about multiple agents and their topologies, such as sensing, communication, and task topologies. In this paper, we consider the problem of planning multi-agent paths that satisfy constraints written in STL-GO. This problem is particularly challenging due to the need of encoding multiple, potentially time-varying graphs via the graph operators inherent to STL-GO. We present two encodings of this problem, one based on mixed-integer programming (MIP) and another based on satisfiability modulo theory (SMT), with soundness guarantees. We provide a unified interface for specifying agent constraints, their graph topologies, and the STL-GO specification, enabling seamless use of both methods and facilitating direct comparison between them. We evaluate both encodings on a multi-UAV search-and-rescue benchmark, ablating over team size and graph complexity, highlighting the expressiveness of the proposed encodings under dynamic multi- graph interactions.

</details>

---

### [[20_Research/Papers/大模型/TAPR_Enhancing_LLM_Performance_with_a_Task-Aware_Prompt_Rewriter|TAPR: Enhancing LLM Performance with a Task-Aware Prompt Rewriter]]

![[assets/2607.28657_figure.png|800]]

- **arXiv**: [2607.28657](https://arxiv.org/abs/2607.28657)
- **PDF**: https://arxiv.org/pdf/2607.28657
- **详细分析**: [[20_Research/Papers/大模型/TAPR_Enhancing_LLM_Performance_with_a_Task-Aware_Prompt_Rewriter|TAPR: Enhancing LLM Performance with a Task-Aware Prompt Rewriter]]
- **作者**: Oliver Savolainen, Emanuele Bastianelli, Hosein Azarbonyad
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.4，强化学习 0.4）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《TAPR: Enhancing LLM Performance with a Task-Aware Prompt Rewriter》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA, StrategyQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) often require carefully crafted prompts to unlock their full potential, which can be a barrier for non-expert users. This work addresses the challenge by introducing a Task-Aware Prompt Rewriter (TAPR), a model that reformulates user prompts into task-optimized prompts with the explicit goal of improving downstream LLM performance. We train TAPR using reinforcement learning with Group Relative Policy Optimization (GRPO), where rewards are derived from LLM-as-judge evaluations of both the reformulated prompt and the corresponding task output. Experimental results on diverse tasks, such as question answering, summarization, and arithmetic reasoning, show that our method yields consistent gains over base models in prompt rewriting ability. Fine-tuning Phi-4-mini-instruct (as the base model for TAPR) produces prompts that contain clearer and more instructive language, leading to higher accuracy on established benchmarks such as Natural Questions and GSM8K. Our code is available at: https://github.com/OliverSavolainen/task-specific-prompt-rewriter

</details>

---

### [[20_Research/Papers/大模型/HenTwin_A_Multimodal_Digital_Twin_Framework_for_Longitudinal_Biological_State_Monitoring_in_Laying_Hens|HenTwin: A Multimodal Digital Twin Framework for Longitudinal Biological State Monitoring in Laying Hens]]

![[assets/2607.28652_first_page.png|800]]

- **arXiv**: [2607.28652](https://arxiv.org/abs/2607.28652)
- **PDF**: https://arxiv.org/pdf/2607.28652
- **详细分析**: [[20_Research/Papers/大模型/HenTwin_A_Multimodal_Digital_Twin_Framework_for_Longitudinal_Biological_State_Monitoring_in_Laying_Hens|HenTwin: A Multimodal Digital Twin Framework for Longitudinal Biological State Monitoring in Laying Hens]]
- **作者**: Yashan Dhaliwal, Shreya Rao, Suresh Neethirajan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 0.6（加权：大模型 0.4，世界模型 0.2）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《HenTwin: A Multimodal Digital Twin Framework for Longitudinal Biological State Monitoring in Laying Hens》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Early-life monitoring in laying hens remains constrained by fragmented single-modality sensing and the absence of formal system-level state representations. HenTwin, a multimodal digital twin framework implemented as a five-layer IoT architecture, formalizes flock-level multimodal biological state dynamics from hatch through 25 weeks of age. A four-dimensional biological state vector integrating body surface temperature, acoustic energy entropy, band energy ratio, and optical-flow-based motion is defined, with the temperature-humidity index treated as an exogenous environmental input to preserve intervention capability. A discrete-time state transition model is estimated from 25 weeks of longitudinal multimodal data collected from 150 Lohmann LSL-Lite hens across five controlled rooms at the Atlantic Poultry Research Centre, Dalhousie University. The estimated transition matrix exhibits modality-specific persistence while remaining asymptotically stable. Perturbation analysis demonstrates that a sustained +2.0 THI increase produces a stable long-run acoustic entropy elevation of 0.54 nats, approximately one-quarter of the entire 1.87-nat developmental decline observed across the study period. Pettitt change-point detection identifies coordinated multimodal developmental state transitions at Weeks 12-14. Cross-room validation suggests that structural transition parameters are partially transferable across rooms, whereas environmental input sensitivity requires room-specific calibration, supporting a two-tier IoT deployment architecture. Leave-one-out cross-validation demonstrates consistent out-of-sample model performance. HenTwin takes a first step toward formal, state-aware digital twin inference in precision livestock farming.

</details>

---

### [[20_Research/Papers/强化学习/ThinkReset_Learnable_Intermediate_Interface_Construction_for_Bounded-Context_Long-Horizon_Reasoning|ThinkReset: Learnable Intermediate Interface Construction for Bounded-Context Long-Horizon Reasoning]]

![[assets/2607.28642_first_page.png|800]]

- **arXiv**: [2607.28642](https://arxiv.org/abs/2607.28642)
- **PDF**: https://arxiv.org/pdf/2607.28642
- **详细分析**: [[20_Research/Papers/强化学习/ThinkReset_Learnable_Intermediate_Interface_Construction_for_Bounded-Context_Long-Horizon_Reasoning|ThinkReset: Learnable Intermediate Interface Construction for Bounded-Context Long-Horizon Reasoning]]
- **作者**: Fei Ding, Yongkang Zhang, Runhao Liu, Yuhao Liao, Zijian Zeng
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《ThinkReset: Learnable Intermediate Interface Construction for Bounded-Context Long-Horizon Reasoning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long chain-of-thought reasoning improves performance on complex problems, but it also introduces redundancy accumulation, context overflow, and error anchoring. We argue that under bounded context windows, the core bottleneck is not trajectory compression or test-time control, but the absence of a reusable intermediate interface that can replace discarded history and support continued solving. We further identify a key failure mode of outcome-reward-driven long-chain reinforcement learning: when the model has not solved the task before the window is nearly exhausted, the final-answer reward encourages premature guessing rather than continued careful reasoning. We propose ThinkReset, a text-space instantiation of this view. ThinkReset explicitly constructs reusable intermediate interfaces through interface writeback and reset, and directly optimizes post-reset continuation success. Across multiple long-horizon reasoning benchmarks, this perspective consistently improves success rates under fixed context windows.

</details>

---

### [[20_Research/Papers/大模型/The_Formalism_Trap_Are_LLM-as-a-Judge_Evaluators_Blinded_by_Consensus_Mimicry_under_Social_Load|The Formalism Trap: Are LLM-as-a-Judge Evaluators Blinded by Consensus Mimicry under Social Load?]]

![[assets/2607.28641_figure.png|800]]

- **arXiv**: [2607.28641](https://arxiv.org/abs/2607.28641)
- **PDF**: https://arxiv.org/pdf/2607.28641
- **详细分析**: [[20_Research/Papers/大模型/The_Formalism_Trap_Are_LLM-as-a-Judge_Evaluators_Blinded_by_Consensus_Mimicry_under_Social_Load|The Formalism Trap: Are LLM-as-a-Judge Evaluators Blinded by Consensus Mimicry under Social Load?]]
- **作者**: Dahlia Shehata, Ming Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《The Formalism Trap: Are LLM-as-a-Judge Evaluators Blinded by Consensus Mimicry under Social Load?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce the \textit{Agentic Formalism Trap} and the Evaluative Dissonance Index ($D_E$), quantifying how LLM-as-a-Judge systems conflate structural proceduralism with semantic truth under adversarial load. Analyzing 22,500 trajectories across 3 domains (GAIA, SWE-bench, Multi-Challenge), we extract a semantic taxonomy of hallucination maneuvers, validated via deterministic lexical grounding ($p &lt; 10^{-120}$). A logistic meta-evaluator isolates the exact syntactic triggers of this evaluator capture (ROC-AUC 0.8779), while a zero-shot Leave-One-Domain-Out transfer proves the vulnerability is universally domain-agnostic (mean ROC-AUC 0.7482). Architectural profiling reveals that distinct simulated swarm topologies induce mathematically disparate semantic blind spots, proving that unanchored closed-loop evaluation is unstable, systemically divergent and necessitates architecture-specific vigilance filters.

</details>

---

### [[20_Research/Papers/大模型/OpenClaw_and_Ollama_in_Agentic_AI_Toward_Fully_Autonomous_and_Scalable_AI_Agent_Systems|OpenClaw and Ollama in Agentic AI: Toward Fully Autonomous and Scalable AI Agent Systems]]

![[assets/2607.28629_figure.png|800]]

- **arXiv**: [2607.28629](https://arxiv.org/abs/2607.28629)
- **PDF**: https://arxiv.org/pdf/2607.28629
- **详细分析**: [[20_Research/Papers/大模型/OpenClaw_and_Ollama_in_Agentic_AI_Toward_Fully_Autonomous_and_Scalable_AI_Agent_Systems|OpenClaw and Ollama in Agentic AI: Toward Fully Autonomous and Scalable AI Agent Systems]]
- **作者**: Konstantinos I. Roumeliotis, Ranjan Sapkota
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《OpenClaw and Ollama in Agentic AI: Toward Fully Autonomous and Scalable AI Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid transition from reactive large language models (LLMs) to persistent, action-capable systems has exposed critical gaps in the architectural understanding of Agentic AI, particularly in separating inference, orchestration, and execution layers for autonomous AI agents. Despite recent advances, unified frameworks for designing and evaluating full-stack agentic systems remain limited. This paper presents a comprehensive, layered architecture for Agentic AI, outlining the evolution from reactive LLM interfaces to persistent, goal-driven autonomous AI agents with memory, planning, and continuous execution. We analyze OpenClaw and Ollama as a full-stack Agentic AI system, where Ollama serves as the LLM inference layer and OpenClaw enables agent runtime orchestration, integrating reasoning, tool use, and action execution. A prototype experimental validation of the OpenClaw-Ollama architecture demonstrates that capabilities such as persistent memory, tool utilization, and adaptive decision-making emerge from system-level integration rather than standalone models, with performance improving consistently as architectural complexity increases. The study further examines challenges in scalability, security, privacy, governance, and evaluation of agentic systems, highlighting the need for robust benchmarking and system-level design. Future directions include scalable multi-agent architectures, distributed autonomous systems, and human-aware Agentic AI frameworks for responsible deployment. Overall, this work establishes a unified architectural foundation for Agentic AI, validates the effectiveness of full-stack autonomous AI agents, and provides a roadmap for building scalable, secure, and trustworthy agentic systems. All models, code, and datasets are publicly released to support reproducibility and benchmarking.

</details>

---

### [[20_Research/Papers/强化学习/SVR_Self-Verifying_Refinement_via_Joint_Verdict-Confidence_Reinforcement_Learning_for_Adaptive_Test-Time_Compute|SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute]]

![[assets/2607.28457_figure.png|800]]

- **arXiv**: [2607.28457](https://arxiv.org/abs/2607.28457)
- **PDF**: https://arxiv.org/pdf/2607.28457
- **详细分析**: [[20_Research/Papers/强化学习/SVR_Self-Verifying_Refinement_via_Joint_Verdict-Confidence_Reinforcement_Learning_for_Adaptive_Test-Time_Compute|SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute]]
- **作者**: Hongyu Chen, Liang Lin, Guangrun Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：C3RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling test-time computation can improve language-model reasoning, but uniform budgets waste computation on easy inputs, while verifier-guided refinement relies on external feedback. We introduce Self-Verifying Refinement (SVR), an oracle-free multi-turn reinforcement learning framework that learns to use self-verification as a compute-control policy. At each turn, the model produces a solution together with a discrete correctness verdict and a confidence score; it retains the current answer only when the verdict is Correct and confidence exceeds a threshold, and otherwise continues refinement using its own self-verification. Ground-truth correctness is used only to construct training rewards and is never exposed to the policy through refinement prompts or required at inference. SVR is trained with GRPO on fixed-horizon trajectories using rewards that promote solution correctness, calibration-aware self-verification, and stop-ready correct states; adaptive stopping is activated only at inference. On seven mathematical reasoning benchmarks with Qwen3.5-2B, SVR achieves a macro-average accuracy of 0.563 with only 2.99 inference turns on average. In the evaluated complete-system comparison, it exceeds standard GRPO, strong multi-turn baselines, and a fixed-budget oracle-guided score-feedback reference while requiring substantially fewer turns than fixed ten-turn inference. These results demonstrate that learned self-verification can serve as an effective internal control signal for answer retention and adaptive test-time compute allocation.

</details>

---
