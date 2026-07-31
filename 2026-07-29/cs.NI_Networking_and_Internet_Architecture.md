# cs.NI | Networking and Internet Architecture | 2026-07-29

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/C-RE-ACT_Causal_RE-ACTing_Agent_for_O-RAN_Forensic_Triage|C-RE-ACT: Causal RE-ACTing Agent for O-RAN Forensic Triage]]

![[assets/2607.25828_figure.png|800]]

- **arXiv**: [2607.25828](https://arxiv.org/abs/2607.25828)
- **PDF**: https://arxiv.org/pdf/2607.25828
- **详细分析**: [[20_Research/Papers/大模型/C-RE-ACT_Causal_RE-ACTing_Agent_for_O-RAN_Forensic_Triage|C-RE-ACT: Causal RE-ACTing Agent for O-RAN Forensic Triage]]
- **作者**: Pau Baguer, J. Xavier Salvat Lozano, Gines Garcia-Aviles, Xavier Costa-Pérez
- **cs 子类**: cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《C-RE-ACT: Causal RE-ACTing Agent for O-RAN Forensic Triage》归入 大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GraphQA, O-CIQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The shift to O-RAN architectures marks a turning point in cellular security, where increased openness and modularity directly translate into a broader attack surface. Among the security threats cataloged by the O-RAN Alliance Working Group 11, performance-degradation attacks constitute the largest class. These attacks induce packet losses and latency spikes that are hard to distinguish from operational events such as misconfigurations, transient congestion, or software regressions. Consequently, upon an adverse incident detection, support engineers must rapidly determine whether to route the corresponding incident ticket to network maintenance or escalate it to security operations. This triage phase represents a critical human-in-the-loop bottleneck in the incident response lifecycle. To address this vulnerability, we introduce C-RE-ACT (Causal RE-ACTing agent), an automated agentic triage framework designed to generate actionable incident reports. C-RE-ACT starts constructing a Weighted Directed Acyclic Graph (WDAG) over O-RAN metrics using the Structural Agnostic Model (SAM). The resulting causal topology is encoded into a continuous soft token via a Graph Isomorphism Network (GIN) aligned with the language space of the Large Language Model (LLM) powering a ReAct agent. We evaluate C-RE-ACT on a physical, O-RAN-compliant testbed across 140 distinct performance-degradation experiments. Empirical results demonstrate the causal ranking isolates the correct root cause within the top three candidates in 89% of instances. Furthermore, graph soft-prompting improves LLM accuracy on causal-topology queries from 0.22 (text-only baseline) to 0.72. The autonomous agent achieves anomaly classification accuracies of 83% for delay anomalies and 84% for packet-loss anomalies.

</details>

---
