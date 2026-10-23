# cs.AI | Artificial Intelligence | 2026-10-21

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/具身智能/UniWALM_Unified_World_Action_Language_Model_for_Embodied_Robot_Control|UniWALM: Unified World Action Language Model for Embodied Robot Control]]

![[assets/2610.28626_figure.png|800]]

- **arXiv**: [2610.28626](https://arxiv.org/abs/2610.28626)
- **PDF**: https://arxiv.org/pdf/2610.28626
- **详细分析**: [[20_Research/Papers/具身智能/UniWALM_Unified_World_Action_Language_Model_for_Embodied_Robot_Control|UniWALM: Unified World Action Language Model for Embodied Robot Control]]
- **作者**: Rahul Sajnani, Diego Romeres, Mingyuan Zhang, Kai Gao, Carl Qi, Baichuan Huang, Srinath Sridhar, Dylan Randle, Lillian J. Ratliff, Jose Barreiros, Manikantan Nambi, Jeroen Vanbaar
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.2，大模型 0.6，机器人 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《UniWALM: Unified World Action Language Model for Embodied Robot Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior? Unlike prior approaches that attach a reasoning or vision-language model to a video-action backbone and run them as distinct stages, UniWALM unifies all three modalities inside a single mixture-of-transformers backbone whose per-modality diffusion heads co-denoise synchronously, decoding subtask and textual memory in the same pass as action with no separate planning stage; the generated language is re-consumed on the next step, closing a language-as-memory loop without an external planner or memory bank. To keep the action stream reliable under this richer objective, we further introduce Flow Matching with Correction (FMC), a training objective that teaches recovery from perturbed action trajectories at no inference-time cost. UniWALM consistently improves over same-backbone baselines (e.g., FastWAM) on compositional pick-and-place (MolmoSpaces) and across the memory-dependent subset of RMBench, where it reaches 34.5% without any pretrained language or reasoning model and exceeds Mem-0's keyframe-equipped setup (28.5%) using only a single anchor frame. On a real-world Find-the-Item task, generating textual memory lifts success from 11.1% to 61.1%, while state-of-the-art VLAs stay at or below chance (&lt;=33.3%).

</details>

---

### [[20_Research/Papers/机器人/Industrial_ReMEmbR_Scaling_Spatiotemporal_Memory_to_Robot_Fleets|Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets]]

![[assets/2610.28624_figure.png|800]]

- **arXiv**: [2610.28624](https://arxiv.org/abs/2610.28624)
- **PDF**: https://arxiv.org/pdf/2610.28624
- **详细分析**: [[20_Research/Papers/机器人/Industrial_ReMEmbR_Scaling_Spatiotemporal_Memory_to_Robot_Fleets|Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets]]
- **作者**: Jad Yammine, Malek Wahidi, Abrar Anwar, Yan Chang, Mihir Acharya, Anthony Rizk
- **cs 子类**: cs.AI, cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NaVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions only on demand. On each robot, an NVIDIA Jetson encodes video clips into retrieval embeddings with Cosmos-Embed1, vision tokens with Cosmos3-Edge, and reconstruction latents with the Wan2.2 VAE, without uploading raw camera frames. The encoding models are re-used to detect people in image patches, zeroing them out to support PII abstraction for GDPR-compliant deployments. We split Cosmos3-Edge at its vision-language boundary, placing the vision encoder on the robot and the language decoder on an on-premises server. A Nemotron agent retrieves memories by content, position, and time and queries the decoder using cached vision tokens. This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.

</details>

---

### [[20_Research/Papers/强化学习/SceneRig_An_Agentic_System_for_Simulation-Ready_3D_Scene_Reconstruction_from_Single_Images|SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images]]

![[assets/2610.28585_figure.png|800]]

- **arXiv**: [2610.28585](https://arxiv.org/abs/2610.28585)
- **PDF**: https://arxiv.org/pdf/2610.28585
- **详细分析**: [[20_Research/Papers/强化学习/SceneRig_An_Agentic_System_for_Simulation-Ready_3D_Scene_Reconstruction_from_Single_Images|SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images]]
- **作者**: Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BlenderGym, IR3D-Bench, Re3Sim, Real-to-Sim, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system that turns a single image into an editable, simulation-ready scene. SceneRig combines geometric, visual, and physical tools to reconstruct a faithful 3D scene. An agent then performs edit-and-validate loops inside a physics simulator to achieve physical stability. Across diverse inputs, SceneRig improves instance segmentation, object-centric appearance, and 3D placement while keeping the reconstructed scenes physically stable. Furthermore, SceneRig is effective for downstream robotics: its scenes predict real-robot policy outcomes more accurately than the baseline method and more reliably support replay of recorded manipulations without trajectory adaptation.

</details>

---

### [[20_Research/Papers/机器人/VLM-Guided_Contact_Retargeting_and_Generative_Partner_Modeling_for_Humanoid-Human_Interaction|VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction]]

![[assets/2610.28523_figure.png|800]]

- **arXiv**: [2610.28523](https://arxiv.org/abs/2610.28523)
- **PDF**: https://arxiv.org/pdf/2610.28523
- **详细分析**: [[20_Research/Papers/机器人/VLM-Guided_Contact_Retargeting_and_Generative_Partner_Modeling_for_Humanoid-Human_Interaction|VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction]]
- **作者**: Yuto Shibata, Kotaro Amaya, Kashu Yamazaki, Lalit Jayanti, Yoshimitsu Aoki, Mariko Isogawa, Katerina Fragkiadaki
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MAGNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid-human interaction requires robots to operate under severe partial observability: during close physical contact, the human partner is occluded, truncated, or outside the robot's field of view, causing pose estimation to fail and often necessitating external tracking or privileged human state. At the same time, heavy mutual occlusions introduce errors into the human-human motion-capture data used for learning. We present REACT, a framework for learning deployable humanoid-human interaction policies from human-human demonstrations. REACT treats semantic contact structure as the key supervisory signal connecting demonstration processing, interaction learning, and onboard control. First, a VLM-guided contact modeling and retargeting pipeline identifies semantically meaningful contacts and transfers them onto humanoid-human geometry while preserving interaction structure. Using these annotations, privileged interaction policies learn physically grounded behaviors through interaction-aware contact rewards and are then distilled into deployable egocentric depth policies trained entirely from onboard sensing using photorealistic human depth rendering. To address severe partial observability, we introduce generative partner-state modeling objectives that predict partner motion from occluded egocentric views. We evaluate REACT in simulation and on a real Unitree G1 humanoid across five contact-rich interactions. Semantic contact modeling substantially improves preservation of demonstrated interactions, while generative partner-state modeling improves contact recall on four of five interactions, most under heavy occlusion. On real hardware, REACT performs all five interactions using onboard sensing alone.

</details>

---

### [[20_Research/Papers/世界模型/Exploring_Temporal_Context-Aware_Physical_Grounding_in_Latent_World_Models|Exploring Temporal Context-Aware Physical Grounding in Latent World Models]]

![[assets/2610.28483_figure.png|800]]

- **arXiv**: [2610.28483](https://arxiv.org/abs/2610.28483)
- **PDF**: https://arxiv.org/pdf/2610.28483
- **详细分析**: [[20_Research/Papers/世界模型/Exploring_Temporal_Context-Aware_Physical_Grounding_in_Latent_World_Models|Exploring Temporal Context-Aware Physical Grounding in Latent World Models]]
- **作者**: Yilei Man, Yang Chen, Jingcai Guo
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.2（加权：世界模型 1.2）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Exploring Temporal Context-Aware Physical Grounding in Latent World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DeltaNet, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning latent dynamics is fundamental to building action-conditioned world models for planning. Among existing families, Joint Embedding Predictive Architectures (JEPAs) offer a natural framework by modeling transitions directly in latent space rather than at the pixel level. However, two issues remain in JEPA-based world models: (i) physical grounding lacks explicit aggregation of temporal context and (ii) action planning always overly relies on generic sampling distributions. To this end, we propose $\mathcal{G}$-JEPA, which incorporates temporal context into physical grounding for latent world models and couples the learned models with prior-guided action planning. Specifically, during learning, we incorporate a shared causal temporal module that aggregates temporal context within observation and prediction sequences under physical state supervision, grounding both in task-relevant physical states. When planning, we further introduce action inference through stepwise conditioning of a generative action distribution on the current and goal latent representations together with their evolving discrepancy, yielding anchored proposals that guide model-based online refinement. Together, physical state supervision guides temporal representation learning, while the action prior guides search through the learned world model. Experiments demonstrate improved planning performance on manipulation tasks, including tasks with increasing temporal separation between initial and goal observations. Code is publicly available at https://github.com/myl11045/G-JEPA.

</details>

---

### [[20_Research/Papers/具身智能/Plausible_Future,_Wrong_Choice_Steering_World-Action_Models_toward_Intended_Future|Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future]]

![[assets/2610.28431_figure.png|800]]

- **arXiv**: [2610.28431](https://arxiv.org/abs/2610.28431)
- **PDF**: https://arxiv.org/pdf/2610.28431
- **详细分析**: [[20_Research/Papers/具身智能/Plausible_Future,_Wrong_Choice_Steering_World-Action_Models_toward_Intended_Future|Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future]]
- **作者**: Zhuohao Li, Jiawei He, Yuxuan Yan, Lang Zhou, Yinghao Li, Yanrui Li, Tianyu Zhang, Yi-Yang Song, Xirui Wu andYi-Lin Wei, Fating Hong, Qing Zhang, Zhilin Zhao...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Plausible Future, Wrong Choice: Steering World-Action Models toward Intended Future》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, StageBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-Action Models (WAMs) have emerged as a promising paradigm for embodied generalist policies by jointly modeling future world evolution and robot actions across diverse manipulation tasks. However, representing diverse futures is only the first step: a capable WAM must also generate futures that match the requirements of the current task and execution progress. In long-horizon manipulation where similar observation-action segments occur across different tasks and stages, existing approaches may generate locally plausible yet misdirected rollouts to drift toward wrong task stage, i.e., a phenomenon we term Stage Confusion. To address this problem, we propose TaskWAM, a closed-loop, stage-aware framework that represents fine-grained task requirements with Mode Tokens and tracks execution progress with State Tokens, forming a structured task state to steer world--action generation toward intended future. We further introduce StageBench, a controlled multi-stage manipulation benchmark with parameterized stage variations and automated evaluation.Extensive experiments on both simulation benchmarks and real-world tasks demonstrate that TaskWAM effectively reduces confusion and achieves competitive performance with state-of-the-art methods. Moreover, TaskWAM provides strong plug-and-play transfer across heterogeneous WAM architectures and robot embodiments, including single-arm robots, dual-arm grippers, dexterous hands, and humanoid robots.

</details>

---

### [[20_Research/Papers/大模型/MAS-Guard_Unified_Guardrails_from_Individual_Agents_to_Multi-Agent_LLM_Systems|MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems]]

![[assets/2610.28397_figure.png|800]]

- **arXiv**: [2610.28397](https://arxiv.org/abs/2610.28397)
- **PDF**: https://arxiv.org/pdf/2610.28397
- **详细分析**: [[20_Research/Papers/大模型/MAS-Guard_Unified_Guardrails_from_Individual_Agents_to_Multi-Agent_LLM_Systems|MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems]]
- **作者**: Mohammad Kachuee, Phu Mon Htut, Sheng Li, Nikolaos Pappas, Miguel Ballesteros Martinez, Yassine Benajiba, Sujith Ravi, Dan Roth
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through specialization and collaboration, but distributed authority, heterogeneous roles, and opaque or potentially compromised participants make safeguarding even more challenging. Existing defenses address important individual threats but provide fragmented coverage across local execution, system-level interactions, and enforcement mechanisms. We introduce MAS-Guard, a unified framework that closes this gap for safeguarding single- and multi-agent AI applications containing both instrumentable and opaque agents. Within instrumentable agents, the proposed local Agent Guardrail (A-Guard) layer applies task-specific experts to assess agentic events. At the system level, developer-owned Agent Charters and a Control Plane combine deterministic structural checks of routes, agent capabilities, and message formats with semantic assessments of roles and message content. These complementary layers enable enforcement through a shared set of interventions: allow, reflection, confirmation, and block. Evaluated across six benchmarks covering diverse single- and multi-agent scenarios with three agent LLMs from different providers, MAS-Guard reduces the overall attack success rate by 71.5-86.3% relative to unguarded agents, while meeting the utility reference criterion on benign tasks.

</details>

---

### [[20_Research/Papers/大模型/FALCA_Falsification-Aware_Reinforcement_Learning_with_Hierarchical_Credit_Assignment_for_Long-Horizon_Deep_Search_Agents|FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents]]

![[assets/2610.28361_figure.png|800]]

- **arXiv**: [2610.28361](https://arxiv.org/abs/2610.28361)
- **PDF**: https://arxiv.org/pdf/2610.28361
- **详细分析**: [[20_Research/Papers/大模型/FALCA_Falsification-Aware_Reinforcement_Learning_with_Hierarchical_Credit_Assignment_for_Long-Horizon_Deep_Search_Agents|FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents]]
- **作者**: Zijun Dou, Kun Luo, Chaofan Li, Shuqi Lu, Zheng Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.5，强化学习 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepSearchQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search trajectory: agents may anchor on an incorrect candidate, collect partially supporting evidence, overlook contradictions, and accumulate errors that misguide subsequent reasoning. We propose FALCA, a falsification-aware framework that formulates deep search as a propose-falsify process. FALCA adopts a collaborative Searcher-Falsifier architecture, where the Searcher proposes candidate answers or sub-answers, while independent Falsifiers actively seek counterevidence, check unmet constraints, identify conflicts, and produce concise falsification reports for research-state revision. To strengthen this loop, we introduce falsification-aware training, combining SFT warmup on falsification trajectories with agentic RL based on parallel rollouts and hierarchical credit assignment over research stages, state transitions, and actions. Experiments on five search benchmarks show that FALCA improves long-horizon deep search performance over backbone and harness ablations, while reducing confirmation bias and error accumulation through more effective falsification and research-state revision.

</details>

---

### [[20_Research/Papers/大模型/Local_Work,_Global_Progress_A_Convergence_Theory_of_AI_Agent_Collaboration|Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration]]

![[assets/2610.28286_first_page.png|800]]

- **arXiv**: [2610.28286](https://arxiv.org/abs/2610.28286)
- **PDF**: https://arxiv.org/pdf/2610.28286
- **详细分析**: [[20_Research/Papers/大模型/Local_Work,_Global_Progress_A_Convergence_Theory_of_AI_Agent_Collaboration|Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration]]
- **作者**: Ivan Ilin, Peter Richtárik
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.0（加权：大模型 0.8，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teams of large language model (LLM) agents are increasingly applied to complex tasks, but their collaboration protocols are mostly designed empirically, without convergence guarantees. We formalize collaborative problem solving as block optimization: each agent improves one part of a shared solution, guided by its local objective plus a correction for how its changes affect the other parts. A coordinator checks every proposal against the global objective and merges proposals that do not interfere with each other. We prove linear convergence up to an error floor that vanishes when the corrections are exact. Interfering proposals can also be merged once their combination has been checked; the rate then depends on how well the proposals actually combine, not on worst-case interactions. With GPT-OSS-120B agents on robot routing, a three-agent team finds collision-free plans in every run, better than those of a single agent that controls all robots. On a larger routing task, a six-agent team completes its search about twice as fast as the single agent (in median). Merging the best checked combination of proposals, rather than only proposals that do not interfere, cuts the team's search time by about 30%. With constants measured on the runs, our convergence bound holds in every round and follows the observed progress. We also test the theory on query planning in SQLite and on a synthetic task.

</details>

---

### [[20_Research/Papers/大模型/PI-MLLM_Psychophysics-Inspired_Multimodal_Large_Language_Model_for_Oddly_Satisfying_Video_Emotion_Analysis|PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis]]

![[assets/2610.28264_figure.png|800]]

- **arXiv**: [2610.28264](https://arxiv.org/abs/2610.28264)
- **PDF**: https://arxiv.org/pdf/2610.28264
- **详细分析**: [[20_Research/Papers/大模型/PI-MLLM_Psychophysics-Inspired_Multimodal_Large_Language_Model_for_Oddly_Satisfying_Video_Emotion_Analysis|PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis]]
- **作者**: Yuheng Zhang, Jie Zhang, Yuecong Min, Yunwei Zhao, Meichen Liu, Qiankun Li, Shiguang Shan
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.6（加权：大模型 1.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Oddly Satisfying Videos (OSVs) can evoke strong viewer responses through repetitive motion, visual tactility, and ASMR-like sounds despite containing few explicit semantic emotion cues. This makes OSVs a challenging setting for Video Emotion Analysis (VEA), since most existing methods focus on semantic video content and under-model the physical sensory dynamics that shape viewer responses. To support Oddly Satisfying Video Emotion Analysis (OSVEA), we construct the Oddly Satisfying Video Dataset (OSVD), comprising 12,000 annotated 5-second clips. Each clip provides viewer-emotion labels under video-only, audio-only, and audio-visual conditions, together with explanations grounded in visual and acoustic sensory evidence. Building on OSVD, we propose PI-MLLM, a psychophysics-inspired multimodal large language model that integrates Modality-Specific Dynamics Alignment (MSDA) and Coalition-Based Audio-Visual Attribution (CAVA). MSDA uses auxiliary prediction objectives to align modality representations with visual motion and acoustic energy-onset dynamics. CAVA evaluates emotion scores across modality coalitions and applies Shapley attribution to identify the dominant modality and determine whether visual and auditory evidence is synergistic or conflicting. Experiments show that PI-MLLM improves both viewer-side emotion prediction and sensory-grounded explanation quality, suggesting the value of physical sensory cues to video emotion analysis.

</details>

---

### [[20_Research/Papers/强化学习/Reframing_Object-Centric_Reinforcement_Learning_From_Absolute_to_Relative_Representations|Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations]]

![[assets/2610.28197_figure.png|800]]

- **arXiv**: [2610.28197](https://arxiv.org/abs/2610.28197)
- **PDF**: https://arxiv.org/pdf/2610.28197
- **详细分析**: [[20_Research/Papers/强化学习/Reframing_Object-Centric_Reinforcement_Learning_From_Absolute_to_Relative_Representations|Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations]]
- **作者**: Cedric Derstroff, Jannis Blüml, Janosch Moos, Michael Girstl, Zihan Ye, Debora Clever, Kristian Kersting
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reframing Object-Centric Reinforcement Learning: From Absolute to Relative Representations》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object-centric reinforcement learning agents typically receive each object's position in a fixed global frame, even though their decisions usually depend on where objects are relative to one another. These absolute views often fail to capture the local context that is most relevant to the agent's behavior. As a result, an agent must relearn the same response at every location where a configuration can occur, and its performance collapses when the scene is merely shifted. In this work, we propose a shift toward Object-Relative Coordinates fixed to Anchor (ORCA), where entities are described in a relative frame of reference. To operationalize this idea, we introduce Object-Relative inductive-Bias Transformers (ORBiT), a transformer-based architecture for processing anchor-relative inputs in reinforcement learning. Our results suggest these relative representations improve performance for both MLP and transformer agents. Furthermore, we demonstrate that ORBiT outperforms the pixel-based PPO baseline, achieving an aggregate HNS IQM greater than 1.0 over 13 Atari games. ORBiT learns the game of Foosball from scratch, dominating all baselines. In our controlled Tag environment, we further show that ORCA extends to rotations, that ORBiT generalizes to unseen numbers of distractors, and that these gains require a decision-relevant anchor.

</details>

---

### [[20_Research/Papers/具身智能/Perceives_but_Doesn't_Brake_A_Perception-Action_Binding_Gap_in_Reasoning_Driving_VLAs|Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs]]

![[assets/2610.28184_figure.png|800]]

- **arXiv**: [2610.28184](https://arxiv.org/abs/2610.28184)
- **PDF**: https://arxiv.org/pdf/2610.28184
- **详细分析**: [[20_Research/Papers/具身智能/Perceives_but_Doesn't_Brake_A_Perception-Action_Binding_Gap_in_Reasoning_Driving_VLAs|Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs]]
- **作者**: Matteo Cercola, Katie Z Luo, Simone Formentin, Marco Pavone
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AlpaSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning-augmented vision-language-action (VLA) driving models can perceive and reason about safety-critical hazards yet fail to translate that evidence into safe actions. We characterize this failure as a perception-action binding gap: hazard information is available inside the model but exerts insufficient control over trajectory generation. Using matched simulated counterfactuals and logged driving replay, we show that in-path hazards are actually encoded in the visual representation, but longitudinal plans are dominated by ego-speed history and respond only weakly to hazard proximity or the model's own reasoning trace. Further analysis shows that the trajectory generator is capable of braking but sometimes fails to do so due to the perception-action binding gap. Without retraining or modifying any weights, we inject a hazard-conditioned energy into the frozen flow-matching sampler of Alpamayo-1.5, restoring the missing coupling at generation time. With exact obstacle geometry, guidance cuts footprint intrusion from 58.1% to 14.5% and recovers safe braking whenever sufficient stopping distance remains, eliminating collisions entirely in our braking-relevant closed-loop battery. It also reverses the diagnosed dependence of the plan, from tracking ego speed to responding to obstacle range. These results separate hazard perception from hazard control in driving VLAs, show that unsafe behavior can arise even when the model has both the evidence and the ability to act on it, and propose a simple fix for bridging this binding gap.

</details>

---

### [[20_Research/Papers/机器人/De-Diffusing_WAMs_Action-Sufficient_Direct_Prediction_for_Robot_Control|De-Diffusing WAMs: Action-Sufficient Direct Prediction for Robot Control]]

![[assets/2610.28122_figure.png|800]]

- **arXiv**: [2610.28122](https://arxiv.org/abs/2610.28122)
- **PDF**: https://arxiv.org/pdf/2610.28122
- **详细分析**: [[20_Research/Papers/机器人/De-Diffusing_WAMs_Action-Sufficient_Direct_Prediction_for_Robot_Control|De-Diffusing WAMs: Action-Sufficient Direct Prediction for Robot Control]]
- **作者**: Shaoyi Zheng, Zhongtao Jiang, Yue Peng, Wenbo Lu, Shunchi Zhang, Xi Wang, Shengji Wan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《De-Diffusing WAMs: Action-Sufficient Direct Prediction for Robot Control》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GigaWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cascade world-action models (WAMs) use predicted visual futures to condition robot actions, but inherit costly iterative inference from diffusion-pretrained experts. We ask what a single-step predicted future must preserve to support accurate single-step action prediction. In the evaluated WAM, resampling video noise has little effect on downstream actions, yet naively truncating both streams to one step substantially reduces task success. Video-space supervision only partially closes this gap, and a local sensitivity analysis shows that vision prediction errors have highly unequal consequences for action accuracy. These findings motivate DirectWAM, which converts pretrained video and action experts into single-step predictors without stochastic sampling through action-sufficient distillation, while retaining the explicit future-to-action cascade. After learning a one-step action model, we train the future predictor by decoding actions from its own predicted futures and backpropagating demonstration action error through the expert, with an optional future-latent reconstruction loss. The resulting objective evaluates the student-generated future through its downstream control consequences rather than relying on representation matching alone. DirectWAM achieves 97.1% average success across four LIBERO suites and 85.4% on RoboTwin 2.0, outperforming Flash-WAM at the same one-evaluation-per-stream budget. This advantage has also extended to three real-world tasks that we designed. Compared with the full iterative teacher, it reduces inference latency by $28.0\times$.

</details>

---

### [[20_Research/Papers/世界模型/Slot-JEPA_Object-Structured_Prediction_Interfaces_for_Latent_World_Models|Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models]]

![[assets/2610.28074_figure.jpg|800]]

- **arXiv**: [2610.28074](https://arxiv.org/abs/2610.28074)
- **PDF**: https://arxiv.org/pdf/2610.28074
- **详细分析**: [[20_Research/Papers/世界模型/Slot-JEPA_Object-Structured_Prediction_Interfaces_for_Latent_World_Models|Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models]]
- **作者**: Peisong Wen, Qianqian Xu, Minye Lei, Siran Dai, Yang Liu, Qingming Huang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.0（加权：世界模型 0.8，机器人 0.2）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models》归入 世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor to redundantly recover object structure that could otherwise be reused across tasks before modeling interactions. Second, the lack of explicit entity correspondence across time makes historical transitions expensive, restricting the predictor's flexibility in utilizing context. Third, without explicit transport structure, existing JEPA models typically use pointwise l1/l2 distances, which are insensitive to spatial displacement when predicted and goal supports are largely disjoint. We propose the Slot-based Joint-Embedding Predictive Architecture (Slot-JEPA), which decomposes dense representations into stable semantic slots and time-varying spatial masks. Pretrained once and frozen downstream, this decomposition exposes a reusable object-structured interface. Building on it, our Transition Memory Predictor (TMP) stores visual transitions as compact masks and retrieves useful context using statistics of corresponding slots. Its two branches separate slot-specific dynamics from shared cross-slot dynamics. We further use Unbalanced Optimal Transport (UOT) to supervise mask prediction and evaluate candidate plans by transporting mass between aligned predicted and goal masks, providing a signal better aligned with spatial progress. Across seven visual-understanding benchmarks, the slot-reconstructed features remain transferable. Slot-JEPA also improves goal-conditioned planning across six planar environments and four robotic arm planning tasks on the REALM-JEPA benchmark.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Tactile-Aware_Hand_Representations_from_Human_Hand-Object_Interaction_Data|Learning Tactile-Aware Hand Representations from Human Hand-Object Interaction Data]]

![[assets/2610.27995_figure.png|800]]

- **arXiv**: [2610.27995](https://arxiv.org/abs/2610.27995)
- **PDF**: https://arxiv.org/pdf/2610.27995
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Tactile-Aware_Hand_Representations_from_Human_Hand-Object_Interaction_Data|Learning Tactile-Aware Hand Representations from Human Hand-Object Interaction Data]]
- **作者**: Yeonguk Yu, Jaehong Kim, Byungok Han
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Tactile-Aware Hand Representations from Human Hand-Object Interaction Data》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile representation learning for dexterous manipulation often requires substantial robot-side data collection, limiting its scalability across different hands and sensors. We explore whether large-scale human hand-object interaction (HOI) data can provide a useful prior for robotic tactile learning. To this end, we propose HuTact, a framework that pretrains tactile-aware hand representations from human HOI data without requiring real tactile signals during pretraining. HuTact transfers the interaction structure learned from human hand motions to robotic tactile observations and can be further adapted with a small amount of unlabeled robot interaction data. We evaluate HuTact on tactile perception and manipulation tasks, including grasp prediction, slip detection, object classification, and tactile-conditioned policy learning. Across these tasks, human HOI pretraining improves data efficiency and provides a strong initialization for downstream learning. Notably, with HOI pretraining followed by midtraining on unlabeled robot play data, HuTact achieves 88.26% Macro-F1 on grasp prediction using only 25\% of the labeled downstream data, comparable to training from scratch on the full labeled dataset (88.23%). These results suggest that human interaction data can serve as a scalable complementary source for robotic tactile representation learning.

</details>

---

### [[20_Research/Papers/强化学习/From_Comparison_to_Selection_Enhancing_Cross-Scale_Generalization_of_Pointer_Networks_Trained_with_Reinforcement_Learning_for_Capacitated_Dr|From Comparison to Selection: Enhancing Cross-Scale Generalization of Pointer Networks Trained with Reinforcement Learning for Capacitated Drone Delivery Routing]]

![[assets/2610.27936_figure.png|800]]

- **arXiv**: [2610.27936](https://arxiv.org/abs/2610.27936)
- **PDF**: https://arxiv.org/pdf/2610.27936
- **详细分析**: [[20_Research/Papers/强化学习/From_Comparison_to_Selection_Enhancing_Cross-Scale_Generalization_of_Pointer_Networks_Trained_with_Reinforcement_Learning_for_Capacitated_Dr|From Comparison to Selection: Enhancing Cross-Scale Generalization of Pointer Networks Trained with Reinforcement Learning for Capacitated Drone Delivery Routing]]
- **作者**: Sofiene Lassoued, Devara Tertia, Stefan Lier, Andreas Schwung
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人
- **相关性评分**: 1.6（加权：强化学习 0.8，机器人 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《From Comparison to Selection: Enhancing Cross-Scale Generalization of Pointer Networks Trained with Reinforcement Learning for Capacitated Drone Delivery Routing》归入 强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Set2Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicles (UAVs) enable fast, flexible last-mile and emergency delivery, but their routing remains challenging as the number of clients varies. Classical approaches based on mixed-integer programming and heuristics can scale poorly or require problem-specific design, motivating learning-based alternatives. Reinforcement learning is particularly promising, provided a single policy can generalize across problem sizes without retraining. Although attention-based Pointer Networks are inherently size-agnostic, their solution quality degrades under both upscaling and downscaling. Using the Capacitated Vehicle Routing Problem (CVRP) as a controlled proxy, with fixed capacity reflecting drone payload constraints, we investigate this degradation and identify three contributing factors: shifts in node density, attention dispersion, and dilution of the mean-pooled graph context. We systematically compare architecture-wide, encoder-side, and decoder-side modifications to address these limitations and propose a learned, permutation-invariant graph-context aggregation mechanism, implemented as a weighted average and as Set2Set. Results reveal distinct requirements for transfer in each direction: entropy-based attention scaling reduces the CVRP20-to-CVRP100 performance gap by 1.41 percentage points, while the proposed aggregation methods achieve the largest improvement on the more challenging CVRP100-to-CVRP20 transfer, approximately 0.9 percentage points. Exploiting this complementarity, we introduce an approach selector that chooses the best model for each training-target size pair. The selector reduces cost relative to the reference model across all nine seen train-test pairs and eight of nine pairs involving unseen sizes (CVRP35, CVRP75, and CVRP200), achieving improvements of up to 3.2 percent.

</details>

---

### [[20_Research/Papers/大模型/Quantum-JEPA_Quantum_Born_Priors_for_Latent-Action_JEPA_World_Models|Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models]]

![[assets/2610.27921_figure.png|800]]

- **arXiv**: [2610.27921](https://arxiv.org/abs/2610.27921)
- **PDF**: https://arxiv.org/pdf/2610.27921
- **详细分析**: [[20_Research/Papers/大模型/Quantum-JEPA_Quantum_Born_Priors_for_Latent-Action_JEPA_World_Models|Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models]]
- **作者**: Zhiyuan Liu, Sicheng Liu, Haiyu Wu
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，世界模型 0.8）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future representations using a conditional quantum Born prior. Circuit measurements generate binary latent actions, which a shared predictor maps to alternative future representations. We train the quantum prior through the quality and diversity of these predictions using a sampled energy objective. Our model learns distinct continuations on constructed multimodal tasks and captures latent-action correlations that support coordinated multi-agent futures. On D3IL, a benchmark of diverse human demonstrations, our trained models generate multiple obstacle-crossing routes from a common starting point without observed motion. On the controlled tasks, our classical and quantum prior implementations improve prediction validity and distributional fidelity over the evaluated variational baselines. Our quantum priors combine competitive predictive quality with a parameter-efficient sampling structure: they avoid an exponentially sized categorical output layer while supporting correlated latent actions. We further validate finite-shot parameter-shift training, including training with readout noise. Unlike most prior work, which focuses on simulation, we also verify the feasibility of inference with trained priors on a real QPU. These results establish a trainable quantum component for JEPA future prediction and a basis for exploring quantum-enhanced world models at larger scales.

</details>

---

### [[20_Research/Papers/大模型/SAPD_Learning_from_Agent_Experience_without_Environment_Interaction|SAPD: Learning from Agent Experience without Environment Interaction]]

![[assets/2610.27847_first_page.png|800]]

- **arXiv**: [2610.27847](https://arxiv.org/abs/2610.27847)
- **PDF**: https://arxiv.org/pdf/2610.27847
- **详细分析**: [[20_Research/Papers/大模型/SAPD_Learning_from_Agent_Experience_without_Environment_Interaction|SAPD: Learning from Agent Experience without Environment Interaction]]
- **作者**: Juncheng Diao, Haibin Wang, Wei Shi, Yifan Ding, Qingbin Li, Rongxiang Weng, Xunliang Cai
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.7，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SAPD: Learning from Agent Experience without Environment Interaction》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling the training of Large Language Model (LLM) agents typically requires a large collection of executable environments, whose construction, maintenance, and operation constrain the expansion of training experience. Existing offline trajectories offer an opportunity to reuse interaction experience, yet effectively refining the current policy without revisiting these environments remains challenging: supervised fine-tuning (SFT) can lead to catastrophic forgetting, while online reinforcement learning requires real-time interaction with the environment. To address this challenge, we propose Step-Advantage Policy Distillation (SAPD), a method for learning from offline trajectories using relative step advantages. SAPD decomposes multi-turn trajectories into individual decision contexts for on-policy distillation, allowing the student to generate responses conditioned on recorded histories, and introduces relative step advantage signals to stabilize training. The entire process requires neither new environment observations nor additional multi-turn interactions. Experiments on ALFWorld, WebShop, and Search-based QA show that SAPD improves performance across different teacher configurations, mitigates catastrophic forgetting compared with SFT, and runs at least $4.7\times$ faster per training step than online OPD. We will release our code soon.

</details>

---

### [[20_Research/Papers/大模型/When_Does_Experience_Memory_Help_Closed-Loop_LLM_Driving_Agents_A_Controlled_Evaluation_with_Resampled_Warmup_Pools,_Token-Matched_Fillers,_|When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines]]

![[assets/2610.27714_first_page.png|800]]

- **arXiv**: [2610.27714](https://arxiv.org/abs/2610.27714)
- **PDF**: https://arxiv.org/pdf/2610.27714
- **详细分析**: [[20_Research/Papers/大模型/When_Does_Experience_Memory_Help_Closed-Loop_LLM_Driving_Agents_A_Controlled_Evaluation_with_Resampled_Warmup_Pools,_Token-Matched_Fillers,_|When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines]]
- **作者**: Yingxin Jia, Xuanyi Li
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, LimSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When does experience memory help a closed-loop LLM driving agent? Published gains cannot say, because the two factors we find to matter most, which warmup experiences the pool contains and what any injected tokens do to the prompt, are controlled in none of them. We answer with a controlled evaluation on one audited HighwayEnv testbed (1Hz, gpt-4o-mini for the decisive contrasts). We treat the warmup pool as a resampled random factor (ten disjoint pools) and add token-matched irrelevant-filler controls, oracle-certified diagnostics, caution-pricing metrics, and quantified audits of the baseline ports. The probe suite spans flat-text retrieval (a DiLu port), a single-frame grid port (RESPOND-inspired), our episodic temporal-graph memory, a retrieval-free consolidated rulebook, and a flat K-step observation-history baseline. Four findings follow, each a property of this testbed. (1) Headline memory gains belong to the warmup draw. The reported pool is the best of ten for both retrieval memories, which beat No-Memory in only one pool of ten (sign test p=0.011), and even the rulebook's apparent pool-immunity collapsed on five fresh draws. (2) No retrieval design tested exceeds token-matched filler. The collision-only merge ceiling is reached by a single 15-token caution instruction, and metrics that price caution erase the rulebook's lead. (3) Representational sophistication is nowhere robustly operative. (4) Baseline port quality silently inverts conclusions. On this testbed, a single-pool comparison without filler controls would have reported memory gains that these controls reverse. We release the testbed, audited ports, seeds, and caches.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Retain_Benchmarking_Cross-Dimension_Effects_of_Vision_Tuning_in_VLAs|VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs]]

![[assets/2610.27698_figure.png|800]]

- **arXiv**: [2610.27698](https://arxiv.org/abs/2610.27698)
- **PDF**: https://arxiv.org/pdf/2610.27698
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Retain_Benchmarking_Cross-Dimension_Effects_of_Vision_Tuning_in_VLAs|VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs]]
- **作者**: Borui Xu, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.5，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：InternVLA, OpenVLA, VLM4VLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain. Measuring this cross-dimension effect requires separating target gains from off-target changes, isolating adaptation effects from architectural differences, ruling out generic forgetting, and comparing tuning choices. Therefore, we introduce VLA-Retain, a benchmark that compares five open VLA models, tuned on Camera-view or Sensor-noise data, with their own base checkpoints on LIBERO-Plus dataset spanning seven perturbation dimensions. Our study reveals four findings. First, targeted vision tuning is not local, and its target gain does not predict retention. Mean off-target gain is negative in 8 of 10 model--domain configurations. Under Camera-view tuning, X-VLA gains $69.4$ percentage points on the target but loses $4.6$ points on average elsewhere, whereas OpenVLA-OFT gains $39.3$ and $1.4$ points, respectively. Second, these regressions are not explained only by performance loss on the same tasks without perturbations. Third, broader training coverage raises overall gain over target-specific training but does not eliminate dimension-level regressions. Fourth, tuning strategies are model-dependent, as DELTA-style feature preservation raises X-VLA's mean off-target gain to $+1.2$ points but lowers OpenVLA-OFT's to $-23.1$. Overall, these findings show that target-domain success alone is insufficient and highlight cross-dimensional retention as a key criterion for targeted VLA adaptation.

</details>

---

### [[20_Research/Papers/具身智能/CovNav_Conformal_Prediction-Guided_Adaptive_Inference_for_Object_Goal_Navigation|CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation]]

![[assets/2610.27677_figure.png|800]]

- **arXiv**: [2610.27677](https://arxiv.org/abs/2610.27677)
- **PDF**: https://arxiv.org/pdf/2610.27677
- **详细分析**: [[20_Research/Papers/具身智能/CovNav_Conformal_Prediction-Guided_Adaptive_Inference_for_Object_Goal_Navigation|CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation]]
- **作者**: Pengying Wu, Zhejia Wen, Kang Ding, Kangjie Zhou, Chunxuan Jiao, Wei Pan, Xiangli Nie, Chang Liu
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.55（加权：具身智能 0.6，大模型 0.45，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CovNav: Conformal Prediction-Guided Adaptive Inference for Object Goal Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TDANet, VLTNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In object goal navigation (ObjectNav), an embodied agent must find a target object (e.g., "find a bed") in a previously unseen environment, relying on spatial commonsense such as object co-occurrence. Large Language Models (LLMs) encode this commonsense, but deploying them on robots exposes a trade-off between reasoning quality and efficiency: cloud-based models incur latency and privacy risks, whereas small on-device LLMs are fast but prone to hallucinated spatial judgments. Hybrid reasoning LLMs offer both a fast non-thinking mode and a slow thinking mode, which raises a key question for embodied agents: when is slow thinking worth its cost? We propose CovNav, a training-free framework that answers this question with Conformal Prediction (CP), turning dual-process (System 1 / System 2) inference into an uncertainty-aware decision. Much like recent decision models such as Jev, CovNav casts each spatial query as a structured binary decision rather than free-form generation: a local LLM in fast mode judges whether the target is likely near an observed object, CP converts its token probabilities into a prediction set, and only ambiguous queries are escalated to slow chain-of-thought reasoning. The object-pair formulation keeps calibration tractable and supports open-set objects through off-the-shelf detectors. Experiments on Gibson and HM3D show that CovNav surpasses the strongest zero-shot baseline by 0.8 and 1.7 percentage points in success rate on HM3D v1 and v2, while invoking slow reasoning for only 12.4% of queries and retaining most of the gain of always-on thinking at a fraction of its latency. Real-robot experiments on a TurtleBot 4 further validate the approach. CovNav shows how calibrated uncertainty can decide when an embodied agent should think slowly, offering a principled form of adaptive test-time reasoning for LLM-based robots.

</details>

---

### [[20_Research/Papers/大模型/Reusing_Multimodal_Agents_Efficient_Evaluation_of_Sound_Designs_in_Games|Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games]]

![[assets/2610.27670_figure.png|800]]

- **arXiv**: [2610.27670](https://arxiv.org/abs/2610.27670)
- **PDF**: https://arxiv.org/pdf/2610.27670
- **详细分析**: [[20_Research/Papers/大模型/Reusing_Multimodal_Agents_Efficient_Evaluation_of_Sound_Designs_in_Games|Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games]]
- **作者**: Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro, Pratch Suntichaikul, Hai Van Pham, Ruck Thawonmas
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.9，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：M2CURL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assessments based on agent performance rather than human ratings, often require retraining agents from scratch for each sound design. Our approach first pre-trains a multimodal encoder that encodes visual and auditory information into a shared latent space. A reinforcement learning agent is then trained using this latent representation. We fine-tune the multimodal encoder for each sound design while keeping the trained policy fixed, allowing us to isolate the effects of sound changes on agent behavior. To evaluate the proposed method, we conducted experiments on games from multiple genres, comparing the performance of blind agents (agents using only sound input) under various sound designs. Experimental results suggest that this approach can detect differences in agent performance caused by degraded or altered sound design. Moreover, we significantly reduce the computational cost compared to retraining the agent from scratch. Experimental results suggest that this approach provides a practical and scalable solution for evaluating in-game sound designs. The source code, data and supplementary document are available: https://github.com/thainv0212/tog-reusing-agents.

</details>

---

### [[20_Research/Papers/强化学习/A_Head_Camera_Is_(Almost)_All_You_Need_An_Electronics-Free_UMI_Glove_Labelled_and_Observed_by_One_Moving_Camera|A Head Camera Is (Almost) All You Need: An Electronics-Free UMI Glove Labelled and Observed by One Moving Camera]]

![[assets/2610.27622_figure.jpg|800]]

- **arXiv**: [2610.27622](https://arxiv.org/abs/2610.27622)
- **PDF**: https://arxiv.org/pdf/2610.27622
- **详细分析**: [[20_Research/Papers/强化学习/A_Head_Camera_Is_(Almost)_All_You_Need_An_Electronics-Free_UMI_Glove_Labelled_and_Observed_by_One_Moving_Camera|A Head Camera Is (Almost) All You Need: An Electronics-Free UMI Glove Labelled and Observed by One Moving Camera]]
- **作者**: Yosub Shin, Yuan Liu, Igor Molybog
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《A Head Camera Is (Almost) All You Need: An Electronics-Free UMI Glove Labelled and Observed by One Moving Camera》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Handheld demonstration devices decouple data collection from the robot, but conventional designs burden the hand with a wrist camera, cables and a pose tracker (SLAM, an IMU, a VR controller, or a fixed external camera that the collector's body occludes), and burden the pipeline with as many data streams to timestamp, synchronise and cross-calibrate. We show that a single egocentric camera (USD 122) worn on the collector's head replaces the wrist camera, the pose tracker and their separate streams with one. It reads printed fiducials on an electronics-free glove (USD 22) against paper tiles taped around the workspace, giving the 6-DoF gripper pose and the jaw width from the same frames the policy will see; at deployment the same camera rides a low-cost (USD 120) arm beside the robot that mimics the collector's head from the robot's joint state. Against the robot's encoders the labels are accurate to 6.5 mm and 1.6 degrees median with 93-100% frame coverage, and a policy trained on them instead of encoders pays 3% in validation loss. Adding 194 glove demonstrations to 48 teleoperated episodes lifts rollout success from 10/25 to 17/25, level with 172 teleoperated episodes alone (18/25), and the full co-trained head-camera policy succeeds in 20/25 against 15/25 for the wrist-camera recipe, whose policies drop the object when the goal leaves their view, and 12/25 for a fixed camera.

</details>

---

### [[20_Research/Papers/大模型/The_More_the_Better_A_Comparison_of_Single-_and_Multi-Agent_LLM_Setups_on_a_Financial_Review_Task|The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task]]

![[assets/2610.27488_first_page.png|800]]

- **arXiv**: [2610.27488](https://arxiv.org/abs/2610.27488)
- **PDF**: https://arxiv.org/pdf/2610.27488
- **详细分析**: [[20_Research/Papers/大模型/The_More_the_Better_A_Comparison_of_Single-_and_Multi-Agent_LLM_Setups_on_a_Financial_Review_Task|The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task]]
- **作者**: Pei Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Practitioner guidance holds that a large language model reviews a document better when the work is divided among agents. We test a narrow form of it in a controlled comparison of single-agent and multi-agent setups on a financial task, reviewing credit assessment memos against requirements. One agent checks six requirements in one call. A team of three on the same model checks the same memo, two requirements each, in the same words, with no roles or later stage. Labels are known for every requirement on 300 synthetic memos, so misses and false alarms are measured separately. Two primary predictions are tested on four models at a Bonferroni-corrected level. Under an instruction to decide each requirement once, the team catches 0.08 to 0.10 more of the defects that carry an explanation on the three models whose single agent misses some, at the corrected level on two. It raises more false alarms on all four, at the corrected level on three. Balanced accuracy, an exploratory measure, changes by 0.02 or less, and the team uses 2.2 to 2.4 times the tokens. Showing each agent the requirements it was not given reduces the added false alarms on the two Claude models, at the corrected level on one. In exploratory comparisons, sampling the single agent three times and flagging on any draw gives higher balanced accuracy than the team on those models, and the team's results depend on the instruction.

</details>

---

### [[20_Research/Papers/强化学习/Refuses_When_Asked,_Complies_When_Acting_A_Runtime_Safety_Check_for_Robot_Control_Loops|Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops]]

![[assets/2610.27350_figure.png|800]]

- **arXiv**: [2610.27350](https://arxiv.org/abs/2610.27350)
- **PDF**: https://arxiv.org/pdf/2610.27350
- **详细分析**: [[20_Research/Papers/强化学习/Refuses_When_Asked,_Complies_When_Acting_A_Runtime_Safety_Check_for_Robot_Control_Loops|Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops]]
- **作者**: Arnav Grover
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harness on three household tasks whose hazard is common knowledge, such as "put the knife in the toy basket", the policy refused 0% of 15 trials, attempted the harm every time, and completed it in 27%. Its one exit, give_up, is meant for goals that cannot be achieved, and it never cited the hazard. We add an optional runtime safety check to the loop: before the first motion, the model is asked whether it would carry out the instruction, given the same camera frames. The check would have stopped all 15 hazardous instructions, including the 4 that completed the harm, and flagged none of the 15 harmless controls. Code and data: https://github.com/Arnav-Gr0ver/Refuses-When-Asked-Complies-When-Acting.

</details>

---

### [[20_Research/Papers/强化学习/VPFlow_Value-Predictive_Planning_with_Imperfect_World_Models_for_Offline_Goal_Reaching|VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching]]

![[assets/2610.27280_figure.png|800]]

- **arXiv**: [2610.27280](https://arxiv.org/abs/2610.27280)
- **PDF**: https://arxiv.org/pdf/2610.27280
- **详细分析**: [[20_Research/Papers/强化学习/VPFlow_Value-Predictive_Planning_with_Imperfect_World_Models_for_Offline_Goal_Reaching|VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching]]
- **作者**: Yunzhe Hu, Dong Xu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.36，世界模型 0.96）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《VPFlow: Value-Predictive Planning with Imperfect World Models for Offline Goal Reaching》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning enables skill acquisition by reaching any goal from any state without dense rewards. Model-based methods allow for planning by scaling test-time compute to solve complex tasks. Combining both holds appealing promise for pre-training on suboptimal demonstrations and zero-shot adaptation via goal specification and planning. Yet existing methods assume effective planning requires accurate next-state prediction in pixel or latent space. In this work, we show that value prediction is more useful for planning, whereas accurate state prediction is often unnecessary. Our key insight is that offline goal reaching naturally admits a closed-form Monte Carlo return, enabling value regression to replace temporal-difference bootstrapping. We use this return as the sole supervision for latent world models: imagined latents are trained to predict goal-reaching value rather than match future states, implicitly preventing representation collapse. These planning-oriented representations let imperfect world models imagine on the level sets of value field beyond dataset transitions. We then present VPFlow, a value-predictive planner that pairs the world models with a one-step flow policy and plans in its noise space via evolutionary search. It enables policy improvement with imagined generalized advantage and reduces out-of-distribution queries common in action-space planning. On 30 state and pixel OGBench datasets, VPFlow surpasses model-free baselines by at least 30.3 and 10.1 percentage points in success rate, respectively, and outperforms latent planners LeWorldModel, PLDM, and TD-MPC2. It achieves this despite a latent prediction error orders of magnitude larger than with state prediction, while minimizing this error lowers success rate. This demonstrates that value-predictive representations, not exact state prediction, are what offline planning requires.

</details>

---

### [[20_Research/Papers/大模型/Visual_Task_Modeling_and_Automated_Planning_for_Humanoid_Robots_in_Education_of_Individuals_with_Autism_Spectrum_Disorder|Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder]]

![[assets/2610.27162_figure.jpg|800]]

- **arXiv**: [2610.27162](https://arxiv.org/abs/2610.27162)
- **PDF**: https://arxiv.org/pdf/2610.27162
- **详细分析**: [[20_Research/Papers/大模型/Visual_Task_Modeling_and_Automated_Planning_for_Humanoid_Robots_in_Education_of_Individuals_with_Autism_Spectrum_Disorder|Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder]]
- **作者**: Lada Kudláčková
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.2，大模型 0.2，机器人 1.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Visual Task Modeling and Automated Planning for Humanoid Robots in Education of Individuals with Autism Spectrum Disorder》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robot-assisted education, a robot must understand how to complete a task in order to effectively guide a student through it. We present a novel method that enables a semi-autonomous, camera-equipped robot to recognise the task goal and plan actions to achieve it. Our work focuses on Shoebox Tasks, an activity commonly used in the education of individuals with Autism Spectrum Disorder (ASD). These tasks are designed so that the goal can be inferred directly from their visual structure. We have developed a solver that uses a vision-based Large Language Model to convert photos of a Shoebox Task into a Planning Domain Definition Language (PDDL) representation and generate action plans for solving it. We have also implemented a robotic interface that enables a Nao robot to autonomously execute various Shoebox Tasks and assist a student by suggesting next steps or signalling detected failures through action demonstrations, voice commands, or gestures. With an adapted robotic interface, the solver can be integrated into a variety of educational robots. No programming expertise is required from teachers, and the solver operates exclusively on captured images as input. Research in special educational needs indicates that students with ASD can benefit substantially from robot-assisted teaching, and our system aims to strengthen these learning opportunities while also fostering interest in robotics among individuals with ASD.

</details>

---

### [[20_Research/Papers/具身智能/Physical_AI_Concepts,_Techniques,_and_Challenges|Physical AI: Concepts, Techniques, and Challenges]]

![[assets/2610.27045_figure.png|800]]

- **arXiv**: [2610.27045](https://arxiv.org/abs/2610.27045)
- **PDF**: https://arxiv.org/pdf/2610.27045
- **详细分析**: [[20_Research/Papers/具身智能/Physical_AI_Concepts,_Techniques,_and_Challenges|Physical AI: Concepts, Techniques, and Challenges]]
- **作者**: Weinan Zhang, Chunhua Shen, Tianfan Xue, Bin Zhao, Bingqi Jiang, Zihan Guo, Zicai Cui, Yang Li, Ming Zhou, Xinyuan Chen, Lihe Ding, Xiao Chen...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 世界模型
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.2，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Physical AI: Concepts, Techniques, and Challenges》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, physical artificial intelligence (physical AI) has experienced rapid development, capturing significant attention in academia and industry. However, the field has yet to reach consensus on its definition, technical landscape, and core challenges. To address this gap, this monograph seeks to define physical AI, present its technical landscape, and examine each key technical subfield in depth. In doing so, it establishes a unified framework for Physical AI: artificial systems that perceive, model, and act upon the physical world through continuous feedback under real-world constraints. Further, this monograph distinguishes physical AI from conventional digital AI, embodied AI, cyber-physical systems, and digital twins. It develops the foundations of physical AI across physics, control, cognition, learning, and reasoning. It reviews key methodologies, including multimodal perception, physical data and simulation, world models, embodied foundation models, motor-control systems, multi-agent coordination, and hardware-software co-design. Furthermore, it examines applications spanning robotics, manufacturing, infrastructure, scientific experimentation, and autonomous services. Particular attention is given to sim-to-real transfer, reliability, real-time execution, evaluation, safety, governance, and long-term deployment. By connecting perception, prediction, decision-making, action, and adaptation in a closed loop, this monograph identifies the technical challenges and research directions required to advance from narrow automation toward more generalizable physical AI and, ultimately, physical artificial general intelligence (Physical AGI).

</details>

---

### [[20_Research/Papers/大模型/M-Plan_Comprehensive_Planning_For_LLM_Agents_with_Memory_Arrangement|M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement]]

![[assets/2610.27032_figure.png|800]]

- **arXiv**: [2610.27032](https://arxiv.org/abs/2610.27032)
- **PDF**: https://arxiv.org/pdf/2610.27032
- **详细分析**: [[20_Research/Papers/大模型/M-Plan_Comprehensive_Planning_For_LLM_Agents_with_Memory_Arrangement|M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement]]
- **作者**: Ziyang Liu, Jiakang Yuan, Jiayuan Fan, Tao Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks, particularly in environments without prior training. A key limitation of single LLMs is their difficulty in processing long contexts, which stems from weaknesses in continuous decision-making and reasoning capabilities. Although existing multi-agent systems (MAS) equipped with long-term memory bases can partially address this gap, they mostly rely on knowledge reuse or summarization, an approach that is often constrained by directly retrieval without any adaptation for the current task, while the retrieved memory may contain much history noises waiting to be preprocessed. In contrast, MAS characterized by task-specific guidance often lack long-term memory specifically designed for the guidance. To address these challenges, we propose M-Plan, a closed-loop MAS framework that integrates long-term and short-term memory. By combining global-local and past-current guidance, M-Plan enhances agents' performance on multi-turn tasks while maintaining a plug-and-play design. During task execution, agents receive task-specific milestones and insights, and are provided with local hints only when confusion arises, which form global-local guidance together. These guidance generation and utilization construct the short-term memory as well. After task completion, relevant information about the current task is optimized or reorganized before being sent to the long-term memory storage for future retrieval. The designments mentioned above build a comprehensive framework different from other individual long-term or short-term memory works. Extensive experiments on multi-turn tasks including ALFWorld, Webshop, and PDDL across diverse models demonstrate that M-Plan outperforms multiple baseline methods in both accuracy and efficiency.

</details>

---

### [[20_Research/Papers/大模型/Exploration_via_Activation-Space_Steering_for_Reinforcement_Learning_with_Verifiable_Rewards|Exploration via Activation-Space Steering for Reinforcement Learning with Verifiable Rewards]]

![[assets/2610.27012_figure.png|800]]

- **arXiv**: [2610.27012](https://arxiv.org/abs/2610.27012)
- **PDF**: https://arxiv.org/pdf/2610.27012
- **详细分析**: [[20_Research/Papers/大模型/Exploration_via_Activation-Space_Steering_for_Reinforcement_Learning_with_Verifiable_Rewards|Exploration via Activation-Space Steering for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Yunan Zeng, Jinhao Jing, Xi Cheng, Yuwang Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Exploration via Activation-Space Steering for Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) trains a language model by sampling responses, scoring them with an automatic verifier, and updating the policy from the resulting rewards. The policy therefore receives direct learning signals only from trajectories that appear in its rollouts. Yet repeated sampling from the same policy can concentrate on similar reasoning paths, leaving useful alternatives unexplored under a fixed rollout budget. We introduce Activation-Space Exploration (ASE), an online method for diversifying training rollouts. By clustering activation differences between correct and incorrect responses to the same problem, ASE builds a structured bank of latent exploration vectors. Different vectors are then applied to subsequent rollouts to explore alternative reasoning paths. On Qwen3-1.7B-Base and Qwen3-8B-Base trained on DAPO-Math-17k, ASE improves average Mean@8 across six mathematical reasoning benchmarks over GRPO by 4.87 and 1.87 percentage points, respectively, under the same rollout budget.

</details>

---

### [[20_Research/Papers/大模型/MAMath-Bench_Process-Aware_and_Robust_Evaluation_of_Multimodal_Multi-Agent_Mathematical_Reasoning|MAMath-Bench: Process-Aware and Robust Evaluation of Multimodal Multi-Agent Mathematical Reasoning]]

![[assets/2610.26943_figure.png|800]]

- **arXiv**: [2610.26943](https://arxiv.org/abs/2610.26943)
- **PDF**: https://arxiv.org/pdf/2610.26943
- **详细分析**: [[20_Research/Papers/大模型/MAMath-Bench_Process-Aware_and_Robust_Evaluation_of_Multimodal_Multi-Agent_Mathematical_Reasoning|MAMath-Bench: Process-Aware and Robust Evaluation of Multimodal Multi-Agent Mathematical Reasoning]]
- **作者**: Xinping Wang, Jie Ma, Rui Xing, Wensong Guo, Xiayi Zhang, Jianhao Deng, Zihao Zhou, Boqian Yang, Feijuan He
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《MAMath-Bench: Process-Aware and Robust Evaluation of Multimodal Multi-Agent Mathematical Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BattleAgentBench, M3MAD-Bench, MAMath-Bench, MQA, MultiAgentBench, OlympiadBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mathematical reasoning is a fundamental capability for educational applications of Large Language Models (LLMs), where reliable problem solving requires not only correct answers but also coherent and verifiable reasoning processes. Multi-agent systems (MASs) have shown growing potential in this domain by leveraging collaboration and verification among multiple LLM agents. However, existing evaluations primarily focus on the correctness of final answers in text-only settings, offering limited insight into multimodal reasoning capabilities, the reliability of intermediate reasoning steps, and robustness against reasoning errors. To address these limitations, we introduce MAMath-Bench, a process-aware benchmark designed to evaluate the multimodal mathematical reasoning capabilities of MASs. MAMath-Bench comprises 1,003 problems spanning 11 mathematical categories, multiple difficulty levels, and several modalities, including text, images, and audio. It features fine-grained milestone annotations to evaluate systems across three dimensions: problem-solving correctness, reasoning-process reliability, and robustness to adversarial reasoning-chain perturbations. Our evaluation yields three key findings. First, multi-agent collaboration does not consistently improve final-answer accuracy over strong single LLMs. Second, collaboration can substantially enhance the coverage of intermediate reasoning, but such gains may come at the cost of increased reasoning redundancy. Third, current systems remain vulnerable to adversarial reasoning errors, particularly those involving subtle structural perturbations. The dataset is available at https://github.com/mira-ai-lab/AgentMath.

</details>

---

### [[20_Research/Papers/强化学习/Expert-Guided_Rubrics_as_Dense_Reward_Signals_for_Reinforcement_Learning_in_Non-Verifiable_Domains|Expert-Guided Rubrics as Dense Reward Signals for Reinforcement Learning in Non-Verifiable Domains]]

![[assets/2610.26932_figure.png|800]]

- **arXiv**: [2610.26932](https://arxiv.org/abs/2610.26932)
- **PDF**: https://arxiv.org/pdf/2610.26932
- **详细分析**: [[20_Research/Papers/强化学习/Expert-Guided_Rubrics_as_Dense_Reward_Signals_for_Reinforcement_Learning_in_Non-Verifiable_Domains|Expert-Guided Rubrics as Dense Reward Signals for Reinforcement Learning in Non-Verifiable Domains]]
- **作者**: Ashish Bansal, Hossam Amer, Keerat Kaur Guliani, Parinita Edke, Lesley Matheson, Leizer Teran
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Expert-Guided Rubrics as Dense Reward Signals for Reinforcement Learning in Non-Verifiable Domains》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RubricRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents in non-verifiable domains such as financial services, where they must interpret user intent, rewrite queries, and retrieve information under domain-specific constraints. Although reinforcement learning (RL) can train such agents from the consequences of their actions, recent successes largely rely on verifiable tasks with automatically computed binary rewards. In non-verifiable retrieval tasks, assessing query quality requires scarce subject-matter expert (SME) judgment that is inherently graded rather than binary. With Group Relative Policy Optimization (GRPO), sparse rewards yield no useful learning signal when all sampled outputs within a group receive the same outcome, causing optimization to stall. We introduce a method that converts a small, fixed investment of SME judgment into a dense reward and combines it with retrieval-based metrics to form a hybrid, GRPO-compatible training signal. Experiments show improvements of up to 6\% in Recall@3 and 6.7\% in MRR@3 compared with sparse-reward baselines.

</details>

---

### [[20_Research/Papers/具身智能/Steerable_Pluralistic_Policy_Alignment_from_Anonymized_Crowd_Feedback|Steerable Pluralistic Policy Alignment from Anonymized Crowd Feedback]]

![[assets/2610.26914_figure.png|800]]

- **arXiv**: [2610.26914](https://arxiv.org/abs/2610.26914)
- **PDF**: https://arxiv.org/pdf/2610.26914
- **详细分析**: [[20_Research/Papers/具身智能/Steerable_Pluralistic_Policy_Alignment_from_Anonymized_Crowd_Feedback|Steerable Pluralistic Policy Alignment from Anonymized Crowd Feedback]]
- **作者**: Akansha Kalra, Ellen R. Novoseller, Vernon J. Lawhern, Daniel S. Brown
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Steerable Pluralistic Policy Alignment from Anonymized Crowd Feedback》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pluralistic alignment requires AI systems to learn from diverse populations whose preferences may reflect heterogeneous or even conflicting objectives, and to personalize their behavior to individual users. Existing approaches in pluralistic alignment often assume access to annotator identities and rely on powerful pretrained representations to model individual preference variations. We propose Preference-PCA Pluralistic Learning (P3L), a novel framework for pluralistic alignment that jointly learns trajectory embeddings and the shared basis of preference directions via PCA decomposition from heterogeneous crowd feedback without requiring annotator identities. At test time, our approach enables rapid and accurate personalized reward learning and downstream policy optimization. Experiments across multiple embodied control tasks demonstrate that P3L enables steerable personal alignment that generalizes beyond the offline dataset to out-of-distribution new users and attains competitive RL and test performance, while substantially reducing computational cost and supporting variable adaptation query budgets.

</details>

---

### [[20_Research/Papers/大模型/Large_language_model_and_reinforcement_learning_based_autonomous_construction_and_progress_updates|Large language model and reinforcement learning based autonomous construction and progress updates]]

![[assets/2610.26899_first_page.png|800]]

- **arXiv**: [2610.26899](https://arxiv.org/abs/2610.26899)
- **PDF**: https://arxiv.org/pdf/2610.26899
- **详细分析**: [[20_Research/Papers/大模型/Large_language_model_and_reinforcement_learning_based_autonomous_construction_and_progress_updates|Large language model and reinforcement learning based autonomous construction and progress updates]]
- **作者**: Yifei Xiao, Huasheng Lin, T. Y. Yang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人
- **相关性评分**: 2.0（加权：大模型 0.8，强化学习 1，机器人 0.2）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《Large language model and reinforcement learning based autonomous construction and progress updates》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Due to the rapid growth of the global population, traditional construction methods are gradually unable to meet the current housing demand. The advancement of machine learning algorithms has encouraged researchers to explore their applications in the construction industry, leading to more intelligent and efficient building processes. In particular, the rise of large language models in recent years has provided more possibilities for the transformation from traditional construction to smart construction. In this study, a large language model and reinforcement learning based autonomous construction method is proposed. An enhanced soft actor-critic reinforcement learning algorithm is developed to plan actions for a mobile crane according to construction tasks. Robot kinematics and control algorithms are used to ensure that the actions generated by the reinforcement learning algorithm can be executed by the crane. In addition, a customized embedding model is developed to extract information from the construction environment according to user interests. Then, a large language model, ChatGPT 5, is used to update construction progress, provide safety information to control system, and generate construction progress reports. The feasibility of proposed method is verified through several full-scall retaining wall construction experiments.

</details>

---

### [[20_Research/Papers/大模型/Navalia_Advancing_Cowork_Agents_through_Verifiable_Task_Synthesis_and_Long-Horizon_Post-Training|Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training]]

![[assets/2610.26887_first_page.png|800]]

- **arXiv**: [2610.26887](https://arxiv.org/abs/2610.26887)
- **PDF**: https://arxiv.org/pdf/2610.26887
- **详细分析**: [[20_Research/Papers/大模型/Navalia_Advancing_Cowork_Agents_through_Verifiable_Task_Synthesis_and_Long-Horizon_Post-Training|Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training]]
- **作者**: Hengqi Liu, Ziyuan Liu, Yang Qin, Wanting Zhou, Zichuan Wang, Jiachen Liang, Xu Chu, Shaowei Chen, Zhaokai Luo, Mu Chuan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OfficeQA, Workspace-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are evolving from conversational assistants into Cowork Agents capable of autonomous planning, tool use, and complex task execution. Financial analysis requires these agents to integrate cross-document evidence and perform multistep numerical reasoning, but expert task authoring is costly, while direct LLM synthesis struggles to produce challenging tasks with reliable answers. We introduce Navalia, a framework for Cowork Agents that combines verifiable task synthesis with long-horizon post-training. Using corporate financial reports as its data source, Navalia semantically selects supporting evidence from complete fact sets and constructs executable computation chains to generate analytical tasks with traceable evidence and actual data dependencies between steps. We further use independent LLM review and programmatic checks to verify evidence consistency and answer correctness. The verified tasks are then used for trajectory collection, cold-start supervised fine-tuning (SFT), and reinforcement learning (RL) to improve long-horizon task execution. Navalia, initialized from Qwen3.6-35B-A3B, achieves consistent gains over the base model across all five benchmarks: OfficeQA Pro, FinSearchComp, Finance Agent Benchmark, APEX-Agents-AA, and Workspace-Bench-Lite. These results demonstrate that Navalia improves evidence integration, tool use, and long-horizon task execution capabilities and generalizes to broader Cowork settings, including general office tasks.

</details>

---
