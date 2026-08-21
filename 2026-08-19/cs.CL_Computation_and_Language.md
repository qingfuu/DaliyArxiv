# cs.CL | Computation and Language | 2026-08-19

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/大模型/Multi-Agent_AI_System_for_Radiology_Report_Structuring_and_Quality_Assurance_with_Independent_Radiologist_Evaluation|Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation]]

![[assets/2608.18072_figure.png|800]]

- **arXiv**: [2608.18072](https://arxiv.org/abs/2608.18072)
- **PDF**: https://arxiv.org/pdf/2608.18072
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_AI_System_for_Radiology_Report_Structuring_and_Quality_Assurance_with_Independent_Radiologist_Evaluation|Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation]]
- **作者**: Iryna Hartsock, Cesar Lam, Christopher Otteni, Aliya Qayyum, Robert Gatenby, Cyrillo Araujo, Ghulam Rasool
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at the sentence level using regex rules and local large language models. It also detected mismatches between the Findings and Impression sections, or within sections; gender-anatomy conflicts; and undocumented communication of critical findings. Two board-certified radiologists independently evaluated a 45-report subset. Results: The multi-agent system structured the Findings sections of all reports (22,270 sentences) into a predefined anatomical format while retaining the original report content. The system flagged 90 (14.1%) reports, most commonly for section mismatches (80 reports, 12.5%). In the radiologist evaluation, both reviewers agreed that 31 (69%) were correctly restructured, 2 reports (4%) were incorrectly restructured, and disagreed on the remaining 12 reports (27%). Both reviewers agreed that no clinically important information was omitted and no fabricated content was introduced. Overall QA performance was rated as "excellent" or "good" in 84% of the evaluated reports, with the remaining reports rated as "fair". Conclusion: A locally deployed multi-agent AI system combined radiology report structuring and quality assurance within a single workflow. The system demonstrated favorable performance in radiologist evaluation. Such systems may support standardization of reporting and quality assurance in radiology practice.

</details>

---

### [[20_Research/Papers/大模型/Chain-of-Experience_for_Continual_LLM_Improvement|Chain-of-Experience for Continual LLM Improvement]]

![[assets/2608.18027_figure.png|800]]

