# cs.CR | Cryptography and Security | 2026-08-05

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/SkillSentry_Adaptive_Honey_Worlds_for_Dynamic_Safety_Testing_of_Agent_Skills|SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills]]

![[assets/2608.03485_figure.png|800]]

- **arXiv**: [2608.03485](https://arxiv.org/abs/2608.03485)
- **PDF**: https://arxiv.org/pdf/2608.03485
- **详细分析**: [[20_Research/Papers/大模型/SkillSentry_Adaptive_Honey_Worlds_for_Dynamic_Safety_Testing_of_Agent_Skills|SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills]]
- **作者**: Nizhang Li, Zonghao Ying, Xiangfan Wu, Zonglei Jing, Xixun Lin, Hao Zhang, Wenxin Zhang, Jiaye Lin, Quanchen Zou, Xiangzheng Zhang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《SkillSentry: Adaptive Honey Worlds for Dynamic Safety Testing of Agent Skills》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HarmfulSkillBench, MalSkillBench, SkillTrustBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

External skills extend the capabilities of large language model agents, but also introduce an execution-time attack surface: a skill that appears benign under inspection may reveal harmful behavior only after particular environmental states, resources, or interaction histories are encountered. Existing scanners primarily rely on static analysis, predefined rules, or one-shot semantic judgments, making such conditional behavior difficult to elicit and attribute. We present SkillSentry, a dynamic safety-testing framework based on adaptive honey worlds. SkillSentry infers the intended capability boundary of a skill, constructs an LLM-simulated environment with controlled decoy resources, and adaptively generates tasks to explore its behavioral states. It then compares skill-enabled trajectories with matched no-skill executions, grounding suspicious behaviors in source code and verified execution traces before making a final decision. We evaluate SkillSentry against seven scanner configurations. SkillSentry achieves 99.50% Recall and 96.26% average F1 on standard benchmarks. Under semantics-preserving evasion, it reaches 92.95% average F1, compared with 80.07% for the strongest baselines. Our code is available at https://github.com/nizhangli062-jpg/SkillSentry-Adaptive-Honey-Worlds-for-Dynamic-Safety-Testing-of-Agent-Skills.

</details>

---

### [[20_Research/Papers/大模型/PolicyGuard_Prompt-Configurable_Semantic_DLP_for_LLM_Coding_Agents|PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents]]

![[assets/2608.02687_figure.png|800]]

- **arXiv**: [2608.02687](https://arxiv.org/abs/2608.02687)
- **PDF**: https://arxiv.org/pdf/2608.02687
- **详细分析**: [[20_Research/Papers/大模型/PolicyGuard_Prompt-Configurable_Semantic_DLP_for_LLM_Coding_Agents|PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents]]
- **作者**: Kyutae Park, Jungwon Kim, Daeyeol Shim
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PolicyGuard: Prompt-Configurable Semantic DLP for LLM Coding Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI coding agents accept free-form natural language prompts that may inadvertently contain credentials, personally identifiable information (PII), or proprietary business data. Existing data loss prevention (DLP) solutions rely on rigid regex patterns, model fine-tuning, or vendor-managed classifiers with limited customizability. We present PolicyGuard, a pre-model interception framework that classifies user prompts using an LLM guided by a natural language policy file. Our key contributions are: (1) the policy-as-prompt paradigm, where DLP classification criteria are defined entirely in a plaintext policy document editable by non-engineers without code changes or model retraining; (2) a sealed evaluation protocol with template-family-level data splits, hidden holdouts, and frozen test sets to rigorously assess generalization; and (3) a comprehensive empirical evaluation across 2,000 multilingual prompts demonstrating 96.5% effective block rate (EBR) with only 3.0% false positive rate (FPR) on a frozen test set of 927 prompts, and perfect 100% accuracy on a 217-prompt hidden holdout. Information-matched baseline experiments show that PolicyGuard's natural language format significantly outperforms equivalent content in JSON format (McNemar chi-squared = 31.58, p &lt; 0.001) and dramatically outperforms zero-shot classification (Cohen's h = 0.915). Cross-model portability experiments demonstrate that the same policy achieves 86.4-96.5% EBR across four different LLMs without modification.

</details>

---
