# cs.SE | Software Engineering | 2026-06-15

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/FastContext_Training_Efficient_Repository_Explorer_for_Coding_Agents|FastContext: Training Efficient Repository Explorer for Coding Agents]]

![[assets/2606.14066_figure.png|800]]

- **arXiv**: [2606.14066](https://arxiv.org/abs/2606.14066)
- **PDF**: https://arxiv.org/pdf/2606.14066
- **详细分析**: [[20_Research/Papers/大模型/FastContext_Training_Efficient_Repository_Explorer_for_Coding_Agents|FastContext: Training Efficient Repository Explorer for Coding Agents]]
- **作者**: Shaoqiu Zhang, Maoquan Wang, Yuling Shi, Yuhang Wang, Xiaodong Gu, Yongqiang Yao, Rao Fu, Shengyu Fu
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《FastContext: Training Efficient Repository Explorer for Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FC-4B-RL, SWE-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) coding agents have achieved strong results on software engineering tasks, yet repository exploration remains a major bottleneck: locating relevant code consumes substantial token budget and pollutes the agent's context with irrelevant snippets. In most agents, the same model explores the repository and solves the task, leaving exploratory reads and searches in the solver's history. We present FastContext, a dedicated exploration subagent that separates repository exploration from solving. Invoked on demand, FastContext issues parallel tool calls and returns concise file paths and line ranges as focused context. FastContext is powered by specialized exploration models spanning 4B--30B parameters. We bootstrap them from strong reference-model trajectories and refine them with task-grounded rewards for broad first-turn search, multi-turn evidence gathering, and precise citation generation. Across SWE-bench Multilingual, SWE-bench Pro, and SWE-QA, integrating FastContext into Mini-SWE-Agent improves end-to-end resolution rates up to 5.5\% while reducing coding-agent token consumption up to 60\%, with marginal overhead. These results show that repository exploration can be separated from solving and handled effectively by specialized models. Code and data: https://github.com/microsoft/fastcontext

</details>

---

### [[20_Research/Papers/大模型/LLM_Agents_Can_See_Code_Repositories|LLM Agents Can See Code Repositories]]

![[assets/2606.14061_figure.png|800]]

- **arXiv**: [2606.14061](https://arxiv.org/abs/2606.14061)
- **PDF**: https://arxiv.org/pdf/2606.14061
- **详细分析**: [[20_Research/Papers/大模型/LLM_Agents_Can_See_Code_Repositories|LLM Agents Can See Code Repositories]]
- **作者**: Dongjian Ma, Silin Chen, Yufei Yang, Yulin Shi, Yanfu yan, Xiaodong Gu
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《LLM Agents Can See Code Repositories》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SWE-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents powered by large language models have demonstrated strong performance on software engineering tasks. Yet most agents consume repositories almost entirely as text, which differs from how human developers use visual structure such as folder hierarchies and dependency relationships to orient themselves in large codebases. With multimodal large language models (MLLMs), it is an open question whether agents can effectively benefit from visual representations of repositories. This paper presents the first systematic empirical study of visual repository representations for LLM-based agents on repository-level issue resolution. We evaluate four recent multimodal models. Our results show that a strictly vision-only setup degrades accuracy and increases token cost, because agents lack sufficient symbolic detail and compensate with repeated visual queries. In contrast, integrating visual graphs of repository structure as a supplementary modality alongside standard text interfaces helps agents understand structure more efficiently: input token consumption decreases by up to 26% while issue-resolution accuracy is maintained or improved. Visualization is most useful during fault localization and when the agent autonomously controls exploration depth. These findings point to a practical hybrid text-and-vision design for next-generation coding agents.

</details>

---
