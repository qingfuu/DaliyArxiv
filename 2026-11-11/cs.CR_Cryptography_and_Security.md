# cs.CR | Cryptography and Security | 2026-11-11

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/BypassGym_A_Benchmark_for_Evaluating_AI_Agents'_Endpoint_Defense_Evasion_Capabilities|BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities]]

![[assets/2611.13684_figure.png|800]]

- **arXiv**: [2611.13684](https://arxiv.org/abs/2611.13684)
- **PDF**: https://arxiv.org/pdf/2611.13684
- **详细分析**: [[20_Research/Papers/大模型/BypassGym_A_Benchmark_for_Evaluating_AI_Agents'_Endpoint_Defense_Evasion_Capabilities|BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities]]
- **作者**: Weifeng Yuan, Zifan Chen, Yucheng Zhang, Feng Dong, Peng Gao, Haoyu Wang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《BypassGym: A Benchmark for Evaluating AI Agents' Endpoint Defense Evasion Capabilities》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoPenBench, BypassGym, CyberGym, CyberSecEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial intelligence agents increasingly automate cybersecurity tasks, including offensive operations. Frequent attacks across the web make endpoint detection and response (EDR) a critical defense, but whether AI agents can evade it remains unclear. Benchmarks evaluate the offensive capabilities of large language model (LLM) agents in areas such as penetration testing and vulnerability discovery. One important capability that these benchmarks do not address is defense evasion, specifically whether an agent can develop a program that executes a payload without being blocked or terminated by a deployed EDR. We introduce BypassGym, to our knowledge the first benchmark to systematically evaluate this capability on real endpoints. Given command-and-control (C2) shellcode, an agent must generate and compile a loader that executes the payload without being blocked or terminated. A supplementary evasion knowledge skill provides domain knowledge and supports comparisons with and without this input. BypassGym is built on Proxmox VE(PVE), so the evaluation environment runs real Windows systems and EDR products inside virtual machines and returns structured detection feedback to the agent. We evaluate 5 lightweight model backends against 6 EDR products and 3 payloads, and find that even these simple models generate successful submissions, with DeepSeek-V4.1 Flash reaching 17/18 successful runs and Bitdefender allowing only 5 of 15 runs to pass. These results provide a systematic measurement of current AI agents' endpoint defense evasion capabilities and identify areas for defenders to investigate.

</details>

---
