# cs.LG | Machine Learning | 2026-08-10

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/强化学习/Wasserstein_Policy_Gradient_for_Entropy-Regularized_Linear-Quadratic_Control|Wasserstein Policy Gradient for Entropy-Regularized Linear-Quadratic Control]]

![[assets/2608.07433_figure.png|800]]

- **arXiv**: [2608.07433](https://arxiv.org/abs/2608.07433)
- **PDF**: https://arxiv.org/pdf/2608.07433
- **详细分析**: [[20_Research/Papers/强化学习/Wasserstein_Policy_Gradient_for_Entropy-Regularized_Linear-Quadratic_Control|Wasserstein Policy Gradient for Entropy-Regularized Linear-Quadratic Control]]
- **作者**: Zhaoyu Zhu, Rui Gao, Shuang Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Wasserstein Policy Gradient for Entropy-Regularized Linear-Quadratic Control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wasserstein policy gradient (WPG) updates state-conditional action laws by transport in the action space. We study entropy-regularized discounted linear-quadratic (LQ) control. A Bellman verification argument shows that the unrestricted problem has a linear-Gaussian optimal policy, and the discounted-occupancy-weighted statewise Wasserstein gradient is tangent to this policy class. WPG therefore reduces exactly to a finite-dimensional ODE for the feedback gain and action covariance. We prove that this ODE is globally well posed and converges exponentially from every admissible initialization. For each fixed LQ problem, the exponent has a positive limit as the entropy temperature tends to zero and contains no perturbative factor of the form $\exp(-c/\tau)$, while retaining the usual dependence on the conditioning of the control problem.

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Myopic_World_Models_Long-Horizon_End-to-End_Training_for_Direct_Future_Prediction|Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction]]

![[assets/2608.07420_figure.png|800]]

- **arXiv**: [2608.07420](https://arxiv.org/abs/2608.07420)
- **PDF**: https://arxiv.org/pdf/2608.07420
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Myopic_World_Models_Long-Horizon_End-to-End_Training_for_Direct_Future_Prediction|Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction]]
- **作者**: Xinyi Li, Zaishuo Xia, Chenjie Hao, Yubei Chen
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are expected to support imagination over extended temporal horizons, yet most are still trained through local few-step prediction objectives and deployed by recursively rolling out their own predictions. This creates a fundamental mismatch: few-step losses optimize local transition fidelity, while long-horizon prediction depends on how errors and gradients propagate through the entire trajectory. As a result, transitions with different downstream influence on the endpoint are treated uniformly during training, and small local errors are amplified through recursive inference. We argue that long-horizon accuracy is better achieved by optimizing directly, through an end-to-end endpoint prediction objective. To instantiate this paradigm, we introduce the Direct Prediction World Model (DPWM), a non-recursive architecture that compresses an action sequence of arbitrary length into a single embedding and predicts the endpoint observation in a single forward pass. This design avoids recurrent rollout in both prediction and gradient propagation, making long-horizon end-to-end training practical at horizons where unrolled autoregressive training becomes unstable. Empirically, DPWM substantially improves long-horizon endpoint prediction over recursive world-model baselines on continuous-control and pixel-based benchmarks, with larger gains as the prediction horizon increases. We further show that recurrent baselines benefit similarly when retrained with the same long-horizon endpoint objective, supporting our central claim that the training objective, rather than the particular backbone choice, is the main driver of long-horizon prediction accuracy. Our results suggest that world models can benefit from being trained and evaluated at the temporal scales where they are ultimately used, shifting the focus from local transition modeling toward long-horizon predictive accuracy.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Fault-Tolerant_Locomotion_with_Adaptive_Gait_Timing|Learning Fault-Tolerant Locomotion with Adaptive Gait Timing]]

![[assets/2608.07328_figure.png|800]]

