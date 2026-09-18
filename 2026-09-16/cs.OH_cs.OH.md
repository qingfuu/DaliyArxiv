# cs.OH | cs.OH | 2026-09-16

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Converter-Grid_Interaction_Stability_Guaranteed_Safe_Deep_Reinforcement_Learning_for_Energy_Storage_Systems_in_Grid_Frequency_Support|Converter-Grid Interaction Stability Guaranteed Safe Deep Reinforcement Learning for Energy Storage Systems in Grid Frequency Support]]

![[assets/2609.16817_figure.png|800]]

- **arXiv**: [2609.16817](https://arxiv.org/abs/2609.16817)
- **PDF**: https://arxiv.org/pdf/2609.16817
- **详细分析**: [[20_Research/Papers/强化学习/Converter-Grid_Interaction_Stability_Guaranteed_Safe_Deep_Reinforcement_Learning_for_Energy_Storage_Systems_in_Grid_Frequency_Support|Converter-Grid Interaction Stability Guaranteed Safe Deep Reinforcement Learning for Energy Storage Systems in Grid Frequency Support]]
- **作者**: Fei Liu, Mengfan Zhang, Zhipeng Li, Frede Blaabjerg, Qianwen Xu
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.2（加权：强化学习 1.2）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Converter-Grid Interaction Stability Guaranteed Safe Deep Reinforcement Learning for Energy Storage Systems in Grid Frequency Support》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CIS-DRL, DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The growing integration of converter interfaced renewable energy resources (RESs) intensifies stability challenges. Energy storage system (ESS) can provide fast and flexible frequency support to mitigate frequency deviations. However, the interface converter of ESS may encounter converter-grid interaction stability issues. This paper proposes a converter-grid interaction stability guaranteed safe DRL (CIS-DRL) method for ESS integrated power systems to achieve frequency regulation. We first obtain a double DNN-based stability region to identify the guaranteed converter-grid interaction stability. Next, a novel converter-grid interaction stability Safe-TD3 (CIS-STD3) algorithm is designed that integrates a stability feasibility projection layer to map unsafe actions into stable action set before execution, enforcing converter-grid interaction stability as a hard constraint throughout learning process. The proposed approach enables ESS for grid frequency support with 100% converter-grid interaction stability without violations. Experimental results show that the proposed CIS-DRL method achieves improved frequency regulation performance while preventing unstable operating points, demonstrating its practical applicability for real time ESS frequency support.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Gradient_over_History-Dependent_Policy_Classes_for_LQR_with_Domain_Randomization|Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization]]

![[assets/2609.16300_figure.png|800]]

- **arXiv**: [2609.16300](https://arxiv.org/abs/2609.16300)
- **PDF**: https://arxiv.org/pdf/2609.16300
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Gradient_over_History-Dependent_Policy_Classes_for_LQR_with_Domain_Randomization|Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization]]
- **作者**: Tesshu Fujinami, Bruce D. Lee, Anastasios Tsiamis, Nikolai Matni, George J. Pappas
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization》归入 强化学习、具身智能 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Domain Randomization (DR) has been widely used to overcome the sim-to-real gap by training a controller on a distribution of simulated environments via reinforcement learning. While DR can achieve robust performance simply using controllers synthesized via policy gradient (PG) methods, the optimization landscape is not well understood, even in the case of linear quadratic regulator (LQR) objectives. To this end, we first study PG of domain randomized LQR over history-dependent policy classes, such as finite impulse response controllers, as they can extend the possibilities of simultaneous stabilization. Second, to find such a stabilizing controller, we propose a curriculum learning based algorithm which gradually expands the memory of the controller. Finally, we show that PG with the proposed algorithm converges globally to the minimizer of a sample average approximation of the DR objective under suitable bounds on the heterogeneity of environments. Empirical results support our findings and highlight promising directions for future work, including nonlinear domain-randomized control.

</details>

---
