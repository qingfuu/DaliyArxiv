# cs.RO | Robotics | 2026-11-06

#arxiv #ComputerScience

**论文数**: 38

### [[20_Research/Papers/具身智能/OopsieRecover_Learning_Transferable_VLA_Corrections_from_Semantic_Interventions|OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions]]

![[assets/2611.08462_figure.png|800]]

- **arXiv**: [2611.08462](https://arxiv.org/abs/2611.08462)
- **PDF**: https://arxiv.org/pdf/2611.08462
- **详细分析**: [[20_Research/Papers/具身智能/OopsieRecover_Learning_Transferable_VLA_Corrections_from_Semantic_Interventions|OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions]]
- **作者**: Arpit Bahety, Skand Peri, Sriniket Ambatipudi, Chen Xu, Haruki Nishimura, Masha Itkina, Roberto Martín-Martín
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL, PRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models can perform a wide range of robotic manipulation tasks, but often fail during deployment. Teaching them to recover from these failures requires substantial corrective data: existing approaches learn to recover from failures by directly associating corrective actions with the observations in which they were demonstrated. For instance, DAgger-like fine-tuning can require tens to hundreds of interactions, yet the resulting policy may still fail to generalize the learned corrections beyond the demonstrated scenarios. We hypothesize that semantics can capture the underlying reasons for failures and their corrections, enabling policies to learn from only a handful of corrective demonstrations and generalize those corrections to novel objects, and scene variations. We propose OopsieRecover, a framework that uses abduction to infer the intent behind a small set of corrective demonstrations and encodes the inferred knowledge as dense spatial representations and conditional costs. These costs capture when a behavior is undesirable and steer the policy toward more desirable action regions. We experiment across 6 tasks and variations in object poses, scenes, and related tasks, and find that only a handful of corrective demonstrations can enable a VLA to overcome failures across a broad range of novel situations, without requiring new corrective data for each variation. Please refer to https://robin-lab.cs.utexas.edu/oopsierecover for videos.

</details>

---

### [[20_Research/Papers/强化学习/Latent_RL_Priors_for_Data-Efficient_Dexterous_Manipulation|Latent RL Priors for Data-Efficient Dexterous Manipulation]]

![[assets/2611.08458_figure.png|800]]

- **arXiv**: [2611.08458](https://arxiv.org/abs/2611.08458)
- **PDF**: https://arxiv.org/pdf/2611.08458
- **详细分析**: [[20_Research/Papers/强化学习/Latent_RL_Priors_for_Data-Efficient_Dexterous_Manipulation|Latent RL Priors for Data-Efficient Dexterous Manipulation]]
- **作者**: Yixiao Wang, Peiyi Chen, Mustafa Mukadam, Shreekant Gayaka, Masayoshi Tomizuka, Son Tran
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Latent RL Priors for Data-Efficient Dexterous Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning dexterous manipulation from limited visual demonstrations is challenging because policies must acquire both perceptual grounding and precise control, while reinforcement learning (RL) in simulation can acquire rich control behaviors from large-scale interaction with privileged information. We introduce \textbf{Latent RL Prior}, a two-stage framework that reuses this control knowledge for data-efficient visual policy learning. During privileged pretraining, we distill large-scale RL rollouts into a flow-matching action decoder conditioned on proprioception and latent task context. During visual adaptation, we freeze the decoder and learn a visual interface that maps images to its latent context using action supervision alone, without privileged labels or latent targets. The same decoder can further be shared across arms by learning coordinated visual contexts for bimanual manipulation. Across three simulated tasks, our method outperforms full-parameter fine-tuning of $π_{0.5}$ and GR00T N1.7 in the low-data regime; on door lifting and bimanual assembly, it surpasses full-data baselines using $10\times$ and $5\times$ fewer demonstrations, respectively. Further analysis shows that direct visual-to-latent conditioning improves adaptation performance and training stability over routing visual predictions through the pretrained state encoder. Robustness to unseen mass variation and greater linear accessibility of contact-force information in decoder representations further provide evidence of retained RL-acquired control knowledge. Project website: https://yixiaowang7.github.io/latent-rl-prior-page/.

</details>

---

### [[20_Research/Papers/大模型/SCALE_Real-Time_Latent_Communication_for_Cyber-Physical_Agents|SCALE: Real-Time Latent Communication for Cyber-Physical Agents]]

![[assets/2611.08390_figure.png|800]]

- **arXiv**: [2611.08390](https://arxiv.org/abs/2611.08390)
- **PDF**: https://arxiv.org/pdf/2611.08390
- **详细分析**: [[20_Research/Papers/大模型/SCALE_Real-Time_Latent_Communication_for_Cyber-Physical_Agents|SCALE: Real-Time Latent Communication for Cyber-Physical Agents]]
- **作者**: Shanghao Shi, Jian Xiao, Ching-Hsiang Chan, Sanjoy Baruah, Sastry Kompella, Yevgeniy Vorobeychik, William Yeoh, Ning Zhang
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《SCALE: Real-Time Latent Communication for Cyber-Physical Agents》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent communication enables agents to collaborate efficiently by directly exchanging intermediate model representations rather than raw sensor data or text messages. Existing approaches, however, are primarily designed for LLM agents and do not consider the bandwidth constraints and heterogeneous task deadlines faced by cyber-physical agents. In this work, we propose SCALE, a real-time latent communication method tailored for cyber-physical agents. Motivated by the spatio-temporal continuity of the physical world, SCALE matches tokens across consecutive latent messages using similarity scores to identify reusable information and avoid redundant transmission. It then profiles the semantic gain and communication cost of transmitting different amounts of latent information. Based on these profiles, SCALE employs a real-time scheduler that jointly determines which pending messages to transmit and how many latent tokens to send, subject to available bandwidth and task deadlines. We evaluate SCALE across three cyber-physical benchmarks and a physical spider robot case study under diverse network conditions and heterogeneous task deadlines. Our results show that SCALE significantly improves both task performance and on-time delivery in bandwidth-constrained networks. Our code is available at: https://anonymous.4open.science/r/SCALE-4E80/.

</details>

---

### [[20_Research/Papers/具身智能/SLA_Scaling_Spatial-Language-Action_Model_via_Continual_Pre-training|SLA: Scaling Spatial-Language-Action Model via Continual Pre-training]]

![[assets/2611.08373_figure.png|800]]

- **arXiv**: [2611.08373](https://arxiv.org/abs/2611.08373)
- **PDF**: https://arxiv.org/pdf/2611.08373
- **详细分析**: [[20_Research/Papers/具身智能/SLA_Scaling_Spatial-Language-Action_Model_via_Continual_Pre-training|SLA: Scaling Spatial-Language-Action Model via Continual Pre-training]]
- **作者**: Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SLA: Scaling Spatial-Language-Action Model via Continual Pre-training》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BridgeVLA, ET-VLA, GeoVLA, Mind-VLA, OpenVLA, PointVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-Action Model that scales implicit spatial alignment to continual pre-training and maintains it during downstream post-training. Initialized from a pretrained pi05 policy, SLA jointly optimizes action prediction and alignment between intermediate visual embeddings and spatial representations from a frozen 3D perception model. We curate and unify heterogeneous robot datasets to support spatial learning across diverse embodiments, tasks, and scenes. To accommodate this diversity, we introduce feature-dependent gates that adaptively aggregate visual embeddings from multiple VLA layers for spatial supervision. The teacher further exploits partially available depth and camera calibration alongside RGB observations, enabling effective use of heterogeneous geometric annotations. Probabilistic state dropout encourages reliance on visual cues and mitigates overfitting to demonstration trajectories. All auxiliary components are used only during training, allowing direct reuse of pretrained VLA weights and preserving the original inference architecture.

</details>

---

### [[20_Research/Papers/机器人/Radio-to-Pose_Information_for_Gauge-Drift_Correction_in_Cooperative_Localization|Radio-to-Pose Information for Gauge-Drift Correction in Cooperative Localization]]

![[assets/2611.08361_figure.png|800]]

- **arXiv**: [2611.08361](https://arxiv.org/abs/2611.08361)
- **PDF**: https://arxiv.org/pdf/2611.08361
- **详细分析**: [[20_Research/Papers/机器人/Radio-to-Pose_Information_for_Gauge-Drift_Correction_in_Cooperative_Localization|Radio-to-Pose Information for Gauge-Drift Correction in Cooperative Localization]]
- **作者**: Aditya Iyer, Andy Ye, Akshay Narayan, Nora Ayanian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Radio-to-Pose Information for Gauge-Drift Correction in Cooperative Localization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative localization uses odometry and inter-robot measurements to estimate the motion of a robot team. These measurements describe only relative geometry, but the team's estimated position and orientation can drift together over time, i.e., gauge drift. In this work, we study correction of this gauge drift using a radio attenuation map registered in the same world coordinate frame used for robot poses. Specifically, we propose Radio-to-Pose Information (RPI), an interface that converts power residuals and their pose derivatives into a Gaussian information matrix and vector pair. RPI builds on the insight that received power is sensitive to shared displacement in the world map. The pose estimator uses the interface together with odometry and inter-robot measurements to update poses and minimize uncertainty. We characterize the shared motions detectable from the map and observed links. For an uncertain shared map, RPI keeps correlations across robots and time and reproduces joint Gaussian pose estimates and covariances. Across $1000$ simulated Gaussian trials, RPI matches the results of joint estimation. Across 32 paired trials with a registered map, RPI reduces common-position RMSE from $0.542$m to $0.140$m in a $50\times50$m arena compared with a baseline that uses radio only to weight relative measurements.

</details>

---

### [[20_Research/Papers/世界模型/GPWM_Modeling_the_World_as_3D_Particle_Motion|GPWM: Modeling the World as 3D Particle Motion]]

![[assets/2611.08338_figure.png|800]]

- **arXiv**: [2611.08338](https://arxiv.org/abs/2611.08338)
- **PDF**: https://arxiv.org/pdf/2611.08338
- **详细分析**: [[20_Research/Papers/世界模型/GPWM_Modeling_the_World_as_3D_Particle_Motion|GPWM: Modeling the World as 3D Particle Motion]]
- **作者**: Robert Ren, Matthew Bronars, He Zhu, Yikai Tang, Jianing Zhang, Sergey Zakharov, Pavel Tokmakov, Katerina Fragkiadaki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，世界模型 0.4，机器人 0.7）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《GPWM: Modeling the World as 3D Particle Motion》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet, PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce GPWM, a Generative Particle World Model that predicts how 3D scenes evolve by generating the motion of particles and rigid bodies over time. Unlike video world models that generate scene appearance, GPWM operates directly in 3D physical space. A single representation and architecture cover rigid, deformable, cloth, and granular materials, in both passive physics and robotic interaction. GPWM is an object-aware multi-resolution transformer that combines flow matching with diffusion forcing to generate coherent physical trajectories far beyond its training horizon. We train and evaluate GPWM on ParticleWorlds, a 25.5-million-frame corpus spanning diverse geometries, materials, interactions, and robot embodiments. GPWM outperforms the best prior learned-dynamics baseline in each of six physical domains, reducing prediction error by 31% on average. Breaking from the domain-specific setting of prior methods, a single Unified GPWM models these heterogeneous regimes with one set of weights, largely outperforming per-domain baselines and even surpassing our own specialist models in two domains. GPWM further generalizes to unseen geometries, physical properties, object counts, and rollout horizons. Beyond prediction, GPWM enables contact-rich planning by learning a generative prior over joint actuator-object motion. Instead of searching over unconstrained actions, planning searches the model's latent noise for interactions that achieve a desired object-space goal. With the same world model, noise-space planning substantially outperforms action-space search on pushing and picking, where complex contact sequences are hard to discover. Executed open-loop in simulation, the resulting plans achieve goal-directed manipulation without reference action trajectories or goal-specific policies.

</details>

---

### [[20_Research/Papers/机器人/RoboARCade_Benchmarking_Agentic_Robot_Control|RoboARCade: Benchmarking Agentic Robot Control]]

![[assets/2611.08209_figure.png|800]]

- **arXiv**: [2611.08209](https://arxiv.org/abs/2611.08209)
- **PDF**: https://arxiv.org/pdf/2611.08209
- **详细分析**: [[20_Research/Papers/机器人/RoboARCade_Benchmarking_Agentic_Robot_Control|RoboARCade: Benchmarking Agentic Robot Control]]
- **作者**: Satvik Sharma, Hengyuan Hu, Mihika Kamat, Dorsa Sadigh, Jeannette Bohg
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《RoboARCade: Benchmarking Agentic Robot Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, EmbodiedBench, MVBench, Meta-World, OSWorld, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improvements in multi-modal capabilities have enabled agents to act directly as robot policies, a setting we refer to as agentic robot control (ARC). We introduce RoboARCade, a benchmark of long-horizon manipulation tasks across three embodiments designed to test in-context adaptation, memory, and reasoning for precise control. The tasks build on existing open-source benchmarks, which we make harder by widening the range of initial conditions. RoboARCade is easy to use and extend: all tasks run on a single simulation backend, MuJoCo, each task is a self-contained data pack, and agents connect through interchangeable interfaces, so new tasks, agents, and interfaces can be added independently. The benchmark separates leading agents: GPT-6 Astra achieves 49.8% compared with 43.6% for Claude Fable 5.1, leaving substantial room for improvement. Comparing two interfaces, we find that a richer visual interface adds only 1.5 to 6.8 points at 1.7 to 2.3 times the cost. Failures stem mostly from choosing a poor manipulation strategy or executing a good one imprecisely, rarely from misunderstanding the scene, and agents incorrectly claim success on 24% to 39% of attempted subtasks. Agents can also improve without human input: one successful demonstration in context raises Astra's score from 53.5% to 73.0% on a five-task subset, and a prompt the agent writes and revises itself reaches 72.0%. Code, videos and full traces are available at roboarcade.org.

</details>

---

### [[20_Research/Papers/机器人/Educational_robotics_beyond_ROS_a_custom_library_for_direct_transfer_of_Webots_controllers_in_the_Turtlebot3|Educational robotics beyond ROS: a custom library for direct transfer of Webots controllers in the Turtlebot3]]

![[assets/2611.08142_figure.png|800]]

- **arXiv**: [2611.08142](https://arxiv.org/abs/2611.08142)
- **PDF**: https://arxiv.org/pdf/2611.08142
- **详细分析**: [[20_Research/Papers/机器人/Educational_robotics_beyond_ROS_a_custom_library_for_direct_transfer_of_Webots_controllers_in_the_Turtlebot3|Educational robotics beyond ROS: a custom library for direct transfer of Webots controllers in the Turtlebot3]]
- **作者**: Jaime P. Pérez-Moro, Alejandro Romero, Hector Quintian, Francisco Bellas
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，机器人 2.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Educational robotics beyond ROS: a custom library for direct transfer of Webots controllers in the Turtlebot3》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot Operating System (ROS) is becoming a standard in robotics courses at higher education, but its installation, configuration and distributed programming model can introduce a significant entry barrier in the new landscape of AI-based master and degree studies, where many students do not have a strong informatics background. This paper presents an educational experience that enables students to program a TurtleBot3 Burger directly in Python, while preserving a direct transfer path from simulation to the physical robot. The approach is based on a custom library that mirrors the Webots API, allowing the same controller code to be executed in the simulator and on the real TurtleBot3 with minimal modification. The library provides access to the robot motors, wheel encoders, inertial sensors and LiDAR, and is complemented by scripts that automate deployment and execution on the physical platform. It was used in a master-level course on introductory autonomous vehicles, and initial student feedback suggests that the approach reduces the perceived complexity of ROS-related infrastructure and helps learners focus on algorithmic logic and real-world behaviour.

</details>

---

### [[20_Research/Papers/机器人/H-TRIP_Exact_Many-to-Many_Distance_Index_for_Multi-Robot_Exploration|H-TRIP: Exact Many-to-Many Distance Index for Multi-Robot Exploration]]

![[assets/2611.08139_figure.png|800]]

- **arXiv**: [2611.08139](https://arxiv.org/abs/2611.08139)
- **PDF**: https://arxiv.org/pdf/2611.08139
- **详细分析**: [[20_Research/Papers/机器人/H-TRIP_Exact_Many-to-Many_Distance_Index_for_Multi-Robot_Exploration|H-TRIP: Exact Many-to-Many Distance Index for Multi-Robot Exploration]]
- **作者**: Elif A. Özaslan, Tolga Özaslan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《H-TRIP: Exact Many-to-Many Distance Index for Multi-Robot Exploration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier-based exploration systems repeatedly evaluate geodesic travel costs between robot poses and candidate viewpoints, and tour-based planners consume the full pairwise distance matrix built from them. Recomputing these matrices with one graph search per source scales with the explored map size, whereas distance caches that refresh only locally affected or newly created frontiers can retain stale costs between surviving pairs when newly discovered free space creates a global shortcut. We present H-TRIP (Hierarchical Tropical Rank-one Incremental Propagation), an exact distance index grounded in Kleene algebra over the min-plus semiring for monotonically growing occupancy grids. H-TRIP partitions the known map into a spatial hierarchy with fixed boundary ports. Each unknown-to-free revelation is decomposed into efficient rank-one min-plus edge insertions at the affected leaf, and only decreased port-to-port summaries are propagated along its ancestor chain. A shared hierarchical lift evaluates the dense many-to-many matrix of shortest distances for all active query points on the occupancy map. We prove that sequential insertions preserve exact shortest-path distances on the grid. Benchmark experiments confirm exact agreement with reference searches on fully built maps and show that dense many-to-many queries at a few dozen viewpoints are up to two orders of magnitude faster than sequential k x BFS. On exploration runs with sixteen robots, in-loop queries on the growing occupancy graph are 2.21x-8.59x faster than co-scheduled k x BFS on maps with side 256, 512, and 1024 cells.

</details>

---

### [[20_Research/Papers/机器人/H-BRICK_Hierarchical_Boundary_Reachability_Index_with_Compressed_Kleene_Closure_for_Directed_Grid_Graphs|H-BRICK: Hierarchical Boundary Reachability Index with Compressed Kleene Closure for Directed Grid Graphs]]

![[assets/2611.08119_first_page.png|800]]

- **arXiv**: [2611.08119](https://arxiv.org/abs/2611.08119)
- **PDF**: https://arxiv.org/pdf/2611.08119
- **详细分析**: [[20_Research/Papers/机器人/H-BRICK_Hierarchical_Boundary_Reachability_Index_with_Compressed_Kleene_Closure_for_Directed_Grid_Graphs|H-BRICK: Hierarchical Boundary Reachability Index with Compressed Kleene Closure for Directed Grid Graphs]]
- **作者**: Tolga Özaslan, Elif A. Özaslan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《H-BRICK: Hierarchical Boundary Reachability Index with Compressed Kleene Closure for Directed Grid Graphs》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repeated directed reachability queries arise in online path planning, task-agent allocation, and swarm control on static grid maps, where reachability is asymmetric and full transitive closure is storage-prohibitive. We introduce H-BRICK, a Hierarchical Boundary Reachability Index with Compressed Kleene closure for exact cell-to-cell queries on directed grid graphs. H-BRICK partitions the graph into tiles, computes a local Boolean Kleene closure within each tile, and projects it onto the tile's boundary ports. The resulting directed port-to-port summaries are then composed recursively across shared interfaces up to a single root covering the graph. We prove algebraically that the construction is exact: in the Boolean Kleene algebra of binary relations, every composed summary equals the boundary projection of the regional reflexive transitive closure, and every cell-to-cell query agrees with reachability in the original graph. Experiments on directed grid graphs across diverse map topologies compare H-BRICK against directed search and component-based baselines, and compare its storage requirements against full transitive closure. A batched reachability evaluation further demonstrates that sharing endpoint lifts across many-source/many-target queries amortizes hierarchical traversal and, at k=64, yields a 5.0x-22.9x throughput improvement over the scalar query loop. The results show that hierarchical boundary compression is most advantageous in query-intensive spatial graphs where online search traverses large reachable regions and the hierarchy maintains compact boundary interfaces.

</details>

---

### [[20_Research/Papers/具身智能/An_Integrated_Open-Source_Stack_for_Vision-Based_Autonomous_Navigation_of_Wheeled_Rovers|An Integrated Open-Source Stack for Vision-Based Autonomous Navigation of Wheeled Rovers]]

![[assets/2611.08100_figure.png|800]]

- **arXiv**: [2611.08100](https://arxiv.org/abs/2611.08100)
- **PDF**: https://arxiv.org/pdf/2611.08100
- **详细分析**: [[20_Research/Papers/具身智能/An_Integrated_Open-Source_Stack_for_Vision-Based_Autonomous_Navigation_of_Wheeled_Rovers|An Integrated Open-Source Stack for Vision-Based Autonomous Navigation of Wheeled Rovers]]
- **作者**: Iaroslav Kolomiets, Iaroslav Sheipak, Mikhail Reppo, Vsevolod Egorov, Viktor Chertopolokhov, Isaac Chairez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《An Integrated Open-Source Stack for Vision-Based Autonomous Navigation of Wheeled Rovers》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based rover autonomy requires integrating perception, localization, planning and platform-specific control under limited sensing and computing resources. We present an open-source ROS 2 stack for following directional arrows, reaching a terminal cone and returning autonomously to the start. It connects YOLOv8n detection and geometric direction, range and bearing estimation with RGB-D SLAM, wheel-inertial state estimation, kinematics-aware planning, behavior-tree mission management and STM32 actuation. Standard interfaces separate reusable autonomy from the hardware layer; a proportional path-following plugin supports low-speed rover motion. Public resources include software, configuration, a labeled dataset, trained weights and evaluation logs. On 478 held-out images, the detector achieves mAP@0.5 of 0.720 under the Ultralytics evaluator and outperforms a classical OpenCV baseline under a shared evaluation protocol. The reported perception latency is 25 ms on a Jetson Orin NX. Three missions, one indoor and two outdoor, demonstrate marker-guided navigation and autonomous return without operator motion commands or reported collisions. Field results document integration failures and corrective choices; repeated instrumented trials remain necessary to quantify physical navigation errors and reliability.

</details>

---

### [[20_Research/Papers/具身智能/STEP_Spatiotemporal_Training_with_Explicit_Prediction_for_Perceptive_Humanoid_Locomotion|STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion]]

![[assets/2611.08097_figure.png|800]]

- **arXiv**: [2611.08097](https://arxiv.org/abs/2611.08097)
- **PDF**: https://arxiv.org/pdf/2611.08097
- **详细分析**: [[20_Research/Papers/具身智能/STEP_Spatiotemporal_Training_with_Explicit_Prediction_for_Perceptive_Humanoid_Locomotion|STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion]]
- **作者**: Youhao Lyu, Chenghao Sun, Zhenxuan Ding, Shuting Zhang, Ziyang Dong, Wenhao Cui
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For perceptive humanoid locomotion, the relevance of terrain geometry depends on the robot's body state and how both evolve under its actions. Existing work has advanced terrain-aware sensory fusion and cross-modal prediction, improving how visual and proprioceptive information is combined and related. However, feature aggregation alone does not specify which cross-modal relationships should be learned, while prediction between simultaneous observations does not explicitly constrain their action-dependent evolution. We present Spatiotemporal Training with Explicit Prediction (STEP), a one-stage framework that jointly supervises cross-modal relationships and action-dependent state evolution within a shared control representation. Multiple learned queries aggregate depth and proprioceptive tokens into a compact policy state. Bidirectional masked prediction uses each visible modality to predict latent features of the omitted modality, explicitly supervising terrain-body relationships. An action-conditioned predictor maps the current policy state and executed action to the next fused state, with an exponential-moving-average target defined directly in the policy representation space. Simulation comparisons show overall improvements in terrain traversal over evaluated fusion alternatives and ablations, while depth-dropout and delay experiments demonstrate the benefits of both predictive objectives under degraded visual input. Deployed on a 23-DoF Noetix E1 humanoid with onboard sensing, STEP succeeds in 98 of 100 hardware trials across stairs, a 40\,cm platform, a 70\,cm gap, stepping stones, and backward stair traversal without rearward terrain visibility.

</details>

---

### [[20_Research/Papers/强化学习/Leave_It_Better_Than_Found_Value-Guided_Cooperation_in_Sequential_Tasks|Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks]]

![[assets/2611.08075_figure.png|800]]

- **arXiv**: [2611.08075](https://arxiv.org/abs/2611.08075)
- **PDF**: https://arxiv.org/pdf/2611.08075
- **详细分析**: [[20_Research/Papers/强化学习/Leave_It_Better_Than_Found_Value-Guided_Cooperation_in_Sequential_Tasks|Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks]]
- **作者**: Mario Gomez Andreu, Michael Amir, Antonio Marino, Tianxu An, Marco Hutter, Amanda Prorok
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Leave It Better Than Found: Value-Guided Cooperation in Sequential Tasks》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the problem of sequential task continuation, where one robot acts in a workspace that has been affected by a previous robot. Current approaches in multi-robot cooperation rely heavily on co-training or co-optimization, assumingthat the robots have access to collective interaction data during the policy training or planning process. However, as increasingly varied robotic embodiments and policies are deployed and operate in the same real-world environment, learning policies for cooperation becomes infeasible due to the combinatorial explosion of possible robot combinations that need to be accounted for. To address this challenge, this paper considers the problem of ad hoc sequential cooperation between robots that have never before operated together in a shared environment. We demonstrate that robots can explicitly communicate their environmental preferences through sharing their value functions, enabling coordination without the need for prior joint training. To ground this exchange and prevent overconfidence in out-of-distribution states, we further introduce a k-nearest neighbors (KNN)- based uncertainty filter. Our method yields an increase of up to 48.5 pp compared with naive or even selfish agents, in task success rates across simulated and real-world experiments, demonstrating that value function transmission between agents is useful not merely as an internal learning tool, but as an effective basis for ad hoc coordination. Website: https://proroklab.github.io/PAVE/

</details>

---

### [[20_Research/Papers/强化学习/Terrain-Indexed_Motion_Priors_and_Geometric_Support_for_Extreme_Humanoid_Parkour|Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour]]

![[assets/2611.08056_figure.png|800]]

- **arXiv**: [2611.08056](https://arxiv.org/abs/2611.08056)
- **PDF**: https://arxiv.org/pdf/2611.08056
- **详细分析**: [[20_Research/Papers/强化学习/Terrain-Indexed_Motion_Priors_and_Geometric_Support_for_Extreme_Humanoid_Parkour|Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour]]
- **作者**: Chenghao Sun, Youhao Lyu, Zizheng Li, Shuting Zhang, Ziyang Dong, Wenhao Cui
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a progressive imitation framework that learns terrain-appropriate humanoid parkour skills and subsequently adapts their hand--knee support. Human demonstrations provide traversal behaviors, but their contact patterns need not suit a robot's proportions or the available support surfaces. Our framework changes the role of demonstrations across three stages: privileged imitation produces physically executable robot references; terrain-indexed adversarial motion priors guide skill acquisition; and geometric support guidance with a reduced motion-prior weight enables contact adaptation. Candidate-based precontact attraction and actual-contact evaluation guide support without prescribing a contact sequence. The deployed policy selects behaviors from onboard depth, proprioception, and velocity commands without an external skill label. On the Noetix E1, the policy achieves 96.34\% hybrid success in simulation and transfers without real-world policy fine-tuning, completing 29 of 30 individual obstacle trials and four of five hybrid courses. Support-adaptation ablations show higher traversal success for the complete adaptation stage on the tested terrains, while qualitative observations show changes in contact placement. These results support acquiring skills from demonstrations before relaxing their influence to accommodate robot-specific support configurations.

</details>

---

### [[20_Research/Papers/大模型/HITCH_Teaching_a_Vision-Language_Model_to_Operate_a_Humanoid_through_a_Whole-Body_Harness|HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness]]

![[assets/2611.08039_figure.png|800]]

- **arXiv**: [2611.08039](https://arxiv.org/abs/2611.08039)
- **PDF**: https://arxiv.org/pdf/2611.08039
- **详细分析**: [[20_Research/Papers/大模型/HITCH_Teaching_a_Vision-Language_Model_to_Operate_a_Humanoid_through_a_Whole-Body_Harness|HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness]]
- **作者**: Qingzhou Lu, Chenxin Liu, Xinming Wang, Liu Cao, Yanjiang Guo, Mengdi Xu, Jianyu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.5，大模型 0.7，机器人 1.1）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling vision-language models (VLMs) to control humanoid robots requires both reliable whole-body interfaces and knowledge of how to use the body that carries over across tasks. We present HITCH (Harness Interfaces To Command Humanoids), a harness in which perception returns the 3D position of any point the VLM selects in its image, and execution turns commands for the pelvis, torso, hands, walking, and gaze into whole-body motion with a learned tracker. We find that both measuring the scene and executing commands accurately raise task success. We then fine-tune a VLM on trajectories in which teacher policies solve five base tasks through HITCH, so that it learns how to operate the humanoid. Without task-specific trajectories, the fine-tuned model completes 51% of SIMPLE episodes and 42.5% of HumanoidArena episodes, and adding five trajectories per SIMPLE task raises its SIMPLE success to 95%. On a real G1, it carries a box and walks to a goal without real training data.

</details>

---

### [[20_Research/Papers/机器人/Development_of_Anthropomorphic_Arm_for_collaborative_and_Home_Service_Robot_CHARMIE|Development of Anthropomorphic Arm for collaborative and Home Service Robot CHARMIE]]

![[assets/2611.08013_first_page.png|800]]

- **arXiv**: [2611.08013](https://arxiv.org/abs/2611.08013)
- **PDF**: https://arxiv.org/pdf/2611.08013
- **详细分析**: [[20_Research/Papers/机器人/Development_of_Anthropomorphic_Arm_for_collaborative_and_Home_Service_Robot_CHARMIE|Development of Anthropomorphic Arm for collaborative and Home Service Robot CHARMIE]]
- **作者**: Hafiz Adil, Tiago Ribeiro, Antonio Ribeiro, Carolina Lopes, Joana Coelho, Gil Lopes, Fernando Ribeiro
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Development of Anthropomorphic Arm for collaborative and Home Service Robot CHARMIE》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Service Robots are becoming a reality and are progressing by leaps and bounds. Alongside this avenue of robotics is also the field of prosthetics, which is evolving rapidly. These topics are hot cakes in the industry and are widely developed. Some have one quality, and some have others, but are making a shoreline towards success. The development of arm and hand as individual or as a package is becoming common as more and more advanced collaborative robots come to the surface and join their human counterparts in the real world. This dissertation presents an open-source 3D-printed arm which was assembled and programmed on two fronts. The first is the control of the hand by utilising teleoperation with a camera and ML-based hand pose estimation. Secondly, it is the control via kinematics utilising the Denavit-Hartenberg method to define the motion and to find the position of the end effector in 3D space.

</details>

---

### [[20_Research/Papers/机器人/Symmetry-Aware_Surrogate-Assisted_Testing_of_UAVs|Symmetry-Aware Surrogate-Assisted Testing of UAVs]]

![[assets/2611.08012_first_page.png|800]]

- **arXiv**: [2611.08012](https://arxiv.org/abs/2611.08012)
- **PDF**: https://arxiv.org/pdf/2611.08012
- **详细分析**: [[20_Research/Papers/机器人/Symmetry-Aware_Surrogate-Assisted_Testing_of_UAVs|Symmetry-Aware Surrogate-Assisted Testing of UAVs]]
- **作者**: Anas Shrinah, Chris Bennett, Kerstin Eder
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Systems

#### 研究背景与动机

《Symmetry-Aware Surrogate-Assisted Testing of UAVs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate a symmetry-aware surrogate-assisted testing approach for UAV autopilots. The proposed approach exploits geometric symmetries between flight missions by trans- forming obstacle configurations into a shared canonical coordi- nate frame. This enables a neural-network surrogate trained on a single reference mission to be reused across arbitrary missions, reducing the amount of high-fidelity simulation data required for training. The surrogate model is trained to predict the minimum clearance distance between a UAV and surrounding obstacles and is used to guide test generation towards safety-critical scenarios. We evaluate this approach using the Aerialist UAV test bench and benchmark its performance against techniques from the 2024 to 2026 UAV Testing Competitions. Results show that the approach achieves an average critical-test-case hit rate of 42% across the evaluated missions, compared with approximately 10% for the constrained-random baseline used to generate the training data. This approach also achieves high input diversity and competitive benchmark performance. However, our findings reveal limitations in transferring surrogate predictions across missions with differing flight-path characteristics, highlighting the boundaries of geometric canonicalization. To support reproducibility and future research, we provide the trained surrogate model and a dataset comprising more than 2,500 high-fidelity simulations.

</details>

---

### [[20_Research/Papers/机器人/A_Unified_Fractal_Impedance_Control_Framework|A Unified Fractal Impedance Control Framework]]

![[assets/2611.08009_figure.jpeg|800]]

- **arXiv**: [2611.08009](https://arxiv.org/abs/2611.08009)
- **PDF**: https://arxiv.org/pdf/2611.08009
- **详细分析**: [[20_Research/Papers/机器人/A_Unified_Fractal_Impedance_Control_Framework|A Unified Fractal Impedance Control Framework]]
- **作者**: Adnan Takriti, Mahmoud Sadeq, Quentin Rouxel, Daniele Cafolla, Michael Mistry, Carlo Tiseo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Unified Fractal Impedance Control Framework》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical human--robot interaction requires controllers capable of maintaining intrinsically bounded interactions with the environment. The Fractal Impedance Controller (FIC) has been proven to guarantee these safety characteristics by design. This paper introduces the robotic implementation and experimental validation of its most advanced architecture: the Harmonic-Passive Motion Paradigm (H-PMP), an evolution of the Passive Motion Paradigm designed to mimic human-like interaction. Furthermore, we present a unified framework for FIC deployment, supported by an open-source software suite featuring ROS2, MuJoCo, and physical hardware integrations. Through three experiments conducted on a Kinova Gen3 arm (trajectory tracking, a wall press with sudden loss of contact, and learning-by-demonstration) we compare the H-PMP against earlier FIC architectures. The results demonstrate that the H-PMP achieves a seamless trade-off between admittance and impedance behaviours. This makes it ideal for deployment in unstructured environments, enabling the robot to transition between interaction modes with no computational overhead.

</details>

---

### [[20_Research/Papers/具身智能/AffordJEV_Affordance_Grounding_by_Confirming_Candidate_Regions|AffordJEV: Affordance Grounding by Confirming Candidate Regions]]

![[assets/2611.07896_first_page.png|800]]

- **arXiv**: [2611.07896](https://arxiv.org/abs/2611.07896)
- **PDF**: https://arxiv.org/pdf/2611.07896
- **详细分析**: [[20_Research/Papers/具身智能/AffordJEV_Affordance_Grounding_by_Confirming_Candidate_Regions|AffordJEV: Affordance Grounding by Confirming Candidate Regions]]
- **作者**: Jincheng Li, Yutian Zhang, Jianyu Zhang, Xinshun Wang, Mengyuan Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《AffordJEV: Affordance Grounding by Confirming Candidate Regions》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Affordance grounding asks which visible part of an object performs a requested operation, a basic capability for embodied manipulation and human--robot interaction. Most existing methods follow a System Two paradigm: a multimodal language model first writes a chain of thought and then turns its conclusion into a box or points for a segmenter. This incurs considerable inference cost, gives the semantic decision little direct control over the extent of the final region, and makes mistakes hard to correct. Yet locating an affordance is essentially a perceptual judgment that need not be argued out in words. We therefore propose, in which frozen segmenters propose candidate regions and a System One model decides directly which of them perform the operation, generating no text and reading each decision from a single forward pass. Our contributions are twofold. (1) An inference framework that confirms candidate regions level by level, from object to part to sub-part, with evidence passed between the levels in both directions so that the levels correct one another. (2) A System One model trained for this framework: existing System One models are built for general-purpose decisions, judge one candidate per request and are ill-suited to the framework's region questions, so ours learns directly from the requests the framework itself produces and judges all candidates of a level at once. Trained only on InstructPart and evaluated with definition-aligned operation words, outperforms chain-of-thought methods in domain and in zero-shot transfer to UMD and IIT-AFF, is better overall than existing System One models run in the same framework, and needs fewer judge requests. To our knowledge, is the first approach to bring System One models to affordance grounding.

</details>

---

### [[20_Research/Papers/具身智能/TactileLab_Sim-to-Real_Dexterous_Robot_Manipulation_with_Efficient_Shear-Sensitive_Tactile_Simulation|TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation]]

![[assets/2611.07881_figure.jpg|800]]

- **arXiv**: [2611.07881](https://arxiv.org/abs/2611.07881)
- **PDF**: https://arxiv.org/pdf/2611.07881
- **详细分析**: [[20_Research/Papers/具身智能/TactileLab_Sim-to-Real_Dexterous_Robot_Manipulation_with_Efficient_Shear-Sensitive_Tactile_Simulation|TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation]]
- **作者**: Yijiong Lin, Wenhao He, Toby Jack, Max Yang, Haoran Li, Nathan F. Lepora
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 5.0（加权：具身智能 3.6，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PETS-Net, Real-to-Sim, TacFlowNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic simulators that represent shear within tactile sensing are becoming increasingly important for contact-rich manipulation. However, simulating contact shear with high-fidelity deformable or soft-body simulation is computationally demanding, limiting scalability to large-scale reinforcement learning. Here we introduce \textit{TactileLab}, a scalable multimodal tactile simulation framework built on IsaacLab, with a particular focus on a new optical-flow-based tactile representation termed \textit{simulated tactile flow}. Instead of relying on soft-body physics to model shear deformation, TactileLab uses rigid-body simulation to efficiently estimate dense tangential motion at the contact interface, producing tactile flow fields that encode shear-relevant contact dynamics. This flow field complements geometric features from a contact depth field. We further introduce a novel policy architecture for jointly processing long-horizon proprioceptive signals and rich tactile observations. Across multiple contact-rich tasks, policies trained using simulated tactile flow learn efficiently at scale and exhibit emergent contact-aware behaviours. To facilitate sim-to-real policy deployment, we then propose a novel real-to-sim tactile translation method that maps real tactile image streams to simulated tactile flow and depth fields, together with a new tactile data collection method, and validate it across diverse tactile sensor designs. Using this pipeline, we demonstrate real-world deployment on tasks encompassing dual-arm and dexterous in-hand manipulation. Overall, TactileLab provides an end-to-end sim-to-real framework for scalable tactile policy learning, enabling diverse shear-sensitive manipulation across heterogeneous tactile robotic systems.

</details>

---

### [[20_Research/Papers/机器人/A_Sequential_Framework_for_Urban_Drone_Delivery_Network_Design,_Vehicle_Sizing,_and_Energy_and_Cost_Assessment|A Sequential Framework for Urban Drone Delivery: Network Design, Vehicle Sizing, and Energy and Cost Assessment]]

![[assets/2611.07808_figure.png|800]]

- **arXiv**: [2611.07808](https://arxiv.org/abs/2611.07808)
- **PDF**: https://arxiv.org/pdf/2611.07808
- **详细分析**: [[20_Research/Papers/机器人/A_Sequential_Framework_for_Urban_Drone_Delivery_Network_Design,_Vehicle_Sizing,_and_Energy_and_Cost_Assessment|A Sequential Framework for Urban Drone Delivery: Network Design, Vehicle Sizing, and Energy and Cost Assessment]]
- **作者**: Hong-Su Nam, Seokhwan Lee, Jungwoo Cho, Hak-Tae Lee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《A Sequential Framework for Urban Drone Delivery: Network Design, Vehicle Sizing, and Energy and Cost Assessment》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A sequential engineering framework is presented for urban drone delivery, linking hub location, route planning, mission-specific vehicle sizing, and energy and operating cost assessment. Aggregate origin-destination demand is assumed known a priori. For each hub configuration, the maximum required link distance is minimized, and feasible routes that return to their departure hubs are generated. Route frequencies are determined using mixed-integer linear programming to satisfy delivery demand. The resulting range requirement guides motor-propeller selection and battery sizing to minimize vehicle takeoff mass. Flight distances and frequencies, cruise performance, and vehicle dimensions are combined to estimate monthly energy consumption, fleet size, hub area, staffing, and operating cost. The framework is applied to district-level Seoul delivery data. Increasing the number of hubs from one to four reduces the required range from 30.6 to 21.9 km and vehicle takeoff mass from 8.12 to 6.12 kg. Despite a 21.5% increase in total flight distance, monthly flight energy consumption decreases by 13.1%, from 15.2 to 13.2 MWh. Battery replacement is the largest vehicle-related operating expense, while operating cost per delivery increases from USD 1.18 to USD 2.20 because of higher rent and labor costs at the hubs. Among the designs evaluated, range-matched vehicles achieve the lowest operating cost in the two- and four-hub networks; a longer-range vehicle is least costly in the three-hub network. Sensitivity analyses further examine the effects of delivery demand and operating assumptions. The results demonstrate that reductions in vehicle mass and energy consumption do not necessarily lead to lower system operating cost.

</details>

---

### [[20_Research/Papers/具身智能/Flexible_Piezoelectric_Tactile_Sensing_System_for_Intelligent_Object_Recognition|Flexible Piezoelectric Tactile Sensing System for Intelligent Object Recognition]]

![[assets/2611.07779_figure.png|800]]

- **arXiv**: [2611.07779](https://arxiv.org/abs/2611.07779)
- **PDF**: https://arxiv.org/pdf/2611.07779
- **详细分析**: [[20_Research/Papers/具身智能/Flexible_Piezoelectric_Tactile_Sensing_System_for_Intelligent_Object_Recognition|Flexible Piezoelectric Tactile Sensing System for Intelligent Object Recognition]]
- **作者**: Razan Khalifeh, Mohamad Yaacoub, Christian Gianoglio, Moustafa Saleh, Maurizio Valle, Yahya Abbass
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Flexible Piezoelectric Tactile Sensing System for Intelligent Object Recognition》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing provides information about object properties that can improve robotic grasping and manipulation. However, accurate object recognition during the early stages of grasping remains challenging, particularly under strict real-time constraints. This study presents a flexible, distributed piezoelectric tactile sensing system for early-stage object recognition. The system was experimentally evaluated using six everyday objects and three recognition approaches: feature-based classification using support vector machines (SVMs), raw-signal classification using 1D convolutional neural networks (1D-CNNs) and convolutional recurrent neural networks (C-RNNs), and spatiotemporal heatmap classification using a 2D-CNN. The effects of sensor count and temporal window size on recognition accuracy and real-time feasibility were systematically investigated. Increasing the number of sensing elements improved recognition performance across all approaches. The best-performing method, based on spatiotemporal heatmaps and a 2D-CNN, achieved F1-scores of 0.9796, 0.9846, and 0.9903 using 16, 24, and 32 sensors, respectively. The optimal configuration, comprising 32 sensors and a 100-ms temporal window (50 samples), was deployed on an embedded edge platform, achieving an end-to-end recognition latency of approximately 101 ms from contact onset and an energy consumption of 63.8 microjoules per inference. These results demonstrate the potential of distributed piezoelectric tactile sensing for accurate, energy-efficient, and real-time object recognition during robotic grasping.

</details>

---

### [[20_Research/Papers/机器人/Wedge-Jamming_Mechanism_for_String_Configuration|Wedge-Jamming Mechanism for String Configuration]]

![[assets/2611.07748_figure.png|800]]

- **arXiv**: [2611.07748](https://arxiv.org/abs/2611.07748)
- **PDF**: https://arxiv.org/pdf/2611.07748
- **详细分析**: [[20_Research/Papers/机器人/Wedge-Jamming_Mechanism_for_String_Configuration|Wedge-Jamming Mechanism for String Configuration]]
- **作者**: Taro Tako, Takanori Jin, Hiroshi Kaminaga, Taisuke Kobayashi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Wedge-Jamming Mechanism for String Configuration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL, JRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Variable stiffness mechanisms that achieve both flexibility and rigidity are important technologies for robotic systems. Recently, wire-based jamming mechanisms have attracted significant attention. In the wire-based jamming mechanisms, modules are chained by a wire, and the overall stiffness is controlled by changing the friction between the modules through wire tension. These mechanisms have been widely studied due to their simple structure and controllability. However, conventional wire-based jamming mechanisms mainly focus on holding torque along the joint axis, and the resistance against disturbances in other directions has not been sufficiently explored. In this study, we propose a wedge-jamming mechanism that introduces wedge-shaped contact surfaces into the modules of wire-based jamming structures. By changing the wedge angle, the holding characteristics against disturbances in different directions can be adjusted. Experimental results show that an out-wedge configuration improves resistance to vertical disturbances, while an in-wedge configuration enhances resistance to torsional disturbances. These results demonstrate that the anisotropic holding performance of wire-based jamming mechanisms depend on wedge geometry.

</details>

---

### [[20_Research/Papers/具身智能/AffectiveVLA_Safe_and_Intent-Aware_VLA_Control_for_Human-Humanoid_Social_Interaction|AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction]]

![[assets/2611.07712_figure.png|800]]

- **arXiv**: [2611.07712](https://arxiv.org/abs/2611.07712)
- **PDF**: https://arxiv.org/pdf/2611.07712
- **详细分析**: [[20_Research/Papers/具身智能/AffectiveVLA_Safe_and_Intent-Aware_VLA_Control_for_Human-Humanoid_Social_Interaction|AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction]]
- **作者**: Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Yara Mahmoud, Iana Zhura, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.7（加权：具身智能 3.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AffectiveVLA, UnifoLM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social touch interactions, such as handshakes, fist bumps, and hugs, require humanoid robots to infer human intent, generate contact-rich motions, and maintain safe physical contact. We present AffectiveVLA, an intent-gated Vision-Language-Action (VLA) pipeline deployed on a Unitree G1 humanoid with dexterous hands. A lightweight RGB-based model recognizes interaction intent from two onboard cameras and converts it into a language prompt for the VLA policy. Low-confidence predictions suppress motion execution, reducing unintended activations. During physical contact, interaction-specific compliance profiles adjust arm impedance, while an independent voice-triggered mechanism initiates a latched safe-stop procedure. Using VR teleoperation, we collected approximately 1,300 multimodal interaction episodes and fine-tuned four VLA models: GR00T, RLDX-1, Being-H0.5, and UnifoLM-VLA-0. On-robot evaluation identifies GR00T as the best-performing standalone model. Integrating intent recognition increases its macro-F1 score from 0.75 to 0.90, while the intent model achieves a p95 inference latency of 6.27 ms. These results demonstrate that explicit intent gating improves the reliability of VLA-based social interaction without compromising real-time operation.

</details>

---

### [[20_Research/Papers/具身智能/PhySA_Decoupling_Aesthetic_and_Physical_Rewards_for_Humanoid_Locomotion|PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion]]

![[assets/2611.07679_figure.png|800]]

- **arXiv**: [2611.07679](https://arxiv.org/abs/2611.07679)
- **PDF**: https://arxiv.org/pdf/2611.07679
- **详细分析**: [[20_Research/Papers/具身智能/PhySA_Decoupling_Aesthetic_and_Physical_Rewards_for_Humanoid_Locomotion|PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion]]
- **作者**: Yunwan Fu, Sicheng He, Jiageng Mao, Yue Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 2.7，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion policies trained without an explicit smoothness objective tend to produce jerky, high-energy gaits that stress actuators. Vision-language models (VLMs) offer an appealing reward source: given a rendered rollout, a VLM returns an aesthetic quality score on [0,10] without task-specific feature engineering. We find, however, that aesthetic preference and physical smoothness point in opposite directions: across four production VLMs, clips with higher joint acceleration receive higher aesthetic scores (mean Pearson r=+0.66). We study PhySA (Physical Smoothness and Aesthetics), which keeps the two on separate, independently removable reward channels: a sparse, asynchronous VLM score and a phase-triggered correction channel that adjusts physical penalty weights from simulator state. Ablations attribute the smoothness gain to the correction channel. On MuJoCo Humanoid-v5 at 2.6M steps, PhySA lowers joint acceleration by 26 to 32% relative to vanilla PPO, Text2Reward, and Eureka (three seeds), at the cost of shorter episodes. In a single extended run it lowers joint acceleration by 59.5% relative to Prompt2Policy, while a three-seed replication shows a smaller, non-significant reduction (7.2%). The gain does not transfer to IsaacLab or the Unitree G1, even after rescaling the smoothness term.

</details>

---

### [[20_Research/Papers/机器人/Real-Time_Event-Based_LED_Tracking_and_Pose_Estimation_with_PWM-Encoded_Markers|Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers]]

![[assets/2611.07630_figure.png|800]]

- **arXiv**: [2611.07630](https://arxiv.org/abs/2611.07630)
- **PDF**: https://arxiv.org/pdf/2611.07630
- **详细分析**: [[20_Research/Papers/机器人/Real-Time_Event-Based_LED_Tracking_and_Pose_Estimation_with_PWM-Encoded_Markers|Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers]]
- **作者**: Junkai Niu, Sheng Zhong, Delei Kong, Xin Wang, Kaizhen Sun, Yusen Zhang, Mingzhen Gan, Yi Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Real-Time Event-Based LED Tracking and Pose Estimation with PWM-Encoded Markers》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Event cameras are neuromorphic vision sensors with pixels that independently and asynchronously respond to brightness changes at microsecond resolution, supporting state estimation under rapid motion, motion blur, and high dynamic range (HDR) illumination. This also enables capture of high-frequency blinking patterns from light-emitting diodes (LEDs). Based on this, we propose a real-time event-based framework for LED tracking and six-degree-of-freedom (6-DoF) relative pose estimation using pulse-width modulation (PWM)-encoded LED markers. Multiple LEDs share a common blinking frequency and encode identities through distinct PWM duty cycles, reducing frequency-resource requirements and computational cost. Our dual-rate asynchronous tracking framework combines low-rate LED detection with high-rate raw-event updates, maintaining robust LED identity association and accurate pixel-level tracking under rapid motion. LED identities and positions establish reliable 2D-3D correspondences for real-time metric 6-DoF relative pose estimation. Extensive evaluations on a self-collected dataset demonstrate robustness under large motion flow and transient image-plane LED overlap. Furthermore, we develop a coordinated robotic platform comprising a quadrotor and a Mecanum-wheeled mobile robot, demonstrating the proposed framework's potential for closed-loop drone guidance through hovering and target-following experiments under time-varying HDR illumination, with onboard deployment on an NVIDIA Jetson Orin NX. The dataset and implementation will be released to facilitate further research.

</details>

---

### [[20_Research/Papers/机器人/Data-Driven_Configuration_of_Protective_Separation_Zones_in_Collaborative_Robot_Cells_from_Operator_Occupancy|Data-Driven Configuration of Protective Separation Zones in Collaborative Robot Cells from Operator Occupancy]]

![[assets/2611.07621_figure.png|800]]

- **arXiv**: [2611.07621](https://arxiv.org/abs/2611.07621)
- **PDF**: https://arxiv.org/pdf/2611.07621
- **详细分析**: [[20_Research/Papers/机器人/Data-Driven_Configuration_of_Protective_Separation_Zones_in_Collaborative_Robot_Cells_from_Operator_Occupancy|Data-Driven Configuration of Protective Separation Zones in Collaborative Robot Cells from Operator Occupancy]]
- **作者**: Aulon Bajrami, Theo Jacobs, Werner Kraus
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Data-Driven Configuration of Protective Separation Zones in Collaborative Robot Cells from Operator Occupancy》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MobileNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The protective separation zone of a collaborative robot cell is commonly dimensioned for a worst case that disregards where the operator is actually present during the task. This paper presents a camera-based, data-driven method that configures this zone from observed operator occupancy. Operator positions accumulated over several production shifts are aggregated into an occupancy heatmap, from which a protective field is derived that trades off the achievable robot velocity against the required safety distance, following the speed and separation monitoring principle of ISO/TS 15066. The resulting configuration is advisory, that is, reviewed within the risk assessment rather than applied autonomously to the robot controller. The method, which builds on a pose-based perception pipeline with activity recognition, was evaluated in two operational cells at two industrial partners, where the protective field could be reduced by approximately 17% and a productivity increase of 9% was measured. However, adoption proved to depend on more than the demonstrated gain alone.

</details>

---

### [[20_Research/Papers/机器人/Whole-Body_Elasto-Geometrical_Calibration_of_Wheeled_Humanoid_Robots_Using_a_Shared-Waist_Dual-Chain_Model|Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model]]

![[assets/2611.07560_figure.png|800]]

- **arXiv**: [2611.07560](https://arxiv.org/abs/2611.07560)
- **PDF**: https://arxiv.org/pdf/2611.07560
- **详细分析**: [[20_Research/Papers/机器人/Whole-Body_Elasto-Geometrical_Calibration_of_Wheeled_Humanoid_Robots_Using_a_Shared-Waist_Dual-Chain_Model|Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model]]
- **作者**: Pengxin Zha, Yi Lu, Haojun Ma, Jun Zhu, Minghao Qiu, Xiaoyan Wang, Wei Shan, Maoqing Yao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Whole-Body Elasto-Geometrical Calibration of Wheeled Humanoid Robots Using a Shared-Waist Dual-Chain Model》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wheeled humanoid robots carry both arms on one actuated waist, usually without torque sensors, so the accuracy of both end-effectors depends on a single waist model. After a first stage that estimates the tracker and target extrinsics, we identify the waist and both arms in one problem from the target positions on both flanges, measured by an optical tracker. The kinematic model is complete, with waist-base, parallel-axis, and branch parameters; arm compliances are driven by measured torques and waist compliances by gravity torques of the robot's mass model; and Gaussian priors with evidence-maximizing scales stabilize the estimate. Independent and sequential single-chain calibration are restrictions of this problem, and its waist information is the sum of the single-chain Schur complements. On two robots with different waists, each without and with a payload, calibration reduces the mean errors on held-out poses from 11.3-31.1 mm to 0.50-1.11 mm. For every training-set size from 20 poses to all, the method has 17-63% lower mean errors than adaptations of two published whole-body calibration methods, mainly through the waist compliance. Independent calibration yields two waist models; using either for both arms raises the other arm's error to up to 3.21 mm.

</details>

---

### [[20_Research/Papers/大模型/Semantics-to-Contact_A_Stagewise_Framework_for_Robust_Contact-Rich_Manipulation|Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation]]

![[assets/2611.07532_figure.png|800]]

- **arXiv**: [2611.07532](https://arxiv.org/abs/2611.07532)
- **PDF**: https://arxiv.org/pdf/2611.07532
- **详细分析**: [[20_Research/Papers/大模型/Semantics-to-Contact_A_Stagewise_Framework_for_Robust_Contact-Rich_Manipulation|Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation]]
- **作者**: Guanren Qiao, Ruixiang Ouyang, Sheng Xu, Yueci Deng, Yunxin Tai, Kui Jia, Guiliang Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 强化学习
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HIL-SERL, RWRL, Real-World, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires precise control under complex contact dynamics while remaining robust to diverse visual conditions. However, real-world reinforcement learning often overfits to the visual appearance of training scenes. We propose Semantics-to-Contact (S2C), a stagewise framework for visually robust contact-rich manipulation. The insight is to decompose the problem into two stages: semantic focusing and contact refinement. In the first stage, a vision-language model localizes task-relevant regions across visually diverse scenes, providing coarse spatial guidance and reducing the burden of exploration. In the second stage, a real-world human-in-the-loop residual reinforcement learning policy learns fine-grained contact behaviors within the localized region using force feedback. To further improve visual robustness, we introduce an object-centric visual augmentation strategy that randomizes background appearance while preserving the robot and task-relevant objects. Experiments on six contact-rich real-world manipulation tasks exhibit that S2C consistently improves success rates over strong baselines and maintains reliable performance under significant visual and positional variations. These results demonstrate that stagewise semantic focusing and contact refinement provide a practical path toward visually robust real-world contact-rich manipulation. Our demos can be seen in https://edem-ai.github.io/S2C/.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_RAG++_Retrieval-Augmented_Generation_From_What_Exists_to_What_Works_in_Embodied_Scenes|Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes]]

![[assets/2611.07517_figure.png|800]]

- **arXiv**: [2611.07517](https://arxiv.org/abs/2611.07517)
- **PDF**: https://arxiv.org/pdf/2611.07517
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_RAG++_Retrieval-Augmented_Generation_From_What_Exists_to_What_Works_in_Embodied_Scenes|Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes]]
- **作者**: Fan Yang, Tatsuya Kikuzuki, Jun Liang, Jun Liu, Wenkai Li, Ryosuke Kawamura, Ananya Hazarika, Prajit KrisshnaKumar, Shaunak Mehta, Yuushi Toyoda
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，大模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：E2W-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To serve a request in a human environment, a robot system must find an object that satisfies a functional requirement and a robot that can feasibly reach it. Scene graphs record which objects exist and where, but they often omit capabilities documented only in product manuals. Retrieval-augmented generation methods can read such manuals, yet they rarely reason jointly over object capabilities, physical instances, robot states, and dynamic connectivity. We introduce E2W-Bench, the Exists-to-Works Benchmark, which links dynamic hybrid scene graphs with real product manuals to evaluate capability-grounded robot--object assignment under availability, mobility, vertical-reach, and connector constraints. We also present Embodied RAG++, a spatially grounded retrieval framework that scopes retrieval to the manuals linked to candidate objects, caches extracted capabilities per product model, and resolves robot--object feasibility through deterministic spatial reasoning. On E2W-Bench, Embodied RAG++ reaches a pair accuracy of 0.90 with Qwen2.5-32B and 1.00 with Llama3.3-70B, compared with at most 0.30 and 0.55 for the baselines, while requiring the shortest preprocessing time among the retrieval-based methods and tying for the lowest total token count.

</details>

---

### [[20_Research/Papers/具身智能/LMGN_A_Unified_Policy_Learning_Model_for_Last-Mile_Grasp-Navigation|LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation]]

![[assets/2611.07515_figure.png|800]]

- **arXiv**: [2611.07515](https://arxiv.org/abs/2611.07515)
- **PDF**: https://arxiv.org/pdf/2611.07515
- **详细分析**: [[20_Research/Papers/具身智能/LMGN_A_Unified_Policy_Learning_Model_for_Last-Mile_Grasp-Navigation|LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation]]
- **作者**: Xuenmin Hu, Qingxue Qian, Wei Luo, Benyi Ma, Bo Tang, Long Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GSNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots equipped with manipulators have shown significant potential in the fields of daily life and industry in complex environments. However, existing methods mainly focus on global navigation or manipulation independently, while overlooking the last-mile navigation problem, where the robot must jointly determine the base placement, approach direction, and grasp execution to achieve reliable object grasping, and different manipulation stages require distinct control behaviors. To address these challenges, we propose Last-Mile Grasp-Navigation (LMGN), a unified policy learning model for Quadruped robot loco-manipulation. An Explicit Distance and Directional Reachability (ED-DR) representation is first introduced to explicitly represent the features of grasp-compatible base placement and approach direction. We then develop a semantically aligned Hierarchical Mixture-of-Experts (HMoE) policy that models stage-aware behaviors across the stages of base adjustment, pre-grasp alignment and grasp execution, and object lift. Finally, a new optimization method that jointly aligns navigation and manipulation, stage-dependent expert routing, and action-level consistency is proposed to optimize the HMoE policy. Extensive experiments on the Habitat and Isaac Gym simulators demonstrate that LMGN consistently outperforms state-of-the-art methods, denoting that integrating grasp-aware reachability with stage-aware policy learning significantly improves the success rates of last-mile navigation and target grasp for robots.

</details>

---

### [[20_Research/Papers/具身智能/Fast_and_Reliable_Open-Vocabulary_Object_Search_with_Absence_Detection_from_Robot_Memory|Fast and Reliable Open-Vocabulary Object Search with Absence Detection from Robot Memory]]

![[assets/2611.07493_figure.png|800]]

- **arXiv**: [2611.07493](https://arxiv.org/abs/2611.07493)
- **PDF**: https://arxiv.org/pdf/2611.07493
- **详细分析**: [[20_Research/Papers/具身智能/Fast_and_Reliable_Open-Vocabulary_Object_Search_with_Absence_Detection_from_Robot_Memory|Fast and Reliable Open-Vocabulary Object Search with Absence Detection from Robot Memory]]
- **作者**: Nicholas Paul, Devson Butani, Eric Martinson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Fast and Reliable Open-Vocabulary Object Search with Absence Detection from Robot Memory》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScanNet, YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile manipulators deployed in everyday human environments, such as homes for assistive care or flexible automation, often need to locate specific objects on demand from accumulated observations. Equally important, they must reliably determine when a target is absent before committing to navigation or interaction. Existing approaches demand either slow exhaustive re-processing or expensive 3D representations, and are evaluated on recall and accuracy rather than specificity, leaving their ability to abstain on missing targets unmeasured. We find existing systems that search using text or visual embedding almost never abstain on absent objects achieving at most 9\% specificity. To support accurate search at speed, we present a two-stage architecture that decouples fast candidate retrieval from verified selection, enabling both high recall and reliable absence detection from sequential RGB observations with pose. We evaluate eight retrieval-selection configurations plus an exhaustive search baseline across ScanNet apartment scenes, including significant numbers of absent objects. Adding a visual verification step to caption-based retrieval matches or exceeds exhaustive search reliability while requiring an order of magnitude fewer detector calls. We reproduce ScanNet scores on a physical robot operating entirely on-board with a single consumer GPU running in real time.

</details>

---

### [[20_Research/Papers/大模型/Kinematic_analysis_of_a_double-closed-loop_four-bar_chain-based_leg_for_a_multimodal_quadruped-pentarotor_robot|Kinematic analysis of a double-closed-loop four-bar chain-based leg for a multimodal quadruped-pentarotor robot]]

![[assets/2611.07470_figure.jpg|800]]

- **arXiv**: [2611.07470](https://arxiv.org/abs/2611.07470)
- **PDF**: https://arxiv.org/pdf/2611.07470
- **详细分析**: [[20_Research/Papers/大模型/Kinematic_analysis_of_a_double-closed-loop_four-bar_chain-based_leg_for_a_multimodal_quadruped-pentarotor_robot|Kinematic analysis of a double-closed-loop four-bar chain-based leg for a multimodal quadruped-pentarotor robot]]
- **作者**: Prashant Raturi, Santhakumar Mohan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.5（加权：具身智能 1.5，大模型 0.3，机器人 1.7）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Kinematic analysis of a double-closed-loop four-bar chain-based leg for a multimodal quadruped-pentarotor robot》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents the kinematic modeling and singularity analysis of a three-degree-of-freedom, double four-bar closed-loop quadruped leg mechanism. This leg is essential for transitioning between the two operational modes; therefore, it is examined in both joint and task spaces, leading to the development of its Jacobian matrix, which is vital for designing the gaits required for terrestrial mode and mid-air aerial reconfiguration (for aerial mode). Various gaits are devised for the system's motion in the MATLAB simulation, and their practical implementation on the single-leg test rig is demonstrated.

</details>

---

### [[20_Research/Papers/具身智能/Closed-Loop_Physics-Based_Manipulation_Evaluation_at_a_Commodity_Price_What_4.4_L4_GPU_hours_at_$3.50_Buys_You|Closed-Loop Physics-Based Manipulation Evaluation at a Commodity Price: What 4.4 L4 GPU hours at $3.50 Buys You]]

![[assets/2611.07441_figure.png|800]]

- **arXiv**: [2611.07441](https://arxiv.org/abs/2611.07441)
- **PDF**: https://arxiv.org/pdf/2611.07441
- **详细分析**: [[20_Research/Papers/具身智能/Closed-Loop_Physics-Based_Manipulation_Evaluation_at_a_Commodity_Price_What_4.4_L4_GPU_hours_at_$3.50_Buys_You|Closed-Loop Physics-Based Manipulation Evaluation at a Commodity Price: What 4.4 L4 GPU hours at $3.50 Buys You]]
- **作者**: Rohun Kshirsagar, Diana Rypkema
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Closed-Loop Physics-Based Manipulation Evaluation at a Commodity Price: What 4.4 L4 GPU hours at $3.50 Buys You》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Running evaluations of contact-rich robotic manipulation at statistical scale has largely been possible only at well-resourced labs, highlighting the need for affordable and efficient options for broader audiences. We present a reproducible evaluation harness wrapper based on a previous study at 200-rollout scale on serverless commodity GPUs, at a cost of approximately $3.50 USD and 38 minutes of wall-clock per replication (4.4 L4-GPU-hours across eight parallel shards). Using the harness, we report a partially controlled negative result on action chunking with sparse data: three independently trained chunked checkpoints produce zero genuine successes across 780 rollouts, while three single-step checkpoints range from 2.6% to 11.8% success rate. A per-step-replanning control partially isolates chunk prediction, rather than open-loop chunk execution as the mechanism, with the failure localized to the training formulation and multi-step prediction. This work further democratizes physics-based policy development and evaluation through our reusable harness.

</details>

---

### [[20_Research/Papers/机器人/An_Ordering_Optimization_for_Fruit-Vegetable_in_High-Density_Environment_based_on_Genetic_Algorithm|An Ordering Optimization for Fruit-Vegetable in High-Density Environment based on Genetic Algorithm]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2611.07293](https://arxiv.org/abs/2611.07293)
- **PDF**: https://arxiv.org/pdf/2611.07293
- **详细分析**: [[20_Research/Papers/机器人/An_Ordering_Optimization_for_Fruit-Vegetable_in_High-Density_Environment_based_on_Genetic_Algorithm|An Ordering Optimization for Fruit-Vegetable in High-Density Environment based on Genetic Algorithm]]
- **作者**: Jaehwi Seol, Jeonghyeon Pak, Hyoung Il Son
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《An Ordering Optimization for Fruit-Vegetable in High-Density Environment based on Genetic Algorithm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a robotic harvesting method that combines RGB-D fruit localization, GA-based harvest ordering, and waypoint-based robot motion in dense and unstructured crop environments. The global RGB-D camera provides 3D fruit positions for ordering, while the end-effector-mounted camera provides close-range observation during execution. The GA determines the harvesting sequence, and static or dynamic waypoints define the intermediate robot motion. The method was evaluated in a controlled laboratory testbed and in four-, five-, and six-fruit field conditions. GA solutions were compared with exhaustive enumeration, and both waypoint offsets were examined by parameter sensitivity analysis. Continuous execution reduced unnecessary Home-return motion, while the dynamic waypoint changed with the remaining fruit distribution without changing the GA sequence. In the field evaluation, the dynamic-waypoint continuous strategy produced 40 collision events and a 70.7% target-approach success rate, compared with 55 collision events and 65.3% for the static-waypoint continuous strategy.

</details>

---

### [[20_Research/Papers/机器人/CRISP_Constraint-Resolved_Interactions_between_Subsystems_for_Predictive_Whole-Body_Cooperation|CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2611.07268](https://arxiv.org/abs/2611.07268)
- **PDF**: https://arxiv.org/pdf/2611.07268
- **详细分析**: [[20_Research/Papers/机器人/CRISP_Constraint-Resolved_Interactions_between_Subsystems_for_Predictive_Whole-Body_Cooperation|CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation]]
- **作者**: Dario Valenzuela, Jeeseop Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a layered control framework that recasts high-dimensional system dynamics as a composition of dynamically interconnected subsystems, with dynamic dual-arm manipulation on the humanoid serving as a representative application. The humanoid is decomposed into a single rigid body (SRB) representing the torso and floating-base dynamic models representing the articulated arms and lower-body. The rigid connections between arm and torso and the closed kinematic chain formed between the end-effectors during cooperative manipulation are represented as holonomic constraints. The corresponding Lagrange multipliers parametrize the interaction wrenches transmitted at the shoulders and between the end-effectors. The high-level nonlinear model predictive control (NMPC) jointly optimizes the subsystem state trajectories, arm torques, ground reaction forces (GRFs), and interaction wrenches, enabling online wrench design and optimization while preserving the dynamic coupling among the independently modeled subsystems. The optimized arm torques are applied directly for cooperative dual-arm manipulation, whereas the prescribed GRFs are mapped to lower-body joint torque for whole-body coordination. We validate the proposed framework through numerical simulations and hardware experiments on a G1 humanoid robot. The results demonstrate optimal interaction wrenches consistent with simulated contact measurement, cooperative dual-arm trajectory tracking, and stable whole-body coordination while executing the NMPC in online manner.

</details>

---

### [[20_Research/Papers/强化学习/An_Empirical_Study_of_Reinforcement_Learning_for_Keypoint_Positioning_of_Deformable_Linear_Objects|An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2611.07261](https://arxiv.org/abs/2611.07261)
- **PDF**: https://arxiv.org/pdf/2611.07261
- **详细分析**: [[20_Research/Papers/强化学习/An_Empirical_Study_of_Reinforcement_Learning_for_Keypoint_Positioning_of_Deformable_Linear_Objects|An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects]]
- **作者**: Vinay Rodrigues, Sara Zeynalpour, Gokhan Solak, Sebastian Hjorth, Arash Ajoudani
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 1.2，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deformable linear object (DLO) manipulation is challenging because high-dimensional configurations, nonlinear contact dynamics, and diverse material and geometric properties produce a broad range of object responses that are both difficult to model and data-intensive to learn. This work studies reinforcement learning for planar manipulation of a one-end-grasped DLO, focusing on training efficiency, observation design, robustness, and zero-shot sim-to-real transfer. We compare three Proximal Policy Optimization training stacks and find that the GPU-parallel MuJoCo Playground stack enables faster convergence and more consistent performance than CPU-based alternatives under the same wall-clock budget. Relative keypoint observations and an asymmetric actor-critic formulation further improve learning efficiency. Policies trained with observation noise, delay, domain randomization, and disturbances achieve simulation success rates of 96.4% for single-point tracking, 98.0% for disturbance recovery, and 88.8% for two-point tracking. Using markerless RGB-D keypoint estimation, the policies transfer without real-world fine-tuning, succeeding in 9/10, 10/10, and 8/10 physical trials, respectively.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Geometric_Optimization_and_Control_of_Rigid_Differential-Drive_Formations_from_Relative-Position_Measurements|Distributed Geometric Optimization and Control of Rigid Differential-Drive Formations from Relative-Position Measurements]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2611.07163](https://arxiv.org/abs/2611.07163)
- **PDF**: https://arxiv.org/pdf/2611.07163
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Geometric_Optimization_and_Control_of_Rigid_Differential-Drive_Formations_from_Relative-Position_Measurements|Distributed Geometric Optimization and Control of Rigid Differential-Drive Formations from Relative-Position Measurements]]
- **作者**: Thanacha Choopojcharoen, Erman Selim, Ramisha Anjum, Baris Fidan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Distributed Geometric Optimization and Control of Rigid Differential-Drive Formations from Relative-Position Measurements》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distance based formation control fixes the shape of a robot team but leaves its position and orientation unconstrained. We regulate all three for differential drive robots that have only one absolute position anchor, absolute headings, body frame relative position measurements, and communication with their neighbors. We derive a two layer estimation control scheme directly from optimization. The first half of the result is a set of graph-proximal estimators that reconstruct the centroid, the anchor vector, and the centered coordinates. Exact proximal updates reach consensus in finitely many steps, and a finite number of primal dual iterations leaves a bounded reconstruction error. The controller combines proximal centroid and orientation steps with distance gradient shape regulation, and a finite rotation removes the orientation drift caused by the shape step. A discrete Lyapunov analysis gives local exponential convergence once the estimators have converged. We validate the method in ROS 2 Gazebo and in experiments with five physical robots.

</details>

---
