# cs.LG | Machine Learning | 2026-06-15

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/A_Statistical_and_Machine_Learning_Framework_for_Operational_Threshold_Detection_and_Deployable_Dispatch_Controller_Development_in_Hydrogen_|A Statistical and Machine Learning Framework for Operational Threshold Detection and Deployable Dispatch Controller Development in Hydrogen Multi-Energy Systems]]

![[assets/2606.14601_figure.png|800]]

- **arXiv**: [2606.14601](https://arxiv.org/abs/2606.14601)
- **PDF**: https://arxiv.org/pdf/2606.14601
- **详细分析**: [[20_Research/Papers/强化学习/A_Statistical_and_Machine_Learning_Framework_for_Operational_Threshold_Detection_and_Deployable_Dispatch_Controller_Development_in_Hydrogen_|A Statistical and Machine Learning Framework for Operational Threshold Detection and Deployable Dispatch Controller Development in Hydrogen Multi-Energy Systems]]
- **作者**: Shadi Heenatigala, Hasanika Samarasinghe
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《A Statistical and Machine Learning Framework for Operational Threshold Detection and Deployable Dispatch Controller Development in Hydrogen Multi-Energy Systems》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study presents a statistical and machine learning framework for characterizing a hydrogen-based multi-energy system (H-MES) using one year of high-resolution operational data. Statistical analysis revealed a binary operation driven by renewable surplus, with solar irradiance explaining 45.7% of rank-based variance in hydrogen production, a large effect by conventional standards. Only high-irradiance periods triggered meaningful electrolyzer engagement, while electricity demand exerted a weaker inverse suppression effect ($ε^2 = 0.126$). Multiple regression confirmed electrolyzer power as the dominant linear predictor, with a synergistic solar-wind interaction. Notably, Random Forest analysis ranked wind output first in predictive importance despite its weak bivariate correlation (r = 0.167), revealing non-linear dynamics invisible to parametric methods. A sequence model exploited strong 24-hour autocorrelation (r = 0.845) for operational forecasting, while a reinforcement learning agent optimized hydrogen revenue dispatch. The core contribution is demonstrating that statistical and machine learning approaches are complementary for H-MES modeling and control.

</details>

---

### [[20_Research/Papers/强化学习/ORCA_A_Platform_for_Open-Source_Dexterity_Research|ORCA: A Platform for Open-Source Dexterity Research]]

![[assets/2606.14561_figure.png|800]]

- **arXiv**: [2606.14561](https://arxiv.org/abs/2606.14561)
- **PDF**: https://arxiv.org/pdf/2606.14561
- **详细分析**: [[20_Research/Papers/强化学习/ORCA_A_Platform_for_Open-Source_Dexterity_Research|ORCA: A Platform for Open-Source Dexterity Research]]
- **作者**: Francesco Capuano, Maximilian Eberlein, Fabrice Bourquin, Clemens Claudio Christoph
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《ORCA: A Platform for Open-Source Dexterity Research》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics manipulation research increasingly focuses on two-finger parallel grippers for their effectiveness, affordability, and ease of teleoperation. Grippers are nonetheless limited by their form factor, often requiring bimanual setups even for simple reorientation tasks. Anthropomorphic hands are a more natural platform for dexterous robot learning -- closer to the human hand, and capable of learning from human video -- yet they remain hard to use in learning research: even where open and accessible hand hardware exists, the software for control, simulation, teleoperation, and retargeting is scattered in one-off code bases, and largely disconnected from the robot-learning ecosystem. In this work, we introduce the \orca~learning stack, an open-source research stack for dexterity as a first-class robot learning domain. Our \orca~stack unifies low-level control, simulation, teleoperation from a range of consumer platforms, and hand retargeting, behind a single interface, and integrates natively with popular robot-learning frameworks such as \lerobot, so dexterous hand researchers can leverage the same data, training, and evaluation pipelines used for non-dexterous robot learning. We demonstrate a complete end-to-end workflow, collecting expert demonstrations of an in-hand reorientation task by teleoperation with a consumer-grade VR headset, training an autonomous policy with \lerobot, and evaluating the learned policy in a fully reproducible and observable setup. We open-source the entire stack as a shared, reproducible foundation for dexterous-manipulation research.

</details>

---

### [[20_Research/Papers/强化学习/Provably_Safe,_Yet_Scalable_Reinforcement_Learning|Provably Safe, Yet Scalable Reinforcement Learning]]

![[assets/2606.14536_figure.png|800]]

- **arXiv**: [2606.14536](https://arxiv.org/abs/2606.14536)
- **PDF**: https://arxiv.org/pdf/2606.14536
- **详细分析**: [[20_Research/Papers/强化学习/Provably_Safe,_Yet_Scalable_Reinforcement_Learning|Provably Safe, Yet Scalable Reinforcement Learning]]
- **作者**: Kai S. Yun, Zeyang Li, Navid Azizan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 1.16，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Provably Safe, Yet Scalable Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CBF-RL, HardNet, PS2-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe reinforcement learning (RL) aims to learn policies that optimize rewards while satisfying constraints. Predominant approaches rely on soft-constrained policy optimization, which has achieved empirical success but does not provide formal safety guarantees for the learned policy. In contrast, methods with strict guarantees typically rely on explicit certificate functions, whose construction requires the direct synthesis and verification of control-invariant sets, a process that scales poorly with state dimension and often yields overly conservative behavior. In this paper, we present the Provably Safe, yet Scalable RL (PS2-RL) framework, a novel two-phase architecture for learning provably safe policies in a scalable manner, designed to overcome the key bottlenecks of prior methods. Rather than explicitly computing invariant sets, PS2-RL leverages a learned backup policy to forward-integrate the system dynamics, generating an implicit control-invariant set online. In the first phase, the backup policy is trained with our proposed safe-arrival value function, which characterizes the optimal backup policy for invariant-set construction. In the second phase, an RL policy is trained end-to-end through a differentiable projection layer that strictly enforces the safety guarantees induced by the learned backup policy. By maximizing the volume of the implicit control-invariant set in the first phase, the resulting PS2 policy from the second phase is performant and scalable, while maintaining provable safety. Crucially, PS2-RL imposes no restrictions on the underlying RL algorithm and can be plugged into any existing training pipeline. We establish theoretical guarantees for the proposed framework and evaluate it on robotic control tasks with state dimensions up to 10, a regime in which prior provably safe RL methods struggle or become impractical.

</details>

---

### [[20_Research/Papers/具身智能/More_with_LESS_--_Local_Scene_Representations_for_Tactile_Imaging|More with LESS -- Local Scene Representations for Tactile Imaging]]

![[assets/2606.14344_figure.png|800]]

- **arXiv**: [2606.14344](https://arxiv.org/abs/2606.14344)
- **PDF**: https://arxiv.org/pdf/2606.14344
- **详细分析**: [[20_Research/Papers/具身智能/More_with_LESS_--_Local_Scene_Representations_for_Tactile_Imaging|More with LESS -- Local Scene Representations for Tactile Imaging]]
- **作者**: Zohar Rimon, Elisei Shafer, Tal Tepper, Daniel Kozin, Alon Malka, Roy Holland, Aviv Tamar
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，机器人 0.4）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《More with LESS -- Local Scene Representations for Tactile Imaging》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile imaging seeks to reconstruct the internal structure of soft objects through touch sensing, with applications in medical diagnosis and robotic manipulation. Recent self-supervised learning approaches have shown promising results, but rely on global, unstructured representations and robot-controlled sensing, limiting generalization and practical use. We propose Local Encoder for Spatial Sensing (LESS), an object-centric tactile representation that exploits the local nature of touch. The tactile scene is modeled as a grid of recurrent encoders with local receptive fields, whose states are fused to reconstruct 2D or 3D images of internal structure. This compositional design enables strong generalization: models trained on single-inclusion phantoms accurately image objects with multiple inclusions and varying sizes. The local structure further supports spatial uncertainty estimation. In addition, we enable hand-held tactile imaging via external pose tracking and human-like palpation data, and extend tactile imaging to full 3D reconstruction.

</details>

---

### [[20_Research/Papers/强化学习/DRIVE_Distributional_and_Retrieval-Augmented_Bidding_with_Value_Evaluation|DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation]]

![[assets/2606.14192_figure.png|800]]

- **arXiv**: [2606.14192](https://arxiv.org/abs/2606.14192)
- **PDF**: https://arxiv.org/pdf/2606.14192
- **详细分析**: [[20_Research/Papers/强化学习/DRIVE_Distributional_and_Retrieval-Augmented_Bidding_with_Value_Evaluation|DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation]]
- **作者**: Miduo Cui, Haochen Wang, Shangqin Mao, Xun Yang, Qianlong Xie, Xingxing Wang, Xuri Ge, Ying Zhou, Zhiwei Xu
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AuctionNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Auto-bidding is a core component of real-time advertising systems, where decisions must optimize long-term performance under budget and cost constraints, while online exploration is prohibitively risky. Offline reinforcement learning and, more recently, Transformer-based sequence modeling have shown promise for learning bidding policies from logged data, but their unimodal and purely parametric formulations often collapse multiple effective bidding strategies into suboptimal averaged actions and perform unreliably under sparse or long-tail traffic. To mitigate these limitations, we propose DRIVE (Distributional and Retrieval-Augmented Bidding with Value Evaluation), a unified Transformer-based framework that decouples candidate action generation from decision making for offline auto-bidding. DRIVE combines distributional action modeling, retrieval-augmented candidate generation from high-quality historical decisions, and value-based evaluation to select the most promising bid at inference time. Extensive experiments on AuctionNet and additional offline reinforcement learning benchmarks demonstrate that DRIVE consistently improves bidding performance and generalizes well across multiple Transformer-based methods.

</details>

---

### [[20_Research/Papers/强化学习/Contract-Based_Compositional_Shielding_for_Safe_Multi-Agent_Reinforcement_Learning|Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning]]

![[assets/2606.14130_first_page.png|800]]

- **arXiv**: [2606.14130](https://arxiv.org/abs/2606.14130)
- **PDF**: https://arxiv.org/pdf/2606.14130
- **详细分析**: [[20_Research/Papers/强化学习/Contract-Based_Compositional_Shielding_for_Safe_Multi-Agent_Reinforcement_Learning|Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning]]
- **作者**: Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe coordination problems surface in multi-agent reinforcement learning when global safety cannot be enforced by any agent unilaterally: the admissibility of one agent's action may depend on the dynamics of other agents. Decentralised shields can enforce safety at runtime, but purely factorised permissions often exclude optimal team behaviour that is safe only through coordination. We study deterministic safety guarantees for agents trained and deployed under decentralised execution, recovering team-optimal safe behaviour without centralised runtime control. Agents have a shared global specification $φ$ in the safety fragment of Linear Temporal Logic ($\mathsf{LTL}_{\mathsf{safe}}$ ), and select among tuples of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations whose conjunction implies the global specification $φ$. Each agent may rely on the other agents' local obligations as assumptions because the whole contract tuple is certified simultaneously and allows projection into local action masks. At learning time, a non-stationary multi-armed bandit chooses among a library of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations to select the tuple that optimises team reward, all without forgoing end-to-end safety. We evaluate the approach across 6 environments and 15 algorithmic variants.

</details>

---

### [[20_Research/Papers/强化学习/Utility-Constrained_Policy_Optimization|Utility-Constrained Policy Optimization]]

![[assets/2606.14029_figure.png|800]]

- **arXiv**: [2606.14029](https://arxiv.org/abs/2606.14029)
- **PDF**: https://arxiv.org/pdf/2606.14029
- **详细分析**: [[20_Research/Papers/强化学习/Utility-Constrained_Policy_Optimization|Utility-Constrained Policy Optimization]]
- **作者**: Mehrdad Moghimi, Bernardo Avila Pires
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Utility-Constrained Policy Optimization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Constrained MDPs (CMDPs) are a widely adopted framework for incorporating safety into RL agents; however, the framework does not support risk-sensitive constraints. This can be problematic: For example, CMDPs allow for optimal solutions that, in order to satisfy the risk-neutral constraints, mix infrequent catastrophic behaviors and frequent, overly conservative ones. Moreover, prior empirical results suggest that enforcing stricter, risk-sensitive constraints can improve performance even under risk-neutral evaluation. The natural framework to incorporate risk-sensitive constraints is utility-constrained MDPs (UCMDPs), but no practical solutions for this problem existed. In this work, we introduce a simple yet powerful methodology for UCMDPs and constrained RL. Besides allowing for risk-sensitive constraints, our framework does not require us to fix constraint limits in advance of training the agent, provided that a sensible range is known. This increases policy flexibility and, in practice, allows for adjustments to these limits at no extra training cost. Besides benefiting from the generality of the framework, our agent shows strong performance in practice, consistently matching or outperforming existing baselines in several Safety Gymnasium benchmark tasks.

</details>

---

### [[20_Research/Papers/具身智能/An_Attention-based_Model_for_Robust_Forecasting_with_Missing_Modality|An Attention-based Model for Robust Forecasting with Missing Modality]]

![[assets/2606.13970_figure.jpg|800]]

- **arXiv**: [2606.13970](https://arxiv.org/abs/2606.13970)
- **PDF**: https://arxiv.org/pdf/2606.13970
- **详细分析**: [[20_Research/Papers/具身智能/An_Attention-based_Model_for_Robust_Forecasting_with_Missing_Modality|An Attention-based Model for Robust Forecasting with Missing Modality]]
- **作者**: Zhitian Zhang, Wenjie Zi, Yunduz Rakhmangulova, Saghar Irandoust, Hossein Hajimirsadeghi, Thibaut Durand
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《An Attention-based Model for Robust Forecasting with Missing Modality》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning with missing modalities is a fundamental challenge in multimodal robot learning, as real-world robotic systems often operate in environments with incomplete sensor data. Attention-based models are appealing for processing multimodal data because they can handle multiple modalities with a single backbone network. However, most multimodal models assume that all modalities are available during both training and inference, limiting their applicability in robotic perception and decision-making. In this paper, we introduce a multimodal model designed to handle missing modalities during both training and inference. The model is formulated as a conditional variational autoencoder (CVAE) and incorporates a transformer-based architecture that leverages attention mechanisms to learn a unified, fixed-dimensional representation, even when some modalities are missing. We show that our proposed model can be trained with missing modalities while approximating a robust representation of all modalities. We evaluate our approach on five multimodal datasets across two robot learning tasks: human trajectory prediction and robot manipulation forecasting. Experimental results demonstrate that our model effectively learns from incomplete data and is superior to prior multimodal fusion approaches.

</details>

---

### [[20_Research/Papers/强化学习/Temporally_Consistent_Graph_Q-Networks_for_Intelligent_Network_Control|Temporally Consistent Graph Q-Networks for Intelligent Network Control]]

![[assets/2606.13848_figure.png|800]]

- **arXiv**: [2606.13848](https://arxiv.org/abs/2606.13848)
- **PDF**: https://arxiv.org/pdf/2606.13848
- **详细分析**: [[20_Research/Papers/强化学习/Temporally_Consistent_Graph_Q-Networks_for_Intelligent_Network_Control|Temporally Consistent Graph Q-Networks for Intelligent Network Control]]
- **作者**: Zacharias Veiksaar, Maxime Bouton
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Temporally Consistent Graph Q-Networks for Intelligent Network Control》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile networks continue to grow in complexity and next generation networks are expected to support both increasing traffic loads and more diverse services. As network complexity rises, optimizing antenna parameters under dynamic or changing objectives becomes increasingly challenging. We propose a novel multi-agent reinforcement learning (MARL) algorithm for high-level control and orchestration of mobile networks. The Temporally Consistent Graph Q-Network (TC-GQN) algorithm learns a self-predicting representation of the whole network that is task-independent and aggregates information from all base-stations. A graph neural network is trained using a global reward function to assign coordinated local actions based on the learned encoding of the global network state. We evaluate the algorithm in a simulated environment to orchestrate an energy-saving feature across multiple sectors and multiple carriers under different quality of service (QoS) constraints. The proposed algorithm outperforms state-of-the-art graph-based baselines and a competitive rule-based controller by improving hardware sleep time while maintaining QoS. Moreover, the learned representation enables rapid adaptation to changing intents.

</details>

---

### [[20_Research/Papers/世界模型/FlowMo-WM_A_World_Model_with_Object_Momentum_and_Hidden_Ambient_Drift|FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift]]

![[assets/2606.13817_figure.png|800]]

- **arXiv**: [2606.13817](https://arxiv.org/abs/2606.13817)
- **PDF**: https://arxiv.org/pdf/2606.13817
- **详细分析**: [[20_Research/Papers/世界模型/FlowMo-WM_A_World_Model_with_Object_Momentum_and_Hidden_Ambient_Drift|FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift]]
- **作者**: Yitao Jiang, Luyang Zhao, Muhao Chen, Devin Balkcom
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.1，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《FlowMo-WM: A World Model with Object Momentum and Hidden Ambient Drift》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Meta-RL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models in robot learning predict future states from visual observations and actions, enabling agents to reason about the consequences of their controls. However, many action-conditioned models are evaluated in settings where motion is dominated by immediate control, whereas aquatic surface vehicles and other real-world objects continue moving under inertia and are displaced by hidden ambient drift, such as water currents or wind. We propose FlowMo-WM, an end-to-end trainable visual world model that infers object-centric motion state and a predictive long-history context associated with hidden drift from image-action histories without direct supervision of flow fields. FlowMo-WM factorizes image-action history into a short-history latent state, trained to summarize object-centric motion, and a longer-history context, trained to summarize slowly varying exogenous influences. A zero-context residual transition separates action-conditioned base dynamics from context-dependent drift effects during latent rollout. In simulated aquatic surface-vehicle environments with diverse hidden flows, disturbances, and randomized vehicle dynamics, FlowMo-WM improves long-horizon rollout accuracy over representative action-conditioned latent world models. Prediction-time context ablations, in which the inferred context is zeroed or shuffled during rollout, show that the ambient context is important for stable prediction under hidden drift, while frozen linear probes characterize information encoded in the learned factors.

</details>

---

### [[20_Research/Papers/大模型/Diffusion_Policy_Optimization_without_Drifting_Apart|Diffusion Policy Optimization without Drifting Apart]]

![[assets/2606.13795_figure.png|800]]

- **arXiv**: [2606.13795](https://arxiv.org/abs/2606.13795)
- **PDF**: https://arxiv.org/pdf/2606.13795
- **详细分析**: [[20_Research/Papers/大模型/Diffusion_Policy_Optimization_without_Drifting_Apart|Diffusion Policy Optimization without Drifting Apart]]
- **作者**: Haozhe Jiang, Haiwen Feng, Pieter Abbeel, Jiantao Jiao, Angjoo Kanazawa, Nika Haghtalab
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Diffusion Policy Optimization without Drifting Apart》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

RL post-training has become increasingly pivotal for improving diffusion policies, but existing diffusion policy-gradient methods are often unstable and cannot achieve reliable policy improvement. We identify the cause as the double-drift phenomenon: optimizing a variational surrogate can let the ELBO separate from the true log-likelihood, which then makes the resulting proxy policy gradient misaligned with the true policy gradient of expected return. We propose \textbf{DiPOD}, a diffusion policy optimization framework that maintains tight-bound behavior throughout training by interleaving self-distillation with policy-improving gradient updates. This leads to a simple and practical algorithm: augmenting each diffusion policy-gradient update with an on-policy ELBO regularizer. Across diffusion language model post-training and continuous-control diffusion policies, DiPOD substantially stabilizes training and reaches higher rewards than previous methods.

</details>

---
