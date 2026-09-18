# cs.CL | Computation and Language | 2026-09-16

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/Enhancing_Accessibility_of_Medical_Texts_through_Large_Language_Model-Driven_Plain_Language_Adaptation|Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation]]

![[assets/2609.17398_figure.png|800]]

- **arXiv**: [2609.17398](https://arxiv.org/abs/2609.17398)
- **PDF**: https://arxiv.org/pdf/2609.17398
- **详细分析**: [[20_Research/Papers/大模型/Enhancing_Accessibility_of_Medical_Texts_through_Large_Language_Model-Driven_Plain_Language_Adaptation|Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation]]
- **作者**: Ting-Wei Chang, Hen-Hsen Huang, Hsin-Hsi Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Enhancing Accessibility of Medical Texts through Large Language Model-Driven Plain Language Adaptation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the challenge of making complex healthcare information more accessible through automated Plain Language Adaptation (PLA). PLA aims to simplify technical medical language, bridging a critical gap between the complexity of healthcare texts and patients' reading comprehension. Recent advances in Large Language Models (LLMs), such as GPT and BART, have opened new possibilities for PLA, especially in zero-shot and few-shot learning contexts where task-specific data is limited. In this work, we leverage the capabilities of LLMs such as GPT-4o-mini, Gemini-1.5-pro, and LLaMA for text simplification. Additionally, we incorporate Mixture-of-Agents (MoA) techniques to enhance adaptability and robustness in PLA tasks. Key contributions include a comparative analysis of prompting strategies, finetuning with QLoRA on different LLMs, and the integration of MoA technique. Our findings demonstrate the effectiveness of LLM-driven PLA, showcasing its potential in making healthcare information more comprehensible while preserving essential content.

</details>

---

### [[20_Research/Papers/大模型/Cascade_Hierarchical_Recoverability_Control_for_Large_Language_Model_Unlearning|Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning]]

![[assets/2609.16890_figure.png|800]]

- **arXiv**: [2609.16890](https://arxiv.org/abs/2609.16890)
- **PDF**: https://arxiv.org/pdf/2609.16890
- **详细分析**: [[20_Research/Papers/大模型/Cascade_Hierarchical_Recoverability_Control_for_Large_Language_Model_Unlearning|Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning]]
- **作者**: Qingchen Yu, Shiying Duan, Xiaodong Li, Yuhua Wang, Zhiyu Li, Shiji Zhou, Yifan Sun, Zhaoxin Fan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《Cascade: Hierarchical Recoverability Control for Large Language Model Unlearning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) unlearning is essential for removing sensitive or copyrighted knowledge while preserving general utility. Existing methods often leave residual knowledge in intermediate representations, which can still be recovered. To address this, we propose Cascade, a hierarchical recoverability control framework that minimizes the internal identifiability of target knowledge. Cascade combines three complementary controls: path-level routing to suppress privacy-associated activation routes, representation-level compression to reduce geometric separability, and decoding-level intervention to limit residual recovery. Experiments on TOFU, MUSE-News, and WMDP, including robustness tests with query reformulation and extraction-style prompts, show that Cascade effectively reduces recoverability while maintaining stable model utility.

</details>

---

### [[20_Research/Papers/大模型/ImpossibleRubrics_Stress-Testing_Generated_Rubrics_as_Reward_Signals|ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals]]

![[assets/2609.16816_first_page.png|800]]

- **arXiv**: [2609.16816](https://arxiv.org/abs/2609.16816)
- **PDF**: https://arxiv.org/pdf/2609.16816
- **详细分析**: [[20_Research/Papers/大模型/ImpossibleRubrics_Stress-Testing_Generated_Rubrics_as_Reward_Signals|ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals]]
- **作者**: Bowen Qin, Yi Xie, Yesheng Liu, Xi Yang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.87（加权：大模型 0.35，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AbstentionBench, CheckEval, G-Eval, GPQA, HealthBench, RM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language model-generated rubrics are increasingly used as reward signals for rubric-based reinforcement learning, LLM-as-a-judge evaluation, and automated grading. Such rubrics are reliable only if they reward honest answers over adversarial answers optimized to exploit them. Yet their robustness to such optimization remains poorly understood. We isolate the hardest regime: impossible tasks, where the prompt pressures the model toward an unsupported conclusion, so the only honest response is to acknowledge the impossibility. We introduce ImpossibleRubrics, a benchmark of 169 impossible tasks spanning six impossibility categories, each paired with a verifiable oracle certificate specifying what an honest answer may and may not claim, together with 48 answerable controls. Rather than providing fixed rubrics, ImpossibleRubrics provides task environments and certificates, allowing rubrics to be generated downstream and then adversarially tested for whether they reward certificate-violating answers. Eleven generators are exploited 8--26% of the time on the unbiased 150-of-169 environment cut; on a deliberately selected stress cut the strongest generator we measured is still exploited 36% while a certificate-faithful rubric is exploited 0%, so what we measure is a rubric-quality gap, not task impossibility. One result runs against intuition. A single generic rubric ("be decisive, penalize hedging") used unchanged for every task is exploited 64% of the time, and seven of the eleven generators are exploited more often than that while writing a rubric tailored to each one. The tailored criteria appear to tell an attacker which claim to fabricate. The problem is not that rubrics are vague; it is that they are specific about the wrong things.

</details>

---

### [[20_Research/Papers/大模型/TIAO_Token_Importance-Aware_Policy_Optimization_for_Text_Summarization|TIAO: Token Importance-Aware Policy Optimization for Text Summarization]]

![[assets/2609.16748_figure.png|800]]

- **arXiv**: [2609.16748](https://arxiv.org/abs/2609.16748)
- **PDF**: https://arxiv.org/pdf/2609.16748
- **详细分析**: [[20_Research/Papers/大模型/TIAO_Token_Importance-Aware_Policy_Optimization_for_Text_Summarization|TIAO: Token Importance-Aware Policy Optimization for Text Summarization]]
- **作者**: Qixiu Li, Chenlong Bao, Xiang Zhu, Xiaoyong Li, Ruixin Cao, Shukai Chen, Zhenxiong Zhou
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.25，强化学习 1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《TIAO: Token Importance-Aware Policy Optimization for Text Summarization》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text summarization requires models to condense content while preserving key qualities such as consistency and coherence. Large language models (LLMs) have shown strong performance on this task and can be further improved through reinforcement learning (RL). However, most existing methods apply reward signals directly to undifferentiated token sequences, overlooking the varying importance of individual tokens to word and sentence level quality in summarization. In this paper, we propose Token Importance-Aware Policy Optimization (TIAO), a novel reinforcement learning strategy that explicitly leverages token-importance awareness. Specifically, TIAO identifies core tokens based on token dependency and reweights a trajectory's advantage according to its overall dependencies. Experiments on the real world dataset show that our TIAO achieves highly competitive results, and that a 7B foundation model enhanced by TIAO performs comparably to GPT-4 and GPT-5-nano. Code is available at this https URL

</details>

---

### [[20_Research/Papers/强化学习/Rewarding_Reasoning,_Not_Answers_Fixing_and_Bounding_Test-Time_Reinforcement_Learning_on_Medical_QA|Rewarding Reasoning, Not Answers: Fixing and Bounding Test-Time Reinforcement Learning on Medical QA]]

![[assets/2609.16660_figure.png|800]]

- **arXiv**: [2609.16660](https://arxiv.org/abs/2609.16660)
- **PDF**: https://arxiv.org/pdf/2609.16660
- **详细分析**: [[20_Research/Papers/强化学习/Rewarding_Reasoning,_Not_Answers_Fixing_and_Bounding_Test-Time_Reinforcement_Learning_on_Medical_QA|Rewarding Reasoning, Not Answers: Fixing and Bounding Test-Time Reinforcement Learning on Medical QA]]
- **作者**: Kailong Fan, Anqi Pu, Yichen Wu, Wanhua Li, Yicong Li, Hanspeter Pfister, Huafeng Liu, Xiang Li, Quanzheng Li, Ning Guo
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Rewarding Reasoning, Not Answers: Fixing and Bounding Test-Time Reinforcement Learning on Medical QA》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time reinforcement learning adapts a model on its own unlabeled test set using majority-vote pseudo-labels and has shown strong results in mathematics. We show that this recipe collapses on medical multiple-choice QA: accuracy stagnates while output diversity rapidly declines. Through a controlled experiment that keeps the questions, model, and optimizer fixed while changing only the answer space, we trace this failure to answer-space structure rather than domain difficulty. In small answer spaces, incorrect rollouts often collide on the same wrong pseudo-label and reinforce it; in large answer spaces, they disperse and receive little reward. This diagnosis motivates PROSE, Process Reward Guided Self-Training, which rewards reasoning quality instead of answer agreement. PROSE scores each reasoning step with a medical process reward model, assigns the trajectory reward as the minimum score across steps, and enforces answer-format constraints. Without labels, PROSE substantially improves a general Llama model, surpassing purpose-built medical models and matching much larger systems. Because the process signal is internalized into the policy, the adapted model requires no reward model at inference and transfers its gains to unseen datasets. We further show that the minimum aggregation is essential: mean aggregation can be exploited, saturating the proxy reward while degrading accuracy.

</details>

---

### [[20_Research/Papers/大模型/Spurious_Tool_Use_When_RL_Agents_Learn_the_Wrong_Reason_to_Act|Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act]]

![[assets/2609.16268_figure.png|800]]

- **arXiv**: [2609.16268](https://arxiv.org/abs/2609.16268)
- **PDF**: https://arxiv.org/pdf/2609.16268
- **详细分析**: [[20_Research/Papers/大模型/Spurious_Tool_Use_When_RL_Agents_Learn_the_Wrong_Reason_to_Act|Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act]]
- **作者**: Yiwei Yang, Haoxiang Zhang, Bingbing Wen, Yao Lu, Yuchen Wu, Lei Zhang, Julian McAuley, Pan Lu, Bill Howe
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.15（加权：大模型 0.95，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic environments combining factual question answering and mathematical reasoning tasks, and inject cues that are strongly correlated with specific tools during training but causally irrelevant to tool necessity. Across counterfactual evaluations where cues are present but the associated tools are not required, agents exhibit substantial shortcut behavior, with spurious tool invocation rates increasing by up to 39 percent. However, shortcut formation is not universal: across the conditions we test, it arises only when the agent has already learned to use the target tool reliably, suggesting that task competence, rather than dataset imbalance alone, is a key factor in shortcut learning. A swapped-cue analysis further shows that semantic alignment between cues and tools substantially amplifies this effect. To mitigate these failures, we introduce a dense, decision-level reward in which an LLM judge evaluates the necessity of each tool call. This tool-necessity reward effectively suppresses cue-driven tool use while preserving task performance, providing a practical approach to improving the robustness of LLM agent tool-use policies.

</details>

---

### [[20_Research/Papers/大模型/Towards_Scalable_RLVR_Multimodal_Instruction_Following_Data_Synthesis_and_Distillation|Towards Scalable RLVR: Multimodal Instruction Following Data Synthesis and Distillation]]

![[assets/2609.16059_figure.png|800]]

- **arXiv**: [2609.16059](https://arxiv.org/abs/2609.16059)
- **PDF**: https://arxiv.org/pdf/2609.16059
- **详细分析**: [[20_Research/Papers/大模型/Towards_Scalable_RLVR_Multimodal_Instruction_Following_Data_Synthesis_and_Distillation|Towards Scalable RLVR: Multimodal Instruction Following Data Synthesis and Distillation]]
- **作者**: Yirong Zeng, Zhang Sai, Yuxian Wang, Yutai Hou, Yufei Liu, Xiao Ding, Bibo Cai
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.65，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Towards Scalable RLVR: Multimodal Instruction Following Data Synthesis and Distillation》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IF-RL, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal instruction following (MMIF) is crucial for building generalist agents. However, current training paradigms rely heavily on Supervised Fine-Tuning (SFT), which often leads to surface-level pattern matching and degrades general capabilities. While Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising alternative, its scalability in MMIF is severely bottlenecked by the scarcity of high-quality, RL-ready multimodal data. To bridge this gap, we present MIFS (\textbf{M}ultimodal \textbf{I}nstruction \textbf{F}ollowing \textbf{S}ynthesis), a systematic pipeline designed to generate RL-ready multimodal data. Specifically, MIFS introduces a generative constraint protocol to synthesize diverse raw samples, followed by a learnability-aware distillation mechanism that filters data based on RL training dynamics to ensure stable policy optimization. Furthermore, a code-based verifier provides high-precision reward signals for policy learning. The resulting dataset comprises 90k samples across 8 constraint categories and 14 task domains. Empirical evaluations demonstrate that MIFS-trained MLLMs achieve an average improvement of 8.13\% on four MMIF benchmarks and a 3$\times$ faster training convergence compared to using raw data. Crucially, our approach mitigates the generalization trade-offs typical of SFT, preserving core visual capabilities while significantly boosting instruction-following precision.

</details>

---

### [[20_Research/Papers/大模型/NepKANUN_A_RAG-Based_Nepali_Legal_Assistant|NepKANUN: A RAG-Based Nepali Legal Assistant]]

![[assets/2609.15999_figure.png|800]]

- **arXiv**: [2609.15999](https://arxiv.org/abs/2609.15999)
- **PDF**: https://arxiv.org/pdf/2609.15999
- **详细分析**: [[20_Research/Papers/大模型/NepKANUN_A_RAG-Based_Nepali_Legal_Assistant|NepKANUN: A RAG-Based Nepali Legal Assistant]]
- **作者**: Bhabuk Thapa, Prasiddha Koirala, Ranjit Raut, Sunil Regmi, Bal Krishna Bal
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《NepKANUN: A RAG-Based Nepali Legal Assistant》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accessing legal information in Nepal is difficult due to complex terminology, limited resources, and misinformation. We introduce an AI-powered legal assistant that is tailored for Nepali legal texts and is built on a fine-tuned large language model. The technology provides precise, streamlined answers to natural language legal inquiries when integrated into a Retrieval-Augmented Generation (RAG) framework. It was trained using a custom dataset of high-quality question-answer pairs, and according to BERTScore, it obtained strong F1 scores of 0.82 (simple), 0.77 (moderate), and 0.71 (complex). Its usability is further confirmed by expert reviews. Our method shows how merging generation and retrieval can effectively democratize access to legal knowledge in Nepal by focusing on customized legal data and incorporating RAG.

</details>

---
