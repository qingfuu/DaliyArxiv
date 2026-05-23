# cs.LG | Machine Learning | 2026-05-22

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/Remember_to_be_Curious_Episodic_Context_and_Persistent_Worlds_for_3D_Exploration|Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration]]

![[assets/2605.22814_figure.png|800]]

- **arXiv**: [2605.22814](https://arxiv.org/abs/2605.22814)
- **PDF**: https://arxiv.org/pdf/2605.22814
- **详细分析**: [[20_Research/Papers/具身智能/Remember_to_be_Curious_Episodic_Context_and_Persistent_Worlds_for_3D_Exploration|Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration]]
- **作者**: Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LingBot-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at https://recuriosity.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/A_note_on_convergence_of_Wasserstein_policy_optimization|A note on convergence of Wasserstein policy optimization]]

![[assets/2605.22622_first_page.png|800]]

- **arXiv**: [2605.22622](https://arxiv.org/abs/2605.22622)
- **PDF**: https://arxiv.org/pdf/2605.22622
- **详细分析**: [[20_Research/Papers/强化学习/A_note_on_convergence_of_Wasserstein_policy_optimization|A note on convergence of Wasserstein policy optimization]]
- **作者**: David Šiška, Yufei Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《A note on convergence of Wasserstein policy optimization》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wasserstein Policy Optimization (WPO) is a recently proposed reinforcement learning algorithm that leverages Wasserstein gradient flows to optimize stochastic policies in continuous action spaces. Despite its empirical success, the theoretical convergence properties of WPO in environments with continuous state and action spaces have yet to be fully established. In this note, we argue that WPO within the framework of entropy-regularised Markov Decision Processes converges linearly. This is done by leveraging recent advances in mean-field analysis for convergence of gradient flows using log-Sobole inequalities. Assuming existence of sufficiently regular solution to the gradient flow equation we demonstrate monotonic energy dissipation along the flow and establish a local log-Sobolev inequality. Ultimately, these properties allow us to argue that the value function should converge linearly to the global optimum.

</details>

---

### [[20_Research/Papers/强化学习/Factored_Diffusion_Policies_Compositionally_Generalized_Robot_Control_with_a_Single_Score_Network|Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network]]

![[assets/2605.22596_figure.png|800]]

- **arXiv**: [2605.22596](https://arxiv.org/abs/2605.22596)
- **PDF**: https://arxiv.org/pdf/2605.22596
- **详细分析**: [[20_Research/Papers/强化学习/Factored_Diffusion_Policies_Compositionally_Generalized_Robot_Control_with_a_Single_Score_Network|Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network]]
- **作者**: Sayan Mitra, Ege Yuceel, Noah Giles, Abhishek Pai
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network》归入 机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic tasks are typically specified by a tuple of factors, such as the object to be grasped, the obstacles to be avoided, the color of the target, and so on. Collecting expert demonstrations for every combination of factor values grows combinatorially. We present factored diffusion policies: a single shared diffusion network trained with per-factor null-token dropout, whose score decomposes additively across factors at inference. Under approximate conditional independence between factors given the action-observation pair, this composition approximates the true joint score with a bounded uniform error, reducing the training-task budget from a product of factor cardinalities to a sum. A trajectory-tube certificate chains this score-level bound through the reverse-time sampling ODE and a contracting tracking controller into a closed-loop state-trajectory tube whose radius factors into an ODE-sensitivity constant and a per-factor score-error budget. Unlike compositional-diffusion methods for control that combine separately trained networks, we use one shared network. Drone racing experiments confirm both the generalization bound and the certificate. On state-based multi-gate racing, the factored policy passes 90% of held-out gates -- matching an oracle -- while a K-network composition baseline collapses to 3%; on vision-based single-gate traversal, it transfers zero-shot to an unseen venue with +11.7pp success-rate gain and 2.4X crash-rate reduction.

</details>

---

### [[20_Research/Papers/大模型/GraphFlow_A_Graph-Based_Workflow_Management_for_Efficient_LLM-Agent_Serving|GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving]]

![[assets/2605.22566_figure.png|800]]

- **arXiv**: [2605.22566](https://arxiv.org/abs/2605.22566)
- **PDF**: https://arxiv.org/pdf/2605.22566
- **详细分析**: [[20_Research/Papers/大模型/GraphFlow_A_Graph-Based_Workflow_Management_for_Efficient_LLM-Agent_Serving|GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving]]
- **作者**: Ao Li, Shangpeng Yang, Fahao Chen, Tianheng Xu, Peng Li, Zhou Su
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based agents demonstrate strong reasoning and execution capabilities on complex tasks when guided by structured instructions, commonly referred to as workflows. However, existing workflow-assisted agent serving systems typically rely on predefined templates and shallow matching mechanisms, which limit their ability to capture deep semantic relationships and generalize to previously unseen tasks. To address these limitations, we propose a new workflow management paradigm that represents workflows using a unified graph, termed wGraph, where each node corresponds to an atomic operation. wGraph serves as a shared substrate from which task-specific workflows are dynamically instantiated. Building on wGraph primitives, we introduce GraphFlow, a system that efficiently integrates workflows into agent serving through two key designs. First, adaptive workflow generation dynamically constructs workflows from wGraph based on task semantics and constraint requirements. Second, workflow state management exploits wGraph structure to efficiently manage Key-Value (KV) caches, reducing redundant computation during agent serving. Extensive experiments across five benchmark datasets show that GraphFlow consistently outperforms state-of-the-art methods, yielding an average performance improvement of approximately 4.95 percentage points, while achieving an approximately 4$\times$ reduction in memory footprint.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_learning_for_ion_shuttling_on_trapped-ion_quantum_computers|Reinforcement learning for ion shuttling on trapped-ion quantum computers]]

![[assets/2605.22463_figure.png|800]]

- **arXiv**: [2605.22463](https://arxiv.org/abs/2605.22463)
- **PDF**: https://arxiv.org/pdf/2605.22463
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_learning_for_ion_shuttling_on_trapped-ion_quantum_computers|Reinforcement learning for ion shuttling on trapped-ion quantum computers]]
- **作者**: Maximilian Schier, Lea Richtmann, Christian Staufenbiel, Tobias Schmale, Daniel Borcherding, Michèle Heurs, Bodo Rosenhahn
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement learning for ion shuttling on trapped-ion quantum computers》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scalable trapped-ion quantum computing is commonly realized with modular chips that feature distinct zones with specific functionalities, such as storage, state preparation, and gate execution. To execute a quantum circuit, the ions must be transported between these zones. This process is called ion shuttling. To achieve reliable computation results, the shuttling process must be optimized. However, as the number of ions increases, this becomes a high-dimensional optimization problem where optimal solutions cannot be computed efficiently. We demonstrate, to the best of our knowledge, the first use of reinforcement learning (RL) for the optimization of ion shuttling. RL is well-suited for such scenarios, as it enables learning a strategy through direct interaction with the problem. We show that our RL approach outperforms current state-of-the-art heuristic techniques, yielding a reduction in shuttling operations of up to 36.3 %. Furthermore, we show that our method is easily applicable to various chip architectures. Our approach offers a versatile method to study shuttling efficiency during chip design and, therefore, a highly relevant tool for future, more complex architectures.

</details>

---

### [[20_Research/Papers/强化学习/Target-Aligned_Bellman_Backup_for_Cross-domain_Offline_Reinforcement_Learning|Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning]]

![[assets/2605.22376_figure.png|800]]

- **arXiv**: [2605.22376](https://arxiv.org/abs/2605.22376)
- **PDF**: https://arxiv.org/pdf/2605.22376
- **详细分析**: [[20_Research/Papers/强化学习/Target-Aligned_Bellman_Backup_for_Cross-domain_Offline_Reinforcement_Learning|Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning]]
- **作者**: Wei Liu, Ting Long
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Target-Aligned Bellman Backup for Cross-domain Offline Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-domain offline reinforcement learning (CDRL) aims to improve policy learning in a target domain by leveraging data collected from a source domain. Existing works typically assess the transferability of source-domain data by measuring its similarity to target-domain transitions, and implicitly perform transition-level selection. Transitions that are considered similar are assigned higher weights or rewards, while dissimilar ones are down-weighted. However, transition-level similarity does not necessarily imply consistency in long-term returns. Even visually or dynamically similar transitions may lead to significantly different outcomes in the target domain, which can mislead policy learning and degrade performance. To address this issue, we revisit the fundamental objective of policy learning. Since policy optimization ultimately relies on Bellman targets to evaluate the quality of decisions, we propose to assess the transferability of source-domain transitions based on their alignment with target-domain Bellman targets, rather than superficial transition similarity. Based on this insight, we propose a method termed Target-Aligned Bellman Backup (TABB), which selectively leverages source-domain data by measuring their contribution to accurate Bellman target estimation in the target domain. We evaluate TABB across a broad range of cross-domain offline RL settings with highly limited target-domain data. Experimental results show that TABB consistently achieves strong performance.

</details>

---

### [[20_Research/Papers/强化学习/Chebyshev_Policies_and_the_Mountain_Car_Problem_Reinforcement_Learning_for_Low-Dimensional_Control_Tasks|Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks]]

![[assets/2605.22305_figure.png|800]]

- **arXiv**: [2605.22305](https://arxiv.org/abs/2605.22305)
- **PDF**: https://arxiv.org/pdf/2605.22305
- **详细分析**: [[20_Research/Papers/强化学习/Chebyshev_Policies_and_the_Mountain_Car_Problem_Reinforcement_Learning_for_Low-Dimensional_Control_Tasks|Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks]]
- **作者**: Stefan Huber, Hannes Unger, Georg Schäfer, Jakob Rehrl
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Chebyshev Policies and the Mountain Car Problem: Reinforcement Learning for Low-Dimensional Control Tasks》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We analytically solve the Mountain Car problem, a canonical benchmark in RL, and derive an optimal control solution, closing a gap after 36 years. This enables us to reveal two surprising insights: The optimal control is quite simple, yet modern RL agents display a large gap to optimality. Motivated by the analysis of the optimal control, we introduce Chebyshev policies as a universal (i.e. dense) class of RL policies from first principles. They can be trained as drop-in replacements of neural nets, reducing the regret by a factor of 4.18, while requiring 277 times fewer parameters, fostering sample efficiency, explainability and realtime capability. Chebyshev policies are evaluated on further RL tasks, including a real-world nonlinear motion control testbed. They consistently improve performance over neural nets with PPO, ARS and REINFORCE. Our results demonstrate how Chebyshev policies offer a compelling and lightweight alternative or addition to neural nets for low-dimensional control tasks.

</details>

---

### [[20_Research/Papers/强化学习/Kernel-Based_Safe_Exploration_in_Deep_Reinforcement_Learning|Kernel-Based Safe Exploration in Deep Reinforcement Learning]]

![[assets/2605.22207_figure.png|800]]

- **arXiv**: [2605.22207](https://arxiv.org/abs/2605.22207)
- **PDF**: https://arxiv.org/pdf/2605.22207
- **详细分析**: [[20_Research/Papers/强化学习/Kernel-Based_Safe_Exploration_in_Deep_Reinforcement_Learning|Kernel-Based Safe Exploration in Deep Reinforcement Learning]]
- **作者**: Rupak Majumdar, Nikhil Singh, Sadegh Soudjani
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Kernel-Based Safe Exploration in Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety has been a major concern when deploying deep reinforcement learning algorithms in the real world. A promising direction that ensures that the learned policy does not visit unsafe regions is to learn a \emph{barrier function} along with the policy. A barrier is a function from states to reals that assigns low values to the initial states, high values to the unsafe states, and decreases in expectation on each transition; such a function can be used to bound the probability of reaching unsafe states. Previous attempts learned a barrier function directly from exploration data, but this required either large amounts of data or restrictions on the system dynamics. In this paper, we show how kernel embeddings can be used to learn barrier functions during deep reinforcement learning for stochastic systems with unknown dynamics. Our algorithm, \emph{kernel-based safe exploration (KBSE)}, learns an optimal policy and a barrier simultaneously during exploration. The barriers are computed iteratively, represented as conditional mean embeddings, and provide better probabilistic safety guarantees with more exploration. The exploration algorithm uses the learned barrier functions to identify safety violations. In the case of violation, it intervenes to modify the unsafe action to a safe action, thereby ensuring that the exploration is restricted to actions that bound the probability of reaching unsafe states. We evaluate KBSE on several complex continuous control benchmarks. Experimental results establish our new algorithm to be suitable for synthesizing control policies that are probabilistically safe without degradation in reward accumulation.

</details>

---

### [[20_Research/Papers/大模型/Reinforced_Graph_of_Thoughts_RL-Driven_Adaptive_Prompting_for_LLMs|Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs]]

![[assets/2605.22195_figure.png|800]]

- **arXiv**: [2605.22195](https://arxiv.org/abs/2605.22195)
- **PDF**: https://arxiv.org/pdf/2605.22195
- **详细分析**: [[20_Research/Papers/大模型/Reinforced_Graph_of_Thoughts_RL-Driven_Adaptive_Prompting_for_LLMs|Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs]]
- **作者**: Manuel Noah Riesen, Peter Alfred von Niederhäusern
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reinforced Graph of Thoughts: RL-Driven Adaptive Prompting for LLMs》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graph of Thoughts (GoT), a generalized form of recent prompting paradigms for large language models (LLMs), has been shown to be useful for elaborate problem solving. By executing a graph of operations, thoughts of the LLM are structured as an arbitrary graph, forming the actual graph of thoughts. Originally, the graph of operations is defined manually, which requires in-depth knowledge about the solution of the problem to solve. Such a static graph of operations is rigid and therefore lacks adaptability. We propose Reinforced Graph of Thoughts (RGoT), an automated approach to the GoT prompting paradigm that leverages reinforcement learning (RL) to adaptively generate a graph of operations from a human-defined set. Results indicate that, under certain constraints, it is possible to construct graphs of operations adaptively to the task's complexity in an automated way.

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Euclidean_Proximity_Repairing_Latent_World_Models_with_Horizon-Matched_Trajectory_Reachability_Metrics|Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics]]

![[assets/2605.22164_figure.png|800]]

- **arXiv**: [2605.22164](https://arxiv.org/abs/2605.22164)
- **PDF**: https://arxiv.org/pdf/2605.22164
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Euclidean_Proximity_Repairing_Latent_World_Models_with_Horizon-Matched_Trajectory_Reachability_Metrics|Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics]]
- **作者**: Liangyu Li, Shengzhi Wang, Qingwen Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models can contain the state needed for control, yet their terminal-cost interface can expose the planner to the wrong decision-relevant information. In common latent MPC, candidate sequences are ranked by Euclidean distance between predicted terminal and goal latent states; this assumes that raw latent distance weights reachability-relevant variables correctly. We propose trajectory reachability metrics (TRM), a post-hoc terminal-ranking method for fixed latent world models. TRM trains a small pairwise head from logged trajectory structure and uses it as a replacement or hybrid cost; the encoder, dynamics, sampler, optimizer, and evaluation manifests remain fixed. The key design choice is horizon-aware supervision: the metric is trained on broad, balanced temporal separations to match the long-horizon terminal candidate ranking problem. On a hard TwoRoom benchmark, raw latent planning with LeWorldModel (LeWM) reaches 7.0% success, while full-horizon TRM reaches 97.0%; shuffled temporal-label controls stay at 0.0%. The same recipe improves a PLDM baseline from 32.7% to 84.0% across three seeds, and a short-horizon TRM variant reaches only 35.0% with the 100,000 pair budget. In TwoRoom, we provide mechanistic evidence for why TRM works: XY position is linearly decodable (R^2=0.998), yet raw latent MSE misranks candidates; the XY-probe rowspace accounts for less than 1% of terminal-goal latent MSE but carries most candidate-quality signal; and SCSA audits show that TRM improves the ordering and selected endpoint seen by the planner. On PushT go50/go75, TRM-style task-state metrics improve SCSA ranking and selected final distance more cleanly than closed-loop success, motivating auxiliary hybrid costs in continuous manipulation. TRM is the planner-facing repair, and audits explain when terminal reachability metrics should replace or augment raw latent proximity.

</details>

---

### [[20_Research/Papers/机器人/CoRMA_Contrastive_RMA_for_Contact-Rich_Meta-Adaptation|CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation]]

![[assets/2605.22082_figure.png|800]]

- **arXiv**: [2605.22082](https://arxiv.org/abs/2605.22082)
- **PDF**: https://arxiv.org/pdf/2605.22082
- **详细分析**: [[20_Research/Papers/机器人/CoRMA_Contrastive_RMA_for_Contact-Rich_Meta-Adaptation|CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation]]
- **作者**: Wentian Wang, Chutong Wen, Hongxu Ma, Wuhao Wang, Zhexiong Xue, Abdul Haseeb Nizamani, Dandi Zhou, Xinhai Sun, Jianqiao Zhu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CURL, Meta-RL, PEARL, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present CoRMA(Contrastive Robotic Motor Adaptation), a context-based meta-adaptation framework that modifies RMA for force-dominant assembly. CoRMA replaces raw simulator-parameter adaptation with a compact 6D simulator-only semantic contact context describing contact onset, lateral engagement, guided transition, contact direction, and jamming. A deployable causal Transformer adapter infers this context online from force, proprioceptive, and action histories using semantic regression and a force-regime contrastive objective. At deployment, oracle context is removed and replaced by the inferred context, enabling within-episode adaptation without demonstrations, privileged inputs, or gradient updates. We evaluate CoRMA on PegInsert, GearMesh, and NutThread in Isaac Lab / Isaac Sim~5.0 and on a real Marvin arm. Compared with FORGE baselines that achieve high simulation success but degrade substantially on hardware, CoRMA retains higher verified real success under controlled target-pose noise. These results support semantic contact inference as a reusable adaptation interface within a related assembly task family, while broader unseen-task generalization and Real2Sim calibration remain future work.

</details>

---

### [[20_Research/Papers/世界模型/stable-worldmodel_A_Platform_for_Reproducible_World_Modeling_Research_and_Evaluation|stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation]]

![[assets/2605.21800_figure.png|800]]

- **arXiv**: [2605.21800](https://arxiv.org/abs/2605.21800)
- **PDF**: https://arxiv.org/pdf/2605.21800
- **详细分析**: [[20_Research/Papers/世界模型/stable-worldmodel_A_Platform_for_Reproducible_World_Modeling_Research_and_Evaluation|stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation]]
- **作者**: Lucas Maes, Quentin Le Lidec, Luiz Facury, Nassim Massaudi, Ayush Chaurasia, Francesco Capuano, Richard Gao, Taj Gillin, Dan Haramati, Damien Scieur, Yann LeCun, Randall Balestriero
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.16，世界模型 0.56）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. It delivers (1) a high-performance Lance-based data layer with native support and conversion tools for MP4, HDF5, and LeRobot datasets, (2) clean, well-tested implementations of modern world model baselines and planning solvers, and (3) a broad suite of environments and tasks extended with controllable visual, geometric, and physical factors of variation for systematic in-silico evaluation of dynamics understanding, control performance, representation quality, and out-of-distribution generalization. By unifying the full pipeline under a single, scalable framework, \texttt{swm} dramatically reduces research overhead and accelerates trustworthy progress toward reliable world models.

</details>

---

### [[20_Research/Papers/大模型/Memory-R2_Fair_Credit_Assignment_for_Long-Horizon_Memory-Augmented_LLM_Agents|Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents]]

![[assets/2605.21768_figure.png|800]]

- **arXiv**: [2605.21768](https://arxiv.org/abs/2605.21768)
- **PDF**: https://arxiv.org/pdf/2605.21768
- **详细分析**: [[20_Research/Papers/大模型/Memory-R2_Fair_Credit_Assignment_for_Long-Horizon_Memory-Augmented_LLM_Agents|Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents]]
- **作者**: Sikuan Yan, Ahmed Bahloul, Ercong Nie, Susanna Schwarzmann, Riccardo Trivisonno, Volker Tresp, Yunpu Ma
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.9，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-augmented LLM agents enable interactions that extend beyond finite context windows by storing, updating, and reusing information across sessions. However, training such agents with reinforcement learning in multi-session environments is challenging because memory turns the agent's past actions into part of its future environment. Once different rollouts write, update, or delete different memories, they no longer share the same intermediate memory state, making trajectory-level comparisons fundamentally unfair. This violates a key assumption behind group-relative methods such as GRPO, where rollouts are compared as if they were sampled from the same effective environment. Consequently, trajectory-level rewards provide noisy or biased credit signals for long-horizon memory operations. To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents. Its core algorithm, LoGo-GRPO, combines local and global group-relative optimization. The global objective preserves end-to-end learning from long-horizon trajectory-level rewards, while local rerollouts compare different memory-operation outcomes from the same intermediate memory state, yielding fairer group comparisons and more precise supervision for memory construction. Beyond credit assignment, Memory-R2 jointly optimizes memory formation and memory evolution with a shared-parameter co-learning design, where a fact extractor and a memory manager are instantiated from the same LLM backbone through role-specific prompts. To stabilize multi-step RL over long memory horizons, we adopt a progressive curriculum that increases the training horizon from 8 to 16 to 32 sessions. Together, these components provide an effective training paradigm for memory-augmented LLM agents in long-horizon multi-session settings.

</details>

---

### [[20_Research/Papers/强化学习/On_the_Sample_Complexity_of_Discounted_Reinforcement_Learning_with_Optimized_Certainty_Equivalents|On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents]]

![[assets/2605.21763_first_page.png|800]]

- **arXiv**: [2605.21763](https://arxiv.org/abs/2605.21763)
- **PDF**: https://arxiv.org/pdf/2605.21763
- **详细分析**: [[20_Research/Papers/强化学习/On_the_Sample_Complexity_of_Discounted_Reinforcement_Learning_with_Optimized_Certainty_Equivalents|On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents]]
- **作者**: Oliver Mortensen, Mohammad Sadegh Talebi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study risk-sensitive reinforcement learning in finite discounted MDPs, where a generative model of the MDP is assumed to be available. We consider a family or risk measures called the optimized certainty equivalent (OCE), which includes important risk measures such as entropic risk, CVaR, and mean-variance. Our focus is on the sample complexities of learning the optimal state-action value function (value learning) and an optimal policy (policy learning) under recursive OCE. We provide an exact characterization of utility functions $u$ for which the corresponding OCE defines an objective that is PAC-learnable. We analyze a simple model-based approach and derive PAC sample complexity bounds. We establish that whenever $u$ does not have full domain $\text{dom}(u)\neq \mathbb{R}$, the corresponding problem is not PAC-learnable. Finally, we establish corresponding lower bounds for both value and policy learning, demonstrating tightness in the size $SA$ of state-action space, and for a more restricted class of utilities, we derive lower bounds that makes the dependence on the effective horizon $\frac{1}{1-γ}$ explicit. Specifically, for $\text{CVaR}_τ$ we show that the correct dependence on $τ$ is $\frac{1}{τ^2}$, thus improving by a factor of $\frac{1}τ$ over state-of-the-art although our bound has a suboptimal dependence on $\frac{1}{1-γ}$.

</details>

---

### [[20_Research/Papers/大模型/AutoMCU_Feasibility-First_MCU_Neural_Network_Customization_via_LLM-based_Multi-Agent_Systems|AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems]]

![[assets/2605.21560_figure.png|800]]

- **arXiv**: [2605.21560](https://arxiv.org/abs/2605.21560)
- **PDF**: https://arxiv.org/pdf/2605.21560
- **详细分析**: [[20_Research/Papers/大模型/AutoMCU_Feasibility-First_MCU_Neural_Network_Customization_via_LLM-based_Multi-Agent_Systems|AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems]]
- **作者**: Penglin Dai, Zijie Zhou, Xincao Xu, Junhua Wang, Xiao Wu, Lixin Duan
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MobileNet, NAS-Bench, Real-World, ShuffleNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying neural networks on microcontroller units (MCUs) is critical for edge intelligence but remains challenging due to tight memory, storage, and computation constraints. Existing approaches, such as model compression and hardware-aware neural architecture search (HW-NAS), often depend on proxy metrics, incur high search cost, and do not fully bridge the gap between architecture design and verified deployment. This paper presents AutoMCU, a feasibility-first large language model (LLM)-based multi-agent system for automated neural network customization under MCU constraints. Given natural-language task requirements and hardware specifications, AutoMCU iteratively generates structured architecture candidates, filters infeasible designs through vendor toolchain feedback before training, evaluates feasible models under a controlled protocol, and verifies deployability through backend-grounded deployment analysis. AutoMCU includes two key mechanisms: 1) hardware-in-the-loop architecture generation for early elimination of undeployable candidates under RAM and Flash constraints, and 2) state-isolated multi-agent scheduling for stable coordination of proposal, training, evaluation, and deployment stages. Experiments on CIFAR-10 and CIFAR-100 under strict MCU constraints show that AutoMCU achieves competitive accuracy while reducing customization time to about 1--2 hours, compared with hundreds of GPU hours for representative MCU-oriented HW-NAS baselines. Comparisons with ColabNAS and the LLM-based NAS method GENIUS on NAS-Bench-201 further demonstrate the effectiveness and stability of AutoMCU. Real-device deployments on multiple STM32 microcontrollers validate its practical applicability to MCU-scale edge intelligence.

</details>

---
