# cs.CR | Cryptography and Security | 2026-11-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Authorization_Drift_in_LLM_Agents_Evaluating_Boundary_Compliance_in_Multi-Step_Tool_Use|Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use]]

![[assets/2611.09113_figure.png|800]]

- **arXiv**: [2611.09113](https://arxiv.org/abs/2611.09113)
- **PDF**: https://arxiv.org/pdf/2611.09113
- **详细分析**: [[20_Research/Papers/大模型/Authorization_Drift_in_LLM_Agents_Evaluating_Boundary_Compliance_in_Multi-Step_Tool_Use|Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use]]
- **作者**: Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, Jinluan Yang, Haoran Li, Yike Guo, Sirui Han
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, AgentBench, AppWorld, EU-Agent-Bench, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmark validation in real agent rollouts rather than LLM self-critique. Across 13 LLMs and three frameworks (25,207 trajectories), greater capability accompanies greater drift, with frontier-capable models exhibiting drift rates of 0.43 to 0.61. Yet 86.18% of tasks admit an observed clean-success trajectory, showing that drift is avoidable. Drift is persistent and dominated by early data over-collection; apparent improvements under agentic scaffolds coincide with collapsing clean-completion performance. To understand potential harms to individuals and society, we map drift points to legal provisions across four jurisdictions, connecting overreach to privacy and information-security concerns. Data minimisation is the most frequently implicated provision, and 93.5% of legally grounded drifting runs map to multiple jurisdictions, making the potential consequences of authorization drift more interpretable.

</details>

---
