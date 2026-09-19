# cs.LG | Machine Learning | 2026-09-18

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/Agile-WAM_An_Agile_Tactile_World_Action_Model_for_Contact-Rich_Robot_Control|Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control]]

![[assets/2609.20761_figure.png|800]]

- **arXiv**: [2609.20761](https://arxiv.org/abs/2609.20761)
- **PDF**: https://arxiv.org/pdf/2609.20761
- **详细分析**: [[20_Research/Papers/大模型/Agile-WAM_An_Agile_Tactile_World_Action_Model_for_Contact-Rich_Robot_Control|Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control]]
- **作者**: Hanchu Zhou, Brendan Lynch, Raman Goyal, Dechen Gao, Begum Kasap, Boqi Zhao, Junshan Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) advance beyond conventional visuomotor policies by jointly predicting future world states and robot actions, enabling the policy to learn physical dynamics that support effective control. However, recent tactile WAMs often rely on large-scale pretrained generative backbones to capture contact-rich physical dynamics, which limit their inference efficiency and flexible deployment. In this paper, we present \ABBR{}, an agile tactile World Action Model for contact-rich robot control. \ABBR{} encodes visual and tactile observations into a shared latent that serves as the source of a direct vision-tactile-to-action flow-matching process, which can jointly generate latent representations of action chunks and future visual/tactile latents. A key observation is that vision and tactile signals evolve at inherently different timescales: adjacent visual frames are often highly similar, whereas tactile signals can change abruptly upon contact. We therefore introduce multi-horizon multimodal prediction in \ABBR{}, which provides supervision for visual latent at a larger temporal offset while predicting the tactile latent in the next frame to capture fine-grained contact dynamics. Across nine simulated and five real-world contact-rich manipulation tasks, \ABBR{} demonstrates strong and robust performance, outperforming the strongest baseline in success rate while maintaining low inference latency. In particular, in five real-world experiments, \ABBR{} yields a relative gain of $\textbf{29.4\%}$ in overall success rates while achieving inference latency of $\textbf{11.9 ms}$. These results demonstrate that multimodal WAM can be achieved with an agile architecture suitable for precise and high-frequency robot control. More details are available on our project page: this https URL .

</details>

---

### [[20_Research/Papers/强化学习/MILER_Semantic_Mid-Level_Representation_for_Sim-to-Real_Reinforcement_Learning_in_Unstructured_Autonomous_Driving|MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving]]

![[assets/2609.20747_figure.png|800]]

