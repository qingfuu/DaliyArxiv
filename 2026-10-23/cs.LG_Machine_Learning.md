# cs.LG | Machine Learning | 2026-10-23

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/强化学习/Same_Luck,_Different_Choice_Twin-World_Credit_Assignment_for_Agentic_Reinforcement_Learning|Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning]]

![[assets/2610.31544_figure.png|800]]

- **arXiv**: [2610.31544](https://arxiv.org/abs/2610.31544)
- **PDF**: https://arxiv.org/pdf/2610.31544
- **详细分析**: [[20_Research/Papers/强化学习/Same_Luck,_Different_Choice_Twin-World_Credit_Assignment_for_Agentic_Reinforcement_Learning|Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning]]
- **作者**: Zeropy Surio, Tobias Engel, Mei-Lin Chou, Anika Raman, Samuel Okafor
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Twin-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of the factual episode, so the outcome difference mixes the effect of the decision with the luck of everything that follows. We observe that in agentic search the retriever, the corpus, and the grader are deterministic, so an episode is a deterministic function of the policy's decisions and its sampling noise. Twin worlds are therefore realizable: the same noise, a different decision. We introduce TWICE (TWIn-world Credit Estimation), which keys the Gumbel noise of every token by turn and line, rolls out counterfactual twins that inherit the factual episode's downstream noise, and turns their paired outcome differences into turn-level advantages for policy-gradient updates on actor-sampled trajectories; only the actor is deployed. Twin credit is unbiased for any coupling quality, its variance is that of an independent counterfactual scaled by $1-ρ$, where $ρ$ is the twins' outcome correlation, and under coupling the number of rollouts needed to resolve an advantage of size $Δ$ falls from $Θ(Δ^{-2})$ to $Θ(Δ^{-1})$. A square-root rule spends the twin budget where outcomes are predicted to disagree per unit cost. On seven question-answering benchmarks, TWICE improves the average exact match of GRPO by 5.3 and 4.5 points on Qwen2.5-3B and 7B, outperforms tree-search and counterfactual-branching baselines, and uses 68% fewer auxiliary tokens than VinePPO.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Robot_Behavior_Priors_from_Non-Robotic_Synthetic_Data|Learning Robot Behavior Priors from Non-Robotic Synthetic Data]]

![[assets/2610.31275_figure.png|800]]

- **arXiv**: [2610.31275](https://arxiv.org/abs/2610.31275)
- **PDF**: https://arxiv.org/pdf/2610.31275
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Robot_Behavior_Priors_from_Non-Robotic_Synthetic_Data|Learning Robot Behavior Priors from Non-Robotic Synthetic Data]]
- **作者**: Mateusz Odrowaz-Sypniewski, Michael Amir, Jasmine Bayrooti, Ajay Shankar, Amanda Prorok
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，机器人 1.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Learning Robot Behavior Priors from Non-Robotic Synthetic Data》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real robot data, rich across tasks and morphologies, is often treated as the bottleneck for training robot learning models, including embodied foundation models that aim for zero-shot physical transfer. In this paper, we investigate the degree to which such models can acquire necessary structure using data from systems without embodiment. To this end, we test if inexpensive, procedurally generated synthetic data can yield useful priors before a model observes any real-world behavior. We study this through robot action prediction, a natural pretraining objective and a direct test of whether structure learned from arbitrary synthetic tasks transfers to embodied settings. We introduce three data generation pipelines that model mathematical abstractions of robotic control, and use them as pretraining priors for a Transformer. We demonstrate that a model trained purely on this non-robotic data attains non-trivial zero-shot prediction performance on unseen physical robot tasks via an in-context learning mechanism, and that our specialized control priors notably improve upon generic causal priors. We also compare against a compute-matched baseline trained on real robot data, and find that it outperforms our model but only on the datasets it was trained on. These findings suggest that procedurally generated, mathematical abstractions can yield useful robotic priors, offering a potential complement to expensive embodied data collection.

</details>

---

