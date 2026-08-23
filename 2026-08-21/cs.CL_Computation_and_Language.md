# cs.CL | Computation and Language | 2026-08-21

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/大模型/Multi-Agent_Orchestration_with_the_Common-Sense_Reasoning_Capabilities_of_LLMs_for_Autonomous_Driving|Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving]]

![[assets/2608.20129_figure.png|800]]

- **arXiv**: [2608.20129](https://arxiv.org/abs/2608.20129)
- **PDF**: https://arxiv.org/pdf/2608.20129
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_Orchestration_with_the_Common-Sense_Reasoning_Capabilities_of_LLMs_for_Autonomous_Driving|Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving]]
- **作者**: Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi, Stefan Henkler, Achim Rettberg
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large Language Models (LLMs) have demonstrated strong capabilities in understanding multimodal information and generating contextual reasoning, however, their use for direct vehicle control can introduce latency and hallucination risks. To address these limitations, a hybrid framework is proposed. This system uses an orchestrator to coordinate PPO-trained reinforcement learning and PID control, with LLM common-sense reasoning applied throughout the framework. LLM reasoning is further employed iteratively to refine the RL reward function for dynamic driving environments. The proposed framework is evaluated in highly randomized CARLA scenarios under diverse environmental and traffic conditions. The results demonstrate the potential of integrating LLM-based reasoning with conventional autonomous driving methods while retaining structured control and safety mechanism.

</details>

---

### [[20_Research/Papers/大模型/Reward-Guided_Autoregressive_Graph_Generation_for_Efficient_Multi-Agent_Communication_Topology_Design|Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design]]

![[assets/2608.20099_figure.png|800]]

