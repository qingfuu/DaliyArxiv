# cs.CL | Computation and Language | 2026-11-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/A_Semantics-First_Approach_to_Multimodal_Video_Captioning_with_Frozen_Encoders_and_Stabilized_Reinforcement_Learning|A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning]]

![[assets/2611.33409_figure.png|800]]

- **arXiv**: [2611.33409](https://arxiv.org/abs/2611.33409)
- **PDF**: https://arxiv.org/pdf/2611.33409
- **详细分析**: [[20_Research/Papers/大模型/A_Semantics-First_Approach_to_Multimodal_Video_Captioning_with_Frozen_Encoders_and_Stabilized_Reinforcement_Learning|A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning]]
- **作者**: Albert Chiwara, Erhan Guven
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.65，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose the Audio-Visual Query Transformer (AVQFormer), a highly efficient architecture built upon a 2.7B parameter LLM featuring a fixed-length $K=16$ semantic alignment module, stabilized via Adaptive Self-Critical Sequence Training (ASCST) with Entropy Regularization. Multimodal Large Language Models (LLMs) often rely on global audio representations to compensate for inefficient, frame-based visual encoders. While our Phase 1 prompted evaluations demonstrate that the Multimodal Base Model achieves strong deep semantic alignment (scoring 0.889 on BERTScore F1), optimizing this architecture for legacy metrics reveals a performance gap. We explore this gap as a hypothesis we term temporal alignment friction: a conflict where global audio representations disrupt the chronological sequence of visual frames, leading to penalties under visually-focused evaluation metrics. Consequently, by stripping away the audio, our Video-Only ablation conforms more closely to this rigid syntax, achieving 63.0 CIDEr. While trailing larger models such as Qwen2.5-VL (67.4 CIDEr), this establishes a strong baseline for sub-3B parameter LLM-based models. This indicates that CIDEr, as applied to datasets such as MSR-VTT, may exhibit a bias toward visually grounded syntax, limiting its ability to fully capture multimodal semantic richness.

</details>

---
