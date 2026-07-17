# cs.LG | Machine Learning | 2026-07-15

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/大模型/Verifier-Based_Reinforcement_Fine-Tuning_of_Reasoning_Models_for_Thermal_Energy_Storage_Control|Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control]]

![[assets/2607.12856_figure.png|800]]

- **arXiv**: [2607.12856](https://arxiv.org/abs/2607.12856)
- **PDF**: https://arxiv.org/pdf/2607.12856
- **详细分析**: [[20_Research/Papers/大模型/Verifier-Based_Reinforcement_Fine-Tuning_of_Reasoning_Models_for_Thermal_Energy_Storage_Control|Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control]]
- **作者**: Takumi Shioda, Kohei Terashima, Tatsuo Nagai
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense rewards for every candidate action. Using only 30 training prompts, reinforcement fine-tuning (RFT) trains the model as an upper-level scheduler that outputs hourly heat-pump setpoints from text-based states and forecasts. Evaluation uses a deliberately simple office-building TES benchmark where exact DP is tractable and the optimum is known. RFT reduces the open-weight model's emissions from 70.5 to 61.2 kg-CO2, close to the DP optimum of 60.8 kg-CO2. GPT-5 nearly matches DP and MPC without task-specific training, while GPT-4o, a non-reasoning LLM, produces higher emissions than the no-storage baseline, so inference-time reasoning appears important. Trace analysis shows that RFT mainly stabilizes observable planning patterns (candidate comparison, look-ahead, and feasibility checking) rather than creating a new strategy. Robustness and generalization tests clarify what transfers: the reinforced planning patterns persist under forecast errors and an unseen TES condition and carry over to a battery task, but its different structure limits the gains. DP-based verifiable rewards offer a practical way to adapt open-weight reasoning models to building storage scheduling. These results motivate higher-fidelity tests of whole-building control and scalable verifiers for city-scale energy management.

</details>

---

### [[20_Research/Papers/强化学习/Directional_Constraints_for_Efficient_Exploration_in_Safe_Reinforcement_Learning|Directional Constraints for Efficient Exploration in Safe Reinforcement Learning]]

![[assets/2607.12784_figure.png|800]]

- **arXiv**: [2607.12784](https://arxiv.org/abs/2607.12784)
- **PDF**: https://arxiv.org/pdf/2607.12784
- **详细分析**: [[20_Research/Papers/强化学习/Directional_Constraints_for_Efficient_Exploration_in_Safe_Reinforcement_Learning|Directional Constraints for Efficient Exploration in Safe Reinforcement Learning]]
- **作者**: Paolo Magliano, Puze Liu, Jan Peters, Davide Tateo, Raffaello Camoriano
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Directional Constraints for Efficient Exploration in Safe Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SafeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning has revolutionized the landscape of robotic research, allowing robust learning of complex robotic skills in simulation. However, real-world deployment in open-ended environments requires strong safety guarantees to prevent dangerous or harmful behaviors. Safe Reinforcement Learning methods address this requirement by enforcing safety constraints. Nevertheless, learning under constraints often reduces learning speed and could lead to suboptimal task performance, as the agent must solve a more complex constrained optimization problem compared to unconstrained settings. To tackle this issue, in this work, we propose an extension of the ATACOM framework, a state-of-the-art reliable safety layer that can be integrated with existing Reinforcement Learning algorithms to enforce constraints derived from prior knowledge of the system or learned directly from data. Our proposed method, named ATACOM Directional Constraints (ATACOM-DC), significantly improves the safety-performance trade-off by introducing directional constraints that distinguish between actions approaching and moving away from constraint boundaries, activating constraint enforcement only when necessary. We evaluate our method across a range of challenging robotic control tasks in simulation, analyzing both constraint-violation costs and achieved task performance. Code and additional material at https://atacom-dc.robot-learning.net.

</details>

---

### [[20_Research/Papers/强化学习/Gradient-free_learning_of_a_closed-loop_wall_controller_for_turbulent_drag_reduction|Gradient-free learning of a closed-loop wall controller for turbulent drag reduction]]

![[assets/2607.12626_figure.png|800]]

- **arXiv**: [2607.12626](https://arxiv.org/abs/2607.12626)
- **PDF**: https://arxiv.org/pdf/2607.12626
- **详细分析**: [[20_Research/Papers/强化学习/Gradient-free_learning_of_a_closed-loop_wall_controller_for_turbulent_drag_reduction|Gradient-free learning of a closed-loop wall controller for turbulent drag reduction]]
- **作者**: Giorgio Maria Cavallazzi, Miguel Pérez Cuadrado, Alfredo Pinelli
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Gradient-free learning of a closed-loop wall controller for turbulent drag reduction》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GRU-MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Closed-loop wall control learnt by multi-agent reinforcement learning can lower skin-friction drag in turbulent channels, but these gradient-based policies are trained on small periodic boxes and exhibit reduced performance when carried over to a larger domain. We recently showed that such policies are also prone to saturated bang-bang actuations that collapse into standing streamwise waves whose scale is set by the computational box rather than by the near-wall cycle, and proposed architectural fixes that avoid these degeneracies. Here, we employ Evolution Strategy (ES) to optimise a recurrent closed-loop controller directly on a large turbulent channel at $\mathit{Re}_τ\simeq180$, evaluating policy performance over full flow episodes using an energy-aware criterion and processing candidate policies in parallel. To our knowledge, this is the first application of an evolution strategy to the control of a turbulent flow. The ES controller reduces the skin friction by about $26\%$, exceeding the gradient-based multi-agent controller of Cavallazzi et al. (2026), GRU-MARL, trained on a minimal box ($17\%$), and marginally exceeding classic opposition control (OC, $22\%$). A wall-normal decomposition of the friction, Reynolds-stress profiles and anisotropy invariants show that the ES and opposition-controlled flows follow separate trajectories through the buffer layer, reaching comparable drag reduction by different reorganisations of the near-wall turbulence. In particular, the ES actuation correlates predominantly with the streamwise velocity fluctuations rather than with the wall-normal velocity that classical OC targets.

</details>

---

### [[20_Research/Papers/强化学习/Environment_Parameter_Gradient_Theorem_for_Policy-Environment_Co-Design_in_Reinforcement_Learning|Environment Parameter Gradient Theorem for Policy-Environment Co-Design in Reinforcement Learning]]

![[assets/2607.12590_first_page.png|800]]

- **arXiv**: [2607.12590](https://arxiv.org/abs/2607.12590)
- **PDF**: https://arxiv.org/pdf/2607.12590
- **详细分析**: [[20_Research/Papers/强化学习/Environment_Parameter_Gradient_Theorem_for_Policy-Environment_Co-Design_in_Reinforcement_Learning|Environment Parameter Gradient Theorem for Policy-Environment Co-Design in Reinforcement Learning]]
- **作者**: Amber Srivastava
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Environment Parameter Gradient Theorem for Policy-Environment Co-Design in Reinforcement Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is traditionally concerned with learning a control policy for a fixed environment. In many engineering systems, however, the environment itself is alterable: physical or operational parameters can be tuned to shape the transition dynamics and costs experienced by the agent. This motivates jointly optimizing both the policy and the environment design parameters. To this end, we establish an Environment Parameter Gradient Theorem -- a formal expression for the gradient of the value function with respect to environment parameters. The key theoretical device is a generalized action-value function $Q_{π,ξ}(s,a,ζ)$, which comprises two copies of the environment parameters: $ζ$ governs the cost and transition dynamics at the current state--action pair, while $ξ$ governs the future rollouts. This decoupling yields a tractable closed-form gradient expression and is essential to the theorem's derivation. Building on this result, we develop a model-free algorithm that simultaneously learns the optimal policy and the environment parameters. We demonstrate the efficacy of our framework on a UAV network design problem, where the optimal UAV placement (environment parameters) and communication routes (governed by the policy) are learned jointly to minimize the total communication cost in the network.

</details>

---

### [[20_Research/Papers/强化学习/Robust_In-Hand_Manipulation_via_Priors_in_Reinforcement_Learning_and_Mechanical_Design|Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design]]

![[assets/2607.12105_figure.png|800]]

- **arXiv**: [2607.12105](https://arxiv.org/abs/2607.12105)
- **PDF**: https://arxiv.org/pdf/2607.12105
- **详细分析**: [[20_Research/Papers/强化学习/Robust_In-Hand_Manipulation_via_Priors_in_Reinforcement_Learning_and_Mechanical_Design|Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design]]
- **作者**: Yifei Chen, Shihan Lu, Ed Colgate, Kevin Lynch
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In-hand manipulation without external sensing is challenging due to uncertainties from finger-object contacts and disturbances by gravity. While reinforcement learning has shown promise in learning complex finger gaiting, existing approaches do not prioritize maintaining well-conditioned grasps for sustained manipulation. We introduce two complementary physics priors for robust in-hand rolling: a global grasp-quality prior derived from classical grasp analysis and a local contact-geometry prior based on fingertip curvature. The grasp-quality prior is used as a dense reward-shaping term that encourages well-distributed contacts with improved worst-case wrench resistance. The contact-geometry prior is expressed in the fingertip geometry that mechanically shapes the contact interface toward task-aligned rolling while reducing off-axis drift. We evaluate the effect of these priors on learning in-hand rolling manipulation for a multifingered robotic hand manipulating three different objects at four palm orientations. Results show significant improvement in rotation efficiency, grasp stability, and disturbance rejection, suggesting that physics priors embedded in both learning and fingertip morphology improve task robustness and sim-to-real transfer. An overview video can be found at https://youtu.be/pdd1wHxQnJM?si=dM-U5kiiPTYsk3Pk.

</details>

---

### [[20_Research/Papers/强化学习/LIDAR-AD_A_Decoder-Free_Latent-Interaction_Dreamer_with_Action-Residual_Chains_for_Autonomous_Driving|LIDAR-AD: A Decoder-Free Latent-Interaction Dreamer with Action-Residual Chains for Autonomous Driving]]

![[assets/2607.11964_figure.png|800]]

- **arXiv**: [2607.11964](https://arxiv.org/abs/2607.11964)
- **PDF**: https://arxiv.org/pdf/2607.11964
- **详细分析**: [[20_Research/Papers/强化学习/LIDAR-AD_A_Decoder-Free_Latent-Interaction_Dreamer_with_Action-Residual_Chains_for_Autonomous_Driving|LIDAR-AD: A Decoder-Free Latent-Interaction Dreamer with Action-Residual Chains for Autonomous Driving]]
- **作者**: Yongzhi Liu, Yang Xiao, Zhong Cao, Zeng Kang, Sunan Zhang, Zhaozhi Dong, Guojun Yu, Weichao Zhuang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.16，世界模型 1.36）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《LIDAR-AD: A Decoder-Free Latent-Interaction Dreamer with Action-Residual Chains for Autonomous Driving》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous driving requires long-horizon closedloop decision making in dynamic traffic environments. Latent world models offer an effective framework for this problem by enabling imagination-based decision making in compact latent spaces. However, multi-source observations contain controlirrelevant redundancy, whereas reliable driving decisions rely on risk-relevant relations, future dynamics, and continuous action adjustments. This mismatch makes observation reconstruction and absolute action modeling suboptimal for learning decisionrelevant latent dynamics. We propose LIDAR-AD, a decoderfree Latent-Interaction Dreamer with Action-Residual Chains for autonomous driving. LIDAR-AD replaces observation reconstruction with redundancy-reduced latent alignment, encouraging compact representations of risk-relevant relations in multi-source driving inputs. It further models vehicle control as residual action updates and uses residual-action sequence contrastive learning to align multi-step residual-driven rollouts with future latent states. A deterministic analysis shows that the latent-tanh residual parameterization preserves interior action reachability while representing smooth long-horizon control as compact local updates. Together, these designs improve risk-aware state abstraction, continuous-control modeling, and long-horizon dynamics prediction. Extensive experiments across diverse simulated driving scenarios demonstrate that LIDAR-AD consistently outperforms world-model baselines, achieving the highest reward and the best success rate among learning-based methods. Evaluations on nuPlan-derived log-reconstructed scenarios further demonstrate the transferability of LIDAR-AD under real-world traffic layouts.

</details>

---
