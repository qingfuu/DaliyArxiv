# cs.SE | Software Engineering | 2026-07-15

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/MetaInfer_A_Knowledge_Only_LLM_Inference_Engine_Generator_SKILL_Toolbox|MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox]]

![[assets/2607.12875_figure.png|800]]

- **arXiv**: [2607.12875](https://arxiv.org/abs/2607.12875)
- **PDF**: https://arxiv.org/pdf/2607.12875
- **详细分析**: [[20_Research/Papers/大模型/MetaInfer_A_Knowledge_Only_LLM_Inference_Engine_Generator_SKILL_Toolbox|MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox]]
- **作者**: Zhenwen Miao, Honglin Wang, Mingheng Mi
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GatedDeltaNet, KernelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLM technology advances, the space of model families, compute hardware, quantization schemes, parallelization strategies, and specialized optimization kernels continues to expand, sharply increasing the code complexity and maintenance cost of general-purpose inference frameworks. Conventional software engineering uses multiple layers of abstraction to support diverse application scenarios, but these abstractions also increase system complexity and may introduce additional performance overhead. This paper presents metainfer, an 'LLM-as-Compiler' approach in which users specify only the runtime constraints of an inference program. An LLM-driven multi-agent collaboration system, coupled with a contract knowledge base, then automatically generates a compact customized inference framework that satisfies these constraints. We evaluate metainfer from three perspectives: the effect of source-code reference, the runtime behavior and performance profile of engines generated under the zero-reference constraint on CKB-covered targets, and knowledge-base evolution for new model and platform scenarios. The results show that metainfer organizes generation constraints, validation feedback, and knowledge consolidation into a continuous closed loop, enabling runnable customized inference solutions to be generated from explicit knowledge. The code is publicly available at https://github.com/MetaInfer/MetaInfer.

</details>

---

### [[20_Research/Papers/其他/Beyond_Test_Presence_Assessing_the_Quality_and_Robustness_of_Agent-Generated_Tests_in_Open-Source_Projects|Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects]]

![[assets/2607.12068_figure.png|800]]

- **arXiv**: [2607.12068](https://arxiv.org/abs/2607.12068)
- **PDF**: https://arxiv.org/pdf/2607.12068
- **详细分析**: [[20_Research/Papers/其他/Beyond_Test_Presence_Assessing_the_Quality_and_Robustness_of_Agent-Generated_Tests_in_Open-Source_Projects|Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects]]
- **作者**: Preet Jhanglani, Zeel Kaushal Desai, Vidhi Kansara, Eman Abdullah AlOmar
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted. While these agents successfully automate the test generation, current evaluation benchmarks (e.g., SWE-bench) largely focus on pass-rates rather than the intrinsic quality of the generated tests. This raises the possibility of "stealth technical debt", in which test suites pass execution but do not offer comprehensive coverage or semantic value. We address this methodological gap through a large-scale, empirical comparison of 204,673 test artifacts which comprises of 24,941 human-authored files and 179,732 agent-generated files; sourced from the AIDev dataset. Using the Abstract Syntax Tree (AST) parsing with Python's naive ast module, we implemented a "white-box" static analysis framework to evaluate three quality dimensions: Assertion Strength (RQ1), Edge-Case Coverage (RQ2), and Flakiness Potential (RQ3). Our results present a nuanced inversion of traditional assumptions. AI agents performed better than humans in Edge-Case Coverage, with almost twice the variety of boundary checks (Variety Score: 0.62 vs 0.32) and a higher frequency of null-safety testing (13.40% vs. 8.3%), even though human developers had a slight advantage in Assertion Strength (88.1% strong assertions vs. 85.37% for agents). But this thoroughness comes at a price: due mostly to their reliance on file I/O and non-deterministic logic, agent-generated tests exhibited a higher risk of flakiness (Candidate Rate: 0.41 vs. 0.30). These findings suggest that while AI agents excel at rigorous boundary testing, they lack the "environmental awareness" needed to write stable, hermetic tests.

</details>

---

### [[20_Research/Papers/其他/Predicting_Acceptance_and_Review_Effort_in_Human_and_Agent_Pull_Requests|Predicting Acceptance and Review Effort in Human and Agent Pull Requests]]

![[assets/2607.12057_figure.png|800]]

- **arXiv**: [2607.12057](https://arxiv.org/abs/2607.12057)
- **PDF**: https://arxiv.org/pdf/2607.12057
- **详细分析**: [[20_Research/Papers/其他/Predicting_Acceptance_and_Review_Effort_in_Human_and_Agent_Pull_Requests|Predicting Acceptance and Review Effort in Human and Agent Pull Requests]]
- **作者**: Kartik Ghanshyambhai Pansuriya, Ehsan Ghorbani, Deepak Singh, Eman Abdullah AlOmar
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Predicting Acceptance and Review Effort in Human and Agent Pull Requests》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pull requests (PRs) are a central mechanism for reviewing and integrating code changes in modern software repositories. As AI coding agents begin to submit more code changes alongside human developers, maintainers face a new challenge: deciding which PRs are likely to be accepted and which ones may require substantial review effort. This paper studies whether such outcomes can be estimated at the time a PR is opened, before reviewer discussion, CI feedback, or merge decisions are available. Using the AIDev dataset, we construct a leakage-aware prediction pipeline for human- and agent-authored PRs. The feature set is limited to submission-time information, including PR text characteristics, metadata, repository context, temporal signals, and lightweight diff statistics. We evaluate classical machine-learning models, including Logistic Regression, Random Forests, Gradient Boosting, Extra Trees, and MLPs, across pooled, human-only, agent-only, and balanced contributor views. Our results show that acceptance prediction is feasible from early signals: tree-based models achieve F1 scores above 0.95, with textual clarity and metadata among the most influential predictors. Review-effort prediction is more difficult. Comment counts and time-to-merge are only modestly explained by submission-time features, suggesting that reviewer availability, project workflow, and team-specific review practices play a major role. These findings indicate that early PR models can support triage and reviewer prioritization, but should be used as advisory tools rather than automated decision-makers.

</details>

---
