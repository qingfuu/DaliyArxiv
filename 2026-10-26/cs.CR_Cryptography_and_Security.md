# cs.CR | Cryptography and Security | 2026-10-26

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/On_Task,_Off_Track_Benchmarking_LLM_and_Agent_Robustness_to_Near-Target_Prompt_Injection|On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection]]

![[assets/2610.32531_figure.png|800]]

- **arXiv**: [2610.32531](https://arxiv.org/abs/2610.32531)
- **PDF**: https://arxiv.org/pdf/2610.32531
- **详细分析**: [[20_Research/Papers/大模型/On_Task,_Off_Track_Benchmarking_LLM_and_Agent_Robustness_to_Near-Target_Prompt_Injection|On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection]]
- **作者**: Yuyang Gong, Zihao Wang, Jiawei Liu, XiaoFeng Wang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：NTBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Prompt injection benchmarks assess whether large language models (LLMs) and agents resist malicious instructions embedded in external content. However, a system could perform well by rejecting attacks that obviously abandon the user's request, while still accepting changes that retain most of a legitimate answer but make it incorrect or harmful. Testing more instructions for unrelated outcomes would not necessarily reveal this weakness. We call attacks seeking responses designed to resemble legitimate answers while introducing incorrect or harmful changes near-target prompt injection. We introduce NTBench, the Near-Target Benchmark, which builds on legitimate tasks from existing datasets. For each task, a legitimate reference outcome guides the generation of target--instruction pairs, with separate tracks targeting incorrect and harmful outcomes in responses or agent tool invocations. Harmful targets can also accompany otherwise correct task completion. We combine LLM-based checks with human validation of the intended deviations, then assess whether injected instructions induce them using response judgments or tool-call checks, excluding deviations already observed without injection. We evaluate seven LLMs on ten datasets for language tasks and two agent benchmarks. Under a common budget of three attack executions per sample, both tracks achieve higher overall attack success rates than the fixed-target baseline for every evaluated model in each setting. On language tasks, the increases range from 9.3 to 35.8 percentage points for incorrect targets and 1.7 to 17.3 percentage points for harmful targets. These results show that resistance to the tested fixed-target attacks does not imply resistance to related incorrect or harmful outcomes, and that reference-guided targets broaden the failures revealed by robustness evaluation.

</details>

---

### [[20_Research/Papers/机器人/Not_an_Accident_Exploiting_Safety_Filter_Inadequacy_in_Humanoid_Robots|Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots]]

![[assets/2610.31923_figure.png|800]]

- **arXiv**: [2610.31923](https://arxiv.org/abs/2610.31923)
- **PDF**: https://arxiv.org/pdf/2610.31923
- **详细分析**: [[20_Research/Papers/机器人/Not_an_Accident_Exploiting_Safety_Filter_Inadequacy_in_Humanoid_Robots|Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots]]
- **作者**: Tiffany Bao, Shangtao Li, Yifan Sun, Mengwen He, Bowei Li, Alden Wang, Changliu Liu, Ruoyu Wang, David Brumley
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: cs.CR

#### 研究背景与动机

《Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As humanoid robots move from research laboratories toward deployment in human-centered environments such as homes, hospitals, and warehouses, safe operation around nearby people and objects becomes a fundamental requirement. Safety filters have emerged as a promising technique to address this challenge by providing mathematical guarantees that generated control actions do not result in collisions. This paper shows that these guarantees hold only when the safety parameters are configured correctly. However, correct parameter configurations are task- and environment-specific, and no general method exists to determine them across diverse deployments. As a result, safety filters shipped with humanoid robots can fail after deployment in specific scenarios. We show that attackers can exploit these failures through only normal user interactions without any additional privileges or capabilities. To demonstrate this risk, we present goal insertion attacks and develop SIREN, an automated tool that identifies vulnerable inserting goals for a given task and environment. Experimental results show that SIREN identifies attacks in all vulnerable scenarios in the SPARK dataset. Compared with a baseline approach, SIREN discovers three times as many attacks. We also show that SIREN is able to generate attacks against a real humanoid and cause it to collide while executing tasks. These results demonstrate that current safety filters introduce exploitable vulnerabilities that can cause safety violations, which reveals that existing safety mechanisms can themselves become a source of safety risk for humanoid robots.

</details>

---
