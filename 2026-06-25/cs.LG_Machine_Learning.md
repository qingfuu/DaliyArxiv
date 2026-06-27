# cs.LG | Machine Learning | 2026-06-25

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/具身智能/ROAD-VLA_Robust_Online_Adaptation_via_Self-Distillation_for_Vision-Language-Action_Models|ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models]]

![[assets/2606.25800_figure.png|800]]

- **arXiv**: [2606.25800](https://arxiv.org/abs/2606.25800)
- **PDF**: https://arxiv.org/pdf/2606.25800
- **详细分析**: [[20_Research/Papers/具身智能/ROAD-VLA_Robust_Online_Adaptation_via_Self-Distillation_for_Vision-Language-Action_Models|ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models]]
- **作者**: Kejing Wang, Toan Nguyen, Minh Hoang Nguyen, Simon Khan, Flora D. Salim
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, ROAD-VLA, ROADVLA, RobustVLA, TT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective online adaptation of vision-language-action (VLA) models remains challenging, as sparse rewards provide weak supervision for high-dimensional autoregressive action policies. Although self-distillation can in principle provide denser training signals, we find that text-based privileged teachers conditioned on demonstrations, retrieved experiences, or high-level plans are ineffective for VLA adaptation, exposing a modality gap between symbolic guidance and low-level robot actions. We propose ROAD-VLA, an advantage-guided self-distillation framework that constructs a proximal teacher directly in action space by perturbing action-token logits with calibrated advantage estimates. This converts sparse rewards into dense token-level supervision while keeping the teacher close to the current policy. We further derive a policy-improvement lower bound under calibrated advantages and accurate teacher matching. Across seven robotic manipulation environments with in-distribution and out-of-distribution shifts, ROADVLA outperforms PPO in nearly all settings, demonstrating robust online VLA adaptation.

</details>

---

### [[20_Research/Papers/强化学习/Memory-Efficient_Policy_Libraries_with_Low-Rank_Adaptation_in_Reinforcement_Learning|Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning]]

![[assets/2606.25700_figure.png|800]]

- **arXiv**: [2606.25700](https://arxiv.org/abs/2606.25700)
- **PDF**: https://arxiv.org/pdf/2606.25700
- **详细分析**: [[20_Research/Papers/强化学习/Memory-Efficient_Policy_Libraries_with_Low-Rank_Adaptation_in_Reinforcement_Learning|Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning]]
- **作者**: Samuel Valland Lyngset, Tor Viljen Raanaas, Gard Sveipe, Eirik Møller Nilsen, Jim Torresen, Kai Olav Ellefsen, Tobias Lømo
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 1.16，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Memory-Efficient Policy Libraries with Low-Rank Adaptation in Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When fine-tuning Large Language Models (LLMs), there has been success in minimizing both memory usage and computation with Parameter-Efficient Fine-Tuning (PEFT), like Low Rank Adaptation (LoRA). In this article, we have explored whether this approach is transferable to the world of robotics and Reinforcement Learning (RL), allowing learning with reduced memory usage and improved computational performance. Specifically, we focused on a version of multi-task robotics, where a library of specialist policies are created. In such a library memory efficiency is especially important. We used a Proximal Policy Optimization (PPO) algorithm and fine-tuned a baseline model to different tasks using LoRA. Our results demonstrate that, depending on the hyperparameters, LoRA can minimize memory usage by a factor of 20-160 compared to full fine-tuning of all layers. This implies a 90-95% storage saving when deploying a library of many (10-50) specialized policies, which can be the differentiating factor between being able to store the entire library in memory or having to use swap-memory in an applied robotics setting. At the same time, our results indicate that there is no significant difference in the success-rate between full fine-tuning and LoRA fine-tuning for the selected tasks.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_One-Size-Fits-All_Diagnosis-Driven_Online_Reinforcement_Learning_with_Offline_Priors|Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors]]

![[assets/2606.25527_figure.png|800]]

