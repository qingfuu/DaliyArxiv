# cs.AI | Artificial Intelligence | 2026-10-26

#arxiv #ComputerScience

**论文数**: 38

### [[20_Research/Papers/具身智能/SceneBloom_Agentic_Indoor_Environment_Generation_with_Realistic_and_Diverse_Layouts_for_Embodied_Learning|SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning]]

![[assets/2610.32978_first_page.png|800]]

- **arXiv**: [2610.32978](https://arxiv.org/abs/2610.32978)
- **PDF**: https://arxiv.org/pdf/2610.32978
- **详细分析**: [[20_Research/Papers/具身智能/SceneBloom_Agentic_Indoor_Environment_Generation_with_Realistic_and_Diverse_Layouts_for_Embodied_Learning|SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning]]
- **作者**: Yuhan Liu, Lianhui Qin, Shenji Wan
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training generalizable embodied agents requires realistic, varied, and simulation-ready indoor environments. Language-guided methods support semantic planning and object-level reasoning, but precise spatial grounding remains difficult. Visual generative models offer rich priors over plausible arrangements, yet their outputs require geometric reasoning to become physically valid 3D scenes. We introduce SceneBloom, an agentic framework that combines visual layout sampling with contract-guided 3D compilation. A hierarchical sampler uses diffusion priors to generate furniture arrangements within functional zones. A compiler then uses relations extracted from each proposal to guide geometric fitting and local pose correction. Across five room types, SceneBloom attains the highest visual quality and physical stability among the compared methods and is the only method with no detected mesh collisions and out-of-bounds objects. Its layouts are also closer to the distribution of real rooms than those of all compared baselines. Object navigation policies trained in these realistic scenes achieve a higher success rate in held-out real scans than those trained on an equal number of real training scans. Code is available at https://github.com/Tinaliu0123/scenebloom.

</details>

---

### [[20_Research/Papers/具身智能/RobustRLlib_A_Unified_Library_and_Benchmark_for_Robust_Reinforcement_Learning_Algorithms|RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms]]

![[assets/2610.32971_figure.png|800]]

- **arXiv**: [2610.32971](https://arxiv.org/abs/2610.32971)
- **PDF**: https://arxiv.org/pdf/2610.32971
- **详细分析**: [[20_Research/Papers/具身智能/RobustRLlib_A_Unified_Library_and_Benchmark_for_Robust_Reinforcement_Learning_Algorithms|RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms]]
- **作者**: Xi Chen, Fengqi Hu, Zeyu Shen, Jiaying Xu, Shangding Gu, Pan Xu, Anqi Liu, Laixi Shi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.52（加权：具身智能 0.9，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RARL, RORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust reinforcement learning (RL) is critical for reliable real-world deployment, where policies may fail under diverse shifts and disruptions. Existing robust RL algorithms offer a rich set of mechanisms and principles, yet two major barriers limit their broader potential: limited algorithm reusability and an unclear empirical capability boundary. We introduce RobustRLlib, an algorithm-centric library and benchmark that addresses both challenges. It integrates 17 representative robust online, offline, and safe RL algorithms under a unified interface for substantially improved reusability, together with an enhanced evaluation platform spanning diverse real-world shifts and advanced humanoid and vision-language-action tasks. Systematic evaluation over 273 perturbation configurations provides an up-to-date capability map of current robust RL algorithms, revealing where they remain effective and where substantial robustness gaps persist. As an open-source, user-friendly platform, RobustRLlib offers a reproducible and extensible codebase for applying existing methods to new problems and developing new robust RL algorithms.

</details>

---

### [[20_Research/Papers/具身智能/DexPort_A_Hand-Held_Skill_Interface_for_Dexterous_Hand_Data_Collection|DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection]]

![[assets/2610.32969_figure.png|800]]

- **arXiv**: [2610.32969](https://arxiv.org/abs/2610.32969)
- **PDF**: https://arxiv.org/pdf/2610.32969
- **详细分析**: [[20_Research/Papers/具身智能/DexPort_A_Hand-Held_Skill_Interface_for_Dexterous_Hand_Data_Collection|DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection]]
- **作者**: Amber Xie, Jiawei Fu, Xiaofeng Guo, Carmelo Sferrazza, Guanya Shi, Haozhi Qi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting high-quality demonstrations remains a central bottleneck for learning dexterous manipulation. Teleoperation records executable robot actions, but it requires a complete robot setup and places the burden of coordinating many finger joints on the operator. Human demonstrations are easier to collect, but their motions must be estimated and retargeted to the robot, and they do not directly provide robot actions. In this paper, we introduce DexPort, a portable data-collection interface for high-DoF robot hands. It uses the same hand hardware for collection and deployment, avoiding a hand embodiment gap, and records both commanded joint targets and measured joint states. Our key observation is that a small set of skills can support a wide range of dexterous tasks. During collection, the operator moves the hand-held interface to specify the robot wrist motion and selects or adjusts skills that coordinate the finger motion. This removes the need to control each joint independently while retaining behaviors such as precise grasping and in-hand manipulation. We collect demonstrations across several real-world tasks and in unstructured environments without a robot arm. We then use behavior cloning to train visuomotor policies directly on the recorded wrist motions and hand commands, without skill labels. We evaluate across 4 tasks: pick-and-place with diverse objects, screwing with in-hand tool use, drawer stowage which requires simultaneous grasp and pulling, and a bimanual scanning task. We collect over 2,500 demonstrations with our portable device, in both laboratory and in-the-wild settings. Across our tasks, we see an improvement from 11% to 64% when using recorded robot commands instead of states, and an improvement from 36% to 78% for task success when using in-the-wild data.

</details>

---

### [[20_Research/Papers/大模型/Do_True_and_False_Add_Up_to_One_Complement_Consistency_in_LLM-Agent_Opinion_Simulations|Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations]]

![[assets/2610.32874_figure.png|800]]

- **arXiv**: [2610.32874](https://arxiv.org/abs/2610.32874)
- **PDF**: https://arxiv.org/pdf/2610.32874
- **详细分析**: [[20_Research/Papers/大模型/Do_True_and_False_Add_Up_to_One_Complement_Consistency_in_LLM-Agent_Opinion_Simulations|Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations]]
- **作者**: Anouar Imel, Jin Qi
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion Simulations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In LLM-agent opinion simulations, each agent reports the probability that a claim is true after seeing its own previous probability and the probabilities reported by its neighbors, and that number becomes its state in the next round. If the number describes the agent's position rather than the sentence it was shown, then rewriting the claim as its complement and replacing every probability p with 1 - p should return the complementary answer, so the two reports should sum to one. We test this with three small open models: Qwen3-4B, Llama-3.2-3B and Gemma-3-4B. On 2,304 agent states taken from a running network simulation, Qwen's paired reports sum to 1.18 on average, and on 48 real fact-checking claims from AVeriTeC they again exceed one. A controlled benchmark of 24 worlds, each with exactly two possible outcomes, shows the same failure in all three models. The discrepancy is two to ten times larger than the change produced by a same-meaning paraphrase, and it persists under repeated sampling and across peer group sizes and report strengths. When the reports are fed back into two populations that start from complementary states, the populations do not remain mirror images: their divergence is positive after five rounds for every model. Averaging each answer with the complement of its paired answer restores consistency by construction and lowers Brier loss averaged over the two wordings, but at the final round it beats the better of the two original wordings for only one of the three models. A schedule-by-targeting experiment on the same model gives a small, stable interaction because such sweeps keep the claim wording fixed. Consistency under rewording therefore needs its own test before simulated probabilities are read as beliefs

</details>

---

### [[20_Research/Papers/具身智能/Reimagining_Enterprise_RAG_for_Multi-Agent_Systems_A_Knowledge_Layer_That_Organizes_Before_It_Retrieves|Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves]]

![[assets/2610.32851_figure.png|800]]

- **arXiv**: [2610.32851](https://arxiv.org/abs/2610.32851)
- **PDF**: https://arxiv.org/pdf/2610.32851
- **详细分析**: [[20_Research/Papers/具身智能/Reimagining_Enterprise_RAG_for_Multi-Agent_Systems_A_Knowledge_Layer_That_Organizes_Before_It_Retrieves|Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves]]
- **作者**: Garima Agrawal, Prasun Das, Akshay Sarvade, Priyanka L, Minisha N, Sravani Joshna, Hemath Manivannan, Lavanya Korada, Sambhrit Pattanayak, Srashti Gupta, Siddu R, Prasad Kalyanasundaram
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocabulary, related in name but operationally distinct, so one end-to-end journey implicates over a thousand near-identical rules that must not be conflated. Flat vector retrieval fails, returning an identical rule from the wrong service at high similarity with no signal of error. Content-level ontology, the traditional remedy, did not exist, and relating every occurrence of recurring entities would have cost more than the engagement and not survived a release cycle. We place the ontology at the artifact level. In this machine-generated corpus, each artifact retains its producer, component, service, domain and type, provenance that disambiguates before content is read. We present a knowledge layer that organizes before retrieving: a self-describing catalog, a sparse metadata registry, and a navigation hypergraph defined over artifacts rather than extracted entities. Queries resolve to artifact identifiers that constrain vector search, so the competing rule from another service is absent rather than outranked, making disambiguation structural, not statistical. Built in under a week and admitting new services by convention, the layer serves SDLC agents, developers, quality engineers and analysts. It supported root-cause analysis and resolution of 100+ production defects with developer verification and attributed 35 release regression failures to specific rules and services.

</details>

---

### [[20_Research/Papers/大模型/ActionRAG_Evidence-Refining_Graph_Diffusion_for_Long-Term_Memory_in_LLM_Agents|ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents]]

![[assets/2610.32752_first_page.png|800]]

- **arXiv**: [2610.32752](https://arxiv.org/abs/2610.32752)
- **PDF**: https://arxiv.org/pdf/2610.32752
- **详细分析**: [[20_Research/Papers/大模型/ActionRAG_Evidence-Refining_Graph_Diffusion_for_Long-Term_Memory_in_LLM_Agents|ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents]]
- **作者**: Navyansh Mahla, Sashank Vandrangi
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. We evaluate ActionRAG on MemoryAgentBench (MAB), which tests accurate retrieval, conflict resolution, long-range understanding, and test-time learning. Across its eight deterministic-scoring columns, ActionRAG achieves 55.1 average accuracy, improving over the strongest retrieval-based memory baseline by 5.4 points. Under MAB's query-time cost accounting, mean synthesis cost stays below \$0.001 per query on the four reported cost columns, and the sum of separately measured retrieval-side p99 components is 440.7 ms on our consumer Apple Silicon setup.

</details>

---

### [[20_Research/Papers/世界模型/Adaptive_World-Models_for_Anomaly_Recognition_(AWARE)_A_Framework_for_Robot_Dynamics_Prediction_and_Introspection|Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection]]

![[assets/2610.32742_figure.png|800]]

- **arXiv**: [2610.32742](https://arxiv.org/abs/2610.32742)
- **PDF**: https://arxiv.org/pdf/2610.32742
- **详细分析**: [[20_Research/Papers/世界模型/Adaptive_World-Models_for_Anomaly_Recognition_(AWARE)_A_Framework_for_Robot_Dynamics_Prediction_and_Introspection|Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection]]
- **作者**: Luke Beddow, George Mavroghenis, Rodrigo Chacon Quesada, Kamil Dreczkowski, Cong Sun, Jiankai Wang, Oscar Kwong-Fai Pang, Antoine Cully
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unrecognized anomalies in critical infrastructure can rapidly cascade into catastrophic physical or operational failures. Current anomaly detection approaches often rely on direct access to the monitored system by utilizing onboard sensors, such as motor encoders, to detect anomalous states. However, legacy hardware often lacks these sensors, or strict security protocols may prohibit access altogether. We therefore present AWARE, a world model framework that is capable of anomaly detection using only external camera monitoring via system dynamics estimation and state prediction. Evaluated across 240 real-world robotic crane trajectories, including payload collisions and motor degradations, AWARE demonstrates a 26% improvement in anomaly classification over our strongest baseline under noisy, camera-only state estimation. Furthermore, the inferred dynamics parameter can be decoded to identify the source of faults, localizing the degrading motor with 88% accuracy.

</details>

---

### [[20_Research/Papers/机器人/Conditional_Neural_Processes_for_Self-Supervised_Goal_Discovery_in_Action_Imitation|Conditional Neural Processes for Self-Supervised Goal Discovery in Action Imitation]]

![[assets/2610.32688_figure.png|800]]

- **arXiv**: [2610.32688](https://arxiv.org/abs/2610.32688)
- **PDF**: https://arxiv.org/pdf/2610.32688
- **详细分析**: [[20_Research/Papers/机器人/Conditional_Neural_Processes_for_Self-Supervised_Goal_Discovery_in_Action_Imitation|Conditional Neural Processes for Self-Supervised Goal Discovery in Action Imitation]]
- **作者**: Marco Gabriele Fedozzi, Yukie Nagai, Francesco Rea, Alessandra Sciutti
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Conditional Neural Processes for Self-Supervised Goal Discovery in Action Imitation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inspired by infants' ability to learn novel tasks by imitating others, in this work we evaluate to what extent Conditional Neural Processes can autonomously learn representations of actions that are informative about their underlying goal. We show that the addition of an attention mechanism in the hidden space fosters the emergence of robust goal representations early on in the observation of an action sequence, making it a promising model for a robotic self-supervised general learner.

</details>

---

### [[20_Research/Papers/具身智能/Retiming_Robot_Demonstrations_with_a_Learned_Speed_Prior|Retiming Robot Demonstrations with a Learned Speed Prior]]

![[assets/2610.32676_figure.png|800]]

- **arXiv**: [2610.32676](https://arxiv.org/abs/2610.32676)
- **PDF**: https://arxiv.org/pdf/2610.32676
- **详细分析**: [[20_Research/Papers/具身智能/Retiming_Robot_Demonstrations_with_a_Learned_Speed_Prior|Retiming Robot Demonstrations with a Learned Speed Prior]]
- **作者**: Seungyong Moon, Deokjae Lee, Hansang Lee, Munkhtselmeg Battsengel, Youngin Kim, Seonghyeon Yun, Sungjin Jeon, SongEun Kim, Jeongmin Park, Hyun Oh Song
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Retiming Robot Demonstrations with a Learned Speed Prior》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Realtime-VLA, TempoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The pace of a robot demonstration is often determined by the teleoperator rather than by the task itself. As a result, the same motion can appear at widely different speeds across demonstrations, and policies trained on such data may inherit operator-specific timing along with task behavior. We propose to learn a speed prior directly from large-scale demonstration data. Given a task instruction, a motion path and the images along it, it predicts a distribution over execution speed along the path, from which a chosen quantile defines a consistent clock for retiming each demonstration. Existing methods derive the acceleration signal from the very data they accelerate, so each new task costs another fit, annotation, or pair of predefined rates. A single trained speed prior instead covers every task in a corpus. We fit a speed prior on both robot teleoperation data and handheld demonstrations in which a human arm, rather than a robot arm, moves the gripper, and use it to retime robot demonstrations to the handheld pace before fine-tuning a vision-language-action policy. For execution, we pair the policy with a real-time optimal-control layer that tracks predicted action chunks under robot constraints using the predicted pace. On 120 RoboLab tasks, policies fine-tuned on our learned clocks succeed more often and move with up to half the jerk compared with policies fine-tuned on the original demonstration timing and uniformly accelerated to the same speed. On a real robot, our policy stacks cups in 3.50s, 1.72$\times$ faster than the default policy's 6.02s while succeeding as often, in 29 of 30 trials. Videos and further material are available at https://mllab.snu.ac.kr/projects/learned_speed_prior.

</details>

---

### [[20_Research/Papers/机器人/Can_AI_Agents_Help_Robotic_Engineers_Lessons_from_Two_Focus_Days_in_Industry|Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry]]

![[assets/2610.32636_first_page.png|800]]

- **arXiv**: [2610.32636](https://arxiv.org/abs/2610.32636)
- **PDF**: https://arxiv.org/pdf/2610.32636
- **详细分析**: [[20_Research/Papers/机器人/Can_AI_Agents_Help_Robotic_Engineers_Lessons_from_Two_Focus_Days_in_Industry|Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry]]
- **作者**: Salim Fares, Steffen Herbold
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，机器人 0.8）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software developers increasingly use AI agents that execute multi-step programming tasks on their own. However, it is unclear if and how this transfers to robotic engineering, where engineers program industrial robots in niche, vendor-specific languages and rely on visual feedback from simulation tools. Within this paper, we report a case study on the use of AI agents by an SME that programs industrial robots. Our results show that the agent did not make the engineers more productive, with the exception of a task that required the generation of highly repetitive code. However, the results with the agent improved over time, as the engineers learned how to use it and the agent was adapted to the domain. Moreover, the experience with AI mattered more for the success with the agent than the experience with robotic engineering. This shows that AI agents are not a plug-and-play solution. Instead, companies must train their engineers on the usage of agents, plan time for a learning curve, and ensure that agent configurations match the domain and developer requirements. The strong learning curve we observed further implies that studies on productivity gains with AI should be longitudinal, as they otherwise miss how engineers adopt agents in practice.

</details>

---

### [[20_Research/Papers/大模型/Tool-Calling_LLM_Agents_Under_Realistic_MCP_Faults_Scale_Does_Not_Purchase_Fault_Tolerance|Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance]]

![[assets/2610.32555_figure.png|800]]

- **arXiv**: [2610.32555](https://arxiv.org/abs/2610.32555)
- **PDF**: https://arxiv.org/pdf/2610.32555
- **详细分析**: [[20_Research/Papers/大模型/Tool-Calling_LLM_Agents_Under_Realistic_MCP_Faults_Scale_Does_Not_Purchase_Fault_Tolerance|Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance]]
- **作者**: Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MCPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware fault-injection middleware that interposes on the MCP tool-call path with controlled persistence (permanent, transient, intermittent) and seedable schedules. Its fault model is calibrated to the observed incident distribution (failure mode x persistence) of the public MCP ecosystem, mined from 57,240 issue and pull-request threads across 1,774 open-source MCP repositories. In a 1,350-cell experiment crossing two backbone sizes (20B, 120B), three agent stacks (custom multi-round plan-and-execute, OpenAI Agents SDK, LangChain), and three fault injection conditions, we find that faults drawn from this permanent-heavy stress profile cause severe quality degradation (task-completion score falls by 60%, from 8.08 to 3.23 out of 10), and that scale does not purchase fault tolerance for the two gpt-oss backbones we test: the 120B retains no larger share of its fault-free score under faults (resilience-ratio model, $p = 0.96$), and its completion rate under faults is, if anything, lower (91.1% vs. 95.6%; difference 4.4 points, 95% CI $[-0.2, 9.3]$). Agent stacks differ in how well they absorb faults, which suggests that framework-level error handling matters more than model scale. These results demonstrate that capability benchmarks alone can mask operational brittleness, motivating protocol-aware fault injection as a complementary evaluation dimension for tool-calling agents.

</details>

---

### [[20_Research/Papers/大模型/When_Agents_Fail_Model_or_Harness--Who's_to_Blame|When Agents Fail: Model or Harness--Who's to Blame?]]

![[assets/2610.32483_figure.png|800]]

- **arXiv**: [2610.32483](https://arxiv.org/abs/2610.32483)
- **PDF**: https://arxiv.org/pdf/2610.32483
- **详细分析**: [[20_Research/Papers/大模型/When_Agents_Fail_Model_or_Harness--Who's_to_Blame|When Agents Fail: Model or Harness--Who's to Blame?]]
- **作者**: Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, Jingping Wang, Chunjiang Mu, Chen Zhang, Yang Chen, Bo Zhang, Shuyue Hu
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《When Agents Fail: Model or Harness--Who's to Blame?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Harness-Bench, LOCA-Bench, Terminal-Bench, VitaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measures: (i) Valid Completion Rate (VCR), how reliably agents finish normally and deliver evaluable results, irrespective of task correctness; (ii) Model-Harness Fit, how well a harness supports task achievement through valid completion for a given model; (iii) Cross-Model Fit, a harness's overall suitability across evaluated models; (iv) Interaction Residuals, pairing-specific execution strengths and weaknesses hidden by component-level summaries; and (v) Token Load, the token demands of agent execution, including failed attempts. We evaluate four general-purpose harnesses (OpenCode, Codex CLI, Pi CLI, and DeepAgents) with four core models, plus two fixed native model-harness systems, on six benchmarks covering context management, tool use, long-context planning, multimodal interaction, and artifact handoff. Including native references and stress conditions, 111 evaluation settings yield 52,168 trajectories. Harness rankings vary across models and benchmarks; task performance and valid completion can favor different pairings, and similar task scores can accompany distinct execution profiles. OpenCode ranks first in cross-model performance, while DeepSeek V4 Flash Preview maintains consistently high Mean VCR across harnesses on the shared four-benchmark panel. These findings support evaluating model-harness interactions, training transferable harness-use capabilities in models, and harness designs adapted to the model and task.

</details>

---

### [[20_Research/Papers/大模型/CauProphet_Teaching_Agents_to_Develop_Causal_Cognition_like_Humans|CauProphet: Teaching Agents to Develop Causal Cognition like Humans]]

![[assets/2610.32477_figure.png|800]]

- **arXiv**: [2610.32477](https://arxiv.org/abs/2610.32477)
- **PDF**: https://arxiv.org/pdf/2610.32477
- **详细分析**: [[20_Research/Papers/大模型/CauProphet_Teaching_Agents_to_Develop_Causal_Cognition_like_Humans|CauProphet: Teaching Agents to Develop Causal Cognition like Humans]]
- **作者**: Kaiwen Wu, Chaochao Lu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《CauProphet: Teaching Agents to Develop Causal Cognition like Humans》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlphaBench, AppWorld, FutureSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. Inspired by human causal cognition, we introduce CauProphet, an agent that develops and updates causal knowledge within its Causal Cognition. For each task, CauProphet combines relevant knowledge in Causal Cognition with current evidence to construct a Causal Belief, a structured belief capturing causal factors and the effects of possible actions. It uses this belief for decision-making and continuously updates both the belief and Causal Cognition as new observations emerge, enabling causal knowledge that persists beyond individual experiences. Evaluations demonstrate that CauProphet progressively acquires causal knowledge and transfers it to future decision-making. In financial research, CauProphet leverages prior discoveries to improve downstream analyses and outperforms all baselines in mean rank correlation with next-day returns, achieving a 25.4% improvement over a baseline agent. It also improves prediction accuracy from 21.3% to 28.6% in dynamic real-world settings. Further experiments validate its ability to perform reliable causal analysis and action selection across scientific and everyday tasks, demonstrating the potential of causal experience learning for next-generation LLM agents.

</details>

---

### [[20_Research/Papers/具身智能/When_to_Stop_Penalizing_Actions_Martingale_GRPO_for_VLA_Reinforcement_Learning|When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning]]

![[assets/2610.32431_figure.png|800]]

- **arXiv**: [2610.32431](https://arxiv.org/abs/2610.32431)
- **PDF**: https://arxiv.org/pdf/2610.32431
- **详细分析**: [[20_Research/Papers/具身智能/When_to_Stop_Penalizing_Actions_Martingale_GRPO_for_VLA_Reinforcement_Learning|When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning]]
- **作者**: Zongyao Zhao, Cheng-Jie Zhao, Ruihang Jiang, Bing Zheng, Zhaolin Wang, Yuanwei Liu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.3，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning》归入 具身智能、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A failed vision-language-action (VLA) rollout does not imply that every action contributed to failure. Yet in group-relative policy optimization (GRPO), a single trajectory-level advantage is assigned to all actions in a rollout. Potentially useful recovery attempts can thus be penalized alongside the errors they aim to correct. Ideal stopping conditions for failure feedback are characterized using success-probability and policy-score martingales. At these stops, the removed gradient contribution has zero conditional expectation given the retained information. Truncation therefore preserves the expectation of a reference GRPO group-gradient estimator and can reduce its covariance. One such stop occurs when the conditional probability of success is zero, motivating error and recovery cues for selecting candidate feedback boundaries. Martingale GRPO (MART-GRPO) is introduced with a vision-language model (VLM) for event-guided truncation. The VLM is fine-tuned on our annotated training set using low-rank adaptation (LoRA). The last visible error without observed recovery is localized by the frozen VLM in complete rollout videos. Failure feedback is retained through the selected error interval and removed afterward, while successful-rollout loss terms and original loss normalization are preserved. For retrospective boundaries, changes in expectation and variance are analyzed to assess departures from ideal stopping. Experiments with OpenVLA-OFT on RoboTwin 2.0 show that MART-GRPO improves success rates over full-trajectory GRPO across multiple tasks.

</details>

---

### [[20_Research/Papers/大模型/Async-RBench_Benchmarking_Asynchronous_Task_Execution_in_LLM_Agents|Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents]]

![[assets/2610.32429_figure.png|800]]

- **arXiv**: [2610.32429](https://arxiv.org/abs/2610.32429)
- **PDF**: https://arxiv.org/pdf/2610.32429
- **详细分析**: [[20_Research/Papers/大模型/Async-RBench_Benchmarking_Asynchronous_Task_Execution_in_LLM_Agents|Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents]]
- **作者**: Detao Zeng, Guilin Ou, Nuo Chen, Yunhao Feng, Hongliang Wang, Qinli Yang, Junming Shao, Zhong Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentChangeBench, AppWorld, Async-RBench, InterruptBench, MultiAgentBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat, while avoiding prohibited changes. Final task success alone does not reveal whether these results were handled correctly, and natural asynchronous arrivals are hard to reproduce. We introduce Async-RBench, a benchmark for asynchronous task execution in LLM agents, with 200 executable tasks covering eight scenarios. A scenario controller regulates result delivery using predefined task-state conditions, while an Event Response Contract (ERC) specifies what each response must change, preserve, avoid, and re-verify. The Dynamic Replanning Score (DRS) weights the response process and outcome equally and is reported separately from task success. We evaluate nine agents and find DRS scores of 19.2 to 45.1, with the lowest scores on duplicate reports and subagent failures. Under our execution protocol, all nine agents obtain lower task success with asynchronous than with batched delivery (26.0% vs. 29.7% on average). For three agents, prompting the main agent to rebuild its plan after every result improves DRS by only 2.6 to 3.5 points. Together, these findings highlight the challenges of reliable asynchronous task execution and the need to evaluate how agents handle incoming results alongside end-to-end task success.

</details>

---

### [[20_Research/Papers/大模型/LeafSkill_Efficient_Leaf-Level_Action_Grounding_for_Recursive_LLM_Agents|LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents]]

![[assets/2610.32412_figure.png|800]]

- **arXiv**: [2610.32412](https://arxiv.org/abs/2610.32412)
- **PDF**: https://arxiv.org/pdf/2610.32412
- **详细分析**: [[20_Research/Papers/大模型/LeafSkill_Efficient_Leaf-Level_Action_Grounding_for_Recursive_LLM_Agents|LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents]]
- **作者**: Shen Liu, Ze Zhou, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recursive large language model (LLM) agents solve long-horizon tasks through decomposition, execution, and environmental feedback. Yet after producing an atomic subtask, they often invoke the same large model again to translate a familiar instruction into an executable action. We observe that high-level planning is task-specific, whereas leaf-level action grounding recurs across tasks and can be checked against environment-admitted actions. We introduce LeafSkill, an external reuse layer that retrieves semantically related grounding experience, binds action templates to current objects and admissible actions, and uses a lightweight 1.7B selector to choose a bound action or defer the unchanged subtask to the original agent. Skills remain outside the model parameters, allowing a frozen selector to use post-training additions. Under lexical and syntactic paraphrases, exact matching retrieves none of the reference actions, while semantic retrieval preserves 96.0% and 97.0% candidate coverage; the frozen selector adopts 97.34% of unseen skill types. On an independent confirmation set of 200 Robotouille tasks, LeafSkill completes 137 tasks versus 121 for ReCAP (68.5% vs. 60.5%, exact McNemar p=.0259). On the 106 tasks completed by both, it reduces Qwen3.5-27B tokens by 14.42% and calls by 14.08%. A separate held-out repeat yields a consistent 9.0-point success gain and 18.98% token reduction. Reusable leaf grounding can thus improve task completion while reducing host-model inference without replacing high-level planning.

</details>

---

### [[20_Research/Papers/大模型/Adaptive_Control_of_Scientific_Instruments_with_Nonstationary_Responses_through_Multimodal_Agents|Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents]]

![[assets/2610.32370_figure.png|800]]

- **arXiv**: [2610.32370](https://arxiv.org/abs/2610.32370)
- **PDF**: https://arxiv.org/pdf/2610.32370
- **详细分析**: [[20_Research/Papers/大模型/Adaptive_Control_of_Scientific_Instruments_with_Nonstationary_Responses_through_Multimodal_Agents|Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents]]
- **作者**: Guoyang Shi, Hongwen Li, Yiding Yu, Zhuang Fu, Siqi Ding, Zhengyuan Chen, JianGuo Chen, Hanyue Zhao, Tianyuan Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controlling scientific instruments requires parameters to be adjusted progressively in response to feedback from successive operations. When unobserved operating conditions evolve with operational history, responses become nonstationary, and a static mapping from actions to responses becomes inadequate for decisions across shots. Shot-to-shot tuning of neutral beam injection (NBI) ion sources in magnetic confinement fusion devices is representative of this class of problems: the conditions of electrode surfaces and vacuum are difficult to observe directly, discharge outcomes vary between shots, and experiments are costly and carry operational risks. We propose a physically grounded multimodal agent with three independently auditable components. Deterministic algorithms extract symbolic physical quantities and visual evidence from multichannel waveforms; a memory with two layers organizes trajectories from the current task, experience from earlier tasks, and procedural knowledge, from which a multimodal large language model (MLLM) generates candidate actions; and an independent action feasibility check enforces action constraints before execution. In a strictly chronological replay of 455 shots from four EXL-50U platforms, physical symbols alone outperformed waveform images alone by 0.21-0.32 in macro-F1 for quality classification across all four evaluated models. Retrieved context increased the mean agreement with historical action directions by 22.4-42.7 percentage points, whereas the contribution of visual evidence varied across models. Under supervised operation on five ion sources, the system achieved a beam-extraction rate of 86.80% across 409 executed shots. These results demonstrate the engineering feasibility of the framework for supervised sequential tuning on a physical scientific instrument.

</details>

---

### [[20_Research/Papers/大模型/TGR-EvoDAG_A_DAG-based_Multi-Agent_Code_Evolution_Framework_for_Generative_Recommendation_on_Tencent|TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent]]

![[assets/2610.32326_first_page.png|800]]

- **arXiv**: [2610.32326](https://arxiv.org/abs/2610.32326)
- **PDF**: https://arxiv.org/pdf/2610.32326
- **详细分析**: [[20_Research/Papers/大模型/TGR-EvoDAG_A_DAG-based_Multi-Agent_Code_Evolution_Framework_for_Generative_Recommendation_on_Tencent|TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent]]
- **作者**: Junlin He, Junzhang Zhu, Yudong Li, Yihong Tang, Xuefeng Jiang, Wei Ma, Chengxiang Zhuo, Zang Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have enabled automated code evolution for algorithm discovery. However, current recursive self-improvement (RSI) research for sequential recommendation faces a dilemma: general-purpose frameworks lack domain-specific feedback, while recommender-specific frameworks rely on linear evolution. Crucially, naively integrating them fails when applied to Generative Recommendation (GR). Unlike end-to-end models, GR relies on a module-cascaded pipeline (tokenization, pre-training, and alignment). In this paradigm, existing evolution methods suffer from: i) cost blindness, squandering budgets by ignoring stage-asymmetric retraining overheads; and ii) short-sighted evaluation, discarding promising upstream innovations that temporarily regress metrics before downstream adaptation. To bridge these gaps, we propose TGR-EvoDAG, a multi-agent code evolution framework tailored for GR. TGR-EvoDAG models code evolution as a Directed Acyclic Graph (DAG) to maintain multiple evolution branches and merge complementary innovations, unifying advanced search with rich GR diagnostic feedback. We further introduce stage-aware cost planning to optimize GPU-hour budgets, and active downstream co-adaptation to navigate temporary regressions and unlock cross-stage gains. On public Amazon datasets, TGR-EvoDAG enables the first autonomous evolution of a complete GR pipeline, improving offline metrics by up to 37.4% and Agent4Rec simulated user satisfaction by 19.7% over the strongest baseline. Furthermore, in industrial deployment on Tencent's large-scale commercial media platform, the evolved GR achieves a 12.16% relative improvement in offline Hit@1 and a statistically significant 0.40% increase in online click-through rate (CTR).

</details>

---

### [[20_Research/Papers/大模型/From_Visual_Affinity_to_Learning_Credit_in_Multimodal_Reinforcement_Learning|From Visual Affinity to Learning Credit in Multimodal Reinforcement Learning]]

![[assets/2610.32324_figure.png|800]]

- **arXiv**: [2610.32324](https://arxiv.org/abs/2610.32324)
- **PDF**: https://arxiv.org/pdf/2610.32324
- **详细分析**: [[20_Research/Papers/大模型/From_Visual_Affinity_to_Learning_Credit_in_Multimodal_Reinforcement_Learning|From Visual Affinity to Learning Credit in Multimodal Reinforcement Learning]]
- **作者**: Yuhang Han, Dingning Liu, Yujie Chen, Yaojie Zhang, Jingwei Song, Zequn Yang, Xuanming Shang, Li Ding, Zhijiang Guo, Linfeng Zhang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《From Visual Affinity to Learning Credit in Multimodal Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：A-OKVQA, ChartQA, ERQA, EmbSpatial-Bench, RxnBench, ScienceQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) improves multimodal reasoning, but uniformly assigning a single response-level advantage to all tokens overlooks the distinct roles of visual observations and subsequent reasoning. Visual affinity alone is insufficient: predictive states may align with both image and prompt-context representations, and upweighting valid visual observations can amplify their negative-advantage updates when later reasoning fails. To address this issue, we propose \textbf{Outcome-Conditioned Visual Credit (OVC)}, a plug-in framework that separates visual-association measurement from token-level credit assignment and is adaptable to policy-optimization methods with uniform response-level advantage allocation. Relative Visual Encoding constructs a context-relative visual coordinate by contrasting each predictive state's affinity to image and prompt-context representations. Outcome-conditioned Evidence Calibration combines this coordinate with uncertainty-scaled predictive features and calibrates their contributions to outcome-discriminative evidence through mean contrasts between positive- and negative-advantage responses, scaled by regularized within-side variation. Visual association thus informs credit through observed outcome differences rather than directly determining update priority. Normalized Credit Allocation conditions the calibrated evidence on the response's advantage sign to produce positive token weights with unit global mean. These detached weights preserve advantage signs while modulating individual token-gradient contributions. OVC reuses existing rollouts without auxiliary reward models, process annotations, or inference-time modules. Instantiated through GSPO-token, OVC retains sequence-level clipping and consistently improves six-benchmark mean accuracy over GSPO across three models, with gains of 1.86-2.39 percentage points.

</details>

---

### [[20_Research/Papers/强化学习/Spatial_Heuristic_Strategy_based_Diffusion_Reinforcement_Learning_for_Online_3D_Bin_Packing|Spatial Heuristic Strategy based Diffusion Reinforcement Learning for Online 3D Bin Packing]]

![[assets/2610.32241_first_page.png|800]]

- **arXiv**: [2610.32241](https://arxiv.org/abs/2610.32241)
- **PDF**: https://arxiv.org/pdf/2610.32241
- **详细分析**: [[20_Research/Papers/强化学习/Spatial_Heuristic_Strategy_based_Diffusion_Reinforcement_Learning_for_Online_3D_Bin_Packing|Spatial Heuristic Strategy based Diffusion Reinforcement Learning for Online 3D Bin Packing]]
- **作者**: Tong Li, Qingyang Xu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《Spatial Heuristic Strategy based Diffusion Reinforcement Learning for Online 3D Bin Packing》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional heuristic methods have accumulated mature experience in core objectives, such as space utilization and layout compactness of 3D bin packing, relying on artificially designed rule-based logic. However, they exhibit obvious limitations in generalization ability and adaptability to dynamic scenarios. Diffusion reinforcement learning, which integrates the spatial search capability of reinforcement learning and the data distribution modeling capability of diffusion learning, has achieved certain progress in action distribution modeling and decision compliance constraints. Nevertheless, there remain issues including insufficient perception of the spatial topological structure in 3D bin packing and limited layout optimization capability. To address these problems, we propose a diffusion reinforcement learning method integrated with spatial heuristic strategies, which combines classical bin packing heuristic rules with a diffusion reinforcement learning framework. Specifically, it compresses the action space through heuristic action pre-screening, introduces a graph neural network to model the spatial structure, and designs a composite reward function incorporating flatness to suppress spatial fragmentation, thereby realizing the organic integration of prior knowledge and adaptive optimization. Experimental results demonstrate that the pro

</details>

---

### [[20_Research/Papers/强化学习/Financial_Context-Rich_Strategy_for_Actor-Critic_based_Agents_A_Deep_Reinforcement_Learning_Approach_for_Stock_Trading|Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading]]

![[assets/2610.32237_figure.png|800]]

- **arXiv**: [2610.32237](https://arxiv.org/abs/2610.32237)
- **PDF**: https://arxiv.org/pdf/2610.32237
- **详细分析**: [[20_Research/Papers/强化学习/Financial_Context-Rich_Strategy_for_Actor-Critic_based_Agents_A_Deep_Reinforcement_Learning_Approach_for_Stock_Trading|Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading]]
- **作者**: Hrishikesh Singh, Aarti Sharma, Millie Pant
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 3.2（加权：大模型 0.4，强化学习 2.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In modern financial markets, more than 3/4th of the large volume trade is executed by algorithmic trading based on advanced trading strategies to attain higher precision and speed than traditional human traders. The conventional strategies focused on price-based indicators are inadequate in capturing the market dynamism arising from real-world events such as social sentiments, political instability, or sudden economic shifts. With the rise of Deep Reinforcement Learning (DRL) and data availability, there is a requirement for more efficient algorithms that can incorporate these external factors in trading strategies. DRL has shown potential in simulating real-world scenarios and in simplifying complex decision-making since DRL agents can automate the trading process i.e. executing trades in a manner comparable to human traders. They have shown reliable performance since they can update their policies based on risk and quantitative factors. In this paper, we propose a DRL approach based on partial and deep-infusion of sentimental analysis. It features distinct policy designs of actor-critic-based agents: only policy optimization (A2C &amp; PPO) and policy optimization along with Q-learning principles (DDPG, TD3 &amp; SAC). Our findings reveal, that the agents based on policy optimization combined with Q-learning, significantly and consistently demonstrate improved performance upon sentiment deep-infusion in profit maximization as well as risk-averse trading.

</details>

---

### [[20_Research/Papers/强化学习/SOPO_Socratic_Guided_Policy_Optimization_for_Span-Level_Hallucination_Detection|SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection]]

![[assets/2610.32212_figure.png|800]]

- **arXiv**: [2610.32212](https://arxiv.org/abs/2610.32212)
- **PDF**: https://arxiv.org/pdf/2610.32212
- **详细分析**: [[20_Research/Papers/强化学习/SOPO_Socratic_Guided_Policy_Optimization_for_Span-Level_Hallucination_Detection|SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection]]
- **作者**: Jiawei Dong, Zilong Bai, Pengtian zhu, Peng Zhou
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HaluEval, PsiloQA, Socratic-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have gained widespread adoption in various natural language processing tasks, but suffer from hallucination issues where they generate unfaithful or inconsistent content. While Reinforcement Learning with Verifiable Rewards (RLVR) has shown promising applications in reasoning tasks, its application to span-level hallucination detection is challenged by localization ambiguity, reward sparsity on hard examples, and uncontrolled length inflation. To address these issues, we introduce Socratic Guided Policy Optimization (SOPO), a multi-turn RL framework for robust hallucination detection. The key innovation of SOPO is a Socratic feedback mechanism, where a teacher model guides the reasoning trajectories during rollout by providing indirect hints inferred from the ground truth. This teacher-guided approach enables the model to generate more effective reasoning trajectories for hard examples, thus alleviating reward sparsity. Furthermore, we incorporate Turn-based Advantage Scaling to penalize verbosity bias, encouraging the model to develop efficient and autonomous reasoning capabilities. Empirical results on RAGTruth demonstrate that SOPO (4B) achieves state-of-the-art performance, surpassing leading proprietary models (e.g., GPT-5) and standard RL baselines, while obtaining higher reported mean scores than GRPO on four out-of-domain benchmarks, with mixed evidence against CAPO. We release our training and evaluation code alongside the 1.7B and 4B SOPO models at https://github.com/patsnap/SOPO.

</details>

---

### [[20_Research/Papers/具身智能/Do_VLAs_Know_They_Will_Fail_Interpretable_Success_and_Failure_Patterns_in_Physical_AI_Systems|Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems]]

![[assets/2610.32208_figure.png|800]]

- **arXiv**: [2610.32208](https://arxiv.org/abs/2610.32208)
- **PDF**: https://arxiv.org/pdf/2610.32208
- **详细分析**: [[20_Research/Papers/具身智能/Do_VLAs_Know_They_Will_Fail_Interpretable_Success_and_Failure_Patterns_in_Physical_AI_Systems|Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems]]
- **作者**: Christian A. Rogers, Qian Lin, Daniel S. Brown
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FPC-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as powerful general-purpose robot policies, but their successes and failures remain difficult to diagnose and understand. In this work, we show that sparse autoencoder (SAE) representations of OpenVLA activations contain outcome-predictive information and can be used to predict task failure before the robot reaches an unrecoverable state. Moreover, to provide insights into what common behaviors may contribute to these outcomes, we identify individual SAE features whose strong activations are associated with specific stages of success or failure, and uncover recurring behavioral patterns by localizing temporal intervals where these features exhibit significant activation changes. We further develop a VLM-based interpretation pipeline to generate behavioral descriptions of these patterns and validate their correspondence to feature activations on held-out intervals.

</details>

---

### [[20_Research/Papers/强化学习/$Ψ$-0.6_Adaptive_Streams_of_Thought_in_a_Unified_Vision-Language_World_Model|$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model]]

![[assets/2610.32177_figure.png|800]]

- **arXiv**: [2610.32177](https://arxiv.org/abs/2610.32177)
- **PDF**: https://arxiv.org/pdf/2610.32177
- **详细分析**: [[20_Research/Papers/强化学习/$Ψ$-0.6_Adaptive_Streams_of_Thought_in_a_Unified_Vision-Language_World_Model|$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model]]
- **作者**: Khai Loong Aw, Klemen Kotar, Baihan Zhang, Yifan Liu, Lilian Chen, Atlas Kazemian, Rahul Venkatesh, Daniel Yamins
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.36，世界模型 0.96）
- **关联关键词**: Multimodal, RL, WorldModel

#### 研究背景与动机

《$Ψ$-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FlowBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans reason about the physical world by flexibly combining different forms of inference as a problem unfolds. Achieving this flexibility is a major open challenge in AI: capabilities often remain separated across specialized models, limiting how they can be composed and jointly adapted to a task. We introduce $Ψ$-0.6, a unified vision-language world model that adaptively composes perception, language, geometry, and simulation within a shared reasoning process we call streams of thought. These streams interleave images, text, and explicit representations of geometry and motion, all of which the model can generate and interpret through a shared token interface. $Ψ$-0.6 surpasses leading open-weight models zero-shot on multi-view spatial reasoning, with further gains from reasoning through geometric intermediates. It also supports counterfactual simulation: generating and interpreting imagined scenes to determine, for example, whether moving an object would obstruct a pathway. Reinforcement learning from task feedback jointly optimizes the selection, generation, and use of intermediate representations, improving visual question-answering accuracy with gains that transfer to unseen benchmarks. $Ψ$-0.6 offers a path toward adaptive physical reasoning -- not only predicting the physical world but also choosing the representations through which to reason.

</details>

---

### [[20_Research/Papers/大模型/The_LLENS_Platform_for_On-Premises_Large_Language_Model_Agents_in_a_Japanese_University_Hospital_Development_and_Evaluation_Study|The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study]]

![[assets/2610.32151_first_page.png|800]]

- **arXiv**: [2610.32151](https://arxiv.org/abs/2610.32151)
- **PDF**: https://arxiv.org/pdf/2610.32151
- **详细分析**: [[20_Research/Papers/大模型/The_LLENS_Platform_for_On-Premises_Large_Language_Model_Agents_in_a_Japanese_University_Hospital_Development_and_Evaluation_Study|The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study]]
- **作者**: Ken Enda, Jien Saito, Masami Mukai, Feng Han, Emir Turkes, Tatsumi Kusakabe, Reona Umeki, Kazuhiro Sumiyoshi, Mitsuya Numata, Takumi Tanikawa, Akira Endoh, Kenji Hirata...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.45（加权：大模型 1.45）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents that use tools could take on part of the electronic health record and desk work that occupies physicians' time, but in many hospitals the medical information systems run inside closed networks, so the model and the agent harness must also sit inside. We designed, implemented, and deployed LLENS, a clinical support AI agent platform that runs inside the closed network of Hokkaido University Hospital on one host with 8 NVIDIA H200 GPUs, the open-weight model Kimi K2.6 (~1 trillion parameters), and a web application rebuilt from Open WebUI. The harness has 10 components, including page image reading, full-text attachment input, a path-addressed document tree without a vector index, a network-isolated sandbox, artifact return, self-checking of generated output, subagents, and saved procedures. Kimi K2.6 was chosen from 3 open-weight candidates and scored 480/500 on the 2026 Japanese Medical Licensing Examination; it generated 119 tokens/s for one user and served 16 concurrent requests at 908 tokens/s in total. On 180 questions over hospital documents (3 seeds each), mean accuracy was 10.7% with no documents, 81.3% with fixed retrieval (top 10 chunks of one lexical search), and 97.2% with interactive access, in which the model reads with document tools and the sandbox (15.9 percentage points above fixed retrieval, 95% CI 10.9-21.3); the difference lay in filtering/counting questions (16.7% vs 87.8%). Five scenarios with synthetic data ran on combinations of the components: needlestick injury response, batch adverse event grading, scanned referral letter transcription, falls data aggregation and plotting, and investigation of 3 topics by subagents. The platform has run on the hospital network since September 14, 2026.

</details>

---

### [[20_Research/Papers/具身智能/TTT_in_VLA_Models_Exploring_Training_with_Human_Demonstrations|TTT in VLA Models: Exploring Training with Human Demonstrations]]

![[assets/2610.32094_figure.jpg|800]]

- **arXiv**: [2610.32094](https://arxiv.org/abs/2610.32094)
- **PDF**: https://arxiv.org/pdf/2610.32094
- **详细分析**: [[20_Research/Papers/具身智能/TTT_in_VLA_Models_Exploring_Training_with_Human_Demonstrations|TTT in VLA Models: Exploring Training with Human Demonstrations]]
- **作者**: Qiangong Zhou, Jiafeng Liang, Yimin Dong, Yang He, Hongxiang Li
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《TTT in VLA Models: Exploring Training with Human Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：InternVLA, RecastVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot tasks require retaining and using past information. We integrate Test-Time Training (TTT), which stores context in fast weights, into InternVLA-A1 and Pi0.5 to study action generation conditioned on human demonstrations through training on paired demonstrations and robot trajectories. We implement memory transfer between the two phases and truncated backpropagation, and examine training objectives, gradient coverage, and contrastive regularization across video, short-video, and single-frame cue tasks. In our experiments, adding TTT and training on paired data at the current scale did not lead to consistent target selection based on demonstrations. Under the tested settings, shorter sequences, full trajectory gradient connectivity, and contrastive regularization did not clearly improve responsiveness to demonstrations. When demonstrations were reduced to single-frame cues, real-robot execution still showed a preference for cups at fixed positions. We document the implementation, training configurations, and observations to support further inspection and replication.

</details>

---

### [[20_Research/Papers/大模型/AgentTrace_Execution-Level_Fingerprinting_of_Black-Box_LLM_Agents|AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents]]

![[assets/2610.32092_figure.png|800]]

- **arXiv**: [2610.32092](https://arxiv.org/abs/2610.32092)
- **PDF**: https://arxiv.org/pdf/2610.32092
- **详细分析**: [[20_Research/Papers/大模型/AgentTrace_Execution-Level_Fingerprinting_of_Black-Box_LLM_Agents|AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents]]
- **作者**: Gejian Zhao, Hanzhou Wu, Xinpeng Zhang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Verifying the provenance of autonomous LLM agents is a critical security challenge. Existing semantic attribution is easily obfuscated by system prompts, while active watermarking conflicts with schema-constrained tool generation. We propose AgentTrace, an active framework that identifies the foundation model behind a black-box agent via observable execution traces. AgentTrace injects structurally ambiguous probes to trigger tokenization-sensitive serialization failures at rigid tool interfaces. While these initial failures provide coarse-grained separation across model families, the temporal sequence of subsequent repair operations reveals fine-grained, model-specific recovery behaviors. By modeling these multi-step trajectories with lightweight Markov chains, AgentTrace achieves 96.0% attribution accuracy under adversarial identity spoofing. Crucially, sequential repair modeling successfully distinguishes the evaluated intra-family variants sharing identical tokenizers (e.g., Llama-3 8B/70B), substantially outperforming unordered behavioral statistics while remaining robust against prompt obfuscation and temperature scaling.

</details>

---

### [[20_Research/Papers/大模型/Behaviour_analysis_for_large_language_model-driven_agents|Behaviour analysis for large language model-driven agents]]

![[assets/2610.32087_first_page.png|800]]

- **arXiv**: [2610.32087](https://arxiv.org/abs/2610.32087)
- **PDF**: https://arxiv.org/pdf/2610.32087
- **详细分析**: [[20_Research/Papers/大模型/Behaviour_analysis_for_large_language_model-driven_agents|Behaviour analysis for large language model-driven agents]]
- **作者**: Tianqiang Yan, Lizhen Qu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Behaviour analysis for large language model-driven agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding language-agent behaviour requires learning how actions are organised across a trajectory and how this organisation relates to context and outcomes. We propose a general framework that connects data-driven behavioural discovery with analysis and experimental investigation. Categories developed from recorded activity define what is measured. Analyses preserve the behaviours' positions in the process and express their relationships as interpretable hypotheses. Statistical assessment and tests in held-out contexts examine the strength and scope of the evidence. Experiments, including prompt steering, then test how behaviour and outcomes change under deliberately varied conditions. A study of iterative self-reflection illustrates how discovery, dependency learning and prompt comparisons can inform one another. We develop this approach for trajectories of varying length, event order and agent roles, and identify advances in coding, analysis and experimentation needed to support its wider use.

</details>

---

### [[20_Research/Papers/具身智能/Understanding_Communication_Failures_in_Multi-Agent_LLM_Systems|Understanding Communication Failures in Multi-Agent LLM Systems]]

![[assets/2610.32060_figure.png|800]]

- **arXiv**: [2610.32060](https://arxiv.org/abs/2610.32060)
- **PDF**: https://arxiv.org/pdf/2610.32060
- **详细分析**: [[20_Research/Papers/具身智能/Understanding_Communication_Failures_in_Multi-Agent_LLM_Systems|Understanding Communication Failures in Multi-Agent LLM Systems]]
- **作者**: Priya Pitre, Jun Hou, Yi Fang, Naren Ramakrishnan, Xuan Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.9）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Understanding Communication Failures in Multi-Agent LLM Systems》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FinQA, HotpotQA, LiveCodeBench, MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems aim to improve reasoning through debate, evidence sharing, and mutual correction, but interaction can also introduce failures that final accuracy alone cannot explain. Agents may converge too early, ignore dissent, suppress correct minority answers, or preserve a wrong framing across rounds. We present a corpus-grounded taxonomy of communication failures, built from 3,211 failed multi-round trajectories across medical QA, coding, finance, multi-hop reasoning, ethics, and embodied text tasks. Using this taxonomy, we analyze failure distributions across datasets and system designs, round-level error dynamics, recovery hardness, majority transitions, minority-signal suppression, and self-reported confidence. We find that failures are dominated by recovery/correction and consensus/decision problems rather than isolated first-round mistakes, with many emerging after agents first observe peer responses. Based on these findings, we recommend stronger disagreement handling, evidence verification, minority-signal preservation, and recovery checks before finalization.

</details>

---

### [[20_Research/Papers/大模型/Do_AI-for-Science_Agents_Preserve_Model_Safety|Do AI-for-Science Agents Preserve Model Safety?]]

![[assets/2610.32045_first_page.png|800]]

- **arXiv**: [2610.32045](https://arxiv.org/abs/2610.32045)
- **PDF**: https://arxiv.org/pdf/2610.32045
- **详细分析**: [[20_Research/Papers/大模型/Do_AI-for-Science_Agents_Preserve_Model_Safety|Do AI-for-Science Agents Preserve Model Safety?]]
- **作者**: Michael Yew Chuan Lee, Manya Sriram, N. Benjamin Erichson
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Do AI-for-Science Agents Preserve Model Safety?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MT-JailBench, SafeSciBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI-for-Science agents are increasingly being used for formulating scientific hypotheses, running autonomous experiments, and interpreting evidence. These agents are constructed by integrating a large language model (LLM) into a domain-specific agent harness, which in turn can improve the LLM's scientific capability and enable the model to orchestrate scientific tools. In this work, we ask whether model safety is preserved when an LLM is integrated in an AI-for-Science agent harness. We evaluate five agent harnesses on 50 harmful chemistry requests. Specifically, we study how the safety behavior changes under direct prompting, two simple adversarial prompting strategies, and an adaptive attack. Across four recent GPT variants, our results show that the agent harness can increase harmful compliance even under direct prompting. More critically, we find that adaptive attacks that are largely unsuccessful against the base LLM suddenly become highly successful after the agent harness is introduced. Our results show that the safety behavior of the base LLM is not durable once a harness is introduced. Thus, as AI-for-Science agents become more capable and autonomous, the community needs to evaluate and align the agent using domain-specific safety benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/PPO_vs._SAC_A_Comparative_Study_for_Cooperative_Motion_Control_of_Dual-Arm_Space_Robots|PPO vs. SAC: A Comparative Study for Cooperative Motion Control of Dual-Arm Space Robots]]

![[assets/2610.32034_figure.png|800]]

- **arXiv**: [2610.32034](https://arxiv.org/abs/2610.32034)
- **PDF**: https://arxiv.org/pdf/2610.32034
- **详细分析**: [[20_Research/Papers/具身智能/PPO_vs._SAC_A_Comparative_Study_for_Cooperative_Motion_Control_of_Dual-Arm_Space_Robots|PPO vs. SAC: A Comparative Study for Cooperative Motion Control of Dual-Arm Space Robots]]
- **作者**: Nasim Fallahiarezoodar, Zheng H. Zhu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.3，强化学习 0.6，机器人 0.2）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《PPO vs. SAC: A Comparative Study for Cooperative Motion Control of Dual-Arm Space Robots》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The growing population of orbital debris has intensified interest in active debris removal and on-orbit servicing, for which dual-arm space manipulators offer improved grasping stability and load distribution relative to single-arm systems. However, coordinating two manipulators under inter-arm collision avoidance, orientation alignment, and sensing uncertainty remains challenging. This paper develops a coordinated reinforcement learning framework for cooperative motion planning of a dual-arm space manipulator in a target-reaching task with inter-arm collision-avoidance constraints. A centralized state representation combines joint-space, end-effector, and target-relative information, while a multi-objective reward function promotes target-reaching accuracy, orientation alignment, motion smoothness, synchronized task completion, and collision avoidance. Within this framework, Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) are compared as representative on-policy and off-policy algorithms, and the learned policies are further evaluated for generalization to previously unseen target configurations. Across five random seeds, SAC substantially outperforms PPO within the considered fixed-base simulation scenarios: it reaches an 80% success threshold in every seed (median 1.6M environment steps) whereas PPO does not reach it within a 4M-step budget, and it attains a higher mean success rate (78.6% versus 7.4%) with lower position and orientation errors and tighter bimanual synchronization. Both algorithms degrade on unseen boundary targets, but SAC retains most of its performance while PPO's collapses. The results also expose a failure mode of PPO: under the two-phase shaped reward, it tends to converge to a reward-loitering local optimum rather than committing to the precision task. This behavior highlights the sensitivity of on-policy learning to reward shaping.

</details>

---

### [[20_Research/Papers/具身智能/CEMIR_vs._FISER_a_comparative_study_of_reasoning-based_and_enrichment-based_approaches_to_pragmatic_intent_recognition|CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition]]

![[assets/2610.32022_figure.png|800]]

- **arXiv**: [2610.32022](https://arxiv.org/abs/2610.32022)
- **PDF**: https://arxiv.org/pdf/2610.32022
- **详细分析**: [[20_Research/Papers/具身智能/CEMIR_vs._FISER_a_comparative_study_of_reasoning-based_and_enrichment-based_approaches_to_pragmatic_intent_recognition|CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition]]
- **作者**: Ziya Hosseynzadeh, Farjad Fallah, Farnoosh Fallah, Soroush Gooran, Mohammad Amanloo, Hossein Sameti
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CEMIR vs. FISER: a comparative study of reasoning-based and enrichment-based approaches to pragmatic intent recognition》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Intent recognition in human-robot interaction requires agents to resolve ambiguous natural language instructions by inferring the speaker's underlying goals. Research has increasingly focused on two notable paradigms for addressing this task: structured symbolic reasoning and multimodal input enrichment. However, it remains unclear whether enrichment-based methods provide benefit in settings where the ambiguity concerns unstated human intent rather than missing observable scene information. In this paper, we present a comparative and diagnostic study benchmarking FISER - a framework utilizing structured social and embodied reasoning - against CEMIR (Context-Enriched Multimodal Intent Recognition), a method that performs multimodal enrichment by synthesizing narratives and photorealistic images from textual prompts. By evaluating both approaches across four Large Language Models (LLMs), ranging from Qwen2.5-Omni-3B to GPT-5, on the HandMeThat v2 benchmark, we analyze their capability to resolve pragmatic ambiguities. Our statistical analysis, employing multiple-comparison correction, reveals no statistically significant difference in performance between FISER and CEMIR across any model or difficulty level. This pattern holds across all sixteen model-by-difficulty comparisons, as well as in a targeted ablation isolating CEMIR's narrative and visual components. Instead, performance is primarily associated with backbone capability and the inherent difficulty of the ambiguity. These findings suggest a boundary condition for text-derived multimodal enrichment: when the relevant task constraints are already available in the textual instruction, synthetic multimodal augmentation may not provide measurable benefit over structured reasoning on the same text.

</details>

---

### [[20_Research/Papers/大模型/The_Helpful_Agent_Problem_When_Emergent_Cooperation_Among_LLM_Agents_Bypasses_Intended_Workflows|The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows]]

![[assets/2610.31985_first_page.png|800]]

- **arXiv**: [2610.31985](https://arxiv.org/abs/2610.31985)
- **PDF**: https://arxiv.org/pdf/2610.31985
- **详细分析**: [[20_Research/Papers/大模型/The_Helpful_Agent_Problem_When_Emergent_Cooperation_Among_LLM_Agents_Bypasses_Intended_Workflows|The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows]]
- **作者**: Moumita Choudhury, Amit Sarker, Shlomo Zilberstein
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CooperBench, FavorBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly deployed in collaborative settings where they pursue separate tasks while sharing resources and operating under review or oversight processes. Such settings create safety risks not only when agents are malicious, but also when they are simply trying to help. Prior work has largely studied adversarial or explicitly collusive behavior; we show that benign agents pursuing separate objectives can spontaneously cooperate in ways that bypass intended workflows. We call this the \emph{helpful agent problem}. We study long-horizon shared-resource environments in which agents sometimes depend on resources owned by their peers and cross-owner changes are normally mediated by a reviewer. When review becomes unavailable, agents begin making changes on one another's behalf despite having no shared reward or explicit incentive to cooperate. Crucially, these actions remain within each agent's local permissions while circumventing the system's intended oversight structure. We introduce \textsc{FavorBench}, a controlled benchmark with measurable downstream side effects, and adapt \textsc{CooperBench} to test the phenomenon in realistic repositories. Across two benchmarks and four models, we find that out-of-workflow favors emerge frequently. Further, in \textsc{FavorBench}, favors from at least three models cause significant harm to parties outside the interaction. These results reveal a distinct multi-agent safety challenge: cooperation itself can create pathways around system-level safeguards.

</details>

---

### [[20_Research/Papers/大模型/Knowing_Whom_to_Trust_is_not_Enough_The_Trust--Agreement_Gap_in_Repeated_Multi-Party_LLM_Negotiation|Knowing Whom to Trust is not Enough: The Trust--Agreement Gap in Repeated Multi-Party LLM Negotiation]]

![[assets/2610.31971_figure.png|800]]

- **arXiv**: [2610.31971](https://arxiv.org/abs/2610.31971)
- **PDF**: https://arxiv.org/pdf/2610.31971
- **详细分析**: [[20_Research/Papers/大模型/Knowing_Whom_to_Trust_is_not_Enough_The_Trust--Agreement_Gap_in_Repeated_Multi-Party_LLM_Negotiation|Knowing Whom to Trust is not Enough: The Trust--Agreement Gap in Repeated Multi-Party LLM Negotiation]]
- **作者**: Amit Sarker, Moumita Choudhury, Saaduddin Mahmud, Shlomo Zilberstein
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Knowing Whom to Trust is not Enough: The Trust--Agreement Gap in Repeated Multi-Party LLM Negotiation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：RepuNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly participate in negotiations on behalf of individuals and organizations, yet they remain vulnerable to manipulation, particularly in repeated multi-party interactions. Classical multi-agent systems address this challenge through explicit trust and reputation models, whereas existing work on LLM negotiation largely treats trust as an emergent phenomenon. We investigate whether LLM agents can form useful trust estimates from prior interactions and leverage them to improve future negotiation outcomes. We introduce a repeated, multi-party, multi-issue negotiation framework in which recurring agents participate in a sequence of negotiation games while one participant covertly attempts to prevent agreement. After each game, agents assess their counterparts and maintain pairwise trust estimates that carry over to subsequent negotiations. We compare trust-aware and trust-agnostic agents and analyze how explicit trust influences negotiation outcomes. Our results reveal a \emph{trust--agreement gap}: trust-aware agents can identify the adversary within a few games, but accurate trust estimates do not consistently translate into better agreements. Trust increases agreement rates by up to 23 percentage points, but only when agents are explicitly guided to use it in their decisions. Explicit trust can therefore improve repeated LLM negotiations, but its value depends critically on how trust is assessed and incorporated into agents' reasoning.

</details>

---

### [[20_Research/Papers/大模型/Beyond_On-Policy_vs._Off-Policy_At_What_Level_Should_LLM_Agent_Distillation_Follow_the_Student|Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?]]

![[assets/2610.31918_figure.png|800]]

- **arXiv**: [2610.31918](https://arxiv.org/abs/2610.31918)
- **PDF**: https://arxiv.org/pdf/2610.31918
- **详细分析**: [[20_Research/Papers/大模型/Beyond_On-Policy_vs._Off-Policy_At_What_Level_Should_LLM_Agent_Distillation_Follow_the_Student|Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?]]
- **作者**: Ya Gao, Zhengtao Zou, Pekka Marttinen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, OfficeBench, ToolQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distilling interactive LLM agents requires choosing between teacher-generated demonstrations and student-generated experience, corresponding broadly to off-policy and on-policy distillation. While both have proven effective, we argue that this distinction is inherently hierarchical: the policy that induces an interaction history need not be the same as the policy that generates the token prefix of the current action. We introduce a hierarchical agent distillation framework that formalizes these two levels of on-policiness and enables explicit control over their pairing, mixture proportions, and training schedule. We study this problem through self-distillation, where a frozen teacher has access to task guidance unavailable to the student, and conduct a three-stage controlled study across three models and four interactive environments. We find that student-induced histories paired with teacher-generated action prefixes generally provide the strongest standalone training signal, whereas following the student at both levels generally performs worst. Nevertheless, fully on-policy data becomes beneficial when incorporated into a mixture with other configurations. Moreover, mixtures with identical teacher/student proportions at each level can yield substantially different performance, showing that how the two levels are paired matters beyond the overall amount of on-policy data. Finally, front-loading fully teacher-generated contexts and delaying fully on-policy contexts improves over a static mixture. These findings provide practical principles for deciding where, how much, and when agent distillation should follow the student.

</details>

---

### [[20_Research/Papers/强化学习/SEVI_Safe_Evidential_Real-World_Reinforcement_Learning|SEVI: Safe Evidential Real-World Reinforcement Learning]]

![[assets/2610.31829_figure.png|800]]

- **arXiv**: [2610.31829](https://arxiv.org/abs/2610.31829)
- **PDF**: https://arxiv.org/pdf/2610.31829
- **详细分析**: [[20_Research/Papers/强化学习/SEVI_Safe_Evidential_Real-World_Reinforcement_Learning|SEVI: Safe Evidential Real-World Reinforcement Learning]]
- **作者**: Shaekh Mohammad Shithil, Lantao Liu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SEVI: Safe Evidential Real-World Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world reinforcement learning has enabled contact-rich manipulation tasks to be trained directly on physical robots, but unsafe interactions during online learning remain a key barrier to practical deployment. We propose Safe Evidential Real-World Reinforcement Learning (SEVI), a framework for reliability-aware safety intervention during real-world policy learning. SEVI introduces an Evidential Safety Critic that estimates both future constraint-violation risk and epistemic uncertainty in a single forward pass. During online learning, SEVI evaluates each task-policy action before execution; if the action is predicted to be unsafe or the prediction is insufficiently supported by evidence, SEVI overrides it with an offline-trained recovery policy that guides the robot toward a lower-risk region. We evaluate SEVI on two simulated manipulation tasks and a real-world USB insertion task under in-distribution and distribution-shifted conditions. Across task-learning and safety-critic baselines, SEVI achieves the strongest trajectory-level safety prediction, the highest final task success, and the lowest unsafe-event counts. SEVI also reduces unsafe events by 13.4 to 57.1 percent relative to recovery-based safe RL while preserving low-latency execution-time filtering. The project page is available at: https://sevi-safe.github.io/

</details>

---

### [[20_Research/Papers/具身智能/PrefO2O_Zero-Shot_Preference-Based_Reinforcement_Learning_via_Offline-to-Online_Latent_Preference_Transfer|PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer]]

![[assets/2610.31812_figure.png|800]]

- **arXiv**: [2610.31812](https://arxiv.org/abs/2610.31812)
- **PDF**: https://arxiv.org/pdf/2610.31812
- **详细分析**: [[20_Research/Papers/具身智能/PrefO2O_Zero-Shot_Preference-Based_Reinforcement_Learning_via_Offline-to-Online_Latent_Preference_Transfer|PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer]]
- **作者**: Ruiqi Wang, Dezhong Zhao, Xuesu Xiao, Erdem Biyik, Byung-Cheol Min, Guohua Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.4（加权：具身智能 0.9，强化学习 0.8，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PEARL, PbRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Preference-based reinforcement learning (PbRL) has emerged as a promising paradigm for learning robot behaviors aligned with human intent. However, its scalability is fundamentally limited by the need to collect expensive human preference labels for every new task. In this work, we present PrefO2O, an offline-to-online latent preference transfer framework that enables zero-shot PbRL on unseen target tasks without requiring any human feedback. The core idea is to learn a task-invariant latent preference space from a small amount of offline preference data on source tasks, where transferable preference structures are disentangled from task-specific variations. This learned manifold allows PrefO2O to transfer preference structures and reward priors to new tasks under distribution shift, while confidence-weighted optimal transport alignment generates reliable pseudo-preference supervision for online reward adaptation. Extensive experiments on robotic manipulation and locomotion benchmarks demonstrate that PrefO2O substantially outperforms existing preference-transfer baselines and matches or exceeds PbRL methods trained with real human feedback, while generalizing across multi-to-one and one-to-one transfer settings as well as across different robot embodiments.

</details>

---

### [[20_Research/Papers/大模型/An_Agentic_Approach_with_Evidence-Grounded_Verification_for_Multimodal_Emotion_Reasoning_in_Conversation|An Agentic Approach with Evidence-Grounded Verification for Multimodal Emotion Reasoning in Conversation]]

![[assets/2610.31685_figure.png|800]]

- **arXiv**: [2610.31685](https://arxiv.org/abs/2610.31685)
- **PDF**: https://arxiv.org/pdf/2610.31685
- **详细分析**: [[20_Research/Papers/大模型/An_Agentic_Approach_with_Evidence-Grounded_Verification_for_Multimodal_Emotion_Reasoning_in_Conversation|An Agentic Approach with Evidence-Grounded Verification for Multimodal Emotion Reasoning in Conversation]]
- **作者**: Elyas Rashno, Farhana Zulkernine
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《An Agentic Approach with Evidence-Grounded Verification for Multimodal Emotion Reasoning in Conversation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EmoBench, MER-UniBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based multimodal emotion reasoning systems perform well on standard benchmarks, but improving them through instruction tuning can be computationally expensive. Agentic pipelines built from frozen models avoid this cost, but introduce a different challenge: when a prediction is wrong, the system must identify which agent or stage caused the error. We address this problem with an agentic framework for traceable multimodal emotion reasoning and prompt-space adaptation. Modality-specific perception agents analyze visual, acoustic, and lexical inputs and post evidence-cited observations to a shared board. An integration agent combines these observations with retrieved multimodal examples to produce an emotion description, label set, and supporting citations, while an MLLM critic can request one revision before the output is finalized. For incorrect predictions, a separate evidence-grounded verification stage applies deterministic checks to verify that cited evidence and references are valid, and an entailment check to determine whether the final claims are supported by that evidence. Detected failures are then grouped by the responsible component and failure type, converted into targeted prompt patches, and accepted only after validation on a held-out set. This adapts the agent prompts without updating model weights. On the MER2025 dataset, targeted prompt adaptation outperforms the frozen static pipeline on all four MLLMs, ranging from 2B to 38B parameters, and matches or outperforms undifferentiated reflection baselines on each of them: VideoLLaMA3-2B, Phi-3.5-vision-instruct, Qwen2.5-VL-7B-Instruct, and InternVL2.5-38B. It improves F-score by 0.6--2.2 points depending on the backbone, including an increase from 52.3 to 54.5 on Qwen2.5-VL-7B.

</details>

---
