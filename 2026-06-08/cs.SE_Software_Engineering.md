# cs.SE | Software Engineering | 2026-06-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/QBugLM_An_Agentic_Benchmarking_Framework_for_LLM-based_Quantum_Software_Debugging|QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging]]

![[assets/2606.07314_figure.png|800]]

- **arXiv**: [2606.07314](https://arxiv.org/abs/2606.07314)
- **PDF**: https://arxiv.org/pdf/2606.07314
- **详细分析**: [[20_Research/Papers/大模型/QBugLM_An_Agentic_Benchmarking_Framework_for_LLM-based_Quantum_Software_Debugging|QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging]]
- **作者**: An B. B. Pham, Hoa T. Nguyen, Muhammad Usman
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《QBugLM: An Agentic Benchmarking Framework for LLM-based Quantum Software Debugging》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval, QHackBench, QuanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantum software bugs often yield silent, incorrect outputs rather than explicit errors, making them particularly difficult to detect and repair with conventional techniques. Although large language models (LLMs) have shown strong performance on classical software engineering tasks, their ability to debug quantum code remains largely unexplored. To bridge this gap, we propose QBugLM, a multi-agent framework that automates the quantum software debugging pipeline, from taxonomy-driven bug injection to LLM-based detection and repair, and finally to simulation-based validation, for framework-agnostic OpenQASM 3.0 programs. We further conduct a comprehensive case study using QBugLM to benchmark two LLMs, Claude 4.6 Sonnet and Qwen3 Coder Next, across different prompting strategies, bug categories, and quantum programs. Our results show that iterative feedback is critical, as a single retry raises Pass@1 from below 25% to above 80%. Moreover, simpler structured prompting can even outperform Chain-of-Thought and ReAct for reasoning-capable models under fixed-resource constraints. Our work takes initial steps toward benchmarking LLM capabilities for debugging quantum programs and offers practical insights to support future efforts in automated quantum software repair.

</details>

---
