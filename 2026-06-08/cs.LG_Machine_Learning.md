# cs.LG | Machine Learning | 2026-06-08

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/具身智能/RhinoVLA_Technical_Report|RhinoVLA Technical Report]]

![[assets/2606.07383_figure.png|800]]

- **arXiv**: [2606.07383](https://arxiv.org/abs/2606.07383)
- **PDF**: https://arxiv.org/pdf/2606.07383
- **详细分析**: [[20_Research/Papers/具身智能/RhinoVLA_Technical_Report|RhinoVLA Technical Report]]
- **作者**: Huixi Intelligence, :, Chen Zhang, Chenyang Zhou, Guanglei Ding, Guanghui He, Haibin Gao, Jiajia Chen, Jianyong Zhang, Lianyi Yu, Ningyi Xu, Ping Xu...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RhinoVLA Technical Report》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DexVLA, InternVLA, LingBot-VLA, OpenVLA, RhinoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.

</details>

---

### [[20_Research/Papers/大模型/Self-evolving_LLM_agents_with_in-distribution_Optimization|Self-evolving LLM agents with in-distribution Optimization]]

![[assets/2606.07367_figure.png|800]]

- **arXiv**: [2606.07367](https://arxiv.org/abs/2606.07367)
- **PDF**: https://arxiv.org/pdf/2606.07367
- **详细分析**: [[20_Research/Papers/大模型/Self-evolving_LLM_agents_with_in-distribution_Optimization|Self-evolving LLM agents with in-distribution Optimization]]
- **作者**: Yudi Zhang, Meng Fang, Zhenfang Chen, Mykola Pechenizkiy
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.9，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Self-evolving LLM agents with in-distribution Optimization》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlfWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have recently emerged as powerful controllers for interactive agents in complex environments, yet training them to perform reliable long-horizon decision making remains a fundamental challenge. A key difficulty lies in credit assignment: agents often receive delayed rewards only at the end of episodes. In this paper, we propose Q-Evolve, a self-evolving framework for LLM agents that unifies automatic process-reward labeling and policy learning within a principled in-distribution reinforcement learning paradigm. In each evolving iteration, our method learns an in-distribution critic from a hybrid off-policy dataset that combines expert demonstrations with agent-generated trajectories, stabilizing Bellman backups in sparse-reward settings via a weighted Implicit Q-Learning objective. The learned value function is then used to derive step-wise process rewards through advantage estimation, enabling dense and reliable supervision without environment backtracking or human annotation. Leveraging these signals, we perform behavior-proximal policy optimization that evolves the agent over the data used for process reward labeling, allowing iterative self-improvement without exacerbating distribution shift. We evaluate our method on AlfWorld, WebShop, and ScienceWorld, showing Q-Evolve outperforms strong baselines in sample efficiency, robustness, and overall task performance. Our results demonstrate that stable agent self-evolution is achievable through the co-evolution of process-level supervision and policy, both grounded within a shared in-distribution learning loop.

</details>

---

### [[20_Research/Papers/世界模型/Bootstrap_Theory_of_Representational_Emergence_Explanatory_Insufficiency_as_a_Driver_of_Representation_Learning_and_World_Models|Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models]]

![[assets/2606.07303_first_page.png|800]]

- **arXiv**: [2606.07303](https://arxiv.org/abs/2606.07303)
- **PDF**: https://arxiv.org/pdf/2606.07303
- **详细分析**: [[20_Research/Papers/世界模型/Bootstrap_Theory_of_Representational_Emergence_Explanatory_Insufficiency_as_a_Driver_of_Representation_Learning_and_World_Models|Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models]]
- **作者**: Jacques Raynal, Pierre Slangen, Elsa Raynal, Jacques Margerit
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Representation learning is central to modern machine learning, enabling transitions from handcrafted features to learned embeddings, latent spaces, foundation models, world models, and digital twins. Yet most research examines how representations are optimized after a representational framework has been selected, while less attention is given to when a new level of representation becomes necessary. We introduce the Bootstrap Theory of Representational Emergence (TBER), a framework describing how new representations arise when existing ones become explanatorily insufficient. In this view, representational innovation is not only driven by more data, larger models, or greater computational power, but also by persistent explanatory gaps: situations in which a representation can still describe observations but can no longer make their organization or transformations intelligible. TBER identifies explanatory insufficiency as a positive signal for representational transition. A representation becomes insufficient not because it is necessarily false, but because its explanatory domain has been exceeded. The bootstrap dynamic follows a recursive sequence: observations reveal anomalies; anomalies expose insufficiencies; insufficiencies motivate new representations; and these new representations generate further observations and possible new insufficiencies.We formalize this process through five stages: stabilized observation, anomaly detection, recognition of explanatory insufficiency, representational emergence, and provisional stabilization. We discuss applications to representation learning, latent spaces, foundation models, world models, digital twins, adaptive biological systems, and scientific discovery. TBER suggests that future AI systems may benefit from mechanisms for detecting the explanatory limits of their own internal representations.

</details>

---

### [[20_Research/Papers/具身智能/GenPO++_Generative_Policy_Optimization_with_Jacobian-free_Likelihood_Ratios|GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios]]

![[assets/2606.06967_figure.png|800]]

- **arXiv**: [2606.06967](https://arxiv.org/abs/2606.06967)
- **PDF**: https://arxiv.org/pdf/2606.06967
- **详细分析**: [[20_Research/Papers/具身智能/GenPO++_Generative_Policy_Optimization_with_Jacobian-free_Likelihood_Ratios|GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios]]
- **作者**: Ke Hu, Shutong Ding, Panxin Tao, Jingya Wang, Ye Shi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 1.92（加权：具身智能 0.3，大模型 0.1，强化学习 1.16，世界模型 0.16，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative policies provide expressive and multimodal action distributions, making them attractive for reinforcement learning (RL) in complex continuous-control tasks. Among them, flow-based policies are especially appealing because they generate actions through deterministic transport maps. However, applying such generative policies to likelihood-based on-policy learning remains limited by the difficulty of evaluating the probability of executed actions. Existing flow RL methods either replace the true action-density ratio with approximate surrogates, which can introduce biased updates, or recover exact likelihoods through dummy-action augmentation, which enlarges the policy space and increases computation. In this work, we propose GenPO++, a reversible generative policy optimization framework that uses history states as auxiliary memory in a high-order reversible ODE solver, yielding exact inversion without changing the original action dimension. The resulting generative policy map has a log-determinant determined only by fixed solver coefficients, enabling exact and Jacobian-free likelihood-ratio computation. This design preserves the expressiveness of generative flow policies while avoiding both action ratio bias and dummy-action overhead. We evaluate GenPO++ on large-scale simulated control, fine-tuning, and real-world robotic manipulation tasks, where it achieves competitive or superior performance over state-of-the-art on-policy RL methods, while improving training stability and computational efficiency.

</details>

---

### [[20_Research/Papers/具身智能/Learning_All-Terrain_Locomotion_for_a_Planetary_Rover_with_Actively_Articulated_Suspension|Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension]]

![[assets/2606.06790_figure.jpg|800]]

- **arXiv**: [2606.06790](https://arxiv.org/abs/2606.06790)
- **PDF**: https://arxiv.org/pdf/2606.06790
- **详细分析**: [[20_Research/Papers/具身智能/Learning_All-Terrain_Locomotion_for_a_Planetary_Rover_with_Actively_Articulated_Suspension|Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension]]
- **作者**: Arthur Bouton, Tristan D. Hasseler, Michael Paton, Travis Brown, Jacob Levy, William Reid, Joshua Martin, Hari Nayar
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.42（加权：具身智能 1.5，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a bump trap, a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized.

</details>

---

### [[20_Research/Papers/强化学习/Performance_Variation_in_Deep_Reinforcement_Learning|Performance Variation in Deep Reinforcement Learning]]

![[assets/2606.06746_figure.png|800]]

- **arXiv**: [2606.06746](https://arxiv.org/abs/2606.06746)
- **PDF**: https://arxiv.org/pdf/2606.06746
- **详细分析**: [[20_Research/Papers/强化学习/Performance_Variation_in_Deep_Reinforcement_Learning|Performance Variation in Deep Reinforcement Learning]]
- **作者**: Haruto Tanaka, A. Rupam Mahmood
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Performance Variation in Deep Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CleanRL, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (RL) algorithms often suffer from low run-to-run robustness, manifesting as significant performance variation across independent runs of identically configured agents. Although this issue poses a spectrum of challenges across research and practice, relatively few studies develop methods to evaluate it; RL research instead often reports uncertainty in the estimated mean performance. In this paper, we outline the limitations of conventional uncertainty and variation estimates, particularly their misalignment with purpose and the risk of underreporting. We then propose an alternative percentile-based statistic and visualization method, min-max IPR and run-wise percentile highlighting, respectively. These percentile-based tools are easy to interpret and rely on standard properties of sample percentiles, providing rich information about run-to-run performance variation. We demonstrate this through three case studies. First, we show that LayerNorm and penultimate-layer normalizations narrow performance variation in PPO, whereas the variation is mostly unchanged in SAC. Second, we compare PPO, SAC, TD-MPC, and TD-MPC2, and show TD-MPC exhibits the least variation while being the most data efficient among the four. Finally, in a comparison of DQN and Rainbow on five Atari environments, we show that both algorithms exhibit similar levels of performance variation.

</details>

---

### [[20_Research/Papers/大模型/Uncertainty-Aware_LLM-Guided_Policy_Shaping_for_Sparse-Reward_Reinforcement_Learning|Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning]]

![[assets/2606.06673_figure.png|800]]

- **arXiv**: [2606.06673](https://arxiv.org/abs/2606.06673)
- **PDF**: https://arxiv.org/pdf/2606.06673
- **详细分析**: [[20_Research/Papers/大模型/Uncertainty-Aware_LLM-Guided_Policy_Shaping_for_Sparse-Reward_Reinforcement_Learning|Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning]]
- **作者**: Ujjwal Bhatta, Utsabi Dangol, Sumaly Bajracharya, Rodrigue Rizk, KC Santosh
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.02（加权：大模型 0.7，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sparse rewards and heterogeneous task sequences remain persistent challenges in Reinforcement Learning (RL), often resulting in slow convergence, weak generalization, and inefficient exploration. We propose Uncertainty-Aware LLM-Guided Policy Shaping (ULPS), a novel framework that integrates a calibrated Large Language Model (LLM) into the RL training loop to provide structured, uncertainty-modulated behavioral guidance. ULPS employs an A*-based oracle to synthesize optimal symbolic trajectories, which are used to fine-tune a BERT-based language model. During training, this model supplies action suggestions whose influence is conditioned on epistemic uncertainty estimated via Monte Carlo (MC) dropout. An entropy-based blending mechanism adaptively balances LLM guidance and the learned policy (via Proximal Policy Optimization, PPO), allowing the agent to prioritize reliable priors while preserving adaptability. We evaluate ULPS on the MiniGridUnlockPickup benchmark and observe consistent improvements in success rate, reward efficiency, and sample complexity over unguided, uncalibrated, and standard RL baselines. ULPS achieves more than 9% improvement in execution accuracy after fine-tuning, requires fewer environment interactions, and yields higher reward AUC. Our results demonstrate that integrating symbolic A* trajectories, pretrained language priors, and uncertainty-aware control offers a principled and effective approach to multi-task reinforcement learning in sparse-reward domains, with potential extensibility to partially observable and multi-agent settings.

</details>

---
