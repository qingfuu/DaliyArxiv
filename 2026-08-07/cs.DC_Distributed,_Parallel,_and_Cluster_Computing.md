# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/TensorCast_The_Missing_Tensor_Management_Layer_in_Large_Language_Model_Infrastructure|TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure]]

![[assets/2608.06007_figure.png|800]]

- **arXiv**: [2608.06007](https://arxiv.org/abs/2608.06007)
- **PDF**: https://arxiv.org/pdf/2608.06007
- **详细分析**: [[20_Research/Papers/大模型/TensorCast_The_Missing_Tensor_Management_Layer_in_Large_Language_Model_Infrastructure|TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure]]
- **作者**: Yuhan Zhou, Yuchu Luo, Hao Nie, Wangrunze Lv, Yu Zhou, Yibo Zhu, Daxin Jiang, Chenren Xu
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern LLM infrastructure increasingly manages tensors not only as computation data, but also as persistent states shared across distributed components. Existing systems optimize individual tensor management tasks, such as model weight loading, KV cache management, and checkpoint synchronization, by deeply integrating task-specific mechanisms with execution engines, networks, or storage backends. However, this specialization creates isolated silos that hinder the reuse and composition of tensor management strategies across evolving LLM workloads. In this paper, we identify tensor lifecycle management as a missing abstraction layer in LLM infrastructure and propose Tensor-as-a-Service (TaaS), which decouples tensor state management from computation logic. We design and build TensorCast, a distributed tensor management layer that provides first-class tensor abstractions, programmable lifecycle primitives, and a runtime that separates tensor management policies from execution mechanisms. This enables developers to write tensor management programs using TensorCast APIs while transparently leveraging distributed execution and data movement. We integrate TensorCast with vLLM and SGLang and evaluate it across diverse tensor lifecycle workloads, including model weight materialization, weight synchronization, KV cache management, and programmable request routing. Our results show that TensorCast achieves competitive performance with specialized tensor management systems while enabling new cross-component optimization policies. A programmable policy implemented with TensorCast improves median TTFT by up to 93.2% under highly concurrent multi-turn agent workloads.

</details>

---
