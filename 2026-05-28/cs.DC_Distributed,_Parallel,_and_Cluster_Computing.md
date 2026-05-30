# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-05-28

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Heterogeneous_Parallelism_for_Multimodal_Large_Language_Model_Training|Heterogeneous Parallelism for Multimodal Large Language Model Training]]

![[assets/2605.27678_figure.png|800]]

- **arXiv**: [2605.27678](https://arxiv.org/abs/2605.27678)
- **PDF**: https://arxiv.org/pdf/2605.27678
- **详细分析**: [[20_Research/Papers/大模型/Heterogeneous_Parallelism_for_Multimodal_Large_Language_Model_Training|Heterogeneous Parallelism for Multimodal Large Language Model Training]]
- **作者**: Yashaswi Karnati, Kamran Jafari, Akash Mehra, Li Ding, Pranav Prashant Thombre, Ali Roshan Ghias, Shifang Xu, Parth Mannan, Yu Yao, Hao Wu, Eric Harper, Ashwath Aithal...
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Heterogeneous Parallelism for Multimodal Large Language Model Training》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation model training is becoming multimodal, from post-training pipelines to large-scale pretraining. As modality coverage broadens, context windows grow, and encoder LLM scales diverge, a single LLM-centric TP/CP/PP/DP/EP layout increasingly limits throughput. This coupling forces encoders to inherit LLM-driven sharding and placement choices that can add communication, limit encoder parallelism, or constrain the LLM schedule; the mismatch is most pronounced at long contexts, where LLM context parallelism is needed for the fused multimodal sequence but encoder inputs remain bounded. We present heterogeneous parallelism for multimodal large language model training, an abstraction that lets modules in one end-to-end graph use independent layouts and rank placements, supporting colocated execution on shared GPUs and non-colocated execution on disjoint rank sets. The key challenge is preserving boundary tensor semantics across independent layouts: forward activations must be materialized for the destination layout, while backward gradients must be routed back to the source layout. We address this with boundary communicators that implement forward and backward layout transforms, plus scheduling extensions for both placement modes. We evaluate optimized homogeneous, colocated heterogeneous, and non-colocated heterogeneous configurations across multimodal workloads and GPU scales to characterize when added layout and placement freedom exposes a better operating point. Across this sweep, colocated heterogeneity improves TFLOPS/GPU by up to 49.3%, while non-colocated heterogeneity improves aggregate token throughput by up to 13.0% and TFLOPS/GPU by up to 9.6%. We validate loss convergence parity against homogeneous baselines and release the system as an open-source Megatron-LM extension.

</details>

---
