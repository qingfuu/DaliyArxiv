# cs.LG | Machine Learning | 2026-09-21

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/具身智能/Benchmarking_World_Models_for_Continual_Learning_on_Compositional_Tasks|Benchmarking World Models for Continual Learning on Compositional Tasks]]

![[assets/2609.22055_figure.png|800]]

- **arXiv**: [2609.22055](https://arxiv.org/abs/2609.22055)
- **PDF**: https://arxiv.org/pdf/2609.22055
- **详细分析**: [[20_Research/Papers/具身智能/Benchmarking_World_Models_for_Continual_Learning_on_Compositional_Tasks|Benchmarking World Models for Continual Learning on Compositional Tasks]]
- **作者**: Haoyu Zhou, Joe Watson, Anson Lei, Ingmar Posner
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.52（加权：具身智能 0.6，大模型 0.1，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Benchmarking World Models for Continual Learning on Compositional Tasks》归入 世界模型、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CausalWorld, Meta-World, MetaWorld, RLBench, URL, VIMA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A desirable property of a world model is the ability to learn continually across tasks, adapting to new environments without forgetting what the agent has already learnt. In particular, the ability to retain and reuse knowledge obtained from prior experiences underpins an agent's ability to efficiently adapt to novel environments, as the dynamics of the physical world can often be described in recurring mechanisms. However, the world model's measure of adaptation entangles two abilities: the speed and capacity to learn unseen tasks, and the reuse of knowledge already acquired, since incoming tasks carry novel content alongside what recurs. In order to isolate knowledge reuse from prior experiences, we propose a compositional continual learning benchmark for world models in robot manipulation. Specifically, we design each task curriculum with compositional tasks that combine aspects of the tasks seen in the sequence. We further factorise this composition along the axes of action and perception to better understand how different input modalities bottleneck knowledge reuse. We evaluate state-of-the-art world models under canonical continual learning methods, alongside a modular world model whose dynamics backbone contains explicitly reusable components. Results show that modularity balances reuse against forgetting better than conventional methods, but none solve the problem fully, leaving clear room for continual world models built to reuse without forgetting. More details are available on our project website: this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Kinematics_Benchmarking_Simulation_Fidelity_for_Muscle-Driven_Imitation_Learning|Beyond Kinematics: Benchmarking Simulation Fidelity for Muscle-Driven Imitation Learning]]

![[assets/2609.21909_figure.png|800]]

- **arXiv**: [2609.21909](https://arxiv.org/abs/2609.21909)
- **PDF**: https://arxiv.org/pdf/2609.21909
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Kinematics_Benchmarking_Simulation_Fidelity_for_Muscle-Driven_Imitation_Learning|Beyond Kinematics: Benchmarking Simulation Fidelity for Muscle-Driven Imitation Learning]]
- **作者**: Ayah G. Ahmad, Claire E. Borden, Maegan Tucker
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Beyond Kinematics: Benchmarking Simulation Fidelity for Muscle-Driven Imitation Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MIRL, MyoSim, OpenSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we conduct a systematic comparison of two state-of-the-art motion-imitation reinforcement learning (MIRL) pipelines, one built on SCONE/HyFyDy and one built on MuJoCo/MyoSim. HyFyDy emphasizes physiological realism through detailed musculotendon modeling, while MuJoCo prioritizes computational efficiency and scalable policy learning. While recent work has demonstrated that both pipelines reproduce human kinematics with high fidelity, it remains unclear if they accurately capture the underlying neuromuscular behavior that produced the movement. This limitation is particularly important for robotic assistive-device design and control, where outcome measures such as muscle activation patterns and metabolic cost are often used as optimization targets. To conduct a systematic comparison, our work compares both pipelines using a common set of human motion-capture and electromyography (EMG) measurements. The results find that while both pipelines produce similar kinematics with relative accuracy, the muscle activations from HyFyDy are more aligned with the experimental EMG, as supported by the average pooled (RMSE, r) values for muscle activations from HyFyDy and MuJoCo: (0.164, 0.4) and (0.344, 0.11), respectively. While we conclude that the more advanced physiological realism of HyFyDy currently makes it more suitable for musculoskeletal modeling, both require further development to bring physiological realism to GPU-parallelizable simulation environments and advance robotic assistive device design.

</details>

---

### [[20_Research/Papers/世界模型/Intervention_Granularity_Matters_Coherent_Treatment_Bundles_in_Counterfactual_Simulation_with_Clinical_World_Models|Intervention Granularity Matters: Coherent Treatment Bundles in Counterfactual Simulation with Clinical World Models]]

![[assets/2609.21906_figure.png|800]]

