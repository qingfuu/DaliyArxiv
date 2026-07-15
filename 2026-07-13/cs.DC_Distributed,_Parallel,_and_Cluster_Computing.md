# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-07-13

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/SiFAR_Synchronization-Free_All-Reduce_for_Low-Latency_LLM_Inference|SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference]]

![[assets/2607.08973_figure.png|800]]

- **arXiv**: [2607.08973](https://arxiv.org/abs/2607.08973)
- **PDF**: https://arxiv.org/pdf/2607.08973
- **详细分析**: [[20_Research/Papers/大模型/SiFAR_Synchronization-Free_All-Reduce_for_Low-Latency_LLM_Inference|SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference]]
- **作者**: Hritvik Taneja, Anish Saxena, Abhishek Revinipati, Jae Hyung Ju, Neal C. Crago, Moinuddin Qureshi
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rise of reasoning models and agentic systems has made LLM token-generation latency a key bottleneck. Unlike chatbots, whose latency gains saturate at human reading speed, these systems generate intermediate reasoning tokens not consumed by humans. Thus, per-token latency directly determines end-to-end response time. Low-latency inference uses minimal batching, making token generation bandwidth-bound. Tensor Parallelism addresses this by sharding model weights across GPUs and loading them in parallel. However, scaling to more GPUs introduces All-Reduce overheads that grow with GPU count. Removing All-Reduce improves token throughput by 43% for Llama-3.1-8B on 8 H200 GPUs. We propose Synchronization-Free All-Reduce (SiFAR), which reduces synchronization overhead during low-latency inference. Existing oneshot and twoshot algorithms incur overheads from barriers before and after communication. First, we find that the bottom barrier in oneshot enforces a WAW dependency and eliminate it by co-designing communication and model execution to enable dual buffering. However, oneshot scales poorly with GPU count. Twoshot performs better at higher TP degrees but incurs an unavoidable bottom barrier. To overcome this, we leverage in-switch reduction in modern switches. We propose redundant pull, where each GPU reduces the full All-Reduce payload at the switch. This improves oneshot scalability while retaining its no-bottom-barrier advantage. Finally, to reduce top-barrier overhead, we observe that each decode step issues multiple All-Reduce operations, keeping GPUs tightly synchronized after the first. We therefore propose speculative reduction, which initiates data transfer before the top barrier and ensures correctness via lightweight validation. SiFAR reduces All-Reduce latency by up to 52% and improves end-to-end throughput by 18.6% for Llama-3.1-8B and 13.1% for Qwen3.5-397B-17B at TP=8.

</details>

---
