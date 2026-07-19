# cs.LG | Machine Learning | 2026-07-17

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/具身智能/BadWAM_When_World-Action_Models_Dream_Right_but_Act_Wrong|BadWAM: When World-Action Models Dream Right but Act Wrong]]

![[assets/2607.15207_figure.png|800]]

- **arXiv**: [2607.15207](https://arxiv.org/abs/2607.15207)
- **PDF**: https://arxiv.org/pdf/2607.15207
- **详细分析**: [[20_Research/Papers/具身智能/BadWAM_When_World-Action_Models_Dream_Right_but_Act_Wrong|BadWAM: When World-Action Models Dream Right but Act Wrong]]
- **作者**: Qi Li, Xingyi Yang, Xinchao Wang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Security

#### 研究背景与动机

《BadWAM: When World-Action Models Dream Right but Act Wrong》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BadWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. In this paper, we show that this assumption is fragile. We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes. BadWAM characterizes this attack surface along two natural criteria: attack strength and stealthiness. When the adversary prioritizes disruption, BadWAM instantiates an action-only adversarial attack, which directly drives the model toward task-failing actions. When the adversary additionally prioritizes stealth, BadWAM instantiates an imagination-preserving adversarial attack, which seeks to induce harmful action shifts while keeping the model's predicted future close to its clean imagination. Together, these two attacks capture a spectrum of WAM-specific failures: from overt action hijacking to stealthier cases where the model appears to imagine a plausible future but executes a desynchronized action. We evaluate BadWAM across different variants of WAMs. Results show that our attacks substantially reduce task success rates under closed-loop execution. For example, our action-only attack reduces the model performance from 96.5% to 43.1% success. The results of our imagination-preserving attack further exposes a WAM-specific vulnerability: moderate future-preserving regularization can maintain strong attack performance while reducing future imagination drift.

</details>

---

### [[20_Research/Papers/强化学习/Evaluating_covariate_balance_for_long_time_horizon_Markov_decision_processes|Evaluating covariate balance for long time horizon Markov decision processes]]

![[assets/2607.15080_first_page.png|800]]

- **arXiv**: [2607.15080](https://arxiv.org/abs/2607.15080)
- **PDF**: https://arxiv.org/pdf/2607.15080
- **详细分析**: [[20_Research/Papers/强化学习/Evaluating_covariate_balance_for_long_time_horizon_Markov_decision_processes|Evaluating covariate balance for long time horizon Markov decision processes]]
- **作者**: Joshua Spear, Rebecca Pope, Neil J Sebire
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Evaluating covariate balance for long time horizon Markov decision processes》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This article explores the application of covariate balance diagnostics for detecting the presence of hidden confounding/model miss-specification in studies applying offline reinforcement learning (RL) to deriving optimal treatment recommendations. The results demonstrate that, either there is a high risk of bias within existing offline RL studies for treatment recommendations or, existing covariate balance metrics are not sufficient to assess such studies. Regardless, existing offline RL studies cannot be concluded as being statistically robust. The conclusions propose future research directions for obtaining more methodologically robust applications of offline RL to treatment recommendation problems.

</details>

---

### [[20_Research/Papers/强化学习/A_Continuous-Time_Reinforcement_Learning_Framework_for_Fine-Tuning_Discrete_Diffusion_Models|A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models]]

![[assets/2607.14522_figure.png|800]]

- **arXiv**: [2607.14522](https://arxiv.org/abs/2607.14522)
- **PDF**: https://arxiv.org/pdf/2607.14522
- **详细分析**: [[20_Research/Papers/强化学习/A_Continuous-Time_Reinforcement_Learning_Framework_for_Fine-Tuning_Discrete_Diffusion_Models|A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models]]
- **作者**: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CTRL, HumanEval, TraceRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We formulate reinforcement learning (RL) in continuous time with discrete state spaces and possibly arbitrary action spaces via a stochastic control approach, where the state dynamics are modeled as a controlled continuous-time Markov chain (CTMC). We consider policy optimization problems and derive the corresponding policy gradient methods, leading to continuous-time variants of proximal policy optimization (PPO) and group relative policy optimization (GRPO). As a primary application, we develop a complete continuous-time RL framework for fine-tuning score-based discrete diffusion models. The proposed framework enables reward-driven optimization without requiring differentiability on the reward signals. In contrast to the existing GRPO-based approaches that only rely on terminal rewards, our formulation allows intermediate reward or advantage signals to be incorporated throughout the denoising trajectory. Importantly, when specialized to masked diffusion models (MDMs), our framework encompasses a rich class of policy parameterizations over the vocabulary simplex with analytically tractable probability ratios, providing a unified perspective on exploration and policy optimization in MDMs. For masked diffusion large language models (dLLMs), we further propose trajectory subsampling techniques to efficiently estimate computationally prohibitive trajectory likelihoods, reducing the computational cost of computing per-position probability ratios. We showcase the effectiveness of our methods on both low-dimensional entropy-regularized optimization problems and RL post-training of dLLMs on mathematical reasoning and coding tasks.

</details>

---

### [[20_Research/Papers/具身智能/Active_Real-World_Factor-Based_Evaluation_for_Generalist_Robot_Policies|Active Real-World Factor-Based Evaluation for Generalist Robot Policies]]

![[assets/2607.14439_figure.jpg|800]]

- **arXiv**: [2607.14439](https://arxiv.org/abs/2607.14439)
- **PDF**: https://arxiv.org/pdf/2607.14439
- **详细分析**: [[20_Research/Papers/具身智能/Active_Real-World_Factor-Based_Evaluation_for_Generalist_Robot_Policies|Active Real-World Factor-Based Evaluation for Generalist Robot Policies]]
- **作者**: Andrew Liao, Hanchen Cui, Karthik Desingh, Aryan Deshwal
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Active Real-World Factor-Based Evaluation for Generalist Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot manipulation policies trained on large, diverse datasets have shown remarkable promise across a wide range of tasks. However, rigorously evaluating these policies remains a fundamental challenge. Real-world performance depends on a large combinatorial space of task factors including object poses and camera viewpoints, making full, exhaustive evaluation intractable. Additionally, real hardware evaluation is slow and resource-intensive, so current practice is to use narrow test suites that can miss critical failure modes and misrepresent true deployment readiness. We propose an active evaluation framework that addresses this challenge by treating policy evaluation as a sequential experimental design problem. Our approach fits a probabilistic surrogate model over a structured space of task factors and adaptively selects evaluation configurations to maximize information gain over the policy's performance distribution, allowing for sample-efficient characterization of policy behavior across unseen conditions and a systematic identification of failure-prone regions. We conduct 2331 real-world evaluations across 3 tasks with 3 factor variations and find that our approach typically saves the evaluator at least 20-40% of trials compared to typical random testing.

</details>

---

### [[20_Research/Papers/强化学习/A_Noise-Robust_Elicit-to-Optimize_Framework_for_Distortion_Riskmetrics_via_Inverse_Reinforcement_Learning|A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning]]

![[assets/2607.14373_figure.png|800]]

- **arXiv**: [2607.14373](https://arxiv.org/abs/2607.14373)
- **PDF**: https://arxiv.org/pdf/2607.14373
- **详细分析**: [[20_Research/Papers/强化学习/A_Noise-Robust_Elicit-to-Optimize_Framework_for_Distortion_Riskmetrics_via_Inverse_Reinforcement_Learning|A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning]]
- **作者**: Yang Liu, Yuhao Liu, Yunran Wei
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRL, RSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose a noise-robust elicit-to-optimize framework that integrates inverse reinforcement learning (IRL) and reinforcement learning (RL) for eliciting agents' risk preferences and optimizing policies under a broad class of risk objectives characterized by distortion riskmetrics. On the elicitation side, we propose an adaptive Bayesian IRL method that infers agents' latent risk objectives from their noisy observed decisions, explicitly allowing agents to take stochastic and suboptimal actions. We establish the existence of a finite set of distinguishing questions that identifies the preferred distortion riskmetric within the candidate class and prove that the convergence rate of the algorithm is of order $O(\exp(-cm+O(\sqrt{m\log m})))$ under general settings, where $c&gt;0$ is a constant and $m$ denotes the number of algorithm iterations. On the optimization side, we develop a model-free RL algorithm for optimizing policies under conditional distortion riskmetrics. By representing the objective as an integral of the conditional cost quantile function with respect to the distortion function, the method unifies distortion-riskmetric objectives. We optimize diverse risk objectives by extending the Proximal Policy Optimization (PPO) algorithm with policy, value, and quantile neural networks, where the quantile network estimates the full conditional cost quantile function and enables numerical evaluation of general risk objectives. A comprehensive empirical study demonstrates the framework's elicitation accuracy and effectiveness in complex financial environments.

</details>

---

### [[20_Research/Papers/具身智能/DiMaS_Distribution_Matching_for_Steering_Vision-Language-Action_Models|DiMaS: Distribution Matching for Steering Vision-Language-Action Models]]

![[assets/2607.14280_first_page.png|800]]

- **arXiv**: [2607.14280](https://arxiv.org/abs/2607.14280)
- **PDF**: https://arxiv.org/pdf/2607.14280
- **详细分析**: [[20_Research/Papers/具身智能/DiMaS_Distribution_Matching_for_Steering_Vision-Language-Action_Models|DiMaS: Distribution Matching for Steering Vision-Language-Action Models]]
- **作者**: Pegah Khayatan, Sara Meziane, Jayneel Parekh, Matthieu Cord
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《DiMaS: Distribution Matching for Steering Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations. Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs. We propose DiMaS, a Distribution-Matching Steering strategy tailored to flow-matching VLAs, which transports between representation distributions rather than shifting along a fixed direction, and show that it effectively controls behavior across two state-of-the-art VLAs. We further examine the generalizability of this strategy as the tasks it is learned from and evaluated on grow increasingly dissimilar, characterizing where behavioral control transfers and where it weakens. Finally, through an analysis of the representation structure of the action expert, we explain why classical linear steering falls short in the visuomotor setting: behavioral features are linearly decodable but not linearly steerable, which motivates the distribution-matching design of DiMaS. Our code is publicly available at https://github.com/pegah-kh/dimas, with additional results and videos at https://pegah-kh.github.io/dimas/

</details>

---
