# cs.CL | Computation and Language | 2026-10-14

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Spectral-Driven_Adaptive-Rank_Optimizer_for_Large_Language_Model_Reinforcement_Learning_with_Verifiable_Rewards|Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards]]

![[assets/2610.16533_figure.png|800]]

- **arXiv**: [2610.16533](https://arxiv.org/abs/2610.16533)
- **PDF**: https://arxiv.org/pdf/2610.16533
- **详细分析**: [[20_Research/Papers/大模型/Spectral-Driven_Adaptive-Rank_Optimizer_for_Large_Language_Model_Reinforcement_Learning_with_Verifiable_Rewards|Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards]]
- **作者**: Zhipeng Chen, Wayne Xin Zhao, Ji-Rong Wen
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.97（加权：大模型 0.85，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Spectral-Driven Adaptive-Rank Optimizer for Large Language Model Reinforcement Learning with Verifiable Rewards》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) is reshaping how large language models (LLMs) acquire reasoning capabilities, yet the optimizers used remain largely inherited from teacher-forcing training. This raises a fundamental question: does RLVR induce a distinct optimization geometry that calls for a different optimizer? We investigate this question through the spectral structure of LLM gradients and find that gradient energy progressively concentrates into a shrinking effective subspace, which is characteristic of RLVR, as it is absent under supervised fine-tuning (SFT) and is largely removed when the verifiable reward is replaced by a random one. Moreover, the rank required to capture a fixed fraction of gradient energy steadily decreases over training, revealing that the effective dimensionality of useful updates itself evolves with training. These findings motivate a new optimization principle: rather than prescribing the update rank externally, an optimizer should adapt its rank to the evolving spectral structure of the gradient. We introduce Ares (Adaptive Rank-Effective Spectral Optimization), which estimates the effective update rank from the gradient's spectral energy distribution, tracks its evolution, and confines the gradient signal driving each update to the resulting low-rank subspace. Across LLMs of different scales, Ares improves accuracy over widely used optimizers and generalizes across RLVR algorithms and tasks. Results suggest that effective optimization may require optimizers to be designed around the geometry and dynamics of the training process. We release the code and data at https://github.com/RUCAIBox/Ares.

</details>

---

### [[20_Research/Papers/具身智能/RSIPO_Recursive_Self-Improving_Policy_Optimization_for_Agentic_Reinforcement_Learning_via_Skill-Policy_Co-Evolution|RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution]]

![[assets/2610.15772_figure.png|800]]