- **arXiv**: [2606.25527](https://arxiv.org/abs/2606.25527)
- **PDF**: https://arxiv.org/pdf/2606.25527
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_One-Size-Fits-All_Diagnosis-Driven_Online_Reinforcement_Learning_with_Offline_Priors|Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors]]
- **作者**: Guozheng Ma, Lu Li, Zilin Wang, Pierre-Luc Bacon, Dacheng Tao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型, 具身智能
- **相关性评分**: 1.92（加权：具身智能 0.3，大模型 0.3，强化学习 0.96，世界模型 0.36）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Beyond One-Size-Fits-All: Diagnosis-Driven Online Reinforcement Learning with Offline Priors》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online reinforcement learning (RL) agents increasingly depend on knowledge acquired offline to achieve practical efficiency. Originally studied in offline-to-online RL, this paradigm now spans foundation model post-training and embodied intelligence, with prior types expanding from offline datasets and pre-trained policies to increasingly diverse knowledge sources such as multimodal foundation models and generative world models. Offline priors have become central to how deep RL is developed and deployed. However, this reliance introduces a challenge that the prevailing benchmark-driven paradigm cannot resolve: because prior validity varies across deployments and shifts during training, no single approach to managing it is universally optimal, and benchmark rankings offer limited guidance for real-world deployments. Rather than pursuing universal solutions, we argue that the field should shift to diagnosis-driven tension management, in which deployment-specific evidence guides how the learner relates to its priors throughout training, enabling both flexible and adaptive deployment. We support this position with a framework characterizing how priors reshape online optimization through three functional roles, controlled experiments demonstrating help-or-hurt reversals, cross-domain evidence from foundation model post-training to embodied intelligence, and engagement with five substantive counterarguments.

</details>

---

### [[20_Research/Papers/强化学习/Low_Variance_Trust_Region_Optimization_with_Independent_Actors_and_Sequential_Updates_in_Cooperative_Multi-agent_Reinforcement_Learning|Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-agent Reinforcement Learning]]

![[assets/2606.25526_figure.png|800]]

