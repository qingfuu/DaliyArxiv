# cs.LG | Machine Learning | 2026-11-04

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/具身智能/PolicyIK_High-Precision_Inverse_Kinematics_for_Robot_Arms_with_Reinforcement_Learning|PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning]]

![[assets/2611.05372_figure.png|800]]

- **arXiv**: [2611.05372](https://arxiv.org/abs/2611.05372)
- **PDF**: https://arxiv.org/pdf/2611.05372
- **详细分析**: [[20_Research/Papers/具身智能/PolicyIK_High-Precision_Inverse_Kinematics_for_Robot_Arms_with_Reinforcement_Learning|PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning]]
- **作者**: Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 3.12（加权：具身智能 0.9，强化学习 0.96，世界模型 0.16，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depends on hand-tuned controllers, and training data on physical robots are costly to collect. We present PolicyIK, a goal-conditioned reinforcement learning policy for high-precision IK. It updates joint-position references from pose feedback and observes its accumulated reference relative to the measured joints, so it can retain the offset that the position controller needs at rest. Two-scale pose errors with an error-dependent action gain resolve millimeter residuals while preserving large motions. Progress and dwell rewards teach it to both reach the tolerance and stay within it. In simulation, a single attempt by the trained PPO policy keeps the mean errors over the final second within 1 mm and 0.2° on 93.5% of held-out tasks, and a deployment protocol raises success to 98.9%. When trained directly on a physical arm with an off-policy RL learner, PolicyIK achieves higher reaching and holding success than all four classical IK controllers under the same time budgets. In simulated pick-and-place, PolicyIK executes the end-effector commands of the $π_{0.5}$ VLA policy with 95.7% success. These results show that reinforcement learning can provide high-precision inverse kinematics for robot arms. Code is available at https://github.com/Tinaliu0123/PolicyIK.

</details>

---

### [[20_Research/Papers/强化学习/GUILD_Guided_Iterative_Data_Collection_for_Imitation_Learning|GUILD: Guided Iterative Data Collection for Imitation Learning]]

![[assets/2611.05368_figure.png|800]]

- **arXiv**: [2611.05368](https://arxiv.org/abs/2611.05368)
- **PDF**: https://arxiv.org/pdf/2611.05368
- **详细分析**: [[20_Research/Papers/强化学习/GUILD_Guided_Iterative_Data_Collection_for_Imitation_Learning|GUILD: Guided Iterative Data Collection for Imitation Learning]]
- **作者**: Shivin Dass, Kevin Nguyen, Rohan Yelandur, Junhong Xu, Roberto Martín-Martín
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GUILD: Guided Iterative Data Collection for Imitation Learning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Closed-World, GenSim, Open-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning policies in robotics are trained on datasets collected through costly real-world teleoperation. Often, the data-collection process is unguided, relying on the teleoperator's intuition, resulting in data that contributes little to overall policy performance. Recent work has shown that curating such unguided datasets can substantially improve policy performance, but these approaches operate by filtering existing datasets after collection and therefore do not prevent the acquisition of uninformative data. In this work, we propose GUILD, a novel Guided Data Collection (GDC) method that actively reasons about which data should be collected to maximize downstream policy performance. We introduce an iterative framework that alternates between 1) task proposal and data collection and 2) data evaluation to close the loop. For task proposal, we leverage semantic priors from vision-language models to identify relevant environments, object configurations, and goals for data collection. However, since semantic relevance does not imply policy improvement, we perform data evaluation. By leveraging predictive data attribution we approximate how the collected trajectories influence policy performance on a target deployment setting. This signal is then used as feedback to guide subsequent data collection, closing the data collection loop. We evaluate our approach in simulation and real robot settings, demonstrating that guided data collection substantially improves sample efficiency and deployment performance compared to passive data collection strategies, multiple baselines and experienced roboticists. More information at https://robin-lab.cs.utexas.edu/guild2026/

</details>

---

### [[20_Research/Papers/强化学习/GSBR_Geometric_Support_Behavior_Regularization_for_Online_RL|GSBR: Geometric Support Behavior Regularization for Online RL]]

![[assets/2611.05295_figure.png|800]]

- **arXiv**: [2611.05295](https://arxiv.org/abs/2611.05295)
- **PDF**: https://arxiv.org/pdf/2611.05295
- **详细分析**: [[20_Research/Papers/强化学习/GSBR_Geometric_Support_Behavior_Regularization_for_Online_RL|GSBR: Geometric Support Behavior Regularization for Online RL]]
- **作者**: Charles Xu, Jacob Berg, Liyiming Ke, Sergey Levine
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《GSBR: Geometric Support Behavior Regularization for Online RL》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DICE-RL, DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Regularizing online reinforcement learning (RL) toward a pretrained base policy can improve sample efficiency and learning stability, but regularization that is too restrictive limits how much the policy can improve. Base policies -- typically diffusion or flow-matching models trained by imitation learning on large, diverse datasets -- capture many behaviors that are reasonable but suboptimal. Existing regularizers using such base policies are too restrictive in one of two ways: behavioral cloning regularizers pull the actor toward the full base-policy distribution, penalizing it for discarding suboptimal modes, while hard support constraints forbid improvements that lie just outside the base policy's support. We propose Geometric Support Behavior Regularization (GSBR), which penalizes actions by their distance from the base policy's support. Actions within the support incur no penalty, so the actor can concentrate on high-value modes; outside the support, where value estimates are less reliable, the penalty grows smoothly with distance while still permitting improvement when the value gained outweighs the penalty. GSBR estimates this distance from a finite set of base-policy samples, so it requires only sample access to the base policy. Across 19 tasks on four robotic benchmarks, GSBR raises the average success rate from 33% for the base policy to 95%, achieving the highest average success rate and throughput among all compared methods, with about 23% higher normalized throughput than the next-best RL method. Project website and open-source code at https://charlesxu0124.github.io/gsbr/ .

</details>

---

### [[20_Research/Papers/强化学习/iGC_Antibody_Optimization_via_Reinforcement_Learning_over_a_Learned_Somatic_Hypermutation_Prior|iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior]]

![[assets/2611.05270_figure.png|800]]

- **arXiv**: [2611.05270](https://arxiv.org/abs/2611.05270)
- **PDF**: https://arxiv.org/pdf/2611.05270
- **详细分析**: [[20_Research/Papers/强化学习/iGC_Antibody_Optimization_via_Reinforcement_Learning_over_a_Learned_Somatic_Hypermutation_Prior|iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior]]
- **作者**: Thao Nguyen, Robert G. Alberstein, Ewa Nowara, Homa MohammadiPeyhani, Holly R. Steach, Sarah A. Robinson, Yuval Shechter, Donald W. Lee, Jason A. Vander Heiden, Franziska Seeger, Andrew Leaver-Fay, Richard Bonneau...
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AbBiBench, RewardNet, TaxNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Antibody affinity maturation is a natural optimization process in which B cells acquire mutations through somatic hypermutation (SHM), undergo selection for improved antigen binding, and iteratively evolve toward higher affinity. Computationally modeling this process requires capturing both biologically plausible mutations and antigen-specific selection. However, existing mutation models do not directly optimize binding, while affinity optimization often neglects realistic mutation trajectories. We introduce iGC (in silico Germinal Centers), a two-stage reinforcement learning (RL) framework for antigen-specific antibody optimization. Stage 1 learns an SHM mutation prior from parent-child pairs in B-cell lineage trees and adapts it to a target affinity-maturation dataset. Stage 2 initializes an RL policy from this prior and optimizes antigen binding with Kullback-Leibler (KL) regularization toward the frozen prior. To prevent reward exploitation, including repetitive high-reward substitutions and structurally tolerated framework mutations, we introduce a Reward-Tax Meta-Gradient objective. RewardNet smooths the affinity landscape, while TaxNet penalizes reward overexploitation, jointly defining a learned meta-reward for policy optimization. We evaluate iGC on mutation prediction, SHM consistency, affinity optimization, and mutation diversity. The mutation prior more than doubles the strongest baseline in mutation-site prediction. Following RL optimization, iGC maintains SHM sequence structure. It also achieves a strong exploration-exploitation balance, yielding competitive reward-diversity products across candidate-selection cutoffs. These results demonstrate that iGC integrates biologically plausible mutation generation with antigen-specific affinity selection, providing an in silico framework for iterative antibody affinity maturation.

</details>

---

### [[20_Research/Papers/强化学习/Stabilizing_On-Policy_Targeted_Guidance_in_Agentic_Reinforcement_Learning|Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning]]

![[assets/2611.05266_figure.png|800]]

- **arXiv**: [2611.05266](https://arxiv.org/abs/2611.05266)
- **PDF**: https://arxiv.org/pdf/2611.05266
- **详细分析**: [[20_Research/Papers/强化学习/Stabilizing_On-Policy_Targeted_Guidance_in_Agentic_Reinforcement_Learning|Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning]]
- **作者**: Kevin Frans, Alexander M Rush, Sergey Levine, Pieter Abbeel, Ashvin Nair
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Stabilizing On-Policy Targeted Guidance in Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Naive on-policy RL is often bottlenecked by the capabilities of the base model --- insufficient coverage can result in an inability to learn from certain rewards. At the same time, rewards in modern post-training systems often come from rich textual sources, e.g. judge models with a rubric of criteria. Can we utilize such structures to provide a rich directional signal that enables improving on otherwise difficult to optimize rewards? In this work, we examine a framework we refer to as targeted guidance that learns from per-turn textual feedback via an on-policy self-distillation objective. Our focus is not only on directly improving hard-to-optimize behaviors, but on how to do so throughout the training process without degrading baseline RL performance. Over a range of settings across an agentic multi-turn software engineering environment, we find success by combining targeted self-distillation with a per-criteria RL reward, and by limiting feedback to turns where the policy specifically fails. We further examine the design choices that lead to stable entropy and reduce oscillatory behavior throughout training.

</details>

---

### [[20_Research/Papers/具身智能/CRONOS_Benchmarking_Non-Episodic_Reinforcement_Learning_for_Robotic_Manipulation|CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation]]

![[assets/2611.05080_figure.png|800]]

- **arXiv**: [2611.05080](https://arxiv.org/abs/2611.05080)
- **PDF**: https://arxiv.org/pdf/2611.05080
- **详细分析**: [[20_Research/Papers/具身智能/CRONOS_Benchmarking_Non-Episodic_Reinforcement_Learning_for_Robotic_Manipulation|CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation]]
- **作者**: Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng, Tsung-Wei Ke
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.02（加权：具身智能 1.8，强化学习 0.96，世界模型 0.16，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NSR-MTRL, OpenVLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is promising for adapting robot policies to unstructured real-world environments. However, standard RL pipelines rely on episodic training with frequent scene resets, which is impractical for real-world deployment due to the need for substantial human intervention. While prior work has studied non-episodic RL in relatively small policies trained from scratch, its behavior when fine-tuning modern large-scale pre-trained vision-language-action (VLA) models remains underexplored. In this work, we introduce CRONOS, a simulation benchmark for RL fine-tuning of VLAs under non-episodic scene resets. CRONOS leverages high-fidelity physics simulators and adopts shared-scene multi-task settings. Using CRONOS, we show that naively fine-tuning pre-trained policies fails in non-episodic settings due to shifts in object configurations and end-effector poses; however, these challenges can be mitigated through targeted reset allocation and by addressing biases in pre-trained models. Moreover, we find that non-episodic training enhances long-horizon manipulation and improves generalization to previously unseen object configurations and task sequences. Project page: https://embodiedai-ntu.github.io/cronos/

</details>

---

### [[20_Research/Papers/强化学习/Cooperative_Multi-Agent_Reinforcement_Learning_with_Submodular_Trajectory_Rewards|Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards]]

![[assets/2611.04774_first_page.png|800]]

- **arXiv**: [2611.04774](https://arxiv.org/abs/2611.04774)
- **PDF**: https://arxiv.org/pdf/2611.04774
- **详细分析**: [[20_Research/Papers/强化学习/Cooperative_Multi-Agent_Reinforcement_Learning_with_Submodular_Trajectory_Rewards|Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards]]
- **作者**: Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization exponential in the horizon and the number of agents. To overcome this challenge while retaining theoretical guarantees, we introduce pre-window curvature $c_m$, which quantifies how states visited more than $m$ steps earlier reduce current marginal gains. Using this curvature to control the error from restricting the policy of each agent to depend only on its last $m+1$ states, we propose a greedy algorithm that exploits the decoupled dynamics to optimize local policies sequentially. For fixed $m$, the algorithm achieves a $\frac{1-c_m}{2-c_m}$ approximation guarantee up to estimation error, and its computation time is polynomial in the number of agents and the horizon. We recover the known $1/2$-factor approximation for time-additive rewards and obtain an approximation factor no smaller than the known total-curvature bound for a single agent. We formulate multi-agent traffic monitoring as an example of this framework and evaluate our algorithm on it.

</details>

---

### [[20_Research/Papers/具身智能/Aero-VPA_Few-Step_Flow-Matching_Control_over_Non-Reconstructive_JEPA_Latents_for_Agile_Flight_on_Edge_Hardware|Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware]]

![[assets/2611.04392_first_page.png|800]]

- **arXiv**: [2611.04392](https://arxiv.org/abs/2611.04392)
- **PDF**: https://arxiv.org/pdf/2611.04392
- **详细分析**: [[20_Research/Papers/具身智能/Aero-VPA_Few-Step_Flow-Matching_Control_over_Non-Reconstructive_JEPA_Latents_for_Agile_Flight_on_Edge_Hardware|Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware]]
- **作者**: Yeonseok Lee
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models generalize across tasks, but their autoregressive decoders need sequential forward passes in proportion to the action horizon, each bounded below on embedded aerial platforms by streaming billions of parameters from memory. We present Aero-VPA, a lightweight Vision-Predictor-Action architecture for 3D navigation on edge hardware. A compact RGB-D Vision Transformer and a five-head ensemble predictor, trained without pixel reconstruction, forecast the next latent state; a Conditional Flow Matching solver generates a velocity and yaw-rate chunk in two Euler steps, so each decision takes five sequential network evaluations; and the ensemble dispersion drives an uncertainty fallback. Version 1 specified the architecture, deployment and protocol without results. This version reports the first closed-loop evaluation: PX4 software-in-the-loop simulation of quadrotor missions in procedurally generated forests. Behaviour cloning failed on all 60 missions despite open-loop errors of 0.02-0.04 m/s: the policy copies its last command, a copycat form of causal confusion. DAgger with a privileged, safety-gated supervisor gave the first successes but plateaued at 11.1-21.1% across six checkpoints. A map-free runtime shield with a 15 s depth memory, barrier constraints, a cap on motion outside the 73-degree field of view and backoff along the flown path raised the first DAgger policy's success on 180 paired missions from 21.1% to 52.2% (95% CI [45.0, 59.4]; exact McNemar p = 1.2 x 10^-10) and cut its crashes from 72.2% to 22.2%, while timeouts rose from 2.8% to 23.3%. All six checkpoints gained 30.0-34.4 percentage points, at mean speeds of 1.16-1.36 m/s. The code (https://github.com/ylee-sling/Aero-VPA), the trained policy (72.6 MB, https://huggingface.co/ylee-sling/aero-vpa) and the full benchmark dataset are public.

</details>

---

### [[20_Research/Papers/大模型/ModelBlaster_Closing_the_Performance_Gap_through_Learning-Augmented_Agents_Across_Models,_Kernels_and_Hardware_Backends|ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends]]

![[assets/2611.04104_figure.png|800]]

- **arXiv**: [2611.04104](https://arxiv.org/abs/2611.04104)
- **PDF**: https://arxiv.org/pdf/2611.04104
- **详细分析**: [[20_Research/Papers/大模型/ModelBlaster_Closing_the_Performance_Gap_through_Learning-Augmented_Agents_Across_Models,_Kernels_and_Hardware_Backends|ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends]]
- **作者**: Shengjun Kris Dong, Dima Nikiforov, Sahil Modi, Sana Damani, Edward C Lin, Siva Kumar Sastry Hari, Christos Kozyrakis
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.5，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：KernelBench, MAIC-RL, SOL-ExecBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, existing LLM agents typically target a single programming interface, toolchain, or accelerator family, focus on kernel-level optimization without model-level transforms, and offer limited reuse of experience across hardware targets. We present ModelBlaster, a Memory-Augmented In-Context Reinforcement Learning (MAIC-RL) framework for optimizing data-parallel kernels and whole models across heterogeneous SIMD and SIMT accelerators. Its mutable policy is a persistent knowledge base updated at inference time by Actor-Critic Textual Gradient Descent (AC-TGD). The knowledge base maps performance states to actions, outcomes, and constraints, enabling experience reuse across kernels, models, and hardware targets. A model-level optimizer uses kernel-level knowledge to inform whole-model decisions. The same optimization loop and knowledge schema support CUDA on NVIDIA GPUs, OpenCL on Qualcomm GPUs, and RVV intrinsics on RISC-V vector cores, with only lowering and measurement layers specific to each target. Compared with PyTorch, ModelBlaster achieves geometric-mean speedups of 1.85x, 5.58x, and 5.18x on KernelBench Levels 1, 2, and 3, and 1.69x on SOL-ExecBench Levels 1 and 2 on a B200 GPU. On Qualcomm Adreno GPUs, it achieves 5.8x over the vendor SDK and 1.7x over Apache TVM; on RISC-V vector cores, it achieves 2.7x over ExecuTorch with XNNPACK across 70 KernelBench problems.

</details>

---

### [[20_Research/Papers/大模型/Computer-Use_Agents_Gain_Little_Benefit_from_a_World_Model_When_Conditioned_on_Tutorials|Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials]]

![[assets/2611.04073_figure.png|800]]

- **arXiv**: [2611.04073](https://arxiv.org/abs/2611.04073)
- **PDF**: https://arxiv.org/pdf/2611.04073
- **详细分析**: [[20_Research/Papers/大模型/Computer-Use_Agents_Gain_Little_Benefit_from_a_World_Model_When_Conditioned_on_Tutorials|Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials]]
- **作者**: Anh Nguyen, Tianyi Xu, Phat Tran, Harry Yu, Huazheng Wang, Stefan Lee
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 2.02（加权：大模型 0.7，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Computer-Use Agents Gain Little Benefit from a World Model When Conditioned on Tutorials》归入 世界模型、大模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has improved computer-use agents (CUAs) by combining retrieved task-relevant tutorials and look-ahead planning using world models with MLLM judges. However, the contribution of each component -- tutorials, the judge, and the world model -- to overall improvement has not been evaluated in isolation. To fill this gap, we first construct OSWorld-Tutorial and ScienceBoard-Tutorial: two datasets for CUAs with curated multimodal tutorials, covering everyday and scientific domains. We then propose RAG-PolicyJudge (RAG-PJ), a policy-judge framework for CUAs conditioned on task-specific tutorials: the policy proposes candidate actions, and the judge selects among them. To isolate the effect of world models given tutorials, we compare RAG-PJ with and without common world models: using either zero-shot text-based descriptions of next states or an oracle that returns ground-truth visual observations. We find that RAG-PJ gains little benefit from these rollouts when tutorials are present, even with perfect visual futures. This suggests prior world-model gains in tutorial-conditioned methods come mainly from tutorial understanding and the judge's ability to select the proposed actions, rather than from predicted rollouts. Error analysis reveals that the bottleneck is not rollout fidelity, but the judge's ability to reason over future states and recognize task completion. This highlights the need to improve not just next-state prediction in world models, but also reasoning over their predicted rollouts. Datasets and code are available at https://github.com/realjoenguyen/RAGPJ-official.

</details>

---

### [[20_Research/Papers/强化学习/Finite-Sample_Convergence_in_Networked_Average_Reward_MARL_Decentralization_Pitfalls_and_Entropy_Remedies|Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies]]

![[assets/2611.04072_figure.png|800]]

- **arXiv**: [2611.04072](https://arxiv.org/abs/2611.04072)
- **PDF**: https://arxiv.org/pdf/2611.04072
- **详细分析**: [[20_Research/Papers/强化学习/Finite-Sample_Convergence_in_Networked_Average_Reward_MARL_Decentralization_Pitfalls_and_Entropy_Remedies|Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies]]
- **作者**: Yizhou Zhang, Yashaswini Murthy, Laixi Shi, Adam Vierman
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the problem of average reward Multi-Agent Reinforcement Learning (MARL) where agents interact within a network. Each agent in the network conducts local updates with information within its $k$-hop neighborhood and collaboratively maximizes the overall reward of the entire network. We first provide impossibility results in achieving convergence to the global optimal joint policies in our setting. These impossibility results highlight the challenges of decentralized learning with local information in multi-agent systems, namely the issues of multiagency, where each agent independently optimizes its policy, and partial observability, where agents have limited visibility into the global state. Given these challenges which indicate that decentralized policy optimization can generally be certified only up to stationarity, we provide finite-sample convergence guarantees for a decentralized actor-critic algorithm with linear function approximation that converges to an approximate stationary point with small gradient norm. To overcome such impossibility results, we further show that adding fixed-state entropy regularization reshapes the objective landscape which leads to even stronger global convergence guarantees for our proposed actor-critic algorithm.

</details>

---

### [[20_Research/Papers/大模型/Decision_Transformer_with_Task-Aware_Representations_for_Offline_Meta-Reinforcement_Learning|Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning]]

![[assets/2611.04010_figure.png|800]]

- **arXiv**: [2611.04010](https://arxiv.org/abs/2611.04010)
- **PDF**: https://arxiv.org/pdf/2611.04010
- **详细分析**: [[20_Research/Papers/大模型/Decision_Transformer_with_Task-Aware_Representations_for_Offline_Meta-Reinforcement_Learning|Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning]]
- **作者**: Xinbo Zhao, Yuhang Liu, Xin Zhang, Lei Le, Zhaohan Xi, Yingxue Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.76，世界模型 0.36）
- **关联关键词**: LLM, RL, WorldModel

#### 研究背景与动机

《Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To enable effective generalization in offline meta-RL, it is essential to accurately infer the underlying task through latent task representations, which provide a compact and transferable summary of task-specific characteristics for guiding policy generation. In this paper, we propose Contrastive Task-Aware Decision Transformer (CoTA-DT), a DT-based offline meta-RL framework that learns task representations by jointly integrating four complementary components: (i) contrastive learning from offline trajectories, (ii) alignment with natural-language task descriptions, (iii) one-step supervision via a task-conditioned world model, and (iv) long-term supervision via a task-conditioned Q function. The learned task representations are used as conditioning signals for a DT-based policy, enabling task-aware meta-policy learning. To further support generalization in both zero-shot and few-shot settings, we design a language-grounded, self-adaptive strategy that enables effective and reliable adaptation to unseen tasks. Notably, in CoTA-DT, the pretrained LLM serves as a shared backbone for language encoding, world modeling, Q-function estimation, and policy learning. This unified design facilitates parameter sharing, improving both efficiency and generalization. Extensive experiments across diverse offline meta-RL benchmarks demonstrate that CoTA-DT consistently outperforms prior methods, particularly in challenging zero-shot generalization scenarios.

</details>

---

### [[20_Research/Papers/世界模型/When_Latent_Dynamics_Meet_Data_Assimilation_A_Benchmark_of_Koopman-Type_Representations|When Latent Dynamics Meet Data Assimilation: A Benchmark of Koopman-Type Representations]]

![[assets/2611.03916_figure.png|800]]

- **arXiv**: [2611.03916](https://arxiv.org/abs/2611.03916)
- **PDF**: https://arxiv.org/pdf/2611.03916
- **详细分析**: [[20_Research/Papers/世界模型/When_Latent_Dynamics_Meet_Data_Assimilation_A_Benchmark_of_Koopman-Type_Representations|When Latent Dynamics Meet Data Assimilation: A Benchmark of Koopman-Type Representations]]
- **作者**: Zhiwei Zhang, Wenxuan Yuan, Xiaoyuan Cheng, Pouria Behnoudfar, Chuanqi Chen, Charlotte Moser, Yuta Tarumi, Jin-Long Wu, Rossella Arcucci, Takemasa Miyoshi, Nan Chen, Marc Bocquet...
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

《When Latent Dynamics Meet Data Assimilation: A Benchmark of Koopman-Type Representations》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Koopman representations describe nonlinear dynamics through linear evolution in a transformed space, offering an attractive framework for their linear simplicity and generality. Yet these advantages do not necessarily translate into improved performance in deep latent data assimilation (LDA). We systematically compare seven representative methods and structural baselines across five systems spanning approximately periodic to strongly chaotic dynamics and a broad range of state dimensions. We evaluate forecast and assimilation accuracy, physical state recovery, latent-trajectory behavior, and dynamical consistency, and assess Gaussian error assumptions, objective convexity, and uniqueness of analysis solutions. Our results reveal a trade-off between representational flexibility and optimization tractability. Linear evolution of the latent state can stabilize short-term forecasts but restrict expressiveness in strongly chaotic and high-dimensional systems, without consistently improving assimilation accuracy. Parameterized linear operators offer greater flexibility, yet their joint optimization with the encoder--decoder remains nonconvex. Methods with closed-form analysis updates generally perform better and exhibit greater robustness in our experiments, although matrix inversion remains a computational bottleneck. These findings show that the practical benefits of Koopman structure depend on both sufficient observational information and the choice of assimilation procedure.

</details>

---
