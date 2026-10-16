# cs.HC | Human-Computer Interaction | 2026-10-14

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Calibrating_LLM_Explanations_to_Human_Decisions_with_Reinforcement_Learning|Calibrating LLM Explanations to Human Decisions with Reinforcement Learning]]

![[assets/2610.17306_figure.png|800]]

- **arXiv**: [2610.17306](https://arxiv.org/abs/2610.17306)
- **PDF**: https://arxiv.org/pdf/2610.17306
- **详细分析**: [[20_Research/Papers/大模型/Calibrating_LLM_Explanations_to_Human_Decisions_with_Reinforcement_Learning|Calibrating LLM Explanations to Human Decisions with Reinforcement Learning]]
- **作者**: Dong Shu, Ziyang Guo, Negar Kamali, Matthew Groh, Jessica Hullman
- **cs 子类**: cs.HC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《Calibrating LLM Explanations to Human Decisions with Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HD-RL, Human_Decision_RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Explanations of LLM outputs are considered an important way to make model behavior legible, helping human users make good decisions on downstream tasks. However, default training approaches for improving explanations target model task performance or human preference rather than human decision quality. To bridge this gap, we introduce \textbf{HD-RL}, a reinforcement learning framework for optimizing LLM explanations for human decision making. Our approach calibrates a human decision simulator on observed human decisions, applying a proxy reward model to optimize the LLM to generate explanations that help people to make good decisions. We apply this framework to AI-generated text detection. In our initial data collection phase, we observed that while LLMs possess strong autonomous detection capabilities, the explanations they generate for users yield near-random human accuracy (51.3\%). By applying the HD-RL framework to the open-source Qwen 3.6 model, we generate optimized explanations that improve human performance, achieving a GLMM-estimated human accuracy of 63.7\% in a randomized between-subjects experiment with repeated measures and outperforming RLVR, RLAIF, and other baselines by over 8\%.

</details>

---
