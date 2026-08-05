# cs.LG | Machine Learning | 2026-08-03

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/Convergence_and_Regret_of_the_Policy_Gradient_for_Multi-Armed_Bandits_in_Diffusion_Environment|Convergence and Regret of the Policy Gradient for Multi-Armed Bandits in Diffusion Environment]]

![[assets/2607.29593_first_page.png|800]]

- **arXiv**: [2607.29593](https://arxiv.org/abs/2607.29593)
- **PDF**: https://arxiv.org/pdf/2607.29593
- **详细分析**: [[20_Research/Papers/强化学习/Convergence_and_Regret_of_the_Policy_Gradient_for_Multi-Armed_Bandits_in_Diffusion_Environment|Convergence and Regret of the Policy Gradient for Multi-Armed Bandits in Diffusion Environment]]
- **作者**: Yanwei Jia, Du Ouyang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Convergence and Regret of the Policy Gradient for Multi-Armed Bandits in Diffusion Environment》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies the policy gradient update for a multi-arm bandit problem in diffusion environment that is described by a stochastic differential equation (SDE) under the continuous-time reinforcement learning framework by Wang et al. (2020), Jia and Zhou (2022b). With the logit parameterization for the stochastic policy, we show that it converges almost surely to the optimal arm under an arbitrary constant learning rate. Furthermore, we derive the non-asymptotic regret upper bound when the constant learning rate is below a time-invariant threshold; and the regret bound has order $O(\log T)$. We improve the analysis in Lattimore (2026a) for the same SDE by constructing a novel Lyapunov function and demonstrate the transparency of analyzing policy gradient using the tools in SDEs. In addition, the same Lyapunov function is also helpful in analyzing the discrete-time policy gradient algorithm.

</details>

---

### [[20_Research/Papers/大模型/Transcript-Managed_Transformers_Monotone_Multi-Agent_Collapse_and_Universality_with_Two_Pop-Enabled_Transcripts|Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts]]

![[assets/2607.29496_first_page.png|800]]

- **arXiv**: [2607.29496](https://arxiv.org/abs/2607.29496)
- **PDF**: https://arxiv.org/pdf/2607.29496
- **详细分析**: [[20_Research/Papers/大模型/Transcript-Managed_Transformers_Monotone_Multi-Agent_Collapse_and_Universality_with_Two_Pop-Enabled_Transcripts|Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts]]
- **作者**: Sergey Salishev
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study transcript management for fixed, finite-precision causal Transformers. A transcript is partitioned into channels of bounded blocks. Each transition consults a fixed visible suffix and may append one block, leaving the model, weights, and token protocol unchanged. The operation $P_c:=\PopContext(c)$ deletes the newest block on channel $c$ and exposes its predecessor. We model the layer by the Transcript-Managed Transducer $\TMTn{k}$: one finite controller, $k$ channels, and per-round actions from stay, push, and pop under a caller-driven status map. Fixed visible windows encode as finite symbols. The pop-free Restricted Transcript-Managed Transducer $\RTMTn{k}$ is the standard append-only layer and, for every fixed $k$, realizes exactly the deterministic finite-state transductions. The same holds for every fixed finite agent population under a monotone protocol that appends, routes, and copies visible blocks. Admitting $\{P_c\}_{c=1}^k$ restores pop. Newest-first, a pop-enabled channel is a stack; compiling to the Hopcroft--Ullman presentation transfers the classical hierarchy: $\DCFL$ for $k=1$ and $\RE$ for every $k\ge2$. Orchestrated one-channel agents match one controller with $k$ channels, so two pop-enabled transcripts---in one agent or two---suffice for universality. Simulation costs and invariance to fixed block size and visible radius are stated. The bounds fix precision, alphabets, blocks, visibility, controller state, and population; growing exact context, hidden-block access, writable stores, and unbounded \textbf{Spawn} add further state.

</details>

---

### [[20_Research/Papers/强化学习/OnlineCache_Learning_Dynamic_Caching_Policies_with_Error_Correction_for_Efficient_Diffusion_Inference|OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference]]

![[assets/2607.29398_figure.png|800]]

- **arXiv**: [2607.29398](https://arxiv.org/abs/2607.29398)
- **PDF**: https://arxiv.org/pdf/2607.29398
- **详细分析**: [[20_Research/Papers/强化学习/OnlineCache_Learning_Dynamic_Caching_Policies_with_Error_Correction_for_Efficient_Diffusion_Inference|OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference]]
- **作者**: Zhikang Xie, Xichen Ye, Yifan Wu, Haoshen Yu, Li chenan, Peizhu Gong, Weizhong Zhang, Cheng Jin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models have revolutionized generative tasks but incur high latency due to iterative denoising. While cache-based strategies accelerate inference by reusing intermediate features, they largely rely on static, sample-agnostic schedules. We argue that this rigidity overlooks two facts empirically validated in this paper: (i) generation difficulty varies across prompts, requiring adaptive resource allocation--complex inputs demand more computation while simpler ones require less; (ii) error sensitivity fluctuates across timesteps, where static policies may cache high-error steps or waste computation on low-error ones. We therefore propose OnlineCache, a dynamic caching framework that jointly learns when to cache and how to correct approximation errors. We leverage policy gradient to train a lightweight network for adaptive speed-quality trade-offs, and incorporate a learnable corrector to mitigate caching-induced errors. Both modules are jointly optimized under a bilevel optimization framework, with the policy targeting global generation quality and the corrector minimizing local errors. Our method automatically allocates computational resources across both samples and timesteps, improving overall generation quality. Extensive experiments demonstrate clear superiority. On FLUX.1-dev model, OnlineCache achieves nearly 3 speedup while preserving generation fidelity. On DiT and CogVideoX, it similarly delivers competitive acceleration without compromising quality; across all scenarios, it consistently outperforms existing cache-based acceleration baselines.

</details>

---

### [[20_Research/Papers/大模型/Simulation_Code_Generation_for_Fluid_Systems_using_Large_Language_Models_Benchmarking_Models_and_Prompting_Strategies|Simulation Code Generation for Fluid Systems using Large Language Models: Benchmarking Models and Prompting Strategies]]

![[assets/2607.29389_figure.png|800]]

- **arXiv**: [2607.29389](https://arxiv.org/abs/2607.29389)
- **PDF**: https://arxiv.org/pdf/2607.29389
- **详细分析**: [[20_Research/Papers/大模型/Simulation_Code_Generation_for_Fluid_Systems_using_Large_Language_Models_Benchmarking_Models_and_Prompting_Strategies|Simulation Code Generation for Fluid Systems using Large Language Models: Benchmarking Models and Prompting Strategies]]
- **作者**: Jan Marius Stürmer, Jascha Knack, Tobias Koch, Andreas Weinmann
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Simulation Code Generation for Fluid Systems using Large Language Models: Benchmarking Models and Prompting Strategies》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have demonstrated a strong ability to generate syntactically correct code from natural-language specifications. In this study, we explore how LLMs can be harnessed to automatically translate a neutral graph representation of fluid system models into executable code for two widely adopted simulation environments: the Python library WNTR and the Modelica Standard Library. We conduct a systematic comparison of ten state-of-the-art LLMs and six prompting strategies that differ in the contextual information supplied (e.g., code or documentation). For each configuration we assess the generated code using a suite of software-quality metrics and we validate the functional fidelity of the resulting simulation models by reproducing benchmark fluid system scenarios. Our findings offer concrete guidance for researchers and engineers seeking to integrate LLM-driven code synthesis into model-based design pipelines. While the best-performing configurations achieve acceptable syntactic quality, we observe substantial gaps remain in simulation fidelity.

</details>

---

### [[20_Research/Papers/强化学习/Sample_Efficient_Hierarchical_Reinforcement_Learning_via_Best_Policy_Identification|Sample Efficient Hierarchical Reinforcement Learning via Best Policy Identification]]

![[assets/2607.29294_first_page.png|800]]

- **arXiv**: [2607.29294](https://arxiv.org/abs/2607.29294)
- **PDF**: https://arxiv.org/pdf/2607.29294
- **详细分析**: [[20_Research/Papers/强化学习/Sample_Efficient_Hierarchical_Reinforcement_Learning_via_Best_Policy_Identification|Sample Efficient Hierarchical Reinforcement Learning via Best Policy Identification]]
- **作者**: Anders Jonsson, Emilie Kaufmann, Gianmarco Tedeschi, Lorenzo Steccanella
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Sample Efficient Hierarchical Reinforcement Learning via Best Policy Identification》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：HBPI-UCRL, HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present HBPI-UCRL, a model-based algorithm for hierarchical reinforcement learning (HRL) that learns high-level and low-level policies in parallel. HBPI-UCRL exploits the fact that a high-level transition corresponds to a multi-step transition at the low level. We introduce two conditions on the low-level dynamics that are sufficient to make parallel HRL learnable. When these conditions hold, we prove that HBPI-UCRL has a polynomial sample complexity in the problem parameters. In the sparse-reward, goal-directed setting, our sample complexity upper bound for HBPI-UCRL is strictly lower than that of its non-hierarchical counterpart, providing theoretical justification for the empirical success of HRL.

</details>

---

### [[20_Research/Papers/大模型/Overcoming_the_Weakest-Link_Effect_in_LLM-Driven_Program_Optimization_via_Heterogeneous_Edit_Recombination|Overcoming the Weakest-Link Effect in LLM-Driven Program Optimization via Heterogeneous Edit Recombination]]

![[assets/2607.28947_figure.png|800]]

- **arXiv**: [2607.28947](https://arxiv.org/abs/2607.28947)
- **PDF**: https://arxiv.org/pdf/2607.28947
- **详细分析**: [[20_Research/Papers/大模型/Overcoming_the_Weakest-Link_Effect_in_LLM-Driven_Program_Optimization_via_Heterogeneous_Edit_Recombination|Overcoming the Weakest-Link Effect in LLM-Driven Program Optimization via Heterogeneous Edit Recombination]]
- **作者**: Jingwen Fu, Zhen Liu, Yuhan Liu, He Zhang, Nanning Zheng
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.8（加权：大模型 0.4，机器人 0.4）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Overcoming the Weakest-Link Effect in LLM-Driven Program Optimization via Heterogeneous Edit Recombination》归入 大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used to solve complex problems by searching over program space, offering a general paradigm for scientific problems that can be naturally represented and solved as programs. Despite recent progress, identifying effective optimization directions for a candidate program remains challenging. By analogy with automatic differentiation, existing methods typically guide the search using a textual ``gradient'': a first-order update direction expressed as textual edits. Such gradients are inferred either from previously evaluated programs or from LLM-generated feedback on the implicit program-score mapping. However, these estimates become increasingly unreliable as the program--score mapping grows more complex, limiting their practical utility. We argue that explicit gradients are not essential for effective program optimization. Leveraging their prior knowledge, LLMs can propose plausible atomic edits directly from the current program, thereby enabling a zeroth-order optimization strategy. However, zeroth-order search suffers from a \textit{weakest-link effect}: when a bundle of edits is accepted or rejected as a whole, a single harmful edit can negate the benefits of all remaining edits. To address this issue, we introduce HERO, a program optimizer that prompts an LLM to generate diverse, non-overlapping atomic edits and then systematically selects and composes them into coherent program improvements using evaluator scores. We evaluate HERO across algorithmic problems, strategy games, the design of LLM-based agentic systems, and robotic path planning. Across these domains, HERO consistently discovers higher-scoring programs and converges substantially faster than prior LLM-based optimizers, while consuming fewer tokens.

</details>

---

### [[20_Research/Papers/世界模型/Latent_Lie-Poisson_Neural_Networks_(LLPNNs)_Discovering_the_motion_of_Lie-Poisson_systems_through_observable_data_and_latent_dynamics|Latent Lie-Poisson Neural Networks (LLPNNs): Discovering the motion of Lie-Poisson systems through observable data and latent dynamics]]

![[assets/2607.28939_figure.png|800]]

- **arXiv**: [2607.28939](https://arxiv.org/abs/2607.28939)
- **PDF**: https://arxiv.org/pdf/2607.28939
- **详细分析**: [[20_Research/Papers/世界模型/Latent_Lie-Poisson_Neural_Networks_(LLPNNs)_Discovering_the_motion_of_Lie-Poisson_systems_through_observable_data_and_latent_dynamics|Latent Lie-Poisson Neural Networks (LLPNNs): Discovering the motion of Lie-Poisson systems through observable data and latent dynamics]]
- **作者**: Vakhtang Putkaradze
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Latent Lie-Poisson Neural Networks (LLPNNs): Discovering the motion of Lie-Poisson systems through observable data and latent dynamics》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Structure-preserving neural networks are essential for the long-term prediction of Hamiltonian systems from data. Many important Hamiltonian systems in mechanics and control admit symmetry reduction to Lie--Poisson systems, including rigid bodies, underwater vehicles, fluids, plasmas, and optimal control problems. A fundamental challenge in learning such systems is that their dynamics evolve in momentum variables that are typically unobservable, while available data consist only of observable quantities such as configurations and velocities. In optimal control applications, the situation is further complicated because the latent variables contain unobservable co-states and the Hamiltonian may be degenerate, preventing the existence of a corresponding Lagrangian and rendering the encoder-decoder approaches inapplicable. We introduce Latent Lie--Poisson Neural Networks (LLPNNs), a structure-preserving framework for learning Lie--Poisson dynamics directly from observable data. The proposed approach exploits three geometric ingredients: (i) learning either a Hamiltonian decoder or a pseudo-Lagrangian encoder on the active variables, (ii) constructing latent trajectories through a universal Noether invariant arising from Lie--Poisson symmetry reduction, and (iii) reconstructing observable and latent dynamics through Lie--Poisson flows combined with Magnus-based Lie-group updates. The resulting method preserves the geometric structure and is applicable to both regular and degenerate Hamiltonian systems. We demonstrate the method on three examples: a generalized rigid body on SO(3), Kirchhoff's underwater vehicle on SE(3), and an optimal-control problem for interacting vehicles on $SE(2)^N$. Numerical experiments show excellent long-term predictive accuracy, strong robustness to noise, and competitive performance using only modest datasets and lightweight neural-network architectures.

</details>

---

### [[20_Research/Papers/大模型/Open-Source_LLM-Driven_Formal_Verification_A_Multi-Agent_Pipeline_for_RTL_Repair|Open-Source LLM-Driven Formal Verification: A Multi-Agent Pipeline for RTL Repair]]

![[assets/2607.28877_figure.png|800]]

- **arXiv**: [2607.28877](https://arxiv.org/abs/2607.28877)
- **PDF**: https://arxiv.org/pdf/2607.28877
- **详细分析**: [[20_Research/Papers/大模型/Open-Source_LLM-Driven_Formal_Verification_A_Multi-Agent_Pipeline_for_RTL_Repair|Open-Source LLM-Driven Formal Verification: A Multi-Agent Pipeline for RTL Repair]]
- **作者**: Ha Trung Tran
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Open-Source LLM-Driven Formal Verification: A Multi-Agent Pipeline for RTL Repair》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Verification consumes the majority of modern chip design effort, yet the formal verification tools that provide mathematical guarantees of correctness remain expensive and restrictively licensed. While large language models (LLMs) have shown promise for hardware design, existing approaches to RTL repair validate their results through simulation - which exercises only a subset of inputs - or rely on commercial tools, and few combine formal proof with an entirely open-source toolchain. In this paper, we present a multi-agent pipeline that couples an LLM with an open-source formal backend (Yosys, SymbiYosys, and Z3) to repair RTL through counterexample-guided iteration: the framework generates formal properties, verifies the design, and feeds counterexamples back to the LLM until the design is proved correct by k-induction or an iteration budget is exhausted. Through an ALU case study, we show that the pipeline can detect and repair a real functional bug with a formal proof of correctness. Across a six-benchmark suite, one design is repaired reliably, and we characterize four distinct failure modes: bounded-cover vacuity, specification ambiguity, temporal-logic bugs, and multi-property pressure. We frame this work as a feasibility study with a detailed failure analysis, and additionally report a practical limitation of the Yosys bind directive relevant to the open-source formal verification community.

</details>

---

### [[20_Research/Papers/具身智能/When_Unlearning_Fails_Reliable_Data_Deletion_under_Post-Training_in_Agent_Networks|When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks]]

![[assets/2607.28829_figure.png|800]]

- **arXiv**: [2607.28829](https://arxiv.org/abs/2607.28829)
- **PDF**: https://arxiv.org/pdf/2607.28829
- **详细分析**: [[20_Research/Papers/具身智能/When_Unlearning_Fails_Reliable_Data_Deletion_under_Post-Training_in_Agent_Networks|When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks]]
- **作者**: Zihao Ding, Jun Huang, Liang Dong
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.4）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks》归入 大模型、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MiniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-improving federated agent networks keep training after deployment by collecting new trajectories with the current policy and feeding them back into later rounds. This closed loop makes unlearning harder than a one-time model repair. When a data owner requests deletion, the target data may have already shaped later retained trajectories, so retraining or model-side unlearning can leave an influence echo that returns as the network continues to operate. We show that this echo survives retained-data retraining, grows with the amount of forget-shaped retained data, and can be traced from deployment, collection, and aggregation records. To address this problem, we propose MUTE, a Muting Unlearned Trajectories' Echoes method for reliable deletion in self-improving federated agent networks. MUTE estimates downstream influence from a lightweight server ledger, removes the current residue through a forget-retain update, contains high-influence retained trajectories through quarantine or down-weighting, and audits later behavior to schedule additional erasure under an uplink budget. Experiments on LIBERO with two vision-language-action backbones, three deletion granularities, and a physical Jetson-based edge testbed show that MUTE keeps behavioral leakage and influence regeneration low while preserving task utility and using much less communication than full retraining.

</details>

---

### [[20_Research/Papers/大模型/Distilling_Knowledge_from_Large_Language_Models_into_Lightweight_Reinforcement_Learning_Agents_for_Autonomous_Cyber_Operations|Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations]]

![[assets/2607.28826_figure.png|800]]

- **arXiv**: [2607.28826](https://arxiv.org/abs/2607.28826)
- **PDF**: https://arxiv.org/pdf/2607.28826
- **详细分析**: [[20_Research/Papers/大模型/Distilling_Knowledge_from_Large_Language_Models_into_Lightweight_Reinforcement_Learning_Agents_for_Autonomous_Cyber_Operations|Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations]]
- **作者**: Konur Tholl, François Rivest, Mariam El Mezouar, Adrian Taylor, Ranwa Al Mallah
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.92（加权：大模型 0.8，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Distilling Knowledge from Large Language Models into Lightweight Reinforcement Learning Agents for Autonomous Cyber Operations》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LLM-to-RL, TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous Cyber Operations (ACO) are increasingly important for defending enterprise networks as cyber threats continue to evolve in sophistication. ACO applications commonly employ Reinforcement Learning (RL) agents to learn defensive behaviors through interaction with environments. However, RL agents typically require extensive exploration during training, often resulting in unstable behavior and poor initial decision-making before converging toward effective defense strategies. In this work, we investigate the use of a Large Language Model (LLM) to improve autonomous defensive decision-making within an ACO environment. Through prompt engineering rather than fine-tuning, we demonstrate that an 8-billion parameter LLM pretrained on cybersecurity data can outperform a baseline RL agent in a modified CybORG CAGE Challenge 2 environment. We then propose an online policy distillation framework that transfers the LLM's defensive policy into a lightweight RL agent containing only 64,910 parameters, reducing model size by several orders of magnitude while maintaining effective defensive capabilities. This provides a pathway toward operationalizing frontier cybersecurity models within lightweight, deployable agents. To evaluate transferability, we construct CybORG scenarios ranging from 4 to 12 hosts and assess the approach across varying network configurations. We also evaluate teacher-guided RL stabilization strategies and observe that none consistently surpass the optimized teacher policy, suggesting policy-alignment limitations between reward-driven RL optimization and teacher-guided defense strategies. Our results demonstrate the potential of cybersecurity-focused LLMs as sources of expertise for autonomous cyber defense, while policy distillation provides a practical path toward operationalizing frontier cybersecurity models within efficient, scalable agents.

</details>

---

### [[20_Research/Papers/具身智能/NeuroSynth_A_Biologically_Inspired_Continual_Reinforcement_Learning_Architecture_for_Mitigating_Catastrophic_Forgetting|NeuroSynth: A Biologically Inspired Continual Reinforcement Learning Architecture for Mitigating Catastrophic Forgetting]]

![[assets/2607.28663_figure.png|800]]

- **arXiv**: [2607.28663](https://arxiv.org/abs/2607.28663)
- **PDF**: https://arxiv.org/pdf/2607.28663
- **详细分析**: [[20_Research/Papers/具身智能/NeuroSynth_A_Biologically_Inspired_Continual_Reinforcement_Learning_Architecture_for_Mitigating_Catastrophic_Forgetting|NeuroSynth: A Biologically Inspired Continual Reinforcement Learning Architecture for Mitigating Catastrophic Forgetting]]
- **作者**: Yash Kini
- **cs 子类**: cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《NeuroSynth: A Biologically Inspired Continual Reinforcement Learning Architecture for Mitigating Catastrophic Forgetting》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial Intelligence (AI) systems often perform well on isolated tasks but struggle under continual learning conditions, where training on new tasks can overwrite previously acquired knowledge, a failure mode known as catastrophic forgetting. Biological learning systems reduce this interference through complementary memory processes involving rapid hippocampal encoding and slower cortical consolidation. This study introduces NeuroSynth, a brain-inspired continual reinforcement learning architecture designed to mitigate catastrophic forgetting through a dual-pathway consolidation mechanism. NeuroSynth separates rapid task acquisition from long-term retention using distinct "plan" and "habit" pathways combined with replay and knowledge distillation. NeuroSynth was evaluated against Proximal Policy Optimization (PPO) and Elastic Weight Consolidation (EWC) across three sequential navigation tasks with changing goal locations in a non-revisitation continual learning setting. Across six independent seeds, NeuroSynth preserved substantially more early-task knowledge than PPO after sequential training, achieving 18.00% Task A success rate compared to 0.33% for PPO (p = 0.014929, Cohen's d = 1.49) and 35.33% Task B success rate compared to 0.00% for PPO (p = 0.002376, Cohen's d = 2.31). NeuroSynth also demonstrated higher final Task C performance than EWC, achieving 9.00% compared to 2.00% (p = 0.226643, Cohen's d = 0.56), indicating a moderate but not statistically significant advantage. These findings suggest that biologically inspired consolidation mechanisms may improve the stability-plasticity balance in continual reinforcement learning systems.

</details>

---