- **arXiv**: [2608.07328](https://arxiv.org/abs/2608.07328)
- **PDF**: https://arxiv.org/pdf/2608.07328
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Fault-Tolerant_Locomotion_with_Adaptive_Gait_Timing|Learning Fault-Tolerant Locomotion with Adaptive Gait Timing]]
- **作者**: Giovanbattista Gravina, Luca Rossini, Carlo Rizzardo, Arturo Laurenzi, Nikos Tsagarakis
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.42（加权：具身智能 1.8，强化学习 0.76，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Fault-Tolerant Locomotion with Adaptive Gait Timing》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hardware failures require legged robots to rapidly reorganize coordination and gait timing to maintain stability and mobility. This is particularly challenging for larger quadrupeds, where increased mass and tighter actuation limits reduce the feasibility of aggressive, high-frequency compensation strategies often observed on smaller platforms. In this work, we propose a deep reinforcement learning approach for fault-tolerant locomotion under actuator power loss. The method employs an asymmetric actor-critic architecture in which the critic has access to privileged information during training, while the actor learns to reconstruct a corresponding latent representation from proprioceptive observations. We introduce a latent-alignment loss that encourages consistency between actor and critic representations. Additionally, we augment the action space with a learnable gait frequency parameter, enabling adaptive gait timing in response to terrain variations and actuator degradation without predefined faulty-leg strategies. The approach is validated in high-fidelity simulation on uneven terrain and real-world experiments on flat ground using a 68 kg quadruped robot.

</details>

---

### [[20_Research/Papers/强化学习/From_Optimal_Actions_to_World_Models_Identifiability_of_Transition_Kernels_in_Discounted_MDPs|From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs]]

![[assets/2608.07301_first_page.png|800]]