### [[20_Research/Papers/大模型/nnInteractive_Agent_General-Purpose_AI_Agents_as_3D_Image_Annotators|nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators]]

![[assets/2610.31080_figure.png|800]]

- **arXiv**: [2610.31080](https://arxiv.org/abs/2610.31080)
- **PDF**: https://arxiv.org/pdf/2610.31080
- **详细分析**: [[20_Research/Papers/大模型/nnInteractive_Agent_General-Purpose_AI_Agents_as_3D_Image_Annotators|nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators]]
- **作者**: Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss, Benjamin Hamm, Philipp Vollmuth, Klaus H. Maier-Hein
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HealthAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpose AI agents can now interpret images, call tools and write code. We show that such agents can take over this work without additional training: the user makes a request in plain language, and the agent works out what has to be segmented, locates the targets, prompts nnInteractive, inspects the 3D result, corrects it and responds to feedback. Asked for 'the muscles used for chewing', an agent identifies and segments the masseters and pterygoids; asked to count liver lesions, it writes its own code to find candidates and splits a merged lesion on request. Our open-source nninteractive-agent provides nnInteractive as tools over the Model Context Protocol (MCP), together with a skill that encodes how experienced users prompt it. On a benchmark spanning CT, MRI, PET and micro-CT of humans, a mouse and an ant (14 images; 51 targets from organs and tumours to muscles, foot bones, vessel trees and an insect brain), Claude Code and Codex reach a mean Dice of 0.81 and 0.84 from the request alone; when told where each target is, both reach 0.85 and prompt nearly as effectively as an oracle that places prompts using the reference segmentation. A text-prompted 3D model (VoxTell) is more accurate on most standard radiological targets but less robust: it returns an empty mask for one of them and fails on the leg muscles, the foot bones, the mouse and the ant, where the agents remain accurate. Code: https://github.com/MIC-DKFZ/nninteractive-agent

</details>

---

### [[20_Research/Papers/强化学习/Ground-Truth-First_Benchmarking_of_Reinforcement_Learning_via_Converse_Optimality_From_Smooth,_Fully_Observed_Systems_to_Non-Smooth_or_Parti|Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks]]

![[assets/2610.30954_figure.png|800]]

- **arXiv**: [2610.30954](https://arxiv.org/abs/2610.30954)
- **PDF**: https://arxiv.org/pdf/2610.30954
- **详细分析**: [[20_Research/Papers/强化学习/Ground-Truth-First_Benchmarking_of_Reinforcement_Learning_via_Converse_Optimality_From_Smooth,_Fully_Observed_Systems_to_Non-Smooth_or_Parti|Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks]]
- **作者**: Grégoire Ouerdane, Sinan Ibrahim, Stefan Streif, Pavel Osinenko
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Benchmarking in reinforcement learning is usually relative: algorithms are ranked by returns on environments with unknown optima. Distance to optimality remains unobservable, while conclusions may depend on reward design, stochasticity, hyperparameters, environment selection, and simulator details. We develop a ground-truth-first framework based on converse optimality, constructing each task with a certified optimal value function and policy withheld from learners and used only for evaluation. The framework unifies two modes: sensitivity benchmarking samples certified environments from continuous-time generators to assess robustness to task variation, while oracle-referenced comparison uses native discrete-time generators to evaluate policies via optimality gap, regret, and policy error. Continuous-time models support physically interpretable sensitivity studies but introduce dependence on the simulator step ($Δt$) and numerical scheme. Native discrete-time models align the environment, oracle, and learner on the same transition law, eliminating external integration choices as a confounder. We reproduce quantitative results covering optimizer sensitivity and oracle-referenced comparisons on serial planar arms, dynamically extended nonholonomic vehicles, and quadrotor-inspired tasks. The methodology extends beyond smooth affine Gaussian systems: virtual-input pullback handles non-affine raw-action interfaces and finite-covariance non-Gaussian disturbances. A non-smooth converse optimality formulation enables certified benchmarks with kinked value functions and switching surfaces. For partially observed evaluation, an information-state formulation reduces benchmarking to converse optimality on a sufficient statistic and provides an information-penalty reference. Code, fixtures, and diagnostics are available on the public project page.

</details>

---

### [[20_Research/Papers/强化学习/Trace2World_Reconstructing_App_Worlds_from_Real_Interaction_Traces_for_Scalable_GUI_Agent_Training|Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training]]

![[assets/2610.30792_figure.png|800]]

- **arXiv**: [2610.30792](https://arxiv.org/abs/2610.30792)
- **PDF**: https://arxiv.org/pdf/2610.30792
- **详细分析**: [[20_Research/Papers/强化学习/Trace2World_Reconstructing_App_Worlds_from_Real_Interaction_Traces_for_Scalable_GUI_Agent_Training|Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training]]
- **作者**: Zezhou Wang, Hanzhang Zhou, Panrong Tong, Quyu Kong, Pengxiang Li, Steven Hoi, Zhuzhong Qian, Yue Wang
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Trace2World: Reconstructing App Worlds from Real Interaction Traces for Scalable GUI Agent Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Agent-World, AndroidWorld, AppWorld, CUA-Gym, MobileGym, PhoneWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling GUI reinforcement learning requires environments that preserve real-app behavior. Yet coupling behavior inference with coding can turn partial traces into runnable mocks with incorrect state transitions. We introduce \textbf{Trace2World}, which separates global behavior reconstruction from implementation. It reconciles traces into a shared, source-linked app model, then compiles an executable environment. Independent replay of source workflows localizes mismatches for bounded implementation repair. Validated worlds then support learner-adaptive task and environment augmentation within source-supported behavior. From 1,570 traces, Trace2World constructs 50 environments. On 200 workflows across ten apps, 91.1% are reproduced end to end, versus 59.8% for the strongest matched task-local baseline. Source-grounded validation retains 94.0% of simulated training gains on real devices, versus 54.7% under self-validation. Learner guidance raises benchmark success from 56.9% to 61.1%. Training in Trace2World further improves the model by 20.2 points on our benchmark, 5.4--16.2 points across four external GUI benchmarks, and 16.3 points on 100 real-device tasks. Reliable reconstruction separates what behavior source evidence supports from whether the implementation preserves it.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Deadline-_and_Energy-Aware_Caching_Algorithms_in_Dynamic_Multi-UAV_Edge_Networks|Adaptive Deadline- and Energy-Aware Caching Algorithms in Dynamic Multi-UAV Edge Networks]]

![[assets/2610.30768_figure.png|800]]

- **arXiv**: [2610.30768](https://arxiv.org/abs/2610.30768)
- **PDF**: https://arxiv.org/pdf/2610.30768
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Deadline-_and_Energy-Aware_Caching_Algorithms_in_Dynamic_Multi-UAV_Edge_Networks|Adaptive Deadline- and Energy-Aware Caching Algorithms in Dynamic Multi-UAV Edge Networks]]
- **作者**: Jian Kim, Ki-Il Kim
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 0.56，世界模型 0.16，机器人 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Adaptive Deadline- and Energy-Aware Caching Algorithms in Dynamic Multi-UAV Edge Networks》归入 机器人、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Content caching via unmanned aerial vehicles (UAVs) becomes one of the solutions to maintain content delivery when terrestrial infrastructure is unavailable or disrupted. However, existing caching approaches often focus primarily on cache-hit performance or average delivery delay, without jointly addressing spatially heterogeneous and time-varying demand, content-specific deadlines, and uneven communication-energy consumption across UAVs. To address these challenges, we formulate a dynamic deadline- and energy-aware cache placement and replacement problem that jointly considers deadline misses, UAV-side communication energy, and inter-UAV energy imbalance. To achieve this, we first develop deadline- and energy-aware UBAC (DE-UBAC), an interpretable hierarchical rule-based realization that incorporates deadline-aware prioritization, cooperative placement, energy-aware coordination, and cache-update cost. However, predefined priorities and thresholds limit its adaptability under dynamically coupled network conditions. We therefore propose GRU-assisted Deadline- and Energy-aware Proximal Policy Optimization (GRU-DEPPO), which combines local and global GRU-based temporal representations with a centralized PPO actor-critic for adaptive cache placement and replacement. Simulation results show that GRU-DEPPO achieves the lowest deadline-miss rate and total UAV-side communication energy among the considered schemes. Compared with DE-UBAC, GRU-DEPPO reduces the deadline-miss rate by approximately 61% and inter-UAV energy imbalance by approximately 40%.

