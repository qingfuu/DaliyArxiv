# cs.GR | Graphics | 2026-05-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/SCRIPT_Scalable_Diffusion_Policy_with_Multi-stage_Training_for_Language-driven_Physics-Based_Humanoid_Control|SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-Based Humanoid Control]]

![[assets/2605.22894_figure.jpg|800]]

- **arXiv**: [2605.22894](https://arxiv.org/abs/2605.22894)
- **PDF**: https://arxiv.org/pdf/2605.22894
- **详细分析**: [[20_Research/Papers/具身智能/SCRIPT_Scalable_Diffusion_Policy_with_Multi-stage_Training_for_Language-driven_Physics-Based_Humanoid_Control|SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-Based Humanoid Control]]
- **作者**: Jingyan Zhang, Han Liang, Ruichi Zhang, Bin Li, Juze Zhang, Xin Chen, Jingya Wang, Lan Xu, Jingyi Yu
- **cs 子类**: cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型, 大模型
- **相关性评分**: 3.52（加权：具身智能 1.8，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

让物理仿真中的人形机器人能够直接理解自然语言指令并执行动作，是迈向通用具身智能体的重要一步，尤其适用于虚拟角色控制、交互式动画和机器人技能编排等场景。现有方法往往陷入“语义表达能力”和“物理可行性”之间的矛盾：要么文本跟随不够准确，要么动作质量和长时序稳定性不足。本文关注的是如何在闭环物理控制中同时提升指令一致性、运动质量与真实感，因此具有较强的研究价值。

#### 方法概述和架构

论文提出 SCRIPT，一种面向语言驱动物理人形控制的可扩展扩散策略，并采用多阶段训练流程。其核心是 JAST-DiT（Joint Action-State-Text Diffusion Transformer），将动作、物理状态和文本分别编码成独立 token 流，再通过联合注意力实现跨模态交互，从而让语言语义与控制动力学直接耦合。为稳定自回归式控制，方法设计了非线性历史条件机制：保留最近时刻的密集上下文，同时从更久远的历史中以更稀疏的方式采样信息，以兼顾短期细节与长期依赖。训练上，第一阶段用监督模仿和 flow matching 进行预训练；第二阶段引入带混合奖励的强化学习后训练（RLHR），在闭环仿真中结合物理反馈与文本奖励，并通过向 flow-sampling 注入可学习噪声来提升探索和优化效果。推理时，模型在 receding-horizon 方式下预测未来一段状态-动作序列，但每次只执行首个动作，再根据新状态滚动更新历史。

#### 实验结果分析

作者在 HumanML3D 与 MotionMillion 上进行了评测，并与此前方法比较了文本对齐、运动质量和物理真实性等指标；从摘要和节选可见，SCRIPT 在多个指标上优于现有 SOTA。论文还对 1200 小时规模的 MotionMillion 做了扩展性研究，结果显示随着模型规模从 0.2B 增至 1.2B，性能持续提升，说明该方法具备良好的可扩展性。消融实验进一步验证了 JAST-DiT、非线性历史条件和混合奖励 RL 后训练的有效性。具体数值在可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

从自然语言指令中控制基于物理仿真的人形机器人，是迈向通用具身智能体的关键一步。然而，现有方法仍受限于语义表达能力与物理可行性之间的张力，往往难以同时实现忠实的指令跟随、高质量运动以及稳定的长时程控制。为此，我们提出 SCRIPT，一种面向语言驱动物理人形控制的可扩展扩散策略，并采用多阶段训练框架。SCRIPT 的核心是 JAST-DiT（Joint Action-State-Text Diffusion Transformer），它将动作、物理状态和文本表示为独立的 token 流，并通过联合注意力将它们耦合起来，从而使语言语义与控制动力学能够直接交互。为了稳定自回归控制，我们引入了一种非线性历史条件机制：它保留密集的近期上下文，并从长期历史中以越来越稀疏的方式采样线索。除监督式模仿预训练之外，我们还提出了后训练阶段，并通过带混合奖励的强化学习（RLHR）进一步提升性能。通过在 flow-sampling 过程中注入可学习噪声，RLHR 在闭环仿真中利用混合物理反馈与文本奖励，有效提升了运动质量和指令跟随能力。定量评估表明，SCRIPT 在文本对齐、运动质量和物理真实感指标上均优于此前最先进方法。此外，在 1200 小时的 MotionMillion 数据集上的扩展性研究表明，模型规模增大时性能能够持续提升，凸显了 SCRIPT 在大规模预训练中的稳健可扩展性。我们的代码将公开发布，以供后续研究使用。

</details>

---
