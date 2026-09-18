# cs.LG | Machine Learning | 2026-09-16

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/具身智能/Intrinsic_Robot_Rewarding_Reusing_VLA_Representations_for_Autonomous_Evaluation_and_Policy_Improvement|Intrinsic Robot Rewarding: Reusing VLA Representations for Autonomous Evaluation and Policy Improvement]]

![[assets/2609.17115_figure.png|800]]

- **arXiv**: [2609.17115](https://arxiv.org/abs/2609.17115)
- **PDF**: https://arxiv.org/pdf/2609.17115
- **详细分析**: [[20_Research/Papers/具身智能/Intrinsic_Robot_Rewarding_Reusing_VLA_Representations_for_Autonomous_Evaluation_and_Policy_Improvement|Intrinsic Robot Rewarding: Reusing VLA Representations for Autonomous Evaluation and Policy Improvement]]
- **作者**: Tobias Schaffer, Mohab Elkhayat, Daniela Nicklas, Mustafa Almohamad, Elham Al-Fuqara
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Intrinsic Robot Rewarding: Reusing VLA Representations for Autonomous Evaluation and Policy Improvement》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HIL-SERL, OpenVLA, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) systems already bring together two valuable resources for robot learning: rich visual representations and demonstrations of successful task execution. Intrinsic Robot Rewarding (IRR) proposes to use these resources for a second, complementary purpose: evaluating the robot's own outcomes and providing feedback for policy improvement. Successful demonstration endpoints define task-specific references, and the policy's frozen visual encoder provides the feature space in which new outcomes are assessed. The core reward mechanism adds a reference bank and a scoring operation to the existing pipeline, without requiring a separate learned evaluator or an additional perception backbone. Our position is that this reuse offers a promising route to lower integration effort, efficient reward computation, and reduced recurring human outcome scoring. Building on established research in visual rewards and learning from experience, IRR brings these ideas into the robot's existing perception and demonstration pipeline. An operational COMAU Racer 3 demonstrator is available at technology readiness level 4 (TRL 4). This laboratory foundation supports the next research step: connecting internal outcome evaluation to physical policy improvement. We present the reward formulation, central research questions, and an evaluation methodology linking reward reliability to task success and supervision effort. The intended contribution is a reusable approach to learn and improve from the data and experience already available in industrial robot systems.

</details>

---

### [[20_Research/Papers/具身智能/The_Latent_That_Never_Was_A_Forensic_Re-run_of_the_CVAE_Ablation_in_Action_Chunking_Transformer|The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer]]

![[assets/2609.16745_first_page.png|800]]

- **arXiv**: [2609.16745](https://arxiv.org/abs/2609.16745)
- **PDF**: https://arxiv.org/pdf/2609.16745
- **详细分析**: [[20_Research/Papers/具身智能/The_Latent_That_Never_Was_A_Forensic_Re-run_of_the_CVAE_Ablation_in_Action_Chunking_Transformer|The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer]]
- **作者**: Bo Kang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformer》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action Chunking Transformers (ACT) are widely used to learn robot manipulation from demonstrations. Their conditional variational autoencoder includes an encoder meant to capture differences between demonstrations during training. The original ACT paper reported that encoder removal dropped the mean success rate from 35% to 2% on two simulated tasks with human demonstrations. We re-ran this ablation in the original code and checked whether the findings depend on the implementation or training data. The published drop does not reappear in our tests, although smaller gains or losses in success rate remain uncertain. To investigate the discrepancy, we varied training length and how checkpoints are selected for evaluation. Both can reverse which policy scores higher, but the published drop's cause remains unknown. Success rates alone leave open whether the encoder provides information that helps the policy reconstruct demonstrated actions. On the tested ACT benchmark, the sampled latent provides little reconstruction benefit at every tested nonzero weight of the penalty on latent information. At inference, ACT leaves this latent unused and sets it to zero. Skipping the encoder increases training throughput in both implementations we timed. We release code, evaluation tools and results so others can repeat the comparisons and test the encoder on other tasks.

</details>

---

### [[20_Research/Papers/强化学习/Fast-Convergent_Meta-RL_via_Gradient-Clustered_BS_Sampling_for_Edge_Caching|Fast-Convergent Meta-RL via Gradient-Clustered BS Sampling for Edge Caching]]

![[assets/2609.16370_figure.png|800]]

- **arXiv**: [2609.16370](https://arxiv.org/abs/2609.16370)
- **PDF**: https://arxiv.org/pdf/2609.16370
- **详细分析**: [[20_Research/Papers/强化学习/Fast-Convergent_Meta-RL_via_Gradient-Clustered_BS_Sampling_for_Edge_Caching|Fast-Convergent Meta-RL via Gradient-Clustered BS Sampling for Edge Caching]]
- **作者**: Farnaz Niknia, Ping Wang
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Fast-Convergent Meta-RL via Gradient-Clustered BS Sampling for Edge Caching》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Meta-RL, T-CacheNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wireless edge caching networks typically consist of many independent Base Stations (BSs), each facing its own request rate and content popularity profile. Training a Reinforcement Learning (RL) caching agent from scratch at every BS forces each agent to relearn, through slow trial and error, a decision problem that is structurally identical across the network. Meta-reinforcement learning removes this redundancy by learning a shared initialization that adapts to any BS in a few local updates; however, meta-training itself becomes the bottleneck at scale: the meta-gradient must be estimated from a small subset of BSs at each meta-iteration, and sampling this subset uniformly at random yields a high-variance estimate, an issue existing meta-RL caching frameworks leave unaddressed. This paper proposes a meta-reinforcement learning framework for caching across independent, non-overlapping BSs that directly targets this bottleneck. Each BS runs a local Proximal Policy Optimization (PPO) agent, formulated as a Semi-Markov Decision Process (SMDP) over content popularity, size, lifetime, and importance, while a shared meta-policy is learned via a Model-Agnostic Meta-Learning (MAML)-style loop. To scale meta-training and accelerate convergence, we introduce gradient-based clustering, which groups BSs by local gradient similarity and draws from every cluster, in proportion to its size, at each meta-iteration. We prove, via an Analysis of Variance (ANOVA)-style decomposition of gradient variance, that this strategy yields a strictly lower-variance meta-gradient estimator than uniform random sampling under BS heterogeneity.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Droplet_Navigation_via_Model-Based_Reinforcement_Learning|Autonomous Droplet Navigation via Model-Based Reinforcement Learning]]

