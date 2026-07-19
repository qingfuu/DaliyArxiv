# cs.CL | Computation and Language | 2026-07-17

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/On-Policy_Delta_Distillation|On-Policy Delta Distillation]]

![[assets/2607.15161_figure.png|800]]

- **arXiv**: [2607.15161](https://arxiv.org/abs/2607.15161)
- **PDF**: https://arxiv.org/pdf/2607.15161
- **详细分析**: [[20_Research/Papers/强化学习/On-Policy_Delta_Distillation|On-Policy Delta Distillation]]
- **作者**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《On-Policy Delta Distillation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model. Although on-policy distillation has been studied and applied across various settings, its fundamental design remains underexplored. In this paper, we introduce a new distillation reward, termed the delta signal, instead of directly imitating the teacher's output distribution. The delta signal is defined as the difference between the teacher model and its base model prior to instruction tuning for reasoning capability. It therefore captures the changes induced by reasoning tuning and provides a more direct signal for transferring reasoning capabilities. Using extensive empirical evidence, we show that the delta signal substantially improves on-policy distillation and refer to the new distillation method as On-Policy Delta Distillation (OPD$^2$). Experiments across mathematics, science, and code-reasoning benchmarks demonstrate that OPD$^2$ consistently outperforms conventional on-policy distillation, enabling reasoning LLMs to achieve strong performance with only a short post-training period. Code will be available at https://github.com/naver-ai/opd2

</details>

---

### [[20_Research/Papers/强化学习/Leveraging_Instruction_Tuning_and_Merging_for_Reasoning_Model_Adaptation|Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation]]

![[assets/2607.14895_first_page.png|800]]

- **arXiv**: [2607.14895](https://arxiv.org/abs/2607.14895)
- **PDF**: https://arxiv.org/pdf/2607.14895
- **详细分析**: [[20_Research/Papers/强化学习/Leveraging_Instruction_Tuning_and_Merging_for_Reasoning_Model_Adaptation|Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation]]
- **作者**: Yu-Du Feng, Niels Mündler-Sasahara, Mark Vero, Martin Vechev
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.95，强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning language models (RLMs) have demonstrated impressive performance in domains such as mathematics and coding. These domains permit reliable verification of model outputs, which is important for enabling the reinforcement learning that drives RLM performance gains. However, training RLMs on domains that lack reliable verifiers remains challenging. Meanwhile, for both verifiable and unverifiable domains, large amounts of unused supervised fine-tuning data with human-written solutions exist. In this work, we show that these data can be used efficiently to further improve RLM performance. For this, we first use classic instruction tuning, supervised fine-tuning without reasoning traces, on the RLM. Next, we merge our instruction-tuned model with the original reasoning model, recovering its reasoning behavior on the target domain. Our extensive evaluation demonstrates that our technique improves RLM performance in both verifiable and hard-to-verify domains, including coding and text summarization, while preserving RLM capabilities across other domains. Importantly, our method is highly cost-effective, enabling such improvements for less than USD $3.

</details>

---

### [[20_Research/Papers/大模型/The_Energy_Society_A_Simulation_Environment_for_Studying_Agent_Cooperation_under_Survival_Pressure|The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure]]

![[assets/2607.14865_figure.png|800]]

- **arXiv**: [2607.14865](https://arxiv.org/abs/2607.14865)
- **PDF**: https://arxiv.org/pdf/2607.14865
- **详细分析**: [[20_Research/Papers/大模型/The_Energy_Society_A_Simulation_Environment_for_Studying_Agent_Cooperation_under_Survival_Pressure|The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure]]
- **作者**: Lucas Bergholdt Hansen, Federico Torrielli, Filippo Tonini, Lukas Galke Poech
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents are increasingly deployed in multi-agent environments whose incentives can shape their behavior. We introduce The Energy Society, a minimal survival economy for studying how competitive and cooperative incentives affect emergent behavior when inference cost is directly tied to survival: Agents spend energy based on model size when generating tokens, regain energy by completing jobs or receiving donations, and deactivate if their energy reaches zero. We compare competitive and cooperative objectives against a baseline setting and several control variants. Across experiments, larger models consistently consume the most energy and spend more energy than they gain, even in those settings where token cost is not size-dependent. Cooperative incentives substantially alter behavior: agents donate to reactivate others, sometimes at the cost of their own survival, and job allocation changes. Ablations reveal that allowing agents to recommend actions to each other supports coordination and ambitious job selection, while memory helps agents calibrate risk from past outcomes. Agents rarely choose direct sabotage, but show more subtle signs of self-serving behavior in the competitive setting. The Energy Society is a compact testbed for studying the interaction between token costs and group incentives under a survival pressure. Source code is available at https://github.com/LucasBergholdt/EnergySociety

</details>

---

### [[20_Research/Papers/强化学习/SEED_Self-Evolving_On-Policy_Distillation_for_Agentic_Reinforcement_Learning|SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning]]

![[assets/2607.14777_figure.png|800]]

- **arXiv**: [2607.14777](https://arxiv.org/abs/2607.14777)
- **PDF**: https://arxiv.org/pdf/2607.14777
- **详细分析**: [[20_Research/Papers/强化学习/SEED_Self-Evolving_On-Policy_Distillation_for_Agentic_Reinforcement_Learning|SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning]]
- **作者**: Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, Yuhao Shen, Lang Feng, Haoran Luo, Zheng Lian, Shuai Zhang, Zhengqi Wen, Jianhua Tao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly trained as interactive agents for long-horizon tasks involving multi-turn interaction, tool use, and environment feedback. Outcome-based reinforcement learning (RL) provides a practical optimization paradigm, but its sparse trajectory-level rewards offer limited guidance on intermediate decisions, leaving a supervision gap between episode-level outcomes and token-level policy learning. We propose SEED (SElf-Evolving On-Policy Distillation), a self-evolving framework that converts completed on-policy trajectories into training-time hindsight skills and distills their behavioral effect back into the policy model. SEED first fine-tunes the policy to analyze completed trajectories and generate natural-language skills that capture reusable workflows, decisive observations, or failure-avoidance rules. During RL, the current policy both collects trajectories and serves as the analyzer that extracts hindsight skills from them. Policy updates therefore improve subsequent decision making and skill analysis together, allowing hindsight supervision to evolve with the policy. SEED then re-scores the sampled actions under ordinary and skill-augmented contexts, converting the skill-induced probability shift into a dense token-level on-policy distillation signal. This signal is jointly optimized with outcome-based RL, keeping the auxiliary supervision aligned with the current trajectory distribution. Extensive experiments on text-based and vision-based agentic tasks show that SEED consistently improves performance and sample efficiency, exhibiting robust generalization to unseen scenarios. Our code is available at https://github.com/jinyangwu/SEED.

</details>

---

### [[20_Research/Papers/大模型/Investigating_first-language_bias_in_LLM-based_automated_essay_scoring_A_cross-prompt_evaluation_of_an_open-weight_AI-model_on_TOEFL_essays|Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays]]

![[assets/2607.14605_figure.png|800]]

- **arXiv**: [2607.14605](https://arxiv.org/abs/2607.14605)
- **PDF**: https://arxiv.org/pdf/2607.14605
- **详细分析**: [[20_Research/Papers/大模型/Investigating_first-language_bias_in_LLM-based_automated_essay_scoring_A_cross-prompt_evaluation_of_an_open-weight_AI-model_on_TOEFL_essays|Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays]]
- **作者**: John Maurice Gayed
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Investigating first-language bias in LLM-based automated essay scoring: A cross-prompt evaluation of an open-weight AI-model on TOEFL essays》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study examines the cross-prompt generalization and first-language (L1) scoring effects of a LoRA-adapted open-weight large language model (Gemma-3-27B-it) applied to automated essay scoring. Using the identical model and inference configuration reported in "AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models" (Gayed, 2026), which was fine-tuned on 480 argumentative essays from two prompts, we evaluate scoring accuracy on the full TOEFL11 corpus: 12,100 essays written by test-takers from 11 first-language backgrounds across eight prompts, none of which were seen during training. The model's raw scores (0.5-5.0) are mapped to the same three proficiency bands (low, medium, high) used by ETS, enabling direct comparison. The model achieved an overall band agreement of 77.79% and a quadratic weighted kappa of 0.702, with adjacent-band agreement of 99.98%. Accuracy was stable across all eight unseen prompts, with no advantage for prompts thematically related to the training data, indicating robust cross-prompt generalization. However, the model exhibited a systematic, L1-linked scoring offset. Within every proficiency band, essays from European-language backgrounds received consistently higher scores than essays from East-Asian-language backgrounds, a pattern not attributable to the composition of the fine-tuning data. This is the first large-scale L1 fairness analysis of a fine-tuned open-weight LLM for automated essay scoring.

</details>

---

### [[20_Research/Papers/大模型/SD-MAR_Multi-image_Analytical_Reasoning_via_Synthetic_Data_and_Reinforcement_Learning|SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning]]

![[assets/2607.14333_figure.png|800]]

- **arXiv**: [2607.14333](https://arxiv.org/abs/2607.14333)
- **PDF**: https://arxiv.org/pdf/2607.14333
- **详细分析**: [[20_Research/Papers/大模型/SD-MAR_Multi-image_Analytical_Reasoning_via_Synthetic_Data_and_Reinforcement_Learning|SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning]]
- **作者**: Shiyu Yuan, Sourav Sanjukta Bhabesh, Zhe Wang, Dmitriy Bespalov, Wesley Rose, Huzefa Rangwala
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.35，强化学习 1）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GQA, ImageNet, MMBench, SEED-Bench, V-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Language Models (VLMs) demonstrate strong perceptual abilities but remain limited in tasks requiring analytical reasoning across multiple visual states, such as multi-image comparison, change detection, and multi-step visual inference. These capabilities are critical for real-world multimodal applications where reasoning must be grounded in systematic differences between visual contexts. However, existing benchmarks rarely require both explicit visual comparison and analytical reasoning, leaving this capability underexplored. To address this gap, we introduce SD-MAR (Synthetic Data for Multi-image Analytical Reasoning), a framework for training and evaluating VLMs on multi-image analytical reasoning. SD-MAR constructs paired visual scenarios through controlled perturbations and generates reasoning tasks spanning semantic change attribution and quantitative comparison. We further train VLMs using GRPO-lite with Backward Discounted Allocation (BDA), a reinforcement learning approach that removes KL regularization to encourage stronger policy optimization while allocating greater credit to the later reasoning steps where analytical conclusions are formed. Experiments on Qwen2.5-VL-7B and InternVL3-8B show that GRPO-lite fine-tuning on SD-MAR improves in-domain accuracy by up to 36.95%, with Qwen2.5-VL-7B outperforming GPT-4.1 on the SD-MAR benchmark. Importantly, out-of-domain generalization is preserved or improved: performance remains within 1% on MME, MMMU-Pro, and MathVista, while improving by up to 4% on MMBench. LLM-as-judge evaluation further demonstrates consistent improvements in logical coherence and explanation quality across both models.

</details>

---

### [[20_Research/Papers/大模型/Multi-Head_Latent_Control_A_Unified_Interface_for_LLM_Agent_Decision_Making|Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making]]

![[assets/2607.14277_figure.png|800]]

- **arXiv**: [2607.14277](https://arxiv.org/abs/2607.14277)
- **PDF**: https://arxiv.org/pdf/2607.14277
- **详细分析**: [[20_Research/Papers/大模型/Multi-Head_Latent_Control_A_Unified_Interface_for_LLM_Agent_Decision_Making|Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making]]
- **作者**: Amirhosein Ghasemabadi, Ruichen Chen, Bahador Rashidi, Di Niu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external tools, or abstain under the given setup. Existing approaches address these decisions through prompt-level routing, external orchestration, or task-specific fine-tuning, which primarily rely on input-side signals, and are often costly and difficult to maintain as model backbones evolve. We ask whether such control decisions can be inferred directly from a model's latent generation process. We introduce Multi-Head Latent Control, a lightweight layer that reads hidden-state trajectories from a frozen LLM or VLM to produce deployment-time control signals. A Capability Head predicts whether the current model can solve the instance or should defer to a stronger collaborator, while a Resolution Head predicts appropriate resolution decision Clarification, Tool Use, Abstention, or Direct Answering. Both heads are trained only on latent traces from the same frozen LLM backbone, enabling post hoc adaptation without modifying the model. Across language and vision-language settings, Multi-Head Latent Control consistently improves the quality-cost tradeoff of multi-model systems, enabling early handoff from partial generations and more accurate intervention decisions. In routed execution (small + large model), it reduces large-model usage by up to 90.7 percent on AndroidWorld and 27-53 percent on average across benchmarks, while retaining most of large-model performance. Additionally, the learned control signals improve tool-use decision quality, yielding up to +158 percent relative score gain and 65.5 percent fewer missed-required tool calls.

</details>

---

### [[20_Research/Papers/大模型/MonteRET_AI_Agent_Enhancing_Multimodal_LLMs_with_Multi-granularity_Knowledge_Retrieval_for_Chest_CT_Report_Generation|MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation]]

![[assets/2607.14264_figure.png|800]]

- **arXiv**: [2607.14264](https://arxiv.org/abs/2607.14264)
- **PDF**: https://arxiv.org/pdf/2607.14264
- **详细分析**: [[20_Research/Papers/大模型/MonteRET_AI_Agent_Enhancing_Multimodal_LLMs_with_Multi-granularity_Knowledge_Retrieval_for_Chest_CT_Report_Generation|MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation]]
- **作者**: Yi Lin, Yihao Ding, Elana Benishay, Elefterios Trikantzopoulos, David Nauheim, Hanley Ong, Jiang Bian, Hua Xu, Yuzhe Yang, George Shih, Yifan Peng
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated chest CT report generation remains challenging because clinically faithful reporting requires both whole-volume understanding and accurate description of localized anatomical findings. Here we developed and retrospectively evaluated MonteRET, a region-aware retrieval-enhanced framework for generating chest CT findings sections. MonteRET integrates global CT features with region-level anatomical representations, retrieves clinically relevant knowledge using predicted medical conditions and region-level vision-language alignment, and refines initial reports through a knowledge-guided report rewriting agent. We trained our model on a public cohort with 24,128 CT scans from RadGenome-ChestCT. We evaluated MonteRET on the public RadGenome-ChestCT test set of 1,564 CT scans and an external cohort of 82 CT scans from NewYork-Presbyterian/Weill Cornell Medical Center. MonteRET improved report quality, semantic similarity, and clinical efficacy compared with a matched baseline and several state-of-the-art methods. Gains were most pronounced for recall, suggesting fewer omitted findings. Human expert evaluation by radiology residents also favored MonteRET.

</details>

---

### [[20_Research/Papers/大模型/Branching_Policy_Optimization_Sandbox-Native_Language_Agent_Reinforcement_Learning|Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning]]

![[assets/2607.14171_figure.png|800]]

- **arXiv**: [2607.14171](https://arxiv.org/abs/2607.14171)
- **PDF**: https://arxiv.org/pdf/2607.14171
- **详细分析**: [[20_Research/Papers/大模型/Branching_Policy_Optimization_Sandbox-Native_Language_Agent_Reinforcement_Learning|Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning]]
- **作者**: Bowei He, Yankai Chen, Xiaokun Zhang, Xue Liu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.87（加权：大模型 0.95，强化学习 1.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes. State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the initial state, and an advantage is computed by subtracting a group baseline. This design ignores a defining property of agent sandboxes. They are deterministic, snapshottable, and resumable from any intermediate state. We argue that this property enables a fundamentally different rollout topology: rather than N independent trees of depth T, one can construct a single tree of N leaves whose siblings share prefixes, and therefore share variance. We instantiate this idea as Branching Policy Optimization (BPO), a sandbox-native RL algorithm that (i) adaptively snapshots the sandbox at high-entropy decision points along a backbone trajectory, (ii) forks K alternative actions per branch point and rolls out each to termination, and (iii) computes per-step advantages from sibling returns rather than from independent prompts. We prove this estimator is unbiased and has strictly lower variance than the trajectory-level baseline, with the reduction equal to the prefix-explained portion of return variance. On WebShop, ALFWorld, and SWE-bench Verified with Qwen2.5-7B and Llama-3.1-8B backbones, BPO improves success by 3.6--6.1 absolute points over GRPO and RLOO at matched compute, halves gradient-norm variance, and matches the best baseline using 38% fewer policy updates.

</details>

---

### [[20_Research/Papers/大模型/Semantic_Register_Compression_in_Multi-Agent_LLM_Cascades|Semantic Register Compression in Multi-Agent LLM Cascades]]

![[assets/2607.14119_figure.png|800]]

- **arXiv**: [2607.14119](https://arxiv.org/abs/2607.14119)
- **PDF**: https://arxiv.org/pdf/2607.14119
- **详细分析**: [[20_Research/Papers/大模型/Semantic_Register_Compression_in_Multi-Agent_LLM_Cascades|Semantic Register Compression in Multi-Agent LLM Cascades]]
- **作者**: Manuele Tele Junior Fernandez
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Semantic Register Compression in Multi-Agent LLM Cascades》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems commonly decompose complex tasks into specialized roles. However, this modularity introduces a representational risk: when intermediate agents transform text across linguistic registers, they can systematically compress the semantic distinctions needed for accurate downstream decisions. We term this phenomenon semantic register compression and characterize it as an observable failure mode in multi-agent cascades. Using a three-agent pipeline (Collector-Evaluator-Decider), we quantify compression via inter-label separation in sentence-transformer embedding space. Across political fact-checking (LIAR), sentiment analysis (SST-5), and medical triage (Triagegeist), critical evaluation consistently reduces label separability by 41.7% at the Evaluator stage, while identity passthrough preserves it nearly fully. Five architectural variants causally isolate oriented semantic transformation as the primary driver. A credibility-seeking variant produces minimal geometric compression yet shifts outputs toward mostly-true, demonstrating that transformation valence controls the direction of distributional collapse independently of compression magnitude. Compression generalizes across the three domains with varying intensity: 41.7% in fact-checking, 27.2% in sentiment, and 20.0% in triage. Prompt-level regression explains 78% of the variance, with operational constraints associated with lower compression. These results demonstrate that semantic register compression is a measurable and generalizable phenomenon in multi-agent LLM systems, with implications for safety evaluation in high-stakes domains.

</details>

---

### [[20_Research/Papers/大模型/Latent_Communication_Between_Language_Model_Agents_Channels,_Alignment,_and_the_Limits_of_Text|Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text]]

![[assets/2607.14103_figure.png|800]]

- **arXiv**: [2607.14103](https://arxiv.org/abs/2607.14103)
- **PDF**: https://arxiv.org/pdf/2607.14103
- **详细分析**: [[20_Research/Papers/大模型/Latent_Communication_Between_Language_Model_Agents_Channels,_Alignment,_and_the_Limits_of_Text|Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text]]
- **作者**: Markus Wenzel
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 1.25（加权：大模型 1.05，世界模型 0.2）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text》归入 大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent systems (MAS) are utilized in many contexts and many professions. Those MAS rely on inter-agent communication, usually implemented by clear-text message passing. We hypothesize that Large Language Models may have a world model at their disposal that exceeds expressibility in text when complex concepts need to be communicated. Our aim is to approach a proof of this hypothesis with structured experiments. In this work, we show that LLM agents communicating via text lose information, which we quantify via Sparse Autoencoder (SAE) feature analysis. We construct three communication channels and measure concept-discriminating information in each. We first show that the SAE-sparse channel retains a 99.4% probe accuracy at 28-fold compression over the dense-latent channel vs 80.4% for the text channel. We then proceed to examine the same for cross-architecture communication by using sparse latent space alignment. We find for Procrustes alignment a 92% top-1 retrieval between Llama and Mistral. Using a text round-trip, we perform feature survival analysis to find that text serialization destroys 88% of SAE features, replacing them with a different feature set. We attribute the loss to identity replacement, not attenuation. By our analysis, we were able to attribute a 3-10pp performance penalty to the linear Procrustes alignment, improving with nonlinear alignment methods. In a task-level evaluation we find that the latent channel matches the text channel on cross-lingual concept tasks but never exceeds it. Text augmentation with latent features provides no benefit, leading us to negative conclusions for the initial hypothesis: lost features mostly or completely encode surface form, not task-relevant semantics. To pinpoint the practical advantage of latent communication over a text channel, deeper tasks eliciting complex concepts and an corresponding analysis framework are needed.

</details>

---
