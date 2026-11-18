# cs.LG | Machine Learning | 2026-11-16

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Training_Reasoning_Models_in_Simulation_to_Natively_Use_Real_Robots|Training Reasoning Models in Simulation to Natively Use Real Robots]]

![[assets/2611.18562_figure.png|800]]

- **arXiv**: [2611.18562](https://arxiv.org/abs/2611.18562)
- **PDF**: https://arxiv.org/pdf/2611.18562
- **详细分析**: [[20_Research/Papers/具身智能/Training_Reasoning_Models_in_Simulation_to_Natively_Use_Real_Robots|Training Reasoning Models in Simulation to Natively Use Real Robots]]
- **作者**: Jiaming Tang, Zhuoyang Zhang, Junxian Guo, Fangzhou Zhao, Yilong Zhao, Zekai Li, Xingyang Li, Yuyang Zhao, Song Bian, Zhijian Liu, Song Han
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.6，大模型 0.3，强化学习 0.36，世界模型 0.16，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Training Reasoning Models in Simulation to Natively Use Real Robots》归入 机器人、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgenticRoboRL, DigiRL, ERQA, GPQA, IFBench, LiveCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-use agents (RUAs) have emerged as a promising approach to general-purpose robot control. However, strong performance has so far been achieved only by frontier proprietary models such as GPT-6 Astra and Claude Fable 5.2, whereas open-weight models remain substantially less capable. We show that an open-weight 27B reasoning model can be trained to use real robots natively through reinforcement learning, entirely in simulation and without demonstrations. Like a computer-use agent (CUA), the model observes the environment, reasons in a chain of thought, and generates the next end-effector pose, without any harness. We build a Post-training Engine for Agentic Robotics (PEAR) and use it to train the model on simulated robot tasks at scale with robot-use reinforcement learning (RURL), mirroring how frontier models acquire computer use. We find that the skills acquired in simulation generalize well beyond the training tasks: they transfer to an unseen robot, to the real world, and to novel instructions. After training on LIBERO and RoboDojo in simulation, the model succeeds in 60% of our trials on a real dual-arm robot, whereas the base model succeeds in none. On LIBERO, training raises the success rate from 1.6% to 74.4%, approaching GPT-6 Astra and GPT-6.1 Sol at maximum reasoning effort. Compared with $π_{0.5}$, a vision-language-action model fine-tuned on demonstrations, our model is substantially more robust to changes in the task itself. On LIBERO-Pro, $π_{0.5}$ succeeds in only 0.75% of episodes when assigned a new task in a familiar scene whereas our model succeeds in 57.4%. Finally, the model retains its general capabilities, with no measurable degradation on nine reasoning, coding and vision benchmarks. These results highlight robot-use reinforcement learning as a promising component of foundation-model post-training.

</details>

---

### [[20_Research/Papers/强化学习/On_numerical_issues_of_divergences_between_nearly_equal_distributions|On numerical issues of divergences between nearly equal distributions]]

![[assets/2611.18511_first_page.png|800]]

- **arXiv**: [2611.18511](https://arxiv.org/abs/2611.18511)
- **PDF**: https://arxiv.org/pdf/2611.18511
- **详细分析**: [[20_Research/Papers/强化学习/On_numerical_issues_of_divergences_between_nearly_equal_distributions|On numerical issues of divergences between nearly equal distributions]]
- **作者**: Brandon Amos
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《On numerical issues of divergences between nearly equal distributions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Barron et al. (2026) recently identified numerical issues in the softmax and soft cross-entropy loss. We show that similar issues are present in standard divergence operations between categorical distributions. This includes the forward and reverse Kullback-Leibler (KL) divergence and generalized Jensen-Shannon divergence (JSD), as well as Monte Carlo KL estimates and entropy. When the distributions are nearly equal, rounding and cancellation issues affect the forward and gradient computations. These issues can affect settings using divergences in optimization objectives, such as knowledge distillation, reinforcement learning, and proximal methods. We propose numerically stable reformulations and provide example implementations for each setting, validated by property-based tests.

</details>

---

### [[20_Research/Papers/大模型/WeatherDreamer_Learning_a_World_Model_from_Multimodal_Earth_Observations|WeatherDreamer: Learning a World Model from Multimodal Earth Observations]]

![[assets/2611.18393_figure.png|800]]

- **arXiv**: [2611.18393](https://arxiv.org/abs/2611.18393)
- **PDF**: https://arxiv.org/pdf/2611.18393
- **详细分析**: [[20_Research/Papers/大模型/WeatherDreamer_Learning_a_World_Model_from_Multimodal_Earth_Observations|WeatherDreamer: Learning a World Model from Multimodal Earth Observations]]
- **作者**: Kate Duffy, Elise Penn, Tristan Ballard, August Posch, Thomas J. Vandal
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Multimodal, WorldModel, Systems

#### 研究背景与动机

《WeatherDreamer: Learning a World Model from Multimodal Earth Observations》归入 世界模型、大模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EarthNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Machine learning weather models now rival operational global forecasts but still start from analyses produced by separate, expensive data assimilation (DA) systems, which for global models are typically updated every six hours. Observation-to-observation models avoid this dependence, but most omit the recursive filtering cycle that lets DA systems carry a background state through sparse, irregular observations. We introduce WeatherDreamer, a world model that learns this cycle end-to-end from 18 global observing systems, without reanalysis. It infers a latent state from observations, carries it forward hour by hour with learned dynamics, corrects it each hour with new observations, and can predict what any of its observing systems would measure at any location. At held-out stations, its ensembles beat NOAA's Global Ensemble Forecast System (GEFS) for temperature, dew point and wind out to 12 h and are better calibrated than GEFS and the ECMWF ensemble. Precipitation, cloud-top height and solar irradiance, never inputs at inference, are inferred with skill matching or exceeding operational products at short leads. Against the first guess of NOAA's Gridpoint Statistical Interpolation (GSI) DA system, WeatherDreamer's short-range departures are within 10% of GSI's at surface stations and within 25% for moisture-sensitive microwave channels, but up to five times larger for temperature-sounding channels. Never given observation errors, its learned update assumes errors close to known instrument and retrieval errors of microwave sounders and scatterometer winds. WeatherDreamer also separates viewing geometry from atmospheric state, recovering 83-96% of observed limb darkening and producing seamless nadir-view imagery. Producing an hourly global analysis in about 1.5 minutes on one GPU, WeatherDreamer shows that assimilation and forecasting can be learned together directly from observations.

</details>

---

### [[20_Research/Papers/强化学习/Enrichment-Oriented_Virtual_Screening_of_Perovskite_Solar_Cells_through_Reinforcement_Learning|Enrichment-Oriented Virtual Screening of Perovskite Solar Cells through Reinforcement Learning]]

![[assets/2611.18043_figure.jpg|800]]

- **arXiv**: [2611.18043](https://arxiv.org/abs/2611.18043)
- **PDF**: https://arxiv.org/pdf/2611.18043
- **详细分析**: [[20_Research/Papers/强化学习/Enrichment-Oriented_Virtual_Screening_of_Perovskite_Solar_Cells_through_Reinforcement_Learning|Enrichment-Oriented Virtual Screening of Perovskite Solar Cells through Reinforcement Learning]]
- **作者**: Yezeyuan Zheng, Ziyang Hu, Maojun Sun. Ruijian Han, Jian Huang, Guanhua Chen, Jie Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Enrichment-Oriented Virtual Screening of Perovskite Solar Cells through Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experimental optimization of perovskite solar cells is constrained by combinatorial diversity in absorber compositions, device layers, and processing, which makes virtual screening attractive for prioritizing recipes before fabrication. We develop a surrogate-guided reinforcement-learning framework that casts recipe generation as virtual screening, enriching candidate shortlists near high-performing experimental neighbors. A frozen Tabular Prior-data Fitted Network (TabPFN) guides recipe generation, while a reference pool of 890 measured devices enables neighborhood-based assessment. Five-fold evaluation on 1,846 devices shows top-ten selection raises mean power conversion efficiency (PCE) from 19.68\% to 23.74\%. Three learned policies are compared with six baselines under 3,000 surrogate evaluations per run. In top-100 shortlists, Proximal policy optimization (PPO) and recurrent PPO (RPPO) achieve neighborhood-supported hit rates of 23\% and 24\% (7.9- and 8.3-fold Pure Random's 2.9\%), versus 10\% (3.4-fold) for the baselines with the highest supported hit rate (L-SHADE and Ax BO, tied) at $K = 100$. Gains coexist with weak-support fractions. Of 9,000 recipes, 65.4\% match a composition family at similarity 0.80, falling to 11.7\% at 0.90. Results support enrichment-oriented prioritization but not experimental performance, seed robustness, or matched-budget advantage.

</details>

---

### [[20_Research/Papers/大模型/A_Generalizable_Approach_to_Safety-Aware_Robotic_Behavior_Planning_with_an_Explicit_Constraint_Space|A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space]]

![[assets/2611.18026_figure.png|800]]

- **arXiv**: [2611.18026](https://arxiv.org/abs/2611.18026)
- **PDF**: https://arxiv.org/pdf/2611.18026
- **详细分析**: [[20_Research/Papers/大模型/A_Generalizable_Approach_to_Safety-Aware_Robotic_Behavior_Planning_with_an_Explicit_Constraint_Space|A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space]]
- **作者**: Xianxu Wu, Shang-Ching Liu, Zhaocong Liang, Hengxiang Chen, Yujian Ma, Shenwen Deng, Qiang Li, Jianwei Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language and vision-language models have substantially advanced robotic behavior planning from natural-language instructions and visual observations. However, safe manipulation in tabletop environments remains challenging because the safety constraints required for a task depend on the surrounding scene and may not be explicitly specified in the instruction. We propose a safety-aware behavior planning framework based on an explicit Constraint Space that stores reusable textual safety rules. Rather than retrieving rules solely by semantic similarity, we formulate constraint selection as task- and environment-conditioned applicability learning. A lightweight query-conditioned dual-tower model identifies the constraints applicable to the current context, which are then provided together with the original task and image to a multimodal behavior planner. To handle incorrect constraint selections and previously unseen hazards, we introduce a multimodal Safety Inspector that evaluates generated primitive plans, reconstructs the complete applicable constraint set, and provides corrective planning feedback. Validated inspection feedback is further used for test-time adaptation of constraint applicability and parameter-efficient adaptation of the Safety Inspector through LoRA, while newly identified constraints are incorporated into the Constraint Space. The resulting framework integrates explicit safety knowledge representation,context-aware constraint selection, corrective safety inspection, and test-time knowledge adaptation for safety-aware robotic behavior planning.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Prediction_Gain_LASR_as_a_Metric_for_Action-Grounded_Latents_in_World_Models|Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models]]

![[assets/2611.17775_figure.png|800]]

- **arXiv**: [2611.17775](https://arxiv.org/abs/2611.17775)
- **PDF**: https://arxiv.org/pdf/2611.17775
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Prediction_Gain_LASR_as_a_Metric_for_Action-Grounded_Latents_in_World_Models|Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models]]
- **作者**: Yu Zhou, Changsong Lei, Yixiang Wei, Kairui Wen, Huankun Sheng, Ming Li, Yeying Fan, Yu-Hui Wen, Yong-Jin Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GenEval, UniVLA, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models that support planning, control, and interpretable reasoning require latent representations that genuinely encode action. Yet the large-scale video data from which such models are learned overwhelmingly lack action annotations. Latent-action models infer action-like variables from observation sequences, enabling action-aware learning from unlabeled videos or trajectories. A fundamental concern, however, remains: a latent that improves future prediction may simply encode the current state, episode progress, task identity, or other predictive shortcuts. Existing evaluation practices---reconstruction loss, rollout fidelity, action recovery, or downstream performance---cannot isolate this distinction. We introduce the Latent Action Support Ratio (LASR), a dimensionless metric that measures, under offline evaluation on held-out data, whether a learned latent provides predictive support for action-related targets beyond the current state and non-action alternatives. LASR provides two complementary summaries: GeoLASR captures typical support, while WorstLASR identifies the weakest case. We instantiate the LASR benchmark with recorded actions and corresponding physical state changes as targets, episode-held-out splits, one predictor type for all comparisons, and positive and negative controls. Experiments on recorded robot manipulation data and a matched multi-task panel demonstrate that LASR detects known action information, rejects representative non-action shortcuts, and enables graded comparisons among imperfect latent representations. We further use LASR to train and audit a lightweight residual adapter, obtaining descriptively better point estimates whose uncertainty is assessed with paired comparisons. LASR thus provides a principled offline protocol for measuring action-related predictive support in world-model latents.

</details>

---

### [[20_Research/Papers/强化学习/Joint_World_Action_Models_through_Differentiable_Trajectory_Optimization|Joint World Action Models through Differentiable Trajectory Optimization]]

![[assets/2611.17626_figure.png|800]]

- **arXiv**: [2611.17626](https://arxiv.org/abs/2611.17626)
- **PDF**: https://arxiv.org/pdf/2611.17626
- **详细分析**: [[20_Research/Papers/强化学习/Joint_World_Action_Models_through_Differentiable_Trajectory_Optimization|Joint World Action Models through Differentiable Trajectory Optimization]]
- **作者**: Mintae Kim, Koushil Sreenath
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.52（加权：强化学习 0.16，世界模型 0.36）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Joint World Action Models through Differentiable Trajectory Optimization》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint world action models (WAMs) generate future actions and states together, modeling world-action trajectories rather than actions alone. However, trajectory imitation does not ensure that these trajectories are task-effective or consistent with dynamics. We present \textbf{world action trajectory optimization (WATO)}, which optimizes generated actions and future states jointly for control. WATO uses both as references in a dynamics-constrained trajectory optimization problem and differentiates the task loss through the optimized trajectory to train the generator. This makes generated trajectories task-aware and dynamics-consistent while using trajectory optimization only during training. At deployment, WATO directly generates candidate trajectories and ranks them with a world model, without iterative trajectory optimization. Across $7$ visual control environments, WATO improves average success from $79.9\%$ for the imitation joint WAM to $91.7\%$, outperforming strong model-based, goal-conditioned RL, and generative control baselines. Compared with cross-entropy method (CEM), WATO is on average $11.5\times$ faster and uses $600.5\times$ fewer world model evaluations at deployment.

</details>

---

### [[20_Research/Papers/强化学习/Offline_KL-Regularized_Reinforcement_Learning_with_Stochastic_Transitions|Offline KL-Regularized Reinforcement Learning with Stochastic Transitions]]

![[assets/2611.17603_first_page.png|800]]

- **arXiv**: [2611.17603](https://arxiv.org/abs/2611.17603)
- **PDF**: https://arxiv.org/pdf/2611.17603
- **详细分析**: [[20_Research/Papers/强化学习/Offline_KL-Regularized_Reinforcement_Learning_with_Stochastic_Transitions|Offline KL-Regularized Reinforcement Learning with Stochastic Transitions]]
- **作者**: Andrew Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Offline KL-Regularized Reinforcement Learning with Stochastic Transitions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

KL-regularized reinforcement learning is the objective behind RL fine-tuning of language models, and its data are often collected by the reference policy itself. However, beyond bandits and deterministic transitions, little is known about how much offline data it needs. In this work, we study finite discounted Markov decision processes with unknown stochastic transitions, $K$ state-action pairs and effective horizon $H$. For data that cover the regularized optimum with concentrability $C\geq 4$, every estimator needs $Ω(KCH^3/(ε\max\{ε,β\}))$ samples on some instances when $ε$ is small, where $β$ is the temperature. Under a fixed design, pessimistic soft value iteration with a variance-aware penalty attains this rate with high probability, up to logarithmic factors, when $β\geq 1.4H$. When the data come from the reference policy itself, we show that it covers the optimum up to a power law whose exponent grows as $H/β$; in the same temperature range, this power law alone gives the estimator a sample complexity polynomial in $1/ε$, with no coverage assumption. For $β\geq H$ the power can also increase the sample size needed by a factor polynomial in $1/ε$. Finally, the plug-in estimator, which is minimax optimal with a generative model, can fail on reference data at small temperatures when many actions are rarely seen, while the pessimistic estimator does not.

</details>

---

### [[20_Research/Papers/世界模型/Learning_Latent_Goal_Costs_for_Visual_World-Model_Planning_with_an_Expanding_Curriculum|Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum]]

![[assets/2611.17529_figure.png|800]]

- **arXiv**: [2611.17529](https://arxiv.org/abs/2611.17529)
- **PDF**: https://arxiv.org/pdf/2611.17529
- **详细分析**: [[20_Research/Papers/世界模型/Learning_Latent_Goal_Costs_for_Visual_World-Model_Planning_with_an_Expanding_Curriculum|Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum]]
- **作者**: Konstantinos Mylonas, Thrasyvoulos Spyropoulos
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.72（加权：强化学习 0.16，世界模型 0.56）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Image-goal planning with a frozen visual world model depends on how predicted observations are scored against the goal. Mean-squared error (MSE) between embeddings from a pretrained visual encoder can provide a useful signal near a goal, yet favor states across an obstacle that are visually similar to the goal and difficult to reach. We fit a small residual adapter on top of frozen I-JEPA embeddings to improve this latent goal cost. Starting near each goal, a planner collects trajectories from progressively wider regions of initial states. The adapter learns from the order of observations along successful trajectories, with additional comparisons inferred from failed rollouts. No task-specific progress labels are used for fitting, so the procedure can be applied to other goal-reaching tasks. DotWall and PointMaze are used in this work. In paired 50-case evaluations with identical starts, goals, world models, and planner settings, success increases from 54% to 98% in DotWall and from 82% to 96% in PointMaze. On 16 unseen DotWall layout-goal cases, the adapter fitted on one fixed layout improves agreement between latent-cost ordering and shortest legal-path ordering from 71.9% to 85.8%. The results indicate that planning experience can improve a frozen visual representation's goal cost without retraining the encoder or the world model.

</details>

---

### [[20_Research/Papers/强化学习/Improved_Regret_via_Variance-Aware_Policy_Optimization_in_Adversarial_MDPs|Improved Regret via Variance-Aware Policy Optimization in Adversarial MDPs]]

![[assets/2611.17469_first_page.png|800]]

- **arXiv**: [2611.17469](https://arxiv.org/abs/2611.17469)
- **PDF**: https://arxiv.org/pdf/2611.17469
- **详细分析**: [[20_Research/Papers/强化学习/Improved_Regret_via_Variance-Aware_Policy_Optimization_in_Adversarial_MDPs|Improved Regret via Variance-Aware Policy Optimization in Adversarial MDPs]]
- **作者**: Ofir Schlisselberg, Alon Cohen, Yishay Mansour
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Improved Regret via Variance-Aware Policy Optimization in Adversarial MDPs》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study episodic adversarial MDPs with unknown dynamics and full-information rewards and achieve regret with leading term $\widetilde O(\sqrt{H^3SAK})$. Here $H$ is the horizon, $S$ the total number of states across decision layers, $A$ the number of actions, and $K$ the number of episodes. This improves the two incomparable prior leading terms by factors $\sqrt{S/H}$ and $\sqrt{H^3}$, leaving a factor $\sqrt H$ to the lower-bound scale. We give a reduction from unknown to known dynamics for \emph{downstream-dependent} algorithms, whose policy at step $h$ is computed only from information at steps $h+1$ and onward. This reduces the remaining leading-order gap to finding a downstream-dependent known-dynamics algorithm with $\widetilde O(H\sqrt K)$ regret, which would yield the tight $\widetilde O(H\sqrt{SAK})$ leading term for unknown dynamics. We instantiate the reduction with VOPO, a policy optimization (PO) algorithm. Its improved guarantees follow from a variance-aware analysis enabled by a novel bonus, which we call the Stability-Matching Bonus (SMB). VOPO achieves $\widetilde O(\sqrt{H^3K})$ regret under known dynamics with full information; its $\sqrt H$ gap to the target $H\sqrt K$ rate is inherited by our unknown-dynamics guarantee. We also show that with known dynamics and trajectory bandit feedback, VOPO achieves $\widetilde O(\sqrt{H^2SAK})$ regret. Both known-dynamics guarantees improve the corresponding state-of-the-art PO bounds by a factor $\sqrt H$. A matching lower bound establishes that the full-information rate is tight in one parameter regime.

</details>

---
