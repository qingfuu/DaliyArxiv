# cs.CL | Computation and Language | 2026-09-18

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Uni-LaDiR_Latent_Diffusion_Unifies_Multimodal_Reasoning|Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning]]

![[assets/2609.19878_figure.png|800]]

- **arXiv**: [2609.19878](https://arxiv.org/abs/2609.19878)
- **PDF**: https://arxiv.org/pdf/2609.19878
- **详细分析**: [[20_Research/Papers/具身智能/Uni-LaDiR_Latent_Diffusion_Unifies_Multimodal_Reasoning|Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning]]
- **作者**: Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Yian Ma, Lianhui Qin
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.95（加权：具身智能 0.9，大模型 0.85，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning》归入 具身智能、大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal reasoning requires models to draw on information from multiple modalities throughout the reasoning process. Yet existing methods often concatenate modality-specific thought tokens in a single sequence, leaving the model to bridge representational differences as it reasons across modalities. We introduce Uni-LaDiR (Unified Latent Diffusion Reasoner), a framework that brings these thoughts into a shared latent space for reasoning. A unified encoder maps teacher reasoning steps from different modalities into shared thought tokens, trained to preserve the information needed for later reasoning steps and the final answer or action. Because the same context can support multiple valid next steps, we use diffusion to predict the next block of thought tokens from the input and preceding blocks. Jointly training the encoder and diffusion reasoner with shared model weights encourages thought tokens to be both useful for the task and predictable from the available context. At inference, the model generates these tokens without teacher observations. Across eleven vision-language model (VLM) benchmarks and two vision-language-action (VLA) suites, Uni-LaDiR achieves relative gains over the strongest evaluated baselines of 7.3% on visual reasoning tasks and 6.1% on robot manipulation tasks.

</details>

---
