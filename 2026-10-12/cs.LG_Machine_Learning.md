# cs.LG | Machine Learning | 2026-10-12

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/强化学习/Goal-Oriented_Bundle_Management_and_Flow_Control_for_Deep-Space_Communications_via_Reinforcement_Learning|Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning]]

![[assets/2610.13923_figure.png|800]]

- **arXiv**: [2610.13923](https://arxiv.org/abs/2610.13923)
- **PDF**: https://arxiv.org/pdf/2610.13923
- **详细分析**: [[20_Research/Papers/强化学习/Goal-Oriented_Bundle_Management_and_Flow_Control_for_Deep-Space_Communications_via_Reinforcement_Learning|Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning]]
- **作者**: Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, Elif Uysal
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DTNSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side scheduling and dropping decisions are inherently goal-oriented: transmission resources should be allocated to bundles most valuable to downstream mission objectives. Conventional schedulers, such as FIFO, do not explicitly optimize task utility and may provide unfair service across heterogeneous planetary sources. This paper presents a closed-loop modeling and learning framework for relay-side bundle and flow management in a contact-driven deep-space network, where lunar and Martian updates are forwarded through a shared-buffer relay to Earth. We quantify destination-side information freshness using excess age $Δ_i^e(t)=[Δ_i(t)-d_i(t)]^+$, where $Δ_i(t)$ denotes the Age of Information of source $i$ and $d_i(t)$ is a source-dependent delay baseline. Based on this metric, we define a goal-oriented loss that supports source-dependent nonlinear penalties, allowing prioritization according to mission relevance. We formulate relay control as a constrained semi-Markov decision process (CSMDP) and solve it using masked Lagrangian Proximal Policy Optimization (PPO). Feasibility-aware action masking restricts transmissions to bundles that can complete within the remaining contact window. DTNSim simulations indicate improved age-based utility and inter-flow fairness compared with baseline schedulers. The proposed framework jointly optimizes relay-side bundle scheduling, dropping, and flow control under contact-driven dynamics with explicit fairness considerations across heterogeneous sources.

</details>

---

### [[20_Research/Papers/强化学习/Hitting-Time_Bounds_for_Asynchronous_Q-Learning|Hitting-Time Bounds for Asynchronous Q-Learning]]

![[assets/2610.13901_first_page.png|800]]

- **arXiv**: [2610.13901](https://arxiv.org/abs/2610.13901)
- **PDF**: https://arxiv.org/pdf/2610.13901
- **详细分析**: [[20_Research/Papers/强化学习/Hitting-Time_Bounds_for_Asynchronous_Q-Learning|Hitting-Time Bounds for Asynchronous Q-Learning]]
- **作者**: Yang Peng
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Hitting-Time Bounds for Asynchronous Q-Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the last iterate of standard asynchronous Q-learning from a single trajectory of a finite Markov decision process. The trajectory follows a fixed behavior policy whose state--action chain is irreducible and may be periodic. For discount factor $γ$, write $H=(1-γ)^{-1}$, and let $μ_{\min}$ be the minimum stationary state--action probability and $\mathfrak h_\star$ the largest expected hitting time of the reverse state--action chain. We prove that zero-initialized Q-learning with a constant step size achieves sup-norm error at most $\varepsilon$ with high probability using $\widetilde{O}(H^4/(μ_{\min}\varepsilon^2)+\mathfrak h_\star)$ transitions, for $0&lt;\varepsilon\le1$. The statistical term retains the quartic effective-horizon dependence of standard Q-learning, while initialization cost is additive in $\mathfrak h_\star$. For aperiodic behavior chains, a comparison with mixing time yields a transient term $\widetilde{O}(t_{\mathrm{mix}}/μ_{\min})$. An empirical state--action count rule selects a constant step size for a subsequent training run and attains the same rate without prior knowledge of model parameters, target accuracy, or confidence level. The output is the last training iterate, with both stages included in the sample count. The proof uses two deterministic Bellman envelopes to separate statistical error from fixed-policy initialization error and adapts reverse-time hitting-cost compensation from TD learning to state--action propagation. An exploration lower bound holds for arbitrary predictable step sizes. Together with the existing statistical lower bound and its extension to pilot-selected constant steps, it yields matching mean-square rates up to logarithmic factors on the stated large-sample parameter classes.

</details>

---

### [[20_Research/Papers/具身智能/SmolWAM_A_Latent_World-Action_Model_for_Robotic_Manipulation_on_Edge_Devices|SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices]]

![[assets/2610.13740_figure.png|800]]

- **arXiv**: [2610.13740](https://arxiv.org/abs/2610.13740)
- **PDF**: https://arxiv.org/pdf/2610.13740
- **详细分析**: [[20_Research/Papers/具身智能/SmolWAM_A_Latent_World-Action_Model_for_Robotic_Manipulation_on_Edge_Devices|SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices]]
- **作者**: Timi Owolabi, Hikmah Olawore, Frances Adelakun, Ayotomiwa Oyewumi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA, TinyVLA, TurboVLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) predict a robot's actions together with the observations those actions will produce. However, the strongest models rely on video diffusion transformers that are far too computationally expensive for resource-constrained edge devices. We present SmolWAM, a latent WAM that we derive from the 2B-parameter Cosmos Policy by keeping its pretrained trunk and rebuilding its inference interface: single-frame visual latents, cached text features that preserve the trunk's attention sinks, 12 of 28 transformer blocks, and 1,008 tokens from which actions and future visual latents are read out in one rectified-flow step. Trained in 3.6 GPU-hours, SmolWAM succeeds in 95.5% of 400 LIBERO episodes at 57 ms and 2.3 TFLOP per 16-action chunk with 2.4 GiB of GPU memory, 11x faster than its teacher with 18.5x fewer FLOPs and 3.2x less memory, and its world head still forecasts scene motion.

</details>

---

### [[20_Research/Papers/大模型/EmoGavel_Grounding-Aware_Reinforcement_Learning_with_Verifiable_Rewards_for_Multimodal_Emotion_Preference_Learning|EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning]]

![[assets/2610.13353_figure.png|800]]

- **arXiv**: [2610.13353](https://arxiv.org/abs/2610.13353)
- **PDF**: https://arxiv.org/pdf/2610.13353
- **详细分析**: [[20_Research/Papers/大模型/EmoGavel_Grounding-Aware_Reinforcement_Learning_with_Verifiable_Rewards_for_Multimodal_Emotion_Preference_Learning|EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning]]
- **作者**: Zilong Huang, Kong Aik Lee, Zezhong Jin, Man-Wai Mak, Tatsuya Kawahara
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CosSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal emotion preference learning uses pairwise comparisons to identify which open-ended emotion descriptions align more closely with human judgments. However, existing methods primarily focus on the final preference decision and provide little explicit supervision for localizing and correcting erroneous content. To address this limitation, we propose EmoGavel, a Grounding-Aware reinforcement learning framework with Verifiable rewards for multimodal Emotion preference Learning. We first introduce grounded supervised fine-tuning (Grounded SFT), which exploits controlled-error construction information to jointly learn preference prediction, error localization, repair, and missing-evidence recovery. We then optimize these verifiable outcomes with grounding-aware group relative policy optimization (GA-GRPO), combining preference-gated grounding rewards with dynamic zero-variance rescue to prioritize preference correctness and recover learning signals from all-wrong groups. Experiments on EmoPrefer and controlled-error evaluation sets show that EmoGavel improves both natural preference prediction and controlled-error discrimination while maintaining strong error-grounding performance. Our code and model checkpoints will be released once the paper is accepted.

</details>

---

### [[20_Research/Papers/大模型/AgentTune_A_Unified_Training_Lifecycle_for_Tool-Using_LLM_Agents|AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents]]

![[assets/2610.13335_figure.png|800]]

- **arXiv**: [2610.13335](https://arxiv.org/abs/2610.13335)
- **PDF**: https://arxiv.org/pdf/2610.13335
- **详细分析**: [[20_Research/Papers/大模型/AgentTune_A_Unified_Training_Lifecycle_for_Tool-Using_LLM_Agents|AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents]]
- **作者**: R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.9，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent projections for training, evaluation, and auditing. Building on this substrate, the library provides a shared agent runtime, tool-calling reinforcement learning, agentic distillation, retrieval-augmented generation, decision workflows, evaluation utilities, and a designed path toward self-healing agents. These components are exposed through composable interfaces so that agent strategies, training methods, evaluation procedures, and recovery mechanisms can be combined without requiring separate representations or pipelines. We demonstrate the framework across agentic tasks including legal contract search and domain-specific applications, illustrating its use for trajectory-based optimization, tool-use evaluation, and cross-task agent development. AgentTune is released as a source-available library at https://github.com/Lexsi-Labs/AgentTune

</details>

---

### [[20_Research/Papers/强化学习/Structure-Aware_Numerical_Stabilization_for_Half-Precision_Proximal_Policy_Optimization|Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization]]

![[assets/2610.13306_figure.png|800]]

- **arXiv**: [2610.13306](https://arxiv.org/abs/2610.13306)
- **PDF**: https://arxiv.org/pdf/2610.13306
- **详细分析**: [[20_Research/Papers/强化学习/Structure-Aware_Numerical_Stabilization_for_Half-Precision_Proximal_Policy_Optimization|Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization]]
- **作者**: Linxuan Wu, Liang Chen
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：QaRL, QuRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Local online training on resource-constrained platforms requires low computational and training-state overhead. We study the numerical stability and computational efficiency of half-precision proximal policy optimization (PPO) on commodity GPUs. Directly converting PPO training to FP16 is unreliable because numerical errors feed back through policy updates and subsequent data collection, while PPO repeatedly compares a current policy with a fixed behavior policy. We propose PPO-FP16 with three structure-aware modules. Global scalar protection stabilizes statistics shared across a minibatch or parameter update. Policy-change residual protection extracts and preserves small differences between the current and behavior policies. Efficient persistent-update protection stabilizes optimizer state and parameter writeback while reducing state storage. These changes preserve the PPO objective, hyperparameters, and training budget. Across six continuous-control tasks and five seeds, PPO-FP16 achieves the lowest mean return-AUC rank (1.90) among the four methods and ranks first in 17 of 30 environment-seed comparisons. Eight of nine performance configurations yield PPO update speedups ranging from 1.16 to 2.03 times. Relative to Full FP32 Adam, optimizer-state memory is reduced by 71.7 to 74.9 percent, and peak allocated GPU memory is reduced by up to 44.5 percent. The results show that protecting a small set of structurally important quantities can deliver stable, efficient FP16 PPO without retuning.

</details>

---

### [[20_Research/Papers/强化学习/MORAD_Reinforcement_Learning_with_Multi-Objective_Rewards_for_RNA_Inverse_Design|MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design]]

![[assets/2610.13305_first_page.png|800]]

- **arXiv**: [2610.13305](https://arxiv.org/abs/2610.13305)
- **PDF**: https://arxiv.org/pdf/2610.13305
- **详细分析**: [[20_Research/Papers/强化学习/MORAD_Reinforcement_Learning_with_Multi-Objective_Rewards_for_RNA_Inverse_Design|MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design]]
- **作者**: Jixin Tang, Ji Guo, Jun Zhao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《MORAD: Reinforcement Learning with Multi-Objective Rewards for RNA Inverse Design》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce MORAD, an online reinforcement learning framework for backbone-conditioned RNA diffusion models that trains a single shared policy across diverse target backbones. Structure-conditioned RNA inverse design seeks nucleotide sequences compatible with a target three-dimensional backbone, yet existing reinforcement learning approaches either optimize a separate policy for each target backbone or rely on offline preference optimization, leaving online post-training of a reusable backbone-conditioned model largely unexplored. MORAD combines backbone-conditioned group sampling, group-relative reward normalization, and a forward-process diffusion objective. Beyond existing RL rewards that primarily target tertiary structural quality, MORAD jointly optimizes six measurements spanning tertiary geometry, base pairing, ensemble behavior, and sequence composition. To aggregate these heterogeneous objectives despite differences in scale and optimization direction, MORAD maps each measurement to a bounded desirability score and combines them with a weighted geometric mean. Compared with a tertiary-structure-only reward, this multi-objective formulation improves 10 of the 11 evaluation metrics that have a preferred direction. Applied to pretrained RIDE, MORAD improves GDT-TS by 16.0% (from 0.3300 to 0.3827) and pairing MCC by 19.4% (from 0.6110 to 0.7295), while reducing normalized ensemble defect by 27.5% (from 0.3906 to 0.2830). On the test set, MORAD outperforms RiboDiffusion, gRNAde, and RDesign across tertiary structural accuracy, secondary-structure pairing, and thermodynamic quality, establishing a new state of the art in structure-conditioned RNA inverse design.

</details>

---

### [[20_Research/Papers/大模型/Monarch-MoE_Structured_Experts_for_Multimodal_Continual_Instruction_Tuning|Monarch-MoE: Structured Experts for Multimodal Continual Instruction Tuning]]

![[assets/2610.13215_first_page.png|800]]

- **arXiv**: [2610.13215](https://arxiv.org/abs/2610.13215)
- **PDF**: https://arxiv.org/pdf/2610.13215
- **详细分析**: [[20_Research/Papers/大模型/Monarch-MoE_Structured_Experts_for_Multimodal_Continual_Instruction_Tuning|Monarch-MoE: Structured Experts for Multimodal Continual Instruction Tuning]]
- **作者**: Xi Zhang, Boyu Diao, Zesen Chen, Ruiqi Liu, Hangda Liu, Yongjun Xu
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Monarch-MoE: Structured Experts for Multimodal Continual Instruction Tuning》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning new tasks in multimodal continual instruction tuning can cause catastrophic forgetting of previously acquired knowledge. Although multi-expert LoRA distributes learning across experts, updates to a dense low-rank expert can still affect many output features. We introduce Monarch-MoE, which replaces the dense factors in LoRA experts with block-diagonal factors connected by a fixed permutation. This structure provides blockwise gradient isolation: individual block-pair updates affect only one output block, while connections between all input and output blocks are maintained. To make these compact experts practical on memory-limited hardware, we combine batched computation, fused forward operators, and an optimized backward pass. Across three continual-learning methods evaluated on MLLM-DCL and UCIT with LLaVA-1.5-7B, Monarch-MoE improves first-task retention while reducing adapter parameters by approximately 75% and 50%, respectively. In the main comparison, first-task forgetting is as low as 0.52 percentage points on MLLM-DCL and 0.10 on UCIT, with method-dependent trade-offs in final performance. Our implementation supports fine-tuning and inference on a single 24 GB RTX 4090, with lower measured memory use and competitive runtime in the evaluated settings. Together, these algorithmic and systems improvements make structured experts a practical option for continual adaptation on memory-limited hardware.

</details>

---

### [[20_Research/Papers/机器人/Prediction-Informed_Landing_Window_Planning_for_UAV_Landing_on_USV_in_High_Sea_States|Prediction-Informed Landing Window Planning for UAV Landing on USV in High Sea States]]

![[assets/2610.13190_figure.png|800]]

- **arXiv**: [2610.13190](https://arxiv.org/abs/2610.13190)
- **PDF**: https://arxiv.org/pdf/2610.13190
- **详细分析**: [[20_Research/Papers/机器人/Prediction-Informed_Landing_Window_Planning_for_UAV_Landing_on_USV_in_High_Sea_States|Prediction-Informed Landing Window Planning for UAV Landing on USV in High Sea States]]
- **作者**: Kaizhen Li, Xi Zhou, Dan Zhang, Xiaowei Li
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Prediction-Informed Landing Window Planning for UAV Landing on USV in High Sea States》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous landing of unmanned aerial vehicle (UAV) on unmanned surface vehicle (USV) is difficult in high sea states. Existing hierarchical landing methods often infer future USV motion only implicitly from short observation histories, which limits their ability to adapt to severe and rapidly changing sea conditions. This paper presents a prediction-informed hierarchical control framework. A pretrained model is developed to explicitly predict the USV attitude during high-level landing decisions. The prediction helps identify suitable landing windows and choose the right touchdown time, while a conventional low-level flight controller maintains UAV stability and tracks motion commands. To evaluate the framework under realistic disturbances, a real-sim validation setup is constructed in which USV-motion data collected in real sea conditions are transferred to a MuJoCo USV. The experiments demonstrate the feasibility of using explicit attitude prediction to improve landing-window selection and support timing-aware UAV landing planning in rapidly varying marine environments.

</details>

---

### [[20_Research/Papers/大模型/CB-Orchestrator_Adaptive_Workflow_Optimization_for_LLM_Agents_via_Contextual_Bandits|CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits]]

![[assets/2610.13064_figure.png|800]]

- **arXiv**: [2610.13064](https://arxiv.org/abs/2610.13064)
- **PDF**: https://arxiv.org/pdf/2610.13064
- **详细分析**: [[20_Research/Papers/大模型/CB-Orchestrator_Adaptive_Workflow_Optimization_for_LLM_Agents_via_Contextual_Bandits|CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits]]
- **作者**: Jiahang Sun, Zhiwei Shang, Zhipiao Liu, Hongwei Yang, Guoqing Xie, Shuang Qiu, Zhongxiang Dai
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization is a promising direction, existing methods often incur expensive API costs during training-phase feedback collection. Furthermore, they fail to adaptively reuse high-quality workflows, which creates a bottleneck for both performance and cost-effectiveness. To address these limitations, we propose CB-Orchestrator, an adaptive framework that decouples workflow generation from selection. In the first stage, we construct a diverse pool of candidate workflows via evolutionary search. In the second stage, we formulate workflow selection as a Contextual Bandit problem, which enables sample-efficient learning by balancing exploration and exploitation, thereby significantly reducing the feedback required for training. During inference, the model adaptively selects the optimal workflow tailored to each query. Evaluations across five diverse benchmarks demonstrate that CB-Orchestrator consistently outperforms all baselines. Notably, on the MATH dataset, CB-Orchestrator achieves better performance than strong recent baselines while reducing training-phase API token overhead by no less than 40.55% and total end-to-end training (including workflow pool generation) token overhead by no less than 29.73%.

</details>

---

### [[20_Research/Papers/大模型/Trajectory-Aware_Policy_Optimization_Closing_the_State_Distribution_Gap_in_Long-Horizon_LLM_RL|Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL]]

![[assets/2610.13020_figure.png|800]]

- **arXiv**: [2610.13020](https://arxiv.org/abs/2610.13020)
- **PDF**: https://arxiv.org/pdf/2610.13020
- **详细分析**: [[20_Research/Papers/大模型/Trajectory-Aware_Policy_Optimization_Closing_the_State_Distribution_Gap_in_Long-Horizon_LLM_RL|Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL]]
- **作者**: Zhicheng Cai, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.92（加权：大模型 0.4，强化学习 1.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become a dominant paradigm for enhancing LLMs' reasoning capabilities. Yet long-horizon autoregressive rollouts introduce a fundamental limitation: local policy mismatch can compound into severe state distribution shift over trajectories. Existing LLM RL methods, such as GRPO and GSPO, control policy mismatch at the token or sequence level, but overlook this trajectory-induced shift, causing training instability and eventual collapse as the horizon grows. To close the state distribution gap, we propose Trajectory-Aware Policy Optimization (TAPO), a principled framework that theoretically derives the state-distribution correction from the off-policy policy gradient and incorporates it into the RL objective. TAPO further employs a geometric-mean estimator for variance reduction, together with a length-aware dynamic clipping that prevents overly deviated updates across the trajectory. Extensive experiments demonstrate that TAPO significantly surpasses existing LLM RL algorithms across eight competition-level benchmarks, achieving up to 48% and 12% improvement over GRPO on mathematical reasoning and algorithmic coding, with substantially enhanced training stability.

</details>

---

### [[20_Research/Papers/大模型/Reinforcement_Learning_via_Fixed-point_Flow_Matching|Reinforcement Learning via Fixed-point Flow Matching]]

![[assets/2610.12848_figure.png|800]]

- **arXiv**: [2610.12848](https://arxiv.org/abs/2610.12848)
- **PDF**: https://arxiv.org/pdf/2610.12848
- **详细分析**: [[20_Research/Papers/大模型/Reinforcement_Learning_via_Fixed-point_Flow_Matching|Reinforcement Learning via Fixed-point Flow Matching]]
- **作者**: Denis Blessing, Onur Celik, Gerhard Neumann
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Reinforcement Learning via Fixed-point Flow Matching》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In maximum entropy and behavior-constrained reinforcement learning (RL), the optimal policy is given by a Boltzmann distribution. Generating samples from this distribution can be challenging, as it is often complex and multimodal. While flow policies trained with flow matching provide a powerful framework for representing such distributions, they traditionally rely on access to training data, which is generally unavailable in online RL. To address this limitation, we propose fixed-point flow matching (FFM), a data-free procedure for training and fine-tuning flow policies in RL. FFM leverages the target flow identity to formulate the actor update as a fixed-point iteration, utilizing a flow-matching-style regression objective where the critic's action gradients serve as regression targets. We show that the optimal policy is a fixed point of this iteration. Through extensive experiments, we demonstrate that FFM effectively fine-tunes pretrained flow policies in the offline-to-online setting and enables efficient and accurate training of flow policies from scratch in online RL. These results establish fixed-point flow matching as a principled approach for learning expressive flow-based policies without requiring training data.

</details>

---

### [[20_Research/Papers/强化学习/Cross-Behavior_Policy_Optimization_Unified_Learning_from_Offline_Demonstrations_and_On-_and_Off-Policy_Rollouts_via_a_Shared_Regression_Targ|Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target]]

![[assets/2610.12830_figure.png|800]]

- **arXiv**: [2610.12830](https://arxiv.org/abs/2610.12830)
- **PDF**: https://arxiv.org/pdf/2610.12830
- **详细分析**: [[20_Research/Papers/强化学习/Cross-Behavior_Policy_Optimization_Unified_Learning_from_Offline_Demonstrations_and_On-_and_Off-Policy_Rollouts_via_a_Shared_Regression_Targ|Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target]]
- **作者**: Du Cheng, Junyu Lu, Jingfan Zhang, Yuzhuo Zhang, Haoxuan Jia, Shichao Weng
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning post-training draws on offline demonstrations and policy-generated rollouts, yet conventional supervised fine-tuning (SFT) followed by reinforcement learning (RL) separates their objectives and limits continued reuse of collected responses. We propose \textbf{Cross-Behavior Policy Optimization} (CBPO), which makes these sources compatible with one regression loss through a fixed-reference target. Because the generating policy does not enter this target, positive and negative offline completions, reference responses, and current and historical rollouts can share a common reward-labeled record format and replay buffer. As new responses enter the buffer, optimization retains the same regression objective without coordinating separate SFT and RL objectives or requiring stored behavior-policy probabilities, importance weighting, or a learned critic. Restricting the available sources gives offline, on-policy, and off-policy variants, while CBPO-Unified combines them. Across two model scales and four mathematical reasoning benchmarks, CBPO delivers leading \texttt{avg@32} and \texttt{pass@32} performance across benchmarks and data regimes. On Qwen3-1.7B, CBPO-Unified improves benchmark-averaged \texttt{avg@32} and \texttt{pass@32} over SFT DAPO by 2.33 and 4.44 percentage points, respectively. In the replay ablation, retaining historical rollouts improves these metrics by 1.87 and 3.72 percentage points over the no-history configuration.

</details>

---

### [[20_Research/Papers/大模型/TreeHCA_Hindsight-Guided_Exploration_and_Credit_Assignment_for_Multi-Turn_LLM_Agents|TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents]]

![[assets/2610.12828_figure.png|800]]

- **arXiv**: [2610.12828](https://arxiv.org/abs/2610.12828)
- **PDF**: https://arxiv.org/pdf/2610.12828
- **详细分析**: [[20_Research/Papers/大模型/TreeHCA_Hindsight-Guided_Exploration_and_Credit_Assignment_for_Multi-Turn_LLM_Agents|TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents]]
- **作者**: Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri, Srinivas Shakkottai, Dileep Kalathil
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Outcome-supervised group-relative policy optimization (GRPO) assigns the same advantage to every token in an LLM agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this feedback, but its estimates rely on trajectories containing informative alternatives at consequential histories. We introduce TreeHCA, which couples hindsight-guided exploration with hindsight credit assignment. TreeHCA uses changes in reference-answer likelihood to revisit intermediate histories and sample alternative continuations, forming a tree of reasoning and tool interactions. Because this exploration changes the distribution of sampled continuations, we derive the corresponding inverse-hindsight importance correction, including an exact finite-pool identity. We use this structure in a normalized tree backup that propagates terminal outcomes into turn-level advantages. This shared hindsight structure is TreeHCA's central design principle, linking informative exploration with hindsight-guided credit assignment. Across seven question-answering benchmarks and three Qwen backbones, TreeHCA outperforms all baselines in aggregate exact match, validating the effectiveness of paired exploration and credit assignment for multi-turn LLM agent training. Our code is available at github.com/TheBlackCat22/TreeHCA.

</details>

---

### [[20_Research/Papers/强化学习/Toward_Maximizing_Algebraic_Connectivity_via_Density-Dependent_Backbone_Construction_and_Reinforcement_Learning_Completion|Toward Maximizing Algebraic Connectivity via Density-Dependent Backbone Construction and Reinforcement Learning Completion]]

![[assets/2610.12697_figure.png|800]]

- **arXiv**: [2610.12697](https://arxiv.org/abs/2610.12697)
- **PDF**: https://arxiv.org/pdf/2610.12697
- **详细分析**: [[20_Research/Papers/强化学习/Toward_Maximizing_Algebraic_Connectivity_via_Density-Dependent_Backbone_Construction_and_Reinforcement_Learning_Completion|Toward Maximizing Algebraic Connectivity via Density-Dependent Backbone Construction and Reinforcement Learning Completion]]
- **作者**: Zeru Zhu, Marco Gamarra, Ji Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Toward Maximizing Algebraic Connectivity via Density-Dependent Backbone Construction and Reinforcement Learning Completion》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies an open network design problem of constructing graph topologies with maximum algebraic connectivity under fixed numbers of vertices and edges. A density-dependent approach is proposed that decomposes the design task into two stages: a high-quality, low-cost structural backbone construction and a reinforcement learning completion stage. The method selects the backbone based on density, using complete multipartite graphs in dense regimes and Cayley graphs in low-to-intermediate regimes, and then refines the remaining edges through a learning-based procedure. Numerical results show that the proposed method achieves high algebraic connectivity with favorable runtime scalability, outperforming existing methods. These results support a structural-family-first strategy for scalable network design.

</details>

---

### [[20_Research/Papers/大模型/SynAct_Synergistic_Active_Feedback_Learning_for_LLM_Agents|SynAct: Synergistic Active Feedback Learning for LLM Agents]]

![[assets/2610.12651_figure.png|800]]

- **arXiv**: [2610.12651](https://arxiv.org/abs/2610.12651)
- **PDF**: https://arxiv.org/pdf/2610.12651
- **详细分析**: [[20_Research/Papers/大模型/SynAct_Synergistic_Active_Feedback_Learning_for_LLM_Agents|SynAct: Synergistic Active Feedback Learning for LLM Agents]]
- **作者**: Ning Liu, Ian Li, Kristina Klinkner
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SynAct: Synergistic Active Feedback Learning for LLM Agents》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents executing multi-step workflows fail in two fundamentally different ways: recoverable slips, which further attempts can repair, and knowledge gaps, which retrying cannot resolve. Expert feedback can address the latter, but expert attention is scarce. The key challenge is therefore not whether to ask for feedback, but where feedback can change the outcome. Existing approaches either avoid expert feedback, allowing agents to reinforce their own errors, or allocate feedback at the task level without identifying consequential decisions. We present SynAct, an active learning framework that treats expert attention as the binding constraint and allocates feedback at the level of individual decisions. SynAct ranks decisions by the mutual information between the selected action and the terminal outcome across repeated rollouts, queries an expert at the highest-value decisions, and distills the resulting corrections into transferable rules that the agent can reuse without expert access at deployment. We theoretically characterize what this signal identifies under finite repeated sampling: with k rollouts and at least m observations per action, outcome-constant decisions have zero mutual information, while outcome-separating decisions have mutual information at least H2(m/k) bits, yielding exact separation for any threshold t in (0,H2(m/k)). This also explains why success-based acquisition can be blind when all rollouts fail: success is constant even when failed runs reach different outcomes. Across four agent benchmarks and four models spanning three families, SynAct improves held-out accuracy in all 16 evaluated settings, by +11.7pp on average. The same signal transfers to inference-time routing, where SynAct outperforms budget-matched cascade, uncertainty, and expert-judge routers in 15 of 16 settings, while a single targeted correction outperforms seven additional unaimed retries.

</details>

---
