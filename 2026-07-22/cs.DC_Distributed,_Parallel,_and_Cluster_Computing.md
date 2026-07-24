# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-07-22

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/InstantInfer_Enabling_Fast_LLM_Cold_Start_with_Communicating_Finite_Automata|InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata]]

![[assets/2607.18957_figure.png|800]]

- **arXiv**: [2607.18957](https://arxiv.org/abs/2607.18957)
- **PDF**: https://arxiv.org/pdf/2607.18957
- **详细分析**: [[20_Research/Papers/大模型/InstantInfer_Enabling_Fast_LLM_Cold_Start_with_Communicating_Finite_Automata|InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata]]
- **作者**: Yitao Yuan, Yongchao He, Shaoke Fang, Wenfei Wu
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《InstantInfer: Enabling Fast LLM Cold Start with Communicating Finite Automata》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cold starts in large language model (LLM) inference services significantly affect user experience, yet they remain inefficient due to sequential initialization and a massive number of fine-grained I/O requests issued by complex software components. Although refactoring the program can yield advantages such as concurrent execution and I/O merging, this approach is error-prone and carries correctness risks when dealing with massive, heterogeneous components. We propose the Communicating Finite Automata (CFA) abstraction to systematically analyze cross-component optimization opportunities, and design a programming framework to enable CFA-based component program refactoring. This framework preserves the original sequential program structure while enabling safe concurrent component execution. We prove the correctness of the program refactoring. We apply the CFA abstraction and framework to refactor process tree creation, tensor loading, and model switching in vLLM, forming a new cold-start system named InstantInfer. Extensive experiments demonstrate that InstantInfer substantially accelerates LLM cold starts (achieving up to 7.2 times speedup) and exhibits robustness across diverse GPUs, workloads, and scales.

</details>

---
