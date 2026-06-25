# cs.LG | Machine Learning | 2026-06-23

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/具身智能/AutoDex_An_Automated_Real-World_System_for_Dexterous_Grasping_Data_Collection|AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection]]

![[assets/2606.23689_figure.png|800]]

- **arXiv**: [2606.23689](https://arxiv.org/abs/2606.23689)
- **PDF**: https://arxiv.org/pdf/2606.23689
- **详细分析**: [[20_Research/Papers/具身智能/AutoDex_An_Automated_Real-World_System_for_Dexterous_Grasping_Data_Collection|AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection]]
- **作者**: Mingi Choi, Gunhee Kim, Jisoo Kim, Taeksoo Kim, Taeyun Ha, Jongbin Lim, Hanbyul Joo
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.7，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robust dexterous grasping requires real-world data that records the physical outcomes of grasp attempts. Such data is hard to obtain at scale: teleoperation yields valid physical outcomes but is slow and operator-biased, while simulation-based generation is cheap and scalable but cannot certify contact validity. A natural solution is to generate candidate grasps and verify them on real hardware, but this scales only if the entire collection loop (perception, execution, labeling, and reset) runs without human intervention. We present AutoDex, an automated real-world data-collection system that closes this loop: for each candidate from a replaceable generator, it localizes the object under severe hand-object occlusion with dense 20-camera perception, executes collision-monitored robot motions, labels lift-and-hold success or failure, and actively resets the object between trials to expose additional candidates across stable poses. The result is a reusable database of physically labeled grasp trials that downstream systems can query by retrieval and feasibility filtering. Using AutoDex, we collect 3,593 grasp trials across Allegro and Inspire hands on 100 diverse objects, with synchronized multi-view observations and robot-state logs. For a matched 500-trajectory collection, AutoDex requires 10.3 h versus 49.4 h for teleoperation, yielding a 4.8x throughput improvement, and grasps retrieved from the AutoDex-validated database succeed 76% versus 34% for simulation-only validation. Code and data will be publicly released.

</details>

---

### [[20_Research/Papers/具身智能/SkyJEPA_Learning_Long-Horizon_World_Models_for_Zero-Shot_Sim-to-Real_Control_of_Quadrotors|SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors]]

![[assets/2606.23444_figure.png|800]]

- **arXiv**: [2606.23444](https://arxiv.org/abs/2606.23444)
- **PDF**: https://arxiv.org/pdf/2606.23444
- **详细分析**: [[20_Research/Papers/具身智能/SkyJEPA_Learning_Long-Horizon_World_Models_for_Zero-Shot_Sim-to-Real_Control_of_Quadrotors|SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors]]
- **作者**: Pratyaksh Rao, Wancong Zhang, Randall Balestriero, Yann LeCun, Giuseppe Loianno
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 3.82（加权：具身智能 1.8，强化学习 0.16，世界模型 1.16，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors》归入 具身智能、世界模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate dynamics models are critical for informed decision-making in robotic systems, particularly for agile aerial vehicles operating under uncertainty. Neural network dynamics models are attractive for capturing complex nonlinear effects, but existing predictive approaches struggle with long-horizon forecasting because their autoregressive rollout mechanism amplifies errors over time. Joint Embedding Predictive Architectures (JEPAs) offer a compelling alternative by modeling dynamics in latent space, yet prior JEPA-style methods for robot navigation have been studied primarily for kinematic-level planning, with limited investigation in high-frequency control. In this work, we introduce the JEPA-style model for real-time quadrotor control. The proposed approach combines a latent dynamics model with a novel physics-inspired prober that maps frozen latents to interpretable state, enabling physically grounded long-horizon prediction. Additionally, we combine the learned model with a sampling-based optimal control solution to take advantage of its predictive capabilities for real-time control on embedded hardware. Finally, to reduce the dependence on expensive and unsafe real-world data collection, we develop a structured pipeline for automated dataset generation. Extensive open-loop and outdoor closed-loop experiments demonstrate accurate prediction, robust zero-shot sim-to-real transfer, and strong generalization across diverse operating conditions.

</details>

---

### [[20_Research/Papers/强化学习/LOLLA_Deep_Reinforcement_Learning_for_Closed-Loop_Link_Adaptation_Towards_a_GPU-Accelerated_AI-RAN|LOLLA: Deep Reinforcement Learning for Closed-Loop Link Adaptation Towards a GPU-Accelerated AI-RAN]]

![[assets/2606.23110_figure.png|800]]

- **arXiv**: [2606.23110](https://arxiv.org/abs/2606.23110)
- **PDF**: https://arxiv.org/pdf/2606.23110
- **详细分析**: [[20_Research/Papers/强化学习/LOLLA_Deep_Reinforcement_Learning_for_Closed-Loop_Link_Adaptation_Towards_a_GPU-Accelerated_AI-RAN|LOLLA: Deep Reinforcement Learning for Closed-Loop Link Adaptation Towards a GPU-Accelerated AI-RAN]]
- **作者**: Rui Wang, Linchao Zhang, Qiang Liu, Kun Yang
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 1.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《LOLLA: Deep Reinforcement Learning for Closed-Loop Link Adaptation Towards a GPU-Accelerated AI-RAN》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, GenRL, MAC-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Outer-loop link adaptation (OLLA) is widely deployed in 5G NR to track channel variations, yet its reliance on first-order, single-bit feedback degrades performance significantly under high-mobility and fast-varying channels. This paper presents LOLLA (Learned Outer-Loop Link Adaptation), a deep reinforcement learning framework that replaces the conventional OLLA staircase with a learned, continuous SINR offset conditioned on rich PHY/MAC telemetry inaccessible to OLLA. The offset modulates the SINR-to-MCS lookup table, preserving 3GPP-compliant MCS selection and provably subsuming the conventional OLLA update rule. A Proximal Policy Optimization (PPO) policy trained under a Lagrangian block error rate (BLER) constraint automatically enforces tunable reliability targets from 1% to 15% without manual penalty calibration. The framework is realized as the first closed-loop AI-native control dApp on a GPU-accelerated 5G NR stack, achieving end-to-end control latencies under 500 microseconds. Evaluations under 3GPP TDL channel models demonstrate 15% to 92% throughput gains over OLLA across Doppler frequencies up to 400 Hz, while attaining a Pareto frontier that strictly dominates OLLA across all evaluated reliability targets. The learned policy generalizes to unseen channel models and scales to eight concurrent UEs under shared-resource scheduling. In the uplink formulation, the gNB directly observes decoding outcomes, enabling simulation-to-deployment parity.

</details>

---

### [[20_Research/Papers/具身智能/NAC_Neural_Action_Codec_for_Vision-Language-Action_Models|NAC: Neural Action Codec for Vision-Language-Action Models]]

![[assets/2606.21372_figure.png|800]]

- **arXiv**: [2606.21372](https://arxiv.org/abs/2606.21372)
- **PDF**: https://arxiv.org/pdf/2606.21372
- **详细分析**: [[20_Research/Papers/具身智能/NAC_Neural_Action_Codec_for_Vision-Language-Action_Models|NAC: Neural Action Codec for Vision-Language-Action Models]]
- **作者**: Ahad Jawaid, Yu Xiang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《NAC: Neural Action Codec for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, ResNet, SEANet, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models rely on discrete action tokenizers to bridge continuous robot control and autoregressive sequence modeling, yet existing tokenizers often trade off between compression, latency, and downstream performance. We revisit this design through the lens of neural audio codecs-convolutional encoder-decoder architectures with residual vector quantization that serve as the standard front end for audio foundation models. Motivated by their success, we introduce the Neural Action Codec (NAC), which treats short robot action trajectories as multi-channel 1D signals and compresses them using a multi-scale RVQGAN architecture. We observe that audio-specific mel-spectrogram objectives are ill-suited for kinematic signals; however, by replacing them with simple time-domain and non-mel spectral reconstruction losses, audio-codec-style models can autoencode actions with high fidelity without substantial architectural changes. NAC provides a compact, ordered token space via offset codebooks, enabling standard autoregressive policies to operate over short, structured sequences. Meanwhile, a Vocos-style decoder with an ISTFT head and adversarial discriminators recovers smooth, detailed trajectories. Across LIBERO-10, RoboMimic, and a suite of real-world manipulation tasks, NAC achieves lower reconstruction error and higher success rates than binning, FAST, and prior VQ-based tokenizers at comparable or better compression rates. These results demonstrate that repurposed neural audio codecs offer a strong, practical backbone for learned action tokenization in modern VLAs.

</details>

---

### [[20_Research/Papers/具身智能/Inductive_Generalization_for_Robotic_Manipulation|Inductive Generalization for Robotic Manipulation]]

![[assets/2606.20999_figure.png|800]]

- **arXiv**: [2606.20999](https://arxiv.org/abs/2606.20999)
- **PDF**: https://arxiv.org/pdf/2606.20999
- **详细分析**: [[20_Research/Papers/具身智能/Inductive_Generalization_for_Robotic_Manipulation|Inductive Generalization for Robotic Manipulation]]
- **作者**: Annabella Macaluso, Haochen Zhang, Ishaan Masilamony, Yingshan Chang, Yonatan Bisk
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Inductive Generalization for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding the generalization capabilities of visuomotor policies is essential in the development of capable robotic agents. Generalizable models learn structures that transfer across domains. However, in practice, visuomotor policies test performance by interpolation on known distributions using unstructured domain shifts (e.g. lighting, clutter, diverse objects). We argue that to measure generalization capabilities we must instead test the inductive capacity of policies on progressively harder, out-of-distribution task variants. We call this inductive generalization, drawing directly on how axis-based evaluation has revealed inherent generalization limitations in language models (e.g. sequence length, counting) arXiv:2502.00197 . We provide a reusable and formal evaluation protocol for measuring inductive generalization in any manipulation policy, and establish baselines showing that existing paradigms fail this test; e.g. SoTA Vision-Language-Action models and find that policies that appear to generalize to prior domain shifts (distractors, etc) fail inductive generalization tests. These results expose a class of learning challenges orthogonal to those addressed by data and model scaling in robot learning, yet are imperative to solve in order to realize general purpose robots.

</details>

---

### [[20_Research/Papers/强化学习/Evolutionary_Discovery_of_Developmental_Reward_Schedules_in_Deep_Reinforcement_Learning|Evolutionary Discovery of Developmental Reward Schedules in Deep Reinforcement Learning]]

![[assets/2606.20858_figure.png|800]]

- **arXiv**: [2606.20858](https://arxiv.org/abs/2606.20858)
- **PDF**: https://arxiv.org/pdf/2606.20858
- **详细分析**: [[20_Research/Papers/强化学习/Evolutionary_Discovery_of_Developmental_Reward_Schedules_in_Deep_Reinforcement_Learning|Evolutionary Discovery of Developmental Reward Schedules in Deep Reinforcement Learning]]
- **作者**: Alan Nadelsticher Ruvalcaba
- **cs 子类**: cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Evolutionary Discovery of Developmental Reward Schedules in Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Evolutionary_RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The temporal structure of reward composition in reinforcement learning (RL) is typically hand-designed and held fixed throughout training, leaving the progression of motivational priorities largely unexplored. In this work, we propose an evolutionary framework for discovering developmental reward schedules, in which three distinct biologically inspired motivational components -- agency, novelty, and reactivity -- are combined through time-varying weights that dynamically shift over the course of training. Evaluated on two sparse-reward MiniGrid tasks: DoorKey-6x6 and KeyCorridorS3R1, our framework compares the generalizability of four evolutionary algorithms: CMA-ES, xNES, DE, and L-SHADE against an extrinsically motivated baseline (our main comparison point), and three additional hand-designed methods. On DoorKey-6x6, all evolved methods outperform the non-evolved baselines, with L-SHADE achieving the best performance -- an approximate relative mean improvement of 11.4% over the extrinsic only baseline. On KeyCorridorS3R1, CMA-ES achieves the best overall performance, with the remaining evolved methods showing weaker and less reliable generalization capability compared to the extrinsic only baseline. Interestingly, the discovered schedules diverge from our defined developmental ordering, with novelty consistently emerging as the dominant early signal during training, across both tasks. Collectively, our results position evolutionary optimization as a promising approach for developmental reward schedule discovery in deep reinforcement learning, and suggest that what evolution finds to be optimal in computational settings may differ from what it finds to be optimal in biology. The code for this project can be found at: https://github.com/alannadels/Evolutionary_RL.git.

</details>

---

### [[20_Research/Papers/具身智能/Empowering_Embodied_AI_in_6G_Networks_Architecture,_Enablers,_and_Open_Challenges|Empowering Embodied AI in 6G Networks: Architecture, Enablers, and Open Challenges]]

![[assets/2606.20592_figure.png|800]]

- **arXiv**: [2606.20592](https://arxiv.org/abs/2606.20592)
- **PDF**: https://arxiv.org/pdf/2606.20592
- **详细分析**: [[20_Research/Papers/具身智能/Empowering_Embodied_AI_in_6G_Networks_Architecture,_Enablers,_and_Open_Challenges|Empowering Embodied AI in 6G Networks: Architecture, Enablers, and Open Challenges]]
- **作者**: Junaid Sajid, Sheikh Salman Hassan, Wenshuai Liu, Yan Kyaw Tun, Yaru Fu, Nguyen H. Tran, Zhu Han, Cedomir Stefanovic, Tharmalingam Ratnarajah, Muhammad Mahtab Alam
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 2.4，大模型 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Empowering Embodied AI in 6G Networks: Architecture, Enablers, and Open Challenges》归入 具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied artificial intelligence (AI) is emerging as a key driver of the sixth-generation (6G) wireless networks by enabling agents that continuously perceive, communicate, and act in dynamic physical environments. Unlike conventional AI systems that process disembodied data, embodied agents such as robots, autonomous vehicles, and extended reality (XR) devices operate through closed-loop perception-communication-action (PCA) interactions, where communication performance directly affects physical behavior, control stability, and task success. However, existing AI-native wireless architectures remain largely connectivity-centric and are not designed to support task-driven embodied intelligence at large scale. Therefore, we present a holistic framework for embodied AI-native 6G systems, in which communication, sensing, computation, and control are jointly designed as a unified closed-loop infrastructure. We introduce a system-level PCA architecture, discuss key enabling technologies and representative applications, and highlight major open challenges in multimodal intelligence, edge-aware deployment, evaluation, trustworthiness, and practical implementation. Our central argument is that future 6G systems must evolve from intelligent communication platforms into active enablers of embodied physical intelligence.

</details>

---
