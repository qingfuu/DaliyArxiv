# cs.CY | Computers and Society | 2026-06-01

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Reinforcement_Learning_for_Special_Education_Aligning_LLM_Tutors_to_Diverse_Learners_through_Disability-Adaptive_Training|Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training]]

![[assets/2605.30670_figure.png|800]]

- **arXiv**: [2605.30670](https://arxiv.org/abs/2605.30670)
- **PDF**: https://arxiv.org/pdf/2605.30670
- **详细分析**: [[20_Research/Papers/大模型/Reinforcement_Learning_for_Special_Education_Aligning_LLM_Tutors_to_Diverse_Learners_through_Disability-Adaptive_Training|Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training]]
- **作者**: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
- **cs 子类**: cs.CY
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training》归入 强化学习、大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PedagogicalRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly deployed as intelligent tutors, yet research on aligning them for special education remains absent. Recent work has applied reinforcement learning to LLM tutors, but these methods target a generic learner in a single domain (mathematics) and do not address the cognitive and communicative diversity of learners with disabilities. We introduce \emph{Special-R1}, a framework that extends pedagogical RL to special education through two components: (1) a two-dimensional adaptive system prompt that couples a difficulty-based support level with a disability-specific teaching style across five disability profiles; and (2) a persona-aware Thinking Reward whose judge rubric is conditioned on the learner's disability profile. On a persona-augmented test set of 690 multi-turn dialogues, our full model raises persona-aware Fit from 6.75 (generic baseline) to 8.40 (+1.65) and SPED-rubric Helpfulness from 0.720 to 0.768, leading on the four-component Total (2.911, +0.064 over the runner-up) while remaining within 0.01 of the strongest variant on the out-of-domain OpenLearnLM benchmark (8.53). Ablations show that the Thinking Reward becomes effective only in combination with adaptive prompting, and that residual weakness on specific learning disability in mathematics motivates targeted multimodal extensions.

</details>

---
