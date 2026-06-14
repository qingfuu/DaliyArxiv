# cs.CL | Computation and Language | 2026-06-12

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/EvoArena_Tracking_Memory_Evolution_for_Robust_LLM_Agents_in_Dynamic_Environments|EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments]]

![[assets/2606.13681_figure.png|800]]

- **arXiv**: [2606.13681](https://arxiv.org/abs/2606.13681)
- **PDF**: https://arxiv.org/pdf/2606.13681
- **详细分析**: [[20_Research/Papers/大模型/EvoArena_Tracking_Memory_Evolution_for_Robust_LLM_Agents_in_Dynamic_Environments|EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments]]
- **作者**: Jundong Xu, Qingchuan Li, Jiaying Wu, Yihuai Lan, Shuyue Stella Li, Huichi Zhou, Bowen Jiang, Lei Wang, Jun Wang, Anh Tuan Luu, Caiming Xiong, Hae Won Park...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, AndroidWorld, HorizonBench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.

</details>

---

### [[20_Research/Papers/大模型/From_Passive_Generation_to_Investigation_A_Proactive_Scientific_Peer_Review_Agent|From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent]]

![[assets/2606.13349_figure.png|800]]

- **arXiv**: [2606.13349](https://arxiv.org/abs/2606.13349)
- **PDF**: https://arxiv.org/pdf/2606.13349
- **详细分析**: [[20_Research/Papers/大模型/From_Passive_Generation_to_Investigation_A_Proactive_Scientific_Peer_Review_Agent|From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent]]
- **作者**: Haishuo Fang, Yue Feng, Iryna Gurevych
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.05（加权：大模型 0.65，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have shown promise in automating scientific peer review. However, existing approaches often struggle to generate in-depth reviews supported by concrete evidence. We argue that a key limitation is the lack of flexibility to proactively investigate suspicious parts of a paper based on accumulated evidence, as human reviewers do. In this paper, we explore how to enable an LLM-based review agent to perform such proactive investigation. We find that this can be naturally formulated as a Markov Decision Process (MDP), and propose ProReviewer, a scientific peer review agent that proactively reviews a paper guided by a maintained, structured review log. The structured review log serves as a workspace for the agent to track evidence and intermediate findings collected during review. Experiments show that ProReviewer with an 8B backbone, trained by supervised fine-tuning and optimized by reinforcement learning, achieves the highest average score across five quality dimensions, outperforming prompt-based methods with much larger frontier LLMs by up to 39% and the strongest fine-tuned baseline by 16% relatively. It also attains the highest win rates against baselines in human evaluation.

</details>

---

### [[20_Research/Papers/大模型/SkillCAT_Contrastive_Assessment_and_Topology-Aware_Skill_Self-Evolution_for_LLM_Agents|SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents]]

![[assets/2606.13317_figure.png|800]]

- **arXiv**: [2606.13317](https://arxiv.org/abs/2606.13317)
- **PDF**: https://arxiv.org/pdf/2606.13317
- **详细分析**: [[20_Research/Papers/大模型/SkillCAT_Contrastive_Assessment_and_Topology-Aware_Skill_Self-Evolution_for_LLM_Agents|SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents]]
- **作者**: Kunfeng Chen, Qihuang Zhong, Juhua Liu, Bo Du
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DocVQA, SkillLearnBench, SkillsBench, SpreadsheetBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, a training-free framework that separates this process into three stages. Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences. Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones and keeps only patches that improve or preserve task outcomes before hierarchical skill patch merging. Topology-Aware Task Execution (TTE) compiles the evolved skills into a routable sub-skill topology, so inference loads only the capability nodes relevant to the task. We evaluate SkillCAT on common agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further test cross-model and out-of-distribution generalization. Across these settings, SkillCAT raises the average score over baselines by up to 40.40%, demonstrating reliable skill evolution without model training.

</details>

---

### [[20_Research/Papers/大模型/Getting_Better_at_Working_With_You_Compiling_User_Corrections_into_Runtime_Enforcement_for_Coding_Agents|Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents]]

![[assets/2606.13174_figure.png|800]]

- **arXiv**: [2606.13174](https://arxiv.org/abs/2606.13174)
- **PDF**: https://arxiv.org/pdf/2606.13174
- **详细分析**: [[20_Research/Papers/大模型/Getting_Better_at_Working_With_You_Compiling_User_Corrections_into_Runtime_Enforcement_for_Coding_Agents|Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents]]
- **作者**: Yujun Zhou, Kehan Guo, Haomin Zhuang, Xiangqi Wang, Yue Huang, Zhenwen Liang, Pin-Yu Chen, Tian Gao, Nuno Moniz, Nitesh V. Chawla, Xiangliang Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PersonaGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Unlike runtime checks written ahead of time by developers, TRACE skills come from the user's own chat corrections. We evaluate TRACE with simulated user-in-the-loop experiments on ClawArena coding-agent tasks and MemoryArena-derived memory-intensive tasks. On ClawArena, TRACE reduces held-out preference violation from 100.0% to 37.6% on in-distribution tasks and from 100.0% to 2.0% on out-of-distribution tasks. On MemoryArena-derived tasks, TRACE reduces in-distribution violation from 100.0% to 60.5% while matching or exceeding the strongest memory baseline on task pass. These results suggest that compiling corrections into runtime enforcement can address a repeated-friction failure mode that memory alone does not reliably solve, reducing the need for users to restate the same correction across future sessions. Experiment code is available at https://github.com/YujunZhou/TRACE_exp, and the deployable skill is available at https://github.com/YujunZhou/tellonce.

</details>

---

### [[20_Research/Papers/强化学习/Demystifying_Hidden-State_Recurrence_Switchable_Latent_Reasoning_with_On-Policy_Reinforcement_Learning|Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning]]

![[assets/2606.13106_figure.png|800]]

- **arXiv**: [2606.13106](https://arxiv.org/abs/2606.13106)
- **PDF**: https://arxiv.org/pdf/2606.13106
- **详细分析**: [[20_Research/Papers/强化学习/Demystifying_Hidden-State_Recurrence_Switchable_Latent_Reasoning_with_On-Policy_Reinforcement_Learning|Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning]]
- **作者**: Jiayu Yang, Chao Chen, Shengen Wu, Yinhong Liu, Yuxuan Fan, Lujundong Li, Songning Lai, Chengwei Qin, Zhijiang Guo
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent chain-of-thought compresses reasoning by replacing visible reasoning traces with continuous hidden-state recurrence, but existing formulations are difficult to optimize with standard on-policy reinforcement learning (RL) and hard to interpret causally. Our key insight is that a single pair of explicit boundary tokens can address both issues at once: discrete entry and exit anchors make the latent block compatible with standard on-policy RL, and the same anchors offer a natural foothold for mechanistic analysis. Motivated by this, we propose SWITCH, a switchable latent reasoning framework. The model emits &lt;swi&gt; to enter latent mode and &lt;/swi&gt; to exit. Because the boundaries are ordinary discrete tokens, the GRPO policy ratio is well-defined at every decision point. The same anchors also expose the latent steps to direct probing and causal intervention. We train the model with a visible-to-latent curriculum and a Switch-GRPO objective that propagates gradients through recurrent latent computation. SWITCH consistently outperforms prior hidden-state-recurrence latent reasoning approaches at similar scale. Mechanistic analysis through the boundary tokens further reveals three findings: (i) &lt;swi&gt; is a sharply localised, learned switching policy rather than a stylistic artefact; (ii) the latent step it opens performs problem-specific, causally important computation rather than acting as an inert placeholder; and (iii) that computation is concentrated at a single hidden-state transition on entry. Together, these results show that hidden-state-recurrence latent reasoning is both RL-trainable and open to direct mechanistic analysis, including of how on-policy RL itself improves the model from the inside.

</details>

---

### [[20_Research/Papers/大模型/SENTINEL_Failure-Driven_Reinforcement_Learning_for_Training_Tool-Using_Language_Model_Agents|SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents]]

![[assets/2606.12908_figure.png|800]]

- **arXiv**: [2606.12908](https://arxiv.org/abs/2606.12908)
- **PDF**: https://arxiv.org/pdf/2606.12908
- **详细分析**: [[20_Research/Papers/大模型/SENTINEL_Failure-Driven_Reinforcement_Learning_for_Training_Tool-Using_Language_Model_Agents|SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents]]
- **作者**: Ziyi Wang, Yuxuan Lu, Yimeng Zhang, Qun Liu, Chen Luo, Jiri Gesi, Hanqing Lu, Yisi Sang, Manling Li, Jing Huang, Dakuo Wang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.75（加权：大模型 0.95，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SENTINEL: Failure-Driven Reinforcement Learning for Training Tool-Using Language Model Agents》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MCP-Bench, Tau2-Bench, ToRL, ToolBench, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language model agents are increasingly effective in solving realistic tasks through multi-turn tool use. However, training reliable tool-using agents remains challenging in practice. While reinforcement learning provides an on-policy paradigm for improving agents from their own environment interactions, its effectiveness depends heavily on the training task distribution. When tasks are fixed before training, the task distribution can become increasingly mismatched with the policy's evolving capabilities, causing many rollouts to be spent on uninformative tasks. We propose SENTINEL, a failure-driven reinforcement learning framework that turns the Solver's rollout failures into targeted training tasks. SENTINEL follows a Controller--Proposer--Solver loop: the Controller analyzes failed trajectories and summarizes recurring error patterns, the Proposer generates executable tasks that stress these weaknesses, and the Solver is trained on the targeted tasks. On Tau2-Bench Retail with Qwen3-4B-Thinking-2507, SENTINEL improves Pass\^{}1 from 66.4 to 74.9 and outperforms RL on general synthetic tasks across Pass\^{}k metrics. These results demonstrate that model failures provide an effective and scalable source of targeted training signal for improving tool-using language model agents.

</details>

---

### [[20_Research/Papers/大模型/X-MADAM-RAG_Diagnosing_and_Handling_Chinese-English_Evidence_Conflict_in_Retrieval-Augmented_Generation|X-MADAM-RAG: Diagnosing and Handling Chinese-English Evidence Conflict in Retrieval-Augmented Generation]]

![[assets/2606.12903_figure.png|800]]

- **arXiv**: [2606.12903](https://arxiv.org/abs/2606.12903)
- **PDF**: https://arxiv.org/pdf/2606.12903
- **详细分析**: [[20_Research/Papers/大模型/X-MADAM-RAG_Diagnosing_and_Handling_Chinese-English_Evidence_Conflict_in_Retrieval-Augmented_Generation|X-MADAM-RAG: Diagnosing and Handling Chinese-English Evidence Conflict in Retrieval-Augmented Generation]]
- **作者**: Yongqi Kang, Yu Fu, Yong Zhao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《X-MADAM-RAG: Diagnosing and Handling Chinese-English Evidence Conflict in Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FaithEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) systems may receive evidence that is not merely noisy but mutually contradictory. This issue becomes particularly salient in multilingual settings, where retrieved Chinese and English evidence may support incompatible answer candidates. We study this problem through X-RAMDocs-ZHEN, a controlled Chinese-English benchmark derived from RAMDocs for diagnosing evidence conflict in RAG. The benchmark contains 300 examples across six balanced conditions, including monolingual support, bilingual agreement, reversed conflict directions, and conflict with optional noise. We further examine X-MADAM-RAG, an interpretable pipeline that decomposes evidence handling into per-document candidate extraction, visible-evidence repair, deterministic candidate grouping, and conflict-aware aggregation. On the original controlled benchmark with Qwen2.5-7B-Instruct, X-MADAM-RAG achieves 0.9667 strict accuracy and 0.9767 conflict-aware success, outperforming an evidence-normalized single-call baseline. However, a zero-call rule-only extractor reaches 1.0000 on the same benchmark, revealing strong template regularity. To probe this limitation, we construct a deterministic naturalized stress test that removes explicit answer templates while preserving candidate strings. On its 100-sample subset, rule-only extraction falls to 0.0000, but X-MADAM-RAG also drops to 0.3000 strict accuracy, below both naive and evidence-normalized baselines. A privileged oracle remains perfect, indicating that document-level extraction is the main bottleneck. These findings position X-RAMDocs-ZHEN and X-MADAM-RAG as diagnostic tools for controlled evidence conflict rather than as evidence of general hallucination detection or robustness to natural retrieval.

</details>

---

### [[20_Research/Papers/大模型/PRISM_Prosody-Integrated_Multi-Agent_Reasoning_Framework_for_Empathetic_Spoken_Dialogue|PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue]]

![[assets/2606.12902_figure.png|800]]

- **arXiv**: [2606.12902](https://arxiv.org/abs/2606.12902)
- **PDF**: https://arxiv.org/pdf/2606.12902
- **详细分析**: [[20_Research/Papers/大模型/PRISM_Prosody-Integrated_Multi-Agent_Reasoning_Framework_for_Empathetic_Spoken_Dialogue|PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue]]
- **作者**: Wen Zhang, Xiaocui Yang, Zhuoyue Gao, Shi Feng, Daling Wang, Yifei Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: https://github.com/Bxzfrm/PRISM.

</details>

---

### [[20_Research/Papers/大模型/ProPlay_Procedural_World_Models_for_Self-Evolving_LLM_Agents|ProPlay: Procedural World Models for Self-Evolving LLM Agents]]

![[assets/2606.12780_figure.png|800]]

- **arXiv**: [2606.12780](https://arxiv.org/abs/2606.12780)
- **PDF**: https://arxiv.org/pdf/2606.12780
- **详细分析**: [[20_Research/Papers/大模型/ProPlay_Procedural_World_Models_for_Self-Evolving_LLM_Agents|ProPlay: Procedural World Models for Self-Evolving LLM Agents]]
- **作者**: Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiaoguang Guo, Weixiang Sun, Chuxu Zhang, Yanfang Ye
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 2.17（加权：大模型 1.05，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《ProPlay: Procedural World Models for Self-Evolving LLM Agents》归入 大模型、世界模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. Existing LLM-agent methods often rely on memory or planning modules, yet they rarely close the loop between them to continually refine an internal understanding of environment dynamics. We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge. Rather than representing experience as isolated rules or low-level action constraints, ProPlay abstracts successful trajectories into procedures and organizes them in a procedure graph that captures causal transitions among task stages. Each transition is associated with a reliability record embedding to estimate its task-specific contribution from past outcomes. Before each episode, ProPlay simulates future procedural trajectories over known graph structures as structured soft guidance; after execution, it refines the graph using environment feedback. Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines. Our code has been released in https://github.com/antman9914/proplay.

</details>

---

### [[20_Research/Papers/大模型/Agent-based_models_for_the_evolution_of_morphological_alternation_patterns|Agent-based models for the evolution of morphological alternation patterns]]

![[assets/2606.12748_first_page.png|800]]

- **arXiv**: [2606.12748](https://arxiv.org/abs/2606.12748)
- **PDF**: https://arxiv.org/pdf/2606.12748
- **详细分析**: [[20_Research/Papers/大模型/Agent-based_models_for_the_evolution_of_morphological_alternation_patterns|Agent-based models for the evolution of morphological alternation patterns]]
- **作者**: Aravinth Kulanthaivelu, Richard Sproat
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agent-based models for the evolution of morphological alternation patterns》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Why is the past of English "go" the apparently unrelated "went"? Such alternations are frequent in languages. They neither aid communication nor learnability, yet they can be persistent, surviving over centuries or millennia. We present a multi-agent simulation of the emergence of morphological stem and inflection alternations. Alternate forms arise by phonological changes or, as with "go/went", from lexical alternatives associated with a subset of the population. When an agent 'hears' another agent use a novel form for a slot in the paradigm of a word (say, the past tense of go), they will with some probability adopt that form, possibly spreading its use to other slots in the paradigm that shared the same original form. Thus alternative forms can spread through the population and become entrenched as stem or inflectional marker alternants. Unlike many previous computational studies, our system allows for naturalistic lexical forms, realistic phonological rules, lexicons with hundreds or thousands of entries, and agent populations in the tens or hundreds. It supports several network topologies, diffusion patterns and agent adoption policies. One issue with such simulations is evaluation: how realistic is the resulting morphology compared to those of real languages? We introduce the AI Historical Linguist, a novel Large Language Model-driven system that models a debate between two historical linguists. We use this to compare a set of real language morphologies, disguised morphologies, and experimentally evolved morphologies. The results suggest that among the factors that favor more plausible morphologies are scale-free social networks and random Bernoulli adoption of forms. We also present three case studies modeling attested historical changes, allowing us to test what might have happened if history had been different. All code and data are released.

</details>

---

### [[20_Research/Papers/世界模型/Identifiability_Without_Gaussianity_Symbolic_World_Models_and_Near-Infinite_Temporal_Consistency|Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite Temporal Consistency]]

![[assets/2606.12471_figure.png|800]]

- **arXiv**: [2606.12471](https://arxiv.org/abs/2606.12471)
- **PDF**: https://arxiv.org/pdf/2606.12471
- **详细分析**: [[20_Research/Papers/世界模型/Identifiability_Without_Gaussianity_Symbolic_World_Models_and_Near-Infinite_Temporal_Consistency|Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite Temporal Consistency]]
- **作者**: Seth Dobrin, Łukasz Chmiel
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.16，世界模型 1.36）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Identifiability Without Gaussianity: Symbolic World Models and Near-Infinite Temporal Consistency》归入 世界模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Klindt, LeCun, and Balestriero (arXiv:2605.26379) proved that Joint-Embedding Predictive Architectures (JEPAs) achieve linear identifiability, the linear recovery of the world's true latent variables, if and only if the world's latent dynamics follow a Gaussian, stationary process. This Gaussian boundary implies a fundamental limit on temporal consistency: for any non-Gaussian physical system, the representation error of a statistical World Model grows monotonically with time. We prove that this limit is an artifact of the statistical alignment mechanism, not a property of World Models in general. We introduce the Physics-Grounded Symbolic Architecture (PGSA) and prove three results: (1) a PGSA achieves exact linear identifiability for all physical regimes, regardless of the latent distribution; (2) the per-step error of a PGSA is bounded by numerical precision alone; and (3) as a direct consequence, a PGSA maintains temporal consistency for an unbounded number of transitions, a property we term near-infinite temporal consistency. We further prove that statistical World Models cannot achieve this property for any non-Gaussian system, regardless of model capacity or the volume of training data. The algebraic cores of four of the theorems are formalized in Lean 4 with Mathlib4 v4.31.0 (zero sorry placeholders); the Klindt et al. converse is taken as an external premise. The contrast establishes that symbolic grounding in the causal generator of the world's dynamics is the sufficient condition and, in non-Gaussian regimes, the only condition for near-infinite temporal consistency.

</details>

---