- **arXiv**: [2608.07301](https://arxiv.org/abs/2608.07301)
- **PDF**: https://arxiv.org/pdf/2608.07301
- **详细分析**: [[20_Research/Papers/强化学习/From_Optimal_Actions_to_World_Models_Identifiability_of_Transition_Kernels_in_Discounted_MDPs|From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs]]
- **作者**: Neal Batra
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: RL

#### 研究背景与动机

《From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study what can be recovered about the transition probabilities of a Markov decision process from optimal actions alone. This is closely related to the inverse problem considered by Letcher et al., who ask when the dynamics can be recovered from numerical \(Q\)-values. Here the numerical values themselves are not observed; only the optimal actions are known, for every reward in a given class. For state-action rewards \(r(s,a)\), knowing the optimal actions for every reward also tells us how much better one action is than another when each is followed by the same fixed policy. This is still not enough to determine the transition probabilities uniquely. We prove that two kernels give the same optimal actions for every reward exactly when \[ Q_{s,a} = \Bigl(P_{s,a}+\tfrac1\gamma e_s^{\mathsf T}(L-I)\Bigr)L^{-1} \] for one invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). Near a kernel with strictly positive entries, there is an \(n(n-1)\)-dimensional family of different kernels with this property. The result is unchanged if we consider only rewards having a unique optimal action at every state. We then compare this with rewards of the forms \(r(s)\) and \(r(s,a,s')\). Rewards that depend on the next state can usually recover the transition kernel itself: every row at a state with at least two actions is determined, and we describe exactly when a row at a state with one action can remain hidden. State rewards reveal less: two kernels give the same optimal actions exactly when every deterministic policy is optimal for the same set of rewards. The results show how the form of the reward affects what can be learned about the dynamics from optimal actions alone.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Suffers_More_Than_the_Policy_Class_Under_Partial_Observability_A_Closed-Form_Analysis|Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis]]

![[assets/2608.07228_figure.png|800]]

- **arXiv**: [2608.07228](https://arxiv.org/abs/2608.07228)
- **PDF**: https://arxiv.org/pdf/2608.07228
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Suffers_More_Than_the_Policy_Class_Under_Partial_Observability_A_Closed-Form_Analysis|Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis]]
- **作者**: Idil Gözel
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse. We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why. The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

</details>

---

### [[20_Research/Papers/强化学习/CrystalGRPO_Target-Aligned_and_Coverage-Preserving_Reinforcement_Learning_for_Flow-Based_Crystal_Structure_Prediction|CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction]]

![[assets/2608.06582_figure.png|800]]

- **arXiv**: [2608.06582](https://arxiv.org/abs/2608.06582)
- **PDF**: https://arxiv.org/pdf/2608.06582
- **详细分析**: [[20_Research/Papers/强化学习/CrystalGRPO_Target-Aligned_and_Coverage-Preserving_Reinforcement_Learning_for_Flow-Based_Crystal_Structure_Prediction|CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction]]
- **作者**: Kaixiang Su, Hongfei Xue, Qiang Zhu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《CrystalGRPO: Target-Aligned and Coverage-Preserving Reinforcement Learning for Flow-Based Crystal Structure Prediction》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OMatG-IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based generative models can efficiently produce candidate structures for crystal structure prediction (CSP), but their pretrained objectives do not directly optimize downstream target recovery. Reinforcement-learning post-training offers a flexible solution, yet existing approaches rely primarily on energy rewards and coordinate-only stochastic policies. Predicted energy does not identify the reference polymorph, while reward-driven concentration can reduce the candidate coverage required for Top-N recovery. We introduce CrystalGRPO, a CSP-aligned post-training framework that extends existing ODE-to-SDE policy constructions to the joint coordinate--lattice state. CrystalGRPO combines MACE-predicted energy with a StructureMatcher-based recovery score and provides two operating modes: CrystalGRPO-Q, which prioritizes single-draw recovery, and CrystalGRPO-C, which combines full-trajectory reference regularization with a coverage-aware group advantage to preserve finite-budget target recovery. Across MP-20 and MPTS-52 with PXRDGen and OMatG backbones, both variants reduce one- and twenty-sample RMSE relative to coordinate-only reinforcement in all four backbone--dataset settings. CrystalGRPO-Q consistently improves Top-1, whereas CrystalGRPO-C achieves a higher Top-20 across all settings.

</details>

---

### [[20_Research/Papers/强化学习/Online_Security_Learning_in_Cooperative_Multi-Agent_Systems_under_Hidden_Byzantine_Attacks|Online Security Learning in Cooperative Multi-Agent Systems under Hidden Byzantine Attacks]]

![[assets/2608.06520_first_page.png|800]]

- **arXiv**: [2608.06520](https://arxiv.org/abs/2608.06520)
- **PDF**: https://arxiv.org/pdf/2608.06520
- **详细分析**: [[20_Research/Papers/强化学习/Online_Security_Learning_in_Cooperative_Multi-Agent_Systems_under_Hidden_Byzantine_Attacks|Online Security Learning in Cooperative Multi-Agent Systems under Hidden Byzantine Attacks]]
- **作者**: Ximing Sun, Yue Wang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Online Security Learning in Cooperative Multi-Agent Systems under Hidden Byzantine Attacks》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study online cooperative control of a multi-agent system under Byzantine attacks. Namely, an unknown, fixed subset of agents are Byzantine comprised and can stealthily overwrite its own coordinates of the team's planned joint action after observing that plan. The learner observes planned actions, public rewards, and public states, but neither the overwrite nor the executed joint action. Our objective is security: to optimize the team performance against the worst overwrites and achieve the optimal security value. We first show that the attacker's information determines the geometry. An attacker that observes the planned action induces an exact $(s,a)$-rectangular robust Markov decision process (MDP) whose rows are convex hulls of overwrite-induced public-outcome laws, whereas a blind attacker induces an $s$-rectangular model. We then identify the information-theoretic limit of security learning, showing that the security regret decomposes exactly into return regret against the response generating the data and a cumulative response gap $D_K$. Two indistinguishable horizon-one instances force $\Omega(K)$ expected security regret while return regret is zero, showing that dependence on $D_K$ is unavoidable. Finally, we develop a stage-tied robust estimation-to-decisions learner and prove a regret bound of $\widetilde{\mathcal O}\!\left(H^2S\sqrt{AK}\right)+\mathbb E[D_K]$. Our studies thus provide comprehensive theoretical and algorithmic foundations of reliable multi-agent systems under Byzantine attacks.

</details>

---

### [[20_Research/Papers/强化学习/Game-Theoretic_Inverse_Reinforcement_Learning_for_Modeling_Competitive_Human_Driving_A_Cut-in_Prediction_Study|Game-Theoretic Inverse Reinforcement Learning for Modeling Competitive Human Driving: A Cut-in Prediction Study]]

![[assets/2608.06445_figure.png|800]]

- **arXiv**: [2608.06445](https://arxiv.org/abs/2608.06445)
- **PDF**: https://arxiv.org/pdf/2608.06445
- **详细分析**: [[20_Research/Papers/强化学习/Game-Theoretic_Inverse_Reinforcement_Learning_for_Modeling_Competitive_Human_Driving_A_Cut-in_Prediction_Study|Game-Theoretic Inverse Reinforcement Learning for Modeling Competitive Human Driving: A Cut-in Prediction Study]]
- **作者**: Yu Song
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Game-Theoretic Inverse Reinforcement Learning for Modeling Competitive Human Driving: A Cut-in Prediction Study》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Capturing the strategic decision-making inherent in competitive human driving is critical for autonomous vehicle safety and traffic simulation. This study demonstrates that game-theoretic Inverse Reinforcement Learning (IRL) provides a robust framework for this challenge. We present a comprehensive analysis comparing data-driven IRL models against an established physics-based game-theoretic approach for predicting aggressive, safety-critical cut-in lane changes. Using the high-fidelity highD dataset, we systematically develop and evaluate a series of IRL models with increasing feature complexity. Our results reveal significant advantages: the best-performing IRL models achieve an overall prediction accuracy exceeding 75 percent while maintaining a Cut-In precision up to 51 percent and recall up to 49 percent. This represents a significant improvement over the established physics-based benchmark, which achieved only 4.4 percent precision in these high-stakes scenarios. The analysis reveals a clear trade-off: incorporating granular, instantaneous features yields higher precision, while adding temporal consistency features maximizes recall. These findings suggest that IRL-based models can effectively bridge the gap between microscopic driver intent and macroscopic safety outcomes, providing a more reliable foundation for modeling interactions in mixed-autonomy environments.

</details>

---

### [[20_Research/Papers/具身智能/Fast_and_Accurate_An_Adaptive_VLA_Inference_Framework_through_Environment-aware_Model_Selection|Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection]]

![[assets/2608.06434_figure.png|800]]

- **arXiv**: [2608.06434](https://arxiv.org/abs/2608.06434)
- **PDF**: https://arxiv.org/pdf/2608.06434
- **详细分析**: [[20_Research/Papers/具身智能/Fast_and_Accurate_An_Adaptive_VLA_Inference_Framework_through_Environment-aware_Model_Selection|Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection]]
- **作者**: Yuewei Sun, Lang Qin, Zechuan Tian, Jingwen Li, Guiqin Wang, Shengzeng Huo, Wenxin Ren, Tao Fang, Xiaochen Zhang, Guanqing Deng, Xiang Wang, Xiaowen Dong...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DP-VLA, FiS-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligence demands both long-horizon reasoning and real-time closed-loop responsiveness. Recent dual-system Vision-Language-Action (VLA) architectures combine fast reactive control with slow deliberative reasoning to balance inference speed and task success rate. However, existing dual-process VLAs tightly couple the fast module to intermediate representations of the slow module, necessitating end-to-end joint training and limiting modularity, extensibility and flexible system switching. In this paper, we propose Environment-aware Model Selection (EMS), an adaptive VLA inference framework that switches between two fully decoupled systems of different scales through environment-aware model selection. The large-scale deliberative system provides globally consistent trajectory planning to ensure task success, while a lightweight reactive system enables high-frequency closed-loop control. A reinforcement-learning-based switching policy dynamically selects which system to invoke based on real-time feedback, enabling sparse use of the slow system and thereby balancing pretrained knowledge utilisation with runtime efficiency. Our design offers three key advantages over prior hierarchical VLA frameworks: (1) a fully decoupled and modular dual-system architecture that supports plug-and-play model replacement; (2) an adaptive, environment-aware switching strategy; (3) high-frequency inference for responsive closed-loop control. We extensively evaluate EMS in both simulation and real-world environments. On the LIBERO benchmark, EMS achieves success rates comparable to the large-scale baseline while increasing the effective action frequency to 93.4 Hz. The framework further demonstrates strong extensibility in real-world dual-arm manipulation tasks, where it accelerates task completion while maintaining robust performance.

</details>

---
