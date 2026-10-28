# cs.CL | Computation and Language | 2026-10-26

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/大模型/Measure_Before_You_Train_Typed_Decision_Models_vs._a_Classical_Baseline_vs._a_Generative_LLM_for_Routing_a_Personal_Multilingual_Inbox|Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox]]

![[assets/2610.32955_first_page.png|800]]

- **arXiv**: [2610.32955](https://arxiv.org/abs/2610.32955)
- **PDF**: https://arxiv.org/pdf/2610.32955
- **详细分析**: [[20_Research/Papers/大模型/Measure_Before_You_Train_Typed_Decision_Models_vs._a_Classical_Baseline_vs._a_Generative_LLM_for_Routing_a_Personal_Multilingual_Inbox|Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox]]
- **作者**: Federico Lucca
- **cs 子类**: cs.CL, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs. a Generative LLM for Routing a Personal Multilingual Inbox》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal email agents decide, for every message, what it is, whether it is urgent, whether to draft a reply, create a task, or ignore it. Their error rate is rarely measured: the stored labels were written by the system itself. We present Foyer, a self-hosted personal inbox agent in daily use, and a measurement protocol (stratified sampling, frozen snapshots, thread-grouped splits, pre-registered hypotheses, human labels in the agent's review loop) that yields ground truth before any training. On 739 real Italian/English emails labelled by the owner (231 unbiased, 500 adversarially sampled), we compare nine systems under thread-grouped cross-validation: the production keyword rules, a TF-IDF + logistic-regression baseline, local typed decision models (Tev1, Nimble), a hosted decision model (Nimble v4-max), and hosted generative LLMs (Qwen2.5-7B, Gemma 4 26B/31B). Four results. The production rules score 28% on message type against a 58% majority class: the field shown most prominently carried no information. With ~200 labels, logistic regression has the highest accuracy on every field (type 0.79, urgency 0.74, needs-reply 0.83, is-noise 0.90), though it never predicts the two rarest classes and is statistically tied with Gemma 4 on type; few-shot prompting does not close the gap. The sender's relationship (client, supplier, service) is recovered from other emails of the same contact with 98.6% accuracy where the contact has been seen, and is not inferable from a single message by any model: it belongs in the contact graph, not the prompt. Finally, accuracy is not the product metric: composed into actions, the most accurate system most often ignores emails needing action (18% vs 4% for the best LLM); a cost-chosen threshold on its noise probability halves that rate and makes it the cheapest system.

</details>

---

### [[20_Research/Papers/强化学习/Frontier-OPD_Discovering_the_Edge_of_Agent_Capability_and_Teaching_Agents_to_Go_Beyond|Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond]]

![[assets/2610.32802_figure.png|800]]

- **arXiv**: [2610.32802](https://arxiv.org/abs/2610.32802)
- **PDF**: https://arxiv.org/pdf/2610.32802
- **详细分析**: [[20_Research/Papers/强化学习/Frontier-OPD_Discovering_the_Edge_of_Agent_Capability_and_Teaching_Agents_to_Go_Beyond|Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond]]
- **作者**: Zheng Jiang, Yiming Chen, Houde Qian, Ling Li, Chaoyang Li, Lifeng Sun
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy distillation aligns teacher feedback with a student's current behavior, yet acquiring useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. We introduce Frontier-OPD, which addresses this problem through the student's learning frontier: decision situations that remain challenging but admit useful autonomous continuation after brief teacher guidance. To operationalize this frontier, Frontier-OPD organizes on-policy experience into a shared-state trajectory graph, where trajectory-balanced aggregation of teacher-student disagreement identifies distinct intervention candidates while preserving the histories needed for replay. Short teacher bridges are then assessed by comparing agreement over the bridge and the ensuing student continuation with an equally long segment of the original trajectory, providing a behavioral proxy for guidance that the current student can build on. Accepted teacher responses augment ordinary distillation data, and fresh rollouts renew the frontier estimate as the policy changes. Experiments on ALFWorld, WebShop, and ScienceWorld report higher mean autonomous performance than the compared distillation baselines across the evaluated student scales and teacher configurations, with ablations indicating complementary effects of candidate selection and guidance filtering. In one ALFWorld timing setting, the additional collection cost is offset by a shorter time to a target success rate.

</details>

---

### [[20_Research/Papers/大模型/The_Butterfly_Defects_Tracing_Cooperation_in_LLM_Agent_Networks|The Butterfly Defects: Tracing Cooperation in LLM Agent Networks]]

![[assets/2610.32726_figure.png|800]]

- **arXiv**: [2610.32726](https://arxiv.org/abs/2610.32726)
- **PDF**: https://arxiv.org/pdf/2610.32726
- **详细分析**: [[20_Research/Papers/大模型/The_Butterfly_Defects_Tracing_Cooperation_in_LLM_Agent_Networks|The Butterfly Defects: Tracing Cooperation in LLM Agent Networks]]
- **作者**: Maria Sampani, Maria Lymperaiou, Angeliki Dimitriou, Giorgos Filandrianos, Chrysoula Zerva, Giorgos Stamou
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《The Butterfly Defects: Tracing Cooperation in LLM Agent Networks》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models (LLMs) increasingly operate as interconnected agents, a fundamental question emerges: does individual cooperation translate into collective cooperation? We investigate this question through the Iterated Prisoner's Dilemma (IPD), moving from dyadic interactions to homogeneous and heterogeneous networks of open-weight LLMs. Our findings reveal that cooperation is highly sensitive to model composition and seemingly minor linguistic changes. Models that cooperate with identical peers can shift toward defection in mixed populations. A simple uncertainty cue can increase or decrease cooperation, redistribute costs, and affect unexposed agents several hops away. Even reversing action-label order can dramatically alter behavior, with uncertainty framing sometimes amplifying this sensitivity. Together, these findings challenge the notion of cooperation as a stable model-level property, revealing how strategic behavior depends on interaction partners, network positions, and the language used to frame decisions.

</details>

---

### [[20_Research/Papers/强化学习/Pseudo-Labels_as_Rewards,_Not_Targets_Group-Relative_Policy_Optimization_for_Semi-Supervised_ASR|Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR]]

![[assets/2610.32572_first_page.png|800]]

- **arXiv**: [2610.32572](https://arxiv.org/abs/2610.32572)
- **PDF**: https://arxiv.org/pdf/2610.32572
- **详细分析**: [[20_Research/Papers/强化学习/Pseudo-Labels_as_Rewards,_Not_Targets_Group-Relative_Policy_Optimization_for_Semi-Supervised_ASR|Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR]]
- **作者**: Shashi Kumar, Yanis Labrak, Sergio Burdisso, Esaú Villatoro-Tello, Petr Motlicek, Kadri Hacioglu, Andreas Stolcke
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting ASR to a domain with only untranscribed audio typically relies on pseudo-labeling, a strong teacher transcribes the audio and a student is fine-tuned on it. Because supervised fine-tuning (SFT) treats every pseudo-label token as a target, the student inherits the teacher's errors. We show that using the same pseudo-labels as a reward reference for Group Relative Policy Optimization (GRPO) is more robust to label noise. In the banking domain, GRPO yields 29.3% to 56.2% relative WER improvements over SFT on Whisper-generated labels, and the advantage holds across four Whisper sizes, four teacher families, three domains and four languages. While SFT reproduces almost 100% of teacher errors verbatim, GRPO passes through only 27%. Rollout statistics explain why, erroneous pseudo-label words rarely appear in on-policy rollouts, so group-relative advantages stay aligned with the clean transcript, whereas SFT forces them into the policy's support and collapses the reward variance GRPO relies on.

</details>

---

### [[20_Research/Papers/大模型/SCI-AGENT-EXAM_Benchmarking_Agents_on_Scientific_Research_Tasks|SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks]]

![[assets/2610.32441_figure.png|800]]

- **arXiv**: [2610.32441](https://arxiv.org/abs/2610.32441)
- **PDF**: https://arxiv.org/pdf/2610.32441
- **详细分析**: [[20_Research/Papers/大模型/SCI-AGENT-EXAM_Benchmarking_Agents_on_Scientific_Research_Tasks|SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks]]
- **作者**: Tianyun Zhong, Wei Wang, Jialin Li, Jianhong Tu, Liyao Li, Chuqiao Kuang, Tianshi Zheng, Songchi Zhou, Weiqi Zhai, Qile Jin, Jiajia Li, Jiasheng Zheng...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ASI-Bench, CORE-Bench, DiscoveryBench, PaperBench, ResearchCodeBench, SciBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, limiting a comprehensive characterization of scientific agents' strengths and weaknesses in realistic research workflows. We introduce SCI-AGENT-EXAM, a workflow-oriented benchmark comprising 120 expert-curated tasks across 11 scientific fields and 7 research task types defined by the Scientific Workflow Task Taxonomy (SWTT). Each task requires both executable artifacts (e.g., code and scripts) and textual artifacts (e.g., reports and explanations). To evaluate the heterogeneous task outputs, we develop a hybrid evaluation protocol combining deterministic programmatic verification for executable artifacts with a calibrated, expert-validated LLM-based judge for textual artifacts. Beyond outcome assessment, we analyze progress and solution stability along execution trajectories to characterize how agents reach their final results. Experiments with 10 frontier LLM agents reveal substantial performance gaps: GPT-6 Astra achieves the highest overall score of 80.9, yet only 26.0% of its runs exceed the 0.95 success threshold. Further analyses uncover distinct capability profiles across scientific task types and substantial variation in execution efficiency and stability. Our code and data are available at https://github.com/SKYLENAGE-AI/Sci-Agent-Exam.

</details>

---

### [[20_Research/Papers/大模型/Profile-Driven_User_Simulation_via_Reinforcement_Learning_with_Hierarchical_Rewards_for_Task-Oriented_Dialogues|Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues]]

![[assets/2610.32435_figure.png|800]]

- **arXiv**: [2610.32435](https://arxiv.org/abs/2610.32435)
- **PDF**: https://arxiv.org/pdf/2610.32435
- **详细分析**: [[20_Research/Papers/大模型/Profile-Driven_User_Simulation_via_Reinforcement_Learning_with_Hierarchical_Rewards_for_Task-Oriented_Dialogues|Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues]]
- **作者**: Juan Li, Fangshu Chang, Xinyi Jiang, Ling Huang, Yunzhang Chen
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.45，强化学习 0.8）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DuetSim, ProfileSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building Task-Oriented Dialogue (TOD) systems for high-value scenarios such as financial marketing requires large volumes of domain-specific dialogue data, which privacy regulations, annotation costs, and the need for expert labor make hard to obtain. User simulation offers a remedy, but existing methods target general-domain dialogue and exhibit two key limitations: insufficient modeling of domain-specific business processes and compliance constraints, and inadequate capture of the colloquial, spoken-language character of voice interactions. We propose ProfileSim, a profile-driven user simulation framework for financial marketing outbound calls. It jointly models user profiles---demographics and Big Five personality traits---and business profiles---intents reverse-engineered from real call logs---enabling fine-grained control over simulated behavior. The base model is fine-tuned on real voice dialogue data and refined by Group Relative Policy Optimization (GRPO) with hierarchical rewards at the dialogue and utterance levels. Paired with a customer service agent integrating Standard Operating Procedure (SOP) constraints and Retrieval-Augmented Generation (RAG), ProfileSim achieves the highest colloquial naturalness, the strongest user profile adherence and the lowest agent score on long-tail intents among all evaluated user generators, while producing substantially shorter user utterances at comparable business compliance. The generated dialogue data is designed to support intent recognition training, agent evaluation, and rapid cold-start deployment.

</details>

---

### [[20_Research/Papers/大模型/Can_LLM_Annotators_Match_Human_Consistency_Benchmarking_Human_Agreement_and_Optimizing_Multi-Agent_with_Contrastive_Knowledge|Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge]]

![[assets/2610.32415_figure.png|800]]

- **arXiv**: [2610.32415](https://arxiv.org/abs/2610.32415)
- **PDF**: https://arxiv.org/pdf/2610.32415
- **详细分析**: [[20_Research/Papers/大模型/Can_LLM_Annotators_Match_Human_Consistency_Benchmarking_Human_Agreement_and_Optimizing_Multi-Agent_with_Contrastive_Knowledge|Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge]]
- **作者**: Xiaopeng Ke, Zhixin Wang, Xuebo Liu, Xinyu Ma, Xing Zheng, Bowen Song, Weiqiang Wang, Min Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases, where single-labeled dataset fail to reflect this disagreement. This gap also limits existing single-agent and workflow-based annotation systems, which often lack adaptability to complex, evolving guidelines. To bridge this gap, we introduce ANT-A Benchmark, a real-world multi-annotator benchmark spanning 7 datasets across domains and modalities, with task-specific guidelines and 5 independent human labels per instance. ANT-A enables a distribution-aware evaluation, using Fleiss kappa to assess how closely model annotations align with human labeling distributions. We further propose ANT-OR, a multi-agent annotation framework that refines prompts by distilling contrastive decision rules from positive and negative feedback. Experiments show that ANT-OR improves agreement@&gt;=2 accuracy by 4.5 points over the strongest baseline and achieves the highest alignment with human annotator distributions as measured by Fleiss kappa within 2 points. Code and benchmark are available at https://github.com/Krueske/ANT-OR.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Final_Outcomes_Quantifying_Claim-Level_Information_Dynamics_in_Multi-Agent_LLM_Interaction|Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction]]

![[assets/2610.32333_first_page.png|800]]

- **arXiv**: [2610.32333](https://arxiv.org/abs/2610.32333)
- **PDF**: https://arxiv.org/pdf/2610.32333
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Final_Outcomes_Quantifying_Claim-Level_Information_Dynamics_in_Multi-Agent_LLM_Interaction|Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction]]
- **作者**: Haocheng Jiang, Herun Wan, Yongyuan Peng, Minnan Luo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When LLM-powered agents interact, information is repeatedly shared, expanded, and forgotten, yet multi-agent evaluation typically focuses on final task outcomes. We study such interaction as claim-level information dynamics and propose RIVER, which decomposes agent outputs into atomic claims and evaluates three complementary dimensions: convergence, exploration, and retention. Convergence captures cross-agent claim correspondence and stance alignment; exploration captures semantic breadth and extension beyond the source; and retention tracks source preservation and the persistence of new claims across stages and lineages. We evaluate five interaction strategies on 40 controlled news-generation cases. Repeatedly pooled interaction promotes convergence but narrows the information space, whereas distributed relay yields broader, less shared information. Further comparisons show that method-specific constraints increase exploration while weakening convergence and retention. Our findings suggest that collective information dynamics are better explained by underlying information-flow mechanisms than by simple downstream performance.

</details>

---

### [[20_Research/Papers/强化学习/CRM-Agent-Bench_Benchmarking_Tool-Using_Agents_in_Stateful_Enterprise_Environments|CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments]]

![[assets/2610.32004_figure.png|800]]

- **arXiv**: [2610.32004](https://arxiv.org/abs/2610.32004)
- **PDF**: https://arxiv.org/pdf/2610.32004
- **详细分析**: [[20_Research/Papers/强化学习/CRM-Agent-Bench_Benchmarking_Tool-Using_Agents_in_Stateful_Enterprise_Environments|CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments]]
- **作者**: Monojit Banerjee, Zhujun Lan, Defu Cao
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRM-Agent-Bench, Evaluation-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying language agents in real applications demands more than the right answer: an agent must execute a multi-step business process correctly, follow domain-specific rules, and interact with a user across a dialogue, where the gap between saying and doing is the gap between a satisfied customer and a real loss. We argue that a deployable-agent benchmark should jointly assess four facets: the outcome an agent reaches, the trajectory it takes, its operational viability, and its policy compliance. Customer relationship management (CRM), where mutable records meet operational rules and consequential effects, exercises all four. We introduce CRM-Agent-Bench, an execution-grounded benchmark of 555 stateful, multi-turn tasks across nine business domains and 36 capability tags. Each task supplies a task-specific executable contract drawn from checks over actions, arguments, order, response, target state, and protected state; success is the strict conjunction of the checks declared for that task. We evaluate the complete agent system through these contracts and report scored coverage, latency, and cost. Across sixteen systems evaluated on the audited final release, strict success spans 64.32% to 83.60%; the closely grouped leading systems nonetheless diverge sharply in cost and per-domain reliability. CRM-Agent-Bench offers an auditable framework for measuring contract-grounded business-transaction integrity and adherence to task-declared benchmark policies, with a portable structure designed for extension as models improve. Github repository: https://github.com/salesforce-misc/crm-agent-bench

</details>

---
