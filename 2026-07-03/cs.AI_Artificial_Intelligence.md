# cs.AI | Artificial Intelligence | 2026-07-03

#arxiv #ComputerScience

**论文数**: 42

### [[20_Research/Papers/大模型/What_LLM_Agents_Say_When_No_One_Is_Watching_Social_Structure_and_Latent_Objective_Emergence_in_Multi-Agent_Debates|What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates]]

![[assets/2607.02507_figure.png|800]]

- **arXiv**: [2607.02507](https://arxiv.org/abs/2607.02507)
- **PDF**: https://arxiv.org/pdf/2607.02507
- **详细分析**: [[20_Research/Papers/大模型/What_LLM_Agents_Say_When_No_One_Is_Watching_Social_Structure_and_Latent_Objective_Emergence_in_Multi-Agent_Debates|What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates]]
- **作者**: Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, Shahriar Noroozizadeh
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR responses that are recorded but never shown to the other participant. Across 10 models, 3 scenarios, and 5 variations within each scenario, alignment-inducing settings produce systematic public-OTR divergence in the targeted agent, with its decision divergence rising from a $\sim$3% baseline to roughly 40%. The effect is consistent across four aggregate analyses: stance, semantic similarity, natural language inference, and survey responses. In some cases, the OTR response explicitly attributes public accommodation to relational pressures, such as career risk or sponsorship obligation. The findings suggest that agent evaluation should extend beyond explicit goals and detect emergent objectives. We present a dual-channel evaluation framework and complementary behavioral measures that operationalize this assessment.

</details>

---

### [[20_Research/Papers/大模型/Reasoning_LLM_Improves_Speaker_Recognition_in_Long-form_TV_Dramas|Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas]]

![[assets/2607.02504_figure.png|800]]

- **arXiv**: [2607.02504](https://arxiv.org/abs/2607.02504)
- **PDF**: https://arxiv.org/pdf/2607.02504
- **详细分析**: [[20_Research/Papers/大模型/Reasoning_LLM_Improves_Speaker_Recognition_in_Long-form_TV_Dramas|Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas]]
- **作者**: Yuxuan Li, Lingxi Xie, Xinyue Huo, Jihao Qiu, Jiacheng Shao, Pengfei Chen, Jiannan Ge, Kaiwen Duan, Qi Tian
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongVideoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integration of auditory, linguistic, and visual cues for speaker recognition. (2) We propose \textbf{DramaSR-LRM}, a robust approach built upon a large reasoning model (LRM). DramaSR-LRM is designed to autonomously aggregate contextual evidence via multimodal tool-use, synthesizing diverse inputs to achieve high-fidelity attribution. Experimental results demonstrate that DramaSR-LRM significantly outperforms existing baselines, particularly on short utterances where acoustic biometrics are inherently unreliable. \textit{All the data and code will be made publicly available at the project page: https://www.github.com/198808xc/DramaSR-LRM.}

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Move_Before_Learning_to_Do_Task-Agnostic_pretraining_for_VLAs|Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs]]

![[assets/2607.02466_figure.png|800]]

- **arXiv**: [2607.02466](https://arxiv.org/abs/2607.02466)
- **PDF**: https://arxiv.org/pdf/2607.02466
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Move_Before_Learning_to_Do_Task-Agnostic_pretraining_for_VLAs|Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs]]
- **作者**: Junhao Shi, Siyin Wang, Xiaopeng Yu, Li Ji, Jingjing Gong, Xipeng Qiu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of expert demonstrations -- triplets of observations, instructions, and actions that are costly to collect at scale. We argue that this bottleneck stems from conflating two distinct learning objectives: acquiring physical competence (how to move) and acquiring semantic alignment (what to do). Crucially, only the latter requires language supervision. Building on this Decomposition Hypothesis, we propose Task-Agnostic Pretraining (TAP), a two-stage framework that first learns transferable motor priors from cheap, unlabeled interaction data -- including discarded off-task trajectories and autonomous robot play -- via a self-supervised Inverse Dynamics objective. A lightweight second stage then grounds these priors in language using minimal expert data. On the SIMPLER benchmark, TAP matches models trained on over 1M expert trajectories while using orders of magnitude less labeled data, yielding a 10% absolute gain over standard behavior cloning. On a real-world WidowX platform, TAP retains 25% success under camera perturbations where internet-scale baselines collapse to 0%, demonstrating that task-agnostic pretraining produces robust, transferable physical representations and offers a scalable path forward for Embodied AI.

</details>

---

### [[20_Research/Papers/大模型/Neuron-Aware_Data_Selection_for_Annotation-Free_LLM_Self-Distillation|Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation]]

![[assets/2607.02460_figure.png|800]]