</details>

---

### [[20_Research/Papers/强化学习/Fast_Iterative_Combinatorial_Auctions_via_Deep_Reinforcement_Learning|Fast Iterative Combinatorial Auctions via Deep Reinforcement Learning]]

![[assets/2610.30667_first_page.png|800]]

- **arXiv**: [2610.30667](https://arxiv.org/abs/2610.30667)
- **PDF**: https://arxiv.org/pdf/2610.30667
- **详细分析**: [[20_Research/Papers/强化学习/Fast_Iterative_Combinatorial_Auctions_via_Deep_Reinforcement_Learning|Fast Iterative Combinatorial Auctions via Deep Reinforcement Learning]]
- **作者**: Luis F. Paul Tosta, Quinn Arnold, Gianluca Brero
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Fast Iterative Combinatorial Auctions via Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Iterative combinatorial auctions are used in spectrum allocation, transportation, and industrial procurement, but rounds are costly. We introduce FastCombo, a deep reinforcement learning approach to sequential price discovery. Bayesian pricing has sharply reduced auction rounds even against subgradient benchmarks tuned with hindsight for each instance, but relies on a one-step objective and repeated online inference and optimization. We prove that greedily maximizing immediate clearing probability can require arbitrarily more rounds in expectation than an informative policy, even with the true valuation distribution known. FastCombo learns price policies offline, assigning credit to queries for the future decisions they enable and producing each online price update with a single neural-network forward pass. We formulate the objective of minimizing expected rounds to clearing in single-minded auctions as a partially observable Markov decision process and train a recurrent bidder-item graph policy over complete auction trajectories. In a one-item experiment, all five trained policies learn an informative opening, reducing expected rounds from 1.85 to 1.65 relative to the tested Bayesian one-step rule. Across four domains from the Combinatorial Auction Test Suite, FastCombo achieves competitive clearing while reducing measured online price-selection time per auction by a factor of roughly 300-900 relative to the standard Bayesian baseline. These results demonstrate the value of learning sequential price policies for both information acquisition and online computational efficiency.

</details>

---

### [[20_Research/Papers/大模型/When_News_Gets_Old_Portfolio_Allocation_with_Reinforcement_Learning_and_Large_Language_Models|When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models]]

![[assets/2610.30564_first_page.png|800]]

- **arXiv**: [2610.30564](https://arxiv.org/abs/2610.30564)
- **PDF**: https://arxiv.org/pdf/2610.30564
- **详细分析**: [[20_Research/Papers/大模型/When_News_Gets_Old_Portfolio_Allocation_with_Reinforcement_Learning_and_Large_Language_Models|When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models]]
- **作者**: Bolin Song, Surui Xiang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《When News Gets Old: Portfolio Allocation with Reinforcement Learning and Large Language Models》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial news can influence investment decisions long after publication. Timely news may reach an investor before prices fully adjust, whereas older news may already be reflected in prices. We examine two ways to handle aging signals: retain them and give a portfolio policy timing information, or filter them out before portfolio selection. A fixed large language model (LLM) extracts signals from public SEC disclosures. We compare these treatments in reinforcement learning (RL) policies and LLMs that choose portfolios directly. We evaluate returns after trading costs in historical tests over 2023-2025. RL choices respond to timing information in a controlled test, but historical returns show no consistent benefit from adding it. For the LLM, filtering old news produced the highest average net return, reaching 18.43% per year when news delivery was delayed by four weeks. This exceeded the returns of all RL strategies that used news.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Incentivise_Using_Reinforcement_Learning_for_Sustainable_Urban_Mobility|Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility]]

