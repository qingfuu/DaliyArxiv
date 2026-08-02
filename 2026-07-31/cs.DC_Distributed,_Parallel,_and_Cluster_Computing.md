# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-07-31

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/SmartGen_Seamless_Disaggregated_LLM_Inference_with_Selective_KV_Cache_Transfer|SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer]]

![[assets/2607.28150_figure.png|800]]

- **arXiv**: [2607.28150](https://arxiv.org/abs/2607.28150)
- **PDF**: https://arxiv.org/pdf/2607.28150
- **详细分析**: [[20_Research/Papers/大模型/SmartGen_Seamless_Disaggregated_LLM_Inference_with_Selective_KV_Cache_Transfer|SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer]]
- **作者**: Xuchuan Luo, Jiacheng Shen, Xin Wang, Yangfan Zhou
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Disaggregating the prefill and decoding stages of large language model (LLM) inference into two separate sets of nodes is widely adopted in today's LLM serving systems. However, such an architecture poses significant challenges for self-hosted LLM deployments on rented cloud instances, since transferring enormous key-value (KV) caches between disaggregated nodes can easily saturate the limited inter-node network bandwidth. In this paper, we propose to mitigate the network bottleneck by selectively transferring essential KV cache entries across the two stages. There are two challenges to achieve selective KV cache transfer, i.e., accurate KV selection during the prefill stage, and efficient KV fetching during the decoding stage. To address these challenges, we design SmartGen, a KV cache transfer engine that allows seamless disaggregated LLM inference with three data transfer paths. Specifically, we leverage 1) a profile-based proactive transfer path to identify and push essential KV cache entries to the decoding node during the prefill stage, 2) a parallel on-demand transfer path to simultaneously fetch remote and local KV cache entries during the decoding stage, and 3) a speculative transfer path to finally deliver all KV caches to the decoding node. Experimental results show that SmartGen reduces time-to-second-token by up to 4.3x compared with the typical full KV cache transfer approach while offering comparable subsequent decoding performance and accuracy.

</details>

---
