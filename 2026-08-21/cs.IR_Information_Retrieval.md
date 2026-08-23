# cs.IR | Information Retrieval | 2026-08-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/SSR-GRPO_Integrating_Supervision_and_Semantic_IDs_into_Reinforcement_Learning_for_Dense_Retrieval_in_E-commerce|SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning for Dense Retrieval in E-commerce]]

![[assets/2608.19595_figure.png|800]]

- **arXiv**: [2608.19595](https://arxiv.org/abs/2608.19595)
- **PDF**: https://arxiv.org/pdf/2608.19595
- **详细分析**: [[20_Research/Papers/强化学习/SSR-GRPO_Integrating_Supervision_and_Semantic_IDs_into_Reinforcement_Learning_for_Dense_Retrieval_in_E-commerce|SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning for Dense Retrieval in E-commerce]]
- **作者**: Guangxin Song, Xing Fang, Mingmin Jin, Jing Wang, Bokang Wang, Zhentao Song, Junjie Bai, Jianbo Zhu
- **cs 子类**: cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《SSR-GRPO: Integrating Supervision and Semantic IDs into Reinforcement Learning for Dense Retrieval in E-commerce》归入 强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embedding-based retrieval (EBR) is pivotal in e-commerce search but often struggles with complex semantics. While recent methods often fine-tune large language models (LLMs) for representation learning, they typically lack robust mechanisms for handling complex and implicit semantics. While Retrieval-GRPO (R-GRPO) recently introduced reinforcement learning to dense retrieval, it suffers from noisy top-K candidates due to limited batch sampling and biased relevance assessments caused by using similarly trained LLMs as reward models. To tackle these issues, we propose Supervised Retrieval-GRPO with Semantic Identifiers (SSR-GRPO). Specifically, our method first proposes a dual-perspective framework for relevance assessment. It leverages both Semantic Identifiers (SIDs) produced by quantization learning and dense representation vectors to generate more unbiased relevance scores. Furthermore, leveraging the hierarchical similarity relationships of the generated SIDs, we mine a set of hard negative samples that serve two purposes: (1) to design a masking function integrated into R-GRPO, effectively filtering intra-group noisy samples; and (2) to construct a Retrieval-DPO task composed of positive and negative sample pairs, enabling the model to capture fine-grained semantic distinctions from a pair-wise perspective. By integrating these optimization strategies, we propose SSR-GRPO. Extensive offline and online experiments validate SSR-GRPO's effectiveness, and it has been deployed on a large-scale e-commerce platform.

</details>

---