- **arXiv**: [2608.20099](https://arxiv.org/abs/2608.20099)
- **PDF**: https://arxiv.org/pdf/2608.20099
- **详细分析**: [[20_Research/Papers/大模型/Reward-Guided_Autoregressive_Graph_Generation_for_Efficient_Multi-Agent_Communication_Topology_Design|Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design]]
- **作者**: Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.75，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training objective provides no explicit incentive for the model to generate sparse and efficient topologies. We address this limitation by introducing a Reward-Guided Autoregressive Graph Generation (RGA-Designer) inspired by Reinforcement Learning from Human Feedback (RLHF). We train a reward model that jointly captures task correctness and structural compactness, and then fine-tune the pretrained graph generator using the reward model as feedback. Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.

</details>

---

### [[20_Research/Papers/大模型/Auditing_Cross-Lingual_Fairness_in_Language_Model_Watermarking|Auditing Cross-Lingual Fairness in Language Model Watermarking]]

![[assets/2608.20047_figure.png|800]]

- **arXiv**: [2608.20047](https://arxiv.org/abs/2608.20047)
- **PDF**: https://arxiv.org/pdf/2608.20047
- **详细分析**: [[20_Research/Papers/大模型/Auditing_Cross-Lingual_Fairness_in_Language_Model_Watermarking|Auditing Cross-Lingual Fairness in Language Model Watermarking]]
- **作者**: Alexander Nemecek, Osama Zafar, Debargha Ganguly, Vikash Singh, Vipin Chaudhary, Erman Ayday
- **cs 子类**: cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Auditing Cross-Lingual Fairness in Language Model Watermarking》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：WaterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

</details>

---

### [[20_Research/Papers/大模型/Robust_Incomplete_Multimodal_Sentiment_Analysis_via_Iterative_Proxy_Correction|Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction]]

![[assets/2608.19971_figure.png|800]]

- **arXiv**: [2608.19971](https://arxiv.org/abs/2608.19971)
- **PDF**: https://arxiv.org/pdf/2608.19971
- **详细分析**: [[20_Research/Papers/大模型/Robust_Incomplete_Multimodal_Sentiment_Analysis_via_Iterative_Proxy_Correction|Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction]]
- **作者**: Zhifa Geng, Subin Huang, Hao Guo, Junjie Chen, Sanmin Liu, Chao Kong
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CENet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal sentiment analysis aims to infer affective states by integrating language, visual, and acoustic cues. However, real-world multimodal inputs are often incomplete or corrupted, which can weaken cross-modal complementarity and introduce misleading information into downstream fusion. Existing proxy-based methods for incomplete MSA commonly rely on one-shot proxy construction to compensate for degraded language information, but the generated proxy may be coarse or unreliable at initialization. Prematurely injecting such a proxy into multimodal reasoning can propagate initial errors and compromise sentiment prediction. To address this limitation, we propose an iterative proxy correction framework for robust incomplete MSA. Our method constructs a language-oriented proxy from non-language modalities and progressively refines it under multimodal context through gated residual correction. The corrected proxy is then adaptively fused with the observed language representation according to an estimated language reliability score, allowing the model to balance proxy-based compensation and trustworthy linguistic evidence. In addition, we introduce a stage-wise latent correction objective that uses the complete language representation as a training-time semantic anchor to stabilize the proxy refinement trajectory. Extensive experiments on MOSI, MOSEI, and SIMS under diverse missing-modality settings demonstrate that the proposed framework consistently outperforms competitive baselines and achieves robust sentiment prediction under incomplete inputs.

</details>

---

### [[20_Research/Papers/大模型/Dynamic_Gated_Cross-Modal_Fusion_with_Sarcastic-aware_Contrastive_Regularization_for_Multimodal_Sarcasm_Detection|Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection]]

![[assets/2608.19942_figure.png|800]]

- **arXiv**: [2608.19942](https://arxiv.org/abs/2608.19942)
- **PDF**: https://arxiv.org/pdf/2608.19942
- **详细分析**: [[20_Research/Papers/大模型/Dynamic_Gated_Cross-Modal_Fusion_with_Sarcastic-aware_Contrastive_Regularization_for_Multimodal_Sarcasm_Detection|Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection]]
- **作者**: Hao Guo, Subin Huang, Junjie Chen, Zhifa Geng, Sanmin Liu, Chao Kong
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization for Multimodal Sarcasm Detection》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal sarcasm detection aims to identify sarcastic intent from multimodal content, where inconsistencies between literal meaning and contextual cues often signal irony. This task has attracted increasing research attention. However, accurate detection remains challenging due to instance-dependent modality contributions and misleading semantic consistency, where surface-level alignment masks underlying contradictory intent. Existing methods often rely on fixed fusion strategies and treat sarcasm as generic cross-modal mismatch, limiting their ability to capture subtle sarcasm cues and instance-specific modality interactions. To address these challenges, we propose a novel MSD framework that integrates Dynamic Gated Cross-Modal Fusion with Sarcastic-aware Contrastive Regularization (SaCR). Specifically, a bidirectional gated interaction module performs cross-modal feature filtering and adaptively calibrates textual and visual contributions at the instance level. A dynamic fusion gate further balances modality importance to generate more robust multimodal representations. Furthermore, SaCR is introduced as a label-aware contrastive regularization objective that encourages semantic consistency for non-sarcastic samples while suppressing misleading consistency in sarcastic cases. The proposed framework is trained end-to-end with a multi-objective learning strategy that jointly optimizes multimodal classification and auxiliary unimodal supervision. Extensive experiments on MMSD and MMSD2.0 demonstrate that the proposed method consistently outperforms strong baselines.

</details>

---

### [[20_Research/Papers/大模型/Stopping_and_Routing_LLM_Judge_Panels|Stopping and Routing LLM Judge Panels]]

![[assets/2608.19802_figure.png|800]]

- **arXiv**: [2608.19802](https://arxiv.org/abs/2608.19802)
- **PDF**: https://arxiv.org/pdf/2608.19802
- **详细分析**: [[20_Research/Papers/大模型/Stopping_and_Routing_LLM_Judge_Panels|Stopping and Routing LLM Judge Panels]]
- **作者**: Bin Zhu, Yi Xie, Yanghui Rao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Stopping and Routing LLM Judge Panels》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HumanEval, JailbreakBench, RewardBench, SummEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-relative roles: copies add no conditional information, complements improve the global panel, and specialists help only on slices. These roles induce a policy: drop copies, add complements globally, route specialists conditionally, and stop when validation gain falls below a threshold. Across reasoning, code, safety, preference, reward-model, summarization, and math audits, the method is compared with single judges, flat panels, matched diversity heuristics, full-call stacking, reliability juries, and frugal cascades. The result is a regime map for judge calls: route specialists on deployable slices, stop in saturated verifier regimes, keep broad ensembles when their risk benefit is worth the cost, and ignore conditional copies. The output is a reusable, auditable call plan for the next evaluation batch.

</details>

---

### [[20_Research/Papers/大模型/SWE-bench_Science_Can_Coding_Agents_Resolve_Engineering_Tasks_in_Science|SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?]]

![[assets/2608.19799_first_page.png|800]]

- **arXiv**: [2608.19799](https://arxiv.org/abs/2608.19799)
- **PDF**: https://arxiv.org/pdf/2608.19799
- **详细分析**: [[20_Research/Papers/大模型/SWE-bench_Science_Can_Coding_Agents_Resolve_Engineering_Tasks_in_Science|SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?]]
- **作者**: Zhipeng Xu, Jiahao Lu, Yining Zheng, Yuxin Wang, Xipeng Qiu
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software increasingly functions as part of the scientific instrument itself, making failures in scientific code capable of compromising not only program behavior but also the evidence underlying scientific conclusions. Yet existing evaluations of coding agents largely emphasize aggregate task success, providing limited insight into why agents fail when repairing scientific software. We introduce \textbf{SWE-bench Science}, a repository-level benchmark for scientific software engineering comprising 119 tasks from 98 GitHub repositories across 20 scientific domains. Each task is organized into one of three paradigms: Issue-driven, Expert-exploratory, and Engineering-integration. Even the best-performing agent, \textbf{Claude Code with Opus-5 (max), achieves a pass@1 below 50\%}, highlighting the substantial challenges posed by scientific software engineering. We identify four recurring failure mechanisms: deficits in scientific knowledge or abstraction, misguided exploration or surface-level repair, incomplete repair coverage or system integration, and failures to generalize scientific knowledge beyond observed cases in our analysis. We further conduct a paired ablation that removes explicit scientific guidance while preserving the repository and executable engineering context. The results show that scientific knowledge is not uniformly beneficial: well-grounded information can constrain repair and improve average performance and token efficiency, whereas poorly aligned guidance can induce anchoring and does not necessarily improve exact repair success. Together, SWE-bench Science provides a broad testbed for studying both the capabilities and failure mechanisms of coding agents in scientific software engineering.

</details>

---

### [[20_Research/Papers/大模型/PersonalBench_Measuring_the_Authorship_Gap_in_LLM_Personalization|PersonalBench: Measuring the Authorship Gap in LLM Personalization]]

![[assets/2608.19746_first_page.png|800]]

- **arXiv**: [2608.19746](https://arxiv.org/abs/2608.19746)
- **PDF**: https://arxiv.org/pdf/2608.19746
- **详细分析**: [[20_Research/Papers/大模型/PersonalBench_Measuring_the_Authorship_Gap_in_LLM_Personalization|PersonalBench: Measuring the Authorship Gap in LLM Personalization]]
- **作者**: Yash Ganpat Sawant
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《PersonalBench: Measuring the Authorship Gap in LLM Personalization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PersonalBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalized text generation aims to make LLMs write in a specific individual's style, yet existing benchmarks measure task accuracy or preference alignment rather than whether the model's output actually resembles the target author's writing. We introduce PersonalBench, a benchmark that evaluates inference-time personalization methods through three independent lenses: LUAR (a trained authorship verification model), an LLM-as-judge, and automated stylometrics. Across 50 authors, 1,000 generations, and two model families (Qwen 3, GLM-4), we find that personalization methods do produce author-differentiated output (LUAR discriminates target authors within generated text at AUC=0.918) but this differentiation never crosses the human-LLM boundary. All methods achieve LUAR similarity to real authors in the range 0.484-0.508, below the cross-author human floor of 0.626 (ceiling 0.756). The LLM's own authorship fingerprint dominates: generated text is more distant from any human author than random humans are from each other. Methods are statistically indistinguishable from each other on LUAR (spread 0.024) despite appearing differentiated on the LLM judge, a discrepancy we trace to circularity between trait extraction and profile extraction. We validate that LUAR reliably measures authorship in our corpus (AUC=0.76 single-post, 0.96 multi-post). We release PersonalBench as a calibrated measuring stick: inference-time personalization modulates the LLM's style but does not bridge the gap to human authorship.

</details>

---

### [[20_Research/Papers/具身智能/One_Success_Isn't_Reliability_Thinkingbox,_a_Sandbox_and_Benchmark_for_Agents_in_Stateful_Business_Workflows|One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows]]

![[assets/2608.19741_figure.png|800]]

- **arXiv**: [2608.19741](https://arxiv.org/abs/2608.19741)
- **PDF**: https://arxiv.org/pdf/2608.19741
- **详细分析**: [[20_Research/Papers/具身智能/One_Success_Isn't_Reliability_Thinkingbox,_a_Sandbox_and_Benchmark_for_Agents_in_Stateful_Business_Workflows|One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows]]
- **作者**: Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, Calvin Wang, Mirco Milletari, Tuhin Kundu, Vadim Smolyakov, Kjartan Olafsson, Tommy Guy
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentBench, AgentGym, AppWorld, MCP-Bench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, a sandbox for tool-agent-user interaction that provides isolated MCP-compatible tool sessions, complete execution traces, and outcome evaluation over terminal backend state. Built on this sandbox, Thinkingbox-bench contains 507 policy-conditioned workflows across numerous scenarios, including retail, hospitality, auto insurance, neobank internal IT, and consulting IT/HR support. Each attempt is evaluated by task-specific executable checks that accept valid trajectories while rejecting wrong, missing, or extra effects; designated tasks additionally check required properties of the final response. Across proprietary and open-weight models, the strongest achieves 65.36% pass@1, but only 25.25% pass^20. Moreover, many failed trials show clean termination and valid state-changing actions, showing that response or tool-call-level signals are not clear proxies for end-to-end task completion. Thinkingbox-bench reveals a large gap between occasionally finding a successful trajectory and reliably completing stateful business tasks. We release both Thinkingbox and Thinkingbox-Bench: https://github.com/microsoft/thinkingbox

</details>

---

### [[20_Research/Papers/大模型/Projector_Is_All_You_Train|Projector Is All You Train]]

![[assets/2608.19726_figure.png|800]]

- **arXiv**: [2608.19726](https://arxiv.org/abs/2608.19726)
- **PDF**: https://arxiv.org/pdf/2608.19726
- **详细分析**: [[20_Research/Papers/大模型/Projector_Is_All_You_Train|Projector Is All You Train]]
- **作者**: Nyx Iskandar, Saathvik Selvan, Slater Victoroff
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Projector Is All You Train》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ERQA, LingoQA, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The typical training process of a multimodal large language model (MLLM) involves adapting both the language model backbone and the projector between the backbone and a modality-specific encoder. We ask whether fine-tuning the backbone of an MLLM is necessary to adapt it to a new modality. Through experiments on 3D MLLMs, we find that training only the projector is sufficient to achieve strong multimodal performance relative to existing baseline models and our jointly trained MLLMs with the same encoder and backbone. We also show that joint training leads to undesirable drift in existing capabilities of the language model, which projector-only training avoids by definition. Furthermore, projector-only training has approximately twice the training sample throughput of joint training. We validate our findings across different language model backbones via 3D classification and captioning benchmarks as well as standard benchmarks evaluating language, vision, and spatial reasoning capabilities.

</details>

---

### [[20_Research/Papers/大模型/ReCache_Efficient_KV_Cache_Reuse_and_Compression_for_Tool-Augmented_LLM_Agents|ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents]]

![[assets/2608.19662_figure.png|800]]

- **arXiv**: [2608.19662](https://arxiv.org/abs/2608.19662)
- **PDF**: https://arxiv.org/pdf/2608.19662
- **详细分析**: [[20_Research/Papers/大模型/ReCache_Efficient_KV_Cache_Reuse_and_Compression_for_Tool-Augmented_LLM_Agents|ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents]]
- **作者**: Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states. We introduce \textbf{ReCache}, a framework for independently caching resource representations while reducing their inference-time computational and memory overhead. Resource-wise attention removes cross-resource interactions and assigns resource-local positions, producing composition-invariant KV blocks. ReCache then restricts resource visibility to contribution-selected layer--KV-head-group routes and retains only invocation-critical fields through structural and semantic pruning. We evaluate ReCache on a benchmark assembled from seven public tool- and skill-use datasets, including resource-disjoint tests. Resource-wise attention matches dense invocation performance (82.3\% versus 82.4\% Inv-F1) while providing a 3.655$\times$ time-to-first-token speedup. The complete framework reduces allocated KV-tensor memory by 92.43\% and accelerates attention by 1.423$\times$. These results show that separating reusable schema encoding from selective resource access substantially reduces agentic inference costs with limited effectiveness loss. The code is available at https://github.com/EIT-NLP/ReCache.

</details>

---

### [[20_Research/Papers/大模型/Mitigating_Identity_Essentialism_in_LLM_Agents_with_Longitudinal_Life_Trajectories|Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories]]

![[assets/2608.19621_figure.png|800]]

- **arXiv**: [2608.19621](https://arxiv.org/abs/2608.19621)
- **PDF**: https://arxiv.org/pdf/2608.19621
- **详细分析**: [[20_Research/Papers/大模型/Mitigating_Identity_Essentialism_in_LLM_Agents_with_Longitudinal_Life_Trajectories|Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories]]
- **作者**: Hexi Wang, Yujia Zhou, Bangde Du, Weihang Su, Xinyuan Cao, Qingyi Pan, Qingyao Ai, Yueyue Wu, Min Zhang, Yiqun Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) offer a scalable approach to social simulation, but their credibility depends on how agents are constructed. Existing methods can partially reproduce population-level patterns, yet often fail to capture human-like diversity. Our analysis shows that static-profile agents exhibit stronger demographic separation and within-group compression than humans, a pattern consistent with identity essentialism: demographic labels can encourage models to treat group-average tendencies as individual traits, homogenizing responses within groups. We argue that this limitation arises from two related factors: sparse, static agent representations and the limited ability of prompt-only memory to persistently integrate experience. Inspired by complementary memory systems, we propose LifeMem, a longitudinal memory framework that combines structured life-event retrieval with agent-specific parametric memory for experience integration. Experiments on Add Health and Understanding Society with three LLMs show that LifeMem improves alignment with human data in terms of response distributions, overall and within-group diversity, and patterns of within-person response change across life stages. These findings highlight the value of longitudinal life-event memory for constructing more faithful and dynamically evolving social agents.

</details>

---

### [[20_Research/Papers/大模型/Remember,_Verify,_or_Ask_Cross-Family_Evaluation_of_Memory_Commitment_in_LLM_Agents|Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents]]

![[assets/2608.19564_first_page.png|800]]

- **arXiv**: [2608.19564](https://arxiv.org/abs/2608.19564)
- **PDF**: https://arxiv.org/pdf/2608.19564
- **详细分析**: [[20_Research/Papers/大模型/Remember,_Verify,_or_Ask_Cross-Family_Evaluation_of_Memory_Commitment_in_LLM_Agents|Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents]]
- **作者**: Baichuan Li, Junyi Yao, Zihao Zheng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, Mem2ActBench, MemBench, PerMemBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior. We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user. MCB contains 140 primary scenarios, split into 70 development and 70 held-out items, plus a separate 70-item contrast set. It evaluates both action labels and structured tool-call selection. Two non-authors independently label the 70 held-out primary and 70 contrast items (97.1% agreement, Cohen's kappa = 0.962); a blind third resolves four disagreements, replacing eight author labels by non-author majority. Across Claude and Qwen, models verify changing facts more reliably than they ask users to resolve ambiguity. Bare Qwen asks on 0/12 clarification items while verifying 12/18 freshness items. Few-shot prompting raises accuracy from 0.557 to 0.771 (paired delta = +0.214, Holm-adjusted exact McNemar p_H = 0.002), yet clarification recall remains 0.333. The policy prompt reduces erroneous persistence from 0.243 to 0.100 (p_H = 0.038), although its accuracy gain is not significant. Label-tool agreement is 57% for each Claude model and 23% for Qwen; Qwen accuracy falls from 0.557 to 0.343 (p_H = 0.047). Memory evaluation must test both stated decisions and tool-call choices.

</details>

---

### [[20_Research/Papers/大模型/NepOOC-M_Bilingual_Nepali-English_Benchmark_and_Comparative_Analysis_of_Multimodal_Architectures_for_OOC_Detection|NepOOC-M: Bilingual Nepali-English Benchmark and Comparative Analysis of Multimodal Architectures for OOC Detection]]

![[assets/2608.19212_figure.png|800]]

- **arXiv**: [2608.19212](https://arxiv.org/abs/2608.19212)
- **PDF**: https://arxiv.org/pdf/2608.19212
- **详细分析**: [[20_Research/Papers/大模型/NepOOC-M_Bilingual_Nepali-English_Benchmark_and_Comparative_Analysis_of_Multimodal_Architectures_for_OOC_Detection|NepOOC-M: Bilingual Nepali-English Benchmark and Comparative Analysis of Multimodal Architectures for OOC Detection]]
- **作者**: Sanjeev Khatiwada
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《NepOOC-M: Bilingual Nepali-English Benchmark and Comparative Analysis of Multimodal Architectures for OOC Detection》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Out-of-context (OOC) misinformation pairs authentic images with misleading captions to construct false narratives without image manipulation, making detection a problem of multimodal alignment rather than image forensics. Despite the prevalence and consequences of OOC misinformation in Nepal, no public benchmark exists for Nepali. We introduce NepOOC, the first publicly available Nepali-dominant multilingual OOC benchmark, comprising 1,090 image-caption pairs (545 pristine, 545 OOC) annotated across five typologies (fabricated, miscaptioned, temporal mismatch, geographic mismatch, identity mismatch) with inter-annotator agreement kappa = 0.84. Systematic evaluation of five multimodal architectures alongside text-only and image-only baselines reveals that caption semantics appear sufficient for strong performance at the current dataset scale. A text-only mBERT model achieves 94.65+/-0.20% Macro-F1, statistically equivalent to the best multimodal system (ResNet-50+mBERT, 94.65+/-0.20%; McNemar median p = 1.000, 0/5 seeds significant at alpha = 0.05). Image-only models perform near chance (33-50%), while training-size scaling suggests that dataset expansion is a more direct path to progress than architectural sophistication or regional specialisation.

</details>

---

### [[20_Research/Papers/大模型/When_Irrelevant_Text_Matters_Affine_Margin_Shifts_in_Multimodal_Large_Language_Models|When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models]]

![[assets/2608.19208_figure.png|800]]

- **arXiv**: [2608.19208](https://arxiv.org/abs/2608.19208)
- **PDF**: https://arxiv.org/pdf/2608.19208
- **详细分析**: [[20_Research/Papers/大模型/When_Irrelevant_Text_Matters_Affine_Margin_Shifts_in_Multimodal_Large_Language_Models|When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models]]
- **作者**: Yinfeng Wang, Zhiyuan Yao, Zheren Fu, Lei Zhang, Zhendong Mao
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《When Irrelevant Text Matters: Affine Margin Shifts in Multimodal Large Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) are frequently exposed to auxiliary textual context, the impact of which on visually grounded tasks remains underexplored. In this paper, we investigate the influence of task-irrelevant context by formulating it as a controlled intervention within a binary visual judgment framework. By maintaining an invariant prompt structure while varying auxiliary inputs, we observe that irrelevant text consistently biases model predictions across diverse benchmarks. To move beyond performance metrics, we characterize this sensitivity through a decision margin defined by the log-probability difference between binary candidates. Our analysis reveals a robust geometric regularity: contextconditioned margins follow a consistent affine transformation of their context-free counterparts. This finding demonstrates that irrelevant context does not manifest as unstructured stochastic noise but as a estimable distortion of model preference. We further interpret the fitted affine parameters as metrics for visual commitment preservation and directional answer bias. These findings provide a margin-level diagnostic view of irrelevant-context effects in MLLMs and offer a basis for future studies on noisy-context robustness

</details>

---

### [[20_Research/Papers/大模型/Compliance,_Capability,_and_Conflict_Benchmarking_Multimodal_LLMs_under_System_Messages|Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages]]

![[assets/2608.19207_figure.png|800]]

- **arXiv**: [2608.19207](https://arxiv.org/abs/2608.19207)
- **PDF**: https://arxiv.org/pdf/2608.19207
- **详细分析**: [[20_Research/Papers/大模型/Compliance,_Capability,_and_Conflict_Benchmarking_Multimodal_LLMs_under_System_Messages|Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages]]
- **作者**: Juan Yeo, Geewook Kim
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MIA-Bench, MM-IFEval, MMBench, Real-World, SysBench, VC-IFEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production deployments of Multimodal Large Language Models (MLLMs) increasingly rely on system messages to govern model behavior. Yet existing benchmarks either evaluate constraints in text only or embed them into the user turn, leaving system-message adherence in multimodal contexts largely unmeasured; they also leave open whether compliance comes at the cost of foundational vision-language capabilities. We introduce VSysBench, a benchmark built on MMVet-v2 that organizes constraints into 5 main categories and 22 sub-categories, ranging from textual directives in visual contexts to fully vision-grounded ones, each paired with a misaligned counterpart that stress-tests the instructional hierarchy. VSysBench scores each response jointly along two axes, constraint compliance and answer correctness, via the Joint Satisfaction Rate (JSR) and Cross-Constraint Sensitivity (CCS). Across 16 MLLMs, we find that imposing system messages substantially erodes base task accuracy, that compliance collapses under user conflict for open-weight models while remaining stable for top proprietary ones, and that vision-grounded constraints are the hardest category for every model.

</details>

---
