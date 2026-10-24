# cs.CL | Computation and Language | 2026-10-23

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/大模型/AfterDeleteBench_Auditing_Post-Deletion_Information_Persistence_in_LLM_Agents|AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents]]

![[assets/2610.31366_figure.png|800]]

- **arXiv**: [2610.31366](https://arxiv.org/abs/2610.31366)
- **PDF**: https://arxiv.org/pdf/2610.31366
- **详细分析**: [[20_Research/Papers/大模型/AfterDeleteBench_Auditing_Post-Deletion_Information_Persistence_in_LLM_Agents|AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents]]
- **作者**: Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, Raef Bassily, Andrew Perrault
- **cs 子类**: cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AfterDeleteBench, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion recovery to be attributed to the original exposure. In our primary setting, a single query recovers the deleted secret from Qwen2.5-7B-Instruct in roughly two thirds of cases, while matched never-exposed controls have zero recovery. Crucially, recovery does not require a surviving verbatim copy: when the complete secret string is absent and only separately stored components remain under a public composition rule, exact reconstruction succeeds in 62-99% of cases across Qwen, Mistral, and Phi-3. We also show that the response interface is part of the measurement system: target-bearing replies can be scored as failures when the requested format and parser are misaligned. Finally, we separate reconstruction from write-back and fresh-session recall. Provenance-aware closure eliminates observed recovery in the tested positive-baseline settings, whereas an exact-literal write filter blocks reinsertion but cannot erase information already present. Together, these results show that source deletion should be evaluated behaviorally at the level of the agent and its memory system, not only as a storage operation.

</details>

---

### [[20_Research/Papers/大模型/ReflectPO_Reflection-Guided_Policy_Optimization_for_Long-Horizon_LLM_Agents|ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents]]

![[assets/2610.30933_figure.png|800]]

- **arXiv**: [2610.30933](https://arxiv.org/abs/2610.30933)
- **PDF**: https://arxiv.org/pdf/2610.30933
- **详细分析**: [[20_Research/Papers/大模型/ReflectPO_Reflection-Guided_Policy_Optimization_for_Long-Horizon_LLM_Agents|ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents]]
- **作者**: Rumei Li, Xunliang Cai
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.95（加权：大模型 0.95，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ReflecTool-Bench, TRAJECT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With external tools, large language models (LLMs) can tackle complex tasks through sustained environmental interaction. LLM-based agents are therefore increasingly used to tackle complex long-horizon tasks in real-world environments. However, these tasks involve sequential, interdependent decisions and changes in environmental states. Early execution errors affect subsequent interaction histories and environmental states, and their effects accumulate along the decision chain. To address this challenge, we propose Reflection-Guided Policy Optimization (ReflectPO), a reinforcement learning framework for autonomous error recovery in long-horizon tasks. ReflectPO comprises two core components. The first is Reflection-Guided Sampling. We use branch differences and repeated visits in interaction trajectories to construct hints for error recovery. The second is Tree-Structured Credit Assignment. We organize sampled trajectories into trees and assign action-level credit using parent--child reward differences and recovery gains. Experiments over two long-horizon tool-use benchmarks show that ReflectPO outperforms multiple existing baselines in most domains. It also achieves the best overall performance on average. Further analyses show that ReflectPO effectively improves agents' ability to recognize their own deviations, recover from erroneous states, and continue making progress toward task completion.

</details>

---

### [[20_Research/Papers/大模型/Inherited,_Not_Invented_Tracing_the_Provenance_of_Wait_in_Reasoning_Models|Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models]]

![[assets/2610.30882_first_page.png|800]]

- **arXiv**: [2610.30882](https://arxiv.org/abs/2610.30882)
- **PDF**: https://arxiv.org/pdf/2610.30882
- **详细分析**: [[20_Research/Papers/大模型/Inherited,_Not_Invented_Tracing_the_Provenance_of_Wait_in_Reasoning_Models|Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models]]
- **作者**: Zhizhuo Kou, Sizai Hou, Long Chen, Jian Yang, Junyu Luo, Jingshu Peng, Wenkai Zhang, Sirui Han, Yike Guo
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Pre-RL, Zero-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is credited with teaching reasoning models to write {wait} before reconsidering a step, yet large RL accuracy gains do not require the word. This view can confuse what RL discovers with what a model inherits from its training data. We trace the word through open models' training histories, reading it with label-free indices of frequency, position, form and usage and an injected-error test, all computed from sampled outputs. We find that zero-RL almost never coins the marker: on bases that lack the word, RL raises MATH-500 accuracy substantially while {wait} stays near absent. It arrives with training data: mid-training in OLMo-3, and fine-tuning on reasoning traces installs it in most models whose base lacks it. Where the base already uses it, both released RL-Zero recipes (OLMo-3, MiMo) multiply it, whereas KL-free GRPO from the same base does not; OLMo-3's recipe wears down its form and makes it a more sensitive but more liberal alarm; RL after supervised fine-tuning barely changes it, and our GRPO recipe erases a marker seeded by fine-tuning. Finally, we show that marker frequency alone does not indicate RL-induced reasoning and caution against LLM-as-a-judge revision metrics, as automated judges can reverse human-labelled trends.

</details>

---

### [[20_Research/Papers/大模型/Compiling_Autoregressive_LLM_Control_into_Policy-Exact_Parallel_Inference_for_Hierarchical_RAG|Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG]]

![[assets/2610.30664_figure.png|800]]

- **arXiv**: [2610.30664](https://arxiv.org/abs/2610.30664)
- **PDF**: https://arxiv.org/pdf/2610.30664
- **详细分析**: [[20_Research/Papers/大模型/Compiling_Autoregressive_LLM_Control_into_Policy-Exact_Parallel_Inference_for_Hierarchical_RAG|Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG]]
- **作者**: Zehao Lin, Qianfeng Shen, Xixuan Hao, Shaobo Cui, Chunyu Li, Kai Chen, Bo Tang, Zhenjun Wang, Jin Yan, Zhiyu Li, Feiyu Xiong
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models increasingly act as controllers in structured decision pipelines, yet their decisions are still executed by autoregressive text decoding. Hierarchical RAG is one such setting: at each frontier of a document tree, an LLM commits to $b$ of $k$ sections under an input-dependent action grammar, executed as either failure-prone free-form JSON or reliable but strictly serial grammar-constrained generation. We show that this serialization is unnecessary for bounded-horizon control: the reachable future forms a shallow action-prefix tree, which we compile --- one root prefill plus one tree-causal probe evaluate every prefix-conditioned action distribution with serial decoding's tokens, positions, and causal ancestry. A prefix-state lemma makes compiled control policy-exact in exact arithmetic: the same policy with a two-forward critical path and zero output tokens. One further probe pass certifies the exact order-marginalized MAP set. Across four document-disjoint splits and two scales on the primary MetaX device, compiled control matches the serial policy on $84$--$89\%$ of questions --- every instrumented divergence a floating-point near-tie --- and cuts control latency by $35$--$47\%$ versus token-wise serial decoding and $6$--$7\%$ versus an idealized chunked engine; an H800 repetition preserves the ordering.

</details>

---

### [[20_Research/Papers/大模型/IFC-MCQ_Automatically_Generating_Multiple-Choice_Benchmarks_for_Evaluating_LLM_Agents_on_IFC_Data_Retrieval|IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval]]

![[assets/2610.30533_figure.png|800]]

- **arXiv**: [2610.30533](https://arxiv.org/abs/2610.30533)
- **PDF**: https://arxiv.org/pdf/2610.30533
- **详细分析**: [[20_Research/Papers/大模型/IFC-MCQ_Automatically_Generating_Multiple-Choice_Benchmarks_for_Evaluating_LLM_Agents_on_IFC_Data_Retrieval|IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval]]
- **作者**: Rabindra Lamsal, Sisi Zlatanova, Xuesong Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GPQA, IFC-Bench, IFC-QA, IFCMemoryBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industry Foundation Classes (IFC), the standard for building information exchange in architecture, engineering, and construction (AEC), is increasingly queried through large language models (LLMs) using natural language. Evaluating these systems at scale is difficult because free-text answers require costly human or LLM-based review. We propose IFC-MCQ, a method that automatically generates multiple-choice benchmarks from IFC files for exact option-set grading. The taxonomy covers 15 categories and 36 subtypes across four groups, with answer keys derived from the file and distractors constructed from file-derived values or predefined rules. We applied IFC-MCQ to IFC models of varying sizes and modelling characteristics to assess generation coverage and evaluated two agentic configurations on selected models using tool- and code-based retrieval. The evaluation exposed category-specific failure modes and showed that performance can vary with the source IFC model and retrieval interface. IFC-MCQ enables scalable benchmarking of LLM-based IFC retrieval in AEC workflows.

</details>

---

### [[20_Research/Papers/大模型/ChemBART_Pre-training_a_Reaction_Language_Model_for_Comprehensive_Synthesis_Planning|ChemBART: Pre-training a Reaction Language Model for Comprehensive Synthesis Planning]]

![[assets/2601.02915_first_page.png|800]]

- **arXiv**: [2601.02915](https://arxiv.org/abs/2601.02915)
- **PDF**: https://arxiv.org/pdf/2601.02915
- **详细分析**: [[20_Research/Papers/大模型/ChemBART_Pre-training_a_Reaction_Language_Model_for_Comprehensive_Synthesis_Planning|ChemBART: Pre-training a Reaction Language Model for Comprehensive Synthesis Planning]]
- **作者**: Kenan Li, Yijian Zhang, Jin Wang, Haipeng Gan, Zeying Sun, Xiaoguang Lei, Hao Dong
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.65，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ChemBART: Pre-training a Reaction Language Model for Comprehensive Synthesis Planning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large language models (LLMs) have demonstrated transformative potential across diverse fields. However, in computer-aided synthesis planning (CASP), current LLM methodologies are often restricted to single-molecule representations, limiting their application to isolated, single-task scenarios such as precursor prediction. Addressing this gap, we present ChemBART, a BART-based language model that adopts a reaction-centric pre-training strategy. By leveraging a mask-filling pre-training task on holistic reaction expressions (Reactant &gt; Reagent &gt; Product), ChemBART effectively solves a variety of chemical problems, including precursor/reagent generation, temperature-yield regression, and molecular property classification. Building on these capabilities, we demonstrate the integration of ChemBART with Monte Carlo tree search (MCTS) for multi-step synthesis route design, where the model serves to optimize the policy and value functions within a reinforcement learning framework. Beyond single-molecule pre-trained LLMs that are constrained to specific applications, ChemBART unifies diverse chemical tasks to facilitate synthesis planning with comprehensive implementation information. Most significantly, the proposed multi-step synthesis routes and reaction conditions were validated in the wet lab, confirming the discovery of shorter synthetic pathways with a &gt;20% yield improvement over established literature benchmarks. Our work highlights the potential of reaction-focused pre-training and showcases the broad utility of ChemBART in closing the loop between in silico prediction and wet-lab synthesis.

</details>

---
