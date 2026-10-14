# cs.RO | Robotics | 2026-10-12

#arxiv #ComputerScience

**论文数**: 42

### [[20_Research/Papers/具身智能/Noise_Space_Learning_for_VLA_Adaptation|Noise Space Learning for VLA Adaptation]]

![[assets/2610.13943_figure.png|800]]

- **arXiv**: [2610.13943](https://arxiv.org/abs/2610.13943)
- **PDF**: https://arxiv.org/pdf/2610.13943
- **详细分析**: [[20_Research/Papers/具身智能/Noise_Space_Learning_for_VLA_Adaptation|Noise Space Learning for VLA Adaptation]]
- **作者**: Junjie Lu, Chuheng Zhang, Yucen Wang, Yuhua Jiang, Xinyao Qin, Min Xu, Li Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Noise Space Learning for VLA Adaptation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language-action (VLA) models encode broad manipulation priors, yet adapting them to specific tasks requires balancing limited robot interaction, computational resources, and safety constraints. Noise space learning (NSL) adapts flow-matching-based VLAs by learning a context-conditioned distribution over noise while keeping the pretrained VLA fixed. Building on prior noise-steering methods, we formulate NSL as an interface for VLA adaptation that accommodates different learning algorithms and instantiate it with PPO, SAC, and AWR. Theoretically, we provide an information-theoretic analysis of how NSL enables efficient adaptation. Empirically, we study these NSL algorithms on LIBERO, RoboTwin, and four real-robot manipulation tasks under interaction, computation, and execution constraints. Across these settings, we develop a suite of effective NSL variants and derive practical recommendations for choosing among them under different resource and deployment regimes.

</details>

---

### [[20_Research/Papers/具身智能/BT-Agent_Deploying_Onboard_Robot_Agents_with_Behavior_Trees_and_Multi-Fidelity_Evaluation|BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation]]

![[assets/2610.13862_figure.png|800]]

- **arXiv**: [2610.13862](https://arxiv.org/abs/2610.13862)
- **PDF**: https://arxiv.org/pdf/2610.13862
- **详细分析**: [[20_Research/Papers/具身智能/BT-Agent_Deploying_Onboard_Robot_Agents_with_Behavior_Trees_and_Multi-Fidelity_Evaluation|BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation]]
- **作者**: Fabio Hübel, Adam Lilja, Yue Yin, Siming He, Claire Tomlin, Shankar Sastry, Jonas Frey, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.6，大模型 0.9，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying language-model agents onboard mobile robots requires task reasoning and responsive execution within limited compute and memory. We propose BT-Agent, an onboard architecture combining LLM-driven task decisions with predefined behavior-tree (BT) skills. These skills enforce execution conditions and return structured failure feedback. We demonstrate fully onboard operation with a 9B model on a quadruped across five task categories. Intervention tests show that local checks stop ongoing navigation without waiting for another model decision, while the agent remains active to retry or report constraints. To compare agent designs efficiently, we introduce a 161-task multi-fidelity benchmark, evaluated in text on all tasks and in Habitat on 39. Text supports 10.9$\times$ higher evaluation throughput, while simulation reveals how perception and motion failures change task outcomes. BT-Agent's largest success gains over the strongest Act/ReAct baseline occur at 4B and 9B: approximately 10 and 5 percentage points. Ablations identify structured tool calls and informative failure feedback as the most useful components.

</details>

---

### [[20_Research/Papers/具身智能/HorizonNav_Geometry-Guided_Video_Diffusion_for_Anticipatory_3D_Robot_Navigation|HorizonNav: Geometry-Guided Video Diffusion for Anticipatory 3D Robot Navigation]]

![[assets/2610.13849_figure.png|800]]

- **arXiv**: [2610.13849](https://arxiv.org/abs/2610.13849)
- **PDF**: https://arxiv.org/pdf/2610.13849
- **详细分析**: [[20_Research/Papers/具身智能/HorizonNav_Geometry-Guided_Video_Diffusion_for_Anticipatory_3D_Robot_Navigation|HorizonNav: Geometry-Guided Video Diffusion for Anticipatory 3D Robot Navigation]]
- **作者**: Hajira Amjad, Valerii Serpiva, Viacheslav Liubimov, Didar Seyidov, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.5，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《HorizonNav: Geometry-Guided Video Diffusion for Anticipatory 3D Robot Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, WonderWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present HorizonNav, a video diffusion-based framework for anticipatory robot navigation that transforms a single RGB image and a text prompt into a geometrically aligned representation of plausible surrounding 3D space. Given the initial observation and a textual description of the reconstruction objective, a vision-language model, guided by designed instructions, interprets the scene and constructs structured prompts for a video diffusion model. The resulting video sequence provides plausible future observations of the environment, which are subsequently processed using monocular ORB-SLAM3 for camera pose estimation and Video Depth Anything for dense depth prediction. Our central contribution is a geometry-guided depth alignment stage that combines the estimated camera poses with triangulated visual landmarks to constrain dense depth predictions across multiple views. This alignment improves the geometric consistency of the reconstructed 3D environment, addressing inconsistencies that temporal coherence of the generated video alone cannot resolve. The experimental evaluation of navigation in imagined 3D environment shows that across a 19-scene horizon study, planning-feasible scenes increase from 13/19 at P20 to 15/19 at P81, while successful RRT trials increase from 62/90 to 75/90. In a separate corridor study, 6 of 25 evaluable generated-camera trajectories violate the reconstructed collision constraints; RRT planner recovers feasible alternatives in 5 of those 6 cases. A larger archive contains 58 usable reconstructions from 67 attempted cases, of which 36 support a downstream plan and 22 do not, exposing reconstruction and free-space failure modes rather than hiding them without lidar. Across 15 corridor reconstructions, the mean reconstruction error is approximately 0.30 m at matched structural landmarks.

</details>

---

### [[20_Research/Papers/强化学习/MARGoS_A_Configuration-Driven_Platform_for_Reproducible_MARL_Experiments_in_ARGoS|MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS]]

![[assets/2610.13772_first_page.png|800]]

- **arXiv**: [2610.13772](https://arxiv.org/abs/2610.13772)
- **PDF**: https://arxiv.org/pdf/2610.13772
- **详细分析**: [[20_Research/Papers/强化学习/MARGoS_A_Configuration-Driven_Platform_for_Reproducible_MARL_Experiments_in_ARGoS|MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS]]
- **作者**: Tom Philipp Backert, Mohammad D. Soorati, Javad Ghofrani
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ARGoS-to-MARL, AirSim, IsaacSim, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reinforcement learning (MARL) has become a prominent research direction, particularly within collective robotics, where the ARGoS simulator is widely used to study emergent swarm behavior. Yet despite this growth, systematic support for reuse and reproducibility in MARL-based swarm robotics remains limited and insufficiently standardized: a single experiment is assembled from manually aligned simulator files, training scripts, configuration values, paths, seeds, and environment details, so reuse and reproduction stay fragile even within one research group. To address this gap, we introduce MARGoS, a lightweight, configuration-driven platform developed in this project that elevates these experiment-defining inputs to first-class, platform-managed artifacts. MARGoS enables reproducible experimentation through configuration hashing, end-to-end seed propagation, frozen (immutable) configurations, structured logging, environment fingerprinting, and exportable experiment bundles that facilitate sharing, replay, and verification of results across machines and over time. A five-dimension evaluation (architecture, efficiency, reproducibility, usability, and collaboration) supports our claim that managing experiment variation as a platform responsibility makes ARGoS+MARL experiments easier to reuse, reproduce, and hand off. Our code is available at https://github.com/tombackert/margos.

</details>

---

### [[20_Research/Papers/具身智能/AutoBio+_Benchmarking_Dexterous_Manipulation_with_Dynamic_Experimental_Phenomena_in_Realistic_Laboratories|AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories]]

![[assets/2610.13643_figure.png|800]]

- **arXiv**: [2610.13643](https://arxiv.org/abs/2610.13643)
- **PDF**: https://arxiv.org/pdf/2610.13643
- **详细分析**: [[20_Research/Papers/具身智能/AutoBio+_Benchmarking_Dexterous_Manipulation_with_Dynamic_Experimental_Phenomena_in_Realistic_Laboratories|AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories]]
- **作者**: Xuanye Wu, Yue Shi, Yongcan Yang, Yiqun Wang, Zhaoqi Wan, Dayu Xia, Jiezhang Cao, Xiangfei Li, Yao Mu, Guangtao Zhai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating biological laboratories requires robots to perform dexterous tool interactions under realistic visual conditions while handling dynamic experimental phenomena, presenting significant challenges for robotic manipulation. To enable systematic evaluation under these conditions, we introduce AutoBio+, a simulation benchmark and framework for dexterous manipulation in realistic biological laboratory environments. AutoBio+ comprises 14 tasks across 4 robot embodiments, spanning functional tool use, precision manipulation, language-conditioned visual grounding, and instrument operation. We introduce controllable dynamic experimental phenomena, including flames, vapor, and bubbles, to capture the evolving visual conditions of laboratory procedures. To further enhance environmental realism, we develop a hybrid rendering pipeline that integrates interactive simulated foreground objects with Gaussian-splatting backgrounds reconstructed from 6 real laboratory scenes. For efficient large-scale data generation and evaluation, we further build a parallel simulation framework on top of mjlab, proposing Parallel Finite-State Machine (PFSM) and integrating batched rendering with decoupled trajectory replay for demonstration generation and model-independent closed-loop policy evaluation. Our evaluation reveals substantial variation in policy performance across tasks, exposing distinct strengths and weaknesses of current manipulation policies. Real-world experiments further demonstrate a reduced sim-to-real gap, supporting the validity of AutoBio+ for realistic manipulation evaluation. Supplementary materials are available at https://autobio-plus.github.io/AutoBioPlus.

</details>

---

### [[20_Research/Papers/具身智能/ATHLETE_Learning_Reactive_Humanoid_Tennis_via_Trajectory-Guided_Motion_Matching|ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching]]

![[assets/2610.13572_figure.png|800]]

- **arXiv**: [2610.13572](https://arxiv.org/abs/2610.13572)
- **PDF**: https://arxiv.org/pdf/2610.13572
- **详细分析**: [[20_Research/Papers/具身智能/ATHLETE_Learning_Reactive_Humanoid_Tennis_via_Trajectory-Guided_Motion_Matching|ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching]]
- **作者**: Zhihao Tian, Zifan Wang, Enzheng Zhu, Xun Yang, Jialong Qin, Mengbo Wang, Junwei Liang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid tennis requires reactive whole-body coordination under rapidly changing ball dynamics, yet collecting task-specific motion-capture demonstrations that cover diverse approach states, contact locations, and timing conditions is costly. Inspired by how humans acquire new skills by combining reusable motor experience with task-specific demonstrations, we present ATHLETE, a framework for learning reactive humanoid tennis from generic locomotion data and ordinary tennis videos. ATHLETE combines LAFAN1 locomotion with video-derived striking motions and uses Trajectory-Guided Motion Matching (TGMM) to construct diverse task-conditioned whole-body references. These references are transformed into a reactive policy through physics-based teacher--student learning with online DAgger distillation, followed by PPO fine-tuning for the tennis task. The resulting policy responds directly to robot and ball observations without requiring reference-motion inputs at deployment. On a real humanoid robot, ATHLETE achieves forehand and backhand hit rates of $90.00\%$ and $86.67\%$, respectively, and enables multi-shot rallies with human players. These results demonstrate that ATHLETE can learn dynamic humanoid tennis skills from reusable locomotion data and video demonstrations. Result videos and code can be found at https://anonymous.4open.science/w/ATHLETE2027/.

</details>

---

### [[20_Research/Papers/具身智能/Reflect-VLA_Internalizing_Reflective_Guidance_via_Dual-Path_On-Policy_Self-Distillation_for_Autonomous_Driving|Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving]]

![[assets/2610.13453_figure.jpg|800]]

- **arXiv**: [2610.13453](https://arxiv.org/abs/2610.13453)
- **PDF**: https://arxiv.org/pdf/2610.13453
- **详细分析**: [[20_Research/Papers/具身智能/Reflect-VLA_Internalizing_Reflective_Guidance_via_Dual-Path_On-Policy_Self-Distillation_for_Autonomous_Driving|Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving]]
- **作者**: Yuechen Luo, He Chong, Fang Li, Shaoqing Xu, Hexin Zhang, Ruiqi Zhang, Ziying Song, Lei Yang, Zhi-Xin Yang, Fuxi Wen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.8，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Reflect-VLA: Internalizing Reflective Guidance via Dual-Path On-Policy Self-Distillation for Autonomous Driving》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ELF-VLA, LingoQA, NuScenes-QA, Reflect-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) substantially improves planning performance in autonomous-driving Vision-Language-Action (VLA) models. However, existing RL methods rely on scalar trajectory rewards that measure overall quality but fail to identify specific planning errors or provide actionable correction signals. In long-tail scenarios, errors in scene understanding, behavior selection, and trajectory execution are compressed into a single score. We observe that Reflective Guidance turns trajectory evaluation into explicit diagnoses and corrective instructions, substantially improving planning accuracy. Yet such guidance requires an initial prediction and its evaluation results, making it unavailable for direct single-pass inference. We propose Reflect-VLA, which treats Reflective Guidance as training-time privileged information and internalizes its planning benefits through Dual-Path On-Policy Self-Distillation (Dual-OPSD). Unlike scalar-reward optimization, Dual-OPSD uses the driving score only to route student-generated trajectories. It distills dense token-level corrective distributions from the teacher for risky trajectories while applying self-imitation to preserve reliable ones. To provide reliable corrective distributions on student rollouts, the teacher is progressively constructed through Driving-Knowledge Pretraining, Planning-and-Refinement SFT, and Self-Refinement Rejection Sampling. At inference time, Reflect-VLA generates trajectories in a single pass without explicit guidance or iterative refinement. Experiments on NAVSIM v1/v2 and Bench2Drive demonstrate competitive planning performance while reducing training time by over 90% compared with RL.

</details>

---

### [[20_Research/Papers/机器人/Robot-WATCHDOG_failure_detection_through_object-centric_graph_representation|Robot-WATCHDOG : failure detection through object-centric graph representation]]

![[assets/2610.13403_figure.png|800]]

- **arXiv**: [2610.13403](https://arxiv.org/abs/2610.13403)
- **PDF**: https://arxiv.org/pdf/2610.13403
- **详细分析**: [[20_Research/Papers/机器人/Robot-WATCHDOG_failure_detection_through_object-centric_graph_representation|Robot-WATCHDOG : failure detection through object-centric graph representation]]
- **作者**: Quentin Rolland, Fabrice Mayran de Chamisso, Jean-Baptiste Mouret
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Robot-WATCHDOG : failure detection through object-centric graph representation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable real-time failure detection is critical for deploying learned robotic policies, yet defining failures explicitly is infeasible in open-world settings. This motivates failure detection from nominal demonstrations alone. Existing methods, however, struggle to balance robustness to benign variations with the ability to capture semantic and interaction-level errors. We introduce Robot-WATCHDOG, a self-supervised framework that models manipulation scenes as object-centric spatio-temporal graphs. Building on this representation, we investigate two complementary failure scores: Trajectory Projection and Correlation (TPC), a non-parametric measure of geometric deviation and relational consistency, and GnnT, a Graph Attention Network with a Transformer that predicts future object states. We evaluate both on a public benchmark and on a new dataset of semantically complex manipulation tasks, across six tasks and ten random seeds. Both scores outperform image-based failure detectors, particularly on semantic and interaction-level failures. TPC provides the strongest performance in AUPR and MCC on both dataset averages, with low variance across seeds. Qualitative results are made available at https://cea-list.github.io/Robot-WATCHDOG/.

</details>

---

### [[20_Research/Papers/强化学习/EndoRSI_Physical-Evidence-Driven_Recursive_Improvement_of_Endoscopic_Robot_Policies|EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies]]

![[assets/2610.13376_figure.png|800]]

- **arXiv**: [2610.13376](https://arxiv.org/abs/2610.13376)
- **PDF**: https://arxiv.org/pdf/2610.13376
- **详细分析**: [[20_Research/Papers/强化学习/EndoRSI_Physical-Evidence-Driven_Recursive_Improvement_of_Endoscopic_Robot_Policies|EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies]]
- **作者**: Chi Kit Ng, Yidong Zhang, Tianchun Wu, Siu Hing Lui, Hanlin Zhao, Huxin Gao, Hongliang Ren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial intelligence is beginning to automate scientific discovery, yet physical robot-policy research still relies on scientists and engineers to interpret experimental failures and decide how controllers should be revised. We present EndoRSI (Endoscopic Recursive Self-Improvement), a human-governed, self-improving robotic research system in which the embedded EndoForge coding agent iteratively develops and refines endoscopic robot policies using evidence from physical experiments. Physical execution remains isolated within a safety-constrained runtime under human authorisation. In motorised endoscopy, validation evidence first caused the agent to reject an initial action representation, while subsequent physical experiments falsified an offline-supported insertion strategy by revealing hazardous closed-loop behaviour absent from the source data. Failed physical rollouts were then incorporated into policy revision; insertion success subsequently increased from 2/21 in the first generation to 17/21 in the fourth. The frozen final policy retained competence across visual and hardware shifts and was the best performing autonomous policy across six independent ex-vivo porcine specimens. These results show that physical robot interaction can serve as experimental evidence for agent-driven robot policy research.

</details>

---

### [[20_Research/Papers/机器人/PartiGen_Part-Aware_Representations_for_Language-Conditioned_Humanoid_Motion_Generation|PartiGen: Part-Aware Representations for Language-Conditioned Humanoid Motion Generation]]

![[assets/2610.13373_figure.png|800]]

- **arXiv**: [2610.13373](https://arxiv.org/abs/2610.13373)
- **PDF**: https://arxiv.org/pdf/2610.13373
- **详细分析**: [[20_Research/Papers/机器人/PartiGen_Part-Aware_Representations_for_Language-Conditioned_Humanoid_Motion_Generation|PartiGen: Part-Aware Representations for Language-Conditioned Humanoid Motion Generation]]
- **作者**: Chuxuan Huang, Zhanxiang Cao, Tianyue Zhan, Haoyang Li, Yang Zhang, Liyun Yan, Chenlin Ming, Keqi Zhu, Yizhi Chen, Shengcheng Fu, Zihao Zhou, Xinyi Peng...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《PartiGen: Part-Aware Representations for Language-Conditioned Humanoid Motion Generation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Translating language into humanoid motion requires coordinating body parts, determining motion duration, and producing references suitable for robot execution. We introduce PartiGen, a part-aware latent diffusion framework that incorporates anatomical structure into a shared whole-body motion representation. Part-specific attention processes anatomically masked frame features, and its outputs are fused to combine local limb information with whole-body context. Conditioned on text and motion history, the model generates motion primitives autoregressively. Forward-kinematics supervision encourages kinematic consistency, while a learned end-of-sequence predictor selects a frame-level endpoint after generation. On HumanML3D retargeted to the Unitree G1, PartiGen achieves a segment-level FID of 3.165, a 16.8% reduction over TextOp, and improves R@1 by 1.4 percentage points. In the duration study with 16-frame primitives, endpoint prediction reduces mean absolute duration error from 12.471 to 3.080 frames compared with a fixed-length cutoff. We further evaluate robot execution using a pretrained, frozen GRIT tracker: 409 of 500 generated references (81.8%) pass the posture-based stability screen in MuJoCo. Following simulation screening and manual selection, 26 of 27 attempted motions are judged successful on the real G1.

</details>

---

### [[20_Research/Papers/强化学习/Evo-RL_Iterative_Robot_Reinforcement_Learning_from_Selective_Experience|Evo-RL: Iterative Robot Reinforcement Learning from Selective Experience]]

![[assets/2610.13345_figure.png|800]]

- **arXiv**: [2610.13345](https://arxiv.org/abs/2610.13345)
- **PDF**: https://arxiv.org/pdf/2610.13345
- **详细分析**: [[20_Research/Papers/强化学习/Evo-RL_Iterative_Robot_Reinforcement_Learning_from_Selective_Experience|Evo-RL: Iterative Robot Reinforcement Learning from Selective Experience]]
- **作者**: Kai Ye, Yifan Jin, Qianhang Luo, Hongru Zhang, Jiedong Zhang, Shuyuan Hu, Song-Yuan Wu, Jihai Xu, Jie Zhao, Bo Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Evo-RL: Iterative Robot Reinforcement Learning from Selective Experience》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Evo-RL, OpenVLA, RW-RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing real-world reinforcement learning methods improve robot policies by combining human corrections with autonomous rollouts. However, accumulated experience varies in its value for policy improvement, and even successful trajectories can contain inefficient or redundant behavior, motivating more selective experience reuse. To this end, we propose Evo-RL, an iterative reinforcement learning method that combines human interventions with advantage-guided experience selection. Evo-RL uses human corrections and experience with positive estimated advantages from successful trajectories to iteratively refine the policy. To support learning from these different experience sources, we introduce RW-RL-Dataset, which spans over 1,000 hours across four robot embodiments. On a real-world high-precision manipulation task, Evo-RL improves attempt success rate over RECAP by 30.46\%. Our code, model checkpoints, and dataset are publicly available.

</details>

---

### [[20_Research/Papers/机器人/PATACON_GPU-Parallel_Tangent-Bundle_RRT-Connect_for_Constrained_Motion_Planning|PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning]]

![[assets/2610.13195_figure.png|800]]

- **arXiv**: [2610.13195](https://arxiv.org/abs/2610.13195)
- **PDF**: https://arxiv.org/pdf/2610.13195
- **详细分析**: [[20_Research/Papers/机器人/PATACON_GPU-Parallel_Tangent-Bundle_RRT-Connect_for_Constrained_Motion_Planning|PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning]]
- **作者**: Gahyun Oh, Junho An, Suhyun Jeon, Suhan Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Agent

#### 研究背景与动机

《PATACON: GPU-Parallel Tangent-Bundle RRT-Connect for Constrained Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fast whole-body motion planning enables continuous replanning for humanoid robots in dynamic environments while satisfying collision avoidance and kinematic constraints. However, constrained motion planning incurs substantial computational cost due to repeated constraint projection in addition to collision checking and nearest-neighbor search. Recently, GPU-based massively parallel planners have been proposed to reduce computational cost. Nevertheless, these planners still steer in the ambient configuration space, so projecting candidates that deviate from the manifold remains a significant source of overhead, particularly in highly constrained, high-dimensional problems. In this work, we introduce PATACON, a GPU-parallel bidirectional planner that explores tangent space to exploit the local manifold geometry induced by known constraint functions. Experiments on dual-arm closed-chain and humanoid whole-body constrained planning tasks show that PATACON outperforms the prior work as configuration-space dimension and constraint codimension grow, achieving up to an 11.25 times speedup. These results suggest that GPU-parallel tangent-space exploration brings constrained whole-body motion planning closer to real-time performance.

</details>

---

### [[20_Research/Papers/具身智能/Grounded-Dreamer_Robot_Learning_from_World_Model_Synthetic_Data_with_Physical_Grounding|Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding]]

![[assets/2610.13164_figure.png|800]]

- **arXiv**: [2610.13164](https://arxiv.org/abs/2610.13164)
- **PDF**: https://arxiv.org/pdf/2610.13164
- **详细分析**: [[20_Research/Papers/具身智能/Grounded-Dreamer_Robot_Learning_from_World_Model_Synthetic_Data_with_Physical_Grounding|Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding]]
- **作者**: Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen, Jiaqi Liang, Yang Chen, Lei Wei, Chen Xie, Ruihai Wu
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 3.7（加权：具身智能 0.6，世界模型 2，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GenSim, RLBench, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling robot manipulation policies requires large amounts of diverse, action-labeled data, yet collecting such data in the real world remains expensive and difficult to scale. Existing methods either depend on human teleoperation, rely on simulation with limited visual realism, or use human videos that lack embodiment-specific annotations. In this paper, we introduce Grounded-Dreamer, a framework for synthesizing physically grounded robot manipulation data with video world models while avoiding human teleoperation demonstrations. Grounded-Dreamer combines the visual realism of generative video models with simulator physics engines. Starting from a small set of real images depicting robot task initial states, our method automatically reconstructs task-relevant objects and camera geometry, aligns them in simulation, and collects physically valid trajectories. These trajectories are used to post-train both a video world model and an inverse dynamics model, enabling the generation of visually realistic robot manipulation videos and corresponding robot actions from real images. To filter physically implausible rollouts, Grounded-Dreamer replays generated trajectories in the reconstructed simulation and retains only those that successfully complete the tasks. The real-world robot policies are trained solely on the grounded synthetic trajectories without any human demonstrations. Empirical results in real-world tasks demonstrate that Grounded-Dreamer can synthesize physically grounded data and substantially facilitate policy learning without requiring human teleoperation effort.

</details>

---

### [[20_Research/Papers/强化学习/Human2Dex_Dexterous_Robot_Learning_from_Wrist-Centric_Human_Demonstrations|Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations]]

![[assets/2610.13119_figure.png|800]]

- **arXiv**: [2610.13119](https://arxiv.org/abs/2610.13119)
- **PDF**: https://arxiv.org/pdf/2610.13119
- **详细分析**: [[20_Research/Papers/强化学习/Human2Dex_Dexterous_Robot_Learning_from_Wrist-Centric_Human_Demonstrations|Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations]]
- **作者**: Jiachen Zhang, Yuanyuan Li, Shaqi Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Human2Dex: Dexterous Robot Learning from Wrist-Centric Human Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting dexterous manipulation demonstrations for each robot hand requires repeated task-specific data acquisition. We ask whether one shared corpus of natural human demonstrations can instead serve as a reusable data interface for different dexterous hands, without collecting task demonstrations on each target robot. We present Human2Dex, a wrist-centric human demonstration interface that separates shared human observation and motion semantics from embodiment-specific execution. It aligns observations through local hand-appearance adaptation and a shared 21-point hand representation with consistent structural semantics across human and robot observations. It constructs executable supervision by retargeting fused human hand motion to each target hand, and introduces the Grasp-Pocket Interaction Representation (GPIR) to express tracked objects relative to a hand-centered Functional Grasp Pocket. The corpus is converted into separate training sets for Linker O6 and Wuji, while action labels, normalization, training, and diffusion-policy checkpoints remain hand-specific. Across six real-world tasks, Human2Dex achieves 109/120 (90.8%) successes on Linker O6 and 97/120 (80.8%) on Wuji. Across both hands, Human-Raw achieves 63/240 (26.3%) successes, whereas the complete Human2Dex configuration achieves 206/240 (85.8%). These results support the use of wrist-centric human demonstrations as a reusable interface across calibrated dexterous hands while retaining embodiment-specific policy learning. The project website is publicly available at https://human2dex.pages.dev/.

</details>

---

### [[20_Research/Papers/具身智能/Forward_Dynamics_Models|Forward Dynamics Models]]

![[assets/2610.13117_figure.png|800]]

- **arXiv**: [2610.13117](https://arxiv.org/abs/2610.13117)
- **PDF**: https://arxiv.org/pdf/2610.13117
- **详细分析**: [[20_Research/Papers/具身智能/Forward_Dynamics_Models|Forward Dynamics Models]]
- **作者**: Zipei Ma, Junzhe Jiang, Jiahui Zhang, Juntong Zhang, Chun Gu, Bozhou Zhang, Jiankang Deng, Xiatian Zhu, Li Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Forward Dynamics Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models and world action models (WAMs) have advanced robotic policy learning by building on pretrained vision-language models (VLMs) and video generative models (VGMs), respectively. Yet VLAs learn without explicit supervision from future world states, while WAMs that condition actions on predicted futures incur extra inference cost and let visual prediction errors propagate into actions. We present Forward Dynamics Models (FDM), a family of robotic action models that couples action and future world-state prediction through an action-to-future paradigm. Future prediction is conditioned on action features, never the reverse: end-to-end training lets ground-truth future states supervise the policy through these features, while prediction errors cannot propagate into actions. At inference, FDM skips future generation entirely, avoiding its computational cost. The paradigm is backbone-agnostic, and we instantiate it with both VLM and VGM backbones. Experiments in simulation and on real robots demonstrate the effectiveness of FDM across both backbone families, achieving a state-of-the-art 99.4% average success rate on LIBERO and absolute gains of up to 13% over VLA and WAM methods on real-world tasks.

</details>

---

### [[20_Research/Papers/强化学习/ReAT_Residual_Action_Tokenization_for_Autoregressive_Robot_Policies|ReAT: Residual Action Tokenization for Autoregressive Robot Policies]]

![[assets/2610.13093_figure.png|800]]

- **arXiv**: [2610.13093](https://arxiv.org/abs/2610.13093)
- **PDF**: https://arxiv.org/pdf/2610.13093
- **详细分析**: [[20_Research/Papers/强化学习/ReAT_Residual_Action_Tokenization_for_Autoregressive_Robot_Policies|ReAT: Residual Action Tokenization for Autoregressive Robot Policies]]
- **作者**: Dijia Zhan, Zhuo Li, Xuemiao Xu, Sun Zheng, Jinyi Li, Wenjun Wang, Jie Tang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ReAT: Residual Action Tokenization for Autoregressive Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MetaWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive robot policies rely on action tokenizers to convert continuous action chunks into compact sequences of discrete prediction targets. Existing tokenizers can reconstruct action chunks from discrete codes, but often leave implicit what each individual token contributes to the reconstructed action. We introduce Residual Action Tokenization (ReAT), which gives each token an explicit role in refining the current action reconstruction. It uses the decoded reconstruction as feedback to construct the next token from the remaining action error. This closes the loop between encoding and decoding, making each new token responsive to the errors left by the actual decoded prefix. Across 19 manipulation tasks spanning three simulation benchmarks and real-world settings, 8-token ReAT policies outperform the evaluated baselines in task success; on LIBERO, even 4-token ReAT surpasses the evaluated 8-token action-tokenization baselines at half the token budget. These results suggest a path toward action tokenization that supports self-corrective policy learning, helping autoregressive policies learn to progressively refine their own action plans.

</details>

---

### [[20_Research/Papers/机器人/Belief-Overlap_Partial_Inversion_Object-Centric_Flow_Replanning_for_Humanoid_Loco-Manipulation|Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation]]

![[assets/2610.13087_figure.png|800]]

- **arXiv**: [2610.13087](https://arxiv.org/abs/2610.13087)
- **PDF**: https://arxiv.org/pdf/2610.13087
- **详细分析**: [[20_Research/Papers/机器人/Belief-Overlap_Partial_Inversion_Object-Centric_Flow_Replanning_for_Humanoid_Loco-Manipulation|Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation]]
- **作者**: Chen Yu, Sudarshan S Harithas, Juan Borbon, Dingqi Zhang, Jiuguang Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

People often learn how an unfamiliar object moves through a small exploratory push, using its response to guide their next motion. Inspired by this behavior, we study humanoids pushing carts whose mass and caster stiffness are initially unknown. Our object-centric framework closes online estimation, flow-based planning, and whole-body control into a loop, creating a tension: replacing the plan whenever the belief shifts disrupts the maneuver under way, while keeping it strands the robot on a path its evidence has ruled out. Belief-Overlap Partial Inversion (BOPI) scales revision to agreement, inverting the flow under the old belief only as far as the beliefs disagree before reconstructing under the new one. Across 18 simulated goals it lowers pooled final position and yaw error by roughly 33% and 47% against fixed-depth replanning, and on hardware it translates and turns a non-holonomic cart.

</details>

---

### [[20_Research/Papers/强化学习/VICAR_Video_Imitation_with_Contact-Aware_Retargeting_for_Humanoid_Interactive_Skills|VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills]]

![[assets/2610.13079_figure.png|800]]

- **arXiv**: [2610.13079](https://arxiv.org/abs/2610.13079)
- **PDF**: https://arxiv.org/pdf/2610.13079
- **详细分析**: [[20_Research/Papers/强化学习/VICAR_Video_Imitation_with_Contact-Aware_Retargeting_for_Humanoid_Interactive_Skills|VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills]]
- **作者**: Dvij Kalaria, Bike Zhang, S. Shankar Sastry
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Third-person human videos offer a scalable alternative to task-specific reward engineering, teleoperation, and manually scripted demonstrations for humanoid loco-manipulation. Recent video-to-humanoid systems have shown that noisy human motion, object trajectories, and contacts can be extracted from unstructured videos and refined into deployable skills. However, a key gap remains for contact-rich imitation: the task is often defined by world-frame contacts whose poses, timing, and speed must survive embodiment mismatch and runtime scene changes. Towards this, we present VICAR (Video Imitation with Contact-Aware Retargeting), a pipeline for learning humanoid interactive skills from third-person human videos. The system first recovers human motion, reconstructs task-relevant obstacles from monocular video, and then retargets the motion to a humanoid while preserving global contact poses, motion speed, and collision clearance. Unlike retargeting methods that only remove penetration or preserve local interaction geometry, our formulation represents user-specified contact poses and collision clearance as high-priority Lagrangian penalty terms and optimizes the full motion to remain smooth through contact-rich transitions. The resulting motions are used to train a contact-conditioned motion generator whose inputs include movable contact points enabling runtime adaptation to new contact positions. We demonstrate the framework on ten diverse third-person video skills, including six table-tennis serves, three object-pickup tasks, and ladder climbing, and deploy the learned skills on hardware. These results suggest that contact-preserving retargeting is a practical step toward humanoids that learn useful interactive behavior by watching humans.

</details>

---

### [[20_Research/Papers/机器人/Failure-Resilient_Multi-Robot_Coordination_with_$k$-Connectivity_Constrained_Submodular_Maximization|Failure-Resilient Multi-Robot Coordination with $k$-Connectivity Constrained Submodular Maximization]]

![[assets/2610.13049_figure.png|800]]

- **arXiv**: [2610.13049](https://arxiv.org/abs/2610.13049)
- **PDF**: https://arxiv.org/pdf/2610.13049
- **详细分析**: [[20_Research/Papers/机器人/Failure-Resilient_Multi-Robot_Coordination_with_$k$-Connectivity_Constrained_Submodular_Maximization|Failure-Resilient Multi-Robot Coordination with $k$-Connectivity Constrained Submodular Maximization]]
- **作者**: Yoonjae Hwang, Hojune Kim, Ellen Novoseller, Guangyao Shi, Gaurav S. Sukhatme
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Security, Systems

#### 研究背景与动机

《Failure-Resilient Multi-Robot Coordination with $k$-Connectivity Constrained Submodular Maximization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot coordination is essential in applications such as coverage, target tracking, and information gathering, where robots must jointly select actions to maximize team performance. Submodular maximization provides an effective framework for such coordination, and resilient variants further account for robot failures or adversarial removals. However, existing methods typically overlook the impact of robot loss on the communication network, which may disconnect the surviving team and prevent continued coordination. To address this issue, we introduce Resilient $k$-Connected Submodular Maximization, which jointly considers task performance, resilience, and communication connectivity. The resulting feasible family is not a matroid, preventing the direct application of classical curvature-greedy guarantees. We overcome this challenge through a Menger-based connectivity reduction, a connectivity-aware greedy algorithm with a feasibility-preserving fallback, and a new curvature-based analysis that captures the cost of enforcing connectivity through a single factor $ρ$. Our method achieves a worst-case post-failure objective within a factor of $[\max(1-ν_f(\mathcal{I}),h(N,β))]^2 ρ\frac{1}{κ_f}(1-e^{-κ_f})$ of the optimal connectivity-respecting resilient assignment, while recovering the classical unconstrained guarantee in the appropriate limits. Experiments on multi-robot target tracking validate the proposed method and characterize the practical impact of connectivity constraints.

</details>

---

### [[20_Research/Papers/具身智能/CeDR-Nav_Cross-Embodiment_Mapless_Navigation_via_Offline_Demonstration_Recasting|CeDR-Nav: Cross-Embodiment Mapless Navigation via Offline Demonstration Recasting]]

![[assets/2610.13007_figure.png|800]]

- **arXiv**: [2610.13007](https://arxiv.org/abs/2610.13007)
- **PDF**: https://arxiv.org/pdf/2610.13007
- **详细分析**: [[20_Research/Papers/具身智能/CeDR-Nav_Cross-Embodiment_Mapless_Navigation_via_Offline_Demonstration_Recasting|CeDR-Nav: Cross-Embodiment Mapless Navigation via Offline Demonstration Recasting]]
- **作者**: Xianghui Wang, Xinming Zhang, Yiwei Qian, Siwei Cheng, Shanze Wang, Dan Zhang, Wei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《CeDR-Nav: Cross-Embodiment Mapless Navigation via Offline Demonstration Recasting》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based methods have demonstrated strong performance in mapless robot navigation. However, a learned policy remains restricted to the embodiment on which it was trained. Many cross-embodiment navigation methods require time-consuming online training and can still underperform target-specific policies. In fact, demonstrations collected on a source embodiment already contain navigation experience that is potentially reusable for deriving a policy for each target embodiment, but the embodiment mismatch prevents these demonstrations from directly serving as valid supervision for the target. In this article, we present CeDR-Nav, a cross-embodiment demonstration recasting framework that trains a dedicated navigation policy for each target embodiment from existing source demonstrations without online data collection. Geometry-consistent scaling with per-demonstration validity assessment converts the source demonstrations into target training data, and a target-specific Gaussian mixture policy generates feasible avoidance maneuvers for each target embodiment. Extensive quantitative simulations and real-world deployments across multiple robot platforms demonstrate the effectiveness of CeDR-Nav, with an average success-rate gain of 13.8 percentage points over DRL-DCLP in cross-embodiment simulations and target-specific policy training completed within seconds.

</details>

---

### [[20_Research/Papers/具身智能/Adaptive_Whole-Body_MPC_with_Optimal_Posture_Planning_for_Humanoid_Robots_under_Unknown_Payloads|Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads]]

![[assets/2610.12972_figure.png|800]]

- **arXiv**: [2610.12972](https://arxiv.org/abs/2610.12972)
- **PDF**: https://arxiv.org/pdf/2610.12972
- **详细分析**: [[20_Research/Papers/具身智能/Adaptive_Whole-Body_MPC_with_Optimal_Posture_Planning_for_Humanoid_Robots_under_Unknown_Payloads|Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads]]
- **作者**: Manh Cuong Nguyen, Duc Cuong Vu, Viet Anh Vu, Duc Tuan Pham, Toan Nguyen, Minh Hiep Phung, Ngo Anh Vien, Minh Nhat Vu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Gait-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots performing lifting and material-handling tasks must maintain balance despite unknown and varying payloads. However, payload uncertainty significantly affects whole-body dynamics and may destabilize conventional controllers. We propose an adaptive whole-body control architecture that integrates three components: (i) a centroidal model predictive controller (MPC) that generates dynamically feasible reference motions, (ii) an adaptive fuzzy balance controller that compensates for payload-induced model mismatch by generating corrective torques distributed across the supporting-leg joints, and (iii) a waypoint-based optimal posture planner built on a triple-integrator model that produces smooth sit-to-stand and stand-to-sit trajectories satisfying center-of-mass (CoM) stability constraints, joint limits, and whole-body feasibility requirements. Together, these components enable stable lowering, grasping, lifting, carrying, and placing behaviors under significant payload uncertainty. Extensive simulation and hardware experiments demonstrate that the proposed framework improves balance robustness and reduces tracking degradation during posture transitions and lifting tasks compared to non-adaptive baselines.

</details>

---

### [[20_Research/Papers/具身智能/Evo-World_A_Lightweight_Vision-Language-Action_Model_with_Future_Motion_Prediction_via_Optical-Flow_Supervision|Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision]]

![[assets/2610.12936_figure.png|800]]

- **arXiv**: [2610.12936](https://arxiv.org/abs/2610.12936)
- **PDF**: https://arxiv.org/pdf/2610.12936
- **详细分析**: [[20_Research/Papers/具身智能/Evo-World_A_Lightweight_Vision-Language-Action_Model_with_Future_Motion_Prediction_via_Optical-Flow_Supervision|Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision]]
- **作者**: Zile Zhong, Yuxin Du, Tao Lin, Haoxiao Wang, Wei Dai, Binhua Zuo, Bo Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Evo-World: A Lightweight Vision-Language-Action Model with Future Motion Prediction via Optical-Flow Supervision》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Evo-World, Meta-World, OpenVLA, SmolVLA, TemporalFlow-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models provide a unified framework for visual understanding, language grounding, and robot control, yet anticipating how the scene will evolve beyond the current observation can provide additional information for control. Action supervision alone does not explicitly encourage such anticipation, while future-image prediction entangles task-relevant motion with largely static appearance. To address these limitations, we introduce Evo-World, a lightweight VLA model that augments policy learning with future motion prediction through optical-flow supervision, thereby providing a task-relevant predictive signal focused on motion rather than appearance. We further design the training procedure to preserve these predictive representations during policy learning, regulating representation diversity while decoupling representation learning from action optimization. Across simulation benchmarks, Evo-World demonstrates strong performance, achieving a tier-averaged success rate of 91.1% on Meta-World MT50 , with a 13.0% relative improvement over the non-predictive baseline. On real-world AgileX robots, Evo-World outperforms the evaluated baselines across single-arm and bimanual manipulation tasks while using only 0.87B parameters and delivering lower GPU memory usage and higher inference efficiency. These results demonstrate that future motion prediction through optical-flow supervision provides an effective and lightweight approach to enhancing the predictive capabilities of VLA models.

</details>

---

### [[20_Research/Papers/强化学习/Sampling-based_Kinodynamic_Planning_with_World_Models|Sampling-based Kinodynamic Planning with World Models]]

![[assets/2610.12910_figure.png|800]]

- **arXiv**: [2610.12910](https://arxiv.org/abs/2610.12910)
- **PDF**: https://arxiv.org/pdf/2610.12910
- **详细分析**: [[20_Research/Papers/强化学习/Sampling-based_Kinodynamic_Planning_with_World_Models|Sampling-based Kinodynamic Planning with World Models]]
- **作者**: Yitian Gao, Hanlan Yang, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，世界模型 1，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Sampling-based Kinodynamic Planning with World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models predict the consequences of actions from images, but planning with them is typically done by optimizers such as CEM and MPPI. However, these optimizers stall on long-horizon tasks where progress requires motion the objective does not reward, such as moving around a block before pushing it. This paper revisits kinodynamic sampling-based motion planning for world models, using the learned model as the propagator of a tree search in latent space. Our key insight is that the sampling strategies devised for high-dimensional search in configuration space apply directly to the latent space of a world model, where they rapidly expand through intermediate states that myopic optimizers never sample. We present two exploration strategies for the high-dimensional latent space, nearest-neighbor-guided RRT and projection-based KPIECE, with GPU-native batched expansion for efficient device utilization. We evaluate with an off-the-shelf DINO-WM on four simulated domains and a real-world block-pushing task. Our approaches match or exceed the success rate of CEM and MPPI at up to 13.8x lower planning time in simulation, and improve the success rate by 20% on the real robot.

</details>

---

### [[20_Research/Papers/具身智能/TAME-Nav_Temporal_Asymmetric_Mixture-of-Experts_Distillation_for_Agile_and_Versatile_Robot_Navigation|TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation]]

![[assets/2610.12877_figure.png|800]]

- **arXiv**: [2610.12877](https://arxiv.org/abs/2610.12877)
- **PDF**: https://arxiv.org/pdf/2610.12877
- **详细分析**: [[20_Research/Papers/具身智能/TAME-Nav_Temporal_Asymmetric_Mixture-of-Experts_Distillation_for_Agile_and_Versatile_Robot_Navigation|TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation]]
- **作者**: Lingjie Zhang, Jun Xue, Shanze Wang, Haoyu Xi, Xinming Zhang, Xiaoyu Shen, Wei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, NavRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agile and reliable navigation is a core capability for embodied robots navigating complex spatial constraints and dynamic interactions. However, a single policy often struggles to accommodate the distinct decision-making demands of diverse scenarios. We present TAME-Nav, an asymmetric Teacher-Student navigation framework built around a temporal soft mixture of experts (Soft-MoE). The Teacher combines clean observations with causally maintained dynamic-obstacle tracks to construct privileged representations, while the Student learns complementary navigation features from corrupted observation histories through temporal encoding, soft expert routing, and latent distillation. Procedural scenario generation and parallel task-level simulation broaden training coverage, while deployment-informed asymmetric domain randomization supports sim-to-real transfer. Across in-distribution and unseen compositional scenarios, TAME-Nav achieves higher success rates, lower collision rates, and higher navigation scores than representative baselines. On a real quadruped robot, it completes all twenty trials across local-trap escape and narrow-passage navigation with sudden dynamic obstacles, with only one minor contact.

</details>

---

### [[20_Research/Papers/具身智能/Evidence-Guided_Counterfactual_Learning_for_Long-Tailed_Robotic_Policies|Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies]]

![[assets/2610.12861_figure.png|800]]

- **arXiv**: [2610.12861](https://arxiv.org/abs/2610.12861)
- **PDF**: https://arxiv.org/pdf/2610.12861
- **详细分析**: [[20_Research/Papers/具身智能/Evidence-Guided_Counterfactual_Learning_for_Long-Tailed_Robotic_Policies|Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies]]
- **作者**: Weiwei Chen, Chenghao Xu, Meiling Yu, Xu Yang, Cheng Deng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Evidence-Guided Counterfactual Learning for Long-Tailed Robotic Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MiniVLA, OpenVLA, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the practical deployment of vision--language--action policies, handling long-tailed task distributions is a common challenge due to the highly imbalanced composition of robot demonstration datasets. To investigate this issue, we study the head-task action bias in shared robot policies, particularly focusing on its relationship with task-specific visual evidence. Our experimental analysis shows that, when the visual evidence required by a tail task is insufficient, the policy increasingly falls back on action patterns reinforced by data-rich head tasks, resulting in degraded performance on under-represented tasks. Motivated by this observation, we propose Evidence-Guided Counterfactual Learning, a training framework for long-tailed robot policies. Our method identifies decision-relevant visual evidence using instruction-related and action-related signals, and constructs counterfactual observations by removing the selected evidence. The resulting counterfactual predictions are used to strengthen the association among task instructions, visual evidence, and actions, with the supervision adaptively adjusted according to the number of demonstrations available for each task. The proposed framework requires neither additional training data nor region-level annotations and incurs no additional computation during deployment. Extensive experiments across simulated benchmarks, different VLA architectures, and real-world robot platforms demonstrate that our method robustly and consistently improves long-tailed robot policy learning, particularly for tail tasks, while maintaining reliable performance on head tasks.

</details>

---

### [[20_Research/Papers/具身智能/VLMs_are_Native_Action_Models_Unleashing_the_Manipulation_Capabilities_of_VLMs_with_Explicit_Action-Space_Grounding|VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding]]

![[assets/2610.12832_figure.png|800]]

- **arXiv**: [2610.12832](https://arxiv.org/abs/2610.12832)
- **PDF**: https://arxiv.org/pdf/2610.12832
- **详细分析**: [[20_Research/Papers/具身智能/VLMs_are_Native_Action_Models_Unleashing_the_Manipulation_Capabilities_of_VLMs_with_Explicit_Action-Space_Grounding|VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding]]
- **作者**: Jingkun Yi, Shujie Zhang, Zirui Zhou, Haoxiao Wang, Haiyang Sun, Yuhang Dong, Xudong Xu, Xing Shen, Tao Zhang, Yong Liu, Jiangning Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VLMs are Native Action Models: Unleashing the Manipulation Capabilities of VLMs with Explicit Action-Space Grounding》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language models (VLMs) already exhibit strong visual, spatial and reasoning capabilities relevant to robotic manipulation. The key challenge in turning pretrained VLMs into generalist manipulation policies is to expose these capabilities through an appropriate action interface. Vision-language-action (VLA) models provide a unified trainable policy, but typically introduce learned action tokens, action heads, or action experts whose semantics must be learned from robot data pretraining. In contrast, modular foundation-model-based manipulation methods can exploit pretrained VLM capabilities for zero-shot manipulation, but rely on external planning and control scaffolds that are not end-to-end trainable as a unified continuous-action policy. In this work, we introduce EASG, an Explicit Action-Space Grounding framework that bridges these two paradigms. By projecting a tool center point (TCP)-centered action frame into the wrist camera observation and expressing actions in the form of VLM's native textual generation interface, EASG makes the semantics of a continuous robot action space directly observable in the VLM's perceptual context. This allows pretrained VLMs to directly generate executable robot actions using their existing visual-spatial reasoning capabilities, without robot-action pretraining or additional action modules. Besides, the same action interface supports direct fine-tuning with robot trajectories, allowing the models to continuously improve beyond their manipulation capabilities unleashed by EASG. Overall, EASG enables zero-shot manipulation and generalization across object positions, categories, and robot embodiments, while supporting effective fine-tuning in the same continuous action space. These results demonstrate that, given an appropriate action interface, pretrained VLMs can themselves serve as native action models for robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Cubic_Spline_Interpolation_for_Smooth_Trajectory_Generation_in_Autonomous_Motion_Systems|Cubic Spline Interpolation for Smooth Trajectory Generation in Autonomous Motion Systems]]

![[assets/2610.12826_first_page.png|800]]

- **arXiv**: [2610.12826](https://arxiv.org/abs/2610.12826)
- **PDF**: https://arxiv.org/pdf/2610.12826
- **详细分析**: [[20_Research/Papers/机器人/Cubic_Spline_Interpolation_for_Smooth_Trajectory_Generation_in_Autonomous_Motion_Systems|Cubic Spline Interpolation for Smooth Trajectory Generation in Autonomous Motion Systems]]
- **作者**: Aarush Mandayam, Sriram Aditya Gundla, Elliott Tammaro
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Cubic Spline Interpolation for Smooth Trajectory Generation in Autonomous Motion Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We presented a program that automates the construction and solution of the cubic spline interpolation problem for a sequence of position-time waypoints, producing trajectories that are continuous in position, velocity, and acceleration and therefore avoid the infinite-acceleration problem inherent to piecewise-linear waypoint following. By assembling the interpolation and continuity conditions into a single linear system and solving directly for the spline coefficients, the program removes the need to manually derive per-segment equations for each new waypoint set. We illustrated the approach on free-form curve drawing and signature digitization, two tasks that use the same underlying machinery required for smooth robot and drone trajectory generation. Future work includes extending the implementation to multi-axis trajectories with explicit velocity and acceleration bounds, adopting the more computationally efficient tridiagonal solution method for larger waypoint sets, and evaluating the approach quantitatively against alternative trajectory generation methods.

</details>

---

### [[20_Research/Papers/具身智能/Gamma_Grounded_Multi-Agent_Memory_with_Mechanical_Audit_for_Memory-Intensive_Manipulation|Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation]]

![[assets/2610.12793_figure.png|800]]

- **arXiv**: [2610.12793](https://arxiv.org/abs/2610.12793)
- **PDF**: https://arxiv.org/pdf/2610.12793
- **详细分析**: [[20_Research/Papers/具身智能/Gamma_Grounded_Multi-Agent_Memory_with_Mechanical_Audit_for_Memory-Intensive_Manipulation|Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation]]
- **作者**: Yudong Liu, Yueqian Lin, Zijia Tang, Yuxi Zheng, Yuan Li, Shuai Zhang, Yi Li, Taotao Jing, Shuangjun Liu, Dashan Gao, Ning Bi, Jingwei Sun...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Gamma: Grounded Multi-Agent Memory with Mechanical Audit for Memory-Intensive Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language-action (VLA) policies fail on memory tasks, behaviour that depends on events observed long before the current frame, because their training data is overwhelmingly Markov and mapping episodic memory directly to action chunks is hard. Yet the same policy, finetuned once to follow a privileged oracle's grounded-subgoal text, nearly solves these tasks: the difficulty lies entirely in mapping memory to a grounded symbolic subgoal. Existing work entrusts this stage to a single VLM that selects keyframes and reasons over raw frames, and falls far short of the oracle: key identities and dynamics are buried in noisy pixels, the reasoning spans hundreds of frames in an unbounded context, and hallucination corrupts the memory itself. We instead present GAMMA (Grounded multi-Agent Memory with Mechanical Audit), which builds the stage as a collaborating two-agent memory system: a detector tool (SAM-3) for spatial grounding, a VLM writer that distils each replan window into one grounded text line, an append-only text memory bank, and a VLM reasoner that reads the bank and emits the next grounded subgoal at the oracle's cadence, wrapped in a propose-verify harness that admits, defers, corrects, or rejects every agent claim against mechanical visual evidence, at training-corpus construction and at deployment alike. On a sixteen-task memory-manipulation suite GAMMA recovers a large fraction of the oracle ceiling with the policy held fixed, reaching the ceiling on several tasks, and transfers with unchanged contracts to a second benchmark.

</details>

---

### [[20_Research/Papers/具身智能/Tactile_Sensing-based_Secure_and_Gentle_Grasping_of_Unknown_Objects|Tactile Sensing-based Secure and Gentle Grasping of Unknown Objects]]

![[assets/2610.12790_figure.png|800]]

- **arXiv**: [2610.12790](https://arxiv.org/abs/2610.12790)
- **PDF**: https://arxiv.org/pdf/2610.12790
- **详细分析**: [[20_Research/Papers/具身智能/Tactile_Sensing-based_Secure_and_Gentle_Grasping_of_Unknown_Objects|Tactile Sensing-based Secure and Gentle Grasping of Unknown Objects]]
- **作者**: Feng Han
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Tactile Sensing-based Secure and Gentle Grasping of Unknown Objects》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic manipulation requires maintaining a firm grasp while strictly avoiding both contact slip and structural damage to the object. Satisfying these inherent \textit{secure-and-gentle} grasping constraints is challenging for unknown objects. We present a novel online data-driven predictive control framework for safe dynamic robotic grasping of unknown objects. The proposed system features a pair of compact, single-channel tactile-sensing modules that characterize the gripper-object dynamic interaction in real time, entirely bypassing the need for prior knowledge or offline training. A finite-state-machine-based grasping force probing mechanism is developed to establish the initial grasping force and explicitly identify grasping force constraints. Through online dynamics learning, a Gaussian Process (GP) model captures gripper-object interaction dynamics. The model uncertainties are further used to form robust grasping constraints, which are embedded into a model predictive control scheme. We demonstrate error convergence in a probabilistic sense. The proposed control framework runs at 100~Hz in real time to dynamically manipulate and handle objects rather than static holding. Extensive experimental evaluations across diverse contact surface topologies and various types of objects validate superior performance and efficiency compared to baseline strategies. The proposed method is able to manipulate objects ranging from delicate items, such as raw tofu and marshmallows, to rough objects, such as rocks.

</details>

---

### [[20_Research/Papers/具身智能/Multimodal_Image-based_Robotic_Assistance_and_Guidance_Environment_(MIRAGE)_A_Novel_Unified_Framework_for_Surgical_Navigation_and_Visualizat|Multimodal Image-based Robotic Assistance and Guidance Environment (MIRAGE): A Novel Unified Framework for Surgical Navigation and Visualization]]

![[assets/2610.12780_figure.jpg|800]]

- **arXiv**: [2610.12780](https://arxiv.org/abs/2610.12780)
- **PDF**: https://arxiv.org/pdf/2610.12780
- **详细分析**: [[20_Research/Papers/具身智能/Multimodal_Image-based_Robotic_Assistance_and_Guidance_Environment_(MIRAGE)_A_Novel_Unified_Framework_for_Surgical_Navigation_and_Visualizat|Multimodal Image-based Robotic Assistance and Guidance Environment (MIRAGE): A Novel Unified Framework for Surgical Navigation and Visualization]]
- **作者**: Ehsan Nasiri, Yi Zheng, Michael A. Kokko, Xiaoyao Fan, William R. Warner, Keith D. Paulsen, Ryan J. Halter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Multimodal Image-based Robotic Assistance and Guidance Environment (MIRAGE): A Novel Unified Framework for Surgical Navigation and Visualization》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents the computational architecture and quantitative preclinical evaluation of MIRAGE, a multimodal image-guided robotic surgery framework for real-time visualization and navigation. It integrates stereovision scene reconstruction, augmented-reality (AR) video overlay, quantified heads-up display (HUD) navigation, and intraoperative ultrasound within the da Vinci console's TilePro display (Intuitive Surgical). Additional modules include optical/electromagnetic tracker registration, stereo calibration, fiducial rigid registration with RMSE feedback, and 3D point-cloud reconstruction. Video I/O and rendering run in a C++ backend, while a Python GUI coordinates calibration, registration, reconstruction, visualization, and user interaction through an in-process zero-copy binding layer. The framework formalizes spatial transforms, module states, and synchronization of heterogeneous video and tracking streams. Preoperative calibration uses synchronized checkerboard image pairs and optimization, with estimated intrinsics, extrinsics, and rectification reused intraoperatively. MIRAGE was validated in phantom experiments across da Vinci S, Si, Xi, and SP platforms. Across clinically relevant working distances, mean 3D reprojection error was 0.6mm, with best 0.1mm RMSE at 100mm on Xi. Results support MIRAGE as a preclinical technical-validation platform for accurate, responsive, and extensible multimodal surgical guidance.

</details>

---

### [[20_Research/Papers/强化学习/Reflex_Visually_Grounded_Reactive_Humanoid_Control|Reflex: Visually Grounded Reactive Humanoid Control]]

![[assets/2610.12772_figure.png|800]]

- **arXiv**: [2610.12772](https://arxiv.org/abs/2610.12772)
- **PDF**: https://arxiv.org/pdf/2610.12772
- **详细分析**: [[20_Research/Papers/强化学习/Reflex_Visually_Grounded_Reactive_Humanoid_Control|Reflex: Visually Grounded Reactive Humanoid Control]]
- **作者**: Taoyang Jia, Weikai Huang, Linxin Song, Jared Darlington, Jieyu Zhao, Yue Wang, Jiafei Duan, Zhongzheng Ren, Ranjay Krishna
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.2，强化学习 0.2，机器人 0.9）
- **关联关键词**: RL

#### 研究背景与动机

《Reflex: Visually Grounded Reactive Humanoid Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans effortlessly react to the world; they adeptly return a tennis shot, catch a falling cup, step aside from a passing cart, or pass a box tossed during truck unloading. These everyday actions require anticipating a moving target and reflexively responding with the whole body within about a second. Such visual reactive whole-body control remains challenging for humanoids, which must (1) coordinate whole-body control, (2) react to object dynamics in real time, and (3) ground perception in egocentric vision. We study catching thrown boxes as a representative task that demands all three capabilities; existing systems cover only part of it, relying on end-effectors, motion capture, or marked objects. We present Reflex, a three-stage framework that learns these capabilities stage by stage while connecting them through a compact representation of object dynamics. First, a state-based policy learns whole-body catching with reinforcement learning. Second, the policy learns to infer the dynamics of a moving box from delayed and incomplete observations. Third, an egocentric RGB-D encoder learns to recover this dynamics representation directly from visual observations while keeping the whole-body controller fixed. This decomposition provides each capability with a direct training signal and makes visual learning substantially more scalable. In simulation, Reflex achieves 85.7% catch success from egocentric RGB-D, compared with 87.9% when given privileged box observations. Temporal visual history is critical: removing it reduces success by 35.6 and 39.8 points on centered and laterally offset throws. On a real Unitree G1, Reflex catches human-thrown boxes with 65% and 40% success at 2.5 and 5 m, reaching 76% and 59% of human catchers' success at the same distances.

</details>

---

### [[20_Research/Papers/具身智能/Verifier-Mediated_Multi-LLM_Coordination_for_Multi-Robot_Path_Planning|Verifier-Mediated Multi-LLM Coordination for Multi-Robot Path Planning]]

![[assets/2610.12761_figure.jpg|800]]

- **arXiv**: [2610.12761](https://arxiv.org/abs/2610.12761)
- **PDF**: https://arxiv.org/pdf/2610.12761
- **详细分析**: [[20_Research/Papers/具身智能/Verifier-Mediated_Multi-LLM_Coordination_for_Multi-Robot_Path_Planning|Verifier-Mediated Multi-LLM Coordination for Multi-Robot Path Planning]]
- **作者**: Vivek Khatana, Zijian Song, Naira Hovakimyan, Petros Voulgaris
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.6，大模型 0.4，机器人 1.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Verifier-Mediated Multi-LLM Coordination for Multi-Robot Path Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models are increasingly used for high-level multi-robot task planning, yet independently generated symbolic plans can become jointly infeasible after geometric grounding because of shared spatial and temporal constraints. We study execution-aware coordination of large-language-model (LLM) planners for multi-robot navigation. We compare a centralized architecture, in which one LLM jointly reasons over the robot team, with a decentralized multi-LLM architecture in which each robot independently proposes a task plan. A geometric verifier grounds the candidate plans into robot trajectories, detects predicted inter-robot conflicts, and converts conflict information into structured feedback for targeted replanning. This verifier-mediated architecture separates semantic task reasoning from execution-level feasibility while enabling iterative coordination among LLM planners. Experiments in CARLA and on Crazyflie aerial robots evaluate coordination performance as task complexity increases and characterize the trade-offs between centralized reasoning, decentralized verifier-mediated coordination, and physical executability.

</details>

---

### [[20_Research/Papers/具身智能/Visual-Wi-Fi_Navigation_to_Signal-Emitting_Devices|Visual-Wi-Fi Navigation to Signal-Emitting Devices]]

![[assets/2610.12733_figure.png|800]]

- **arXiv**: [2610.12733](https://arxiv.org/abs/2610.12733)
- **PDF**: https://arxiv.org/pdf/2610.12733
- **详细分析**: [[20_Research/Papers/具身智能/Visual-Wi-Fi_Navigation_to_Signal-Emitting_Devices|Visual-Wi-Fi Navigation to Signal-Emitting Devices]]
- **作者**: Lihao Wang, Tianjian Xu, Tianmin Shu, Renjie Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Visual-Wi-Fi Navigation to Signal-Emitting Devices》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Indoor navigation to task-relevant targets remains difficult when the target is small, occluded, or visually indistinct. Meanwhile, smart appliances, mobile devices, and IoT tags emit Wi-Fi signals during everyday communication, providing a pervasive but underused spatial cue. We study visual-Wi-Fi navigation, where a robot reaches a signal-emitting device in an unmapped environment using onboard visual observations and Wi-Fi packets overheard from the device, without connecting to the device or modifying infrastructure. Realizing this requires pose-dependent Wi-Fi observations during closed-loop policy learning and reliable spatial cues from bearing measurements corrupted by indoor multipath propagation on a moving robot. We present WiFiSpaces, which extends the Habitat embodied simulator with online ray-traced Wi-Fi sensing, rendering Wi-Fi observations for a robot-mounted antenna array at continuous poses during policy rollouts. On top of it, we build ViFiNav, a localization-aware navigation framework: an online source-localization algorithm exploits robot motion to disambiguate and robustly aggregate bearings from multiple viewpoints into a confidence-aware source estimate, and a learned policy fuses this evolving estimate with depth observations and learns to act on it as it is refined. Experiments show that exploiting robot motion is key to accurate source estimates, and that fine-tuning on ray-traced Wi-Fi observations in WiFiSpaces improves the success rate of ViFiNav. The policy transfers zero-shot to unseen scene datasets, and we deploy it on a real robot with a Wi-Fi sensor built from a commodity router, without any real-world training.

</details>

---

### [[20_Research/Papers/具身智能/REMM_Revisable_Embodied_Memory_for_Manipulation|REMM: Revisable Embodied Memory for Manipulation]]

![[assets/2610.12710_figure.png|800]]

- **arXiv**: [2610.12710](https://arxiv.org/abs/2610.12710)
- **PDF**: https://arxiv.org/pdf/2610.12710
- **详细分析**: [[20_Research/Papers/具身智能/REMM_Revisable_Embodied_Memory_for_Manipulation|REMM: Revisable Embodied Memory for Manipulation]]
- **作者**: Revanth Krishna Senthilkumaran, Ruwan Wickramarachchi, Alessandro Oltramari, Jonathan Francis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《REMM: Revisable Embodied Memory for Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChainVLA, EventVLA, MemoryVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon manipulation requires robots to retain task-relevant history while revising conclusions no longer supported by physical evidence. Retaining observations alone does not specify which completed conditions should be withdrawn after a disturbance or which obligations require repair. We introduce REMM, Revisable Embodied Memory for Manipulation, a supervisory memory layer for a frozen G0.5 vision-language-action executor. REMM separates an append-only evidence history from revisable task state and explicitly links derived relations and completed conditions to their supporting facts. When accepted evidence changes a supporting fact, it withdraws dependent conclusions and schedules targeted recovery at verified skill boundaries without updating the executor. Across 51 physical trials, including operator-assisted runs, REMM improves mean recorded task progress over the strongest baseline from 57% to 91% in intervention recovery and from 43% to 70% in sequence recall. Complementary video diagnostics show improved grounding of retained history into the next instruction, including comparisons with $π_{0.5}$-compatible high-level planner adaptations. These results support revisable memory as a practical interface for continued manipulation without policy retraining. Project: https://revanthsenthil.github.io/remm/.

</details>

---

### [[20_Research/Papers/具身智能/Spa-Bench_A_Real-Robot_Benchmark_for_Spatial_Grounding_in_Vision-Language-Action_Models|Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models]]

![[assets/2610.12696_figure.png|800]]

- **arXiv**: [2610.12696](https://arxiv.org/abs/2610.12696)
- **PDF**: https://arxiv.org/pdf/2610.12696
- **详细分析**: [[20_Research/Papers/具身智能/Spa-Bench_A_Real-Robot_Benchmark_for_Spatial_Grounding_in_Vision-Language-Action_Models|Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models]]
- **作者**: Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ManipBench, OpenVLA, RLBench, Real-World, Spa-Bench, VIMA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) offer a promising route toward general-purpose robotics by transferring semantic knowledge from large-scale vision-language pretraining into language-conditioned control. However, most VLA evaluations emphasize aggregate manipulation success under changes in objects, instructions, or environments, leaving unclear how reliably these policies ground spatial descriptions in the physical scenes where they act. We therefore ask a sharper question: how reliably can current VLAs translate spatial descriptions into appropriate real-robot behavior? To investigate this, we introduce Spa-Bench, a real-robot benchmark that evaluates spatial grounding across six tabletop tasks covering Object State, Relative Size, Referential Description, Relational Placement, Ordinal Position, and Counting. Our primary evaluation compares in-distribution (ID) and out-of-distribution (OOD) spatial configurations while retaining training support for the relevant objects, concepts, and actions, reducing object and motor unfamiliarity as alternative explanations for failure. Four diagnostic conditions further probe physical execution, sensitivity to wording, object-task associations, and recognition that no action is required. We release 4,092 episodes collected on the SO-101 robot arm: 1,200 human-teleoperated demonstrations and 2,892 real-robot evaluation rollouts from five state-of-the-art VLA policies. Across the three fully evaluated policies, success falls from 67.5-73.3% on ID spatial configurations to 40.7-52.0% on OOD spatial configurations, while matched direct instructions improve success by 28.3-40.0 percentage points. These results show that the evaluated VLAs can often execute the required manipulations but lack robust spatial grounding. Project materials, including videos, code, and benchmark data, are available at https://justintiensmith.github.io/Spa-Bench/.

</details>

---

### [[20_Research/Papers/机器人/Robust_and_Scalable_UAV-UGV_Planning_for_Aerial_Monitoring_under_Energy_and_Precedence_Constraints|Robust and Scalable UAV-UGV Planning for Aerial Monitoring under Energy and Precedence Constraints]]

![[assets/2610.12670_first_page.png|800]]

- **arXiv**: [2610.12670](https://arxiv.org/abs/2610.12670)
- **PDF**: https://arxiv.org/pdf/2610.12670
- **详细分析**: [[20_Research/Papers/机器人/Robust_and_Scalable_UAV-UGV_Planning_for_Aerial_Monitoring_under_Energy_and_Precedence_Constraints|Robust and Scalable UAV-UGV Planning for Aerial Monitoring under Energy and Precedence Constraints]]
- **作者**: Cahit Ikbal Er, Yasin Yazicioglu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Robust and Scalable UAV-UGV Planning for Aerial Monitoring under Energy and Precedence Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider planning for unmanned aerial vehicle (UAV) and unmanned ground vehicle (UGV) teams in aerial monitoring missions with ordering requirements on the monitoring points to be visited by the UAV. The system consists of multiple UAV-UGV teams, each comprising one UAV and one UGV. UAV energy limitations are modeled through endurance, defined as the maximum flight time on a full battery. The UGVs serve as mobile charging stations and transport the UAVs between consecutive aerial tours. Given a set of monitoring points subject to ordering constraints and the teams' initial and terminal positions, the objective is to minimize mission completion time while satisfying UAV energy limits and the required visit order under bounded travel-time disturbances that may arise during execution. Unlike prior work, the plan jointly determines vehicle routes and their timing, allowing teams to slow down as needed to satisfy the ordering constraints. We develop a polynomial-time algorithm that generates efficient solutions to the underlying NP-hard planning problem. We establish feasibility guarantees, characterize the algorithm's computational complexity, and evaluate its performance via numerical comparisons.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Harmonic-Covariance_Feedback_for_Hole_Closure_in_Planar_Robot_Swarms|Distributed Harmonic-Covariance Feedback for Hole Closure in Planar Robot Swarms]]

![[assets/2610.12637_first_page.png|800]]

- **arXiv**: [2610.12637](https://arxiv.org/abs/2610.12637)
- **PDF**: https://arxiv.org/pdf/2610.12637
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Harmonic-Covariance_Feedback_for_Hole_Closure_in_Planar_Robot_Swarms|Distributed Harmonic-Covariance Feedback for Hole Closure in Planar Robot Swarms]]
- **作者**: Jitian Liu, Subhrajit Bhattacharya
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Distributed Harmonic-Covariance Feedback for Hole Closure in Planar Robot Swarms》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider hole closure in a planar multi-agent system whose sensing disks form a time-varying Čech complex. We propose a harmonic-covariance feedback that uses harmonic edge signals to locate holes and converts those signals into agent forces. For distributed evaluation, we use a fixed-degree polynomial of the regularized Hodge Laplacian. This polynomial is evaluated through local operator applications. The closed loop has a unique global trajectory from every safe initial state. The model data and initial state are supplied with procedures for approximation to any requested accuracy with explicit error bounds. We assume that hole area is measurable and bounded, holes evolve continuously without splitting or merging, and only finitely many temporary new holes appear. Under these conditions, offline finite calculations produce rational lower bounds for the cumulative hole area on the time horizon without querying trajectory data. These bounds converge to that cumulative area, whether finite or infinite. If it is finite, holes close in the time-averaged sense: the average normalized hole area over every fixed-length time window tends to zero as time tends to infinity. In a 15-second numerical demo, all holes close by 9.9s and remain closed through the end.

</details>

---

### [[20_Research/Papers/机器人/Selectively_Actuated_Fiberbots_for_High-precision_Minimally_Invasive_Surgery|Selectively Actuated Fiberbots for High-precision Minimally Invasive Surgery]]

![[assets/2610.12636_figure.png|800]]

- **arXiv**: [2610.12636](https://arxiv.org/abs/2610.12636)
- **PDF**: https://arxiv.org/pdf/2610.12636
- **详细分析**: [[20_Research/Papers/机器人/Selectively_Actuated_Fiberbots_for_High-precision_Minimally_Invasive_Surgery|Selectively Actuated Fiberbots for High-precision Minimally Invasive Surgery]]
- **作者**: Jinshi Zhao, Libaihe Tian, Alex Ranne, Qindong Zheng, Yue Li, Xiaotong Guo, Ziqi Yang, Ali Anil Demircali, Mohamed E. M. K. Abdelaziz, Bruno Gil Rosa, Ferdinando Rodriguez y Baena, Burak Temelkuran
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Selectively Actuated Fiberbots for High-precision Minimally Invasive Surgery》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long, slender instruments are essential for minimally invasive surgery (MIS), but achieving precise distal manipulation becomes increasingly difficult when actuation extends along the entire instrument. Here, we present an electrothermally actuated fiber-based robot designed for MIS procedures, in which Joule heating is concentrated in the distal active segment. The fiber is fabricated using a thermal drawing process and uses embedded metallic wires for thermal actuation. This robotic fiber, 1.9 mm in diameter and 1.2 m in length, can precisely manipulate surgical laser fibers with positional precision below 100 $μ$m. The compact size of the fiber robot allows it to pass through the working channel of a flexible endoscope, while keeping both devices mechanically uncoupled to allow independent motion. A phantom demonstration combining the robotic fiber with a da Vinci instrument conceptually demonstrated its compatibility with existing endoscopic systems for clinical applications. Our robotic fiber enables precise distal motion and holds the potential to improve clinical outcomes by enhancing precision in MIS procedures.

</details>

---

### [[20_Research/Papers/具身智能/Image-Based_Path-Planning_for_Navigation_of_Soft-Growing_Robots_in_the_Spinal_Sub-Arachnoid_Space|Image-Based Path-Planning for Navigation of Soft-Growing Robots in the Spinal Sub-Arachnoid Space]]

![[assets/2610.12631_first_page.png|800]]

- **arXiv**: [2610.12631](https://arxiv.org/abs/2610.12631)
- **PDF**: https://arxiv.org/pdf/2610.12631
- **详细分析**: [[20_Research/Papers/具身智能/Image-Based_Path-Planning_for_Navigation_of_Soft-Growing_Robots_in_the_Spinal_Sub-Arachnoid_Space|Image-Based Path-Planning for Navigation of Soft-Growing Robots in the Spinal Sub-Arachnoid Space]]
- **作者**: George Dimas, Panagiotis G. Kalozoumis, Panagiotis Vartholomeos, Dimitris K. Iakovidis
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Image-Based Path-Planning for Navigation of Soft-Growing Robots in the Spinal Sub-Arachnoid Space》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, soft robotic procedures are being developed aiming at achieving targeted minimally invasive operations or drug administration in specific locations in the human body. Accordingly, specialized path-planning algorithms need to be investigated for the estimation of efficient paths that would protect the delicate tissue structures and simultaneously satisfy a set of requirements for the efficient navigation of the robot. In this context, we propose an image-based 3D pathplanning algorithm, which is an extension of the A* algorithm, for the navigation of a soft-growing robot inside the spinal subarachnoid space (SSS). The proposed algorithm is capable of estimating a safe pathway towards the goal location, while ensuring the establishment of anchor points that facilitate the efficient steering of the soft robot. The algorithm is evaluated using a highly detailed model of the SSS with respect to its capacity to satisfy the robot movement requirements and path efficiency.

</details>

---

### [[20_Research/Papers/机器人/Graph-Based_Heuristics_for_Minimum_Constraint_Removal_in_Cluttered_Robot_Motion_Planning|Graph-Based Heuristics for Minimum Constraint Removal in Cluttered Robot Motion Planning]]

![[assets/2610.12609_first_page.png|800]]

- **arXiv**: [2610.12609](https://arxiv.org/abs/2610.12609)
- **PDF**: https://arxiv.org/pdf/2610.12609
- **详细分析**: [[20_Research/Papers/机器人/Graph-Based_Heuristics_for_Minimum_Constraint_Removal_in_Cluttered_Robot_Motion_Planning|Graph-Based Heuristics for Minimum Constraint Removal in Cluttered Robot Motion Planning]]
- **作者**: Antony Thomas, Fulvio Mastrogiovanni, Marco Baglietto
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，机器人 1.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Graph-Based Heuristics for Minimum Constraint Removal in Cluttered Robot Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid and service robots operating in clut- tered human environments may encounter motion planning problems that are infeasible when all surrounding objects are treated as fixed obstacles. The Minimum Constraint Removal problem, which we refer to as MCR, addresses this situation by identifying the minimum number of constraints, such as movable objects, whose removal enables a collision-free path. However, computing an optimal MCR solution is NP-hard. In this work, we propose a graph-based heuristic pipeline that combines bidirectional feasible-set generation with fixed- length searches over reduced MCR graphs. We further derive an extended feasible-set generator for instances in which the candidates produced by the first generator do not contain a complete optimal removal set. Across six benchmarks, the evaluated pipeline matches the exact solution in three cases and, in the remaining cases, selects at most 31.25% more obstacles than the optimum, while being between 3.4 and 33.7 times faster than exact search. In one of the benchmarks, involving a manipulation task amidst clutter, selecting two rather than seven obstructing objects reduces the combined MCR, inverse- kinematics, and motion planning time from 84.72 s to 30.59 s. These results indicate that the proposed approach provides a practical compromise between computational efficiency and solution quality for motion planning among movable obstacles.

</details>

---

### [[20_Research/Papers/具身智能/What_Should_Embodied_Agents_Remember_Benchmarking_and_Evaluating_Memory_Modality_for_Embodied_Agents|What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents]]

![[assets/2610.12561_figure.png|800]]

- **arXiv**: [2610.12561](https://arxiv.org/abs/2610.12561)
- **PDF**: https://arxiv.org/pdf/2610.12561
- **详细分析**: [[20_Research/Papers/具身智能/What_Should_Embodied_Agents_Remember_Benchmarking_and_Evaluating_Memory_Modality_for_Embodied_Agents|What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents]]
- **作者**: Junxiang Wang, Yuchen Liu, Yi Wu, Guofei Chen, Nir Pechuk, Tao Chen, Zackory Erickson, Yuzhe Qin, Tianyu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.7，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongMemEval, MeMoREval, OpenEQA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory allows large language model (LLM) agents to use past experience, often stored as textual records, when responding to requests. For embodied agents that control robots, visual and spatial observations introduce a broader choice of memory modalities, affecting both the information available for subsequent tasks and the model inference costs of constructing and using memory. We introduce MeMoREval, a benchmark for studying this problem through a controlled experience-request protocol. Agents first experience a sequence of events without knowing the subsequent tasks, and subsequently they use memory to respond to information and action requests without receiving new observations. The benchmark comprises 53 tasks across four simulated indoor environments and measures task success alongside the inference costs of memory construction and use. Our reference evaluations reveal that storing frames outperforms storing generated descriptions at lower write-time inference cost for the primary model, while storing frames with scene graphs achieves the highest aggregate task success for every tested model. Extensions to accumulated experience, selective frame retention, and visual input to memory writers demonstrate how the benchmark accommodates further memory-design investigations. Two physical-robot demonstrations establish the feasibility of applying its protocol beyond simulation.

</details>

---

### [[20_Research/Papers/强化学习/PanTact_Teaching_Whole-Body_Dexterity_with_a_Wearable_Contact_Interface|PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface]]

![[assets/2610.12558_figure.jpg|800]]

- **arXiv**: [2610.12558](https://arxiv.org/abs/2610.12558)
- **PDF**: https://arxiv.org/pdf/2610.12558
- **详细分析**: [[20_Research/Papers/强化学习/PanTact_Teaching_Whole-Body_Dexterity_with_a_Wearable_Contact_Interface|PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface]]
- **作者**: Xiaomeng Xu, Han Zhang, Zhian Ruan, Xiaofeng Guo, Jinkun Cao, Ruihan Yang, Carmelo Sferrazza, Shuran Song, Guanya Shi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots have many degrees of freedom and contact surfaces, yet most loco-manipulation research restricts manipulation to the hands and avoids other body contacts with the environment. To extend manipulation beyond the hands, we present PanTact, a system that learns humanoid whole-body dexterity, the capability to manipulate with any suitable body surface, directly from robot-free human demonstrations. Our key idea is to use contact as manipulation-centric information that transfers across embodiments. Contact locations and timing specify the interactions needed to accomplish a task, while the robot chooses how to coordinate its body to realize them within its own physical constraints. Specifically, PanTact captures, learns, and executes whole-body contact via: 1) a wearable, robot-free data collection interface that augments egocentric vision and bimanual UMI grippers with whole-body modular contact patches to record body contact locations and states; 2) a visuomotor policy that mitigates the egocentric observation gap and predicts whole-body contact goals; and 3) contact-aware whole-body control formulations that realize active contact goals using suitable robot surfaces. We deploy PanTact on a Unitree G1 humanoid without additional body contact sensors, demonstrating whole-body dexterity involving body support, pushing, sweeping, and load-sharing. Website: https://pantact.github.io

</details>

---
