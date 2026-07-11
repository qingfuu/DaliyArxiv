# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-07-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/GIFT_Geometry-Informed_Low-precision_Gradient_Communication_for_LLM_Pretraining|GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining]]

![[assets/2607.07494_figure.png|800]]

- **arXiv**: [2607.07494](https://arxiv.org/abs/2607.07494)
- **PDF**: https://arxiv.org/pdf/2607.07494
- **详细分析**: [[20_Research/Papers/大模型/GIFT_Geometry-Informed_Low-precision_Gradient_Communication_for_LLM_Pretraining|GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining]]
- **作者**: Jieying Wang, Shuyuan Fan, Mingkai Zheng, Zhao Zhang
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion. We present GIFT, a geometry-informed gradient scaling method that performs low-precision communication in geometry-aware coordinates. By transforming gradients into a near-isotropic space before quantization, GIFT makes low-precision representations substantially more faithful to their high-precision counterparts. GIFT only changes the coordinate system used for low-precision gradient communication and does not change the optimizer, training recipe, communication collective, or low-precision format. We also develop a simplified geometry-aware transformation algorithm with low-rank approximation and selective application to balance the computation overhead and communication reduction. We examine the empirical convergence of GIFT using Llama-300M and Llama-600M models. Our results show that GIFT reduces the end-to-end pretraining time of Llama-600M by 7.6% on 64 NVIDIA GH200 Superchips, while improving the downstream task preservation profile over direct Euclidean FP8 communication under the same optimizer and communication path.

</details>

---