- **arXiv**: [2609.21906](https://arxiv.org/abs/2609.21906)
- **PDF**: https://arxiv.org/pdf/2609.21906
- **详细分析**: [[20_Research/Papers/世界模型/Intervention_Granularity_Matters_Coherent_Treatment_Bundles_in_Counterfactual_Simulation_with_Clinical_World_Models|Intervention Granularity Matters: Coherent Treatment Bundles in Counterfactual Simulation with Clinical World Models]]
- **作者**: Fangzhou Wang, Yixuan Yang, Camilla Balzarotti, Rishikesan Kamaleswaran
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Intervention Granularity Matters: Coherent Treatment Bundles in Counterfactual Simulation with Clinical World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Counterfactual simulation with a clinical world model means fixing a patient's history, changing the treatment, and reading off the predicted response. Doing so requires deciding what counts as one intervention. In clinical settings, interventions are documented as bundles: a co-occurrence audit of 945,707 patient-hours from MIMIC-IV shows groups of components, such as every parameter of a dialysis circuit, that never appear apart, so an edit that changes one component on its own describes an hour that never occurs in the data. We hypothesize that the granularity at which an intervention is edited changes how a world model responds, and test this with Clin-JEPA, a latent world model of patient trajectories conditioned on hourly treatment text. At 1,019 documented onsets of invasive ventilation, we keep the patient's history and other treatments fixed and compare editing one ventilator setting with editing the complete configuration recorded for a real patient with the most similar recent trajectory. The complete bundle moves the predicted next state further than any single setting, consistently across all five settings, and the difference remains after accounting for how much each edit changes the model's input. Intervention granularity therefore materially affects the response of a clinical world model: single-component edits may understate treatment sensitivity, and bundle-aware editing may offer a better-supported basis for counterfactual treatment simulation.

</details>

---

### [[20_Research/Papers/强化学习/From_Pretraining_to_Proficiency_Real-World_Subtask_RL_for_Long-Horizon_Manipulation_with_Minimal_Human_Intervention|From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention]]

![[assets/2609.21788_figure.png|800]]

- **arXiv**: [2609.21788](https://arxiv.org/abs/2609.21788)
- **PDF**: https://arxiv.org/pdf/2609.21788
- **详细分析**: [[20_Research/Papers/强化学习/From_Pretraining_to_Proficiency_Real-World_Subtask_RL_for_Long-Horizon_Manipulation_with_Minimal_Human_Intervention|From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention]]
- **作者**: Sichang Su, Benjamin Yang, Zhiyun Deng, Boyuan Liang, Yip Fun Yeung, Zelin Wang, Lingfeng Sun
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.42（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《From Pretraining to Proficiency: Real-World Subtask RL for Long-Horizon Manipulation with Minimal Human Intervention》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A pretrained robot foundation policy may execute most of a long-horizon task yet repeatedly fail at a few critical subtasks. Collecting additional full-task demonstrations for supervised fine-tuning (SFT) requires operators to repeat behaviors the policy already performs well. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches struggle to solve long-horizon tasks using only sparse rewards. We present PARTS (Policy Adaptation with RL on Targeted Subtasks), a real-world subtask RL framework that concentrates practice at these bottlenecks while allowing training rollouts to proceed with minimal human intervention. The frozen pretrained policy supplies nominal actions throughout execution, while agent-generated selectors and success verifiers activate residual corrections and provide local outcome rewards. These rewards support learning from successful subtasks even when complete-task successes are scarce. Training combines online RL with success-reweighted retraining, and each retrained residual policy is redeployed to collect further experience. Humans identify bottlenecks during setup and perform physical resets when needed. On bimanual YAM and single-arm Franka tasks, PARTS improves complete-task success from 32% to 61% and from 50% to 95%, respectively, using tens of minutes of real-world RL rollouts per task on average. Compared with existing real-world RL fine-tuning methods, PARTS raises full-task success by more than 25% under the same robot-rollout budget while requiring less human involvement.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Rollout_Truncation_Based_on_Epistemic_Uncertainty_for_Efficient_Offline_World_Model_Training|Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training]]

![[assets/2609.21482_figure.png|800]]