![[assets/2610.30469_figure.png|800]]

- **arXiv**: [2610.30469](https://arxiv.org/abs/2610.30469)
- **PDF**: https://arxiv.org/pdf/2610.30469
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Incentivise_Using_Reinforcement_Learning_for_Sustainable_Urban_Mobility|Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility]]
- **作者**: Germán Pardo-González, Shaghayegh Vosough, Katerina Papadaki, Claudio Roncoli
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traffic management has traditionally focused on toll-based and road pricing solutions. However, road pricing often raises concerns about accessibility and public dissatisfaction, leading to its prohibition in some places, such as Finland. This study optimises the dynamic allocation of incentives to drivers, encouraging them to reroute onto alternative (potentially longer) paths to achieve greater societal benefit, reduced total travel time (TTT) and total emissions in the transportation network, contributing to sustainable urban mobility. We employ a multi-agent reinforcement learning approach to dynamically assign incentives to drivers to reduce both TTT and emissions, with travel times estimated using traffic simulation software. We demonstrate that, with an unlimited budget and an objective of minimising travel time, the incentive scheme reduces TTT by 16%, compared to the dynamic User-Equilibrium (UE) with a budget equivalent to about 11% of the UE total time. When the goal is to minimise emissions, a 9% reduction in CO2 emissions is observed under an unlimited budget. We demonstrate a critical trade-off: minimising TTT leads to an increase in emissions, while prioritising emission reductions raises TTT. However, with the right combination of weights in the multi-objective function, both TTT and total emissions are improved beyond the baseline.

