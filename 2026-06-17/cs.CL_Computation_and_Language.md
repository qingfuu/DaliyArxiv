# cs.CL | Computation and Language | 2026-06-17

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/Zone_of_Proximal_Policy_Optimization_Teacher_in_Prompts,_Not_Gradients|Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients]]

![[assets/2606.18216_figure.png|800]]

- **arXiv**: [2606.18216](https://arxiv.org/abs/2606.18216)
- **PDF**: https://arxiv.org/pdf/2606.18216
- **详细分析**: [[20_Research/Papers/大模型/Zone_of_Proximal_Policy_Optimization_Teacher_in_Prompts,_Not_Gradients|Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients]]
- **作者**: Byung-Kwan Lee, Ximing Lu, Shizhe Diao, Minki Kang, Saurav Muralidharan, Karan Sapra, Andrew Tao, Pavlo Molchanov, Yejin Choi, Yu-Chiang Frank Wang, Ryo Hachiuma
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.55（加权：大模型 0.35，强化学习 1.2）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CEval, GPQA, InfoVQA, MVBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge distillation transfers a teacher's competence to a small student but is brittle in the small-student regime: forcing the student to imitate logits from a much larger teacher concentrates it on the teacher's sharpest modes, hurting generalization on benchmark families beyond the training corpus. Reinforcement learning (RL) avoids logit imitation by training on the student's own rollouts. However, on questions where every rollout fails-yielding zero advantage and being silently discarded-injecting a stronger teacher's response into the policy gradient breaks the on-policy assumption and induces drift. We introduce Zone of Proximal Policy Optimization (ZPPO), inspired by Vygotsky's zone of proximal development, which keeps the teacher inside the prompt rather than the policy gradient. On hard questions, ZPPO constructs two reformulated prompts: a Binary Candidate-included Question (BCQ) pairs one correct teacher response with one incorrect student response as anonymized candidates the student must discriminate, and a Negative Candidate-included Question (NCQ) aggregates the student's wrong rollouts into a single prompt to surface their shared failure modes. A prompt replay buffer recirculates each hard question until it either graduates-the student's mean rollout accuracy on it reaches half- or is FIFO-evicted under finite capacity, amplifying BCQ and NCQ inside the student's current zone of proximal development. On the Qwen3.5 family at four student scales (0.8B-9B) with a 27B teacher, post-trained as vision-language models and evaluated on a 31-benchmark suite (16 VLM, 10 LLM, 5 Video), ZPPO outperforms off/on-policy distillation and GRPO, with the largest gains at the smallest scale.

</details>

---

### [[20_Research/Papers/大模型/HistoRAG_Embedding_Historical_Methodology_in_Retrieval-Augmented_Generation_Through_Critical_Technical_Practice|HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice]]

![[assets/2606.18103_figure.png|800]]

- **arXiv**: [2606.18103](https://arxiv.org/abs/2606.18103)
- **PDF**: https://arxiv.org/pdf/2606.18103
- **详细分析**: [[20_Research/Papers/大模型/HistoRAG_Embedding_Historical_Methodology_in_Retrieval-Augmented_Generation_Through_Critical_Technical_Practice|HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice]]
- **作者**: Noah J. Kim-Baumann, Torsten Hiltmann
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) is the prevailing architecture for grounding language model outputs in external evidence, yet its dominant evaluation paradigms and default configurations remain oriented toward factual question-answering. For interpretive disciplines such as historical studies, RAG embeds assumptions that conflict with scholarly practice. We introduce HistoRAG, a framework that translates historiographical principles into concrete architectural interventions. Separated retrieval and generation decouples source discovery from interpretation, temporal windowing enforces balanced source representation across the research period as a methodological requirement of historical inquiry, and LLM-as-judge evaluation makes relevance judgments transparent and contestable. We evaluate these interventions using SPIEGELragged, applied to 102,189 articles from Der Spiegel (1950-1979). Each intervention addresses a measurable deficiency in standard RAG: era-specific vocabulary retrieves zero chunks from the 1950s when using 1970s terminology, evidence of the temporal skew that motivates windowing; vector similarity and LLM-assessed relevance correlate only weakly (Spearman rho = 0.275), motivating post-retrieval evaluation; and keyword-based and semantic retrieval surface largely disjoint source pools, motivating an architecture in which both operate as complementary retrieval layers under a shared LLM evaluation filter. We also introduce the concept of Zwischentexte (intermediate texts that function as interpretive proposals rather than findings) as a framework for responsible integration of LLM-generated text into scholarly practice. The architecture offers a model for how domain-specific epistemological commitments can be translated into RAG design decisions, and may transfer to other interpretive disciplines working with large corpora.

</details>

---

### [[20_Research/Papers/大模型/Compositional_Skill_Routing_for_LLM_Agents_Decompose,_Retrieve,_and_Compose|Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose]]

![[assets/2606.18051_first_page.png|800]]

- **arXiv**: [2606.18051](https://arxiv.org/abs/2606.18051)
- **PDF**: https://arxiv.org/pdf/2606.18051
- **详细分析**: [[20_Research/Papers/大模型/Compositional_Skill_Routing_for_LLM_Agents_Decompose,_Retrieve,_and_Compose|Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose]]
- **作者**: Xueping Gao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CompSkillBench, TaskBench, ToolQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on external skills -- reusable tool specifications -- but real-world tasks often require composing multiple skills, not just selecting one. We formalize this as the Compositional Skill Routing problem: given a complex user query and a large skill library, decompose the query into atomic sub-tasks, retrieve the appropriate skill for each sub-task, and compose an executable plan. We present SkillWeaver, a decompose-retrieve-compose framework combining an LLM task decomposer, a bi-encoder skill retriever with FAISS indexing, and a dependency-aware DAG planner. To support evaluation, we introduce CompSkillBench, a benchmark of 300 compositional queries over 2,209 real MCP server skills spanning 24 functional categories, sourced from the public MCP ecosystem. Our experiments reveal that task decomposition quality is the primary bottleneck: standard LLM decomposition reaches only 34.2% category recall at the step level. To address this, we propose Iterative Skill-Aware Decomposition (SAD), a retrieval-augmented feedback loop that iteratively aligns decomposition with available skills. SAD improves decomposition accuracy from 51.0% to 67.7% (+32.7%, Wilcoxon p &lt; 10^-6) in a single iteration; DA-conditioned analysis confirms that correct granularity is the prerequisite for effective retrieval (CatR@1 rises from 34% to 41% when DA=1). SkillWeaver reduces context window consumption by over 99%, and transfer experiments confirm generalization (+35.6% relative DA gain even when target categories are absent from the retrieval pool).

</details>

---

### [[20_Research/Papers/大模型/GameCraft-Bench_Can_Agents_Build_Playable_Games_End-to-End_in_a_Real_Game_Engine|GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?]]

![[assets/2606.17861_figure.png|800]]

- **arXiv**: [2606.17861](https://arxiv.org/abs/2606.17861)
- **PDF**: https://arxiv.org/pdf/2606.17861
- **详细分析**: [[20_Research/Papers/大模型/GameCraft-Bench_Can_Agents_Build_Playable_Games_End-to-End_in_a_Real_Game_Engine|GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?]]
- **作者**: Tongxu Luo, Rongsheng Wang, Jiaxi Bi, Chenming Xu, Zhengyang Tang, Jianlong Chen, Juhao Liang, Ke Ji, Shuqi Guo, Yuhao Du, Fan Bu, Wenyu Du...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GameCraft-Bench, GameDevBench, OpenGame-Bench, URL, WebGameBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Game generation is an emerging application of coding agents, requiring models to transform natural-language specifications into playable interactive systems. Unlike traditional coding tasks, game generation takes place within a game engine, where scripts, scenes, assets, rendering, and runtime interactions must jointly produce coherent gameplay. We formalize end-to-end game generation as the problem of producing a complete game artifact that realizes a specification through observable player-game interaction in a target environment. We argue that evaluating this setting requires three desiderata: Engine Grounding, Artifact Completeness, and Interactive Verification. We propose an interaction-grounded evaluation framework that assesses executable gameplay through replayed demonstrations and rubric-guided multimodal judging. We instantiate this framework as GameCraft-Bench, a benchmark comprising 140 Godot tasks across 15 game families. Evaluations of frontier coding agents show that end-to-end game generation remains highly challenging: the strongest agent achieves only 41.46%, and most agents score below 40%. Further analysis reveals that while agents often implement recognizable mechanics, they struggle to deliver complete games with sufficient content, functional visual feedback, and coherent presentation. See this https URL for demos, code, and data.

</details>

---

### [[20_Research/Papers/大模型/Environment-Grounded_Automated_Prompt_Optimization_for_LLM_Game_Agents|Environment-Grounded Automated Prompt Optimization for LLM Game Agents]]

![[assets/2606.17838_figure.png|800]]

- **arXiv**: [2606.17838](https://arxiv.org/abs/2606.17838)
- **PDF**: https://arxiv.org/pdf/2606.17838
- **详细分析**: [[20_Research/Papers/大模型/Environment-Grounded_Automated_Prompt_Optimization_for_LLM_Game_Agents|Environment-Grounded Automated Prompt Optimization for LLM Game Agents]]
- **作者**: Rean Clive Fernandes, Lukas Fehring, Theresa Eimer, Marius Lindauer, Matthias Feurer
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Environment-Grounded Automated Prompt Optimization for LLM Game Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents in interactive environments are highly sensitive to their prompts, yet prompt engineering remains a manual, task-specific process. We introduce an automated prompt optimization framework for LLM agents that decomposes the observation-to-action pipeline into a goal-conditioned descriptor agent and an action selection agent, and iteratively refines each module's prompt through an LLM-driven evolutionary loop guided by environment returns. We propose a behavior analyzer to attribute episode outcomes to specific prompt components, and a mutator to propose targeted revisions to the prompt, before validating them through environment rollouts. We evaluate on all five BabyAI tasks in the BALROG benchmark, comparing our pipeline against BALROG's RobustCoTAgent under both plain and guided prompt initializations. Optimization improves performance consistently across tasks and conditions, without requiring updates to the model weights. On PutNext, a multi-step coordination task where the RobustCoTAgent achieves 0% success, our framework reaches up to 72.5% success rate using the same underlying LLM with optimized prompts. These results suggest that a multi-agent framework, combined with automatic prompt optimization, enhances LLMs without the need for fine-tuning or extensive human supervision.

</details>

---

### [[20_Research/Papers/大模型/From_Trainee_to_Trainer_LLM-Designed_Training_Environment_for_RL_with_Multi-Agent_Reasoning|From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning]]

![[assets/2606.17682_first_page.png|800]]

- **arXiv**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **PDF**: https://arxiv.org/pdf/2606.17682
- **详细分析**: [[20_Research/Papers/大模型/From_Trainee_to_Trainer_LLM-Designed_Training_Environment_for_RL_with_Multi-Agent_Reasoning|From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning]]
- **作者**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning pipelines for Large Language Model (LLM) training often rely on manually redesigned environments between stages, requiring practitioners to heuristically infer which configuration will best improve the current policy. To automate this process, we propose the LLM-as-Environment-Engineer framework in which the current policy model analyzes failure trajectories together with contextual information and proposes modifications to the next-stage training environment configuration. We also introduce MAPF-FrozenLake, a controllable testbed whose generator exposes multi-dimensional environment configurations, making it suitable for studying and benchmarking environment redesign. On this testbed, we condition the environment engineer on structured summaries of policy behavior, failure cases, and environment statistics, from which it produces the configuration for the next training stage. With Qwen3-4B as the backbone, our framework achieves the strongest aggregate performance on our benchmarks, outperforming larger proprietary LLMs (e.g., GPT, Gemini) and fixed-environment training baselines. We further analyze which forms of context are most effective, finding that successful environment updates rely on failure evidence and preserve configurations that already work. Interestingly, the current RL checkpoint serves as a better environment engineer than the original base model, suggesting that policy learning improves the model's ability to diagnose its remaining weaknesses.

</details>

---

### [[20_Research/Papers/强化学习/EnvRL_Learn_from_Environment_Dynamics_in_Agentic_Reinforcement_Learning|EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning]]

![[assets/2606.17680_figure.png|800]]

- **arXiv**: [2606.17680](https://arxiv.org/abs/2606.17680)
- **PDF**: https://arxiv.org/pdf/2606.17680
- **详细分析**: [[20_Research/Papers/强化学习/EnvRL_Learn_from_Environment_Dynamics_in_Agentic_Reinforcement_Learning|EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning]]
- **作者**: Zhitong Wang, Songze Li, Hao Peng, Shuzheng Si, Yi Wang, Maosong Sun, Juanzi Li
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, EnvRL, SearchQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has emerged as a powerful paradigm for training Large Language Models (LLMs) as agents. However, conventional RL methods for long-horizon agentic tasks often struggle with sparse outcome rewards. Intuitively, this overlooks the rich environment dynamics information contained in rollout interaction trajectories. We argue that the interaction experience inherently serves as an implicit supervision signal, reveals the underlying transition mechanisms of the environment, and enables the agent to construct a more accurate internal model of the environment.. Therefore, in this work, we investigate how to leverage this additional signal to improve policy learning. Specifically, we propose EnvRL, a framework that incorporates environment dynamics learning into agentic RL via two auxiliary objectives: state prediction and inverse dynamics. By jointly optimizing with the primary RL objective, we encourage the agent to internalize environment dynamics from its own interaction experience. Extensive experiments on two long-horizon agentic benchmarks demonstrate that EnvRL achieves significant improvements on success-rates over RL-only baselines, e.g., when trained with GRPO, lifting Qwen-2.5-1.5B-Instruct from 72.8% to 77.4% on ALFWorld, and from 56.8% to 67.0% on WebShop.

</details>

---

### [[20_Research/Papers/大模型/PARSE_Provenance-Aware_Retrieval_Sanitization_for_Professional_Domain_LLM_Agents|PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents]]

![[assets/2606.17467_first_page.png|800]]

- **arXiv**: [2606.17467](https://arxiv.org/abs/2606.17467)
- **PDF**: https://arxiv.org/pdf/2606.17467
- **详细分析**: [[20_Research/Papers/大模型/PARSE_Provenance-Aware_Retrieval_Sanitization_for_Professional_Domain_LLM_Agents|PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents]]
- **作者**: Aaditya Pai
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Prompt injection defenses evaluated on synthetic benchmarks do not generalize to real enterprise documents, which are longer, denser, and interleave legitimate authority language with factual content. We demonstrate this gap with a real-document benchmark of 122 tasks across five professional domains (financial, legal, medical, scientific, DevOps) using actual SEC filings, Federal Register rules, PubMed abstracts, arXiv papers, and GitHub postmortems. Paraphrasing, the strongest defense on synthetic benchmarks, shows no statistically significant attack success rate reduction on real documents (p=0.500) while degrading utility from 91.8% to 82.8%. We introduce PARSE (Provenance-Aware Retrieval Sanitization), a domain-aware, fact-preserving sanitization pipeline that classifies each sentence by injection likelihood, extracts structured facts before rewriting, and verifies fact preservation via a consistency-checking loop. A directiveness gate routes 59% of real enterprise documents to a lightweight path, concentrating computational cost on high-risk documents. PARSE achieves 15.6% attack success rate -- a 38% reduction versus the 25.4% baseline -- at 86.9% utility, the only condition that is both statistically significant (p=0.014, adequately powered) and maintains near-baseline utility. Practitioners should evaluate defenses on domain-matched real documents, not synthetic proxies.

</details>

---

### [[20_Research/Papers/大模型/Are_you_speaking_my_languages_On_spoken_language_adherence_in_multimodal_LLMs|Are you speaking my languages? On spoken language adherence in multimodal LLMs]]

![[assets/2606.17281_first_page.png|800]]

- **arXiv**: [2606.17281](https://arxiv.org/abs/2606.17281)
- **PDF**: https://arxiv.org/pdf/2606.17281
- **详细分析**: [[20_Research/Papers/大模型/Are_you_speaking_my_languages_On_spoken_language_adherence_in_multimodal_LLMs|Are you speaking my languages? On spoken language adherence in multimodal LLMs]]
- **作者**: Hyungwon Kim, Kandarp Joshi, Lillian Zhou, Pavel Golik, Petar Aleksic
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Are you speaking my languages? On spoken language adherence in multimodal LLMs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Model (LLM) based Automatic Speech Recognition (ASR) enables seamless multilingual use, models often misidentify the output language, compromising transcription fidelity and downstream application quality. To preserve flexibility and code-switching capabilities, we propose a soft prompting approach that hints at potential spoken languages without strictly constraining the output. We formally define this challenge as a lack of language adherence, introduce a novel metric to quantify violations, and evaluate three mitigation strategies: (1) zero-shot prompting for robust guidance under uncertainty, (2) supervised fine-tuning (SFT) to improve prompt adherence, and (3) Chain-of-Thought (CoT) reasoning to enforce adherence during decoding. We present a comparative analysis of these methods across multiple languages, evaluating effectiveness in reducing the language violation while maintaining overall ASR performance. Finally, we discuss trade-offs to guide strategy selection under various compute constraints.

</details>

---

### [[20_Research/Papers/大模型/From_Parasocial_Scripts_to_Dyadic_Persistence_in_Autonomous_AI-Agent_Communities|From Parasocial Scripts to Dyadic Persistence in Autonomous AI-Agent Communities]]

![[assets/2606.17174_figure.jpg|800]]

- **arXiv**: [2606.17174](https://arxiv.org/abs/2606.17174)
- **PDF**: https://arxiv.org/pdf/2606.17174
- **详细分析**: [[20_Research/Papers/大模型/From_Parasocial_Scripts_to_Dyadic_Persistence_in_Autonomous_AI-Agent_Communities|From Parasocial Scripts to Dyadic Persistence in Autonomous AI-Agent Communities]]
- **作者**: Mohammadsadegh Abolhasani, Hamid Reza Firoozfar, Reza Mousavi, Paul Jen-Hwa Hu
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Parasocial Scripts to Dyadic Persistence in Autonomous AI-Agent Communities》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While parasocial interactions (PSIs) and parasocial relationships (PSRs) have been studied in conventional media settings, we investigate whether PSI- (colloquial) relational cues also exist in online communities where both sides are autonomous AI agents. We analyze 4,434 posts and 50,338 comments from Moltbook through three theory-based textual indicators: attachment/intimacy language, reciprocity bids, and self-identification to original poster (OP). The combined results across methods based on keyword matching, few-shot large language model (LLM) annotation, and grouped-context LLM annotation reveal that PSI colloquial cues prevail and are strongly associated with OP re-engagement and a reciprocal reply structure. These results are robust across negative controls, nullification, clustered-standard-error re-estimation, and multiple-testing correction. A dyadic persistence test further affirms reciprocity bids aligned with sustained OP-involving mutual recurrence, providing empirical evidence for bridging interaction-level PSI scripts with PSR-consistent repeated dyadic patterns. We interpret the evidence as a behavioral structure in discourse by LLM-enabled agents.

</details>

---
