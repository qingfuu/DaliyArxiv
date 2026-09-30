# cs.NE | Neural and Evolutionary Computing | 2026-09-28

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Modeling_quantum_neural_network_gradient_with_reinforcement_learning|Modeling quantum neural network gradient with reinforcement learning]]

![[assets/2609.31066_figure.png|800]]

- **arXiv**: [2609.31066](https://arxiv.org/abs/2609.31066)
- **PDF**: https://arxiv.org/pdf/2609.31066
- **详细分析**: [[20_Research/Papers/强化学习/Modeling_quantum_neural_network_gradient_with_reinforcement_learning|Modeling quantum neural network gradient with reinforcement learning]]
- **作者**: Nhan Trong Luu, Duong Trung Luu, Nam Ngoc Pham, Thang Cong Truong
- **cs 子类**: cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Modeling quantum neural network gradient with reinforcement learning》归入 强化学习、大模型 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, TensorRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training quantum neural networks (QNNs) on near-term hardware remains hampered by two compounding difficulties: the exponential vanishing of gradient variance known as the barren plateau, and the $\mathcal{O}(L \cdot 2^n)$ time and memory cost of differentiating through an $n$-qubit, $L$-layer circuit. We propose RLQ-Grad, a reinforcement-learning-based optimizer in which a classical policy $π_φ$ (a spectrally-normalized PPO agent) learns to propose parameter updates directly, conditioned on the QNN's current parameters, loss, accuracy, and previous update. Because the surrogate gradient is emitted by a classical network rather than obtained by differentiating through the unitary $U(θ)$, its variance is not constrained by the barren plateau concentration bound, and its cost scales with the number of trainable parameters rather than the Hilbert-space dimension. We prove these properties formally and verify them on a hardware-efficient ansatz across four supervised benchmarks with up to $n=20$ qubits. RLQ-Grad preserves a near-flat gradient-variance curve where backpropagation, parameter-shift, and adjoint differentiation decay by 1 to 2 orders of magnitude. Accounting for the full training pipeline (PPO rollouts, actor-critic updates, and optimizer states), RLQ-Grad needs under 2 MB of memory and runs $2490\times$, $7876\times$, and $673\times$ faster per iteration than these three methods at $n=20$. It improves top-1 accuracy by up to $+10\%$ over gradient-based baselines on circuits of up to 12 qubits, and matches dedicated barren plateau mitigation methods on CIFAR-10 at 14 to 20 qubits, where evolutionary and gradient-free optimizers collapse to chance.

</details>

---