</details>

---

### [[20_Research/Papers/具身智能/A_Transformer-based_Approach_for_Real-time_Multi-agent_Path_Planning_with_Varying_Initial_Final_Conditions|A Transformer-based Approach for Real-time Multi-agent Path Planning with Varying Initial/Final Conditions]]

![[assets/2610.30388_figure.png|800]]

- **arXiv**: [2610.30388](https://arxiv.org/abs/2610.30388)
- **PDF**: https://arxiv.org/pdf/2610.30388
- **详细分析**: [[20_Research/Papers/具身智能/A_Transformer-based_Approach_for_Real-time_Multi-agent_Path_Planning_with_Varying_Initial_Final_Conditions|A Transformer-based Approach for Real-time Multi-agent Path Planning with Varying Initial/Final Conditions]]
- **作者**: Qian Zhang, Shanqing Liu, Jerome Darbon, George Karniadakis
- **cs 子类**: cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，机器人 0.8）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《A Transformer-based Approach for Real-time Multi-agent Path Planning with Varying Initial/Final Conditions》归入 机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SympOCNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We address the problem of real-time multi-agent path planning under prescribed initial and final configurations, formulated as a high-dimensional optimal control problem subject to inter-agent collision avoidance and obstacle constraints. Classical solvers based on the Hamilton--Jacobi--Bellman equation or Pontryagin's maximum principle (PMP) become computationally intractable as the number of agents grows, due to the curse of dimensionality and the non-convexity introduced by interaction constraints. We propose OCFormer, a transformer-based neural network that parameterizes the inverse of a coordinate transformation mapping a simple, analytically tractable latent space, in which agents evolve independently under a decoupled Hamiltonian, to the physical space of the coupled, interacting system. The model is trained by minimizing a physics-informed loss comprising the Hamiltonian ODE residual from the PMP and a boundary matching term, without requiring pre-computed trajectory data. The self-attention mechanism endows OCFormer with permutation equivariance over agents, a structural symmetry that prior symplectic network approaches do not natively enforce. When trained on a distribution of boundary conditions, the amortized OCFormer produces near-optimal trajectories for unseen initial and final configurations in a single forward pass ($\sim$220ms), enabling real-time inference without retraining. We further introduce a lightweight transfer learning framework that adapts a pretrained OCFormer to out-of-distribution perturbations in seconds via L-BFGS fine-tuning. Numerical experiments on two- and three-dimensional multi-agent navigation with up to 128 agents demonstrate the scalability and efficiency of the proposed approach.

</details>

---