- **arXiv**: [2609.21482](https://arxiv.org/abs/2609.21482)
- **PDF**: https://arxiv.org/pdf/2609.21482
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Rollout_Truncation_Based_on_Epistemic_Uncertainty_for_Efficient_Offline_World_Model_Training|Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training]]
- **作者**: Nikodem Sebastian Zymla, Laurin Thiele, Johannes Pitz
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training》归入 世界模型、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate neural world models are central to model-based robotics, where they enable robots to predict future states from previously observed trajectories. Multi-step autoregressive training improves long-horizon prediction, but fixed rollout horizons also increase computational cost and can amplify early training errors when the model is still inaccurate. Existing training schemes typically use the same rollout length throughout optimization, independent of the model's current predictive reliability. We propose an epistemic uncertainty-driven adaptive rollout strategy for offline world model training following an auto-curriculum training scheme. Instead of always unrolling to a fixed horizon, the model terminates autoregressive rollouts once epistemic uncertainty exceeds a threshold calibrated from a warm-up phase. We study two uncertainty estimators: a five-head ensemble with a shared recurrent backbone and Monte Carlo Dropout. A two-stage warm-up procedure stabilizes uncertainty estimates before we enable adaptive truncation. Experiments on ANYmal-D and ANT show that ensemble-based adaptive truncation matches or improves the prediction accuracy of fixed-horizon training and the RWM-U baseline while requiring substantially fewer cumulative rollout steps. Training a world model on ANYmal-D following the presented approach reaches comparable final performance with the baselines with roughly 72% less rollout computation. These results indicate that epistemic uncertainty is useful not only for downstream policy regularization, but also for making world model training itself more compute-efficient.

</details>

---

### [[20_Research/Papers/具身智能/FootQuery_Future-Touchdown-Guided_Retrieval_from_Depth_History_for_Perceptive_Humanoid_Locomotion|FootQuery: Future-Touchdown-Guided Retrieval from Depth History for Perceptive Humanoid Locomotion]]

![[assets/2609.21447_figure.png|800]]

- **arXiv**: [2609.21447](https://arxiv.org/abs/2609.21447)
- **PDF**: https://arxiv.org/pdf/2609.21447
- **详细分析**: [[20_Research/Papers/具身智能/FootQuery_Future-Touchdown-Guided_Retrieval_from_Depth_History_for_Perceptive_Humanoid_Locomotion|FootQuery: Future-Touchdown-Guided Retrieval from Depth History for Perceptive Humanoid Locomotion]]
- **作者**: Tao Dong, Jia Yu, Yuxuan Fan, Linna Zhao, Jiaqi Gong, Andong Yang, Chao Gao, Guyue Zhou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FootQuery: Future-Touchdown-Guided Retrieval from Depth History for Perceptive Humanoid Locomotion》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion over complex terrain requires anticipating footholds that may no longer be visible at touchdown. Limited camera coverage and self-occlusion make it necessary to retrieve relevant terrain information from earlier observations. We present FootQuery, a perceptive locomotion framework that queries depth history using each foot's predicted next touchdown. The policy predicts touchdown locations and uncertainty from proprioception and uses these distributions, together with per-foot features, to query sparsely sampled historical depth frames. During training, realized contacts are projected into historical images to supervise retrieval at the regions where those contacts were visible. The retrieved per-foot features are fused with global visual memory to generate control actions. A progressive force-assistance curriculum supports early exploration, while event-consistent tread-midline shaping encourages coordinated stair contacts. Deployment requires only proprioception and onboard depth images. In simulation, the complete framework outperforms its component ablations on the most challenging tested stairs, gaps, and platforms. Real-world experiments on a Unitree G1 demonstrate continuous traversal with a single policy across outdoor stairs and indoor routes combining stair ascent and descent, platforms, and gaps. These results support organizing visual history around anticipated contacts for perceptive humanoid locomotion.

</details>

---

### [[20_Research/Papers/强化学习/REFINEPPO_Learning_Continuous_Control_Policies_by_Iterative_Action_Refinement|REFINEPPO: Learning Continuous Control Policies by Iterative Action Refinement]]

![[assets/2609.21108_figure.png|800]]

- **arXiv**: [2609.21108](https://arxiv.org/abs/2609.21108)
- **PDF**: https://arxiv.org/pdf/2609.21108
- **详细分析**: [[20_Research/Papers/强化学习/REFINEPPO_Learning_Continuous_Control_Policies_by_Iterative_Action_Refinement|REFINEPPO: Learning Continuous Control Policies by Iterative Action Refinement]]
- **作者**: Sachini Weerasekara, Sagar Kamarthi, Jacqueline Isaacs
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《REFINEPPO: Learning Continuous Control Policies by Iterative Action Refinement》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) has achieved strong performance across a wide range of continuous-control problems. These continuous-control policies, however, are often defined as direct mappings from an observed state to an action or action distribution, requiring a single feed-forward network to construct an optimal control decision in one pass. While effective, this formulation leaves little opportunity for the policy to reconsider or progressively improve an action once an initial prediction has been formed. In this work, we explore an alternative approach: rather than learning only to directly predict an action, can a policy learn to iteratively improve one, and can this iterative process provide advantages during policy learning? We introduce Iterative Action Refinement (IAR), an iterative action-construction method that constructs control actions through a sequence of learned residual corrections. Starting from an initial proposal, a shared refinement network repeatedly conditions on the observed state and the current action proposal, allowing each refinement step to revise the action constructed by preceding steps. The final refined proposal is then used to determine the action executed by the agent. We integrate this iterative action-construction mechanism with Proximal Policy Optimization (PPO), yielding REFINEPPO. We evaluate REFINEPPO across 14 benchmark control tasks, complemented by controlled ablations of refinement depth and update schedules and analyses aimed at understanding why iterative refinement is effective. Across these environments, REFINEPPO matches or exceeds the performance of standard PPO while demonstrating faster convergence on several tasks.

</details>

---

### [[20_Research/Papers/强化学习/Efficient_Bayes-Adaptive_Reinforcement_Learning_with_Temporal_Logic_Specifications|Efficient Bayes-Adaptive Reinforcement Learning with Temporal Logic Specifications]]

![[assets/2609.20954_first_page.png|800]]

- **arXiv**: [2609.20954](https://arxiv.org/abs/2609.20954)
- **PDF**: https://arxiv.org/pdf/2609.20954
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_Bayes-Adaptive_Reinforcement_Learning_with_Temporal_Logic_Specifications|Efficient Bayes-Adaptive Reinforcement Learning with Temporal Logic Specifications]]
- **作者**: Jonathan Hau, Alessandro Abate
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Efficient Bayes-Adaptive Reinforcement Learning with Temporal Logic Specifications》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BA-LCRL, LCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a novel end-to-end model-based Reinforcement Learning (RL) algorithm for efficient policy synthesis under given Linear Temporal Logic (LTL) specifications (e.g., safety or reachability) in unknown environments. To do so, a Limit-Deterministic B{ü}chi Automaton (LDBA) representation of the LTL task is synchronised with a Bayes-Adaptive Markov Decision Process (BAMDP) representation of the environment, which allows us to leverage an enhanced exploration-exploitation trade-off that is achieved via Bayesian RL, as opposed to traditional non-Bayesian approaches. We further propose a novel Bayes-Adaptive Monte-Carlo Planning (BAMCP) algorithm to allow for approximate Bayes-optimal strategy synthesis in the synchronised BAMDP construct. A range of finite- and infinite-horizon task experiments demonstrate the effectiveness of our approach in terms of both property satisfaction and sample efficiency, when compared to traditional model-free approaches. Additional ablation studies also successfully highlight the value of the novel BAMCP algorithm in comparison to classical BAMCP for LTL task satisfaction. Finally, we also showcase a successful application of our approach for \textit{cautious} RL, namely to reduce the number of task violations incurred during policy training.

