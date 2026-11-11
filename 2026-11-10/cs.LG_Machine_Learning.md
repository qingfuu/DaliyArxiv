# cs.LG | Machine Learning | 2026-11-10

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/具身智能/VLA_Adaptation_with_Real_and_Simulated_Data_A_Case_Study_on_Robotic_Chess|VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess]]

![[assets/2611.12676_figure.png|800]]

- **arXiv**: [2611.12676](https://arxiv.org/abs/2611.12676)
- **PDF**: https://arxiv.org/pdf/2611.12676
- **详细分析**: [[20_Research/Papers/具身智能/VLA_Adaptation_with_Real_and_Simulated_Data_A_Case_Study_on_Robotic_Chess|VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess]]
- **作者**: Matěj Kripner, Milan Straka
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.42（加权：具身智能 1.8，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are trained as general-purpose foundation models for robot learning, and require fine-tuning for each downstream task and robot. This raises practical questions such as how much data and training updates are needed, how checkpoints should be selected, and whether simulation can be leveraged to alleviate the cost of real data collection. We study these questions on a task that requires both precise manipulation and spatial understanding of the scene. In this task, an SO-101 arm moves a chess king between two squares that are given only by their names, such as e4 and a5. We fine-tune $π_{0.5}$ with various dataset sizes and update budgets, using teleoperated demonstrations as well as simulated demonstrations from a randomized scripted expert that imitates the variability of human demonstrations. In simulation, the success rate scales with both data and updates. Importantly, we find that a short learning-rate cool-down adds up to 31 points and is necessary for comparing checkpoints, and that validation loss and action error are unreliable for model selection. On the real arm, we fine-tune on up to 256 teleoperated demonstrations and evaluate ten policies in 25 trials each. Partial results indicate that pretraining on the simulated demonstrations helps substantially, most clearly when real data is scarce. We also present a negative result, in which training on the policy's own rollouts with filtered behavior cloning, RECAP-style advantage conditioning, corrections from an automatic coach, or residual reinforcement learning did not yield a measurable improvement over plain behavior cloning in our setting. We release the simulator, the expert and the real demonstrations.

</details>

---

### [[20_Research/Papers/强化学习/Simulation-aided_Reinforcement_Learning_with_Control_Variates|Simulation-aided Reinforcement Learning with Control Variates]]

![[assets/2611.12643_figure.png|800]]

- **arXiv**: [2611.12643](https://arxiv.org/abs/2611.12643)
- **PDF**: https://arxiv.org/pdf/2611.12643
- **详细分析**: [[20_Research/Papers/强化学习/Simulation-aided_Reinforcement_Learning_with_Control_Variates|Simulation-aided Reinforcement Learning with Control Variates]]
- **作者**: Omer Hemo, Ido Sefi, Mirco Mutti, Aviv Tamar, Kfir Y. Levy
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Simulation-aided Reinforcement Learning with Control Variates》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) algorithms often rely on data collected from a target environment, which can be expensive and noisy. Although simulators can generate large amounts of additional data, standard simulation mixing approaches, which directly combine simulated and real experience, can degrade performance due to simulator inaccuracies, especially when they bias the solution away from the optimal policy. We propose a conservative simulation-aided learning method based on control variates, where simulated data is used solely to reduce variance in the learning process rather than directly shaping the learning target. We develop our approach for Policy-Evaluation, which is a fundamental building block of RL algorithms. Then we combine it within the actor-critic framework towards policy improvement, as well as extend it towards offline RL scenarios. Experiments on multiple MuJoCo benchmark tasks demonstrate improvements over standard simulation mixing approaches, highlighting control variates as an effective tool for simulation-aided reinforcement learning.

</details>

---

### [[20_Research/Papers/强化学习/Fade_to..._Red_Scheduling_Coloured_Noise_Exploration_Supports_Efficient_Robot_Learning_with_Reduced_Movement_Jerk|Fade to... Red? Scheduling Coloured Noise Exploration Supports Efficient Robot Learning with Reduced Movement Jerk]]

![[assets/2611.11868_figure.png|800]]

- **arXiv**: [2611.11868](https://arxiv.org/abs/2611.11868)
- **PDF**: https://arxiv.org/pdf/2611.11868
- **详细分析**: [[20_Research/Papers/强化学习/Fade_to..._Red_Scheduling_Coloured_Noise_Exploration_Supports_Efficient_Robot_Learning_with_Reduced_Movement_Jerk|Fade to... Red? Scheduling Coloured Noise Exploration Supports Efficient Robot Learning with Reduced Movement Jerk]]
- **作者**: Francisco M. López, Francisco Cruz
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.62（加权：具身智能 0.6，强化学习 0.56，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Fade to... Red? Scheduling Coloured Noise Exploration Supports Efficient Robot Learning with Reduced Movement Jerk》归入 机器人、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploration in deep reinforcement learning (RL) for continuous control is commonly driven by temporally uncorrelated Gaussian (white) action noise, which leads to jerky motions with locally constrained exploration. In contrast, temporally correlated coloured noise, particularly pink noise, has been shown to support more efficient exploration in RL. Motivated by these findings, we inquire whether scheduling changes to the noise colour over the course of training can outperform white noise for continuous control robotics. We perform a systematic study of 49 linear schedules between white and red noise, together with generalised state-dependent exploration (gSDE), on four sparse-reward manipulation tasks with a Fetch arm and a Shadow Dexterous Hand. We find that the noise colour at the end of training does not affect learning efficiency or end performance, whereas fading towards red noise halves the jerk of exploration in every task. Balancing learning efficiency, end performance and smoothness, red noise emerges as the preferred strategy: it learns as efficiently as pink noise with almost 2-fold less movement jerk. We therefore recommend exploration schedulers that fade towards red noise as the default for off-policy robot learning.

</details>

---

### [[20_Research/Papers/具身智能/DeltaForge_A_Post-hoc_Mixture-of-Experts_VLA_for_Multi-Domain_Autonomous_Driving|DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving]]

![[assets/2611.11856_figure.png|800]]

- **arXiv**: [2611.11856](https://arxiv.org/abs/2611.11856)
- **PDF**: https://arxiv.org/pdf/2611.11856
- **详细分析**: [[20_Research/Papers/具身智能/DeltaForge_A_Post-hoc_Mixture-of-Experts_VLA_for_Multi-Domain_Autonomous_Driving|DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving]]
- **作者**: Bingzhang Wang, Mo Poorsartep, Yasaman Esfandiari
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into a single model. Weight merging loses accuracy as heterogeneous domains accumulate, and dense mixture-of-experts routing is prohibitively expensive to combine them. We present DeltaForge, to our knowledge the first post-hoc mixture-of-experts VLA for driving, which consolidates N independently finetuned per-domain models into a single multi-domain model from their weights and a small proxy set alone. When different operators finetune the same base model, their weight updates end up sharing a lot of structure. We exploit this by decomposing all the updates together using singular value decomposition (SVD), splitting each one into a shared part (the same across all domains) and a tiny domain-specific part. The router then only needs to work with those tiny domain-specific pieces, not the full expert weights, which is what keeps the approach efficient. Then two cooperating clip-level blind routers, one over the VLM reasoning experts and one over the flow-matching dynamics experts, are trained from soft labels on the proxy dataset. Across six diverse domains spanning urban, off-road, and highway driving on cars, trucks, and all-terrain vehicles (ATVs), DeltaForge approaches the accuracy of the per-domain experts and surpasses every merging, routing, centralized, and federated baseline at close to single-model parameter and compute cost. Adding a new domain requires only projecting its weight update onto the shared basis with no end-to-end retraining needed. The resulting model also generalizes to domain combinations it was never explicitly trained on.

</details>

---

### [[20_Research/Papers/世界模型/Planners_Exploit_Deterministic_Error_Dithered_Low-Bit_World_Models|Planners Exploit Deterministic Error: Dithered Low-Bit World Models]]

![[assets/2611.11780_first_page.png|800]]

- **arXiv**: [2611.11780](https://arxiv.org/abs/2611.11780)
- **PDF**: https://arxiv.org/pdf/2611.11780
- **详细分析**: [[20_Research/Papers/世界模型/Planners_Exploit_Deterministic_Error_Dithered_Low-Bit_World_Models|Planners Exploit Deterministic Error: Dithered Low-Bit World Models]]
- **作者**: Yong Hwi Song, Keon Myung Lee
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Planners Exploit Deterministic Error: Dithered Low-Bit World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sampling-based planners such as MPPI and CEM query a learned world model thousands of times per control step, so low-bit world models are an obvious way to make model-based control cheaper on a robot. With round-to-nearest activation quantization and no calibration, we find that planning can collapse, by up to 100 points of success, while the world model's latent one-step prediction error stays no larger than that of a stochastic rounding scheme that plans well. At the same bit width, what decides the outcome is not the size of the rounding error but whether it persists across planner iterations and is shared across candidates. Round-to-nearest leaves an error that persists, and an iterating planner drifts toward the candidates that this error favors; in TD-MPC2, holding the same dither fixed within a step or an episode brings the drift back. Dither shared by all candidates and redrawn at every iteration removes most of the damage at the same bit width and without training: at least half of it in all 19 affected Meta-World cells (task $\times$ bit width) of TD-MPC2 (median 95%), in 4 of 5 DINO-WM cells, and in all 8 affected tasks of a 317M-parameter multi-task TD-MPC2. Captured as CUDA graphs on an Ampere GPU, a W8A4 integer TD-MPC2 world model runs its planning rollouts 1.9-3.3$\times$ and the whole planning step 1.3-1.5$\times$ faster than FP32, though not faster than BF16 with pre-converted weights; shared dither adds at most 2.3% latency. In TD-MPC2, block-scaled NVFP4 removes most of the damage and MXFP4 part of it, which ties the failure to coarse grids with a shared scale. Hypotheses, thresholds and analysis code were fixed before the data that test them, and the hypotheses that failed are reported.

</details>

---

### [[20_Research/Papers/强化学习/Data-Driven_Precision_Control_of_Soft_Helicoid_Robots|Data-Driven Precision Control of Soft Helicoid Robots]]

![[assets/2611.11709_figure.png|800]]

- **arXiv**: [2611.11709](https://arxiv.org/abs/2611.11709)
- **PDF**: https://arxiv.org/pdf/2611.11709
- **详细分析**: [[20_Research/Papers/强化学习/Data-Driven_Precision_Control_of_Soft_Helicoid_Robots|Data-Driven Precision Control of Soft Helicoid Robots]]
- **作者**: Roshan S. Kaundinya, Mark Leone, Roberto Sabella, Hugo Buurmeijer, Luis Pabon, John Irvin Alora, Marco Pavone, George Haller
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.52（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Data-Driven Precision Control of Soft Helicoid Robots》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A purely data-driven method grounded in the theory of adiabatic spectral submanifolds (aSSMs) was recently used to model and control nonlinear soft robotic simulators. Here, we extend the methodology to learn aSSM-reduced models from data collected from hardware soft robotic platforms. Specifically, we learn a five dimensional (5D) aSSM-reduced nonlinear ordinary differential equation (ODE) that accurately models the dynamics of a soft-helicoid trunk robot. We then use this ODE in a model predictive control scheme to demonstrate real-time precision control across various challenging closed-loop trajectory-tracking tasks, ranging from 2D to 3D trajectories with static and dynamic constraints. We find that our methodology enhances accuracy and precision across all control tasks compared to available data-driven linear methods and model-free reinforcement learning. While we focus here on a soft-helicoid trunk robot, our methodology relies solely on hardware data and is therefore applicable to a broader class of soft robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Streaming_Failure_Forecasting_VLA_Failure_Monitors_That_Keep_Learning_After_Deployment|Streaming Failure Forecasting: VLA Failure Monitors That Keep Learning After Deployment]]

![[assets/2611.11688_figure.png|800]]

- **arXiv**: [2611.11688](https://arxiv.org/abs/2611.11688)
- **PDF**: https://arxiv.org/pdf/2611.11688
- **详细分析**: [[20_Research/Papers/具身智能/Streaming_Failure_Forecasting_VLA_Failure_Monitors_That_Keep_Learning_After_Deployment|Streaming Failure Forecasting: VLA Failure Monitors That Keep Learning After Deployment]]
- **作者**: Amit Jadhav, Shaurya Beriwala, David Q. Liu, Yanfei Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Streaming Failure Forecasting: VLA Failure Monitors That Keep Learning After Deployment》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ArmnetBench, CoRL, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Failure monitors for vision-language-action (VLA) policies are trained offline and then frozen. After deployment, lighting, objects and cameras drift, and the policy itself is updated or moved to new tasks. On recorded real-robot runs, after a switch of task or policy version, a frozen monitor fit on the old task ranks failures little better than chance. We present Streaming Failure Forecasting (SFF), a monitor that keeps learning from the one label every episode provides: whether it succeeded. SFF keeps the offline monitor's network fixed and refits only its last linear layer after each episode, at 2.18 ms per policy call on a Jetson CPU core. Its alarm threshold moves only after successes, which in simulation kept false alarms near target except when two drifts came at once. With every setting locked before testing, SFF ranks failures better than the same monitor kept frozen on 4 of 5 simulated test suites under unannounced drift, and above resetting on detected drift on every suite. Carried with its locked learner settings to 434 recorded runs of four VLAs on real SO-101 arms, replayed across unannounced switches of task or policy version, it ranks failures better than the frozen monitor for every VLA and, in an exploratory comparison, above a full reset at the true switch. A deployed failure monitor need not stay frozen: refitting its readout from outcomes is cheap and helps after the changes we tested.

</details>

---

### [[20_Research/Papers/机器人/Brain-Aligned_Latent_Actions_Imposing_Premotor_Cortex_Geometry_on_a_Robot's_Action_Vocabulary|Brain-Aligned Latent Actions: Imposing Premotor Cortex Geometry on a Robot's Action Vocabulary]]

![[assets/2611.11674_first_page.png|800]]

- **arXiv**: [2611.11674](https://arxiv.org/abs/2611.11674)
- **PDF**: https://arxiv.org/pdf/2611.11674
- **详细分析**: [[20_Research/Papers/机器人/Brain-Aligned_Latent_Actions_Imposing_Premotor_Cortex_Geometry_on_a_Robot's_Action_Vocabulary|Brain-Aligned Latent Actions: Imposing Premotor Cortex Geometry on a Robot's Action Vocabulary]]
- **作者**: Amit Jadhav
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Brain-Aligned Latent Actions: Imposing Premotor Cortex Geometry on a Robot's Action Vocabulary》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies increasingly act through a small vocabulary of discrete latent actions learned from unlabeled video, yet training leaves open which motion receives which code. We find this choice highly unstable: two independently trained runs of Moto's latent motion tokenizer assign the same robot clips to nearly unrelated codes (adjusted Rand index 0.001), and evaluating one tokenizer in bf16 instead of fp32 reassigns 74% of its tokens. We use this freedom to impose the representational geometry of macaque ventral premotor cortex (PMv), recorded while a monkey drew shapes, on the tokenizer's code assignment, with a straight-through similarity loss trained alongside its reconstruction objective on robot video. In one training run per target, on five shape categories the loss never saw, the PMv-trained tokenizer reaches a representational similarity of 0.52 with PMv, against 0.20-0.26 for released and no-prior tokenizers and 0.42 for the 95th percentile of random kinematic encoders. Kinematic, language, and random targets do not transfer (-0.17 to -0.03). Two results limit the claim: a hand-picked kinematic descriptor, the stroke's initial direction, matches PMv better (0.65), and a label-shuffled PMv control scores 0.41. We specify the downstream manipulation test, on a CALVIN pipeline that reproduces Moto's published results, before running it.

</details>

---

### [[20_Research/Papers/强化学习/Uncertainty-Guided_Reward_Labeling_for_Reinforcement_Learning_under_Limited_Feedback|Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback]]

![[assets/2611.11091_figure.png|800]]

- **arXiv**: [2611.11091](https://arxiv.org/abs/2611.11091)
- **PDF**: https://arxiv.org/pdf/2611.11091
- **详细分析**: [[20_Research/Papers/强化学习/Uncertainty-Guided_Reward_Labeling_for_Reinforcement_Learning_under_Limited_Feedback|Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback]]
- **作者**: Renhao Zhang, Shreyas Chaudhari, Bruno Castro da Silva
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IDRL, Offline-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In reinforcement learning from limited feedback (RLLF), only a small fraction of an offline dataset can be labeled with rewards, and the central question is which samples should be labeled to learn a high-performing policy from the resulting partially labeled dataset. Prior work formalized this as a reward-selection problem by focusing on the selection stage while treating downstream policy learning as a black box, in a regime where queried rewards are not retained for reward-model training. We instead study the retained-label setting, where queried rewards can be stored and used to fit a reward model before policy learning. We bound the suboptimality of the learned policy in terms of two sources of error: one arising from offline RL on a fixed, offline dataset, and the other from uncertainty in the reward model. Since reward selection cannot change the offline dataset, the limited labeling budget must be used to strategically reduce reward uncertainty. Motivated by RLLF's observation that useful rewards tend to keep the agent on high-return trajectories, we introduce Successor-Guided Uncertainty REduction (SURE), a novel method that uses successor features to select rewards that are both uncertain and associated with states from which high-valued states are reachable. We formally derive SURE from a bound-induced design objective and characterize its exact one-step marginal gain. Empirically, SURE reaches near full-feedback performance with few reward labels across a variety of domains and offline-RL backbones, yielding an effective method for feedback-efficient reinforcement learning.

</details>

---

### [[20_Research/Papers/具身智能/DPDP_Diffusion_Policy-Steered_Diffusion_Planner_for_Offline_Reinforcement_Learning|DPDP: Diffusion Policy-Steered Diffusion Planner for Offline Reinforcement Learning]]

![[assets/2611.10993_first_page.png|800]]

- **arXiv**: [2611.10993](https://arxiv.org/abs/2611.10993)
- **PDF**: https://arxiv.org/pdf/2611.10993
- **详细分析**: [[20_Research/Papers/具身智能/DPDP_Diffusion_Policy-Steered_Diffusion_Planner_for_Offline_Reinforcement_Learning|DPDP: Diffusion Policy-Steered Diffusion Planner for Offline Reinforcement Learning]]
- **作者**: Ruyi An, Mingyuan Zhou
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DPDP: Diffusion Policy-Steered Diffusion Planner for Offline Reinforcement Learning》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In offline reinforcement learning, diffusion models fill two roles with complementary strengths. Typically guided by a critic, a diffusion policy is value-aware and favors high-return, behavior-supported actions, but it is short-sighted: it never lays out the states it intends to visit. A diffusion planner is far-sighted, synthesizing such a long-horizon trajectory, but it is only behavior-driven at execution, realizing each planned transition using only offline behavior.Each is strong exactly where the other is weak. We introduce DPDP to bring them together at the planner's execution step, where a planned transition becomes an action. Reading the planner's inverse-dynamics executor as a posterior over actions: the environment's transition likelihood relates an action to the planned next state, while the behavioral prior determines its weight under the offline data. Replacing this prior with a value-optimized diffusion policy preserves the planned transition likelihood and favors valuable actions that can serve the plan. We target the resulting clean-action distribution in two ways. A training-free sampler composes policy and inverse-dynamics scores at matched action noise levels and applies Langevin correction; this route uses a shared action noise schedule and an approximately common terminal prior. A preference objective instead amortizes the transfer into a single diffusion executor. Across D4RL, DPDP improves the planner it builds on, staying competitive with reactive diffusion policies on locomotion and leading on long-horizon navigation.

</details>

---

### [[20_Research/Papers/强化学习/Risk-Sensitive_Reinforcement_Learning_for_an_Options_Market_Maker_An_Empirical_Study_with_Real_S&P_500_Options|Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options]]

![[assets/2611.10956_figure.png|800]]

- **arXiv**: [2611.10956](https://arxiv.org/abs/2611.10956)
- **PDF**: https://arxiv.org/pdf/2611.10956
- **详细分析**: [[20_Research/Papers/强化学习/Risk-Sensitive_Reinforcement_Learning_for_an_Options_Market_Maker_An_Empirical_Study_with_Real_S&P_500_Options|Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options]]
- **作者**: Jacky Chen, Ing-Haw Cheng, John Hull, Landis Li, Zissis Poulos, Justin Shi, Andreas Veneris, Zeyu Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Options market makers absorb client order flow and must hedge the resulting inventory risk under trading frictions. We study whether an option hedging reinforcement learning (RL) agent trained on historical market data outperforms three alternatives in tail-risk protection: (i) traditional delta hedging, (ii) simple hedge-ratio rules, and (iii) the same agent trained in simulated markets. Most RL hedging agents are trained in model-generated markets that do not capture the crashes and volatility regimes present in real data. We introduce an empirical replay environment using S&amp;P 500 option data from 1996 to 2017 and compare against a matched geometric Brownian motion (GBM) environment, a stochastic-volatility (SABR) simulator, and a hybrid that values historical paths with Black-Scholes, all sharing the same portfolio mechanics, stochastic arrivals, costs, and test period. We train a distributional Twin Delayed Deep Deterministic Policy Gradient (TD3) agent and evaluate it out of sample over 2018-2023. The agent trained on empirical data reduces Conditional Value-at-Risk (CVaR) tail loss by 3.1% compared to delta hedging and outperforms every hedge-ratio rule chosen during the training period and every alternative training environment. The reduction reaches 8.9% in volatile and falling markets, but reverses to a cost of 7-10% in rising markets. Empirical training induces a state-dependent short net delta: the policy under-hedges negative-delta books, most strongly after prices have fallen. This tilt disappears with GBM training and is weaker with SABR or hybrid training. These findings suggest that exposure to historical market dynamics can materially change a tail-risk hedging policy, although the evidence rests on a single test path and the edge is regime-conditional.

</details>

---

### [[20_Research/Papers/强化学习/Learning_When_to_Think_Adaptive_Internal_Computation_for_Reinforcement_Learning|Learning When to Think: Adaptive Internal Computation for Reinforcement Learning]]

![[assets/2611.10822_first_page.png|800]]

- **arXiv**: [2611.10822](https://arxiv.org/abs/2611.10822)
- **PDF**: https://arxiv.org/pdf/2611.10822
- **详细分析**: [[20_Research/Papers/强化学习/Learning_When_to_Think_Adaptive_Internal_Computation_for_Reinforcement_Learning|Learning When to Think: Adaptive Internal Computation for Reinforcement Learning]]
- **作者**: Rohit Kumar Salla, Simon Stepputtis
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.72（加权：具身智能 0.3，强化学习 0.76，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning When to Think: Adaptive Internal Computation for Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PonderNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Iterative neural policies usually spend the same computation on every decision, although the benefit of additional processing varies across states. We introduce Adaptive Internal Computation (AIC), an iterative policy that learns when to stop refining its latent representation and act. In AIC, we train action selection and stopping jointly, an expected-depth penalty values computation and intermediate value predictions provide auxiliary supervision. We show that when only some states benefit from further refinement, an ideal state-dependent allocator outperforms every state-independent stopping schedule at the same expected depth. With at most eight refinement steps per decision, AIC executes 3.3 steps on average across twelve benchmark tasks and lowers per-decision latency by 31--44% relative to a fixed eight-step policy on four control and robotics tasks. Its mean reward exceeds the best fixed-depth policy on seven tasks and trails it on four. Ablating adaptive stopping and value supervision separately shows that stopping accounts for most of the reward gain on PickCube and AntMaze, where it also executes more refinement steps and that supervision accounts for most of it on RareEvent.

</details>

---

### [[20_Research/Papers/世界模型/The_World_Model_Planning_Accelerator_(WMPA)_Hardware-Algorithm_Co-Design_for_Embedded_AI_in_Robotics|The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics]]

![[assets/2611.10316_figure.png|800]]

- **arXiv**: [2611.10316](https://arxiv.org/abs/2611.10316)
- **PDF**: https://arxiv.org/pdf/2611.10316
- **详细分析**: [[20_Research/Papers/世界模型/The_World_Model_Planning_Accelerator_(WMPA)_Hardware-Algorithm_Co-Design_for_Embedded_AI_in_Robotics|The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics]]
- **作者**: Prerana Ramkumar, Suhas Suresh Bharadwaj, Fazal Hameed
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.52（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.9）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embedded AI is moving from perception to prediction. Robots now use world models$\unicode{x2014}$learned simulators that predict the outcome of candidate actions in a compressed latent space before any is executed. Every predicted step must be computed on board within a tight power and thermal budget, yet the energy these steps fundamentally require, and how far real hardware sits from it, have not been characterized. We derive lower bounds on the arithmetic operations and the CMOS dynamic energy of a latent state transition from information theory and Boolean circuit complexity. Profiling a DreamerV3-style Recurrent State Space Model (RSSM) shows that every rollout operation is memory-bandwidth bound and that a GPU consumes at least $5.9\times10^{10}$ times the CMOS energy floor. Transient 3D thermal simulations show that this inefficiency is also a thermal one, since sustained back-to-back planning heats a millimeter-scale silicon tile to 556 K even behind an ideal copper heat spreader. Guided by this chain from bound to bottleneck, we propose the World Model Planning Accelerator (WMPA), a chip architecture for embedded world model planning that combines near-memory computation, real-time entropy estimation, variable-precision rollout units, and copy-on-write latent scratchpads. With a design target of 40x lower power, the same tile stays near ambient at 306 K in simulation, pointing toward practical planning on thermally constrained robots.

</details>

---

### [[20_Research/Papers/具身智能/Agibot_An_Open-Source_Modular_Swerve-Drive_Robot_Platform_for_Agricultural_Robotics_Research_and_Education|Agibot: An Open-Source Modular Swerve-Drive Robot Platform for Agricultural Robotics Research and Education]]

![[assets/2611.10235_figure.png|800]]

- **arXiv**: [2611.10235](https://arxiv.org/abs/2611.10235)
- **PDF**: https://arxiv.org/pdf/2611.10235
- **详细分析**: [[20_Research/Papers/具身智能/Agibot_An_Open-Source_Modular_Swerve-Drive_Robot_Platform_for_Agricultural_Robotics_Research_and_Education|Agibot: An Open-Source Modular Swerve-Drive Robot Platform for Agricultural Robotics Research and Education]]
- **作者**: Moeen Ul Islam, Bishal Adhikari, Kori Edwards, Lorien Harvey, J. Alex Thomasson, Dong Chen
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.3，大模型 0.1，机器人 1.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Agibot: An Open-Source Modular Swerve-Drive Robot Platform for Agricultural Robotics Research and Education》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agricultural production faces persistent labor shortages and increasing demand for automation, yet progress in agricultural robotics remains constrained by the limited availability of affordable, flexible, and accessible research platforms. This paper presents Agibot, an open-source, modular, low-cost agricultural robotics platform designed for autonomy research and experimentation, with potential applications in hands-on robotics education. The platform integrates four-wheel independent swerve drive, swappable computing, distributed embedded control, multimodal sensing, and configurable manipulation within a unified sense-plan-act-verify framework supporting perception, control, navigation, manipulation, and autonomous task verification. The platform was evaluated through representative row-crop navigation and manipulation tasks under varying lighting and soil conditions. Experiments demonstrated reliable lane following, autonomous row-to-row navigation, target identification, seed dispensing, plant manipulation, and closed-loop verification of task success. Its modular architecture supports independent testing, modification, and validation of autonomy components for rapid prototyping and experimentation. These proof-of-concept tasks, controller-tuning studies, and integrated trials demonstrate the platform's research capabilities, while its accessible and reconfigurable design supports its use for hands-on robotics education. By combining affordability, modularity, open-source accessibility, configurable manipulation, and end-to-end sense-plan-act-verify autonomy, Agibot provides a practical platform for agricultural robotics research, technology development, and workforce training.

</details>

---
