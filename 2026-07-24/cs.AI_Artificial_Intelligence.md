# cs.AI | Artificial Intelligence | 2026-07-24

#arxiv #ComputerScience

**论文数**: 50

### [[20_Research/Papers/大模型/OpenForgeRL_Train_Harness-native_Agents_in_Any_Environment|OpenForgeRL: Train Harness-native Agents in Any Environment]]

![[assets/2607.21557_figure.png|800]]

- **arXiv**: [2607.21557](https://arxiv.org/abs/2607.21557)
- **PDF**: https://arxiv.org/pdf/2607.21557
- **详细分析**: [[20_Research/Papers/大模型/OpenForgeRL_Train_Harness-native_Agents_in_Any_Environment|OpenForgeRL: Train Harness-native Agents in Any Environment]]
- **作者**: Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《OpenForgeRL: Train Harness-native Agents in Any Environment》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ClawEval, OSWorld, OpenForgeRL, QwenClawBench, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. By decoupling training and inference, OpenForgeRL allows researchers to easily train, study, and improve agents directly in the real harnesses and environments they are deployed with. We validate our framework across diverse, complex harnesses and environments, spanning tool/claw-based agents and multimodal GUI browser- and computer-use agents. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Both outperform open baselines of similar size on nearly all benchmarks, and in the GUI setting match or surpass models several times larger. Beyond benchmarks, we analyze how harness choice (e.g., ZeroClaw, OpenClaw, Codex) and RL shape agent behavior. We find that some harnesses are substantially harder to learn than others, and that RL improves agentic reliability, such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak.

</details>

---

### [[20_Research/Papers/大模型/MIRROR_Learning_from_the_Other_View_for_Multi-Modal_Reasoning|MIRROR: Learning from the Other View for Multi-Modal Reasoning]]

![[assets/2607.21552_figure.png|800]]

- **arXiv**: [2607.21552](https://arxiv.org/abs/2607.21552)
- **PDF**: https://arxiv.org/pdf/2607.21552
- **详细分析**: [[20_Research/Papers/大模型/MIRROR_Learning_from_the_Other_View_for_Multi-Modal_Reasoning|MIRROR: Learning from the Other View for Multi-Modal Reasoning]]
- **作者**: Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《MIRROR: Learning from the Other View for Multi-Modal Reasoning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LeanGeo-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent text, diagram, and combined diagram+text views. We show that these views often elicit different behaviors: a model may solve a problem from text but fail on the corresponding diagram, or succeed visually while failing textually. This inconsistency suggests that different views expose complementary reasoning paths and failure modes that standard multimodal post-training does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined image+text views of the same problems, together with splits for training and evaluating modality-dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning Optimization (MIRROR), a reinforcement learning approach for improving multimodal reasoning via self supervision. For each problem, MIRROR evaluates the model under all views, selects the best-performing view as a teacher, and trains other views with a reverse-KL objective towards the teacher. Across reasoning benchmarks that evaluate on geometry problems, MIRROR improves over standard RL and yields more accurate and consistent behavior across modalities

</details>

---

### [[20_Research/Papers/具身智能/GS-Agent_Creating_4D_Physical_Worlds_With_Generative_Simulation|GS-Agent: Creating 4D Physical Worlds With Generative Simulation]]

![[assets/2607.21522_figure.png|800]]

- **arXiv**: [2607.21522](https://arxiv.org/abs/2607.21522)
- **PDF**: https://arxiv.org/pdf/2607.21522
- **详细分析**: [[20_Research/Papers/具身智能/GS-Agent_Creating_4D_Physical_Worlds_With_Generative_Simulation|GS-Agent: Creating 4D Physical Worlds With Generative Simulation]]
- **作者**: Hongxin Zhang, Chunru Lin, Junyan Li, Zhou Xian, Tsun-Hsuan Wang, Chuang Gan
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.65（加权：具身智能 0.6，大模型 0.75，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《GS-Agent: Creating 4D Physical Worlds With Generative Simulation》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Creating dynamic and physically realistic 4D worlds from natural language descriptions is both fascinating and challenging. Traditional computer graphics methods rely on manual creation, requiring extensive human effort to fine-tune materials, motions, and visual fidelity. Recent advances in generative foundation models have sparked interest in learning to generate such 4D worlds from large-scale data; however, existing methods still struggle to ensure physical plausibility and controllability. In this work, we take a different path by leveraging foundation models to construct an agentic system that emulates how humans traditionally create 4D worlds, yet automates the entire process. We present GS-Agent, an end-to-end multi-agent framework that integrates physics engines in the loop to generate realistic, dynamic, and controllable 4D physical worlds from natural language. Inspired by how humans build 4D worlds, GS-Agent decomposes the task into entity management, covering 3D asset curation, material tuning, placement, and motion control, and rendering configuration, including camera and lighting manipulation. Multiple agents with distinct expertise interact with the physics engine via code, seek multimodal feedback, and collaborate to iteratively construct 4D worlds that align with the given descriptions. Experimental results show that GS-Agent effectively converts natural language into diverse and physically plausible 4D worlds exhibiting rich interactions among liquids, deformable objects, and rigid bodies, while achieving cinematic camera and lighting control. We envision GS-Agent as a foundation for a new paradigm in 4D world generation, empowering creative content creation and physical AI. Project page at https://umass-embodied-agi.github.io/gs-agent/

</details>

---

### [[20_Research/Papers/具身智能/Compact_Latent_Coordination_for_Autonomous_Vehicles_at_Unsignalized_Intersections|Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections]]

![[assets/2607.21488_figure.jpg|800]]

- **arXiv**: [2607.21488](https://arxiv.org/abs/2607.21488)
- **PDF**: https://arxiv.org/pdf/2607.21488
- **详细分析**: [[20_Research/Papers/具身智能/Compact_Latent_Coordination_for_Autonomous_Vehicles_at_Unsignalized_Intersections|Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections]]
- **作者**: Gil Lifshits, Igal Bilik, Gilad Katz
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.2，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CommNet, DRL, MADRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent generates a compact, continuous embedding, denoted as proto-plan, that encodes a global coordination strategy. Decentralized Worker agents integrate this embedding with local observations to execute vehicle-specific control, decoupling strategic intent from tactical execution and enabling independent optimization of each module. As a proof-of-concept evaluation of this coordination mechanism, we test MAPS across 72 intersection configurations in HighwayEnv. MAPS achieves collision-free navigation while significantly reducing average travel time, outperforming state-of-the-art baselines. The learned proto-plans further exhibit robust generalization: a system trained with three agents achieves a 94% success rate when deployed zero-shot to five-agent scenarios, confirming that proto-plan-based hierarchical learning provides a promising framework for multi-vehicle coordination.

</details>

---

### [[20_Research/Papers/强化学习/AREX_Towards_a_Recursively_Self-Improving_Agent_for_Deep_Research|AREX: Towards a Recursively Self-Improving Agent for Deep Research]]

![[assets/2607.21461_figure.png|800]]

- **arXiv**: [2607.21461](https://arxiv.org/abs/2607.21461)
- **PDF**: https://arxiv.org/pdf/2607.21461
- **详细分析**: [[20_Research/Papers/强化学习/AREX_Towards_a_Recursively_Self-Improving_Agent_for_Deep_Research|AREX: Towards a Recursively Self-Improving Agent for Deep Research]]
- **作者**: Shuqi Lu, Chaofan Li, Kun Luo, Zhang Zhang, Hui Wang, Hongwang Xiao, Zheng Liu, Lei Xiong, Jiahao Wang, Sen Wang, Xiyan Jiang, Wanli Li...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《AREX: Towards a Recursively Self-Improving Agent for Deep Research》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeepSearchQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do more than simply search longer: it should recursively improve its current answer by verifying intermediate results and using the partially verified state to guide subsequent refinement. We introduce AREX, a family of Recursively Self-Improving (RSI) deep research agents. AREX alternates between an inner research loop that gathers evidence and constructs a provisional answer, and an outer self-improvement loop that audits the answer constraint-wise, identifies unresolved claims, and launches targeted follow-up research. To sustain RSI over long horizons, AREX learns an autonomous context-update tool that compresses growing interaction history into a compact improvement state preserving verified evidence and unresolved constraints, without relying on an external model. We train AREX on verified synthetic tasks and high-quality trajectories through agentic mid-training and long-horizon reinforcement learning. To mitigate sparse final rewards during long horizon learning, we emphasize key steps where decisive evidence is acquired or erroneous research directions are corrected. We instantiate a dense 4B model and a 122B-A10B Mixture-of-Experts model. Across BrowseComp, WideSearch, DeepSearchQA, Humanity's Last Exam (HLE), and other reasoning and tool-use benchmarks, AREX substantially outperforms comparable-scale baselines and remains competitive with models using substantially more activated parameters.

</details>

---

### [[20_Research/Papers/大模型/PATS_Policy-Aware_Training_Scaffolding_for_Agentic_Reinforcement_Learning|PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning]]

![[assets/2607.21419_figure.png|800]]

- **arXiv**: [2607.21419](https://arxiv.org/abs/2607.21419)
- **PDF**: https://arxiv.org/pdf/2607.21419
- **详细分析**: [[20_Research/Papers/大模型/PATS_Policy-Aware_Training_Scaffolding_for_Agentic_Reinforcement_Learning|PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning]]
- **作者**: Yipeng Shi, Zhipeng Ma, Yue Wang, Qitai Tan, Yang Li, Peng Chen, Zhengzhou Zhu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.2，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ActGuide-RL, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. However, they remain centered on the skills themselves rather than being designed as adaptive training-time support for the evolving policy. To address this, we propose a policy-centric training paradigm that reframes skills as a dynamic training scaffold. Our framework, Pats, converts rollout groups from the latest policy into evidence cards and uses task-specific evaluation to adjust the context used in subsequent rollouts. Concrete guidance helps weak policies to complete challenging tasks. As policy improves, redundant context is revised or removed to reduce reliance on explicit guidance while preserving useful rollout variation. The policy is optimized with environmental rewards using standard RLVR, and the training scaffold is discarded at deployment. On ALFWorld and WebShop, Pats improves over strong baselines by up to 18.6%. Across seven search-augmented QA benchmarks, it remains competitive while using 32.1% fewer prompt tokens than the baseline.

</details>

---

### [[20_Research/Papers/具身智能/VoLN_Vision-Only_Long-Horizon_Navigation---Paradigm,_Benchmark,_and_Method|VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method]]

![[assets/2607.21400_figure.png|800]]

- **arXiv**: [2607.21400](https://arxiv.org/abs/2607.21400)
- **PDF**: https://arxiv.org/pdf/2607.21400
- **详细分析**: [[20_Research/Papers/具身智能/VoLN_Vision-Only_Long-Horizon_Navigation---Paradigm,_Benchmark,_and_Method|VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method]]
- **作者**: Jiabin Lou, Haopeng Wang, Yuanshuai Wang, Xinyu Liu, Xuxin Lv, Yuxin Guo, Lei Huang, Rongye Shi, Wenjun Wu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《VoLN: Vision-Only Long-Horizon Navigation---Paradigm, Benchmark, and Method》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-Language Navigation (VLN) enables embodied agents to follow natural-language instructions. However, route-level instructions commonly encode spatial priors, such as orientation, distance, and layout, that are not explicitly available from onboard sensing at deployment in open, GPS-denied environments. Benchmark performance under such interfaces therefore jointly reflects visual navigation ability and the use of route structure explicitly supplied by the task description. As a complementary formulation, we propose Vision-Only Long-Horizon Navigation (VoLN), which shifts route-relevant information from externally supplied instructions and global guidance to locally observable in-scene cues. In VoLN, goal views specify the destination, while route-relevant information is available only through locally observable in-scene cues that the agent must detect, interpret, and select online. We instantiate VoLN for aerial navigation through VoLN-UAV, a 7,210-episode benchmark that combines long-horizon goal-directed flight, continuous 3D motion, large viewpoint changes, and context-dependent beacon selection. We further provide VoLN-MLLM as an initial reference baseline. It aligns self-supervised visual features with a structured semantic space and predicts short-horizon waypoint segments from observation history, goal views, retrieved visual--semantic tokens, and proprioception. On the five-environment Test-Unseen split, it obtains success rates of 7.4%, 4.5%, and 1.8% on Easy, Normal, and Hard episodes, respectively. These results provide an initial evaluation of VoLN and reveal substantial remaining challenges in long-horizon evidence integration, cross-view goal matching, and closed-loop stability. Project page: https://admire-ljb.github.io/VoLN-UAV/

</details>

---

### [[20_Research/Papers/大模型/GRADRAG_Cross-Component_Prompt_Adaptation_for_Coordinated_Multi-Agent_RAG|GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG]]

![[assets/2607.21324_figure.png|800]]

- **arXiv**: [2607.21324](https://arxiv.org/abs/2607.21324)
- **PDF**: https://arxiv.org/pdf/2607.21324
- **详细分析**: [[20_Research/Papers/大模型/GRADRAG_Cross-Component_Prompt_Adaptation_for_Coordinated_Multi-Agent_RAG|GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG]]
- **作者**: Paolo Pedinotti, Enrico Santus
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) systems increasingly employ multiple LLM agents. Yet, most prior work optimizes components in isolation rather than coordinating improvements across the pipeline. We introduce GRADRAG, a framework for cross-component prompt adaptation that models the RAG pipeline as a computational graph and propagates structured evaluation feedback to update upstream agents. An Evaluator critiques downstream answers and supporting evidence, producing actionable feedback that a Prompt Optimizer uses to iteratively update adaptive agents, such as retrievers, graph constructors, and answerers. The Evaluator also triggers early stopping when the output is deemed satisfactory. We evaluate GRADRAG on the SQUALITY and QMSUM benchmarks under two retrieval paradigms: flat chunk-based retrieval using IRCoT-style query refinement (Trivedi et al., 2023), and graph-based retrieval that constructs and iteratively enriches an entity-relation graph from the document. Across both settings, GRADRAG consistently outperforms one-step refinement baselines that update only the final generator, achieving a 12-15 percentage point net preference margin in LLM-judged pairwise comparisons, with most gains realized within two refinement iterations.

</details>

---

### [[20_Research/Papers/强化学习/Expert_Behavior_Prior_Reinforcement_Learning|Expert Behavior Prior Reinforcement Learning]]

![[assets/2607.21302_figure.png|800]]

- **arXiv**: [2607.21302](https://arxiv.org/abs/2607.21302)
- **PDF**: https://arxiv.org/pdf/2607.21302
- **详细分析**: [[20_Research/Papers/强化学习/Expert_Behavior_Prior_Reinforcement_Learning|Expert Behavior Prior Reinforcement Learning]]
- **作者**: Gong Gao, Weidong Zhao, Xianhui Liu, Ning Jia
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.1，强化学习 1，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Expert Behavior Prior Reinforcement Learning》归入 强化学习、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BPRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavior prior reinforcement learning (BPRL) has emerged as a promising paradigm to improve sample efficiency in online reinforcement learning (RL) by leveraging policy priors derived from offline demonstrations. However, most existing BPRL methods rely on static offline datasets, which often suffer from low data diversity and suboptimal trajectory quality. This reliance restricts the effectiveness of policy priors, hindering both policy exploitation and stability during online training. Consequently, agents are prone to inefficient exploration and unstable learning dynamics. To address these limitations, we deviate from existing offline pre-training methods and propose an Expert Behavior Prior (EBP) algorithm. Specifically, we introduce a Q-guided conditional variational autoencoder (Q-CVAE) that learns to generate expert policy priors directly from the online replay buffer. This enables the generation of high-value actions for guiding policy updates without relying on pre-collected expert trajectories. To further enhance policy exploitation, we propose an expert policy guidance (EPG) mechanism that selects expert actions from a generative support set, and we integrate a policy gradient correction (PGC) module to harmonize Q-guidance with expert supervision, promoting stable and consistent policy improvement. Extensive experiments conducted on robotic control (Gym, PyBullet) and industrial control (DMControl) benchmarks demonstrate that EBP significantly outperforms state-of-the-art online RL algorithms, achieving higher sample efficiency and more stable convergence.

</details>

---

### [[20_Research/Papers/大模型/Unlearning_Under_Imbalance_Benchmarking_Fairness_in_Multimodal_LLM_Unlearning|Unlearning Under Imbalance: Benchmarking Fairness in Multimodal LLM Unlearning]]

![[assets/2607.21300_figure.png|800]]

- **arXiv**: [2607.21300](https://arxiv.org/abs/2607.21300)
- **PDF**: https://arxiv.org/pdf/2607.21300
- **详细分析**: [[20_Research/Papers/大模型/Unlearning_Under_Imbalance_Benchmarking_Fairness_in_Multimodal_LLM_Unlearning|Unlearning Under Imbalance: Benchmarking Fairness in Multimodal LLM Unlearning]]
- **作者**: Lorenzo Orsingher, Thomas De Min, Massimiliano Mancini, Davide Talon, Elisa Ricci
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Unlearning Under Imbalance: Benchmarking Fairness in Multimodal LLM Unlearning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FIUBench, MLLMU-Bench, MMUBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Machine unlearning has emerged as a tool for removing personal data from trained models to comply with recent AI regulations. To evaluate unlearning effectiveness in multimodal large language models (MLLMs), prior works fine-tune models on fictitious identities, simulating unlearning requests on subsets of these IDs, which are typically uniformly distributed. However, in realistic scenarios, people from different demographic groups may request to be unlearned at different frequencies, potentially altering the model's internal beliefs for these groups and leading to biased behaviors. To fill this gap, we propose FAIRGET, the first Visual Question Answering benchmark that evaluates unlearning under unbalanced, realistic, forget requests. These requests are designed to simulate multiple realistic scenarios, ranging from simple to challenging settings, that lead to biased unlearned models if fairness is not accounted for. Additionally, we propose FAUN, the first unlearning algorithm for MLLMs that forgets unlearning data while preserving model fairness. FAUN exploits a bias-aware activation steering mechanism to unlearn identities while accounting for the unbalanced nature of the forget data. Experiments on FAIRGET and the established FIUBench demonstrate our method's superiority both in unlearning quality and fairness.

</details>

---

### [[20_Research/Papers/大模型/pAI-Econ-claude_A_Gated_Human-in-the-Loop_Multi-Agent_Architecture_for_AI-Assisted_Economic_Theory_Development|pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development]]

![[assets/2607.21268_figure.png|800]]

- **arXiv**: [2607.21268](https://arxiv.org/abs/2607.21268)
- **PDF**: https://arxiv.org/pdf/2607.21268
- **详细分析**: [[20_Research/Papers/大模型/pAI-Econ-claude_A_Gated_Human-in-the-Loop_Multi-Agent_Architecture_for_AI-Assisted_Economic_Theory_Development|pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development]]
- **作者**: Chen Zhu, Xiaolu Wang, Weilong Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In many social-science research tasks, such as economics, LLM-based agents must produce outputs for which no cheap, task-complete, machine-readable correctness signal exists. This creates a distinctive reliability problem for multi-agent systems: how should generation, critique, coordination, and human judgment be organized when no component can certify the final result? We address this problem through pAI-Econ-claude, a gated, human-in-the-loop multi-agent architecture for AI-assisted economic theory development. Agents coordinate through a shared workspace of inspectable intermediate records; specialized gates diagnose targeted failure modes and recommend loopbacks without certifying correctness; and human checkpoints retain authority over decisions that are costly to reverse. We evaluate the architecture on five matched economic-theory tasks against an ungated baseline. Two evaluators blinded to configuration agreed on all five pairwise rankings, preferring the gated architecture in four tasks and the baseline in one. Mean failure severity fell from 1.58 to 1.16, while overall usefulness rose from 2.60 to 3.10. The largest observed gain occurred when a reality check rejected a false market-structure premise and a proof review prompted revision of a false welfare claim. The negative case shows that scaffolding can also compress an economically important mechanism too aggressively. The results support a bounded claim: gated oversight improves the auditability of AI-assisted economic theory without substituting for formal verification, and the allocation of irreversible human judgment is a more informative design variable than pure agent autonomy. The workflow is publicly available at https://github.com/maxwell2732/pAI-Econ-claude.

</details>

---

### [[20_Research/Papers/大模型/Case_study_solving_P-99_with_LPTP_and_an_LLM|Case study: solving P-99 with LPTP and an LLM]]

![[assets/2607.21196_first_page.png|800]]

- **arXiv**: [2607.21196](https://arxiv.org/abs/2607.21196)
- **PDF**: https://arxiv.org/pdf/2607.21196
- **详细分析**: [[20_Research/Papers/大模型/Case_study_solving_P-99_with_LPTP_and_an_LLM|Case study: solving P-99 with LPTP and an LLM]]
- **作者**: Fred Mesnard, Thierry Marianne, Étienne Payet, Wim Vanhoof
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《Case study: solving P-99 with LPTP and an LLM》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ninety-Nine Prolog Problems (P-99) is a famous set of Prolog exercises. We solved the first thirty three just by prompting an LLM (Large Language Model). We used Claude from Anthropic. By solved we mean: generate the Prolog code and a test file, run the tests and check whether they pass, then formally prove types, groundness, termination, uniqueness, existence and also sometimes functional correctness with LPTP (Logic Program Theorem Prover). Hence our approach is an experiment in vibe-coding/vericoding of P-99. It is a vibe-coding experiment because we started from informal specifications written in English and let Claude generate the Prolog code. It also fits within vericoding because the LLM proved reliability guarantees on the generated Prolog code. Claude wrote 58 logic procedures, 508 tests, 257 lemmas for a total of 11800 proof lines. We manually checked each file generated by the LLM. We checked the Prolog code, ran the tests, examined the logical statements generated by Claude and proof-checked Claude's proofs with LPTP. This paper describes this experiment and provides the main details so that it can be reproduced by the interested reader.

</details>

---

### [[20_Research/Papers/大模型/Case_study_proving_sqrt(2)_irrational_with_LPTP_and_an_LLM|Case study: proving sqrt(2) irrational with LPTP and an LLM]]

![[assets/2607.21187_first_page.png|800]]

- **arXiv**: [2607.21187](https://arxiv.org/abs/2607.21187)
- **PDF**: https://arxiv.org/pdf/2607.21187
- **详细分析**: [[20_Research/Papers/大模型/Case_study_proving_sqrt(2)_irrational_with_LPTP_and_an_LLM|Case study: proving sqrt(2) irrational with LPTP and an LLM]]
- **作者**: Fred Mesnard, Étienne Payet, Wim Vanhoof
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Case study: proving sqrt(2) irrational with LPTP and an LLM》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present the interactions with an LLM (Large Language Model) aiming at proving that the square root of 2 is not a rational number in an LP (Logic Programming) context. We start from a few basic pure logic programming predicate definitions. We rely on the LPTP (Logic Program Theorem Prover) system for stating and proving properties about logic programs. As the proof language of LPTP is based on natural deduction, the proofs are human readable. In our case study, we sketch in LPTP the usual proof showing the irrationality of the square root of 2. Then we describe the interactions we had with the LLM. We end up with a complete formal proof, partially generated by an LLM and fully proof-checked by LPTP.

</details>

---

### [[20_Research/Papers/具身智能/TOUR_A_Trajectory-Level_Unlearning_Benchmark_for_Offline_Reinforcement_Learning|TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning]]

![[assets/2607.21111_figure.png|800]]

- **arXiv**: [2607.21111](https://arxiv.org/abs/2607.21111)
- **PDF**: https://arxiv.org/pdf/2607.21111
- **详细分析**: [[20_Research/Papers/具身智能/TOUR_A_Trajectory-Level_Unlearning_Benchmark_for_Offline_Reinforcement_Learning|TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning]]
- **作者**: Chaofan Pan, Lingfei Ren, Xiangyu Jiang, Yanhua Li, Xuemei Cao, Xiangkun Wang, Hao Yu, Wei Wei, Xin Yang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.72（加权：具身智能 0.3，大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline Reinforcement Learning (RL) agents are trained on fixed behavioral trajectories, which makes trajectory-level deletion important when selected data must be removed after training. Evaluating such deletion is difficult because a lower membership score can reflect trajectory removal, residual memorization visible to another attack, or policy collapse that destroys useful behavior. We introduce Trajectory-level memOrization and Unlearning in offline RL (TOUR), a benchmark that combines trajectory-level partitioning, matched non-member controls, retraining references, retained-performance anchors, and multi-attack privacy auditing. Across D4RL locomotion experiments and an exploratory AntMaze extension, TOUR shows that common deletion baselines have environment-dependent privacy-utility behavior. Retraining and fine-tuning often provide stronger retained-utility references than uniform GA+Refit, while TrajDeleter remains a useful comparator but is not uniformly stronger under the same audit. Reference-model, threshold, deviation, equivalence, action-error, representation-based, and query-limited attacks further show that a single likelihood-based membership score can overstate deletion quality. In the evaluated settings, conclusions about offline RL unlearning are therefore not stable under single-score auditing. They depend on matched non-member construction, retraining-relative calibration, attack family, retained utility, and explicit scope for diagnostic architecture or component-level evidence.

</details>

---

### [[20_Research/Papers/大模型/AttriMem_Attribution-Guided_Process_Feedback_for_Agent_Memory_Learning|AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning]]

![[assets/2607.21106_figure.png|800]]

- **arXiv**: [2607.21106](https://arxiv.org/abs/2607.21106)
- **PDF**: https://arxiv.org/pdf/2607.21106
- **详细分析**: [[20_Research/Papers/大模型/AttriMem_Attribution-Guided_Process_Feedback_for_Agent_Memory_Learning|AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning]]
- **作者**: Qinfeng Li, Yuntai Bao, Xinyan Yu, Hongze Chen, Wenqi Zhang, Xuhong Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals indicate task success but cannot identify which intermediate memory contents support the final answer, creating a fine-grained credit-assignment bottleneck. However, constructing such process feedback is prohibitively difficult because intermediate memory decisions lack unique ground-truth targets, while the appropriate credit varies with the agent's uncertain reasoning trajectory and therefore cannot be specified in advance. We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. AttriMem augments the global outcome reward with local rewards derived from token-level contributions to the final answer. Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

</details>

---

### [[20_Research/Papers/大模型/Training_Large_Language_Models_for_Self-Explanation_Faithfulness|Training Large Language Models for Self-Explanation Faithfulness]]

![[assets/2607.21090_figure.png|800]]

- **arXiv**: [2607.21090](https://arxiv.org/abs/2607.21090)
- **PDF**: https://arxiv.org/pdf/2607.21090
- **详细分析**: [[20_Research/Papers/大模型/Training_Large_Language_Models_for_Self-Explanation_Faithfulness|Training Large Language Models for Self-Explanation Faithfulness]]
- **作者**: Yeoktatt Cheah, María Pérez-Ortiz, Noah Y. Siegel, Oana-Maria Camburu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.87（加权：大模型 0.35，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Training Large Language Models for Self-Explanation Faithfulness》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Social-IQA, StrategyQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose a Reinforcement Learning (RL) method to directly optimize the faithfulness of self-explanations - the extent to which a model's generated reasoning accurately reflects its internal decision-making process. While existing work focuses on evaluating faithfulness or using inference-time prompting frameworks to improve an LLM's self-explanation's tractability, these approaches do not provide a mechanism to directly optimize a model's parameters to generate faithful self-explanations. We bridge this gap by modifying existing faithfulness metrics into an RL training objective. We investigate (1) if models can be trained to accurately detect factors that affect their decisions, and (2) whether RL can directly optimize for the disclosure of these factors thereby improving LLM self-explanations' faithfulness. We experiment with two intervention types: random-word insertions and user-bias insertions, using a per-sample reward derived from the Phi-CCT correlation metric. RL fine-tuned Llama3.1-8B and Qwen3-8B show substantial improvements on the Phi-CCT faithfulness metric, with in-distribution scores rising from near-zero to as high as 0.664, and out-of-distribution scores reaching up to 0.691 on held-out tasks such as StrategyQA. Cross-intervention generalization is weaker but more interesting: a priori we would not expect a model trained only on random word insertions to generalize to user-bias phrases, yet Llama3.1-8B shows non-zero transfer in this direction. The reverse direction and Qwen3-8B do not replicate this, indicating model-dependent and setup-dependent effects we cannot yet explain. Lastly we analyze model behavior to rule out reward gaming behaviors that often plague RL training. Ultimately, we show that models can be trained to implicitly identify influential factors and disclose them, offering a scalable path toward reducing unfaithful reasoning in LLMs.

</details>

---

### [[20_Research/Papers/大模型/HiMe_Real-Time_Self-Hosted_Personal_Agent_Platform_for_Health_Insights_with_Wearable_Devices|HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices]]

![[assets/2607.21019_figure.png|800]]

- **arXiv**: [2607.21019](https://arxiv.org/abs/2607.21019)
- **PDF**: https://arxiv.org/pdf/2607.21019
- **详细分析**: [[20_Research/Papers/大模型/HiMe_Real-Time_Self-Hosted_Personal_Agent_Platform_for_Health_Insights_with_Wearable_Devices|HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices]]
- **作者**: Wei Liu, Siya Qi, Linhai Zhang, Lorainne Tudor Car, Yulan He
- **cs 子类**: cs.AI, cs.CL, cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional approaches to wearable health signal analysis, such as smartwatches, are constrained by rigid analytical frameworks and limited personalisation. The emergence of LLM agents creates a new opportunity for Personal Health Agentic Analysis, where health insights can be generated adaptively and in context. However, currently there is no open-source locally deployable platform capable of processing personal health data in real time while preserving privacy. We present HiMe, a locally deployable, privacy-first agent platform that is fully compatible with real-time health data ecosystems across a wide range of wearable devices. HiMe is guided by three design principles. The database is treated as a first-class component. Effectiveness and efficiency are jointly optimised to achieve a low-cost Pareto-optimal balance. Data are processed in real time while the user is modelled over the long term. Together, these principles make it practical for individuals to harness Personal Health Agents for continuous, personalised health monitoring for better wellbeing.

</details>

---

### [[20_Research/Papers/大模型/EmoAgent-R1_Towards_Multimodal_Emotion_Understanding_with_Reinforcement_Learning-based_Dynamic_Agent_Specialization|EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization]]

![[assets/2607.21013_figure.png|800]]

- **arXiv**: [2607.21013](https://arxiv.org/abs/2607.21013)
- **PDF**: https://arxiv.org/pdf/2607.21013
- **详细分析**: [[20_Research/Papers/大模型/EmoAgent-R1_Towards_Multimodal_Emotion_Understanding_with_Reinforcement_Learning-based_Dynamic_Agent_Specialization|EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization]]
- **作者**: Lihuang Fang, Yuchen Zou, kebin Jin, Jinghui Qin
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.9，强化学习 1）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《EmoAgent-R1: Towards Multimodal Emotion Understanding with Reinforcement Learning-based Dynamic Agent Specialization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MER-UniBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have achieved impressive performance in multimodal emotion recognition (MER) tasks and lifted MER to a new level that is complex emotion understanding with advanced video understanding abilities and natural language description. However, existing MLLM-based methods often use a fixed prompt to perceive the emotions, ignoring the dynamicity and complexity of the emotion source in the multimodal inputs. To address these issues, we propose a novel Reinforcement Learning-based Dynamic Agent Specialization framework (\textbf{EmoAgent-R1}) to optimize the emotion recognition, reasoning, and generalization abilities of an MLLM with dynamic agent specialization based on reinforcement learning. Specifically, we first adopt a cold start strategy to endow an MLLM with preliminary emotion recognition, reasoning, and agent routing ability by training with synthetic answer-conditioned chain-of-thought data and agent routing data. Then, we further train the MLLM with reinforcement learning to perceive emotions in a two-step agentic workflow with agent selection and agent specialization. To effectively train EmoAgent-R1, we propose a novel Progressive Group-Relative Policy Optimization (P-GRPO) to combine group-based relative advantages with a PMI-inspired progressive token-level modulation to transform sparse rewards into fine-grained learning signals, mitigating the coarse-grained uniform credit assignment issue in GRPO. Extensive experiments on MER benchmarks demonstrate the superiority of our EmoAgent-R1 in stronger emotion reasoning performance and improved optimization stability.

</details>

---

### [[20_Research/Papers/具身智能/HyWorldVLA_A_Vision-Language-Action_Model_with_Hybrid_World_Modeling_for_Autonomous_Driving|HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving]]

![[assets/2607.20988_figure.png|800]]

- **arXiv**: [2607.20988](https://arxiv.org/abs/2607.20988)
- **PDF**: https://arxiv.org/pdf/2607.20988
- **详细分析**: [[20_Research/Papers/具身智能/HyWorldVLA_A_Vision-Language-Action_Model_with_Hybrid_World_Modeling_for_Autonomous_Driving|HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving]]
- **作者**: Quanfu Yu, Xian Wu, Hao Xu, Liulong Ma
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 1.9（加权：具身智能 1.5，世界模型 0.4）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving》归入 具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AutoVLA, DriveVLA, HyWorldVLA, OpenDriveVLA, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models augmented with world modeling represent a promising paradigm for end-to-end autonomous driving. While pixel-level future prediction enables fine-grained spatiotemporal reasoning, it compromises robustness in noisy driving scenarios. Conversely, latent-based world models alleviate this sensitivity but often incur limited interpretability and representational degradation due to absent pixel-level grounding. To reconcile this trade-off, we propose HyWorldVLA, a hybrid world-VLA framework that unifies pixel-level supervision and latent representation learning. In the pre-training stage, HyWorldVLA predicts video latents encoded by a pre-trained video VAE, while simultaneously reconstructing video frames to provide precise pixel-level grounding. During the subsequent co-fine-tuning phase, the model exclusively predicts latent features, which are fed into an action expert to generate trajectories. Extensive experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly outperforms both pixel-based and latent-based world model baselines. Notably, we present the first comprehensive qualitative and quantitative analysis of world model noise robustness in autonomous driving, establishing a new benchmark for evaluating future architectures.

</details>

---

### [[20_Research/Papers/大模型/GuardianAgentBench_Where_Agents_Fail_and_How_to_Guard_Them|GuardianAgentBench: Where Agents Fail and How to Guard Them]]

![[assets/2607.20982_figure.jpeg|800]]

- **arXiv**: [2607.20982](https://arxiv.org/abs/2607.20982)
- **PDF**: https://arxiv.org/pdf/2607.20982
- **详细分析**: [[20_Research/Papers/大模型/GuardianAgentBench_Where_Agents_Fail_and_How_to_Guard_Them|GuardianAgentBench: Where Agents Fail and How to Guard Them]]
- **作者**: Vishal Ishwar Naik, Chenyu Xu, Donna Dong, Hussein Hassan, Abhishek Pradhan, Ofer Mendelevitch, Tallat Shafat, Humayun Irshad
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《GuardianAgentBench: Where Agents Fail and How to Guard Them》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ASSEBench, Agent-SafetyBench, AgentSafetyBench, GABench, GuardianAgentBench, MobileSafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model agents increasingly operate autonomously with access to tools and external environments, ensuring their safe and reliable behavior becomes critical. We present GuardianAgentBench (GABench), a benchmark of 580 scenarios across six domains evaluated on three production-ready frameworks: LangChain, LlamaIndex, and Vectara. The benchmark incorporates rigorous multi-stage validation and five adversarial attack modes. Experiments with six state-of-the-art models reveal that even the strongest configuration achieves only 74.8% overall accuracy and expose two distinct failure regimes: stronger models under-call required tools, while weaker models mis-select and over-call tools. Performance degrades monotonically with both tool-set size and sequential turn depth, with long-horizon planning proving the steeper bottleneck. Our guardrail implementation consistently outperforms system-prompt-based defenses across all models, recovering 19.9% of failures at a false positive rate of just 0.5%. These results demonstrate that execution-time structural intervention improves safety without disrupting correct agent behavior.

</details>

---

### [[20_Research/Papers/大模型/Scientific_exploration,_collaboration_and_labor_division_in_the_large_language_model_era|Scientific exploration, collaboration and labor division in the large language model era]]

![[assets/2607.20923_figure.png|800]]

- **arXiv**: [2607.20923](https://arxiv.org/abs/2607.20923)
- **PDF**: https://arxiv.org/pdf/2607.20923
- **详细分析**: [[20_Research/Papers/大模型/Scientific_exploration,_collaboration_and_labor_division_in_the_large_language_model_era|Scientific exploration, collaboration and labor division in the large language model era]]
- **作者**: Xiang Zheng, Xi Hong, Jialin Liu, Chaoqun Ni
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《Scientific exploration, collaboration and labor division in the large language model era》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have rapidly and significantly entered scientific workflows, but it remains unclear how their diffusion is associated with changes in scientists' strategies in research directions and team building. We link PubMed Central full text with OpenAlex publication and collaboration histories for 775,323 scientists and analyze CRediT contribution statements from 137,120 multi-author papers. After 2022, scientists increasingly published across more intellectually distant fields and entered fields in which they had not previously worked. These increases in interdisciplinarity and exploration were especially pronounced among established scientists and scientists from non-English-speaking low- and middle-income countries. Authors with stronger AI-writing signals were already more interdisciplinary and exploratory before the widespread adoption of LLMs, and the gap widened further after 2022 compared with authors with weaker AI-writing signals. Scientists' collaboration networks also became more interdisciplinary after 2022. Yet, among authors with stronger AI-writing signals, research interdisciplinarity was less closely tied to the disciplinary diversity of their collaborators. The division of labor within research teams also became more differentiated. Contributors on papers published after 2022 reported narrower role sets on average, coauthors shared fewer roles in common, and their role profiles became less rigid and more fluid. Software and validation roles increased, while conceptual and management roles decreased. These patterns suggest that team members are taking on more distinct responsibilities and may rely less on one another to perform research tasks. Overall, this study indicates that the LLM era coincides with a broader reorganization of scientific exploration, collaboration, and the division of labor.

</details>

---

### [[20_Research/Papers/强化学习/Multi-turn_RL_with_Structural_and_Performance_Aware_Rewards_for_CUDA_Kernel_Generation|Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation]]

![[assets/2607.20908_figure.png|800]]

- **arXiv**: [2607.20908](https://arxiv.org/abs/2607.20908)
- **PDF**: https://arxiv.org/pdf/2607.20908
- **详细分析**: [[20_Research/Papers/强化学习/Multi-turn_RL_with_Structural_and_Performance_Aware_Rewards_for_CUDA_Kernel_Generation|Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation]]
- **作者**: Quazi Ishtiaque Mahmud, Nesreen K. Ahmed, Ali Jannesari
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CodeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful technique to enhance the reasoning capacity of LLMs for optimized code generation. However, existing RLVR approaches primarily rely on outcome-based signals such as correctness and speedup, overlooking performance-critical structural properties of programs that are essential for generating optimized code. In this work, we propose CudaPerf, a reflective RL framework that incorporates both verifiable execution rewards and structural code-aware rewards derived from parallelization features (e.g., memory coalescing, occupancy, Arithmatic Intensity, and synchronization patterns). CudaPerf operates in two stages: (1) an offline pairwise ranking module that learns to distinguish strong and weak program candidates via contrastive comparisons, and (2) an online RL training phase that jointly optimizes for correctness, performance, and structural efficiency through a unified reward signal. To further enhance learning, CudaPerf utilizes iterative refinement using execution feedback enabling progressive improvement of generated candidates. We also introduce a dataset comprising 2.9k C to CUDA and 1k PyTorch to CUDA programs, each paired with diverse input configurations and multiple CUDA implementations encompassing diverse optimization strategies. CudaPerf is evaluated across multiple benchmarks comprising both C to CUDA and PyTorch to CUDA transformations. Empirical findings suggest that CudaPerf significantly outperforms strong baselines, including Qwen-3-32B (for C to CUDA) and CUDA Agent (for PyTorch to CUDA) by achieving up to 5X &amp; 3.32X improvements in speedup, and 17% &amp; 7% improvements in correctness, respectively.

</details>

---

### [[20_Research/Papers/大模型/Auditing_Provenance_Sensitivity_in_LLM_Agent_Action_Selection|Auditing Provenance Sensitivity in LLM Agent Action Selection]]

![[assets/2607.20827_figure.png|800]]

- **arXiv**: [2607.20827](https://arxiv.org/abs/2607.20827)
- **PDF**: https://arxiv.org/pdf/2607.20827
- **详细分析**: [[20_Research/Papers/大模型/Auditing_Provenance_Sensitivity_in_LLM_Agent_Action_Selection|Auditing Provenance Sensitivity in LLM Agent Action Selection]]
- **作者**: Junchi Liao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Auditing Provenance Sensitivity in LLM Agent Action Selection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. Evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence. We introduce a target-specific authorization audit that labels context factors separately for each tool and argument target. Its primary test holds the task, proposition, position, and policy fixed while changing only the proposition's source authority. We then test behavior when valid evidence is weakened and use context-subset interactions as a secondary localization diagnostic. Across 450 controlled next-action tasks and multiple open-weight LLM families, trusted and untrusted variants produce different actions in 5.4 percent of competing cases versus 1.7 percent of supporting cases. Under controlled degradation, unauthorized competition is retained in a full-correct, mixed-error, clean-correct pattern in 2.4 percent of comparisons, with a 95 percent confidence interval from 2.1 to 3.0 percent. These are controlled stress-set rates, not deployment prevalence. The models respond to textual source-authority cues, but this does not prevent untrusted evidence from influencing their actions.

</details>

---

### [[20_Research/Papers/大模型/Enhancing_Explainable_Cardiac_Diagnosis_with_Guide-Grounded_Multimodal_LLMs|Enhancing Explainable Cardiac Diagnosis with Guide-Grounded Multimodal LLMs]]

![[assets/2607.20814_figure.png|800]]

- **arXiv**: [2607.20814](https://arxiv.org/abs/2607.20814)
- **PDF**: https://arxiv.org/pdf/2607.20814
- **详细分析**: [[20_Research/Papers/大模型/Enhancing_Explainable_Cardiac_Diagnosis_with_Guide-Grounded_Multimodal_LLMs|Enhancing Explainable Cardiac Diagnosis with Guide-Grounded Multimodal LLMs]]
- **作者**: Hai-Nam Duy Vuong, Duy-Anh Bui, Trong-Nghia Nguyen, Kim-Ngan Thi Nguyen, Trang Mai Xuan, Tien-Cuong Nguyen, Van-Dem Pham, Thien Van Luong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Enhancing Explainable Cardiac Diagnosis with Guide-Grounded Multimodal LLMs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The electrocardiogram (ECG) is a cornerstone of cardiac as- sessment, yet clinical deployment of deep learning models remains con- strained by limited interpretability and the hallucination risk of large language models (LLMs). Existing CNN+Grad-CAM+multimodal LLM frameworks can generate ECG reports, but their explanations are often only weakly grounded in established diagnostic criteria, reducing trust- worthiness and reproducibility. We propose a guide-grounded multimodal framework that explicitly anchors report generation in curated clinical knowledge. A convolutional neural network (CNN) and Grad-CAM first produce class probabilities and class-specific heatmaps from 12-lead ECG images. In parallel, authoritative ECG textbooks and guideline materials are distilled offline into a structured ECG Interpretation Guide, which is injected as a fixed knowledge block for every sample. Conditioned on the ECG image, Grad-CAM overlay, CNN-derived fact pack, and the in- jected guide, a multimodal LLM generates structured diagnostic reports with guideline-consistent terminology and criteria usage. Experiments on the full PTB-XL test set demonstrate that guide grounding improves se- mantic quality and perceived consistency of generated reports while pre- serving competitive classification performance. In particular, our method increases the average BERTScore of generated impressions from 0.818 to 0.953 relative to a strong CNN+Grad-CAM+MLLM baseline, indicat- ing closer alignment with reference reports. These findings suggest that injecting a distilled interpretation guide into the multimodal prompting pipeline offers a practical pathway to reduce hallucinations and enhance the clinical plausibility of LLM-based ECG explanations, bringing ex- plainable cardiac diagnosis closer to real-world deployment.

</details>

---

### [[20_Research/Papers/具身智能/Robostral_Navigate|Robostral Navigate]]

![[assets/2607.20785_figure.png|800]]

- **arXiv**: [2607.20785](https://arxiv.org/abs/2607.20785)
- **PDF**: https://arxiv.org/pdf/2607.20785
- **详细分析**: [[20_Research/Papers/具身智能/Robostral_Navigate|Robostral Navigate]]
- **作者**: Arjun Majumdar, Avinash Sooriyarachchi, Benjamin Tibi, Chris Bamford, Elliot Chane-Sane, Guillaume Lample, Khyathi Raghavi Chandu, Ludovic Ho Fuh, Mathieu Poiree, Olivier Duchenne, Rosalie Millner, Srijan Mishra...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 强化学习
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.2，强化学习 0.2，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Robostral Navigate》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying navigation systems at scale requires a recipe that minimizes sensor assumptions, generalizes across robot embodiments, and trains efficiently. Yet, today's best systems depend on depth sensors, multi-camera rigs, or pre-built maps, limiting the hardware they support and increasing deployment cost. We introduce Robostral Navigate, an 8B vision-language model built around this scalability objective. The model consumes only a stream of monocular RGB images - the most ubiquitous sensor across robotic platforms and predicts waypoints by pointing to the next target location in the current camera view. Operating purely in image space, rather than robot-specific coordinates, makes the policy naturally robust to changes in camera intrinsics and scene scale, enabling deployment across wheeled, legged, and aerial robots without recalibration. We generate 2.4 million trajectories across 350k simulated scenes to reduce the reliance on real-world data collection and scale easily. We further introduce a prefix-caching training recipe that packs entire episodes into single training sequences, reducing training tokens by 22x and cutting training time from months to days. A tree-based attention mask prevents conditioning on previous ground-truth actions, encouraging visually grounded action prediction, and reinforcement learning is used to further improve exploration and recovery capabilities. On the Room-to-Room and Room-Across-Room in Continuous Environments (R2R-CE and RxR-CE) benchmarks, Robostral Navigate sets a new state of the art. On R2R-CE, it achieves a 77.4% success rate, surpassing the best monocular method by 10.5 points and the strongest depth- or multi-camera system by 5.3 points despite using only a single RGB camera. On RxR-CE, it reaches 75.1% success rate, outperforming all monocular baselines.

</details>

---

### [[20_Research/Papers/具身智能/Emergent_Compositional_Skills_in_Mixture-of-Experts_VLAs|Emergent Compositional Skills in Mixture-of-Experts VLAs]]

![[assets/2607.20771_figure.png|800]]

- **arXiv**: [2607.20771](https://arxiv.org/abs/2607.20771)
- **PDF**: https://arxiv.org/pdf/2607.20771
- **详细分析**: [[20_Research/Papers/具身智能/Emergent_Compositional_Skills_in_Mixture-of-Experts_VLAs|Emergent Compositional Skills in Mixture-of-Experts VLAs]]
- **作者**: Shlok Shah, Rhiaan Jhaveri, Tharun Kumar Tiruppali Kalidoss, Chirayu Nimonkar, Ishaan Javali
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Emergent Compositional Skills in Mixture-of-Experts VLAs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SmolVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the problem of learning compositional robot policies end-to-end from expert demonstrations, without any pre-specified notion of task decomposition or hierarchy. We ask whether a VLA trained with a simplified Mixture-of-Experts (MoE) action head can emergently learn to decompose tasks into reusable, interpretable primitives. We find that learned experts are heavily reused across tasks and consistently correspond to qualitatively distinct low-level behaviors, suggesting that the router implicitly learns to perform high-level sequencing while experts serve as compositional primitives. Our MoE matches the task performance of a monolithic baseline while demonstrating meaningful expert specialization, a step toward modular, interpretable robot policies that emerge from data alone.

</details>

---

### [[20_Research/Papers/大模型/IssueTrojanBench_Benchmarking_AI_Coding_Agents_Against_Malicious_Issue_Requests|IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests]]

![[assets/2607.20759_figure.jpeg|800]]

- **arXiv**: [2607.20759](https://arxiv.org/abs/2607.20759)
- **PDF**: https://arxiv.org/pdf/2607.20759
- **详细分析**: [[20_Research/Papers/大模型/IssueTrojanBench_Benchmarking_AI_Coding_Agents_Against_Malicious_Issue_Requests|IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests]]
- **作者**: Ankur Singh, Jinqiu Yang, Tse-Hsun Chen
- **cs 子类**: cs.AI, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IssueTrojanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools. Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments. This paper presents a systematic evaluation of malicious issue requests against state-of-the-art coding agents (Cursor, Claude Code, and Codex Desktop), powered by two major model families (OpenAI GPT-5.3 Codex/GPT-5.4 and Anthropic Sonnet 4.6). Our novel benchmark IssueTrojanBench contains malicious issues that are constructed based on four novel attack categories (i.e., embedded as malicious instructions in issues), six delivery vectors (e.g., PDF, or issue comment), and further augmented by perturbations. Our results reveal critical vulnerabilities in the as-deployed modern coding agents, i.e., 66.5% of the malicious issues from IssueTrojanBench penetrate all the guardrails (agent- and LLM-level) of coding agents. Our further analysis shows that rejection is almost entirely from LLMs rather than the agent frameworks, with GPT models broadly vulnerable and Sonnet 4.6 exhibiting more selective, risk-aware blocking of high-impact actions. Our evaluation also highlights that the current agent-level defense strategy offers limited additional protection for coding agents. Our findings highlight the urgent need for stronger agent- and model-level safety mechanisms to protect AI coding agents.

</details>

---

### [[20_Research/Papers/机器人/Self-Supervised_Bio-Inspired_Robotic_Trajectory_Planning_with_Obstacle_Avoidance|Self-Supervised Bio-Inspired Robotic Trajectory Planning with Obstacle Avoidance]]

![[assets/2607.20743_figure.png|800]]

- **arXiv**: [2607.20743](https://arxiv.org/abs/2607.20743)
- **PDF**: https://arxiv.org/pdf/2607.20743
- **详细分析**: [[20_Research/Papers/机器人/Self-Supervised_Bio-Inspired_Robotic_Trajectory_Planning_with_Obstacle_Avoidance|Self-Supervised Bio-Inspired Robotic Trajectory Planning with Obstacle Avoidance]]
- **作者**: Miroslav Krupa, Miroslav Cibula, Kristína Malinovská
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Self-Supervised Bio-Inspired Robotic Trajectory Planning with Obstacle Avoidance》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trajectory planning is a fundamental problem in robotics, requiring the generation of collision-free and efficient trajectories in a potentially complex environment. While sampling-based planners remain the dominant approach, they are often computationally expensive, particularly in high-dimensional spaces and obstacle-rich environments. Methods based on model learning offer a promising alternative, enabling efficient planning through a bounded number of forward passes through a neural trajectory planner, but commonly suffer from low sample efficiency or limited generalisation due to their reliance on exploration or expert demonstrations. This follow-up work tests our neuro-inspired self-supervised learning framework for trajectory planning that leverages forward and inverse models as the internal supervisory mechanism in an environment that contains an obstacle. Experimental results demonstrate the feasibility of the approach while revealing a tendency of our planner to exploit the learning signal provided by the forward and inverse models. To address this issue, additional training regimes and mitigation strategies are proposed and evaluated.

</details>

---

### [[20_Research/Papers/大模型/NVIDIA-labs_OO_Agents_Native_Python_Object-Oriented_Agents|NVIDIA-labs OO Agents: Native Python Object-Oriented Agents]]

![[assets/2607.20709_figure.png|800]]

- **arXiv**: [2607.20709](https://arxiv.org/abs/2607.20709)
- **PDF**: https://arxiv.org/pdf/2607.20709
- **详细分析**: [[20_Research/Papers/大模型/NVIDIA-labs_OO_Agents_Native_Python_Object-Oriented_Agents|NVIDIA-labs OO Agents: Native Python Object-Oriented Agents]]
- **作者**: Paul Furgale, Severin Klingler, James Nolan, Matt Staats, Gaia Di Lorenzo, Elisa Martinez Abad, Christian Schüller, Razvan Dinu, Alessio Devoto, Pascal Berard, Gal Kaplun, Elad Sarafian...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《NVIDIA-labs OO Agents: Native Python Object-Oriented Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CyberGym, Read-Eval, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs. We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents. NOOA takes a simpler approach: an agent is a Python object. Its methods are the actions the model can take, fields are its state, docstrings are its prompts, and its type annotations are contracts. A method whose code body consists of "..." is completed at runtime by an LLM-driven agent loop, while methods with normal bodies remain standard deterministic Python. This gives developers and agents the same interface, so agent behavior can be tested, traced, refactored, and improved just like other software. This paper makes three contributions. (1) We present the agent-as-a-Python-object programming model and the design principles behind it. Where Python has existing abstractions, we adopt them directly. Agent-specific capabilities--context, events, state rendering, long-term memory, and validated LLM loops--are exposed through simple Pythonic APIs, so both developers and agents share one familiar programming model. (2) We identify six model-facing ideas that NOOA is, to our knowledge, the first to combine on a single surface: typed input/output, pass-by-reference over live objects, code as action, programmable loop engineering, explicit object state, and model-callable harness APIs for context and events. We find the community already converging on several of these ideas--often as experimental or partial features--and present the comparison to encourage further adoption. (3) We demonstrate that current models use this interface effectively, both in targeted capability tests and on agentic and reasoning benchmarks such as SWE-bench Verified and Terminal-Bench 2.0 and ARC-AGI-3.

</details>

---

### [[20_Research/Papers/强化学习/From_Agent_Failures_to_Text_Policies_What_Works_and_What_Breaks|From Agent Failures to Text Policies: What Works and What Breaks]]

![[assets/2607.20668_figure.png|800]]

- **arXiv**: [2607.20668](https://arxiv.org/abs/2607.20668)
- **PDF**: https://arxiv.org/pdf/2607.20668
- **详细分析**: [[20_Research/Papers/强化学习/From_Agent_Failures_to_Text_Policies_What_Works_and_What_Breaks|From Agent Failures to Text Policies: What Works and What Breaks]]
- **作者**: Jaideep Ray, Ankit Goyal
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《From Agent Failures to Text Policies: What Works and What Breaks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LangMARL, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

TextGrad improves language-model systems by revising text from feedback. Its core thesis is that natural-language feedback can act as a gradient for optimizing text components without changing model weights. Applying it to agents is harder because feedback arrives only after a sequence of actions, making it difficult to identify which decision caused failure. We study this problem by separating the ability to follow a useful policy from the ability to learn that policy from experience. Our main finding is a clear gap between these two abilities. Human-written policies improve two frozen 7B agents on TextWorldExpress by 5.0 success points, showing that useful policy text exists. However, policies generated from agent trajectories do not reliably outperform fixed prompting, even with richer traces, counterfactual evidence, or iterative GEPA search. The main challenge for agent-level TextGrad is therefore not executing textual policy updates, but reliably generating and selecting them from experience.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Multi-Horizon_Reinforcement_Learning|Adaptive Multi-Horizon Reinforcement Learning]]

![[assets/2607.20656_figure.png|800]]

- **arXiv**: [2607.20656](https://arxiv.org/abs/2607.20656)
- **PDF**: https://arxiv.org/pdf/2607.20656
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Multi-Horizon_Reinforcement_Learning|Adaptive Multi-Horizon Reinforcement Learning]]
- **作者**: Manoosh Samiei, Doina Precup, Paul Masset
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Adaptive Multi-Horizon Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective decision-making in complex and changing environments requires balancing short-term and long-term consequences. In reinforcement learning (RL), this trade-off is typically controlled through a fixed discount factor, which imposes a single exponentially discounted temporal horizon. However, biological agents exhibit flexible and adaptive temporal discounting, suggesting that effective planning requires multiple timescales. Here, we propose a multi-horizon approach that adaptively selects and combines temporal horizons, enabling robust adaptation to changes in reward structure without manual discount-factor tuning. This flexibility makes the method particularly suitable for continual learning scenarios involving task switches and varying environmental configurations. Empirically, we demonstrate that our approach identifies effective discount factors across a range of MiniGrid environments, including continual settings composed of three sequentially changing tasks. These results suggest that adaptive temporal discounting can improve parameter efficiency and enhance adaptability in both artificial and biologically inspired learning systems.

</details>

---

### [[20_Research/Papers/强化学习/SalesLoop_Reinforcement_Learning_from_Performance_Feedback_for_Sales_Lead_Ranking|SalesLoop: Reinforcement Learning from Performance Feedback for Sales Lead Ranking]]

![[assets/2607.20655_figure.png|800]]

- **arXiv**: [2607.20655](https://arxiv.org/abs/2607.20655)
- **PDF**: https://arxiv.org/pdf/2607.20655
- **详细分析**: [[20_Research/Papers/强化学习/SalesLoop_Reinforcement_Learning_from_Performance_Feedback_for_Sales_Lead_Ranking|SalesLoop: Reinforcement Learning from Performance Feedback for Sales Lead Ranking]]
- **作者**: Chenyu Zhang
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SalesLoop: Reinforcement Learning from Performance Feedback for Sales Lead Ranking》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ListNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lead ranking in Customer Relationship Management (CRM) systems faces a persistent challenge: models achieving high offline accuracy often underperform in production. We identify three fundamental gaps responsible for this disconnect: offline-online metric mismatch, pointwise-listwise objective misalignment, and temporal distribution drift. To address these gaps, we propose SalesLoop, a reinforcement learning framework that establishes a closed feedback loop between model predictions and real-world business outcomes. Our approach introduces (1) a performance-aware reward that encodes conversion outcomes weighted by ranking position and conversion velocity, and (2) Discriminative GRPO, a listwise optimization objective that adapts Group Relative Policy Optimization to discriminative ranking models. SalesLoop improves NDCG@K by +7.9\% and P@K by +15.8\% over the strongest static baseline. A 160-day production A/B test at a New Energy Vehicle manufacturer, spanning 16.5M leads and 280 sales specialists across two provincial markets, validates statistically significant cumulative lift of +4.7\% ($p=0.047$) and +8.7\% ($p=0.002$). In production, the ranking backbone achieves Top-10\% recall of 44.1\% and surfaces high-intent leads at $2.3\times$ the conversion rate of specialist baselines.

</details>

---

### [[20_Research/Papers/大模型/Frontier_Financial_Judgement_Can_agents_tell_what_might_move_a_stock|Frontier Financial Judgement: Can agents tell what might move a stock?]]

![[assets/2607.20645_first_page.png|800]]

- **arXiv**: [2607.20645](https://arxiv.org/abs/2607.20645)
- **PDF**: https://arxiv.org/pdf/2607.20645
- **详细分析**: [[20_Research/Papers/大模型/Frontier_Financial_Judgement_Can_agents_tell_what_might_move_a_stock|Frontier Financial Judgement: Can agents tell what might move a stock?]]
- **作者**: Joshua Harris
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Frontier Financial Judgement: Can agents tell what might move a stock?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Frontier Financial Judgement, a challenging new benchmark developed in collaboration with professional equity analysts to assess agents' ability to replicate expert human judgements. Rapidly identifying new information, evaluating its implications and determining its valuation impact is one of the most time-consuming and challenging aspects of real-world equity coverage. This is becoming ever more difficult and important as AI rapidly increases the quantity of new information to process. The strongest agent we evaluate on Frontier Financial Judgement matches all expert labels in only 52.4% of cases. We also find significant divergence in estimated false-positive rates among frontier agents, ranging from ~1% for GPT-5.6 Sol to ~32% for Claude Sonnet 4.6. To construct the benchmark and make it representative of real-world settings, we combine human-designed and labelled synthetic articles with live news articles and historical documents, creating 656 items for assessment. The resulting task requires agents to distinguish genuinely new, valuation-relevant financial information from stale, immaterial or misleading news under realistic conditions. We find substantial trade-offs among agent accuracy, cost, false positives and reliability that continue to hinder the reliable deployment of news-flow filtering in practice.

</details>

---

### [[20_Research/Papers/大模型/Demonstrating_GenDB_Instance-Optimized_and_Customized_Query_Processing_Code_Generation_via_LLM_Agents|Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents]]

![[assets/2607.20630_first_page.png|800]]

- **arXiv**: [2607.20630](https://arxiv.org/abs/2607.20630)
- **PDF**: https://arxiv.org/pdf/2607.20630
- **详细分析**: [[20_Research/Papers/大模型/Demonstrating_GenDB_Instance-Optimized_and_Customized_Query_Processing_Code_Generation_via_LLM_Agents|Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents]]
- **作者**: Jiale Lao, Immanuel Trummer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional query processing engines require continuous development and extensions to support new techniques and user requirements, and in some cases, entirely new systems must be built from scratch. However, these engines are difficult to extend due to their internal complexity, and building new systems demands significant engineering effort and cost. To address this, we demonstrate GenDB, a generative query engine that shifts query processing from manually engineered systems to query processing code generation driven by Large Language Models (LLMs). An early prototype of GenDB uses LLM agents to generate instance-optimized query execution code tailored to specific data, workloads, and hardware resources. This prototype suits offline code generation for repetitive, templated queries, since the upfront generation cost amortizes over many executions and correctness can be ensured through extensive fuzz testing and manual inspection. For ad-hoc queries, GenDB can work with a traditional DBMS in a hybrid architecture: the DBMS handles one-off queries, while GenDB speeds up frequent SQL templates. Our demonstration allows users to (1) visually and interactively explore how GenDB analyzes workloads, profiles hardware resources and underlying data, produces query plans, generates code based on them, and finally uses an optimizer to iteratively achieve a correct and efficient implementation; (2) use visual inspection and analysis to gain qualitative insights into why GenDB produces code that achieves significantly better performance than state-of-the-art query engines on two benchmarks: TPC-H and a newly constructed benchmark designed to reduce potential data leakage from LLM training data; and (3) upload their own data and queries to explore GenDB with different LLMs and query patterns.

</details>

---

### [[20_Research/Papers/大模型/Monkey_King_Bang_A_Unified_Scientific_Multimodal_Foundation_Model|Monkey King Bang: A Unified Scientific Multimodal Foundation Model]]

![[assets/2607.20557_figure.png|800]]

- **arXiv**: [2607.20557](https://arxiv.org/abs/2607.20557)
- **PDF**: https://arxiv.org/pdf/2607.20557
- **详细分析**: [[20_Research/Papers/大模型/Monkey_King_Bang_A_Unified_Scientific_Multimodal_Foundation_Model|Monkey King Bang: A Unified Scientific Multimodal Foundation Model]]
- **作者**: Hesen Chen, Xinyu Su, Xiaomeng Yang, Yuetan Lin, Zixiong Yang, Junyi An, Fenglei Cao, Yifeng Jiao, Yunqi Zhang, Yuan Cheng, Zhiyu Tan, Hao Li...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Monkey King Bang: A Unified Scientific Multimodal Foundation Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific discovery is increasingly shifting from isolated disciplines to multi-domain reasoning, and AI for science faces a similar transition. Existing systems are either specialised for individual domains or unify scientific data mainly through text tokenisation and prompt-based interfaces, limiting their ability to handle diverse scientific inputs, produce modality-native outputs, and support joint understanding, reasoning, and generation across scientific domains. We introduce MKB, a unified scientific multimodal model for both understanding and generation, built around a shared Transformer backbone and modality-tailored encoders, adapters, and decoders. MKB covers six scientific branches, including DNA, RNA, proteins, small molecules, earth science, and medical images, and supports native outputs such as biological sequences, molecular strings, meteorological fields, and segmentation masks. Training follows a two-stage modality-then-language curriculum: Stage 1 aligns modality-specific components with the frozen backbone, and Stage 2 consolidates them with the language backbone using mixed scientific and general corpora. Experiments show that MKB achieves competitive scientific understanding across biological and molecular benchmarks, produces high-fidelity native outputs for weather forecasting, biological generation, and medical-image segmentation, and largely retains the general capabilities of its Qwen3-VL backbone. These results demonstrate the feasibility of the proposed paradigm, suggesting that shared-backbone models with modality-tailored components can provide a promising foundation for future cross-domain scientific multimodal exploration. The model and code are publicly available at https://github.com/Shanghai-Academy-of-AI-For-Science/MKB and https://huggingface.co/sais-org/MKB.

</details>

---

### [[20_Research/Papers/大模型/CMI-Mem_Toward_Generalizable_Long-Term_Memory_Management_via_CMI-Augmented_Reinforcement_Learning|CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning]]

![[assets/2607.20553_figure.png|800]]

- **arXiv**: [2607.20553](https://arxiv.org/abs/2607.20553)
- **PDF**: https://arxiv.org/pdf/2607.20553
- **详细分析**: [[20_Research/Papers/大模型/CMI-Mem_Toward_Generalizable_Long-Term_Memory_Management_via_CMI-Augmented_Reinforcement_Learning|CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning]]
- **作者**: Yubo Wang, Qiuyu Zhao, Zenghui Sun, Shichao Dong, Jinsong Lan, Xiaoyong Zhu, Haoyang Li, Bo Zheng, Lei Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.15（加权：大模型 0.35，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Memory-QA, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory Manager models are pivotal in agent systems. Existing methods rely predominantly on LLM-judged synthetic question-answer (QA) pairs, making memory valuation dependent on sampled queries and the downstream reader. To address this limitation, we propose \textbf{CMI-Mem}, a reinforcement learning(RL)-based lightweight memory manager model with a hybrid reward that combines downstream QA correctness and intrinsic Conditional Mutual Information (CMI). CMI evaluates the information contributed by new conversational inputs relative to the current memory state without conditioning on a sampled QA query, thereby complementing rather than replacing QA grounding. Our codes are available at: https://github.com/Wyb0627/CMIMem , and the CMI-Mem-4B model checkpoint is available at: https://www.modelscope.cn/models/wyb0627/CMIMem-4B

</details>

---

### [[20_Research/Papers/大模型/Beyond_SBDD_Geometric_Deep_Learning_in_Polypharmacology_and_Multi-target_Drug_Design|Beyond SBDD: Geometric Deep Learning in Polypharmacology and Multi-target Drug Design]]

![[assets/2607.20550_first_page.png|800]]

- **arXiv**: [2607.20550](https://arxiv.org/abs/2607.20550)
- **PDF**: https://arxiv.org/pdf/2607.20550
- **详细分析**: [[20_Research/Papers/大模型/Beyond_SBDD_Geometric_Deep_Learning_in_Polypharmacology_and_Multi-target_Drug_Design|Beyond SBDD: Geometric Deep Learning in Polypharmacology and Multi-target Drug Design]]
- **作者**: Tianming Han, Zhijie Pan, Wenchi Ge, Qi Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Beyond SBDD: Geometric Deep Learning in Polypharmacology and Multi-target Drug Design》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The traditional "one drug, one target" paradigm of structure-based drug design (SBDD) frequently proves inadequate for treating multifactorial diseases such as cancer and neurodegenerative disorders, owing to compensatory signaling pathways and the emergence of drug resistance. While polypharmacology offers a synergistic therapeutic strategy, the rational design of ligands capable of simultaneously satisfying the geometric constraints imposed by multiple targets remains a major computational bottleneck. This review positions geometric deep learning (GDL) as a powerful integrative approach to overcome these limitations. We systematically survey GDL architectures ranging from invariant graph neural networks to SE(3)-equivariant diffusion models that harness non-Euclidean molecular data to capture intrinsic three-dimensional (3D) structural interdependencies. We critically analyze GDL applications across three core dimensions, including the characterization of shared binding pockets via geometric embeddings, multi-target bioactivity prediction through heterogeneous graph fusion, and de novo generation of dual-target ligands. Particular emphasis is placed on emerging structure-conditioned generative algorithms that integrate diffusion models with reinforcement learning to autonomously resolve complex geometric conflicts between competing binding sites. Furthermore, we evaluate the pivotal role of multimodal omics integration and specialized geometric benchmarking infrastructures in validating these models. By synthesizing these methodological advances, this review elucidates the paradigm shift in drug discovery from serendipitous exploration to rational, structure-driven polypharmacological molecular engineering, thereby providing a clear, structured guide for navigating the complexities of next-generation therapeutics.

</details>

---

### [[20_Research/Papers/强化学习/When_RLVR_Shrinks_the_Reasoning_Boundary_Diagnosing_Pass@k_Inversion|When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion]]

![[assets/2607.20543_first_page.png|800]]

- **arXiv**: [2607.20543](https://arxiv.org/abs/2607.20543)
- **PDF**: https://arxiv.org/pdf/2607.20543
- **详细分析**: [[20_Research/Papers/强化学习/When_RLVR_Shrinks_the_Reasoning_Boundary_Diagnosing_Pass@k_Inversion|When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion]]
- **作者**: Todd Zhou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) can improve one-sample accuracy while making a model worse under repeated sampling. We study this pass@k inversion: after training, the policy may solve fewer distinct problems than its base model at large $k$. The failure concentrates on boundary prompts, where the base model contains rare correct trajectories that are recoverable by sampling but too sparse to reliably appear in finite RLVR rollout groups. We argue that a two-mode account explains this as an absence-of-evidence failure: rare correct trajectories may disappear before RLVR samples and reinforces them often enough. The main contribution is this diagnostic and mechanistic framing. Per-Problem Base Anchoring (PBA) is a deliberately simple proof-of-concept: sharpen prompts with sufficient frozen-base correct evidence, and anchor risky prompts to the base distribution. Across three training seeds on Omni-MATH-Test, with MATH500 as a secondary high-coverage validation benchmark, PBA improves both \PassK{1} and high-budget coverage over matched GRPO. A 3000-prompt regime-controlled diagnostic study is consistent across seeds with the expected signature: ordinary GRPO loses base-solvable boundary prompts, while PBA preserves rare verifier-positive trajectories. We use mathematical verifiers as a controlled testbed for verifier-guided optimization; the same pass@k inversion risk applies to ECCV-relevant vision-language agents when repeated visual, spatial, or chart-reasoning attempts are checked by external tools or verifiers. Reasoning post-training should decide not only how strongly to optimize, but which prompts are safe to optimize.

</details>

---

### [[20_Research/Papers/大模型/AppWorld-UL_Benchmarking_Diverse_Agent-User_Interactions_for_Tool-Use|AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use]]

![[assets/2607.20536_figure.png|800]]

- **arXiv**: [2607.20536](https://arxiv.org/abs/2607.20536)
- **PDF**: https://arxiv.org/pdf/2607.20536
- **详细分析**: [[20_Research/Papers/大模型/AppWorld-UL_Benchmarking_Diverse_Agent-User_Interactions_for_Tool-Use|AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use]]
- **作者**: Junzhi Chen, Harsh Trivedi, Jane Pan, Michael JQ Zhang, Tejas Srinivasan, Niranjan Balasubramanian, Ashish Sabharwal
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AppWorld-UL: Benchmarking Diverse Agent-User Interactions for Tool-Use》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AppWorld, ColBench, UserBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-use agents that address day-to-day digital tasks such as ordering groceries must not only operate applications, but also interact with the user, e.g., to ask clarification questions, prompt for confirmation, and inform the user when the instruction is infeasible. However, current benchmarks for evaluating agent-user interactions do not capture the diversity of such interactions. Further, they operate in small environments with few, often non-state-changing, APIs. To address this gap, we introduce AppWorld-UL, a ``user-in-the-loop'' benchmark of 516 challenging tasks requiring diverse agent-user interactions. Building upon the AppWorld framework with 9 popular simulated apps like Amazon and Spotify, we systematically modify original tasks to introduce ambiguities and constraints that necessitate various types of agent-user interaction. User behavior is simulated by an LLM prompted to respond with carefully designed knowledge boundaries, offering more reliable simulation than the unconstrained or overly rigid alternatives used in prior work. Our evaluation reveals that a state-of-the-art LLM, Claude Opus 4.7, achieves only 48.6% success on AppWorld-UL, and only 35.7% on the harder, compositional subset. On the stricter, scenario-level metric, compositional task performance drops to only 21.3%. Our analysis reveals that correct user-interaction is crucial for success. This demonstrates the benchmark's difficulty and its potential to advance research on user-in-the-loop tool-use agents.

</details>

---

### [[20_Research/Papers/大模型/DynamicMCPBench_A_Trace-Grounded,_Effect-Scored_Benchmark_for_LLM_Agents_over_Live_MCP_Servers|DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers]]

![[assets/2607.20531_figure.png|800]]

- **arXiv**: [2607.20531](https://arxiv.org/abs/2607.20531)
- **PDF**: https://arxiv.org/pdf/2607.20531
- **详细分析**: [[20_Research/Papers/大模型/DynamicMCPBench_A_Trace-Grounded,_Effect-Scored_Benchmark_for_LLM_Agents_over_Live_MCP_Servers|DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers]]
- **作者**: Jerzy Kamiński, Ilya Galyukshev, Artem Kuznetsov, Sergey Chuprin, Kirill Redko, Aidar Shumbalov, Anna Kalyuzhnaya
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《DynamicMCPBench: A Trace-Grounded, Effect-Scored Benchmark for LLM Agents over Live MCP Servers》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DynamicMCPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly deployed over Model Context Protocol (MCP) servers, yet the benchmarks used to evaluate them score the final answer or a fixed "ground-truth" list of tools, both of which are fragile once the underlying data is live and stateful. We present DynamicMCPBench, a reusable framework rather than a fixed dataset. A practitioner can run it on their own MCP servers to test models on their own tasks, or let it collect servers automatically to measure a model's general ability to solve agentic tasks. Given the servers and any set of models, it generates realistic goals, pursues each one live to record a successful trajectory, distills that trajectory into path-agnostic effect checkpoints, and scores an agent on whether it reproduces those effects, never on the final answer. To show what the framework reveals, we run it at scale: 24 models over 121 servers and 750 tasks spread evenly over 15 task categories (50 each), where each category targets a distinct tool-use challenge of the generated questions. Each task is scored by pass^3: it counts as solved only if all three independent attempts succeed. Even the strongest agents solve only about half of the tasks, 31% of tasks are solved by no model at all, and accuracy collapses as the required tool chain grows longer (from 39% on the shortest chains to 13% on the longest). A human validation study confirms the automatic scoring is reliable (chance-corrected agreement of 0.76). DynamicMCPBench thus turns benchmark construction into something practitioners can rerun on their own servers and models, while exposing a consistent inability of current agents to handle long, multi-step agentic tasks.

</details>

---

### [[20_Research/Papers/大模型/Uncertainty-Aware_Trust_Estimation_for_Multi-LLM_Systems_via_Structured_Expert_Judgement|Uncertainty-Aware Trust Estimation for Multi-LLM Systems via Structured Expert Judgement]]

![[assets/2607.20529_figure.png|800]]

- **arXiv**: [2607.20529](https://arxiv.org/abs/2607.20529)
- **PDF**: https://arxiv.org/pdf/2607.20529
- **详细分析**: [[20_Research/Papers/大模型/Uncertainty-Aware_Trust_Estimation_for_Multi-LLM_Systems_via_Structured_Expert_Judgement|Uncertainty-Aware Trust Estimation for Multi-LLM Systems via Structured Expert Judgement]]
- **作者**: Jiawei Zheng, Jiazhen Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《Uncertainty-Aware Trust Estimation for Multi-LLM Systems via Structured Expert Judgement》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) ensembles are increasingly used to improve reliability by combining predictions from multiple LLMs. However, existing aggregation methods typically assume that all models are equally trustworthy, overlooking differences in uncertainty quality. This assumption is poorly suited to heterogeneous LLMs, whose reliability and capability vary significantly, making naive aggregation vulnerable to unreliable or adversarial experts. In this work, we formulate multi-LLM aggregation as a problem of uncertainty-aware trust estimation. We adapt structured expert judgment from decision theory, using context-aware calibration questions to estimate expert reliability based on the quality of its probabilistic predictions. Specifically, we employ Cooke-style log weighting, which penalises overconfident incorrect predictions and favours well-calibrated experts. We evaluate our approach on MMLU and MMLU-Pro across homogeneous, heterogeneous, and contaminated expert panels. Results show that while aggregation methods perform similarly in homogeneous settings, Cooke weighting becomes critical under heterogeneity and contamination. It achieves a superior accuracy-reliability balance and remains robust when unreliable experts are introduced. These findings suggest that Multi-LLM aggregation requires not just combining predictions, but calibrating trust under uncertainty.

</details>

---

### [[20_Research/Papers/大模型/PromptPack_Scaling_LLM_Annotation_Agents_for_Online_Recommendation|PromptPack: Scaling LLM Annotation Agents for Online Recommendation]]

![[assets/2607.20528_figure.png|800]]

- **arXiv**: [2607.20528](https://arxiv.org/abs/2607.20528)
- **PDF**: https://arxiv.org/pdf/2607.20528
- **详细分析**: [[20_Research/Papers/大模型/PromptPack_Scaling_LLM_Annotation_Agents_for_Online_Recommendation|PromptPack: Scaling LLM Annotation Agents for Online Recommendation]]
- **作者**: Sebastian Koralewski, Merwan Barlier, Yulia Stolin, Blaž Škrlj
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《PromptPack: Scaling LLM Annotation Agents for Online Recommendation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online recommendation platforms increasingly use Large Language Models (LLMs) to extract structured features from ad creatives. While deploying a single-call LLM annotation agent yields significant Click-Through Rate (CTR) improvements in our live production environment, per-creative prompting is prohibitively expensive to scale. The redundant system instructions sent in every request account for 94% of billed input tokens. To break this cost bottleneck, we introduce PromptPack, a scalable, high-throughput LLM annotation agent. PromptPack achieves this scale via in-context batching, combining a shared system prompt, a strict XML structural envelope, and an output correction layer to ensure deterministic, pipeline-ready feature extraction across multiple creatives simultaneously. We evaluate PromptPack via an offline retrieval benchmark using a downstream logistic-regression ranker. To deeply profile the agent's behavior, we measure AUC and introduce Volume-Weighted Absolute Lift (VWAL), a novel metric capturing the signal quality of the generated features. Compared to our live, unbatched production baseline, PromptPack at batch size 20 cuts our LLM costs by 89% and accelerates throughput by 2.5x while fully preserving AUC.

</details>

---

### [[20_Research/Papers/大模型/Reliability-Aware_LLM_Alignment_from_Inconsistent_Human_Feedback|Reliability-Aware LLM Alignment from Inconsistent Human Feedback]]

![[assets/2607.20515_figure.jpg|800]]

- **arXiv**: [2607.20515](https://arxiv.org/abs/2607.20515)
- **PDF**: https://arxiv.org/pdf/2607.20515
- **详细分析**: [[20_Research/Papers/大模型/Reliability-Aware_LLM_Alignment_from_Inconsistent_Human_Feedback|Reliability-Aware LLM Alignment from Inconsistent Human Feedback]]
- **作者**: Jingyi Huang, Ruohan Zong, Yujun Feng, Liran Ma, Lanyu Shang, Yang Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reliability-Aware LLM Alignment from Inconsistent Human Feedback》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning from Human Feedback (RLHF) is critical for aligning Large Language Models (LLMs) with human preferences. However, its efficacy is often compromised by the inherent inconsistency and subjectivity of human annotations. Existing preference optimization frameworks, such as Direct Preference Optimization (DPO), typically treat ambiguous pairs with high annotator disagreement identically to those with unanimous consensus, forcing models to overfit to inconsistent supervision signals and leading to suboptimal alignment. In this work, we propose Reliability-Guided Preference Optimization (RGPO), a robust framework designed to mitigate the impact of inconsistent human feedback. RGPO estimates annotator reliability and infers latent ground truth labels from noisy human feedback to identify robust preferences. Furthermore, we introduce a reliability-aware consistency optimization that dynamically modulates the training objective based on the consensus level of annotations, ensuring the model prioritizes high-consensus supervision signals. Extensive experiments on LLM alignment benchmarks demonstrate that RGPO effectively reduces inconsistency and noise in training data and achieves superior performance compared to widely adopted RLHF baselines. Our code and configurations are available at https://github.com/GenieHuang/RGPO.

</details>

---

### [[20_Research/Papers/大模型/SiGMA_Sign-Guided_Merging_and_Adaptation_for_Multimodal_Continual_Instruction_Tuning|SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning]]

![[assets/2607.20511_figure.jpg|800]]

- **arXiv**: [2607.20511](https://arxiv.org/abs/2607.20511)
- **PDF**: https://arxiv.org/pdf/2607.20511
- **详细分析**: [[20_Research/Papers/大模型/SiGMA_Sign-Guided_Merging_and_Adaptation_for_Multimodal_Continual_Instruction_Tuning|SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning]]
- **作者**: Keonhee Park, Gunhee Kim
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal

#### 研究背景与动机

《SiGMA: Sign-Guided Merging and Adaptation for Multimodal Continual Instruction Tuning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ArxivQA, ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Continual Instruction Tuning (MCIT) is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving a sequence of downstream tasks. Prior methods mostly utilize Mixture of Experts or expansion merge approach, primarily focusing on catastrophic forgetting, yet they still suffer from negative interference during inference, where newly learned updates overwrite useful prior knowledge and degrade overall performance. To address this, we propose SiGMA (Sign Guided Merging and Adaptation), a simple yet effective framework that mitigates negative interference with two components: sign guided adaptive tuning during training and sign guided merging at inference. Sign guided adaptive tuning reduces collisions with past knowledge and learns the current task with minimal drift, mitigating severe forgetting. Sign guided merging further improves consolidation by selectively scaling salient parameters to preserve and amplify useful task specific knowledge. Experiments on UCIT and DCL benchmarks show that SiGMA significantly reduces negative interference and outperforms state of the art MCIT methods. Our code is available at SiGMA.

</details>

---

### [[20_Research/Papers/大模型/Telco-GAIA_Bilingual_Benchmark_for_Agents_in_Telecom_Domain|Telco-GAIA: Bilingual Benchmark for Agents in Telecom Domain]]

![[assets/2607.20510_figure.png|800]]

- **arXiv**: [2607.20510](https://arxiv.org/abs/2607.20510)
- **PDF**: https://arxiv.org/pdf/2607.20510
- **详细分析**: [[20_Research/Papers/大模型/Telco-GAIA_Bilingual_Benchmark_for_Agents_in_Telecom_Domain|Telco-GAIA: Bilingual Benchmark for Agents in Telecom Domain]]
- **作者**: Dmitrii Khizbullin, Zaid Alyafeai, Abdelrahman Eldesokey, Nourah AlSultan, Raghad Alshalan, David R. Pugh, Bernard Ghanem
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Telco-GAIA: Bilingual Benchmark for Agents in Telecom Domain》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, FinanceBench, MMLongBench, TelAgentBench, WixQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Telco-GAIA, a bilingual, multi-modal benchmark for evaluating tool-using agents on the data of a real-world telecommunications operator. Telco-GAIA comprises 100 human-verified question-answering tasks, in English and Arabic, that each demand multi-hop reasoning (4.2 hops on average) over three heterogeneous sources: a static website snapshot (HTML, images, and linked PDFs), a synthetic relational SQL database, and external web archives, spanning text, image, and tabular modalities. The benchmark is delivered as a sandboxed Docker environment and scored by normalized exact string matching, making evaluation objective, deterministic, and reproducible over time without any LLM-as-a-Judge. Evaluating a purpose-built reference agent across twelve commercial and open LLMs, we find Telco-GAIA challenging: even the strongest model solves only 71% of tasks; under a moderate cost budget, this falls to about 40%, and the visually grounded categories remain the weakest, where the average backend scores below 30%, leaving substantial headroom in document and image understanding. Telco-GAIA offers a rigorous, reproducible testbed for enterprise agents and a template for constructing closed-domain benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Autonomous_Topology_Mutation_Safe_Runtime_Restructuring_for_Multi-Agent_LLM_Systems_with_Capability,_State,_and_Shadow_Invariants|Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants]]

![[assets/2607.20488_first_page.png|800]]

- **arXiv**: [2607.20488](https://arxiv.org/abs/2607.20488)
- **PDF**: https://arxiv.org/pdf/2607.20488
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_Topology_Mutation_Safe_Runtime_Restructuring_for_Multi-Agent_LLM_Systems_with_Capability,_State,_and_Shadow_Invariants|Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants]]
- **作者**: Bronislav Sidik, Chaya Levi, Nizzan Kimhi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM frameworks typically fix their team topology at boot time. When an individual agent becomes overloaded at runtime, for example by mixing too many action categories, accumulating tool errors, or queueing behind too many calls, the system has no mechanism to restructure itself. We introduce Autonomous Topology Mutation (ATM), a runtime team-mutation mechanism for multi-agent LLM frameworks. ATM combines telemetry-driven overload detection with three safety invariants that gate each structural change: capability monotonicity, state-routing completeness, and shadow-before-live validation. ATM monitors a six-signal Bottleneck Index that includes queue depth, context thrash, tool-error rate, role entropy, retry-loop rate, and cross-agent wait time. When a warmup-calibrated threshold is breached for multiple consecutive ticks, ATM factorises the overloaded agent into specialised sub-agents and hot-swaps the parent into a coordinator role while preserving its external identity. State transfer is controlled by privacy-level-aware routing: each memory atom is routed only to a permitted child set, or explicitly dropped with a logged reason. No candidate topology receives live traffic until it has passed a shadow validation window. On 720 DeepSeek-V3-driven task runs with deterministic tool stubs across four ablation conditions and three workloads, the ATM factoriser split lifts code-task success from 3.3% to 61.7%. The full rail-and-distillation system reduces detected high-privacy memory exposure under a regex classifier from 2.0 to 0.0 events per task while preserving task quality. The runtime rails carrying ATM's invariants add less than 500 microseconds of p99 latency on the agent hot path. A small live-tool probe with real Python execution is included as an external-validity check. The implementation, benchmark harness, and traces are open-sourced.

</details>

---

### [[20_Research/Papers/具身智能/PersonaTrail_Benchmarking_Personalized_Web_Agents_through_Browsing_Trails|PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails]]

![[assets/2607.20482_first_page.png|800]]

- **arXiv**: [2607.20482](https://arxiv.org/abs/2607.20482)
- **PDF**: https://arxiv.org/pdf/2607.20482
- **详细分析**: [[20_Research/Papers/具身智能/PersonaTrail_Benchmarking_Personalized_Web_Agents_through_Browsing_Trails|PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails]]
- **作者**: Seungbin Yang, Chaewoon Ki, Dohyun Lee, Jaegul Choo, ChaeHun Park
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large language models have enabled web agents to autonomously execute complex tasks. In practice, users frequently provide underspecified instructions, requiring agents to infer the missing context from their raw browsing histories. Existing benchmarks fail to capture this form of personalization, as they either restrict tasks to fully explicit prompts or abstract web interaction history into simplified forms. To bridge this gap, we introduce PersonaTrail, a benchmark for personalized web agents operating in a managed open web environment. By leveraging realistic browsing trajectories as user history, PersonaTrail evaluates an agent's ability to infer user preferences and recall information from past browsing sessions. We further propose Preference-Aware Contextual Memory (PACMem), a framework that decomposes raw browsing histories into two types of structured memory: factual memories that summarize individual sessions and preference memories that distill recurring behavioral patterns. At inference time, the agent retrieves the most relevant entries from these memories to guide personalized navigation. Extensive experiments show that PACMem consistently outperforms existing memory-based baselines on both tasks.

</details>

---

### [[20_Research/Papers/大模型/InferenceBench_A_Benchmark_for_Open-Ended_LLM_Inference_Optimization_by_AI_Agents|InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents]]

![[assets/2607.20468_figure.png|800]]

- **arXiv**: [2607.20468](https://arxiv.org/abs/2607.20468)
- **PDF**: https://arxiv.org/pdf/2607.20468
- **详细分析**: [[20_Research/Papers/大模型/InferenceBench_A_Benchmark_for_Open-Ended_LLM_Inference_Optimization_by_AI_Agents|InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents]]
- **作者**: Jehyeok Yeon, Ben Rank, Maksym Andriushchenko
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ISO-Bench, InferenceBench, KernelBench, LongBench, PostTrainBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are increasingly used to automate research and development tasks, yet existing benchmarks typically evaluate them on prescribed workflows or narrow action spaces. Even nominally open-ended tasks can often be solved by retrieving a well-known recipe and tuning a few hyperparameters, making it unclear whether strong results reflect genuine optimization or memorized solutions. We introduce InferenceBench, where an agent must deploy an OpenAI-compatible inference server and optimize the speed of LLM inference. Each agent receives a target LLM, one H100 GPU, an optimization scenario, and a wall-clock time budget of two hours. Three optimization scenarios isolate distinct bottlenecks of inference (prefill latency, decode latency, and concurrent request throughput) and a fourth balances all three at the same time. Across 15 frontier agent configurations, agents reliably improve over a naive PyTorch baseline (up to $8.08\times$) and often match or exceed serving engines with default settings ($4.05\times$ for vLLM), but still fall below a simple hyperparameter search under the same time budget (up to $11.53\times$). Qualitative analysis of agent trajectories shows that although agents enumerate many relevant optimization techniques, they overwhelmingly converge on a single inference framework. They test only a few distinct configurations and spend the remaining budget re-measuring, repairing, or optimizing hyperparameters rather than exploring substantially different strategies. This suggests the bottleneck is not domain knowledge, but the ability to propose diverse configurations, evaluate them systematically, and submit the best identified solution. Overall, InferenceBench reflects the ability of agents to operate in an open-ended AI engineering setting, where memorized solutions lead to limited improvements.

</details>

---

### [[20_Research/Papers/大模型/CAMeR_Keyword-Gated_Hybrid_Activation_for_Adaptive_Memory_Retention_in_LLM_Agents|CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents]]

![[assets/2607.20458_figure.png|800]]

- **arXiv**: [2607.20458](https://arxiv.org/abs/2607.20458)
- **PDF**: https://arxiv.org/pdf/2607.20458
- **详细分析**: [[20_Research/Papers/大模型/CAMeR_Keyword-Gated_Hybrid_Activation_for_Adaptive_Memory_Retention_in_LLM_Agents|CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents]]
- **作者**: Haowen Lai
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CAMeR-Bench, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents operating over extended dialogues accumulate vast amounts of information, yet existing memory systems either retain everything indiscriminately or apply uniform forgetting heuristics that fail to distinguish relevant from irrelevant knowledge. We present CAMeR (Context-Activated Memory Reinforcement), a memory retention framework combining keyword-gated hybrid activation -- a joint symbolic (word-level Jaccard) and sub-symbolic (embedding cosine) gating mechanism -- with adaptive weight dynamics. CAMeR computes a hybrid similarity score for each memory-query pair; memories exceeding a threshold receive reinforcement while all memories undergo controlled decay. We introduce CAMeR-Bench, a 76-memory, 100-round benchmark spanning 8 topic clusters with graded activation frequency, designed to test adaptive retention where existing benchmarks (LoCoMO, LongMemEval) cannot. On CAMeR-Bench, CAMeR's keyword gate achieves a 1.6$\times$ larger retention gap between high-frequency and never-referenced memories compared to embedding-only gating (scissors gap: 0.039 vs. 0.024), while time-driven baselines (Oblivion, SuperLocalMemory) collapse to near-zero weights over 100 rounds. CAMeR's top-5 retrieval saves 83.2\% tokens versus full-context approaches (39k vs. 231k cumulative) while producing weight signals that improve retrieval precision. Through 8 ablation conditions we establish that the keyword gate -- not learnable decay -- is the primary performance driver at this scale. Our findings demonstrate that hybrid symbolic-neural gating provides a simple yet effective mechanism for adaptive memory retention in LLM agents.

</details>

---

### [[20_Research/Papers/大模型/LLM-INSTRUCT_at_UZH_Shared_Task_2026_Constraint-Aware_Retrieval_and_Selective_Debate_for_Paragraph-Level_Argument_Mining|LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining]]

![[assets/2607.20430_first_page.png|800]]

- **arXiv**: [2607.20430](https://arxiv.org/abs/2607.20430)
- **PDF**: https://arxiv.org/pdf/2607.20430
- **详细分析**: [[20_Research/Papers/大模型/LLM-INSTRUCT_at_UZH_Shared_Task_2026_Constraint-Aware_Retrieval_and_Selective_Debate_for_Paragraph-Level_Argument_Mining|LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining]]
- **作者**: Phuong Huu Vu Tran, Long Minh Vo, Son Nguyen Minh Le, Hoang Van
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present LLM-INSTRUCT, the winning system for the UZH Shared Task at ArgMining 2026 on paragraph-level argument mining in UN and UNESCO resolutions. The task requires paragraph-type classification, prediction of a subset of 141 official tags, and directed relation prediction under a strict JSON schema setting using only open-weight models up to 8B parameters. We frame the task as constrained structured prediction. The system first narrows the candidate tag space with metadata-aware dense retrieval, then applies constrained decoding with per-dimension caps, escalates only uncertain cases to a three-agent debate branch, and finally validates the output schema. On the official leaderboard, LLM-INSTRUCT ranked 1st overall, with 1st in F1 and 5th in LLM-as-a-Judge. During development, our configuration search further improved Task 1b Micro-F1 from 35.83% to 40.08% while keeping the internal Task 2 score at 4.421. The main lesson is simple: reducing the decision space before generation improves both accuracy and submission robustness. Our code and supporting scripts are publicly available at: https://github.com/LLM-Instruct-at-UZH-Shared-Task-2026/Method

</details>

---
