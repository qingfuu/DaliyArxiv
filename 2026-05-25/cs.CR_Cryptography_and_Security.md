# cs.CR | Cryptography and Security | 2026-05-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Less_Effort,_Shorter_Proofs_Reinforcement_Learning_for_Security_Protocol_Analysis_in_Tamarin|Less Effort, Shorter Proofs: Reinforcement Learning for Security Protocol Analysis in Tamarin]]

![[assets/2605.23643_figure.png|800]]

- **arXiv**: [2605.23643](https://arxiv.org/abs/2605.23643)
- **PDF**: https://arxiv.org/pdf/2605.23643
- **详细分析**: [[20_Research/Papers/强化学习/Less_Effort,_Shorter_Proofs_Reinforcement_Learning_for_Security_Protocol_Analysis_in_Tamarin|Less Effort, Shorter Proofs: Reinforcement Learning for Security Protocol Analysis in Tamarin]]
- **作者**: Matthias Cosler, Cas Cremers, Bernd Finkbeiner, Mohamed Ghanem, Niklas Medinger
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

形式化验证工具如 Tamarin 和 ProVerif 已经能分析 EMV、5G、WPA2 等复杂真实协议，甚至发现零日漏洞，但在实际使用中，证明搜索仍然非常耗时，且高度依赖人工经验与启发式调参。对于安全协议分析而言，如何在保证可验证性的前提下减少搜索成本、缩短证明长度，是一个很现实的瓶颈。这篇工作值得关注之处在于，它尝试把强化学习引入 Tamarin 的证明搜索流程，用学习型策略替代部分手工启发式。

#### 方法概述和架构

论文提出了一个受 AlphaZero 和 AlphaProof 启发的强化学习框架，用于 Tamarin 中的证明搜索。作者为 Tamarin 设计了一个无状态的 API，把定理证明过程抽象成经典强化学习环境：客户端先获取初始约束系统及其规则，再通过不断执行推理规则扩展搜索树。框架使用蒙特卡洛树搜索（MCTS）作为主搜索器，并由神经网络启发式进行引导；该神经启发式从已完成的子证明中学习，从而预测哪些证明路径更有希望。推理阶段，系统在搜索树上扩展、评估并回溯，直到找到反例或确认不存在反例，最后构造证明树并交由 Tamarin 检查其正确性。整体上，这一管线把 Tamarin 变成了可程序化交互的证明环境，并使 RL 与传统符号推理紧密结合。

#### 实验结果分析

作者在 16 个案例研究上评估了该框架，覆盖经典协议模型以及近年来论文中的更具挑战性的前沿协议模型。实验结果表明，该方法能自动找到比 Tamarin 标准搜索更多的证明，并且生成的证明长度短于标准搜索和人工设计的启发式策略。节选中未给出具体数值，但结论明确显示：该方法具有较好的开箱即用性，能够直接辅助活跃研究中的 Tamarin 用户，减少人工工作量。

<details>
<summary>完整摘要</summary>

Tamarin 和 ProVerif 等工具已经在分析和验证诸如 EMV、5G 和 WPA2 之类的复杂真实协议方面取得了显著成功，甚至能够发现零日漏洞。尽管有这些成就，验证此类协议仍然是一项耗时且困难的任务，往往需要大量人工努力和专业知识。本文提出了一个受 AlphaZero 和 AlphaProof 启发的强化学习（RL）框架，为 Tamarin 实现一种新的证明搜索方式。我们为 Tamarin 开发了一个无状态 API，将其作为一个经典的 RL 环境。我们使用神经启发式来引导蒙特卡洛树搜索（MCTS），该启发式从已完成的子证明中学习。我们在 16 个案例研究上评估了该框架，范围从经典协议模型到近期论文中具有挑战性的最先进协议模型。我们的方法比 Tamarin 的标准搜索自动找到更多证明，并且生成的证明短于标准搜索和人工设计的启发式方法。我们的流程可直接用于协助正在开展研究的 Tamarin 用户，减少所需的人力成本。此外，我们标准化的接口为用户以程序化方式与 Tamarin 交互提供了途径。最后，我们的工作展示了将基于 RL 的方法迁移到 Tamarin 场景中的可喜潜力。

</details>

---