</details>

---

### [[20_Research/Papers/强化学习/Continuous_Delayed-Memory_Stochastic_Gradient_Descent_and_Continuous-Time_Reinforcement_Learning_from_History_of_Astrophysical_Time_Series_S|Continuous Delayed-Memory Stochastic Gradient Descent and Continuous-Time Reinforcement Learning from History of Astrophysical Time Series Studies]]

![[assets/2609.20906_figure.png|800]]

- **arXiv**: [2609.20906](https://arxiv.org/abs/2609.20906)
- **PDF**: https://arxiv.org/pdf/2609.20906
- **详细分析**: [[20_Research/Papers/强化学习/Continuous_Delayed-Memory_Stochastic_Gradient_Descent_and_Continuous-Time_Reinforcement_Learning_from_History_of_Astrophysical_Time_Series_S|Continuous Delayed-Memory Stochastic Gradient Descent and Continuous-Time Reinforcement Learning from History of Astrophysical Time Series Studies]]
- **作者**: Debartha Paul, Juncheng Yi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Continuous Delayed-Memory Stochastic Gradient Descent and Continuous-Time Reinforcement Learning from History of Astrophysical Time Series Studies》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quasars are luminous objects in the universe that exhibit stochastic brightness variations encoding information about the supermassive black holes powering them, and modeling these variations from ground-based survey data time series, known as light curves, is a statistical challenge. This paper reviews how stochastic differential equations (SDEs) have been adapted with neural network parameterizations to overcome this challenge in history. We create the Continuous-Delayed-Memory Stochastic Gradient Descent which depend on the past state of the discrete iteration process. We performed the simulation on some 2-dimensional landscape and observed some wider-exploration and more precise convergent behavior compared to Vanilla SGD by adjusting hyperparameters. Besides, we proposed a reinforcement learning structure with continuous time policy gradients for exploratory policies without solving HJB PDE, and we show that its optimality conditions recover the Gibbs policy of previous works.

</details>

---
