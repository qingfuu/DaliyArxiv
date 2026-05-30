# cs.LG | Machine Learning | 2026-05-28

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/强化学习/Optimal_Data_Acquisition_for_Reinforcement_Learning_A_Large_Deviations_Perspective|Optimal Data Acquisition for Reinforcement Learning: A Large Deviations Perspective]]

![[assets/2605.28675_figure.png|800]]

- **arXiv**: [2605.28675](https://arxiv.org/abs/2605.28675)
- **PDF**: https://arxiv.org/pdf/2605.28675
- **详细分析**: [[20_Research/Papers/强化学习/Optimal_Data_Acquisition_for_Reinforcement_Learning_A_Large_Deviations_Perspective|Optimal Data Acquisition for Reinforcement Learning: A Large Deviations Perspective]]
- **作者**: Mingjie Hu, Jian-Qiang Hu, Enlu Zhou
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Optimal Data Acquisition for Reinforcement Learning: A Large Deviations Perspective》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data acquisition efficiency is a central challenge in deploying reinforcement learning in business and healthcare operations, where interactions are costly, slow, and often involve humans in the loop. This paper develops a unified large deviations framework for data acquisition in infinite-horizon reinforcement learning. We introduce the exponential decay rate of the policy-selection error probability as a principled efficiency metric and derive a variational characterization of this rate via large deviations theory for Markov chains, yielding a nested optimization problem. Based on this characterization, we formalize two complementary notions of optimality in terms of the optimal solution of the nested problem. Because the resulting program is implicit and generally intractable, we propose a tractable convex relaxation with explicit constraints. We then develop a lazy one-step projected subgradient method to solve the relaxed problem and use its iterates to construct an adaptive data acquisition policy. We prove that the resulting reinforcement learning algorithm is near-robustly optimal under our optimality criterion, up to a constant factor. Finally, we extend the framework to linear function approximation to improve scalability, and numerical experiments support the effectiveness of the proposed approach.

</details>

---

### [[20_Research/Papers/具身智能/SPRINT_Efficient_Spectral_Priors_for_Humanoid_Athletic_Sprints|SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints]]

![[assets/2605.28549_figure.png|800]]

- **arXiv**: [2605.28549](https://arxiv.org/abs/2605.28549)
- **PDF**: https://arxiv.org/pdf/2605.28549
- **详细分析**: [[20_Research/Papers/具身智能/SPRINT_Efficient_Spectral_Priors_for_Humanoid_Athletic_Sprints|SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints]]
- **作者**: Yantong Wei, Kaihong Huang, Hainan Pan, Jiawei Luo, Jiawei Zhou, Ziyan Mai, Zhiwen Zeng, Yaonan Wang, Huimin Lu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Humanoid-Gym, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The pursuit of humanoid athletic sprints is hindered by a scarcity of humanoid-viable kinematic reference data and the inability of existing frameworks to maintain stability during sprints. To overcome these limitations, we introduce SPRINT, a novel framework driven by efficient, frequency-adaptive spectral priors. By characterizing the fundamental periodicity of human locomotion in the frequency domain using a reference library of five discrete motion sequences, these priors generate kinematically feasible joint trajectories across a broad velocity spectrum, successfully extrapolating to speeds that exceed the reference distribution. Guided by these pretrained priors, the SPRINT policy achieves zero-shot sim-to-real transfer in field experiments on the Unitree G1 platform, reaching a peak sprinting velocity of 6 m/s and demonstrating seamless gait transitions while preserving biomimetic naturalness. Ultimately, this work establishes frequency-adaptive spectral priors as a highly data-efficient foundation for humanoid athletic sprints. The project page is available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/Tactile-Proprioceptive_Sensor_Fusion_for_Contact_Wrench_Estimation_in_Whole-Body_Physical_Human-Robot_Interaction|Tactile-Proprioceptive Sensor Fusion for Contact Wrench Estimation in Whole-Body Physical Human-Robot Interaction]]

![[assets/2605.28412_figure.png|800]]

