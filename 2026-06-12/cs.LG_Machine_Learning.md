# cs.LG | Machine Learning | 2026-06-12

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Distribution-Agnostic_Robust_Trajectory_Optimization_via_Chance-Constrained_Reinforcement_Learning|Distribution-Agnostic Robust Trajectory Optimization via Chance-Constrained Reinforcement Learning]]

![[assets/2606.13605_figure.png|800]]

- **arXiv**: [2606.13605](https://arxiv.org/abs/2606.13605)
- **PDF**: https://arxiv.org/pdf/2606.13605
- **详细分析**: [[20_Research/Papers/强化学习/Distribution-Agnostic_Robust_Trajectory_Optimization_via_Chance-Constrained_Reinforcement_Learning|Distribution-Agnostic Robust Trajectory Optimization via Chance-Constrained Reinforcement Learning]]
- **作者**: Yashdeep Chaudhary, Roberto Armellin, Harry Holt, Marco Sagliano
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Distribution-Agnostic Robust Trajectory Optimization via Chance-Constrained Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RCCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a distribution-agnostic robust trajectory-optimization framework based on chance-constrained reinforcement learning. The uncertainty is represented here through initial conditions and process noise, with the only requirement being that it can be sampled. A deterministic nominal trajectory is first computed offline, and reinforcement learning is then used only to robustify that baseline through a structured affine closed-loop correction law comprising a feedforward control adjustment and time-varying feedback gains. Probabilistic feasibility is enforced empirically through rollout-based upper-tail quantiles, while terminal dispersion is regulated through covariance-feasibility penalties. The framework is assessed on two materially different trajectory design problems. The flagship case study is a three-dimensional multi-impulse Earth-Mars transfer, where the learned policy is benchmarked against a recent robust trajectory-optimization reference under Gaussian uncertainty and then evaluated under bounded uniform uncertainty and under process disturbances not seen during training. The second case study is a stochastic atmospheric pinpoint rocket landing problem, used to assess portability to a short-horizon continuous-thrust setting with drag, mass depletion, and glide-slope constraints. The results show that the proposed framework can remain competitive in upper-tail fuel cost while preserving probabilistic feasibility, and that the same robustification scaffold can be carried across heterogeneous spacecraft trajectory planning problems without redesign of its core stochastic-control structure.

</details>

---

### [[20_Research/Papers/世界模型/Extracting_Governing_Equations_from_Latent_Dynamics_via_Multi-View_Contrastive_Learning|Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning]]

![[assets/2606.13260_figure.png|800]]

- **arXiv**: [2606.13260](https://arxiv.org/abs/2606.13260)
- **PDF**: https://arxiv.org/pdf/2606.13260
- **详细分析**: [[20_Research/Papers/世界模型/Extracting_Governing_Equations_from_Latent_Dynamics_via_Multi-View_Contrastive_Learning|Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning]]
- **作者**: Paolo Muratore, Mackenzie Weygandt Mathis
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Identifying latent dynamical systems from noisy, high-dimensional measurements is a central problem at the intersection of representation learning, system identification, and scientific discovery. We present DYSCO, a multi-view temporal contrastive learning algorithm that jointly recovers latent trajectories and the governing dynamics from such observations, by leveraging multiple independent noisy views of the same underlying process to disentangle signal from noise. By parameterizing the dynamics in a structured functional basis, our framework further enables symbolic recovery of the governing equations within an affine gauge. We offer theoretical guarantees for strong identification up to an affine indeterminacy, extending prior identifiability results to the realistic setting of noisy nonlinear observations. Empirically, we demonstrate accurate recovery of both latent trajectories and flow fields across a diverse set of dynamical regimes (e.g., chaotic, oscillatory, and metastable) under both Gaussian and Poisson observation noise, the latter being particularly relevant for neural recordings.

</details>

---

### [[20_Research/Papers/世界模型/Scale_Buys_Interpolation,_Structure_Buys_a_Horizon_Certified_Predictability_for_Equivariant_World_Models|Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models]]

![[assets/2606.13092_figure.png|800]]

- **arXiv**: [2606.13092](https://arxiv.org/abs/2606.13092)
- **PDF**: https://arxiv.org/pdf/2606.13092
- **详细分析**: [[20_Research/Papers/世界模型/Scale_Buys_Interpolation,_Structure_Buys_a_Horizon_Certified_Predictability_for_Equivariant_World_Models|Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models]]
- **作者**: Hongbo Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Robotics, WorldModel, Systems

#### 研究背景与动机

《Scale Buys Interpolation, Structure Buys a Horizon: Certified Predictability for Equivariant World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scale buys interpolation; structure buys a certified horizon. A world model's average error says nothing about whether a particular prediction can be trusted, or for how long. For equivariant latent world models we give a computable, multi-step certificate of the predictable horizon: $T$-step rollout error is provably constant over each symmetry orbit (Theorem A) and stratified channel-by-channel by the predictor's Lyapunov spectrum, $T_j(ε)\sim\log(1/ε)/λ_j$. The horizon is two-sided -- a matching lower bound makes approximate equivariance provably horizon-limited -- and the certificate is exclusive to structure: orbit-constant error characterizes equivariance, so no non-equivariant model has it at any scale. Empirically, on 40-D Lorenz-96 only a $\mathbb{Z}_N$-equivariant network recovers the full Lyapunov spectrum ($R^2{=}0.98$); dense and recurrent baselines fail. Because the spectrum is faithful, the certificate acts, a priori: under a fixed sensing budget a $c\times$-inflated certificate provably needs $c\times$ the budget, and the equivariant certificate meets a budget its inflated dense counterpart cannot -- with zero calibration data. The same read-out, unchanged, audits public pretrained world models training-free: TD-MPC2 checkpoints land on the certificate's own scope taxonomy -- calibrated where strongly expansive (ratio 0.94-1.02), optimistic where weakly expansive, correctly abstaining where contracting -- a map a deployed monitor replicates cell-by-cell, out-of-sample. Across the official 1M-317M multitask ladder, calibration does not improve with parameters. On V-JEPA 2-AC (1B, real robot data) the measured cross-check correctly overrides an over-promising tangent spectrum -- the cross-validated audit, not the raw number, is the deployable object. Scale buys interpolation, not a calibrated horizon.

</details>

---

### [[20_Research/Papers/强化学习/$α$-fair_heterogeneous_agent_reinforcement_learning|$α$-fair heterogeneous agent reinforcement learning]]

![[assets/2606.13076_first_page.png|800]]

- **arXiv**: [2606.13076](https://arxiv.org/abs/2606.13076)
- **PDF**: https://arxiv.org/pdf/2606.13076
- **详细分析**: [[20_Research/Papers/强化学习/$α$-fair_heterogeneous_agent_reinforcement_learning|$α$-fair heterogeneous agent reinforcement learning]]
- **作者**: Yao-hua Franck Xu, Tayeb Lemlouma, Jean-Marie Bonnin, Arnaud Braud
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.4，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《$α$-fair heterogeneous agent reinforcement learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HATRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperation in multi-agent systems is typically optimized through utilitarian objectives that maximize overall efficiency but fail to account for reward distribution, often resulting in inequitable "leader-follower" dynamics. While fairness-based approaches encourage pro-social behaviors where every agent benefits from cooperation, many current algorithms - including those utilizing reward shaping - break the stationarity of Markov Games or lack rigorous theoretical guarantees. This creates a critical gap between fair objective methods and theoretically safe learning frameworks. We propose a novel framework that bridges $α$-fairness with Heterogeneous-Agent Trust Region Learning (HATRL), ensuring monotonic improvement and convergence toward Nash Equilibria. Our approach leverages a fair advantage function that dynamically weights agent utilities based on their expected returns, allowing the global objective to transition from purely utilitarian efficiency to $α$-fairness welfare based on the parameter $α$. We introduce two practical algorithms, $α$-fair HATRPO and $α$-fair HAPPO, and demonstrate through experiments in sequential social dilemmas like CleanUp and CommonHarvest that they perform better than HATRL's algorithms from a utilitarian point of view while achieving socially higher outcomes.

</details>

---

### [[20_Research/Papers/世界模型/EPM-JEPA_Operator-Side_Experience_Modulation_in_JEPA-Family_World_Models|EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models]]

![[assets/2606.12979_figure.png|800]]

- **arXiv**: [2606.12979](https://arxiv.org/abs/2606.12979)
- **PDF**: https://arxiv.org/pdf/2606.12979
- **详细分析**: [[20_Research/Papers/世界模型/EPM-JEPA_Operator-Side_Experience_Modulation_in_JEPA-Family_World_Models|EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models]]
- **作者**: Vedant Pandya
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: cs.LG

#### 研究背景与动机

《EPM-JEPA: Operator-Side Experience Modulation in JEPA-Family World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

JEPA-family world models use a static predictor whose weights do not adapt when test-time dynamics diverge from training. We compare two mechanisms for incorporating accumulated experience into a JEPA predictor under distribution shift: operand-side injection, where a compressed experience representation is added as a residual to the predictor's hidden state (EI-JEPA), and operator-side modulation, where the same representation generates low-rank weight deltas via LoRA applied to the predictor's weights (EPM-JEPA). On a pre-registered comparison (Moving MNIST, gravity shift), EPM-JEPA (D_shift^{n=50} = 0.7848 +/- 0.0078, three seeds) differs from EI-JEPA (0.8238) by delta = 4.74% - Outcome C: a null result - by our stated criterion, a valid outcome. As a secondary, non-pre-registered observation, EPM-JEPA improves 1.90% over a no-memory baseline (0.8000), consistently across seeds, while EI-JEPA underperforms the baseline, indicating the benefit is specific to weight-level modulation. Our primary contribution is a mechanism analysis: the D_shift^{n=50} trajectory reflects three independent dynamical processes - buffer cycling, EMA target drift, and an intrinsic LoRA settling transient of +0.021 - rather than convergence to equilibrium. These findings motivate PEM-JEPA, a physics-grounded successor addressing this dynamical-peak limitation.

</details>

---

### [[20_Research/Papers/强化学习/Graph_Reinforcement_Learning_for_Calibration-Aware_Quantum_Circuit_Routing|Graph Reinforcement Learning for Calibration-Aware Quantum Circuit Routing]]

![[assets/2606.12816_figure.png|800]]

- **arXiv**: [2606.12816](https://arxiv.org/abs/2606.12816)
- **PDF**: https://arxiv.org/pdf/2606.12816
- **详细分析**: [[20_Research/Papers/强化学习/Graph_Reinforcement_Learning_for_Calibration-Aware_Quantum_Circuit_Routing|Graph Reinforcement Learning for Calibration-Aware Quantum Circuit Routing]]
- **作者**: Yash Vardhan Tomar, Dheeraj Peddireddy, Vaneet Aggarwal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Graph Reinforcement Learning for Calibration-Aware Quantum Circuit Routing》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantum circuit routing is a key step in compiling programs for noisy intermediate-scale quantum processors. Routes that appear efficient by standard overhead metrics can still lose fidelity when they pass through poorly calibrated couplers. We study a calibration-aware graph reinforcement-learning router that uses same-day IBM Heron r2 calibration data to choose hardware-edge SWAPs. We train the policy with proximal policy optimization and evaluate it with exact simulated fidelity across nine Munich Quantum Toolkit (MQT) Bench circuits and three calibration snapshots. Across these evaluations, pooled mean exact fidelity is $0.727$, compared with $0.440$ for SABRE-best20 and $0.481$ for target-aware SABRE. Fidelity gains come with higher routed two-qubit counts and are concentrated in the 5q and 8q circuit families; under the fixed tree action graph, all 10q families favor SABRE-best20. Overall, our results show that calibration-aware learned routing can improve fidelity beyond gate-count-driven compilation.

</details>

---

### [[20_Research/Papers/强化学习/Individual_Control_Barrier_Functions-Guided_Diffusion_Model_for_Safe_Offline_Multi-Agent_Reinforcement_Learning|Individual Control Barrier Functions-Guided Diffusion Model for Safe Offline Multi-Agent Reinforcement Learning]]

![[assets/2606.12640_figure.png|800]]

- **arXiv**: [2606.12640](https://arxiv.org/abs/2606.12640)
- **PDF**: https://arxiv.org/pdf/2606.12640
- **详细分析**: [[20_Research/Papers/强化学习/Individual_Control_Barrier_Functions-Guided_Diffusion_Model_for_Safe_Offline_Multi-Agent_Reinforcement_Learning|Individual Control Barrier Functions-Guided Diffusion Model for Safe Offline Multi-Agent Reinforcement Learning]]
- **作者**: Qingyun Guo, Junyi Shi, Jianuo Huang, Tianyu Shi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Individual Control Barrier Functions-Guided Diffusion Model for Safe Offline Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning allows control policies to be learned directly from data without online interaction, making it suitable for safety-critical tasks. Recent studies have applied diffusion models to offline reinforcement learning to leverage their strong capacity for modeling complex data distributions. However, existing approaches primarily focus on single-agent settings, leaving the safety challenges in multi-agent environments largely unexplored. In this work, we propose a safe offline multi-agent reinforcement learning algorithm that embeds neural individual control barrier functions into the diffusion model to enhance safety during trajectory generation, with control policies recovered through inverse dynamics. We evaluate our algorithm across diverse benchmarks, demonstrating substantial safety improvements while maintaining competitive rewards.

</details>

---

### [[20_Research/Papers/具身智能/$μ$VLA_On_Recurrent_Memory_for_Partially_Observable_Manipulation_in_VLA_Models|$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models]]

![[assets/2606.12497_figure.png|800]]

- **arXiv**: [2606.12497](https://arxiv.org/abs/2606.12497)
- **PDF**: https://arxiv.org/pdf/2606.12497
- **详细分析**: [[20_Research/Papers/具身智能/$μ$VLA_On_Recurrent_Memory_for_Partially_Observable_Manipulation_in_VLA_Models|$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models]]
- **作者**: Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CronusVLA, MIKASA-Robo-VLA, MemoryVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a controlled isolation study of recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer with a small set of learnable memory tokens carried across timesteps and updated through self-attention, trained end to end with truncated backpropagation through time, with no auxiliary losses and no architectural changes. We instantiate this as $μ$VLA, a family of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory update rule (cross-step gradients or a detached EMA), so that recurrence is the only varying factor. On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring different memory structure, performance remains near baseline. On LIBERO, the strongest recurrent variant achieves 96.2% average success, indicating no regression under full observability. We interpret these results as a calibration of the capability envelope of minimal in-backbone recurrence, identifying the regime in which it is sufficient and the regime where additional memory structure is required. Demos and videos can be found in https://avanturist322.github.io/mu-vla/.

</details>

---
