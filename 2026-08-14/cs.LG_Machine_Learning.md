# cs.LG | Machine Learning | 2026-08-14

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Online_Inference_for_Quantile_Temporal_Difference_Learning_in_Distributional_Reinforcement_Learning|Online Inference for Quantile Temporal Difference Learning in Distributional Reinforcement Learning]]

![[assets/2608.12973_first_page.png|800]]

- **arXiv**: [2608.12973](https://arxiv.org/abs/2608.12973)
- **PDF**: https://arxiv.org/pdf/2608.12973
- **详细分析**: [[20_Research/Papers/强化学习/Online_Inference_for_Quantile_Temporal_Difference_Learning_in_Distributional_Reinforcement_Learning|Online Inference for Quantile Temporal Difference Learning in Distributional Reinforcement Learning]]
- **作者**: Zijie Cheng, Yang Peng, Zhihua Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Online Inference for Quantile Temporal Difference Learning in Distributional Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we study how to perform statistical inference for quantile temporal difference learning (QTD) in distributional reinforcement learning. Assuming access to a generative model, we first establish functional central limit theorems for both synchronous and asynchronous QTD, which show that the averaged iterates of QTD converge weakly to a rescaled Brownian motion. We next provide online inference methods. Based on random scaling, the inference procedure constructs an asymptotically pivotal statistic for inference by using the information along the whole QTD path. Meanwhile, the proposed statistic can be computed online without storing the entire trajectory of QTD iterates. This substantially reduces the memory requirement and enables efficient statistical inference in distributional reinforcement learning.

</details>

---

### [[20_Research/Papers/世界模型/Diagnosing_JEPA_World_Models_with_Action-Conditioned_Predictive_Consistency|Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency]]

![[assets/2608.12939_first_page.png|800]]

- **arXiv**: [2608.12939](https://arxiv.org/abs/2608.12939)
- **PDF**: https://arxiv.org/pdf/2608.12939
- **详细分析**: [[20_Research/Papers/世界模型/Diagnosing_JEPA_World_Models_with_Action-Conditioned_Predictive_Consistency|Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency]]
- **作者**: Guo An, Zijing Wu, Honghua Dong, Yuhao Yan, Zixuan Gui, Haochong Chen, Shanzhao Ruan, Xiang Wang, Yurong Ling, Qi Tian
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: cs.LG

#### 研究背景与动机

《Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CARRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) learn world models that predict in a compact latent space rather than in pixels, reducing the pressure to model nuisance appearance. Yet this provides no guarantee against visual perturbations: they can still alter the encoded representation and affect subsequent action-conditioned predictions. Bisimulation captures this requirement precisely: two observations should be treated as the same state only when their action-conditioned consequences agree. Guided by this criterion, we introduce Action-Conditioned Predictive Consistency (ACPC), a diagnostic that measures how far a clean history and a visually perturbed view of it diverge after being rolled forward under the same action sequence. We prove that this divergence bounds the perturbation-induced change in multi-step prediction error and planner cost. Building on pairwise ACPC, we define two complementary measures: the Invariance Radius (IR) summarizes clean-perturbed rollout spread, while the Separation Rate (SR) checks whether different states remain distinguishable after rollout. Experiments on four visual control tasks show that pairwise ACPC predicts perturbation-induced prediction and cost changes. On LeWM, the IR-SR screen transfers across tasks, and the joint diagnostic remains informative under blur and resize. PLDM exhibits similar diagnostic trends under a different architecture.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Socially_Compliant_Navigation_in_Deep_Reinforcement_Learning_via_Proxemics-Based_Reward_Modeling|Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling]]

![[assets/2608.12917_first_page.png|800]]

- **arXiv**: [2608.12917](https://arxiv.org/abs/2608.12917)
- **PDF**: https://arxiv.org/pdf/2608.12917
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Socially_Compliant_Navigation_in_Deep_Reinforcement_Learning_via_Proxemics-Based_Reward_Modeling|Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling]]
- **作者**: Takieddine Soualhi, Jacques Saraydaryan, Laetitia Matignon
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 3.02（加权：具身智能 0.6，强化学习 1.76，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Towards Socially Compliant Navigation in Deep Reinforcement Learning via Proxemics-Based Reward Modeling》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Developing effective robot navigation methods in crowded environments is essential for real-world applications. Although recent deep reinforcement learning (DRL) methods have improved navigation performance in crowded environments, they often focus primarily on task-centric objectives and underrepresent social compliance objectives. In this paper, we introduce a novel proxemics-based reward formulation for DRL social navigation that provides a dense, interpretable social learning signal while maintaining navigation efficiency. Our approach models each human's personal space as a radial Gaussian-mixture field derived from Hall's proxemics theory and computes a robot-centric local cost over the robot's field of view. We integrate the proposed reward into established DRL navigation methods and evaluate it in simulation across multiple crowd scenarios, reward baselines, and crowd densities using both navigation metrics and social metrics. Results show that the proposed reward consistently improves social metrics in simulation while maintaining competitive navigation performance relative to the compared reward models.

</details>

---

