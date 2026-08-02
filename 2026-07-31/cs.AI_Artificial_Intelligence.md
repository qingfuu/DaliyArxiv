# cs.AI | Artificial Intelligence | 2026-07-31

#arxiv #ComputerScience

**论文数**: 51

### [[20_Research/Papers/强化学习/PAC-MAN_Perception-Aware_CBF-RL_for_Whole-Body_Safety_in_Humanoid_Dodgeball|PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball]]

![[assets/2607.28623_figure.png|800]]

- **arXiv**: [2607.28623](https://arxiv.org/abs/2607.28623)
- **PDF**: https://arxiv.org/pdf/2607.28623
- **详细分析**: [[20_Research/Papers/强化学习/PAC-MAN_Perception-Aware_CBF-RL_for_Whole-Body_Safety_in_Humanoid_Dodgeball|PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball]]
- **作者**: Lizhi Yang, Junheng Li, Aaron D. Ames
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CBF-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present PAC-MAN, a perception-aware CBF-RL framework that couples control-barrier safety with deployment-realistic onboard sensing for whole-body humanoid dodgeball. The deployed policy sees the ball only as segmentation-masked depth from a head-mounted camera, while training-time CBF guidance represents clearance to every body link, and an adversarial motion prior regularizes the resulting evasive reflexes. We evaluate on a controlled any-link contact benchmark with seeded throws in two regimes: single throws and a deployment loop in which the robot walks back to its station and recovers between throws. On this benchmark, the policy comes within a few points of a privileged state oracle: a fixed onboard camera alone is adequate for evasion. We find that usable barrier structure depends on perceptual observability: Joint-CBF gives the best performance with accurate ball states, degrades under fixed-camera observations when used only as training guidance, and recovers with a ball-tracking gimbal or privileged runtime filter. We therefore deploy a lightweight Link-CBF policy zero-shot on the Unitree G1 in the real world, where it tolerates imperfect perception, succeeds on 95% of throws, and uses semantic segmentation to dodge different balls.

</details>

---

### [[20_Research/Papers/大模型/AISPA_User-Centric_System_Prompt_Auditing_for_Large_Language_Model_Applications|AISPA: User-Centric System Prompt Auditing for Large Language Model Applications]]

![[assets/2607.28617_figure.png|800]]

- **arXiv**: [2607.28617](https://arxiv.org/abs/2607.28617)
- **PDF**: https://arxiv.org/pdf/2607.28617
- **详细分析**: [[20_Research/Papers/大模型/AISPA_User-Centric_System_Prompt_Auditing_for_Large_Language_Model_Applications|AISPA: User-Centric System Prompt Auditing for Large Language Model Applications]]
- **作者**: Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang, Yipeng Zhao, Chengxuan Qian, Tianwei Wang, Ziheng Zhang, Zhenlong Yuan, Dingcheng Wang, Juncheng Wu...
- **cs 子类**: cs.AI, cs.CL, cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《AISPA: User-Centric System Prompt Auditing for Large Language Model Applications》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems. AISPA examines specific parts of a system prompt and evaluates them along eight dimensions that matter to users. We then use this framework to review 3,249 instructions from system prompts in 88 commercial AI products, classifying each instruction as either protective (of users) or problematic. Our audit surfaces four core findings. First, system prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5. Second, protective instructions are widely adopted but shallow in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy. Third, system prompts have grown steadily longer and more protective of users, suggesting that user protection is becoming a more visible concern in commercial prompt design. Fourth, despite this progress, problematic instructions remain pervasive: roughly 40% of products contain at least one instruction that works against user interests, and protective and problematic instructions frequently coexist within the same prompt. Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.

</details>

---

### [[20_Research/Papers/强化学习/OSReward_Instituting_Standardized_Evaluation_for_Cross-Platform_Computer-Use_Reward_Models|OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models]]

![[assets/2607.28609_figure.png|800]]

- **arXiv**: [2607.28609](https://arxiv.org/abs/2607.28609)
- **PDF**: https://arxiv.org/pdf/2607.28609
- **详细分析**: [[20_Research/Papers/强化学习/OSReward_Instituting_Standardized_Evaluation_for_Cross-Platform_Computer-Use_Reward_Models|OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models]]
- **作者**: Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li...
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.65（加权：大模型 0.45，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

</details>

---

### [[20_Research/Papers/大模型/DualG-MRAG_Decoupling_Macro-Reasoning_and_Micro-Matching_for_Multimodal_Retrieval-Augmented_Generation|DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation]]

![[assets/2607.28580_figure.png|800]]

- **arXiv**: [2607.28580](https://arxiv.org/abs/2607.28580)
- **PDF**: https://arxiv.org/pdf/2607.28580
- **详细分析**: [[20_Research/Papers/大模型/DualG-MRAG_Decoupling_Macro-Reasoning_and_Micro-Matching_for_Multimodal_Retrieval-Augmented_Generation|DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation]]
- **作者**: Jiacheng Tao, Qingyun Sun, Haonan Yuan, Ziwei Zhang, Jianxin Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal

#### 研究背景与动机

《DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MMQA, MultiModalQA, ScienceQA, WebQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instance-level matching, which often fails to capture explicit relationships across modalities and documents. Although Graph-enhanced methods introduce structural modeling, they face a fundamental challenge in multimodal scenarios: incorporating fine-grained visual features leads to rapid graph expansion and retrieval noise, whereas coarse-grained representations cause the discarding of critical local evidence. To address this dilemma, we propose DualG-MRAG, a Dual-tier framework that introduces a decoupled architecture comprising Macro-reasoning and Micro-matching Graphs for Multimodal RAG. Specifically, to suppress retrieval noise by isolating global structural reasoning from fine-grained evidence matching, we construct a Macro Graph for global topological routing and a Micro Graph for precise local verification. Subsequently, to enable dynamic relevance propagation across heterogeneous evidence sources, we formulate retrieval as a query-driven message passing process via a GNN Retriever. Furthermore, to provide the generative model with coherent structural guidance, we introduce a dynamic programming decoding mechanism that extracts explicit reasoning paths directly from the GNN's forward pass, replacing the standard input of isolated document chunks. Extensive experiments demonstrate that DualG-MRAG outperforms baselines in both evidence recall and complex QA accuracy.

</details>

---

### [[20_Research/Papers/强化学习/APO_Unsupervised_Atomic_Policy_Optimization_for_3D_Structure_Prediction_of_Atomic_Systems|APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of Atomic Systems]]

![[assets/2607.28553_figure.png|800]]

- **arXiv**: [2607.28553](https://arxiv.org/abs/2607.28553)
- **PDF**: https://arxiv.org/pdf/2607.28553
- **详细分析**: [[20_Research/Papers/强化学习/APO_Unsupervised_Atomic_Policy_Optimization_for_3D_Structure_Prediction_of_Atomic_Systems|APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of Atomic Systems]]
- **作者**: Shentong Mo, Yatao Bian
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of Atomic Systems》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting the 3D structures of atomic systems is fundamental to advancing material science and drug discovery. While flow-matching models (, FlowDPO) have recently shown promise in this domain, their performance relies heavily on alignment with ground-truth coordinates via supervised preference learning. However, obtaining experimental labels for novel crystal phases or de novo proteins is prohibitively expensive, creating a bottleneck for structural modeling in data-scarce regimes. In this work, we propose (Atomic Policy Optimization), a fully unsupervised alignment framework that eliminates the need for ground-truth reference structures. APO adapts group-relative policy optimization to 3D atomic environments, utilizing a novel dual-reward mechanism: (i) a that reinforces the policy's dominant latent structural modes through eigen-decomposition of sample similarities, and (ii) a that enforces thermodynamic stability. Our framework enables the model to ``self-correct'' by identifying physically plausible configurations within sampled groups. Extensive benchmarks on crystal and antibody structure prediction demonstrate that APO consistently outperforms fully supervised baselines, achieving a new state-of-the-art in match rates and structural fidelity. Furthermore, we show that APO effectively straightens probability paths, significantly improving inference efficiency. Our results suggest that intrinsic physical consistency can serve as a superior guide for alignment compared to noisy, supervised coordinate matching.

</details>

---

### [[20_Research/Papers/大模型/ORCA-bench_How_Ready_Are_Language_Model_Agents_for_Oncall|ORCA-bench: How Ready Are Language Model Agents for Oncall?]]

![[assets/2607.28545_figure.png|800]]

- **arXiv**: [2607.28545](https://arxiv.org/abs/2607.28545)
- **PDF**: https://arxiv.org/pdf/2607.28545
- **详细分析**: [[20_Research/Papers/大模型/ORCA-bench_How_Ready_Are_Language_Model_Agents_for_Oncall|ORCA-bench: How Ready Are Language Model Agents for Oncall?]]
- **作者**: Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《ORCA-bench: How Ready Are Language Model Agents for Oncall?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ITBench, SREGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and OpenSearch via Grafana) and full source-code access--with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's $κ_w=0.90$). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard--a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Crucially, these are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a system whose code and instrumentation are public. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.

</details>

---

### [[20_Research/Papers/大模型/MANTA_Multi-Agent_Network_Topology_Adaptation_for_Self-Evolving_Multi-Agent_Systems|MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems]]

![[assets/2607.28527_figure.png|800]]

- **arXiv**: [2607.28527](https://arxiv.org/abs/2607.28527)
- **PDF**: https://arxiv.org/pdf/2607.28527
- **详细分析**: [[20_Research/Papers/大模型/MANTA_Multi-Agent_Network_Topology_Adaptation_for_Self-Evolving_Multi-Agent_Systems|MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems]]
- **作者**: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Open-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

</details>

---

### [[20_Research/Papers/强化学习/SVR_Self-Verifying_Refinement_via_Joint_Verdict-Confidence_Reinforcement_Learning_for_Adaptive_Test-Time_Compute|SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute]]

![[assets/2607.28457_figure.png|800]]

- **arXiv**: [2607.28457](https://arxiv.org/abs/2607.28457)
- **PDF**: https://arxiv.org/pdf/2607.28457
- **详细分析**: [[20_Research/Papers/强化学习/SVR_Self-Verifying_Refinement_via_Joint_Verdict-Confidence_Reinforcement_Learning_for_Adaptive_Test-Time_Compute|SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute]]
- **作者**: Hongyu Chen, Liang Lin, Guangrun Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement Learning for Adaptive Test-Time Compute》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：C3RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling test-time computation can improve language-model reasoning, but uniform budgets waste computation on easy inputs, while verifier-guided refinement relies on external feedback. We introduce Self-Verifying Refinement (SVR), an oracle-free multi-turn reinforcement learning framework that learns to use self-verification as a compute-control policy. At each turn, the model produces a solution together with a discrete correctness verdict and a confidence score; it retains the current answer only when the verdict is Correct and confidence exceeds a threshold, and otherwise continues refinement using its own self-verification. Ground-truth correctness is used only to construct training rewards and is never exposed to the policy through refinement prompts or required at inference. SVR is trained with GRPO on fixed-horizon trajectories using rewards that promote solution correctness, calibration-aware self-verification, and stop-ready correct states; adaptive stopping is activated only at inference. On seven mathematical reasoning benchmarks with Qwen3.5-2B, SVR achieves a macro-average accuracy of 0.563 with only 2.99 inference turns on average. In the evaluated complete-system comparison, it exceeds standard GRPO, strong multi-turn baselines, and a fixed-budget oracle-guided score-feedback reference while requiring substantially fewer turns than fixed ten-turn inference. These results demonstrate that learned self-verification can serve as an effective internal control signal for answer retention and adaptive test-time compute allocation.

</details>

---

### [[20_Research/Papers/机器人/Machines_that_know_they_are_aging_a_framework_for_hardware-aware_autonomous_intelligence|Machines that know they are aging: a framework for hardware-aware autonomous intelligence]]

![[assets/2607.28451_figure.png|800]]

- **arXiv**: [2607.28451](https://arxiv.org/abs/2607.28451)
- **PDF**: https://arxiv.org/pdf/2607.28451
- **详细分析**: [[20_Research/Papers/机器人/Machines_that_know_they_are_aging_a_framework_for_hardware-aware_autonomous_intelligence|Machines that know they are aging: a framework for hardware-aware autonomous intelligence]]
- **作者**: Cheng Siong Chin, Jianhua Zhang, Mohan Venkateshkumar
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Machines that know they are aging: a framework for hardware-aware autonomous intelligence》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems inevitably age, yet their artificial intelligence typically assumes hardware remains in its original condition. Batteries degrade, sensors drift, processors accumulate timing errors, and memory reliability declines, creating a growing mismatch between assumed and actual capability. This can lead to agnostic collapse, where mission failure arises from accumulated hardware degradation rather than a single component fault. We propose Aging-Aware Autonomous Intelligence (AAAI), a framework that integrates hardware health directly into reasoning, planning, and mission execution. AAAI is built on three pillars: hardware self-awareness, which continuously estimates the health of power, sensing, memory, and computation subsystems using physics-of-failure models; self-adaptive reasoning, which adjusts inference complexity, planning horizon, and task priorities according to remaining hardware capability; and survival-centric intelligence, which allocates remaining operational life across mission objectives through performance optimization, resource conservation, and graceful degradation. Rather than introducing new hardware, AAAI unifies prognostics, lifecycle management, and hardware-aware computing into a closed-loop cognitive architecture. We argue that such integration is essential for autonomous systems operating in inaccessible or safety-critical environments, including space missions, marine robotics, and implantable medical devices. By enabling machines to recognize and respond to their own aging, AAAI improves resilience, extends operational lifetime, and supports safer, more graceful mission completion.

</details>

---

### [[20_Research/Papers/大模型/When_Derived_Measurements_Mislead_Quantifying_and_Mitigating_LLM_Over-Trust_with_Privileged-Modality_Reliability_Evidence|When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence]]

![[assets/2607.28421_figure.png|800]]

- **arXiv**: [2607.28421](https://arxiv.org/abs/2607.28421)
- **PDF**: https://arxiv.org/pdf/2607.28421
- **详细分析**: [[20_Research/Papers/大模型/When_Derived_Measurements_Mislead_Quantifying_and_Mitigating_LLM_Over-Trust_with_Privileged-Modality_Reliability_Evidence|When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence]]
- **作者**: Zongheng Guo, Tao Chen, Tianli Li, Mingzhe Cui, Yang Jiao, Lei Xie, Yi Pan, Xiao Hu, Manuela Ferrario
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Derived measurements increasingly enter large language model (LLM) pipelines as direct facts despite their instance-dependent validity. We define derived-feature over-trust (DFOT) as the failure in which a downstream LLM assigns such a measurement the epistemic status of a direct fact or uses it outside its valid scope. Using physiological sensing as a case study, D1 tests acceptance of a PPG-derived rhythm contradicted by offline ECG, whereas D2 tests rejection of an offline-confirmed reliable PPG rhythm under misleading severe history. ECG supplies training supervision and offline reference construction but is never shown to the LLM. Five estimands quantify this chain: conflict over-trust rate (COTR) and context-induced error rate (CIR) characterize D1/D2; correct repair rate (CRR) measures frozen-error repair; evidence-specific repair margin (ESRM) contrasts matched and patient-disjoint shuffled evidence; and utility harm rate (UHR) measures unnecessary verification among HIGH-reliability cases used without verification at baseline. The framework does not depend on a particular reliability generator. We demonstrate it on 50,000 paired PPG-ECG records using ECG-to-PPG privileged distillation as an illustrative baseline and PPG-only inference. On a protocol-locked 187-patient test, the baseline improves four repair and specificity endpoints by 1.82-6.69 percentage points, with all paired confidence intervals excluding zero; UHR increases by 0.67 percentage points (95% CI: -0.4 to +1.7). DFOT provides a common evaluation target for stronger mitigation methods. The code is available at https://github.com/Zongheng-Guo/When-Derived-Measurements-Mislead.

</details>

---

### [[20_Research/Papers/世界模型/QQWorld_Quantile-Quantile_Matching_for_World_Model_Regularization|QQWorld: Quantile-Quantile Matching for World Model Regularization]]

![[assets/2607.28415_first_page.png|800]]

- **arXiv**: [2607.28415](https://arxiv.org/abs/2607.28415)
- **PDF**: https://arxiv.org/pdf/2607.28415
- **详细分析**: [[20_Research/Papers/世界模型/QQWorld_Quantile-Quantile_Matching_for_World_Model_Regularization|QQWorld: Quantile-Quantile Matching for World Model Regularization]]
- **作者**: Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《QQWorld: Quantile-Quantile Matching for World Model Regularization》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：QQWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models enable efficient planning by predicting future states in a compact representation space, but their performance depends critically on the quality of the learned latent distribution. LeWorldModel (LeWM) regularizes its latents toward an isotropic Gaussian using the Epps-Pulley (EP) objective. We show that the corrective gradients of EP rapidly vanish for isolated tail samples, leaving heavy-tailed deviations insufficiently controlled. To address this limitation, we propose QQWorld, which replaces EP with a quantile-quantile matching objective that directly aligns projected latent samples with rank-matched Gaussian quantiles, thereby maintaining effective corrective gradients in the tails. We further develop cross-batch QQ, which enlarges the effective ranking pool using detached samples from previous batches, and characterize its bias-variance trade-off. Across four control environments, QQWorld effectively improves the average planning success rate of LeWM, while consistently yielding better Gaussian alignment and thinner latent tails.

</details>

---

### [[20_Research/Papers/大模型/GLM-RAG_Graph_Language_Models_for_Graph-Based_Retrieval-Augmented_Generation|GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation]]

![[assets/2607.28397_figure.png|800]]

- **arXiv**: [2607.28397](https://arxiv.org/abs/2607.28397)
- **PDF**: https://arxiv.org/pdf/2607.28397
- **详细分析**: [[20_Research/Papers/大模型/GLM-RAG_Graph_Language_Models_for_Graph-Based_Retrieval-Augmented_Generation|GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation]]
- **作者**: Maya Arseven, Anette Frank, Beni Egressy, Johann Higl, Moritz Plenz
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Systems

#### 研究背景与动机

《GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) over knowledge graphs requires retrievers that can effectively capture both graph structure and semantic information. Recent approaches have explored graph neural network (GNN)-based retrievers to model graph topology in multi-hop reasoning tasks. In parallel, graph language models (GLMs) have emerged as a promising paradigm that integrates graph reasoning and the semantic capabilities of language models. In this work, we introduce a GLM-based retriever and investigate the comparative strengths of GLM-based, GNN-based, and traditional vector-search-based retrievers in single- and multi-hop RAG settings, and with a particular focus on transferability to unseen domains. Our findings suggest that finetuned GLM retrievers generalize better out of domain, achieving SOTA on two multi-hop benchmarks. On in-domain multi-hop QA datasets they remain comparable to prior work, with promising scaling as parameters and subgraph coverage increase. GNN-based retrievers achieve higher graph coverage with an efficient training setup, whereas the vector-search baseline excels at single-hop datasets.

</details>

---

### [[20_Research/Papers/世界模型/ShadowDancer_Teaching_Video_World_Models_Any_Action_by_Learning_Unified_Dynamics_Representations_from_a_Video_and_Its_Shadow|ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow]]

![[assets/2607.28362_figure.png|800]]

- **arXiv**: [2607.28362](https://arxiv.org/abs/2607.28362)
- **PDF**: https://arxiv.org/pdf/2607.28362
- **详细分析**: [[20_Research/Papers/世界模型/ShadowDancer_Teaching_Video_World_Models_Any_Action_by_Learning_Unified_Dynamics_Representations_from_a_Video_and_Its_Shadow|ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow]]
- **作者**: Jin Cao, Zian Meng, Kaipeng Zhang
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ShadowDancer, a novel approach to any-action, frame-level control of interactive video world models. The obstacle is representational: existing interfaces either encode an action loosely, leaving how it unfolds for the model to improvise, or encode it exactly through structured signals that serve one family and are hard to acquire, so precise control across diverse dynamics remains impractical. Demonstration videos are the natural remedy, specifying any dynamics frame by frame; yet a video shows its dynamics only through one particular appearance, a single shadow of the underlying dynamics, so actions learned from demonstrations transfer poorly to new scenes. ShadowDancer addresses this with two key innovations: (1) shadow pairs, video pairs that replay the same dynamics under independently resampled appearance, constructed at scale by our Shadow Library, so that a dynamics family becomes controllable exactly when such pairs can be constructed for it; and (2) cross-shadow prediction, which learns actions by predicting one shadow from the other, so that whatever the pairing resamples is discarded by construction and whatever it preserves becomes the action, yielding a unified dynamics representation that drives a block-causal world model. Any demonstrated clip thus becomes a reusable action asset, replayed in new environments without action labels, motion estimators, or fine-tuning. Experiments demonstrate improved action transfer and long action rollout over strong latent-action and interactive world model baselines across diverse dynamics families, with an average blinded win rate of 86% in rollout comparisons. We show video results at https://ShadowDancer-1.github.io

</details>

---

### [[20_Research/Papers/大模型/Paying_for_Honesty_Without_Knowing_the_Truth_Reputation-Penalty_Design_for_LLM_Marketplace_Agents|Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents]]

![[assets/2607.28330_figure.png|800]]

- **arXiv**: [2607.28330](https://arxiv.org/abs/2607.28330)
- **PDF**: https://arxiv.org/pdf/2607.28330
- **详细分析**: [[20_Research/Papers/大模型/Paying_for_Honesty_Without_Knowing_the_Truth_Reputation-Penalty_Design_for_LLM_Marketplace_Agents|Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents]]
- **作者**: Mingdai Yang, Shicheng Fan, Kejing Yu, Duohao Wang, Li Sun, Hao Peng, Philip S. Yu, Zhiwei Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly act as autonomous merchants that write their own product listings, and under competitive pressure, they fabricate attributes to win sales. Even under instructions to be honest, they fabricate attributes in a majority of listings across models. A platform's obvious remedy---verifying each claim against the truth---is unavailable, because it observes only a noisy, biased complaint signal, never the ground truth. We design CARP, a reputation-penalty mechanism with a deadband that forgives complaint noise and a state-dependent severity that counters reputation-driven detection erosion. CARP requires no product-level ground truth and is robust to strategic gaming. CARP protects consumers by suppressing the sales volume of low-rated liars while sparing honest sellers. Paired with SPARC, it closes most of the consumer-welfare gap relative to a perfect-information oracle, without ever accessing the truth. It also achieves the best welfare of the policies we compare. We further show that this felt penalty becomes behaviorally binding through SPARC, a byte-clean code-gated reflection mechanism: LLM merchants fabricate when lying is free but restrain themselves when fabrication costs them sales, a self-interested response rather than compliance. We trace this distinction to penalty-gated self-correction reasoning, and observe the binding across models, with supporting confidence intervals.

</details>

---

### [[20_Research/Papers/大模型/One_Human,_$N$_Agents_Audit-Budget_Allocation_for_LLM_Agent_Fleets_under_Miscalibrated,_Correlated_Confidence|One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence]]

![[assets/2607.28317_figure.png|800]]

- **arXiv**: [2607.28317](https://arxiv.org/abs/2607.28317)
- **PDF**: https://arxiv.org/pdf/2607.28317
- **详细分析**: [[20_Research/Papers/大模型/One_Human,_$N$_Agents_Audit-Budget_Allocation_for_LLM_Agent_Fleets_under_Miscalibrated,_Correlated_Confidence|One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence]]
- **作者**: Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A single human must audit $N$ LLM agents under a budget of $B \ll N$ audits per round, guided by self-reported confidence that may be adversarially miscalibrated and by correlated errors. We model this as budgeted noisy inspection over a two-level Gaussian copula and locate the miscalibration threshold $δ^*$ past which confidence-ranked auditing is \emph{worse} than random. Two a-priori expectations reverse: $δ^*$ \emph{rises} as the budget shrinks, and cross-family correlation is not low---shared difficulty dominates lineage. Five open-weight LLMs show operationally useless (near-constant) confidence, point estimates at or beyond the flip though CIs straddle it; a proprietary model is informative and lands below it. We give a quantitative criterion for \emph{vacuous} oversight, and replaying policies on recorded traces confirms the ordering.

</details>

---

### [[20_Research/Papers/强化学习/Tycho_Active_Abstraction_with_Programmatic_World_Models_for_ARC-AGI-3|Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3]]

![[assets/2607.28287_figure.png|800]]

- **arXiv**: [2607.28287](https://arxiv.org/abs/2607.28287)
- **PDF**: https://arxiv.org/pdf/2607.28287
- **详细分析**: [[20_Research/Papers/强化学习/Tycho_Active_Abstraction_with_Programmatic_World_Models_for_ARC-AGI-3|Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3]]
- **作者**: Jens Lehmann, Andrei Aioanei, Sahar Vahdati
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.7（加权：大模型 0.1，世界模型 0.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OPINE-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

ARC-AGI-3 turns abstraction into an interactive problem of skill acquisition. A player must infer an unfamiliar game's rules, hidden state, and goal while maintaining action efficiency because every move counts. We formalize these environments as parameterized rendered deterministic Moore machines and introduce Tycho, a coding-agent system that constructs and uses game-specific models during interaction. Tycho separates actionable observations from intermediate animation, level-completion, and game-over frames. From this structured history, an agent can model, test, plan with, repair, or bypass a free-form executable hypothesis. In one matched public-set run per policy, we compare four orchestration policies on all 25 public games using Claude Opus 4.8 under matched inference budgets. Actor-requested delegation to a model builder obtains the highest observed mean Relative Human Action Efficiency (RHAE), 88.49. With this selected policy, GPT-5.6 Sol and Opus 5 both reach 100.00 RHAE and complete all 183 levels. Their game-balanced first-run human-replay midranks are 98.5 and 100.0. Opus 5 uses 61% fewer scored actions than the aggregate official human baselines. Automatic repair after verification failures produces models that reproduce observed transitions much more accurately, yet reaches only 83.07 RHAE. Transition match indicates whether a simulator reproduces observed dynamics, not whether it has identified the objective or improves the next action. Strong play also requires deciding when to construct, repair, use, or bypass a model. We call this joint problem active abstraction: generating a testable model from costly interaction and deciding when acquiring or using it is worth its cost.

</details>

---

### [[20_Research/Papers/具身智能/EgoGenesis_Egocentric_World-Action_Modeling_with_Online_Anchored_Projective_Memory_and_Action-3D_RoPE|EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE]]

![[assets/2607.28243_figure.png|800]]

- **arXiv**: [2607.28243](https://arxiv.org/abs/2607.28243)
- **PDF**: https://arxiv.org/pdf/2607.28243
- **详细分析**: [[20_Research/Papers/具身智能/EgoGenesis_Egocentric_World-Action_Modeling_with_Online_Anchored_Projective_Memory_and_Action-3D_RoPE|EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE]]
- **作者**: Zexuan Yan, Yuzhou Wu, Yue Ma, Zonghang He, Kaibo Yin, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Shijian Wang, Jinghong Liu, Linfeng Zhang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EgoSim, RynnWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric video offers rich manipulation experience for embodied AI, yet collecting diverse egocentric data across scenes, objects, motions, and embodiments remains costly. We present \method, an egocentric world-action simulator that synthesizes controllable, high-quality manipulation videos to expand scarce real-world training data. \method{} builds on a pretrained video generation prior and introduces two geometry-aware conditioning mechanisms. Online Anchored Projective Memory (OAPM) preserves a first-frame 3D scene anchor while periodically refreshing a recent state during autoregressive generation. Action-3D Rotary Position Embedding (A3D-RoPE) encodes end-effector motion with camera-aware 3D rotary coordinates, injecting action geometry into skeleton-to-video cross-attention for precise control. Together, these components improve visual fidelity, geometric stability, and action alignment in long egocentric rollouts. Moreover, augmenting 400 real trajectories with 400 \method-generated trajectories improves out-of-distribution real-robot success from 77\% to 84\% on single-arm tasks and from 53\% to 70\% on dual-arm tasks, demonstrating that the synthesized data substantially improve downstream WAM generalization.

</details>

---

### [[20_Research/Papers/大模型/EMBL_AI_Librarian_Life-Sciences_Knowledge_Layer_for_AI_Agents|EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents]]

![[assets/2607.28229_first_page.png|800]]

- **arXiv**: [2607.28229](https://arxiv.org/abs/2607.28229)
- **PDF**: https://arxiv.org/pdf/2607.28229
- **详细分析**: [[20_Research/Papers/大模型/EMBL_AI_Librarian_Life-Sciences_Knowledge_Layer_for_AI_Agents|EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents]]
- **作者**: Luigi Sigillo, Matteo Silvestri, Francesco Tabaro, Rajat Bhatnagar, Syed Irtaza Mubashar, Matt Jeffryes, Daljit Nijjer, Vittorio Perera, Ola Spjuth, Julio Saez-Rodriguez, Melissa Harrison, Fabio Petroni
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScholarQABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The web is increasingly accessed by AI agents rather than humans. Every agent needs knowledge, especially in the life-sciences, where agentic pipelines are growing fast. Access to the literature is a crucial part of that need, and resources such as Europe PMC, with over 40M indexed records, are widely used to meet it. Yet these resources were not built for AI agents: they take keywords and complex syntax and return whole papers, so every agent must learn the syntax, issue several searches, and read full papers to find the evidence it needs. We introduce EMBL AI Librarian, a knowledge layer that upgrades the Europe PMC interface for AI agents: an agent asks in natural language and receives evidence that answers it. A single LLM orchestrates the whole knowledge retrieval process: it plans complementary subqueries executed by the live Europe PMC search engine, then reads the selected papers and locates the relevant evidence. We evaluate Librarian across four benchmarks: literature synthesis, claim verification, open-domain question answering, and downstream biology tasks such as protocol questions and sequence manipulation. On ScholarQABench, Librarian improves Citation F1 by more than $16$ points over strong recently published baselines. Used as the retrieval layer of an existing claim-verification pipeline, it increases agreement with expert consensus; and on the open-form LitQA2 benchmark, a GPT-5.4 agent scores about $8$ points higher when grounded in Librarian than with web search. Overall, our results show that equipping life-science agents with the Librarian knowledge layer improves performance across a range of tasks. We release our code publicly at https://github.com/petroni-lab/librarian

</details>

---

### [[20_Research/Papers/强化学习/Qwen-UI-Agent_Technical_Report_Toward_Next-Generation_Real-World_Centric_Foundation_GUI_Agents|Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents]]

![[assets/2607.28227_figure.png|800]]

- **arXiv**: [2607.28227](https://arxiv.org/abs/2607.28227)
- **PDF**: https://arxiv.org/pdf/2607.28227
- **详细分析**: [[20_Research/Papers/强化学习/Qwen-UI-Agent_Technical_Report_Toward_Next-Generation_Real-World_Centric_Foundation_GUI_Agents|Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents]]
- **作者**: Hanzhang Zhou, Panrong Tong, Xu Zhang, Quyu Kong, Chenglin Cai, Tianyu Xia, Gongjie Zhang, Jianan Zhang, Long Li, Long Chen, Lei Wang, Gaole Dai...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Claw-Eval, MMBench, MobileWorld, OSWorld, Real-World, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

GUI agents have the potential to become a general purpose executor over existing digital devices. To advance them toward real-world use, we envision agents that operate reliably on real devices, execute workflows across platforms, combine GUI interaction with CLI execution, complete long-horizon tasks, proactively initiate useful services, and autonomously improve their capabilities with minimal human effort. Guided by this vision, we present Qwen-UI-Agent, a real-world centric foundation GUI agent spanning mobile, computer-use, web, and DeepSearch environments. Qwen-UI-Agent combines diverse sandbox environments with a large-scale real-device mobile runtime. Its unified action space interleaves GUI operations with CLI execution and generates batched actions in a single model turn. An AutoResearch-style data flywheel uses agents to construct tasks and environments, diagnose failures, and plan subsequent iterations. Online RL supports training on trajectories exceeding 100 turns, with over 10,000 concurrent environments accelerating rollout. A lightweight harness layer supports proactive service initiation and stateful workflows across mobile and computer. Across a broad suite of evaluations, Qwen-UI-Agent sets state-of-the-art performance on mobile-use benchmarks while delivering competitive performance on computer- and browser-use tasks against frontier models, including Opus 4.8, Gemini 3.1 Pro, and GPT-5.6 Sol. On mobile use, it achieves 82.1% on MobileWorld, 92.2% on MobileWorld-Real, and 97.5% on AndroidDaily. On computer use, it achieves 79.5% on OSWorld-Verified and a 40.0% partial-progress score on OSWorld-v2. On browser use and GUI grounding, it achieves 73.6% on WebArena and 81.5% on ScreenSpot-Pro, respectively.

</details>

---

### [[20_Research/Papers/具身智能/Security_of_World-Model-Based_Embodied_AI_A_Lifecycle_of_Threats,_Defenses,_and_Evaluation|Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation]]

![[assets/2607.28226_figure.png|800]]

- **arXiv**: [2607.28226](https://arxiv.org/abs/2607.28226)
- **PDF**: https://arxiv.org/pdf/2607.28226
- **详细分析**: [[20_Research/Papers/具身智能/Security_of_World-Model-Based_Embodied_AI_A_Lifecycle_of_Threats,_Defenses,_and_Evaluation|Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation]]
- **作者**: Fazhong Liu, Zhuoyan Chen, Haozhen Tan, Yan Meng, Guoxing Chen, Haojin Zhu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 2.6（加权：具身智能 2.4，世界模型 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation》归入 具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HY-World, OpenVLA, PlaNet, UrbanWorld, WebWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models give embodied AI a predictive core: they compress observations into states, simulate action-conditioned futures, and enable planning beyond reactive control. This predictive layer, however, opens a new security boundary-compromise can propagate from data, sensors, prompts, or feedback into physical action. Rather than treating world models as an isolated component, this survey traces threats across their entire lifecycle-from data construction and representation learning, through state grounding and imagination, to trajectory evaluation, execution, and long-term adaptation via memory and tools. We show that familiar attack families: poisoning, backdoors, adversarial examples, sensor spoofing, prompt injection, trajectory manipulation, and supply-chain attacks take on distinct meanings when they corrupt world states, learned dynamics, affordance estimates, or safety costs. We also highlight a duality: world models can serve as runtime safety shields, yet when compromised or over-trusted they generate predictive safety illusions. The survey offers a lifecycle taxonomy, maps existing attacks to world-model security properties, outlines evaluation protocols for safety failures, and structures defenses across provenance, robust grounding, uncertainty-aware prediction, trajectory gating, feedback auditing, and deployment assurance.

</details>

---

### [[20_Research/Papers/大模型/Vibe-FDTR_An_agent-oriented_framework_for_reproducible_frequency-domain_thermoreflectance_data_analysis|Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis]]

![[assets/2607.28200_first_page.png|800]]

- **arXiv**: [2607.28200](https://arxiv.org/abs/2607.28200)
- **PDF**: https://arxiv.org/pdf/2607.28200
- **详细分析**: [[20_Research/Papers/大模型/Vibe-FDTR_An_agent-oriented_framework_for_reproducible_frequency-domain_thermoreflectance_data_analysis|Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis]]
- **作者**: Fuwei Yang, Weiheng Li, Bai Song
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Vibe-FDTR: An agent-oriented framework for reproducible frequency-domain thermoreflectance data analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frequency-domain thermoreflectance (FDTR) is a laser pump-probe technique widely used to measure thermal properties at the micro- and nanoscale; however, it relies on a complex data analysis procedure that demands substantial domain expertise and is susceptible to subtle human errors. Here, we present Vibe-FDTR, an agent-oriented framework that enables large language model (LLM) agents to perform reliable and reproducible FDTR analyses directly from natural language requests. This framework couples a configuration-driven FDTR code package, which enforces physical and parametric consistency, with procedural agent skills that translate user intentions into organized and verifiable analysis steps. We evaluate Vibe-FDTR using a controlled benchmark with two levels: synthetic single-step tasks and real-data multi-step tasks based on measurements of gold-coated graphite samples. Across the two levels, agents using Vibe-FDTR achieve success rates of 100% and 98.9%, respectively. In sharp contrast, ablating skills (Code-agent) reduces performance to 91.4% and 36.7%, which drops further to 38.6% and 0% when the domain package is also omitted (Agent-only). Beyond success rate, Vibe-FDTR also reduces computational cost by 87.7% relative to the Code-agent variant and cuts execution time by more than 60%. Finally, an optional expert mode supports experimental planning via autonomous sensitivity and uncertainty evaluations, and formulates physically grounded recommendations for underspecified tasks. These results demonstrate that encapsulating domain code and expert knowledge into agent skills offers a promising route toward low-barrier, autonomous, and trustworthy thermal metrology.

</details>

---

### [[20_Research/Papers/大模型/MIND_Lightweight_and_Effective_Memory_Injection_Defense_for_LLM_Agents_via_Intent-Aware_Information_Bottleneck|MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck]]

![[assets/2607.28103_figure.png|800]]

- **arXiv**: [2607.28103](https://arxiv.org/abs/2607.28103)
- **PDF**: https://arxiv.org/pdf/2607.28103
- **详细分析**: [[20_Research/Papers/大模型/MIND_Lightweight_and_Effective_Memory_Injection_Defense_for_LLM_Agents_via_Intent-Aware_Information_Bottleneck|MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck]]
- **作者**: Dongyi Liu, Haixing He, Xiaobao Wu, Jia Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ReAct-StrategyQA, StrategyQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising(MIND), a lightweight defense framework for memory injection attack. Our preliminary analysis reveals that benign and poisoned trajectories exhibit distinguishable relationships between the initial user intent and subsequent behavior. Building on this observation, MIND employs an intent-aware Information Bottleneck(IB) to extract compact intent--behavior representations from the initial intent and turn-level behavior. The IB preserves intent-relevant cross-turn attack signals while filtering task-irrelevant and repetitive information, and a lightweight detector identifies malicious memories from the resulting representations. As such, MIND mitigates information redundancy in multi-turn contexts while avoiding the overhead of repeated LLM auditing. Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency. Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.

</details>

---

### [[20_Research/Papers/大模型/Group-Reflective_Self-Distillation_for_Agentic_Reinforcement_Learning|Group-Reflective Self-Distillation for Agentic Reinforcement Learning]]

![[assets/2607.28076_figure.png|800]]

- **arXiv**: [2607.28076](https://arxiv.org/abs/2607.28076)
- **PDF**: https://arxiv.org/pdf/2607.28076
- **详细分析**: [[20_Research/Papers/大模型/Group-Reflective_Self-Distillation_for_Agentic_Reinforcement_Learning|Group-Reflective Self-Distillation for Agentic Reinforcement Learning]]
- **作者**: Binbin Zheng, Zijun Xie, Guanqun Zhao, Enlei Gong, Xing Ma, Xiaoliang Fu, Zeyu Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Group-Reflective Self-Distillation for Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) is effective for training large language model agents. However, terminal rewards provide only coarse trajectory-level supervision, leaving successful behaviors, recurring mistakes, and incidental choices entangled in the same outcome signal. Existing agentic self-distillation methods enrich sparse supervision with natural-language skills, but skills retrieved externally or extracted from a single trajectory by stronger models may mismatch current experience, exceed the policy's capability, or remain path-specific. We propose Group-Reflective Self-Distillation (GRSD), which derives capability-aligned and outcome-discriminative guidance from the policy's own verified rollouts. For each prompt, the policy reflects on each verified trajectory in an on-policy group, and a stop-gradient snapshot contrasts the resulting reflections from successful and failed rollouts to construct group-level privileged guidance. Conditioned on this guidance, a self-teacher refines turn-level credit assignment by modulating outcome-based advantages while preserving the verifier-determined learning direction. Experiments across multiple agentic environments and model scales demonstrate that GRSD consistently outperforms competitive baselines and generalizes more effectively to unseen tasks.

</details>

---

### [[20_Research/Papers/大模型/IndustryForge-27B_A_Domain-Enhanced_Multimodal_Foundation_Model_for_Industrial_CAD|IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD]]

![[assets/2607.28050_figure.png|800]]

- **arXiv**: [2607.28050](https://arxiv.org/abs/2607.28050)
- **PDF**: https://arxiv.org/pdf/2607.28050
- **详细分析**: [[20_Research/Papers/大模型/IndustryForge-27B_A_Domain-Enhanced_Multimodal_Foundation_Model_for_Industrial_CAD|IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD]]
- **作者**: Nianchen Deng, Jiaxin Ai, Tao Hu, Shu Zou, Yurui Dong, Siqi Li, Xinyu Cai, Xuemeng Yang, Licheng Wen, Hongbin Zhou, Hairong Zhang, Pinlong Cai...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《IndustryForge-27B: A Domain-Enhanced Multimodal Foundation Model for Industrial CAD》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：CAD-VQA, ComCADBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating industrial CAD design and manufacturing places distinctive demands on multimodal foundation models: the model must see engineering drawings and 3D geometry screenshots, write correct parametric-modelling scripts and Windows COM API code, and cover the full range from single parts to assemblies. General-purpose multimodal models fall short on these tasks, while single-task fine-tuning is too narrow to support the diverse calls that upper-layer agents issue. We build IndustryForge-27B on top of Qwen3.5-VL-27B by curating and integrating six industrial-CAD sub-corpora totalling $\sim$52k multimodal samples---CAD Visual QA (CAD-VQA), parametric CAD code (text2cadquery), assembly-level CAD code (text2cadquery-assembly), and three COM sub-corpora for Inventor / SolidWorks (com_2d / com_3d / com_assembly)---and training with a unified multi-task SFT recipe. Across four CAD-domain benchmarks IndustryForge-27B lifts the base model by $+33.65$~pp on average and outperforms the strong closed-source model GPT-5.4 on all four; across eleven general-capability benchmarks it retains, and slightly improves upon, the base model ($+1.56$~pp mean, no catastrophic forgetting). IndustryForge-27B will serve as the common substrate for downstream industrial-agent projects, providing a unified starting point for a full-stack industrial agent that spans from CAD design to industrial-software operation, from parts to assemblies, and from single-shot generation to closed-loop self-improvement.

</details>

---

### [[20_Research/Papers/大模型/SKILL-KD_Contrastive_Skill_Distillation_for_LLM_Agents|SKILL-KD: Contrastive Skill Distillation for LLM Agents]]

![[assets/2607.28048_figure.png|800]]

- **arXiv**: [2607.28048](https://arxiv.org/abs/2607.28048)
- **PDF**: https://arxiv.org/pdf/2607.28048
- **详细分析**: [[20_Research/Papers/大模型/SKILL-KD_Contrastive_Skill_Distillation_for_LLM_Agents|SKILL-KD: Contrastive Skill Distillation for LLM Agents]]
- **作者**: Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SKILL-KD: Contrastive Skill Distillation for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skill-based prompting has become a practical mechanism for improving large language model (LLM) agents, yet existing skill acquisition methods often treat skills as experience summaries, memory entries, or direct summaries of successful demonstrations. This creates a mismatch for weaker student agents: when a student fails because it lacks task knowledge or operational strategy, its failed trajectory may not contain enough evidence to infer the missing behavior, while the teacher trajectory may be too implicit to be internalized as reusable guidance. We propose SKILL-KD, a contrastive skill distillation framework that treats skills as an explicit distillation medium between agents of different capabilities. Given a student failure and the teacher trajectory on the same task, SKILL-KD distills their actionable discrepancy into a textual skill patch, evaluates the patch by re-running the student, and iteratively refines the patch when the student still fails. To prevent repeated local updates from causing skill drift, SKILL-KD further maintains trace-linked edit histories and performs Drift-Aware Skill Consolidation, deciding whether each patch should add a new rule, delete or modify an existing rule, or be skipped. Across five agent benchmarks and two student settings, SKILL-KD consistently improves frozen student agents over fixed-model adaptation baselines.

</details>

---

### [[20_Research/Papers/大模型/MMLDSum-LLM_Multimodal_Long-Document_Summarization_with_Visual-Alignment_and_Keyword-Aware|MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware]]

![[assets/2607.28006_first_page.png|800]]

- **arXiv**: [2607.28006](https://arxiv.org/abs/2607.28006)
- **PDF**: https://arxiv.org/pdf/2607.28006
- **详细分析**: [[20_Research/Papers/大模型/MMLDSum-LLM_Multimodal_Long-Document_Summarization_with_Visual-Alignment_and_Keyword-Aware|MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware]]
- **作者**: Xianpeng Zhang, Jiahua Yang, Dongyu Chen, Lei zhang, Jian Ma, Xu guohuan, Haonan Lu, Tianhuang Su, Chuangchuang Wang, Kai Tang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《MMLDSum-LLM: Multimodal Long-Document Summarization with Visual-Alignment and Keyword-Aware》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MMLDSum-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal long documents are core carriers of professional knowledge, where critical evidence is sparsely distributed across paragraphs and modalities. This easily causes key information omission and cross-modal hallucinations in summarization by multimodal LLMs. These issues stem from attention drift in long-range dependency modeling and gaps in inter-modal alignment. To address this, we introduce MMLDSum-Bench, a high-quality benchmark for multimodal long-document summarization, covering multiple domains, context-length scales, and visual-textual modality distributions. We further propose MMLDSum-LLM, a reproducible two-stage training framework that combines supervised fine-tuning with visual-alignment weighted loss and keyword-aware weighted loss, followed by GRPO with a multi-objective reward (keyword coverage, image-text alignment, ROUGE, and length control). Extensive experiments on MMLDSum-Bench, comparing against leading closed-source and open-source multimodal models under a unified evaluation protocol - including LLM-as-a-judge scoring, atomic-claim precision/recall, image-text alignment (ITA), and ROUGE - demonstrate that our approach significantly improves key-information coverage and cross-modal consistency.

</details>

---

### [[20_Research/Papers/大模型/TAPO_Transition-Aware_Policy_Optimization_for_LLM_Agents|TAPO: Transition-Aware Policy Optimization for LLM Agents]]

![[assets/2607.27973_figure.png|800]]

- **arXiv**: [2607.27973](https://arxiv.org/abs/2607.27973)
- **PDF**: https://arxiv.org/pdf/2607.27973
- **详细分析**: [[20_Research/Papers/大模型/TAPO_Transition-Aware_Policy_Optimization_for_LLM_Agents|TAPO: Transition-Aware Policy Optimization for LLM Agents]]
- **作者**: Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.42（加权：大模型 1.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TAPO: Transition-Aware Policy Optimization for LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on predictive knowledge of environmental consequences. Inspired by this, we propose TAPO: Transition-Aware Policy Optimization for LLM Agents, a unified training framework that alternates between policy optimization and transition supervision. Beyond standard RL updates, TAPO repurposes rollout data to apply action-conditioned next-observation prediction supervision on a shared backbone model. This approach enhances the model's sensitivity to environmental transition dynamics and action consequences while concurrently optimizing the policy. It serves as a computationally lightweight, plug-and-play enhancement module for existing agent RL algorithms, requiring no additional expert data, extra sampling costs, or inference-time overhead. We conduct systematic experiments on WebShop and ALFWorld, integrating foundation models of various scales with different policy optimization algorithms. Empirical results demonstrate that TAPO consistently improves task performance over pure policy optimization baselines.

</details>

---

### [[20_Research/Papers/具身智能/MARS-RA_Rank_Aggregation_for_Credit_Assignment_via_Multimodal_Comparisons_in_Embodied_Multi-Agent_Cooperation|MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation]]

![[assets/2607.27967_figure.jpg|800]]

- **arXiv**: [2607.27967](https://arxiv.org/abs/2607.27967)
- **PDF**: https://arxiv.org/pdf/2607.27967
- **详细分析**: [[20_Research/Papers/具身智能/MARS-RA_Rank_Aggregation_for_Credit_Assignment_via_Multimodal_Comparisons_in_Embodied_Multi-Agent_Cooperation|MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation]]
- **作者**: Dawei Wang, Di Zhao, Xinyuan Liu, Marci Chi Ma, Xiaoyang Liu, Chengming Zhou, Gary Ushaw, Richard Davison
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.9，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《MARS-RA: Rank Aggregation for Credit Assignment via Multimodal Comparisons in Embodied Multi-Agent Cooperation》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL, MARS-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Credit assignment is a fundamental challenge in cooperative multi-agent reinforcement learning, particularly in embodied AI settings characterized by limited and delayed feedback as well as dynamically changing numbers of active agents. We propose MARS-RA, a framework that reformulates credit assignment as a rank aggregation problem using contribution-based pairwise comparisons among agents generated by large multimodal models. This shift from absolute to relative estimation ensures robustness against noise and dynamic agent participation, converting comparison results into contribution scores for potential-based reward shaping. We provide theoretical justification for the convergence and robustness of the proposed framework, and show that Shapley values can be used as an interpretive reference. Experimental results on challenging tasks of different types indicate that MARS-RA can guide agents toward effective cooperation.

</details>

---

### [[20_Research/Papers/大模型/$Σ$-Mem_An_Online_Reliability_Memory_for_LLM-based_Multi-Agent_Systems|$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems]]

![[assets/2607.27958_first_page.png|800]]

- **arXiv**: [2607.27958](https://arxiv.org/abs/2607.27958)
- **PDF**: https://arxiv.org/pdf/2607.27958
- **详细分析**: [[20_Research/Papers/大模型/$Σ$-Mem_An_Online_Reliability_Memory_for_LLM-based_Multi-Agent_Systems|$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems]]
- **作者**: Peilin Feng, Suorong Yang, Soujanya Poria
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce $Σ$-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. $Σ$-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, $Σ$-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that $Σ$-Mem progressively accumulates actionable reliability information. These results establish reliability memory as a reusable foundation for adaptive coordination in LLM-based multi-agent systems.

</details>

---

### [[20_Research/Papers/大模型/From_Scoring_to_Acting_Outcome-Verified_Comparative_Self-Distillation_for_LLM_Agents|From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents]]

![[assets/2607.27937_figure.png|800]]

- **arXiv**: [2607.27937](https://arxiv.org/abs/2607.27937)
- **PDF**: https://arxiv.org/pdf/2607.27937
- **详细分析**: [[20_Research/Papers/大模型/From_Scoring_to_Acting_Outcome-Verified_Comparative_Self-Distillation_for_LLM_Agents|From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents]]
- **作者**: Xu Xia, Jinghua Piao, Min Yang, Xiaochong Lan, Jiaju Chen, Yong Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《From Scoring to Acting: Outcome-Verified Comparative Self-Distillation for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work on LLM agents is shifting from external capability elicitation to capability internalization, enabling agents to retain useful skills without retrieval at inference time. On-policy self-distillation (OPSD) offers a promising direction, but many existing methods typically supervise students by scoring actions along student-generated trajectories. Such supervision has two limitations: teacher preferences are not validated by environment outcomes, and action-level scores underuse information from student rollouts, teacher rollouts, and their behavioral relationship. We therefore advocate outcome-verified teacher supervision and comparative learning over teacher-student trajectories. Based on this view, we propose Outcome-Verified Comparative Self-Distillation (OVCSD). OVCSD organizes failed student rollouts into a prefix tree, adaptively invokes a skill-conditioned teacher from student-reached states, and retains only outcome-verified successful continuations. It then applies localized comparative learning at the first state-aligned divergence and distills the post-divergence teacher suffix to transfer completion behavior. Experiments on ALFWorld and WebShop across three model scales show that OVCSD consistently outperforms skill-free RL and existing self-distillation baselines, achieving up to 29.7 and 5.4 absolute success-rate gains over the strongest baselines on ALFWorld and WebShop, respectively, while adding less than 3% privileged interaction during training.

</details>

---

### [[20_Research/Papers/强化学习/Class-Aware_Reinforcement_Learning_for_Counterfactual_Explanation_Generation|Class-Aware Reinforcement Learning for Counterfactual Explanation Generation]]

![[assets/2607.27905_figure.png|800]]

- **arXiv**: [2607.27905](https://arxiv.org/abs/2607.27905)
- **PDF**: https://arxiv.org/pdf/2607.27905
- **详细分析**: [[20_Research/Papers/强化学习/Class-Aware_Reinforcement_Learning_for_Counterfactual_Explanation_Generation|Class-Aware Reinforcement Learning for Counterfactual Explanation Generation]]
- **作者**: Muhammad Adil Saleem, Syed Ali Raza, Mary-Anne Williams
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Class-Aware Reinforcement Learning for Counterfactual Explanation Generation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CounterNet, DRL, VCNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Counterfactual explanations (CFEs) enhance the interpretability of black-box models by generating alternative instances with adjusted feature values that achieve a contrastive outcome. Reinforcement learning (RL) offers a promising approach for CFE generation, enabling efficient exploration of counterfactual instances while ensuring control over key metrics like validity, sparsity, and proximity. Previous studies have formulated RL states exclusively using features derived from the predictors in the supervised dataset. This study explores the impact of including an instance's predicted class, alongside features derived from the predictors, in the RL state representation for generating CFEs. The hypothesis is that class-awareness enhances exploration efficiency and improves policy optimality. We compare the proposed class-aware RL method with the class-blind RL method, which is similar but excludes the instance's class information from the state representation. The comparison was conducted using seven datasets from diverse domains, varying in size. The results show that during training, class-aware RL offers benefits in terms of convergence speed, reward optimization, and episode length reduction. Moreover, it generates significantly more valid CFEs compared to class-blind RL. Finally, the instance's class-based feature consistently ranks among the most influential predictors in RL's action-selection, as shown by the SHAP and LIME values, underscoring the significance of class-awareness in RL for CFE generation. The impact is heightened clarity, faster learning, improved validity, and more effective counterfactual generation across diverse datasets.

</details>

---

### [[20_Research/Papers/具身智能/RoboBRIDGE_A_Modular_Framework_for_Bridging_Policies_to_Robust_Real-World_Robotic_Agents|RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents]]

![[assets/2607.27881_figure.png|800]]

- **arXiv**: [2607.27881](https://arxiv.org/abs/2607.27881)
- **PDF**: https://arxiv.org/pdf/2607.27881
- **详细分析**: [[20_Research/Papers/具身智能/RoboBRIDGE_A_Modular_Framework_for_Bridging_Policies_to_Robust_Real-World_Robotic_Agents|RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents]]
- **作者**: Sihyung Yoon, Minjong Yoo, Sanghyun Ahn, Seojeong Choi, Honguk Woo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.2，大模型 0.5，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CycleVLA, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have attracted growing interest as a scalable approach to robotic manipulation. While these models are effective action predictors, deploying them as robotic agents exposes critical gaps: no mechanism for failure recovery, inconsistent execution over long horizons, and limited robustness to shifts in observations, tasks, or embodiments. Existing solutions address these limitations individually through model retraining or environment-specific modules, yet what is needed is a general framework that systematically transforms a pretrained VLA into a robotic agent. We present RoboBRIDGE, a modular framework that provides an orchestration layer over five coordinated modules, namely Monitor, Perceptor, Planner, Controller, and Robot Interface, to compose robust robotic agents from off-the-shelf components, including pretrained VLAs. The Monitor pairs rapid failure detection with hierarchical recovery to correct errors before they cascade. When the environment diverges from the current plan, the Planner triggers replanning while the Perceptor updates scene understanding asynchronously, avoiding execution stalls. Within the Controller, primitive skill fine-tuning factors manipulation into domain-invariant primitives with dedicated LoRA adapters, reducing sensitivity to domain shifts when a VLA is used. Across LIBERO, RoboCasa, and real-world case studies spanning multiple robot platforms and VLA backbones, RoboBRIDGE consistently outperforms both standalone policies and prior augmented VLA deployments. These results suggest that reliable robotic agency does not arise from scaling action predictors alone, but from structured orchestration around them.

</details>

---

### [[20_Research/Papers/大模型/ARES_Adaptive_Reasoning-Effort_Steering_for_PPA-_and_Cost-Aware_RTL_Optimization_with_LLM_Agents|ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents]]

![[assets/2607.27879_figure.png|800]]

- **arXiv**: [2607.27879](https://arxiv.org/abs/2607.27879)
- **PDF**: https://arxiv.org/pdf/2607.27879
- **详细分析**: [[20_Research/Papers/大模型/ARES_Adaptive_Reasoning-Effort_Steering_for_PPA-_and_Cost-Aware_RTL_Optimization_with_LLM_Agents|ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents]]
- **作者**: Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VerilogEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute that quality to an engineered cross-design memory, and hold the reasoning effort of every call fixed. We propose Ares with three corresponding innovations. (1) We introduce a normalized dollar cost per LLM call reported alongside the figure of merit (FoM), enabling fair comparison across effort levels and optimizers. (2) Using this accounting, we find the construction of the long-term memory matters little. An engineered memory brings no dependable gain over a plain concatenation of the same experience. (3) We instead adapt the per-call reasoning effort by escalating to deeper reasoning only once progress at a lower effort stalls, via a patience counter fit on 21 training designs, allocating reasoning where it pays rather than uniformly across all iterations. On three test designs unseen during training, the effort policy lowers the FoM by 23-27% where the best fixed effort reaches 16-23%, at equal normalized cost. Ares closes up to 83% of the gap from an LLM-drafted multiply-accumulate unit to its highly hand-optimized counterpart, and reaches a 25% deeper FoM than state-of-the-art Dr. RTL at 12% of its tokens.

</details>

---

### [[20_Research/Papers/大模型/MemTxn_A_Transaction_Boundary_for_Source-Supported_Updates_and_Complete-State_Recovery_in_Agent_Memory|MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory]]

![[assets/2607.27834_figure.png|800]]

- **arXiv**: [2607.27834](https://arxiv.org/abs/2607.27834)
- **PDF**: https://arxiv.org/pdf/2607.27834
- **详细分析**: [[20_Research/Papers/大模型/MemTxn_A_Transaction_Boundary_for_Source-Supported_Updates_and_Complete-State_Recovery_in_Agent_Memory|MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory]]
- **作者**: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongMemEval, Mem2ActBench, MemBench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent memory lets long-running large language model agents reuse information across sessions and tasks. Yet errors in writable memory can persist and corrupt future behavior. Existing systems improve storage and retrieval, but they do not provide a transaction boundary for reliable updates and recovery. We therefore propose MemTxn, a governance layer outside the answer model. MemTxn verifies whether an update is supported by its source. It also selects the visible version when facts conflict and restores the application-visible state after a fault. The system uses Ordered PatchTest to validate writes, a Temporal Resolver to select versions, and a durable snapshot journal to recover state. On an item-disjoint audit, MemTxn accepts all 60 supported originals and rejects all 179 hard negatives. Under persistent multi-key faults on LongMemEval-S and LoCoMo states, it restores the complete declared active map without knowing the actual physical write set. On MemoryAgentBench FactConsolidation, MemTxn achieves the highest average F1 across all twelve answer-model configurations. It outperforms Dense by 17.06--24.07 points in five representative settings.

</details>

---

### [[20_Research/Papers/大模型/Semantic-Aligned_Structural_Abstraction_for_Multimodal_Sentiment_Analysis|Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis]]

![[assets/2607.27790_figure.png|800]]

- **arXiv**: [2607.27790](https://arxiv.org/abs/2607.27790)
- **PDF**: https://arxiv.org/pdf/2607.27790
- **详细分析**: [[20_Research/Papers/大模型/Semantic-Aligned_Structural_Abstraction_for_Multimodal_Sentiment_Analysis|Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis]]
- **作者**: Wei Chen, Junkai Li, Tongguan Wang, Hui Liu, Feiyue Xue, Chuanxiang Ma, Ying Sha
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Semantic-Aligned Structural Abstraction for Multimodal Sentiment Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Sentiment Analysis (MSA) aims to interpret complex human emotions by integrating natural language with non-verbal modalities. Non-verbal modalities share a structural isomorphism with natural language, as both can be viewed as feature sequences evolving over time. This isomorphism enables the transformation of non-verbal modalities into text-like tokens for unified semantic reasoning. Large Language Models (LLMs), designed to understand and generate sequential data, can thus be utilized to interpret complex affective sequences. However, existing LLM-based methods primarily capture low-level superficial features, failing to model affective semantics arising from structural variations and contextual interactions. To address this limitation, we propose \textbf{SentiLLM}, a unified framework that leverages \textit{Semantic-Aligned Structural Abstraction} to distill continuous raw signals into compact, semantically meaningful tokens. Specifically, we introduce a \textit{Dual-Stream Salience-Context Calibration Mechanism}, which disentangles non-verbal feature sequences into a focus stream and an ambient stream. The focus stream captures salient sentiment shifts (e.g., facial expressions) guided by textual priors, while the ambient stream characterizes stable background states. Through calibrating these dynamic sentiment shifts against background states, SentiLLM effectively projects non-verbal modalities into a unified semantic space, making them naturally understandable for LLMs. Serving as a plug-and-play module, SentiLLM significantly improves discriminative performance with only a small number of trainable parameters. Our method achieves superior performance on four datasets, MOSI, MOSEI, CH-SIMS, and CH-SIMS v2, demonstrating the effectiveness of the structural abstraction paradigm in MSA. Our code is available at: \href{https://github.com/especiallyW/SentiLLM}.

</details>

---

### [[20_Research/Papers/强化学习/LoRA_Scaffolded_Policy_Optimization_(LSPO)_A_Sampling-Time_Low-Rank_Scaffold_for_Recovering_Reinforcement-Learning_Gradient_on_Zero-Reward_C|LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts]]

![[assets/2607.27787_figure.png|800]]

- **arXiv**: [2607.27787](https://arxiv.org/abs/2607.27787)
- **PDF**: https://arxiv.org/pdf/2607.27787
- **详细分析**: [[20_Research/Papers/强化学习/LoRA_Scaffolded_Policy_Optimization_(LSPO)_A_Sampling-Time_Low-Rank_Scaffold_for_Recovering_Reinforcement-Learning_Gradient_on_Zero-Reward_C|LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts]]
- **作者**: Ken Ding
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《LoRA Scaffolded Policy Optimization (LSPO): A Sampling-Time Low-Rank Scaffold for Recovering Reinforcement-Learning Gradient on Zero-Reward Cliff Prompts》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SFT-plus-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from verifiable rewards (RLVR) for mathematical reasoning suffers from a structural blind spot: on "cliff" prompts-those on which every sampled rollout in a group fails-the group-normalized advantage is identically zero, so GRPO produces no gradient on precisely the prompts at the frontier of the model's capability. We introduce LoRA Scaffolded Policy Optimization (LSPO), a sampling-time mechanism that recovers this lost gradient. Each RL step, LSPO detects cliff prompts, fits a small low-rank (LoRA) adapter by a brief supervised step on their ground-truth solutions, re-rolls the cliffs with the base-plus-adapter model, splices the now-successful completions back into the RL batch with an importance-sampling correction, and takes a GRPO step on the base alone; the adapter receives only the supervised gradient and is discarded at checkpoint, yielding a base-only model. On DeepMath-103K with DeepSeek-R1-Distill-Qwen-1.5B, evaluated over n=5 paired seeds per arm at a matched 1000-step reporting horizon, LSPO's 5-seed mean matches or beats a DAPO baseline on all 16 (benchmark, pass@k) cells (15 strict wins and one exact tie), with gains of up to +10.7 points on AIME24/pass@4, +6.7 points on AIME24 and AIME26 at pass@16, and +2.4 points on MATH500/pass@1; averaged over the 16 cells the improvement is +3.8 points.

</details>

---

### [[20_Research/Papers/具身智能/RedFlow_Redirect_Failure_into_Action-Level_Corrections_for_Flow-matching_VLA_Policy|RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy]]

![[assets/2607.27782_figure.png|800]]

- **arXiv**: [2607.27782](https://arxiv.org/abs/2607.27782)
- **PDF**: https://arxiv.org/pdf/2607.27782
- **详细分析**: [[20_Research/Papers/具身智能/RedFlow_Redirect_Failure_into_Action-Level_Corrections_for_Flow-matching_VLA_Policy|RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy]]
- **作者**: Zhengyang Yan, Junhao Li, Fangqi Zhu, Zijun Wang, Quanxin Shou, Yikun Miao, Xiaoyi Pang, Zicong Hong, Song Guo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 2.1，强化学习 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment. While offline reinforcement learning (RL) provides a practical way to improve deployed policies using rollout data, existing methods either ignore failure data or exploit it only at the trajectory level, resulting in low learning efficiency and persistent errors. We propose **RedFlow**, a fine-grained offline RL framework that redirects failure experiences into action-level corrective supervision for flow-matching VLA policies. RedFlow consists of two key components: (1) a **Context-Aware Corrective Matching** mechanism that identifies failure-inducing actions and retrieves successful alternatives from similar contexts as corrective targets, and (2) an **Adaptive Redirection Objective** that jointly reinforces successful actions, suppresses undesirable ones, and redirects recoverable failures toward corrective targets. By converting both successful and failed experiences into dense supervision, RedFlow enables robust recovery learning from mixed-quality data. Experiments on the LIBERO benchmark and three real-world manipulation tasks show that RedFlow consistently outperforms state-of-the-art offline RL baselines, improving the real-world success rate from 56.7% to 74.7%. It also matches strong on-policy methods (PPO, GRPO, and DDPO) while requiring roughly an order of magnitude fewer training samples.

</details>

---

### [[20_Research/Papers/大模型/RefineSVG_Visual_Feedback-Driven_Reinforcement_Learning_for_Image-to-SVG_Generation|RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation]]

![[assets/2607.27699_figure.png|800]]

- **arXiv**: [2607.27699](https://arxiv.org/abs/2607.27699)
- **PDF**: https://arxiv.org/pdf/2607.27699
- **详细分析**: [[20_Research/Papers/大模型/RefineSVG_Visual_Feedback-Driven_Reinforcement_Learning_for_Image-to-SVG_Generation|RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation]]
- **作者**: Shaobo Liu, Feiqiao Mao, Shuaishuai Zhou, Yan Zhan, Weiqi Tan, Zhiqiong Lu, Zhengping Liang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Generation》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SVG-Bench, VGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose RefineSVG, a single-step closed-loop visual feedback framework that enables multimodal large language models (MLLMs) to perform high-fidelity image-to-SVG generation through self-correction. Existing MLLM-based approaches rely on single-pass open-loop inference, where the model receives visual input only once and must generate thousands of SVG code tokens without intermediate verification. This paradigm inevitably leads to geometric drift, error accumulation, and visual hallucination on complex images. RefineSVG overcomes this limitation by invoking an external rendering engine after an initial SVG generation pass to compare the rendered output against the target image. The comparison yields a multi-dimensional visual residual map (Diff-Map) that is fed back to the model as a ReAct-style correction signal, driving a targeted correction step. To support this render-observe-correct interaction, we further introduce an SVG-oriented semantic vocabulary that compresses token sequences by over 52%. A progressive training pipeline spanning supervised fine-tuning, rejection-sampling cold-start data construction, and end-to-end agentic reinforcement learning aligns the model with closed-loop visual correction. Extensive experiments show that RefineSVG consistently outperforms existing baselines in reconstruction fidelity, structural accuracy, and code efficiency.Code is available at https://github.com/liuxiaobo66/RefineSVG.

</details>

---

### [[20_Research/Papers/机器人/LabEvolver_Training-Free_Experience_Evolution_for_Safe_and_Grounded_Wet-Lab_Agents|LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents]]

![[assets/2607.27690_figure.png|800]]

- **arXiv**: [2607.27690](https://arxiv.org/abs/2607.27690)
- **PDF**: https://arxiv.org/pdf/2607.27690
- **详细分析**: [[20_Research/Papers/机器人/LabEvolver_Training-Free_Experience_Evolution_for_Safe_and_Grounded_Wet-Lab_Agents|LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents]]
- **作者**: Jingya Wang, Yuyang Gao, Liuzhenghao Lv, Yonghong Tian, Yuyang Liu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce LabEvolver, a training-free framework that equips safe and grounded wet-lab agents with episodic memory from execution experience. LabEvolver couples a state-grounded inner trial loop for adaptive perception, online planning, and safety validation with an outer evolution loop that distills completed trajectories into reusable skill, strategy, and safety experience. On robotic solution-preparation tasks, LabEvolver demonstrates real-world feasibility, reducing pH-regulation completion time and safety-gate intercepts by 48.2% and 60.0%, respectively. On ALFWorld, it further improves cumulative success rate within 20 steps from 76.2% with ReAct to 91.4% over 500 continual tasks, showing generality beyond wet-lab settings. These results support learn-by-doing experience evolution as a feasible path toward closed-loop automated scientific discovery. The project page is available at https://github.com/AndyGao6186/LabEvolver.

</details>

---

### [[20_Research/Papers/具身智能/Arm2Air_Cross-Embodiment_Skeleton_Transfer_for_3D_Relay_Formation|Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation]]

![[assets/2607.27627_figure.png|800]]

- **arXiv**: [2607.27627](https://arxiv.org/abs/2607.27627)
- **PDF**: https://arxiv.org/pdf/2607.27627
- **详细分析**: [[20_Research/Papers/具身智能/Arm2Air_Cross-Embodiment_Skeleton_Transfer_for_3D_Relay_Formation|Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation]]
- **作者**: Dohun Lee, Kyeonghyun Yoo, Seokmin Kim, Byongho Lee, Seungjoo Oh, Hwangnam Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Arm2Air: Cross-Embodiment Skeleton Transfer for 3D Relay Formation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) relay networks can restore connectivity after communication infrastructure is damaged. Urban relay placement is difficult because line-of-sight blockage, communication range, altitude, and three-dimensional obstacles must be considered jointly. Arm2Air transfers obstacle-avoidance skeletons from robot arms to UAV relay placement through cross-embodiment transfer. Source-domain robot-arm motions from a pretrained Neural MP model are converted into ordered skeletons that pretrain a transformer-based transfer platform, which is then adapted to the UAV domain using limited target data and Low-Rank Adaptation. The transferred skeleton initializes a relay chain that is refined for connectivity, bottleneck capacity, delay, and movement cost. On nine held-out high-clutter 3D urban maps, Arm2Air reduced median end-to-end planning runtime by 64.9 percent relative to the fastest conventional planner. On the high-obstruction group of a separate 30-map dense urban holdout, it increased bottleneck capacity by 32.6 percent, reduced capacity variance by 74.7 percent, reduced maximum hop distance by 13.2 percent, reduced hop-distance variance by 75.2 percent, and reduced relay displacement by 16.9 percent relative to IMPC-MD. With only three target-domain training maps, Arm2Air reduced relay-position root mean square error by 53.6 percent relative to training from scratch while updating 0.134 million parameters, compared with 1.383 million for Scratch and Full Fine-tuning. These results demonstrate computationally and data-efficient UAV relay placement and suggest a broader principle for transferring ordered structural priors across heterogeneous embodied tasks.

</details>

---

### [[20_Research/Papers/强化学习/World_Action_Planner_Generalizable_Decision-Making_with_Action-Conditioned_World_Models|World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models]]

![[assets/2607.27599_figure.png|800]]

- **arXiv**: [2607.27599](https://arxiv.org/abs/2607.27599)
- **PDF**: https://arxiv.org/pdf/2607.27599
- **详细分析**: [[20_Research/Papers/强化学习/World_Action_Planner_Generalizable_Decision-Making_with_Action-Conditioned_World_Models|World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models]]
- **作者**: Xiangcheng Zhang, Yilun Du
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，世界模型 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building generalizable agents for diverse applications remains a fundamental challenge. While imitation learning-based policies succeed in specific training environments, they often fail to generalize to novel scenes and tasks. In this work, we propose World Action Planner, a robot planning system that leverages the reasoning capabilities of Vision-Language Models (VLMs) and the physical grounding of a multi-task pose-image conditioned world model. Our system enables an agent to propose initial action plans and iteratively refine them via optimization and search, reasoning over imagined world model rollouts. We demonstrate that our approach achieves superior performance across compositional tasks, new layouts, and zero-shot generalization scenarios, significantly outperforming state-of-the-art end-to-end policy models such as VLAs and WAMs. Project website at worldactionplanner.github.io

</details>

---

### [[20_Research/Papers/机器人/A_Systems_Engineering_Framework_for_Vision-Language-Enabled_UAV_Triage_and_Disaster_Response|A Systems Engineering Framework for Vision-Language-Enabled UAV Triage and Disaster Response]]

![[assets/2607.27597_figure.png|800]]

- **arXiv**: [2607.27597](https://arxiv.org/abs/2607.27597)
- **PDF**: https://arxiv.org/pdf/2607.27597
- **详细分析**: [[20_Research/Papers/机器人/A_Systems_Engineering_Framework_for_Vision-Language-Enabled_UAV_Triage_and_Disaster_Response|A Systems Engineering Framework for Vision-Language-Enabled UAV Triage and Disaster Response]]
- **作者**: Swapnil Saha, Bhuvan Rajanasiriyur Jagadeesha, Karishma Patnaik, Neelakshi Majumdar
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《A Systems Engineering Framework for Vision-Language-Enabled UAV Triage and Disaster Response》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in Vision Language Models (VLMs) have created new opportunities for disaster response, where responders must interpret large volumes of sensor data under time pressure. Current VLM applications include social media monitoring for situational awareness, generation of draft action plans, and translation of technical alerts into public-facing messages. While these efforts can accelerate information flow, they remain largely limited to decision-support roles. Such approaches can increase operator burden because humans must still translate outputs into coordinated actions across teams and robotic assets. This study explores the viability of embedding VLMs as coordination agents within the human-UAV loop. The proposed architecture integrates natural language interaction, mission-level task coordination, software-in-the-loop implementation, and communication aligned with the Incident Command System (ICS). Rather than functioning solely as advisory tools, VLMs facilitate communication between human operators, mission control logic, and UAV task execution. The framework was developed using a Model-Based Systems Engineering (MBSE) approach, with use case and block definition diagrams representing system roles, internal structure, and component interactions. Three key elements, the VLM Coordinator Agent, UAV Mission Control, and Task Allocator, were implemented within an integrated simulation and control environment. A preliminary human-factors evaluation with seven participants showed reduced perceived workload across mental demand, effort, and frustration, along with high ratings for AI trust and communication clarity. By integrating MBSE, software-in-the-loop testing, and human-factors evaluation, this work advances scalable human-autonomy teaming for high-stakes disaster response, with broader implications for aerospace autonomy and civil safety.

</details>

---

### [[20_Research/Papers/大模型/DeepResearch_Agent_System|DeepResearch Agent System]]

![[assets/2607.27562_first_page.png|800]]

- **arXiv**: [2607.27562](https://arxiv.org/abs/2607.27562)
- **PDF**: https://arxiv.org/pdf/2607.27562
- **详细分析**: [[20_Research/Papers/大模型/DeepResearch_Agent_System|DeepResearch Agent System]]
- **作者**: Yong Huang, Yulu Huang, for the team Collaboration
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DeepResearch Agent System》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：WebWalkerQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The DeepResearch Agent System is a large language model system engineered for deep information retrieval, multi-step reasoning, and autonomous research tasks. Built upon a sparse activation architecture with 30 billion total parameters of which only 3 billion are activated per token, the system achieves state-of-the-art performance on multiple agent search benchmarks while delivering 3.2 times faster inference compared to dense counterparts of equivalent scale. The system supports a 128K-token context window with hierarchical attention mechanisms that yield 18.7% accuracy and 23.4% recall improvements over standard long-context approaches. A dual-mode reasoning engine provides both a ReAct paradigm for basic multi-step problem solving and an IterResearch mode for high-performance iterative research with up to 20 reasoning steps, collectively delivering a 31.2% accuracy improvement over single-pass baselines. Multi-tool coordination integrates retrieval, computation, web search, and file parsing modules to achieve 92.1% tool-use accuracy. A reinforcement learning optimization framework based on the GRPO algorithm provides token-level policy gradients that improve training stability by 35% and accelerate convergence by 42%. An automated data synthesis pipeline with seed-based expansion achieves a 92.5% usability rate. Benchmark results include 87.3% on Humanity's Last Exam, 85.3% on BrowserComp Chinese, and 91.2% on WebWalkerQA. The system is fully open-sourced, including data synthesis, training, and inference code, and supports applications in academic research, business analysis, R&amp;D support, and education.

</details>

---

### [[20_Research/Papers/具身智能/Cross-Embodiment_Transfer_via_Behavior-Aligned_Representations|Cross-Embodiment Transfer via Behavior-Aligned Representations]]

![[assets/2607.27549_figure.png|800]]

- **arXiv**: [2607.27549](https://arxiv.org/abs/2607.27549)
- **PDF**: https://arxiv.org/pdf/2607.27549
- **详细分析**: [[20_Research/Papers/具身智能/Cross-Embodiment_Transfer_via_Behavior-Aligned_Representations|Cross-Embodiment Transfer via Behavior-Aligned Representations]]
- **作者**: Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale, Dorsa Sadigh
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Cross-Embodiment Transfer via Behavior-Aligned Representations》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MiniVLA, Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions, end-effector traces of robot motion) in vision-language-action (VLA) models to promote cross-embodiment transfer. We hypothesize that by possessing invariances across embodiments while being predictive of robot actions, these representations can help unify large-scale cross-embodiment data to enhance transfer. To assess our hypothesis, we develop a simulation-based benchmark designed to assess transfer with diverse cross-embodiment data to new embodiments. Using this benchmark, we compare different representations and ways of incorporating them. We identify that end-effector traces can be particularly beneficial for transfer, representations are generally more useful with larger prior datasets, and can be used to benefit from action-free data. We also demonstrate that they can enhance sim-to-real cross-embodiment transfer, improving task completion progress of real robot policies pre-trained on simulation data by 28%. We provide videos of our evaluations at our website: https://ajaysridhar.com/barx/.

</details>

---

### [[20_Research/Papers/大模型/ThreatForest_Multi-Agent_Attack_Tree_Generation_with_Pluggable_TTP_Framework_Mapping|ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping]]

![[assets/2607.27528_figure.png|800]]

- **arXiv**: [2607.27528](https://arxiv.org/abs/2607.27528)
- **PDF**: https://arxiv.org/pdf/2607.27528
- **详细分析**: [[20_Research/Papers/大模型/ThreatForest_Multi-Agent_Attack_Tree_Generation_with_Pluggable_TTP_Framework_Mapping|ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping]]
- **作者**: Cristian Leo, Anton Dykyi, Danny Cortegaca, Daniel Begimher, Prakash Jha
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Threat modeling is essential for secure software development, yet manual analysis of cloud-native architectures is slow and demands scarce security expertise. We present ThreatForest, a multi-agent system that generates structured attack trees from source code repositories, maps attack steps to adversary tactics, techniques, and procedures (TTPs) from a pluggable set of frameworks (MITRE ATT&amp;CK, CAPEC, and cloud-specific threat matrices), and synthesizes actionable mitigations. ThreatForest decomposes threat modeling into a multi-stage agent pipeline -- repository analysis, context refinement, threat generation, parallel attack-tree construction with TTP mapping and mitigation synthesis, and report generation -- orchestrated as a directed graph with deterministic verification gates, bounded retries, and three human-in-the-loop validation points. A domain-specific sentence-transformer maps each attack step to candidate techniques by cosine similarity; we show empirically that this embedding stage, not the surrounding pipeline, is the dominant accuracy bottleneck. We evaluate ThreatForest across seven application domains on a sixteen-dimension rubric, scored by a panel of independent LLM raters with an adversarial verification pass and expert review. Panel-measured quality reaches 0.63-0.68 (on a 0-1 scale) for threat statements, attack trees, and mitigations, but only 0.29 for embedding-only TTP mapping -- a gap stable across all seven domains that isolates the binding constraint. A controlled single-call baseline on the same model more than doubles mapping defensibility, pinning the limitation on the embedding encoder rather than the multi-agent design. To our knowledge, ThreatForest is the first end-to-end system that turns a code repository into TTP-mapped attack trees with evidence-based mitigations across adversary frameworks, with a reusable framework for benchmarking such systems.

</details>

---

### [[20_Research/Papers/大模型/Models_for_minimalist_RAG_B1ade_335M_Embedding_and_1B_Parameter_Small_Language_Models|Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models]]

![[assets/2607.27506_figure.png|800]]

- **arXiv**: [2607.27506](https://arxiv.org/abs/2607.27506)
- **PDF**: https://arxiv.org/pdf/2607.27506
- **详细分析**: [[20_Research/Papers/大模型/Models_for_minimalist_RAG_B1ade_335M_Embedding_and_1B_Parameter_Small_Language_Models|Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models]]
- **作者**: Shreyas Subramanian, Mecit Gungor, Vikram Elango
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: RL

#### 研究背景与动机

《Models for minimalist RAG: B1ade 335M Embedding and 1B Parameter Small Language Models》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HotPotQA, HotpotQA, PopQA, PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language and embedding models used in RAG systems are conventionally assumed to require large-scale pretraining and explicit grounding supervision. We present B1ade, an efficient RAG architecture comprising two purpose-built components: a compact embedding model and a purpose-built SLM. B1ade-embed, a 335M parameter retrieval model constructed via parameter-free fusion of five pretrained encoders achieves top MTEB scores among sub-500M models with zero additional training, and B1ade-1B, an SLM trained on low-cost GPUs using Group Relative Policy Optimization (GRPO) on 723M tokens (2.2M examples) of curated context-question pairs with rewards that optimize only answer similarity. Our central finding is emergent attribution: despite receiving no explicit supervision for source citation, B1ade-1B cites retrieved passages in 42.4% of responses, exceeding the attribution rate of its training distribution by 5.5 percentage points. This demonstrates that grounding behavior can emerge as an accuracy-maximizing strategy under RL training, without explicit reward engineering. On standard QA benchmarks, B1ade-1B achieves 81.82% on PopQA, 65.8% on PubMedQA, and 51.09% on FEVER. In end-to-end RAG evaluation, B1ade-1B achieves an average score of 0.654 across correctness, completeness, coherence, and faithfulness, a 10.8% improvement over the SFT, while closing the gap with models 1.5x its size. These results show that strategic model composition and reward design suffice for resource-efficient RAG, without large-scale pretraining.

</details>

---

### [[20_Research/Papers/具身智能/Leveraging_Trajectory_Graphs_for_Pre-Execution_Error_Diagnosis_in_Agentic_LLM_Systems|Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems]]

![[assets/2607.27443_figure.png|800]]

- **arXiv**: [2607.27443](https://arxiv.org/abs/2607.27443)
- **PDF**: https://arxiv.org/pdf/2607.27443
- **详细分析**: [[20_Research/Papers/具身智能/Leveraging_Trajectory_Graphs_for_Pre-Execution_Error_Diagnosis_in_Agentic_LLM_Systems|Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems]]
- **作者**: Xu Zheng, Zhuomin Chen, Chaohao Lin, Hua Wei, Haifeng Chen, Wei Cheng, Dongsheng Luo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.9）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Leveraging Trajectory Graphs for Pre-Execution Error Diagnosis in Agentic LLM Systems》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlfWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model~(LLM)-based agents have demonstrated exceptional performance across a wide range of complex interactive tasks. However, they often struggle with long-horizon interactive tasks common in domains, such as embodied AI. The complexity and vast action spaces in these settings lead to compounding errors, where a single suboptimal action can derail an entire trajectory, causing the agent to exhaust its limited step budget on inefficient or unrecoverable paths. To overcome this without costly fine-tuning, we draw inspiration from software debugging, where execution logs are analyzed to preemptively catch errors. We propose \textit{Trajectory Graph Copilot}, a novel framework that acts as a ``copilot'' for LLM agents by diagnosing potential action errors before they are executed. At its core,\textit{Graph Debugger} models historical trajectories as a probabilistic graph and uses a Graph Neural Network to identify sequential action patterns that frequently lead to failure. Functioning as a proactive diagnostic sandbox, our method provides early warnings on potentially flawed actions, prompting the agent to self-correct. This pre-action error diagnosis prevents costly mistakes, significantly enhancing the agent's ability to complete long-horizon tasks successfully. The extensive experiments on four benchmarks with three LLM agents demonstrate a $14.69\%$ pass ratio improvement on average.

</details>

---

### [[20_Research/Papers/大模型/SkillMentor_LLM_Agent_Self-Evolution_via_Learning_Blind-Spot_Diagnosis|SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis]]

![[assets/2607.27360_figure.png|800]]

- **arXiv**: [2607.27360](https://arxiv.org/abs/2607.27360)
- **PDF**: https://arxiv.org/pdf/2607.27360
- **详细分析**: [[20_Research/Papers/大模型/SkillMentor_LLM_Agent_Self-Evolution_via_Learning_Blind-Spot_Diagnosis|SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis]]
- **作者**: Xiaoyi Bao, Yuanzhen Xie, Yunzhi Tan, Jinghang Gu, Zhongqing Wang, Chu-Ren Huang, Bo Hu, Zang Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AppWorld, MemRL, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent self-evolution has primarily focused on learning how to act, while overlooking an equally important capability: learning to discover what an agent does not know. Existing approaches typically assume that failure discovery is given, focusing on how to repair failures once they are identified. We ask whether blind-spot diagnosis itself can be learned. We thus study diagnosis as an agent capability separate from execution, and exclude two alternative sources of progress: executor adaptation and human supervision. Under these constraints, performance cannot improve through executor updates or annotated examples, forcing all improvements to originate from the learned diagnostic capability. We propose SkillMentor, which trains a Mentor policy via reinforcement learning to generate diagnostic tasks, identify recurrent failure modes, and curate them into reusable corrective skills. Across AppWorld and BFCLv3, SkillMentor improves executor performance by an average of 44.2%. These results suggest that blind-spot diagnosis is a learnable capability, enabling self-evolution without updating executor weights or relying on human-curated data.

</details>

---

### [[20_Research/Papers/大模型/Flat_Score,_Amplified_Failures_How_the_Error_Budget_Masks_Damage_in_Quantized_LLM_Agents|Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents]]

![[assets/2607.27275_figure.png|800]]

- **arXiv**: [2607.27275](https://arxiv.org/abs/2607.27275)
- **PDF**: https://arxiv.org/pdf/2607.27275
- **详细分析**: [[20_Research/Papers/大模型/Flat_Score,_Amplified_Failures_How_the_Error_Budget_Masks_Damage_in_Quantized_LLM_Agents|Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents]]
- **作者**: Jiwon Jang, Kisu Yang, Heuiseok Lim, Hyunwoo Park
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training quantization to 4-bit weights is widely reported to be nearly lossless. We test this claim for multi-turn, tool-calling agents, where it now matters most. On $τ^2$-bench, across two open-weight model families in dense and MoE variants and two domains (eight cells, 456 episodes each, at 16-, 8-, and 4-bit weights), quantization indeed looks free on the standard metric. No cell shows a score change that survives multiple-comparison correction, and in the cell that carries the largest process damage, equivalence testing bounds the change within $\pm$7.5 points. The process tells a different story. Quantization amplifies the failure the model already exhibits at full precision (tool-name hallucination in telecom, with the same directional trend in retail entity errors) by up to 2.5$\times$ in volume (+17.6 points per task), while creating essentially no new failures. The failure set is the same at every precision (rank correlation $\geq$ 0.94, 0.18% novel events). The score stays flat because the benchmark's ten-error budget absorbs the extra failures. Shrinking the budget to two errors re-exposes a score gap of 17 points, and it does so only in the one cell where quantization added error volume, exactly as the masking account predicts. A targeted error-repair prompt, run for five telecom models at every precision, removes the damage exactly and only where it lives. Both diagnostics, the per-channel error rate and success under a shrinking budget, come from logs benchmarks already collect; we suggest reporting them alongside task reward.

</details>

---

### [[20_Research/Papers/大模型/FAVA_Formal_Authorization_for_Verified_Agents_with_Evidence-Backed_Permission_Graphs|FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs]]

![[assets/2607.27267_figure.png|800]]

- **arXiv**: [2607.27267](https://arxiv.org/abs/2607.27267)
- **PDF**: https://arxiv.org/pdf/2607.27267
- **详细分析**: [[20_Research/Papers/大模型/FAVA_Formal_Authorization_for_Verified_Agents_with_Evidence-Backed_Permission_Graphs|FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs]]
- **作者**: Yifan Zhang, Xinkui Zhao, Sai Liu, Hengxuan Lou, Guanjie Cheng, Chang Liu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《FAVA: Formal Authorization for Verified Agents with Evidence-Backed Permission Graphs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OctoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents autonomously interleave semantic reasoning with complex system operations. In these dynamic environments, static tool-level permissions are fundamentally insufficient; safe authorization is highly context-dependent and heavily reliant on evolving runtime states and data flows. We present FAVA (Formal Authorization for Verified Agents), a permission-carrying authorization framework for agent execution. FAVA utilizes an LLM-guided Permission Intermediate Representation (IR) to translate ambiguous natural-language tasks into structured constraints. A deterministic lowering pass then converts this IR into an evidence-backed permission graph that explicitly tracks data flows, dependencies, and contextual labels. To provide strict security guarantees, a Satisfiability Modulo Theories (SMT) authorizer mathematically verifies the current graph against security policies before any effectful action executes. A runtime gateway then enforces the solver's result, either authorizing the execution or intercepting it with a precise counterexample. We evaluate FAVA across OpenAgentSafety, OctoBench, and ActPlane scenarios. Our evaluation demonstrates that FAVA achieves a 90.5% Decision Compliance Rate (DCR) over the aggregate dataset, successfully intercepting dynamic violating traces in the evaluated trace-conditioned scenarios.

</details>

---

### [[20_Research/Papers/其他/Do_Context_Files_Help_Coding_Agents_A_Two-Agent_Ablation_Study_on_Real_Repositories|Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories]]

![[assets/2607.27250_figure.png|800]]

- **arXiv**: [2607.27250](https://arxiv.org/abs/2607.27250)
- **PDF**: https://arxiv.org/pdf/2607.27250
- **详细分析**: [[20_Research/Papers/其他/Do_Context_Files_Help_Coding_Agents_A_Two-Agent_Ablation_Study_on_Real_Repositories|Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories]]
- **作者**: Prakhar Khatri
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CrossCodeEval, RepoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent context files (AGENTS.md, CLAUDE.md) are standard practice for guiding AI coding agents, yet evidence for their effectiveness is contradictory. We present a controlled ablation of context-injection strategy across two frontier agents (Claude Code and Codex), 17 real tasks from 3 repositories (15 shared + 2 Codex-only), and 288 evaluated runs with gold-test evaluation. Context strategy does not measurably move correctness on either agent (bounded to &lt;=10-15pp via equivalence testing). A failure-mode triage reveals why: agents fail on implementation skill---feature design, pattern selection, exact wiring---not missing repository knowledge that a context file could supply; a manipulation probe confirms the real AGENTS.md never converts a near-miss to a pass on either agent. We further show that borderline task difficulty is agent-specific (Spearman rho=0.75), offering a candidate explanation for prior contradictions: single-agent studies draw tasks from different agents' informative bands. We release all code, data, and analysis.

</details>

---
