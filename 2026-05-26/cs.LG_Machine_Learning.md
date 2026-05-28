# cs.LG | Machine Learning | 2026-05-26

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/强化学习/Global_Convergence_of_Wasserstein_Policy_Gradient_for_Entropy-Regularized_Reinforcement_Learning|Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning]]

![[assets/2605.26078_first_page.png|800]]

- **arXiv**: [2605.26078](https://arxiv.org/abs/2605.26078)
- **PDF**: https://arxiv.org/pdf/2605.26078
- **详细分析**: [[20_Research/Papers/强化学习/Global_Convergence_of_Wasserstein_Policy_Gradient_for_Entropy-Regularized_Reinforcement_Learning|Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning]]
- **作者**: Zhaoyu Zhu, Rui Gao, Shuang Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 1.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wasserstein policy gradient (WPG) is a policy optimization method for reinforcement learning (RL) that exploits the optimal-transport geometry of action distributions. For the entropy-regularized RL objective, WPG evolves each state-conditional policy by transporting it along the action gradient of the soft Q-function together with a Langevin-type diffusion. Despite its appeal for continuous-control problems, its global convergence properties remain poorly understood. Standard Langevin analyses do not directly apply, because the RL objective depends on the policy through the Bellman recursion rather than through a static convex functional, and the Langevin drift is determined by the soft Q-function, whose regularity must be controlled along the policy iterates. In this paper, we develop a global convergence theory for WPG by exploiting the Bellman structure of entropy-regularized RL. We show that the role usually played by convexity can be replaced by a Bellman-based argument: the soft Bellman residual admits a statewise KL representation with respect to a Gibbs policy; Bellman contraction relates this residual to the global optimality gap; and a Bellman resolvent identity connects value improvement to relative Fisher information. Combined with a uniform log-Sobolev inequality (LSI) for the evolving Gibbs family, these ingredients yield a distributional Polyak--Łojasiewicz condition. We further establish the regularity and uniform bounds needed to control the discretization error, thereby obtaining geometric contraction up to a discretization bias. Conceptually, our analysis shows that although entropy-regularized RL is not convex in the usual flat sense, the Bellman recursion induces a favorable Polyak--Lojasiewicz-type (PL) geometry that supports global convergence of WPG.

</details>

---

### [[20_Research/Papers/强化学习/Latent_Representation_Alignment_for_Offline_Goal-Conditioned_Reinforcement_Learning|Latent Representation Alignment for Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2605.25740_figure.png|800]]

- **arXiv**: [2605.25740](https://arxiv.org/abs/2605.25740)
- **PDF**: https://arxiv.org/pdf/2605.25740
- **详细分析**: [[20_Research/Papers/强化学习/Latent_Representation_Alignment_for_Offline_Goal-Conditioned_Reinforcement_Learning|Latent Representation Alignment for Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Hyungkyu Kang, Byeongchan Kim, Min-hwan Oh
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Latent Representation Alignment for Offline Goal-Conditioned Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GCRL, OGBench, QRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning (GCRL) provides a practical framework for obtaining goal-reaching policies from fixed datasets. However, learning a reliable goal-conditioned value function in long-horizon tasks remains challenging. In this paper, we identify erroneous generalization in goal-conditioned value functions as a fundamental bottleneck, and demonstrate that appropriate inductive bias in the value function is crucial for addressing the bottleneck. Building on these findings, we propose Latent-Aligned Value Learning (LAVL), an offline GCRL algorithm that integrates latent-representation-based value generalization with hierarchical planning in a unified framework. Extensive experiments on OGBench demonstrate that LAVL consistently outperforms existing offline GCRL methods, achieving the highest performance on 20 out of 22 datasets. Notably, LAVL exhibits strong performance in long-horizon tasks and trajectory stitching datasets, where prior methods suffer significant performance degradation. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/DeepSeekMath_Meets_Order_Book_Group-Aware_Policy_Optimization_for_High-Frequency_Directional_Trading|DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading]]

![[assets/2605.25527_figure.png|800]]

- **arXiv**: [2605.25527](https://arxiv.org/abs/2605.25527)
- **PDF**: https://arxiv.org/pdf/2605.25527
- **详细分析**: [[20_Research/Papers/强化学习/DeepSeekMath_Meets_Order_Book_Group-Aware_Policy_Optimization_for_High-Frequency_Directional_Trading|DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading]]
- **作者**: Sayak Charabarty, Souradip Pal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《DeepSeekMath Meets Order Book: Group-Aware Policy Optimization for High-Frequency Directional Trading》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies reinforcement learning for high-frequency trading on limit order books by pairing an Order-Flow-based state model with policy-gradient methods. Instead of value-based RL techniques like tabular Q-learning, our approach deploys policy-based methods like vanilla PPO and DeepSeekMath-inspired variants like GRPO and GSPO, that use group-normalized updates and downside-aware shaping. On backtests with financial assets AMZN, AAPL, and GOOG under a simplified backtesting setup based on spread-scaled rewards, these new policies improve net average PnL, profitability, and drawdown over the Q-Learning baseline. Our results show that (1) Order-Flow signals are an adequate state for policy RL and (2) group-aware PPO surrogates are preferable over value-based baselines.

</details>

---

### [[20_Research/Papers/强化学习/Counterfactually_Safe_Reinforcement_Learning|Counterfactually Safe Reinforcement Learning]]

![[assets/2605.25114_figure.png|800]]

- **arXiv**: [2605.25114](https://arxiv.org/abs/2605.25114)
- **PDF**: https://arxiv.org/pdf/2605.25114
- **详细分析**: [[20_Research/Papers/强化学习/Counterfactually_Safe_Reinforcement_Learning|Counterfactually Safe Reinforcement Learning]]
- **作者**: Jingyi Li, Peng Wu, Chengchun Shi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Counterfactually Safe Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning algorithms are generally designed to maximize the expected return across a population. However, a policy that is optimal on average may be suboptimal for certain individuals, leading to potential safety concerns. To address this, we first formalize the notion of individual harm from a counterfactual perspective and define harm as the event in which a chosen action results in a strictly worse outcome than a baseline alternative. We then propose a general two-stage procedure for learning policies that maximize the expected return while accounting for individual harm. We further establish the finite-sample properties of the learned policy, derive an upper bound on its sub-optimality gap, and show that the harm rate remains well-controlled. Numerical experiments on both simulated and real-world datasets demonstrate the effectiveness of the proposed approach.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Laser_Additive_Manufacturing_Scan-Order_Optimisation_A_Bilevel_Proxy--FEA_Diagnostic_Framework_for_Reward_and_Wor|Reinforcement Learning for Laser Additive Manufacturing Scan-Order Optimisation: A Bilevel Proxy--FEA Diagnostic Framework for Reward and World-Model Diagnosis]]

![[assets/2605.25063_figure.png|800]]

- **arXiv**: [2605.25063](https://arxiv.org/abs/2605.25063)
- **PDF**: https://arxiv.org/pdf/2605.25063
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Laser_Additive_Manufacturing_Scan-Order_Optimisation_A_Bilevel_Proxy--FEA_Diagnostic_Framework_for_Reward_and_Wor|Reinforcement Learning for Laser Additive Manufacturing Scan-Order Optimisation: A Bilevel Proxy--FEA Diagnostic Framework for Reward and World-Model Diagnosis]]
- **作者**: Xian Wu, Haoran Li, Dongbin Zhao, Ruiyao Zhang, Yuanqi Chu, Bin Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning for Laser Additive Manufacturing Scan-Order Optimisation: A Bilevel Proxy--FEA Diagnostic Framework for Reward and World-Model Diagnosis》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning offers a promising approach for scan-order optimisation in laser additive manufacturing, where sequential scan decisions critically influence thermal accumulation, residual stress, distortion, and final part quality. A central challenge in applying RL to this domain lies in reward and world-model fidelity: full finite-element analysis is computationally prohibitive for dense in-the-loop evaluation, while cheap thermo-inspired proxy metrics, though efficient, may capture only partial aspects of the true thermo-mechanical objectives. This paper investigates a bilevel Proxy--FEA diagnostic framework for reward and world-model diagnosis in reinforcement-learning-guided scan-order optimisation. The lower level employs lightweight scan-path and thermo-inspired proxies for rapid candidate generation and preliminary policy-side screening, while the upper level utilises sparse Abaqus FEA simulations to provide simulation-based reference labels. The framework is examined on a simplified whole-track heating LDED32 stripe benchmark comprising ten representative scan strategies. Final-cooling residual Mises stress, U3 vertical distortion, and PEEQ plasticity metrics reveal an observed stress--distortion trade-off rather than a single monotonic quality objective. Within the evaluated set, the center_out strategy emerges as a robust compromise candidate, while raster_left_to_right and edge_in form opposing endpoints of the trade-off. Proxy--FEA alignment analysis shows that current cheap path-based metrics predominantly capture distortion-related (U3) behaviour and exhibit only weak correlation with the sparse FEA reference labels. These findings highlight that proxy-only reward designs risk misalignment in future RL training and underscore the value of sparse FEA reference signals for diagnostic-guided reward and world-model refinement prior to large-scale policy optimisation.

</details>

---

### [[20_Research/Papers/强化学习/A_perspective_on_fluid_mechanical_environments_for_challenges_in_reinforcement_learning|A perspective on fluid mechanical environments for challenges in reinforcement learning]]

![[assets/2605.25011_figure.png|800]]

- **arXiv**: [2605.25011](https://arxiv.org/abs/2605.25011)
- **PDF**: https://arxiv.org/pdf/2605.25011
- **详细分析**: [[20_Research/Papers/强化学习/A_perspective_on_fluid_mechanical_environments_for_challenges_in_reinforcement_learning|A perspective on fluid mechanical environments for challenges in reinforcement learning]]
- **作者**: Shruti Mishra, Michael Chang, Vamsi Spandan, Shmuel M. Rubinstein
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《A perspective on fluid mechanical environments for challenges in reinforcement learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the challenge of developing agents that efficiently interact with high-dimensional, evolving environments, towards a view of practical reinforcement learning (RL) agents interacting with open worlds, of which they witness and affect only a small part. We argue that canonical fluid mechanics problems, and their simulations, present a compelling testbed for the development of such methods. These problems arise in nonlinear instabilities, where small disturbances can grow to transform the dynamics of a system. Nonlinear instabilities represent several open scientific challenges with industrial applications -- the droplet breakup of a liquid jet, mixing at an interface between two fluids, and the appearance of unusually tall rogue waves in the ocean. In these settings, agents may leverage preserved representations across the changing dynamics to learn efficiently. We present two problem descriptions of agents interacting with a fluid mechanical environment, and describe the state and action spaces, and reward functions, for these agents. For these examples, we specify the aspects of the environment which are nonstationary and the preserved invariances. We note Dedalus and JAX-CFD as open-source simulators that can be used for the development of reinforcement learning methods (Burns et al., 2016; Kochkov et al., 2021)) We demonstrate the use of Dedalus for environment generation by creating RL agents that learn to navigate in a stationary environment that is simulated using Dedalus. This sets the stage for future development of RL agents that learn to meaningfully interact with simulated environments that represent scientific challenges in natural and industrial flows.

</details>

---

### [[20_Research/Papers/具身智能/Convex-Neural_RRT_Fast_and_Reliable_Learning-Guided_Sampling_for_High-Quality_Robot_Path_Planning|Convex-Neural RRT*: Fast and Reliable Learning-Guided Sampling for High-Quality Robot Path Planning]]

![[assets/2605.25006_first_page.png|800]]

- **arXiv**: [2605.25006](https://arxiv.org/abs/2605.25006)
- **PDF**: https://arxiv.org/pdf/2605.25006
- **详细分析**: [[20_Research/Papers/具身智能/Convex-Neural_RRT_Fast_and_Reliable_Learning-Guided_Sampling_for_High-Quality_Robot_Path_Planning|Convex-Neural RRT*: Fast and Reliable Learning-Guided Sampling for High-Quality Robot Path Planning]]
- **作者**: Hichem Cheriet, Badra Khellat Kihel, Samira Chouraqui, Bara J. Emran
- **cs 子类**: cs.LG, cs.NE, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，机器人 2.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Convex-Neural RRT*: Fast and Reliable Learning-Guided Sampling for High-Quality Robot Path Planning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sampling-based algorithms for robot path planning offer probabilistic completeness and strong empirical convergence properties across environments with diverse obstacle configurations. However, in practice, these methods often require many iterations to obtain high-quality solutions. This paper proposes Convex-Neural RRT*, an enhanced RRT* variant that incorporates neural guidance to predict informative waypoint regions near high-quality paths. Convex candidate regions are extracted from these predictions, enabling the planner to concentrate exploration on geometrically relevant areas while preserving global exploration. The proposed algorithm is evaluated against Neural RRT*, Neural Informed RRT*, classical RRT*, and LTA* across three environment types and 18 benchmark maps. Experimental results show that Convex-Neural RRT* reduces computation time by 30-75% compared to neural-guided variants and up to 88-98% relative to LTA*, while achieving an average path length reduction of approximately 5% compared to classical RRT*, with larger improvements observed in complex environments. The method also maintains an overall success rate above 99% across varying obstacle densities. These findings indicate that convex-guided neural sampling provides an effective balance between computational efficiency and solution quality, supporting its applicability to time-sensitive robotic navigation tasks.

</details>

---

### [[20_Research/Papers/具身智能/Learning,_locomotion,_and_navigation_of_soft_synthetic_snakes_in_three-dimensional,_heterogeneous_environments|Learning, locomotion, and navigation of soft synthetic snakes in three-dimensional, heterogeneous environments]]

![[assets/2605.24985_first_page.png|800]]

- **arXiv**: [2605.24985](https://arxiv.org/abs/2605.24985)
- **PDF**: https://arxiv.org/pdf/2605.24985
- **详细分析**: [[20_Research/Papers/具身智能/Learning,_locomotion,_and_navigation_of_soft_synthetic_snakes_in_three-dimensional,_heterogeneous_environments|Learning, locomotion, and navigation of soft synthetic snakes in three-dimensional, heterogeneous environments]]
- **作者**: Xiaotian Zhang, Ali Albazroun, Tixian Wang, Songyuan Cui, Prashant G. Mehta, Mattia Gazzola
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.32（加权：具身智能 1.5，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning, locomotion, and navigation of soft synthetic snakes in three-dimensional, heterogeneous environments》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Limbless terrestrial animals exhibit exceptional locomotor versatility and control, currently unmatched by engineered counterparts. Here, we introduce a computational framework that enables soft synthetic snakes to navigate unstructured, heterogeneous 3D terrains. Our approach is grounded in bio-inspired actuation and sensing models that reduce the control complexity inherent to high-degree-of-freedom, continuum bodies. These models are integrated into a reinforcement learning architecture to derive environment-traversing policies. Training first occurs in simplified, homogeneous terrains to learn locomotion primitives. These are then composed into adaptive strategies for complex landscapes. We demonstrate robustness by deploying a snake in high-fidelity 3D environments reconstructed from real-world imaging, achieving reliable navigation. Overall, this work provides a physically-realistic simulation platform and practical insights for the control of continuum systems in natural terrains.

</details>

---

### [[20_Research/Papers/强化学习/Global_linear_convergence_of_entropy-regularized_softmax_policy_gradient_beyond_tabular_MDPs|Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs]]

![[assets/2605.24939_first_page.png|800]]

- **arXiv**: [2605.24939](https://arxiv.org/abs/2605.24939)
- **PDF**: https://arxiv.org/pdf/2605.24939
- **详细分析**: [[20_Research/Papers/强化学习/Global_linear_convergence_of_entropy-regularized_softmax_policy_gradient_beyond_tabular_MDPs|Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs]]
- **作者**: Ziyue Chen, David Šiška, Lukasz Szpruch
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Global linear convergence of entropy-regularized softmax policy gradient beyond tabular MDPs》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the global convergence of policy gradient for infinite-horizon entropy-regularized Markov decision processes (MDPs) with continuous state and action spaces. We consider log-linear softmax policies with linear function approximation, which extend the tabular softmax parameterization while retaining a tractable policy class. Under $Q^\pi_\tau$-realizability for the regularized state-action value function, we first establish a non-uniform Polyak--Łojasiewicz (PŁ) inequality. The non-uniformity arises through degeneracy of constants associated with the policy geometry, namely the Fisher information matrix or an uncentered feature covariance matrix. We then identify two feature regimes under which this non-uniform constant can be bounded along the gradient flow. For full-affine-span features, we prove radial unboundedness of the KL regularizer and show that the smallest eigenvalue of the Fisher information matrix remains bounded below by an initialization-dependent positive constant. For simplex-valued features, we prove an analogous radial unboundedness result in the subspace orthogonal to the all-ones vector and obtain a uniform lower bound for the smallest eigenvalue of the uncentered covariance matrix. These results imply global linear convergence of the regularized objective along the gradient flow, i.e. suboptimality decaying as $\mathcal{O}(e^{-Ct})$ for some $C&gt;0$. Our analysis extends the global convergence theory of entropy-regularized softmax policy gradient beyond the tabular setting of Agarwal et al. (2020); Bhandari and Russo (2024); Mei et al. (2020).

</details>

---

### [[20_Research/Papers/强化学习/Unifying_Value_Alignment_and_Assignment_in_Cross-Domain_Offline_Reinforcement_Learning_with_Heterogeneous_Datasets|Unifying Value Alignment and Assignment in Cross-Domain Offline Reinforcement Learning with Heterogeneous Datasets]]

![[assets/2605.24862_figure.png|800]]

- **arXiv**: [2605.24862](https://arxiv.org/abs/2605.24862)
- **PDF**: https://arxiv.org/pdf/2605.24862
- **详细分析**: [[20_Research/Papers/强化学习/Unifying_Value_Alignment_and_Assignment_in_Cross-Domain_Offline_Reinforcement_Learning_with_Heterogeneous_Datasets|Unifying Value Alignment and Assignment in Cross-Domain Offline Reinforcement Learning with Heterogeneous Datasets]]
- **作者**: Zhongjian Qiao, Jiafei Lyu, Chenjia Bai, Peisong Wang, Siyang Gao, Shuang Qiu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Unifying Value Alignment and Assignment in Cross-Domain Offline Reinforcement Learning with Heterogeneous Datasets》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-domain offline reinforcement learning (RL) aims to learn a policy in the target domain with a limited target domain dataset and a source domain dataset that exhibits a dynamics shift. Training directly on the original source dataset typically leads to performance collapse. Recent studies perform data filtering from the perspective of dynamics alignment or value alignment to enable efficient policy transfer. However, these studies are typically validated on single-domain or single-behavior-policy source datasets. In this work, we explore a more general heterogeneous cross-domain offline RL setting, where the source datasets may be collected from multiple source domains by diverse behavior policies. We first uncover a critical yet overlooked issue in this setting: value misassignment. Empirically and theoretically, we demonstrate that value misassignment can undermine value alignment, mislead data filtering toward selecting suboptimal samples, and loosen the suboptimality gap, thereby degrading the agent's performance. To address this issue, we propose V2A, which integrates dynamics alignment, value alignment, and value assignment. V2A first employs temporally-consistent modality representation learning to extract dynamics modalities from the source dataset, followed by modality-aware advantage learning to rectify value alignment. Finally, it adopts a data filtering paradigm to selectively share source data for policy learning. Empirical results show that V2A significantly outperforms strong baseline methods under general heterogeneous cross-domain offline RL settings.

</details>

---

### [[20_Research/Papers/强化学习/A_Contractive_Feedback_Semantics_for_Reinforcement_Learning|A Contractive Feedback Semantics for Reinforcement Learning]]

![[assets/2605.24759_first_page.png|800]]

- **arXiv**: [2605.24759](https://arxiv.org/abs/2605.24759)
- **PDF**: https://arxiv.org/pdf/2605.24759
- **详细分析**: [[20_Research/Papers/强化学习/A_Contractive_Feedback_Semantics_for_Reinforcement_Learning|A Contractive Feedback Semantics for Reinforcement Learning]]
- **作者**: Zuyuan Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《A Contractive Feedback Semantics for Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discounted reinforcement learning is usually presented through Bellman equations on closed Markov decision processes. This paper develops a compositional view: a one-step decision process is treated as an open stochastic component, and infinite-horizon policy evaluation is obtained by closing a contractive feedback loop. The resulting semantics assigns typed Bellman transformers to open components, interprets series and parallel wiring as composition and tensoring of transformers, and interprets feedback as an admissible guarded Banach trace realized by a unique fixed point. This perspective yields three theoretical consequences. First, approximate component equivalence is a contextual congruence for admitted well-typed guarded one-hole contexts: local operator error remains controlled after plugging the component into a surrounding circuit that uses the hole once and whose feedback nodes have certified uniform guardedness. Second, exact and approximate state abstractions become commuting or near-commuting coalgebraic diagrams, giving value-preservation and explicit sup-norm distortion bounds. Third, under monotone $\omega$-continuous contract-transformer semantics, safety, risk, and resource specifications can be represented as quantale-valued contracts, where local inductive bounds lift through wiring and feedback by least-fixed-point reasoning. Its central claim is not that all RL morphisms form a global traced monoidal category, but that discounted Bellman evaluation admits a contractive feedback semantics on the admissible class of guarded circuits.

</details>

---

### [[20_Research/Papers/强化学习/How_Neural_Reward_Models_Learn_Features_for_Policy_Optimization_A_Single-Index_Analysis|How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis]]

![[assets/2605.24749_first_page.png|800]]

- **arXiv**: [2605.24749](https://arxiv.org/abs/2605.24749)
- **PDF**: https://arxiv.org/pdf/2605.24749
- **详细分析**: [[20_Research/Papers/强化学习/How_Neural_Reward_Models_Learn_Features_for_Policy_Optimization_A_Single-Index_Analysis|How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis]]
- **作者**: Rei Higuchi, Ryotaro Kawata, Akifumi Wachi, Shokichi Takakura, Kohei Miyaguchi, Taiji Suzuki
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《How Neural Reward Models Learn Features for Policy Optimization: A Single-Index Analysis》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward modeling is not only a prediction problem: in KL-regularized policy optimization, the learned reward is exponentiated to define the deployed policy, so downstream value depends on errors in reward-tilted regions. We study this feedback in a Gaussian single-index model with $r^*(x) = \sigma^*(\langle \theta^*, x\rangle)$ and $x \sim N(0, I_d)$. We analyze a two-stage neural reward model that first learns the hidden direction $\theta^*$ from reward-weighted samples and then fits the readout layer by weighted ridge regression. Exponential reward weighting changes the Hermite signal available to the first layer; for any feature-learning temperature $\beta_1$ above a dimension-free $O(1)$ threshold, a constant fraction of neurons recover the hidden direction, with weak-recovery complexity governed by the generative exponent. After feature recovery, we derive tilted-policy value-gap bounds for an idealized label-weighted fit with weights $e^{y/\beta_2}$ and a more practical surrogate-weighted fit with weights $e^{r_{a_0}(x)/\beta_2}$. Keeping the $\beta_2$-dependence explicit yields an admissible set of deployment temperatures, balancing the gain from lowering $\beta_2$ against the learning cost amplified by exponential weighting; in the surrogate-weighted case, proxy-dependent factors shrink this admissible set.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Reachability_Guaranteeing_Asymptotic_Optimality|Reinforcement Learning for Reachability: Guaranteeing Asymptotic Optimality]]

![[assets/2605.24740_figure.png|800]]

- **arXiv**: [2605.24740](https://arxiv.org/abs/2605.24740)
- **PDF**: https://arxiv.org/pdf/2605.24740
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Reachability_Guaranteeing_Asymptotic_Optimality|Reinforcement Learning for Reachability: Guaranteeing Asymptotic Optimality]]
- **作者**: Amogh Palasamudram, Jakub Svoboda, Suguman Bansal, Krishnendu Chatterjee
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning for Reachability: Guaranteeing Asymptotic Optimality》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) for reachability specifications is fundamental in sequential decision-making, yet theoretical guarantees remain less explored. A recent work achieves asymptotic convergence to optimal policies. However, this approach provides limited insight into convergence dynamics. In this work, we present an alternative approach that provides deeper theoretical insights into convergence. Our approach builds on PAC learning with assumptions. PAC learning guarantees near-optimal policies with high confidence in finite time but requires knowing internal MDP parameters like minimum transition probability. We argue that while these parameters are unknown in RL, they can be iteratively refined and estimated with increasing accuracy. By iteratively satisfying PAC conditions, we show that exact optimality can be achieved in the limit. Empirical evaluations on standard benchmarks validate our theoretical insights into convergence dynamics.

</details>

---

### [[20_Research/Papers/强化学习/Streaming_Reinforcement_Learning_under_Partial_Observability_with_Real-Time_Recurrent_Learning|Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning]]

![[assets/2605.24709_figure.png|800]]

- **arXiv**: [2605.24709](https://arxiv.org/abs/2605.24709)
- **PDF**: https://arxiv.org/pdf/2605.24709
- **详细分析**: [[20_Research/Papers/强化学习/Streaming_Reinforcement_Learning_under_Partial_Observability_with_Real-Time_Recurrent_Learning|Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning]]
- **作者**: Noah Farr, Aryaman Reddi, Carlo D'Eramo, Jan Peters
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：POPGym, RTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Streaming reinforcement learning has emerged as an online learning paradigm that conforms to the restrictions of natural learning agents that process data incrementally, i.e. with a batch size of 1 and no replay buffer. While streaming RL has recently been shown to scale with deep function approximation with full observability, partially observable settings have remained out of reach. Truncated backpropagation through time collapses to a one-step gradient horizon under the streaming setting, and exact real-time recurrent learning is prohibitively expensive. We close this gap using recurrent trace units, a diagonal recurrent architecture that enables exact RTRL with linear time and memory complexity in the parameter count, and show that they integrate cleanly into existing streaming algorithms across both discrete and continuous control. On a MemoryChain diagnostic with chain lengths from 2 to 128, our method sustains performance where streaming TBPTT(1) baselines using feedforward, GRU, and RTU networks collapse. On five POPGym tasks and on partially observable MuJoCo continuous control, the streaming approach is competitive with batched PPO on POPGym and recovers a substantial fraction of batched performance on masked MuJoCo, despite using no replay buffer or batched updates.

</details>

---

### [[20_Research/Papers/具身智能/Sum_of_Costs_Diffusion_with_Dynamic_Guidance_for_Motion_Planning|Sum of Costs Diffusion with Dynamic Guidance for Motion Planning]]

![[assets/2605.24690_figure.png|800]]

- **arXiv**: [2605.24690](https://arxiv.org/abs/2605.24690)
- **PDF**: https://arxiv.org/pdf/2605.24690
- **详细分析**: [[20_Research/Papers/具身智能/Sum_of_Costs_Diffusion_with_Dynamic_Guidance_for_Motion_Planning|Sum of Costs Diffusion with Dynamic Guidance for Motion Planning]]
- **作者**: Aysu Aylin Kaplan, Özgür Erkent
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Sum of Costs Diffusion with Dynamic Guidance for Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The motion planning problem for robotic manipulation can be addressed through classical or deep learning approaches. Existing methods face significant challenges in generalizing to diverse settings. In this study, we present a method with high generalization capability that generates collision-free trajectories using diffusion models where the denoising process is guided by the gradient of the total collision cost. We are also presenting a dynamic approach for choosing start step of the gradient guidance. Experimental results demonstrate that guiding the diffusion model dynamically with the sum of collision costs offers more robust performance by overcoming the generalization issues faced by competing methods. The proposed model demonstrates its effectiveness by achieving the highest performance on diverse test settings in M$\pi$nets\ dataset among the compared methods.

</details>

---

### [[20_Research/Papers/强化学习/Vision-Guided_Outdoor_Flight_and_Obstacle_Evasion_via_Reinforcement_Learning|Vision-Guided Outdoor Flight and Obstacle Evasion via Reinforcement Learning]]

![[assets/2605.24449_figure.png|800]]

- **arXiv**: [2605.24449](https://arxiv.org/abs/2605.24449)
- **PDF**: https://arxiv.org/pdf/2605.24449
- **详细分析**: [[20_Research/Papers/强化学习/Vision-Guided_Outdoor_Flight_and_Obstacle_Evasion_via_Reinforcement_Learning|Vision-Guided Outdoor Flight and Obstacle Evasion via Reinforcement Learning]]
- **作者**: Shiladitya Dutta, Aayush Gupta, Varun Saran, Avideh Zakhor
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.02（加权：具身智能 0.6，强化学习 0.76，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Vision-Guided Outdoor Flight and Obstacle Evasion via Reinforcement Learning》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AerialGym, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although quadcopters boast impressive traversal capabilities enabled by their omnidirectional maneuverability, the need for continuous pilot control in complex environments impedes their application in GNSS and telemetry-denied scenarios. To this end, we propose a novel sensorimotor policy that uses stereo-vision depth and visual-inertial odometry (VIO) to autonomously navigate through obstacles in an unknown environment to reach a goal point. The policy is comprised of a pre-trained autoencoder as the perception head followed by a planning and control LSTM network which outputs velocity commands that can be followed by an off-the-shelf commercial drone. We leverage reinforcement and privileged learning paradigms to train the policy in simulation through a two-stage process: 1) initial training with optimal trajectories generated by a global motion planner acting as a supervisory backbone, 2) further fine-tuning in a curriculum environment. To bridge the sim-to-real gap, we employ domain randomization and reward shaping to create a policy that is both robust to noise and domain shift. In outdoor experiments, our approach achieves successful zero-shot transfer to both obstacle environments and a drone platform that were never encountered during training.

</details>

---

### [[20_Research/Papers/强化学习/A_Reinforcement_Learning_Inspired_Latent_Yield_Based_Adaptive_Algorithm_Switching_Mechanism|A Reinforcement Learning Inspired Latent Yield Based Adaptive Algorithm Switching Mechanism]]

![[assets/2605.24436_figure.png|800]]

- **arXiv**: [2605.24436](https://arxiv.org/abs/2605.24436)
- **PDF**: https://arxiv.org/pdf/2605.24436
- **详细分析**: [[20_Research/Papers/强化学习/A_Reinforcement_Learning_Inspired_Latent_Yield_Based_Adaptive_Algorithm_Switching_Mechanism|A Reinforcement Learning Inspired Latent Yield Based Adaptive Algorithm Switching Mechanism]]
- **作者**: Jayprakash S. Nair, Jimson Mathew, Shivashankar B. Nair
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《A Reinforcement Learning Inspired Latent Yield Based Adaptive Algorithm Switching Mechanism》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Selecting the most suitable algorithm for a given problem instance remains a challenging task, particularly in online or dynamic environments where problem characteristics evolve over time. Relying solely on instantaneous performance metrics can result in a reactive and unstable behaviour, often leading to suboptimal algorithm switching. This paper introduces a computationally efficient approach for aggregating an algorithm's performance across multiple problem instances that is fairly immune to erratic variations in instance features. Inspired by features inherent to Reinforcement Learning (RL), this technique encapsulates rewards and penalties into a latent yield that, in turn, triggers exploitation and exploration, consequently resulting in adaptive algorithm switching. The proposed technique employs island models, inspired by Genetic Algorithms, to facilitate parallel exploration and performance exchanges among algorithm populations inhabiting local repertoires. Experimental evaluations on sorting algorithms and robotic obstacle avoidance tasks demonstrate the feasibility and effectiveness of the approach, highlighting its potential in domains where adaptive algorithm selection is critical.

</details>

---

### [[20_Research/Papers/强化学习/Evolving_Robustness--Exploration_Trade-off_in_Online_Reinforcement_Learning_via_Quantile_Bayesian_Risk_MDPs|Evolving Robustness--Exploration Trade-off in Online Reinforcement Learning via Quantile Bayesian Risk MDPs]]

![[assets/2605.24345_figure.png|800]]

- **arXiv**: [2605.24345](https://arxiv.org/abs/2605.24345)
- **PDF**: https://arxiv.org/pdf/2605.24345
- **详细分析**: [[20_Research/Papers/强化学习/Evolving_Robustness--Exploration_Trade-off_in_Online_Reinforcement_Learning_via_Quantile_Bayesian_Risk_MDPs|Evolving Robustness--Exploration Trade-off in Online Reinforcement Learning via Quantile Bayesian Risk MDPs]]
- **作者**: Meichen Song, Yuhao Wang, Enlu Zhou
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Evolving Robustness--Exploration Trade-off in Online Reinforcement Learning via Quantile Bayesian Risk MDPs》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In online reinforcement learning, data scarcity creates epistemic uncertainty that makes robustness important early in learning, whereas sufficient exploration is needed to learn the true-environment optimal policy. We study this time-varying robustness--exploration trade-off through a quantile Bayesian risk-aware Markov decision process (BR-MDP), in which the quantile level controls how posterior uncertainty enters the Bellman backup. We characterize this control through an asymptotic normality result for the difference between the quantile BR-MDP value and the value in the true environment. The result implies that upper/lower-tail quantiles induce optimism/pessimism towards epistemic uncertainty, and the magnitude of the optimism/pessimism decreases as data accumulate. Building on this characterization, we propose an online Bayesian risk-aware algorithm with an adaptive quantile schedule that emphasizes robustness early and gradually encourages exploration of less-visited state--action pairs. We establish sublinear Bayesian regret bounds with respect to both the true optimal value and the optimal BR-MDP robust value. Numerical experiments demonstrate strong performance in both exploration-demanding and exploration-costly environments.

</details>

---
