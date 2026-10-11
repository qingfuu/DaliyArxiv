# cs.RO | Robotics | 2026-10-09

#arxiv #ComputerScience

**论文数**: 41

### [[20_Research/Papers/具身智能/SpatialHarness_Test-Time_Spatial_Scaffolding_for_Fine_Robotic_Manipulation|SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation]]

![[assets/2610.12457_figure.png|800]]

- **arXiv**: [2610.12457](https://arxiv.org/abs/2610.12457)
- **PDF**: https://arxiv.org/pdf/2610.12457
- **详细分析**: [[20_Research/Papers/具身智能/SpatialHarness_Test-Time_Spatial_Scaffolding_for_Fine_Robotic_Manipulation|SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation]]
- **作者**: Jiayu Wang, Yue Yu, Bin Zhu, Zhiyao Yang, Jingjing Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.5（加权：具身智能 2.1，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ActiveVLA, OpenVLA, Real-is-Sim, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier multimodal foundation models (e.g., GPT-6 Astra) have recently shown strong potential for direct robotic control, yet their performance on fine manipulation remains limited. We argue that an important source of failure is not necessarily insufficient policy capability, but insufficient spatial observability, where task-critical spatial relationships may be poorly revealed by the existing physical camera setup. We introduce SpatialHarness, a test-time embodied harness that provides test-time spatial scaffolding for fine robotic manipulation without policy fine-tuning or changes to the physical sensing setup. SpatialHarness maintains an online simulated scene synchronized with real-world execution, identifies task-critical spatial relationships, and renders complementary virtual views that expose them to a frozen multimodal policy. To keep the simulated scene aligned during interaction, we develop interaction-aware scene synchronization that distinguishes static, held, and transition modes. We evaluate SpatialHarness on four real-robot manipulation tasks spanning precise geometric alignment, object-relative placement, and articulated-object interaction. Using the same frozen GPT-6 Astra policy, SpatialHarness substantially improves task success, including from 26.7% to 66.7% on plug insertion and from 0% to 100% on Tower of Hanoi. These results indicate that improving spatial observability at test time can unlock fine-manipulation capabilities already present in strong multimodal foundation models. Project website: https://emilia113.github.io/SpatialHarness/.

</details>

---

### [[20_Research/Papers/强化学习/Generative_Neural_Retargeting_for_Human-to-Robot_Dexterous_Manipulation|Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation]]

![[assets/2610.12440_figure.png|800]]

- **arXiv**: [2610.12440](https://arxiv.org/abs/2610.12440)
- **PDF**: https://arxiv.org/pdf/2610.12440
- **详细分析**: [[20_Research/Papers/强化学习/Generative_Neural_Retargeting_for_Human-to-Robot_Dexterous_Manipulation|Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation]]
- **作者**: Dechen Gao, Yue Yang, Ben Abbatematteo, Nathan Godwin, Pengcheng Wang, Roger Boldu, Steven Man, Zhiyang Dou, Chuan Qin, Sho Nakagome, Eric Whitmire
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.4，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations are a scalable data source for learning dexterous manipulation, but the embodiment gap prevents human motion from being executed directly on robots. Inverse kinematics (IK) retargets human motion to robots efficiently but ignores dynamics, often producing infeasible motions. Reinforcement learning (RL) and sampling-based model predictive control (MPC) are commonly employed to yield dynamically feasible motions, but both are sample-inefficient and sensitive to hyperparameters. RL suffers from costly and unstable training and tedious reward engineering; MPC avoids policy optimization, yet retargets each trajectory in isolation, and solving one does not make the next easier. Sampling cost grows rapidly with dataset size and task difficulty. We hypothesize that dynamically feasible trajectories concentrate near a low-dimensional manifold shared across demonstrations, so that retargeting can be reduced to sampling from that manifold, conditioned on human motion, rather than solving a fresh optimization problem for every demonstration. We propose \textbf{Generative Neural Retargeting} (GNR), which uses a flow matching model to sample feasible trajectories. GNR outperforms MPC with only $8.5\%$ of the samples required by MPC, achieving a success rate of $56.20\%$ compared to $27.20\%$ for MPC. GNR can be used for scalable and efficient retargeting of large-scale, long-horizon, and millimeter precision human demonstrations: by applying GNR within a real-to-sim data engine, we produce a dexterous manipulation dataset with dense contact-force labels, spanning $223$k demonstrations and $3.3$k object geometries.

</details>

---

### [[20_Research/Papers/机器人/A_Physics-Informed_Collision_Learning_Framework_for_Collaborative_Robot_Motion_Generation|A Physics-Informed Collision Learning Framework for Collaborative Robot Motion Generation]]

![[assets/2610.12404_figure.png|800]]

- **arXiv**: [2610.12404](https://arxiv.org/abs/2610.12404)
- **PDF**: https://arxiv.org/pdf/2610.12404
- **详细分析**: [[20_Research/Papers/机器人/A_Physics-Informed_Collision_Learning_Framework_for_Collaborative_Robot_Motion_Generation|A Physics-Informed Collision Learning Framework for Collaborative Robot Motion Generation]]
- **作者**: Chen Cai, Steven Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《A Physics-Informed Collision Learning Framework for Collaborative Robot Motion Generation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PairwiseNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Close-proximity multi-arm manipulation requires collision models that are both geometrically accurate and differentiable enough for real-time optimization. Classical geometry checkers provide reliable distances but are difficult to use inside gradient-based model predictive control, while conservative proxy models can restrict tightly coupled motion. We present PI-UDF, a physics-informed unified differentiable framework for body-to-body collision distance prediction between articulated robots. PI-UDF combines analytical forward kinematics with learnable link-geometry embeddings and a shared residual network to predict pairwise inter-arm distances directly from robot configurations. To improve safety-critical fidelity, we combine quota-driven boundary mining with an asymmetric boundary-crossing penalty that emphasizes false-safe sign errors near the collision boundary. The learned distance field is integrated into nonlinear MPC as a differentiable inter-arm clearance term. We validate the framework on a real dual-Franka platform through high-speed close-proximity 14-DoF dual-arm swapping, sustained single-arm dynamic evasion, and dynamic-evasion planning configurations with frozen, predicted, and target-switching treatments of the moving arm. Hardware experiments and offline Drake/FCL replay show that PI-UDF provides a differentiable inter-arm clearance estimate suitable for closed-loop collision-aware collaborative robot motion generation.

</details>

---

### [[20_Research/Papers/具身智能/LiteNWM_Efficient_Latent_World_Models_for_Onboard_Visual_Navigation_in_the_Wild|LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild]]

![[assets/2610.12368_figure.png|800]]

- **arXiv**: [2610.12368](https://arxiv.org/abs/2610.12368)
- **PDF**: https://arxiv.org/pdf/2610.12368
- **详细分析**: [[20_Research/Papers/具身智能/LiteNWM_Efficient_Latent_World_Models_for_Onboard_Visual_Navigation_in_the_Wild|LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild]]
- **作者**: Linkai Liu, Yuntian Zhang, Zhenshan Bing, Chen Chen, Lingjuan Lyu, Shangguang Wang, Mengwei Xu, Dongqi Cai
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlaNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences. Generative navigation world models provide this foresight through visual rollouts, which are costly when evaluating multiple candidates. We present LiteNWM, a latent navigation world model that shares visual encoding across candidates and jointly predicts their action-conditioned future representations at multiple horizons, while a learned scorer uses these predictions to select trajectories. In offline evaluations on RECON, SCAND, and SACSoN, LiteNWM reduces macro-averaged trajectory error by 17.56% relative to NoMaD+NWM-XL and achieves a 128.00-fold end-to-end speedup on an RTX 5090. The same evaluator transfers from NoMaD to MBRA without proposer-specific retraining, reducing MBRA's macro-averaged trajectory error by 16.2%. In real-robot experiments in unseen indoor and outdoor environments, LiteNWM improves navigation success from 43.3% to 83.3% relative to NoMaD. These results demonstrate that LiteNWM can be deployed for future-aware planning and closed-loop navigation on a physical robot.

</details>

---

### [[20_Research/Papers/具身智能/PLaW-VLA_Predictive_Latent_World_Modeling_for_Vision-Language-Action_Policies|PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies]]

![[assets/2610.12285_figure.png|800]]

- **arXiv**: [2610.12285](https://arxiv.org/abs/2610.12285)
- **PDF**: https://arxiv.org/pdf/2610.12285
- **详细分析**: [[20_Research/Papers/具身智能/PLaW-VLA_Predictive_Latent_World_Modeling_for_Vision-Language-Action_Policies|PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies]]
- **作者**: Yu Liu, Hetian Guo, Tianlv Huang, Ziyi Cai, Wudi Chen, Hantang Wang, Qiutong Liu, Yingzhi Peng, Wei Han, Peijun Tang, Jianan Wang, Zipei Fan...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.2（加权：具身智能 2.7，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, RL, WorldModel

#### 研究背景与动机

《PLaW-VLA: Predictive Latent World Modeling for Vision-Language-Action Policies》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：JEPA-VLA, PLaW-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning to predict how the world evolves can provide vision-language-action (VLA) policies with predictive context for long-horizon control, but its effectiveness depends on what future representation is modeled and how it conditions action generation. We introduce PLaW-VLA, which models task-relevant future states in a pretrained prediction-oriented representation space, reducing the need to predict control-irrelevant visual details. Built on a Mixture-of-Transformers architecture, PLaW-VLA conditions action generation on observation history, current task semantics, and predicted future states through structured causal attention. Experiments show a +11.8 percentage-point (pp) gain over reactive policies on RoboTwin Hard Horizon III and a +1.77 pp gain over reconstruction-oriented latent prediction on zero-shot LIBERO-Plus, supporting improved long-horizon control and generalization under distribution shift, respectively. By avoiding low-level visual reconstruction, PLaW-VLA lowers the burden of future prediction, enabling a lightweight latent world model with parallel future prediction and about 1/19 the inference latency of generative world-action modeling at comparable policy performance.

</details>

---

### [[20_Research/Papers/具身智能/Walking_on_Roofs_Exploring_the_Potential_of_Walking_Robots_for_Construction_Work_on_Roofs|Walking on Roofs: Exploring the Potential of Walking Robots for Construction Work on Roofs]]

![[assets/2610.12272_figure.png|800]]

- **arXiv**: [2610.12272](https://arxiv.org/abs/2610.12272)
- **PDF**: https://arxiv.org/pdf/2610.12272
- **详细分析**: [[20_Research/Papers/具身智能/Walking_on_Roofs_Exploring_the_Potential_of_Walking_Robots_for_Construction_Work_on_Roofs|Walking on Roofs: Exploring the Potential of Walking Robots for Construction Work on Roofs]]
- **作者**: Bjoern-Felix Dettmar, Arne Roennau
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.9，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Walking on Roofs: Exploring the Potential of Walking Robots for Construction Work on Roofs》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates the feasibility of deploying quadruped walking robots for the automation of work in roof environments. While quadrupeds have demonstrated versatility across various domains, their large-scale deployment remains limited, partly due to lack of application-specific designs. Roof environments represent a novel and unexplored use case, combining high safety risks for human workers with repetitive, strenuous tasks that could benefit from robotic assistance. A dedicated test rig of a roof's surface was designed to evaluate the baseline performance of a commercial quadruped, the \emph{Unitree Go2}, in this new environment. Experiments revealed that standard ball feet are inherently inadequate for locomotion on sloped roofs: slippage increased quadratically with incline angle, get-up and lie-down sequences were only possible on small inclines, and critical failures already occurred regularly on moderate inclines of 25°. This work provides the first systematic assessment of quadruped locomotion in roof environments, highlighting both the potential and the current limitations of this application and establishes a baseline for future research. Effective solutions will require a combination of task-oriented foot designs, advanced contact mechanics and environment-specific control strategies, such as reinforcement learning for roof-adapted gaits.

</details>

---

### [[20_Research/Papers/机器人/Fixed-Reference_Pose_Residuals_for_Measuring_Cross-Dataset_Cue_Transfer_in_Human-Robot_Interaction_Anticipation|Fixed-Reference Pose Residuals for Measuring Cross-Dataset Cue Transfer in Human-Robot Interaction Anticipation]]

![[assets/2610.12245_figure.png|800]]

- **arXiv**: [2610.12245](https://arxiv.org/abs/2610.12245)
- **PDF**: https://arxiv.org/pdf/2610.12245
- **详细分析**: [[20_Research/Papers/机器人/Fixed-Reference_Pose_Residuals_for_Measuring_Cross-Dataset_Cue_Transfer_in_Human-Robot_Interaction_Anticipation|Fixed-Reference Pose Residuals for Measuring Cross-Dataset Cue Transfer in Human-Robot Interaction Anticipation]]
- **作者**: Bowen Yang, Xinliang Xiao, Wenjing Zhang, Li Yang, Wei Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Fixed-Reference Pose Residuals for Measuring Cross-Dataset Cue Transfer in Human-Robot Interaction Anticipation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social and service robots in public spaces need to anticipate which nearby person is about to approach and touch them, so that a response can be prepared before contact. It is largely unknown which cues support this anticipation when a model trained with one robot is used on another robot at a different site. We study this question with a fixed-reference pose residual (FRPR) model: a geometry predictor built from the person's bounding box and mask is trained and frozen, and a temporal network then learns from body pose an additive correction to its logit, so that every prediction splits exactly into a geometry term and a pose term. Between two public egocentric datasets recorded by different robots, HUI360 and SSUP-A, with every choice made on source data, the pose correction raised average precision (AP) from 0.277 to 0.321 from SSUP-A to HUI360 and gave no measurable gain in the opposite direction; the same asymmetry held over a stronger, source-selected geometry reference. Freezing gave no AP advantage over joint training, and simple geometric baselines and tree ensembles remained competitive or better, so the construction serves measurement rather than prediction accuracy. A head-orientation residual added small gains in both directions. Post hoc, whether a person faces the camera kept its discriminative direction across datasets, whereas head pitch reversed. With thresholds chosen on source data, the neural models that use geometry detected at most 17% of target interactions. Code and processed data are available at https://github.com/WeiZhou96/FRPR-interaction-anticipation.

</details>

---

### [[20_Research/Papers/具身智能/Residual_Modeling_Closes_the_Regression_and_Generative_Policy_Gap_in_Robot_Learning|Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning]]

![[assets/2610.12231_figure.png|800]]

- **arXiv**: [2610.12231](https://arxiv.org/abs/2610.12231)
- **PDF**: https://arxiv.org/pdf/2610.12231
- **详细分析**: [[20_Research/Papers/具身智能/Residual_Modeling_Closes_the_Regression_and_Generative_Policy_Gap_in_Robot_Learning|Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning]]
- **作者**: Yuchen Zhou, Jiacheng You, Weikang Wan, Weijun Dong, Yang Gao, Jiayuan Mao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Residual Modeling Closes the Regression and Generative Policy Gap in Robot Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from demonstration has enabled impressive robot behaviors. A common choice for policy learning is to use diffusion or flow matching (Flow-Policies), which often outperforms direct action regression trained with mean squared error (MSE-Policies). This gap is commonly attributed to multimodal demonstrations. We revisit this gap from the perspective of statistical modeling: how action-prediction residuals shape policy optimization. Our analysis of real-world robot demonstration data reveals substantial state-dependent variation in residual scales and heavier-than-Gaussian tails. While both MSE-Policies and Flow-Policies exhibit heavy-tailed action residuals, their training gradients behave differently: MSE allocates more gradient magnitude to observations with large action residuals, which hurts optimization. Motivated by these findings, we introduce heteroscedastic Student-t action regression (HT-Policies), which learns input-dependent residual scales and reduces the influence of heavy tails. HT-Policies predict action chunks with a single feed-forward pass and can reuse pretrained flow-matching-based policy networks as the backbone. Across four simulation benchmarks and real-robot evaluations, HT-Policies achieves success rates competitive with generative policy baselines, both when trained from scratch and from pretrained vision-language-action and world-action models, despite being faster in training and inference. Together, these findings shed light on the practical advantages of generative objectives in robot learning from demonstrations and offer an efficient direct-regression alternative for a range of architectures and tasks. Project page: https://the-labone.github.io/regression-policy-project/

</details>

---

### [[20_Research/Papers/强化学习/Sim-to-Real_RL_for_ASVs_using_SysID|Sim-to-Real RL for ASVs using SysID]]

![[assets/2610.12202_figure.png|800]]

- **arXiv**: [2610.12202](https://arxiv.org/abs/2610.12202)
- **PDF**: https://arxiv.org/pdf/2610.12202
- **详细分析**: [[20_Research/Papers/强化学习/Sim-to-Real_RL_for_ASVs_using_SysID|Sim-to-Real RL for ASVs using SysID]]
- **作者**: Cody Sheltraw, Tsimafei Lazouski, Maani Ghaffari, Alan Papalia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Sim-to-Real RL for ASVs using SysID》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous Surface Vehicles (ASVs) operating in dynamic marine environments require robust control policies for tasks such as path following and station keeping, making reinforcement learning (RL) a promising alternative to classical controllers. However, existing ASV simulators rarely support parallel environments for RL training. Such existing simulators require accurate hydrodynamic modeling from computational fluid dynamics solvers or towing tank tests for setting hydrodynamic parameters to address the sim-to-real gap. To address these challenges, we present an ASV simulator and accompanying pipeline that enables training policies starting from unknown vehicle dynamics. Our framework uses only a CAD model and brief set of open-water field trajectories for approximating and refining both hydrodynamic and thruster parameters. Real-world deployments on a BlueBoat ASV demonstrate successful zero-shot sim-to-real transfer in path following and station-keeping tasks without prior hydrodynamic and propeller information.

</details>

---

### [[20_Research/Papers/具身智能/RESETTLE_Robotic_Recovery_through_Disagreement-Triggered_Retrieval_and_Efficient_Corrective_Control|RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control]]

![[assets/2610.12185_figure.png|800]]

- **arXiv**: [2610.12185](https://arxiv.org/abs/2610.12185)
- **PDF**: https://arxiv.org/pdf/2610.12185
- **详细分析**: [[20_Research/Papers/具身智能/RESETTLE_Robotic_Recovery_through_Disagreement-Triggered_Retrieval_and_Efficient_Corrective_Control|RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control]]
- **作者**: Yuxin Chen, Senqiao Yang, Zixuan Wang, Jinhui Ye, Changsheng Lu, Pengguang Chen, Shu Liu, Zhuotao Tian, Jiaya Jia
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE(Robotic rEcovery through diSagrEement-Triggered reTrievaL and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery when two action proposals independently sampled under identical conditioning persistently disagree. It retrieves a same-task demonstration reference using an adapted V-JEPA encoder and combines a state-servo prior with a guarded visual residual to execute one corrective action without online trajectory optimization or additional vision-language reasoning, then returns control to the base policy. Across six base policies in simulation, RESETTLE achieves up to 8.70%, 6.28%, and 6.83% absolute success-rate gains on LIBERO-Plus, Meta-World, and RoboCasa Tabletop, respectively, with further improvements on four real-world tasks using two policies. In QwenPI-based comparisons, its monitoring-and-recovery computation latency is 74.04%--93.57% lower than VoLoAgent's monitoring-and-planning latency for grasp and place tool calls. It also raises Harness VLA's LIBERO-Pro Swap success from 42% to 50%, demonstrating compatibility with high-level agentic planning. Code available at: https://github.com/JIA-Lab-research/RESETTLE

</details>

---

### [[20_Research/Papers/大模型/Instance-anchored_interaction_evidence_Grounding_robot_plans_in_human_pointing_and_handling|Instance-anchored interaction evidence: Grounding robot plans in human pointing and handling]]

![[assets/2610.12157_figure.png|800]]

- **arXiv**: [2610.12157](https://arxiv.org/abs/2610.12157)
- **PDF**: https://arxiv.org/pdf/2610.12157
- **详细分析**: [[20_Research/Papers/大模型/Instance-anchored_interaction_evidence_Grounding_robot_plans_in_human_pointing_and_handling|Instance-anchored interaction evidence: Grounding robot plans in human pointing and handling]]
- **作者**: Xinliang Xiao, Bowen Yang, Wenjing Zhang, Li Yang, Wei Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Instance-anchored interaction evidence: Grounding robot plans in human pointing and handling》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EgoPlan-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot that assists people must often act on what a person has shown rather than said: which of several identical cartons was pointed at, or which box was handled. The plan is executed from the final scene, whereas the evidence occurs earlier, possibly on objects that have since moved. We propose instance-anchored interaction evidence (IAE), which registers every object of the final scene to its public identifier, keeps each identity through the video by backward mask propagation, and describes every frame by the geometry between hands, forearms and these instances. An evidence network trained only from task outcomes scores the instances. For pointing tasks, a grammar-constrained dynamic program trained with a structured loss decodes object-destination programs; symbolic programs handle reference disambiguation and, without learning, episodic tasks. On 1,255 WatchAct benchmark requests, scored by symbolic execution, IAE reaches 64.2% plan success on implicit-intent tasks against 27.5% for a 32B vision-language model (strict success 49.7% against 15.4%), and 46.4% against 27.0% on restoration, reversal and imitation without task-specific training. Controls with the same perception overlays, the same 32 frames, forward tracking, or a relation model trained on the same labels do not explain the gain. Given IAE's evidence as text with its meaning explained, the same language model reaches 57.4%: most of the gain comes from the instance-anchored evidence, and the explicit programs add 6.8 points at a fraction of the cost. Pointing remains the hardest case, with 16.9% strict success. The code is available at https://github.com/WeiZhou96/iae-watchact.

</details>

---

### [[20_Research/Papers/强化学习/Leveraging_Human-In-The-Loop_Demonstrations_in_Reinforcement_Learning_for_Digital_Twin-Driven_Robot_Flexibility|Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digital Twin-Driven Robot Flexibility]]

![[assets/2610.12140_figure.png|800]]

- **arXiv**: [2610.12140](https://arxiv.org/abs/2610.12140)
- **PDF**: https://arxiv.org/pdf/2610.12140
- **详细分析**: [[20_Research/Papers/强化学习/Leveraging_Human-In-The-Loop_Demonstrations_in_Reinforcement_Learning_for_Digital_Twin-Driven_Robot_Flexibility|Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digital Twin-Driven Robot Flexibility]]
- **作者**: Yuzhu Sun, Mien Van, Nguyen Minh Nhat, Stephen McIlvanna, Sean McLoone
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Leveraging Human-In-The-Loop Demonstrations in Reinforcement Learning for Digital Twin-Driven Robot Flexibility》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Growing automation makes collaborative robots work in more variable environments, increasing the need for adaptation. We propose a human-in-the-loop online training framework combining a digital twin (DT), reinforcement learning (RL), and human demonstrations. Unlike DTs used mainly to generate synthetic data before task execution, our DT is synchronized with the physical system in real time through camera feeds, allowing the virtual robot to update its observations and policy from real-world feedback. A dual actor framework integrates imitation learning (IL) without adding a direct imitation loss to the RL actor, so demonstrations can guide adaptation instead of manual reprogramming. The proposed framework is demonstrated on the Ufactory Xarm5 collaborative robot, where the robot's end-effector aims to reach the target position while avoiding obstacles. The experiments show that the framework can resume training after a change in the physical workspace and that, with a fixed set of non-optimal demonstrations, the dual actor framework achieves a much higher final success rate than two methods that add an imitation loss to the actor. The same pattern holds with real human demonstrations collected in virtual reality (VR): with demonstrations that never reach the goal, the dual actor framework reached 83-100% mean deterministic evaluation success, against 0-17% for the two imitation-loss methods.

</details>

---

### [[20_Research/Papers/具身智能/PIER_An_Evidence-Gated_Execution_Interface_for_Robotic_Manipulation|PIER: An Evidence-Gated Execution Interface for Robotic Manipulation]]

![[assets/2610.12123_figure.png|800]]

- **arXiv**: [2610.12123](https://arxiv.org/abs/2610.12123)
- **PDF**: https://arxiv.org/pdf/2610.12123
- **详细分析**: [[20_Research/Papers/具身智能/PIER_An_Evidence-Gated_Execution_Interface_for_Robotic_Manipulation|PIER: An Evidence-Gated Execution Interface for Robotic Manipulation]]
- **作者**: Zoe Li, Anze Wang, Zhongyu Chen, Jingran Hu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《PIER: An Evidence-Gated Execution Interface for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating a plausible robot action does not establish that current observations justify its execution. Motivated by exploratory observations of high-confidence visual outputs under severe occlusion, we present PIER, an execution-authorization interface that separates evidence checks, decision provenance, and stage-scoped re-observation from hardware control. The deterministic gate evaluates declared visual and tactile inputs, while its caller maintains a budget of at most one re-observation per stage. We evaluate the implementation using 1,600 threshold-grid cases and 1,200 paired synthetic traces spanning score noise, missing tactile inputs, stale observations, and falsely reassuring scores. The finite grid yields zero declared invariant violations, and a matched Boolean baseline reproduces all non-recovery decisions. Under synthetic score noise, re-observation reduces valid-state denials from 57/120 to 18/120 while increasing invalid-state proceeds from 5/120 to 7/120. Stale and falsely reassuring inputs expose limitations that threshold checks alone cannot resolve. Exploratory visual, tactile, and robot setup records provide context but do not establish physical task performance. These results characterize an inspectable authorization interface and its input-contract limitations, without claiming superiority over equivalent rule logic, calibrated tactile accuracy, or certified physical safety.

</details>

---

### [[20_Research/Papers/具身智能/UNITAS_A_3D-Native_World_Action_Model_for_Embodied_Manipulation|UNITAS: A 3D-Native World Action Model for Embodied Manipulation]]

![[assets/2610.12099_figure.png|800]]

- **arXiv**: [2610.12099](https://arxiv.org/abs/2610.12099)
- **PDF**: https://arxiv.org/pdf/2610.12099
- **详细分析**: [[20_Research/Papers/具身智能/UNITAS_A_3D-Native_World_Action_Model_for_Embodied_Manipulation|UNITAS: A 3D-Native World Action Model for Embodied Manipulation]]
- **作者**: Ruixiang Wang, Yongyi Su, Wenlve Zhou, Bo Yue, Hengyan Liu, Dekun Lu, Yuxin Tian, Yihan Fang, Zerui Wu, Xing Hu, Jietao Chen, Yong Guo...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《UNITAS: A 3D-Native World Action Model for Embodied Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GeomVLA, PointWorld, Real-World, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models (WAMs) aim to answer a coupled physical question: given a task instruction, what motion should the robot execute, and how will that motion change the surrounding world? Most existing WAMs build on pretrained video generators and represent world evolution through images or visual latents. Robotic interaction, however, takes place in metric three-dimensional space, while images are view-dependent projections whose pixel distances do not directly encode physical distances. We introduce UNITAS, to our knowledge the first 3D-native world action model that unifies observations, actions, and scene dynamics in a shared metric 3D frame within each interaction, using a common representation across robot embodiments and human hands. Action flow represents human hands and robot grippers as 3D point trajectories, while scene flow describes scene-point displacements conditioned on these trajectories. World-aligned 3D positional embeddings ground visual tokens with or without depth input, and a physical-time trajectory tokenizer encodes each point trajectory as one token anchored at its current 3D position. This interface supports both direct action execution and action-conditioned scene prediction. With 1.7B parameters, UNITAS achieves the best action-conditioned scene prediction on RoboTwin among the compared methods, with up to 49% lower displacement errors than PointWorld, and state-of-the-art manipulation success, including 99.8% on LIBERO and an average of 85% across real-world tasks. The code is available at https://github.com/DexForce/UNITAS.

</details>

---

### [[20_Research/Papers/具身智能/ManiUnit_A_Manipulation_Skill_Dataset_and_Benchmark_for_Long-Horizon_Tasks|ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks]]

![[assets/2610.12089_figure.png|800]]

- **arXiv**: [2610.12089](https://arxiv.org/abs/2610.12089)
- **PDF**: https://arxiv.org/pdf/2610.12089
- **详细分析**: [[20_Research/Papers/具身智能/ManiUnit_A_Manipulation_Skill_Dataset_and_Benchmark_for_Long-Horizon_Tasks|ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks]]
- **作者**: Guoting Wei, Dawei Yan, Xia Yuan, Gengming Zhang, Yelin He, Guodong Du, Jiaquan Ye, Heng Zhang, Xinming Wei, Xianbiao Qi, Chunxia Zhao, Haokui Zhang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon mobile manipulation requires a robot to navigate multi-room environments and execute a sequence of manipulation skills under a single natural language instruction. Learning and evaluating these skills present three challenges: similar observations under a fixed task instruction may make skill selection ambiguous; even when a preceding skill succeeds, the robot state inherited by the next skill may deviate from its demonstrated starting states and affect execution; and task-level metrics hinder skill-specific diagnosis, while early failures leave later skills untested. We therefore introduce ManiUnit, a manipulation skill dataset and benchmark built from 50 BEHAVIOR-1K activities. Its dataset contains 137,899 segments across 21 skill types and 417 subtasks, and its benchmark contains 1,260 test instances. Correspondingly, ManiUnit pairs each segment with an explicit subtask instruction; measures sensitivity to perturbations of the robot's starting base position or joint configuration; and restores intermediate simulator states and defines local success conditions so that each skill can be evaluated without executing preceding stages. Evaluations of representative vision-language-action (VLA) policies show that similar aggregate scores can hide substantial per-skill differences. The tested starting-state perturbations also degrade execution: on the full benchmark, joint perturbations reduce success rates by approximately 56% relative to those from demonstrated starting states. On two long-horizon activities, a skill policy trained on ManiUnit segments achieves 78.7% local manipulation success, compared with 49.3% for a task policy trained on complete demonstrations. The trained skills further support complete-task execution on these activities, as coordinating the task and skill policies through a planner raises full-task success from 4.0% to 18.0%.

</details>

---

### [[20_Research/Papers/具身智能/Tell_Robot_What_Not_to_Do_A_Negation_Understanding_Perspective|Tell Robot What Not to Do: A Negation Understanding Perspective]]

![[assets/2610.11952_figure.png|800]]

- **arXiv**: [2610.11952](https://arxiv.org/abs/2610.11952)
- **PDF**: https://arxiv.org/pdf/2610.11952
- **详细分析**: [[20_Research/Papers/具身智能/Tell_Robot_What_Not_to_Do_A_Negation_Understanding_Perspective|Tell Robot What Not to Do: A Negation Understanding Perspective]]
- **作者**: Fazeng Li, Gan Sun, Hao Cheng, Weihong Ren, Yang Cong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Tell Robot What Not to Do: A Negation Understanding Perspective》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Fine-VLA, NegBench, NegaBench, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instruction following enables robots to perform diverse tasks specified in natural language, making it a fundamental capability for human-robot interaction. Beyond communicating desired outcomes, users also need to specify constraints on what not to do. We investigate how to enable vision-language-action models (VLAs) to follow negated instructions, where robots must accomplish task goals while respecting explicit exclusions. To this end, we propose NegaAlign, a parameter-efficient, plug-and-play framework that extends pretrained VLAs to follow negated instructions through image-language supervision alone. Specifically, we introduce Negation Transformation Layers into selected layers of the vision-language backbone to reshape intermediate instruction representations. Meanwhile, a teacher-guided alignment mechanism is designed to align instruction-relevant visual tokens, transferring action-relevant grounding from instructions that satisfy the negated constraint. The training phase uses supervision constructed from existing demonstrations and updates only the inserted layers, keeping all pretrained parameters frozen, including the action generator. We further introduce NegaBench, a simulation benchmark spanning 10 scenarios across five domains for systematically evaluating manipulation under negated constraints. Experiments across GR00T, $π_0$, and $π_{0.5}$ demonstrate consistent improvements in negated instruction following. With 11.6M trainable parameters, NegaAlign increases the negated-instruction success rate of $π_{0.5}$ from 2.60% to 88.45% on NegaBench and from 12.4% to 88.8% on real-world tasks, while retaining performance on affirmative instructions.

</details>

---

### [[20_Research/Papers/具身智能/STAG_A_Sparse_Traversability-Aware_Graph_Representation_from_Grid-Based_Costmaps_for_Robotic_Navigation|STAG: A Sparse Traversability-Aware Graph Representation from Grid-Based Costmaps for Robotic Navigation]]

![[assets/2610.11943_figure.png|800]]

- **arXiv**: [2610.11943](https://arxiv.org/abs/2610.11943)
- **PDF**: https://arxiv.org/pdf/2610.11943
- **详细分析**: [[20_Research/Papers/具身智能/STAG_A_Sparse_Traversability-Aware_Graph_Representation_from_Grid-Based_Costmaps_for_Robotic_Navigation|STAG: A Sparse Traversability-Aware Graph Representation from Grid-Based Costmaps for Robotic Navigation]]
- **作者**: Gabriel Manuel Garcia, Stéphanie Aravecchia, Miguel Angel Olivares-Mendez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《STAG: A Sparse Traversability-Aware Graph Representation from Grid-Based Costmaps for Robotic Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous rovers navigating large unstructured environments need efficient global planning that accounts for terrain traversability. However, searching dense grid-based costmaps becomes computationally expensive as the mapped area grows. We introduce STAG, a Sparse Traversability-Aware Graph that converts costmaps into compact graphs. STAG combines a medial-axis topological backbone, representative nodes for homogeneous traversability regions, and transition nodes near strong traversability gradients. Edges encode geometry and traversability to account for path length and terrain difficulty. We compare A* on STAG and dense grids using synthetic cave maps, mine maps and the DARPA CERBERUS dataset. Across five benchmark categories comprising 203 map instances and 101,200 queries, STAG reduces median planning time by 3.4x to 9.9x and peak query memory by 2.1x to 15.4x, with median relative path-length differences of -2.9% and +7.6%. STAG offers a compact representation for global planning, trading dense-grid traversability optimality for faster, less memory-intensive search.

</details>

---

### [[20_Research/Papers/具身智能/PathTime-VLA_Path-Time_Decoupling_for_Factorized_Post-Training_of_Vision-Language-Action_Policies|PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies]]

![[assets/2610.11771_figure.png|800]]

- **arXiv**: [2610.11771](https://arxiv.org/abs/2610.11771)
- **PDF**: https://arxiv.org/pdf/2610.11771
- **详细分析**: [[20_Research/Papers/具身智能/PathTime-VLA_Path-Time_Decoupling_for_Factorized_Post-Training_of_Vision-Language-Action_Policies|PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies]]
- **作者**: Qing Huang, Yifei Yang, Ziqing Zou, Anzhe Chen, Zhenjie Zhu, Yufei Wei, Rong Xiong, Yue Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《PathTime-VLA: Path-Time Decoupling for Factorized Post-Training of Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：E2VLA, HIL-SERL, OpenVLA, PathTime-VLA, TempoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies typically predict actions at fixed time intervals, coupling the route a robot follows with its execution pace. This coupling complicates adaptation from teleoperation: useful geometric guidance comes with timing shaped by interface delays and operator behavior. Our key insight is to bring the path-time parameterization of classical motion planning into the learned action representation of a VLA. We introduce PathTime-VLA, which represents motion as a progress-indexed interaction path $X(s)$ and a positive interval-time profile. The latter defines a monotone time law $t(s)$, yielding controller commands $X(s(t))$. For a given path, alternative executions are expressed through the time profile, allowing chunk-wise speed choices without changing the geometric prediction target. This representation supports a staged post-training procedure: demonstrations and DAgger interventions establish a target-domain prior, Speed-DQN learns execution multipliers from robot interaction, and Path-AWR uses rollout outcomes to refine the diffusion path generator. A path-conditioned action expert realizes the resulting motions while maintaining distinct learning interfaces for path generation and execution timing. Across three tasks, the complete method achieves $58/60$ successes versus $57/60$ for PathTime-VLA under BC + DAgger at fixed $1\times$, with approximately $39$-$52\%$ shorter mean completion times over successful trials.

</details>

---

### [[20_Research/Papers/具身智能/UltraLight_Luma_A_Novel_Edge-Deployable_Perception_Network_for_Crop-Row_Segmentation_in_Agricultural_Robotics|UltraLight Luma: A Novel Edge-Deployable Perception Network for Crop-Row Segmentation in Agricultural Robotics]]

![[assets/2610.11764_figure.png|800]]

- **arXiv**: [2610.11764](https://arxiv.org/abs/2610.11764)
- **PDF**: https://arxiv.org/pdf/2610.11764
- **详细分析**: [[20_Research/Papers/具身智能/UltraLight_Luma_A_Novel_Edge-Deployable_Perception_Network_for_Crop-Row_Segmentation_in_Agricultural_Robotics|UltraLight Luma: A Novel Edge-Deployable Perception Network for Crop-Row Segmentation in Agricultural Robotics]]
- **作者**: Dhanushka Balasingham, Shamod Ginigaddarage, Hanojhan Rajahrajasingh, Nuwan Kodagoda, Rajitha de Silva
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《UltraLight Luma: A Novel Edge-Deployable Perception Network for Crop-Row Segmentation in Agricultural Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ENet, LinkNet, MobileNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable crop-row perception is essential for autonomous agricultural robots, but low-cost deployment is constrained by computation, memory, power, and inference time. This paper addresses crop-row detection and navigation-line extraction using UltraLight Luma, a compact encoder-decoder segmentation network with a progressive learning strategy and only 13.1k trainable parameters. The predicted crop-row masks are processed using a post-processing algorithm to estimate row alignment for downstream visual servoing. UltraLight Luma improves parameter efficiency over U-Net, YOLOv8, and YOLOv26 while maintaining reliable crop-row detection performance. The model required only 25.23 mJ per inference, demonstrating its suitability for resource-constrained agricultural robots.

</details>

---

### [[20_Research/Papers/具身智能/2DGS-Planner_Rasterization-based_Path_Planning_in_2D_Gaussian_Splatting_Map|2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map]]

![[assets/2610.11752_figure.png|800]]

- **arXiv**: [2610.11752](https://arxiv.org/abs/2610.11752)
- **PDF**: https://arxiv.org/pdf/2610.11752
- **详细分析**: [[20_Research/Papers/具身智能/2DGS-Planner_Rasterization-based_Path_Planning_in_2D_Gaussian_Splatting_Map|2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map]]
- **作者**: Jiwon Park, Dong-Uk Seo, Hyun Myung
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《2DGS-Planner: Rasterization-based Path Planning in 2D Gaussian Splatting Map》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Gaussian splatting provides an explicit and efficiently rasterizable scene representation for robot navigation. However, individual Gaussian primitives may not reliably represent obstacles as they are jointly optimized through alpha-composited rendering from a finite set of reconstruction views. We propose 2DGS-Planner, a path planner for ground robots that reads planning-relevant geometry from a 2D Gaussian splatting (2DGS) map through rasterization, rather than treating individual Gaussian primitives as obstacles. During offline roadmap construction, multi-view attribution converts rendered normal dispersion into structural scores for non-ground disks supported by the reconstruction views. These scores guide adaptive node sampling on the ground. Path-aligned orthographic queries validate candidate edges, while cylindrical queries estimate local clearance fields that are cached on the edges. During online planning, graph search initializes a route, and path refinement reuses the cached fields while accounting for the robot's dimensions and ground constraints. Experiments demonstrate improved roadmap connectivity, more accurate clearance estimation, and higher planning success compared with the tested baselines. These results support rasterization as an effective geometric query interface for planning directly on Gaussian maps. Code and data are available at https://2dgs-planner.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_thermodynamic_cycles_via_robotic_mobility_and_sensing|Autonomous thermodynamic cycles via robotic mobility and sensing]]

![[assets/2610.11667_figure.jpg|800]]

- **arXiv**: [2610.11667](https://arxiv.org/abs/2610.11667)
- **PDF**: https://arxiv.org/pdf/2610.11667
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_thermodynamic_cycles_via_robotic_mobility_and_sensing|Autonomous thermodynamic cycles via robotic mobility and sensing]]
- **作者**: Sofia Kuperman, Ezra Ben-Abu, Yaron Veksler, Anna Zigelman, Sefi Givli, Amir D. Gat
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Autonomous thermodynamic cycles via robotic mobility and sensing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Thermodynamic cycles are the foundation of energy conversion across natural and engineered systems, transforming heat into useful work. However, these cycles traditionally operate between fixed thermal reservoirs, restricting them to specific locations and temperature differences. Here, we introduce autonomous thermodynamic cycles enabled by robotic mobility and sensing, allowing robots to perform thermodynamic cycles by accessing spatially varying temperature fields. We experimentally realize this concept using multistable gas-filled capsules that circulate within the system across a thermal gradient. Our model reveals that rapid transitions in the capsules' energy states allow the system to operate as a mobile heat engine that harvests and stores energy. By linking the capsule-scale internal energy dynamics to the robot's large-scale navigation strategy, we optimize locomotion paths that balance motion cost and energy harvesting. These findings demonstrate that thermodynamic cycles can emerge when autonomous systems navigate their environments, offering an artificial analog of organisms that forage for energy across spatial resources.

</details>

---

### [[20_Research/Papers/机器人/YOCO_You_Only_Calibrate_Once!_Fast_Mocap_Calibration_for_Dexterous_Teleoperation|YOCO: You Only Calibrate Once! Fast Mocap Calibration for Dexterous Teleoperation]]

![[assets/2610.11657_figure.png|800]]

- **arXiv**: [2610.11657](https://arxiv.org/abs/2610.11657)
- **PDF**: https://arxiv.org/pdf/2610.11657
- **详细分析**: [[20_Research/Papers/机器人/YOCO_You_Only_Calibrate_Once!_Fast_Mocap_Calibration_for_Dexterous_Teleoperation|YOCO: You Only Calibrate Once! Fast Mocap Calibration for Dexterous Teleoperation]]
- **作者**: Yu Zhang, Yunqi Li, Yushi Du, Yi Ma, Yanchao Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《YOCO: You Only Calibrate Once! Fast Mocap Calibration for Dexterous Teleoperation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HyperNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous teleoperation requires reliable human-hand state estimations. However, common low-cost motion-capture gloves and markerless trackers often exhibit biases that vary across users, glove fit, and recording sessions, degrading retargeting and demonstration quality. We present YOCO, a fast few-shot, fine-tuning-free calibration framework that corrects biased hand-pose streams from a small set of paired raw and target poses. Instead of optimizing a separate model for every operator or session, YOCO conditions a calibration HyperNet on the paired examples and predicts LoRA-style updates for a frozen MANO hand-estimation module, turning per-user calibration into a lightweight feed-forward adaptation step while preserving the geometric prior of MANO and the efficiency of a compact estimator. We train YOCO with synthetic drift augmentations on InterHand2.6M and evaluate on augmented InterHand sequences, offline real glove data, and dexterous teleoperation tasks. Across these settings, YOCO improves calibration efficiency, hand-state estimation quality and teleoperation performance compared with uncalibrated input and standard calibration baselines.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Language-Conditioned_Traversability_Representations_for_Adaptive_Visual_Navigation|Learning Language-Conditioned Traversability Representations for Adaptive Visual Navigation]]

![[assets/2610.11622_figure.png|800]]

- **arXiv**: [2610.11622](https://arxiv.org/abs/2610.11622)
- **PDF**: https://arxiv.org/pdf/2610.11622
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Language-Conditioned_Traversability_Representations_for_Adaptive_Visual_Navigation|Learning Language-Conditioned Traversability Representations for Adaptive Visual Navigation]]
- **作者**: Senda Chen, Changxu Cheng, Fangdi Li, Tao Wang, Wuyue Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Learning Language-Conditioned Traversability Representations for Adaptive Visual Navigation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traversability is essential for visual navigation but varies with robot capabilities and user preferences. Conventional pipelines often rely on explicit costmaps or segmentation masks with predefined criteria, requiring hand-crafted rules and careful tuning. Moreover, viewpoint-dependent segmentation masks complicate asynchronous planning under perception latency. We present LaTraNav, a framework that learns language-conditioned traversability representations for adaptive visual navigation. Its asynchronous architecture combines a slow vision-language model that produces latent representations of traversability and navigation goals, with a fast flow-matching planner conditioned on these representations. To train the system, we develop a simulation-based data generation pipeline with controllable trajectories, producing observations paired with language instructions, traversability maps, goal locations, and diverse trajectories. Photorealistic image translation further enhances visual realism. Evaluations on datasets from multiple sources demonstrate effective language-guided traversability segmentation and goal localization by the slow VLM, alongside adaptive pixel-space path planning by the fast planner. Latent conditioning improves planning performance over explicit segmentation masks, while asynchronous scheduling increases the path-update rate by $6.05\times$ at the same semantic-update rate.

</details>

---

### [[20_Research/Papers/具身智能/Acting_from_Belief,_Looking_When_Needed_A_Bayesian_Spatial_World_Model_for_Navigation_under_Intermittent_Perception|Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception]]

![[assets/2610.11591_first_page.png|800]]

- **arXiv**: [2610.11591](https://arxiv.org/abs/2610.11591)
- **PDF**: https://arxiv.org/pdf/2610.11591
- **详细分析**: [[20_Research/Papers/具身智能/Acting_from_Belief,_Looking_When_Needed_A_Bayesian_Spatial_World_Model_for_Navigation_under_Intermittent_Perception|Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception]]
- **作者**: Feihong Yang, Xiang Long, Jincheng Yu, Jianfei Zhang, Guangjun Ge, Chao Wang, Yu Wang
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，世界模型 0.8，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot navigation commonly uses wide-coverage, high-frequency sensing to reduce partial observability; this reliance becomes restrictive when another task temporarily redirects a shared sensor from navigation, interrupting navigation-relevant observations. We study navigation under intermittent perception: acting from an internal spatial belief and looking again only when execution needs a new observation, potentially freeing the shared sensor for other tasks between navigation observations. ALONE, a Bayesian spatial world model, propagates a structured spatial belief using executed actions and corrects it with selectively acquired observations; learned priors over common geometric structures infer unobserved structure from available observation history. It decodes the belief into a spatial estimate for the motion-planning module and predicts a reliability map expressing confidence in the estimate's accuracy. ALONE requests an observation only if insufficient reliability hinders navigation and new evidence should make relevant-region spatial information more reliable; otherwise, it continues acting from the propagated belief. We instantiate ALONE for drone navigation with intermittent single-camera depth images. Across two simulated scene families, it achieves 98% and 97% closed-loop success at a 10 Hz decision rate. Among successful trials, median fractions of decision steps requiring a new depth observation are only 0.9% and 1.3%, respectively, demonstrating high navigation success with substantially reduced observation demand. Real-world indoor flight experiments further validate navigation under intermittent depth observations, with all 10 trials successful.

</details>

---

### [[20_Research/Papers/机器人/RAGNAROK_Radar-Aided_Gravity-Normalized_Alignment_for_Robust_Open_Keyframe-based_Radar-Visual-Kinematic-Inertial_SLAM|RAGNAROK: Radar-Aided Gravity-Normalized Alignment for Robust Open Keyframe-based Radar-Visual-Kinematic-Inertial SLAM]]

![[assets/2610.11531_figure.png|800]]

- **arXiv**: [2610.11531](https://arxiv.org/abs/2610.11531)
- **PDF**: https://arxiv.org/pdf/2610.11531
- **详细分析**: [[20_Research/Papers/机器人/RAGNAROK_Radar-Aided_Gravity-Normalized_Alignment_for_Robust_Open_Keyframe-based_Radar-Visual-Kinematic-Inertial_SLAM|RAGNAROK: Radar-Aided Gravity-Normalized Alignment for Robust Open Keyframe-based Radar-Visual-Kinematic-Inertial SLAM]]
- **作者**: Hanjun Kim, Chiyun Noh, Sangwoo Jung, Jaehyung Jung, Simon Boche, Cedric Le Gentil, Stefan Leutenegger, Ayoung Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《RAGNAROK: Radar-Aided Gravity-Normalized Alignment for Robust Open Keyframe-based Radar-Visual-Kinematic-Inertial SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots offer superior mobility in unstructured environments, but reliable operation in such conditions requires robust state estimation. To address the vulnerability of proprioceptive estimators in rough terrain, recent methods have incorporated radar to provide velocity measurements. However, their limited yaw observability still leads to drift, and failure-aware fusion for adverse environments remains underexplored. In this letter, we present RAGNAROK, the first radar-visual-kinematic-inertial SLAM designed for robust operation in challenging environments. It integrates slip- and rolling-contact-aware leg velocity estimation, a kinematics-aware radar factor, and degradation-aware image enhancement. We further incorporate a B-spline-based radar-aided proprioceptive backbone, adaptive weighting, and online extrinsic calibration. Extensive experiments on public and self-collected datasets demonstrate that RAGNAROK achieves robust performance under challenging conditions and outperforms state-of-the-art baselines. The source code and dataset are available at https://github.com/hanjun815/RAGNAROK.

</details>

---

### [[20_Research/Papers/具身智能/DAMP_Humanoid_Locomotion_via_Denoised_Belief_Learning_and_Adversarial_Motion_Priors|DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors]]

![[assets/2610.11505_figure.png|800]]

- **arXiv**: [2610.11505](https://arxiv.org/abs/2610.11505)
- **PDF**: https://arxiv.org/pdf/2610.11505
- **详细分析**: [[20_Research/Papers/具身智能/DAMP_Humanoid_Locomotion_via_Denoised_Belief_Learning_and_Adversarial_Motion_Priors|DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors]]
- **作者**: Puying Shen, Wenhao Cui, Huaxing Huang, Bangyu Qin, Shengtao Li, Ziyang Dong, Guoteng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《DAMP: Humanoid Locomotion via Denoised Belief Learning and Adversarial Motion Priors》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots possess the structural capability to traverse complex terrains. However, achieving stable t raversal without relying on perceived information remains challenging, particularly in complex environments. This paper introduces DAMP, a reinforcement learning framework aimed at achieving robust and naturalistic humanoid locomotion over challenging terrains, with the assumption that no perceived information is available. The framework leverages recurrent neural networks to capture temporal dependencies and implicitly infer privileged and other task-relevant latent information. By aligning the learned representations with the task objective, the method enables robust and goal-consistent policy learning. This end-to-end framework achieves transfer learning from simulation to real-world environments, demonstrating the proposed method's robustness and generalization capabilities. The video of the real-world demonstration can be found at the following link: https://youtu.be/AkI7TZB2DDM.

</details>

---

### [[20_Research/Papers/具身智能/Experience-Guided_Initiation_Search_for_Learned_Skills_in_Skill_Composition|Experience-Guided Initiation Search for Learned Skills in Skill Composition]]

![[assets/2610.11418_figure.png|800]]

- **arXiv**: [2610.11418](https://arxiv.org/abs/2610.11418)
- **PDF**: https://arxiv.org/pdf/2610.11418
- **详细分析**: [[20_Research/Papers/具身智能/Experience-Guided_Initiation_Search_for_Learned_Skills_in_Skill_Composition|Experience-Guided Initiation Search for Learned Skills in Skill Composition]]
- **作者**: Qixuan Li, Yanhong Zhao, Jincheng Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Experience-Guided Initiation Search for Learned Skills in Skill Composition》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HarnessVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying frozen learned skills, such as Vision-Language-Action (VLA) policies, in new environments requires identifying initiation configurations that support reliable execution. In skill composition, an initiation configuration affects not only the current skill but also the physical state passed to subsequent skills, so successful execution of an individual skill does not necessarily imply successful completion of the composed task. Estimating target-specific capability through extensive rollouts is costly in real-world deployment, while directly reusing historical experience can be unreliable under environment changes. We propose EVIS, an Experience-Guided and Behavior-Validated Initiation Search framework for discovering reliable initiation configurations under limited target interaction. EVIS uses historical execution experience to prioritize promising candidates and target-environment behavior to validate whether they remain effective. We evaluate EVIS on single-skill and two-stage manipulation tasks with frozen VLA policies. EVIS reduces mean target-environment queries and improves reliable candidate discovery under small interaction budgets. These results show that combining historical guidance with target-side behavioral validation can reduce the interaction cost of deploying frozen learned skills in new environments.

</details>

---

### [[20_Research/Papers/具身智能/USDCraft_Geometrically_Grounded_Programmatic_Modeling_of_Articulated_3D_Assets_for_Simulation|USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation]]

![[assets/2610.11322_figure.png|800]]

- **arXiv**: [2610.11322](https://arxiv.org/abs/2610.11322)
- **PDF**: https://arxiv.org/pdf/2610.11322
- **详细分析**: [[20_Research/Papers/具身智能/USDCraft_Geometrically_Grounded_Programmatic_Modeling_of_Articulated_3D_Assets_for_Simulation|USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation]]
- **作者**: Chuanrui Zhang, Zaijia Yang, Duomin Wang, Lu Shi, Daquan Zhou, Ruihua Zhang, Ziwei Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GAPartNet, PartNet, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometrically faithful and functional articulated 3D assets are essential for real-to-sim robot manipulation, where policies trained in simulation must transfer to physical objects. Recent mesh-based methods learn to infer articulation from annotated 3D assets, but deployment remains challenging when real-world objects fall outside the training distribution or their meshes are incomplete or corrupted. To address these limitations, we formulate articulated asset reconstruction as programmatic modeling grounded in partial geometric evidence and introduce USDCraft, a framework in which a pretrained LLM writes and revises executable programs for simulation-ready articulated assets without task-specific training. We propose source geometry analysis, which converts the source mesh into a metric textual description that distinguishes observed surface from unknown space, and iterative geometric rechecking, which re-encodes each candidate in the same representation so that discrepancies point to program edits while unobserved regions remain open to completion. Visual feedback and physical authoring guidance complete the modeling process, which produces articulated USD assets with explicit physical properties that load into Isaac Sim without manual adjustment. Experiments demonstrate leading articulation recovery on two benchmarks and validate USDCraft's effectiveness for real-to-sim-to-real robot manipulation.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Relative_Localization_for_Homogeneous_Multi-Robot_Systems_through_UWB_Ranging_and_Limited_Communications|Distributed Relative Localization for Homogeneous Multi-Robot Systems through UWB Ranging and Limited Communications]]

![[assets/2610.11308_figure.png|800]]

- **arXiv**: [2610.11308](https://arxiv.org/abs/2610.11308)
- **PDF**: https://arxiv.org/pdf/2610.11308
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Relative_Localization_for_Homogeneous_Multi-Robot_Systems_through_UWB_Ranging_and_Limited_Communications|Distributed Relative Localization for Homogeneous Multi-Robot Systems through UWB Ranging and Limited Communications]]
- **作者**: Zhiqiang Cao, Ran Liu, Billy Pik Lik Lau, Chau Yuen, U-Xuan Tan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Distributed Relative Localization for Homogeneous Multi-Robot Systems through UWB Ranging and Limited Communications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate and reliable relative localization is crucial for multi-robot applications like exploration, search, and rescue missions. LiDAR-based solutions offer high accuracy in localizing surrounding objects; however, distinguishing homogeneous robots with similar appearances remains challenging due to the lack of distinctive identification features. In this paper, we propose a fully distributed relative pose estimation approach by integrating LiDAR, UWB, and odometry measurements, allowing each robot to accurately and continuously localize its teammates without external infrastructure. Specifically, potential anonymous teammate robot clusters from LiDAR scans are tracked by a dynamic tracker. We then identify teammate robots from these tracked anonymous clusters using a joint matching strategy, ensuring reliable data association between robots and clusters. Finally, by combining the corresponding LiDAR observations, UWB ranging, and odometry measurements, each robot precisely localizes others while minimizing data exchange. The system requires only odometry data exchange through onboard UWB, eliminating the need for additional communication infrastructure like WiFi routers or mesh networks. Extensive simulation and real-world experiments demonstrate the effectiveness and reliability of the proposed relative localization approach.

</details>

---

### [[20_Research/Papers/具身智能/SimVLA_Zero-Shot_Sim-to-Real_VLA_Learning_for_Mobile_Manipulation|SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation]]

![[assets/2610.11248_figure.png|800]]

- **arXiv**: [2610.11248](https://arxiv.org/abs/2610.11248)
- **PDF**: https://arxiv.org/pdf/2610.11248
- **详细分析**: [[20_Research/Papers/具身智能/SimVLA_Zero-Shot_Sim-to-Real_VLA_Learning_for_Mobile_Manipulation|SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation]]
- **作者**: Kyoungin Baik, Youngwoon Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspVLA, Real-World, SimVLA, SimVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale, diverse datasets have driven the success of LLMs and VLMs. But VLAs for robotics remain limited by the cost and complexity of real-world data collection. While simulation offers a scalable alternative, its potential for sim-to-real VLA learning in mobile manipulation remains largely underexplored. We introduce SimVLA, an end-to-end framework that trains VLAs entirely on synthetic simulation data without teleoperation for mobile manipulation. SimVLA is first pre-trained on two complementary simulation-derived datasets: SimAction, a large-scale robot action dataset spanning 35 diverse mobile manipulation tasks, generated by composing atomic skills, and SimVQA, which leverages privileged simulator state to provide spatial, geometric, and subtask-level visual-language supervision. We further post-train SimVLA on a mixture of SimAction and SimDeploy, a dataset collected from policy rollouts across diverse simulated environments. We evaluate SimVLA on tasks including restocking, pouring, and cleaning, and show zero-shot transfer to real-world mobile manipulation, including real home environments. SimVLA outperforms policies trained on 50 in-domain real-world demonstrations, suggesting that simulation can enable scalable sim-to-real mobile manipulation. We further demonstrate the value of multiple complementary forms of supervision for effectively leveraging simulation in VLA training.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Relative_Localization_Based_on_Ultra-WideBand_and_LiDAR_for_Multi-robot_with_Limited_Communication|Distributed Relative Localization Based on Ultra-WideBand and LiDAR for Multi-robot with Limited Communication]]

![[assets/2610.11141_figure.png|800]]

- **arXiv**: [2610.11141](https://arxiv.org/abs/2610.11141)
- **PDF**: https://arxiv.org/pdf/2610.11141
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Relative_Localization_Based_on_Ultra-WideBand_and_LiDAR_for_Multi-robot_with_Limited_Communication|Distributed Relative Localization Based on Ultra-WideBand and LiDAR for Multi-robot with Limited Communication]]
- **作者**: Zhiqiang Cao, Ran Liu, Billy Pik Lik Lau, Chau Yuen, U-Xuan Tan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Distributed Relative Localization Based on Ultra-WideBand and LiDAR for Multi-robot with Limited Communication》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Relative localization is crucial for a multi-robot system to collaboratively perform tasks, such as exploration and formation. However, this is highly challenging for homogeneous robots with similar appearance in GPS-denied and communication-limited environments. In this paper, we propose a fully distributed relative position estimation approach for a team of robots based on onboard UWB and LiDAR sensors, in which LiDAR is utilized to obtain the position of anonymous objects in Line-of-Sight (LOS), and UWB is used for ranging between robots. We construct two graphs, namely UWB connection graph and LiDAR connection graph, to represent the spatial relationship among objects (robots and obstacles) based on UWB and LiDAR measurements. Identification and relative position estimation are formulated as a common subgraph matching problem. A falsely-matched robot identification approach is designed to recognize the falsely-matched results caused by obstacle blockage in LiDAR field of view. These robots are then localized by leveraging the well-matched robots and the UWB ranging measurements in the UWB connection graph. We conducted experiments to evaluate the performance of our approach. The results show that the proposed approach is capable of achieving satisfactory positioning accuracy for a team of robots in a distributed manner with only exchanging limited information.

</details>

---

### [[20_Research/Papers/具身智能/FOCUS_From_Privileged_States_to_RGB-D_with_Controlled_Modality_Switching_and_Representation_Alignment|FOCUS: From Privileged States to RGB-D with Controlled Modality Switching and Representation Alignment]]

![[assets/2610.11119_figure.png|800]]

- **arXiv**: [2610.11119](https://arxiv.org/abs/2610.11119)
- **PDF**: https://arxiv.org/pdf/2610.11119
- **详细分析**: [[20_Research/Papers/具身智能/FOCUS_From_Privileged_States_to_RGB-D_with_Controlled_Modality_Switching_and_Representation_Alignment|FOCUS: From Privileged States to RGB-D with Controlled Modality Switching and Representation Alignment]]
- **作者**: Filip Grigorov, Kourosh Darvish, Nandita Vijaykumar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FOCUS: From Privileged States to RGB-D with Controlled Modality Switching and Representation Alignment》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based reinforcement learning for robotic manipulation is sample-inefficient because RGB-D observations are high-dimensional and noisy. Privileged state information available in simulation can accelerate training, but its absence at test time creates a train-test modality gap. We propose FOCUS, a single-stage PPO framework that trains the critic on privileged state while automatically regulating whether the actor collects rollouts from RGB-D or privileged-state latents. Regulation is driven by the KL divergence between the action distributions induced by the two modalities, while representation alignment encourages consistent action selection across them. Together, these mechanisms limit RGB-D rollouts when the actor's action distributions from RGB-D and privileged-state latents disagree. As they align, RGB-D exposure increases, shifting on-policy training toward the RGB-D inputs used at test time. Across five manipulation tasks, FOCUS raises average test success from 0.71 to 0.93 relative to the strongest RGB-D-at-test baseline on each task. When accounting for each method's complete training pipeline, budget-normalized training-success AUC increases from 0.47 to 0.65. On Pick-and-Place, test success rises from 0.47 to 0.86, while AUC increases from 0.12 to 0.61, a 5.0x improvement in learning efficiency over the fixed interaction budget.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Path-Creative_Navigation_Robot_Navigation_through_Embodied_Interaction|Towards Path-Creative Navigation: Robot Navigation through Embodied Interaction]]

![[assets/2610.11072_figure.png|800]]

- **arXiv**: [2610.11072](https://arxiv.org/abs/2610.11072)
- **PDF**: https://arxiv.org/pdf/2610.11072
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Path-Creative_Navigation_Robot_Navigation_through_Embodied_Interaction|Towards Path-Creative Navigation: Robot Navigation through Embodied Interaction]]
- **作者**: Haoyu Xi, Siwei Cheng, Xiangyuan Liu, Brenda Li, Wei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Towards Path-Creative Navigation: Robot Navigation through Embodied Interaction》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous navigation in cluttered and constrained environments typically assumes a fixed environment and searches only for paths within existing free space. However, a route can be blocked by an articulated structure, a movable object, or a pedestrian, and reaching the goal may therefore require appropriate embodied interaction with the environment. This paper formulates Path-Creative Navigation (PCN), a navigation paradigm in which the robot recovers free space by coordinating locomotion and embodied interaction, and addresses one class of PCN tasks with a mapless framework. The vision-LiDAR-odometry framework integrates local observations, obstacle geometry, and robot-state estimates through a unified navigation system, providing stable semantic and geometric information for navigation and interaction. The traversability-aware decision method utilizes visual and LiDAR distance information to determine whether a blockage is actionable and whether it can be safely bypassed, enabling the robot to interact only when necessary while supporting articulated structure pushing, movable object pushing, obstacle avoidance, and pedestrian requests. We design simulation scenarios and evaluate different methods in both simulation and two real-world tasks that cannot be completed by conventional navigation alone without embodied interaction. These results demonstrate that our framework achieves higher task completion than the baseline methods by coordinating navigation and interaction in cluttered and constrained environments. Code is available at:{https://anonymous.4open.science/r/path-creative-navigation/}.

</details>

---

### [[20_Research/Papers/具身智能/A_Reconfigurable_Fabric_Based_Pneumatic_Actuator_with_Button_Fastened_Constraint_Modules_for_Multi_Mode_Actuation|A Reconfigurable Fabric Based Pneumatic Actuator with Button Fastened Constraint Modules for Multi Mode Actuation]]

![[assets/2610.11054_figure.jpg|800]]

- **arXiv**: [2610.11054](https://arxiv.org/abs/2610.11054)
- **PDF**: https://arxiv.org/pdf/2610.11054
- **详细分析**: [[20_Research/Papers/具身智能/A_Reconfigurable_Fabric_Based_Pneumatic_Actuator_with_Button_Fastened_Constraint_Modules_for_Multi_Mode_Actuation|A Reconfigurable Fabric Based Pneumatic Actuator with Button Fastened Constraint Modules for Multi Mode Actuation]]
- **作者**: Kentaro Kimura, Hiroki Ishizuka, Yusuke Sakaue, Sei Ikeda, Osamu Oshiro
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《A Reconfigurable Fabric Based Pneumatic Actuator with Button Fastened Constraint Modules for Multi Mode Actuation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft pneumatic actuators are widely used in soft robotics. However, their actuation modes are typically fixed by internal chamber designs or reinforcements, making post fabrication reconfiguration difficult. This paper presents a reconfigurable fabric-based pneumatic actuator that enables rapid, tool free, and reusable switching among multiple actuation modes by attaching constraint fabric modules to a buttoned textile sleeve. By rearranging low-stretch constraint parts on a single actuator body, the proposed system realizes four actuation modes isotropic expansion, contraction, bending, and twisting without redesigning or disassembling the actuator.We further introduce an attachable capacitive fabric-based tactile sensor module that can be mounted at arbitrary locations on the actuator surface for task dependent contact sensing. Experiments demonstrated an elongation ratio of 1.2, a maximum bending angle of approximately 60 degrees, and a twisting angle of approximately 90 degrees at 24 kPa, while achieving blocking forces exceeding 10 N across all modes. The tactile sensor exhibited a monotonic, force-dependent increase in capacitance with low hysteresis (approximately 12%) and stable cyclic responses under preload. Finally, we constructed soft robotic arms composed of multiple actuators and demonstrated in situ motion reconfiguration for grasping by changing the attached constraint patterns. These results indicate that the proposed modular constraint and sensing framework improves the functional adaptability of fabric-based soft robots while preserving a simple, robust actuator structure.

</details>

---

### [[20_Research/Papers/强化学习/Informationally_Decoupled_Trajectory_Design_for_Sim-to-Real_System_Identification|Informationally Decoupled Trajectory Design for Sim-to-Real System Identification]]

![[assets/2610.10905_figure.png|800]]

- **arXiv**: [2610.10905](https://arxiv.org/abs/2610.10905)
- **PDF**: https://arxiv.org/pdf/2610.10905
- **详细分析**: [[20_Research/Papers/强化学习/Informationally_Decoupled_Trajectory_Design_for_Sim-to-Real_System_Identification|Informationally Decoupled Trajectory Design for Sim-to-Real System Identification]]
- **作者**: Sangwoo Shin, Ashvin Anilkumar, Ryan Gao, Josiah P. Hanna
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Informationally Decoupled Trajectory Design for Sim-to-Real System Identification》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sampling-based system identification estimates physically meaningful parameters by tuning a simulator to reproduce the target system dynamics, providing an interpretable approach to improving sim-to-real transfer. Yet when the collected trajectories do not distinguish the effects of different parameters, multiple parameter combinations can reproduce those trajectories, leading to unreliable parameter estimates. To address this challenge, we introduce an Informationally Decoupled Trajectory Design framework (IDTD), which formulates the objective for the exploration policy built on the Schur complement score derived from the Fisher information matrix. To faithfully reflect parameter separability in the exploration objective, IDTD normalizes the score against the per-parameter information, selects the most favorable trajectory segment for each parameter, and aggregates the resulting scores logarithmically. The optimized trajectory is therefore composed of complementary intervals, each exposing a distinct subset of parameters whose contribution to the motion over that interval can be attributed unambiguously. Across diverse simulation environments, ranging from a linear-dynamics system to the Go2 quadruped, G1 humanoid, and Crazyflie quadrotor, IDTD reduces the parameter identification error by 39.6% on average relative to the strongest prior active-exploration baseline and attains improved downstream policy transfer. Furthermore, we validate the proposed trajectory design on a real K1 humanoid, demonstrating that the resulting identified parameters accurately capture the real-system dynamics.

</details>

---

### [[20_Research/Papers/强化学习/OmniHOI_Dexterous_Hand-Object_Interaction_from_Monocular_Human_Video|OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video]]

![[assets/2610.10855_figure.png|800]]

- **arXiv**: [2610.10855](https://arxiv.org/abs/2610.10855)
- **PDF**: https://arxiv.org/pdf/2610.10855
- **详细分析**: [[20_Research/Papers/强化学习/OmniHOI_Dexterous_Hand-Object_Interaction_from_Monocular_Human_Video|OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video]]
- **作者**: Ting Mao, Yanming Shao, Ziheng Wang, Haoyu Liu, Yiqun Wang, Xuanye Wu, Yao Mu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《OmniHOI: Dexterous Hand-Object Interaction from Monocular Human Video》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular videos of human manipulation provide abundant dexterous demonstrations, yet reconstructing hand-object interaction from a single view and transferring it to robot hands remain difficult, limiting their direct use for robot execution. Prior methods either require task-specific RL training, limiting scalability, or assume clean motion-capture trajectories and thus cannot operate directly on video. We present OmniHOI, a pipeline that turns an RGB video of hand-object interaction into an interaction-faithful trajectory on dexterous hands. The key idea is to enforce physical consistency using the evidence available at each stage: image evidence during reconstruction, contact geometry during retargeting, and dynamics during physics-in-the-loop refinement. Each stage optimizes the corresponding representation directly, correcting errors before they propagate downstream or must be absorbed by a learned policy. Across 150 motion-capture trajectories transferred to each of five dexterous hands with 6 to 22 DoF, we achieve 39-89% success, compared with at most 31% for prior transfer methods. On 60 monocular video clips, we achieve 53% success, compared with 28% for the best prior video-to-robot pipeline. Its trajectories also execute on a real bimanual robot across diverse tasks.

</details>

---

### [[20_Research/Papers/世界模型/Cross-Embodiment_Robot_Foundation_World_Models_with_Latent_Actions|Cross-Embodiment Robot Foundation World Models with Latent Actions]]

![[assets/2610.10846_figure.png|800]]

- **arXiv**: [2610.10846](https://arxiv.org/abs/2610.10846)
- **PDF**: https://arxiv.org/pdf/2610.10846
- **详细分析**: [[20_Research/Papers/世界模型/Cross-Embodiment_Robot_Foundation_World_Models_with_Latent_Actions|Cross-Embodiment Robot Foundation World Models with Latent Actions]]
- **作者**: Huang Huang, Sriram Yenamandra, Arjun Majumdar, Elie Aljalbout, Tushar Nagarajan, Tsung-Yen Yang, Akshara Rai, Michael Rabbat, Li Fei-Fei, Jiajun Wu, Tingfan Wu, Franziska Meier
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.9（加权：具身智能 0.6，世界模型 1，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Cross-Embodiment Robot Foundation World Models with Latent Actions》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The diversity of robot embodiments and action spaces makes it challenging to build robot world models that generalize across different embodiments. We introduce the Latent Action-Conditioned Robot World Model (LAC-WM), which operates within a learned unified latent action space shared across diverse embodiments. This unified action space improves the world model's performance when adapted to previously unseen robot embodiments. We compare LAC-WM with an Explicit Action-Conditioned World Model (EAC-WM), which conditions on explicit motion labels. Our results show that explicit action conditioning leads to disjoint action representations across embodiments, limiting downstream performance when adapting to new robots. We evaluate both models on dexterous manipulation tasks and a modified LIBERO benchmark. LAC-WM improves downstream performance over EAC-WM by up to 46.7% on dexterous manipulation and 11.7% on LIBERO. Crucially, the unified latent action space allows LAC-WM's downstream performance to scale positively with the number of embodiments used during pretraining. In contrast, the disjoint action space in EAC-WM leads to decreased performance as the number of pretraining embodiments increases. These results highlight the importance of a unified action space for efficient cross-embodiment learning, addressing a key challenge in robotics. Project website: https://lacwm.github.io/

</details>

---

### [[20_Research/Papers/大模型/Skill-SLM_Agent_Skill-driven_Small_Language_Models_for_Reliable_Robot_Operation|Skill-SLM: Agent Skill-driven Small Language Models for Reliable Robot Operation]]

![[assets/2610.10812_figure.png|800]]

- **arXiv**: [2610.10812](https://arxiv.org/abs/2610.10812)
- **PDF**: https://arxiv.org/pdf/2610.10812
- **详细分析**: [[20_Research/Papers/大模型/Skill-SLM_Agent_Skill-driven_Small_Language_Models_for_Reliable_Robot_Operation|Skill-SLM: Agent Skill-driven Small Language Models for Reliable Robot Operation]]
- **作者**: Wenhao Wang, Yanyan Li, Jiawei Yuan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Skill-SLM: Agent Skill-driven Small Language Models for Reliable Robot Operation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small language models (SLMs) have been increasingly adopted for onboard robot operation because they enable intelligent decision-making. However, existing approaches are mainly distillation-oriented and rely on enumerating representative task-solution pairs. This makes dataset construction difficult and limits generalization to diverse robot tasks whose possible forms grow rapidly. This paper proposes Skill-SLM, a framework that reformulates SLM-driven robot operation as a task-decomposition and skill-composition problem. Given a natural language task instruction, Skill-SLM decomposes the task into subtasks, selects appropriate skills from the skill library, and orchestrates the selected skills into executable robot operations. First, to support the skill-driven workflow, we propose a novel robot operational skill aware context-free grammar (CFG) to extract the skills required to accomplish tasks and build the skill library accordingly. Then, we configure LLM teachers to induce and synthesize training datasets for the SLMs, enabling SLMs to decompose tasks and orchestrate skills reliably. Additionally, we employ a progressive skill orchestration strategy to improve the reliability of skill implementation and overall robot operation. Experiments on UAV operation tasks indicate that Skill-SLM substantially outperforms distillation-oriented baselines, especially on unseen tasks that require generalization of capabilities. Additional experiments on ground vehicle tasks further demonstrate that Skill-SLM can be applied to different robot platforms.

</details>

---

### [[20_Research/Papers/具身智能/TAPNAV_Humanoid_Navigation_through_Tactile_Active_Perception|TAPNAV: Humanoid Navigation through Tactile Active Perception]]

![[assets/2610.10748_figure.png|800]]

- **arXiv**: [2610.10748](https://arxiv.org/abs/2610.10748)
- **PDF**: https://arxiv.org/pdf/2610.10748
- **详细分析**: [[20_Research/Papers/具身智能/TAPNAV_Humanoid_Navigation_through_Tactile_Active_Perception|TAPNAV: Humanoid Navigation through Tactile Active Perception]]
- **作者**: Huaze Liu, Zhenyu Wu, Jaehwi Jang, Junjie Sheng, Andrew Collins, Aaron Xie, Zhaoyuan Gu, Kaijie Zhu, Ding Jiang, Kevin Cai, Ye Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《TAPNAV: Humanoid Navigation through Tactile Active Perception》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation in vision-denied environments is challenging for humanoid robots because proprioceptive odometry drifts and localization uncertainty accumulates rapidly. We present TAPNAV, a tactile active-perception framework that enables humanoid navigation toward a goal by actively probing surrounding structures without relying on vision. TAPNAV maintains a pose belief from odometry, IMU, and tactile contact observations, and couples uncertainty-aware global route planning with information-gain-driven local probing. The global planner searches for routes that keep predicted localization uncertainty bounded by exploiting opportunities for tactile correction, while the local planner selects probe actions that maximize expected information gain. A whole-body controller coordinates the humanoid's locomotion and end-effector contact to execute the planned navigation and probe motions. We evaluate TAPNAV in simulation and on a Unitree G1 across different floor plans and obstacle geometries. TAPNAV achieves lower state estimation error and a higher task completion rate than baselines. These results demonstrate that actively planning physical interactions with the environment can provide localization cues for reliable humanoid navigation without vision.

</details>

---

### [[20_Research/Papers/强化学习/TacHair_Tactile_Contact-Distribution_Guided_Online_Correction_for_Robotic_Hair_Stroking_and_Perception|TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception]]

![[assets/2610.10637_figure.png|800]]

- **arXiv**: [2610.10637](https://arxiv.org/abs/2610.10637)
- **PDF**: https://arxiv.org/pdf/2610.10637
- **详细分析**: [[20_Research/Papers/强化学习/TacHair_Tactile_Contact-Distribution_Guided_Online_Correction_for_Robotic_Hair_Stroking_and_Perception|TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception]]
- **作者**: Ruiyi Hu, Yongqiang Zhao, Daniel Bak, Yupeng Wang, Xuyang Zhang, Shan Luo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hair stroking is common in daily grooming and personal care, and is also widely used in hair-product evaluation, motivating robots with similar physical interaction capabilities. Existing robotic hair-care and surface-following methods mainly rely on trajectory planning, compliance, force regulation, or tactile-conditioned policies, but deformable hair can remain in contact while gradually drifting across the end-effector, making local interaction difficult to regulate. We propose TacHair, a tactile contact-distribution guided online correction framework that represents high-resolution tactile observations as a spatial hair-contact distribution. A visuotactile imitation policy generates the nominal stroking motion, while a separately trained residual module corrects local contact deviations, separating task progression from contact recovery. We evaluate TacHair in 525 real-robot trials across five head geometries and three hair conditions. A successful stroke requires both sufficient task progression and contact maintenance; our method improves success from 42.9% to 62.3% and contact maintenance from 59.4% to 88.0% over the same visuotactile policy without correction. These results demonstrate spatial tactile contact distributions as an effective feedback representation for contact-preserving interaction with deformable and visually occluded surfaces. Demos, code, and datasets are available at https://tachair.github.io.

</details>

---

### [[20_Research/Papers/具身智能/Teaching_a_Robot_Dog_New_Tricks_Diverse_Quadruped_Skills_via_Combined_Reinforcement_and_Imitation_Learning_with_Adversarial_Task_Selection|Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection]]

![[assets/2610.10601_figure.png|800]]

- **arXiv**: [2610.10601](https://arxiv.org/abs/2610.10601)
- **PDF**: https://arxiv.org/pdf/2610.10601
- **详细分析**: [[20_Research/Papers/具身智能/Teaching_a_Robot_Dog_New_Tricks_Diverse_Quadruped_Skills_via_Combined_Reinforcement_and_Imitation_Learning_with_Adversarial_Task_Selection|Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection]]
- **作者**: Lemon Foxmere, Anthony Furman, Yizheng Du, Oliver Chang, Leilani Gilpin, Steve McGuire
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.9（加权：具身智能 1.8，强化学习 0.2，机器人 1.9）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MTRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has enabled legged robots to perform a range of skills in single-task settings. However, applications such as farm robotics or space exploration require diverse skills such as locomotion, digging, or close-range surveying. Training an end-to-end policy to address this problem remains difficult due to challenges such as sample inefficiency and gradient conflict between tasks in multi-task learning. We propose a three-stage method that trains a single policy to perform distinct tasks such as walking, digging, and hopping, and compose them into novel behaviors such as crawling. First, multiple teacher policies are trained using RL on narrowly defined tasks. Then, two additional stages train a student policy with a multi-teacher distillation setup that uses a combined RL and Imitation Learning (IL) objective under an adversarial task selection process that focuses training on the worst-performing task. With this method, we train a student policy that performs 22 tasks using 8 teachers. Evaluations show our method preserves motion quality and tracks commands more accurately than PPO and distill-then-finetune baselines, and in some cases generalizes to new tasks without explicit training. Finally, we demonstrate real-world robustness by deploying the resulting policy on a Unitree B1 quadruped. Video: https://youtu.be/V9yX04EBcFA

</details>

---
