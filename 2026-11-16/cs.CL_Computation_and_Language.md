# cs.CL | Computation and Language | 2026-11-16

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/大模型/Agentic_induction_of_common_data_elements_and_information_extraction_from_sarcoma_case_report_abstracts|Agentic induction of common data elements and information extraction from sarcoma case report abstracts]]

![[assets/2611.18506_figure.png|800]]

- **arXiv**: [2611.18506](https://arxiv.org/abs/2611.18506)
- **PDF**: https://arxiv.org/pdf/2611.18506
- **详细分析**: [[20_Research/Papers/大模型/Agentic_induction_of_common_data_elements_and_information_extraction_from_sarcoma_case_report_abstracts|Agentic induction of common data elements and information extraction from sarcoma case report abstracts]]
- **作者**: Daniel Reichenpfader, Kwaku Appiagyei, Manovah Nadarajah, Ahmed Reda Bahr, Irina Filchenko, Fabio Dennstädt
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agentic induction of common data elements and information extraction from sarcoma case report abstracts》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CaseReportBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Common data elements (CDEs) support clinical data comparability but are usually defined manually. We investigated whether large language model agents could derive a CDE schema from sarcoma case report abstracts and apply it at scale. An agent proposed 72,909 candidate CDEs from 24,588 PubMed abstracts; agentic consolidation yielded 1,570 CDEs. We retained 53 supported by at least 50 abstracts and attempted evidence-linked extraction across the corpus. Processing succeeded for all retained CDEs in 79.2% of abstracts, including responses indicating non-mention. Two human reviewers approved 83.0% of retained CDEs for relevance, 67.9% for clarity, and 56.6% for correctness. In 100 sampled abstracts, exact agreement with the value extracted by the LLM was 94.9% among 1,116 pairs with a non-empty answer (abstract-level bootstrap 95% CI, 93.0-96.4%). Errors concentrated in anatomical and temporal fields. These findings support agent-assisted schema drafting followed by expert curation before large-scale extraction.

</details>

---

### [[20_Research/Papers/大模型/Clean_Tickets,_Wrong_Orders_Catching_Silent_Errors_with_a_Language_Model_in_Your_Browser_Tab|Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab]]

![[assets/2611.18284_first_page.png|800]]

- **arXiv**: [2611.18284](https://arxiv.org/abs/2611.18284)
- **PDF**: https://arxiv.org/pdf/2611.18284
- **详细分析**: [[20_Research/Papers/大模型/Clean_Tickets,_Wrong_Orders_Catching_Silent_Errors_with_a_Language_Model_in_Your_Browser_Tab|Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab]]
- **作者**: Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, Sergey Ivanov, Ivan Khodnenko
- **cs 子类**: cs.CL, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A small language model that turns a typed order into structure can fail in two ways. It can print something broken, which any system rejects. Or it can print a clean, well formed order that nobody placed. Our companion work calls the second kind a silent error, and it is the dangerous one. We present a web demo in which a fine-tuned 0.8B parameter model runs entirely inside the visitor's browser tab, through llama.cpp compiled to WebAssembly. No order text leaves the device. The page parses orders as the visitor types, scores every ticket with the PIZZA benchmark's own matcher ported to TypeScript, refuses anything off the menu with "?" so the model can face the open web, and lets visitors hunt for silent errors or try to cause one. Run in the browser on all 1,357 PIZZA test orders, the deployed model writes the same output as the server evaluation for 99.0% of them and reaches the same exact match (0.882); we also report its latency on 3 consumer laptops. Demo: https://wrong.cuyor.com

</details>

---

### [[20_Research/Papers/大模型/Agent-as-a-Judge|Agent-as-a-Judge]]

![[assets/2611.18067_figure.png|800]]

- **arXiv**: [2611.18067](https://arxiv.org/abs/2611.18067)
- **PDF**: https://arxiv.org/pdf/2611.18067
- **详细分析**: [[20_Research/Papers/大模型/Agent-as-a-Judge|Agent-as-a-Judge]]
- **作者**: Runyang You, Hongru Cai, Caiqi Zhang, Qiancheng Xu, Meng Liu, Tiezheng Yu, Yongqi Li, Wenjie Li
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agent-as-a-Judge》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：G-Eval, MT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial intelligence has progressed from task-specific systems toward general models spanning perception, generation, reasoning, and autonomous interaction, making reliable evaluation essential for comparison, deployment, and post-training feedback. At scale, modern evaluation pipelines increasingly rely on LLM-as-a-Judge to produce scores, preferences, and critiques; in its fixed-context setting, the judge relies on the supplied evaluand and evaluation materials. Yet a reliable verdict may require evidence beyond the supplied evaluand and context---either because critical environmental states remain unrecorded in the static execution log, or because controversial factual claims require external verification. Passive judges cannot obtain that missing evidence before deciding, especially when evaluating agent trajectories, executable artifacts, or domain-specific reports. Recent work therefore develops active evaluators that seek missing evidence and update their grounds for judgment before deciding. We bring these advances together through Agent-as-a-Judge, focusing on how evaluators construct and control checking processes within the broader LLM-based judging landscape. We define the scope through evaluation-directed checks and the use of their results, covering both structured workflows and observation-driven control. We organize the design space by multi-agent collaboration, tool integration, memory, and planning, and show how these mechanisms supply the checks and evidence on which a verdict rests. We consolidate published scores and reproduce missing entries for key agentic judges; the comparison reveals uneven agentic gains and motivates dedicated agentic evaluation. We conclude by characterizing application demands and open challenges in cost, reliability, safety, and governance that condition trusted deployment of agentic judges at scale.

</details>

---

### [[20_Research/Papers/大模型/RAG-FGO_Dynamic_Optimization_of_Query-Rewriting_Agents_for_Generative_RAG|RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG]]

![[assets/2611.17788_figure.png|800]]

- **arXiv**: [2611.17788](https://arxiv.org/abs/2611.17788)
- **PDF**: https://arxiv.org/pdf/2611.17788
- **详细分析**: [[20_Research/Papers/大模型/RAG-FGO_Dynamic_Optimization_of_Query-Rewriting_Agents_for_Generative_RAG|RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG]]
- **作者**: Qigan Sun, Xudong Wang, Chaoning Zhang, Chenghao Li, Jiaquan Zhang, Jiehui Xie, Sungyoung Lee, Jie Zou, Ning Xie, Peng Wang, Yang Yang, Heng Tao Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In retrieval-augmented generation (RAG), query rewriting serves as a core interface that aligns user intent with external knowledge bases, and its effectiveness directly determines overall system performance. However, generative retrieval faces three critical challenges in real-world deployment: noisy retrieval feedback, the difficulty of jointly optimizing discrete prompt templates and continuous decoding-control parameters, and the limited generalization of static rewriting strategies under semantically complex scenarios. To address these issues, we propose RAG-FGO, a dynamic optimization framework for generative retrieval strategies. RAG-FGO formulates query rewriting as a non-differentiable black-box optimization problem in a mixed discrete-continuous space, and represents prompt templates and decoding parameters as adaptively optimizable query-rewriting agents. The framework performs global search to enable semantic jumps and structural reorganization that escape local optima, while applying local perturbations for fine-grained alignment and precise refinement. In addition, RAG-FGO introduces an elite-preserving memory pool that accumulates high-quality strategies across iterations, thereby mitigating the impact of stochasticity and noisy feedback on optimization stability. Experimental results on a diverse suite of benchmarks demonstrate the effectiveness and robustness of the proposed method, supporting its applicability to complex semantic retrieval tasks.

</details>

---

### [[20_Research/Papers/大模型/See_Every_Block_Once_Variance-Reduced_Post-Training_for_Masked_Diffusion_Language_Models|See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models]]

![[assets/2611.17754_first_page.png|800]]

- **arXiv**: [2611.17754](https://arxiv.org/abs/2611.17754)
- **PDF**: https://arxiv.org/pdf/2611.17754
- **详细分析**: [[20_Research/Papers/大模型/See_Every_Block_Once_Variance-Reduced_Post-Training_for_Masked_Diffusion_Language_Models|See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models]]
- **作者**: Yunzhen He, Hiroaki Yamagiwa, Hidetoshi Shimodaira
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.55（加权：大模型 0.35，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy gradient methods are widely used to align large language model outputs with human preferences, but the log-likelihoods they require cannot be directly computed in Masked Diffusion Language Models (MDLMs). MDLM post-training therefore relies on a surrogate objective based on the Evidence Lower Bound (ELBO), and recent work estimates a blockwise variant of this objective via Monte Carlo methods to support blockwise generation. However, existing estimation schemes randomly sample the block index, so they may evaluate the same block more than once and leave some blocks unevaluated. This introduces variance arising from block selection into the estimates. In this work, we propose a full-block estimator that evaluates every block exactly once and averages the results. We theoretically show that the proposed estimator remains unbiased while eliminating the between-group variance arising from block selection, thereby achieving lower variance than the baseline for the same sample size. In experiments on five benchmarks spanning mathematics, planning, and coding, our method achieves the highest accuracy on four benchmarks and outperforms the random block sampling baseline by an average of 12.79 points.

</details>

---

### [[20_Research/Papers/大模型/LightTAR_Light_and_Fast_Target-Aware_Representations_for_Multimodal_Tabular_Learning|LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning]]

![[assets/2611.17600_first_page.png|800]]

- **arXiv**: [2611.17600](https://arxiv.org/abs/2611.17600)
- **PDF**: https://arxiv.org/pdf/2611.17600
- **详细分析**: [[20_Research/Papers/大模型/LightTAR_Light_and_Fast_Target-Aware_Representations_for_Multimodal_Tabular_Learning|LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning]]
- **作者**: Eilam Shapira, Alan Arazi, Shoham Grunblat, Roi Reichart
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MulTaBench, RamanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal tabular learning involves classification and regression on tables combining structured numerical and categorical features with unstructured text and images. These unstructured fields are commonly represented by pretrained encoder embeddings reduced with principal component analysis (PCA). This reduction prioritizes input variance but may overlook information relevant to predicting the target. We introduce LightTAR, a simple, inexpensive method that adapts dimensionality reduction to the prediction task. LightTAR augments the standard PCA representation with a few target-aware features extracted jointly from the final and an intermediate encoder layer using regularized partial least squares (PLS). We evaluate LightTAR with 21 tabular models, including tree ensembles, neural networks, and tabular foundation models. LightTAR improves average predictive performance for all models and, averaged across models, improves prediction on almost every MulTaBench dataset. These gains come with a small increase in total runtime relative to PCA representations. LightTAR integrates directly into existing encoding pipelines, improving tabular learners' predictive performance without modifying the encoder or the learner.

</details>

---

### [[20_Research/Papers/大模型/Unfinished-Bench_Measuring_Rule_Violations_by_Persistent_Agents_in_Realistic_Work_Environments|Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments]]

![[assets/2611.17460_figure.png|800]]

- **arXiv**: [2611.17460](https://arxiv.org/abs/2611.17460)
- **PDF**: https://arxiv.org/pdf/2611.17460
- **详细分析**: [[20_Research/Papers/大模型/Unfinished-Bench_Measuring_Rule_Violations_by_Persistent_Agents_in_Realistic_Work_Environments|Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments]]
- **作者**: Seunghyun Lee, Jaehui Hwang, Dongyoon Han, Sangdoo Yun
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Unfinished-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are increasingly equipped with persistence toward task completion to run delegated work autonomously for long periods, under many unstated constraints from internal documents and other people's authority. When completion requires violating a rule, the agent must decide alone, yet benchmarks of instruction-rule conflicts state the rule in the prompt or keep it hidden and do not evaluate persistence. We present Unfinished-Bench, a benchmark that gives models persistence in autonomous runs without a user, in realistic work environments with embedded rules. In each of its 97 scenarios across 7 organizations and 7 risk categories, the goal and the rule cannot both hold. We find that persistence raised violations of a rule in an internal document from 32.2% to 43.6%, five times the 8.5% for the same rule stated by the user. Of the document-rule violations, 98.3% occurred after the rule was displayed, and in 89% of a judged sample the agent first wrote down the rule. Violations of rules placed in the environment without user oversight can lead to serious incidents, so persistence-driven risks need to be evaluated. Benchmark documentation: https://francis21c.github.io/unfinished-bench/

</details>

---