- **arXiv**: [2609.20747](https://arxiv.org/abs/2609.20747)
- **PDF**: https://arxiv.org/pdf/2609.20747
- **详细分析**: [[20_Research/Papers/强化学习/MILER_Semantic_Mid-Level_Representation_for_Sim-to-Real_Reinforcement_Learning_in_Unstructured_Autonomous_Driving|MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving]]
- **作者**: Thomas Steinecker, Denis Trescher, Alexander Bienemann, Thorsten Luettel, Mirko Maehlisch
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.92（加权：具身智能 1.5，强化学习 0.96，世界模型 0.16，机器人 0.3）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning in Unstructured Autonomous Driving》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CaRL, DriverGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning constitutes a promising approach owing to its potential for superhuman performance and self-learned policies. However, its application to real-world autonomous driving remains scarce, particularly in unstructured environments, because of the challenges associated with sim-to-real transfer for unstructured environments. In this work, we present MILER, an end-to-end policy framework with zero-shot sim-to-real transfer. During offline training, we employ a custom semantic mid-level representation (MLR) simulator and train the policy network using reinforcement learning, with its control outputs applied directly to a bicycle model. During deployment on the real vehicle, camera and LiDAR data are processed by BEVFusion to generate a semantic bird's-eye-view representation consistent with that of the MLR simulator. The actions generated by the policy network are not applied directly to the real vehicle. Instead, we employ a trajectory-alignment strategy that enables zero-shot sim-to-real transfer of both perception and control. We extensively evaluate the proposed framework on a diverse test track comprising numerous challenges, including various obstacles, hairpin curves, velocities of up to 33.6 km/h, and off-road sections. In total, we drove 17.3 km with two different vehicles on a 3.0 km test track without human intervention, thereby demonstrating the effectiveness of our approach. Furthermore, the entire software stack runs on a Jetson AGX Orin.

</details>

---

### [[20_Research/Papers/强化学习/Model-based_Bootstrap_for_Offline_Policy_Evaluation_in_Tabular_Reinforcement_Learning|Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning]]

![[assets/2609.20389_first_page.png|800]]

- **arXiv**: [2609.20389](https://arxiv.org/abs/2609.20389)
- **PDF**: https://arxiv.org/pdf/2609.20389
- **详细分析**: [[20_Research/Papers/强化学习/Model-based_Bootstrap_for_Offline_Policy_Evaluation_in_Tabular_Reinforcement_Learning|Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning]]
- **作者**: Weiwei Wang, Yuqiang Li, Xianyi Wu, Bingyi Jing
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Model-based Bootstrap for Offline Policy Evaluation in Tabular Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline policy evaluation (OPE) is crucial in high-stakes reinforcement learning applications, where new policies must be assessed reliably before deployment. In such settings, point estimates alone are insufficient; principled uncertainty quantification, such as confidence intervals and variance estimates, is essential for safe and risk-aware decision-making. A comprehensive way to unify these tasks is to estimate the sampling distribution of the evaluation error. Existing approaches, however, often suffer from limited robustness, scalability, or finite-sample validity. In this paper, we propose a model-based bootstrap framework for uncertainty quantification of OPE in finite-horizon, time-inhomogeneous Markov decision processes (MDPs). Unlike classical bootstrap methods that rely on resampling complete episodes, the proposed method regenerates trajectories from an estimated MDP and can therefore accommodate a much broader range of offline data formats, including complete trajectories, transition-level observations, and trajectory fragments. This flexibility further improves finite-sample statistical efficiency. We establish bootstrap distributional consistency, asymptotically valid confidence intervals, and consistent variance estimation for the target policy value. Extensive simulations show that the proposed method accurately captures the sampling distribution of the OPE estimator, yielding tighter confidence intervals and more accurate variance estimates in most settings.

</details>

---

### [[20_Research/Papers/大模型/Improving_Generalization_and_Robustness_in_Offline_Reinforcement_Learning_via_Boundary-Aware_Data_Augmentation|Improving Generalization and Robustness in Offline Reinforcement Learning via Boundary-Aware Data Augmentation]]

![[assets/2609.20300_figure.png|800]]

- **arXiv**: [2609.20300](https://arxiv.org/abs/2609.20300)
- **PDF**: https://arxiv.org/pdf/2609.20300
- **详细分析**: [[20_Research/Papers/大模型/Improving_Generalization_and_Robustness_in_Offline_Reinforcement_Learning_via_Boundary-Aware_Data_Augmentation|Improving Generalization and Robustness in Offline Reinforcement Learning via Boundary-Aware Data Augmentation]]
- **作者**: Gong Gao, Weidong Zhao, Xianhui Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Improving Generalization and Robustness in Offline Reinforcement Learning via Boundary-Aware Data Augmentation》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, ORL, S4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current offline reinforcement learning (ORL) algorithms tend to overfit the training dataset and exhibit poor in-distribution generalization and robustness performance when deployed to real environments, thus compromising their effectiveness. Existing methods typically enhance in-distribution generalization and robustness by leveraging regularization techniques widely used in computer vision. However, due to the high sensitivity of low-level physical signals to distributional shifts, these methods still suffer from notable limitations in in-distribution generalization and robustness, making it difficult to achieve stable performance in complex environments. To address this issue, we theoretically analyze the error bounds of the behavior policy and action-value function trained with random episode interpolation, revealing that the error scales positively correlated with the distance between states. Based on this insight, we propose a method called $\bf{B}$oundary-$\bf{A}$ware $\bf{D}$ata $\bf{A}$ugmentation (BADA), which leverages neighboring states to construct interpolation boundaries, enabling the generation of synthetic data that more faithfully preserves the original data distribution. We first conduct qualitative studies in a toy environment, showing that BADA generates mixed samples that preserve desirable policy smoothness while accurately reconstructing multimodal value distributions. Extensive experiments on limited offline datasets further demonstrate that BADA attains state-of-the-art performance across diverse benchmarks.

</details>

---

### [[20_Research/Papers/强化学习/Improving_Online_Reinforcement_Learning_via_Bidirectional_Behavior_Prior_Distillation|Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation]]

![[assets/2609.20268_figure.png|800]]

- **arXiv**: [2609.20268](https://arxiv.org/abs/2609.20268)
- **PDF**: https://arxiv.org/pdf/2609.20268
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Online_Reinforcement_Learning_via_Bidirectional_Behavior_Prior_Distillation|Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation]]
- **作者**: Gong Gao, Xiao Lai, Jiaji Shen, Ning Jia, Xianhui Liu, Weidong Zhao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BPRL, DICE-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online reinforcement learning (RL) algorithms frequently exhibit poor sample efficiency and unstable learning dynamics, stemming from systematic critic estimation errors that are exacerbated by greedy policy updates. Existing behavior-prior reinforcement learning methods attempt to alleviate this issue by relying on offline pre-training to learn behavior models from fixed datasets and using policy priors to constrain online policy updates. However, the limited quality of offline datasets often hinders the ability to provide high-value policies that can effectively guide policy updates. The absence of expert trajectories significantly impairs online policy learning, leading to low sample efficiency and suboptimal performance. To address these challenges, we depart from conventional behavior prior approaches and propose a Bidirectional Behavior Prior Distillation (B2PD) algorithm. B2PD leverages action-value priors to guide a conditional variational autoencoder (CVAE) in generating a high-value behavior support set. The resulting expert behavior priors are further distilled into the agent, effectively reducing inefficient exploration and enabling stable policy optimization, while establishing a bidirectional knowledge flow mechanism. Empirical evaluations on both state- and pixel-based tasks verify that B2PD substantially improves sample efficiency while maintaining stable policy optimization. More broadly, this work shows that enforcing high-quality behavioral support during online learning effectively mitigates critic-induced error amplification, enabling structured behavior priors to guide policy updates in a principled and sample-efficient manner.

</details>

---

### [[20_Research/Papers/强化学习/Robust_Federated_Q-Learning_with_Almost_No_Communication|Robust Federated Q-Learning with Almost No Communication]]

![[assets/2609.20174_figure.png|800]]

- **arXiv**: [2609.20174](https://arxiv.org/abs/2609.20174)
- **PDF**: https://arxiv.org/pdf/2609.20174
- **详细分析**: [[20_Research/Papers/强化学习/Robust_Federated_Q-Learning_with_Almost_No_Communication|Robust Federated Q-Learning with Almost No Communication]]
- **作者**: Sreejeet Maity, Aritra Mitra
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Robust Federated Q-Learning with Almost No Communication》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider a federated reinforcement learning setting involving $M$ agents, all of whom interact with a common Markov Decision Process (MDP). The agents exchange information via a central server to learn the optimal value function. Our goal is to understand to what extent one can hope for collaborative sample-complexity speedups in such a setting, when a small fraction of the agents are adversarial and can act arbitrarily. To that end, we propose Robust Fed-Q}, a federated Q-learning algorithm that blends ideas from both model-based and model-free RL, along with the median-of-means device from robust statistics. We prove that despite corruption, with high-probability, Robust Fed-Q (i) guarantees exact convergence to the optimal value function in the limit of infinite samples, and (ii) enjoys near-optimal finite-time rates that benefit from collaboration. In addition, our approach requires just $\tilde{O}(1)$ rounds of communication to achieve each of the above guarantees, a feature of independent interest in FL where communication is the major bottleneck.

</details>

---

### [[20_Research/Papers/具身智能/DeliveryGym_An_RL_Environment_for_Long-Horizon_Embodied_Agent_Planning_with_Adaptive_Curriculum|DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum]]

![[assets/2609.19801_figure.png|800]]

- **arXiv**: [2609.19801](https://arxiv.org/abs/2609.19801)
- **PDF**: https://arxiv.org/pdf/2609.19801
- **详细分析**: [[20_Research/Papers/具身智能/DeliveryGym_An_RL_Environment_for_Long-Horizon_Embodied_Agent_Planning_with_Adaptive_Curriculum|DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum]]
- **作者**: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 世界模型
- **相关性评分**: 2.42（加权：具身智能 1.2，大模型 0.7，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum》归入 具身智能、大模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DeliveryBench, DeliveryGym, SimWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Executable environments enable LLM agents to learn from the consequences of their actions. For embodied agents, those consequences extend beyond whether the current task succeeds: completing a delivery can consume the time, energy, or money needed for later work. Learning to plan therefore requires environments that preserve these dependencies and turn them into feedback across a complete trajectory. We introduce DeliveryGym, a 3D environment for evaluating and training agents on continuous courier shifts. It couples multimodal tool interaction with persistent world dynamics and computes trajectory rewards from simulator events, making the costs of an agent's decisions available for reinforcement learning (RL). The environment also adapts future training shifts to the policy's observed weaknesses while keeping evaluation fixed. Across six models and 13 city maps, evaluation exposes a gap between reliably executing assigned deliveries and choosing and sequencing work over a shift. On the fixed test suite, RL improves Qwen3-VL-4B's net income by 54.3%, showing that learning from complete shifts improves performance under these coupled constraints. Adapting the training environment improves test income by 16.5% over uniform sampling at the same rollout budget, indicating that which situations an agent practices also matters. DeliveryGym provides an executable setting for studying how agents learn to coordinate deliveries and preserve resources for later orders within an episode.

</details>

---

### [[20_Research/Papers/具身智能/UniExo_Unified_Multi-Skill_Policies_for_Musculoskeletal_Locomotion_and_Co-Adaptive_Exoskeleton_Control|UniExo: Unified Multi-Skill Policies for Musculoskeletal Locomotion and Co-Adaptive Exoskeleton Control]]

![[assets/2609.19690_figure.png|800]]

- **arXiv**: [2609.19690](https://arxiv.org/abs/2609.19690)
- **PDF**: https://arxiv.org/pdf/2609.19690
- **详细分析**: [[20_Research/Papers/具身智能/UniExo_Unified_Multi-Skill_Policies_for_Musculoskeletal_Locomotion_and_Co-Adaptive_Exoskeleton_Control|UniExo: Unified Multi-Skill Policies for Musculoskeletal Locomotion and Co-Adaptive Exoskeleton Control]]
- **作者**: Yifei Yuan, Jakob Wolf, Ghaith Androwis, Xianlian Zhou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.42（加权：具身智能 1.5，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《UniExo: Unified Multi-Skill Policies for Musculoskeletal Locomotion and Co-Adaptive Exoskeleton Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Daily locomotion encompasses diverse activities and frequent transitions between them, yet most exoskeleton controllers are designed for a single activity or a narrow set of related movements. Changes in activity therefore typically require explicit mode switching and separately tuned or retrained controllers. Simulation-based learning reduces the need for hardware-based tuning but generally retains this limitation. Here we present UniExo, a framework that first constructs a multi-skill musculoskeletal human policy and then jointly trains an exoskeleton control policy with it. Four single-skill imitation experts for walking, turning, running and backward walking are distilled into a single network structured by a skill latent and subsequently fine-tuned through reinforcement learning on transition sequences. The resultant unified human policy achieves a mean tracking success rate of 94.7% on unseen clips of the four skills and exhibits greater robustness to perturbations than its constituent experts. A single hip exoskeleton controller (UniExo) is initialized from hip moment prediction of the human policy and co-adapted with it through multi-agent reinforcement learning across the four skills. This co-adaptation shifts the timing of the assistance torque and raises the fraction of positive work delivered to the hip. When deployed on a custom hip exoskeleton, the controller generalizes across four treadmill speeds in six participants and assists one participant through a continuous route of all four skills and their transitions, without skill labels or explicit mode switching. UniExo thus provides a step towards replacing activity-specific controllers with unified, user-specific controllers that support diverse locomotor activities and the transitions between them.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedMind_Adaptive_Data_Curation_and_Prefix-Tree_Reinforcement_Learning_for_Efficient_Embodied_Intelligence|EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence]]

![[assets/2609.19659_figure.png|800]]

- **arXiv**: [2609.19659](https://arxiv.org/abs/2609.19659)
- **PDF**: https://arxiv.org/pdf/2609.19659
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedMind_Adaptive_Data_Curation_and_Prefix-Tree_Reinforcement_Learning_for_Efficient_Embodied_Intelligence|EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence]]
- **作者**: Feifan Wang, Zongbing Zhang, Yu Zhang, Lingfeng Wang, Yurui Zhu, Jin Deng, Mingliang Zhang, Zhengguang Gao, Yongcheng Wang, Jin Xu, Ri Yang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.12（加权：具身智能 1.5，强化学习 1.16，世界模型 0.16，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《EmbodiedMind: Adaptive Data Curation and Prefix-Tree Reinforcement Learning for Efficient Embodied Intelligence》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training embodied foundation models typically requires massive-scale datasets and extensive computational resources, yet often suffers from three critical limitations: (1) inefficient sample utilization due to low-informative samples; (2) imbalanced gradient contributions across heterogeneous tasks; and (3) severe credit assignment problem in long-horizon planning, where trajectory-level rewards indiscriminately penalize all tokens. To address these issues, we propose an efficient training paradigm that achieves state-of-the-art average performance through strategic data selection and hierarchical policy optimization. Our approach consists of three synergistic stages. First, Rejection Sampling-based Fine-Tuning (RSFT) filters out low-informative samples to establish robust behavioral priors while preventing distributional collapse. Second, Iterative Rejection GRPO (IR-GRPO) employs task-specific queues stratified by difficulty to keep datasets balanced across reinforcement learning iterations, coupled with a hybrid reward mechanism for precise cross-task feedback. Third, to enhance long-horizon task planning, we introduce Trie-GRPO, a novel reinforcement learning algorithm based on action prefix trees, which enables step-level advantage estimation. This resolves the credit assignment problem by isolating intermediate correct decisions from downstream errors, while effectively balancing exploration efficiency and depth compared to conventional search trees. As a result, EmbodiedMind achieves a state-of-the-art average performance of 70.02% across 18 benchmarks, and significantly outperforms other embodied foundation models in long-horizon task planning accuracy. Our project will be released for reproducibility.

</details>

---

### [[20_Research/Papers/具身智能/GLAMDRING_Gait_Learning_And_Morphology_co-Design_via_Reinforcement_LearnING_of_CPGs|GLAMDRING: Gait Learning And Morphology co-Design via Reinforcement LearnING of CPGs]]

![[assets/2609.19452_figure.png|800]]

- **arXiv**: [2609.19452](https://arxiv.org/abs/2609.19452)
- **PDF**: https://arxiv.org/pdf/2609.19452
- **详细分析**: [[20_Research/Papers/具身智能/GLAMDRING_Gait_Learning_And_Morphology_co-Design_via_Reinforcement_LearnING_of_CPGs|GLAMDRING: Gait Learning And Morphology co-Design via Reinforcement LearnING of CPGs]]
- **作者**: Amogh Joshi, Kaushik Roy
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.72（加权：具身智能 0.9，强化学习 0.96，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《GLAMDRING: Gait Learning And Morphology co-Design via Reinforcement LearnING of CPGs》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CPG-RL, HopfNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots are moving out of the structured factory floor and into unstructured environments such as disaster sites, planetary surfaces, and agricultural fields, for which the right robot often does not yet exist. We present GLAMDRING, a framework that synthesizes the optimal robot for a locomotion task and, jointly, learns the controller that drives it. For the given specifications of forward-velocity bounds, a per-actuator power budget, an actuator library, and a payload requirement, GLAMDRING returns a matched quadruped morphology (link geometry and per-joint actuators) and a Hopf-oscillator Central Pattern Generator (CPG) gait policy. We rank feasible designs against a target design objective, viz., maximum speed, minimum Cost of Transport (CoT), or max Payload Margin. Because body and locomotion are coupled, the optimal morphology dictates how a robot is driven, while optimal gait depends on the physical body. We train a small number of CPG policies by reinforcement learning across the space of candidate morphologies, co-learning the gait with the underlying robot hardware. Link lengths and actuators are then resolved post-hoc from the policy's logged operating envelope, reducing synthesis cost to a small, fixed number of reinforcement-learning runs instead of one per candidate. Our experiments show three key findings: co-designing body and gait is necessary to satisfy locomotion constraints; actuator-envelope feasibility, rather than locomotion success alone, determines realizable payload capacity; and canonical animal gaits emerge naturally in most designs from morphology and constraints alone. A real-world demonstration further highlights the efficacy of our work.

</details>

---

### [[20_Research/Papers/强化学习/Improving_Offline_Goal-Conditioned_Reinforcement_Learning_via_Selective_Reward_Stimulation|Improving Offline Goal-Conditioned Reinforcement Learning via Selective Reward Stimulation]]

![[assets/2609.19414_figure.png|800]]

- **arXiv**: [2609.19414](https://arxiv.org/abs/2609.19414)
- **PDF**: https://arxiv.org/pdf/2609.19414
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Offline_Goal-Conditioned_Reinforcement_Learning_via_Selective_Reward_Stimulation|Improving Offline Goal-Conditioned Reinforcement Learning via Selective Reward Stimulation]]
- **作者**: Jing Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Improving Offline Goal-Conditioned Reinforcement Learning via Selective Reward Stimulation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Goal-conditioned reinforcement learning aims to learn policies that reach specified goals, but remains challenging in offline settings with sparse rewards and long-horizon dependencies. In such settings, goal-completion information can be temporally distant from the early decisions that enable success, while offline value estimation introduces additional error. We study this issue from a reward-propagation perspective and show, in a stylized delayed-goal setting, how goal-directed value separation can become small relative to local estimation error. Motivated by this analysis, we propose Reward Stimulation Implicit Q-Learning (RSIQL), a simple non-hierarchical method that introduces additional reward signals at progress-making intermediate states in offline trajectories. RSIQL uses an auxiliary goal-conditioned value function to identify intermediate states estimated to make progress toward the goal and applies reward stimulation to provide less-delayed training supervision. Unlike hierarchical methods, RSIQL does not learn a separate high-level subgoal policy. Experiments on D4RL goal-reaching benchmarks and OGBench show that RSIQL improves over goal-conditioned IQL on average and achieves performance competitive with hierarchical offline goal-conditioned methods, while retaining a simple flat policy structure.

</details>

---