- **arXiv**: [2607.02460](https://arxiv.org/abs/2607.02460)
- **PDF**: https://arxiv.org/pdf/2607.02460
- **详细分析**: [[20_Research/Papers/大模型/Neuron-Aware_Data_Selection_for_Annotation-Free_LLM_Self-Distillation|Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation]]
- **作者**: Zhuowei Chen, Xiang Lorraine Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SciKnowEval, TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these approaches are not without drawbacks: SFT- and GRPO-based variants suffer out-of-domain performance degradation, while reward-based on-policy RL inflates calibration error. In this paper, we propose Neuron On-Policy Self-Distillation (Neuron-OPSD), a data-centric framework for annotation-free self-distillation that leverages internal neuron activations to guide both training-data selection and teacher context construction. The model is then trained via on-policy distillation from the teacher distribution, requiring no ground-truth labels at any stage. Across specialized-domain benchmarks, Neuron-OPSD improves in-domain task performance while preserving cross-domain generalization and mitigating calibration collapse over prior annotation-free baselines. This framework is particularly relevant to settings where online interaction or external supervision is costly or infeasible, and is conceptually distinct from offline RL approaches that rely on logged, reward-labeled trajectories.

</details>

---

### [[20_Research/Papers/具身智能/WorldSample_Closed-loop_Real-robot_RL_with_World_Modelling|WorldSample: Closed-loop Real-robot RL with World Modelling]]

![[assets/2607.02431_figure.png|800]]

- **arXiv**: [2607.02431](https://arxiv.org/abs/2607.02431)
- **PDF**: https://arxiv.org/pdf/2607.02431
- **详细分析**: [[20_Research/Papers/具身智能/WorldSample_Closed-loop_Real-robot_RL_with_World_Modelling|WorldSample: Closed-loop Real-robot RL with World Modelling]]
- **作者**: Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《WorldSample: Closed-loop Real-robot RL with World Modelling》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HIL-SERL, ProphRL, RLinf-VLA, Real-World, SimpleVLA-RL, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations. However, deploying RL on real robots remains constrained by high interaction costs, since each physical rollout is costly and reflects only one realized action-outcome path. To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for real-robot RL that closes a real-synthetic loop between physical rollouts, world-model generation, and policy improvement. Grounded on real rollouts, WorldSample generates high-fidelity synthetic transitions through a post-trained world model, which greatly lowers the visual hallucination. Specifically, rather than simply using these transitions as real-world experience, WorldSample introduces Policy-Paced Learning (PPL) to regulate the training process through sample selection and scheduling, balancing useful augmentation against value overestimation and mitigating the hallucination-induced noise. Experiments on robot manipulation tasks involving contact-rich and precise tasks show that WorldSample improves policy success rate by 28% while reducing training steps by 59% compared with baselines. Furthermore, WorldSample improves world model visual fidelity by 19.4dB in PSNR and 0.47 in SSIM over demonstration-only post-training, validating the effectiveness of the real-synthetic loop for both policy and world model performance.

</details>

---

### [[20_Research/Papers/大模型/QFedAgent_Quantum-Enhanced_Personalized_Federated_Learning_for_Multi-Agent_Activity_Recognition|QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition]]

![[assets/2607.02426_figure.png|800]]

- **arXiv**: [2607.02426](https://arxiv.org/abs/2607.02426)
- **PDF**: https://arxiv.org/pdf/2607.02426
- **详细分析**: [[20_Research/Papers/大模型/QFedAgent_Quantum-Enhanced_Personalized_Federated_Learning_for_Multi-Agent_Activity_Recognition|QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition]]
- **作者**: Quoc Bao Phan, Tuy Tan Nguyen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.7（加权：大模型 0.5，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid quantum-classical personalized FL framework for multi-agent activity recognition. The approach integrates a variational quantum circuit fusion module that models accelerometer--gyroscope interactions through quantum state encoding and entanglement, requiring only 72 quantum rotation parameters versus 33K in classical multi-layer perceptron-based fusion, achieving approximately 10x total parameter reduction. Experiments on the OPPORTUNITY dataset under subject-based non-IID partitions demonstrate 97.7% mean test accuracy, confirming that parameter-efficient quantum fusion remains competitive with conventional federated baselines.

</details>

---

### [[20_Research/Papers/具身智能/ACID_Action_Consistency_via_Inverse_Dynamics_for_Planning_with_World_Models|ACID: Action Consistency via Inverse Dynamics for Planning with World Models]]

![[assets/2607.02403_figure.png|800]]

- **arXiv**: [2607.02403](https://arxiv.org/abs/2607.02403)
- **PDF**: https://arxiv.org/pdf/2607.02403
- **详细分析**: [[20_Research/Papers/具身智能/ACID_Action_Consistency_via_Inverse_Dynamics_for_Planning_with_World_Models|ACID: Action Consistency via Inverse Dynamics for Planning with World Models]]
- **作者**: Gawon Seo, Dongwon Kim, Suha Kwak
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 0.6，世界模型 1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ACID: Action Consistency via Inverse Dynamics for Planning with World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decision-time planning with action-conditioned world models has become a popular paradigm for embodied control. However, the standard planning cost judges a candidate solely by how close its predicted terminal state lies to the goal, leaving the realizability of the intermediate transitions unchecked -- a predicted trajectory can look convincing while the environment rollout drifts away from it. In this paper, we propose ACID, a decision-time planning framework that introduces cycle action consistency: the action inferred backward from a predicted transition by an inverse dynamics model should recover the one that was conditioned on. We fold this per-step residual into the planning cost via a scale-invariant adaptive weight. Across four action-conditioned world models and six tasks spanning rigid and deformable manipulation, articulated control, and visual navigation, ACID consistently improves planning and matches the baseline's accuracy with substantially less planning compute.

</details>

---

### [[20_Research/Papers/大模型/VisionAId_An_Offline-First_Multimodal_Android_Assistant_for_People_with_Visual_Impairment,_Featuring_Personalized_Object_Retrieval|VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval]]

![[assets/2607.02371_figure.png|800]]

- **arXiv**: [2607.02371](https://arxiv.org/abs/2607.02371)
- **PDF**: https://arxiv.org/pdf/2607.02371
- **详细分析**: [[20_Research/Papers/大模型/VisionAId_An_Offline-First_Multimodal_Android_Assistant_for_People_with_Visual_Impairment,_Featuring_Personalized_Object_Retrieval|VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval]]
- **作者**: Cristian-Gabriel Florea, Stelian Spînu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, MobileFaceNet, YuNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time visual assistant. The system integrates six on-device deep learning models (metric monocular depth estimation, instance segmentation, visual and facial embeddings, face detection, and a custom banknote detector) running entirely through ONNX Runtime, with an optional cloud large language model (Google Gemini Flash) used only for narrative scene description and automatic object labeling. A distinctive contribution is a few-shot pipeline for personal objects: the user photographs an object from several angles, and the system later locates that specific instance in the environment, guiding the user toward it with augmented-reality markers, spatial audio, and distance-proportional haptics. All feedback is multimodal (Romanian speech synthesis, voice commands, vibration). On a reference device (Samsung Galaxy S21 Ultra), INT8 quantization reduces depth latency from ~1200 ms to ~491 ms, the custom banknote detector reaches an mAP@50 of 0.986, and metric depth is calibrated to below 1 cm of error within 3 m.

</details>

---

### [[20_Research/Papers/大模型/SkillFuzz_Fuzzing_Skill_Composition_for_Implicit_Intents_Discovery_in_Open_Skill_Marketplaces|SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces]]

![[assets/2607.02345_figure.png|800]]

- **arXiv**: [2607.02345](https://arxiv.org/abs/2607.02345)
- **PDF**: https://arxiv.org/pdf/2607.02345
- **详细分析**: [[20_Research/Papers/大模型/SkillFuzz_Fuzzing_Skill_Composition_for_Implicit_Intents_Discovery_in_Open_Skill_Marketplaces|SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces]]
- **作者**: Jinwei Hu, Yi Dong, Youcheng Sun, Xiaowei Huang
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting such intents is challenging because the effect emerges only through skill composition, execution environments are often unavailable at admission time, and the space of possible co-activations grows exponentially with marketplace size. In this paper, we formulate implicit-intent discovery as a fuzzing problem over skill compositions, where skill compositions are the unit under test, planning artifacts expose agent intent before execution, and deviations from a skill-free baseline serve as a differential oracle. Based on this formulation, we propose skillfuzz, the first execution-free testing approach that extracts structured skill contracts and uses contract-guided Monte Carlo Tree Search to prioritize potentially conflicting compositions. Across representative skill-marketplace workloads, skillfuzz discovers over 1,000 distinct implicit intents under a fixed query budget, confirms more than 80% of the highest-risk flagged compositions during execution-time validation, and identifies substantially more high-severity implicit intents than alternative search strategies while exploring only a fraction of the pairwise interaction space they require.

</details>

---

### [[20_Research/Papers/大模型/Grounded_autonomous_research_a_fault-tolerant_LLM_pipeline_from_corpus_to_manuscript_in_frontier_computational_physics|Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics]]

![[assets/2607.02329_figure.png|800]]

- **arXiv**: [2607.02329](https://arxiv.org/abs/2607.02329)
- **PDF**: https://arxiv.org/pdf/2607.02329
- **详细分析**: [[20_Research/Papers/大模型/Grounded_autonomous_research_a_fault-tolerant_LLM_pipeline_from_corpus_to_manuscript_in_frontier_computational_physics|Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics]]
- **作者**: Haonan Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to-end from a corpus of 11,083 recent condensed-matter physics arXiv papers to a publication-grade manuscript with three substantive physics findings (here on altermagnetic piezomagnetism): the agent autonomously conceives a research direction by mapping the corpus, calibrates methodology by reproducing published references, conducts novel first-principles computations, and writes the manuscript - grounded in literature throughout, across 47 fresh-context sessions in six phases sharing only on-disk state, with 2,162 literature-consultation events. Fault tolerance emerges from redundancy: fresh-context isolation, distributed grounding, and adversarial review catch what any single session misses; pre- and post-pilot stages are fully autonomous, and pilot requires bounded human intervention only at reproduction failures - operational knowledge curation, not scientific direction. Two paired failure modes - a pre-architecture baseline and a no-pilot ablation - isolate structurally enforced numerical confrontation at calibration checkpoints as the operative grounding mechanism. The primitives, characterized failure modes, and quantified intervention pattern lay a foundation for autonomous research in high-stakes scientific domains beyond computational physics.

</details>

---

### [[20_Research/Papers/强化学习/Generalization_in_offline_RL_The_structure_is_more_important_than_the_amount_of_pessimism|Generalization in offline RL: The structure is more important than the amount of pessimism]]

![[assets/2607.02288_figure.png|800]]

- **arXiv**: [2607.02288](https://arxiv.org/abs/2607.02288)
- **PDF**: https://arxiv.org/pdf/2607.02288
- **详细分析**: [[20_Research/Papers/强化学习/Generalization_in_offline_RL_The_structure_is_more_important_than_the_amount_of_pessimism|Generalization in offline RL: The structure is more important than the amount of pessimism]]
- **作者**: Max Weltevrede, Matthijs T. J. Spaan, Wendelin Böhmer
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Generalization in offline RL: The structure is more important than the amount of pessimism》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While pessimism counteracts overestimation bias in offline reinforcement learning (RL), being overly conservative has been associated with hindering certain forms of generalization. However, in this paper we demonstrate that being overly pessimistic does not inherently prevent optimal generalization in contextual MDPs (CMDPs). Instead, we argue successful generalization depends not on the amount of pessimism, but whether the pessimistic structure respects the underlying symmetries of the optimal solution. We prove that a mildly pessimistic, non-symmetric value function can generalize worse than an overly pessimistic, symmetric one. In offline RL, the structure of the pessimism is determined by the structure of the dataset coverage. As such, enforcing a symmetric value function can be non-trivial, and might require techniques such as data augmentation (DA). Inspired by our theoretical results, we argue that DA can best be applied through a consistency loss during policy extraction, rather than the common practice of (regular) offline training on an augmented dataset. This is empirically validated using IQL and CQL on a rotationally symmetric reacher environment.

</details>

---

### [[20_Research/Papers/大模型/AgenticSTS_A_Bounded-Memory_Testbed_for_Long-Horizon_LLM_Agents|AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents]]

![[assets/2607.02255_first_page.png|800]]

- **arXiv**: [2607.02255](https://arxiv.org/abs/2607.02255)
- **PDF**: https://arxiv.org/pdf/2607.02255
- **详细分析**: [[20_Research/Papers/大模型/AgenticSTS_A_Bounded-Memory_Testbed_for_Long-Horizon_LLM_Agents|AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents]]
- **作者**: Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao, Yihao Liu, Fanrui Zhang, Li Jin, Kaipeng Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the same game reports zero wins at the lowest difficulty across five configurations, and the developer-reported human win rate at the same difficulty is 16%; the task is hard but not saturated. Within our harness, a fixed-A0 ablation shows the largest observed difference when triggered strategic skills are enabled: the no-store baseline wins 3/10 games and adding the skill layer 6/10. At this sample size the comparison is directional rather than statistically decisive (Fisher exact p\approx0.37); a cross-backbone probe and public accumulating-context baselines are reported as operational comparisons rather than controlled tests of the contract variable itself. We release a reproducible testbed: 298 completed trajectories with condition tags, frozen memory/skill snapshots, prompt records, and analysis scripts -- an agent design and a validated, reusable methodology for studying how explicit memory layers shape long-horizon LLM-agent decisions.

</details>

---

### [[20_Research/Papers/具身智能/CoFL-S_Spatially_Queryable_Sector_Flow_Fields_for_Local_Language-Conditioned_Navigation|CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation]]

![[assets/2607.02222_figure.png|800]]

- **arXiv**: [2607.02222](https://arxiv.org/abs/2607.02222)
- **PDF**: https://arxiv.org/pdf/2607.02222
- **详细分析**: [[20_Research/Papers/具身智能/CoFL-S_Spatially_Queryable_Sector_Flow_Fields_for_Local_Language-Conditioned_Navigation|CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation]]
- **作者**: Haokun Liu, Zhaoqi Ma, Yicheng Chen, Wentao Zhang, Masaki Kitagawa, Zicen Xiong, Jinjie Li, Moju Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Navigation has increasingly emphasized high-level instruction reasoning, memory, global map construction, and instruction decomposition, while the low-level action representation remains comparatively underexplored. We propose CoFL-S, a low-level vision-language-action framework that predicts a language-conditioned flow field over the robot's local visible sector and generates continuous trajectories by rolling out the predicted field. To train this low-level representation, we convert each VLN-CE episode, originally a whole-episode instruction paired with an action sequence, into frame-level local supervision with aligned sub-instructions and matched action, trajectory, and dense flow-field targets. For evaluation, we introduce a continuous-time Habitat benchmark that isolates low-level action interfaces from instruction decomposition and executes all methods through a shared velocity-command controller, enabling decomposition-independent closed-loop comparison across different planner frequencies rather than fixed discrete forward-and-turn transitions in VLN-CE. Under matched encoders and training settings, CoFL-S consistently outperforms action-token and action-chunk baselines across planner frequencies in the continuous-time Habitat benchmark, and zero-shot real-world closed-loop deployment further shows its advantage over both baselines beyond simulation.

</details>

---

### [[20_Research/Papers/强化学习/ART_for_Diffusion_Sampling_Continuous-Time_Control_and_Actor-Critic_Learning|ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning]]

![[assets/2607.02137_figure.png|800]]

- **arXiv**: [2607.02137](https://arxiv.org/abs/2607.02137)
- **PDF**: https://arxiv.org/pdf/2607.02137
- **详细分析**: [[20_Research/Papers/强化学习/ART_for_Diffusion_Sampling_Continuous-Time_Control_and_Actor-Critic_Learning|ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning]]
- **作者**: Yilie Huang, Wenpin Tang, Xun Yu Zhou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ART-RL, CTRL, ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study timestep allocation for score-based diffusion sampling, where a learned reverse-time dynamics is discretized on a finite grid. Uniform and hand-crafted schedules are standard choices, but they rely on fixed prescriptions and can therefore be suboptimal. To address this limitation, we propose Adaptive Reparameterized Time (ART), a continuous-time control formulation that learns a time change by treating the speed of the sampling clock as the control, so that a uniform grid on the learned clock induces adaptive timesteps in the original diffusion time. Based on a leading-order Euler error surrogate, ART provides a principled objective for allocating timesteps along the sampling trajectory. To solve this deterministic control problem, we introduce ART-RL, an auxiliary randomized formulation with Gaussian policies that turns schedule learning into a continuous-time reinforcement learning problem. We prove that the randomized ART-RL formulation is equivalent to ART at the optimizer level, in the sense that its optimal Gaussian policy recovers the optimal ART time-warping rate through its mean. We further establish policy evaluation and policy improvement characterizations and derive trajectory-based moment identities that yield implementable actor--critic updates for learning the schedule. Across experiments ranging from controlled low-dimensional settings to image generation, ART-RL can be plugged into existing diffusion samplers by changing only the timestep grid, consistently improving sample quality over strong baseline schedules at matched budgets while leaving the rest of the sampling pipeline unchanged. The learned schedules also exhibit broad generalization, transferring without retraining across sampling budgets, datasets, solvers, pipelines, and representation spaces.

</details>

---

### [[20_Research/Papers/大模型/ContextNest_Verifiable_Context_Governance_for_Autonomous_AI_Agent|ContextNest: Verifiable Context Governance for Autonomous AI Agent]]

![[assets/2607.02116_figure.jpg|800]]

- **arXiv**: [2607.02116](https://arxiv.org/abs/2607.02116)
- **PDF**: https://arxiv.org/pdf/2607.02116
- **详细分析**: [[20_Research/Papers/大模型/ContextNest_Verifiable_Context_Governance_for_Autonomous_AI_Agent|ContextNest: Verifiable Context Governance for Autonomous AI Agent]]
- **作者**: Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala, Gabe Goodhart
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《ContextNest: Verifiable Context Governance for Autonomous AI Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNext, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNext does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer beneath retrieval, determining which artifacts are approved, current, attributable, and integrity-verified before retrieval systems operate over them. The specification combines typed Markdown documents with metadata, deterministic set-algebraic selectors, contextnest:// URI references, SHA-256 hash-chained version histories, graph-level checkpoints, source nodes for live data through the Model Context Protocol (MCP), and audit traces of agent context consumption. These mechanisms let organizations reconstruct which knowledge versions informed an agent output and whether those versions were AI-eligible when consumed. We report first empirical results from two controlled experiments. In a stale-version attack isolating the governance-versus-retrieval failure mode, governed selection strictly Pareto-dominates BM25 sparse retrieval, with higher answer-quality pass rate (97% versus 93-90%) at about one-third the input-token cost. In a retrieval-determinism experiment over a 1,060-document corpus, deterministic selectors and BM25 return stable document sets across repeated identical queries (Jaccard 1.0), while a dense+HNSW baseline is non-deterministic on 80% of queries (mean Jaccard 0.611, worst case 0.210). These results suggest that context governance addresses failure modes retrieval quality alone is not designed to resolve. We release a core engine, CLI, and MCP server under open licenses.

</details>

---

### [[20_Research/Papers/具身智能/Guided_Action_Flow_Q-Guided_Inference_for_Flow-Matching_Vision-Language-Action_Policies|Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies]]

![[assets/2607.02092_figure.png|800]]

- **arXiv**: [2607.02092](https://arxiv.org/abs/2607.02092)
- **PDF**: https://arxiv.org/pdf/2607.02092
- **详细分析**: [[20_Research/Papers/具身智能/Guided_Action_Flow_Q-Guided_Inference_for_Flow-Matching_Vision-Language-Action_Policies|Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies]]
- **作者**: Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SignVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching vision-language-action policies generate robot action chunks through an iterative transport process, creating an opportunity for test-time guidance without retraining the base policy. We study this opportunity in Guided Action Flow, an inference-time framework that keeps a pretrained SmolVLA policy frozen and uses a learned action-chunk critic to guide its reverse-time flow sampler. The critic is trained from real success and failure rollouts, can condition on task-description features from the frozen SmolVLA language pathway, and is used only through action gradients during sampling. We evaluate the approach on LIBERO manipulation tasks. A single-task critic improves success from 68.0% to 82.0% on one seed window and from 82.0% to 86.0% on another. A multi-family task-description critic improves validation success from 46.0% to 56.0%, while the locked held-out test gain is positive but modest, from 65.0% to 67.5%. These results support the feasibility of Q-guided inference for frozen flow-matching VLA policies, while showing that critic generalization and uncertainty-aware guidance remain the central bottlenecks.

</details>

---

### [[20_Research/Papers/其他/Traceable_Fault_Diagnosis_for_Battery_Energy_Storage_Systems_via_Retrieval-Augmented_Multi-Agent_O&M_Assistant|Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant]]

![[assets/2607.01992_first_page.png|800]]

- **arXiv**: [2607.01992](https://arxiv.org/abs/2607.01992)
- **PDF**: https://arxiv.org/pdf/2607.01992
- **详细分析**: [[20_Research/Papers/其他/Traceable_Fault_Diagnosis_for_Battery_Energy_Storage_Systems_via_Retrieval-Augmented_Multi-Agent_O&M_Assistant|Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant]]
- **作者**: Jiangdi Ru, Bing Li, Yage Huang, Ding Wang, Keru Hua
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, ComputerVision, Systems

#### 研究背景与动机

《Traceable Fault Diagnosis for Battery Energy Storage Systems via Retrieval-Augmented Multi-Agent O&M Assistant》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale battery energy storage systems (BESSs) require O&amp;M decisions that combine alarms, cell-level measurements, device topology, diagnostic tables, historical cases, and maintenance documents. Monitoring platforms can flag threshold violations, but they often cannot explain whether voltage inconsistency, resistance drift, short-circuit risk, capacity divergence, or thermal abnormality needs intervention. This digest presents a traceable BESS fault-diagnosis assistant that uses retrieval-augmented multi-agent reasoning to connect operational data, domain knowledge, visual evidence, and report generation. Reliability is improved through BESS-specific task routing, schema-constrained natural-language database access, hybrid text-image retrieval, and evidence-based answer synthesis. Preliminary internal evaluation is reported for routing, database access, and diagnostic reasoning.

</details>

---

### [[20_Research/Papers/具身智能/Episodic-to-Semantic_Consolidation_Without_Identity_Drift|Episodic-to-Semantic Consolidation Without Identity Drift]]

![[assets/2607.01988_figure.png|800]]

- **arXiv**: [2607.01988](https://arxiv.org/abs/2607.01988)
- **PDF**: https://arxiv.org/pdf/2607.01988
- **详细分析**: [[20_Research/Papers/具身智能/Episodic-to-Semantic_Consolidation_Without_Identity_Drift|Episodic-to-Semantic Consolidation Without Identity Drift]]
- **作者**: Xue Qin, Simin Luan, Cong Yang, Zhijun Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Episodic-to-Semantic Consolidation Without Identity Drift》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-running adaptive intelligent agents face a structural tension between knowledge consolidation and information integrity. Memory consolidation is conventionally treated as an agent-changing operation: a model is fine-tuned, a prompt rewritten, a policy distilled, or a reflection appended to the context that governs future behaviour. In regulated autonomic deployment this is a liability because the agent operates under commitments and audit contracts that bind to a specific, cryptographically certified identity. We propose to treat consolidation not as a mutation of the planner or the identity manifest, but as a deterministic function f: M^ep -&gt; M^sem over episodic memory whose output is a separately addressable semantic knowledge layer; the identity hash does not read M^sem, so consolidation updates knowledge without changing the agent's certified identity. We give a formal account of the agent representation, prove identity invariance through a structural lemma on the manifest's hash-input set, specify a deterministic aggregation algorithm whose outputs are auditable database rows with explicit confidence and supporting-event provenance, and validate the construction with synthetic experiments demonstrating per-field correctness, byte-equal identity across consolidation passes, and a mean 79.82% reduction in unproductive planner attempts (95% BCa CI [78.02%, 81.49%] across 10 seeds) against a calibrated Bayesian-shrunk baseline. The construction is a knowledge-update discipline for autonomic agents in which lessons accumulate as queryable facts while the agent's certified identity remains byte-equal across its operational lifetime, with an embodied service agent as the running case study.

</details>

---

### [[20_Research/Papers/大模型/MolSight_A_Graph-Aware_Vision-Language_Model_for_Unified_Chemical_Image_Understanding|MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding]]

![[assets/2607.01982_figure.png|800]]

- **arXiv**: [2607.01982](https://arxiv.org/abs/2607.01982)
- **PDF**: https://arxiv.org/pdf/2607.01982
- **详细分析**: [[20_Research/Papers/大模型/MolSight_A_Graph-Aware_Vision-Language_Model_for_Unified_Chemical_Image_Understanding|MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding]]
- **作者**: Wenda Wang, Yihan Tong, Yuwei Hu, Zhewei Wei
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《MolSight: A Graph-Aware Vision-Language Model for Unified Chemical Image Understanding》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Using molecular large language models (LLMs) as a unified framework for understanding molecular structures and functions is emerging as a new trend in tasks such as molecular design and drug discovery. However, these models struggle to fully capture the visual representation of molecular structures, limiting their potential. While existing molecular vision-language models (VLMs) show promise, they still face challenges in structural alignment and lack the necessary topological modeling for accurate molecular understanding. To address this, we propose MolSight, a graph-aware vision-language model framework designed to enhance the understanding of molecular images by VLMs. MolSight integrates a Molecular Topology Module to inject chemical-bond adjacency information into vision tokens, and a Molecular Grounding Module to align visual features with chemical symbolic semantics. Our experiments demonstrate that MolSight significantly outperforms existing VLMs, molecular LLMs, and specialized tools across multiple chemical visual understanding tasks, achieving a new level of molecular image reasoning.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Knowledge_Edit-Scoped_Generalization_for_Online_Recursive_MLLM_Editing|Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing]]

![[assets/2607.01978_figure.png|800]]

- **arXiv**: [2607.01978](https://arxiv.org/abs/2607.01978)
- **PDF**: https://arxiv.org/pdf/2607.01978
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Knowledge_Edit-Scoped_Generalization_for_Online_Recursive_MLLM_Editing|Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing]]
- **作者**: Siyuan Li, Youyuan Zhang, Ruitong Liu, Junxi Wang, Jing Li
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Multimodal Knowledge Edit-Scoped Generalization for Online Recursive MLLM Editing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online multimodal knowledge editing requires injecting a continual stream of visual-textual corrections into multimodal large language models (MLLMs) with bounded overhead and minimal disruption to unrelated behaviors. Existing editors mainly emphasize edit reliability and long-horizon stability, but rarely control the semantic boundary of each edit. Our pilot analyses of post-edit behaviors and internal neuronal activities reveal a scope gap behind reliable edits: instance-level success neither guarantees transfer to valid cross-modal variants nor prevents leakage to unrelated inputs, while edit-related cross-modal responses concentrate in deeper semantic layers. Therefore, we formulate Edit-Scoped Generalization, reframing online MLLM editing from merely correcting an instance to controlling the propagation boundary of each edit. To this end, we propose ScopeEdit, a scope-aware online editor that decomposes each update into a modality-local absorption branch and an evidence-gated shared generalization branch. The local branch supports stable edit absorption, whereas the shared branch enables cross-modal propagation only when visual and textual evidence are sufficiently aligned. Both branches perform scope-separated write geometries in orthogonal low-rank spaces and maintain branch-wise preconditioners via Sherman--Morrison recursions, yielding constant per-edit overhead. Extensive experiments across diverse benchmarks, long-horizon edit streams, MLLM backbones, real-world VLKEB scenarios, and complex vision-language architectures show that ScopeEdit consistently improves the trade-off between in-scope cross-modal transfer and out-of-scope locality, while preserving edit reliability, stability and online efficiency. Our code is available at https://github.com/lab-klc/ScopeEdit.

</details>

---

### [[20_Research/Papers/具身智能/PhysMani_Physics-principled_3D_World_Model_for_Dynamic_Object_Manipulation|PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation]]

![[assets/2607.01938_figure.png|800]]

- **arXiv**: [2607.01938](https://arxiv.org/abs/2607.01938)
- **PDF**: https://arxiv.org/pdf/2607.01938
- **详细分析**: [[20_Research/Papers/具身智能/PhysMani_Physics-principled_3D_World_Model_for_Dynamic_Object_Manipulation|PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation]]
- **作者**: Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, Bo Yang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.72（加权：具身智能 0.9，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PhysMani-Bench, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating fast and dynamically moving targets in unstructured 3D environments remains challenging for embodied AI. Existing visual-language-action models and world models struggle with accurate 3D geometry and physically meaningful forecasting. We propose PhysMani, a framework that couples a physics-principled 3D Gaussian world model with a future-aware action policy model. The world model learns a divergence-free Gaussian velocity field via online optimization for fast and physically grounded future dynamics prediction. The policy model integrates the predicted 3D scene future dynamics through a learnable token based cross-attention module. We introduce PhysMani-Bench, a dynamic manipulation benchmark with 16 tasks, and demonstrate a superior success rate over strong baselines in both simulation and real-world robot experiments.

</details>

---

### [[20_Research/Papers/大模型/Rank-Then-Act_Reward-Free_Control_from_Frame-Order_Progress|Rank-Then-Act: Reward-Free Control from Frame-Order Progress]]

![[assets/2607.01897_figure.jpg|800]]

- **arXiv**: [2607.01897](https://arxiv.org/abs/2607.01897)
- **PDF**: https://arxiv.org/pdf/2607.01897
- **详细分析**: [[20_Research/Papers/大模型/Rank-Then-Act_Reward-Free_Control_from_Frame-Order_Progress|Rank-Then-Act: Reward-Free Control from Frame-Order Progress]]
- **作者**: Yuriy Maksyuta, George Bredis, Ruslan Rakhimov, Daniil Gavrilov
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.3，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Rank-Then-Act: Reward-Free Control from Frame-Order Progress》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL, MetaWorld, XIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Rank-Then-Act (RTA), a framework for learning control policies from expert video demonstrations without environment rewards. RTA trains a Vision-Language Model (VLM) offline as a progress-based ordinal scorer, using a Group Relative Policy Optimization (GRPO) objective over shuffled frame sequences, which forces the model to recover temporal ordering from visual semantics rather than trivial time cues. Importantly, instead of using the scorer directly as a scalar reward model, we propose a correlation-based reward function for reinforcement learning: at each interaction window, we compute the Spearman rank correlation between predicted progress rankings and true temporal indices, yielding a bounded, scale-invariant learning signal. This design decouples reward learning from absolute calibration and enables stable transfer across tasks and environments. We evaluate RTA on discrete control benchmarks (PyBoy: Catrap, Kirby) and continuous control tasks (PointMaze, MetaWorld). RTA consistently matches or outperforms prior video-based reward learning methods and rank-based baselines, while demonstrating strong cross-task reuse of a single pretrained progress scorer. Our results suggest that correlation-structured supervision over video-derived ordinal signals is sufficient for policy learning, offering a scalable alternative to explicit reward design.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_Chunking_Strategies_for_Retrieval-Augmented_Generation_on_Academic_Texts|Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts]]

![[assets/2607.01852_figure.png|800]]

- **arXiv**: [2607.01852](https://arxiv.org/abs/2607.01852)
- **PDF**: https://arxiv.org/pdf/2607.01852
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_Chunking_Strategies_for_Retrieval-Augmented_Generation_on_Academic_Texts|Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts]]
- **作者**: Valentin J. J. Kreileder, Johannes Reisinger, Andreas Fischer
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.AI

#### 研究背景与动机

《Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) systems use the question-answering capabilities of Large Language Models (LLMs) to access information outside their parameters. We evaluate if cluster-based semantic chunking improves retrieval and answer quality compared to fixed-size and recursive chunking evaluating on long, structured academic theses using the Retrieval Augmented Generation Assessment (RAGAs) framework. RAGAs based faithfulness shows limited reliability in this setup. Performance on fixed versus document specific questions varied substantially, likely related to the formatting of documents and preprocessing. Under the tested configuration, cluster-based chunking did not outperform simpler strategies.

</details>

---

### [[20_Research/Papers/大模型/MMIR-TCM_Memory-Integrated_Multimodal_Inference_and_Retrieval_for_TCM_Clinical_Decision_Support|MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support]]

![[assets/2607.01814_figure.png|800]]

- **arXiv**: [2607.01814](https://arxiv.org/abs/2607.01814)
- **PDF**: https://arxiv.org/pdf/2607.01814
- **详细分析**: [[20_Research/Papers/大模型/MMIR-TCM_Memory-Integrated_Multimodal_Inference_and_Retrieval_for_TCM_Clinical_Decision_Support|MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support]]
- **作者**: Lihui Luo, Joongwon Chae, Ziyan Chen, Yang Liu, Siyi Cheng, Weihan Gao, Zelin Zeng, Xiaoming Yin, Samaneh Beheshti Kashi, Dongmei Yu, Lian Zhang, Jing Sui...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《MMIR-TCM: Memory-Integrated Multimodal Inference and Retrieval for TCM Clinical Decision Support》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TCMBench, TCMEval, TongueNet, TransUNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional Chinese Medicine (TCM) diagnosis, particularly through tongue inspection, faces persistent challenges in subjectivity and reproducibility. The application of multimodal artificial intelligence to TCM clinical tasks, such as syndrome differentiation and prescription generation, is significantly hampered by the semantic gap between visual tongue features and textual reasoning, as well as the lack of large-scale, standardized datasets. To address these challenges, we introduce MMIR-TCM, a novel framework that emulates the diagnostic process of TCM experts by integrating multimodal large language model(MLLM) with memory-augmented segmentation and retrieval-augmented generation (RAG). Employing a three-stage architecture, MMIR-TCM integrates a training-free Memory-SAM module for robust tongue extraction, a fine-tuned Qwen3-VL model for structured tongue diagnosis generation, and a Qwen3-based RAG component for evidence-grounded clinical decision support generation. The framework was developed and validated using MedTCM, a new large-scale multimodal dataset that we introduce specifically for advanced TCM research. To properly evaluate our framework's clinical accuracy, which existing metrics fail to capture, we also developed TDEU, a domain-specific evaluation metric incorporating semantic understanding and diagnostic importance. Our comprehensive experiments demonstrate that MMIR-TCM significantly outperforms leading models, including GPT-4o and Gemini 2.5 Flash.

</details>

---

### [[20_Research/Papers/具身智能/Lightweight_Safe_Reinforcement_Learning_for_End-to-End_UAV_Navigation|Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation]]

![[assets/2607.01794_figure.png|800]]

- **arXiv**: [2607.01794](https://arxiv.org/abs/2607.01794)
- **PDF**: https://arxiv.org/pdf/2607.01794
- **详细分析**: [[20_Research/Papers/具身智能/Lightweight_Safe_Reinforcement_Learning_for_End-to-End_UAV_Navigation|Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation]]
- **作者**: Shenghui Zhang, YuXuan Gao, Songwei Zhao, Jifeng Hu, Zijing Zhang, Hechang Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: EmbodiedAI, RL, Systems

#### 研究背景与动机

《Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid development of autonomous aerial systems, Unmanned Aerial Vehicles (UAVs) are increasingly deployed in applications such as inspection, environmental monitoring, and rescue, creating growing demand for reliable autonomous navigation. However, autonomous UAV navigation in dense environments remains challenging under sparse perception and dynamic constraints. Most reinforcement learning (RL) methods lack explicit safety mechanisms, leading to unsafe exploration, unstable training, and risky behaviors, especially during high-speed flight. Even in safe RL approaches, safety is often enforced by projecting policy outputs onto a safe action set, which may introduce instability. Meanwhile, many learning-based methods rely on dense inputs or large networks, increasing computational burden and limiting lightweight onboard deployment. Facing the above challenges, we propose a safety-constrained perception-control integrated framework for UAV navigation. A lightweight network encodes sparse observations into collision-risk-aware features using asymmetric and depthwise separable convolutions. We formulate the task as a constrained Markov decision process within a hierarchical control architecture and solve it using a Lagrangian-based safe PPO algorithm. Curriculum learning further improves training stability. Experiments with varying obstacle densities and flight speeds demonstrate higher success rates, improved safety, and better efficiency than existing reinforcement learning baselines.

</details>

---

### [[20_Research/Papers/大模型/Safety_Testing_LLM_Agents_at_Scale_From_Risk_Discovery_to_Evidence-Grounded_Verification|Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification]]

![[assets/2607.01793_figure.png|800]]

- **arXiv**: [2607.01793](https://arxiv.org/abs/2607.01793)
- **PDF**: https://arxiv.org/pdf/2607.01793
- **详细分析**: [[20_Research/Papers/大模型/Safety_Testing_LLM_Agents_at_Scale_From_Risk_Discovery_to_Evidence-Grounded_Verification|Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification]]
- **作者**: Yunhao Feng, Ruixiao Lin, Ming Wen, Qinqin He, Yanming Guo, Yifan Ding, Yutao Wu, Jialuo Chen, Yunhao Chen, Xiaohu Du, Jianan Ma, Zixing Chen...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Vera-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly perform autonomous actions through external tools, leading to complex and evolving safety risks. However, existing safety testing targets expert-designed safety violations, and the corresponding outcomes are evaluated by hard-coded rules, making them costly to extend as agents evolve. To this end, we present Vera, an end-to-end automated safety testing framework that instantiates software engineering testing principles for non-deterministic agents through a three-stage, self-reinforcing pipeline. First, a literature-driven exploration continuously discovers and structures emerging risks into taxonomies of safety risks, attack methods, and tool execution environments. Second, combinatorial composition across taxonomy dimensions produces executable safety cases, each specifying a concrete safety goal, a programmatically constructed initial state, and a deterministic verification predicate grounded in observable artifacts. Third, adaptive execution runs heterogeneous agents in isolated sandboxes where a control agent steers multi-turn interaction based on runtime observations, while evidence-grounded verifiers judge outcomes from environment state and tool-call evidence rather than model self-report. We evaluate Vera on four production agent frameworks (OpenClaw, Hermes, Codex, Claude Code), revealing substantial safety weaknesses, with average attack success rates reaching 93.9\% under multi-channel attacks; we also release Vera-Bench, comprising 1600 executable safety cases spanning 124 risk categories across three execution settings. These results indicate that modular, executable testing infrastructure is essential for rigorous and maintainable safety evaluation of rapidly evolving agentic systems at scale. The code is publicly available at https://github.com/Yunhao-Feng/Vera.

</details>

---

### [[20_Research/Papers/具身智能/SimWorlds_A_Multi-Agent_System_for_Dynamic_3D_Scene_Creation|SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation]]

![[assets/2607.01766_figure.png|800]]

- **arXiv**: [2607.01766](https://arxiv.org/abs/2607.01766)
- **PDF**: https://arxiv.org/pdf/2607.01766
- **详细分析**: [[20_Research/Papers/具身智能/SimWorlds_A_Multi-Agent_System_for_Dynamic_3D_Scene_Creation|SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation]]
- **作者**: Chunjiang Liu, Xiaoyuan Wang, Haoyu Chen, Yizhou Zhao, Ming-Hsuan Yang, László A. Jeni
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.6）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BlenderBench, BlenderGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly used to translate natural language into 3D scenes in a procedural way, but existing systems focus on static output. Dynamic 4D scenes from text alone, in which liquids flow, particles emit, rigid bodies cascade, and articulated mechanisms move, remain largely unexplored despite their value as editable content and as physics-grounded training data for video generation and embodied AI. Two challenges set the dynamic case apart from static text-to-scene work: an agent must jointly coordinate spatial layout, multiple physics solvers, temporal sequencing, camera, and lighting in a single coherent scene, and verifying motion correctness from rendered video is fundamentally harder than judging a single image. We present SimWorlds: a multi-agent framework that produces dynamic, editable 4D scenes from text, with Blender-specific procedural knowledge, a planner-coder-reviewer workflow driving a fixed ordered sequence of construction stages, a layered scene protocol enforced by a deterministic verifier, and a runtime-state inspection tool suite that catches mechanism failures the rendered image cannot reveal. We also introduce 4DBuildBench, a benchmark for assessing both visual fidelity and physical consistency of the procedural dynamic 3D scenes generated from text prompts. Experiments show that SimWorlds outperforms prior dynamic Blender generation baselines.

</details>

---

### [[20_Research/Papers/强化学习/Full_Bayesian_Reinforcement_Learning_via_LF-IBIS|Full Bayesian Reinforcement Learning via LF-IBIS]]

![[assets/2607.01741_figure.png|800]]

- **arXiv**: [2607.01741](https://arxiv.org/abs/2607.01741)
- **PDF**: https://arxiv.org/pdf/2607.01741
- **详细分析**: [[20_Research/Papers/强化学习/Full_Bayesian_Reinforcement_Learning_via_LF-IBIS|Full Bayesian Reinforcement Learning via LF-IBIS]]
- **作者**: Stefano Masini, Cecilia Viscardi, Michela Baccini
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Full Bayesian Reinforcement Learning via LF-IBIS》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：ABC-RL, BRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) is a sequential decision-making framework in which an agent learns optimal policies through interaction with an environment by maximizing cumulative rewards. Among RL methods, Bayesian Reinforcement Learning (BRL) addresses common practical challenges related to data scarcity by leveraging prior knowledge about the environment and sequential belief updates. However, most BRL approaches require an explicit likelihood function, which is frequently inaccessible or intractable in real-world settings. We propose Likelihood-Free Iterated Batch Importance Sampling (LF-IBIS), a novel algorithm for BRL that updates the agent's beliefs online as new interactions become available. By combining Approximate Bayesian Computation with Iterated Batch Importance Sampling, LF-IBIS enables full Bayesian inference in settings where the environment dynamics are not described by an explicit or tractable likelihood. The method yields approximate posterior distributions over both environment parameters and optimal policies, providing a quantification of policy uncertainty useful for a Bayesian treatment of the exploration-exploitation trade-off. We test the method on a simulation study in response-adaptive randomization in clinical trials, where closed-form posteriors enable validation. Additional experiments address settings where the posterior has no closed form and illustrate online policy updating based on the posterior distribution of the optimal policy.

</details>

---

### [[20_Research/Papers/强化学习/Predicting_Closed-Loop_Performance_of_Latent_World_Models_Offline_Checkpoint_Selection_for_MPC_and_Model-Based_RL_Under_Non-Markovian_Reward|Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander]]

![[assets/2607.01736_figure.jpg|800]]

- **arXiv**: [2607.01736](https://arxiv.org/abs/2607.01736)
- **PDF**: https://arxiv.org/pdf/2607.01736
- **详细分析**: [[20_Research/Papers/强化学习/Predicting_Closed-Loop_Performance_of_Latent_World_Models_Offline_Checkpoint_Selection_for_MPC_and_Model-Based_RL_Under_Non-Markovian_Reward|Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander]]
- **作者**: Nikolai Smolyanskiy
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Predicting Closed-Loop Performance of Latent World Models: Offline Checkpoint Selection for MPC and Model-Based RL Under Non-Markovian Rewards in LunarLander》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study how to predict the downstream closed-loop performance of a learned latent world model from validation-time diagnostics alone. Choosing the right checkpoint from a world-model training run is difficult: validation loss and multi-step prediction RMSE keep improving long after closed-loop performance has collapsed. We present a suite of structural validation-time diagnostics drawn from optimal-control theory and apply them to Gymnasium's LunarLander v3, which features shaped rewards. We train an RSSM [5, 4] world model on it and treat per checkpoint CEM-MPC return as the oracle for closed-loop quality. By evaluating 40 metrics against this oracle, we find that the strongest single predictor is the Reward Observability Fraction (ROF), which measures the reward predictor's dependence on the observable subspace. We combine ROF with three structural regularizers into a single-number offline checkpoint selection score, the Composite Reward Observability Fraction (CROF). The CROF-selected world model trains a model-based A2C policy that beats a fairly evaluated model-free A2C baseline by ~24.5 return points while using ~65x fewer real-environment interactions, and the same world model also drives a strong zero-shot CEM-MPC policy. Code and data: https://github.com/nsmoly/LunarLander_RSSM.

</details>

---

### [[20_Research/Papers/强化学习/DRL-CLBA_A_Clean_Label_Backdoor_Attack_for_Speech_Classification_via_DDPG_Reinforcement_Learning|DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning]]

![[assets/2607.01729_figure.png|800]]

- **arXiv**: [2607.01729](https://arxiv.org/abs/2607.01729)
- **PDF**: https://arxiv.org/pdf/2607.01729
- **详细分析**: [[20_Research/Papers/强化学习/DRL-CLBA_A_Clean_Label_Backdoor_Attack_for_Speech_Classification_via_DDPG_Reinforcement_Learning|DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning]]
- **作者**: Yueming Huang, Wenhan Yao, Fen Xiao, Xiarun Chen, Weiping Wen
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, Security

#### 研究背景与动机

《DRL-CLBA: A Clean Label Backdoor Attack for Speech Classification via DDPG Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep learning models for speech classification are vulnerable to backdoor attacks, where malicious triggers cause misclassification at inference time. While sample-specific attacks can bypass many defenses, they often rely on poisoned label attack, making them detectable via manual data defense. In this paper, we propose DRL-CLBA, a novel clean label backdoor attack for speech classification that leverages Deep Deterministic Policy Gradient (DDPG) reinforcement learning. We also utilize deep audio steganography to embed sample-specific triggers into source audio, creating feature-space anchors. The proposed reinforcement learning framework effectively optimizes target samples toward trigger-bearing anchor points in the model's deep latent space, enabling label-migration-free poisoning of target samples. Experimental results across three datasets and four different DNNs demonstrate that DRL-CLBA achieves a high attack success rate, effectively bypassing some backdoor defenses. The attack demonstrates strong resistance against fine-tuning, pruning, and spectral signature defenses, exposing critical vulnerabilities in speech-controlled systems.

</details>

---

### [[20_Research/Papers/大模型/AgenticDataBench_A_Comprehensive_Benchmark_for_Data_Agents|AgenticDataBench: A Comprehensive Benchmark for Data Agents]]

![[assets/2607.01647_first_page.png|800]]

- **arXiv**: [2607.01647](https://arxiv.org/abs/2607.01647)
- **PDF**: https://arxiv.org/pdf/2607.01647
- **详细分析**: [[20_Research/Papers/大模型/AgenticDataBench_A_Comprehensive_Benchmark_for_Data_Agents|AgenticDataBench: A Comprehensive Benchmark for Data Agents]]
- **作者**: Zhaoyan Sun, Shan Zhong, Daizhou Wen, Jiaxing Han, Guoliang Li, Ying Yan, Peng Zhang, Yu Su, Xiang Qi, Baolin Sun, Chengyuan Yang, Tao Fang...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgenticDataBench: A Comprehensive Benchmark for Data Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgenticDataBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data science aims to derive actionable insights from heterogeneous raw data, unlocking the value of the massive amounts of data generated in modern society. Automating this process is essential to reducing labor-intensive efforts for data scientists and enabling scalable data-driven applications. Recently, large language model (LLM)-based data agents have emerged as a promising solution to automate data science workflows. However, the field lacks comprehensive benchmarks to rigorously evaluate these agents across diverse scenarios with fine-grained granularity. To address this gap, we propose AgenticDataBench, a comprehensive benchmark featuring realistic tasks spanning diverse domains with fine-grained ground-truth labels. This enables evaluations to capture the diversity and complexity of data science workflows and the detailed performance of agents. First, to cover diverse domains, we collect real datasets and tasks from 15 vertical domains, including 5 real-world B2B use cases from a leading fintech company. Second, to remove redundancy in real-world tasks and generate high-quality tasks for domains lacking real data, we introduce data science skills, recurring data-centric operational patterns, and quantify benchmark coverage by the number of skills included. Representative skills are extracted from large-scale task solutions on Stack Overflow using skill-aligned hierarchical clustering. Third, for real-world business tasks, we select task-solution pairs that maximize diversity in skill composition, ensuring broad coverage of practical scenarios. Fourth, to generate realistic tasks for devise domains without real tasks, we propose a systematic LLM-based task generation approach to create workflows and tasks based on these skills. Finally, we evaluate state-of-the-art data agents using our annotated benchmark and open-sourced testbed, providing detailed skill-level insights.

</details>

---

### [[20_Research/Papers/大模型/Safe_and_Adaptive_Cloud_Healing_Verifying_LLM-Generated_Recovery_Plans_with_a_Neural-Symbolic_World_Model|Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model]]

![[assets/2607.01595_figure.png|800]]

- **arXiv**: [2607.01595](https://arxiv.org/abs/2607.01595)
- **PDF**: https://arxiv.org/pdf/2607.01595
- **详细分析**: [[20_Research/Papers/大模型/Safe_and_Adaptive_Cloud_Healing_Verifying_LLM-Generated_Recovery_Plans_with_a_Neural-Symbolic_World_Model|Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model]]
- **作者**: Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo, Tianyu Shen, Zeyu Qiao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.95（加权：大模型 0.55，强化学习 0.6，世界模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As the scale and complexity of cloud-based AI systems continue to escalate, ensuring service reliability through rapid fault detection and adaptive recovery has become a critical challenge. While existing approaches integrate Large Language Models (LLMs) for semantic understanding and Deep Reinforcement Learning (DRL) for policy optimization, they often rely on sequential, loosely coupled architectures that underutilize the generative and reasoning capabilities of LLMs. In this paper, we propose a paradigm shift with PASE, a Planning-Aware Semantic self-healing engine, a novel fault self-healing framework that reconceptualizes recovery as a neuro-symbolic program synthesis task. PASE employs an LLM as a core Plan Synthesis Engine to generate structured recovery plans from a library of semantic primitives. A Neural-Symbolic World Model verifies plan feasibility through simulation, while a Meta-Prompt Optimizer, trained via DRL, learns to generate optimal prompts that guide the LLM's planning process. This tight reason-plan-verify-adapt loop enables dynamic, context-aware recovery strategy generation beyond predefined action spaces. Experiments on a real-world cloud fault injection dataset demonstrate that PASE significantly outperforms state-of-the-art methods, reducing average system recovery time by over 40% and improving fault detection accuracy in unknown fault scenarios. Our framework advances autonomous system management by unifying LLM-based reasoning with model-assisted verification and meta-learned guidance.

</details>

---

### [[20_Research/Papers/具身智能/VLAFlow_A_Unified_Training_Framework_for_Vision-Language-Action_Models_via_Co-training_and_Future_Latent_Alignment|VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment]]

![[assets/2607.01586_figure.png|800]]

- **arXiv**: [2607.01586](https://arxiv.org/abs/2607.01586)
- **PDF**: https://arxiv.org/pdf/2607.01586
- **详细分析**: [[20_Research/Papers/具身智能/VLAFlow_A_Unified_Training_Framework_for_Vision-Language-Action_Models_via_Co-training_and_Future_Latent_Alignment|VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment]]
- **作者**: Guoyang Xia, Fengfa Li, Hongjin Ji, Lei Ren, Fangxiang Feng, Kun Zhan, Yan Xie
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, MindVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) have recently advanced robotic manipulation, yet the effects of different robot-data pre-training paradigms remain difficult to compare because existing models often differ in architecture, data, action space, and evaluation protocol. We present VLAFlow (Vision-Language-Action Flow), a unified flow-matching framework for controlled comparison of VLA training objectives. Using a heterogeneous robot corpus, OXEMix, containing approximately 5,000 hours of data from DROID, OpenX-Embodiment, OpenX-Augmented, and RoboCOIN, we evaluate four paradigms under the same pi0-style architecture, shared VLM backbone, action expert, and 14-dimensional action space: action-only modeling (MindPI), language-supervised co-training (MindLPI), future latent alignment (MindWPI), and their combination (MindLWPI). Experiments on LIBERO, LIBERO-Plus, and SimplerEnv show that action-only pre-training is sensitive to heterogeneous data. In contrast, language supervision helps preserve vision-language generalization, while future latent alignment improves state-transition and action-outcome modeling. By combining both signals, MindLWPI achieves the most stable overall transfer performance across benchmarks. These results suggest a meta-action space view: language and future latent representations provide complementary intermediate constraints that make heterogeneous action supervision smoother and more transferable.

</details>

---

### [[20_Research/Papers/大模型/EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_Hypothesis_Generation|EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation]]

![[assets/2607.01584_figure.png|800]]

- **arXiv**: [2607.01584](https://arxiv.org/abs/2607.01584)
- **PDF**: https://arxiv.org/pdf/2607.01584
- **详细分析**: [[20_Research/Papers/大模型/EO-Agents_A_Three-Agent_LLM_Pipeline_for_Earth_Observation_Hypothesis_Generation|EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation]]
- **作者**: Mahyar Ghazanfari, Amin Tabrizian, Armin Mehrabian, Peng Wei
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models have recently been explored for scientific hypothesis generation, but most prior work relies on unstructured literature and free-form textual claims. We present a pipeline for Earth observation that grounds hypothesis generation directly in the NASA Earth Observation Knowledge Graph. A heterogeneous graph neural network trained on historical co-usage relations ranks candidate dataset pairings, and a three-agent LLM pipeline filters, generates, and evaluates structured research hypotheses. Applied to 1,475 NASA datasets, the system produces 160 hypotheses spanning multiple Earth-science domains, including ecohydrology, glaciology, aerosol--cloud interactions, vegetation phenology, and stratospheric chemistry. Model-predicted novel dataset pairings are rated nearly as plausible as held-out real co-usages from the literature, indicating that the pipeline surfaces scientifically coherent yet unexplored combinations. A 2*2*2 factorial experiment across GPT-5.2 and Claude Sonnet 4.6 shows that hypothesis rankings remain stable, while absolute scores depend strongly on judge identity, highlighting limitations of single-judge LLM evaluation.

</details>

---

### [[20_Research/Papers/大模型/DiPS_Dialogue_Policy_Selection_for_High-Stakes_Persuasion_Agents|DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents]]

![[assets/2607.01557_figure.png|800]]

- **arXiv**: [2607.01557](https://arxiv.org/abs/2607.01557)
- **PDF**: https://arxiv.org/pdf/2607.01557
- **详细分析**: [[20_Research/Papers/大模型/DiPS_Dialogue_Policy_Selection_for_High-Stakes_Persuasion_Agents|DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents]]
- **作者**: Tianyi Zhang, Mousumi Das, Abrar Anwar, Jesse Thomason, David Traum
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) often struggle with persuasion in high-stakes scenarios. People's individual personalities and concerns require tailored strategies rather than a one-size-fits-all approach. To address this challenge, we focus on a fire-rescue scenario in which an operator must persuade a resident to evacuate as a high-stakes persuasion domain and propose Dialogue Policy Selection (DiPS), a Q-learning framework to dynamically select persuasion strategies adapted to the evolving conversational context. Specifically, we train a critic, trained to maximize the chance of evacuation success, to select a persuasion policy at each turn based on the resident's recent utterances.We then evaluate DiPS against multiple baselines in both simulated and real human interactions. We find that DiPS achieves higher evacuation success than a zero-shot LLM and generic RAG-augmented approach.

</details>

---

### [[20_Research/Papers/大模型/OPINE-World_Programmatic_World_Modeling_with_Ontology-error-Prioritized_Interactive_Exploration|OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration]]

![[assets/2607.01531_figure.png|800]]

- **arXiv**: [2607.01531](https://arxiv.org/abs/2607.01531)
- **PDF**: https://arxiv.org/pdf/2607.01531
- **详细分析**: [[20_Research/Papers/大模型/OPINE-World_Programmatic_World_Modeling_with_Ontology-error-Prioritized_Interactive_Exploration|OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration]]
- **作者**: David Courtis, Wenhao Li, Scott Sanner
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.02（加权：大模型 0.3，强化学习 0.16，世界模型 0.56）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OPINE-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning how an environment behaves from interaction is central to building agents that adapt to unfamiliar tasks. World models learned with deep networks are flexible but data-hungry and transfer poorly beyond their training distribution. Program-synthesized world models, written as source code by LLMs and refined through counterexample-guided inductive synthesis (CEGIS), are instead data-efficient and reusable, yet they have been demonstrated mainly on structured-state worlds with a given object vocabulary, and a single program search does not scale to pixel-rendered environments whose object structure must be hypothesized flexibly. We introduce OPINE-World, an LLM agent that learns an object-centric programmatic world model online from interaction. OPINE-World couples two cooperating agents in a loop of hypothesis and test, one acting in the environment and one synthesizing the model in code with replay verification and model-based planning, and it steers exploration with a Bayesian measure of object-type adequacy we call ontology error. We evaluate OPINE-World on ARC-AGI-3, a benchmark for skill-acquisition efficiency in which the object vocabulary, the goal, and the action semantics are withheld. OPINE-World solves 20 of 25 games without per-game training and reaches an action-efficiency score of 78.4 against the human baseline.

</details>

---

### [[20_Research/Papers/大模型/Don't_Let_Gains_FADE_Breaking_Down_Policy_Gradient_Weights_in_RL|Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL]]

![[assets/2607.01490_figure.png|800]]

- **arXiv**: [2607.01490](https://arxiv.org/abs/2607.01490)
- **PDF**: https://arxiv.org/pdf/2607.01490
- **详细分析**: [[20_Research/Papers/大模型/Don't_Let_Gains_FADE_Breaking_Down_Policy_Gradient_Weights_in_RL|Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL]]
- **作者**: Juliette Decugis, Sean O'Brien, Francis Bach, Gabriel Synnaeve, Taco Cohen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LiveCodeBench, MaxRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning post-training dramatically improves LLM reasoning, but suffers from training instability and diversity collapse. Advantage functions offer an appealing fix: they reshape the training objective, reweight which rollouts drive learning, and are trivial to implement. Yet a proliferation of methods makes it unclear which advantage to use and when. We cut through the confusion with a unifying framework that decomposes any advantage into its positive and negative gradient mass along two orthogonal axes. On the sign axis, imbalanced updates collapse either entropy or weight geometry. On the difficulty axis, hard-problem focus sharpens signal but costs sample size. Both trade-offs shift during training: exploration favors balance and hard focus; exploitation favors suppression and medium focus. This motivates FADE (Focal Advantage with Dynamic Entropy), a self-adapting advantage that reads training dynamics to schedule the gradient weight automatically. FADE reaches peak pass@1 20k steps earlier than the best static baseline at the 7B scale and 2k steps earlier at the 32B , while achieving the best accuracy-diversity trade-off across all pass@k on LiveCodeBench and AIME.

</details>

---

### [[20_Research/Papers/大模型/MultAttnAttrib_Training-Free_Multimodal_Attribution_in_Long_Document_Question_Answering|MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question Answering]]

![[assets/2607.01420_figure.png|800]]

- **arXiv**: [2607.01420](https://arxiv.org/abs/2607.01420)
- **PDF**: https://arxiv.org/pdf/2607.01420
- **详细分析**: [[20_Research/Papers/大模型/MultAttnAttrib_Training-Free_Multimodal_Attribution_in_Long_Document_Question_Answering|MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question Answering]]
- **作者**: Dang Quang Thien Tran, Quang V. Dang, Vinamra Tyagi, Sai Soorya Rao Veeravalli, Trang Nguyen, Ryan A. Rossi, Franck Dernoncourt, Nedim Lipka, Koustava Goswami, Samyadeep Basu
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal

#### 研究背景与动机

《MultAttnAttrib: Training-Free Multimodal Attribution in Long Document Question Answering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MCiteBench, MultAttrEval, SciClaimEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As grounded QA systems are increasingly deployed in AI assistants, accurately attributing generated answers to evidence is critical for user trust and model safety. While unimodal attributions have been explored in depth, the multimodal setting remains relatively under-researched. As a result, we introduce MultAttnAttrib, a training-free attribution-generation method that leverages a model's prefill pass, selected attention heads, and calibrated thresholds to locate source evidence within a document. To establish baseline results for the method, we introduce MultAttrEval, a complementary benchmark dataset annotated with fine-grained, ground-truth attributions for answer components grounded in multimodal source documents. To our knowledge, this is the first evaluation dataset designed specifically for multimodal attribution in long-form documents. Experimental results show that MultAttnAttrib consistently outperforms a variety of attribution-generation methods, including several strong prompting-based approaches and matches the latest frontier models such as GPT 5.4. Our method not only substantially improves attribution accuracy for both unimodal and multimodal attribution types, but also produces attributions at up to one-seventh of the direct inference latency compared to prompting on the same base model.

</details>

---

### [[20_Research/Papers/大模型/Black-Box_Inference_of_LLM_Architectural_Properties_with_Restrictive_API_Access|Black-Box Inference of LLM Architectural Properties with Restrictive API Access]]

![[assets/2607.01313_figure.png|800]]

- **arXiv**: [2607.01313](https://arxiv.org/abs/2607.01313)
- **PDF**: https://arxiv.org/pdf/2607.01313
- **详细分析**: [[20_Research/Papers/大模型/Black-Box_Inference_of_LLM_Architectural_Properties_with_Restrictive_API_Access|Black-Box Inference of LLM Architectural Properties with Restrictive API Access]]
- **作者**: Christopher Ellis, Shreyas Chaudhari, Mei-Yu Wang, Leighton Barnes, Giulia Fanti, José M. F. Moura
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《Black-Box Inference of LLM Architectural Properties with Restrictive API Access》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Common-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In practice, most commercial LLM providers do not publicly release details of underlying LLM architectures. However, prior work has shown that given limited API access to an LLM (namely, top-$k$ logits and/or a logit bias function), one can recover certain architectural details of an LLM, such as the hidden dimension of the feed-forward network. Perhaps in response to these results, most commercial LLM providers have restricted their APIs to expose only the single logit for each decoded token, and they no longer give users the ability to bias logits. We show that even under current restrictive APIs, several architectural parameters are still recoverable. We present NightVision, an attack that uses restrictive black-box API access to estimate the hidden dimension, depth, and parameter count of an LLM. Algorithmically, NightVision relies on a novel common set prompting technique in which multiple prompts expose log probabilities for the same set of output tokens; a spectral analysis of these results is used to infer hidden dimension. NightVision additionally uses end-to-end time to first token (TTFT) measurements and the estimated hidden dimension to estimate depth and parameter count. We empirically evaluate NightVision on 32 open-source LLMs, recovering hidden dimension to within 23% average relative error across all models (9% on MoE models), and depth and parameter count to within 53% for models exceeding three billion parameters. We run extensive ablations to demonstrate how these accuracies scale with token budget and model properties. Overall, our results suggest that current LLM APIs are not sufficiently restricted to fully obfuscate the architectural details of their underlying models.

</details>

---

### [[20_Research/Papers/大模型/A_Practice_Auditing_Framework_for_Large_Language_Model_Use_Collective_Empiricism,_Pseudo-Rational_Cognition,_and_Governance_of_AI-Generated_|A Practice Auditing Framework for Large Language Model Use: Collective Empiricism, Pseudo-Rational Cognition, and Governance of AI-Generated Content]]

![[assets/2607.01248_first_page.png|800]]

- **arXiv**: [2607.01248](https://arxiv.org/abs/2607.01248)
- **PDF**: https://arxiv.org/pdf/2607.01248
- **详细分析**: [[20_Research/Papers/大模型/A_Practice_Auditing_Framework_for_Large_Language_Model_Use_Collective_Empiricism,_Pseudo-Rational_Cognition,_and_Governance_of_AI-Generated_|A Practice Auditing Framework for Large Language Model Use: Collective Empiricism, Pseudo-Rational Cognition, and Governance of AI-Generated Content]]
- **作者**: Yang Zhao, Yingshuo Li, Zeyu Zhang
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《A Practice Auditing Framework for Large Language Model Use: Collective Empiricism, Pseudo-Rational Cognition, and Governance of AI-Generated Content》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly used for knowledge acquisition, code generation, academic writing, and agent-based automation. In these settings, users may obtain highly structured answers, plans, and judgments without sufficient domain practice. This paper proposes a practice auditing framework for LLM use and AI-generated content governance. It introduces collective empiricism to describe how LLMs compress and reorganize large-scale human experience into outputs that appear empirical and rational, and pseudo-rational cognition to describe how users may mistake AI-generated structured expression for their own rational understanding. The paper analyzes AI subjectivity illusion, subjectivity structures in input materials, template loops in AI-AI conversations, statistical misjudgment in AIGC detection, and memory pollution when generated content enters future contexts, long-term memory, retrieval spaces, or agent skill systems. To reduce these risks, the paper proposes an auditing process based on requirement definition, problem-boundary identification, evidence-source auditing, practical validation, reverse questioning, logging, version management, rollback, and renewed cognition. The framework does not reject AI productivity; it argues that LLM outputs should be returned to verifiable, reproducible, and intervenable processes of practice. The paper provides a conceptual and auditable framework for cognitive risks in LLM interaction, AI-generated content governance, long-term memory systems, and human-AI interaction.

</details>

---

### [[20_Research/Papers/大模型/ExPerT_Personalizing_LLM_Responses_to_Users'_Domain_Expertise_via_Query-Wise_Semantic_and_Keystroke_Behavioral_Cues|ExPerT: Personalizing LLM Responses to Users' Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues]]

![[assets/2607.01242_first_page.png|800]]

- **arXiv**: [2607.01242](https://arxiv.org/abs/2607.01242)
- **PDF**: https://arxiv.org/pdf/2607.01242
- **详细分析**: [[20_Research/Papers/大模型/ExPerT_Personalizing_LLM_Responses_to_Users'_Domain_Expertise_via_Query-Wise_Semantic_and_Keystroke_Behavioral_Cues|ExPerT: Personalizing LLM Responses to Users' Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues]]
- **作者**: Yeji Park, Jiwon Tark, Taesik Gong
- **cs 子类**: cs.AI, cs.CL, cs.HC, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《ExPerT: Personalizing LLM Responses to Users' Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used by end users, yet existing personalization methods relying on static profiles or text-only signals fail to capture query-specific expertise variation. We present ExPerT, a query-wise personalization framework that adapts LLM responses to users' query domain expertise by combining semantic and behavioral cues. ExPerT consists of two key components: (i) a semantic-behavioral expertise inference module that jointly interprets query text and keystroke dynamics via in-context LLM prompting, and (ii) an expertise-conditioned response generation that adapts the level of detail, terminology, and conceptual complexity. Our user study with 40 participants and 1270 queries demonstrated that ExPerT reduced expertise inference error by 65.7% compared to the strongest baseline (MAE = 0.398 vs. 1.162) and improved response satisfaction by 17.52% (from 3.71 to 4.36) on a 5-point Likert scale.

</details>

---

### [[20_Research/Papers/大模型/Safeguarding_LLM_Agents_from_Misalignment_through_Provenance_Analysis|Safeguarding LLM Agents from Misalignment through Provenance Analysis]]

![[assets/2607.01236_figure.png|800]]

- **arXiv**: [2607.01236](https://arxiv.org/abs/2607.01236)
- **PDF**: https://arxiv.org/pdf/2607.01236
- **详细分析**: [[20_Research/Papers/大模型/Safeguarding_LLM_Agents_from_Misalignment_through_Provenance_Analysis|Safeguarding LLM Agents from Misalignment through Provenance Analysis]]
- **作者**: Yining She, Yiliang Liang, Eunsuk Kang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Safeguarding LLM Agents from Misalignment through Provenance Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, WorkBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLM agents gain increasing access to powerful tools, ensuring that their actions are aligned with the user's intent becomes critical. When an agent's proposed tool invocation deviates from the user's intent -- a phenomenon called misalignment -- it may lead to harmful consequences that are difficult to undo. Existing runtime guardrails rely on an LLM-as-a-judge paradigm that lacks a systematic framework for reasoning about alignment, often producing judgments that are inconsistent or difficult to audit. Motivated by provenance analysis, we propose a provenance-based conceptual framework that formalizes misalignment detection as determining whether a proposed tool call is supported by traceable evidence in the agent's context. Building on this framework, we propose ProvenanceGuard, a multi-stage pipeline that analyzes the agent's action for three types of misalignment before the selected tool is executed and only allows the action to take place when it is considered aligned with the user's input query. We evaluated our proposed approach on two different benchmarks, Agent-SafetyBench and WorkBench, across 10 backbone LLMs. Compared to the LLM-as-a-judge baseline, ProvenanceGuard reduces error rate on misaligned traces from 42.9% to 1.8% on Agent-SafetyBench and from 32.1% to 17.3% on WorkBench, while reducing intervention burden on task-successful traces from 30.5% to 12.8% and introducing no statistically significant increase in unnecessary interventions on aligned traces. These results demonstrate that structured, provenance-based reasoning provides an effective and practical foundation for safeguarding LLM agents from misalignment.

</details>

---
