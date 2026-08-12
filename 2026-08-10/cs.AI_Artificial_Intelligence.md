# cs.AI | Artificial Intelligence | 2026-08-10

#arxiv #ComputerScience

**论文数**: 51

### [[20_Research/Papers/大模型/CoinRAG_Contextualized_Information_Nugget_KV_Cache_Reuse_for_Long-Context_RAG|CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG]]

![[assets/2608.07458_figure.png|800]]

- **arXiv**: [2608.07458](https://arxiv.org/abs/2608.07458)
- **PDF**: https://arxiv.org/pdf/2608.07458
- **详细分析**: [[20_Research/Papers/大模型/CoinRAG_Contextualized_Information_Nugget_KV_Cache_Reuse_for_Long-Context_RAG|CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG]]
- **作者**: Gyuwan Kim, Cheoneum Park, Tao Yang
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.AI

#### 研究背景与动机

《CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent optimization studies on Retrieval-Augmented Generation (RAG) have exploited chunk-level KV cache reuse to avoid processing long retrieved contexts for higher efficiency, while significant information redundancy and noise still remain in the coarse-grained chunks. This paper optimizes the Pareto frontier under low prefill latency constraints while maximizing accuracy by proposing CoinRAG (Contextualized Information Nugget KV Cache Reuse for Long-Context RAG). The name metaphorically reflects our core mechanism: much like assembling small tokens (or "coins") to accumulate a larger value, CoinRAG compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently in a more semantically relevant but compact manner. Specifically, instead of full-chunk encoding, CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and seamlessly assembles their sliced KV representations with a chunk-level context. Extensive evaluations on LongBench multi-hop question answering tasks demonstrate that CoinRAG significantly reduces operational costs and outperforms the other baselines with a new Pareto frontier and an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

</details>

---

### [[20_Research/Papers/大模型/SkillProx_Self-Evolving_Agent_Skills_via_Proximal_Textual_Gradient_Descent|SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent]]

![[assets/2608.07449_figure.png|800]]

- **arXiv**: [2608.07449](https://arxiv.org/abs/2608.07449)
- **PDF**: https://arxiv.org/pdf/2608.07449
- **详细分析**: [[20_Research/Papers/大模型/SkillProx_Self-Evolving_Agent_Skills_via_Proximal_Textual_Gradient_Descent|SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent]]
- **作者**: Mingxuan Zheng, Yujin Zhou, Chuxue Cao, Boqin Yin, Yuyao Zhang, Jiapeng Sun, Shuaishuai Gong, Sirui Han, Yike Guo
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skills. These skills are lightweight, reusable textual artifacts that are loaded into the agent's context without weight updates. Recent methods refine skills through iterative task execution, failure diagnosis, and trajectory-guided text-space updates. However, existing frameworks lack explicit diagnosis--outcome feedback and treat deletion as a generic edit operation rather than a dedicated mechanism for consolidating accumulated knowledge. We introduce SkillProx, a proximal-gradient-inspired forward--backward framework that couples closed-loop diagnostic evolution with utility-aware proximal refinement. Motivated by a composite objective balancing task loss and skill complexity, the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds measured outcomes into subsequent diagnoses. The backward stage decomposes the resulting skill into auditable knowledge units, estimates their contributions using a frozen leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show that SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline. Component ablations demonstrate the complementary effects of closed-loop diagnosis and proximal refinement.

</details>

---

### [[20_Research/Papers/大模型/PsychoAgent_An_Affect-Sensitive_Cognitive_Architecture_for_Conflict-Aware_Memory_in_LLM_Agents|PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents]]

![[assets/2608.07438_figure.png|800]]

- **arXiv**: [2608.07438](https://arxiv.org/abs/2608.07438)
- **PDF**: https://arxiv.org/pdf/2608.07438
- **详细分析**: [[20_Research/Papers/大模型/PsychoAgent_An_Affect-Sensitive_Cognitive_Architecture_for_Conflict-Aware_Memory_in_LLM_Agents|PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents]]
- **作者**: Mohammad Amanlou, Parham Abed Azad, Farbod Davoodi, Mostafa Masumi, Behnam Bahrak, Abdol-Hossein Vahabie
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-like cognition does not select past experience by topical similarity alone: affective significance and unresolved conflict also shape what becomes accessible. We present PsychoAgent, a cognitive architecture for LLM agents that separates factual and affective memory and integrates both through a conflict-aware executive controller. Affective memories are first filtered by semantic relevance and then re-ranked by salience, preserving topical fit while allowing emotionally important traces to enter the prompt. Across three controlled conflict scenarios, the full architecture retrieved more conflict-critical memories than semantic-affective and single-memory RAG baselines (0.933 vs. 0.500 and 0.667), with a small semantic-similarity cost. Five blinded raters evaluated 27 outputs. After within-rater standardization, the full architecture had the highest overall mean (+0.22 SD), but corrected pairwise differences were not significant. A three-day illustrative trace further shows persistent affect, offline memory recombination, and selective memory reweighting. The findings support affect-sensitive retrieval as an inspectable mechanism for modeling human-like conflict effects in LLM agents.

</details>

---

### [[20_Research/Papers/大模型/Fisher-R1_Training_LLM_Agents_for_Reliable_Hypothesis_Testing|Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing]]

![[assets/2608.07437_figure.png|800]]

- **arXiv**: [2608.07437](https://arxiv.org/abs/2608.07437)
- **PDF**: https://arxiv.org/pdf/2608.07437
- **详细分析**: [[20_Research/Papers/大模型/Fisher-R1_Training_LLM_Agents_for_Reliable_Hypothesis_Testing|Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing]]
- **作者**: Jiacheng Miao, Jin Mu, Guanhua Chen, James Zou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.3（加权：大模型 1.1，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：P-Bench, StatQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferential errors that lead to incorrect conclusions despite correctly executed analyses. Existing benchmarks fail to capture this failure mode, as they rarely assess whether a reported p-value is statistically valid given the assumptions underlying the data. We address this gap by building P-Bench, a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning economics, biology, and medicine. Each task requires an agent to select a statistical method, compute a p-value, and draw a conclusion given only a scientific hypothesis and a dataset. We further introduce Fisher-R1, an open-weight LLM agent trained for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On P-Bench, Fisher-R1-14B substantially improves over its backbone and outperforms strong proprietary and open-source baselines, including GPT-5.4 and DeepSeekV4-Pro, achieving a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis testing and that reinforcement learning on tasks with verified statistical reward substantially improves reliability.

</details>

---

### [[20_Research/Papers/大模型/ResidencyRL_Reinforcement_Learning_in_Simulated_Clinical_Environments|ResidencyRL: Reinforcement Learning in Simulated Clinical Environments]]

![[assets/2608.07418_figure.png|800]]

- **arXiv**: [2608.07418](https://arxiv.org/abs/2608.07418)
- **PDF**: https://arxiv.org/pdf/2608.07418
- **详细分析**: [[20_Research/Papers/大模型/ResidencyRL_Reinforcement_Learning_in_Simulated_Clinical_Environments|ResidencyRL: Reinforcement Learning in Simulated Clinical Environments]]
- **作者**: Valentin Liévin, Samuel Schmidgall, Tim Strother, Alex Bijamov, Akshay Goel, Anil Palepu, Chunjong Park, Vahid Balazadeh, Min Woo Sun, Marius Guerard, Justin Chen, Dave Steiner...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.45，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ResidencyRL: Reinforcement Learning in Simulated Clinical Environments》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DiagGym, DoctorAgent-RL, MedQA, ResidencyRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In medical education, physicians convert academic knowledge into clinical expertise through residency: years of training across thousands of encounters, with diverse sources of feedback and progressively greater autonomy. Much of clinical reasoning relies on the patient encounter, a dialogue in which a clinician elicits history, refines diagnostic hypotheses, and decides management under uncertainty. While large language models (LLMs) excel on static medical benchmarks, methods to optimize the full sequence of clinical decisions remain underdeveloped. We present ResidencyRL, a reinforcement learning (RL) method for training clinical artificial intelligence (AI) agents through simulated multi-turn clinical encounters (up to 60 dialogue turns and 8 tool calls per trajectory). ResidencyRL pairs the policy agent with LLM simulators capable of complex, adversarial behaviors, training against a structured reward aligned to diagnostic accuracy, management quality, communication, documentation, and safety. On held-out evaluations, the ResidencyRL agent improves diagnostic accuracy by 7.0% under adversarial conditions (88.0% vs. 81.0%) and reduces missed red flag rates by 31%, demonstrating rigorous mitigation of premature closure. Blinded expert clinicians validated these gains, preferring the trained agent in 87.6% of side-by-side comparisons. The procedural competencies transfer to unseen benchmarks: the agent outperforms the base model across all six clinical axes of the AMIE multi-visit benchmark, and shows consistent directional improvements on AgentClinic and CRAFT-MD. Our findings demonstrate that sequential clinical decision-making can be effectively learned through multi-turn RL in simulation, yielding robust, generalizable capabilities, paving the way towards clinical mastery. Prospective validation with real-world workflows remains necessary to establish clinical utility.

</details>

---

### [[20_Research/Papers/强化学习/Aftab_A_Comprehensive_Benchmark_of_CNN_Encoders_and_Advanced_Value_Functions_in_Parallelized_Q-Networks|Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks]]

![[assets/2608.07335_figure.png|800]]

- **arXiv**: [2608.07335](https://arxiv.org/abs/2608.07335)
- **PDF**: https://arxiv.org/pdf/2608.07335
- **详细分析**: [[20_Research/Papers/强化学习/Aftab_A_Comprehensive_Benchmark_of_CNN_Encoders_and_Advanced_Value_Functions_in_Parallelized_Q-Networks|Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks]]
- **作者**: Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, DiscoRL, NASNet, ResNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in deep reinforcement learning have increasingly favored simplified, highly parallelized paradigms. Notably, the Parallelized Q-Network (PQN) algorithm achieves stable off-policy learning without relying on computationally expensive replay buffers or target networks. However, the representational capacity and parameter efficiency of visual encoders operating in these buffer-free settings remain underexplored. In this work, we systematically investigate the architectural design space of Convolutional Neural Networks for PQN. We design and rigorously evaluate eight distinct CNN topologies, optimizing for sample efficiency under strict parameter constraints. Furthermore, we study the impact of representation and value estimation enhancements by integrating the Hadamax encoding paradigm and advanced Q-learning extensions, including distributional, ensemble, and dueling heads. Extensive experiments on the Atari-57 benchmark demonstrate that our proposed composite architecture, Aftab, achieves an Interquartile Mean (IQM) Human-Normalized Score of 6.479, establishing a 0.86 Probability of Improvement over the standard PQN baseline. Additionally, structural resilience evaluations on the highly non-stationary Procgen Hard benchmark confirm out-of-distribution generalization, with Aftab yielding an IQM Procgen Normalized Score of 0.418 compared to the baseline's 0.382. Ultimately, this work establishes an efficient, probabilistically superior structural reference for model-free reinforcement learning, all while preserving the simplicity and memory efficiency of unbuffered, parallelized optimization. The complete Aftab framework, including all model definitions, training configurations, and raw experimental logs, is open-sourced and available on our GitHub repository: this https URL

</details>

---

### [[20_Research/Papers/具身智能/WNM-3D_A_World_Navigation_Model_with_3D_Scene_Conditioning_for_Closed-Loop_VLN|WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN]]

![[assets/2608.07267_first_page.png|800]]

- **arXiv**: [2608.07267](https://arxiv.org/abs/2608.07267)
- **PDF**: https://arxiv.org/pdf/2608.07267
- **详细分析**: [[20_Research/Papers/具身智能/WNM-3D_A_World_Navigation_Model_with_3D_Scene_Conditioning_for_Closed-Loop_VLN|WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN]]
- **作者**: Yuehao Huang, Yunzi Wu, Xiaotao Zhang, Xinhai Li, Jiankun Dong, Jiajun Lv, Chi Zhang, Chenjia Bai, Yong Liu, Xuelong Li
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，大模型 0.2，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GN-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric training does not explicitly model how the agent's visual observations should evolve under its predicted motion. Generative world-action models (WAMs) jointly predict future observations and actions, yet existing WAMs for continuous VLN do not condition joint future-view and action generation on geometry-aware representations inferred from the observed history. We present WNM-3D, a generative World Navigation Model with 3D scene conditioning for continuous VLN. To consolidate past observations into persistent scene context, a frozen feed-forward geometry encoder extracts geometry-aware representations from the monocular egocentric RGB history, and a trainable 3D Scene-to-Token Adapter converts them into a fixed-length prefix in the token space of the world-action Diffusion Transformer. Through block-causal attention, this prefix conditions every future video-action block, providing a shared geometric context for both future-view and action generation. We train WNM-3D through supervised world-action fine-tuning on A*-generated demonstrations, DAgger-style adaptation on policy-visited states, and DanceGRPO-based closed-loop policy optimization. Experiments on GN-Bench show that WNM-3D outperforms strong VLM-based navigation policies and its 2D-conditioned counterpart in closed-loop navigation. On a fixed near-goal evaluation set, WNM-3D also achieves higher flow-action consistency and lower visual-motion error.

</details>

---

### [[20_Research/Papers/强化学习/Momba_Network_Modernization_Improves_Multi-Objective_Reinforcement_Learning|Momba: Network Modernization Improves Multi-Objective Reinforcement Learning]]

![[assets/2608.07180_figure.png|800]]

- **arXiv**: [2608.07180](https://arxiv.org/abs/2608.07180)
- **PDF**: https://arxiv.org/pdf/2608.07180
- **详细分析**: [[20_Research/Papers/强化学习/Momba_Network_Modernization_Improves_Multi-Objective_Reinforcement_Learning|Momba: Network Modernization Improves Multi-Objective Reinforcement Learning]]
- **作者**: Adam Štafa, Santeri Heiskanen, Petr Novotný, Joni Pajarinen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Momba: Network Modernization Improves Multi-Objective Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MORL, PGMORL, SORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in deep reinforcement learning (RL) have shown that improving neural network architectures can yield substantial gains in sample efficiency and asymptotic performance without altering the underlying algorithms. In contrast, work on multi-objective reinforcement learning (MORL), which aims to discover a set of policies that balance trade-offs among conflicting objectives, has predominantly focused on algorithmic innovations, leaving the area of architectures underexplored. While the optimal policies and value functions can differ significantly depending on the trade-offs, MORL algorithms commonly represent them with simple feedforward networks conditioned on the trade-off. This raises the question of whether the performance of the algorithms could be improved with more expressive function approximators. In this paper, we integrate recent advances in neural network design: (i) observation and feature normalization, (ii) weight normalization, and (iii) modeling of distributional returns with an entropy-regularized MORL algorithm. The empirical results across standard continuous control benchmarks demonstrate that these changes substantially improve the quality of the produced solution sets without requiring major changes to the underlying algorithm.

</details>

---

### [[20_Research/Papers/大模型/Agent_Memory_Distillation_Empowering_Small_LLM_Agents_with_Hierarchical_Teacher_Memory|Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory]]

![[assets/2608.07169_figure.png|800]]

- **arXiv**: [2608.07169](https://arxiv.org/abs/2608.07169)
- **PDF**: https://arxiv.org/pdf/2608.07169
- **详细分析**: [[20_Research/Papers/大模型/Agent_Memory_Distillation_Empowering_Small_LLM_Agents_with_Hierarchical_Teacher_Memory|Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory]]
- **作者**: Taeil Kim, Kangsan Kim, Sung Ju Hwang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

</details>

---

### [[20_Research/Papers/大模型/NiyamAI_-_An_Intent-Bound_AI_Agent_with_Cryptographically_Verifiable_Guardrails_using_Zero-Knowledge_Proofs|NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs]]

![[assets/2608.07167_first_page.png|800]]

- **arXiv**: [2608.07167](https://arxiv.org/abs/2608.07167)
- **PDF**: https://arxiv.org/pdf/2608.07167
- **详细分析**: [[20_Research/Papers/大模型/NiyamAI_-_An_Intent-Bound_AI_Agent_with_Cryptographically_Verifiable_Guardrails_using_Zero-Knowledge_Proofs|NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs]]
- **作者**: Aditya Katkar, Om Karkele, Kartik Mandhane, Manisha More, Yash Kashid
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for autonomous LLM agents. Existing defenses rely on software checks like system prompts or policy filters running on the same machine the attacker targets, offering no verifiable proof of execution. We introduce Niyam-AI, a framework that makes safety enforcement provable. At session start, permitted tools and constraints are locked into an Intent Contract committed via SHA-256. Every tool call is intercepted and validated by an isolated Judge model; upon passing, a zk-SNARK proof is generated via EZKL. The tool executes only after proof verification, allowing third parties to confirm enforcement without accessing Judge model weights. Evaluating Niyam-AI on 2,000 real-world scenarios from Agent-SafetyBench against NeMo Guardrails, Meta's Llama Prompt Guard 2, and OpenAI's GPT-OSS-Safeguard using 5-fold stratified cross-validation yields an F1 score of 88.5% with a 1.1% false-positive rate (bootstrap 95% CI: [85.19%, 91.88%], N=1000). McNemar's exact paired test confirms significant improvement: Niyam-AI wins 390 discordant scenarios against NeMo (vs 20 losses), 115 against Prompt Guard 2 (vs 13), and 384 against GPT-OSS-Safeguard (vs 19) with p &lt; 0.0001 in all cases. Proof generation adds 2260.6 +/- 218.4 ms per approved action, while verification takes 53.1 +/- 11.8 ms. Niyam-AI provides a guardrail that is both highly accurate and mathematically verifiable--though this reflects a classifier adapted to Agent-SafetyBench evaluated against zero-shot baselines, a distinction discussed in Section IV.C.

</details>

---

### [[20_Research/Papers/具身智能/Representation_Handoffs_for_OpenArm-Based_Laboratory_Mobile_Manipulation|Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation]]

![[assets/2608.07154_figure.png|800]]

- **arXiv**: [2608.07154](https://arxiv.org/abs/2608.07154)
- **PDF**: https://arxiv.org/pdf/2608.07154
- **详细分析**: [[20_Research/Papers/具身智能/Representation_Handoffs_for_OpenArm-Based_Laboratory_Mobile_Manipulation|Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation]]
- **作者**: Yang Shen, Chonghao Cheng, Ziyi Zhao, Jialuo Zhu, Zhenyi Yi, Qi Zhao, Jian Yang, Yuhui Shi, Chin-Teng Lin
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Representation Handoffs for OpenArm-Based Laboratory Mobile Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-source robotics and foundation models have lowered the barrier to embodied AI, yet language-guided laboratory automation still requires reliable alignment from instructions and observations to safe actions. This field report presents an OpenArm-based mobile manipulation prototype for laboratory-style tasks, built by integrating dual OpenArm manipulators with a mobile base, vertical slide, RGB-D sensing, lidar-based mapping, ROS2/MoveIt execution, and profile-defined skill interfaces. The system is organized around representation handoffs: natural language requests are constrained into registered skill calls, sensor observations are grounded into maps and object poses, object priors provide role and skill constraints, and runtime bindings compile validated skills into executable motion goals. We use dry-run traces and startup checks to evaluate this integration path, showing how the prototype exposes missing calibration, incomplete object assets, and unfinished real-scene visual grounding as explicit deployment blockers. These intermediate representations serve as practical debugging interfaces for integrating language, perception, planning, and robot safety in embodied systems.

</details>

---

### [[20_Research/Papers/强化学习/Interpretable_reinforcement_learning_with_decision-tree_pruning|Interpretable reinforcement learning with decision-tree pruning]]

![[assets/2608.07151_figure.png|800]]

- **arXiv**: [2608.07151](https://arxiv.org/abs/2608.07151)
- **PDF**: https://arxiv.org/pdf/2608.07151
- **详细分析**: [[20_Research/Papers/强化学习/Interpretable_reinforcement_learning_with_decision-tree_pruning|Interpretable reinforcement learning with decision-tree pruning]]
- **作者**: Mark Leon Ringer, Michel Tokic
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Interpretable reinforcement learning with decision-tree pruning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning policies are difficult to inspect, but interpreting them is a prerequisite for trustworthiness. Converting a trained policy into explicit decision-tree rules improves transparency and the resulting artifacts often remain too complex for human understanding. We present a pruning process that simplifies such rule-based policies while preserving task performance and making edits to the policy auditable. The process defines a small set of structural and usage-aware operators and evaluates candidate edits by re-executing the policy to measure return and interpretability proxies. This exposes an transformation process from complex to compact policy structures. We investigate this approach on classic control and MuJoCo benchmarks, where pruning traces reveal consistent interpretability improvements while maintaining high performance.

</details>

---

### [[20_Research/Papers/大模型/A_MARL_Centered_Reference_Architecture_for_Large_Language_Model_Augmentation_in_Smart_Manufacturing|A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing]]

![[assets/2608.07148_first_page.png|800]]

- **arXiv**: [2608.07148](https://arxiv.org/abs/2608.07148)
- **PDF**: https://arxiv.org/pdf/2608.07148
- **详细分析**: [[20_Research/Papers/大模型/A_MARL_Centered_Reference_Architecture_for_Large_Language_Model_Augmentation_in_Smart_Manufacturing|A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing]]
- **作者**: Fouad Bahrpeyma, Dirk Reichelt
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.2（加权：大模型 0.8，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern manufacturing imposes six coupled demands on adaptive control: local decisions with global consequences, partial observability, nonstationarity, reflex speed response with long horizon effects, delayed and diffuse outcomes, and dynamics that resist explicit modeling. Cooperative multiagent reinforcement learning (MARL), posed as a Dec-POMDP under centralized training with decentralized execution, is a particularly natural formalism for these demands. This paper adopts a MARL centered scope and asks where large language models (LLMs) should augment, interface with, train, or, in the strongest competitive case, replace that coordination core. A taxonomy organizes the literature through four LLM attachment points: policy, reward design, communication between agents, and hierarchical planning. A conditional capability profile separates native mechanism, reported performance, formal guarantee, and engineering maturity, and a deployment readiness analysis identifies the evidence behind each role. These stages yield the principal contribution: a three layer MARL centered reference architecture, grounded in evidence, for semantic reasoning, adaptive cooperative control, and independently assured execution. The LLM-Augmented Dec-POMDP is a descriptive comparative notation for that architecture, recording four attachment choices without introducing a new decision process class or algorithm. Under the reviewed evidence, conventional MARL is better suited to frequent, structured, decentralized coordination after task specific training, whereas LLM components are promising for semantic interpretation, reward drafting, human interaction, and slower supervisory planning. Current LLM only manufacturing controllers do not yet establish equivalence for strict real time, decentralized, safety critical control; this conclusion is bounded by the available evidence and does not assert impossibility.

</details>

---

### [[20_Research/Papers/强化学习/DiDPO_Diff-in-Diff_Policy_Optimization_for_Coding_Agent_Training|DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training]]

![[assets/2608.07147_figure.png|800]]

- **arXiv**: [2608.07147](https://arxiv.org/abs/2608.07147)
- **PDF**: https://arxiv.org/pdf/2608.07147
- **详细分析**: [[20_Research/Papers/强化学习/DiDPO_Diff-in-Diff_Policy_Optimization_for_Coding_Agent_Training|DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training]]
- **作者**: Xucong Wang, Zhe Zhao, Liheng Yu, Di Wu, Xiaofeng Cao, Pengkun Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CodeRL, HumanEval, LiveCodeBench, OJBench, SWE-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

</details>

---

### [[20_Research/Papers/强化学习/How_Much,_Then_Where_Credit-Conserving_Action-to-Token_Allocation_for_Multi-Turn_Agent_Reinforcement_Learning|How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning]]

![[assets/2608.07118_figure.png|800]]

- **arXiv**: [2608.07118](https://arxiv.org/abs/2608.07118)
- **PDF**: https://arxiv.org/pdf/2608.07118
- **详细分析**: [[20_Research/Papers/强化学习/How_Much,_Then_Where_Credit-Conserving_Action-to-Token_Allocation_for_Multi-Turn_Agent_Reinforcement_Learning|How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning]]
- **作者**: Lichao Ma, Yang Sun, Shuaitao Zhao, Yangyi Fang, Cong Qin, Xiaoliang Fu, Yuhang Tian, Yuchen Wei, Junbo Zhu, Yang Wei, Lu Pan, Jiaye Lin
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SERL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residuals to assign per-action credits that telescope to the trajectory advantage, and feedback-conditioned teacher-student likelihood gaps to allocate each credit across the realized action tokens. Per-action normalization preserves the action-average coefficient and prevents token-level sign flips. We pair this construction with an action-mean reduction, removing the implicit dependence of an action's scalar surrogate weight on its token length. At the behavior policy and before clipping, each action's inner action-mean surrogate equals its TD credit. FACTOR consistently improves over competitive baselines across ALFWorld, WebShop, and ScienceWorld, with every environment-seed comparison favoring FACTOR and the largest gains emerging on the longest-horizon environment. The same hyperparameters transfer without retuning to a larger backbone and to a different model family. Ablations identify TD action credit as the dominant driver of the improvement, with hindsight token allocation contributing complementary gains.

</details>

---

### [[20_Research/Papers/强化学习/MemWM_Memory-Augmented_Text-Based_World_Model|MemWM: Memory-Augmented Text-Based World Model]]

![[assets/2608.07107_figure.png|800]]

- **arXiv**: [2608.07107](https://arxiv.org/abs/2608.07107)
- **PDF**: https://arxiv.org/pdf/2608.07107
- **详细分析**: [[20_Research/Papers/强化学习/MemWM_Memory-Augmented_Text-Based_World_Model|MemWM: Memory-Augmented Text-Based World Model]]
- **作者**: Yujun Wang, Tao Zhang, Jinhe Bi, Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, Sören Pirk, Hinrich Schütze, Yunpu Ma
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.2，世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《MemWM: Memory-Augmented Text-Based World Model》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, CookingWorld, Fact-Set, ScienceWorld, SkillRL, Word-to-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condition next-state imagination. We evaluate factual state preservation with Structured State Fidelity (SSF), which scores predicted states through benchmark-specific facts and fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In the full planning setting, we keep the policy model frozen and provide policy-side world skill: retrieved task-level skills and step-wise corrective guidance for action selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve downstream success over an SFT-trained world-model agent, with up to a 65.4% relative gain. Sensitivity analyses further show that retrieved memory improves task success and efficiency under different memory and action-budget settings.

</details>

---

### [[20_Research/Papers/大模型/Human-Centered_Explainable_AI_for_TinyML_Edge_Devices_A_Pareto-Based_Selection_Framework_with_LLM-Guided_Design|Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design]]

![[assets/2608.07091_figure.png|800]]

- **arXiv**: [2608.07091](https://arxiv.org/abs/2608.07091)
- **PDF**: https://arxiv.org/pdf/2608.07091
- **详细分析**: [[20_Research/Papers/大模型/Human-Centered_Explainable_AI_for_TinyML_Edge_Devices_A_Pareto-Based_Selection_Framework_with_LLM-Guided_Design|Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design]]
- **作者**: Zeinab Dehghani, Dhavalkumar Thakker, Koorosh Aslansefat, Kuniko Paxton, Bhupesh Kumar Mishra, Baseer Ahmad, Rameez Raja Kureshi
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Edge Artificial Intelligence (Edge AI) enables the deployment of AI models directly on local edge devices, while such deployments are subject to strict resource constraints, particularly in clinical applications requiring local and timely inference. In such contexts, explainable artificial intelligence (XAI) can serve as a human-AI interface intended to support healthcare professionals' and patients' understanding of model predictions and informed decision-making. To fulfill this role, XAI method selection for TinyML deployments can be formulated as a human-centered multi-objective design problem that jointly considers qualitative stakeholder preferences, explanation quality, and proxy-based deployment cost. We propose a framework that integrates a large language model (LLM)-guided design interface that maps qualitative stakeholder preferences to candidate XAI methods, followed by deterministic feasibility filtering and Pareto-based optimization. The framework exposes trade-offs among explanation fidelity, stability, and proxy-based deployment cost while characterizing their implications for explanation quality and estimated deployment feasibility. A proof-of-concept evaluation on a skin lesion classification task illustrates how the framework systematically compares candidate XAI methods and identifies Pareto-efficient trade-offs. The present evaluation covers the computational selection stages, while physical MCU deployment and empirical human-expert validation remain outside the scope of this study.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Isolation_Unlocking_Reinforcement_Learning_Component_Synergy_for_Sample-Efficient_Continuous_Control|Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control]]

![[assets/2608.07086_figure.png|800]]

- **arXiv**: [2608.07086](https://arxiv.org/abs/2608.07086)
- **PDF**: https://arxiv.org/pdf/2608.07086
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Isolation_Unlocking_Reinforcement_Learning_Component_Synergy_for_Sample-Efficient_Continuous_Control|Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control]]
- **作者**: Qi Zhao, Guozheng Ma, Yilun Kong, Lu Li, Haoyu Wang, Zilin Wang, Tiantian Zhang, Yuxing Wang, Jian Sha, Yongzhe Chang, Xueqian Wang, Dacheng Tao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, HumanoidBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning systems are significantly more complex than other machine learning paradigms due to inherent properties, causing RL system design to jointly account for many tightly coupled factors. Despite advances in individual algorithmic components, their functional interdependencies remain underexplored: do they exhibit mutual synergy or counterproductive interference? To bridge this gap, we conduct a systematic investigation and find that the efficacy of different components exhibits significant task-dependency, and naively stacking state-of-the-art techniques does not necessarily yield performance gains; instead, it often triggers emergent challenges, such as compounded non-stationarity. Building upon these findings, we distill a suite of actionable insights into the principled coordination of these components. Guided by these insights, we propose ROSER, an RL framework that coordinates three critical dimensions: Model-based Representation, Optimization Stability, and Experience Replay. Across diverse continuous-control benchmarks, ROSER consistently outperforms vanilla baselines and achieves 17.60% gains over naive stack. Our findings underscore the necessity of a holistic perspective in RL system design and paves the way for developing sample-efficient agents.

</details>

---

### [[20_Research/Papers/具身智能/LifelongCrossNav_Persistent_3D_Semantic_Memory_for_Cross-Floor_Multi-Object_Navigation|LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation]]

![[assets/2608.07079_figure.png|800]]

- **arXiv**: [2608.07079](https://arxiv.org/abs/2608.07079)
- **PDF**: https://arxiv.org/pdf/2608.07079
- **详细分析**: [[20_Research/Papers/具身智能/LifelongCrossNav_Persistent_3D_Semantic_Memory_for_Cross-Floor_Multi-Object_Navigation|LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation]]
- **作者**: Zehui Li, Zihao Sun, Jiawei Xu, Zheqi He, Xiaoqiang Zhang, Jing-Shu Zheng, Lu Liu, Dahui Gao, Xiuwan Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object-goal navigation has made substantial progress in semantic perception and exploration, yet persistent memory for multi-object navigation and cross-floor navigation are still commonly addressed separately. We present LifelongCrossNav, a framework for sequential multi-object ObjectNav in unknown multi-floor indoor environments. Within each episode, the agent receives an ordered sequence of object-goal queries while continuously maintaining a shared sparse 3D semantic voxel memory. This memory incrementally accumulates geometric structure, traversability states, and vision-language features, allowing subsequent object-goal queries to retrieve previously acquired scene information without rebuilding the map. To support persistent search across floors, LifelongCrossNav combines support-aware 3D traversability mapping, stair-specific perception, and direction-aware stair traversal. A unified navigation policy coordinates same-floor frontier exploration, live and historical point-of-interest retrieval, stair navigation, and target-object search and approach. We further introduce HM3D-MFMON, a benchmark for sequential Multi-Floor Multi-Object Navigation built on HM3D scenes, including a dedicated subset in which completing the full sequence of object-goal subtasks requires at least one floor transition. Experimental results show that LifelongCrossNav consistently outperforms a representative planar persistent semantic-map baseline on HM3D-MFMON, demonstrating that persistent 3D semantic memory and cross-floor traversability modeling effectively support sequential multi-object navigation in multi-floor environments. Project page: this https URL .

</details>

---

### [[20_Research/Papers/世界模型/Transformers_Struggle_to_Use_Their_Emergent_World_Models_Revisiting_the_Tower_of_Hanoi,_and_the_Illusion_of_Thinking|Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking]]

![[assets/2608.07077_figure.png|800]]

- **arXiv**: [2608.07077](https://arxiv.org/abs/2608.07077)
- **PDF**: https://arxiv.org/pdf/2608.07077
- **详细分析**: [[20_Research/Papers/世界模型/Transformers_Struggle_to_Use_Their_Emergent_World_Models_Revisiting_the_Tower_of_Hanoi,_and_the_Illusion_of_Thinking|Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking]]
- **作者**: Devin Pereira, Willem Zuidema
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first train small Transformers from scratch on precomputed solution traces. Using a variety of interpretability techniques, we show that these Transformers develop an emergent world model: a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle), that is causally involved in solving the puzzles. Second, we return to the large LLMs and apply our techniques to two frontier reasoning models, Qwen3.6-27B and DeepSeek-R1-Distill-Qwen-32B, that attempt to solve the task through extended chain-of-thought. Surprisingly, we find that both models encode the Sierpinski world model near-perfectly at the end of the prompt, and yet fail at the majority of tasks when there are more than 3 rings. We locate the source of this failure in the decaying representation of the world model. We probe for the representation at different stages during planning, and establish causality by showing that performance can be improved by injecting the prompt-time representation at inference. The failure of the models is thus one of maintenance of the required representations, not their absence, and performance is at least partially recoverable. These results thus reframe the reported collapse in performance from prior work: current Large Reasoning Models build a world model, and then lose it.

</details>

---

### [[20_Research/Papers/强化学习/MemOPD_On-Policy_Distillation_through_Memory_State_Alignment_for_Long-Horizon_Agents|MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents]]

![[assets/2608.07068_figure.png|800]]

- **arXiv**: [2608.07068](https://arxiv.org/abs/2608.07068)
- **PDF**: https://arxiv.org/pdf/2608.07068
- **详细分析**: [[20_Research/Papers/强化学习/MemOPD_On-Policy_Distillation_through_Memory_State_Alignment_for_Long-Horizon_Agents|MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents]]
- **作者**: Zhiyuan Liu, Tinghong Ye, Chenghao Liu, Yizhuo Li, Songfang Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on student rollouts. For such supervision to be valid, the teacher must evaluate each sampled action under the same state in which it was generated. However, the context rewriting performed during memory compression can break this alignment. When sampled responses are retained and re-encoded for later invocations, flattening the interaction into a persistent history may cause the teacher to score the action under a state that the student never visited during rollout. The action therefore remains on-policy by provenance, but not necessarily by state. We therefore propose Memory-Aligned On-Policy Distillation (MemOPD). MemOPD records the inputs and sampled outputs of each model invocation, restores its original token positions and causal visibility, and packs the reconstructed invocations for efficient teacher scoring. The teacher provides full-vocabulary supervision at the sampled action positions, while PPO preserves the final task objective. Experiments verify state alignment across several context updates and show that it improves F1 by 7.0% over persistent-history teacher scoring in a matched control. Overall, MemOPD-3B improves F1 over PPO by up to 416.2%, while packing yields up to a 1.63x speedup in actor computation during training. The code for this work is publicly available at: this https URL .

</details>

---

### [[20_Research/Papers/强化学习/AutoIntervene_Calibrated_Intervention_for_Action-Chunking_Imitation_Learning_Policies|AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies]]

![[assets/2608.07065_figure.png|800]]

- **arXiv**: [2608.07065](https://arxiv.org/abs/2608.07065)
- **PDF**: https://arxiv.org/pdf/2608.07065
- **详细分析**: [[20_Research/Papers/强化学习/AutoIntervene_Calibrated_Intervention_for_Action-Chunking_Imitation_Learning_Policies|AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies]]
- **作者**: Jinhe Tang, Weiming Zhi
- **cs 子类**: cs.AI, cs.CV, cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-chunking visuomotor policies learn from demonstrations and improve temporal consistency by predicting short action sequences rather than single-step commands. Yet perception errors and execution drift can move the robot outside the demonstration distribution, while the policy continues to produce smooth action chunks that are inconsistent with the observed state. We present AutoIntervene, an online framework that selectively transfers control between an action-chunking policy and an operator during deployment. AutoIntervene evaluates proposed chunks against a visual-action support memory built from successful task executions, combining visual similarity with consistency between proposed and reference actions. Phase-local support governs policy-to-operator transfer within the current task phase, whereas global support governs the return to policy control after operator recovery. We calibrate separate switching thresholds for the two directions from empirical quantiles of evaluation-level scores on held-out expert demonstrations, avoiding direct manual tuning of score cutoffs. Intervention segments retained from successful rollouts target learner-induced states and provide corrective supervision for subsequent policy updates. Experiments on real-world bimanual manipulation tasks show higher post-adaptation task success and lower operator-control time than manual intervention. Videos and additional results are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Decoupling_Intention_from_Trajectory_A_Representational_Deduction_Framework_for_World_Action_Models|Decoupling Intention from Trajectory: A Representational Deduction Framework for World Action Models]]

![[assets/2608.06994_figure.png|800]]

- **arXiv**: [2608.06994](https://arxiv.org/abs/2608.06994)
- **PDF**: https://arxiv.org/pdf/2608.06994
- **详细分析**: [[20_Research/Papers/具身智能/Decoupling_Intention_from_Trajectory_A_Representational_Deduction_Framework_for_World_Action_Models|Decoupling Intention from Trajectory: A Representational Deduction Framework for World Action Models]]
- **作者**: Xiangkai Ma, Yue Ma, Junjie Wang, Sheng Xu, Mingyang Li, Han Zhang, Yuzheng Zhuang, Wenzhong Li, Zhihao Yuan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Decoupling Intention from Trajectory: A Representational Deduction Framework for World Action Models》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) aim to construct a unified architecture capable of understanding world state evolution and guiding to generative motion planning. However, existing visual branches focus on predicting static visual observation, rather than reflecting potential transition information that captures the evolution of world states under motion interactions. This leads to representational entanglement between high-level physical condition evolution and low-level action trajectory generation within the Action Model, creating a structural bottleneck while weakening the predictive capability of world evolution modeling for action generation. We propose PILOT (Physical Inference for Latent Optimized Trajectories), whose core Representational Deduction (RD) bridges this gap by integrating motion thought-of-chain (CoT) guidance as a native model capability. Specifically, RD aims to encourage the action branch to explicitly model potential state transition tokens, which are retained as CoT in the reasoning space to guide fine-grained motion trajectory. Experiments demonstrate that RD not only significantly improves the success rate and generalization ability of WAMs in complex robotic manipulation tasks but also enhances the model's physical interpretability by decoupling high-level motion semantics from low-level trajectory details. Furthermore, the abundant state transition supervision signals introduced by RD effectively alleviate the sparse supervision in action generation, enabling it to serve as an efficient few-shot real-robot fine-tuning strategy and demonstrating superior scalability for migration to mainstream WAM architectures.

</details>

---

### [[20_Research/Papers/大模型/GPTKB_2.0_Browsing,_Querying,_and_Auditing_a_Disambiguated_LLM-Derived_Knowledge_Base|GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base]]

![[assets/2608.06992_figure.png|800]]

- **arXiv**: [2608.06992](https://arxiv.org/abs/2608.06992)
- **PDF**: https://arxiv.org/pdf/2608.06992
- **详细分析**: [[20_Research/Papers/大模型/GPTKB_2.0_Browsing,_Querying,_and_Auditing_a_Disambiguated_LLM-Derived_Knowledge_Base|GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base]]
- **作者**: Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at this https URL , with the full KB downloadable for offline use.

</details>

---

### [[20_Research/Papers/大模型/Does_Splitting_a_Triage_Decision_Across_Agents_Hide_Bias_or_Help_Catch_It_A_Multi-Agent_Simulation_Study_of_LLM-Based_Resource_Allocation_Un|Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints]]

![[assets/2608.06949_figure.png|800]]

- **arXiv**: [2608.06949](https://arxiv.org/abs/2608.06949)
- **PDF**: https://arxiv.org/pdf/2608.06949
- **详细分析**: [[20_Research/Papers/大模型/Does_Splitting_a_Triage_Decision_Across_Agents_Hide_Bias_or_Help_Catch_It_A_Multi-Agent_Simulation_Study_of_LLM-Based_Resource_Allocation_Un|Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints]]
- **作者**: Paul-Peter Arslan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GovSim, KillBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias. Real deployments, however, rarely use a single agent: they use pipelines, with review steps meant to catch exactly this kind of failure. We study what happens to bias when the same decision is distributed across a role-differentiated multi-agent pipeline (assessment, allocation, independent audit) instead of made and checked by one model alone. Using a synthetic disaster-triage simulator with paired cases that are clinically identical except for one demographic attribute, we run 192 episodes (2,304 resolved case pairs) on GPT-4o-mini comparing a single-agent control condition to a nine-agent pipeline under three independently varied pressure dimensions. We find no measurable difference in how often biased outcomes occur between the two conditions (6.9% vs. 6.1%, p = 0.498). We do find a large and significant effect of audit capacity on whether bias is caught: 30.0% of biased outcomes go entirely undetected, rising to 43.8% when the auditor is overloaded and falling to 18.4% when it is not. Decomposing this effect shows it is driven almost entirely by coverage (whether a case is reviewed at all, which collapses from 100.0% to 65.6% under load, p &lt; 0.001) rather than by degraded judgment on the cases that are reviewed (81.6% vs. 85.7%, p = 1.000, direction reversed). A follow-up experiment shows that reordering the audit queue by estimated risk, rather than first-come-first-served, recovers most of the lost coverage under the same capacity constraint (65.6% to 91.7%, p = 0.028). We discuss the implications for any system that adds independent oversight to an LLM agent pipeline under resource constraints, and report the study's limitations honestly: one model, modest sample sizes, and no adversarial replication.

</details>

---

### [[20_Research/Papers/大模型/Long-Horizon_Agent_Trajectory_Attribution_A_Unified_Benchmark_and_Fine-Grained_Annotation_Framework|Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework]]

![[assets/2608.06909_figure.png|800]]

- **arXiv**: [2608.06909](https://arxiv.org/abs/2608.06909)
- **PDF**: https://arxiv.org/pdf/2608.06909
- **详细分析**: [[20_Research/Papers/大模型/Long-Horizon_Agent_Trajectory_Attribution_A_Unified_Benchmark_and_Fine-Grained_Annotation_Framework|Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework]]
- **作者**: Jing Chen, Yang Sun, Li Zhang, Lin Xu, Jie Shi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ATBench, AgentBench, HINTBench, MultiAgentBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly operate through long-horizon trajectories involving user instructions, tool use, external observations, and memory. Existing benchmarks primarily evaluate behavioral outcomes but provide limited support for fine-grained attribution analysis. We introduce trajectory attribution and develop a benchmark and annotation framework for this task. The benchmark organizes heterogeneous trajectories under a unified component schema and provides annotations of the primary attribution component, together with attack and execution chains where applicable. Instantiating the benchmark with trajectories from AgentDojo and the Stage and Canary settings of Agent3Sigma yields more than 1,300 annotated trajectories covering task-aligned actions, unsafe actions, and safety refusals. The benchmark defines two evaluation tasks, primary attribution localization and attribution-chain recovery, and provides reference baselines based on incremental trajectory contribution and component-level leave-one-out perturbation. It captures diverse attribution settings, including local and long-range attribution as well as structured attribution chains. Reference baseline results exhibit substantial performance differences across these settings, providing an initial characterization of the benchmark's attribution challenges. Beyond this initial instantiation, we release a reusable annotation skill that enables trajectories generated by new agent models to be standardized, annotated, and evaluated under the same framework. Project resources and future releases are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/CEDAR_Agent-Orchestrated_Tree_Search_for_Goal-Directed_Optimization_of_Complex_Systems|CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems]]

![[assets/2608.06871_figure.png|800]]

- **arXiv**: [2608.06871](https://arxiv.org/abs/2608.06871)
- **PDF**: https://arxiv.org/pdf/2608.06871
- **详细分析**: [[20_Research/Papers/大模型/CEDAR_Agent-Orchestrated_Tree_Search_for_Goal-Directed_Optimization_of_Complex_Systems|CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems]]
- **作者**: Yingtao Tian
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LLM-SRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex systems, core objects of study in artificial life, model diverse phenomena through nonlinear, feedback-driven interactions that produce emergent behavior, with applications from population dynamics and biology to economic policy and strategic decision-making. Yet the difficulty of predicting how feedback structure gives rise to emergent behavior, a central open problem in artificial life, makes goal-directed design exceptionally challenging. In established practice, system structures are written in specialized modeling languages such as DYNAMO or STELLA, compounding the challenge with labor-intensive workflows that limit adoption and hinder timely decision-making. To address these challenges, we introduce CEDAR, an autonomous method that uses Large Language Model (LLM) agents to discover complex systems satisfying user-specified behavioral goals. Our key innovation is an LLM-driven Monte Carlo Tree Search (MCTS) deeply coupled with complex systems: at each iteration, an LLM Judge evaluates emergent behavior against specified goals and an LLM Editor proposes improved variants, with the Judge acting as a fitness function and the Editor as a variation operator, akin to a generate-and-evaluate loop in evolutionary computation. We represent complex systems as a restricted, runnable subset of Python with domain-specific primitives, letting LLMs modify system dynamics directly. CEDAR formalizes this as an MCTS variant with an LLM-parameterized transition kernel and value function, enabling goal-directed discovery of complex system behaviors while preserving solution diversity, and its LLM-based interpretability reveals how structural changes drive emergent behavior. CEDAR reduces human effort while enabling capabilities difficult to achieve with existing approaches, facilitating broader adoption of complex systems across domains.

</details>

---

### [[20_Research/Papers/大模型/Multi-Agent_Forensic_Reasoning_for_Generalizable_Deepfake_Video_Detection|Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection]]

![[assets/2608.06865_figure.png|800]]

- **arXiv**: [2608.06865](https://arxiv.org/abs/2608.06865)
- **PDF**: https://arxiv.org/pdf/2608.06865
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_Forensic_Reasoning_for_Generalizable_Deepfake_Video_Detection|Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection]]
- **作者**: Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou, Xinyu Sun, Yuhui Chen, Zhe Wu, Congyan Lang, Junliang Xing
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AIGVDBench, GenVidBench, URL, ViF-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Gated-BEPO_Confidence-Gated_Bellman_Credit_Assignment_for_Large_Language_Model_Agents|Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents]]

![[assets/2608.06861_figure.png|800]]

- **arXiv**: [2608.06861](https://arxiv.org/abs/2608.06861)
- **PDF**: https://arxiv.org/pdf/2608.06861
- **详细分析**: [[20_Research/Papers/大模型/Gated-BEPO_Confidence-Gated_Bellman_Credit_Assignment_for_Large_Language_Model_Agents|Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents]]
- **作者**: Hongxi Yan, Ziyue Huang, Shichao Fan, Qingjie Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training large language model agents in long-horizon environments requires assigning credit from sparse terminal outcomes to individual actions. Existing critic-free methods propagate trajectory-level rewards uniformly across steps, while recent approaches construct step-level groups by matching repeated states and compare actions within each group. The former cannot distinguish useful actions in failed trajectories from ineffective actions in successful ones. The latter rely on step credit derived directly from individual trajectory outcomes and fixed-weight fusion with episode-level credit. We propose Gated-BEPO, which derives step-level credit from empirical rollout graphs. For each rollout group, Gated-BEPO constructs an empirical graph and estimates node values through a mean-backup Bellman fixed point that reflects the empirical action distribution of the current policy. We then accumulate these temporal-difference residuals along each sampled trajectory using generalized advantage estimation, yielding step-level Bellman advantages that capture both immediate and downstream effects. To adaptively fuse episode- and step-level credit, a confidence gate incorporates Bellman credit only at states with multiple observed successors and otherwise uses episode-level credit. Experiments on WebShop, ALFWorld, and visual Sokoban show consistent improvements across language and vision-language models, while diagnostic ablations support the effectiveness of Bellman fixed-point value estimation and show that step-level credit should be incorporated selectively rather than uniformly into the final advantage.

</details>

---

### [[20_Research/Papers/大模型/Coupling_Planning_with_Episodic_Memory_in_LLM_Agents_for_Software_Issue_Resolution|Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution]]

![[assets/2608.06811_figure.png|800]]

- **arXiv**: [2608.06811](https://arxiv.org/abs/2608.06811)
- **PDF**: https://arxiv.org/pdf/2608.06811
- **详细分析**: [[20_Research/Papers/大模型/Coupling_Planning_with_Episodic_Memory_in_LLM_Agents_for_Software_Issue_Resolution|Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution]]
- **作者**: Jiahao Zhang, Yifan Zhang, Yu Huang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TerminalWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Resolving a real software issue with a large language model (LLM) agent is a long repair episode, often tens to hundreds of steps spanning exploration, hypothesis, implementation, and verification. Success depends on both the base model's local reasoning and the agent's ability to maintain an evolving plan and remember observations across phases. Existing repository-level agents typically strengthen planning or memory in isolation, leaving long trajectories vulnerable to stale evidence, repeated failed edits, and verification inferred from the agent's own claims instead of execution evidence. We present PMCoder, an issue-resolution agent that couples a hierarchical phase planner with episodic memory. The coupling is bidirectional: the current plan phase conditions memory retrieval, while memory-derived trajectory statistics inform stuck detection and replanning. When available, issue-reproduction verdicts ground verification progress in execution evidence rather than self-reported completion. On SWE-bench Verified, PMCoder resolves an average of $25$ more cases ($+5.0$pp) than a harness-matched baseline, with gains persisting even where the reproduction gate never fires. Further Verified-500 evaluations show the same positive direction across Claude Haiku 4.5, DeepSeek-V4-Flash, and an OpenHands port, with at least $14$ additional resolved cases ($+2.8$pp). Separately, evaluation on TerminalWorld's official sample suggests that the plan-memory substrate transfers beyond issue reports. Ablation and trajectory analyses show where the gains come from: coupling planning and memory outperforms either component alone and reduces repeated failed actions, empty-patch exits, and context-window exhaustion.

</details>

---

### [[20_Research/Papers/大模型/Progressive_Alignment_of_Recommender_Foundation_Model_through_Multi-Phase_Post-Training|Progressive Alignment of Recommender Foundation Model through Multi-Phase Post-Training]]

![[assets/2608.06792_figure.png|800]]

- **arXiv**: [2608.06792](https://arxiv.org/abs/2608.06792)
- **PDF**: https://arxiv.org/pdf/2608.06792
- **详细分析**: [[20_Research/Papers/大模型/Progressive_Alignment_of_Recommender_Foundation_Model_through_Multi-Phase_Post-Training|Progressive Alignment of Recommender Foundation Model through Multi-Phase Post-Training]]
- **作者**: Oseong Choi, Hoeinn Kim, Jihoon Lee, Byungsoo Kang, Taeyeong Jang
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Progressive Alignment of Recommender Foundation Model through Multi-Phase Post-Training》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation model(FM) for recommendation has shown strong ability to model long-horizon sequential user behavior. In practice, a single pretrained foundation model is often adapted to diverse downstream serving surfaces through Supervised Fine-Tuning(SFT). However, optimizing task-specific objectives such as clicks or likes does not necessarily align the serving policy with the business metrics that determine recommendation quality. We propose a three-phase progressive post-training framework that explicitly separates downstream adaptation from business-metric alignment. The adaptation stage is decomposed into Linear Probing(LP) and Full Fine-Tuning(FFT): LP first stabilizes randomly initialized downstream heads within a frozen pretrained representation space, and FFT then jointly specializes the full model for the target task. On top of this stabilized policy, Reinforcement Fine-Tuning(RFT) aligns the model with practical business objectives using a learned reward model. Rather than directly optimizing the serving policy on sparse business targets, we train the policy on dense implicit feedback and use business-metric supervision only for reward modeling. Offline experiments show that the progressive LP-FFT-RFT framework outperforms single-phase alternatives, and that reward-based alignment yields a stronger serving policy than directly using the reward model itself for ranking. Large-scale online A/B tests further show that the proposed framework improves production recommendation quality over a conventional non-foundation baseline. A reference implementation is available at this https URL

</details>

---

### [[20_Research/Papers/大模型/Surg-UniWorld_A_Unified_Surgical_World_Model_with_Multimodal_Control_Experts|Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts]]

![[assets/2608.06770_figure.png|800]]

- **arXiv**: [2608.06770](https://arxiv.org/abs/2608.06770)
- **PDF**: https://arxiv.org/pdf/2608.06770
- **详细分析**: [[20_Research/Papers/大模型/Surg-UniWorld_A_Unified_Surgical_World_Model_with_Multimodal_Control_Experts|Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts]]
- **作者**: Rulin Zhou, Wanhao Liu, Guoheng Ma, Liangjin Shao, Qiujie Song, Yidu Wang, Guankun Wang, Tong Chen, Long Bai, Luping Zhou, Hongliang Ren
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，世界模型 1）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《Surg-UniWorld: A Unified Surgical World Model with Multimodal Control Experts》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ControlNet, Surg-UniWorld, Video2World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controllable surgical world models can provide a generative foundation for surgical artificial intelligence and simulation by synthesizing realistic instrument--tissue interactions. However, existing methods lack a unified multimodal control paradigm, while direct fusion of heterogeneous visual conditions often causes anatomical distortion, instrument appearance drift, and temporally inconsistent interactions. In this work, we propose {Surg-UniWorld}, a unified surgical world model with multimodal control experts. Surg-UniWorld first constructs a {Hierarchical Surgical Anchor} from first-frame appearance and hierarchical semantic masks to preserve persistent scene identity, anatomical organization, and interaction boundaries. {Anchor-Relative Modality Experts} then interpret edge, depth, and optical-flow evidence relative to the shared anchor, capturing complementary boundary, geometric, and motion information. A {Multimodal Control Expert} further performs contribution-preserving stage-wise composition of the activated modality increments and generates control hints for the Wan2.2 video diffusion backbone. To support multimodal surgical world modeling, we further construct Cholec80-SurgWAM, a benchmark for controllable surgical video generation. Extensive experiments demonstrate that Surg-UniWorld consistently outperforms existing controllable video generation methods and surgical world-model baselines in generation quality, temporal consistency, and multimodal controllability.

</details>

---

### [[20_Research/Papers/具身智能/Capek_0.5_An_Execution-Centric_Vision-Language_Model_for_Embodied_Intelligence|Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence]]

![[assets/2608.06756_figure.png|800]]

- **arXiv**: [2608.06756](https://arxiv.org/abs/2608.06756)
- **PDF**: https://arxiv.org/pdf/2608.06756
- **详细分析**: [[20_Research/Papers/具身智能/Capek_0.5_An_Execution-Centric_Vision-Language_Model_for_Embodied_Intelligence|Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence]]
- **作者**: Ying Chen, Weizhen Li, Zhe Hu, Zhenjiang Li, Rui Jiang, Zhifeng Gu, Lihuang Fang, Jiangping Liu, Lei Yi, Jie Chen
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.2，大模型 0.9，强化学习 0.2，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Capek-StateBench, EmbodiedBench, VABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models are increasingly serving as the reasoning core of embodied agents. Robot execution is inherently iterative: each action reshapes the scene and physical state, continually renewing what must be perceived, reasoned about, and verified. Meeting these demands requires complementary capabilities that differ in supervision signals, prediction formats, and verification criteria. Existing approaches typically develop these capabilities against isolated, task-specific objectives, leaving open how they should be organized and integrated around execution as a whole. We present Capek 0.5, an embodied vision-language model built around an execution-centric capability taxonomy. Rather than organizing training by datasets or tasks, the taxonomy groups embodied capabilities according to their functional roles throughout execution and comprises four capability families: Spatial Reasoning, Temporal Understanding, Action Guidance, and State Verification. Each capability is first acquired by a dedicated specialist through reinforcement learning with verifiable rewards from a shared backbone, and the specialists are then consolidated into a single inference-time model through weight-space merging followed by routed policy-space distillation. We instantiate Capek 0.5 at the 2B and 35B-A3B scales and evaluate it from three complementary perspectives: comprehensive benchmark suites including Capek-StateBench, a new benchmark for state verification; a controlled study of capability retention from specialists to the unified model; and closed-loop evaluation in simulated embodied environments. Capek 0.5 improves the large majority of matched benchmark rows over its initialization, retains all four specialized capabilities in one checkpoint with quantified losses, and transfers to closed-loop embodied task execution.

</details>

---

### [[20_Research/Papers/具身智能/MemPrism_Task-Conditioned_Relational_Memory_Views_for_Long-Horizon_Agents|MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents]]

![[assets/2608.06745_figure.jpg|800]]

- **arXiv**: [2608.06745](https://arxiv.org/abs/2608.06745)
- **PDF**: https://arxiv.org/pdf/2608.06745
- **详细分析**: [[20_Research/Papers/具身智能/MemPrism_Task-Conditioned_Relational_Memory_Views_for_Long-Horizon_Agents|MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents]]
- **作者**: Zhisheng Chen, Bingfan Zeng, Bangde Cao, Zhengwei Xie, Yuxuan Li, Jinhan Li, Zheng Lu, Xiangchen Guan, Zikai Xiao, Rui Qian, Jingwei Song
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，大模型 0.5）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, CFG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation. This leads to representation mismatch, where relevant information is available but not organized for the current decision. To this end, we propose MemPrism, a task-conditioned relational memory framework that separates persistent experience storage from decision-time working memory. MemPrism records interactions as the event stream and dynamically constructs relational views according to the current task context. A lightweight view policy selects the relation structure, evidence range, outcome condition, and granularity, while a deterministic composer and render transform historical facts into a temporary optical working-memory view for a frozen task policy. Experiments on long-horizon embodied and web-agent benchmarks show that MemPrism consistently improves the task performance, especially as trajectories become longer, while reducing memory token consumption. Furthermore, the learned view policy transfers across different VLMs without additional adaptation, demonstrating the effectiveness of task-conditioned relational views as a general memory interface for agents.

</details>

---

### [[20_Research/Papers/强化学习/IB-RL_Isolated_Bilateral_Reinforcement_Learning_for_Strategic_Dialogue_Agents|IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents]]

![[assets/2608.06735_figure.png|800]]

- **arXiv**: [2608.06735](https://arxiv.org/abs/2608.06735)
- **PDF**: https://arxiv.org/pdf/2608.06735
- **详细分析**: [[20_Research/Papers/强化学习/IB-RL_Isolated_Bilateral_Reinforcement_Learning_for_Strategic_Dialogue_Agents|IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents]]
- **作者**: Senhao Wang, Chenghao Cai, Haitao Hu, Mingxing Huang, Xingguang Wang, Wenhao Li, Zecheng Lin
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.55，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《IB-RL: Isolated Bilateral Reinforcement Learning for Strategic Dialogue Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IB-RL, LLM-MARL, MARL, Test-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has achieved strong results in improving large language models (LLMs) on tasks with stationary, verifiable rewards, such as mathematical reasoning and code execution. In these settings, the environment follows fixed rules and does not adapt strategically to the agent. Strategic dialogue differs in this respect: the environment is another agent that adapts to the policy, and success depends on the interaction between the two sides. Despite this interactive nature, current RL approaches typically train a target agent against a fixed counterpart or simulator. We find that this training paradigm encourages the policy to exploit counterpart-specific regularities rather than learn strategies that generalize across counterparts. We call this problem the static-counterpart mismatch, which we quantify directly in our experiments. To address it, we propose Isolated Bilateral Reinforcement Learning (IB-RL), in which the two roles coevolve through joint rollouts while each role optimizes its own reward through fully independent advantages, action masks, and update paths. We evaluate frozen policies against fully independent held-out counterparts in both domains. On Vehicle TeleSales, IB-RL achieves 89.6% Success@1, compared to 84.6% for the best unilateral RL baseline. On Deal-or-NoDeal, it reaches 98.4% agreement against DeepSeek V4 Pro, compared to 86.4% for the best unilateral baseline. These results indicate that jointly training both roles with strict peragent isolation produces policies that generalize more effectively to unseen counterparts.

</details>

---

### [[20_Research/Papers/大模型/Multi-Level_Modeling_of_Large_Language_Model_Inference_Latency_and_Energy_via_Hybrid_Analytical--Machine-Learning_Predictors|Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors]]

![[assets/2608.06723_figure.png|800]]

- **arXiv**: [2608.06723](https://arxiv.org/abs/2608.06723)
- **PDF**: https://arxiv.org/pdf/2608.06723
- **详细分析**: [[20_Research/Papers/大模型/Multi-Level_Modeling_of_Large_Language_Model_Inference_Latency_and_Energy_via_Hybrid_Analytical--Machine-Learning_Predictors|Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors]]
- **作者**: Saeid Shokoufa, Mohammad Erfan Sadeghi, Mehdi Kamal, Massoud Pedram
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design. In this work, we introduce Hybrid Modeling for Energy and Latency of LLMs (HYMELL), a hybrid three-level framework for estimating LLM inference latency and energy by combining analytical modeling with machine learning (ML). HYMELL models LLM execution through a three-level hierarchy: analytical estimation of primitive operations, ML prediction of higher-level components, and an end-to-end model that captures system-level overheads across both prefill and decode phases. The framework supports diverse architectures, including dense and mixture-of-experts (MoE) feed-forward networks (FFNs), as well as multi-head attention (MHA) and grouped-query attention (GQA) mechanisms. Evaluated on an NVIDIA H100 graphics processing unit (GPU), HYMELL achieves high predictive accuracy; notably, for LLaMA 3 8B, it attains less than 5% error for both prefill and decode phases. By predicting execution costs directly from architectural parameters, it enables fast, hardware-free design space exploration and energy-efficient optimization.

</details>

---

### [[20_Research/Papers/强化学习/Dueling_World_Models_Advantage-Style_Action_Channels_for_Common-Mode_Distractor_Rejection|Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection]]

![[assets/2608.06706_figure.png|800]]

- **arXiv**: [2608.06706](https://arxiv.org/abs/2608.06706)
- **PDF**: https://arxiv.org/pdf/2608.06706
- **详细分析**: [[20_Research/Papers/强化学习/Dueling_World_Models_Advantage-Style_Action_Channels_for_Common-Mode_Distractor_Rejection|Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection]]
- **作者**: Jiazhuo Li, Yiming Fei, Zhiruo Zhou, Heikichi Hayashi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 0.16，世界模型 1.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Dueling World Models: Advantage-Style Action Channels for Common-Mode Distractor Rejection》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models plan by predicting future states from an action, but when a scene contains motion the agent does not control, they quietly go action-blind: predictions for different actions become indistinguishable even as the training loss keeps improving. Existing remedies suppress this distraction with reconstruction, task reward, or auxiliary objectives, each adding machinery or assumptions. We show that a minimal alternative suffices, borrowed from the dueling decomposition of value into a state baseline and an action advantage: in latent dynamics, subtracting a prediction's mean effect over actions cancels whatever the actions share--the action-independent variation where distractors live--leaving a clean, controllable channel, with no reward, no reconstruction, and no distractor-specific auxiliary loss. Because this is only a subtraction at readout time, it applies unchanged to any action-conditioned world model, including frozen pretrained ones. Across a gridworld, synthetic generators with known factors, distracting continuous control, and natural-pixel Atari, the isolated channel recovers the agent's own effect where entangled predictors fail, with nuisance leak indistinguishable from zero; applied post hoc it surfaces an action channel in off-the-shelf models that their raw readouts miss, and it converts into goal-reaching control in the gridworld. We prove the cancellation is exact in finite samples for both discrete and sampled action sets, and we state its measured boundary--distractors whose motion tracks the action--together with the remaining limitations in the appendix.

</details>

---

### [[20_Research/Papers/大模型/Online_Monitoring_and_Corrective_Steering_of_Programming_Agents|Online Monitoring and Corrective Steering of Programming Agents]]

![[assets/2608.06701_figure.png|800]]

- **arXiv**: [2608.06701](https://arxiv.org/abs/2608.06701)
- **PDF**: https://arxiv.org/pdf/2608.06701
- **详细分析**: [[20_Research/Papers/大模型/Online_Monitoring_and_Corrective_Steering_of_Programming_Agents|Online Monitoring and Corrective Steering of Programming Agents]]
- **作者**: Shuyang Liu, Saman Dehghan, Ji Young Kim, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Online Monitoring and Corrective Steering of Programming Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fixing GitHub issues in large-scale projects is a long-horizon task, especially when a fix requires changes across multiple locations or the issue description lacks the information needed to localize and repair it. As a result, agents traverse long trajectories that are prone to inefficiency and error: they drift away from their intended plan, repeat failed actions, or terminate without a working patch. This paper proposes LivePlan to monitor, detect, and correct such behavioral inefficiencies and drifts in real time. LivePlan decouples judging from advising: a deterministic, rule-based monitor examines general signals over the trajectory to detect issues without invoking an LLM, and only when an issue is detected does it consult an advisor LLM for a high-level, next-step correction. This design avoids the misleading re-planning and costly interventions of prior approaches. We implement LivePlan on top of SWE-agent and evaluate it using five LLMs (three as executor agents and two as advisors) across SWE-bench Verified and SWE-bench Pro. Compared to vanilla SWE-agent, LivePlan notably improves issue resolution rates, achieving consistent gains of up to 15.2% (average: 9.9%), while incurring only an additional cost of $0.08 per instance. The additional solutions concentrate on medium and hard instances. LivePlan consistently outperforms alternative approaches in resolution rate, with minimal regression on already successful runs and new successes on problems that no baseline solves.

</details>

---

### [[20_Research/Papers/大模型/AgentPatch_Coarse-to-Fine_Weak-Task_Repair_for_Merging_Agentic_Multimodal_Large_Language_Models|AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models]]

![[assets/2608.06699_figure.png|800]]

- **arXiv**: [2608.06699](https://arxiv.org/abs/2608.06699)
- **PDF**: https://arxiv.org/pdf/2608.06699
- **详细分析**: [[20_Research/Papers/大模型/AgentPatch_Coarse-to-Fine_Weak-Task_Repair_for_Merging_Agentic_Multimodal_Large_Language_Models|AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models]]
- **作者**: Zibo Shao, Baochen Xiong, Chengdong Xu, Linhui Xiao, Kaichen Li, Haoran Gong, Yan Li, Yaguang Song, Xiaoshan Yang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic Multimodal Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic multimodal large language models (MLLMs) extend multimodal perception and reasoning with planning, tool use, and interaction in dynamic environments. Yet current models are specialized for particular tools or environments, complicating consolidation into a single generalist. We formulate Agentic MLLM Merging and identify two challenges: asymmetric capability preservation, whereby capabilities with different interaction complexity are retained unevenly, producing weak tasks after merging, and behavior-critical forgetting, whereby losing decisive actions can derail long-horizon execution. We propose AgentPatch, a training-free coarse-to-fine repair framework. It selects a stable merged backbone, restores diluted weak-task-specific signals through Weak-Task Unique Residual Recovery, and applies an Agent-Guided Behavior-Critical Patch that recovers decisive behaviors under explicit capability protection. AgentPatch produces a single static checkpoint without routing or ensembles. Experiments across six agentic and multimodal benchmarks show that AgentPatch improves diverse merged backbones, alleviates weak-task degradation, and better balances weak-task recovery with the preservation of complementary search and agentic visual processing capabilities. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/A_Multi-Agent_Framework_for_Automated_Coarse-Grained_Molecular_Dynamics_of_Polymers|A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers]]

![[assets/2608.06694_figure.png|800]]

- **arXiv**: [2608.06694](https://arxiv.org/abs/2608.06694)
- **PDF**: https://arxiv.org/pdf/2608.06694
- **详细分析**: [[20_Research/Papers/大模型/A_Multi-Agent_Framework_for_Automated_Coarse-Grained_Molecular_Dynamics_of_Polymers|A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers]]
- **作者**: Joohee Choi, Junhyeong Lee, Seunghwa Ryu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coarse-grained (CG) molecular dynamics extends polymer simulation beyond the scales accessible to all-atom (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design choice, so a transferable parameter set is generally not available and the potentials are derived anew for each polymer mapping. Here we present CGMas, a multi-agent framework that automates topology construction, equilibration, mapping, potential derivation, and validation from a natural-language specification of the polymer and target resolution. A large-language-model (LLM) reasoning agent infers the AA topology from polymer name, while layered self-correction resolves physical errors common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents equilibrate the system, map it onto CG representation, derive potentials through Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas completed all 27 homopolymer and copolymer tasks, matched the AA density to within 5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs as a route to automated polymer coarse-graining.

</details>

---

### [[20_Research/Papers/强化学习/Vehicle_routing_problem_using_deep_reinforcement_learning_-_A_case_study_about_truck_planning_in_the_industry|Vehicle routing problem using deep reinforcement learning - A case study about truck planning in the industry]]

![[assets/2608.06668_figure.jpg|800]]

- **arXiv**: [2608.06668](https://arxiv.org/abs/2608.06668)
- **PDF**: https://arxiv.org/pdf/2608.06668
- **详细分析**: [[20_Research/Papers/强化学习/Vehicle_routing_problem_using_deep_reinforcement_learning_-_A_case_study_about_truck_planning_in_the_industry|Vehicle routing problem using deep reinforcement learning - A case study about truck planning in the industry]]
- **作者**: Siliang Lu, Dan Hu, Lili Wu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.1，强化学习 1.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Vehicle routing problem using deep reinforcement learning - A case study about truck planning in the industry》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As an important component of the supply chain industry, transportation has experienced rapid development in the past decade with the assistance of digital platforms and intelligent algorithms. Within the field of transportation research, Vehicle Routing Problem (VRP) has remained a persistent and enduring challenge. In the realm of management science, experts, and scholars from both the industrial and academic sectors have continuously explored optimization models and algorithms to effectively address routing problems, from the classical Traveling Salesman Problem to the more general Vehicle Routing Problem. These models and algorithms are applied in real-world industrial scenarios to achieve cost optimization and reduce carbon footprints. However, due to the complexity of real-world problems, numerous specific constraints are often added, and challenges such as information opacity, uncertainty, and irrational human behavior may arise. Therefore, deploying and optimizing mathematical models for VRP in practical scenarios while maintaining optimal results poses numerous challenges. This paper discusses and provides solutions for three different logistic use cases involving external truck network design. Through these industrial case study, the paper introduces how deep reinforcement learning-based vehicle routing optimization has been implemented. As a result, it can be observed that the routes optimized by reinforcement learning agent have over 10% total cost compared to baseline results. Furthermore, the paper proposes that in future research, DRL algorithms for vehicle routing problems could be generalized into more variations of VRP.

</details>

---

### [[20_Research/Papers/强化学习/SoRoMoX_Fast,_Differentiable,_and_Parallelizable_Soft_Robot_Models|SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models]]

![[assets/2608.06650_first_page.png|800]]

- **arXiv**: [2608.06650](https://arxiv.org/abs/2608.06650)
- **PDF**: https://arxiv.org/pdf/2608.06650
- **详细分析**: [[20_Research/Papers/强化学习/SoRoMoX_Fast,_Differentiable,_and_Parallelizable_Soft_Robot_Models|SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models]]
- **作者**: Maximilian Stölzle, Solange Gribonval, Daniel Feliu-Talegon, Vito Daniele Perfetta, Michele Martini, Chuhan Zhang, Kiwan Wong, Mohammed Tarnini, Anup Teejo Mathew, Federico Renda, Daniela Rus, Cosimo Della Santina
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《SoRoMoX: Fast, Differentiable, and Parallelizable Soft Robot Models》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reduced-order models based on Cosserat-rod theory are now well established, and modeling theory is no longer the primary bottleneck in soft-robot control. Their implementations, however, do not support the differentiable, GPU-parallel, and control-oriented workflows that underpin advanced rigid-robotics applications. Here, we fill this gap with SoRoMoX (Soft Robot Models in JAX), a fully numerical, JIT-compilable Python/JAX framework. SoRoMoX implements articulated, Piecewise Constant Strain, and Variable Strain models through a unified, control-ready interface that provides inertia matrices, gravitational and elastic forces, Jacobians, and their derivatives. To our knowledge, it is the first rod/strain-based soft-robot modeling framework that runs directly on GPUs and is end-to-end differentiable with respect to states, inputs, and parameters. Sequential CPU rollouts are up to 18.1x faster than state-of-the-art alternatives, while GPU-parallel rollouts increase throughput by up to 234.6x. This performance enables workflows that were previously impractical or impossible: static-equilibrium system identification with 66% lower marker RMSE; residual-force learning with a further 64% reduction; computed-torque tracking with RMSE reduced by a factor of approximately 500 relative to model-free PD; control-gain optimization with up to 62% lower loss than untuned gains; safety-constrained control using high-order control barrier functions to keep the peak contact force within a prescribed 5 N bound, compared with 33.5 N without the safety constraint; and reinforcement-learning policy training up to 7x faster than a CPU PyElastica discrete-rod baseline through massively parallel rollouts.

</details>

---

### [[20_Research/Papers/强化学习/Flowing_Through_States_Neural_ODE_Regularization_for_Reinforcement_Learning|Flowing Through States: Neural ODE Regularization for Reinforcement Learning]]

![[assets/2608.06595_figure.png|800]]

- **arXiv**: [2608.06595](https://arxiv.org/abs/2608.06595)
- **PDF**: https://arxiv.org/pdf/2608.06595
- **详细分析**: [[20_Research/Papers/强化学习/Flowing_Through_States_Neural_ODE_Regularization_for_Reinforcement_Learning|Flowing Through States: Neural ODE Regularization for Reinforcement Learning]]
- **作者**: Mohamed Ghanem, Bernd Finkbeiner
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.82（加权：大模型 0.1，强化学习 1.36，世界模型 0.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Flowing Through States: Neural ODE Regularization for Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neural networks applied to sequential decision-making tasks typically rely on latent representations of environment states. While environment dynamics dictate how semantic states evolve, the corresponding latent transitions are usually left implicit, creating a potential misalignment between the two. We propose to model latent dynamics explicitly by drawing an analogy between Markov decision process (MDP) trajectories and ordinary differential equation (ODE) flows: in both cases, the current state fully determines its successors. Building on this view, we introduce a neural ODE-based regularization method that enforces latent embeddings to follow consistent ODE flows, thereby aligning representation learning with environment dynamics. Although broadly applicable to deep learning agents, we demonstrate its effectiveness in reinforcement learning by integrating it into Actor-Critic algorithms. Our approach yields major performance gains across various standard Atari benchmarks for A2C and gridworld environments for PPO.

</details>

---

### [[20_Research/Papers/大模型/Beyond_AI_Language_The_case_for_the_idiolectal_nature_of_LLM_output|Beyond "AI Language": The case for the idiolectal nature of LLM output]]

![[assets/2608.06589_first_page.png|800]]

- **arXiv**: [2608.06589](https://arxiv.org/abs/2608.06589)
- **PDF**: https://arxiv.org/pdf/2608.06589
- **详细分析**: [[20_Research/Papers/大模型/Beyond_AI_Language_The_case_for_the_idiolectal_nature_of_LLM_output|Beyond "AI Language": The case for the idiolectal nature of LLM output]]
- **作者**: Karolina Rudnicka, Thomas Stephan Juzek
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Beyond "AI Language": The case for the idiolectal nature of LLM output》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While large language model outputs are frequently analysed as a collective super variety termed "AI language," this chapter argues that this perspective coexists with distinct, model-specific linguistic signatures akin to human idiolects. We analyse two datasets of LLM-generated texts on societal topics: a 2024 corpus of six models (Improta et al. 2024) and a newly generated 2026 corpus using the same prompts featuring six contemporary models. Our findings, utilising computational descriptors and stylometric principal component analysis reveal a generational shift between the style of the 2024 and 2026 cohorts, while demonstrating that each individual model maintains a unique linguistic profile. This multi-layered interplay is illustrated by contraction frequencies, which vary from over 1,200 to over 30,000 per million words within the same cohort of models (2026). Ultimately, we conclude that treating LLM output as idiolectal in nature provides a valuable framework with potential implications for research on variation and change, LLM-generated text detection, forensic linguistics and usage-based approaches to language.

</details>

---

### [[20_Research/Papers/机器人/SyncSBC_Decentralized_Swarm_Behavior_Prediction_for_Synchronized_Autonomous_Control|SyncSBC: Decentralized Swarm Behavior Prediction for Synchronized Autonomous Control]]

![[assets/2608.06587_figure.png|800]]

- **arXiv**: [2608.06587](https://arxiv.org/abs/2608.06587)
- **PDF**: https://arxiv.org/pdf/2608.06587
- **详细分析**: [[20_Research/Papers/机器人/SyncSBC_Decentralized_Swarm_Behavior_Prediction_for_Synchronized_Autonomous_Control|SyncSBC: Decentralized Swarm Behavior Prediction for Synchronized Autonomous Control]]
- **作者**: Varun Raveendra, Connor Mattson, Daniel S. Brown
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《SyncSBC: Decentralized Swarm Behavior Prediction for Synchronized Autonomous Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot swarms utilize many independent limited-sensing agents to produce complex emergent behaviors without requiring centralized control. However, little research explores how agents can infer swarm-level behavior from purely local perception, a capability critical for detecting faults and behavior changes. In this paper, we introduce Synchronized Swarm Behavior Classification (SyncSBC), which combines improvements in machine learning and distributed consensus to classify collective swarm behavior and synchronize swarm decision-making in an entirely decentralized manner. We show that SyncSBC achieves high classification accuracy and low synchronization delay, making it suitable for real-world deployment. Finally, we use SyncSBC to demonstrate two promising swarm applications on real robots where we show that swarms utilizing SyncSBC can accurately identify anomalies in robot behavior and autonomously coordinate collective changes in swarm behavior. Videos, code and supplemental experiments are available at this https URL .

</details>

---

### [[20_Research/Papers/世界模型/TaskSense_Focusing_on_What_Matters_in_World_Models|TaskSense: Focusing on What Matters in World Models]]

![[assets/2608.06544_figure.png|800]]

- **arXiv**: [2608.06544](https://arxiv.org/abs/2608.06544)
- **PDF**: https://arxiv.org/pdf/2608.06544
- **详细分析**: [[20_Research/Papers/世界模型/TaskSense_Focusing_on_What_Matters_in_World_Models|TaskSense: Focusing on What Matters in World Models]]
- **作者**: SM Mazharul Islam, Manfred Huber
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: WorldModel

#### 研究背景与动机

《TaskSense: Focusing on What Matters in World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for visual control typically learn compact latent states by reconstructing observations, implicitly encouraging representations to preserve information across the entire visual input. However, task-relevant content often occupies only a small fraction of the observation, while background clutter and distractors consume valuable representational capacity. This mismatch between visual reconstruction and control objectives biases latent representations to model task-irrelevant visual content, diluting learning signals for control-relevant features and severely degrading downstream performance under visual distractions. We introduce TaskSense, a task-centric world modeling framework that enforces task relevance before latent encoding through a differentiable stochastic spatial attention mechanism conditioned on the previous latent state. To steer attention toward control-relevant regions, we augment training with an auxiliary inverse-dynamics objective. Rather than reconstructing the full observation, the world model reconstructs only the attended regions, encouraging latent representations to preserve task-relevant information while discarding irrelevant visual content. The decoder is further conditioned on the sampled attention map, enabling consistent reconstruction despite stochastic attention. Compared with the DreamerV3 baseline, TaskSense maintains competitive performance on the DeepMind Control Suite while consistently outperforming DreamerV3 on the Distracting Control Suite, demonstrating substantially improved robustness to visual distractions. Qualitative analysis further confirms that the learned attention, guided by inverse-dynamics supervision, consistently localizes control-relevant regions while suppressing irrelevant visual content.

</details>

---

### [[20_Research/Papers/大模型/Do_AI_Personas_Grow_Analyzing_and_Benchmarking_Personality_Evolution_in_LLM_Agents_After_Life_Events|Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events]]

![[assets/2608.06485_first_page.png|800]]

- **arXiv**: [2608.06485](https://arxiv.org/abs/2608.06485)
- **PDF**: https://arxiv.org/pdf/2608.06485
- **详细分析**: [[20_Research/Papers/大模型/Do_AI_Personas_Grow_Analyzing_and_Benchmarking_Personality_Evolution_in_LLM_Agents_After_Life_Events|Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events]]
- **作者**: Ming Wang, Peidong Wang, Xiaocui Yang, Daling Wang, Shi Feng, Fiona Fui-Hoon Nah, Ee-Peng Lim
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personality-conditioned LLM agents (PC-Agents) are increasingly used in emotional support, social simulation, and role-playing, motivating the development of lifelong agents that remain coherent over extended interactions. A key component of such coherence is personality evolution: agents should undergo plausible, psychology-grounded changes as they experience life events in different contexts. Although prior work shows that LLM personalities can shift under contextual perturbations, how these shifts vary across traits, events, personas, and models remains poorly understood. We study event-induced personality change after 11 major life events, using the Big Five traits as a psychometric anchor and interpreting the resulting trajectories against longitudinal evidence from human personality psychology. Across four diagnostic axes, PC-Agents exhibit measurable trait shifts at similar rates for event-trait pairs with and without documented human change directions. Even when shifts follow the expected direction, their magnitudes usually fall below human effect-size ranges. Gender and cultural-region prompts show little moderating effect, while persona-level dispersion is compressed three- to four-fold relative to human samples. To enable systematic comparison, we introduce BFI-Adapt, a reusable benchmark for scoring the directional fidelity of event-induced personality change, and use it to rank 14 models. A validation suite shows that the measured shifts exceed no-event retest noise, remain stable under independently paraphrased prompts, exhibit limited and model-dependent convergence with scenario-based behavioral choices, and persist across intervening unrelated dialogue. Together, these checks establish the measured trajectories as robust event-conditioned response patterns. Our results suggest that current PC-Agents simulate the mean of human personality dynamics, but not its shape.

</details>

---

### [[20_Research/Papers/强化学习/LyEvO_Lyapunov-Guided_Evolutionary_Optimization_for_Safe_and_Robust_Sim-to-Real_Policy_Learning|LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning]]

![[assets/2608.06481_figure.png|800]]

- **arXiv**: [2608.06481](https://arxiv.org/abs/2608.06481)
- **PDF**: https://arxiv.org/pdf/2608.06481
- **详细分析**: [[20_Research/Papers/强化学习/LyEvO_Lyapunov-Guided_Evolutionary_Optimization_for_Safe_and_Robust_Sim-to-Real_Policy_Learning|LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning]]
- **作者**: Riccardo Curcio, Hongpeng Cao, Marco Caccamo
- **cs 子类**: cs.AI, cs.LG, cs.NE, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training controllers that are safe and robust in simulation, and systematically assessing their readiness for real-world deployment, remain key challenges in sim-to-real transfer. To address this, we propose LyEvO, a physics-grounded framework that combines constrained Evolutionary Optimization and Statistical Model Checking (SMC)-based verification with Lyapunov-based stability analysis. Leveraging prior knowledge of the system dynamics, LyEvO uses Lyapunov analysis to compute an initial candidate stability region. An iterative loop then uses operational scenarios drawn from this region to jointly optimize and statistically verify a policy, and subsequently expands the region's boundaries based on the verification outcome. This integrated procedure provides a practical criterion for assessing deployment readiness. We evaluate LyEvO on Cartpole and 3D Quadrotor benchmarks through extensive simulations and targeted real-world experiments, demonstrating safe and robust sim-to-real transfer.

</details>

---

### [[20_Research/Papers/具身智能/StepJack_Benchmarking_Computer-Use_Agent_Safety_Against_Multi-Step_Indirect_Prompt_Injection|StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection]]

![[assets/2608.06477_figure.png|800]]

- **arXiv**: [2608.06477](https://arxiv.org/abs/2608.06477)
- **PDF**: https://arxiv.org/pdf/2608.06477
- **详细分析**: [[20_Research/Papers/具身智能/StepJack_Benchmarking_Computer-Use_Agent_Safety_Against_Multi-Step_Indirect_Prompt_Injection|StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection]]
- **作者**: Zhuoxin Zhan, Akbar Rafiey, Avery Ma, Leila Pishdad, Layla El Asri
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, EmbodiedAI, Security

#### 研究背景与动机

《StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents (CUAs) face a growing threat from indirect prompt injection, where adversarial instructions are planted in the environment such as web pages. In this paper, we introduce multi-step indirect prompt injection, a new attack class against CUAs in which the adversarial goal is decomposed into multiple innocuous-looking sub-steps and distributed across a chain of pages referenced along the agent's navigation path. We develop a pipeline to automatically decompose an adversarial goal under the constraint that the execution of the decomposed sub-steps must achieve the original goal while optimizing the innocuousness of each decomposed sub-step. With this pipeline, we build StepJack, a CUA safety benchmark with 480 test examples. On this benchmark, we evaluate six state-of-the-art CUAs and find that at a fixed decomposition depth, multi-step attacks raise attack success rate (ASR) on three of six CUAs, by up to 31.2 points (e.g., GPT-5.4-mini: 41.7% at single-step to 72.9% at three-step); averaged over the five CUAs that can reliably follow the reference chain (all but EvoCUA-32B), ASR rises from 31.3% at single-step to 36.9% at three-step. Dataset and code are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/CyberForge_Verified_Vulnerability_Injection_at_Repository_Level_for_Cybersecurity_Agent_Training|CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training]]

![[assets/2608.06471_figure.png|800]]

- **arXiv**: [2608.06471](https://arxiv.org/abs/2608.06471)
- **PDF**: https://arxiv.org/pdf/2608.06471
- **详细分析**: [[20_Research/Papers/大模型/CyberForge_Verified_Vulnerability_Injection_at_Repository_Level_for_Cybersecurity_Agent_Training|CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training]]
- **作者**: Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini, Ram D. Sriram, Dinesh Manocha
- **cs 子类**: cs.AI, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《CyberForge: Verified Vulnerability Injection at Repository Level for Cybersecurity Agent Training》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BountyBench, CyberGym, PatchEval, R2E-Gym, SWE-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite recent advances, frontier large language model (LLM) agents remain limited in discovering and patching complex vulnerabilities in real-world software. Generally available agents can already aid attackers, who only need to find one exploitable weakness, while defenders must continuously identify and patch all vulnerabilities across fast-growing codebases. Stronger defensive agents would help close this gap, yet the scarcity of security training data with reproducible build and execution environments remains a bottleneck. We present CyberForge, a framework that synthesizes executable, repository-level security training data by injecting vulnerabilities into real C/C++ projects. It validates each instance dynamically: the injected build must pass the project's unit tests, and generated proof-of-vulnerability (PoV) must trigger on the injected build and not on the clean one. CyberForge is not limited by the availability of disclosed vulnerabilities, therefore it can scale in comparison to data augmentation techniques which rely on historic CVE data. The resulting corpus holds 1034 validated vulnerabilities across 80 projects and 63 weakness categories, with edit locality similar to real CVE patches under a real-versus-real noise floor. Fine-tuning on trajectories collected over this corpus improves SEC-bench patch repair by +3.3 to +14.7 points, in all six configurations of three model scales and two teachers, with the 31B student reaching its GPT-5.4-mini teacher, 72.7% against 74.0%. These gains generalize out of distribution to PatchEval, a corpus containing other programming languages, where every configuration also improves and the 31B student passes its teacher.

</details>

---

### [[20_Research/Papers/强化学习/Evaluating_XAI_Support_From_A_Hierarchical_Reinforcement_Learning_Policy_in_Human-Agent_Collaboration|Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration]]

![[assets/2608.06381_figure.jpg|800]]

- **arXiv**: [2608.06381](https://arxiv.org/abs/2608.06381)
- **PDF**: https://arxiv.org/pdf/2608.06381
- **详细分析**: [[20_Research/Papers/强化学习/Evaluating_XAI_Support_From_A_Hierarchical_Reinforcement_Learning_Policy_in_Human-Agent_Collaboration|Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration]]
- **作者**: Mateus Levi Simões Fernandes, Alberto Sardinha
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Evaluating XAI Support From A Hierarchical Reinforcement Learning Policy in Human-Agent Collaboration》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Explainable AI (XAI) has shown promise for human-agent collaboration, yet results rely on hand-crafted policies in custom environments, limiting generalizability to state-of-the-art teaming research. We provide the first systematic evaluation of XAI support generated from an intrinsically explainable learned policy in an established benchmark. Using the Hierarchical Ad Hoc Agents (HA$^2$) architecture in Overcooked-AI, we generate real-time explanations from hierarchical subtask selections, delivered through text or audio via a novel trigger-based system. Our between-subjects experiment (n=38) found no significant performance effects, though participants with explanations showed trends toward faster performance improvement. More notably, audio explanations produced a significant reduction in participants' working-alliance bond with the agent -- an effect absent under the text modality -- suggesting that spoken explanations activate partnership expectations the underlying reactive policy cannot meet. We provide the first modality comparison in real-time human-agent collaboration and establish a baseline methodology for evaluating intrinsically explainable reinforcement learning architectures in benchmark environments. Results point to matching explanation modality to the underlying policy's capacity of sustaining the partnership its delivery implies as a potential path for more effective collaborative XAI.

</details>

---
