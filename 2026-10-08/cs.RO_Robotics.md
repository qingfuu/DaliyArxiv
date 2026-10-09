# cs.RO | Robotics | 2026-10-08

#arxiv #ComputerScience

**论文数**: 43

### [[20_Research/Papers/强化学习/RoboPrompt_Intuitive_Robot_Policy_Steering_with_Sparse_Human_Input|RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input]]

![[assets/2610.10534_figure.png|800]]

- **arXiv**: [2610.10534](https://arxiv.org/abs/2610.10534)
- **PDF**: https://arxiv.org/pdf/2610.10534
- **详细分析**: [[20_Research/Papers/强化学习/RoboPrompt_Intuitive_Robot_Policy_Steering_with_Sparse_Human_Input|RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input]]
- **作者**: Yanwen Zou, Chenyang Shi, Guoxuan Xu, Wenye Yu, Wendi Chen, Ye Pan, Cewu Lu, Chuan Wen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《RoboPrompt: Intuitive Robot Policy Steering with Sparse Human Input》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end robot policies trained through imitation learning remain constrained by limited data diversity, making reliable zero-shot deployment in real-world settings challenging. Shared-autonomy methods enable human correction through teleoperation, but specialized hardware and operator training hinder deployment at scale. Other approaches incorporate human guidance as additional policy inputs, often requiring architectural changes and dedicated training for steerability, which limits their applicability across policies. We present RoboPrompt, a general-purpose, lightweight robot policy steering system that enables users to guide policy behavior through intuitive, sparse inputs, including drawn traces, target points, and coarse directional instructions. RoboPrompt decouples human-intention translation from the underlying policy: a reusable module converts human guidance into action drafts, which are refined through the diffusion or flow-matching dynamics of the base policy. By controlling action generation in noise space, RoboPrompt balances human intent with the policy prior without modifying the base policy architecture or fine-tuning it for steerability. Experiments demonstrate effective steering across Diffusion Policy, $π_{0.5}$, and FastWAM. We further use steered rollouts for online policy improvement through DAgger. After 2-3 rounds of iteration, average success rates increase by 15.5\% for $π_{0.5}$ across three tasks and by 21.3\% across three policies(Diffusion Policy, $π_{0.5}$, FastWAM) on the Insert Bread task, while average human intervention counts decrease by 44.0\% (2.86 to 1.60) and 81.9\% (2.60 to 0.47), respectively.

</details>

---

### [[20_Research/Papers/强化学习/Factorized_Tactile_Representation_and_Control_for_Sim-to-Real_Manipulation|Factorized Tactile Representation and Control for Sim-to-Real Manipulation]]

![[assets/2610.10510_figure.png|800]]

- **arXiv**: [2610.10510](https://arxiv.org/abs/2610.10510)
- **PDF**: https://arxiv.org/pdf/2610.10510
- **详细分析**: [[20_Research/Papers/强化学习/Factorized_Tactile_Representation_and_Control_for_Sim-to-Real_Manipulation|Factorized Tactile Representation and Control for Sim-to-Real Manipulation]]
- **作者**: Siqi Shang, Bianca Aumann, Tye Brady, Joshua Migdal, Taskin Padir
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Factorized Tactile Representation and Control for Sim-to-Real Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet, TactileRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sim-to-real learning must bridge simulated contact and device-specific sensor responses while preserving information needed for control. We propose a factorized tactile representation and control framework that maps normal force and contact patch to an effective contact response recoverable from sensor readings. The response is separated into contact geometry, force distribution, and temporal contact change, with representation-specific encoding and randomization. A Tactile Gated Policy preserves these representations separately through control and operates over all mask configurations without retraining. We evaluate the approach through response reconstruction, spatial alignment, force regulation, and contact-rich adversarial peg insertion in simulation and the real world, enabling the utility and transfer reliability of different tactile representations to be assessed independently. The approach achieves &lt;1 mm contact localization, 1.69 N force-tracking error on unseen geometries, and a 35% improvement in real-world adversarial peg insertion over the unfactorized response, with different tactile representations benefiting different interactions.

</details>

---

### [[20_Research/Papers/具身智能/HuMBLE_Human_Motion-Driven_Behavior_Learning_for_Embodied_Locomotion|HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion]]

![[assets/2610.10489_figure.png|800]]

- **arXiv**: [2610.10489](https://arxiv.org/abs/2610.10489)
- **PDF**: https://arxiv.org/pdf/2610.10489
- **详细分析**: [[20_Research/Papers/具身智能/HuMBLE_Human_Motion-Driven_Behavior_Learning_for_Embodied_Locomotion|HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion]]
- **作者**: Mike Zhang, Dongho Kang, Kevin Bergamin, Nicola Burger, Robin Deits, Jonathan Foster, Bilal Hammoud, Katie Hughes, Francesco Iacobelli, Twan Koolen, M. Eva Mungai, Zach Nobles...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.4（加权：具身智能 2.7，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time steerable, robust, and biomimetic locomotion policies from human data. Using an in-house curated locomotion dataset covering diverse speeds and directions, we first learn a natural locomotion prior policy through a teacher-student distillation process. Specifically, we train a full-body reference-conditioned policy with Reinforcement Learning (RL), then distill it into a lightweight prior policy conditioned solely on proprioception and a planar torso-velocity steering command. Next, we fine-tune the prior policy with multi-task RL to expand command coverage and robustness beyond the data distribution, pairing a goal-conditioned task that tracks arbitrary commands with a reference-guided task that tracks the human data as an explicit style regularizer. We validate our framework on three humanoid robots: the Boston Dynamics Atlas R1, Atlas D1, and Unitree G1. Experimental results demonstrate robust performance across real-world scenarios, including direct user-controlled locomotion in indoor and outdoor environments, and integration as the locomotion layer within hierarchical control stacks. Benchmarks against Tabula Rasa RL policies trained without human data and ablation studies confirm that our framework yields a lightweight, deployable policy that reconstructs coordinated whole-body behavior from a steering command, retaining the human gait characteristics while remaining robust and fully steerable.

</details>

---

### [[20_Research/Papers/机器人/Robotic_Boomerang_Throwing_via_Model-Based_Release_Design|Robotic Boomerang Throwing via Model-Based Release Design]]

![[assets/2610.10472_figure.jpg|800]]

- **arXiv**: [2610.10472](https://arxiv.org/abs/2610.10472)
- **PDF**: https://arxiv.org/pdf/2610.10472
- **详细分析**: [[20_Research/Papers/机器人/Robotic_Boomerang_Throwing_via_Model-Based_Release_Design|Robotic Boomerang Throwing via Model-Based Release Design]]
- **作者**: Yang Liu, Colin Jones, Aude Billard
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Robotic Boomerang Throwing via Model-Based Release Design》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Throwing objects that generate aerodynamic lift can greatly extend robot throwing beyond ballistic flight. A returning boomerang is a challenging example because its flight depends strongly on the release velocity, attitude, and spin, while robotic manipulators cannot readily reproduce the rapid motions used in human throwing. We present a model-based framework for robotic boomerang throwing centered on the release state. We identify the boomerang flight dynamics in stages to predict how flight changes across design variations. To systematically design the robot throwing motion, we screen candidate parameters according to how strongly and consistently they control release spin under uncertain contact conditions. These models are then used to design the throwing motion and boomerang for a 6-DoF manipulator with limited joint speeds. To our knowledge, this is the first robotic manipulator to generate a returning boomerang flight. In the demonstrated returning trial, the boomerang is released at 51 rad/s (8.1 rev/s), reaches 2.03 m from the robot base, and returns to touch down 0.31 m from the base. The successful release differs significantly from the measured human throws, showing that a robot need not imitate human throwing motion to achieve a returning flight. The project page is available at https://robot-boomerang.github.io

</details>

---

### [[20_Research/Papers/机器人/CMP-IRRT_A_Perception-Assisted_Height-Adaptive_Planner_for_Quadruped_Robots|CMP-IRRT*: A Perception-Assisted Height-Adaptive Planner for Quadruped Robots]]

![[assets/2610.10470_figure.png|800]]

- **arXiv**: [2610.10470](https://arxiv.org/abs/2610.10470)
- **PDF**: https://arxiv.org/pdf/2610.10470
- **详细分析**: [[20_Research/Papers/机器人/CMP-IRRT_A_Perception-Assisted_Height-Adaptive_Planner_for_Quadruped_Robots|CMP-IRRT*: A Perception-Assisted Height-Adaptive Planner for Quadruped Robots]]
- **作者**: Mingfan Zhao, Wendong Mao, Zhongfeng Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《CMP-IRRT*: A Perception-Assisted Height-Adaptive Planner for Quadruped Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots can traverse low obstacles, but many 2D planning pipelines still model obstacles as binary occupied regions and rely on sampling-based search that can be inefficient under a limited budget. We propose a perception-assisted height-adaptive planning framework based on CMP-IRRT*, a Channel Mamba PointNet-guided Informed RRT* planner. Given a calibrated top-view RGB observation, the perception module estimates obstacle regions and converts depth predictions into a ground-relative height map. The planner then performs height-conditioned collision checking, treating high obstacles as blocked while allowing low obstacles to be traversed, and uses the CMP guide to bias sampling toward promising regions while retaining standard free-space and informed sampling fallbacks. Experiments on 2D planning benchmarks show that CMP-IRRT* reduces explored nodes and iterations compared with classical and neural-guided baselines, and a controlled ablation supports the contribution of the Mamba-based guide. In constructed traversability-aware scenarios, the proposed planner reduces path length by up to 16.3% when low obstacles are traversable, and a Unitree Go2 demonstration further shows executable bypassing and traversal behaviors. Our code is publicly available at https://github.com/MingfanZhao/height-adaptive-planner.

</details>

---

### [[20_Research/Papers/具身智能/RFPO_Rectified_Flow_Policy_Optimization_for_Embodied_Control|RFPO: Rectified Flow Policy Optimization for Embodied Control]]

![[assets/2610.10453_figure.png|800]]

- **arXiv**: [2610.10453](https://arxiv.org/abs/2610.10453)
- **PDF**: https://arxiv.org/pdf/2610.10453
- **详细分析**: [[20_Research/Papers/具身智能/RFPO_Rectified_Flow_Policy_Optimization_for_Embodied_Control|RFPO: Rectified Flow Policy Optimization for Embodied Control]]
- **作者**: Ting Huang, Lisiyu Pan, Haoyu Wang, Zeyu Zhang, Siyuan Qian, Yanjun Li, Yandong Guo, Boxin Shi, Hao Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《RFPO: Rectified Flow Policy Optimization for Embodied Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based policies provide an expressive framework for continuous robot control, but their iterative ODE integration incurs substantial inference cost. Naively reducing the integration budget can severely degrade control, since policies optimized under full-step execution are not explicitly constrained to remain reliable under coarse numerical integration. We refer to this mismatch as the few-step discretization gap. To address this problem, we introduce RFPO, a flow-policy optimization framework for reliable few-step execution. Reward-aware online Reflow rectifies student-induced transport paths during on-policy learning, making the resulting policy more robust to coarse integration. A frozen Gaussian PPO controller supplies complementary action-space supervision at full and intermediate integration budgets, while the deployed policy remains a single flow student executed with one Euler step. Across Unitree Go2, Boston Dynamics Spot, Unitree H1, and Unitree G1, RFPO consistently preserves full-step control performance under one-step execution, with one-step returns remaining within 2.4% of their corresponding 64-step values across both zero and random initialization. On Unitree Go2, one-step execution retains 98.5% of the 64-step reward while reducing onboard mean inference latency from 4.39 ms to 0.08 ms, yielding a 54.9x speedup. Real-robot experiments further validate stable one-step locomotion. Code: https://github.com/AIGeeksGroup/RFPO. Website: https://aigeeksgroup.github.io/RFPO.

</details>

---

### [[20_Research/Papers/机器人/NeRFifyMesh_Optimizing_Neural_Radiance_Fields_from_Textured_Meshes_for_Robotics_Scene_Building|NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building]]

![[assets/2610.10387_figure.jpg|800]]

- **arXiv**: [2610.10387](https://arxiv.org/abs/2610.10387)
- **PDF**: https://arxiv.org/pdf/2610.10387
- **详细分析**: [[20_Research/Papers/机器人/NeRFifyMesh_Optimizing_Neural_Radiance_Fields_from_Textured_Meshes_for_Robotics_Scene_Building|NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building]]
- **作者**: Nillan Nimal, Mahboubeh Asadi, Sajad Saeedi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《NeRFifyMesh: Optimizing Neural Radiance Fields from Textured Meshes for Robotics Scene Building》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotics, scene representation plays a pivotal role in understanding and interacting with the environment. The advent of Neural Radiance Fields (NeRF) and its variants, as a novel representation, has opened a new frontier of research. In applications such as semantic mapping and simulation, roboticists aim to build scenes using multiple NeRF models, each representing an object. While extensive datasets of 3D mesh models already exist, there is an urgent need to develop tools to convert these assets to NeRF models for rapid algorithm development and testing. This paper presents a new pipeline for converting existing mesh models to NeRF representations by artificially generating a ground truth point-based radiance field through sampling mesh geometry and texture. This approach alleviates the need for camera-based sampling or rendering multi-view images of the original mesh to train the NeRF model. Extensive benchmarking demonstrates that our method yields comparable rendering quality to the baselines. Additionally, the application of this representation is shown by constructing unified NeRF scenes and performing collision simulations with extracted geometry.

</details>

---

### [[20_Research/Papers/具身智能/OpenViTac_Learning_and_Benchmarking_Visuo-Tactile_Policies_in_a_Unified_Sim-and-Real_Framework|OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework]]

![[assets/2610.10384_figure.png|800]]

- **arXiv**: [2610.10384](https://arxiv.org/abs/2610.10384)
- **PDF**: https://arxiv.org/pdf/2610.10384
- **详细分析**: [[20_Research/Papers/具身智能/OpenViTac_Learning_and_Benchmarking_Visuo-Tactile_Policies_in_a_Unified_Sim-and-Real_Framework|OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework]]
- **作者**: Yifan Wu, Qin Li, Nan Min, Guojin Zhong, Haoyu Zhao, Zhiyuan Li, Houze Xu, Shengqi Xu, Xingyao Lin, Zijie Diao, Zhaoxiang Liu, Shiguo Lian...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NeoSim, Real-World, SoftVTBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulation and the real world. OpenViTac organizes contact-rich manipulation into four tactile-relevant capability dimensions and provides paired simulation-real-world settings for consistent evaluation of VLA, WAM, and VTLA policies. Building upon this benchmark, we investigate how different tactile representations and integration strategies affect the performance of pretrained VLA models. Correspondingly, we introduce OpenVTLA, a tactile augmentation framework that combines the best-performing representation and integration strategy. Furthermore, we leverage the paired benchmark setting to study sim-real co-training and analyze factors affecting cross-domain policy learning. Together, OpenViTac provides a unified platform for evaluating and advancing visuo-tactile robot manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Hall_Effect-Based_Tactile_Force_Detection_Sensor_for_Robot-Assisted_Minimally_Invasive_Surgery|Hall Effect-Based Tactile Force Detection Sensor for Robot-Assisted Minimally Invasive Surgery]]

![[assets/2610.10346_figure.png|800]]

- **arXiv**: [2610.10346](https://arxiv.org/abs/2610.10346)
- **PDF**: https://arxiv.org/pdf/2610.10346
- **详细分析**: [[20_Research/Papers/具身智能/Hall_Effect-Based_Tactile_Force_Detection_Sensor_for_Robot-Assisted_Minimally_Invasive_Surgery|Hall Effect-Based Tactile Force Detection Sensor for Robot-Assisted Minimally Invasive Surgery]]
- **作者**: Charles DeLorey, Michael Brockdorff, Adam Metcalf, Benjamin Calmé, Pietro Valdastri, Dominic Jones
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Hall Effect-Based Tactile Force Detection Sensor for Robot-Assisted Minimally Invasive Surgery》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic minimally invasive surgery has revolutionized surgical practice. However, as the surgeons are mechanically separated from the surgical tools, loss of tactile feedback occurs. We present a compact force sensor with three, millimeter scale sensing elements (taxels) that can be affixed to the grasping face of a robotic surgical tool. The sensor features a miniaturized design using Hall effect sensors and magnets embedded in a deformable elastomer contact layer. Sensor calibration is achieved with a 6 degree of freedom (DoF) parallel robot. Each taxel can detect applied normal and shear forces with average RMSE of 2.133 kPa. The calibrated sensor was validated on phantom and ex vivo porcine tissue, demonstrating tactile sensing during retraction as well as slip. This work introduces a small-scale Hall effect based tactile sensor, enabling sensing for force-sensitive robotic surgical applications.

</details>

---

### [[20_Research/Papers/具身智能/Benchmarking_Behavioral_Steerability_in_Behavior_Foundation_Models|Benchmarking Behavioral Steerability in Behavior Foundation Models]]

![[assets/2610.10198_figure.png|800]]

- **arXiv**: [2610.10198](https://arxiv.org/abs/2610.10198)
- **PDF**: https://arxiv.org/pdf/2610.10198
- **详细分析**: [[20_Research/Papers/具身智能/Benchmarking_Behavioral_Steerability_in_Behavior_Foundation_Models|Benchmarking Behavioral Steerability in Behavior Foundation Models]]
- **作者**: Minghe Gao, Zhanxi Yan, Jiahui Liu, Wendong Bu, Xiaoting Chen, Qizhou Wang, Yi Su, Siliang Tang, Jun Xiao, Yueting Zhuang, Tat-Seng Chua, Juncheng Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Benchmarking Behavioral Steerability in Behavior Foundation Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HumanoidBench, Meta-World, Mimicking-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavior Foundation Models (BFMs) are emerging as a paradigm for translating human intentions into executable humanoid behaviors. As these models evolve beyond behavior generation toward general-purpose behavioral systems, a fundamental question arises: can they be reliably steered according to user intentions? In this paper, we introduce the concept of behavioral steerability, defined as the ability of BFMs to faithfully generate behaviors that satisfy user-specified intentions. To study this capability, we present RoboSteer, the first benchmark for behavioral steerability in BFMs. RoboSteer organizes behavioral steerability into a three-level hierarchy-Conditional Steering, Constraint Steering, and Compositional Steering-and establishes a unified evaluation framework supported by a large-scale multimodal motion corpus. Using RoboSteer, we conduct the first large-scale empirical study of behavioral steerability across 9 existing BFMs. We view behavioral steerability as more than a capability for controlling motion: it concerns how embodied systems translate human intentions into purposeful actions. We hope RoboSteer will advance research on intention realization as a foundation for general-purpose embodied intelligence.

</details>

---

### [[20_Research/Papers/机器人/Design_of_a_Fully_Actuated_4-DOF_Robotic_Finger_With_Joint-Specific_Hybrid_Remote_Actuation|Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation]]

![[assets/2610.10180_figure.png|800]]

- **arXiv**: [2610.10180](https://arxiv.org/abs/2610.10180)
- **PDF**: https://arxiv.org/pdf/2610.10180
- **详细分析**: [[20_Research/Papers/机器人/Design_of_a_Fully_Actuated_4-DOF_Robotic_Finger_With_Joint-Specific_Hybrid_Remote_Actuation|Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation]]
- **作者**: Hyojae Kang, Hyun-mok Jung, Joonho Lee, Dongil Park, Hyunmin Do, Jongwoo Park, Jeongdo Ahn
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a fully actuated 4-DOF robotic finger using a joint-specific hybrid remote-actuation architecture. The metacarpophalangeal (MCP) joint is driven by two coordinated rigid-link transmission sets, whereas the proximal interphalangeal (PIP) and distal interphalangeal (DIP) joints are independently actuated by closed-loop wire transmissions incorporating circular rolling-contact joints (RCJs). A larger transmission radius is used at the PIP joint than at the DIP joint. The RCJ wire geometry maintains the total wire-loop length during joint rotation, and the DIP wire routing is designed so that PIP motion does not affect its differential actuation for a fixed MCP configuration. The distal wire transmission, MCP linkage, and fingertip kinematics are analytically modeled. In experiments, the transmission behavior was quantitatively evaluated from the ball-screw displacements measured using ArUco-marker tracking. MCP actuation produced measurable displacements of the PIP and DIP transmission units, whereas isolated PIP and DIP actuation with the MCP fixed supported the intended mechanical decoupling between the distal transmissions. The mean peak fingertip forces under isolated MCP, PIP, and DIP actuation were 21.28 N, 9.22 N, and 5.75 N, respectively. The resulting finger postures were also examined using objects of different geometries and sizes.

</details>

---

### [[20_Research/Papers/具身智能/Do_Vision-Language-Action_Models_Understand_Instructions_A_Mechanistic_Interpretability_Study_on_Language_Grounding|Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding]]

![[assets/2610.10178_figure.png|800]]

- **arXiv**: [2610.10178](https://arxiv.org/abs/2610.10178)
- **PDF**: https://arxiv.org/pdf/2610.10178
- **详细分析**: [[20_Research/Papers/具身智能/Do_Vision-Language-Action_Models_Understand_Instructions_A_Mechanistic_Interpretability_Study_on_Language_Grounding|Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding]]
- **作者**: Theodor Wulff, Angelo Cangelosi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.5，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their Vision-Language model backbones. For this reason, we conduct a controlled mechanistic interpretability study on the language grounding capabilities of two state-of-the-art Vision-Language-Action models, $π_{0.5}$ and GR00T N1.7, by applying activation and attribution patching to the residual stream of the action generation modules. We systematically corrupt the task instruction of input samples of the LIBERO benchmark following five strategies: synonym replacement, semantic scaling, directional corruption, random object substitution, and empty string. Our experiments find that both models are comparatively insensitive to abstract rephrasing and to referencing non-existent objects, but react strongly to empty task descriptions and, especially, to directional language. During action generation, this sensitivity is concentrated in different loci for each model: mainly in the early, periodic cross-attention layers for GR00T N1.7, versus distributed across the earliest and selected later layers for $π_{0.5}$. For GR00T N1.7, directional perturbations drive some of the largest causal effects while leaving the internal representational geometry comparatively unchanged, a dissociation we do not observe clearly for $π_{0.5}$. Finally, the reliability of attribution patching is model-dependent: it closely tracks activation patching for GR00T N1.7 but not for $π_{0.5}$.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Motion_Planning_for_Multi-Robot_Systems_under_Topological_Constraints|Distributed Motion Planning for Multi-Robot Systems under Topological Constraints]]

![[assets/2610.10065_figure.png|800]]

- **arXiv**: [2610.10065](https://arxiv.org/abs/2610.10065)
- **PDF**: https://arxiv.org/pdf/2610.10065
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Motion_Planning_for_Multi-Robot_Systems_under_Topological_Constraints|Distributed Motion Planning for Multi-Robot Systems under Topological Constraints]]
- **作者**: Gianpietro Battocletti, Dimitris Boskos, Dimos V. Dimarogonas, Bart De Schutter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Distributed Motion Planning for Multi-Robot Systems under Topological Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient and distributed coordination of mobile robots is one of the main challenges in multi-robot systems. Topological constraints, often expressed as topological braids, are a popular tool to encode complex coordination patterns between multiple mobile robots, as they offer a compact and abstract representation of the desired qualitative relation between the space-time trajectories of the robots. However, execution of joint motion plans encoded as braid-based topological constraints via distributed controllers is challenging, with existing approaches, generally based on the execution of one braid generator at a time, producing slow and suboptimal trajectories. We propose a distributed controller based on Model Predictive Control (MPC) to efficiently execute braid-based topological specifications. Rather than directly tracking the braid specification, we propose to use winding numbers, which are topological invariants for braids, as a proxy. This has the twofold benefit of converting braids into a continuous function, which can be easily tracked by an MPC controller through an appropriate term in the cost function, and of decoupling the global braid specification into a set of pairwise specifications, which can be tracked distributedly through the solution of only local MPC problems. To maintain global coordination, we propose a consensus-based progress estimation approach, which allows the robots to synchronize their motion toward the desired specification. We validate the proposed approach in simulation and in real-world experiments, where we demonstrate the effectiveness of the proposed approach and the improvement over existing approaches in terms of execution speed and control effort.

</details>

---

### [[20_Research/Papers/具身智能/Decoding_Neural_Population_Dynamics_through_Robotic_Analog|Decoding Neural Population Dynamics through Robotic Analog]]

![[assets/2610.09977_first_page.png|800]]

- **arXiv**: [2610.09977](https://arxiv.org/abs/2610.09977)
- **PDF**: https://arxiv.org/pdf/2610.09977
- **详细分析**: [[20_Research/Papers/具身智能/Decoding_Neural_Population_Dynamics_through_Robotic_Analog|Decoding Neural Population Dynamics through Robotic Analog]]
- **作者**: Wenhui Chen, Jiyue Tao, Yitao Cheng, Yutong Shi, Feitian Zhang, Xitong Liang, Ke Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Decoding Neural Population Dynamics through Robotic Analog》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Animal evidence shows that precise voluntary movements arise from rotational neural population dynamics in motor cortex, but their physical effects remain unknown. We developed a robotic analog of biological motor systems with artificial muscles, multimodal sensors, and a neural network controller trained via reinforcement learning. The robotic analog exhibited accurate movements, robustness to damage, and neural population dynamics akin to animals. This task-driven, embodied model illuminates the causal link between neural population dynamics and motor outcomes. We discovered that neural rotations generate oscillatory maneuvers orthogonal to the reaching direction, optimizing trajectory adjustments, which is confirmed by primate neural data. The model also revealed counterintuitive neural energy principles under sensor and motor redundancies, and striking Eureka moments during motor learning, bridging biological and artificial systems. These findings provide new perspectives on how neural dynamics contribute to accurate and flexible movement, inspiring future intelligent robots with animal-like mobility.

</details>

---

### [[20_Research/Papers/具身智能/Borrowed_Eyes_Markerless_Nano-UAV_Flight_with_an_Active_Quadruped_Observer|Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer]]

![[assets/2610.09967_figure.png|800]]

- **arXiv**: [2610.09967](https://arxiv.org/abs/2610.09967)
- **PDF**: https://arxiv.org/pdf/2610.09967
- **详细分析**: [[20_Research/Papers/具身智能/Borrowed_Eyes_Markerless_Nano-UAV_Flight_with_an_Active_Quadruped_Observer|Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer]]
- **作者**: Alejandro Lorite Mora, Dimitrios Arapis, Andrés Faíña
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.8（加权：具身智能 1.5，机器人 2.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Borrowed Eyes: Markerless Nano-UAV Flight with an Active Quadruped Observer》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nano unmanned aerial vehicles (nano-UAVs) can navigate confined spaces that larger robots cannot, but their payload capacity severely limits the sensors and compute available for self-localization in global navigation satellite system (GNSS)-denied environments. We present a vision-based system that localizes a nano-UAV from a quadruped robot with an arm-mounted camera. The quadruped tracks the drone, estimates its position in its own coordinate system using segmentation masks and depth, and transmits that position over a real-time radio link. To ensure continuous tracking, we developed a perception-aware nonlinear Model Predictive Controller (NMPC) that dynamically adjusts the quadruped's body and arm to maximize the drone's visibility, treating observation reliability as a primary control objective. Relying solely on this external estimate, the nano-UAV executed predefined trajectories from takeoff to landing with a median 3D localization error of 59 mm. The system demonstrates robustness against short visual occlusions by smoothly transitioning to onboard inertial flight when line-of-sight is temporarily lost. Ultimately, this framework allows a quadruped to offload the localization burden of a nano-UAV, enabling inspection of complex spaces that neither robot could navigate alone.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Accurate_End-Effector_Localization_for_UMI-Style_Robotic_Manipulation_Teaching|Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching]]

![[assets/2610.09857_figure.png|800]]

- **arXiv**: [2610.09857](https://arxiv.org/abs/2610.09857)
- **PDF**: https://arxiv.org/pdf/2610.09857
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Accurate_End-Effector_Localization_for_UMI-Style_Robotic_Manipulation_Teaching|Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching]]
- **作者**: Junjie Zhang, Deteng Zhang, Zhisong Xu, Bo Sun, Liuyang Li, Yihong Tian, Jie Yin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 1.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Towards Accurate End-Effector Localization for UMI-Style Robotic Manipulation Teaching》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MILD-Sim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstration learning requires accurate and temporally complete end-effector localization during close-range manipulation and camera occlusion. Existing SLAM benchmarks emphasize navigation motions, whereas manipulation datasets prioritize policy learning over localization evaluation. We introduce MILD, a Manipulation-Interface Localization Dataset with real-world and simulation sequences. The real-world subset provides 86 sensor sequences from Insta360 X5 and Insight9 across 15 repeated tabletop tasks, calibration assets, and a per-execution robot end-effector reference trajectory. The simulation subset, MILD-Sim, extends task coverage in Isaac Sim for controlled manipulation-replay studies. Benchmarking visual-inertial and fiducial-aided systems on instrumented real-world recordings reveals large differences in both TCP-relative trajectory error and temporal coverage, even under the same nominal task. To support marker-augmented teaching workspaces without a pre-surveyed fiducial map, we present AprilVINS, which combines fisheye visual-inertial estimation with sequence-local AprilTag geometry and separates prior admission from guarded export of the jointly optimized state. On Insta360 AprilTag4 recordings, AprilVINS(full) under a unified protocol with sequence-specific profiles reaches millimeter-level SE(3)-aligned TCP-relative APE RMSE with high time completion and lower reported error than the tested routes under their respective protocols, whereas fisheye VIO without tag factors remains at centimeter scale. Ablations separate accuracy from exportability, and a MILD-Sim replay study provides task-specific tolerance references for interpreting those error magnitudes. Together, MILD and AprilVINS provide a diagnostic benchmarking framework for UMI-style demonstration collection. Code, datasets, and evaluation manifests will be released upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/Enhancing_Robotic_Perception_and_Adaptability_through_Sensor_Fusion_and_Origami-Inspired_Designs|Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs]]

![[assets/2610.09828_figure.png|800]]

- **arXiv**: [2610.09828](https://arxiv.org/abs/2610.09828)
- **PDF**: https://arxiv.org/pdf/2610.09828
- **详细分析**: [[20_Research/Papers/具身智能/Enhancing_Robotic_Perception_and_Adaptability_through_Sensor_Fusion_and_Origami-Inspired_Designs|Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs]]
- **作者**: Namai Chandra, Jaison Jose, Kavi Arya, Shivaram Kalyanakrishnan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Enhancing Robotic Perception and Adaptability through Sensor Fusion and Origami-Inspired Designs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compact mobile robots must recover scene geometry under changing lighting and surface texture while working within tight payload and cost limits. We present a compact mobile robot that uses origami-inspired wheels for locomotion and active control of its sensing geometry. As the wheels move between terrain-adaptive configurations, the changing chassis pitch sweeps a 2D LiDAR through intermediate elevations; held wheel positions provide a chosen viewing angle. An IMU accounts for chassis attitude, and a fusion node projects LiDAR returns into the RGB-D depth stream supplied to RTAB-Map. The arrangement uses the wheel actuation already present on a sub-300 USD, sub-2 kg prototype to extend the scanner's viewing geometry. We assess depth fusion in a textureless indoor corridor and an outdoor sunlit area, with three runs per sensor configuration in each setting. Mean full-frame invalid-depth fractions fell from 21% to 11% indoors and from 48% to 18% outdoors. The prototype combines improved depth coverage with a continuously adjustable LiDAR viewpoint using the same actuation that reconfigures its wheels.

</details>

---

### [[20_Research/Papers/机器人/On-Demand_Robotic_Assembly_via_Differentiable_Geometric_Part_Repair|On-Demand Robotic Assembly via Differentiable Geometric Part Repair]]

![[assets/2610.09777_figure.png|800]]

- **arXiv**: [2610.09777](https://arxiv.org/abs/2610.09777)
- **PDF**: https://arxiv.org/pdf/2610.09777
- **详细分析**: [[20_Research/Papers/机器人/On-Demand_Robotic_Assembly_via_Differentiable_Geometric_Part_Repair|On-Demand Robotic Assembly via Differentiable Geometric Part Repair]]
- **作者**: Millicent Schlafly, Fabio Schaub, Diogo Costa Pais, Luca Lelli, Janne Dvorak, Claire Colmont, Sven Marti, Mark D. Fuge
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《On-Demand Robotic Assembly via Differentiable Geometric Part Repair》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Blox-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transitioning from a digital design to a robotic assembly process currently requires months of expert manual tuning to reconcile part geometries with robotic constraints. This paper presents an end-to-end, autonomous pipeline for the design and physical construction of bespoke wooden assemblies. A generative AI agent translates user prompts into initial 3D geometries, balancing the visual fidelity of the design with select physical constraints. The assemblability of the design is further improved by a gradient-based repair stage that backpropagates through a graph attention network surrogate to adjust component geometries. In addition to correcting for disjointed and overlapping components, we demonstrate hardware-specific corrections, differentiably optimizing the geometry of components to enable robot screwdriving for 86.7% of 60 novel natural language inputs, significantly outperforming prior work by a factor of ten. For ten of the structures, we physically demonstrate assemblability with two UR5e robots. This work marks a meaningful step toward on-demand robotic manufacturing, enabling the rapid production of customized, low-volume goods.

</details>

---

### [[20_Research/Papers/具身智能/ΔWAM_Distilling_Action_Tangent_Fields_into_World_Action_Models|ΔWAM: Distilling Action Tangent Fields into World Action Models]]

![[assets/2610.09734_figure.png|800]]

- **arXiv**: [2610.09734](https://arxiv.org/abs/2610.09734)
- **PDF**: https://arxiv.org/pdf/2610.09734
- **详细分析**: [[20_Research/Papers/具身智能/ΔWAM_Distilling_Action_Tangent_Fields_into_World_Action_Models|ΔWAM: Distilling Action Tangent Fields into World Action Models]]
- **作者**: Ke Wu, Hanwen Huang, Bo Gu, Kaizhao Zhang, Xiangting Meng, Yupeng Zheng, Zijun Xu, Jieru Zhao, Wenchao Ding
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.3（加权：具身智能 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《ΔWAM: Distilling Action Tangent Fields into World Action Models》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ABot-PhysWorld, Ctrl-World, Pelican-Sim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAM) improve robot policies by augmenting sparse action supervision with dense future prediction. However, much of the predictable future is dominated by appearance and scene persistence rather than action-dependent dynamics. We observe that several recent WAM designs, including optical flow, motion-centric representations, and latent actions, can be understood from a common perspective in which world supervision becomes more efficient as it contains a higher proportion of action-relevant variation. Based on this insight, we introduce Action Tangent Fields, which reformulate world supervision through a local Taylor expansion of how actions induce changes in future dynamics. We represent future dynamics in Residual-VAE space, where the future latent remains recoverable from the current latent and its residual, and use a strong action-conditioned world model (ACWM) to probe the local correspondence between action variations and residual-world variations. This local first-order structure is distilled into the WAM to guide its denoising supervision toward dynamics that are more tightly coupled to action, rather than merely predictable from appearance. Across LIBERO-Plus, RoboTwin, and RoboTwin2.0-Plus, our method consistently improves robustness to lighting, background, camera, layout, and other environmental perturbations. Despite using no large-scale embodied pretraining, it achieves stronger robustness under several distribution shifts than pretrained policies. We further distill multi-step VideoDiT denoising into a single step for efficient inference. Our results suggest that effective WAM supervision should remain information-rich while concentrating its predictive capacity on the directions along which actions change the future.

</details>

---

### [[20_Research/Papers/具身智能/RoboPace_Contact-Aware_Time-Optimal_Retiming_for_Action-Chunk_Policies|RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies]]

![[assets/2610.09696_figure.png|800]]

- **arXiv**: [2610.09696](https://arxiv.org/abs/2610.09696)
- **PDF**: https://arxiv.org/pdf/2610.09696
- **详细分析**: [[20_Research/Papers/具身智能/RoboPace_Contact-Aware_Time-Optimal_Retiming_for_Action-Chunk_Policies|RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies]]
- **作者**: Mimo Shirasaka, Takehiko Ohkawa, Takuya Okubo, Nicola Scianca, Tatsuya Matsushima, Kei Ota
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TempoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation data collection has been shifting from teleoperation toward robot-free demonstrations, through interfaces such as the Universal Manipulation Interface (UMI) or directly from human hands. Vision-Language-Action (VLA) policies trained on such data inherit the demonstrator's timing. Yet human timing does not directly transfer to robots: compliant hands tolerate fast contact, whereas robots may overshoot due to actuator and tracking limitations; conversely, robots can move faster in free space. This motivates a unified approach that reconciles execution speed with contact safety. We present RoboPace, an online retiming layer that preserves the policy's geometric path while adapting its timing, respecting the target robot's kinematic and dynamic constraints. It adapts execution speed based on predicted contact, jointly accounting for contact-dependent speed limits and the robot's motion constraints. The method requires no policy retraining and operates in real time. Across three contact-rich tasks on a dual-arm robot, faster uniform execution and physical-limit-only retiming largely fail. RoboPace instead achieves higher overall success than slow uniform execution while completing four of five commands in approximately half the time, retaining the reliability of slow execution without its time cost.

</details>

---

### [[20_Research/Papers/具身智能/Fast_and_Robust_Teach-and-Repeat_Navigation_Using_MixVPR_Visual_Place_Recognition|Fast and Robust Teach-and-Repeat Navigation Using MixVPR Visual Place Recognition*]]

![[assets/2610.09631_figure.png|800]]

- **arXiv**: [2610.09631](https://arxiv.org/abs/2610.09631)
- **PDF**: https://arxiv.org/pdf/2610.09631
- **详细分析**: [[20_Research/Papers/具身智能/Fast_and_Robust_Teach-and-Repeat_Navigation_Using_MixVPR_Visual_Place_Recognition|Fast and Robust Teach-and-Repeat Navigation Using MixVPR Visual Place Recognition*]]
- **作者**: Václav Truhlařík, Tomáš Pivoňka, Libor Přeučil
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Fast and Robust Teach-and-Repeat Navigation Using MixVPR Visual Place Recognition*》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D2-Net, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teach-and-repeat navigation systems employing advanced visual place recognition techniques for localization exhibit key attributes for long-term mobile robot navigation, such as the ability to operate in unstructured and dynamic environments. However, existing solutions based on deep-learning techniques are computationally demanding, limiting their applicability. This work introduces a novel and efficient teach-and-repeat system built on the modern visual place recognition method MixVPR. Real-world testing demonstrated its ability to operate both indoors and outdoors, achieving robustness and navigation precision comparable to other state-of-the-art systems. In addition, its lower hardware requirements make it suitable for a wide range of robotic platforms and practical applications.

</details>

---

### [[20_Research/Papers/具身智能/Targeted_Modality_Dropout_for_Real-Robot_Manipulation_Robust_to_Intermittent_Vision_Loss|Targeted Modality Dropout for Real-Robot Manipulation Robust to Intermittent Vision Loss]]

![[assets/2610.09566_figure.png|800]]

- **arXiv**: [2610.09566](https://arxiv.org/abs/2610.09566)
- **PDF**: https://arxiv.org/pdf/2610.09566
- **详细分析**: [[20_Research/Papers/具身智能/Targeted_Modality_Dropout_for_Real-Robot_Manipulation_Robust_to_Intermittent_Vision_Loss|Targeted Modality Dropout for Real-Robot Manipulation Robust to Intermittent Vision Loss]]
- **作者**: Genki Shikada, Kazuki Osamura, Masaru Ide, Tetsuya Ogata, Kanata Suzuki
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Targeted Modality Dropout for Real-Robot Manipulation Robust to Intermittent Vision Loss》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning policies that integrate multiple sensory modalities are prone to overreliance on a dominant modality, such as vision, during training, which can disrupt policy execution when that modality is lost at inference time. In this paper, we introduce Targeted Modality Dropout (TMD), in which the dependence on each modality is estimated using attention and the most dominant modality is selectively dropped. This is combined with entropy regularization over the dependence distribution. Through real-robot evaluation using a bimanual manipulator, we show that under vision loss the success rate of the baseline policy drops substantially, whereas TMD sustains task execution. In contrast, a conventional dropout that selects the dropped modality at random, without the entropy regularization, fails on many tasks even without vision loss.

</details>

---

### [[20_Research/Papers/具身智能/MagCilia_A_Compact_Magnetociliary_Tactile_Sensor_with_3D_Force_Sensing_for_Robotic_Contact_Perception_and_Grasping_Feedback|MagCilia: A Compact Magnetociliary Tactile Sensor with 3D Force Sensing for Robotic Contact Perception and Grasping Feedback]]

![[assets/2610.09536_figure.png|800]]

- **arXiv**: [2610.09536](https://arxiv.org/abs/2610.09536)
- **PDF**: https://arxiv.org/pdf/2610.09536
- **详细分析**: [[20_Research/Papers/具身智能/MagCilia_A_Compact_Magnetociliary_Tactile_Sensor_with_3D_Force_Sensing_for_Robotic_Contact_Perception_and_Grasping_Feedback|MagCilia: A Compact Magnetociliary Tactile Sensor with 3D Force Sensing for Robotic Contact Perception and Grasping Feedback]]
- **作者**: Yu Feng, Hao Wu, Haotian Guo, Haoming Liu, William Su, Jingxiang Guo, Jiankun Li, Masayoshi Tomizuka, Wen Jung Li, Jianshu Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MagCilia: A Compact Magnetociliary Tactile Sensor with 3D Force Sensing for Robotic Contact Perception and Grasping Feedback》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic grasping and surface exploration benefit from simultaneous measurement of normal and tangential forces and from surface information obtained through contact. Here, we present a compact magnetociliary tactile sensor (MagCilia) that combines a flexible magnetic-cilia structure with a Hall sensor for 3D force sensing. Quasi-static finite element analysis is used to investigate structural deformation and magnetic responses under multidirectional loading. To reconstruct forces from the coupled magnetic channels, we propose causal history fusion regression (CHFR), which combines current magnetic-field measurements with their recent changes. Five-fold cross-validation grouped by calibration record yields root-mean-square errors of 0.40, 0.57, and 0.69 N for Fx, Fy, and Fz, respectively, with corresponding coefficients of determination of 0.93, 0.90, and 0.92. Robotic experiments demonstrate tangential-force-guided gripper adjustment and multi-axis load monitoring under external perturbations. Frequency-domain features of the reconstructed forces distinguish six surface categories with 99.39% accuracy in three-fold cross-validation grouped by acquisition session. An online robotic demonstration additionally identifies all six tested surfaces. These results demonstrate 3D force reconstruction, grasping feedback, and surface recognition using a single compact tactile unit.

</details>

---

### [[20_Research/Papers/具身智能/Precise_SE(3)_End-Effector_Tracking_in_Whole-Body_Humanoid_Control|Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control]]

![[assets/2610.09479_first_page.png|800]]

- **arXiv**: [2610.09479](https://arxiv.org/abs/2610.09479)
- **PDF**: https://arxiv.org/pdf/2610.09479
- **详细分析**: [[20_Research/Papers/具身智能/Precise_SE(3)_End-Effector_Tracking_in_Whole-Body_Humanoid_Control|Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control]]
- **作者**: Joohwan Seo, Xiaofeng Guo, Jinkun Cao, Roberto Horowitz, Rocky Duan, Guanya Shi, Koushil Sreenath
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Precise SE(3) End-Effector Tracking in Whole-Body Humanoid Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise end-effector tracking during humanoid whole-body motion is challenging due to floating-base oscillations, gravity, dynamic coupling, and locomotion-induced disturbances. We propose ResGAC, a whole-body humanoid controller for precise end-effector pose tracking that combines geometric admittance control (GAC) with residual reinforcement learning. GAC provides structured $\SE$ task-space feedback and generates nominal arm joint-position targets, while residual RL compensates for unmodeled dynamics and coordinates locomotion and balance in the shared joint-position action space. The left-invariant geometric formulation allows the same GAC law to be used across manipulation reference frames. This enables the use of a ground-attached heading frame that preserves planar locomotion while removing pelvis roll, pitch, and heave from the manipulation reference, thereby reducing reference-induced end-effector motion during locomotion. ResGAC is validated on a real Unitree G1 humanoid. Across four standing end-effector tracking benchmarks, ResGAC consistently outperforms representative baselines, including SONIC, achieving lower translational and rotational errors. Real-world experiments further demonstrate reduced propagation of pelvis motion to the desired end-effector pose using the proposed ground-attached heading frame. ResGAC achieves $90\%$ success in a standing peg-in-hole task compared with $50\%$ for SONIC, and accurate world-frame $\SE$ end-effector pose tracking during lower-body motion. Experimental videos are included in the supplementary material and are also available on the project website: https://resgac.github.io/ResGAC-website/.

</details>

---

### [[20_Research/Papers/具身智能/TMT_Runtime_Backdoor_Detection_for_Vision-Language-Action_Policies_on_Unseen_Tasks|TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks]]

![[assets/2610.09462_figure.png|800]]

- **arXiv**: [2610.09462](https://arxiv.org/abs/2610.09462)
- **PDF**: https://arxiv.org/pdf/2610.09462
- **详细分析**: [[20_Research/Papers/具身智能/TMT_Runtime_Backdoor_Detection_for_Vision-Language-Action_Policies_on_Unseen_Tasks|TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks]]
- **作者**: Zirun Zhou, Jingfeng Zhang, HaoChuan Xu, Xizhe Zhang, Elliott Wen, Jing Sun, Hong Jia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.3（加权：具身智能 1.8，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, RL, WorldModel

#### 研究背景与动机

《TMT: Runtime Backdoor Detection for Vision-Language-Action Policies on Unseen Tasks》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BadVLA, DropVLA, OpenVLA, TrustVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Backdoored vision-language-action (VLA) policies can preserve benign task performance while producing malicious actions when a trigger appears. Detecting such activation is difficult because malicious behavior can comprise individually plausible actions, while unfamiliar tasks introduce legitimate changes in observations and behavior. We introduce TMT, a runtime backdoor detector based on Token Manifold and latent Transition modeling. Trained on benign rollouts, its two branches assess input-token structure and prediction errors in adjacent-layer latent dynamics. A suspicious rollout identified by the token manifold branch, once confirmed through latent deviations, guides transition selection for subsequent monitoring. We further explore policy purification through self-distillation: a frozen copy of the backdoored policy provides benign-input actions to supervise a student on paired benign and triggered observations, without requiring a separate clean reference policy. For evaluation, we adapt traditional backdoor detectors and repurpose anomaly and failure detection methods as VLA backdoor detectors. In a post-hoc comparison with ten baselines, TMT achieves state-of-the-art backdoor detection performance on unseen tasks across three VLA backdoor attacks. Our project page is available at https://zzr42.github.io/tmt/.

</details>

---

### [[20_Research/Papers/具身智能/RobotAPO_Adversarial_Physics_Preference_Optimization_for_Robotic_Manipulation_Video_Generation|RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation]]

![[assets/2610.09454_first_page.png|800]]

- **arXiv**: [2610.09454](https://arxiv.org/abs/2610.09454)
- **PDF**: https://arxiv.org/pdf/2610.09454
- **详细分析**: [[20_Research/Papers/具身智能/RobotAPO_Adversarial_Physics_Preference_Optimization_for_Robotic_Manipulation_Video_Generation|RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation]]
- **作者**: Kerui Li, Zhe Jing, Chenyi Huang, Xiaofeng Wang, Zheng Zhu, Haoming Cui, Huaibo Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation videos are increasingly used as visual plans for embodied agents, but optimizing purely for visual plausibility often fails to capture the fragile physical manifold of real-world interactions. Even minor physics-violating errors at the interaction boundary, such as interpenetration or premature object motion, can completely invalidate the inferred timing and pose needed for downstream execution. Because standard supervised fine-tuning lacks the direct pressure to penalize these localized failures, we introduce AgiBot-PhysPref. This rigorously curated 10,000-sample preference dataset isolates condition-matched physics violations, turning the generator's own failure distribution into a foundational signal for physical consistency. Building upon this, we propose RobotAPO, an adversarial physics preference optimization framework operating in the continuous flow-matching denoising space. To prevent the policy from merely memorizing static curated failures, RobotAPO employs a lightweight adversarial counterfactual proposer that learns a condition-dependent, physical-failure-biased direction in denoising space. This encourages the model to explore and better respect the physical interaction boundary, all while maintaining a pure prompt-and-reference inference interface without requiring external structural conditioning. Comprehensive evaluations demonstrate that explicitly correcting these localized physics violations improves downstream robot execution from generated videos. On held-out AgiBot conditions, RobotAPO outperforms the strongest controlled internal baseline in physical consistency by 6.8% hard score and 10.0% soft score. Crucially, in real-robot replay, it translates these physical-consistency gains into a 37.4% relative improvement in task success over the strongest controlled internal baseline.

</details>

---

### [[20_Research/Papers/具身智能/TempoBridge_Language-Guided_Tempo_Control_for_Vision-Language-Action_Policies|TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies]]

![[assets/2610.09451_figure.png|800]]

- **arXiv**: [2610.09451](https://arxiv.org/abs/2610.09451)
- **PDF**: https://arxiv.org/pdf/2610.09451
- **详细分析**: [[20_Research/Papers/具身智能/TempoBridge_Language-Guided_Tempo_Control_for_Vision-Language-Action_Policies|TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies]]
- **作者**: Yeonseo Lee, Hyosup Shin, Guebin Hwang, Sungho Jo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CTRL, Real-World, TempoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextual VLM representations, aligns them with task progress through a causal phase router, and modulates nominal motion commands during execution. Across LIBERO tasks, TempoBridge improves Tempo Success Rate from 52.6% to 89.7% under canonical tempo instructions while retaining high task success. It also preserves near-baseline performance when no tempo cue is present and generalizes to unseen tempo expressions without additional training. Experiments on a physical robot further demonstrate language-conditioned tempo modulation in real-world manipulation.

</details>

---

### [[20_Research/Papers/大模型/IVG-UAV_An_Intelligent_Voice-Guided_UAV_System_for_Autonomous_Ripe_Fruit_Harvesting_with_Vision-Based_Classification_and_Adaptive_Path_Plann|IVG-UAV: An Intelligent Voice-Guided UAV System for Autonomous Ripe Fruit Harvesting with Vision-Based Classification and Adaptive Path Planning]]

![[assets/2610.09398_figure.png|800]]

- **arXiv**: [2610.09398](https://arxiv.org/abs/2610.09398)
- **PDF**: https://arxiv.org/pdf/2610.09398
- **详细分析**: [[20_Research/Papers/大模型/IVG-UAV_An_Intelligent_Voice-Guided_UAV_System_for_Autonomous_Ripe_Fruit_Harvesting_with_Vision-Based_Classification_and_Adaptive_Path_Plann|IVG-UAV: An Intelligent Voice-Guided UAV System for Autonomous Ripe Fruit Harvesting with Vision-Based Classification and Adaptive Path Planning]]
- **作者**: Dinh Trung Duong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.1，机器人 1.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《IVG-UAV: An Intelligent Voice-Guided UAV System for Autonomous Ripe Fruit Harvesting with Vision-Based Classification and Adaptive Path Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In tropical regions, their agricultural sectors remain highly dependent on manual labor for fruit harvesting. On large-scale farms, this dependency often results in significant labor cost and logistic complexities. This project presents the development and simulation of a voice-controlled Unmanned Aerial Vehicle (UAV) system designed to automate harvesting tasks in extensive plantations. The proposed system integrates speech recognition using Whisper [1] and LLM, computer vision-based ripeness classification, and adaptive path planning within a unified framework. The entire system is modeled and validated in a Gazebo simulation environment, allowing performance evaluation under controlled agricultural scenarios

</details>

---

### [[20_Research/Papers/具身智能/COOL_Curiosity-Driven_Object_Ownership_Learning_for_Personalized_Robotic_Assistance|COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance]]

![[assets/2610.09358_figure.jpg|800]]

- **arXiv**: [2610.09358](https://arxiv.org/abs/2610.09358)
- **PDF**: https://arxiv.org/pdf/2610.09358
- **详细分析**: [[20_Research/Papers/具身智能/COOL_Curiosity-Driven_Object_Ownership_Learning_for_Personalized_Robotic_Assistance|COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance]]
- **作者**: Samira Huber, Ruben Hammele, Sören Pirk
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSNet, Per-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots are increasingly expected to provide personalized services in everyday environments. To do so, they must ground natural-language commands such as "Where is my backpack?" or "Find my bottle" and execute them by reasoning about object instances, people, locations, and ownership. This is challenging because ownership is rarely labeled explicitly and must be inferred from long-term, behavioral evidence of human-object interactions. To address this, we present COOL, a novel robotic framework for autonomously learning object ownership from everyday observations and maintaining a long-term spatial memory of its environment. To keep its memory current, COOL uses an agent-based curiosity-driven data collection strategy that guides the robot toward the most promising locations to gain information and refresh stale observations. Offline experiments, ablation studies, and real-world evaluations show that COOL can infer ownership relations from real-world interactions and use this knowledge for ownership-conditioned navigation and task execution.

</details>

---

### [[20_Research/Papers/机器人/ClimbLab_MATLAB_Simulation_Platform_for_Legged_Climbing_Robotics|ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics]]

![[assets/2610.09315_figure.png|800]]

- **arXiv**: [2610.09315](https://arxiv.org/abs/2610.09315)
- **PDF**: https://arxiv.org/pdf/2610.09315
- **详细分析**: [[20_Research/Papers/机器人/ClimbLab_MATLAB_Simulation_Platform_for_Legged_Climbing_Robotics|ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics]]
- **作者**: Kentaro Uno, Warley F. R. Ribeiro, Yusuke Koizumi, Keigo Haji, Koki Kurihara, William Jones, Kazuya Yoshida
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《ClimbLab: MATLAB Simulation Platform for Legged Climbing Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RaiSim, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an open-sourced MATLAB simulation and analysis platform dedicated to legged climbing robots. This simulator enables the design of any limbed robotic system as an articulated multi-body with a floating base and simulates it walking and climbing in an arbitrary environment. The main variable environmental parameters are inclination, gravity, and ground stiffness, and any point cloud can be installed as the terrain map. Furthermore, the simulator employs a rigid body dynamics engine. This paper first describes the simulator structure, and the computational flow and next presents the representative simulation examples where quadrupedal robots assumed gripping on the wall or climbing on the steep slope.

</details>

---

### [[20_Research/Papers/具身智能/Predicted_Futures_Are_Not_Enough_Learning_Executable_Goals_for_Robot_Manipulation|Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation]]

![[assets/2610.09309_figure.png|800]]

- **arXiv**: [2610.09309](https://arxiv.org/abs/2610.09309)
- **PDF**: https://arxiv.org/pdf/2610.09309
- **详细分析**: [[20_Research/Papers/具身智能/Predicted_Futures_Are_Not_Enough_Learning_Executable_Goals_for_Robot_Manipulation|Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation]]
- **作者**: Tzu-Yu Chuang, Ching-Hsiang Chang, Yi-Hsiu Lee, Yi-Ting Chen, Min Sun, YuanFu Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.5（加权：具身智能 1.2，世界模型 0.4，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative world models provide rich predictions of how manipulation scenes may evolve toward task objectives, yet those futures do not directly expose the compact task variables required by control. When training supervises future prediction alone, terminal goal accuracy is not an explicit learning objective, even when geometric recovery is available. We present Entity-Level Goal Readout, a learned prediction-to-execution interface that makes the executable terminal goal an explicit output of a 3D trace world model. It combines object-centric pose prediction with translation grounded in observed depth to produce a compact goal in SE(3). A shared Pose-Native Executor consumes this fixed goal with online object-pose feedback for closed-loop control without rerunning the world model. Across five manipulation tasks, the pipeline achieves a mean success rate of 79.69%. Goal diagnostics directly measure terminal goal accuracy, while controlled translation perturbations characterize how execution degrades under goal error. Zero-shot deployment on a Franka arm achieves 73.33% success on nominal StackCube, 66.67% with distractors, and 75.00% on PickPlate with a target unseen during policy training. These results support treating the prediction-to-execution interface as an explicit learned component of world-model planning rather than incidental post-processing in the control pipeline itself. Project page: https://claire0730.github.io/executable-goals/

</details>

---

### [[20_Research/Papers/具身智能/LACE-CRAFT_Robot_Co-Design_with_Actor_Inheritance_and_Blackboard_Collaboration|LACE-CRAFT: Robot Co-Design with Actor Inheritance and Blackboard Collaboration]]

![[assets/2610.09283_figure.png|800]]

- **arXiv**: [2610.09283](https://arxiv.org/abs/2610.09283)
- **PDF**: https://arxiv.org/pdf/2610.09283
- **详细分析**: [[20_Research/Papers/具身智能/LACE-CRAFT_Robot_Co-Design_with_Actor_Inheritance_and_Blackboard_Collaboration|LACE-CRAFT: Robot Co-Design with Actor Inheritance and Blackboard Collaboration]]
- **作者**: Yuhan Wen, Jiawei Wang, Qixuan Zhang, Yusen Qin, Lan Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《LACE-CRAFT: Robot Co-Design with Actor Inheritance and Blackboard Collaboration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot co-design couples morphology search with policy learning, yet training every new design from scratch discards acquired control experience. We present LACE-CRAFT, which compares continued learning on the current robot with policy adaptation to new morphology-reward pairs. LACE resumes the incumbent's full learning state and initializes compatible challengers with its actor parameters and observation statistics. A fixed task metric selects among both branches and the frozen incumbent. CRAFT coordinates Feedback, Morphology, Reward, and Integration roles through shared experimental records and behavioral replays to generate and cross-review paired proposals. A generative extension converts generated meshes into editable articulated models with configured joints, actuator interfaces, and consistently updated simulation assets. Across five locomotion benchmarks, mean scores over three evaluation seeds are 6.4-91.9% higher than D2C. Both methods train 30 new morphology-reward pairs over five rounds; LACE additionally uses four continuation training units. Five-task ablations examine policy inheritance and replay-derived feedback. A fabricated prototype demonstrates indoor walking and illustrates the geometry-to-hardware workflow.

</details>

---

### [[20_Research/Papers/强化学习/RoboRender_Robot-Oriented_Video_Generation_for_Visual_Sim-to-Real_Transfer|RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer]]

![[assets/2610.09254_first_page.png|800]]

- **arXiv**: [2610.09254](https://arxiv.org/abs/2610.09254)
- **PDF**: https://arxiv.org/pdf/2610.09254
- **详细分析**: [[20_Research/Papers/强化学习/RoboRender_Robot-Oriented_Video_Generation_for_Visual_Sim-to-Real_Transfer|RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer]]
- **作者**: Huang Huang, Wensi Ai, Ziyu Chen, Youhui Wang, Zijian Du, Yang Liu, Jiaolong Yang, Li Fei-Fei, Jiajun Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation enables large-scale, low-cost robot data generation, but policies trained in simulation often fail to transfer to the real world due to the sim-to-real visual discrepancies. Existing approaches often rely on intermediate representations, which can discard rich semantic information or require additional perception modules at deployment. We address this visual sim-to-real gap with RoboRender, a framework that converts simulated trajectories into photorealistic RGB videos for policy learning. RoboRender trains a robot-oriented video generation model conditioned on simulated depth videos, language instructions, and robot RGB mask videos, preserving simulator geometry, robot motion, and action labels while synthesizing realistic textures, backgrounds, and distractors. The generated RGB videos are paired with simulator-provided states and actions to train policies for zero-shot real-world deployment. On robot video test sets, our video model outperforms depth-conditioned video generation baselines in generation quality. In real-world experiments across pick-and-place, articulated-object manipulation, and mobile manipulation tasks, policies trained on RoboRender-generated data achieve a 71% average success rate, outperforming raw simulation renderings and conventional visual domain randomization by approximately 7.1x and 3.6x, respectively. We further show that policy performance improves with more generated videos per simulation trajectory, increasing opening-task success by 65 percentage points. These results demonstrate that generative video rendering mitigates the visual sim-to-real gap for zero-shot policy transfer. Project website: https://robo-render.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Co-Evolving_Robot_Orchestrators_and_Policies_through_Deployment|Co-Evolving Robot Orchestrators and Policies through Deployment]]

![[assets/2610.09228_figure.png|800]]

- **arXiv**: [2610.09228](https://arxiv.org/abs/2610.09228)
- **PDF**: https://arxiv.org/pdf/2610.09228
- **详细分析**: [[20_Research/Papers/具身智能/Co-Evolving_Robot_Orchestrators_and_Policies_through_Deployment|Co-Evolving Robot Orchestrators and Policies through Deployment]]
- **作者**: Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang, Jiajun Wu, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Co-Evolving Robot Orchestrators and Policies through Deployment》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bottleneck of the whole system. Fine-tuning the policy can remove this bottleneck, but updating it alone decouples it from an orchestrator tuned to its old behavior. We propose Robo-COP, in which the orchestrator and policy co-evolve during deployment. Robo-COP curates skill demonstrations from its own executions, fine-tunes the policy when this data can address recurring failures, and adopts each new policy only after it improves the skills it was trained for. Across ten simulated RoboLab tasks, Robo-COP raises mean held-out success from 64.8% to 73.8% over the same harness with a frozen policy, while fine-tuning on a fixed schedule without verification reaches only 65.8%. On three real-world tasks, Robo-COP raises held-out success from 38.3% to 50.0%. Robo-COP turns deployment into a self-improving flywheel in which robots learn by doing, with each improvement in execution producing better data for the next round of learning. Videos and code are available at https://robo-cop.pages.dev/.

</details>

---

### [[20_Research/Papers/具身智能/Fast_Planning_for_Multi-object_Multi-target_Throwing|Fast Planning for Multi-object Multi-target Throwing]]

![[assets/2610.09224_figure.png|800]]

- **arXiv**: [2610.09224](https://arxiv.org/abs/2610.09224)
- **PDF**: https://arxiv.org/pdf/2610.09224
- **详细分析**: [[20_Research/Papers/具身智能/Fast_Planning_for_Multi-object_Multi-target_Throwing|Fast Planning for Multi-object Multi-target Throwing]]
- **作者**: Zhengming Zhu, Yang Liu, Xiao Gao, Aude Billard
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Fast Planning for Multi-object Multi-target Throwing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot throwing has emerged as a promising technique for improving efficiency in logistics and warehouse automation, by enlarging the workspace and speeding up the process. To significantly increase the throwing system's throughput, we develop strategies for throwing multiple objects in one swipe. Such multi-object multi-target throwing (MOMT) leverages the large degrees of freedom of anthropomorphic hands. The key is to quickly generate fast and feasible throwing motions, which involves a complex trade-off between short trajectory duration and short planning time. We solve this problem in two stages. Offline, we build a model of the feasible set by combining object's inverted flying dynamics and the robot's kinematics and dynamics. Online, we generate feasible throws through fast solution matching and filtering of object's valid detach state and robot's feasible state that can compose sequences of throws in less than 5 ms. We validate the framework on a 7-DoF manipulator equipped with a multi-fingered hand. In simulation, coordinated two-object throwing reduces execution time by up to 46% compared to independent single-object planning, and this improvement is maintained when scaling to three objects. Real-world experiments with two objects confirm a 29% reduction; the remaining gap to the theoretical 50% is attributed to inter-throw transition overhead. When target positions are randomly changed mid-execution, the system re-plans and successfully reaches the new targets within 100 ms latency without stopping the robot. These results establish the first unified planning framework for MOMT throwing -- demonstrating scalability to multiple objects in simulation and real-world feasibility on two-object tasks -- advancing the frontier of high-throughput robotic manipulation. A video summarizing the method and the hardware experiments is available at https://liuyangdh.github.io/momt-video

</details>

---

### [[20_Research/Papers/强化学习/Embedded_Evaluation_of_Task_Admission_Coalescing_in_Decentralized_Multi-Robot_Systems|Embedded Evaluation of Task Admission Coalescing in Decentralized Multi-Robot Systems]]

![[assets/2610.09187_figure.png|800]]

- **arXiv**: [2610.09187](https://arxiv.org/abs/2610.09187)
- **PDF**: https://arxiv.org/pdf/2610.09187
- **详细分析**: [[20_Research/Papers/强化学习/Embedded_Evaluation_of_Task_Admission_Coalescing_in_Decentralized_Multi-Robot_Systems|Embedded Evaluation of Task Admission Coalescing in Decentralized Multi-Robot Systems]]
- **作者**: James Lott, Vahraz Honary
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Embedded Evaluation of Task Admission Coalescing in Decentralized Multi-Robot Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot task allocators in dynamic missions commonly admit newly released tasks immediately, potentially invoking allocation for each new arrival. We evaluate task-admission coalescing as a mechanism for controlling allocator processor work while accounting for target-service latency, using CBAA, ACBBA, PI, and HIPC as a representative MRTA suite. The study comprises a 3,000-mission AGX Orin campaign with measured computation delay, 3,000 paired zero-compute missions, and a 96-mission Pololu 3pi+ RP2040 allocator hardware-in-the-loop campaign. Immediate (Eager) admission is compared with thresholds of two, four, and eight tasks and a four-task policy with a 10-s waiting bound across three arrival rates. Across the AGX experiments, coalescing reduces both allocator calls and processor work in 31 of 48 evaluated conditions, although the magnitude of the saving varies by allocator. The principal cost appears under sparse arrivals, where four-task batching increases online-target mean latency by 20.08-23.57 s, predominantly through admission waiting. Bounded admission reduces mean work in ten of twelve allocator-load conditions, including a 19.35% reduction with a 1.40-s mean latency increase for high-arrival HIPC. RP2040 experiments show that this tradeoff can become more favorable as processor constraints tighten. Across four matched medium-arrival HIPC scenarios, Count b=4 reduces mean RP2040 work by 59.85% and service latency by 39.47%, while the corresponding AGX cases increase latency by 27.69%. These results show that the usefulness of task-admission coalescing depends on arrival intensity, allocator-specific behavior, and the relative cost of computation on the execution platform.

</details>

---

### [[20_Research/Papers/强化学习/CAP_Codebook-Aligned_Prediction_for_Tokenized_Robot_Policies|CAP: Codebook-Aligned Prediction for Tokenized Robot Policies]]

![[assets/2610.09178_first_page.png|800]]

- **arXiv**: [2610.09178](https://arxiv.org/abs/2610.09178)
- **PDF**: https://arxiv.org/pdf/2610.09178
- **详细分析**: [[20_Research/Papers/强化学习/CAP_Codebook-Aligned_Prediction_for_Tokenized_Robot_Policies|CAP: Codebook-Aligned Prediction for Tokenized Robot Policies]]
- **作者**: Haoran Chen, Jingtian Ji, Samuel Wheeler, Kaylene Caswell Stocking, Matthew Walter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CAP: Codebook-Aligned Prediction for Tokenized Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action tokenization converts continuous robot actions into discrete symbols that can be modeled autoregressively. However, existing tokenizer-based policies typically ignore the tokenizer's learned latent code structure: after tokenization, the policy treats tokens as unrelated class indices and learns a new classifier from scratch. We show that this discarded structure is valuable. We introduce Codebook-Aligned Prediction (CAP), a method that directly reuses the tokenizer's code vectors as policy class prototypes while leaving the tokenizer and policy backbone otherwise unchanged. Across four quantizer families, three simulation benchmarks, and two real-robot tasks, CAP consistently improves task success over standard token classification heads while holding the tokenizer (and therefore its reconstruction quality) fixed. Our analysis further shows that these gains are not explained by higher token accuracy or changes in the policy head alone. Instead, reusing the tokenizer codebook provides the policy with valuable information about the tokenizer's learned latent structure across tokens, making token prediction errors more benign in action space and improving the representations learned by the policy backbone. These results suggest that action tokenizers learn useful action-aware latent structure beyond discrete targets that should be preserved when training downstream policies.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Reconstruction_What_Matters_in_Action_Tokenization_for_Robot_Policies|Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?]]

![[assets/2610.09170_first_page.png|800]]

- **arXiv**: [2610.09170](https://arxiv.org/abs/2610.09170)
- **PDF**: https://arxiv.org/pdf/2610.09170
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Reconstruction_What_Matters_in_Action_Tokenization_for_Robot_Policies|Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?]]
- **作者**: Haoran Chen, Jingtian Ji, Samuel Wheeler, Kaylene Caswell Stocking, Matthew Walter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive action-token policies such as vision-language-action models require action tokenizers to translate discrete token sequences into precise control actions in continuous space. Many action tokenizers learn the mapping between tokens and actions via a reconstruction objective. However, as we show through extensive analysis, sufficiently accurate action reconstruction is only one part of what makes a downstream robot policy successful. It is also critical that the policy is able to predict the right tokens for new observations, and that unseen policy token predictions still decode into reasonable actions. These properties are downstream of tokenizer training and are not directly incentivized by a reconstruction objective alone. In this work, we introduce Predictable and Robust Action Tokenization (ProAct), a tokenizer training method that strategically augments reconstruction with the goal of improving downstream predictability and robustness. ProAct is policy-agnostic and uses only action datasets for training. Across the Robomimic, LIBERO, and RoboTwin benchmarks and a diverse set of tokenizer architectures, ProAct improves rollout success by an average of 11.3 percentage points. These improvements also translate to vision-language-action policies and real-world robotic manipulation, yielding average gains of 21.8 and 36.7 percentage points, respectively. These results suggest that effective action tokenization should be designed as a policy interface that balances fidelity, predictability, and robustness, rather than as a reconstruction problem alone.

</details>

---

### [[20_Research/Papers/机器人/geodex_A_Library_for_Motion_Planning_on_Riemannian_Manifolds|geodex: A Library for Motion Planning on Riemannian Manifolds]]

![[assets/2610.09165_figure.png|800]]

- **arXiv**: [2610.09165](https://arxiv.org/abs/2610.09165)
- **PDF**: https://arxiv.org/pdf/2610.09165
- **详细分析**: [[20_Research/Papers/机器人/geodex_A_Library_for_Motion_Planning_on_Riemannian_Manifolds|geodex: A Library for Motion Planning on Riemannian Manifolds]]
- **作者**: Phone Thiha Kyaw, Ben Wei, Sepehr Samavi, Miguel Angel Rogel Garcia, Jonathan Kelly
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《geodex: A Library for Motion Planning on Riemannian Manifolds》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning motions that respect the intrinsic geometry of a robot's configuration space, including its curvature and a configuration-dependent notion of cost, yields shorter, lower-energy, and more natural trajectories than planning under the ambient flat metric. Existing libraries for optimization on manifolds provide rich geometric primitives but do not plan around obstacles. While general-purpose motion planning libraries support many state spaces and custom distance functions, they do not yet treat a configuration-dependent Riemannian metric as the geometry that drives distance, interpolation, and geodesics. We present geodex, an open-source C++20 library with Python bindings. The library exposes the manifold, its Riemannian metric, the retraction, and the sampler as independent, interchangeable components through a single sampling-based motion planning interface. The same planner runs unchanged on canonical spaces $\mathbb{R}^n$, $\mathbb{T}^n$, $\mathbb{S}^n$, matrix Lie groups such as $SO(2)$, $SE(2)$, $SO(3)$, and $SE(3)$, products of these spaces, and articulated-robot configuration spaces, each equipped with a user-defined Riemannian metric. We make geodex publicly available with documentation, tests, and a reproducible benchmark suite.

</details>

---

### [[20_Research/Papers/强化学习/World_Models_Dream_of_Success_Diagnosing_and_Repairing_Failure_Insensitivity_in_Robot_World_Models|World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models]]

![[assets/2610.09134_figure.png|800]]

- **arXiv**: [2610.09134](https://arxiv.org/abs/2610.09134)
- **PDF**: https://arxiv.org/pdf/2610.09134
- **详细分析**: [[20_Research/Papers/强化学习/World_Models_Dream_of_Success_Diagnosing_and_Repairing_Failure_Insensitivity_in_Robot_World_Models|World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models]]
- **作者**: Jiuyi Xu, Xiao Hu, Meida Chen, Peng Gao, Yang Ye, Yangming Shi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《World Models Dream of Success: Diagnosing and Repairing Failure Insensitivity in Robot World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, Dex-Net, MiraBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot world models support policy evaluation, planning, and synthetic data generation, but these applications require predictions that distinguish successful actions from failures. Across four released checkpoints from two architecture families, we observe weak sensitivity to action changes and success-like predictions on verified failures. Although recent work incorporates failures into model training, which data can repair released checkpoints without changing their architecture or training objective still remains underexplored. To this end, we introduce CureWM, which constructs alternative actions from successful demonstrations across a severity grid, verifies their outcomes through execution in simulation or on hardware, and fine-tunes released models on the resulting failures and surviving successes alongside nominal demonstrations. This construction provides controlled action contrasts from shared starting contexts. On 484 held-out LIBERO failure counterfactuals, optimism falls from 80\% after fine-tuning on the official data to 30--43\% across four independently fine-tuned CureWM models (38\% mean). In two separate evaluations on a physical robot arm, failure predictions scored as success-like by a latent-distance diagnostic decrease from 90\% after fine-tuning on successful demonstrations alone to 33\% with CureWM. With failure counts per task, successful replay data, and training budget matched, counterfactual failures yield a success--failure value gap of 0.124, compared with 0.014 for freshly collected on-policy failures. These findings support execution-verified counterfactual replay for post-hoc repair and show why reduced optimism must be evaluated alongside success--failure discrimination. Code is available at https://github.com/jiuyixu25/CureWM.

</details>

---

### [[20_Research/Papers/具身智能/FlashNeRD_Performance-First_Contact-Rich_Neural_Robot_Dynamics|FlashNeRD: Performance-First Contact-Rich Neural Robot Dynamics]]

![[assets/2610.09130_figure.png|800]]

- **arXiv**: [2610.09130](https://arxiv.org/abs/2610.09130)
- **PDF**: https://arxiv.org/pdf/2610.09130
- **详细分析**: [[20_Research/Papers/具身智能/FlashNeRD_Performance-First_Contact-Rich_Neural_Robot_Dynamics|FlashNeRD: Performance-First Contact-Rich Neural Robot Dynamics]]
- **作者**: Mohammadmehdi Ataei, Mohammad Amin Nabian, Jie Xu, Miles Macklin, Yashraj Narang, Eric Heiden, Octi Zhang, Yunrong Guo, Ruben D'Sa, Oliver Hennigh, Gavriel State, Sanjay Choudhry
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.9（加权：具身智能 0.6，世界模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《FlashNeRD: Performance-First Contact-Rich Neural Robot Dynamics》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compared with analytical physics, learned dynamics models promise robot simulation that is faster, inherently differentiable, and easily adaptable to real data. Neural Robot Dynamics (NeRD) pursues this by keeping collision detection analytical and replacing a simulator's numerical dynamics for the robot with a learned model. Three limitations remain. NeRD offers little speedup over the simulator it learned from, accepts contact only at predefined points, and has no two-way coupling with objects it manipulates. FlashNeRD removes all three with a parallel streaming architecture that makes each prediction faster and more accurate, an encoder that accepts contacts wherever they occur, and two-way coupling with objects simulated by analytical solvers. Experiments across five robots show faster and more accurate dynamics, faster policy learning, and faster inference-time planning. Across three robots, FlashNeRD's dynamics model is up to $55\times$ faster than an optimized NeRD and more accurate over long rollouts. This speedup extends to policy learning, where PPO trains an ANYmal locomotion policy in 34 seconds, $3.8\times$ faster than the analytical simulator and $2.7\times$ faster than an optimized NeRD. With DIAL-MPC, a sampling-based MPC method, the robot climbs all six test platforms where fixed-contact NeRD manages one, at approximately half the analytical simulator's planning time. Cube-reorientation policies trained with FlashNeRD complete within 2% of the simulator-trained policy's target count.

</details>

---

### [[20_Research/Papers/强化学习/From_Wearable_Interfaces_to_Dexterous_Policies_Contact_Shifts_and_Tactile_Representations|From Wearable Interfaces to Dexterous Policies: Contact Shifts and Tactile Representations]]

![[assets/2610.08870_figure.png|800]]

- **arXiv**: [2610.08870](https://arxiv.org/abs/2610.08870)
- **PDF**: https://arxiv.org/pdf/2610.08870
- **详细分析**: [[20_Research/Papers/强化学习/From_Wearable_Interfaces_to_Dexterous_Policies_Contact_Shifts_and_Tactile_Representations|From Wearable Interfaces to Dexterous Policies: Contact Shifts and Tactile Representations]]
- **作者**: Ruitong Tian, Fang Xu, Noah B. Wilson, Xianyao Li, Eric Jing Du
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《From Wearable Interfaces to Dexterous Policies: Contact Shifts and Tactile Representations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unlike conventional teleoperation, wearable interfaces allow operators to collect dexterous demonstrations through their own hand motions while directly interacting with task objects. This direct interaction reduces dependence on the target robot during collection, but it also makes the collection hardware part of the physical process that generates each demonstration. Interface geometry can influence both how a task is performed and what tactile observations are recorded for learning. We study two versions of a DexUMI-family exoskeleton that share the same robot command definition, mapping procedure, and tactile module type but differ in hand-side geometry. The revised interface reduces reported physical demand, improves selected device ratings, enables tactile access in a precision grasp that is mechanically blocked by the baseline, and produces task-dependent changes in recorded contact. Lid twisting primarily exhibits a change in contact location, whereas egg carton opening primarily exhibits a change in contact occurrence. We then train matched policies using either a binary aggregate input or a spatial-plus-force input. On lid twisting and egg carton opening, policies trained on revised-interface demonstrations achieve higher success than those trained on baseline demonstrations, with a significant pooled interface effect. Across these and two additional tasks, USB insertion and soldering tool pick and place, the spatial-plus-force input likewise outperforms binary aggregation. These results show that wearable collection hardware is part of the data-generation process for robot learning. Such interfaces should therefore be evaluated not only through operator experience, but also through the tactile interactions they make recordable and the policy performance their demonstrations support.

</details>

---

### [[20_Research/Papers/具身智能/SAFE_Unified_Slip_and_Fracture_Detection_with_Low-Cost_Acoustic_Sensing_in_Robotic_Grasping|SAFE: Unified Slip and Fracture Detection with Low-Cost Acoustic Sensing in Robotic Grasping]]

![[assets/2610.08802_figure.png|800]]

- **arXiv**: [2610.08802](https://arxiv.org/abs/2610.08802)
- **PDF**: https://arxiv.org/pdf/2610.08802
- **详细分析**: [[20_Research/Papers/具身智能/SAFE_Unified_Slip_and_Fracture_Detection_with_Low-Cost_Acoustic_Sensing_in_Robotic_Grasping|SAFE: Unified Slip and Fracture Detection with Low-Cost Acoustic Sensing in Robotic Grasping]]
- **作者**: Zerun Wang, Vivek Kamat, Shekhar Bhansali
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《SAFE: Unified Slip and Fracture Detection with Low-Cost Acoustic Sensing in Robotic Grasping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating fragile objects remains challenging as robots must understand the state of what they grasp, such as slip or fracture, to respond appropriately, especially when material properties are unknown. In this paper, we present SAFE: a low-cost, general-purpose sensing approach that detects both slip and fracture in real time using two passive polyvinylidene fluoride (PVDF) acoustic sensors and motor proprioception, without relying on vision or prior material knowledge. The sensors are mounted on a compliant Fin Ray gripper, and a unified HistGradientBoosting classifier reports the state (normal, slip, or fracture) from a 79-dimensional feature vector. Under leave-one-grasp-out cross-validation, SAFE achieves an Alert-F1 of 0.884 with near-zero slip-fracture confusion, and ablations confirm that acoustic sensing is indispensable. An adaptive grasp controller built on this detection layer runs at 104 Hz on a Jetson Orin Nano, achieving 91.3% success across 46 closed-loop robot trials spanning diverse object categories, while each fixed-force strategy drops to 0% on object conditions that mismatch its preset. It further reaches 82.4% success on novel objects unseen during training, demonstrating robust, failure-aware grasp control without object-specific calibration.

</details>

---