![[assets/2609.16369_first_page.png|800]]

- **arXiv**: [2609.16369](https://arxiv.org/abs/2609.16369)
- **PDF**: https://arxiv.org/pdf/2609.16369
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Droplet_Navigation_via_Model-Based_Reinforcement_Learning|Autonomous Droplet Navigation via Model-Based Reinforcement Learning]]
- **作者**: Rajneesh Anand, Mayuresh V. Kothare
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 0.96，世界模型 0.96）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Autonomous Droplet Navigation via Model-Based Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise manipulation of liquid droplets underpins lab-on-a-chip platforms for diagnostics, chemical synthesis, and biological assays. Yet autonomous droplet transport through confined geometries of varying complexity remains an open challenge. Droplets exhibit contact-angle hysteresis, deformability, and capillary pinning, which make their response to actuation nonlinear and history dependent, that classical controllers and pre-programmed trajectories cannot cope in multi-turn environments. Here we demonstrate autonomous navigation of a liquid droplet through geometries of increasing complexity on a gravity driven (Labyrinth) platform using model-based reinforcement learning. A thin silicone oil film reduces contact-line pinning while two-axis tilt supplies the gravitational driving force, and an overhead camera tracks the droplet in real time. An offline-trained policy discovers effective tilt strategies from limited physical interaction data, without simulation or analytical droplet models. The system operates under partial observability, as oil-film thickness, instantaneous contact angle, and droplet deformation state remain hidden from the controller. Despite these challenges, the learned policy achieves reliable navigation across straight, right-angle, and curved-arc paths, including outside-corner geometries. We further demonstrate that a policy trained on a simpler geometry transfers to complex ones, succeeding zero-shot on right-angle and staircase paths and reaching full success on a curved arc with a fifth of the training data. The findings suggest promising avenues for enabling droplet based microfluidic systems to serve as intelligent chemical laboratories.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Surrogate_Based_Dequantization_of_Quantum_Reinforcement_Learning|Towards Surrogate Based Dequantization of Quantum Reinforcement Learning]]

![[assets/2609.16266_figure.png|800]]

- **arXiv**: [2609.16266](https://arxiv.org/abs/2609.16266)
- **PDF**: https://arxiv.org/pdf/2609.16266
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Surrogate_Based_Dequantization_of_Quantum_Reinforcement_Learning|Towards Surrogate Based Dequantization of Quantum Reinforcement Learning]]
- **作者**: Pablo Rodriguez-Grasa, Sofiene Jerbi, Mikel Sanz, Ryan Sweke
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Towards Surrogate Based Dequantization of Quantum Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, the utility of parameterized quantum circuits as function approximators has been widely studied. In the context of reinforcement learning, this approach has led to variational quantum algorithms such as quantum Q-learning. While these methods show promising empirical results, and can provide provable advantages for artificial problems, it remains unclear whether they can provide a provable quantum advantage over classical approaches for problems of practical relevance. A natural way to investigate this question is through the lens of dequantization: The construction of efficient classical algorithms capable of matching the performance of quantum variational methods. Building on recent kernel-based dequantization results for supervised learning, we take steps towards extending this surrogate-based dequantization program to reinforcement learning. Specifically, we study the simplified setting of reinforcement learning with a uniform generative model in which uniformly random state-action samples are available, which models the regime of sampling from a large experience replay buffer after sufficient exploration. Within this setting, we provide finite sample guarantees for classical kernelized Fitted Q-Iteration, with classical kernels designed to match the inductive bias of particular parameterized quantum circuits. Using these results, we then provide a set of sufficient conditions, on the data-encoding strategy of a parameterized quantum circuit, the corresponding classical kernel, and the problem structure, under which kernelized Fitted Q-Iteration provides a meaningful dequantization of quantum Q-learning, in this simplified setting. Apart from providing rigorous dequantization guarantees when these conditions are met, these results also motivate the use of kernelized fitted Q-iteration as a dequantization heuristic when these sufficient conditions cannot be verified.

</details>

---
