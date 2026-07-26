# cs.CL | Computation and Language | 2026-07-24

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/大模型/An_Evaluation_Framework_for_Structured_Audio_Captions_Validated_by_Controlled_Perturbations|An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations]]

![[assets/2607.21424_figure.png|800]]

- **arXiv**: [2607.21424](https://arxiv.org/abs/2607.21424)
- **PDF**: https://arxiv.org/pdf/2607.21424
- **详细分析**: [[20_Research/Papers/大模型/An_Evaluation_Framework_for_Structured_Audio_Captions_Validated_by_Controlled_Perturbations|An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations]]
- **作者**: Liang-Yuan Wu, Sripathi Sridhar, Mark Cartwright, Magdalena Fuentes
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in automated audio captioning (AAC) have shifted from monolithic sentence generation toward structured formats that explicitly disentangle distinct acoustic and semantic properties. However, evaluating this heterogeneous data remains a significant challenge. Existing caption metrics focus on flat textual outputs and fail to reliably assess multimodal attributes. To bridge this gap, we propose a multi-axis evaluation framework tailored for structured audio descriptions. Building on the AudioCards dataset, we evaluate outputs across five orthogonal axes: tag-sets, descriptions, logical reasoning, numeric measurements, and spectral profiles. Our approach combines Large Language Model (LLM) judges to capture semantic nuance with deterministic computational metrics to precisely measure acoustic deviations. To rigorously validate the reliability of this framework, we introduce a controlled perturbation testing protocol that injects typed, graded errors into groundtruth annotations. Our results demonstrate that this framework successfully distinguishes meaning-preserving paraphrases from genuine semantic and acoustic corruptions.

</details>

---

### [[20_Research/Papers/大模型/MemTools_A_Unified_Research_Framework_for_Interoperable_Agent_Memory|MemTools: A Unified Research Framework for Interoperable Agent Memory]]

![[assets/2607.21404_figure.png|800]]

- **arXiv**: [2607.21404](https://arxiv.org/abs/2607.21404)
- **PDF**: https://arxiv.org/pdf/2607.21404
- **详细分析**: [[20_Research/Papers/大模型/MemTools_A_Unified_Research_Framework_for_Interoperable_Agent_Memory|MemTools: A Unified Research Framework for Interoperable Agent Memory]]
- **作者**: Chengfeng Zhao, Jinhui Chen, Sirui Liang, Shizhu He, Yequan Wang, Jun Zhao, Kang Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《MemTools: A Unified Research Framework for Interoperable Agent Memory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While memory systems are essential for agent architectures, pervasive architectural fragmentation restricts systematic research. Existing implementations typically couple different stages of the memory lifecycle, entangle evaluation logic with specific datasets, and provide limited support for the management of heterogeneous memory types. We introduce MemTools, an interoperability research framework that decouples memory system components from their underlying deployment environments. MemTools standardizes the memory lifecycle through declarative data contracts, enabling the interchangeable assembly of components across different systems. It orthogonally separates benchmark datasets from execution protocols to facilitate controlled assessments. Furthermore, MemTools provides a unified computational interface for coordinating symbolic, neural, and multimodal memory representations within a shared runtime. Empirical evaluations on cross-system component integration, evaluation protocol reconfiguration, and heterogeneous memory coordination demonstrate that MemTools enables systematic isolation and analysis of memory design variables. These findings suggest that MemTools provides a practical and extensible infrastructure for advancing principled research on agent memory.

</details>

---

### [[20_Research/Papers/大模型/Capital_Markets_LLM_Reliability_Score_(CM-LRS)_From_Plausible_to_Bankable|Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable]]

![[assets/2607.21340_first_page.png|800]]

- **arXiv**: [2607.21340](https://arxiv.org/abs/2607.21340)
- **PDF**: https://arxiv.org/pdf/2607.21340
- **详细分析**: [[20_Research/Papers/大模型/Capital_Markets_LLM_Reliability_Score_(CM-LRS)_From_Plausible_to_Bankable|Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable]]
- **作者**: Prerit Ahuja
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BIG-Bench, ContractEval, ConvFinQA, FinQA, FinanceBench, InvestorBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accuracy, and finance benchmarks (FinanceBench, FinQA, ConvFinQA) advance document-grounded and numerical QA but evaluate at the question-answer layer rather than the workflow outputs practitioners defend. We introduce CM-LRS, a Capital Markets LLM Reliability Score, evaluating outputs at the workflow-output layer across seven dimensions: factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability. Each is scored 0-5 against a rubric anchored on signals reviewers in regulated settings use; the aggregate is tunable to the workflow. We demonstrate CM-LRS on five workflows (DCM transaction-terms extraction, precedent retrieval, issuer profile synthesis, M&amp;A transaction-comparable reasoning, ECM transaction-terms extraction) over public SEC EDGAR filings, a public UK takeover release, and fictional synthetic supplements, scoring four models against four independent LLM judges spanning three model families. Three findings. First, the frontier closed-source models cluster within 0.22 points on four-judge averaged CM-LRS (Sonnet 4.6 = 4.31, Opus 4.7 = 4.30, GPT-5.5 = 4.09); all four judges place the open-weights baseline (Llama 3.3 70B = 3.15) last. Second, that gap concentrates on retrieval (2.23) and synthesis (2.15), not extraction (0.84). Third, Decision Usefulness shows the widest cross-model dispersion of any dimension (4.0 points on issuer profiling) and top-tier inter-judge agreement (mean r = 0.52). Plausibility is cheap. Bankability is the bar.

</details>

---

### [[20_Research/Papers/大模型/A_Unified_Moral-Value_Dataset_for_Instruction_Tuning|A Unified Moral-Value Dataset for Instruction Tuning]]

![[assets/2607.21279_figure.png|800]]

- **arXiv**: [2607.21279](https://arxiv.org/abs/2607.21279)
- **PDF**: https://arxiv.org/pdf/2607.21279
- **详细分析**: [[20_Research/Papers/大模型/A_Unified_Moral-Value_Dataset_for_Instruction_Tuning|A Unified Moral-Value Dataset for Instruction Tuning]]
- **作者**: Zhaohui Zeng, Florian Mai
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: cs.CL

#### 研究背景与动机

《A Unified Moral-Value Dataset for Instruction Tuning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have developed rapidly and become valuable tools in everyday life. However, how to align LLMs to a particular set of human values is still an open problem. Recent studies show that instruction tuning has strong potential for zero-shot tasks and may serve as an effective approach to addressing value alignment. Nevertheless, although many datasets for instruction tuning already exist, they are not specifically designed around moral scenarios and behaviors. We construct a unified moral-value dataset that can be directly used for instruction tuning. This dataset is built upon existing moral-value datasets by merging them into a unified corpus and converting them into an instruction-response format. We show that training on a mixed dataset combining general task datasets with our dataset preserves general-task performance, and we report preliminary observations on how the mixing ratio affects value-oriented task performance. Our work provides a moral-value dataset for instruction tuning and offers a useful resource for further alignment research. The dataset is available at https://huggingface.co/datasets/teohzzh/value-for-instruction-tuning.

</details>

---

### [[20_Research/Papers/大模型/Sample-Efficient_Learning_from_Agent_Experience|Sample-Efficient Learning from Agent Experience]]

![[assets/2607.21051_first_page.png|800]]

- **arXiv**: [2607.21051](https://arxiv.org/abs/2607.21051)
- **PDF**: https://arxiv.org/pdf/2607.21051
- **详细分析**: [[20_Research/Papers/大模型/Sample-Efficient_Learning_from_Agent_Experience|Sample-Efficient Learning from Agent Experience]]
- **作者**: Chenhui Gou, Haoqin Tu, Yunhao Fang, Jianfei Cai, Hamid Rezatofighi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Sample-Efficient Learning from Agent Experience》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interaction histories without sacrificing environment sample efficiency remains underexplored. We term this problem Experience Distillation and develop an implementation that requires no further environment interaction beyond the collected experience. Experiments on 749 curated software-engineering tasks and six text-adventure games show that it retains at least 64.8\% of the gains from in-context learning across both domains, whereas direct supervised fine-tuning on the collected experience recovers only 3.8\%. Compared with classical reinforcement-learning baselines, in-context learning from trial-and-error experience followed by Experience Distillation matches their performance with at least \(9.6\times\) fewer environment samples.

</details>

---

### [[20_Research/Papers/大模型/Tencent_WorkBuddy_Bench_A_Multi-Domain_Coding-Agent_Benchmark_with_Contamination-Resistant_Task_Construction|Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction]]

![[assets/2607.20911_figure.png|800]]

- **arXiv**: [2607.20911](https://arxiv.org/abs/2607.20911)
- **PDF**: https://arxiv.org/pdf/2607.20911
- **详细分析**: [[20_Research/Papers/大模型/Tencent_WorkBuddy_Bench_A_Multi-Domain_Coding-Agent_Benchmark_with_Contamination-Resistant_Task_Construction|Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction]]
- **作者**: Tencent WorkBuddy Bench Team, Siqi Cai, Shaopeng Chen, Xiang Fei, Yong Mao, Zihan Xu, Zhiheng Lyu, Zhijian Shao, Yuchen Shi, Shuwen Zhang, Chaofan Qiu, Linjie Che...
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CursorBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Tencent WorkBuddy Bench, a multi-domain evaluation suite for coding agents; this report documents its construction methodology, scoring protocol, and a cross-model leaderboard. At its core is a unified evaluation framework for constructing and running distribution-informed coding-agent tasks across four work domains - Code, Web, Office, and Security. Rather than adapting public issue text, every task is reverse-engineered from a real commit, pull request, or business scenario and rewritten as a short, colloquial, role-played request, so that a task's prompt is not recoverable by web-searching the underlying issue, pull request, or commit thread. Because the dataset is released openly - task directories, environment images, evaluation harness, tests, and reference solutions - contamination resistance rests on this construction together with dataset versioning rather than on secrecy. The four subsets - repository-level engineering, front-end development, office and business workflows, and red-/blue-team security - probe complementary facets of real work, each with its own verification style. All are packaged in a uniform task-directory format and run, under a uniform and reproducible protocol, on two agent harnesses (CodeBuddy Code and Claude Code); the full open release makes the benchmark reproducible end to end and directly auditable, since any third party can re-run each task and inspect its content. Because each subset uses a different scoring instrument, scores are not comparable across subsets and the suite reports no suite-wide average. We report a cross-model leaderboard across several model families.

</details>

---

### [[20_Research/Papers/大模型/Learning_to_Detect_UI_Principle_Violations_via_Reinforcement_Learning|Learning to Detect UI Principle Violations via Reinforcement Learning]]

![[assets/2607.20690_figure.png|800]]

- **arXiv**: [2607.20690](https://arxiv.org/abs/2607.20690)
- **PDF**: https://arxiv.org/pdf/2607.20690
- **详细分析**: [[20_Research/Papers/大模型/Learning_to_Detect_UI_Principle_Violations_via_Reinforcement_Learning|Learning to Detect UI Principle Violations via Reinforcement Learning]]
- **作者**: Nishi Mehta, Swathi Alse, Himani Kumavat, Yue Yu, Pratik Jayarao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.55，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Learning to Detect UI Principle Violations via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small language models and coding agents increasingly generate web front-end code, yet their outputs are typically evaluated primarily for functional correctness. A generated interface may compile, render, and pass unit tests while still violating established interface quality principles, including accessibility barriers, deceptive design patterns, poor visual hierarchy, and excessive decision complexity. Existing auditing approaches face a trade-off between cost, coverage, and scalability: expert human review provides rich judgment but is slow and expensive; frontier vision-language models offer broader reasoning capabilities but remain costly to deploy at scale; and rule-based tools such as axe-core and Lighthouse are inexpensive but primarily capture mechanically checkable accessibility issues. We investigate whether a lightweight vision-language model can serve as an effective critic for generated interfaces. We unify 19 interface-quality principles from three complementary sources of HCI knowledge: WCAG 2.2 accessibility standards, deceptive design taxonomies, and established theories of perception, cognition, and interaction. To train this critic, we construct a verified dataset of approximately 10,000 generated web pages by synthetically injecting known violations into clean, LLM-generated Tailwind pages. Continued reinforcement learning on a 4B vision-language model improves micro-F1 from 36\% to 84\%, with 13 of 19 principles exceeding 80\% F1. The resulting critic can audit generated interfaces, filter low-quality interface training data, and provide a reward signal for design-aware code generation. We release our data-generation recipe and injection/verification prompts to support reproducible evaluation and future work on scalable interface-quality assessment.

</details>

---

### [[20_Research/Papers/大模型/Domyn-Small_A_European_10B_Reasoning_Language_Model|Domyn-Small: A European 10B Reasoning Language Model]]

![[assets/2607.20448_figure.png|800]]

- **arXiv**: [2607.20448](https://arxiv.org/abs/2607.20448)
- **PDF**: https://arxiv.org/pdf/2607.20448
- **详细分析**: [[20_Research/Papers/大模型/Domyn-Small_A_European_10B_Reasoning_Language_Model|Domyn-Small: A European 10B Reasoning Language Model]]
- **作者**: Simone Angarano, Francesco Bertolotti, Federico D'Ambrosio, Michele Resta, Alessandro Rognoni, Nicolò Ruggeri, Dario Salvati, Andrea Valenti, Alberto Veneri, Martin Cimmino
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《Domyn-Small: A European 10B Reasoning Language Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CCNet, GPQA, GQA, IFEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Domyn-Small, a 10-billion-parameter open-weight reasoning language model released under the MIT license. Domyn-Small is the product of an initial pre-training phase on 9 trillion tokens multilingual data, followed by a post-training pipeline for reasoning, instruction following, and context extension. For the latter, we performed a Continued Pre-Training (CPT) phase that doubles the native context window to 32K tokens, followed by SFT with a math-focused annealing run. Finally, the RL phase includes GRPO with verifiable rewards, DPO, and a multi-environment GRPO stage spanning five task domains: mathematics, code, multiple-choice QA, instruction-following, and tool calling. The 32K-token native context extends to 128K at inference via YaRN, and a chat-template toggle enables dual-mode reasoning. Against peer models in the 7--10B class (Qwen3.5-9B, OLMo-3-7B-Think, Nemotron-Nano-8B, Ministral-3-8B), Domyn-Small achieves a strong accuracy-efficiency balance: it produces roughly one-third as many tokens as Qwen3.5-9B and approximately 35% of OLMo-3-7B-Think's token budget on core reasoning benchmarks, while delivering strong instruction-following (IFEval 79.9) and competitive science reasoning (GPQA-Diamond 50.0). We release the weights and the post-training recipe alongside Domyn Swarm (Apache~2.0), an open-source framework for scalable LLM inference on HPC clusters developed during this program and used throughout this work.

</details>

---

### [[20_Research/Papers/大模型/Distinguishing_Artificial_from_Authentic_Evaluating_LLMs_for_Detecting_LLM-Generated_Content|Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content]]

![[assets/2607.20446_figure.png|800]]

- **arXiv**: [2607.20446](https://arxiv.org/abs/2607.20446)
- **PDF**: https://arxiv.org/pdf/2607.20446
- **详细分析**: [[20_Research/Papers/大模型/Distinguishing_Artificial_from_Authentic_Evaluating_LLMs_for_Detecting_LLM-Generated_Content|Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content]]
- **作者**: Juho Leinonen, Paul Denny
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models (LLMs) are increasingly used by students to generate natural language responses and program code, there is growing interest in whether LLMs themselves can be used to distinguish AI-generated work from human-authored submissions. In this paper, we investigate the extent to which LLMs can detect their own generated content across multiple educational task types, including programming exercises, reflective writing, and short-answer questions. Using authentic student responses and multiple variants of LLM-generated answers, we evaluate detection performance under different prompting strategies and output formats. Our study addresses three research questions: (1) how accurately LLMs can identify their own outputs across task domains, (2) how detection effectiveness is influenced by factors such as prompt design, response length, and task type, and (3) what characteristics of LLM-generated responses contribute to successful or failed detection. Our findings show that LLM-based detection is highly task-dependent: detection is substantially more reliable for programming tasks and longer reflective responses, but performs poorly for short-answer questions, where LLMs frequently judge their own outputs as more human-like than authentic student responses. We further find that prompt framing and response verbosity have a pronounced effect on detectability in reflective writing tasks, with relatively minor prompt variations significantly reducing detection accuracy, while programming-related detection is more robust to prompt changes. Together, these results highlight both the potential and the limitations of LLM self-detection in educational settings and suggest caution in relying on LLMs as standalone tools for identifying AI-generated student work.

</details>

---

### [[20_Research/Papers/大模型/Belief_Propagation_in_LLM_World_Models_Measuring_Strategic_Information_Bias_with_Prediction_Markets|Belief Propagation in LLM World Models: Measuring Strategic Information Bias with Prediction Markets]]

![[assets/2607.20441_figure.png|800]]

- **arXiv**: [2607.20441](https://arxiv.org/abs/2607.20441)
- **PDF**: https://arxiv.org/pdf/2607.20441
- **详细分析**: [[20_Research/Papers/大模型/Belief_Propagation_in_LLM_World_Models_Measuring_Strategic_Information_Bias_with_Prediction_Markets|Belief Propagation in LLM World Models: Measuring Strategic Information Bias with Prediction Markets]]
- **作者**: Mykola Khandoga, Yevhen Kostiuk, Anton Polishko, Yurii Filipchuk, Kostiantyn Kozlov, Dmytro Zamriy, Artur Kiulian
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.37（加权：大模型 0.45，强化学习 0.16，世界模型 0.76）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Belief Propagation in LLM World Models: Measuring Strategic Information Bias with Prediction Markets》归入 世界模型、大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ForecastBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Every information ecosystem produces beliefs that shape strategic decisions. Both human analysts and AI systems inherit the blind spots of their information sources. We show that LLMs, combined with prediction markets, function as a calibrated instrument for measuring how far ecosystem-induced beliefs deviate from an external reference: LLMs extract the beliefs a text corpus implies, and prediction market price trajectories, anchored at resolution by realised outcomes, provide the calibration reference against which to quantify the deviation. We isolate the bias contribution of specific text through ablation: varying information context while holding the model fixed, with a contaminated model that knows actual outcomes as control. Applied to 111 Ukraine-related prediction markets, comprising approximately 93,000 predictions across four models, we find that English news context systematically biases territorial predictions, wrong 64 to 72 percent of the time when it pushes predictions toward territorial capture. A contaminated model that knows actual outcomes shows the same error rate, indicating that the bias originates primarily in the text. Supplementing with Ukrainian military-analytical sources reduces the bias for all clean models, while absolute-error gains are partial and model-dependent. We show that the distortion originates primarily in the sources, not the models. Consistent across four architectures, it will persist in any system that processes them and propagate into downstream decisions.

</details>

---

### [[20_Research/Papers/大模型/Skill-Contracted_Agents_for_Evidence-Aware_Materials_Literature_Analysis|Skill-Contracted Agents for Evidence-Aware Materials Literature Analysis]]

![[assets/2607.20431_figure.png|800]]

- **arXiv**: [2607.20431](https://arxiv.org/abs/2607.20431)
- **PDF**: https://arxiv.org/pdf/2607.20431
- **详细分析**: [[20_Research/Papers/大模型/Skill-Contracted_Agents_for_Evidence-Aware_Materials_Literature_Analysis|Skill-Contracted Agents for Evidence-Aware Materials Literature Analysis]]
- **作者**: Bixuan Li, Yu Liu, Shuo Shi, Xiaoya Huang, Peng Kang, Lei Zheng
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Skill-Contracted Agents for Evidence-Aware Materials Literature Analysis》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Materials science literature analysis requires simultaneous attention to composition, processing, characterization, and property relationships, yet conventional retrieval-augmented generation pipelines struggle to reconcile heterogeneous tasks within a single retrieve-then-generate architecture. Here we present AlphaAgent, a skill-driven agent framework that decouples retrieval-based question answering from paper-level report generation through explicit skill contracts. A dedicated retrieval skill rewrites user requests into material-specific search intents, queries a curated index of more than 300,000 papers from the Journal Citation Reports Metallurgy and Metallurgical Engineering category, and reformulates queries when initial evidence is insufficient. A separate report-generation skill parses full-text PDFs to produce structured per-paper analytical reports and cross-paper summaries. In a blind evaluation on 40 materials-science questions, half of which required deep analytical reasoning, AlphaAgent substantially outperformed a baseline system matched for underlying model, document index, and retrieval scale, with the largest gains in mechanistic explanation and awareness of credibility boundaries. These results indicate that explicit task separation, refined retrieval intent, and evidence-aware generation improve large-language-model-based literature analysis for materials research.

</details>

---

### [[20_Research/Papers/大模型/Human-in-the-Loop_Large_Language_Model_Framework_for_Identification_of_Cutaneous_Immune-Related_Adverse_Events|Human-in-the-Loop Large Language Model Framework for Identification of Cutaneous Immune-Related Adverse Events]]

![[assets/2607.20428_first_page.png|800]]

- **arXiv**: [2607.20428](https://arxiv.org/abs/2607.20428)
- **PDF**: https://arxiv.org/pdf/2607.20428
- **详细分析**: [[20_Research/Papers/大模型/Human-in-the-Loop_Large_Language_Model_Framework_for_Identification_of_Cutaneous_Immune-Related_Adverse_Events|Human-in-the-Loop Large Language Model Framework for Identification of Cutaneous Immune-Related Adverse Events]]
- **作者**: Charles Lu, Olivia Burke, Debby Cheng, Adam Kashlan, Caitlyn Duffy, Zeyun Lu, Lirit Fuksman, Jin Ning Tian, Andrew Sedlack, Priya Katyal, Eudora Lee, Ralina Karagenova...
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Human-in-the-Loop Large Language Model Framework for Identification of Cutaneous Immune-Related Adverse Events》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study evaluated a retrieval-augmented, multi-agent large language model (LLM)-driven, human-in-the-loop framework for detecting cutaneous immune-related adverse events (cirAEs) from clinical notes. Compared with unassisted manual review, the LLM-assisted workflow improved accuracy (F1 = 0.88 vs 0.77), inter-rater agreement measured by Cohen's kappa (kappa = 0.82 vs 0.50), and reduced average review time by approximately half. This framework pilots how LLMs can be applied to identify immune-related toxicities across organ systems and, more broadly, enable accurate, scalable, and transparent adverse event data extraction.

</details>

---

### [[20_Research/Papers/具身智能/Search-on-Graph-R1_Training_Large_Language_Models_to_Search_Knowledge_Graphs_with_Reinforcement_Learning|Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning]]

![[assets/2607.18481_figure.png|800]]

- **arXiv**: [2607.18481](https://arxiv.org/abs/2607.18481)
- **PDF**: https://arxiv.org/pdf/2607.18481
- **详细分析**: [[20_Research/Papers/具身智能/Search-on-Graph-R1_Training_Large_Language_Models_to_Search_Knowledge_Graphs_with_Reinforcement_Learning|Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning]]
- **作者**: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GrailQA, KGQA, Rule-KBQA, SFT-then-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-Graph-R1 (\sogrone{}), which internalizes this navigation into a compact 8B model through supervised fine-tuning (SFT) followed by reinforcement learning (RL). Our central idea is to scaffold a frontier teacher with each question's gold SPARQL query, so the teacher traverses a known answer-bearing path with a live \texttt{Search} tool rather than having to discover the path itself. Since every call executes against a live Freebase server, the resulting trajectories are grounded in the knowledge graph by construction. On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against. It does so using no auxiliary module at inference and no LLM judge during training. Isolating each training stage shows that SFT and RL contribute complementary gains, our approach transfers across model families, and RL learns to reach answers in fewer \texttt{Search} calls than its SFT initialization.

</details>

---

### [[20_Research/Papers/具身智能/Search-on-Graph_Iterative_Informed_Navigation_for_Large_Language_Model_Reasoning_on_Knowledge_Graphs|Search-on-Graph: Iterative Informed Navigation for Large Language Model Reasoning on Knowledge Graphs]]

![[assets/2510.08825_figure.png|800]]

- **arXiv**: [2510.08825](https://arxiv.org/abs/2510.08825)
- **PDF**: https://arxiv.org/pdf/2510.08825
- **详细分析**: [[20_Research/Papers/具身智能/Search-on-Graph_Iterative_Informed_Navigation_for_Large_Language_Model_Reasoning_on_Knowledge_Graphs|Search-on-Graph: Iterative Informed Navigation for Large Language Model Reasoning on Knowledge Graphs]]
- **作者**: Jia Ao Sun, Hao Yu, Fabrizio Gotti, Fengran Mo, Yihong Wu, Yuchen Hui, Zhan Su, Lingfeng Xiao, Jian-Yun Nie
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, EmbodiedAI

#### 研究背景与动机

《Search-on-Graph: Iterative Informed Navigation for Large Language Model Reasoning on Knowledge Graphs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ChatKBQA, EffiQA, FC-KBQA, GRAFT-Net, KGQA, PullNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) augmented with knowledge graphs (KGs) offer a promising approach for knowledge-intensive reasoning. Central to this approach is the selection of appropriate reasoning paths in the KG. Yet, existing methods face a common limitation: reasoning path selection is often performed by separate modules using criteria that are only weakly connected to the reasoning requirements. This often results in selecting incorrect relations or premature pruning of relevant paths. We propose Search-on-Graph (SoG), a method that strengthens the connection between path selection and reasoning by having the LLM itself select which relations to follow, informed by both the available KG structure and the complete reasoning history. SoG follows an \textit{observe-think-navigate} paradigm: at each step, the LLM observes the relational connections available at the current entity, reasons about which path best advances toward answering the question, and navigates accordingly. This context-aware navigation fully exploits the LLM's reasoning capabilities rather than relying on independent selection modules with surrogate criteria. Experiments on six knowledge graph question answering (KGQA) benchmarks demonstrate that SoG outperforms state-of-the-art methods while requiring no task-specific fine-tuning and generalizing across different KG schemas.

</details>

---
