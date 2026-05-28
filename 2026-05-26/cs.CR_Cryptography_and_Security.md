# cs.CR | Cryptography and Security | 2026-05-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Capability_and_Robustness_Cannot_Both_Be_Free_An_Information-Theoretic_Bound_for_Vision-Language-Action_Models|Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models]]

![[assets/2605.25889_figure.png|800]]

- **arXiv**: [2605.25889](https://arxiv.org/abs/2605.25889)
- **PDF**: https://arxiv.org/pdf/2605.25889
- **详细分析**: [[20_Research/Papers/具身智能/Capability_and_Robustness_Cannot_Both_Be_Free_An_Information-Theoretic_Bound_for_Vision-Language-Action_Models|Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models]]
- **作者**: Jianwei Tai
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, RL, Security

#### 研究背景与动机

《Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Gaussian-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are increasingly deployed on real robots, where each predicted action is executed and each failure carries a safety cost. They reach high success rates on clean inputs but collapse under small adversarial perturbations. A $16/255$ PGD attack on OpenVLA-7B drops LIBERO success from above $95\%$ to under $5\%$. Empirical defenses recover some robustness at a cost in clean accuracy, but the literature does not say whether the trade-off has a theoretical floor. We prove that it does. For any VLA policy with discrete actions, the sum of capability (mutual information between policy action and oracle action) and robustness (mutual information preserved under adversarial perturbation, net of trivial channel leakage) is upper-bounded by a policy-independent budget: task entropy plus adversarial channel capacity. The proof is two applications of the Data Processing Inequality plus MI non-negativity. The pixel-level bound is loose on current models ($\sim 10^3$ nats), but an encoder-specific corollary restricts the channel to the policy-relevant subspace, reducing the budget from $\sim 5{,}000$ to $\sim 31$ nats on OpenVLA; the policy already consumes $\sim 24\%$ of this tighter budget, leaving limited room for simultaneous robustness improvement. We validate the bound across $252$ closed-form Gaussian-VLA cells and $48$ OpenVLA-7B $\times$ LIBERO $\times$ PGD cells (zero violations). We propose encoder-specific slack as a normalized comparison axis for defense papers, and release all code, manifests, and results.

</details>

---
