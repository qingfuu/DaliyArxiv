# cs.IR | Information Retrieval | 2026-07-24

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Diffusion_Language_Model_for_Recommendation|Diffusion Language Model for Recommendation]]

![[assets/2607.21519_figure.png|800]]

- **arXiv**: [2607.21519](https://arxiv.org/abs/2607.21519)
- **PDF**: https://arxiv.org/pdf/2607.21519
- **详细分析**: [[20_Research/Papers/大模型/Diffusion_Language_Model_for_Recommendation|Diffusion Language Model for Recommendation]]
- **作者**: Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM

#### 研究背景与动机

《Diffusion Language Model for Recommendation》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-empowered recommender systems have emerged as a promising paradigm for generative recommendation, leveraging their strong semantic reasoning and generative capacity to model complex, diverse user preferences. However, most existing approaches rely on an autoregressive paradigm that is suboptimal for recommendation. The next-token objective emphasizes sequential order rather than the structural inter-item dependencies underlying user preferences. In addition, prefix-constrained generation restricts bidirectional context and commits to left-to-right decoding, causing early errors to accumulate without correction. Inspired by the success of diffusion language models, we propose \textbf{DLMRec}, a discrete diffusion language model tailored for recommendation that offers a compelling alternative to autoregressive generation. Specifically, DLMRec introduces three key components to bridge diffusion language modeling with recommendation. First, a collaborative-aware stochastic tokenizer encodes multi-hop collaborative signals into expressive discrete tokens compatible with diffusion modeling. Second, a curriculum-driven training strategy aligns the denoising process with preference recovery through progressive item- and token-level learning. Third, a stability-aware voting mechanism aggregates iterative predictions to improve generation consistency and robustness.

</details>

---