- **arXiv**: [2610.15772](https://arxiv.org/abs/2610.15772)
- **PDF**: https://arxiv.org/pdf/2610.15772
- **详细分析**: [[20_Research/Papers/具身智能/RSIPO_Recursive_Self-Improving_Policy_Optimization_for_Agentic_Reinforcement_Learning_via_Skill-Policy_Co-Evolution|RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution]]
- **作者**: Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, Yefeng Zheng, Bo Zhang, Haoxuan Li, Pheng-Ann Heng
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，强化学习 1.6）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution》归入 强化学习、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent focus in agentic reinforcement learning (RL) seeks to improve credit assignment in long-horizon tasks. One promising direction combines reinforcement learning with verifiable rewards (RLVR) and on-policy self-distillation (OPSD), integrating trajectory-level advantages with dense token-level supervision. This line of work often conditions a teacher model on privileged context, such as agentic skills, to score tokens generated by the student policy. Despite their progress, they largely overlook the on-policy evolution of agentic skills and the reliability of teacher supervision. Towards this end, we introduce Recursive Self-Improving Policy Optimization (RSIPO), a self-evolving agentic RL framework that enables agentic skills and the policy model to co-evolve throughout the training process. Specifically, RSIPO enables the policy itself to extract skills from completed trajectories and explicitly optimizes its skill-generation capability through trajectory replay. It further employs empirical Bayes shrinkage to dynamically calibrate the student's trust in teacher scores, accounting for the fact that skill-enhanced teacher guidance can sometimes be less reliable. Experiments with Qwen-family models on embodied interaction and search-based agentic tasks demonstrate that RSIPO outperforms all the compared baseline approaches. With Qwen2.5-7B as the base model, RSIPO achieves an average success rate of 98.6\% on ALFWorld, yielding absolute improvements of 2.5\% and 17.4\% over the second-best baseline and standard GRPO, respectively.

</details>

---

### [[20_Research/Papers/具身智能/A_Persian_Vision-Language-Action_Dataset_and_Benchmark_for_Ambiguity-_and_Infeasibility-Aware_Instruction-to-Plan_Grounding|A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding]]

![[assets/2610.15666_figure.jpg|800]]

- **arXiv**: [2610.15666](https://arxiv.org/abs/2610.15666)
- **PDF**: https://arxiv.org/pdf/2610.15666
- **详细分析**: [[20_Research/Papers/具身智能/A_Persian_Vision-Language-Action_Dataset_and_Benchmark_for_Ambiguity-_and_Infeasibility-Aware_Instruction-to-Plan_Grounding|A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding]]
- **作者**: Abdollah Pourasghari, Saeedeh Sadat Sadidpour, Mohammad Roustaei
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.05（加权：具身智能 1.5，大模型 0.35，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding》归入 具身智能、大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Converting natural-language instructions into executable action plans conditioned on a scene image is a core capability for embodied human-robot interaction, but existing benchmarks target English, simulated or video-grounded environments, and largely assume instructions are clear and executable. We introduce the first Persian vision-language-action dataset for this task: 258 instances over 230 real household/office photographs, annotated with reference plans, deliberate ambiguity and infeasibility labels, disambiguating question-answer pairs, and an auto-generated chain-of-thought rationale for training. Using this resource, we ablate retrieval-augmentation, chain-of-thought prompting, and an agentic disambiguation step, evaluated with an LLM-as-judge protocol and a new metric, PGOS-FA, extending prior work (PG2S) with step-order sensitivity, an over-generation penalty, and Persian-adapted embeddings. Paired statistical testing across 36 comparisons shows retrieval-augmentation is a large, robustly significant effect, while finer-grained additions are directionally consistent but not statistically distinguishable from noise at this scale, and the LLM-judge metric has near-zero power where PGOS-FA succeeds. A blind human-correlation study on 79 real outputs shows PGOS-FA tracks human judgment at least as closely as the LLM-judge. Testing generalization beyond the ablation's single backbone, we find that most of the gap between an open-weight and a substantially stronger closed planner is attributable to open-weight model generation rather than to the closed model's capability specifically, and that our best configuration significantly outperforms an independently reproduced external baseline despite a weaker backbone. The dataset, PGOS-FA implementation, and evaluation code will be made available upon reasonable request.

</details>

---

### [[20_Research/Papers/大模型/AlphaPilot_Multi-Turn_Tool-Using_LLM_Agents_for_Adaptive_Alpha_Mining_with_Reinforcement_Learning|AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning]]

![[assets/2610.15488_first_page.png|800]]

- **arXiv**: [2610.15488](https://arxiv.org/abs/2610.15488)
- **PDF**: https://arxiv.org/pdf/2610.15488
- **详细分析**: [[20_Research/Papers/大模型/AlphaPilot_Multi-Turn_Tool-Using_LLM_Agents_for_Adaptive_Alpha_Mining_with_Reinforcement_Learning|AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning]]
- **作者**: Peiqi Jiang, Fan Zhang, Xin Xu, Tianhao Chen, Can Yang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.97（加权：大模型 1.05，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Formulaic alpha mining seeks interpretable expressions that rank assets by future returns. The task is challenging because it demands simultaneous processing of unstructured market descriptions, historical data, and quantitative evaluation of candidate factors, yet most existing methods exploit only a subset of these signals. We introduce AlphaPilot, a reinforcement-learning framework that trains multi-turn tool-using LLM agents for adaptive alpha mining. The agent conditions on market descriptions, proposes factor expressions, queries real-data evaluator feedback, and updates a retained factor pool across turns. This design jointly leverages market text, LLM financial knowledge, real data, and evaluation feedback. At inference time, AlphaPilot performs day-by-day search and pool updates to adapt to shifting market regimes. Across three independent runs in out-of-sample rolling backtests on CSI300 and CSI500, AlphaPilot achieves mean total returns of 42.93% and 54.19%, with mean Sharpe ratios of 2.46 and 2.86, respectively. It attains the highest mean total return, Sharpe, and RankIC among the evaluated methods on both universes.

</details>

---

### [[20_Research/Papers/大模型/Training-Free_BioNEL-RAG_Advancing_Biomedical_Entity_Linking_through_Retrieval-Augmented_Generation_and_Large_Language_Model|Training-Free BioNEL-RAG: Advancing Biomedical Entity Linking through Retrieval-Augmented Generation and Large Language Model]]

![[assets/2610.14789_figure.png|800]]

- **arXiv**: [2610.14789](https://arxiv.org/abs/2610.14789)
- **PDF**: https://arxiv.org/pdf/2610.14789
- **详细分析**: [[20_Research/Papers/大模型/Training-Free_BioNEL-RAG_Advancing_Biomedical_Entity_Linking_through_Retrieval-Augmented_Generation_and_Large_Language_Model|Training-Free BioNEL-RAG: Advancing Biomedical Entity Linking through Retrieval-Augmented Generation and Large Language Model]]
- **作者**: Ziyi Chen, Hui Liu, Ziyang Ling, Ronald X. Xu, Mingzhai Sun
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.75（加权：大模型 1.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Training-Free BioNEL-RAG: Advancing Biomedical Entity Linking through Retrieval-Augmented Generation and Large Language Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IFEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biomedical Named Entity Linking (BioNEL) is the task of mapping mentions extracted from biomedical texts to canonical entities or concepts in the standardized knowledge base. Although existing methods have achieved remarkable performance in mapping accuracy, most rely on training with domain-specific datasets, which fundamentally limits their cross-domain adaptability. To address this limitation, we propose BioNEL-RAG, a novel training-free framework that combines retrieval-augmented generation (RAG) with large language models (LLMs). Within this framework, the RAG module focuses on retrieving candidate entities, while the large language model module plays the role of selecting the most appropriate candidate for entity normalization, which is based on the analysis of the mention's context, with the aid of its remarkable text comprehension capabilities. Experimental results demonstrate that BioNEL-RAG achieves performance comparable to existing methods without requiring training on subdomain datasets, whereas these methods necessitate fine-tuning on specific subdomains such as genes, diseases, or chemical compounds.

</details>

---
