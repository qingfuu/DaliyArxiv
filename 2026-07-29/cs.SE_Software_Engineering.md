# cs.SE | Software Engineering | 2026-07-29

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/WarmTuner_Program-Specific_Warm_Starts_for_Compiler_Autotuning_via_Offline-to-Online_Reinforcement_Learning|WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning]]

![[assets/2607.25831_figure.png|800]]

- **arXiv**: [2607.25831](https://arxiv.org/abs/2607.25831)
- **PDF**: https://arxiv.org/pdf/2607.25831
- **详细分析**: [[20_Research/Papers/强化学习/WarmTuner_Program-Specific_Warm_Starts_for_Compiler_Autotuning_via_Offline-to-Online_Reinforcement_Learning|WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning]]
- **作者**: Tianlu Qiao, Mingxuan Zhu, Zeyu Sun, Dan Hao
- **cs 子类**: cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning》归入 强化学习 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PolyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compilers are fundamental software tools that translate high-level programs into machine code. Modern compilers expose hundreds of optimizations, each turned on or off through an optimization flag, to improve the performance of the generated code. However, the number of possible flag combinations grows exponentially, making it difficult to find a flag configuration well suited to a given target program. Existing compiler auto-tuning techniques reduce tuning cost by pruning the search space, injecting search biases, or predicting configuration performance. Although some exploit program features, the knowledge they extract from historical data is frozen once search begins; runtime feedback then guides only the search itself, never the prior. As a result, when this prior mismatches the target program, these methods waste much of the limited online budget before the search reaches good configurations. We propose WarmTuner, an offline-to-online reinforcement learning framework that instead turns historical records into a program-conditioned policy that predicts each flag's setting over the full flag space and remains adaptable on the target program. Offline, WarmTuner learns this program-conditioned policy over the full flag space from historical good configurations. Online, it refines the same policy on the target program using real compile-run feedback, so that the policy is driven by measured speedups rather than limited to the historical data. We instantiate the online update with Group Relative Policy Optimization (GRPO), which compares candidates in the same round and avoids a separate value model. We evaluate WarmTuner on GCC 15.2.0 with cBench and PolyBench. The results show that WarmTuner achieves an average speedup of 1.732x over GCC -O3 and obtains the best result on 14/30 programs, significantly outperforming the compared techniques.

</details>

---
