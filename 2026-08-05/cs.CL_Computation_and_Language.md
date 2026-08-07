# cs.CL | Computation and Language | 2026-08-05

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/ParVL_Parallel_Scaling_and_Expandable_Compute_Allocation_for_Multimodal_LLMs|ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs]]

![[assets/2608.04010_figure.png|800]]

- **arXiv**: [2608.04010](https://arxiv.org/abs/2608.04010)
- **PDF**: https://arxiv.org/pdf/2608.04010
- **详细分析**: [[20_Research/Papers/大模型/ParVL_Parallel_Scaling_and_Expandable_Compute_Allocation_for_Multimodal_LLMs|ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs]]
- **作者**: Yang Yang, Qinyu Zhao, Mouxiang Chen, Xiaohui Li, Lixin Gu, Wenhai Wang, Hongjie Zhang, Wenwei Zhang
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing scaling strategies for Multimodal Large Language Models (MLLMs) typically expand either model parameters or sequential inference computation, incurring substantial memory or latency overhead. More importantly, most existing methods fail to alter the rigid, fixed computation allocation between the Vision Transformer and the Large Language Model components, limiting task-specific optimization. To address this, we introduce the Parallel Vision-Language (ParVL) scaling framework for MLLMs, which scales parallel computation by reusing the existing ViT and LLM backbone parameters across multiple vision and language branches. This framework raises a central question: given a fixed backbone parameter budget, how should additional shared-backbone computation be allocated between the vision and language modalities? We instantiate each parallel computational stream with branch-specific prefix parameters over a shared backbone, and train the entire model end-to-end via full-parameter supervised fine-tuning on roughly 13B tokens. We systematically study the computation-allocation trade-off between the ViT encoder and LLM decoder. ParVL improves overall multimodal performance over same-recipe single-branch baselines, and the best evaluated vision--language allocation varies across tasks. Code is available at https://github.com/YangYangGirl/ParVL.

</details>

---

### [[20_Research/Papers/强化学习/Hi-TTRL_Regulating_Consensus_with_Hints_for_Test-Time_Reinforcement_Learning|Hi-TTRL: Regulating Consensus with Hints for Test-Time Reinforcement Learning]]

![[assets/2608.03545_figure.png|800]]

- **arXiv**: [2608.03545](https://arxiv.org/abs/2608.03545)
- **PDF**: https://arxiv.org/pdf/2608.03545
- **详细分析**: [[20_Research/Papers/强化学习/Hi-TTRL_Regulating_Consensus_with_Hints_for_Test-Time_Reinforcement_Learning|Hi-TTRL: Regulating Consensus with Hints for Test-Time Reinforcement Learning]]
- **作者**: Kunbin Xu, Xingzuo Li, Xuefeng Bai, Kehai Chen
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Hi-TTRL: Regulating Consensus with Hints for Test-Time Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Hi-TTRL, TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time reinforcement learning (TTRL) improves the reasoning capabilities of large language models without labeled data by updating the policy with pseudo-labels constructed through majority voting. While effective, the reward signal assigned from majority voting is highly sensitive to consensus strength, defined as the frequency of the most common answer within a rollout group. In TTRL, consensus strength plays a dual role: it reflects both the reliability of the pseudo-label and the distribution of advantages. Low consensus can amplify updates from unreliable pseudo-labels through disproportionately large advantages, whereas high consensus reduces reward contrast and ultimately yields vanishing gradients. In this paper, we introduce Hi-TTRL, a test-time reinforcement learning framework that utilizes hints during sampling to regulate rollout consensus strength. Hi-TTRL first estimates consensus strength from a partial rollout group. When the consensus strength falls outside a target interval, it invokes a Markov chain Monte Carlo (MCMC) hint sampler. The sampler targets the power-transformed prefix distribution and uses finite-step approximate sampling to generate rollout prefixes as hints. By tuning the power exponent, Hi-TTRL generates hints with a sharpened or flattened power target, steering rollout consensus strength toward the target interval. Experiments on multiple datasets and backbones show that Hi-TTRL consistently improves over standard TTRL, with ablations and consensus-steering analyses validating the effectiveness of adaptive hint-guided consensus regulation.

</details>

---

### [[20_Research/Papers/大模型/Relational_Priors_as_Convergence_Pressure_in_LLM-Based_Multi-Agent_Systems|Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems]]

![[assets/2608.03239_first_page.png|800]]

- **arXiv**: [2608.03239](https://arxiv.org/abs/2608.03239)
- **PDF**: https://arxiv.org/pdf/2608.03239
- **详细分析**: [[20_Research/Papers/大模型/Relational_Priors_as_Convergence_Pressure_in_LLM-Based_Multi-Agent_Systems|Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems]]
- **作者**: Ming Shen, Chao Shang, Sadat Shahriar, Devang Kulshreshtha, Yi Zhang, Sandesh Swamy, Yanjun Qi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. Across a commons-governance simulation and multi-agent debate, relational priors primarily act as convergence pressure: increasing relational positivity tends to make agents coordinate or agree more readily. This pressure can help when utility rewards behavioral alignment, as in sustainable resource governance and subjective consensus. It does not, however, reliably improve accuracy. In objective QA debates, higher positivity can increase agreement even when correctness-conditioned agreement does not improve and may decline in some settings. Effects vary by model backbone, relation type, and topology; explicit neutrality is not equivalent to omitting relational framing. We argue that relational priors should not be a default add-on for LLM-MAS. Their safer use is diagnostic and task-specific: compare against a no-prior baseline, monitor correctness-conditioned metrics when truth matters, and omit the relational layer when validation does not justify it.

</details>

---

### [[20_Research/Papers/大模型/DP-MemView_A_Memory_Interface_for_Attribute-Level_Transcript_Privacy_in_Long-Term_LLM_Agents|DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents]]

![[assets/2608.03130_figure.png|800]]

- **arXiv**: [2608.03130](https://arxiv.org/abs/2608.03130)
- **PDF**: https://arxiv.org/pdf/2608.03130
- **详细分析**: [[20_Research/Papers/大模型/DP-MemView_A_Memory_Interface_for_Attribute-Level_Transcript_Privacy_in_Long-Term_LLM_Agents|DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents]]
- **作者**: Jong Wook Kim, Byoungjae Min, Kennedy Edemacu, Yoonhyuk Choi, Sae-Hong Cho, Beakcheol Jang
- **cs 子类**: cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory enables persistent personalization in LLM agents, but repeated memory-conditioned responses can cumulatively reveal protected attributes even when they are never stated explicitly. We formalize this threat as adaptive transcript privacy and introduce DP-MemView, a differentially private interface that privately selects public response-conditioning views and exposes those views---rather than raw memory---to the response LLM. Each private selection is charged to every protected attribute whose memory group intersects the read set. Per-attribute ledgers block any selection that would exceed its cap and return a fixed generic view instead. Under an explicit interface contract, we prove pure B_a-DP for the entire adaptive transcript. We also extend the result to stores that differ across multiple protected groups and bound how much observing the transcript can change an adversary's prior odds. We evaluate the online and preallocated modes with three response LLMs on a controlled adjacent-store benchmark and a public-corpus transfer track. Both modes keep transcript distinguishability near chance while preserving target-required personalization and overall response quality. Further diagnostics show that removing key safeguards causes mismatched output support, missing ledger charges, revealing side channels, or growing long-horizon leakage.

</details>

---

### [[20_Research/Papers/强化学习/Convex-Hull-Neighborhood_Smooth_Dual_Generalization_Controlling_Local_Correction_Propagation_in_Offline_RL|Convex-Hull-Neighborhood Smooth Dual Generalization: Controlling Local Correction Propagation in Offline RL]]

![[assets/2608.03108_figure.png|800]]

- **arXiv**: [2608.03108](https://arxiv.org/abs/2608.03108)
- **PDF**: https://arxiv.org/pdf/2608.03108
- **详细分析**: [[20_Research/Papers/强化学习/Convex-Hull-Neighborhood_Smooth_Dual_Generalization_Controlling_Local_Correction_Propagation_in_Offline_RL|Convex-Hull-Neighborhood Smooth Dual Generalization: Controlling Local Correction Propagation in Offline RL]]
- **作者**: Yi Yang, Zhennan Chen, Mingfeng Lv, Hanlei Li, Zhengsen Ruan, Lvqing Yang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Convex-Hull-Neighborhood Smooth Dual Generalization: Controlling Local Correction Propagation in Offline RL》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning (offline RL) can benefit from nearby out-of-distribution (OOD) actions, but estimation errors at these actions may be amplified by bootstrapping. Existing regularization and local-generalization methods control either the admissible OOD region or the influence of generalized targets, often through separate mechanisms. We propose Convex Hull Neighborhood Smooth Dual Generalization (CSDG), which expresses the Bellman backup as an in-sample value target plus a CHN-local correction. This formulation makes the generalized contribution explicit and separates it from the in-sample reference path. The correction is obtained by smoothing in-sample-oriented and OOD-oriented candidates sampled at different perturbation radii. A mixture coefficient lambda scales its contribution to each backup, while the recursive discount remains gamma. Under boundedness and fixed perturbation kernels, we derive an exact one-step correction identity, a time-varying iterate bound, and a fixed-point bound that depends only on the branch discrepancy at the fixed point. We further characterize the implicit policies induced by the idealized operators and give a conditional non-degradation criterion. The practical algorithm approximates these quantities using asymmetric bounded noise and expectile regression, without exact support classification or an additional pessimistic OOD penalty. Experiments on Gym-MuJoCo and AntMaze show strong aggregate performance and stable value estimation. Code is available at: https://github.com/YOUNG-fnxm/CSDG

</details>

---

### [[20_Research/Papers/具身智能/What_Language_Does_and_What_the_Evidence_Supports_A_Functional_Role_Taxonomy_and_Evidence_Audit_of_Language_Grounding_in_Embodied_Agents|What Language Does and What the Evidence Supports: A Functional Role Taxonomy and Evidence Audit of Language Grounding in Embodied Agents]]

![[assets/2608.03099_figure.png|800]]

- **arXiv**: [2608.03099](https://arxiv.org/abs/2608.03099)
- **PDF**: https://arxiv.org/pdf/2608.03099
- **详细分析**: [[20_Research/Papers/具身智能/What_Language_Does_and_What_the_Evidence_Supports_A_Functional_Role_Taxonomy_and_Evidence_Audit_of_Language_Grounding_in_Embodied_Agents|What Language Does and What the Evidence Supports: A Functional Role Taxonomy and Evidence Audit of Language Grounding in Embodied Agents]]
- **作者**: Yifan Guo, Chenghao Li, Zhu Wang, Wei Xu, Yu Li, Yulong Zhu, Zhuo Sun, Bin Guo, Zhiwen Yu
- **cs 子类**: cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.75（加权：具身智能 1.2，大模型 0.55）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《What Language Does and What the Evidence Supports: A Functional Role Taxonomy and Evidence Audit of Language Grounding in Embodied Agents》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Anticipation-VLA, ChatVLA, CoT-VLA, CogVLA, DexGraspVLA, DexVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models place language throughout embodied agents, but its presence does not show what it contributes or how well that contribution is grounded. This survey separates these two questions. We define five non-exclusive functional roles for language: Specification, Embodied Representation, Action Orchestration, Grounding Regulation, and Execution Coupling. For each role, we trace the path from linguistic content to its embodied consumer and identify the observations or interventions that can test the claimed responsibility. Applying this framework to the reviewed literature reveals a recurring gap between functional use and evidential support. Interpretable or revised linguistic intermediates may be incorrect, go unused, or fail to affect later behavior. Even when actions are directly conditioned on language, system-level success does not by itself isolate language's contribution. We therefore evaluate grounding claim by claim, asking whether the reported evidence supports the specific responsibility assigned to language. Using role claims rather than architectures as the unit of comparison allows us to compare modular and end-to-end embodied agents without extending conclusions beyond the reported evidence.

</details>

---

### [[20_Research/Papers/强化学习/PAMT_Process-Aligned_Reinforcement_Learning_for_Multi-Domain_Machine_Translation|PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation]]

![[assets/2608.03077_figure.png|800]]

- **arXiv**: [2608.03077](https://arxiv.org/abs/2608.03077)
- **PDF**: https://arxiv.org/pdf/2608.03077
- **详细分析**: [[20_Research/Papers/强化学习/PAMT_Process-Aligned_Reinforcement_Learning_for_Multi-Domain_Machine_Translation|PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation]]
- **作者**: Yongshi Ye, Biao Fu, Chongxuan Huang, Yidong Chen, Xiaodong Shi
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《PAMT: Process-Aligned Reinforcement Learning for Multi-Domain Machine Translation》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-domain machine translation (MDMT) requires more than fluent generation: it demands domain-sensitive translation decisions such as domain disambiguation, terminology control, and stylistic adaptation. Large reasoning models (LRMs) make such decisions explicit through intermediate translation steps, but our analysis across 15 domains and four translation directions shows that this explicit reasoning is double-edged: it improves long-form and high-difficulty translation, yet often drifts in terminology-intensive and stylistically constrained settings. We trace this failure to a credit-assignment bottleneck: existing methods optimize final outputs or coarse trajectories, but cannot identify which translation steps actually help the final translation. To address this, we propose PAMT, a process-aligned training framework that combines cold-start domain-aware Long-CoT supervision with reinforcement learning. PAMT uses sequence-level format and outcome rewards for the final translation, together with a step-level process reward that measures how much each explicit translation step increases the likelihood of the reference translation. Across two backbones, PAMT improves over base models, outperforms MT-specialized baselines on average, and remains competitive with strong LLMs/LRMs across in-domain, OOD, and multilingual settings.

</details>

---

### [[20_Research/Papers/大模型/LACE_Large_Language_Model_Aided_Multi-Agent_Framework_for_Agile_RISC-V_Instruction_Extension|LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension]]

![[assets/2608.02915_first_page.png|800]]

- **arXiv**: [2608.02915](https://arxiv.org/abs/2608.02915)
- **PDF**: https://arxiv.org/pdf/2608.02915
- **详细分析**: [[20_Research/Papers/大模型/LACE_Large_Language_Model_Aided_Multi-Agent_Framework_for_Agile_RISC-V_Instruction_Extension|LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension]]
- **作者**: Pingqing Zheng, Jiayin Qin, Fuqi Zhang, Zishen Wan, Shang Wu, Yu Cao, Caiwen Ding, Yang Katie Zhao
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Domain-specific Instruction Set Architecture eXtensions (ISAX) are widely adopted in the RISC-V ecosystem to accelerate emerging workloads, but implementing and validating ISAXes across different cores remains slow and fragmented. Existing frameworks still require per-core interface adaptation, and differential testing often breaks once either the microarchitecture or the ISAX changes. We present LACE, an LLM-aided multi-agent workflow that translates natural-language ISAX intents into a compact two-level IR (operation-level and HDL task-level), performs retrieval-guided localized RTL edits over large repositories, and closes the loop with a compiler-agnostic riscv-formal checking flow (assuming RVFI availability or instrumentation). Across four embedded RISC-V cores, LACE raises pass@1 generation accuracy from near-zero to 72.8\% within our evaluation setup, while improving code localization and reducing integration rework. The code of LACE is available at https://github.com/UMN-ZhaoLab/LACE.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_with_Evolving_Rubrics_as_Rewards_for_Audio_Reasoning|Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning]]

![[assets/2608.02831_figure.png|800]]

- **arXiv**: [2608.02831](https://arxiv.org/abs/2608.02831)
- **PDF**: https://arxiv.org/pdf/2608.02831
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_with_Evolving_Rubrics_as_Rewards_for_Audio_Reasoning|Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning]]
- **作者**: Fangxu Yu, Tao Feng, Dehai Min, Zinan Lin, Weijia Xu, Michael Xu, Philip S. Yu, Ge Liu, Tianyi Zhou
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：R1-AQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audio reasoning is essential for machine understanding of the acoustic world. Reinforcement learning with verifiable rewards can elicit such reasoning, yet existing reward designs are complementary in their limitations: outcome-based rewards supervise only the final answer and let the model reach it without attending to the audio, whereas process-based rewards score the reasoning itself but rely on coarse, hand-crafted, and fixed criteria that neither adapt to each question nor stay grounded in the acoustic evidence. Moreover, questions differ in what they demand, with some hinging on perception and others on multi-step reasoning, and any static criterion weakens as the policy improves. Supervising the reasoning process with fine-grained, audio-grounded, and adaptive rewards is therefore crucial, yet challenging since such rewards are impractical to design by hand for every sample. To this end, we introduce AudioRubrics, a reinforcement learning framework that supervises audio reasoning with self-evolving, audio-grounded rubric rewards. AudioRubrics synthesizes per-sample rubrics from the raw waveform and, conditioned on the model's own rollouts, regenerates and reweights criteria per group, supplying a continuous learning signal that keeps targeting the current policy's weaknesses as static criteria saturate. Comprehensive evaluations across three audio reasoning benchmarks reveal that AudioRubrics substantially outperforms a wide range of open-source and training-based baselines. Furthermore, our analysis shows that the gains scale with the capability of the rubric generator and judge, and AudioRubrics converges to a stable reasoning length that avoids both degenerate collapse and unbounded growth. The improvement in audio perception further demonstrates the effectiveness of anchoring supervision in the acoustic evidence. Our project page is available at https://audiorubrics.github.io.

</details>

---

### [[20_Research/Papers/大模型/ARCHead_Activation-Metric_Residual_Correction_for_Large_Language_Model_Output_Heads|ARCHead: Activation-Metric Residual Correction for Large Language Model Output Heads]]

![[assets/2608.02703_figure.png|800]]

- **arXiv**: [2608.02703](https://arxiv.org/abs/2608.02703)
- **PDF**: https://arxiv.org/pdf/2608.02703
- **详细分析**: [[20_Research/Papers/大模型/ARCHead_Activation-Metric_Residual_Correction_for_Large_Language_Model_Output_Heads|ARCHead: Activation-Metric Residual Correction for Large Language Model Output Heads]]
- **作者**: Şuayp Talha Kocabay, Talha Rüzgar Akkuş, Kamer Ali Yuksel
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM

#### 研究背景与动机

《ARCHead: Activation-Metric Residual Correction for Large Language Model Output Heads》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Weight-only quantization substantially reduces the storage of large language model (LLM) transformer blocks, but practical backends often retain the final language-modeling head (LM-head) in BF16 or FP16. Quantizing this projection naively can strongly perturb the vocabulary-logit distribution. We present ARCHead, a packed LM-head compressor that combines a quantized low-rank core, group-wise INT4 residuals, and a low-rank correction fitted in an activation-derived metric. ARCHead stores no dense BF16 head and reduces persistent LM-head storage by 3.7-3.9x. On Qwen3-8B-Base, it uses 25.6% of BF16 head storage while attaining 1.007 relative perplexity; storage-matched naive INT4 yields 1.14-1.16. Replacing the BF16 head left by AWQ or bitsandbytes adds only 0.006-0.007 cross-entropy, with less than 2% throughput change in our measurements. ARCHead therefore complements block quantizers by compressing the large output projection they can leave untouched. Code is available at https://github.com/suayptalha/archead.

</details>

---