### [[20_Research/Papers/强化学习/Revisiting_Overestimation_Bias_Problem_of_Q-learning_Settling_Large_Discrete_Action_Space_via_Action_Intersection|Revisiting Overestimation Bias Problem of Q-learning: Settling Large Discrete Action Space via Action Intersection]]

![[assets/2608.12912_figure.png|800]]

- **arXiv**: [2608.12912](https://arxiv.org/abs/2608.12912)
- **PDF**: https://arxiv.org/pdf/2608.12912
- **详细分析**: [[20_Research/Papers/强化学习/Revisiting_Overestimation_Bias_Problem_of_Q-learning_Settling_Large_Discrete_Action_Space_via_Action_Intersection|Revisiting Overestimation Bias Problem of Q-learning: Settling Large Discrete Action Space via Action Intersection]]
- **作者**: Pu Li, Tao Tan, Hong Xie, Xiaoyu Shi, Mingsheng Shang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Revisiting Overestimation Bias Problem of Q-learning: Settling Large Discrete Action Space via Action Intersection》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper considers the overestimation bias problem of Q-learning in the setting of a large action space, for the purpose of relieving the bottleneck of existing methods. We find that the large action space increases the randomness in Q-value estimation. The randomness makes two paradigms that drive the major literature on the overestimation problem have their own bottlenecks: the coupling paradigm, i.e., the optimal action and its Q-value are estimated with the same Q-function, always has a positive bias. This is because randomness leads to some actions having abnormally high estimated values than their true values, and the coupling methods prefer these actions. The decoupling paradigm, i.e., the optimal action and its Q-value are estimated with two independent Q-functions, always has a negative bias. This is because randomness increases the estimation gap between the two independent Q-tables for the same action. This paper shows that action intersection can be a simple yet powerful strategy to relieve these bottlenecks. The action intersection strategy enables semi-decoupling via two designs: (1) it allows two Q-functions to share a certain fraction of trajectory data; (2) if a data sample is shared, each Q-function is updated using the coupling paradigm; otherwise, using the decoupling paradigm. Two properties make the action intersection strategy powerful: (1) attaining a large bias range, i.e., varying the data sharing fraction, the estimation bias varies from underestimating to overestimating; (2) fine granularity: the action intersection size can be made arbitrarily finer to enable finer control. We consider two experiment settings, i.e., tabular and deep RL, deep RL experiments show that our method outperforms several SOTA baselines drastically; tabular experiments reveal why our method can achieve superior performance.

</details>

---

### [[20_Research/Papers/强化学习/Decentralized_Multi-Player_Q-Learning_in_Episodic_Markov_Decision_Processes_with_Information_Asymmetry|Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry]]

![[assets/2608.12753_first_page.png|800]]

- **arXiv**: [2608.12753](https://arxiv.org/abs/2608.12753)
- **PDF**: https://arxiv.org/pdf/2608.12753
- **详细分析**: [[20_Research/Papers/强化学习/Decentralized_Multi-Player_Q-Learning_in_Episodic_Markov_Decision_Processes_with_Information_Asymmetry|Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry]]
- **作者**: Larissa Xu, King Bi, William Chang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Decentralized Multi-Player Q-Learning in Episodic Markov Decision Processes with Information Asymmetry》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study decentralized multi-player reinforcement learning in episodic tabular Markov decision processes (MDPs) under three forms of information asymmetry: (A) unobserved actions with common rewards, (B) observed actions with independent rewards, and (C) unobserved actions with independent rewards. Players cannot communicate during learning but may agree on a protocol a priori. For Problems A and B we propose \texttt{mQ-learning} and \texttt{mQ-learning-intervals}, achieving $\tilde{O}(\sqrt{H^4 S A_{\text{joint}}\, T})$ regret, where $H$ is the horizon, $S$ the state count, $T = KH$ the total steps, and $A_{\text{joint}} = \prod_{i=1}^M |\mathcal{A}_i|$ the joint action space across $M$ players. For Problem C we give \texttt{mEXC} and \texttt{mEXC-Bellman}, two-phase explore-then-commit algorithms with regret $\tilde{O}(H (S A_{\text{joint}})^{1/3} T^{2/3})$. Against the centralized joint-action benchmark, decentralized learning under information asymmetry matches the single-agent Q-learning rate of \cite{jin2018q} up to logarithmic factors. Because $A_{\text{joint}}$ grows exponentially in $M$, the bounds are most meaningful for small $M$ or small per-player action sets.

</details>

---

### [[20_Research/Papers/具身智能/Scaling_Automatic_Research_Agents_via_World_Models|Scaling Automatic Research Agents via World Models]]

![[assets/2608.12564_figure.png|800]]

- **arXiv**: [2608.12564](https://arxiv.org/abs/2608.12564)
- **PDF**: https://arxiv.org/pdf/2608.12564
- **详细分析**: [[20_Research/Papers/具身智能/Scaling_Automatic_Research_Agents_via_World_Models|Scaling Automatic Research Agents via World Models]]
- **作者**: Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Chenlei Guo, Jingrui He, Zhenyu Liao
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 大模型, 强化学习
- **相关性评分**: 2.22（加权：具身智能 0.6，大模型 0.5，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Scaling Automatic Research Agents via World Models》归入 世界模型、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSBench, MLE-Bench, MLGym, WMRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment execution) scale in very different manners, since all generation shares compute through batching, while each execution occupies its exclusive sandbox and real machine time. As a result, the environment execution dominates the training cost and becomes the bottleneck as trajectories grow. To resolve this tension, we propose World Model RL (WMRL), which replaces environment execution with a world model to remove this bottleneck. Additionally, the world model can be imperfect, as its rewards are corrupted by bias and noise. Therefore, we further equip WMRL with two mitigations, Online Debiasing and Inverse-Variance Denoising, which offset the bias and suppress the noise respectively. Theoretically, we prove that both mitigations of WMRL strictly improve the convergence guarantee. Empirically, WMRL accelerates training by 3-4x on various tasks at different agent scales, while exceeding the performance of standard RL baselines. Moreover, our post-trained 4B and 9B agents outperform much larger open-weight agents of 48B and 120B on held-out benchmarks. Beyond AutoResearch, WMRL also transfers to post-training embodied VLA policies, which demonstrates the generalizability of our method.

</details>

---

### [[20_Research/Papers/强化学习/Multi-AUV_Ad-hoc_network-based_Target_Tracking_A_Value_Gradient_Guidance_Multi-Agent_Diffusion_Reinforcement_Learning_Approach|Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach]]

![[assets/2608.12436_figure.png|800]]

- **arXiv**: [2608.12436](https://arxiv.org/abs/2608.12436)
- **PDF**: https://arxiv.org/pdf/2608.12436
- **详细分析**: [[20_Research/Papers/强化学习/Multi-AUV_Ad-hoc_network-based_Target_Tracking_A_Value_Gradient_Guidance_Multi-Agent_Diffusion_Reinforcement_Learning_Approach|Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach]]
- **作者**: Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, Zhenyu Wang
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DMADRL, MARL, VGG-MADiffRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized coordination through centralized training, existing methods suffer from high-dimensional joint state-action modeling, noise-sensitive policy generation, leading to unstable training and degraded tracking. To address these issues, we propose VGG-MADiffRL, a value-gradient-guided multi-agent diffusion RL algorithm, and MDCA, a diffusion?based hierarchical control architecture. Leveraging underwater mission characteristics, we model sonar detection mechanisms and ocean current disturbances, formulating cooperative tracking for multi-AUV ad-hoc networks as an MDP. The proposed MDCA constitutes a three-tier closed-loop control framework: a global intelligent control layer, a local online training layer, and a physical action execution layer. This structure enables synergistic optimization across task allocation, local decision processes, and execution feedback. Within MDCA, the local online training layer is the policy learning framework; VGG-MADiffRL builds on diffusion policies and incorporates value gradients to guide action generation in the reverse denoising process, steering the generated actions towards higher expected returns. It employs twin value networks with joint optimization and soft target updates to mitigate overestimation and training oscillations, promoting more stable convergence. Experimental results show that VGG-MADiffRL consistently achieves faster convergence, higher tracking accuracy, and smoother training dynamics in cooperative tracking scenarios, validating its effectiveness and practical engineering value in dynamic underwater settings.

</details>

---

### [[20_Research/Papers/大模型/LoKiFormer_Locality-aware_Attention_with_Decoupled_Knowledge_Memory_for_Efficient_Large_Language_Model_Pretraining|LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining]]

![[assets/2608.12419_figure.png|800]]

- **arXiv**: [2608.12419](https://arxiv.org/abs/2608.12419)
- **PDF**: https://arxiv.org/pdf/2608.12419
- **详细分析**: [[20_Research/Papers/大模型/LoKiFormer_Locality-aware_Attention_with_Decoupled_Knowledge_Memory_for_Efficient_Large_Language_Model_Pretraining|LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining]]
- **作者**: Qiuwu Chen, Zimo Liu, Yuchen Li, Ying Sun, Yifan Zhang, Zhijie Qiu, Zeng You, Ryan Dong, Simeng Ma, Yaofo Chen, Mingkui Tan
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have achieved remarkable breakthroughs across various applications. However, their architectures remain inefficient in pretraining due to two main limitations: (i) self-attention lacks an explicit inductive bias for locality, leading to redundant modeling of sequence-internal local information; (ii) mixture-of-experts (MoE) implicitly couples knowledge storage with computational pathways, hindering flexible access to sequence-external global knowledge. To overcome these limitations, we propose LoKiFormer, a novel LLM architecture that augments the standard decoder with two dedicated modules: 1) Local Fusion Attention (LFA), which incorporates a convolutional fusion to attention, explicitly capturing local patterns and allowing the attention to operate on more informative representations; 2) Knowledge Memory Module (KMM), which introduces a parametric key-value memory that explicitly stores global knowledge in addressable slots, decoupling storage from computation and enabling direct knowledge retrieval. Together, these modules enable LoKiFormer to achieve more efficient and effective integration of information at both levels. Experimental results show that LoKiFormer converges 1.33x faster in pre-training than baseline models, underscoring its superiority over existing LLM architectures.

</details>

---
