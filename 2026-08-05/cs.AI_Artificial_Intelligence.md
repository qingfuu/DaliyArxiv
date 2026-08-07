# cs.AI | Artificial Intelligence | 2026-08-05

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/大模型/Video-DeepResearch_Towards_the_Next-Generation_Multimodal_Deepresearch_Agent|Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent]]

![[assets/2608.03979_figure.png|800]]

- **arXiv**: [2608.03979](https://arxiv.org/abs/2608.03979)
- **PDF**: https://arxiv.org/pdf/2608.03979
- **详细分析**: [[20_Research/Papers/大模型/Video-DeepResearch_Towards_the_Next-Generation_Multimodal_Deepresearch_Agent|Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent]]
- **作者**: Zhen Fang, Yu Zeng, Wenxuan Huang, Yiming Zhao, Shiting Huang, Tianfei Ren, Qi Lu, Qingnan Ren, Qisheng Su, Lionel Z. Wang, Qingyu Yin, Shuang Chen...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA, Video-DR-Bench, VideoDR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address these challenges, we propose Video-DR, featuring a decoupled perception-exploration pipeline with stage-wise tool unlocking that compels exhaustive cross-frame visual grounding prior to web retrieval. Our framework adopts a two-stage training recipe: supervised fine-tuning followed by Group Relative Policy Optimization (GRPO), enabling autonomous exploration that breaks the imitation-learning ceiling. Furthermore, we curate Video-DR-Bench, a human-AI collaborative benchmark comprising 200 complex, multi-hop VQA instances. Empirical results demonstrate that our Video-DeepResearch-35B-A3B establishes a new state-of-the-art of 64.0% average accuracy, surpassing proprietary Claude-4.5-Sonnet (59.0%) by 5.0 points and significantly outperforming GPT-5 (52.5%) and Gemini 2.5 Pro (57.5%). The 30B-A3B variant achieves 59.3%, competitive with Claude-4.5-Sonnet and demonstrating the effectiveness of our training paradigm even at compact scale. Code: https://github.com/Osilly/Vision-DeepResearch.

</details>

---

### [[20_Research/Papers/机器人/When_Efficiency_Becomes_Fragility_Exploiting_Dynamic_Routing_Vulnerabilities_in_Adaptive_UAV_Tracking|When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking]]

![[assets/2608.03902_figure.png|800]]

- **arXiv**: [2608.03902](https://arxiv.org/abs/2608.03902)
- **PDF**: https://arxiv.org/pdf/2608.03902
- **详细分析**: [[20_Research/Papers/机器人/When_Efficiency_Becomes_Fragility_Exploiting_Dynamic_Routing_Vulnerabilities_in_Adaptive_UAV_Tracking|When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking]]
- **作者**: Shaofeng Liang, Runwei Guan, Wenshuo Chen, Jiemin Wu, Bowen Tian, Haozhe Jia, Kaishen Yuan, Songning Lai, Daizong Liu, Yutao Yue
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Security

#### 研究背景与动机

《When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage an input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded local Lipschitz constant at discrete layer-skipping decision boundaries. This mathematical discontinuity renders adaptive tracking networks inherently unstable: tiny input perturbations can be amplified at the gating modules, causing dramatic changes in the inference topology. We formally characterize this singularity in the context of adaptive tracking architectures and, for the first time, identify it as a directly exploitable new attack surface. This insight reveals a previously overlooked and highly vulnerable topological path space attack surface. Based on this, we propose the Adversarial Path-Inversion (API) framework. API generates imperceptible perturbations to precisely manipulate the gating decisions, forcing the inference onto altered computational paths. The severe inconsistency between the original and the inverted paths dismantles the representation capability of the model. Extensive experiments on state-of-the-art adaptive trackers demonstrate that API achieves superior perturbation stealthiness, more effective attack, and faster inference speeds. This work opens a new dimension for the security analysis of dynamic tracking networks and provides a theoretical warning for constructing robust adaptive tracking architectures in the future.

</details>

---

### [[20_Research/Papers/强化学习/Enhancing_VLM_Reward_Models_Through_Structure-Aware_Fine-Tuning|Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning]]

![[assets/2608.03875_figure.png|800]]

- **arXiv**: [2608.03875](https://arxiv.org/abs/2608.03875)
- **PDF**: https://arxiv.org/pdf/2608.03875
- **详细分析**: [[20_Research/Papers/强化学习/Enhancing_VLM_Reward_Models_Through_Structure-Aware_Fine-Tuning|Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning]]
- **作者**: Pyrros Koussios, Chenhao Li, Xin Chen, Andreas Krause
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing effective reward functions remains a major bottleneck in Reinforcement Learning (RL). Recent work uses large foundation Vision-Language Models (VLMs) as reward models, computing text-observation similarity to bypass manual reward engineering. Although promising, these rewards are often noisy and unreliable, limiting their direct utility during deployment. We present Structure-Aware Fine-Tuning (SAFT), a simple, self-supervised method that refines these imperfect reward signals online without access to ground-truth supervision. SAFT leverages intrinsic structural priors to regularize the VLM's latent space via LoRA adapters. We rigorously evaluate SAFT across a spectrum of base model capabilities to demonstrate its versatility. Our results show that SAFT consistently denoises the reward landscape, yielding faster policy convergence and substantially improved alignment (EPIC distance) relative to the underlying base model, suggesting that failures can often be attributed to structural brittleness rather than semantic misunderstanding. By replacing extensive human preference annotation with structural inductive biases inherent to the task, SAFT offers a scalable path for stabilizing text-conditioned RL and underscores the broader value of incorporating task structure as a general inductive bias.

</details>

---

### [[20_Research/Papers/大模型/ContinualSkillBench_Can_LLM_Agents_Truly_Evolve_Their_Capabilities|ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?]]

![[assets/2608.03874_figure.png|800]]

- **arXiv**: [2608.03874](https://arxiv.org/abs/2608.03874)
- **PDF**: https://arxiv.org/pdf/2608.03874
- **详细分析**: [[20_Research/Papers/大模型/ContinualSkillBench_Can_LLM_Agents_Truly_Evolve_Their_Capabilities|ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?]]
- **作者**: Tianyi Guan, Yiding Wang, Haotong Yang, Siyuan Cao, Shirui Liu, Yi Hu, Jiaqi Li, Muhan Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CL-Bench, ClawBench, ContinualSkillBench, LawBench, MedAgentsBench, OMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficulty and opportunities for cross-task skill reuse. Our experiments show that sequential execution generally improves performance, but the gains vary substantially across models and domains. Moreover, in-context learning performs comparably to explicit skill maintenance on average, suggesting that much of the improvement arises from adaptation to prior context and feedback rather than reusable skill abstraction alone. Explicit skills nevertheless provide selective benefits for tasks requiring reusable procedures or precise outputs. We further find that less capable models tend to accumulate larger, more fragmented collections of task-specific skills. These findings show that current in-context skill evolution mechanisms can support continual adaptation, but still struggle to consistently consolidate experience into robust and transferable skills.

</details>

---

### [[20_Research/Papers/大模型/MAFIA_Query-Only_Memory_Attacks_via_Probing_and_Factual_Injection_against_Audited_LLM_Agents|MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents]]

![[assets/2608.03844_figure.png|800]]

- **arXiv**: [2608.03844](https://arxiv.org/abs/2608.03844)
- **PDF**: https://arxiv.org/pdf/2608.03844
- **详细分析**: [[20_Research/Papers/大模型/MAFIA_Query-Only_Memory_Attacks_via_Probing_and_Factual_Injection_against_Audited_LLM_Agents|MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents]]
- **作者**: Jiaming Chen, Yisen Gao, Yanping Li, Zifan Liu, Yumeng Zhang, Jun Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiveness and rigorous semantic checks. To overcome these limitations, we propose MAFIA, a query-only Memory Attack framework via probing and Factual Injection against Audit, tailored to this extended threat model. Specifically, MAFIA introduces: (1) a placement strategy that ensures retrieval-competitive injection via memory probing, budget allocation, and scheduling; and (2) a payload design that bypasses audits using compact factual cloaks, preserving malicious effects while maintaining high semantic similarity. Extensive evaluations reveal that MAFIA achieves up to a 90.7% attack success rate while suppressing audit detection from a peak of 83.3% to at most 7.4%, exposing critical vulnerabilities across agentic memory systems. Code will be made publicly available at https://github.com/JiamingChen1234/MAFIA.

</details>

---

### [[20_Research/Papers/大模型/VIBE_A_VAD-Informed_Benchmark_for_Entity-Centered_Affective_Profiling_of_Large_Language_Model_Outputs|VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs]]

![[assets/2608.03810_figure.png|800]]

- **arXiv**: [2608.03810](https://arxiv.org/abs/2608.03810)
- **PDF**: https://arxiv.org/pdf/2608.03810
- **详细分析**: [[20_Research/Papers/大模型/VIBE_A_VAD-Informed_Benchmark_for_Entity-Centered_Affective_Profiling_of_Large_Language_Model_Outputs|VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs]]
- **作者**: Andrei Chetvergov, Alexander Evseev, Timofei Sivoraksha, Stepan Ukolov, Mikhail Solovev, Danil Sazanakov, Sergey Bolovtsov
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and a passport reporting format. We introduce VIBE, a benchmark for entity-centered affective profiling of LLM outputs in Valence-Arousal-Dominance (VAD) space. Its core contribution is a measurement contract: VIBE separates generation from external scoring, distinguishes scalar favorability, response-level VAD, and target-directed VAD, and reports profiles through an Affective Passport. Three empirical layers support the contract. H1 shows scalar favorability does not subsume arousal and dominance: valence findings are cross-validated (rV = 0.944 judge-human, rV = 0.954 inter-scorer); arousal and dominance are single-scorer directional estimates, not point-precise, consistent with known inter-annotator difficulty on these axes (rA = 0.495, rD = 0.702 among human annotators). H2 shows whole-response and target-directed VAD are different contracts: the same text can carry one affective tone overall while representing the named target differently. H3 is a protocol-drift diagnostic: elicitation conditions shift profiles, motivating context metadata in every affective report. These results motivate entity-centered affective profiling as a documented practice: profiles should be released with scorer identity, coverage, protocol, and interpretation limits.

</details>

---

### [[20_Research/Papers/大模型/Failure-Informed_Image_Self-Augmentation_for_Multimodal_Large_Language_Model_Self-Improvement|Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement]]

![[assets/2608.03733_figure.png|800]]

- **arXiv**: [2608.03733](https://arxiv.org/abs/2608.03733)
- **PDF**: https://arxiv.org/pdf/2608.03733
- **详细分析**: [[20_Research/Papers/大模型/Failure-Informed_Image_Self-Augmentation_for_Multimodal_Large_Language_Model_Self-Improvement|Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement]]
- **作者**: Chunyang Jiang, Pingping Zhang, Yuzhi Zhao, Wenao Ma, Zhijian Hou, Mengyang Wu, Yiyang Cai, Senkang Hu, Sitong Cheng, Chi-Min Chan, Wei Xue, Yike Guo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Failure-Informed Image Self-Augmentation for Multimodal Large Language Model Self-Improvement》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：A-OKVQA, MMBench, SEEDBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have achieved remarkable performance across vision-language tasks, but their progress depends heavily on large-scale, high-quality multimodal data that are costly to annotate. Self-augmentation offers a promising alternative by enabling models to expand their own training data without external supervision. However, existing MLLM self-augmentation methods are largely text-centric, while image augmentation remains underexplored and typically relies on generic or handcrafted transformations that are weakly aligned with the model's actual incapability. We propose Failure-informed Image Self-Augmentation (\textbf{FISA}), a framework for MLLM self-improvement that constructs augmented images from the model's own failure cases. Our method generates visually challenging yet answer-preserving image complications, verifies their utility through self-examination, and applies dual fidelity filtering to avoid semantic distortion. Experiments on visual question answering benchmarks show that the proposed method consistently improves performance across both in-distribution and out-of-distribution settings. Further experiments validate the compatibility of FISA with existing textual self-augmentation approaches, the superior data efficiency of the synthesized samples over generic image augmentation baselines, and the practical effectiveness of the proposed filtering strategy.

</details>

---

### [[20_Research/Papers/具身智能/LiLa-WAM_Lightweight_Latent_Reasoning_World-Action_Model_for_Robotic_Manipulation|LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation]]

![[assets/2608.03701_figure.png|800]]

- **arXiv**: [2608.03701](https://arxiv.org/abs/2608.03701)
- **PDF**: https://arxiv.org/pdf/2608.03701
- **详细分析**: [[20_Research/Papers/具身智能/LiLa-WAM_Lightweight_Latent_Reasoning_World-Action_Model_for_Robotic_Manipulation|LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation]]
- **作者**: Fan Yang, Yuting Su, Xiaobo Wang, Yuncheng You, Fugui Fan, Yuting Wu, Minghui Wu, Chenxu Zhao, JiaHong Ning, Peiguang Jing
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 1.2，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Interleave-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action modeling has emerged as a promising paradigm for robotic control, as it empowers models to go beyond reacting to observations and anticipate how a scene will evolve. However, existing WAMs often incur substantial computational overhead. Pixel-space methods often allocate substantial capacity to visual details that may not be directly relevant to control, while some latent-space methods require multi-stage training to construct the reasoning space. The resulting training cost can make such methods difficult to train under modest computational budgets. In this work, we propose LiLa-WAM, a lightweight world-action model that reasons about the future in a compact latent space and can be trained end-to-end on a single 24GB GPU. Its core design is a compact latent reasoning space jointly shaped by future-state prediction and action generation, which keeps the model lightweight while remaining well aligned with control. For task specification, we further propose the Visual Transition Token(VTT), a language-free task representation that encodes each task as a direction in visual feature space. Experiments on RoboTwin~2.0, LIBERO, and real-robot tasks demonstrate LiLa-WAM's effectiveness, achieving 90.48\% success across 50 RoboTwin tasks with single-GPU training.

</details>

---

### [[20_Research/Papers/具身智能/PhyAI_Real-Time_Physical_AI_at_the_Edge,_Scalable_Rollouts_in_the_Cloud|PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud]]

![[assets/2608.03682_figure.png|800]]

- **arXiv**: [2608.03682](https://arxiv.org/abs/2608.03682)
- **PDF**: https://arxiv.org/pdf/2608.03682
- **详细分析**: [[20_Research/Papers/具身智能/PhyAI_Real-Time_Physical_AI_at_the_Edge,_Scalable_Rollouts_in_the_Cloud|PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud]]
- **作者**: Chenghua Wang, Daliang Xu, Dongqi Cai, Duojin Sun, Hao Zhang, Haoze Qian, Huaiyuan Zhang, Jinshuo Cui, Kezhao Zhao, Longxi Gao, Mengwei Xu, Rongjie Yi...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Cosmos3-Nano-Policy-DROID, GigaWorld, LingBot-VLA, OpenVLA, RynnBrain-VLA, RynnVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical AI policies require inference throughout their lifecycle, including model evaluation, cloud reinforcement learning rollout, edge GPU serving, and onboard deployment. Although these settings share the same checkpoint and action semantics, they often rely on separate inference programs. To unify them, we build PhyAI, a Physical AI inference engine with a single runtime that keeps architecture-specific conditioning, solver, cache, and output logic in model adapters while sharing graph execution, kernels, memory management, and parallel services. The same codebase runs vision-language-action (VLA) models and world-action models (WAMs) on single or multiple GPUs across onboard, edge, and cloud deployments. We used the adapter interface to add MiniCPM-Robot on the day of its release. PhyAI achieves 1.40x-4.65x speedups over the official implementations of pi0, pi0.5, GR00T N1.7, and MiniCPM-Robot. On Cosmos3-Nano-Policy-DROID it reduces latency from 2.46 to 1.18 s on eight H20 GPUs (CFG=2, TP=4), a 2.08x speedup. Specialized runtimes remain faster in several configurations, so our goal is one runtime with competitive latency rather than the fastest result in every case. Detailed profiles reveal why different models need different execution policies: on a Hopper-series GPU at batch size one, the pi0.5 action expert accounts for 8.8% of FLOPs but 57.2% of latency; at batch size 32 its share drops to 13.5% and throughput reaches about 100 samples/s. Cosmos3 remains generation-dominated and gains only 14.3% throughput as batch size increases from 1 to 16. We further introduce the control-time Roofline, which distinguishes inference-bound from environment-bound control; the measured pi0.5 points on four LIBERO suites are environment-bound while Cosmos3 stays inference-bound. Code and benchmarks: https://github.com/mingti-org/phyai.

</details>

---

### [[20_Research/Papers/大模型/Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for_Decision_Agents|Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents]]

![[assets/2608.03606_figure.png|800]]

- **arXiv**: [2608.03606](https://arxiv.org/abs/2608.03606)
- **PDF**: https://arxiv.org/pdf/2608.03606
- **详细分析**: [[20_Research/Papers/大模型/Learning_Clinical-Trial_Strategy_Offline_Policy_Training_for_Decision_Agents|Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents]]
- **作者**: William Bolton, Philip Torr
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.6，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical development is sequential decision-making under uncertainty, where a sponsor must plan a portfolio of experiments from heterogeneous evidence. We study this setting by framing oncology clinical development as an offline decision-making problem in which an agent predicts the next six-month trial portfolio of an oncology drug program from information available at the decision date. To support this, we construct a temporal dataset that combines 31.7k heterogeneous public data records, including trial registries, regulatory reviews, sponsor filings, utilization data, and epidemiology, into 881 offline decision episodes across 45 historical programs. We compare four offline objectives: behavioral cloning, reward-weighted behavioral cloning, learned-reward training, and value-based implicit Q-learning against four frontier LLM agents that share a common date-gated retrieval scaffold across held-out drug, sponsor, drug-class, and temporal splits. Models trained offline outperform the non-fine-tuned baselines, particularly in the post-August 2025 contamination-clean holdout. Reward-weighted behavioral cloning performs the best, obtaining 46.2% indication F1 and 14.2% strict F1 against 25.0% and 2.1%, respectively, for the best-performing tool agent on each metric. These results suggest that structured offline learning can teach agents to plan clinical experiments.

</details>

---

### [[20_Research/Papers/大模型/DiagChain_A_Diagnostic_Benchmark_for_Evaluating_LLM_Agents_on_Evidence-Grounded_Attack_Chain_Reconstruction|DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction]]

![[assets/2608.03591_figure.png|800]]

- **arXiv**: [2608.03591](https://arxiv.org/abs/2608.03591)
- **PDF**: https://arxiv.org/pdf/2608.03591
- **详细分析**: [[20_Research/Papers/大模型/DiagChain_A_Diagnostic_Benchmark_for_Evaluating_LLM_Agents_on_Evidence-Grounded_Attack_Chain_Reconstruction|DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction]]
- **作者**: Xuyang Liu, Yibin Han, Zhenwei Zhang, Kai Chang, Zhiwei Xu, Tian Qiu, Weixian Deng, Jiabao Gao, Xiaolin Peng, Hai Wan, Xibin Zhao
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AttackSeqBench, AuditBench, CTIBench, ExCyTIn-Bench, HIDBench, SIABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents offer a promising approach to attack chain reconstruction by retrieving and interpreting heterogeneous telemetry to infer ordered attacker actions. However, existing benchmarks mainly evaluate final outputs or aggregate accuracy, providing limited insight into how errors arise and propagate across intermediate reasoning stages. We present DiagChain, a diagnostic benchmark for evidence-grounded attack chain reconstruction that enables stage-wise evaluation of LLM agents. DiagChain includes MAIN-69, a suite of 69 scenarios spanning multiple operating systems, evidence noise levels, and chain lengths. It further introduces Evidence-Centric Retrieval-Augmented Generation (ECRAG), which couples evidence retrieval with an evolving structured representation of the reconstructed chain. Five complementary metrics are introduced to assess distinct stages of the reconstruction process and support systematic failure diagnosis. Based on evaluations using 6 LLMs, DiagChain reveals that even the strongest configuration succeeds on only 39.6% of the 849 reference steps in MAIN-69. Our analysis further shows that smaller models struggle with the more basic task of incorporating retrieved evidence into their outputs, whereas larger models can proceed to later steps, where correctly ordering that evidence becomes the main bottleneck. These results validate the importance of diagnostic evaluation beyond end-to-end accuracy and provide actionable insights for improving evidence-grounded cybersecurity agents.

</details>

---

### [[20_Research/Papers/大模型/Training_Documents_Reranker_with_Search_Rubrics_for_Deep_Research_Agent|Training Documents Reranker with Search Rubrics for Deep Research Agent]]

![[assets/2608.03527_figure.png|800]]

- **arXiv**: [2608.03527](https://arxiv.org/abs/2608.03527)
- **PDF**: https://arxiv.org/pdf/2608.03527
- **详细分析**: [[20_Research/Papers/大模型/Training_Documents_Reranker_with_Search_Rubrics_for_Deep_Research_Agent|Training Documents Reranker with Search Rubrics for Deep Research Agent]]
- **作者**: Wenhan Liu, Yu Lu, Qiaolin Xia, Hui Xu, Tong Zhao, Jian Xi, Yutao Zhu, Haijin Liang, Haibo Shi, Hao Wang, Zhicheng Dou
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.05（加权：大模型 0.85，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Training Documents Reranker with Search Rubrics for Deep Research Agent》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DeepResearchBench, HealthBench, HotpotQA, ResearchQA, WebWalkerQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval systems help deep research agents generate high-quality answers by providing relevant documents. However, existing retrievers typically select documents through relevance matching, while individually well-matched top-$k$ documents may not form a \textit{set} that satisfies the complex information needs of an agent query (\eg, diverse, concise and authoritative documents). In this paper, we propose search-oriented rubrics that \textit{explicitly} define the requirements that high-quality document sets should satisfy for each agent query. Our search rubrics are organized into a hierarchical structure and synthesized using a powerful LLM. Based on these search rubrics, we further train a document reranker \textbf{RubricRanker} to select a high-quality subset from retrieved documents. We design a two-stage training framework that consists of rubrics-guided supervised fine-tuning and rubric-based reinforcement learning. Extensive experiments demonstrate that RubricRanker outperforms the strongest baseline by 2.6 points on four deep research benchmarks and generalizes well to five RAG benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Hybrid_LLM-Augmented_Reinforcement_Learning_Agents_for_Complex_Sequential_Decision_Tasks|Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks]]

![[assets/2608.03502_first_page.png|800]]

- **arXiv**: [2608.03502](https://arxiv.org/abs/2608.03502)
- **PDF**: https://arxiv.org/pdf/2608.03502
- **详细分析**: [[20_Research/Papers/大模型/Hybrid_LLM-Augmented_Reinforcement_Learning_Agents_for_Complex_Sequential_Decision_Tasks|Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks]]
- **作者**: Christophe D. Hounwanou, John Emeka Eze, Yaé Ulrich Gaba
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.02（加权：大模型 0.9，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents. However, LLM-based agents struggle with long-horizon sequential decision tasks that require precise action optimization and environment interaction. Reinforcement Learning (RL), while effective for sequential control, often lacks the high-level abstraction and task decomposition abilities needed for complex scenarios. This paper introduces an LLM-Augmented Reinforcement Learning Agent that integrates LLM-driven planning with RL-based action optimization. The proposed architecture leverages the LLM to generate subgoals, structured plans, and contextual guidance, while the RL agent refines low-level actions through interaction with the environment. Experiments on sequential decision tasks demonstrate improved sample efficiency, higher success rates, and more coherent action trajectories compared to RL-only and LLM-only baselines. This hybrid paradigm highlights a promising direction for building more capable autonomous systems.

</details>

---

### [[20_Research/Papers/其他/WeClawArena_An_Auditable_Sandbox_and_Benchmark_for_Cross-User_Agents_Collaboration_and_Security_in_Human-Centered_Agent_Networks|WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks]]

![[assets/2608.03499_figure.png|800]]

- **arXiv**: [2608.03499](https://arxiv.org/abs/2608.03499)
- **PDF**: https://arxiv.org/pdf/2608.03499
- **详细分析**: [[20_Research/Papers/其他/WeClawArena_An_Auditable_Sandbox_and_Benchmark_for_Cross-User_Agents_Collaboration_and_Security_in_Human-Centered_Agent_Networks|WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks]]
- **作者**: Prince Zizhuang Wang, Aojie Yuan, Haiyue Zhang, Xiyang Hu, Yue Zhao, Shuli Jiang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, Security, Systems

#### 研究背景与动机

《WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AgentSocialBench, MultiAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in persistent personal-agent frameworks are making human-centered agent networks realistic deployment targets: each user can be served by an AI agent that acts on the user's behalf, maintains state, and communicates with other agents through social and task relations. In these networks, everyday tool use becomes multi-party owned-agent collaboration over personal workspaces, where files, records, tools, and policies are not directly visible across owners. Existing agent benchmarks study tool use and collaboration, but they do not provide an end-to-end sandbox for verifiable cross-user agent collaboration with realistic user digital workspaces or test how harmful actions can travel through the human-centered agent network. We introduce WeClawArena, an auditable benchmark and runtime sandbox for multi-party owned-agent collaboration over personal workspaces. WeClawArena targets collaborative tool-use tasks in which personal workspaces serve as both operational tools and personal constraints. The benchmark contains 124 base tasks across six cross-user task domains and expands them into 620 scenario variants, with one benign control and four attack-vector variants per base task. The sandbox records peer messages, tool calls, resource operations, governed decisions, and final workspace states. WeClawArena reports utility and attack success rate separately and audits attack success from bounded runtime evidence, supporting diagnosis of task breakdown, privacy leakage, poisoned evidence, and invalid authority paths.

</details>

---

### [[20_Research/Papers/机器人/Principles_of_Robot_Autonomy|Principles of Robot Autonomy]]

![[assets/2608.03496_first_page.png|800]]

- **arXiv**: [2608.03496](https://arxiv.org/abs/2608.03496)
- **PDF**: https://arxiv.org/pdf/2608.03496
- **详细分析**: [[20_Research/Papers/机器人/Principles_of_Robot_Autonomy|Principles of Robot Autonomy]]
- **作者**: Daniele Gammelli, Joseph Lorenzetti, Katie Luo, Gioele Zardini, Marco Pavone
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Principles of Robot Autonomy》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots are moving rapidly from research labs into everyday life - on roads, in the air, in warehouses, and in space. Robot autonomy is no longer solely an academic pursuit, but a collection of mature, field-tested methods and tools that practitioners rely on in real-world deployments. This book offers a clear, unified introduction to the methods that make this possible. Built on decades of teaching at Stanford, the text develops the core elements of modern autonomy stacks within a single conceptual framework, bridging classical robotics and modern physical AI. Every major topic is paired with hands-on Jupyter notebooks and implementation-driven exercises, so readers build practical intuition alongside theoretical understanding. The result is a principled, accessible, and deployment-aware foundation for anyone seeking to design, analyze, or contribute to the next generation of autonomous systems. This is a comprehensive resource for students, engineers, and researchers entering one of today's fastest-growing fields.

</details>

---

### [[20_Research/Papers/具身智能/Continue_or_Replan_Bernoulli-Continuation_Policy_Learning_for_Adaptive_Horizon_Execution|Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution]]

![[assets/2608.03483_figure.png|800]]

- **arXiv**: [2608.03483](https://arxiv.org/abs/2608.03483)
- **PDF**: https://arxiv.org/pdf/2608.03483
- **详细分析**: [[20_Research/Papers/具身智能/Continue_or_Replan_Bernoulli-Continuation_Policy_Learning_for_Adaptive_Horizon_Execution|Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution]]
- **作者**: Weichen Xu, Zhenhua Liu, Lin Luo, Yaobo Liang, Chengtang Yao, Qingyu Mei, Jian Cao, Xixin Cao, Xing Zhang, Jiaolong Yang, Baining Guo
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.9，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, Real-World, SimpleVLA-RL, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing chunk-based Vision-Language-Action (VLA) models execute a fixed number of actions (i.e., execution horizon) before replanning, turning replanning into a task-agnostic periodic schedule that is independent of task progress. As a result, when no replanning boundary falls before a critical manipulation stage, it is executed from a stale chunk rather than a freshly replanned one. To address this limitation, we propose Bernoulli-Continuation Policy (BCP), a lightweight, plug-and-play framework for adaptive horizon execution that keeps the base VLA frozen. Given a fixed-length action chunk, its continuation head decomposes execution-horizon selection into a sequence of continue-or-replan decisions, which imposes an ordinal, prefix-sharing inductive bias over candidate horizons rather than treating them as independent classes. Since the optimal horizon for each chunk is not observable, we train this head with reinforcement learning from trajectory-level outcomes and introduce a Replanning-Efficiency Reward that jointly rewards task success and efficient VLA usage, discouraging the policy from collapsing to unnecessarily short horizons. On RoboTwin 2.0 with LingBot-VLA as the base policy, BCP improves the average success rate by +11.08% on 13 low-success tasks and from 89.88% to 93.94% (+4.06%) across all 50 tasks. Although trained only under the Clean setting, BCP generalizes to the Randomized setting, raising the average success rate by +4.06%. It also transfers to a different base policy $π_{0.5}$, achieving a better result on LIBERO (+1.7%) and, notably, on the harder LIBERO-PRO (+6.8%). On a real robot, BCP lifts success from 74% to 92% and from 44% to 84% on two manipulation tasks. Meanwhile, its negligible overhead, combined with higher success, makes BCP's overall runtime even lower than the fixed-horizon baselines.

</details>

---

### [[20_Research/Papers/大模型/LeanMem_Simple_and_Efficient_Long-Term_Memory_for_LLM_Agents|LeanMem: Simple and Efficient Long-Term Memory for LLM Agents]]

![[assets/2608.03463_figure.png|800]]

- **arXiv**: [2608.03463](https://arxiv.org/abs/2608.03463)
- **PDF**: https://arxiv.org/pdf/2608.03463
- **详细分析**: [[20_Research/Papers/大模型/LeanMem_Simple_and_Efficient_Long-Term_Memory_for_LLM_Agents|LeanMem: Simple and Efficient Long-Term Memory for LLM Agents]]
- **作者**: Yuxin Liao, Le Wu, Min Hou, Hao Liu, Han Wu, Zishu Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LeanMem: Simple and Efficient Long-Term Memory for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory is essential for LLM-based agents to sustain interactions and reliably leverage distant history. However, existing memory systems typically process heterogeneous dialogue content through a uniform summarization and retrieval pipeline, leading to either excessive token consumption or irreversible loss of fine-grained evidence. We argue that historical dialogue content should be handled differently according to its compressibility, temporal dynamics, and fidelity requirements. Based on this insight, we propose LeanMem, a lightweight long-term memory framework. LeanMem first filters out low-value content, then stores informative segments as compact profile memory, temporally structured event memory, or source-grounded record memory, depending on the nature of the information. During maintenance, only dynamically evolving event memories are selectively updated, avoiding redundant consolidation of stable profiles and immutable records. During inference, LeanMem dynamically selects memory types and allocates retrieval budgets according to query-specific evidence demands, assembling relevant evidence on demand. On LoCoMo and LongMemEval-S with GPT-4.1-mini and Qwen3-8B, LeanMem improves accuracy over the strongest memory-based baseline in every setting, by up to 15.1 points, at the lowest or near-lowest construction cost, inference tokens, and latency. The code and datasets are included in the supplementary materials.

</details>

---

### [[20_Research/Papers/机器人/Shaping_Wind-Tunnel_Airflow_for_Unmanned_Aerial_Vehicles_using_Online_Learning|Shaping Wind-Tunnel Airflow for Unmanned Aerial Vehicles using Online Learning]]

![[assets/2608.03378_first_page.png|800]]

- **arXiv**: [2608.03378](https://arxiv.org/abs/2608.03378)
- **PDF**: https://arxiv.org/pdf/2608.03378
- **详细分析**: [[20_Research/Papers/机器人/Shaping_Wind-Tunnel_Airflow_for_Unmanned_Aerial_Vehicles_using_Online_Learning|Shaping Wind-Tunnel Airflow for Unmanned Aerial Vehicles using Online Learning]]
- **作者**: Ghadeer Elmkaiel, Michael Muehlebach
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Shaping Wind-Tunnel Airflow for Unmanned Aerial Vehicles using Online Learning》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The development and testing of advanced aerial robots require experiments in controlled environments with tailored airflow profiles. This paper presents an online learning algorithm for controlling the complex airflow field in a multi-fan vertical wind tunnel. Our method combines a simplified physical model with iterative, measurement-based learning, enabling sample-efficient convergence to desired airflow distributions. We demonstrate the method's versatility by generating complex airflow, such as uniform, Gaussian, and parabolic profiles. Crucially, we show that our algorithm can produce an airflow profile specifically designed for passive soaring, greatly enhancing flight performance of a soaring robot. Variability, practical utility, and robustness of our approach are further highlighted by successful operation with a varying number of fans.

</details>

---

### [[20_Research/Papers/大模型/Screenshots_or_Tools_Eliciting_Tool_Use_and_Managing_Multimodal_Context_in_Hybrid_GUI-MCP_Computer-Use_Agents|Screenshots or Tools? Eliciting Tool Use and Managing Multimodal Context in Hybrid GUI-MCP Computer-Use Agents]]

![[assets/2608.03327_figure.png|800]]

- **arXiv**: [2608.03327](https://arxiv.org/abs/2608.03327)
- **PDF**: https://arxiv.org/pdf/2608.03327
- **详细分析**: [[20_Research/Papers/大模型/Screenshots_or_Tools_Eliciting_Tool_Use_and_Managing_Multimodal_Context_in_Hybrid_GUI-MCP_Computer-Use_Agents|Screenshots or Tools? Eliciting Tool Use and Managing Multimodal Context in Hybrid GUI-MCP Computer-Use Agents]]
- **作者**: Siqi Fan, Minghao Li, Xiaoqian Ma, Wenhui Tan, Xiusheng Huang, Juntong Wu, Liujie Zhang, Shuo Shang, Weihang Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Screenshots or Tools? Eliciting Tool Use and Managing Multimodal Context in Hybrid GUI-MCP Computer-Use Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：AndroidWorld, ComputerRL, DigiRL, MCPWorld, OSWorld, WebRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hybrid computer-use agents can act through screenshots or call text tools. We find that having a tool available does not settle which way the effect goes. Under one identical GUI-MCP harness on the OSWorld-MCP benchmark (309 tasks), the same MCP tools improve a reasoning model by +4.0pp and degrade a non-reasoning model by -5.9pp (5 runs each, both beyond 2 SE). What separates the two is tool-decision behavior. The non-reasoning policy ignores, misnames, or falsely terminates around tools. The reasoning model avoids these failures, yet still calls a tool on only 55/309 tasks, 23.9% of the tool-reachable ones. We call this shortfall the adoption gap. Both levels of the problem share one cause: the model already has a cheaper route and is never trained to take it. Multi-turn RL probes that cause. At the action level, a dense tool bonus raises spreadsheet adoption 0.03 -&gt; 0.33 and carries into greedy decoding, but held-out accuracy does not follow. Behavior is steerable; competence is not. The bottleneck lies in tool-call semantics. At the context level, a successful tool call often makes the next screenshot redundant. Dropping it and halving image history cuts input tokens by about a third, at a small accuracy cost. Retraining under the same observation rule removes that cost. The compressed agent then reaches 37.8% against 33.0% for the uncompressed operating point, at 53% of the input cost, and closes the rich-lean gap on a pre-registered degraded subset to zero. Tools help when the model chooses and integrates them, and current hybrid agents leave many such choices unused.

</details>

---

### [[20_Research/Papers/具身智能/Structure-Aware_Robust_Fine-Tuning_Defending_Vision-Language-Action_Robots_Against_Physical_Attention_Hijacking|Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking]]

![[assets/2608.03231_figure.png|800]]

- **arXiv**: [2608.03231](https://arxiv.org/abs/2608.03231)
- **PDF**: https://arxiv.org/pdf/2608.03231
- **详细分析**: [[20_Research/Papers/具身智能/Structure-Aware_Robust_Fine-Tuning_Defending_Vision-Language-Action_Robots_Against_Physical_Attention_Hijacking|Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking]]
- **作者**: Jinquan Zhang, Dongfu Yin, Run Yang, Yufeng Yan, Zhen Tian, F. Richard Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ADVLA, AttackVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch. To demonstrate the threat, we propose Attention-Guided Semantic Disruption (AGSD), an Expectation-over-Transformation (EOT) optimized printable patch that jointly (i) concentrates action-to-vision attention on the patch and (ii) disrupts vision-language semantic alignment, yielding strong cross-task and cross-architecture transfer. To mitigate such attacks, we introduce Structure-Aware Robust Fine-Tuning (SARF), a zero-inference-overhead defense that fine-tunes only the visual encoder using feature anchoring, policy-critical attention correction, and language-guided geometric consistency restricted to semantically relevant regions. On LIBERO, SARF reduces OpenVLA's failure rate under AGSD from 100% to 14.2%-56.8% (28.6% average) across suites while preserving clean performance, and on a real PiPER manipulator it improves average success under AGSD from 23.0% to 65.0%. These results highlight mechanism-level robustness as a practical path to securing VLA robots against physical attention hijacking.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Reinforcement_Learning_with_Self-Distilled_Reward_Shaping|Agentic Reinforcement Learning with Self-Distilled Reward Shaping]]

![[assets/2608.03223_figure.jpg|800]]

- **arXiv**: [2608.03223](https://arxiv.org/abs/2608.03223)
- **PDF**: https://arxiv.org/pdf/2608.03223
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Reinforcement_Learning_with_Self-Distilled_Reward_Shaping|Agentic Reinforcement Learning with Self-Distilled Reward Shaping]]
- **作者**: Ranxu Zhang, Guinan Chen, Chenshaodong, Jinghao Lin, Xiaozhou Xu, Sunzhe, Yanyong Zhang, Chao Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Agentic Reinforcement Learning with Self-Distilled Reward Shaping》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, KDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning enables LLM agents to learn through interaction, but sparse trajectory-level rewards reveal success without identifying which intermediate decisions deserve credit. Training-only privileged skills can provide denser supervision by allowing the same frozen policy snapshot to rescore fixed tokens from skill-free trajectories while conditioned on task-matched procedural skills. Existing methods, however, do not jointly calibrate teacher scores across interaction steps, relate teacher confidence to realized returns, and integrate the resulting signal into native reward-to-advantage construction. We introduce Agentic Reinforcement Learning with Self-Distilled Reward Shaping (ADRS), a framework for constructing return-associated token-level credit for multi-turn language agents. ADRS centers and normalizes privileged token scores within each step, modulates them with a return-associated Teacher Value Advantage (TVA) gate based on within-group confidence--return association, and incorporates the gated token signal into native RL credit construction. Together, these components determine what the teacher prefers, when that preference is return-relevant, and how it enters the native reinforcement-learning credit path, while keeping rollouts and inference skill-free. Finally, experiments across three interactive benchmarks show that ADRS consistently improves performance on long-horizon tasks, with gains persisting across RL backbones, reduced-data settings, unseen tasks, and extended training. For anonymous review, our code is available at the following the link: https://github.com/gitrxh/ADRS-arxiv

</details>

---

### [[20_Research/Papers/强化学习/GROW_Group-Relative_Advantage-Weighted_On-Policy_Reinforcement_Learning_of_Autoregressive-Diffusion_Text-to-Speech_model|GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model]]

![[assets/2608.03215_first_page.png|800]]

- **arXiv**: [2608.03215](https://arxiv.org/abs/2608.03215)
- **PDF**: https://arxiv.org/pdf/2608.03215
- **详细分析**: [[20_Research/Papers/强化学习/GROW_Group-Relative_Advantage-Weighted_On-Policy_Reinforcement_Learning_of_Autoregressive-Diffusion_Text-to-Speech_model|GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model]]
- **作者**: Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma, Yakun Song, Zhikang Niu, Qi Chen, Wenming Tu, Haitao Li, Shan Yang, Xie Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for flow-matching text-to-speech is complicated by deterministic ODE sampling: trajectory-level policy-gradient methods typically convert the ODE into an SDE and track per-step likelihood ratios, introducing stochastic perturbations and substantial overhead. We propose GROW, a group-relative advantage-weighted on-policy RL method that acts directly on the standard flow-matching objective. For each prompt, GROW samples a group of on-policy utterances, separately standardizes intelligibility and speaker-similarity rewards within the group, and combines them to reweight flow-matching regression. A Wasserstein-2 velocity penalty anchors the updated model to a frozen pretrained reference. A group-mean reward baseline is introduced to convert reward weighting into advantage weighting. For strong pretrained TTS models with concentrated rewards, positive exponential weighting is dominated by reward-agnostic self-imitation, whereas a zero-mean signed advantage preserves effective within-group credit assignment. Instantiated on DiTAR and evaluated on LibriSpeech and Seed-TTS EN/ZH, GROW reduces average WER from 2.016 to 1.558 and raises speaker similarity from 0.676 to 0.715 while keeping UTMOS. With 10-NFE training rollouts and 32-NFE evaluation, GROW retains comparable performance while training 2.9x faster than 32-NFE DiTAR-GRPO. We will open-source complete GROW codes, faithful DiTAR reproduction, and all model checkpoints.

</details>

---

### [[20_Research/Papers/大模型/EduClaw-Bench_A_Long-Horizon_Benchmark_for_Pedagogical_LLM_Agents_with_Simulated_Learners|EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners]]

![[assets/2608.03206_figure.png|800]]

- **arXiv**: [2608.03206](https://arxiv.org/abs/2608.03206)
- **PDF**: https://arxiv.org/pdf/2608.03206
- **详细分析**: [[20_Research/Papers/大模型/EduClaw-Bench_A_Long-Horizon_Benchmark_for_Pedagogical_LLM_Agents_with_Simulated_Learners|EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners]]
- **作者**: Unggi Lee, Sookbun Lee, Yeil Jeong, Eunjoo Lee, Minchul Shin, Hoilym Kwon
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, EduAgentBench, EduClaw-Bench, ISD-Agent-Bench, MathTutorBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) power educational applications from tutoring to essay scoring, but each is a point solution to a single task, and only recently have these point solutions been integrated into agents operating over a learning management system (LMS). Yet tutoring is long-horizon, since a learner improves over days and weeks rather than in a single turn, and no benchmark evaluates an agent tutor across a sustained relationship. We introduce EduClaw-Bench, a benchmark that places an agent tutor in a continuous 30-day relationship with a simulated learner grounded in knowledge tracing (KT), whose knowledge-concept mastery, from a KT model trained on real-student data, drives its answers and is probed for learning gain across 55 scenarios. Each agent is scored on three primary axes (learning gain, responsiveness, and helpfulness) and two curriculum-design axes (Gagné and Rosenshine), with helpfulness and the curriculum axes judged by a cross-family panel of three LLM judges. Evaluating 10 agent adapters over three base-model tiers yields two findings that single-tier, single-session evaluation cannot reach. First, tutoring quality belongs to the base model and the agent harness together rather than either alone. Second, almost no combination sustains good tutoring over the full horizon. A calibration check ($\text{ECE}=0.049$) and a live-classroom field study confirm that the simulated learner and its measurements track reality. Our work is a step toward trustworthy AI tutors for future education.

</details>

---

### [[20_Research/Papers/大模型/Adversarial_Stress_Testing_of_Role-Playing_Language_Agents_using_Multi-Agent_Evaluation|Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation]]

![[assets/2608.03166_figure.png|800]]

- **arXiv**: [2608.03166](https://arxiv.org/abs/2608.03166)
- **PDF**: https://arxiv.org/pdf/2608.03166
- **详细分析**: [[20_Research/Papers/大模型/Adversarial_Stress_Testing_of_Role-Playing_Language_Agents_using_Multi-Agent_Evaluation|Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation]]
- **作者**: Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HarmBench, RAS-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Role-Playing Language Agents (RPLAs) are increasingly deployed in high-stakes applications such as healthcare assistance, customer support, and education, where maintaining consistent personas, ethical constraints, and behavioral coherence under adversarial pressure is critical. Existing evaluation approaches rely on static benchmarks or isolated single-turn prompts that fail to capture cumulative behavioral failures emerging over extended interactions. We present a modular multi-agent platform for adversarially stress-testing RPLAs through structured, multi-turn dialogue. The system coordinates three agents: a strategy-driven Interrogator Agent that applies six progressive adversarial strategies, a Target Agent representing the RPLA under evaluation, and an automated Judging Agent that scores behavior across role fidelity, drift, ethical deviation, and consistency dimensions. Through experiments across three personas and three LLM families, we demonstrate that multi-strategy adversarial evaluation reveals failure modes invisible to single-strategy testing, reducing overall robustness scores by 0.17--0.20 points on average. Cross-model validation confirms consistent degradation patterns across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with Authority Challenge and Emotional Manipulation emerging as the most effective attack strategies. Automated judging achieves strong human alignment ($r = 0.82$, Fleiss' $κ= 0.71$). This work is released as an open-source platform to support AI safety and reproducible RPLA benchmarking. While the framework enables systematic discovery of failure modes, we acknowledge potential ethical risks associated with adversarial testing methodologies and emphasize responsible usage for improving AI safety.

</details>

---

### [[20_Research/Papers/大模型/Verifiable_Memory_Learning_Unified_Memory_Management_with_Local_and_Global_Verifiers_for_Large_Language_Model_Agents|Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents]]

![[assets/2608.03137_figure.png|800]]

- **arXiv**: [2608.03137](https://arxiv.org/abs/2608.03137)
- **PDF**: https://arxiv.org/pdf/2608.03137
- **详细分析**: [[20_Research/Papers/大模型/Verifiable_Memory_Learning_Unified_Memory_Management_with_Local_and_Global_Verifiers_for_Large_Language_Model_Agents|Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents]]
- **作者**: Xiaolong Sun, Qichao Wang, Hangyu Li, Liang Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents must retain reusable information, control a bounded active context, and recover earlier evidence during long-horizon interaction. Existing methods commonly optimize long-term memory (LTM) and short-term memory (STM) separately, while unified policies are often trained primarily with trajectory-level feedback, which provides weak credit for individual memory decisions. We present Verifiable Memory (VerMem), a framework that represents LTM, active context, and episodic history as distinct states and controls them with one memory operation policy. Seven atomic operations let the policy add, revise, or soft-delete LTM entries; retrieve LTM into the active context; filter or summarize the active context; and restore selected episodic fragments. VerMem is initialized by supervised fine-tuning and trained with a three-stage reinforcement-learning curriculum. The local verifier scores executable memory transitions, and a global verifier assesses evidence coherence and terminal-memory consistency after task completion. These scores are combined with programmatically computed task, evidence-recall, efficiency, and constraint signals through hierarchical credit assignment. The verifiers are used only during training. Across five benchmarks and two LLM backbones, VerMem achieves the best result on the vast majority of reported metrics and consistently outperforms strong memory baselines. Under controlled online-token budgets on three interactive benchmarks, it also achieves the strongest efficiency--performance frontier among the compared methods. Code is available at https://github.com/Sun-SYSU-24/VerMem.

</details>

---

### [[20_Research/Papers/机器人/DigitCode_Symbolic_Tokenization_of_Hand_Motion_by_Anatomical_Units|DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units]]

![[assets/2608.03127_figure.png|800]]

- **arXiv**: [2608.03127](https://arxiv.org/abs/2608.03127)
- **PDF**: https://arxiv.org/pdf/2608.03127
- **详细分析**: [[20_Research/Papers/机器人/DigitCode_Symbolic_Tokenization_of_Hand_Motion_by_Anatomical_Units|DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units]]
- **作者**: Haoyu Gu, Haotian Lu, Jingrun Du, Xiao-Ping Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hand motion carries the finest-grained information in human activity, yet the representations behind hand generation, understanding, and robot learning are overwhelmingly continuous--joint angles or MANO parameters. These are accurate but unstructured: a finger cannot be indexed or edited as a symbol, and nothing marks a pose as anatomically valid. Discrete symbolic representations supply exactly this structure, and Hand Labanotation (HL) has shown they are feasible for the hand, writing motion as a T x 40 grid of one fixed direction symbol per bone. Building on this grid, we ask the question underneath it: the anatomical unit a symbol should span--bone, finger, or whole hand. DigitCode answers it by adapting, grouping, and layering HL's alphabet along the hand's unit hierarchy within one code, cutting the symbolic representation's quantization error by three quarters. The lever is the unit, not the quantizer family: at a fixed unit, training-free and learned strong quantizers are interchangeable on reconstruction, while moving down the anatomical hierarchy is what shifts accuracy. The hierarchy also tracks what downstream tasks need. Because a finger is a genuine, enumerable unit, one per-finger token doubles as a training-free, editable handle for jobs a continuous representation cannot address--repairing malformed generated hands, and retargeting them onto robots. We release HandTok, a reproducible testbed, so hand tokenizers can be compared unit-for-unit. Project page: https://digitcode-demo.github.io.

</details>

---

### [[20_Research/Papers/大模型/Don't_Peek_at_the_Answer_Outcome-Masked_Group_Relative_Policy_Optimization_for_Label-Free_RLVR|Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR]]

![[assets/2608.03119_figure.png|800]]

- **arXiv**: [2608.03119](https://arxiv.org/abs/2608.03119)
- **PDF**: https://arxiv.org/pdf/2608.03119
- **详细分析**: [[20_Research/Papers/大模型/Don't_Peek_at_the_Answer_Outcome-Masked_Group_Relative_Policy_Optimization_for_Label-Free_RLVR|Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR]]
- **作者**: Yongshi Ye, Liang Zhang, Yidong Chen, Xiaodong Shi, Biao Fu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Don't Peek at the Answer: Outcome-Masked Group Relative Policy Optimization for Label-Free RLVR》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) improves LLM reasoning but typically relies on ground-truth (GT) answers, limiting scalability. Voting-based label-free RLVR replace gold supervision with answer-level consensus from model samples. However, collapse arises when the same answer-level signal is used both to estimate rewards and to drive token-level policy optimization, encouraging the model to directly reinforce answer tokens rather than improve reasoning. We propose OM-GRPO, a label-free RLVR framework that decouples reward estimation from policy optimization. OM-GRPO masks gradients on the answer span while retaining answer-level rewards through a soft consensus signal, shifting optimization pressure away from answer tokens. We further introduce Contrast-Augmented Reward, which refines reward estimation via low-cost pairwise comparisons over existing trajectories without additional rollouts. Across diverse reasoning benchmarks and three LLM backbones, OM-GRPO consistently outperforms existing label-free RLVR methods and matches supervised GT-reward training with stable optimization. This stability is particularly beneficial in the Test-Time Training setting, where OM-GRPO surpasses majority voting by 4.24 points.

</details>

---

### [[20_Research/Papers/具身智能/A_Hierarchical_Approach_to_Imitation_Learning_for_Manipulation_Tasks_Requiring_Time_Varying_Forces|A Hierarchical Approach to Imitation Learning for Manipulation Tasks Requiring Time Varying Forces]]

![[assets/2608.03103_figure.png|800]]

- **arXiv**: [2608.03103](https://arxiv.org/abs/2608.03103)
- **PDF**: https://arxiv.org/pdf/2608.03103
- **详细分析**: [[20_Research/Papers/具身智能/A_Hierarchical_Approach_to_Imitation_Learning_for_Manipulation_Tasks_Requiring_Time_Varying_Forces|A Hierarchical Approach to Imitation Learning for Manipulation Tasks Requiring Time Varying Forces]]
- **作者**: Rishabh Shukla, Adithya Santhosh, Shaili Gandhi, Samrudh Moode, Satyandra K. Gupta
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《A Hierarchical Approach to Imitation Learning for Manipulation Tasks Requiring Time Varying Forces》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies have shown strong performance in learning complex, multi-modal behaviors for robotic manipulation. However, their application to contact-rich disassembly tasks remains limited by a key trade-off: the iterative denoising process introduces inference latencies that makes high frequency control difficult, which is essential for realizing dynamic interactions such as chiseling and prying. Recent action-chunking techniques mitigate latency but use an open-loop execution window, rendering the system blind to rapid force transients caused by fracture events. To bridge this gap, we introduce the Diffusion Policy Augmented by Fast Trajectory Generation (DPA-FTG). Compared to recent visual-tactile approaches that focus on positional correction, DPA-FTG decouples low-frequency planning from high-frequency force regulation. At the high level ($5$ Hz), a conditional diffusion model predicts a sequence of latent parameters for selecting a strategy from a learned vocabulary of task primitives. At the low level ($60$ Hz), a lightweight, force-conditioned policy acts as a neural impedance controller, modulating execution in real-time to maintain contact stability. We validate our approach on a bimanual battery disassembly task involving the separation of a compliant sheet. Experimental evaluation demonstrates that DPA-FTG outperforms state-of-the-art baselines, including Reactive Diffusion Policy (RDP).

</details>

---

### [[20_Research/Papers/强化学习/SMOPD_Multi-Reward_Reinforcement_Learning_via_Specialize-and-Merge_Online_Policy_Distillation|SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation]]

![[assets/2608.03092_figure.png|800]]

- **arXiv**: [2608.03092](https://arxiv.org/abs/2608.03092)
- **PDF**: https://arxiv.org/pdf/2608.03092
- **详细分析**: [[20_Research/Papers/强化学习/SMOPD_Multi-Reward_Reinforcement_Learning_via_Specialize-and-Merge_Online_Policy_Distillation|SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation]]
- **作者**: Wen Wang, Jiahua Bao, Tu Yongsiqi, Yihao Liu, Haotian Zhou, Haoxuan Ma, Mengyu Zhou, Wenkui Fan, Junwei He, Xiaoxi Jiang, Guanjun Jiang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We aim to improve model performance in multi-reward reinforcement learning training process. Existing Group reward-Decoupled Normalization Policy Optimization (GDPO) has mitigated the issue of reward signals masking one another during direct scalarization by normalizing each reward dimension separately before aggregation. However, our experiments show that GDPO still struggles to balance reward signals with different granularities. Specifically, in some particular training tasks, the model may receive a dense reward that assigns fine-grained scores ranging from 0.1 to 1.0, together with a sparse reward that provides only binary feedback of either 0 or 1. In such cases, we find that the sparse reward may provide an insufficient optimization signal, preventing its corresponding capability from being effectively reinforced. Therefore, how can we strengthen the optimization signal from the sparse reward without sacrificing the capability already learned from the fine-grained reward? To overcome this limitation, we propose Specialize-and-Merge Online Policy Distillation (SMOPD), a two-stage training method for multi-reward optimization. Stage1-Specialize: SMOPD first employs reward-priority configurations to train multiple reward-specialized teachers, allowing each reward to be learned under conditions where its signal can effectively drive optimization. Stage2-Merge: SMOPD then utilizes online policy distillation to combine the reward-specialized capabilities of these teachers into a single student policy, while maintaining balanced task-level optimization. To validate our method, we conduct experiments on two multi-reward settings: complementary rewards(tool-calling accuracy and format) and conflicting rewards (helpful and harmless rewards). Based on above settings, SMOPD outperforms GDPO across 1.5B, 3B and 7B backbones.

</details>

---

### [[20_Research/Papers/其他/AI_Agent_Economics_Can_Autonomous_Economic_Behavior_Emerge_among_AI_Agents_under_Minimal_External_Conditions|AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?]]

![[assets/2608.03076_figure.png|800]]

- **arXiv**: [2608.03076](https://arxiv.org/abs/2608.03076)
- **PDF**: https://arxiv.org/pdf/2608.03076
- **详细分析**: [[20_Research/Papers/其他/AI_Agent_Economics_Can_Autonomous_Economic_Behavior_Emerge_among_AI_Agents_under_Minimal_External_Conditions|AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?]]
- **作者**: Lingyun Zhang, Shang Shang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentSim, GovSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent studies commonly place AI agents in predefined games, markets, or roles, making it difficult to distinguish endogenous economic organization from behavior inherited from the scenario. We ask whether economic relations emerge when agents receive executable mechanisms for work, transfer, elections, and allocation but no prescribed social or economic strategy. We define AI Agent Economics as systems of production, allocation, consumption, exchange, and institutions that alter agents' future feasible actions. We develop a two-stage framework comprising a no-production boundary test and 24 independent six-agent worlds across GPT and DeepSeek. Without productive tasks, agents communicate and govern resource provision but show no substantive inter-agent transfer activity. With verified work and scarce task access, transfers, loans, access promises, vote-for-access exchanges, and allocation strategies emerge. Holding the election interface fixed, executable allocation authority increases differentiation while reducing failed allocation and prolonged exclusion. When energy becomes symbolic, continuation support disappears, yet competition over task access persists. These findings show that organization follows executable rights and resource consequences rather than role labels or prompt language, and motivate governance audits of the mechanisms that actually constrain agents' future actions.

</details>

---

### [[20_Research/Papers/大模型/CVPO_Enhancing_LLM_Reinforcement_Learning_Reasoning_via_Value-Variance_Adaptation_and_Dynamic_Curriculum_Learning|CVPO: Enhancing LLM Reinforcement Learning Reasoning via Value-Variance Adaptation and Dynamic Curriculum Learning]]

![[assets/2608.03068_figure.png|800]]

- **arXiv**: [2608.03068](https://arxiv.org/abs/2608.03068)
- **PDF**: https://arxiv.org/pdf/2608.03068
- **详细分析**: [[20_Research/Papers/大模型/CVPO_Enhancing_LLM_Reinforcement_Learning_Reasoning_via_Value-Variance_Adaptation_and_Dynamic_Curriculum_Learning|CVPO: Enhancing LLM Reinforcement Learning Reasoning via Value-Variance Adaptation and Dynamic Curriculum Learning]]
- **作者**: Ziqi Jia, Yalu Ouyang, Bo Pang, Panpan Li, Hangfei Xu, Shengzhao Wen, Shiyong Li, Yanpeng Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.77（加权：大模型 0.45，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《CVPO: Enhancing LLM Reinforcement Learning Reasoning via Value-Variance Adaptation and Dynamic Curriculum Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has emerged as an effective method for enhancing the reasoning capabilities of large language models (LLMs). However, existing methods suffer from insufficient precision in feedback on generated answer trajectories and exhibit the phenomenon of problem difficulty drift. To address these challenges, we propose CVPO - Curriculum-guided Value-Variance Policy Optimization. At the response trajectory level, we find that token-level value-variance correlates with exploration intensity. Our theoretical analysis shows this variance bounds policy update magnitude. We then use the estimated trajectory value-variance to quantify the intrinsic randomness in generation. Based on this, we design a variance-aware advantage adjustment mechanism for different reward types. At the question level, we introduce a dynamic curriculum weighting method that adapts to question difficulty. This helps the model focus on tasks matched to its current ability during each training stage. Experimental results show our method outperforms strong value-based baselines like VAPO. It achieves better performance and stronger exploration, enabling more accurate and robust reasoning in language models across various math tasks.

</details>

---

### [[20_Research/Papers/大模型/LLM_Serving_in_the_Wild_An_Empirical_Study_of_Frameworks,_Methods,_and_System_Designs|LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs]]

![[assets/2608.03036_figure.png|800]]

- **arXiv**: [2608.03036](https://arxiv.org/abs/2608.03036)
- **PDF**: https://arxiv.org/pdf/2608.03036
- **详细分析**: [[20_Research/Papers/大模型/LLM_Serving_in_the_Wild_An_Empirical_Study_of_Frameworks,_Methods,_and_System_Designs|LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs]]
- **作者**: Forough Majidi, Mohammad Mehdi Morovati, Foutse Khomh, Heng Li
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《LLM Serving in the Wild: An Empirical Study of Frameworks, Methods, and System Designs》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) are integrated into software systems and AI services, making efficient LLM serving a concern for software engineering. Serving LLMs is challenging because inference requires computation, memory, GPU resources, and execution while maintaining latency and throughput. Although prior research has proposed LLM inference, optimization, and serving techniques and frameworks, little is known about how they are adopted in practice. In this study, we investigate the use of LLM serving frameworks and serving methods in open-source software systems. We identify and analyze five LLM-specific frameworks: vLLM, SGLang, TensorRT-LLM, LMDeploy, and FlashInfer. We examine how these frameworks and techniques are adopted individually and in combination, how adoption varies across categories of LLMs, and how repositories differ in intent, focus, use case, and architectural design. Our results show that vLLM is the most visible framework in popularity and adoption, while parallel computation, memory management, and network pruning are the most frequently used serving-method categories. Multi-framework usage is limited, suggesting that developers rely on a single serving framework; however, combined frameworks connect complementary capabilities across the serving stack. Framework adoption varies across model families, modalities, model sizes, domain specializations, and deployment settings. Repository-level analysis shows that LLM serving frameworks support applications and architectures, including Reinforcement Learning (RL)-based reasoning, multimodal generation and understanding, microservices, and cloud infrastructure. Overall, this study provides a large-scale empirical characterization of LLM serving framework adoption in practice and offers insights for researchers, framework maintainers, and practitioners working on LLM systems.

</details>

---

### [[20_Research/Papers/具身智能/PACE_Adaptive_Budget_Allocation_for_Time-Efficient_Embodied_Planning|PACE: Adaptive Budget Allocation for Time-Efficient Embodied Planning]]

![[assets/2608.03034_figure.png|800]]

- **arXiv**: [2608.03034](https://arxiv.org/abs/2608.03034)
- **PDF**: https://arxiv.org/pdf/2608.03034
- **详细分析**: [[20_Research/Papers/具身智能/PACE_Adaptive_Budget_Allocation_for_Time-Efficient_Embodied_Planning|PACE: Adaptive Budget Allocation for Time-Efficient Embodied Planning]]
- **作者**: Yuchen Huang, Xijiang Ying, Zhenhua Ma, Xiaxiang Yuan, Zhijie Gao, Jiayi Huang, Ruichi Mao, Jiazheng Zhang, Hongsheng Ti, Maotao Tian, Rong Shi, Lu Zhao...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《PACE: Adaptive Budget Allocation for Time-Efficient Embodied Planning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning-enhanced large language models have achieved remarkable improvements in planning tasks, yet their deployment in embodied systems remains impractical due to prohibitive inference delays-often exceeding minutes per planning instance. The fundamental bottleneck stems from the serial nature of existing paradigms: models must complete all reasoning before any action execution, leaving execution time windows entirely unexploited. We introduce PACE (Planning with Adaptive Cognitive Effort), a framework that enables interleaved reasoning and execution through two key innovations: an Interleaved Think-Act architecture that pipelines cognitive processing with action execution, and a Dynamic Budget Allocator that adapts reasoning token budgets to available execution time windows. On the Robotouille benchmark using Qwen3-8B-AWQ, PACE achieves a 10% success rate-representing a 67% improvement over the ReAct+Think baseline-while delivering 6.9 times acceleration in thinking time compared to unconstrained reasoning. The framework hides 66.8% of thinking time within execution windows, demonstrating that strategic cognitive effort allocation can simultaneously improve both planning quality and time efficiency. These results provide evidence that time-aware architectural innovations enable reasoning models to operate in latency-sensitive embodied domains where they were previously impractical.

</details>

---

### [[20_Research/Papers/具身智能/Neurosymbolic_Reasoning_with_Incremental_Knowledge_for_Sample_Efficient_Hierarchical_Reinforcement_Learning|Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning]]

![[assets/2608.02993_figure.png|800]]

- **arXiv**: [2608.02993](https://arxiv.org/abs/2608.02993)
- **PDF**: https://arxiv.org/pdf/2608.02993
- **详细分析**: [[20_Research/Papers/具身智能/Neurosymbolic_Reasoning_with_Incremental_Knowledge_for_Sample_Efficient_Hierarchical_Reinforcement_Learning|Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning]]
- **作者**: Subrat Prasad Panda, Blaise Genest, Arvind Easwaran
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, HRL, PAHRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

(Flat) Reinforcement Learning (RL) agents face significant challenges in environments with sparse rewards that require long-horizon reasoning. A compelling approach to improve sample efficiency is to incorporate knowledge into learning and decision-making. In standard Hierarchical RL (HRL), knowledge is encoded in a fixed, non-updatable form, such as architectural choices, and remains unchanged throughout learning. With fixed HRL, reasoning with incremental knowledge learned during exploration is impractical before sufficient environmental knowledge is acquired, leading to poor sample efficiency. In this work, we propose neurosymbolic HRL with {\em Incremental Knowledge (InK)}: symbolic high-level components perform {\em symbolic planning} (e.g. using $D^*$) on an updatable representation of current InK, while low-level goal-conditioned neural modules learn motion primitives through experience using reward shaping. Experiments on navigation tasks demonstrate that incorporating InK substantially improves sample efficiency. Additionally, to perform {\em optimal} symbolic planning given {\em prior} knowledge about the world, we develop Belief World Tree Search. The code is available at https://github.com/CPS-research-group/ink_bwts.

</details>

---

### [[20_Research/Papers/具身智能/ValueFormer_A_Causal_Transformer_Value_Function_with_Stage-Aware_Labels_for_Semi-Autonomous_Vision-Language-Action_Policies|ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies]]

![[assets/2608.02958_figure.png|800]]

- **arXiv**: [2608.02958](https://arxiv.org/abs/2608.02958)
- **PDF**: https://arxiv.org/pdf/2608.02958
- **详细分析**: [[20_Research/Papers/具身智能/ValueFormer_A_Causal_Transformer_Value_Function_with_Stage-Aware_Labels_for_Semi-Autonomous_Vision-Language-Action_Policies|ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies]]
- **作者**: Inkyu Sa, Konstantin Stulov, Rajat Bhageria
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ValueFormer: A Causal Transformer Value Function with Stage-Aware Labels for Semi-Autonomous Vision-Language-Action Policies》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies trained by behavior cloning fail silently: from the action stream alone, a collapsing rollout looks much like one making clean progress, because imitation supplies no notion of progress. Reinforcement learning would supply one, but it is impractical here, where real-robot experience is costly and deformable food resists simulation. The cheap alternative, a terminal success / failure bit, is learnable in principle yet far too sparse to say when a rollout went wrong. We argue that the per-frame label, not the architecture, is the hard part: to be useful it must be dense, continuous, and correctly shaped. We present ValueFormer, a compact policy-agnostic causal transformer over a frozen DINOv3 backbone that emits two per-frame signals in one forward pass: a smooth Monte Carlo value, V_mc, for advantage estimation and a sharp binary value for online mistake detection, targets that pull in opposite directions by design. Failed episodes are labeled with a stage-aware, success-then-decay return that preserves the success curve before the failure stage, and detection is supervised from mistake intervals rather than a single failure time, so mistakes the policy recovers from also carry signal. On a real-robot bimanual sandwich-assembly task 1,427 episodes), a critic-derived per-frame training weight lifts task completion from 70% to 85% (within noise at n=20), and a batched bf16 encoder cuts the live serving cost 3~5 times so the critic runs at 2 Hz alongside the policy on a single GPU.

</details>

---

### [[20_Research/Papers/大模型/SP3O_Reinforcement_Learning_from_Segment_Preferences_without_Reward_Modeling|SP3O: Reinforcement Learning from Segment Preferences without Reward Modeling]]

![[assets/2608.02951_figure.png|800]]

- **arXiv**: [2608.02951](https://arxiv.org/abs/2608.02951)
- **PDF**: https://arxiv.org/pdf/2608.02951
- **详细分析**: [[20_Research/Papers/大模型/SP3O_Reinforcement_Learning_from_Segment_Preferences_without_Reward_Modeling|SP3O: Reinforcement Learning from Segment Preferences without Reward Modeling]]
- **作者**: Evan Assmus, Qining Zhang, Lei Ying
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.56，世界模型 0.16，机器人 0.2）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《SP3O: Reinforcement Learning from Segment Preferences without Reward Modeling》归入 强化学习、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Preference-based reinforcement learning (PbRL) for general stochastic MDPs often requires training a reward model. Existing reward-model-free methods are either restricted to bandits or deterministic MDPs, such as DPO or P3O, or use zeroth-order, gradient-free optimization, which in general exhibits a slower convergence rate than gradient-based algorithms. Furthermore, existing reward-model-free preference-based RL algorithms almost exclusively use trajectory-level feedback, which can require significant effort from a human evaluator when trajectories are long. On the other hand, segments are much shorter, so they are easier to compare and evaluate. In this paper, we introduce a novel reward-model-free, critic-free, and gradient-based PbRL algorithm compatible with segment preferences named Segment Pairwise Proximal Policy Optimization (SP3O). SP3O utilizes segment-level preference feedback to construct an accurate policy value difference estimator via off-policy importance sampling, and then uses the estimator to compute the policy gradient via a PPO-type loss function. We provide a theoretical basis for the algorithm and analyze the tradeoff in choosing the segment length. We also evaluate it experimentally against other PbRL/RLHF algorithms in robotic control and LLM finetuning settings to show its improved performance, especially in long-horizon tasks.

</details>

---

### [[20_Research/Papers/强化学习/Improved_Quantum_Algorithms_for_Reinforcement_Learning_Under_a_Generative_Model|Improved Quantum Algorithms for Reinforcement Learning Under a Generative Model]]

![[assets/2608.02826_first_page.png|800]]

- **arXiv**: [2608.02826](https://arxiv.org/abs/2608.02826)
- **PDF**: https://arxiv.org/pdf/2608.02826
- **详细分析**: [[20_Research/Papers/强化学习/Improved_Quantum_Algorithms_for_Reinforcement_Learning_Under_a_Generative_Model|Improved Quantum Algorithms for Reinforcement Learning Under a Generative Model]]
- **作者**: Joao F. Doriguello
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Improved Quantum Algorithms for Reinforcement Learning Under a Generative Model》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning is a subfield of machine learning that studies how an agent interacts with an environment in order to extract as large a reward as possible. A standard approach to study such interaction is through Markov Decision Processes (MDPs) and the task of choosing an optimal policy --- a function that tells the agent which action to take. In this work, we study two types of MDPs --- finite-horizon and infinite-horizon discounted --- and propose new quantum algorithms for computing approximate optimal policies. Our quantum algorithms are based on a new combination of standard value iteration and quantum subroutines like quantum mean estimation and quantum maximum finding, overall enhanced with techniques from sample-optimal classical algorithms. Our resulting query complexities improve upon previous works, thus approaching already established quantum lower bounds.

</details>

---

### [[20_Research/Papers/大模型/$S^3$_Improving_Agent_Safety_through_Multi-Stage_Defense|$S^3$: Improving Agent Safety through Multi-Stage Defense]]

![[assets/2608.02683_figure.png|800]]

- **arXiv**: [2608.02683](https://arxiv.org/abs/2608.02683)
- **PDF**: https://arxiv.org/pdf/2608.02683
- **详细分析**: [[20_Research/Papers/大模型/$S^3$_Improving_Agent_Safety_through_Multi-Stage_Defense|$S^3$: Improving Agent Safety through Multi-Stage Defense]]
- **作者**: Zibo Xiao, Haoyu Wang, Jun Sun
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《$S^3$: Improving Agent Safety through Multi-Stage Defense》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ATBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents rely on multi-stage agentic workflows, with stages such as memory, planning, and tool execution, to accomplish complex tasks. However, risks may emerge at different stages, propagate across steps, and become difficult to detect and mitigate. Existing safety methods protect only isolated stages and are difficult to integrate, leaving agents without comprehensive protection throughout the workflow. To address these limitations, we introduce Stage-Specific Safety Skills, a unified abstraction that represents heterogeneous safety designs as reusable and composable components with explicit stage semantics. We further develop an automated transformation pipeline that converts existing safety designs into reusable safety skills and establish a community-driven safety skill library. Building on this abstraction, we propose $S^3$, a multi-stage defense framework in which a guard agent orchestrates stage-specific safety skills for risk detection and mitigation throughout the agentic workflow. We also construct the Multi-Stage Risk Benchmark (MSRB) to evaluate representative risks across workflow stages. Experimental results show that $S^3$ consistently outperforms representative state-of-the-art baselines in both safety effectiveness and utility preservation. These results demonstrate the potential of stage-specific safety skills as a scalable and composable foundation for building resilient and trustworthy agent systems.

</details>

---

### [[20_Research/Papers/大模型/TraceCompiler_Skill-Guided_Mining_and_Compilation_of_LLM_Agent_Traces_into_Mostly_Deterministic_Workflows|TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows]]

![[assets/2608.02680_figure.png|800]]

- **arXiv**: [2608.02680](https://arxiv.org/abs/2608.02680)
- **PDF**: https://arxiv.org/pdf/2608.02680
- **详细分析**: [[20_Research/Papers/大模型/TraceCompiler_Skill-Guided_Mining_and_Compilation_of_LLM_Agent_Traces_into_Mostly_Deterministic_Workflows|TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows]]
- **作者**: Salma El Yadouni, Guanyi Li
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《TraceCompiler: Skill-Guided Mining and Compilation of LLM Agent Traces into Mostly Deterministic Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using language-model agents repeatedly rediscover procedures they have already executed, producing traces that mix reusable structure with retries, exploration, accidental ordering, and repeated lookups. We present TraceCompiler, a skill-guided system that mines clusters of noisy agent traces and compiles them into executable, mostly deterministic workflows. It admits an inter-tool dependency only when a consumer argument contains a value attributable uniquely to an earlier producer; every hard edge carries an auditable evidence tuple, and ambiguous relations are marked suspected and impose no ordering constraint. Bindings are classified as constants, user inputs, copied outputs, transforms, or residual LLM decisions. On T1, a mechanized form of the rule recovers producer-consumer dependencies at 0.928 precision and 0.943 recall over 15,775 def-use edges of its training split, against 0.711 F1 for adjacency and 0.712 for a frequency-thresholded directly-follows measure on identical data; the compiler skill run blind reaches 0.992 on 250 of those edges. On AppWorld we replay released trajectories in the deterministic simulator to recover masked return values and measure the rule against 563 token edges at 0.993 precision - a self-consistency check, since replay injects tokens by a related heuristic. We compile two recurring intents: a Venmo money-request intent reduces 34 observed API calls to 11 runtime calls and, under leave-one-out execution against the benchmark's own state tests, passes 15 of 21, the failing fold escalating rather than acting because its required branch was never observed; and a Spotify/Todoist intent the compiler correctly refuses to compile, because an irreversible side effect is under-determined. We measure call reduction but not offline compilation cost, so we claim no net efficiency result.

</details>

---

### [[20_Research/Papers/大模型/DenialRAG_Single-Document_RAG_Poisoning_via_Embedded_Parametric_Denial|DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial]]

![[assets/2608.02678_figure.png|800]]

- **arXiv**: [2608.02678](https://arxiv.org/abs/2608.02678)
- **PDF**: https://arxiv.org/pdf/2608.02678
- **详细分析**: [[20_Research/Papers/大模型/DenialRAG_Single-Document_RAG_Poisoning_via_Embedded_Parametric_Denial|DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial]]
- **作者**: Abay Zhurekbay, Tao Liu, Fan Li
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning: an attacker who inserts a crafted document into the retrieval corpus can steer the underlying large language model (LLM) toward an attacker-chosen wrong answer. Prior single-document attacks typically avoid explicitly naming and refuting the correct answer inside the poisoned passage. In this paper, we examine a complementary design and propose \emph{DenialRAG}, a single-document poisoning attack that explicitly names the correct answer, denies it, and presents an attacker-controlled explanation for favoring the wrong answer. By placing both the correct answer and the corresponding poisoned answer inside the same retrieved passage, DenialRAG embeds the conflict directly into the context seen by the generator. We evaluate DenialRAG against four published single-document poisoning attacks across three open-domain question-answering datasets, eight target LLMs from four vendors, and five inference-time defenses. The results show that attack effectiveness is strongly model-dependent: DenialRAG achieves the highest attack success rate (ASR) on all three Mistral-7B datasets and remains effective on several other target LLMs, while other attacks dominate in some model regimes. Defense results show meaningful ASR reductions but non-uniform protection, with each defense leaving residual ASR in some settings. Component-level and cross-model analyses further identify the embedded denial as the most influential tested component and show that different poisoning mechanisms lose effectiveness at different rates across model groups. Together, these results show that RAG poisoning risk cannot be fully characterized by a single attack family or a single target model.

</details>

---

### [[20_Research/Papers/大模型/HyperAgent_Planning_and_Acting_over_Tool-Schema_Hypergraphs_for_Tool-Use_LLM_Agents|HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents]]

![[assets/2608.02650_figure.png|800]]

- **arXiv**: [2608.02650](https://arxiv.org/abs/2608.02650)
- **PDF**: https://arxiv.org/pdf/2608.02650
- **详细分析**: [[20_Research/Papers/大模型/HyperAgent_Planning_and_Acting_over_Tool-Schema_Hypergraphs_for_Tool-Use_LLM_Agents|HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents]]
- **作者**: Zian Zhai, Xingyu Tan, Gaowang Zou, Xiaoyang Wang, Wenjie Zhang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AppWorld, ToolNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly rely on external tools to complete complex real-world tasks. However, reliable tool-use planning remains challenging due to the limitations of implicit reasoning and the evolving nature of real-world execution environments. Existing tool-use agents typically rely on LLMs to infer tool compositions from textual descriptions, which can lead to inefficient exploration and unreliable execution in complex tasks. To address these challenges, we model tool relations at the schema level and construct a directed Tool--Schema Hypergraph, in which tools are represented as hyperedges from their required input-schema nodes to their output-schema nodes. Furthermore, we propose HyperAgent, a Tool--Schema Hypergraph-guided framework for dynamic planning and execution. Given a task, HyperAgent first extracts a task-relevant tool context graph and uses it to guide the construction of a schema-aware Task DAG. During execution, HyperAgent dynamically realizes each subtask by constructing a state-conditioned tool support graph through deficit-oriented expansion, which identifies unresolved requirements and retrieves supporting producer tools according to the current agent state. Experiments on AppWorld demonstrate that HyperAgent improves task completion performance while reducing redundant API calls, LLM interactions, and token consumption compared with existing agent baselines.

</details>

---

### [[20_Research/Papers/大模型/Verified_Tool_Calls_Improve_LLM_Agent_Reliability_Under_Non-Atomic_Failures|Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures]]

![[assets/2608.02645_figure.png|800]]

- **arXiv**: [2608.02645](https://arxiv.org/abs/2608.02645)
- **PDF**: https://arxiv.org/pdf/2608.02645
- **详细分析**: [[20_Research/Papers/大模型/Verified_Tool_Calls_Improve_LLM_Agent_Reliability_Under_Non-Atomic_Failures|Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures]]
- **作者**: Isham Kalappurackal Mansoor, Abhishek Phadke, Pratip Rana
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentBench, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents rely on external tools to perform multistage tasks. Existing agent frameworks typically assume that tool calls are atomic and return binary success or failure signals. However, real-world systems exhibit non-atomic behaviors such as timeouts after dispatch, delayed visibility, and partial state updates. These mismatches lead to reliability issues including duplicate actions, task success, and unnecessary tool executions. A lightweight, verification-aware tool wrapper is introduced that augments tool calls with postcondition verification, verify-before-retry logic, and idempotency keys. The approach is evaluated in a controlled simulated environment with injected non-atomic failures across multiple task templates. The results demonstrate that the proposed method significantly reduces duplicate actions, while maintaining comparable task success rates. Overall, the findings suggest that strengthening tool interaction semantics is a promising direction for improving LLM agent reliability without requiring modifications to the underlying language model.

</details>

---

### [[20_Research/Papers/具身智能/RF-HOI_Recognize_Human-Object_Interaction_with_Radio_Frequency_Signals|RF-HOI: Recognize Human-Object Interaction with Radio Frequency Signals]]

![[assets/2608.00289_figure.png|800]]

- **arXiv**: [2608.00289](https://arxiv.org/abs/2608.00289)
- **PDF**: https://arxiv.org/pdf/2608.00289
- **详细分析**: [[20_Research/Papers/具身智能/RF-HOI_Recognize_Human-Object_Interaction_with_Radio_Frequency_Signals|RF-HOI: Recognize Human-Object Interaction with Radio Frequency Signals]]
- **作者**: Lihao Wang, Linlu Gao, Jiacan Yu, Yanyu Lin, Yifan Yin, Jianxin Wang, Tianmin Shu, Renjie Zhao
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《RF-HOI: Recognize Human-Object Interaction with Radio Frequency Signals》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recognizing Human-Object Interactions (HOI) is essential for intelligent systems, underpinning applications in virtual and augmented reality, embodied AI, and assistive robotics. However, vision-based HOI methods face challenges in privacy concerns and poor light conditions. In this work, we introduce RF-HOI, the first framework that only uses radio frequency (RF) signals for HOI recognition. A key challenge of RF-HOI is that single-modality RF sensing is insufficient to recognize both actions and the objects being interacted with. RF-HOI addresses this through a novel modality fusion that combines mmWave radar and RFID, enabling simultaneous action recognition and target identification. Another challenge is limited training data across diverse setups, which impairs the generalizability of the recognition model. To overcome this, we develop a simulator that synthesizes multimodal RF data for diverse HOIs at scale, allowing us to fine-tune with only a small amount of real-world data. Experiment results show that RF-HOI outperforms all baselines, approaching vision model performance, and that our diverse synthetic training data can significantly boost our system's performance on real-world scenarios. These results highlight the potential of multimodal RF sensing for robust and privacy-preserving HOI recognition as well as the effectiveness of our RF data synthesis.

</details>

---

### [[20_Research/Papers/大模型/AgentStream_How_Well_Do_Self-Evolving_LLM_Agents_Perform_Under_Streaming_Tasks|AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?]]

![[assets/2608.00155_figure.png|800]]

- **arXiv**: [2608.00155](https://arxiv.org/abs/2608.00155)
- **PDF**: https://arxiv.org/pdf/2608.00155
- **详细分析**: [[20_Research/Papers/大模型/AgentStream_How_Well_Do_Self-Evolving_LLM_Agents_Perform_Under_Streaming_Tasks|AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?]]
- **作者**: Dong Yan, Jian Liang, Dapeng Hu, Ran He, Nicholas Jing Yuan, Qi Zhang, Tieniu Tan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents can self-evolve by continually improving from their own accumulated experience. However, existing studies predominantly adopt independent evaluation. Consequently, the behavior of self-evolving agents in realistic streaming settings, where agents adapt to diverse and complex task streams, remains poorly understood. To address this gap, we introduce AgentStream, a unified framework that evaluates self-evolving agents spanning diverse evolution components by organizing agentic benchmarks into a configurable task stream and instantiating the \texttt{Isolated}, \texttt{Sequential}, and \texttt{Interleaved} streaming scenarios at test time, which progressively vary the scope and domain composition of the stream. Over these scenarios, we combinatorially evaluate five representative self-evolving methods across three frontier foundation models, disentangling how model capability, method architecture, and streaming scenario jointly shape self-evolution. Our results show that self-evolution reliability varies across streaming scenarios, the benefit of self-evolution is gated by model capability and non-monotonic in model strength, and no single method dominates across models and scenarios. These findings offer concrete guidance for selecting self-evolving methods across models and streaming scenarios. Overall, we advocate that self-evolving agents should be evaluated under realistic task streams rather than isolated single-task settings.

</details>

---
