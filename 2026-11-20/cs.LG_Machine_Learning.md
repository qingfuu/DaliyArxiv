# cs.LG | Machine Learning | 2026-11-20

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/强化学习/Grid_Cells_as_Spectral_Successor_Features_A_Reusable_Basis_for_Continual_Reinforcement_Learning|Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning]]

![[assets/2611.26504_figure.png|800]]

- **arXiv**: [2611.26504](https://arxiv.org/abs/2611.26504)
- **PDF**: https://arxiv.org/pdf/2611.26504
- **详细分析**: [[20_Research/Papers/强化学习/Grid_Cells_as_Spectral_Successor_Features_A_Reusable_Basis_for_Continual_Reinforcement_Learning|Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning]]
- **作者**: Élodie Côté-Gauthier, Doina Precup, Isabeau Prémont-Schwarz
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $θ_i = 1/(1-γλ_i)$, where $λ_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.

</details>

---

### [[20_Research/Papers/世界模型/FEA_solver_integration_of_a_composite_World_Model_with_a_Spiking_Neural_Network_memory_Block_for_computationally_efficient_modelling_of_defe|FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities]]

![[assets/2611.26419_figure.png|800]]

- **arXiv**: [2611.26419](https://arxiv.org/abs/2611.26419)
- **PDF**: https://arxiv.org/pdf/2611.26419
- **详细分析**: [[20_Research/Papers/世界模型/FEA_solver_integration_of_a_composite_World_Model_with_a_Spiking_Neural_Network_memory_Block_for_computationally_efficient_modelling_of_defe|FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities]]
- **作者**: Bassam El Said, Adam Sobey
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《FEA solver integration of a composite World Model with a Spiking Neural Network memory Block for computationally efficient modelling of defects and variabilities》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Each fibre-reinforced composite structure has a unique material architecture. The manufacturing methods used and the presence of defects lead to local variations which require material-scale models that can resolve the response in real time at every location in the structure. Concurrent multi-scale schemes provide this capability, but at a prohibitive computational cost for large structures as the number of integration points and time increments scales with size. Surrogates have been studied extensively as replacements for material-scale models to mitigate these computational limitations. A surrogate must represent an arbitrary local architecture including defects, track the irreversible material state over an unknown number of increments, remain stable when driven recursively by its own predictions, and fit within the memory available at every integration point. Here, a Composites World Model based on a Multi-Modal Spiking Transformer architecture is designed to meet these requirements. The proposed architecture combines a material encoder, a Spiking Neural Network memory block that tracks the long-term internal state of the material, and transformer blocks that learn the short-term applied strain state. The system is trained in three stages: material architecture encoding, base training on short time windows, and recursive fine-tuning with scheduled sampling to suppress cumulative error drift. The trained model is disassembled at inference and coupled to a non-linear FE solver, enabling structural scale simulation of composites containing embedded defects. Benchmarks against experimental results for IM7/8552 laminates under tension, compression and transverse shear, for pristine and wrinkled composites, show that the SNN memory block successfully tracks the material internal state and results in prediction errors between 0.4% and 4.8%.

</details>

---

### [[20_Research/Papers/具身智能/Reference-Free_Humanoid_Skateboarding_via_Termination-Shaped_Reinforcement_Learning|Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning]]

![[assets/2611.26054_figure.png|800]]

- **arXiv**: [2611.26054](https://arxiv.org/abs/2611.26054)
- **PDF**: https://arxiv.org/pdf/2611.26054
- **详细分析**: [[20_Research/Papers/具身智能/Reference-Free_Humanoid_Skateboarding_via_Termination-Shaped_Reinforcement_Learning|Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning]]
- **作者**: Ganeshvar Soenessardien, Michael Przystupa, Kevin Sebastian Luck
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.42（加权：具身智能 1.8，强化学习 1.16，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion research has advanced rapidly on walking and running, but \emph {object-mediated} locomotion, in which a robot must coordinate its body with a passive external object, remains difficult. One challenging task is skateboarding, which requires simultaneous interaction with the ground and a passive but movable platform to achieve forward motion. Current methods for tackling skateboarding with humanoid robots either require human demonstrations or utilise analytic steering models that require system identification. In this paper, we introduce a deep reinforcement learning framework that does not rely on prior data such as demonstrations and enables robots such as the K1 humanoid to learn to skateboard using model-free learning. The method combines task rewards with exploit-blocking terminations. We introduce a number of constraints restricting behaviours such as losing the planted board foot, standing with both feet on the board, excessive twisting, separation from the board, and unstable board motion. Their changing prevalence during training produces an implicit progression from stance control towards sustained robot--board locomotion.

</details>

---

### [[20_Research/Papers/大模型/Goal-Guided_Reinforcement_Learning_via_Fine-Tuning_Vision-Language_Models|Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models]]

![[assets/2611.25742_figure.png|800]]

- **arXiv**: [2611.25742](https://arxiv.org/abs/2611.25742)
- **PDF**: https://arxiv.org/pdf/2611.25742
- **详细分析**: [[20_Research/Papers/大模型/Goal-Guided_Reinforcement_Learning_via_Fine-Tuning_Vision-Language_Models|Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models]]
- **作者**: Yajie Qi, Wei Wei, Lin Li, Lijun Zhang, Jianye Hao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SGRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in Craftax-Classic, and propose a vision-language model (VLM)-guided RL framework that learns environment-specific goal guidance from this dataset. The framework consists of two stages: offline VLM fine-tuning and online goal-guided RL. In the offline stage, we align the VLM with goal preferences using Kullback-Leibler Token-level Direct Preference Optimization (KLTDPO), which combines token-level KL regularization with distributionally robust reweighting. Experiments on Craftax-Classic show that our method collects diamonds earlier than state-of-the-art baselines, achieves the highest score and reward, and attains the highest success rates on most achievements.

</details>

---

### [[20_Research/Papers/强化学习/Improving_Imitation_Policies_for_Multi-Phase_Tasks_through_Residual_Learning_Allocation|Improving Imitation Policies for Multi-Phase Tasks through Residual Learning Allocation]]

![[assets/2611.25320_first_page.png|800]]

- **arXiv**: [2611.25320](https://arxiv.org/abs/2611.25320)
- **PDF**: https://arxiv.org/pdf/2611.25320
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Imitation_Policies_for_Multi-Phase_Tasks_through_Residual_Learning_Allocation|Improving Imitation Policies for Multi-Phase Tasks through Residual Learning Allocation]]
- **作者**: Clinton Enwerem, Saleh Kemal, John S. Baras, Calin Belta
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Improving Imitation Policies for Multi-Phase Tasks through Residual Learning Allocation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Residual reinforcement learning corrects an imitation-trained base policy using a limited budget of environment interaction. In a task with several phases, this budget must be divided among the phases, and the phase in which the base policy fails is not necessarily the phase in which a correction most improves task completion. We formalize this distinction through the completion gain: the change in full-task completion probability when, during a single phase, a state-feedback controller replaces selected components of the base policy's action. We decompose the completion gain into the probability of reaching the phase and the conditional improvement in completion from the start of the phase, and we estimate it from paired episodes. The positive estimates determine which action components the residual policy corrects and how training episodes are distributed across phases. In stochastic point-mass docking experiments, most failures occurred in the final docking phase, whereas the largest completion gain occurred in the preceding channel phase; gain-based allocation improved completion over allocation proportional to failure counts and, in a variant with a longer approach, over uniform allocation at half of the budget. In simulated bimanual robotic assembly, the completion-gain estimates were positive only for insertion and release, although few failures occurred during release; in a second assembly configuration, a residual policy trained in the release phase improved completion from held-out states at the start of release by 16.9%.

</details>

---

### [[20_Research/Papers/强化学习/Cross-Question_Reliable_Reinforcement_Learning|Cross-Question Reliable Reinforcement Learning]]

![[assets/2611.25292_figure.png|800]]

- **arXiv**: [2611.25292](https://arxiv.org/abs/2611.25292)
- **PDF**: https://arxiv.org/pdf/2611.25292
- **详细分析**: [[20_Research/Papers/强化学习/Cross-Question_Reliable_Reinforcement_Learning|Cross-Question Reliable Reinforcement Learning]]
- **作者**: Hector G. Rodriguez, Marcus Rohrbach
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Cross-Question Reliable Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CommonsenseQA, GPQA, HotpotQA, SimpleQA, TriviaQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI systems operating near the limits of their capabilities can maximize utility while minimizing the risk of error by abstaining or deferring questions they are not confident about to a human or a stronger model. Recently, large language models (LLMs) have been post-trained to estimate confidence in their own answers. To achieve this, methods reinforce confidence scores based on the correctness signal to each question-answer pair individually, with rewards that encourage assigning confidence 1 to correct answers and 0 to incorrect answers. However, estimating confidence scores is useful in that it enables selecting only the most confident answers, to maximize the share of solved questions while accommodating the user's risk tolerance. Assigning confidence 1 to correct answers and 0 to incorrect ones is theoretically optimal, but unattainable in practice and detrimental for selective prediction with a non-zero risk tolerance: confidences pushed to 0 and 1 carry no information about how answers compare to one another. We therefore introduce CARE (Cross-question Abstention Reward Estimation), which computes rewards over a set of question-answer pairs: At each of several risk tolerances, the confidences across the set induce an abstention threshold, and each confidence is rewarded for lying on the correct side of it. Since the threshold itself comes from the set, every verbalized confidence is reinforced relative to other questions' confidence, not against its own binary correctness label. On math, CARE increases the coverage at 5% risk (C@5) across MATH-500, GSM8K, and Big-Math-Digits from 0.8% to 42.4%, compared to existing pointwise correctness-matching rewards. When trained on multi-hop Wikipedia QA from HotpotQA, CARE improves C@5 in out-of-distribution general-knowledge, reasoning, and math benchmarks (including CommonsenseQA, GPQA, SimpleQA, and TriviaQA) from 12.3% to 23.6%.

</details>

---

### [[20_Research/Papers/强化学习/φTD_Distributional_Reinforcement_Learning_using_Characteristic_Functions|φTD: Distributional Reinforcement Learning using Characteristic Functions]]

![[assets/2611.25208_figure.png|800]]

- **arXiv**: [2611.25208](https://arxiv.org/abs/2611.25208)
- **PDF**: https://arxiv.org/pdf/2611.25208
- **详细分析**: [[20_Research/Papers/强化学习/φTD_Distributional_Reinforcement_Learning_using_Characteristic_Functions|φTD: Distributional Reinforcement Learning using Characteristic Functions]]
- **作者**: Thomas Mousseau, Tyler Kastner, Davide Baldelli, Amir-massoud Farahmand
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《φTD: Distributional Reinforcement Learning using Characteristic Functions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeepRL, DistRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distributional Reinforcement Learning methods aim to learn the entire distribution of returns, yet current algorithmic approaches are limited to a narrow class of distributions. We propose $\varphi$TD, a method to overcome this limitation by computing the loss in the frequency domain. We demonstrate that this further unifies quantile and categorical approaches to distributional RL, and enables the learning of distributions that were previously impossible to capture, such as mixtures of continuous distributions. We empirically study $\varphi$TD, across synthetic benchmarks and large-scale deep RL environments and demonstrate that the flexibility obtained from wider parametric families can lead to improved performance.

</details>

---
