# cs.SE | Software Engineering | 2026-07-13

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Writing_Bug_Reports_for_Software_Repair_Agents_What_Information_Matters_Most|Writing Bug Reports for Software Repair Agents: What Information Matters Most?]]

![[assets/2607.09553_first_page.png|800]]

- **arXiv**: [2607.09553](https://arxiv.org/abs/2607.09553)
- **PDF**: https://arxiv.org/pdf/2607.09553
- **详细分析**: [[20_Research/Papers/大模型/Writing_Bug_Reports_for_Software_Repair_Agents_What_Information_Matters_Most|Writing Bug Reports for Software Repair Agents: What Information Matters Most?]]
- **作者**: Vincenzo Luigi Bruno, Alessandro Giagnorio, Daniele Bifolco, Leon Wienges, Massimiliano Di Penta, Gabriele Bavota
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Writing Bug Reports for Software Repair Agents: What Information Matters Most?》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Software Engineering 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software development is increasingly moving toward agentic-first workflows. This includes AI agents responsible for generating initial fixes for submitted issue reports. In this setting, issue reports are no longer merely documentation for human maintainers; they become the primary task specification for the agent. However, little is known about how such reports should be written to maximize the agent's chances of producing a correct fix. We study what makes a bug report agent-ready. Starting from the SWE-bench Verified benchmark (i.e., a collection of 500 real repository issues with human-written gold patches and test suites for evaluating generated fixes) we manually classify each issue by change type (e.g., bug fix vs refactoring) and annotate each sentence with its information type, such as observed behavior, expected behavior, reproduction steps, localization cues, and suggested fixes. We focus on the 441 issues representing bug reports, and we run on them mini-swe-agent using three LLM backbones (i.e., GPT-5-mini, MiniMax M2.5, and Gemini 3 Flash). We then fit a binomial regression model to estimate the incremental association between each information type and agent success, controlling for confounding factors. Our results suggest that agentic-first reports benefit most from information that narrows the agent's search and repair space. Localization cues, such as references to affected code areas, are positively associated with successful repairs, while suggested fixes, expressed either in code or natural language, show some of the strongest positive associations with pass probability. An ablation study removing selected information types confirms that agents benefit less from information traditionally useful to humans, such as reproduction steps, and more from sentences that expose a repair direction, either through bug localization or a suggested fix.

</details>

---

### [[20_Research/Papers/大模型/Balancing_Usefulness_and_Naturalness_An_LLM-based_Curation_Pipeline_for_Code_Review_Comments|Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments]]

![[assets/2607.09524_figure.png|800]]

- **arXiv**: [2607.09524](https://arxiv.org/abs/2607.09524)
- **PDF**: https://arxiv.org/pdf/2607.09524
- **详细分析**: [[20_Research/Papers/大模型/Balancing_Usefulness_and_Naturalness_An_LLM-based_Curation_Pipeline_for_Code_Review_Comments|Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments]]
- **作者**: Oussama Ben Sghaier, Martin Weyssow, Houari Sahraoui
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code review is a cornerstone of software development, where reviewers provide feedback through written comments to ensure code quality, maintainability, and correctness. The effectiveness of this process hinges on the quality of review comments. As large language models (LLMs) gain traction in automating code review tasks, the utility of these systems is directly limited by the quality of the datasets on which they are trained. Unfortunately, existing code review datasets are often noisy, inconsistent, or poorly structured, which hinders the ability of LLMs to learn to generate accurate, helpful, and human-like review comments. To overcome these limitations, we propose two different curation pipelines designed to improve both the quality and the utility of large-scale code review datasets. In the first pipeline, all review comments are systematically reformulated by an LLM to improve their clarity, conciseness, and civility while preserving their semantic intent. The curated dataset resulting from this approach, called CuREV, offers cleaner, higher-quality, and easier-to-learn-from comments that lead to measurable improvements in downstream automation tasks, namely review comment generation and code refinement. Building on this, we propose an improved pipeline, guided by high-quality exemplars, that enhances the realism and diversity of curated review comments. This method first separates the dataset into high-quality and low-quality reviews, based on a systematic quality assessment using an evaluation framework. High-quality comments are preserved in their original form and further used as in-context exemplars to inspire the reformulation of low-quality comments. By varying the exemplars provided, the reformulated comments are not only clearer and more actionable but also exhibit a broader range of writing styles, making them more realistic and human-like.

</details>

---

### [[20_Research/Papers/大模型/Exploring_the_Potential_of_Program_Flowcharts_on_Code_Generation_Using_Multimodal_LLMs|Exploring the Potential of Program Flowcharts on Code Generation Using Multimodal LLMs]]

![[assets/2607.09146_figure.png|800]]

- **arXiv**: [2607.09146](https://arxiv.org/abs/2607.09146)
- **PDF**: https://arxiv.org/pdf/2607.09146
- **详细分析**: [[20_Research/Papers/大模型/Exploring_the_Potential_of_Program_Flowcharts_on_Code_Generation_Using_Multimodal_LLMs|Exploring the Potential of Program Flowcharts on Code Generation Using Multimodal LLMs]]
- **作者**: Yuki Toi, Tao Xiao, Kazushi Tomoto, Masanari Kondo, Yasutaka Kamei
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Exploring the Potential of Program Flowcharts on Code Generation Using Multimodal LLMs》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, Large Language Models (LLMs) have made significant strides, leading to the emergence of multimodal LLMs capable of processing diverse inputs such as images and audio. Previous research indicates that the supply of multimodal LLMs with combined textual and visual information improves the automatic code generation capabilities. In software development, diagrams such as flowcharts are widely employed to facilitate tasks like code comprehension. While existing studies investigated the impact of visual inputs on LLMs and the usage of software diagrams, the potential influence of providing flowcharts on multimodal LLM performance remains underexplored. In this study, we generated flowcharts from example solution code for AtCoder problems and provided these visual aids alongside problem statements to GPT-4o for code generation. Our findings demonstrate that integrating flowcharts with problem statements yields performance improvements of up to 10%. Furthermore, when employing abstracted flowcharts, we observed a trend indicating that increasing levels of flowchart detail correlate with enhanced performance. Additionally, we compared the effectiveness of flowchart provision to Few-Shot Learning approaches. The findings suggest that one-shot learning provides sustainable improvements, whereas two-shot learning results in only minor improvements. Our work highlights the importance of software diagrams in supporting multimodal LLM-driven code generation.

</details>

---

### [[20_Research/Papers/大模型/Multi-Agent_LLM_Collaboration_for_Unit_Test_Generation_via_Human-Testing-Inspired_Workflows|Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows]]

![[assets/2607.09101_figure.png|800]]

- **arXiv**: [2607.09101](https://arxiv.org/abs/2607.09101)
- **PDF**: https://arxiv.org/pdf/2607.09101
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_LLM_Collaboration_for_Unit_Test_Generation_via_Human-Testing-Inspired_Workflows|Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows]]
- **作者**: Quanjun Zhang, Ye Shang, Siqi Gu, Jianyi Zhou, Chunrong Fang, Zhenyu Chen, Liang Xiao
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, the emergence of Large Language Models (LLMs) has spurred a surge of research into automated unit test generation, yielding impressive performance and reducing manual effort. However, existing LLM-based approaches still suffer from two major limitations: (1) they follow rigid, procedural workflows that underutilize the autonomous reasoning potential of LLMs, making it difficult to dynamically adapt testing strategies based on real-time feedback; and (2) they rely on rule-based context extraction that is not tailored to test generation, failing to capture fine-grained code dependencies and test-specific knowledge required for deriving test requirements. In this paper, we propose TestAgent, an LLM-based test generation approach that addresses the above limitations by emulating human testing practices via a multi-agent collaboration mechanism. Particularly, TestAgent designs three specialized agents, namely a requirement planner, a test generator, and a test reviewer, to simulate how developers understand, construct, and validate unit tests. To unleash the autonomous capabilities of LLMs, we equip TestAgent with a set of tool APIs that can be invoked dynamically in an on-demand and adaptive manner. To further support repository-level reasoning, TestAgent constructs a test-specialized knowledge graph via static analysis, which captures code entities and their dependencies across the project and persistently stores testing artifacts (e.g., test reports and failure analyses) produced during generation. Experimental results show that TestAgent achieves 97.46% execution rate, 92.34% line coverage, 90.24% branch coverage, and 83.69% mutation score on six Java projects, outperforming LLM-based baselines across all metrics and achieving substantially higher mutation scores than search-based tools.

</details>

---

### [[20_Research/Papers/大模型/Better_Harnesses,_Smaller_Models_Building_90%_Cheaper_Agents_via_Automated_Harness_Adaptation|Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation]]

![[assets/2607.08938_figure.png|800]]

- **arXiv**: [2607.08938](https://arxiv.org/abs/2607.08938)
- **PDF**: https://arxiv.org/pdf/2607.08938
- **详细分析**: [[20_Research/Papers/大模型/Better_Harnesses,_Smaller_Models_Building_90%_Cheaper_Agents_via_Automated_Harness_Adaptation|Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation]]
- **作者**: Chenyang Yang, Xinran Zhao, Tongshuang Wu, Christian Kästner
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier LLM agents are automating many business tasks, but their high inference cost makes large-scale deployment unsustainable. Small language models (SLMs) offer a cheaper alternative, yet they typically fall short when swapped into a harness designed for a frontier LLM. We show that for many routine business tasks, SLM agents can match LLM performance at 90% lower cost, when paired with an adapted harness that can be automatically discovered by a meta agent. The key insight is that much of the task difficulty is shared across instances and can be lifted from the model into the harness via tailored instructions, tools, and orchestration loops. To study this systematically, we create a framework that maps agent failure modes to harness adaptation strategies, and build a harness optimizer that automatically discovers effective adaptations from failure trajectories. Across seven business-oriented agentic tasks and three SLM families, we found optimized harnesses significantly improve performance on 16 of 21 task-SLM pairs, with seven pairs closing the SLM-LLM performance gap and the best SLM agent recovering 89.7% of LLM performance at 4% of the cost. Our analysis further shows that adaptation works best for tasks with more repetitive workflows and for SLMs with sufficient base capabilities. Together, these results suggest that harness adaptation can expand the practical deployment range of SLM agents in routine business tasks.

</details>

---
