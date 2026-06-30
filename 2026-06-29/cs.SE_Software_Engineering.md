# cs.SE | Software Engineering | 2026-06-29

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/Humanizing_Automatically_Generated_Unit_Test_Suites_with_LLM-Based_Refactoring|Humanizing Automatically Generated Unit Test Suites with LLM-Based Refactoring]]

![[assets/2606.28229_figure.png|800]]

- **arXiv**: [2606.28229](https://arxiv.org/abs/2606.28229)
- **PDF**: https://arxiv.org/pdf/2606.28229
- **详细分析**: [[20_Research/Papers/大模型/Humanizing_Automatically_Generated_Unit_Test_Suites_with_LLM-Based_Refactoring|Humanizing Automatically Generated Unit Test Suites with LLM-Based Refactoring]]
- **作者**: Wendkûuni C. Ouédraogo, Yinghua Li, Xueqi Dang, Paweł Borsukiewicz, Lingfeng Bao, Anil Koyuncu, Jacques Klein, David Lo, Tegawendé F. Bissyandé
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《Humanizing Automatically Generated Unit Test Suites with LLM-Based Refactoring》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Search-based test generation tools such as EvoSuite produce compilable and high-coverage unit tests at scale, but their suites are often hard to read and maintain. LLMs can generate more natural tests, yet direct generation remains brittle, with compilation rates of only 51-78% in our study. We introduce TestHumanizer, a hybrid SBST+LLM approach that uses LLMs as controlled refactoring layers over compilable SBST suites to improve naming, structure, and developer-oriented clarity while preserving behavior and compilation validity. We evaluate TestHumanizer on 350 classes from Defects4J and SF110. EvoSuite generates 15 suites per class, and each suite is refactored under three context configurations using gpt-4o and mistral-large-2407, yielding 31,500 refactorings. TestHumanizer reaches 88-98% compilation rates, close to EvoSuite's 100% baseline and clearly above direct LLM generation. Structural coverage is largely preserved, typically within 1-2 percentage points, and 86-95% of refactorings satisfy a composite faithful-refactoring threshold. Refactored suites also improve predicted readability, reduce control-flow and cognitive complexity, and mitigate structural smells. The summary-based setting offers the most robust trade-off, while long code-centric prompts are more prone to hallucination-induced failures. A developer study on 30 classes and 444 test methods confirms significant gains in perceived readability and willingness to adopt, with Wilcoxon p less than 0.01 and substantial inter-rater agreement. Overall, LLMs are most effective not as standalone generators but as validation-gated refinement layers over robust SBST outputs.

</details>

---

### [[20_Research/Papers/强化学习/BashCoder-R1_Towards_Robust_and_Explainable_Bash_Code_Generation_with_Robustness-Aware_Group_Relative_Policy_Optimization|BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization]]

![[assets/2606.27733_figure.png|800]]

- **arXiv**: [2606.27733](https://arxiv.org/abs/2606.27733)
- **PDF**: https://arxiv.org/pdf/2606.27733
- **详细分析**: [[20_Research/Papers/强化学习/BashCoder-R1_Towards_Robust_and_Explainable_Bash_Code_Generation_with_Robustness-Aware_Group_Relative_Policy_Optimization|BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization]]
- **作者**: Lei Yu, Peng Wang, Jia Xu, Jingyuan Zhang, Xin Wang, Jiajia Ma, Li Yang, Changzhi Deng, Zenghua Wang, Fengjun Zhang
- **cs 子类**: cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《BashCoder-R1: Towards Robust and Explainable Bash Code Generation with Robustness-Aware Group Relative Policy Optimization》归入 强化学习 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BashBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bash scripts are the cornerstone of system administration and DevOps automation, where code quality directly impacts system stability and security. In automated Bash script generation using Large Language Models (LLMs), two interconnected failures emerge: unauditable "black box" reasoning and critical robustness vulnerabilities in generated code. To address both, we propose BashCoder-R1, a novel framework for robust and explainable Bash script generation. Our pipeline combines: (1) Continual Pre-training (CPT) to specialize the model on Bash paradigms; (2) Long Chain-of-Thought Supervised Fine-Tuning (L-CoT SFT) on expert-validated reasoning-and-code samples to emulate proactive risk-aware thinking; and (3) Robustness-Aware Group Relative Policy Optimization (R-GRPO), a reinforcement learning phase optimizing a weighted reward for syntax correctness, robustness (via shellcheck), and format correctness. We evaluate on BashBench, a new benchmark of 952 real-world tasks (773 single-line, 179 multi-line). BashCoder-R1 achieves SyntaxPass (100.00%/94.97%), RobustWarnRate (4.01%/16.47%), RobustPass (95.99%/79.33%), FuncRate (93.01%/93.85%), and FullRate (90.04%/73.18%) for single-line/multi-line tasks, outperforming the strongest baseline DeepSeek-V3.2 (Reasoning) by 37.82% and 20.18% in FullRate. Human evaluation on Functionality, Robustness, and Clarity further confirms BashCoder-R1 achieves the highest quality ratings.

</details>

---

### [[20_Research/Papers/大模型/LLM-Assisted_Model-Based_GUI_Testing_for_Vue.js_Web_Applications|LLM-Assisted Model-Based GUI Testing for Vue.js Web Applications]]

![[assets/2606.27665_figure.png|800]]

- **arXiv**: [2606.27665](https://arxiv.org/abs/2606.27665)
- **PDF**: https://arxiv.org/pdf/2606.27665
- **详细分析**: [[20_Research/Papers/大模型/LLM-Assisted_Model-Based_GUI_Testing_for_Vue.js_Web_Applications|LLM-Assisted Model-Based GUI Testing for Vue.js Web Applications]]
- **作者**: Tao Li, Chenhui Cui, Rubing Huang, Dave Towey, Shikai Guo, Lei Ma
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM-Assisted Model-Based GUI Testing for Vue.js Web Applications》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vue.js is a popular framework for building modern web applications. As Vue.js functionality and tooling support grow, ensuring its reliability (through automated testing) is becoming increasingly important. Although model-based testing has been successfully used to automate graphical user interface (GUI) testing on other platforms, its application to Vue.js remains challenging: Transition candidates, which are spread across router configurations and single-file components (SFCs), must be concretized and normalized into an executable page transition graph (PTG) for testing. To address this, we propose the LLMVue framework, which uses a large language model (LLM) to generate a PTG from Vue.js source code. LLMVue infers component hierarchies and route transitions, merging them into a unified PTG across multiple SFCs. We evaluated LLMVue on a collection of ten open-source Vue.js projects from GitHub, using GPT-4o as the LLM backbone. The constructed graphs demonstrate high precision and recall, with low graph edit distance. LLMVue -guided testing also significantly improves the coverage and exploration efficiency, compared to a random exploration baseline (with the same time constraints). To the best of our knowledge, this is the first use of LLMs for model-based GUI testing of Vue.js applications using source-level PTG extraction.

</details>

---

### [[20_Research/Papers/大模型/Glite_ARF_Verifier-Driven_Research_with_Parallel_LLM_Coding_Agents|Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents]]

![[assets/2606.27416_figure.png|800]]

- **arXiv**: [2606.27416](https://arxiv.org/abs/2606.27416)
- **PDF**: https://arxiv.org/pdf/2606.27416
- **详细分析**: [[20_Research/Papers/大模型/Glite_ARF_Verifier-Driven_Research_with_Parallel_LLM_Coding_Agents|Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents]]
- **作者**: Vassili Philippov, Pavel Katunin, Dmitry Andreev, Igor Ostanin, Anton Nikolaev
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, MLAgentBench, MLE-Bench, MLR-Bench, Scientist-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM coding agents make it tempting to automate empirical research by delegating experiments to them directly, but naive delegation does not scale to large projects: low-rate instruction lapses compound into broken, irreproducible artefacts. To address this problem, we present Glite ARF, an open-source Python framework for running many LLM coding agents in parallel on a research repository without sacrificing reproducibility or auditability. The framework defines a three-role stack: a human researcher chooses which hypotheses to test, coding agents (Claude Code, Codex CLI) implement individual tasks under a fixed structure, and deterministic Python verifier scripts enforce task isolation, immutability of completed work, a corrections overlay, and a materialised project overview. We call this verifier-driven research: the rules of the research process live in code that fails loudly when violated, not in prose that agents are merely asked to follow. Using Glite ARF, we developed our submission to the BEA 2026 vocabulary-difficulty shared task, placing first in the closed track and second in the open track on all three target languages (Spanish, German, Mandarin) and reducing the official baseline RMSE by 29.9% (closed) and 35.9% (open). The campaign comprised 273 tracked tasks (146 experiment runs) across 129 feature sets, run by up to twelve parallel agents orchestrated from a single laptop - with some model training on rented A100s - at approximately \$450 in LLM API spend (\$498 total third-party cost), and structured per-fold provenance let us catch and strip four target-leaking feature sets, correcting an implausible 0.609 RMSE to 0.802. Across three campaigns in three domains, the framework's structural machinery adds only about 1% of wall-clock time. Framework and a public demo project accompany this paper.

</details>

---
