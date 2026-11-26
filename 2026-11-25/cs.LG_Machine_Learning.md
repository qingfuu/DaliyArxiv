# cs.LG | Machine Learning | 2026-11-25

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Exploratory_Midtraining_for_Robot_Policies|Exploratory Midtraining for Robot Policies]]

![[assets/2611.33130_figure.png|800]]

- **arXiv**: [2611.33130](https://arxiv.org/abs/2611.33130)
- **PDF**: https://arxiv.org/pdf/2611.33130
- **详细分析**: [[20_Research/Papers/强化学习/Exploratory_Midtraining_for_Robot_Policies|Exploratory Midtraining for Robot Policies]]
- **作者**: Kshitiz, Zheyuan Hu, Robyn Wu, Yizhou Li, Yunchu Zhang, Vattanary Tevy, Kavya Tayal, Shawn Yin, Aykut Onol, Kushal Arora, Dhruv Shah, Abhishek Gupta...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Exploratory Midtraining for Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies predominantly learn from human-collected data emphasizing competent behavior, limiting coverage of the low-level behaviors needed to support autonomous improvement. We study how a form of midtraining can be used to build coverage over diverse low-level behaviors that connect challenging states of the robot and its environment to states from which further progress is possible ("connected behavioral coverage"). We also examine how this coverage supports downstream adaptation and online improvement. To this end, we introduce $β$-Data, a dataset collected via adversarial teleoperation, where a human adversary reversibly perturbs the environment while a human operator continues toward completion without resetting. We relabel trajectory segments with local outcomes in natural language and finetune a pretrained policy conditioned on recent action history. The resulting policy exhibits sustained use of more low-level behaviors. Across manipulation tasks in simulation and on three real-robot platforms, our approach yields more favorable data scaling laws, better zero-shot generalization, and more effective use of additional rollout time than training on standard demonstrations. During online finetuning, these policies need fewer rollouts to collect successful experience and reach higher success rates, suggesting that midtraining can prepare robots for both more robust task execution and continued autonomous improvement. Our project page and robot videos are available at https://kshitiz-1225.github.io/exploratory-midtraining-robot-policies/.

</details>

---

### [[20_Research/Papers/强化学习/Breaking_the_Joint_Action_Space_Dependence_in_Distributionally_Robust_Multi-Agent_Reinforcement_Learning|Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning]]

![[assets/2611.32812_first_page.png|800]]

- **arXiv**: [2611.32812](https://arxiv.org/abs/2611.32812)
- **PDF**: https://arxiv.org/pdf/2611.32812
- **详细分析**: [[20_Research/Papers/强化学习/Breaking_the_Joint_Action_Space_Dependence_in_Distributionally_Robust_Multi-Agent_Reinforcement_Learning|Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning]]
- **作者**: Yue Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.3，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Breaking the Joint Action Space Dependence in Distributionally Robust Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Q-FTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the sample complexity of learning robust coarse correlated equilibria (CCE) in finite-horizon, general-sum, distributionally robust Markov games with known rewards and a generative model of the nominal transitions. Each player evaluates a policy by its worst-case return over total-variation (TV) balls centered at the nominal transition distribution of every stage, state, and joint action; this is the standard $(s,a)$-rectangular uncertainty set. Existing generative-model guarantees for this model scale with the number $\prod_iA_i$ of joint actions, where $A_i$ is the number of actions of player~$i$. Since this number grows exponentially with the number of players, these guarantees suffer from the curse of multiagency. We design an algorithm whose sample complexity depends on the action sets only through the largest individual action-set size $A_*:=\max_iA_i$. The algorithm uses $\widetilde O(SA_*H^5D^4/\varepsilon^4)$ transition samples and, with probability at least $1-δ$, returns a Markov policy that is an $\varepsilon$-robust CCE from every initial state. Here $S$ is the number of states, $H$ is the horizon, and $D:=\max_i\min\{H,1/ρ_i\}$, where $ρ_i$ is the TV radius of player~$i$. Two ingredients make this possible: a plug-in estimate of the robust backup whose mean error does not depend on the number of states, and a single batch of samples per round that serves as bandit feedback for all players at once. The result shows that the dependence on $\prod_iA_i$ can be avoided without modifying the $(s,a)$-rectangular uncertainty set.

</details>

---

### [[20_Research/Papers/具身智能/CriticJEPA_World_Models_Are_Better_Critics_Than_Optimizers|CriticJEPA: World Models Are Better Critics Than Optimizers]]

![[assets/2611.32357_first_page.png|800]]

- **arXiv**: [2611.32357](https://arxiv.org/abs/2611.32357)
- **PDF**: https://arxiv.org/pdf/2611.32357
- **详细分析**: [[20_Research/Papers/具身智能/CriticJEPA_World_Models_Are_Better_Critics_Than_Optimizers|CriticJEPA: World Models Are Better Critics Than Optimizers]]
- **作者**: Xvyuan Liu, Jianjie Fang, Honglin Zhang, Zhaolu Wang, Xin Zhang, Wei Wu, Fengli Xu, Chen Gao, Yong Li
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CriticJEPA: World Models Are Better Critics Than Optimizers》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models enable goal-directed planning by predicting action outcomes. Gradient-based planners optimize actions to lower predicted goal cost, but continued optimization can exploit prediction errors after execution stops improving. Comparing plans requires informative relative scores; improving them also requires reliable update directions. Exact-state execution reveals that a frozen hierarchical world model ranks goal-conditioned proposals even when its rankings among outputs of prolonged gradient search are uninformative. Effective planning pairs goal-directed candidates with predictions that distinguish their outcomes. We introduce CriticJEPA, which learns goal-conditioned flow proposals from reward-free trajectories and uses frozen rollouts to select among them at every hierarchy level. Forward selection forms a complete planner; short anchored updates refine candidates before selection. Across visual navigation and manipulation, CriticJEPA increases success at a fraction of the planning compute, transferring shared settings across independently trained models, hierarchy depths, and unseen tasks while keeping every world-model weight fixed.

</details>

---

### [[20_Research/Papers/具身智能/ReJEPA_Bounded_Predictive_Regulation_for_Latent_World_Models|ReJEPA: Bounded Predictive Regulation for Latent World Models]]

![[assets/2611.31910_first_page.png|800]]

- **arXiv**: [2611.31910](https://arxiv.org/abs/2611.31910)
- **PDF**: https://arxiv.org/pdf/2611.31910
- **详细分析**: [[20_Research/Papers/具身智能/ReJEPA_Bounded_Predictive_Regulation_for_Latent_World_Models|ReJEPA: Bounded Predictive Regulation for Latent World Models]]
- **作者**: Fangzhou Lin, Yuping Wang, Shuo Xing, Yang Chen, Yuwen Heng, Xin Li, Wenbin He, Yuhan Yao, Zhengzhong Tu, Liu Ren
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ReJEPA: Bounded Predictive Regulation for Latent World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models learn representations by predicting future states in an abstract embedding space rather than reconstructing raw pixels. When training across multi-frame sequences, however, not all frames and spatial regions are equally informative or predictable. We argue that forcing a world model to minimize every prediction error may be unnecessary and harmful. Under standard $L_2$ loss, unbounded gradients force the encoder and predictor to overfit noisy or transient frames at the expense of core physical structure, while amplifying gradient conflict with representation regularizers. Conversely, $L_1$ loss bounds large gradients, but its constant gradient magnitude near zero disrupts the local smoothness required for planning. We resolve this tension with \textbf{ReJEPA}, a bounded predictive regulation principle that combines bounded gradients for large errors with smooth quadratic behavior near zero, instantiated simply via the element-wise $\log\cosh$ loss. As a drop-in training replacement across Temporal Straightening, LeWorldModel, and V-JEPA~2.1, $\log\cosh$ consistently outperforms $L_2$, a curvature-matched quadratic control, $L_1$, and Smooth-$L_1$ baselines without altering architectures or inference procedures. Notably, the gains grow with environmental complexity, scaling from simple navigation to contact-rich manipulation and real-world autonomous driving on NAVSIM. Probing and geometric analyses confirm that relaxing the penalty on extreme errors yields representations that better capture physical states and align with the true planning cost landscape.

</details>

---

### [[20_Research/Papers/强化学习/Curvature-Equilibrated_Policy_Optimization_for_Deep_Reinforcement_Learning|Curvature-Equilibrated Policy Optimization for Deep Reinforcement Learning]]

![[assets/2611.31680_first_page.png|800]]

- **arXiv**: [2611.31680](https://arxiv.org/abs/2611.31680)
- **PDF**: https://arxiv.org/pdf/2611.31680
- **详细分析**: [[20_Research/Papers/强化学习/Curvature-Equilibrated_Policy_Optimization_for_Deep_Reinforcement_Learning|Curvature-Equilibrated Policy Optimization for Deep Reinforcement Learning]]
- **作者**: Gang Chen
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.92（加权：强化学习 2.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Curvature-Equilibrated Policy Optimization for Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Gradient-based actor optimization is central to deep reinforcement learning. However, conventional first-order optimizers do not explicitly exploit the local curvature of neural actor losses. We propose EQUIP (Curvature-Equilibrated Gradients for Policy Search), a novel approach that seeks to balance local contraction and expansion of the actor parameter space by equilibrating positive and negative curvature. EQUIP constructs a trajectory-informed search subspace and uses the projected Hessian of actor loss to build a bounded local metric for curvature equilibration. First-order loss matching preserves the approximated first-order decrease in actor loss. Meanwhile, gradient mixing and curvature-based gradient selection adjust the gradient applied for actor optimization. We establish the geometric properties of curvature equilibration, derive bounds on gradient alignment and magnitude, and identify conditions for improved actor loss reduction and convergence toward stationarity under direct gradient updates. We integrate EQUIP into Soft Actor-Critic (SAC) without modifying its actor loss, critic learning, or replay mechanism. Experiments on 6 MuJoCo continuous control benchmarks show that the resulting EQUIP-SAC algorithm achieves higher mean sample efficiency than SAC and two second-order policy optimization baselines. Ablation studies further highlight the benefits of curvature equilibration and trajectory-informed geometry for policy training.

</details>

---

### [[20_Research/Papers/强化学习/One_Phase_Is_Enough_Sim-to-Real_Transfer_with_Direct_Visual_Reinforcement_Learning|One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning]]

![[assets/2611.31588_figure.png|800]]

- **arXiv**: [2611.31588](https://arxiv.org/abs/2611.31588)
- **PDF**: https://arxiv.org/pdf/2611.31588
- **详细分析**: [[20_Research/Papers/强化学习/One_Phase_Is_Enough_Sim-to-Real_Transfer_with_Direct_Visual_Reinforcement_Learning|One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning]]
- **作者**: John Marangola, Antonia Bronars, Younghyo Park, Stephen Andrews, Kushal Kedia, Pulkit Agrawal
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.12（加权：具身智能 1.5，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sim-to-real reinforcement learning (RL) has enabled impressive robotic behaviors, yet deploying policies directly from vision remains challenging. A common approach first trains a teacher policy with RL using privileged state observations, then distills its behavior into a vision-based student via imitation. However, the resulting student can substantially underperform its teacher. Directly training visual policies with RL offers a promising alternative, but learning task-relevant visual representations from scratch can be sample-inefficient, making one-phase visual RL intractable. We propose DRIFT, a simple recipe for efficient one-phase visual RL using image observations available at test time. Our key insight is to use frozen, pretrained foundation vision encoders, allowing RL to focus on learning control from existing visual representations. Freezing the encoder avoids costly backpropagation through the vision backbone, while its pretrained representations enable real-world transfer from fast, rasterized simulation rendering. Under matched architectures, observations, and compute budgets, DRIFT outperforms two-phase distillation and achieves a 58.8% relative improvement in average real-world success rate across three manipulation tasks. Controlled simulation evaluations demonstrate that DRIFT's relative advantage grows from roughly 9% in-distribution to over 61% under out-of-distribution shifts, suggesting that stronger generalization contributes to superior real-world transfer. Project website: https://jmarangola.github.io/one-phase-visual-rl/

</details>

---

### [[20_Research/Papers/具身智能/Near-Zero_Forgetting_Is_Not_Enough_Out-of-Distribution_Robustness_in_Continual_Learning_of_Pretrained_VLAs|Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs]]

![[assets/2611.31511_figure.png|800]]

- **arXiv**: [2611.31511](https://arxiv.org/abs/2611.31511)
- **PDF**: https://arxiv.org/pdf/2611.31511
- **详细分析**: [[20_Research/Papers/具身智能/Near-Zero_Forgetting_Is_Not_Enough_Out-of-Distribution_Robustness_in_Continual_Learning_of_Pretrained_VLAs|Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs]]
- **作者**: Adrià Ruiz, Bartłomiej Twardowski, Tinne Tuytelaars, Sergi Masip
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ExpReS-VLA, ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay. However, robustness to domain shift of learned tasks remains unexplored. In this work, we study the robustness of Pi0 fine-tuned with experience replay under out-of-distribution (OOD) data using the LIBERO and LIBERO-Plus benchmarks. While the in-domain (ID) setup achieves near-zero catastrophic forgetting, OOD performance on previous tasks quickly collapses. Specifically, we show that during the continual learning process, the OOD capabilities of the model degrade, following a shared representational pattern across domain shifts, which is also visible behaviorally in the two simpler suites. Representational analysis shows that drift concentrates in the multimodal and action features. Linear probes indicate that OOD features still retain task-relevant information, but appear unreadable, consistent with representation misalignment. These findings suggest that even when ID stability remains intact, severe OOD forgetting can still occur, accompanied by representational drift during continual learning.

</details>

---

### [[20_Research/Papers/世界模型/CaLA_Causal_Latent_Adjustment_for_World_Models_under_Adaptive_Policies|CaLA: Causal Latent Adjustment for World Models under Adaptive Policies]]

![[assets/2611.31431_figure.png|800]]

- **arXiv**: [2611.31431](https://arxiv.org/abs/2611.31431)
- **PDF**: https://arxiv.org/pdf/2611.31431
- **详细分析**: [[20_Research/Papers/世界模型/CaLA_Causal_Latent_Adjustment_for_World_Models_under_Adaptive_Policies|CaLA: Causal Latent Adjustment for World Models under Adaptive Policies]]
- **作者**: Robert Ness, Sofiane Ennadir, Oleg Smirnov
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: WorldModel

#### 研究背景与动机

《CaLA: Causal Latent Adjustment for World Models under Adaptive Policies》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models is answering ``imagine" answers to ``what-if'' questions via imagined rollouts. But rollouts collected by adaptive policies induce treatment-outcome confounding in imagined rollouts. We study this problem in Match-3 difficulty adjustment, where latent player skill influences both assigned difficulty and churn. We build a fully specified Match-3 SCM with sequential mechanics, adaptive assignment, and paired ground-truth interventions, on which unadjusted models fit to the logged trajectories select difficulty settings that raise churn. We then introduce Causal Latent Adjustment (CaLA), a DAG-constrained world model that infers a variational player representation from pretreatment history. Across our evaluations, CaLA provides the most reliable population-level intervention estimates and competitive individualized decisions, although rich handcrafted histories can remain advantageous for individual-level adjustment. We further find that residual correction can degrade causal decision quality despite improving predictive fit, highlighting the need to distinguish predictive accuracy, confounding adjustment and the behavior of downstream causal estimators.

</details>

---