- **arXiv**: [2605.28412](https://arxiv.org/abs/2605.28412)
- **PDF**: https://arxiv.org/pdf/2605.28412
- **详细分析**: [[20_Research/Papers/机器人/Tactile-Proprioceptive_Sensor_Fusion_for_Contact_Wrench_Estimation_in_Whole-Body_Physical_Human-Robot_Interaction|Tactile-Proprioceptive Sensor Fusion for Contact Wrench Estimation in Whole-Body Physical Human-Robot Interaction]]
- **作者**: Junha Min, Junghyeon Ma, Jiwung Kwon, Sunggyu Bae, Joohyung Kim, Kyungseo Park
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Tactile-Proprioceptive Sensor Fusion for Contact Wrench Estimation in Whole-Body Physical Human-Robot Interaction》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Direct physical guidance is a natural means of teaching and interacting with robots, and robotic skins make a key contribution by enabling sensitive contact sensing and localization. This paper presents a tactile-proprioceptive sensor fusion framework for natural physical human-robot interaction. Tactile cues from pneumatic skin pads serve as contact indicators that bypass the ambiguity between frictional residues and applied external forces, enabling highly sensitive contact detection without explicit friction identification. We fuse these cues with motor-current-based proprioception to reconstruct multi-axis contact forces on the robot surface. To maintain accuracy during motion, we employ a temporal convolutional network (TCN) to mitigate friction hysteresis during stick-slip transitions, reducing uncertainty at contact onset and yielding smooth, responsive guidance. We validate the approach on a skin-integrated robot arm: (i) multi-axis forces are reconstructed in stationary contacts, and (ii) simultaneous force estimation and kinesthetic teaching are demonstrated. Results indicate improved sensitivity and responsiveness across diverse contact conditions compared with tactile-only and proprioceptive-only baselines, supporting tactile-proprioceptive fusion as a reliable pathway to safe, intuitive physical human-robot interaction.

</details>

---

### [[20_Research/Papers/强化学习/Teacher-Student_Representational_Alignment_for_Reinforcement_Learning-Driven_Imitation_Learning|Teacher-Student Representational Alignment for Reinforcement Learning-Driven Imitation Learning]]

![[assets/2605.28372_figure.png|800]]

- **arXiv**: [2605.28372](https://arxiv.org/abs/2605.28372)
- **PDF**: https://arxiv.org/pdf/2605.28372
- **详细分析**: [[20_Research/Papers/强化学习/Teacher-Student_Representational_Alignment_for_Reinforcement_Learning-Driven_Imitation_Learning|Teacher-Student Representational Alignment for Reinforcement Learning-Driven Imitation Learning]]
- **作者**: Meraj Mammadov, Pedro Zuidberg Dos Martires, Johannes Andreas Stork
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.02（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Teacher-Student Representational Alignment for Reinforcement Learning-Driven Imitation Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning (IL) from a state-based reinforcement learning (RL) policy is a common approach to overcome the curse of dimensionality in complex and high-dimensional observation spaces prevalent in robotics. This paper addresses the irreducible imitation gap that emerges when teacher and student are learned in isolation, and the teacher policy has the liberty to rely on privileged state information that the student cannot infer from its observations. Instead of improving poor student performance with RL finetuning after IL, which often requires a whole new training setup, we propose a novel algorithm which learns a shared embedding space that hides agent-specific observations and thus trains imitable teacher policies by construction. We train the shared embedding space with self-supervised contrastive learning in parallel to the teacher policy and prevent it from extracting private information by limiting its gradients from updating the encoder networks. We perform evaluations on several example domains and compare to state-of-the-art baselines showing that our algorithm enables higher student performance with substantially reduced imitation gap.

</details>

---

### [[20_Research/Papers/具身智能/LEIA_Learned_Environment_for_Interactive_Architected_Materials|LEIA: Learned Environment for Interactive Architected Materials]]

![[assets/2605.28368_figure.png|800]]

- **arXiv**: [2605.28368](https://arxiv.org/abs/2605.28368)
- **PDF**: https://arxiv.org/pdf/2605.28368
- **详细分析**: [[20_Research/Papers/具身智能/LEIA_Learned_Environment_for_Interactive_Architected_Materials|LEIA: Learned Environment for Interactive Architected Materials]]
- **作者**: Haiqian Yang, Yuan Cao, Markus J. Buehler
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 1.22（加权：具身智能 0.3，强化学习 0.16，世界模型 0.56，机器人 0.2）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《LEIA: Learned Environment for Interactive Architected Materials》归入 世界模型、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DE-DeepONet, DeepONet, LatticeGraphNet, MeshGraphNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have enabled interactive exploration of game environments and robotic manipulation, but physical engineering remains beyond their reach: real materials exhibit nonlinear constitutive laws, carry history-dependent internal state, undergo inertial dynamics, and may possess hierarchical structures spanning multiple length scales. We present LEIA (Learned Environment for Interactive Architected materials), a world model that lets engineers apply boundary conditions step by step and observe the resulting deformation and stress fields in real time. LEIA handles large three-dimensional unstructured meshes and generates autoregressive responses to user-specified loading. We introduce MicroPlate, a benchmark of architected plates spanning two regimes of microstructure modeling: architected lattices that resolve microstructure explicitly through three-dimensional geometry, and a homogeneous plate where microstructural change is modeled implicitly through internal degrees of freedom. MicroPlate is used to assess LEIA alongside four baseline methods across both regimes. Finally, we demonstrate that LEIA enables efficient candidate generation and ranking for fast surrogate-guided search for de novo designs of architected materials, with stress-accurate candidate ranking validated by finite element ground truth.

</details>

---

### [[20_Research/Papers/强化学习/Variance-Adaptive_Optimal_Algorithm_for_Reinforcement_Learning_with_Multinomial_Logit_Function_Approximation|Variance-Adaptive Optimal Algorithm for Reinforcement Learning with Multinomial Logit Function Approximation]]

![[assets/2605.28364_figure.png|800]]

- **arXiv**: [2605.28364](https://arxiv.org/abs/2605.28364)
- **PDF**: https://arxiv.org/pdf/2605.28364
- **详细分析**: [[20_Research/Papers/强化学习/Variance-Adaptive_Optimal_Algorithm_for_Reinforcement_Learning_with_Multinomial_Logit_Function_Approximation|Variance-Adaptive Optimal Algorithm for Reinforcement Learning with Multinomial Logit Function Approximation]]
- **作者**: Wonyoung Kim, Min-Hwan Oh, Garud Iyengar, Assaf Zeevi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Variance-Adaptive Optimal Algorithm for Reinforcement Learning with Multinomial Logit Function Approximation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with multinomial logistic (MNL) function approximation has become an important framework due to its flexibility and broad applicability. While existing studies have established regret guarantees under worst-case analysis, they do not capture how performance depends on the variability of the interaction between the learner and the environment. In this paper, we develop a new theoretical analysis for MNL-based Markov decision processes that yields explicit variance-adaptive regret bounds. Our algorithm is computationally efficient and achieves the instance-wise optimal rate of regret, narrowing the gap between upper and lower bounds. Our numerical experiments validate that our method learns optimal policies more efficiently than conventional approaches.

</details>

---

### [[20_Research/Papers/强化学习/AtomComposer_Discovering_Chemical_Space_from_First_Principles_with_Reinforcement_Learning|AtomComposer: Discovering Chemical Space from First Principles with Reinforcement Learning]]

![[assets/2605.28287_figure.png|800]]

- **arXiv**: [2605.28287](https://arxiv.org/abs/2605.28287)
- **PDF**: https://arxiv.org/pdf/2605.28287
- **详细分析**: [[20_Research/Papers/强化学习/AtomComposer_Discovering_Chemical_Space_from_First_Principles_with_Reinforcement_Learning|AtomComposer: Discovering Chemical Space from First Principles with Reinforcement Learning]]
- **作者**: Bjarke Hastrup, Francois Cornet, Tejs Vegge, Arghya Bhowmik
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《AtomComposer: Discovering Chemical Space from First Principles with Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MolGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discovering novel stable molecules without training data remains a grand scientific challenge. Current molecular generative models are trained on large, pre-curated datasets, which introduce biases and limit exploration of novel chemistry. In contrast, we propose a new paradigm: autonomous, generalized agents capable of mapping vast, unknown chemical spaces without any pretraining. For the first time, we present AtomComposer, a self-guided agent that autonomously constructs valid 3D isomers under stoichiometric constraints and is trained exclusively online using reinforcement learning. Unlike existing approaches that generally overfit to a specific chemical formula, we establish a multi-composition training scheme that enables a broad generalization across diverse chemistry, guided by energy- and validity-based rewards. Our agent can discover up to an order of magnitude more valid isomers on unseen test formulas than existing single-composition reinforcement-learning baselines trained with per-step energy rewards. These results fulfill the promise of online reinforcement learning as a powerful paradigm for scalable, from-scratch exploration of chemical configuration space.

</details>

---

### [[20_Research/Papers/强化学习/Commit_to_the_Bit_Reactive_Reinforcement_Learning_Done_Right|Commit to the Bit: Reactive Reinforcement Learning Done Right]]

![[assets/2605.28276_first_page.png|800]]

- **arXiv**: [2605.28276](https://arxiv.org/abs/2605.28276)
- **PDF**: https://arxiv.org/pdf/2605.28276
- **详细分析**: [[20_Research/Papers/强化学习/Commit_to_the_Bit_Reactive_Reinforcement_Learning_Done_Right|Commit to the Bit: Reactive Reinforcement Learning Done Right]]
- **作者**: Onno Eberhard, Claire Vernade, Michael Muehlebach
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Commit to the Bit: Reactive Reinforcement Learning Done Right》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning algorithms are commonly analyzed (and designed) under the Markov assumption. This is unrealistic, as most environments encountered in practice are either partially observable, or require function approximation that restricts the agent to access non-Markovian state features. We consider the problem of learning an optimal reactive policy in a finite environment with deterministic observations (or equivalently, hard state aggregation). We introduce a new algorithm, Committed Q-learning, and prove almost-sure convergence to the optimal reactive policy under an intuitive assumption we call rewire-robustness. This assumption is strictly weaker than the $q_\star$-realizability condition used in prior work. Our algorithm is a variant of classical Q-learning in which the behavior policy commits to a single action upon entering a feature, and only resamples actions when the observed feature changes. A crucial part of our analysis is the introduction of quasi-Markov environments.

</details>

---

### [[20_Research/Papers/具身智能/ProgVLA_Progress-Aware_Robot_Manipulation_Skill_Learning|ProgVLA: Progress-Aware Robot Manipulation Skill Learning]]

![[assets/2605.28231_figure.png|800]]

- **arXiv**: [2605.28231](https://arxiv.org/abs/2605.28231)
- **PDF**: https://arxiv.org/pdf/2605.28231
- **详细分析**: [[20_Research/Papers/具身智能/ProgVLA_Progress-Aware_Robot_Manipulation_Skill_Learning|ProgVLA: Progress-Aware Robot Manipulation Skill Learning]]
- **作者**: Seungsu Kim, Jinyoung Choi, Seungmin Baek, Jean-Michel Renders
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.72（加权：具身智能 2.1，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ProgVLA: Progress-Aware Robot Manipulation Skill Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Meta-World, ProgVLA, SmolVLA, SuccessVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ProgVLA, a compact vision-language-action (VLA) model designed for reliable robot manipulation under tight compute and memory budgets. The model specifically focuses on efficiently processing long multi-modal sequences by maintaining an explicit representation of task progress over extended horizons. To this end, ProgVLA integrates two key components. First, a multi-modal encoder with a two-stage Perceiver resampling scheme compresses variable-length visual, language, and proprioceptive streams into a fixed set of control-ready context tokens, substantially reducing sequence length while preserving cross-modal grounding. Second, an auxiliary set of progress heads is trained with offline reinforcement learning (RL) objectives to jointly learn critics over normalized remaining-horizon targets. This provides the policy with an internal estimate of task progress and enables advantage- and success-weighted flow-matching imitation learning. On two well-established multi-task robot manipulation benchmarks, a 0.1B-parameter ProgVLA model reaches success rates that are competitive with, and on long-horizon and harder task tiers exceed, substantially larger pretrained baselines. Ablations indicate that the learned context resampler and task-adaptive visual fine-tuning are the largest single contributors, while progress-aware training provides a consistent additional gain that is concentrated on long-horizon and multi-object tasks. We further validate the approach in real-world toy-kitchen environments.

</details>

---

### [[20_Research/Papers/强化学习/Joint_Training_of_Multi-Token_Prediction_in_Reinforcement_Learning_via_Optimal_Coefficient_Calibration|Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration]]

![[assets/2605.28184_figure.png|800]]

- **arXiv**: [2605.28184](https://arxiv.org/abs/2605.28184)
- **PDF**: https://arxiv.org/pdf/2605.28184
- **详细分析**: [[20_Research/Papers/强化学习/Joint_Training_of_Multi-Token_Prediction_in_Reinforcement_Learning_via_Optimal_Coefficient_Calibration|Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration]]
- **作者**: Zili Wang, Jiajun Chai, Lin Chen, Xiaohan Wang, Shiming Xiang, Guojun Yin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MTP-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as the standard paradigm for improving reasoning capability of large language models, while Multi-Token Prediction (MTP) has been a widely adopted module in pretraining. Combining them is a natural approach, yet current RL practices detach MTP gradients because joint training degrades the performance. We revisit this failure from an optimization perspective. We show that the per-step effect of MTP on the RL objective can be decomposed into two terms: a first-order correlation and a second-order perturbation penalty. This decomposition unifies three MTP training regimes: Detach, Cross-Entropy loss, and Policy loss, and explains why each succeeds or fails. Further analysis of policy loss reveals that, although it aligns with intuition, performance still degrades: the correlation term decays while the quadratic penalty persists. Guided by the analysis, we propose Optimal Coefficient Calibration (OCC), an adaptive scheme that tracks the optimal coefficient online via a log-probability proxy at negligible cost. Across six competition-level mathematical reasoning benchmarks, OCC consistently matches or exceeds the detach baseline, delivering improved joint MTP-RL training performance.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Coarse-to-Fine_Subgoal_Refinement_for_Long-Horizon_Offline_Goal-Conditioned_Reinforcement_Learning|Adaptive Coarse-to-Fine Subgoal Refinement for Long-Horizon Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2605.28127_figure.png|800]]

- **arXiv**: [2605.28127](https://arxiv.org/abs/2605.28127)
- **PDF**: https://arxiv.org/pdf/2605.28127
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Coarse-to-Fine_Subgoal_Refinement_for_Long-Horizon_Offline_Goal-Conditioned_Reinforcement_Learning|Adaptive Coarse-to-Fine Subgoal Refinement for Long-Horizon Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Kaiqiang Ke, Shenghong He, Chengdong Xu, Yuheng Luo, Xiangyuan Lan, Chao Yu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Adaptive Coarse-to-Fine Subgoal Refinement for Long-Horizon Offline Goal-Conditioned Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CFHRL, GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning (GCRL) is challenging in long-horizon tasks, where distant state--goal pairs provide weak supervision and value estimates become vulnerable to accumulated bootstrapping errors. Hierarchical methods mitigate this difficulty by introducing intermediate subgoals, but fixed temporal abstractions or fixed hierarchy depths can be mismatched to state--goal pairs with different reachability horizons. We propose Coarse-to-Fine Hierarchical Goal Reinforcement Learning (CFHRL), a fully offline GCRL framework that adaptively refines distant goals before execution. Starting from the final goal, CFHRL recursively proposes intermediate targets, trained from replay-supported candidates, and stops refinement once the current target is estimated to be locally executable by a learned reachability cost. The key idea is that a subgoal need not be an exact midpoint or globally optimal waypoint; it only needs to provide reliable progress and reduce the remaining reaching difficulty, enabling subsequent refinement over shorter horizons. A stylized analysis further supports the robustness of approximate recursive contraction. Experiments on OGBench show substantial gains on several long-horizon tasks, with ablations validating the proposed refinement and stopping mechanisms

</details>

---

### [[20_Research/Papers/世界模型/Chreode_A_Cell_World_Model_for_One-Step_Temporal_Dynamics_and_Perturbation_Prediction|Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction]]

![[assets/2605.28111_figure.png|800]]

- **arXiv**: [2605.28111](https://arxiv.org/abs/2605.28111)
- **PDF**: https://arxiv.org/pdf/2605.28111
- **详细分析**: [[20_Research/Papers/世界模型/Chreode_A_Cell_World_Model_for_One-Step_Temporal_Dynamics_and_Perturbation_Prediction|Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction]]
- **作者**: Mufan Qiu, Genhui Zheng, Yinuo Xu, Ruichen Zhang, Ying Ding, Qi Long, Tianlong Chen
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Chreode: A Cell World Model for One-Step Temporal Dynamics and Perturbation Prediction》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TrajectoryNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how a cell will change its transcriptional state under a developmental signal or a genetic perturbation is the computational core of in-silico biology and the AI Virtual Cell program. Existing approaches either fit static control-to-treated maps that discard time, or solve multi-step ODE / Schrödinger-bridge problems on each dataset independently. We introduce Chreode, a one-step cell world model that predicts action-conditioned cell-state transitions through a structured residual transition operator. It shifts distributional evolution from inference time to training time, enabling single-pass generation while preserving a Waddington-inspired decomposition into downhill landscape flow, rotational in-tangent dynamics, and stochastic spread. The model is pretrained with a shared scVI encoder and a DiT-based dynamics backbone on a 2.4M-cell mouse embryonic atlas spanning 7 datasets. As a fine-tuning initialization, Chreode improves per-target Sinkhorn distance on Weinreb hematopoiesis and Veres islet differentiation over matched scratch models, PI-SDE, and PRESCIENT. As a transferable gene-state embedding for GEARS, the pretrained dynamics representation reduces shared-vocabulary DE20 mean squared error on Norman Perturb-seq from 0.2121 to 0.1858, a 12.4% relative improvement, without changing the GEARS training procedure. We interpret this transfer to perturbation prediction as evidence that pretrained developmental-trajectory dynamics encode differentiation primitives transferable to CRISPR-induced state shifts, since both involve cell-state transitions in a shared latent geometry. The pretrained backbone additionally produces zero-shot clonal fate scores on Weinreb that are competitive with strong dynamic-OT baselines.

</details>

---

### [[20_Research/Papers/强化学习/Long_Live_The_Balance_Information_Bottleneck_Driven_Tree-based_Policy_Optimization|Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization]]

![[assets/2605.28109_first_page.png|800]]

- **arXiv**: [2605.28109](https://arxiv.org/abs/2605.28109)
- **PDF**: https://arxiv.org/pdf/2605.28109
- **详细分析**: [[20_Research/Papers/强化学习/Long_Live_The_Balance_Information_Bottleneck_Driven_Tree-based_Policy_Optimization|Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization]]
- **作者**: Hao Jiang, Shurui Li, Tianpeng Bu, Bowen Xu, Xin Liu, Qihua Chen, Hongtao Duan, Lulu Hu, Bin Yang, Minying Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in online reinforcement learning (RL) for large language models (LLMs) have demonstrated promising performance in complex reasoning tasks. However, they often exhibit an imbalanced exploration-exploitation trade-off, resulting in unstable optimization and sub-optimal performance. We introduce IB-Score, a novel metric grounded in Information Bottleneck theory that evaluates policy's exploration-exploitation balance by quantifying the trade-off between step-level reasoning diversity and mutual information shared with the correct answer. Analysis based on IB-Score shows that popular online RL approaches (e.g., GRPO) with common regularizers fail to consistently maintain balance during training with suboptimal results. To address this, we propose Information Bottleneck-driven Tree-based Policy Optimization (IB-TPO), a principled framework that formulates IB-Score as a fine-grained optimization objective and utilizes a novel IB-guided tree sampling strategy that not only improves the efficiency of online sampling with 50% more trajectories under the same token budget, but also reuses the tree structure for effective IB-Score Monte Carlo estimation. Extensive experiments across standard benchmarks show that our method significantly outperforms GRPO baseline by 2.9% to 3.6% and also outperforms other state-of-the-art online RL approaches. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/BPPO_Binary_Prefix_Policy_Optimization_for_Efficient_GRPO-Style_Reasoning_RL_with_Concise_Responses|BPPO: Binary Prefix Policy Optimization for Efficient GRPO-Style Reasoning RL with Concise Responses]]

![[assets/2605.28028_figure.png|800]]

- **arXiv**: [2605.28028](https://arxiv.org/abs/2605.28028)
- **PDF**: https://arxiv.org/pdf/2605.28028
- **详细分析**: [[20_Research/Papers/强化学习/BPPO_Binary_Prefix_Policy_Optimization_for_Efficient_GRPO-Style_Reasoning_RL_with_Concise_Responses|BPPO: Binary Prefix Policy Optimization for Efficient GRPO-Style Reasoning RL with Concise Responses]]
- **作者**: Qingfei Zhao, Huan Song, Shuyu Tian, Jiawei Shao, Xuelong Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《BPPO: Binary Prefix Policy Optimization for Efficient GRPO-Style Reasoning RL with Concise Responses》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group Relative Policy Optimization (GRPO) is widely used for training reasoning models, but updating all sampled completions in each group incurs substantial cost and can reinforce verbose reasoning trajectories. In this paper, we study whether all completions provide equally useful update signals in GRPO-style reasoning RL. Our gradient-similarity analysis shows that, within the same prompt group, same-class completions often induce highly similar update directions, whereas correct-incorrect pairs provide more distinct contrastive signals. Motivated by this observation, we propose Binary Prefix Policy Optimization (BPPO), which uses the shortest correct completion and the shortest incorrect completion as a compact update unit while preserving full-group advantage normalization. BPPO further improves efficiency with adaptive completion scheduling and prefix-focused optimization; by updating only response prefixes, it avoids reinforcing redundant suffixes and encourages more concise responses. Experiments on GSM8K, MATH, and Geo3K show that BPPO achieves up to 6.08x speedup over GRPO while maintaining competitive accuracy, and reduces mean response length by approximately 30-50% without modifying the reward with an explicit length penalty.

</details>

---

### [[20_Research/Papers/强化学习/Cyclical_Entropy_Eruption_Entropy_Dynamics_in_Agent_Reinforcement_Learning|Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning]]

![[assets/2605.27954_figure.png|800]]

- **arXiv**: [2605.27954](https://arxiv.org/abs/2605.27954)
- **PDF**: https://arxiv.org/pdf/2605.27954
- **详细分析**: [[20_Research/Papers/强化学习/Cyclical_Entropy_Eruption_Entropy_Dynamics_in_Agent_Reinforcement_Learning|Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning]]
- **作者**: Wendi Li, Shawn Im, Sharon Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Agent-RL, AlfWorld, VeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic large language models are increasingly used to solve real-world tasks by reasoning over goals, invoking tools, and interacting with external environments. Reinforcement learning provides a natural framework for improving these behaviors, and recent agent RL methods have achieved strong results across domains. However, the training dynamics of agent RL remain poorly understood, limiting our ability to diagnose instabilities and design more effective training algorithms. In this work, we identify a previously underexplored phenomenon in agent RL, which we term cyclical entropy eruption. Unlike single-turn reasoning RL, where entropy typically collapses and stays low, agent RL training exhibits unique recurring cycles of sharp entropy eruption and gradual subsidence. We decompose this dynamic into three phases and provide theoretical and empirical analyses of each, explaining the mechanisms underlying its cyclical oscillation. We further show that degenerate patterns such as sentence duplication and hallucination, once acquired during eruption, can persist and accumulate across cycles. Motivated by these findings, we propose SEAL (Separation-Enhanced Agent Learning), a lightweight auxiliary loss that separates correct and incorrect trajectories in representation space, directly targeting the root cause of entropy eruption. Experiments across multiple benchmarks, models, and RL algorithms demonstrate that SEAL stabilizes training and yields stronger downstream agent performance.

</details>

---

### [[20_Research/Papers/具身智能/Frequency-Guided_Action_Diffusion_via_Sub-Frequency_Manifold_Traversal|Frequency-Guided Action Diffusion via Sub-Frequency Manifold Traversal]]

![[assets/2605.27919_figure.png|800]]

- **arXiv**: [2605.27919](https://arxiv.org/abs/2605.27919)
- **PDF**: https://arxiv.org/pdf/2605.27919
- **详细分析**: [[20_Research/Papers/具身智能/Frequency-Guided_Action_Diffusion_via_Sub-Frequency_Manifold_Traversal|Frequency-Guided Action Diffusion via Sub-Frequency Manifold Traversal]]
- **作者**: Junlin Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Frequency-Guided Action Diffusion via Sub-Frequency Manifold Traversal》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning visuomotor policies via behavior cloning typically involves mimicking expert demonstrations collected by human operators. However, natural human demonstrations inherently contain high-frequency noise, such as intermittent jerks, pauses, and action jitter. Training policies to directly imitate these raw trajectories inevitably causes the model to inherit these suboptimal behaviors. This pathology is particularly pronounced in diffusion-based policies, where iterative denoising steps can inadvertently amplify high-frequency artifacts at the expense of meaningful fine-grained details. To address these limitations, we present a novel frequency-based algorithm that enables implicit spectral maneuvering and smooth action generation. Our method, Frequency Guidance Operator (FGO), steers the generation process of diffusion polices by progressively driving the noisy samples through intermediate sub-frequency manifolds with expanding spectral bands. Validated on 15 robotic manipulation tasks from 5 benchmarks, FGO achieves superior performance in enhancing action smoothness and temporal consistency while preserving the details necessary for successful task execution. Project website: this https URL

</details>

---

### [[20_Research/Papers/强化学习/Reward_Transfer_from_Inverse_Reinforcement_Learning_A_Coupled_Minimax_Approach|Reward Transfer from Inverse Reinforcement Learning: A Coupled Minimax Approach]]

![[assets/2605.27834_figure.png|800]]

- **arXiv**: [2605.27834](https://arxiv.org/abs/2605.27834)
- **PDF**: https://arxiv.org/pdf/2605.27834
- **详细分析**: [[20_Research/Papers/强化学习/Reward_Transfer_from_Inverse_Reinforcement_Learning_A_Coupled_Minimax_Approach|Reward Transfer from Inverse Reinforcement Learning: A Coupled Minimax Approach]]
- **作者**: Guang-Yuan Hao, Lars van der Laan, Aurélien Bibaut, Nathan Kallus
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Reward Transfer from Inverse Reinforcement Learning: A Coupled Minimax Approach》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the transfer of rewards learned using inverse reinforcement learning from expert demonstrations in one environment to reinforcement learning in a new, different environment. This arises naturally when demonstrations are collected in a controlled environment. We formulate the problem as a joint system of Bellman equations across the source and target environments and develop minimax estimators for the target soft-$q$-function. Whereas a sequential solution approach first estimates the source reward and then plugs it into the target control problem, a coupled approach solves the source and target system of equations jointly. We show that, in contrast to the sequential approach, the coupled approach removes the first-order influence of source Bellman residual error. We characterize the local behavior of each approach, develop finite-sample soft-$q$-function error bounds, and prove regret guarantees for the resulting soft-control policy. An empirical investigation using a sepsis simulator validates the theoretical comparison.

</details>

---

### [[20_Research/Papers/强化学习/Accelerating_Reinforcement_Learning_Training_Using_Simulation_Surrogate_Models|Accelerating Reinforcement Learning Training Using Simulation Surrogate Models]]

![[assets/2605.27556_figure.png|800]]

- **arXiv**: [2605.27556](https://arxiv.org/abs/2605.27556)
- **PDF**: https://arxiv.org/pdf/2605.27556
- **详细分析**: [[20_Research/Papers/强化学习/Accelerating_Reinforcement_Learning_Training_Using_Simulation_Surrogate_Models|Accelerating Reinforcement Learning Training Using Simulation Surrogate Models]]
- **作者**: Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Accelerating Reinforcement Learning Training Using Simulation Surrogate Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-fidelity simulation models are widely used to analyze complex stochastic systems, but their high computational cost motivates the development of cheaper surrogate models that approximate the simulation model's input-output relationship. In parallel, reinforcement learning (RL) has emerged as a powerful framework for making online decisions in stochastic environments, with increasing attention being given to the use of simulation models as training environments for RL models. We investigate a class of surrogate models suitable for accelerating RL training in settings where the reward structure, model parameters, or system dynamics change over time and explore their interactions with simulation models and RL models. Through numerical experiments on a stochastic service system modeled via discrete-event simulation, we demonstrate that leveraging surrogate models can substantially accelerate RL training and re-training.

</details>

---
