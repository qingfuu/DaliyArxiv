# cs.LG | Machine Learning | 2026-11-09

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/具身智能/Computer-Use_Agents_Are_Embodied_Generalists|Computer-Use Agents Are Embodied Generalists]]

![[assets/2611.09847_figure.png|800]]

- **arXiv**: [2611.09847](https://arxiv.org/abs/2611.09847)
- **PDF**: https://arxiv.org/pdf/2611.09847
- **详细分析**: [[20_Research/Papers/具身智能/Computer-Use_Agents_Are_Embodied_Generalists|Computer-Use Agents Are Embodied Generalists]]
- **作者**: Pranjal Aggarwal, Sean Welleck
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.5，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Computer-Use Agents Are Embodied Generalists》归入 具身智能、大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In many areas of AI, general-purpose models have increasingly replaced handcrafted methods and specialized architectures. We argue that embodied AI is poised for a similar shift. Our key claim is that embodied tasks can be formulated as interaction with digital software. Specifically, we build software that renders an agent's view of a physical environment on a screen and provides controls for acting in it. A computer-use agent (CUA) can then perform embodied tasks through the same screenshots and keyboard and mouse actions that it uses to operate ordinary software. Using a single CUA design and changing only the software, our entries win first-, second-, third-, and sixth-place prizes across four ECCV workshop competitions, without any competition-specific agent tuning. These results suggest that the skills CUAs learn on software, such as visual grounding, precise clicking, and exploration, already carry over to embodied tasks, giving CUAs a far broader scope in embodied AI than previously realized. We therefore advocate that computer-use agents can be embodied generalists. Further, we advocate that, by following the training strategy that made computer-use agents general, embodied AI can converge on a single general model as well, ushering in a new era of general embodied AI. Website: https://pranjal2041.github.io/cua-embodied

</details>

---

### [[20_Research/Papers/大模型/Designing_Effective_Monitor-Based_Interventions_for_Mitigating_Reward_Hacking_During_RL|Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL]]

![[assets/2611.09828_figure.png|800]]

- **arXiv**: [2611.09828](https://arxiv.org/abs/2611.09828)
- **PDF**: https://arxiv.org/pdf/2611.09828
- **详细分析**: [[20_Research/Papers/大模型/Designing_Effective_Monitor-Based_Interventions_for_Mitigating_Reward_Hacking_During_RL|Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL]]
- **作者**: Aria Wong, Joshua Engels, Neel Nanda
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as reward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open source three realistic environments where Qwen3-4B reward hacks: a coding environment hackable via test overwriting, a medical chat environment hackable via sycophancy, and a biography generation environment hackable via hallucination. We first focus on the coding environment, where we find that: (1) models can learn to evade highly accurate monitors by exploiting systemic flaws in probes and LLM judges; (2) monitors that leak more learning signal during RL suppress reward hacking but are more often evaded; and (3) including easier problems in training can decrease reward hacking. We apply our findings to build better reward hacking monitors for the medical chat and biography generation environments that improve upon naive baselines to reduce reward hacking rates across seeds to before-training levels in some interventions. Our results demonstrate that our takeaways translate to new settings and that better monitor intervention designs are possible.

</details>

---

### [[20_Research/Papers/强化学习/Autonomous_Particle_Image_Velocimetry_Using_Zero-Shot_Sim-to-Real_Reinforcement_Learning|Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning]]

![[assets/2611.09679_figure.png|800]]

- **arXiv**: [2611.09679](https://arxiv.org/abs/2611.09679)
- **PDF**: https://arxiv.org/pdf/2611.09679
- **详细分析**: [[20_Research/Papers/强化学习/Autonomous_Particle_Image_Velocimetry_Using_Zero-Shot_Sim-to-Real_Reinforcement_Learning|Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning]]
- **作者**: Chang Rajani, Luke Sebastien Marsden, Stephan Kunz, Claudio Mucignat, Ivan Lunati
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.72（加权：具身智能 1.2，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.3）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Particle image velocimetry (PIV) reconstructs a flow field from the motion of tracer particles but the reconstruction quality is bounded by how well the flow structure of interest is resolved in the images. The acquisition position is typically fixed by the operator before the measurement. We cast camera placement as a sequential decision-making problem and train a reinforcement learning agent to control a 6-DoF manipulator equipped with a camera, enabling it to locate, frame and resolve a hydrofoil wake in a water tunnel. The agent commands the camera pose and observes the scene only through the velocity field and uncertainty estimated from time-separated image pairs. It is trained entirely in a photorealistic simulation of our water tunnel, with wakes generated by Computational Fluid Dynamics (CFD) simulations of hydrofoils with varying profiles, positions and angles of attack. After zero-shot transfer to the real water tunnel, the policy reliably locates and frames the wakes of randomly placed hydrofoils. It resolves the wake at a higher resolution than a fixed camera view and with lower error in the measured flow statistics, in roughly half the time of a full scan and with far fewer image pairs.

</details>

---

### [[20_Research/Papers/强化学习/Future-Informed_Actor-Critic|Future-Informed Actor-Critic]]

![[assets/2611.09417_first_page.png|800]]

- **arXiv**: [2611.09417](https://arxiv.org/abs/2611.09417)
- **PDF**: https://arxiv.org/pdf/2611.09417
- **详细分析**: [[20_Research/Papers/强化学习/Future-Informed_Actor-Critic|Future-Informed Actor-Critic]]
- **作者**: Samy Mokeddem, Gaspard Lambrechts, Adrien Bolland, Damien Ernst
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Future-Informed Actor-Critic》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actor-critic methods optimize a parametrized policy using a critic to estimate their policy gradient. Recent work has shown that conditioning the critic on features of future states, actions, or rewards can improve sample efficiency and even final return. However, existing methods are restricted to exogenous features (independent of actions), overlooking endogenous features (dependent on actions) that may be crucial for credit assignment. We introduce the future-informed value function, which can be conditioned on both exogenous and endogenous features of future states, actions, and rewards. Then, we express the policy gradient using this value function, yielding the future-informed policy gradient. Building on that, we propose the future-informed actor-critic algorithm. Empirical results show that this algorithm leveraging endogenous features of the future outperforms standard actor-critic algorithms in environments with noisy and sparse rewards.

</details>

---

### [[20_Research/Papers/强化学习/Probably_Safe_Sim-to-Real_Transfer_with_Lifetime_Validity|Probably Safe Sim-to-Real Transfer with Lifetime Validity]]

![[assets/2611.09344_first_page.png|800]]

- **arXiv**: [2611.09344](https://arxiv.org/abs/2611.09344)
- **PDF**: https://arxiv.org/pdf/2611.09344
- **详细分析**: [[20_Research/Papers/强化学习/Probably_Safe_Sim-to-Real_Transfer_with_Lifetime_Validity|Probably Safe Sim-to-Real Transfer with Lifetime Validity]]
- **作者**: Rohan Tangri, Jan-Peter Calliess
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型
- **相关性评分**: 1.72（加权：具身智能 1.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Probably Safe Sim-to-Real Transfer with Lifetime Validity》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Dejavu, a method that makes sim-to-real transfer of reinforcement learning policies in constrained Markov decision processes probably safe over an unbounded sequence of policy updates. An anytime valid test using per-decision importance sampling and a betting confidence sequence certifies each candidate trained in simulation before deployment using only trajectories collected by a safe baseline policy operating in production. Simulation quality does not affect the safety guarantee, only the production sample efficiency of the method. Finally, a summable per-test failure probability yields the lifetime valid property. Empirical results across three sim-to-real benchmarks support the theoretical work.

</details>

---

### [[20_Research/Papers/强化学习/Safety-Focused_Reinforcement_Learning_Using_Risk-Sensitive_Coupled_Control|Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control]]

![[assets/2611.09290_figure.png|800]]

- **arXiv**: [2611.09290](https://arxiv.org/abs/2611.09290)
- **PDF**: https://arxiv.org/pdf/2611.09290
- **详细分析**: [[20_Research/Papers/强化学习/Safety-Focused_Reinforcement_Learning_Using_Risk-Sensitive_Coupled_Control|Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control]]
- **作者**: Jiabin Lin, Shana Moothedath, Vivek S. Borkar
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CRL, GridWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates the coupled control problem within safety-focused reinforcement learning, addressing the essential challenge of achieving optimal performance while ensuring safety in systems operating within complex environments. We define safety as the requirement to prevent the system from reaching undesirable or hazardous states. We propose a coupled control approach that prioritizes safety by employing effective methods to prevent the system from entering unsafe states while optimizing the performance metric, defined as the average cost. We propose a novel problem transformation that reformulates it into a risk-sensitive problem combined with an average reward criterion. We present a two-timescale Q-learning algorithm where in the faster timescale, the algorithm solves a risk-sensitive control problem to ensure safety, while on a slower timescale, the algorithm focuses on average cost control. We provide theoretical guarantees for the convergence of our algorithms, establishing their significance in ensuring safe, optimal control in dynamic environments. We validated the performance of our approach using GridWorld and CarGoal task in Safety Gymnasium.

</details>

---

### [[20_Research/Papers/机器人/Augmentron_Scalable_Multi-View_Visual_Augmentation_for_Robot_Learning|Augmentron: Scalable Multi-View Visual Augmentation for Robot Learning]]

![[assets/2611.09145_figure.png|800]]

- **arXiv**: [2611.09145](https://arxiv.org/abs/2611.09145)
- **PDF**: https://arxiv.org/pdf/2611.09145
- **详细分析**: [[20_Research/Papers/机器人/Augmentron_Scalable_Multi-View_Visual_Augmentation_for_Robot_Learning|Augmentron: Scalable Multi-View Visual Augmentation for Robot Learning]]
- **作者**: Tanay Tandon, Aseem Doriwala, Jade Choghari, Catherine Weaver, Pragna Mannam
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Augmentron: Scalable Multi-View Visual Augmentation for Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies trained on visually narrow demonstrations can become sensitive to environmental features that are unrelated to the task. Existing generative augmentation methods can introduce visual diversity, but processing every frame and camera view independently is computationally expensive and may produce inconsistent observations across cameras and timestamps. We introduce Augmentron, a geometry-aware pipeline that generates reusable scene representations and renders them through recorded camera poses. This produces temporally and multi-view consistent environ- ment and workspace variations while preserving the robot, task objects, actions, and annotations. Across three physical manipulation tasks, replacing half of the real world training dataset with Augmentron data improves model success across three tasks for both in out-of-distribution distractor objects, and out-of-distribution workspace variation evaluations. In a separate comparison against alternate augmentation techniques, Augmentron achieves the highest pooled success in all three conditions. The results show that introducing augmented data to a data training recipe can help policies generalize to dynamic real-world settings.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Robust_Reinforcement_Learning_Market_Making_Lessons_from_Loss_Function_Experimentation|Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation]]

![[assets/2611.09012_first_page.png|800]]

- **arXiv**: [2611.09012](https://arxiv.org/abs/2611.09012)
- **PDF**: https://arxiv.org/pdf/2611.09012
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Robust_Reinforcement_Learning_Market_Making_Lessons_from_Loss_Function_Experimentation|Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation]]
- **作者**: Siddharth Nand, Bora Guney
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Market makers play a vital role in ensuring efficient trade within financial markets. Recent literature has delved into training market-making systems using reinforcement learning. This paper delves into the impact of various loss function formulations on risk management behavior within reinforcement-based market making. Through empirical evaluation, we contrast profit-maximizing strategies with risk-averse approaches, finding that penalties for inventory and cash management foster more resilient and adaptable market-making strategies. Our results underscore the significance of striking a balance between profit maximization and risk management in algorithmic trading, providing actionable insights for refining strategies in practical settings.

</details>

---

### [[20_Research/Papers/具身智能/VLA_Handover_Failure-Prediction-Based_Switching_from_On-Robot_to_Server_VLA_Models|VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models]]

![[assets/2611.08987_figure.png|800]]

- **arXiv**: [2611.08987](https://arxiv.org/abs/2611.08987)
- **PDF**: https://arxiv.org/pdf/2611.08987
- **详细分析**: [[20_Research/Papers/具身智能/VLA_Handover_Failure-Prediction-Based_Switching_from_On-Robot_to_Server_VLA_Models|VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models]]
- **作者**: Takayuki Nishio
- **cs 子类**: cs.LG, cs.NI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AsyncVLA, CloudEdgeVLA, ComVLA, L-VLA, S-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large vision-language-action (VLA) models generalize well but are difficult to run in real time on a robot, and small VLAs that run there fail more often. Remote inference over beyond-5G and 6G networks lets a robot use a large VLA on a server, but querying the server for every action chunk limits the number of robots per server. We propose VLA handover: the robot runs a small VLA (S-VLA) and switches to a large VLA (L-VLA) on a server only when the S-VLA is likely to fail. We formulate the switching as minimizing the request cost under a required success probability and, since this problem cannot be solved directly, propose a heuristic framework that retrains neither VLA. In simulation with SmolVLA and $π_{0.5}$ on three of the four LIBERO suites, VLA handover raised the success rate by 11-22 percentage points over the S-VLA alone and sent 49-77% fewer requests than server-only control at a 2-4 percentage-point lower success rate, and its completion time grew less with the network latency.

</details>

---

### [[20_Research/Papers/具身智能/STRIDE_Learning_Humanoid_Locomotion_in_Minutes_with_Acceleration-Based_Rewards|STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards]]

![[assets/2611.08857_figure.png|800]]

- **arXiv**: [2611.08857](https://arxiv.org/abs/2611.08857)
- **PDF**: https://arxiv.org/pdf/2611.08857
- **详细分析**: [[20_Research/Papers/具身智能/STRIDE_Learning_Humanoid_Locomotion_in_Minutes_with_Acceleration-Based_Rewards|STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards]]
- **作者**: Nico Bohlinger, Jan Peters
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.82（加权：具身智能 3，强化学习 0.36，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning locomotion directly on a humanoid robot is a promising direction to avoid the sim-to-real gap. However, locomotion rewards in Reinforcement Learning (RL) typically track the base velocity, which cannot be measured onboard without an external motion capture system or well-calibrated state estimator. This is why we introduce \method{}, which learns humanoid locomotion from minutes of samples with a reward that only requires the onboard Inertial Measurement Unit (IMU). Instead of tracking the base velocity, STRIDE rewards the robot for following a commanded acceleration profile. To learn efficiently from this reward, we use the off-policy RL algorithm XQC and combine a high gain setting for the joint position controllers with left-right symmetry augmentation. In simulation, STRIDE learns to walk on the Unitree G1 and Booster T1 humanoids within 14 minutes of samples. Compared to learning without these two components, it reduces the falls during training by 81%, while without them the robot learns only in over an hour.

</details>

---

### [[20_Research/Papers/大模型/What_Are_LLM_Agents_Actually_Learning_on_Low-Budget_Molecular_Optimization_Benchmarks|What Are LLM Agents Actually Learning on Low-Budget Molecular Optimization Benchmarks?]]

![[assets/2611.08522_first_page.png|800]]

- **arXiv**: [2611.08522](https://arxiv.org/abs/2611.08522)
- **PDF**: https://arxiv.org/pdf/2611.08522
- **详细分析**: [[20_Research/Papers/大模型/What_Are_LLM_Agents_Actually_Learning_on_Low-Budget_Molecular_Optimization_Benchmarks|What Are LLM Agents Actually Learning on Low-Budget Molecular Optimization Benchmarks?]]
- **作者**: Jiayu Qin, Zhengquan Luo, Changyou Chen, Zhiqiang Xu
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《What Are LLM Agents Actually Learning on Low-Budget Molecular Optimization Benchmarks?》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work reports large gains for LLM agents on low-budget molecular optimization. We measure the contributions of online optimization, retrievable task information, and permissive oracle landscapes. On PMO at 50 oracle calls, a GPT-4o mini agent's sum AUC falls from 14.44 to 4.85 after task names and curated reference compounds are hidden. An identity-blinded condition that states only the oracle form (e.g., similarity to a hidden reference) scores 5.39, while a deterministic retrieval-only baseline with no LLM reaches 12.16 (84% of the full agent). A full 23-task 2x2 ablation and a three-seed replication on eight tasks support this interpretation. On a protein-targeted benchmark with an AutoDock Vina composite oracle, a single-edit random walk is a strong lower bound; across three seeds it obtains composite 0.636 +/- 0.008 and docking improvement -1.11 +/- 0.04 kcal/mol. As a positive control, a retrieval-free population agent exceeds REINVENT at a matched 50-call AUC budget, with its strongest result at 100 calls. These results motivate two inexpensive sanity checks: retrieval-safe PMO prompts and a random-walk floor for docking-based optimization.

</details>

---