- **arXiv**: [2608.18027](https://arxiv.org/abs/2608.18027)
- **PDF**: https://arxiv.org/pdf/2608.18027
- **详细分析**: [[20_Research/Papers/大模型/Chain-of-Experience_for_Continual_LLM_Improvement|Chain-of-Experience for Continual LLM Improvement]]
- **作者**: Haoqin Tu, Yunhao Fang, Yizhong Wang, Cihang Xie, Shen Yan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Chain-of-Experience for Continual LLM Improvement》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GPQA, LiveBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans continuously learn from experience, whereas conventional large language model (LLM) evaluations ignore the models' ability to improve through inference-time interaction. In this paper, we study how LLMs learn from iterative experience at test time, a setting we refer to as Chain-of-Experience (CoE), where models accumulate experiential traces through iterative interactions with self or environmental feedback to form a continual improvement loop beyond zero-shot inference. We instantiate CoE with diverse feedback mechanisms, including model self-feedback and environmental signals such as correctness or public coding test pass rates, and evaluate across math, coding, and knowledge domains using 8 LLMs, including GPT-5, Gemini-2.5 Pro, Claude-4.5 Sonnet. Our study shows that leveraging iterative experience consistently outperforms feedback-free baselines, achieving substantial gains with self feedback alone, alongside a 5.6% overall improvement and 19% lower API cost across tasks and models. We further show that combining complementary feedback channels (e.g., model and correctness signals) yields additional gains, and that CoE delivers higher accuracy per token than existing test-time strategies. We observe a positive correlation between LLM base ability and improvement capacity, and show that models remain robust under weak or spurious feedback, with different feedback contributing to distinct improvement aspects and most gains emerging early in the iterations.

</details>

---

### [[20_Research/Papers/大模型/Judge,_Retrieve,_or_Abstain_Uncertainty-Guarded_LLM_Judging_with_Provable_Risk_Guarantees|Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees]]

![[assets/2608.17994_first_page.png|800]]

- **arXiv**: [2608.17994](https://arxiv.org/abs/2608.17994)
- **PDF**: https://arxiv.org/pdf/2608.17994
- **详细分析**: [[20_Research/Papers/大模型/Judge,_Retrieve,_or_Abstain_Uncertainty-Guarded_LLM_Judging_with_Provable_Risk_Guarantees|Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees]]
- **作者**: Sher Badshah, Ali Emami, Hassan Sajjad
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the former enables efficient evaluation, the judge may hallucinate or lack sufficient evidence for its verdict. Conversely, tool augmentation can provide additional evidence but introduces extra computational cost and requires an appropriate mechanism to determine when and how that evidence should be used reliably. More importantly, neither approach alone provides formal control over the risk of accepted verdicts or guarantees their reliability at a specified level. We propose a risk-controlled framework that calibrates uncertainty thresholds on a held-out set so that the false discovery rate among accepted verdicts remains below a user-specified level~$α$ with high probability, using finite-sample Clopper--Pearson intervals. When the parametric mode is not sufficiently confident, the instance is routed to a retrieval-augmented mode, where the judge gathers web evidence and re-evaluates the instance under a second calibrated threshold. The finite-sample guarantee carries over to this two-threshold routing without additional assumptions. Across open-domain QA benchmarks and judges of varying scales, the framework maintains the target error rate while achieving substantially higher coverage than single-mode baselines.

</details>

---

### [[20_Research/Papers/大模型/An_Empirical_Study_of_Reward_Specification_and_Benchmark_Reliability_in_GRPO-based_LLM_Unlearning|An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning]]

![[assets/2608.17804_first_page.png|800]]

- **arXiv**: [2608.17804](https://arxiv.org/abs/2608.17804)
- **PDF**: https://arxiv.org/pdf/2608.17804
- **详细分析**: [[20_Research/Papers/大模型/An_Empirical_Study_of_Reward_Specification_and_Benchmark_Reliability_in_GRPO-based_LLM_Unlearning|An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning]]
- **作者**: Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, anti-refusal shaping, rubric-based broad answering, and an explicit refusal contrast, with and without SFT warm-up. The experiments show that optimization success is not equivalent to behavioral unlearning: RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics can point to different conclusions. We trace these disagreements to reward-hacking endpoints, policy-support limits in GRPO, benchmark probes that miss endpoint changes, and rewards that can select broad-topic answering with low semantic leakage during optimization.

</details>

---

### [[20_Research/Papers/强化学习/Thinking_in_a_Low-Resource_Language_What_SFT_Builds,_What_RL_Fixes,_What_Accuracy_Cannot_See|Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See]]

![[assets/2608.17744_figure.png|800]]

- **arXiv**: [2608.17744](https://arxiv.org/abs/2608.17744)
- **PDF**: https://arxiv.org/pdf/2608.17744
- **详细分析**: [[20_Research/Papers/强化学习/Thinking_in_a_Low-Resource_Language_What_SFT_Builds,_What_RL_Fixes,_What_Accuracy_Cannot_See|Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See]]
- **作者**: Ayoub Kirouane, Christos Petrocheilos
- **cs 子类**: cs.CL, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ECQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Take three frontier mixture-of-experts models (Alibaba, OpenAI, NVIDIA; 3.6-4.0B active parameters each) and fine-tune them to reason in a low-resource language. On accuracy benchmarks almost nothing happens, and the benchmark itself is noise at this scale: changing only the random seed moves the score by 7.7 points, more than every data and recipe effect we measured. That null is our first result. The real changes live where accuracy cannot see. Base models never think in Greek: 0 of 1,000 reasoning traces, even when the question is Greek, so the model answers correctly while reasoning in a form its user cannot read, audit, or correct. After supervised fine-tuning (SFT), every released checkpoint reasons in the language of the question on ~98% of items, one family at 3x fewer tokens, with judged grammaticality improving on all four models and general ability within a few points of each base: nothing was forgotten, and fluency was gained. We propose six behavioural dimensions that make such changes measurable, each gated to reject any metric that correlates with output length, and we report how our own instruments lied: six failures, each caught by a control. What SFT cannot do is fix its own defects: a quarter of answers skip the requested format, answers leak into the reasoning channel, and an explicit "think in English" is obeyed under half the time. Reinforcement learning with verifiable rewards, pre-registered before training, fixes the first two outright (fallback 24% to 2.5%, leak 3.5% to 0.0%, both against a flat random-reward control) and moves the third (+9.1pp), while the Greek reasoning habit survives an accuracy-only gradient untouched. We release five checkpoints. The instruments, the controls and the pre-registration travel to any low-resource language; Greek is the case that let us measure them.

</details>

---

### [[20_Research/Papers/强化学习/Write,_Execute,_Refine_From_Skill_Followers_to_Skill_Optimizers_via_Reinforcement_Learning_from_Execution_Feedback|Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback]]

![[assets/2608.17587_figure.png|800]]

- **arXiv**: [2608.17587](https://arxiv.org/abs/2608.17587)
- **PDF**: https://arxiv.org/pdf/2608.17587
- **详细分析**: [[20_Research/Papers/强化学习/Write,_Execute,_Refine_From_Skill_Followers_to_Skill_Optimizers_via_Reinforcement_Learning_from_Execution_Feedback|Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback]]
- **作者**: Kang Peng, Zhiwei Zhang, Yichen Zhang, Zezhong Wang, Yiming Du, Geng Tu, Baojun Wang, Bin Liang, Ruifeng Xu, Kam-Fai Wong
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.95（加权：大模型 0.35，强化学习 0.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkillRL, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Expert-written natural language skills can improve tool-using agents, yet agent-authored skills perform 8-11 points worse than using no skill. This gap suggests that following procedural guidance and improving it from execution evidence are distinct capabilities. Inference time loops can repair skills but do not improve the model that writes the next one. We study how to organize execution experience from intermediate skills into training states for an optimizer. We introduce WER (Write, Execute, and Refine), a multi-phase framework that trains a Skill Optimizer outside a frozen executor. The optimizer proposes skills, a frozen agent executes each repeatedly, and a programmatic verifier scores the outcomes. The scores provide relative credit and select mixed-outcome records. Matched successful and failed trajectories from these records form the next phase's refinement states, so the optimizer learns from the consequences of its earlier outputs. On BFCL v4 multi-turn and tau2-bench, WER improves average Pass@1 over the no-skill baseline by 7.80 and 3.85 points, respectively. Under an identical refinement workflow, it outperforms the same backbone without optimizer training by 9.35 and 10.29 points. The trained 4B optimizer reaches 76.63 percent on BFCL v4, outperforming all evaluated off-the-shelf general-purpose models used as skill optimizers on average.

</details>

---

### [[20_Research/Papers/大模型/Auditing_Exposure_to_Harmful_Content_on_TikTok_using_Multimodal_Language_Models_A_Cross-National,_Age-Stratified_Study|Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study]]

![[assets/2608.17583_figure.png|800]]

- **arXiv**: [2608.17583](https://arxiv.org/abs/2608.17583)
- **PDF**: https://arxiv.org/pdf/2608.17583
- **详细分析**: [[20_Research/Papers/大模型/Auditing_Exposure_to_Harmful_Content_on_TikTok_using_Multimodal_Language_Models_A_Cross-National,_Age-Stratified_Study|Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study]]
- **作者**: Hamidreza Saffari, Francesco Pierri
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online video platforms can expose young users to harmful content, but independent audits remain difficult because video annotation is costly and moderation judgments vary across languages. We audit TikTok in France, Italy, and Sweden with sockpuppet accounts representing four age personas (13, 16, 19, 40), collecting 36,971 videos from passive For-You-page scrolling and active sessions that scroll, search for harm keywords, and scroll again. To scale annotation, we validate four multimodal LLMs against native-speaker labels on a 300-video reference set. Gemini 2.5 Flash with eight sampled frames plus text performs best (aggregate kappa = 0.42), at half the per-call cost of native-video upload, and we apply it to a 10% sample for approximately \$50 in total API spend across both modalities. Keyword search returns 35-56% harmful content, a 1.5-7.5x increase over the scrolling baseline in ten of twelve country-age combinations; the spike is temporary and flattens the age differences observed in France and Sweden. Under passive scrolling, Italy has the highest harm rate at every age, with Italian age-19 reaching 48.6%. Overall, MLLM-based auditing offers a scalable approach for cross-national youth-safety audits, while provider safety filters (1.1% refusal rate) under-count the most explicit harms.

</details>

---

### [[20_Research/Papers/大模型/Reflex-Guard_A_Low-Latency_Guardrail_for_LLM_Prompt_Safety_Using_Dense_Semantic_Embeddings|Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings]]

![[assets/2608.17556_figure.png|800]]

- **arXiv**: [2608.17556](https://arxiv.org/abs/2608.17556)
- **PDF**: https://arxiv.org/pdf/2608.17556
- **详细分析**: [[20_Research/Papers/大模型/Reflex-Guard_A_Low-Latency_Guardrail_for_LLM_Prompt_Safety_Using_Dense_Semantic_Embeddings|Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings]]
- **作者**: Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon, Abu-fuad Ahmad, Thi Hong Tran
- **cs 子类**: cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderation endpoints raises significant data privacy concerns. This paper introduces Reflex-Guard, a lightweight guardrail that runs locally. It uses jailbreak-aware preprocessing, compact sentence-transformer embeddings, and seven fast binary classifiers. Together, these components enable high-accuracy prompt safety filtering with much lower latency than existing solutions. Through systematic evaluation on a strategically balanced dataset of 30,568 samples drawn from five complementary sources, we demonstrate that Reflex-Guard achieves 95.9% recall on harmful prompts at 37.6 ms end-to-end latency. It is faster than existing baselines, including Llama Guard 2 at 255 ms and SafeDecoding at 723 ms. It can detect 100% of GCG suffix attacks and Base64-encoded prompts using the default threshold. However, DrAttack structured prompts required lowering the threshold to 0.03 for optimal detection, as they produced a distinct probability distribution. Reflex-Guard achieves Reflex Efficiency Score (RES) scores up to 16.79, significantly outperforming Llama Guard 2 (11.90) and SafeDecoding (9.80). This analysis offers practical deployment advice and shows that different attack types occupy distinct regions in the embedding probability space.

</details>

---

### [[20_Research/Papers/大模型/Decomposition_Attacks_Across_Unlinkable_Identities_Limits_of_Stateful_Defenses_for_LLM_Services|Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services]]

![[assets/2608.17445_first_page.png|800]]

- **arXiv**: [2608.17445](https://arxiv.org/abs/2608.17445)
- **PDF**: https://arxiv.org/pdf/2608.17445
- **详细分析**: [[20_Research/Papers/大模型/Decomposition_Attacks_Across_Unlinkable_Identities_Limits_of_Stateful_Defenses_for_LLM_Services|Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services]]
- **作者**: Bowen Sun, Zhengyue Zhao, Xiaogeng Liu, Yinzhi Cao, Chaowei Xiao
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answers elsewhere, leaving no reliable grouping signal. We ask whether decomposition attacks can still be stopped under this setting. For a fixed attack strategy without retries, we prove that the achievable security and utility tradeoff depends entirely on how benign requests for the same capabilities are grouped. Persistent, recognizable groups permit a useful defense; fresh, indistinguishable groups do not. When attackers can retry and learn from Allow/Block decisions, this useful operating point disappears: the feedback reveals what passes but not whether a block was correct. Experiments on 91 executable tasks and 11,393 capability-matched benign requests support these results. Under a 1% denial cap for these requests and a 0.5% cap for unrelated background traffic, all ten tested policies, including one privileged policy with an exact request-to-operation map, either fail to stop attacks or exceed the budget. On defense-unseen task families, attack success is at least 99% after one attempt and 100% after two. Effective defenses therefore require additional evidence or mechanisms tied to grouping, such as reliable identity linkage, costs for fresh identities, or control over answer use.

</details>

---

### [[20_Research/Papers/大模型/Towards_Safer_RAG_Only_Agents_Capable_of_System_2_Thinking_may_Access_Untrusted_Documents|Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents]]

![[assets/2608.17153_first_page.png|800]]

- **arXiv**: [2608.17153](https://arxiv.org/abs/2608.17153)
- **PDF**: https://arxiv.org/pdf/2608.17153
- **详细分析**: [[20_Research/Papers/大模型/Towards_Safer_RAG_Only_Agents_Capable_of_System_2_Thinking_may_Access_Untrusted_Documents|Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents]]
- **作者**: Mehrdad Ghassabi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FiQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

</details>

---

### [[20_Research/Papers/大模型/Emotion_Across_Speech_and_Faces_Shared_Affective_Mechanisms_in_Multimodal_Foundation_Models|Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models]]

![[assets/2608.17102_figure.png|800]]

- **arXiv**: [2608.17102](https://arxiv.org/abs/2608.17102)
- **PDF**: https://arxiv.org/pdf/2608.17102
- **详细分析**: [[20_Research/Papers/大模型/Emotion_Across_Speech_and_Faces_Shared_Affective_Mechanisms_in_Multimodal_Foundation_Models|Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models]]
- **作者**: Xiutian Zhao, Luqi Sun, Björn Schuller, Berrak Sisman
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern multimodal foundation models (MFMs) have made rapid progress on tasks requiring integrated perception across speech, vision, and language, including emotion recognition. However, it remains unclear whether they recognize speech and facial emotion through shared affective functional units or modality-specific pathways. We explore emotion-sensitive neurons (ESNs), sparse decoder neurons selectively associated with emotion categories, in three MFMs: Gemma-4-12B-it, MiniCPM-o-4.5, and Qwen2.5-Omni-7B. Using speech emotion recognition and facial expression recognition as complementary probes, we identify acoustic and visual ESNs. Visual ESNs are causally meaningful: deactivating them selectively impairs recognition of the associated facial emotion, whereas steering their activations selectively enhances recognition of that emotion relative to other emotion categories. Acoustic and visual ESNs further show emotion-matched overlap and similar layer-wise distributions, indicating partial structural alignment between affective representations across speech and faces. Finally, cross-modal interventions reveal bidirectional causal transfer: ESNs identified from one modality produce emotion-specific effects when applied to the other. Our findings provide one of the first cross-modality activation-level analyses of affective functional units in MFMs, suggesting that speech and facial emotion recognition partially converge onto sparse decoder-level components that can be localized and manipulated without training.

</details>

---

### [[20_Research/Papers/具身智能/Uncertainty-Aware_Decision_Making_in_Multimodal_Large_Language_Models|Uncertainty-Aware Decision Making in Multimodal Large Language Models]]

![[assets/2608.17084_figure.png|800]]

- **arXiv**: [2608.17084](https://arxiv.org/abs/2608.17084)
- **PDF**: https://arxiv.org/pdf/2608.17084
- **详细分析**: [[20_Research/Papers/具身智能/Uncertainty-Aware_Decision_Making_in_Multimodal_Large_Language_Models|Uncertainty-Aware Decision Making in Multimodal Large Language Models]]
- **作者**: Abderrahmene Boudiaf, Irfan Hussain, Sajid Javed
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.95（加权：具身智能 0.3，大模型 0.65）
- **关联关键词**: Multimodal, EmbodiedAI, Systems

#### 研究背景与动机

《Uncertainty-Aware Decision Making in Multimodal Large Language Models》归入 大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) increasingly answer questions whose correctness depends on visual, textual, temporal, acoustic, document, chart, or embodied evidence. Their failures are therefore not only linguistic. A fluent answer may conceal poor input quality, a perceptual error, weak grounding, conflict between modalities, unstable reasoning, distribution shift, or a question that is not answerable from the supplied evidence. This survey organizes the literature on uncertainty-aware MLLMs around a decision-centered framework: uncertainty sources give rise to observable signals, signals must be calibrated or controlled for risk, and calibrated uncertainty should determine the system action. We review work on token and logit uncertainty, semantic disagreement, perturbation instability, grounding and attribution scores, verbalized confidence, verifier and judge scores, conformal prediction, selective answering, abstention, clarification, retrieval, self-checking, and escalation. The central argument is that uncertainty should not be evaluated only as a confidence number; it should be evaluated by whether it improves behavior under insufficient, conflicting, shifted, or high-risk multimodal evidence. We position this survey against text-only uncertainty and abstention surveys, broad MLLM surveys, MLLM hallucination surveys, and safety-oriented reviews. We conclude with open problems in source-aware decomposition, action-aware benchmarks, calibration under shift, black-box uncertainty estimation, broader modality coverage, reproducible reporting, and human-centered uncertainty communication.

</details>

---