- **arXiv**: [2606.25526](https://arxiv.org/abs/2606.25526)
- **PDF**: https://arxiv.org/pdf/2606.25526
- **详细分析**: [[20_Research/Papers/强化学习/Low_Variance_Trust_Region_Optimization_with_Independent_Actors_and_Sequential_Updates_in_Cooperative_Multi-agent_Reinforcement_Learning|Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-agent Reinforcement Learning]]
- **作者**: Bang Giang Le, Viet Cuong Ta
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Low-Variance-Trust-Region-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent reinforcement learning assumes each agent shares the same reward function and can be trained effectively using the Trust Region framework of single-agent. Instead of relying on other agents' actions, the independent actors setting considers each agent to act based only on its local information, thus having more flexible applications. However, in the sequential update framework, it is required to re-estimate the joint advantage function after each individual agent's policy step. Despite the practical success of importance sampling, the updated advantage function suffers from exponentially high variance problems, which likely result in unstable convergence. In this work, we first analyze the high variance advantage both empirically and theoretically. To overcome this limitation, we introduce a clipping objective to control the upper bounds of the advantage fluctuation in sequential updates. With the proposed objective, we provide a monotonic bound with sub-linear convergence to $ε$-Nash Equilibria. We further derive two new practical algorithms using our clipping objective. The experiment results on three popular multi-agent reinforcement learning benchmarks show that our proposed method outperforms the tested baselines in most environments. By carefully analyzing different training settings, our proposed method is highlighted with both stable convergence properties and the desired low advantage variance estimation. For reproducibility purposes, our source code is publicly available at https://github.com/giangbang/Low-Variance-Trust-Region-MARL.

</details>

---

### [[20_Research/Papers/强化学习/Stagnant_Neuron_Towards_Understanding_the_Plasticity_Loss_in_Multi-Agent_Reinforcement_Learning_Value_Factorization_Methods|Stagnant Neuron: Towards Understanding the Plasticity Loss in Multi-Agent Reinforcement Learning Value Factorization Methods]]

![[assets/2606.25335_figure.png|800]]

- **arXiv**: [2606.25335](https://arxiv.org/abs/2606.25335)
- **PDF**: https://arxiv.org/pdf/2606.25335
- **详细分析**: [[20_Research/Papers/强化学习/Stagnant_Neuron_Towards_Understanding_the_Plasticity_Loss_in_Multi-Agent_Reinforcement_Learning_Value_Factorization_Methods|Stagnant Neuron: Towards Understanding the Plasticity Loss in Multi-Agent Reinforcement Learning Value Factorization Methods]]
- **作者**: Zhengzhu Liu, Zeming Gao, Haoyuan Qin, Jiawei Hu, Junhao Wu, Miao Zhu, Haipeng Zhang, Chennan Ma, Siqi Shen, Cheng Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Stagnant Neuron: Towards Understanding the Plasticity Loss in Multi-Agent Reinforcement Learning Value Factorization Methods》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Agent Reinforcement Learning (MARL) value factorization methods can suffer from a loss of plasticity, gradually failing to adapt when transferring to new task instances. We trace this issue to stagnant neurons, units whose gradient updates become negligibly small relative to their weights, thereby hindering learning. While existing plasticity injection methods exist, they prove ineffective for such neurons. To address this, we propose Knowledge-retentive Neuron-level PlastIcity Focusing InjEction (KNIFE), a novel method that directly targets stagnant neurons. KNIFE replaces each stagnant neuron with a composite unit comprising three specialized components: a frozen knowledge neuron to preserve acquired knowledge, a re-initialized active neuron to restore learning capacity, and a compensation neuron to ensure the combined output matches the original, thus maintaining previous learned cooperation knowledge. Extensive experiments on SMACv2, predator-prey, and matrix games demonstrate that KNIFE significantly outperforms state-of-the-art plasticity injection methods.

</details>

---

### [[20_Research/Papers/强化学习/Inverse_Reinforcement_Learning_for_Interpretable_Keystroke_Biomarkers_in_Parkinson's_Disease|Inverse Reinforcement Learning for Interpretable Keystroke Biomarkers in Parkinson's Disease]]

![[assets/2606.25270_figure.png|800]]

- **arXiv**: [2606.25270](https://arxiv.org/abs/2606.25270)
- **PDF**: https://arxiv.org/pdf/2606.25270
- **详细分析**: [[20_Research/Papers/强化学习/Inverse_Reinforcement_Learning_for_Interpretable_Keystroke_Biomarkers_in_Parkinson's_Disease|Inverse Reinforcement Learning for Interpretable Keystroke Biomarkers in Parkinson's Disease]]
- **作者**: Navin Bondade
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Inverse Reinforcement Learning for Interpretable Keystroke Biomarkers in Parkinson's Disease》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRL, PhysioNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Keystroke dynamics have been explored extensively as a passive digital biomarker for Parkinson's disease (PD), typically by extracting summary statistics from typing timing and training a classifier to discriminate PD from healthy controls. We instead apply inverse reinforcement learning (IRL) to keystroke data, modeling each keystroke as a discrete choice over typing speed and recovering, per subject, an interpretable reward function that explains their observed timing behavior. To our knowledge this is the first application of IRL to keystroke dynamics. On the public neuroQWERTY MIT-CSXPD dataset (85 subjects, 42 with PD), an initial four-parameter reward decomposition (speed, effort, smoothness, hand-alternation cost) was found to suffer severe feature collinearity between two terms ($r=1.000$ in typical contexts); we diagnose and correct this, yielding an identifiable three-parameter model. The recovered speed-preference weight correlates with UPDRS-III severity at $r=-0.607$ ($p&lt;0.001$, $n=42$), replicates independently across two sub-cohorts, is stable across nine sensitivity configurations, and retains a statistically significant contribution beyond raw typing speed alone (incremental $R^2$ from 0.194 to 0.338, $p=0.006$). Two other recovered weights (consistency, hand-alternation) did not survive confound checks and are reported as negative results. We document two implementation bugs found during adversarial code review (session-boundary contamination, a rolling-window data leakage) and show the headline result is materially unchanged after fixing both. We discuss this result in the context of a literature where reported accuracies vary widely between studies (pooled AUC 0.85, I^2=94% in a 2022 meta-analysis), and argue that the validation process itself, not only the correlation coefficient, is part of the contribution.

</details>

---

### [[20_Research/Papers/大模型/Forget_to_Improve_On-Device_LLM-Agent_Continual_Learning_via_Budget-Curated_Memory|Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory]]

![[assets/2606.25115_figure.png|800]]

- **arXiv**: [2606.25115](https://arxiv.org/abs/2606.25115)
- **PDF**: https://arxiv.org/pdf/2606.25115
- **详细分析**: [[20_Research/Papers/大模型/Forget_to_Improve_On-Device_LLM-Agent_Continual_Learning_via_Budget-Curated_Memory|Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory]]
- **作者**: Beining Wu, Zihao Ding, Jun Huang, Yanxiao Zhao
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.0（加权：大模型 0.8，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory》归入 大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-device language-model agents improve by accumulating experience in retrieved memory rather than by updating weights. This memory is hard-bounded and exposed: it consumes RAM and energy, reaches peers through a thin uplink, and becomes an attack surface because it is writable by what the agent reads. Existing systems each cover one part of this problem: agentic memories grow without a budget, on-device methods keep entries by success alone, and poisoning is studied mainly as an attack rather than as a memory-governance problem. We propose \sys{}, a single net-value-per-byte score that governs an agent's experience-memory lifecycle. The main idea is to let the budget act as the curator: each entry is scored as value minus harm, per byte, so one ruler decides what to keep, share, and trust. \sys{} makes three decisions: (1) \textbf{KEEP} evicts low-value bytes under the RAM and energy budget; (2) \textbf{SHARE} sends an insight only when its value exceeds its uplink cost; and (3) \textbf{TRUST} gates a peer entry by provenance. On language-model-agent task-drift benchmarks and a real heterogeneous Jetson testbed with two robot-arm nodes and a hub, \sys{} reduces memory by $2.7\times$ and uplink by $2.4\times$, drives injection success from 0.75 to zero, and raises accuracy on cases corrupted by poison or stale memory. Curating by net value reduces footprint, energy, uplink, and injection success together without reducing accuracy. In this setting, forgetting by net value improves the agent rather than weakening it.

</details>

---

### [[20_Research/Papers/强化学习/Bias-Controlled_Primal-Dual_Natural_Actor-Critic_Optimal_Rates_for_Constrained_Multi-Objective_Average-Reward_RL|Bias-Controlled Primal-Dual Natural Actor-Critic: Optimal Rates for Constrained Multi-Objective Average-Reward RL]]

![[assets/2606.25012_first_page.png|800]]

- **arXiv**: [2606.25012](https://arxiv.org/abs/2606.25012)
- **PDF**: https://arxiv.org/pdf/2606.25012
- **详细分析**: [[20_Research/Papers/强化学习/Bias-Controlled_Primal-Dual_Natural_Actor-Critic_Optimal_Rates_for_Constrained_Multi-Objective_Average-Reward_RL|Bias-Controlled Primal-Dual Natural Actor-Critic: Optimal Rates for Constrained Multi-Objective Average-Reward RL]]
- **作者**: Ankur Naskar, Swetha Ganesh, Vaneet Aggarwal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Bias-Controlled Primal-Dual Natural Actor-Critic: Optimal Rates for Constrained Multi-Objective Average-Reward RL》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many reinforcement learning (RL) problems in the infinite-horizon average-reward setting require optimizing multiple conflicting objectives while satisfying multiple safety constraints. A common approach is concave scalarization, where the agent maximizes a utility $ f(J^π_{r_1}, \ldots, J^π_{r_M}) $ subject to a scalarized constraint $ g(J^π_{c_1}, \ldots, J^π_{c_N}) \ge 0 $, where $J^π_{r_m}$ and $J^π_{c_n}$ denote the average-reward and cost under policy $π$. However, the nonlinearity of $f$ and $g$ introduces bias in policy-gradient and actor-critic methods, since gradients must be evaluated using noisy estimates of $J^π,$ and $ \mathbb{E}[\partial f(J^π)] \neq \partial f(\mathbb{E}[J^π]),$ and this bias propagates through both primal and dual updates. We propose an MLMC-based primal-dual Natural Actor-Critic algorithm for average-reward MDPs that controls bias in scalarized objectives, constraint evaluation, and actor-critic estimation without requiring mixing-time knowledge. We show that the algorithm achieves optimal global convergence and constraint-violation rates of $ \tilde{O}(1/\sqrt{T}) $. To our knowledge, this is the first result establishing optimal convergence for concave scalarized multi-objective RL in the average-reward setting, both with and without constraints, and the first to do so without mixing-time information even in the absence of scalarization.

</details>

---

### [[20_Research/Papers/强化学习/Solving_Markov_Decision_Processes_with_Future_Information_via_MPC|Solving Markov Decision Processes with Future Information via MPC]]

![[assets/2606.24991_figure.png|800]]

- **arXiv**: [2606.24991](https://arxiv.org/abs/2606.24991)
- **PDF**: https://arxiv.org/pdf/2606.24991
- **详细分析**: [[20_Research/Papers/强化学习/Solving_Markov_Decision_Processes_with_Future_Information_via_MPC|Solving Markov Decision Processes with Future Information via MPC]]
- **作者**: Shambhuraj Sawant, Akhil S Anand, Dirk Reinhardt, Sebastien Gros
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.56，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Solving Markov Decision Processes with Future Information via MPC》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MPC-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model Predictive Control (MPC) is widely used in industrial and robotic systems for enforcing constraints and embedding domain knowledge through finite-horizon optimization-based planning. However, despite these strengths, an MPC scheme typically does not yield optimal policies for sequential decision-making problems formulated as Markov Decision Processes (MDPs). Recent combinations of MPC with Reinforcement Learning (RL) alleviate this issue by treating MPC as a parameterized model of the optimal policy of an MDP and adjusting its parameters using data. While these approaches typically consider classical MDPs, many real-world problems include future information--such as forecasts, prices, or reference trajectories--at decision time, which must be included in the MDP state for optimal decision-making. Current MPC-RL approaches do not directly account for this augmented-state structure, raising the question of how to incorporate future information into MPC to obtain an optimal policy. This work establishes the structural requirements under which a parameterized MPC can exactly represent the optimal value functions and policy of an MDP with future information. We further demonstrate that such a parameterized MPC can serve as a structured function approximator, with its parameters learned using RL. The approach is illustrated on a point-mass racing task with future reference information.

</details>

---

### [[20_Research/Papers/强化学习/CKM-Driven_Communication-Aware_UAV_Intelligent_Trajectory_Optimization_for_Urban_Inspection|CKM-Driven Communication-Aware UAV Intelligent Trajectory Optimization for Urban Inspection]]

![[assets/2606.24979_figure.png|800]]

- **arXiv**: [2606.24979](https://arxiv.org/abs/2606.24979)
- **PDF**: https://arxiv.org/pdf/2606.24979
- **详细分析**: [[20_Research/Papers/强化学习/CKM-Driven_Communication-Aware_UAV_Intelligent_Trajectory_Optimization_for_Urban_Inspection|CKM-Driven Communication-Aware UAV Intelligent Trajectory Optimization for Urban Inspection]]
- **作者**: Yang Xiaomeng, Jia Ziye, Zhu Qiuming, Wu Qihui
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 0.36，世界模型 0.16，机器人 1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《CKM-Driven Communication-Aware UAV Intelligent Trajectory Optimization for Urban Inspection》归入 机器人、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicles (UAVs) are increasingly employed in urban inspection tasks, where reliable communication is critical but challenging due to the severe spatial channel heterogeneity. To address the issue, in this paper, we focus on the communication-aware path planning for multi-UAV tasks, and propose a channel knowledge map (CKM)-driven trajectory planning framework which integrates the channel modeling and trajectory decision-making. Specifically, we apply the diffusion model to construct a time-accumulated CKM and achieve the accurate perception with low flight overhead, which leverages the sparse observation data to reconstruct the high-fidelity global channel quality distribution. Based on the CKM, we propose a global-to-local graph attention network soft actor-critic algorithm. The graph attention network optimizes the complex combinatorial node ordering problem, generating an optimal and communication-aware sequence for the inspection targets. Subsequently, the soft actor-critic algorithm performs continuous action control to ensure the smoothness of the flight path and dynamically avoid communication attenuation areas. Simulation results demonstrate that the proposed method effectively guides UAVs through high-quality channel regions without dependence on real-time channel feedback, significantly improving both the trajectory efficiency and communication reliability.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Scalable_Multi-Task_Reinforcement_Learning_with_Large_Decision_Models|Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models]]

![[assets/2606.24962_figure.png|800]]

- **arXiv**: [2606.24962](https://arxiv.org/abs/2606.24962)
- **PDF**: https://arxiv.org/pdf/2606.24962
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Scalable_Multi-Task_Reinforcement_Learning_with_Large_Decision_Models|Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models]]
- **作者**: Thibaut Kulak
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress in large-scale sequence modeling has shown that a single model can learn useful representations across highly diverse data distributions. Inspired by these advances, we investigate whether a unified transformer policy can be trained across large collections of heterogeneous reinforcement learning environments. We introduce LDM-v0, a Large Decision Model trained offline on trajectories collected from thousands of environments spanning multiple domains and modalities. LDM-v0 is a multi-task, multi-modal transformer policy conditioned on histories of observations, actions, rewards, and termination signals, and trained through supervised next-action prediction over offline trajectories. We describe the environment infrastructure, automated data generation pipeline, model architecture, and training methodology used to build LDM-v0, and evaluate its performance across diverse environments. We show that a single pretrained model matches the performance of independently trained task-specific reference policies on approximately 1,000 environments including robotics, autonomous driving, inventory management, cybersecurity, trading, and video games. These results demonstrate the feasibility of large-scale offline pretraining across heterogeneous reinforcement learning environments using a single transformer policy.

</details>

---

### [[20_Research/Papers/具身智能/Swarm-Inspired_Generation_of_Collective_Behaviors_in_Graph_Dynamical_Systems|Swarm-Inspired Generation of Collective Behaviors in Graph Dynamical Systems]]

![[assets/2606.24958_figure.png|800]]

- **arXiv**: [2606.24958](https://arxiv.org/abs/2606.24958)
- **PDF**: https://arxiv.org/pdf/2606.24958
- **详细分析**: [[20_Research/Papers/具身智能/Swarm-Inspired_Generation_of_Collective_Behaviors_in_Graph_Dynamical_Systems|Swarm-Inspired Generation of Collective Behaviors in Graph Dynamical Systems]]
- **作者**: Ji Chen, Song Chen, Chengzhang Gong, Li Fan, Chao Xu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Swarm-Inspired Generation of Collective Behaviors in Graph Dynamical Systems》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Hamilton2017InductiveRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collective behavior arises when locally interacting units produce coordinated global organization, from synchronization in dynamical systems to task-relevant information flow on graphs. The central challenge is not only to explain how collective behavior emerges, but to design local interaction rules that can produce desired global organization and generalize across graphs, dynamics and tasks.To address this challenge, we introduce the Swarm-Inspired Emergent Synchronizer (SIES), a graph-dynamical framework that learns generalizable local-interaction laws for controllable collective organization. Each node is an agent-like dynamical unit with a state and task cue, and signed source-target-conditioned attention acts as an adaptive coupling term inside an explicit evolution model. Therefore, SIES combines an explicit dynamical engine with local agent intelligence, similar to biological swarms. For synchronization control, SIES learns a generalizable coupling operator that produces prescribed synchronization patterns for CDSs across untrained network scales, target phase relations, and intrinsic node dynamics without retraining. The learned operator also reaches gait-related modes faster than three oscillator baselines and generalizes synchronization-driven locomotion to simulated multi-legged robots of different scales and a physical hexapod after leg disablement. For graph representation learning, SIES applies the same signed interaction principle to message passing and achieves the highest performance among the compared methods on heterophilous node-classification benchmarks. Together, these results position SIES as a generalizable and learnable graph-dynamical interaction framework with promise for synchronization control, adaptive robot coordination, and heterophilous graph representation learning.

</details>

---

### [[20_Research/Papers/强化学习/Supervised_Reinforcement_Learning_for_the_Coordination_of_Distributed_Energy_Resources|Supervised Reinforcement Learning for the Coordination of Distributed Energy Resources]]

![[assets/2606.24947_figure.png|800]]

- **arXiv**: [2606.24947](https://arxiv.org/abs/2606.24947)
- **PDF**: https://arxiv.org/pdf/2606.24947
- **详细分析**: [[20_Research/Papers/强化学习/Supervised_Reinforcement_Learning_for_the_Coordination_of_Distributed_Energy_Resources|Supervised Reinforcement Learning for the Coordination of Distributed Energy Resources]]
- **作者**: Haoyuan Deng, Yihong Zhou, Thomas Morstyn, Yi Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Supervised Reinforcement Learning for the Coordination of Distributed Energy Resources》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The increasing integration of distributed energy resources (DERs) is crucial for power system decarbonization, yet unlocking DERs' flexibility is challenged by their inherent uncertainties and modelling complexity. As traditional optimization methods struggle with such uncertainty and complexity of DERs, reinforcement learning (RL) has emerged as a promising alternative for DER management. However, standard RL methods suffer from sample inefficiency and sub-optimality when trained from scratch. Inspired by the training paradigms in large language models, this paper proposes a Supervised Reinforcement Learning (SRL) framework for learning DER coordination policies. This framework first pre-trains a policy on demonstration data in a supervised-learning fashion, which is then further fine-tuned using RL. Furthermore, we propose a two-step fine-tuning process: offline fine-tuning for enhancing policy performance and online fine-tuning for adapting it to the real-world dynamics. Experiments demonstrate that RL implementations based on the proposed framework significantly outperform all benchmarks, achieving high cost efficiency even under low-quality demonstration data.

</details>

---

### [[20_Research/Papers/世界模型/Conformal_Orbit-Valid_Trust_Horizons_for_Equivariant_World_Models|Conformal Orbit-Valid Trust Horizons for Equivariant World Models]]

![[assets/2606.24946_figure.png|800]]

- **arXiv**: [2606.24946](https://arxiv.org/abs/2606.24946)
- **PDF**: https://arxiv.org/pdf/2606.24946
- **详细分析**: [[20_Research/Papers/世界模型/Conformal_Orbit-Valid_Trust_Horizons_for_Equivariant_World_Models|Conformal Orbit-Valid Trust Horizons for Equivariant World Models]]
- **作者**: Hongbo Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Conformal Orbit-Valid Trust Horizons for Equivariant World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned world models are useful only over horizons on which their rollout error remains controlled. We study trust-horizon certification for latent world models with known group symmetries. Given a one-step latent residual and a finite-time expansion estimate, we form a raw horizon curve and calibrate it with a split-conformal multiplicative factor. On the reproducible audit set, the conformal factor is $γ_α=1.0$: the raw certificate is already conservative under the audit protocol. Across 50 stable audits, we observe zero anti-conservative violations, corresponding to an exact-binomial 95% upper bound of 5.8% on the violation rate. Our main structural result is that exact equivariance transports a calibrated trust-horizon curve over the group orbit: when the environment dynamics, encoder, predictor, action transform, and latent metric satisfy the stated equivariance/invariance conditions, rollout errors and trust horizons are orbit-constant. Empirically, the implemented models exhibit small orbit-transport residuals, with median 1.1% and maximum 4.1% over 14 orbit audits. The certificate is also non-vacuous (median certified-to-measured horizon ratio 0.67). A certificate-level calibration-cost study shows two complementary regimes. On a symmetric 2D substrate, equivariant, plain, and augmented models are all orbit-valid from a single calibration sector -- no separation, because the substrate already makes non-equivariant baselines approximately orbit-robust. A 3D yaw audit shows the other regime: the equivariant model obtains a one-sector safe and non-vacuous orbit-valid certificate, while healthy non-equivariant baselines pay violation, slack, sharpness, or additional-sector cost. The certificate is a conservative, distributional audit rather than a global reachability guarantee, and certificate-guided subgoal spacing is not confirmed in the current 3D CEM-MPC behavior layer.

</details>

---

### [[20_Research/Papers/世界模型/When_Do_Conservation_Laws_Survive_Learned_Representations_Certified_Horizons_for_Latent_World_Models|When Do Conservation Laws Survive Learned Representations? Certified Horizons for Latent World Models]]

![[assets/2606.24945_figure.png|800]]

- **arXiv**: [2606.24945](https://arxiv.org/abs/2606.24945)
- **PDF**: https://arxiv.org/pdf/2606.24945
- **详细分析**: [[20_Research/Papers/世界模型/When_Do_Conservation_Laws_Survive_Learned_Representations_Certified_Horizons_for_Latent_World_Models|When Do Conservation Laws Survive Learned Representations? Certified Horizons for Latent World Models]]
- **作者**: Hongbo Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: cs.LG

#### 研究背景与动机

《When Do Conservation Laws Survive Learned Representations? Certified Horizons for Latent World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We ask a representation-learning question about physical world models: when does a conservation law remain certifiable after a model learns a latent representation? A certified horizon bounds -- in advance, from measurable model defects -- how many steps a rollout provably stays on a physical invariant's level set. The key design choice is what is certified: not a learned latent Hamiltonian or a learned scalar witness (a model can conserve either while drifting in true energy), but the decoded physical invariant obtained by decoding the latent state and evaluating the known invariant. Around this object we derive shell-horizon certificates whose budget decomposes into representation, readout, and latent-dynamics defects, with a monotone alignment bridge through which a soft learned witness yields a certified horizon for the decoded invariant, and test them across state, learned-lift, and pixel observations on conservative systems. Conservation certificates can survive learned representation, but not all geometric priors survive equally: hard canonical symplectic structure yields the longest horizons in known phase coordinates yet does not cross a learned chart, whereas a controlled-Lipschitz-aligned soft invariant survives in the learned-representation settings we test; pixel certification is recovered on a readout-stable sub-tube; and the Kepler problem exposes a geometric boundary. The central object is therefore not a latent Hamiltonian, but a decoded physical invariant whose robustness to representation learning can be measured, certified, and falsified.

</details>

---

### [[20_Research/Papers/强化学习/TurboMPC_Fast,_Scalable,_and_Differentiable_Model_Predictive_Control_on_the_GPU|TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU]]

![[assets/2606.24039_figure.png|800]]

- **arXiv**: [2606.24039](https://arxiv.org/abs/2606.24039)
- **PDF**: https://arxiv.org/pdf/2606.24039
- **详细分析**: [[20_Research/Papers/强化学习/TurboMPC_Fast,_Scalable,_and_Differentiable_Model_Predictive_Control_on_the_GPU|TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU]]
- **作者**: Gabriel Bravo-Palacios, Jianghan Zhang, Zachary Pestrikov, Brian Plancher, Thomas Lew
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU》归入 机器人、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics increasingly relies on GPUs for parallel simulation, large-scale learning, and neural-network inference. For model predictive control (MPC) to scale with this paradigm, solvers must run efficiently on this hardware while remaining fast, differentiable, and compatible with expressive MPC formulations used in robotics. We present TurboMPC, a differentiable MPC solver that runs entirely on the GPU and supports state and control inequality constraints, implicit integrators, cross-time-coupled costs, and slack variables. TurboMPC combines sequential quadratic programming (SQP), an alternating direction method of multipliers (ADMM) inner solver, implicit differentiation, and a co-designed JAX-CUDA implementation for efficiency and ease of use. In simulation, we validate TurboMPC on constrained planning, humanoid imitation learning, and reinforcement learning with neural-network cost function tasks, achieving up to $15\times$ and $58\times$ speedups over state-of-the-art CPU and GPU differentiable solvers, respectively. We deploy TurboMPC on a full-scale car for minimum-time racing and find that batched, GPU-accelerated tuning of MPC parameters via Bayesian optimization yields significantly faster driving than a hand-tuned baseline. TurboMPC also scales to planning horizons of over $8000$ knot points while maintaining control of the vehicle. We open-source TurboMPC at: https://github.com/ToyotaResearchInstitute/turbompc

</details>

---
