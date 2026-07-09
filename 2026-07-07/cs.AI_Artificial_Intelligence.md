# cs.AI | Artificial Intelligence | 2026-07-07

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/具身智能/From_Fixed_to_Free_Cameras_Calibration-Free_View-Robust_Vision-Language-Action_Model|From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model]]

![[assets/2607.05396_figure.png|800]]

- **arXiv**: [2607.05396](https://arxiv.org/abs/2607.05396)
- **PDF**: https://arxiv.org/pdf/2607.05396
- **详细分析**: [[20_Research/Papers/具身智能/From_Fixed_to_Free_Cameras_Calibration-Free_View-Robust_Vision-Language-Action_Model|From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model]]
- **作者**: Wenhao Li, Xueying Jiang, Quanhao Qian, Deli Zhao, Shijian Lu, Gongjie Zhang, Ran Xu
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AnyCamVLA, CamVLA, OC-VLA, RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To this end, we introduce Camera-Centric VLA (CamVLA), a new VLA model that decouples manipulation controls from camera geometry by predicting (i) a camera-centric end-effector action expressed in the local camera frame, and (ii) a 6-DoF hand-eye matrix relating cameras to the robot base. A deterministic geometric transformation composes the two predictions into a robot base-frame action. This disentangles how I should move in pose-independent camera-centric action generation from where I am looking from in camera-perspective geometric grounding. The resulting policy is calibration-free, depth-free, and single-view, requiring only a single monocular RGB image as the visual observation and task instruction at deployment. Evaluations in both simulation and real-world robot data show that CamVLA consistently improves success rates across diverse unseen viewpoints. Project page: https://alibaba-damo-academy.github.io/CamVLA/.

</details>

---

### [[20_Research/Papers/大模型/LLM-as-a-Verifier_A_General-Purpose_Verification_Framework|LLM-as-a-Verifier: A General-Purpose Verification Framework]]

![[assets/2607.05391_figure.png|800]]

- **arXiv**: [2607.05391](https://arxiv.org/abs/2607.05391)
- **PDF**: https://arxiv.org/pdf/2607.05391
- **详细分析**: [[20_Research/Papers/大模型/LLM-as-a-Verifier_A_General-Purpose_Verification_Framework|LLM-as-a-Verifier: A General-Purpose Verification Framework]]
- **作者**: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.35（加权：具身智能 0.3，大模型 0.55，机器人 0.5）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《LLM-as-a-Verifier: A General-Purpose Verification Framework》归入 大模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, MedAgentBench, RoboRewardBench, SWE-Bench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate solutions, LLM-as-a-Verifier computes the expectation over the distribution of scoring token logits to generate continuous scores. This probabilistic formulation enables verification to scale along multiple dimensions: (1) score granularity, (2) repeated evaluation, and (3) criteria decomposition. In particular, we show that scaling the scoring granularity leads to better separation between positive and negative solutions, resulting in more calibrated comparisons. Moreover, scaling repeated evaluation and criteria decomposition consistently lead to additional gains in verification accuracy through variance and complexity reduction. We further introduce a cost-efficient ranking algorithm for selecting the best solution among candidates using the verifier's continuous scores. LLM-as-a-Verifier achieves state-of-the-art performance on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%). Beyond verification, the fine-grained signals from LLM-as-a-Verifier can also serve as a proxy for estimating task progress. We build an extension for Claude Code, enabling developers to monitor and improve their own agentic systems. Finally, we show that LLM-as-a-Verifier can provide dense feedback for RL, improving the sample efficiency of SAC and GRPO on robotics and mathematical reasoning benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Cortex_A_Bidirectionally_Aligned_Embodied_Agent_Framework_for_Long-horizon_Manipulation|Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation]]

![[assets/2607.05377_figure.png|800]]

- **arXiv**: [2607.05377](https://arxiv.org/abs/2607.05377)
- **PDF**: https://arxiv.org/pdf/2607.05377
- **详细分析**: [[20_Research/Papers/具身智能/Cortex_A_Bidirectionally_Aligned_Embodied_Agent_Framework_for_Long-horizon_Manipulation|Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation]]
- **作者**: Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgibotWorld, InternVLA, OpenVLA, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

</details>

---

### [[20_Research/Papers/强化学习/GaP_A_Graph-as-Policy_Multi-Agent_Self-Learning_Harness_For_Variational_Automation_Tasks|GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks]]

![[assets/2607.05369_figure.png|800]]

- **arXiv**: [2607.05369](https://arxiv.org/abs/2607.05369)
- **PDF**: https://arxiv.org/pdf/2607.05369
- **详细分析**: [[20_Research/Papers/强化学习/GaP_A_Graph-as-Policy_Multi-Agent_Self-Learning_Harness_For_Variational_Automation_Tasks|GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks]]
- **作者**: Kaiyuan Chen, Shuangyu Xie, Letian Fu, Justin Yu, William Pacini, Sandeep Bajamahal, Hudson Kim, Jaimyn Drake, Daehwa Kim, Haoru Xue, Jonathan Francis, Christian Juette...
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.75（加权：具身智能 0.3，大模型 0.55，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Blox-Net, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and industrial applications. Motivated by prior work on Task and Motion Planning (TAMP) and the Robot Operating System (ROS), we introduce Graph-as-Policy (GaP), a multi-agent coding harness that generates directed computation graphs with perception, planning, and control nodes from a Modular Open Robot Skill Library (MORSL). GaP then generates an internal simulation environment to rehearse task instances with different graphs in parallel to iteratively refine the graph structure and parameters to improve success rates and throughput. Evaluation with 8 new open VA task benchmarks, 4 in-simulation and 4 in real-world, suggests that GaP can achieve success rates that significantly outperform baselines. Details, code, and data can be found online: https://graph-robots.github.io/gap

</details>

---

### [[20_Research/Papers/世界模型/Multiplayer_Interactive_World_Models_with_Representation_Autoencoders|Multiplayer Interactive World Models with Representation Autoencoders]]

![[assets/2607.05352_first_page.png|800]]

- **arXiv**: [2607.05352](https://arxiv.org/abs/2607.05352)
- **PDF**: https://arxiv.org/pdf/2607.05352
- **详细分析**: [[20_Research/Papers/世界模型/Multiplayer_Interactive_World_Models_with_Representation_Autoencoders|Multiplayer Interactive World Models with Representation Autoencoders]]
- **作者**: Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, Chris Mulder, Aditya Makkar, Amélie Royer, Manu Orsini, Alyx Liao, Adam Jelley, Eloi Alonso, Florian Laurent, Fredrik Norén...
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Multiplayer Interactive World Models with Representation Autoencoders》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, tightly coupled dynamics. Trained on 10,000 hours of gameplay collected with publicly available bots, our 5-billion-parameter latent diffusion model generates four-player matches in real time, producing 20 frames per second on a single Nvidia B200 GPU. Although trained only on short clips, its rollouts stay stable far beyond the training horizon: distributional quality holds steady out to five minutes, the longest horizon we measure, and in practice we observe rollouts continuing for hours with no sign of collapse. We systematically investigate the central design choices: the video codec, the generative objective, and the multiplayer conditioning scheme. In addition, we characterize how behavior changes with model and data scale, including the capabilities that emerge and the failure modes that persist. We further develop targeted evaluations that probe the model's physical understanding rather than visual appearance alone. To support continued research on multiplayer world models, we release our dataset, our full training and inference codebase, and a live demo.

</details>

---

### [[20_Research/Papers/强化学习/Relational_Multi-Agent_Reinforcement_Learning_for_Dynamic_Pricing_in_High-Speed_Railway_Markets|Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets]]

![[assets/2607.05179_figure.png|800]]

- **arXiv**: [2607.05179](https://arxiv.org/abs/2607.05179)
- **PDF**: https://arxiv.org/pdf/2607.05179
- **详细分析**: [[20_Research/Papers/强化学习/Relational_Multi-Agent_Reinforcement_Learning_for_Dynamic_Pricing_in_High-Speed_Railway_Markets|Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets]]
- **作者**: Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez, Giovanni Montana, Luis Jimenez-Linares
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, G2ANet, InforMARL, MARL, MRGRL, RelationalRailPricing-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning, where standard approaches typically treat observations as unstructured vectors, ignoring the underlying market topology that governs strategic interactions. To address this, an entity graph modelling approach is proposed, which represents the environment as a graph of operational units, rather than decision-making agents or static infrastructure, encoding competition, coordination, and connectivity relations between entities. Then, an extension of the multi-agent twin delayed deep deterministic policy gradient algorithm with graph-based representation learning processes the features of the entities through a multi-layer relational graph convolutional network and aggregates them via a learnt attention mechanism. Experimental results in a rail pricing reinforcement learning environment show that this novel framework achieves higher revenue and stability in two different settings of increasing market complexity compared to a representative selection of relational and non-relational baselines. The code is publicly available at: https://github.com/Kinrre/RelationalRailPricing-RL

</details>

---

### [[20_Research/Papers/强化学习/Diffusion-Guided_Uncertainty-Aware_Delayed_Policy_Optimization|Diffusion-Guided Uncertainty-Aware Delayed Policy Optimization]]

![[assets/2607.05064_figure.png|800]]

- **arXiv**: [2607.05064](https://arxiv.org/abs/2607.05064)
- **PDF**: https://arxiv.org/pdf/2607.05064
- **详细分析**: [[20_Research/Papers/强化学习/Diffusion-Guided_Uncertainty-Aware_Delayed_Policy_Optimization|Diffusion-Guided Uncertainty-Aware Delayed Policy Optimization]]
- **作者**: Junqi Tu, Zejiao Liu, Fangfei Li, Yang Tang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人
- **相关性评分**: 1.4（加权：强化学习 1.2，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Diffusion-Guided Uncertainty-Aware Delayed Policy Optimization》归入 强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning in real world environments often suffers from severe performance degradation due to delayed feedback. Existing approaches typically mitigate performance degradation caused by observation delays by constructing augmented states or predicting the true states. However, these methods often overlook the inherent discrepancy between delayed state and true states induced by stochastic MDP. We theoretically prove the existence of such a discrepancy and show that it leads to the degradation of the optimal policy. To address this challenge, we propose Diffusion Guided Uncertainty Aware Delayed Policy Optimization (DUPO). Our method explicitly models the relationship between delayed state message and the current state using a diffusion model, and leverages the resulting discrepancy estimates to weight delayed policies. Extensive experiments on continuous robotic control tasks with multiple stochastic delays demonstrate that DUPO consistently outperforms existing methods and remains effective even under long and random delay scenarios.

</details>

---

### [[20_Research/Papers/大模型/Toward_Trustworthy_Large_Language_Model_Agents_in_Healthcare|Toward Trustworthy Large Language Model Agents in Healthcare]]

![[assets/2607.05055_figure.png|800]]

- **arXiv**: [2607.05055](https://arxiv.org/abs/2607.05055)
- **PDF**: https://arxiv.org/pdf/2607.05055
- **详细分析**: [[20_Research/Papers/大模型/Toward_Trustworthy_Large_Language_Model_Agents_in_Healthcare|Toward Trustworthy Large Language Model Agents in Healthcare]]
- **作者**: Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham, Ammar Mohanna, Ali Chehab
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.6（加权：大模型 1.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Toward Trustworthy Large Language Model Agents in Healthcare》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availability and degrade patient access to care. This paper presents CareConnect, a safety-first conversational agent for healthcare logistics automation that leverages large language model (LLM) function calling, retrieval-augmented generation (RAG), and layered deterministic safety guardrails. The system orchestrates eight domain-specific tools to support appointment booking, modification, cancellation, and facility information retrieval, while enforcing strict scope constraints that prohibit medical advice or diagnosis. Safety-critical situations are handled through deterministic short-circuit mechanisms for emergency detection and medical intent refusal. We evaluate CareConnect on a comprehensive benchmark of 680 task-oriented scenarios spanning end-to-end workflows, multi-turn interactions, and edge cases. Experimental results demonstrate a 91.8% task completion rate with a median per-request latency of 2.2 seconds, 96.0% safety compliance on the dedicated safety-critical evaluation subset, and an average operational cost of $0.0324 per appointment, yielding a significant cost reduction compared to manual human scheduling. These findings show that carefully scoped and rigorously safeguarded LLM-based agents can reliably automate complex healthcare operational workflows while maintaining safety guarantees and achieving substantial cost efficiency. The source code and system implementation are publicly available at https://github.com/Hadi-Hsn/CareConnect.

</details>

---

### [[20_Research/Papers/机器人/Multi-Robot_Open_Adaptive_Teaming_Across_Unseen_Environments,_Partners,_and_Scales|Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales]]

![[assets/2607.04972_figure.png|800]]

- **arXiv**: [2607.04972](https://arxiv.org/abs/2607.04972)
- **PDF**: https://arxiv.org/pdf/2607.04972
- **详细分析**: [[20_Research/Papers/机器人/Multi-Robot_Open_Adaptive_Teaming_Across_Unseen_Environments,_Partners,_and_Scales|Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales]]
- **作者**: Yang Li, Feng Xue, Fan Mo, Yunhao Liu, Jianhong Wang, Ying Wen, Qingrui Zhang, Shaoshuai Mou, Wei Pan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.1，机器人 1.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying robot teams in the real world requires simultaneous adaptation to unseen environments, unknown partners, and varying team sizes, yet existing approaches often address these challenges in isolation under the closed-world assumption of fixed teammates. We formalize this as open adaptive multi-robot teaming and propose a hypergraphic-form game formulation that captures team-level cooperative relationships beyond pairwise interactions, providing a principled foundation for coordination structure inference when team composition changes dynamically within episodes. Unlike graph neural network architectures, this is a game-theoretic construct for modeling strategic interactions and payoff structures among agents. Building on this formulation, we develop the Hypergraphic Open-ended Learning Algorithm (HOLA), which progressively expands partner and environment diversity during training rather than optimizing for fixed configurations. Evaluated on cooperative pursuit with multi-drone and multi-quadruped platforms, HOLA outperforms all baselines across all three adaptability dimensions. Learned policies transfer directly to physical hardware without fine-tuning, with successful deployments on Crazyflie and Zsibot L1 platforms confirming robust real-world coordination in novel environments with unseen teammates.

</details>

---

### [[20_Research/Papers/大模型/STAPO_Selective_Trajectory-Aware_Policy_Optimization_for_LLM_Agent_Training|STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training]]

![[assets/2607.04963_figure.png|800]]

- **arXiv**: [2607.04963](https://arxiv.org/abs/2607.04963)
- **PDF**: https://arxiv.org/pdf/2607.04963
- **详细分析**: [[20_Research/Papers/大模型/STAPO_Selective_Trajectory-Aware_Policy_Optimization_for_LLM_Agent_Training|STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training]]
- **作者**: Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, Linjian Mo, Ming Kong, Jie Liu, Feng Zhang, Qiang Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 2.1（加权：大模型 1.1，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy-based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision reliability. To address this issue, we propose normalized entropy, which measures confidence deviations relative to an agent's average behavior under a given state, thereby strengthening the association between low-quality actions and trajectory neglect. Building on this insight, we introduce Selective Trajectory-Aware Policy Optimization (STAPO), a hierarchical group-based RL framework. STAPO leverages normalized entropy to locate outlier steps associated with trajectory neglect and optimizes them via a joint mechanism of trajectory-aware reward and trajectory-independent penalty, enhancing trajectory awareness while preserving training stability. Extensive experiments on ALFWorld, WebShop, and Search-Augmented QA demonstrate that STAPO achieves state-of-the-art performance while substantially alleviating trajectory neglect, validating its effectiveness and robustness for agentic tasks.

</details>

---

### [[20_Research/Papers/具身智能/DSWAM_A_Dual-System_World_Action_Foundation_Model_for_Fine-Grained_Robot_Manipulation|DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation]]

![[assets/2607.04927_figure.png|800]]

- **arXiv**: [2607.04927](https://arxiv.org/abs/2607.04927)
- **PDF**: https://arxiv.org/pdf/2607.04927
- **详细分析**: [[20_Research/Papers/具身智能/DSWAM_A_Dual-System_World_Action_Foundation_Model_for_Fine-Grained_Robot_Manipulation|DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation]]
- **作者**: Jian Zhu, Jianjun Zhang, Taiyi Su, Tianbin Liu, Zhangyuan Wang, Kai Xie, Zitai Huang, Chong Ma, Youzhang He, Tianjian Wang, Hanyang Wang, Weihao Ding...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 2.1，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeMaVLA, GigaWorld, Real-World, WAM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile, the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.

</details>

---

### [[20_Research/Papers/大模型/Turning_Off-Policy_Tokens_On-Policy_A_Plug-in_Approach_for_Improving_LLM_Alignment|Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment]]

![[assets/2607.04728_figure.png|800]]

- **arXiv**: [2607.04728](https://arxiv.org/abs/2607.04728)
- **PDF**: https://arxiv.org/pdf/2607.04728
- **详细分析**: [[20_Research/Papers/大模型/Turning_Off-Policy_Tokens_On-Policy_A_Plug-in_Approach_for_Improving_LLM_Alignment|Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment]]
- **作者**: Yu Li, Xiuyu Li, Mingyang Yi, Jiaxing Wang, zhangliangxu, Zhaolong Xing, Zhen Chen
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.55，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably results in off-policy training data. To resolve this, Importance sampling (IS) is proposed, while the token-level ratios compound over long sequences, causing severe variance exploded. A natural idea is "transferring" these off-policy token into on-policy token, so that the importance scores for correction are unnecessary. Following this idea, we propose Selective Importance Sampling (SIS), which is inspired by rejection sampling. Concretely, SIS implements by viewing off-policy model as proposal distribution, and implement a token-level rejection test: accepted tokens are viewed as on-policy, so that receive unit importance score, while rejected tokens retain the standard IS correction. Our proposed SIS is theoretically proved reducing the gap between token-level and sequence-level off-policy gradient estimators. The SIS acts as a plug-in that only modifies the importance ratio in the policy loss, adding negligible wall-clock overhead, and can be combine with a vast vary of RL post-training algorithms. Experiments on dense and MoE LLMs across math and agent benchmarks show that SIS consistently improves all objectives, while providing substantially stronger robustness under off-policy data.

</details>

---

### [[20_Research/Papers/具身智能/Geometry-Aware_Motion_Latents_for_Learning_Robust_Manipulation_Policies|Geometry-Aware Motion Latents for Learning Robust Manipulation Policies]]

![[assets/2607.04714_figure.png|800]]

- **arXiv**: [2607.04714](https://arxiv.org/abs/2607.04714)
- **PDF**: https://arxiv.org/pdf/2607.04714
- **详细分析**: [[20_Research/Papers/具身智能/Geometry-Aware_Motion_Latents_for_Learning_Robust_Manipulation_Policies|Geometry-Aware Motion Latents for Learning Robust Manipulation Policies]]
- **作者**: Yunchao Zhang, Yijia Weng, Ruizhe Liu, Ming Hu, Leonidas Guibas, Yanchao Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Geometry-Aware Motion Latents for Learning Robust Manipulation Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InstructRL, RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning motion latents for robotic manipulation heavily relies on extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional objective -- spatial geometry changing through time -- forces latent representations to encode actual physical motion rather than appearance patterns. GeoMoLa achieves state-of-the-art performance using only single-view RGB-D input, while existing methods require multi-view reconstruction, succeeding across diverse manipulation benchmarks. Our ablations reveal that geometric prediction is the key to driving performance, quantitatively validating that manipulation depends on spatial understanding. Furthermore, the learned codes exhibit effective motion abstraction: applying them to novel scenes produces physically consistent transformations regardless of visual context. Our real-world experiments also confirm this robustness capability, achieving robust manipulation with minimal demonstrations in cluttered environments where geometric reasoning determines success. Thus, we demonstrate that effective motion latents for robot control can better emerge from understanding motion through its three-dimensional effects rather than pixel-level patterns.

</details>

---

### [[20_Research/Papers/大模型/RSPO_Reward-Swap_Policy_Optimization_for_Multi-Turn_LLM_Agents|RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents]]

![[assets/2607.04713_figure.png|800]]

- **arXiv**: [2607.04713](https://arxiv.org/abs/2607.04713)
- **PDF**: https://arxiv.org/pdf/2607.04713
- **详细分析**: [[20_Research/Papers/大模型/RSPO_Reward-Swap_Policy_Optimization_for_Multi-Turn_LLM_Agents|RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents]]
- **作者**: Qiang Liu, Taian Guo, Ruizhi Qiao, Xing Sun
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.02（加权：大模型 0.7，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SPA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Conversely, while employing customized dense process rewards provides richer signals and accelerates convergence, these surrogate rewards may exhibit potential misalignment with the ground-truth outcome rewards. This inconsistency can bias the training direction and ultimately degrade the model's final performance. In this work, we propose Reward-Swap Policy Optimization (RSPO), a method designed to leverage the rich information from dense process rewards to facilitate training with outcome rewards. By utilizing a reward-swap mechanism, RSPO ensures the diversity of sampled trajectories while guaranteeing consistency between the optimization objective and the true outcome rewards, thereby elevating the performance ceiling of the model. We conduct extensive experiments on two challenging agent benchmarks, WebShop and ALFWorld. By applying our method to various reinforcement learning algorithms, including GRPO, PPO, and GiGPO, we demonstrate that RSPO achieves consistent performance improvements across different baselines and benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Do_Vision-Language-Action_Models_Mean_What_They_Say_On_the_Role_of_Faithfulness_in_Embodied_Reasoning|Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning]]

![[assets/2607.04681_figure.png|800]]

- **arXiv**: [2607.04681](https://arxiv.org/abs/2607.04681)
- **PDF**: https://arxiv.org/pdf/2607.04681
- **详细分析**: [[20_Research/Papers/具身智能/Do_Vision-Language-Action_Models_Mean_What_They_Say_On_the_Role_of_Faithfulness_in_Embodied_Reasoning|Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning]]
- **作者**: Matthew Foutter, Matteo Cercola, Lena Wild, Yunshan Wang, Michelle Li, Daniele Gammelli, Marco Pavone
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.5（加权：具身智能 2.7，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

</details>

---

### [[20_Research/Papers/强化学习/SILO_Simulation-in-the-Loop_Sim-to-Real_Transfer_for_Multi-Stage_Cable_Routing|SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing]]

![[assets/2607.04616_figure.png|800]]

- **arXiv**: [2607.04616](https://arxiv.org/abs/2607.04616)
- **PDF**: https://arxiv.org/pdf/2607.04616
- **详细分析**: [[20_Research/Papers/强化学习/SILO_Simulation-in-the-Loop_Sim-to-Real_Transfer_for_Multi-Stage_Cable_Routing|SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing]]
- **作者**: Stone Tao, Jie Xu, Hesam Rabeti, Yashraj Narang, Yijie Guo, Iretiayo Akinola
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SILO: Simulation-in-the-Loop Sim-to-Real Transfer for Multi-Stage Cable Routing》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Linear-deformable manipulation remains challenging due to the complex deformations of objects such as cables and ropes. Prior data-driven approaches, particularly imitation learning, have shown some promise in narrowly defined settings but typically require thousands of demonstrations for specific tasks and cable types, limiting scalability and generalization. We introduce a sim-to-real reinforcement learning (RL) framework for multi-stage cable routing that leverages GPU-parallelized simulation to approximate linear deformable behaviors. Training across thousands of parallel simulations enables the learned policies to generalize across diverse cable geometries and deformation patterns. To bridge the sim-to-real gap, we propose a novel deployment strategy that combines a Simulation In the LOop (SILO) execution framework, localized RL policies, and robust cable state estimation. On real-world cable routing tasks, our approach achieves higher success rates and 2x reduction in cycle times compared to prior state-of-the-art learning methods. To our knowledge, this is the first successful sim-to-real transfer of RL policies for multi-stage cable routing. Videos and additional visualizations are available at https://silo-cable-routing.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Simple-to-Complex_Structured_Demonstrations_for_Vision-Language-Action_Learning|Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning]]

![[assets/2607.04591_figure.jpg|800]]

- **arXiv**: [2607.04591](https://arxiv.org/abs/2607.04591)
- **PDF**: https://arxiv.org/pdf/2607.04591
- **详细分析**: [[20_Research/Papers/具身智能/Simple-to-Complex_Structured_Demonstrations_for_Vision-Language-Action_Learning|Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning]]
- **作者**: Xinchuan Qiu, Yi Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 2.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboNet, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation by integrating visual perception, language understanding, and robot action generation. Existing research has primarily focused on improving model architectures, training strategies, and dataset scale, while little attention has been paid to how demonstrations are collected and organized. We identify demonstration organization as a fundamental yet overlooked aspect of imitation learning, as it directly affects policy learning efficiency, training stability, and policy generalization. To address this gap, we propose a simple-to-complex structured demonstration collection strategy for VLA learning using a dual-arm robotic platform. Our approach systematically organizes data through three general principles: (i) decomposing complex manipulation tasks into progressively learnable sub-skills, (ii) standardizing the interaction environment to reduce unnecessary variability, and (iii) organizing demonstrations according to progressively increasing task complexity. This structured design enables VLA models to first acquire fundamental manipulation skills before learning increasingly complex task compositions, facilitating more effective learning of long-horizon manipulation tasks. We evaluate the proposed strategy on two representative robotic manipulation tasks: block grasping and sorting, and towel folding. Experimental results show consistent improvements in task success rate and training stability compared with the baseline method of directly collecting end-to-end complete task trajectories. These findings highlight demonstration organization as a previously underexplored but important factor in VLA learning and provide practical insights into efficient skill acquisition, scalable dataset construction, and long-horizon robotic manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Mask2Real-WM_Segmentation_Masks_as_a_Sim-to-Real_Bridge_for_Controllable_Dexterous_World_Models|Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models]]

![[assets/2607.04546_figure.png|800]]

- **arXiv**: [2607.04546](https://arxiv.org/abs/2607.04546)
- **PDF**: https://arxiv.org/pdf/2607.04546
- **详细分析**: [[20_Research/Papers/强化学习/Mask2Real-WM_Segmentation_Masks_as_a_Sim-to-Real_Bridge_for_Controllable_Dexterous_World_Models|Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models]]
- **作者**: Riccardo O. Feingold, Davide Liconti, Chenyu Yang, Robert K. Katzschmann
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 4.52（加权：具身智能 2.7，强化学习 0.16，世界模型 1.36，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, Ctrl-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps the predicted masks to photorealistic RGB using a ControlNet-augmented Stable Video Diffusion backbone. The smaller sim-to-real gap in segmentation space enables the dynamics model to benefit from large-scale pretraining on over 50 h of synthetic simulation data, followed by fine-tuning on fewer than 2.5 h of real demonstrations. Experiments on a dexterous pick-and-place benchmark show that mask conditioning and simulation pretraining are both required for per-DoF action controllability across all 23 degrees of freedom. In contrast, monolithic baselines capture broad hand and end-effector trajectories but do not reliably reflect fine-grained, per-joint action effects.

</details>

---

### [[20_Research/Papers/具身智能/VLA_Grounder_Language-Conditioning_Space_Optimization_for_Black-Box_VLA_Models|VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models]]

![[assets/2607.04517_figure.png|800]]

- **arXiv**: [2607.04517](https://arxiv.org/abs/2607.04517)
- **PDF**: https://arxiv.org/pdf/2607.04517
- **详细分析**: [[20_Research/Papers/具身智能/VLA_Grounder_Language-Conditioning_Space_Optimization_for_Black-Box_VLA_Models|VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models]]
- **作者**: Damir Shodiev, Aleksei Staroverov, Nikita Kachaev, Alexey K. Kovalev, Aleksandr I. Panov
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.5，强化学习 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, RL4VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies can be improved by optimizing language space rather than updating action weights. Our method introduces a language-conditioning space policy that translates a human instruction into a short VLA-grounded command using object appearance, spatial relations, and target-grounding cues. The language-conditioning space policy is initialized with a failure-derived command-space prior and optimized with reinforcement learning from sparse task-completion rewards, while the downstream VLA remains fully frozen. This yields language-conditioning space optimization: RL discovers which VLA-grounded commands best elicit successful behavior from the frozen action policy. Experiments on RL4VLA and VL-Think show that language-conditioning space optimization improves success on instruction-sensitive, symbolic, and multi-object manipulation tasks, demonstrating that language can serve as an optimizable variable for a robot foundation models. Website: https://tttonyalpha.github.io/vla_grounder

</details>

---

### [[20_Research/Papers/大模型/Regime-Conditional_Stabilisation_of_LLM-Augmented_Cooperative_Multi-Agent_Reinforcement_Learning|Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2607.04470_figure.png|800]]

- **arXiv**: [2607.04470](https://arxiv.org/abs/2607.04470)
- **PDF**: https://arxiv.org/pdf/2607.04470
- **详细分析**: [[20_Research/Papers/大模型/Regime-Conditional_Stabilisation_of_LLM-Augmented_Cooperative_Multi-Agent_Reinforcement_Learning|Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Faid Keddouri, Sohaib Houhou, Aissa Boulmerka, Nadir Farhi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.92（加权：大模型 0.8，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LAMARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) offer a natural interface for translating human objectives into reward signals for cooperative multi-agent reinforcement learning (MARL), yet the training-time dynamics of this integration remain poorly understood. We show that dynamically updating LLM-generated reward weights during off-policy MARL violates the stationarity assumption of Potential-Based Reward Shaping (PBRS) and contaminates the experience replay buffer, whose stored transitions carry reward labels computed under stale shaping weights. We characterise the result as a regime-dependent failure whose severity depends on how competent the unshaped baseline already is. To control it we propose two stabilisation strategies: a Phase-Based Freeze Schedule that enforces strict stationarity within training phases, and Exponential Moving Average (EMA) smoothing that bounds per-episode weight drift. We evaluate across three cooperative environments and five random seeds with QMIX, complemented by an exploratory VDN extension, yielding a three-regime taxonomy. In the augmentative regime (Simple Spread), where the baseline is functional (74.4 %), EMA significantly improves success to 86.7 % ($+12.3$ pp, $p&lt;0.01$) while naive dynamic updates collapse it to 15.2 %. In the essential regime (Level-Based Foraging), where the baseline is broken (0.1 %), any shaping unlocks the task (95.9 % under EMA). In the supplementary regime (SMAC 3m), where the baseline is near-saturated (98.8 %), stabilised shaping preserves performance (99.9 %) while unstabilised shaping adds variance without gain. These findings establish reward-signal stationarity as a necessary design constraint and indicate that regime placement is a practical predictor of whether dynamic LLM shaping helps or harms.

</details>

---

### [[20_Research/Papers/强化学习/Operator-on-F_complements_value-equivalence_a_planning-time_diagnostic_for_latent_world_models|Operator-on-F complements value-equivalence: a planning-time diagnostic for latent world models]]

![[assets/2607.04464_figure.png|800]]

- **arXiv**: [2607.04464](https://arxiv.org/abs/2607.04464)
- **PDF**: https://arxiv.org/pdf/2607.04464
- **详细分析**: [[20_Research/Papers/强化学习/Operator-on-F_complements_value-equivalence_a_planning-time_diagnostic_for_latent_world_models|Operator-on-F complements value-equivalence: a planning-time diagnostic for latent world models]]
- **作者**: Donna Vakalis
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.36，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Operator-on-F complements value-equivalence: a planning-time diagnostic for latent world models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-model evaluation for model-based reinforcement learning typically asks whether the learned model predicts reward and value well, which can leave planning-relevant errors in the model's latent rollouts unmeasured. We introduce a complementary diagnostic, operator-on-F, that compares a model's k-step latent pushforward to the environment's on an observable subset F, using the model's own predictor. On a TD-MPC2 size sweep over cheetah-run, reward-prediction error stays within [0.028, 0.091] for every model size - only about 3x variation - so an unnormalized reward-fit check has narrow resolution to distinguish them; the (unnormalized) Bellman residual and reward error themselves have weak relationships with return (Spearman -0.10 and -0.30). Operator error spans 0.28 to 2.62 over the same sizes. At 317M the operator error is 2.62 - an order of magnitude above the 0.28-0.36 cluster - and the planning return collapses to 0.9, while reward-prediction error (0.091) is the highest of the five but stays within the same small [0.028, 0.091] range as the rest of the sweep. The rank correlation between operator error and return loss is -0.90 (anchor-bootstrap 95% CI [-0.90, -0.70] at n=5 sizes; leave-one-out removal of any single size leaves it at -0.80 or stronger). The operator also returns informative, architecture-discriminating estimates in a cross-architecture comparison between TD-MPC2 and a pure-SSL latent world model. The operator diagnostic complements value-equivalence rather than replacing it.

</details>

---

### [[20_Research/Papers/具身智能/RoboDojo_A_Unified_Sim-and-Real_Benchmark_for_Comprehensive_Evaluation_of_Generalist_Robot_Manipulation_Policies|RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies]]

![[assets/2607.04434_figure.png|800]]

- **arXiv**: [2607.04434](https://arxiv.org/abs/2607.04434)
- **PDF**: https://arxiv.org/pdf/2607.04434
- **详细分析**: [[20_Research/Papers/具身智能/RoboDojo_A_Unified_Sim-and-Real_Benchmark_for_Comprehensive_Evaluation_of_Generalist_Robot_Manipulation_Policies|RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies]]
- **作者**: Tianxing Chen, Yue Chen, Zixuan Li, Junyuan Tang, Kailun Su, Weijie Wan, Baijun Chen, Haoran Lu, Haowen Yan, Honghao Su, Zhiyang Dou, Kaixuan Wang...
- **cs 子类**: cs.AI, cs.CV, cs.GR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ManipulationNet, RMBench, Real-World, RoboDojo-RealEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

</details>

---

### [[20_Research/Papers/大模型/MechMath_Agent_Team_LLM_Driven_Agents_for_Mathematical_Research|MechMath Agent Team: LLM Driven Agents for Mathematical Research]]

![[assets/2607.04394_figure.png|800]]

- **arXiv**: [2607.04394](https://arxiv.org/abs/2607.04394)
- **PDF**: https://arxiv.org/pdf/2607.04394
- **详细分析**: [[20_Research/Papers/大模型/MechMath_Agent_Team_LLM_Driven_Agents_for_Mathematical_Research|MechMath Agent Team: LLM Driven Agents for Mathematical Research]]
- **作者**: Yichuan Cao, Ruichen Qiu, Junqi Liu, Jiaqi Wang, Dakai Guo, Ruyong Feng, Lihong Zhi, Xiao-Shan Gao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MechMath Agent Team: LLM Driven Agents for Mathematical Research》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI reasoning has become a central focus in contemporary artificial intelligence, largely driven by the success of large language models. However, mathematical research, which is characterized by non-linear derivation paths, rigorous logical requirements, and protracted exploration cycles, poses severe challenges for existing reasoning systems. To overcome these limitations, we present the MechMath Agent Team (MMAT), which is a large language model driven agent designed to serve as a co-pilot throughout the full cycle of mathematical research. We design a tripartite Harness Architecture that decouples system responsibilities into Control, Execution, and Augmentation planes, thereby reconciling rigorous logical control with the agility demanded by open-ended research. Building upon this framework, we instantiate three specialized agents: a Knowledge Base Manager, a Natural Language Prover, and a Formal Language Prover, all operating in a closed loop to produce formally certified mathematical proofs. We evaluate MMAT on open problems in Number Theory, Algebraic Complexity Theory, Differential Algebra, Operator Algebra, and Inequalities. Across a two-month deployment, 11 problems have been solved, demonstrating its capacity to act as a co-pilot throughout the entire research cycle. The contributions are threefold: a general decoupled Harness Architecture for multi-agent mathematical reasoning, its concrete instantiation in the MMAT system, and empirical validation on a diverse suite of open problems.

</details>

---

### [[20_Research/Papers/具身智能/HALO-WA_Hybrid-Attention_Latent-Guided_Online_Reinforcement_Learning_for_World-Action_Models|HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models]]

![[assets/2607.04265_figure.png|800]]

- **arXiv**: [2607.04265](https://arxiv.org/abs/2607.04265)
- **PDF**: https://arxiv.org/pdf/2607.04265
- **详细分析**: [[20_Research/Papers/具身智能/HALO-WA_Hybrid-Attention_Latent-Guided_Online_Reinforcement_Learning_for_World-Action_Models|HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models]]
- **作者**: Angen Ye, Weijie Ke, Xiaofeng Wang, Xinze Chen, Chaojun Ni, Guosheng Zhao, Boyuan Wang, Zheng Zhu, Junjie Xie, Dapeng Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 1，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GR-RL, GigaWorld, HIL-SERL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

</details>

---

### [[20_Research/Papers/大模型/Progress-_and_Reliability-Oriented_Group_Policy_Optimization_for_Agentic_Reinforcement_Learning|Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning]]

![[assets/2607.04242_figure.png|800]]

- **arXiv**: [2607.04242](https://arxiv.org/abs/2607.04242)
- **PDF**: https://arxiv.org/pdf/2607.04242
- **详细分析**: [[20_Research/Papers/大模型/Progress-_and_Reliability-Oriented_Group_Policy_Optimization_for_Agentic_Reinforcement_Learning|Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning]]
- **作者**: Mingxuan Fan, Peiyang Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.3，强化学习 1.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-based reinforcement learning (RL) has become an effective paradigm for improving large language model agents on long-horizon interactive tasks. To obtain finer-grained policy updates than trajectory-level optimization, recent work has moved toward step-level group-based RL, where intermediate steps are grouped and compared within a rollout batch. However, step-level advantage estimation is sensitive to how groups are formed: grouping by broad state keys improves coverage but may compare actions taken under different histories, while enforcing historical consistency yields fairer comparisons at the cost of fragmented groups and missing peer-comparison signal. In this paper, we propose ProGPO (Progress- and Reliability-Oriented Group Policy Optimization), a learned-critic-free method for context-consistent step-level learning. ProGPO keeps exact-prefix action comparison, and complements sparse peer comparisons with transition credit derived from rollout-based state potentials. To estimate these potentials reliably, ProGPO combines semantic expansion with inverse-variance fusion across history depths. We evaluate ProGPO on two challenging agentic tasks, ALFWorld and WebShop, with Qwen2.5-1.5B-Instruct. Results show that ProGPO improves over matched agentic RL baselines under comparable computational overhead, and additional Qwen2.5-3B-Instruct experiments further test the scalability of the proposed method.

</details>

---

### [[20_Research/Papers/具身智能/SoftVTBench_A_Safety-Aware_Visuo-Tactile_Benchmark_for_Physically_Constrained_Robotic_Manipulation_of_Deformable_Objects|SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects]]

![[assets/2607.04234_figure.png|800]]

- **arXiv**: [2607.04234](https://arxiv.org/abs/2607.04234)
- **PDF**: https://arxiv.org/pdf/2607.04234
- **详细分析**: [[20_Research/Papers/具身智能/SoftVTBench_A_Safety-Aware_Visuo-Tactile_Benchmark_for_Physically_Constrained_Robotic_Manipulation_of_Deformable_Objects|SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects]]
- **作者**: Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen, Junjie He, Yang Cui, Yiming Hou, Weitao Zhou, Jiawei Wang, Minglei Li, Dandan Zhang...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AT-VLA, DaXBench, DeMaVLA, DefGraspSim, Meta-World, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deformable object manipulation poses challenges beyond task completion: successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception, and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.

</details>

---

### [[20_Research/Papers/强化学习/Mask-based_Predictive_Representations_for_Reinforcement_Learning|Mask-based Predictive Representations for Reinforcement Learning]]

![[assets/2607.04153_figure.png|800]]

- **arXiv**: [2607.04153](https://arxiv.org/abs/2607.04153)
- **PDF**: https://arxiv.org/pdf/2607.04153
- **详细分析**: [[20_Research/Papers/强化学习/Mask-based_Predictive_Representations_for_Reinforcement_Learning|Mask-based Predictive Representations for Reinforcement Learning]]
- **作者**: Kai Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Mask-based Predictive Representations for Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CURL, DRL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based deep reinforcement learning involves dealing with high-dimensional inputs of image information. It is crucial to abstract effective states from high-dimensional image inputs and limited samples for sample-efficient reinforcement learning. To address this challenge, inspired by fields such as natural language processing and computer vision, we propose a self-supervised task based on mask prediction as an auxiliary task for reinforcement learning. This non-reconstruction method uses the sequence information collected by the agent from the environment and the context information in the sequence to predict the masked information, thereby strengthening the agent's understanding of the task and learning effective representations. Combined with transformers, we find that the model reconstructs the masked input sequence in the latent space. By feeding the compressed representations learned by this method into reinforcement learning models, we observe an improvement in the sample efficiency of reinforcement learning. Moreover, the model outperforms state-of-the-art sample-efficient reinforcement learning methods on multiple continuous and discrete control benchmarks.

</details>

---

### [[20_Research/Papers/机器人/!Imperio,_smolVLA_The_Implications_of_Data_Poisoning_on_Open_Source_Robotics|!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics]]

![[assets/2607.04146_figure.png|800]]

- **arXiv**: [2607.04146](https://arxiv.org/abs/2607.04146)
- **PDF**: https://arxiv.org/pdf/2607.04146
- **详细分析**: [[20_Research/Papers/机器人/!Imperio,_smolVLA_The_Implications_of_Data_Poisoning_on_Open_Source_Robotics|!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics]]
- **作者**: Stefan Bühler, Mark Schutera
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Security

#### 研究背景与动机

《!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

</details>

---

### [[20_Research/Papers/具身智能/Worldscape-MoE_A_Unified_Mixture-of-Experts_World_Model_for_Scalable_Heterogeneous_Action_Control|Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control]]

![[assets/2607.03964_figure.png|800]]

- **arXiv**: [2607.03964](https://arxiv.org/abs/2607.03964)
- **PDF**: https://arxiv.org/pdf/2607.03964
- **详细分析**: [[20_Research/Papers/具身智能/Worldscape-MoE_A_Unified_Mixture-of-Experts_World_Model_for_Scalable_Heterogeneous_Action_Control|Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control]]
- **作者**: Jianjie Fang, Yongyan Xu, Ziyou Wang, Chen Gao, Yuchao Huang, Zhaolu Wang, Rongze Tang, Mingyuan Jia, Baining Zhao, Weichen Zhang, Xin Zhang, Haisheng Su...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.2，大模型 0.1，世界模型 1，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, HY-World, Hand2World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

</details>

---

### [[20_Research/Papers/强化学习/Explainable_Reinforcement_Learning_for_Adaptive_Traffic_Signal_Control|Explainable Reinforcement Learning for Adaptive Traffic Signal Control]]

![[assets/2607.03703_figure.png|800]]

- **arXiv**: [2607.03703](https://arxiv.org/abs/2607.03703)
- **PDF**: https://arxiv.org/pdf/2607.03703
- **详细分析**: [[20_Research/Papers/强化学习/Explainable_Reinforcement_Learning_for_Adaptive_Traffic_Signal_Control|Explainable Reinforcement Learning for Adaptive Traffic Signal Control]]
- **作者**: Dickens Kwesiga, Nishu Choudhary, Angshuman Guin, Michael Hunter
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Explainable Reinforcement Learning for Adaptive Traffic Signal Control》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has emerged as a powerful paradigm for adaptive traffic signal control. However, in safety-critical infrastructure like traffic control, the opaque, black-box nature of deep RL models poses challenges for transportation agency acceptance, regulatory compliance, operational trust, troubleshooting, and fine-tuning. To bridge this gap between high-performance optimization and human-comprehensible interpretability, this effort introduces a novel, explainable entity centric RL framework for safe and transparent traffic signal control. Rather than processing traffic states through monolithic, flat vectors, the proposed architecture disaggregates real-time intersection observations into distinct, high-dimensional lane entities and phase temporal configurations to inherently preserve the structural topology and geometric configurations of the intersection. Relational dependencies and inter-lane conflicts are dynamically extracted via a dual-stage attention network featuring sequential multi-head cross-attention and self-attention blocks. This design yields a real time affinity matrix that quantifies the direct influence of signal phases on specific approach volumes and queues, providing full visual and analytical interpretability. To ensure strict operational reliability, a deterministic action-masking interface is integrated directly into the Proximal Policy Optimization pipeline, explicitly blocking invalid phase transitions to guarantee absolute compliance with established signal timing and safety constraints. Evaluated in a microscopic simulation environment, outperforms state-of-the-art baselines in delay minimization. More importantly, the emergent attention weights align precisely with established traffic engineering principles, offering an auditable, trust-enabling, and deployable architecture for next-generation adaptive traffic control systems.

</details>

---

### [[20_Research/Papers/大模型/Agent_Reinforcement_Learning_via_Pivotal-Aware_Self-Feedback_Retry|Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry]]

![[assets/2607.03702_figure.png|800]]

- **arXiv**: [2607.03702](https://arxiv.org/abs/2607.03702)
- **PDF**: https://arxiv.org/pdf/2607.03702
- **详细分析**: [[20_Research/Papers/大模型/Agent_Reinforcement_Learning_via_Pivotal-Aware_Self-Feedback_Retry|Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry]]
- **作者**: Weiyang Guo, Zesheng Shi, Longhui Zhang, Zeen Zhu, Min Zhang, Jing Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.4（加权：大模型 0.8，强化学习 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ARL, MetaRL, PivoARL, SearchQA, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have shown strong decision-making capabilities in long-horizon interactive tasks, yet they still struggle to effectively leverage failed trajectories: full retries incur high interaction costs, while experience retrieval tends to dilute critical experience signals. To address this, we propose PivoARL, a self-feedback retry framework for experience exploitation in LLM agents. PivoARL identifies the pivotal erroneous turn through structured reflection and performs local retry only from the corresponding pivotal state, thereby reusing the correct prefix and reducing redundant interactions. From an information-gain perspective, we further show that pivotal retry concentrates useful experience signals near the error boundary, mitigating the signal dilution caused by state-agnostic experience utilization. Based on this insight, we design a pivotal-aware credit assignment mechanism that rewards correct prefixes while isolating erroneous suffixes, and optimize reflection quality through implicit reflection returns. We conduct a systematic evaluation on 4 agent tasks and 7 search-based QA benchmarks. Results show that PivoARL achieves significant improvements on Pass@2/3 across all tasks, with an average gain of about 11.5\% over MetaRL. Moreover, benefiting from contrastive preference signals induced by pivotal turns, PivoARL also consistently improves Pass@1 on over 80\% of the tasks. On Minesweeper environment, PivoARL improves over GiGPO by more than 45\% and reduces interaction turns by about 42\% on average compared with full-retry methods. Code is available at https://github.com/yuki-younai/PivoARL.

</details>

---

### [[20_Research/Papers/大模型/Don't_Blame_the_Large_Language_Model_How_Scaffolding_Evolution_Shapes_Coding_Agent_Quality|Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality]]

![[assets/2607.03691_figure.png|800]]

- **arXiv**: [2607.03691](https://arxiv.org/abs/2607.03691)
- **PDF**: https://arxiv.org/pdf/2607.03691
- **详细分析**: [[20_Research/Papers/大模型/Don't_Blame_the_Large_Language_Model_How_Scaffolding_Evolution_Shapes_Coding_Agent_Quality|Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality]]
- **作者**: Oussama Ben Sghaier, Hao Li, Bram Adams, Ahmed E. Hassan
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Don't Blame the Large Language Model: How Scaffolding Evolution Shapes Coding Agent Quality》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents, autonomous systems that use large language models (LLMs) to resolve software engineering tasks, rely on agentic scaffolding: a middleware layer in between a developer and a large language model that orchestrates system prompts, tool execution, context management, and iterative reasoning loops. While these scaffoldings evolve at extreme velocities, no study has examined how this evolution affects agent quality (i.e., effectiveness and efficiency) over time. Practitioners regularly report quality regressions after scaffolding updates, yet consistently attribute them to the underlying model rather than the scaffolding itself. In this paper, we address this gap by conducting the first controlled longitudinal study that isolates the scaffolding's contribution. Unlike prior work that fixes the scaffolding and varies the model, we fix the model and vary only the scaffolding, evaluating 35 sequential releases to measure their impact on agent effectiveness and efficiency. We first empirically study the development and release evolution of five major open-source scaffoldings (i.e., Codex, Qwen Code, Gemini, OpenCode, and OpenHands), revealing extreme release velocities exceeding two releases per day and thousands of issues within months. We then perform a controlled deep dive into 35 sequential releases of the Qwen Code CLI, evaluating each against 50 stratified SWE-bench Verified tasks while holding the underlying LLM constant. We trace the resulting quality fluctuations to specific development patterns and architectural components, and illustrate our findings with concrete qualitative evidence linking individual pull requests to measured quality shifts.

</details>

---

### [[20_Research/Papers/具身智能/HiMe_Hierarchical_Embodied_Memory_for_Long-Horizon_Vision-Language-Action_Control|HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control]]

![[assets/2607.03449_figure.png|800]]

- **arXiv**: [2607.03449](https://arxiv.org/abs/2607.03449)
- **PDF**: https://arxiv.org/pdf/2607.03449
- **详细分析**: [[20_Research/Papers/具身智能/HiMe_Hierarchical_Embodied_Memory_for_Long-Horizon_Vision-Language-Action_Control|HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control]]
- **作者**: Li Ji, Siyin Wang, Pengfang Qian, Xiaopeng Yu, Yihai Tian, Zhaoye Fei, Jingjing Gong, Xipeng Qiu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 3.3，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations. Existing solutions face a ''frequency-competence paradox,'' where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through ''Add, Update, and Delete'' operations. This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct its internal knowledge based on human preferences.

</details>

---

### [[20_Research/Papers/强化学习/Hierarchical_Multi-Agent_Reinforcement_Learning_for_Carbon-Aware_AI_Data_Centers_in_Power_Distribution_Systems|Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems]]

![[assets/2607.03324_figure.png|800]]

- **arXiv**: [2607.03324](https://arxiv.org/abs/2607.03324)
- **PDF**: https://arxiv.org/pdf/2607.03324
- **详细分析**: [[20_Research/Papers/强化学习/Hierarchical_Multi-Agent_Reinforcement_Learning_for_Carbon-Aware_AI_Data_Centers_in_Power_Distribution_Systems|Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems]]
- **作者**: Hyunsoo Lee, Panggah Prabawa, Dae-Hyun Choi, Joongheon Kim
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Hierarchical Multi-Agent Reinforcement Learning for Carbon-Aware AI Data Centers in Power Distribution Systems》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CA-MARL, HRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Eco-friendly energy management for artificial intelligence data centers (AIDCs) is crucial because of the significant increase in energy consumption-induced carbon emissions from AIDCs resulting from the rapid expansion of AI applications. This paper proposes a hierarchical carbon-aware multi-agent reinforcement learning (CA-MARL) framework for robust and efficient operations of AIDCs under uncertainties while ensuring low-carbon operation of power distribution systems. The framework comprises a workload manager (WM) agent and multiple local AIDC agents trained using a multi-agent transformer method, corresponding to a global AIDC aggregator and a local AIDC operator, respectively. Leveraging AIDC operation data along with nodal carbon intensity (NCI) calculated from the carbon emission flow-integrated distribution system operator problem, the WM agent spatially allocates AI training and inference jobs among all AIDCs. Based on the jobs allocated from the WM agent and NCI information, each AIDC agent schedules economical and eco-friendly operations of the AIDC by performing the following tasks: i) temporal shifting of training jobs, ii) spatial allocation of training graphics processing unit (GPU) blocks and inference GPUs within the AIDC, and iii) control of the supply air temperature of the cooling system. The effectiveness of the proposed framework was assessed using an IEEE 33-node power distribution system.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Operators_and_Benchmarking_Toward_Reusable_and_Deployable_Embodied_Intelligence_Systems|Embodied Operators and Benchmarking: Toward Reusable and Deployable Embodied Intelligence Systems]]

![[assets/2607.03283_first_page.png|800]]

- **arXiv**: [2607.03283](https://arxiv.org/abs/2607.03283)
- **PDF**: https://arxiv.org/pdf/2607.03283
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Operators_and_Benchmarking_Toward_Reusable_and_Deployable_Embodied_Intelligence_Systems|Embodied Operators and Benchmarking: Toward Reusable and Deployable Embodied Intelligence Systems]]
- **作者**: Junwu Xiong, Jiaxuan Gao, Wei Chai, Renxing Chen, Yuzhen Li, Yu Guo, Yucheng Guo, Mingxi Luo, Wenyang Ma, Yiyun Mou, Yifei Zhang, Chen Zhou...
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.5，大模型 0.1，世界模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Embodied Operators and Benchmarking: Toward Reusable and Deployable Embodied Intelligence Systems》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, OpenVLA, YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligence systems require not only end-to-end policy models, but also reusable functional modules that transform multimodal observations, robot states, human demonstrations, and task contexts into structured representations, decisions, trajectories, control references, and system services. This work defines these modules as embodied operators and studies them as independent yet composable units in embodied intelligence pipelines. We clarify their definition boundary, emphasizing task semantics, standardized input-output contracts, deployability, reusability, and multi-layer optimizability. We further construct a taxonomy covering five categories: detection and segmentation, spatial localization and 3D understanding, hand motion recovery, embodied foundation models and task-decision operators, and planning, control, and system support operators. For each category, we summarize representative functions, technical paradigms, application roles, and practical limitations. Beyond taxonomy, we propose a multi-dimensional benchmark framework that evaluates embodied operators in terms of correctness, end-to-end efficiency, resource usage, temporal stability, portability, interface compatibility, deployment reliability, and downstream task utility. We also discuss workflow-level operator acceleration and open challenges in operator composition, data standardization, world models, VLA safety, edge deployment, and real-world application value. Overall, this work argues that embodied operators should be optimized and evaluated as holistic deployable components, providing a foundation for reusable, scalable, and verifiable embodied intelligence systems.

</details>

---

### [[20_Research/Papers/具身智能/AnchorVLA_Bridging_Discrete_Decisions_and_Continuous_Trajectories_for_Vision-Language-Action_Planning|AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning]]

![[assets/2607.03182_figure.jpg|800]]

- **arXiv**: [2607.03182](https://arxiv.org/abs/2607.03182)
- **PDF**: https://arxiv.org/pdf/2607.03182
- **详细分析**: [[20_Research/Papers/具身智能/AnchorVLA_Bridging_Discrete_Decisions_and_Continuous_Trajectories_for_Vision-Language-Action_Planning|AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning]]
- **作者**: Qi Liu, Yabei Li, Hongsong Wang, Heng Zhang, Lei He
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AnchorVLA, AutoVLA, DiffVLA, LinkVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

</details>

---

### [[20_Research/Papers/强化学习/ACPO_Adaptive_Credit_Policy_Optimization_via_Fine-Grained_Surrogate_Entropy|ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy]]

![[assets/2607.03126_figure.png|800]]

- **arXiv**: [2607.03126](https://arxiv.org/abs/2607.03126)
- **PDF**: https://arxiv.org/pdf/2607.03126
- **详细分析**: [[20_Research/Papers/强化学习/ACPO_Adaptive_Credit_Policy_Optimization_via_Fine-Grained_Surrogate_Entropy|ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy]]
- **作者**: Zijun Xie, Yuyang You, Yongzhi Li, Enlei Gong, Zeyu Chen, Quan Chen, Yanhua Cheng, Peng Jiang, Yadong Mu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has substantially improved the reasoning ability of large language models (LLMs), but sparse outcome rewards still make token-level credit assignment difficult. Existing scalable RL methods typically assign trajectory-level rewards uniformly across tokens, while recent entropy-aware approaches either rely on coarse detached heuristics or directly optimize true entropy, which can introduce non-local gradient components misaligned with sampled-token policy updates. We propose Adaptive Credit Policy Optimization (ACPO), a token-level credit assignment framework based on a mode-local surrogate entropy. ACPO asymmetrically modulates policy updates by emphasizing uncertain decisions in successful rollouts and overconfident tokens in failed rollouts. We show that the surrogate admits deterministic entropy bounds and, under modal alignment and proximal updates, preserves the policy-gradient direction to leading order. Experiments on mathematical reasoning and coding benchmarks, including AIME 2025 and HumanEvalPro, show that ACPO consistently improves over strong RL baselines such as DAPO, GTPO, and SAPO.

</details>

---

### [[20_Research/Papers/具身智能/Differential_Amplifier-Inspired_AmpAttention_for_Multi-View_Robotic_Manipulation|Differential Amplifier-Inspired AmpAttention for Multi-View Robotic Manipulation]]

![[assets/2607.02845_figure.png|800]]

- **arXiv**: [2607.02845](https://arxiv.org/abs/2607.02845)
- **PDF**: https://arxiv.org/pdf/2607.02845
- **详细分析**: [[20_Research/Papers/具身智能/Differential_Amplifier-Inspired_AmpAttention_for_Multi-View_Robotic_Manipulation|Differential Amplifier-Inspired AmpAttention for Multi-View Robotic Manipulation]]
- **作者**: Jin Yang, Ping Wei, Nanning Zheng
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Differential Amplifier-Inspired AmpAttention for Multi-View Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-view robotic manipulation methods with the attention mechanism have recently achieved significant progress in both training efficiency and task performance. However, the inherent redundancy, occlusion, and viewpoint dependency in robotic view images often lead to severe attention drift. To address this challenge, we propose AmpAttention, a novel attention mechanism inspired by differential amplifiers in analog circuits. It aims to suppress attention noise and capture high signal-to-noise ratio signals for more reliable perception. Based on this, we introduce the RVAF model, which integrates task-guided intra-view and inter-view AmpAttention. Compared to previous state-of-the-art methods, RVAF achieves the optimal average success rate across 18 RLBench tasks (249 variations) while reducing training time by 33.3\%. RVAF also demonstrates strong potential in real-world high-precision tasks, exemplified by its ability to pick up a dart and accurately insert it into the red bullseye. Furthermore, we extend RVAF to RVAF++ by incorporating the SAM2 image encoder. RVAF++ achieves substantial gains on high-precision tasks, achieving a 91\% success rate on the `insert peg' task. More qualitative results are provided at the anonymous project website https://anonymous.4open.science/w/RVAF-Anonymization.

</details>

---

### [[20_Research/Papers/具身智能/iFLYTEK-Embodied-Omni_Technical_Report|iFLYTEK-Embodied-Omni Technical Report]]

![[assets/2607.02542_first_page.png|800]]

- **arXiv**: [2607.02542](https://arxiv.org/abs/2607.02542)
- **PDF**: https://arxiv.org/pdf/2607.02542
- **详细分析**: [[20_Research/Papers/具身智能/iFLYTEK-Embodied-Omni_Technical_Report|iFLYTEK-Embodied-Omni Technical Report]]
- **作者**: Yuan Zhang, Jingfei Ni, Guanchen Lu, Shiqi Zhang, Qingshan Xu, Chi Liu, Xin Nie, Wenjie Xu, Lin Gao, Zhiyuan Cheng, Mingxin Zhou, Jiajia Wu...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.4，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《iFLYTEK-Embodied-Omni Technical Report》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose embodied agents must understand multimodal instructions, anticipate how their environment will evolve, and produce precise control actions over extended horizons. Existing approaches typically specialize in visual-language reasoning, video-based world modeling, or action generation, while cascaded pipelines that first synthesize future observations and then infer actions can introduce interface bottlenecks and compound prediction errors. We present iFLYTEK-Embodied-Omni, a unified multimodal foundation model that jointly models vision(videos and images), language, and action within a single Omni framework. Its modality-specific visual-language, video-generation, and action-generation components communicate through shared multimodal self-attention. This design establishes brain-cerebellum collaboration: the vision-language modeland video generation model form a high-level brain for instruction understanding, task planning, progress tracking, and future visual-state prediction, whereas the action generation modelserves as a low-level cerebellum that directly converts planned subgoals and shared multimodal context into executable action chunks. To develop these capabilities, we combine action-annotated and action-free embodied videos from human demonstrations and robot interactions with embodied reasoning, embodied perception, and general-purpose image-text data to construct a comprehensive dataset. We further adopt a four-stage strategy that progressively trains the VLM, VGM, and AGM before jointly fine-tuning the complete model.

</details>

---

### [[20_Research/Papers/具身智能/Closing_the_Reality_Gap_Zero-Shot_Sim-to-Real_Deployment_for_Dexterous_Force-Based_Grasping_and_Manipulation|Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

![[assets/2601.02778_first_page.png|800]]

- **arXiv**: [2601.02778](https://arxiv.org/abs/2601.02778)
- **PDF**: https://arxiv.org/pdf/2601.02778
- **详细分析**: [[20_Research/Papers/具身智能/Closing_the_Reality_Gap_Zero-Shot_Sim-to-Real_Deployment_for_Dexterous_Force-Based_Grasping_and_Manipulation|Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- **作者**: Zhe Zhao, Haoyu Dong, Zhengmao He, Yang Li, Xinyu Yi, Zhibin Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.8（加权：具身智能 3.9，强化学习 0.4，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities, but training control policies that can directly deploy on real hardware remains difficult due to contact-rich physics and imperfect actuation. We close this gap with a practical sim-to-real reinforcement learning (RL) framework that utilizes dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling to bridge the actuation gaps with randomization of non-ideal effects such as backlash, torque-speed saturation. Using an asymmetric actor-critic PPO pipeline trained entirely in simulation, our policies deploy directly to a five-finger hand. The resulting policies demonstrated two essential skills: (1) command-based, controllable grasp force tracking, and (2) reorientation of objects in the hand, both of which were robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with effective sensing/actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

</details>

---
