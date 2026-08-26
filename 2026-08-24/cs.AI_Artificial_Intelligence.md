# cs.AI | Artificial Intelligence | 2026-08-24

#arxiv #ComputerScience

**论文数**: 47

### [[20_Research/Papers/强化学习/Re$^3$Cap_Retrieval-Guided_Refinement_for_Image_Captioning_Enhancement_via_Reinforcement_Learning|Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning]]

![[assets/2608.21305_figure.png|800]]

- **arXiv**: [2608.21305](https://arxiv.org/abs/2608.21305)
- **PDF**: https://arxiv.org/pdf/2608.21305
- **详细分析**: [[20_Research/Papers/强化学习/Re$^3$Cap_Retrieval-Guided_Refinement_for_Image_Captioning_Enhancement_via_Reinforcement_Learning|Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning]]
- **作者**: Haonan Jia, Shichao Dong, Zenghui Sun, Jiawen Zheng, Ziqi Miao, Gege Shi, Qiuyu Zhao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has demonstrated significant gains in image captioning, yet it is still limited in encouraging Large Vision-Language Models (LVLMs) to explore novel reasoning strategies. This limitation leads to a performance gap between RL and Supervised Fine-Tuning (SFT). In this paper, we argue that multi-modal retrieval can serve as an effective reasoning signal for caption refinement. Based on this insight, we present the Retrieval-Guided Refinement for Image Captioning (Re$^3$Cap), a retrieval-guided reasoning strategy that enhances image captioning without requiring additional annotations. Instantiated by Caption Refinement Suggester (CRS) and Caption Quality Assessor (CQA), this strategy identifies hallucinations and omissions in image captions, leading to more accurate and detailed descriptions. Extensive experiments demonstrate the superiority of our method in image captioning, even compared with Supervised Fine-Tuning. Especially, Re$^3$Cap outperforms GRPO with an average improvement of 8.64% in relation reasoning on the COCO-LN500 benchmark.

</details>

---

### [[20_Research/Papers/强化学习/AUSO_Action-Level_Unified_Skill_Optimization_from_Internalization_to_Utilization|AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization]]

![[assets/2608.21292_figure.png|800]]

- **arXiv**: [2608.21292](https://arxiv.org/abs/2608.21292)
- **PDF**: https://arxiv.org/pdf/2608.21292
- **详细分析**: [[20_Research/Papers/强化学习/AUSO_Action-Level_Unified_Skill_Optimization_from_Internalization_to_Utilization|AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization]]
- **作者**: Huizu Lin, Chengkai Huang, Tianqi Gao, Tao Huang, Daijiao Liu, Tongxin Li, Xiaoyan Sun, Lina Yao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，强化学习 0.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Search-QA, SearchQA, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skills play different roles as an agent's policy evolves: they should first provide learnable knowledge, then support capability formation, and finally be invoked only when they improve individual decisions. Existing methods rarely model this lifecycle. They either keep skills outside the model, fully internalize them, or select among internalization and utilization objectives through noisy task-level success rates. Such designs fragment training and assign uniform importance to actions within the same trajectory, even though skill guidance may help some decisions while distracting others. To solve these problems, we introduce AUSO (Action-level Unified Skill Optimization), which unifies skill learning and skill use through a progressive, action-aware optimization process. At the beginning of training, AUSO jointly learns from teacher guidance and environmental outcomes, enabling the policy to acquire foundational skills without losing task-oriented feedback. It subsequently emphasizes outcome-based policy optimization to consolidate autonomous problem-solving ability. As the policy matures, AUSO evaluates each sampled action under both skill-conditioned and skill-free contexts. The resulting action-level information signal is coupled with the trajectory outcome advantage, allowing beneficial skill-sensitive actions to receive stronger updates and harmful ones to be suppressed. Therefore, skills gradually transition from an external source of supervision into decision knowledge whose utilization is adapted to its action-level benefit, while reinforcement learning remains the shared backbone across all stages. Experiments on ALFWorld, WebShop, and SearchQA show that AUSO consistently improves agent performance and out-of-distribution generalization over competitive baselines.

</details>

---

### [[20_Research/Papers/大模型/EnSI-RAG_Entity-Structure-Indexed_Retrieval-Augmented_Generation_for_Long-Document_Question_Answering|EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering]]

![[assets/2608.21252_figure.png|800]]

- **arXiv**: [2608.21252](https://arxiv.org/abs/2608.21252)
- **PDF**: https://arxiv.org/pdf/2608.21252
- **详细分析**: [[20_Research/Papers/大模型/EnSI-RAG_Entity-Structure-Indexed_Retrieval-Augmented_Generation_for_Long-Document_Question_Answering|EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering]]
- **作者**: Xuanyu Meng, Jiashuo Sun, Jash Rajesh Parekh, Jiawei Han
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM

#### 研究背景与动机

《EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Question answering (QA) over long, connected documents remains challenging because relevant evidence may span multiple entities and their relationships. Existing retrieval-augmented generation (RAG) methods typically index documents as raw chunks and retrieve them through embedding similarity. Their performance degrades when chunk boundaries separate entities from supporting evidence or when a question requires multi-hop reasoning across the corpus. We propose EnSI-RAG (Entity-Structure-Indexed Retrieval-Augmented Generation), a framework that constructs a query-independent, entity-centered index. Each record (e, t, k, v) represents an entity e, its type t, a semantic category k in {property, relation, aspect}, and a value v, while retaining links to the original source passages. At query time, these records serve as retrieval handles, and an LLM synthesizes the retrieved passages into the final answer. This design separates evidence localization from answer synthesis while preserving traceable source evidence. Across Loong and Oolong, EnSI-RAG achieves an average accuracy of 78.24. Relative to the published baseline scores used as references, this is 6.62 points higher, suggesting its effectiveness across these settings. The code is available at https://github.com/RamonMeng/EnSI-RAG.

</details>

---

### [[20_Research/Papers/大模型/Specification_Portability_Across_LLM_Development_Agents_Cross-Agent_Compatibility_in_Specification-Driven_Software_Migration|Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration]]

![[assets/2608.21208_first_page.png|800]]

- **arXiv**: [2608.21208](https://arxiv.org/abs/2608.21208)
- **PDF**: https://arxiv.org/pdf/2608.21208
- **详细分析**: [[20_Research/Papers/大模型/Specification_Portability_Across_LLM_Development_Agents_Cross-Agent_Compatibility_in_Specification-Driven_Software_Migration|Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration]]
- **作者**: Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna, Vasyl Lyashkevych
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates cross-agent specification portability using Oracle-to-PostgreSQL migration as a controlled software transformation task. The study combines two experimental stages. First, a specification-first migration pipeline was evaluated on 1,006 PL/SQL files, of which 623 were successfully regenerated and 380 generated scripts executed successfully in PostgreSQL 16. Second, cross-agent experiments were conducted on a dataset of 1,802 Oracle scripts with corresponding PostgreSQL implementations using Amazon Kiro, Google Gemini, and GitHub Copilot, with Claude Code and Cursor included in the initial single-agent evaluation. Native and foreign specifications were assessed using Token F1, exact match, SQL syntax validity, AST exact match, AST mean similarity, and immediate runnability. The results show that specification size alone does not predict implementation quality and that cross-agent transfer can produce substantial agent-dependent degradation. The strongest replicated case occurred when Gemini directly consumed a Kiro-origin specification, producing a Token F1 of 0.035, SQL syntax validity of 2.33%, and AST mean similarity of 0.015. Rewriting substantially improved Gemini in the tested configuration, compression did not provide a universal benefit, and retrieval-augmented ingestion was the only common strategy represented on the per-agent Pareto frontiers of both Gemini and Copilot. The findings suggest that specifications in heterogeneous SDD workflows should not automatically be treated as agent-neutral artifacts and motivate explicit consideration of specification portability, agent-specific interpretation, and retrieval-based access in multi-agent software engineering.

</details>

---

### [[20_Research/Papers/大模型/No_PUN_Intended_Plausible_Unknown_Names_for_Person-Centred_LLM_Evaluation|No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation]]

![[assets/2608.21206_figure.png|800]]

- **arXiv**: [2608.21206](https://arxiv.org/abs/2608.21206)
- **PDF**: https://arxiv.org/pdf/2608.21206
- **详细分析**: [[20_Research/Papers/大模型/No_PUN_Intended_Plausible_Unknown_Names_for_Person-Centred_LLM_Evaluation|No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation]]
- **作者**: Dimitri Staufer, David Hartmann, Ibrahim Baroud
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Person names are widely used as prompt variables in LLM evaluations of factuality, privacy leakage, bias and abstention, but when a name's evidential status is uncontrolled, measurements may conflate memorisation, retrieval, name priors and wrong-person attribution. We operationalise an unknown name as one with plausible First-Last form, no indexed full-name evidence, and no ambiguity signals under a documented validation run, and introduce PUN (Plausible Unknown Names), a protocol for constructing and validating such names, combining Wikidata-derived components, web-enabled LLM screening, and controlled search revalidation. We report acceptance rate, reproducibility, ablations, and a 204-participant human study, finding accepted names are more name-like than controls while participants recover person evidence in only 3% of cases. We release 300 names with comparison controls.

</details>

---

### [[20_Research/Papers/具身智能/SRL-MPC_Shape-Aware_Reinforcement_Learned_Model_Predictive_Control|SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control]]

![[assets/2608.21175_figure.png|800]]

- **arXiv**: [2608.21175](https://arxiv.org/abs/2608.21175)
- **PDF**: https://arxiv.org/pdf/2608.21175
- **详细分析**: [[20_Research/Papers/具身智能/SRL-MPC_Shape-Aware_Reinforcement_Learned_Model_Predictive_Control|SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control]]
- **作者**: Ruihua Han, Rui Gao, Zhe Liu, Xinyi Wang, Chang Chen, Shuai Wang, Qi Hao, Jia Pan, Hengshuang Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, SARL, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging. Traditional approaches often assume homogeneous robots, sparse workspaces, simplified geometry, offline computation, or handcrafted parameters to make the problem tractable, which limits their deployment in dense crowd scenarios. Toward this end, we propose Shape-Aware Reinforcement Learned Model Predictive Control (SRL-MPC), a method for safe, efficient, and adaptive navigation in crowds with heterogeneous shapes without geometry simplification. To encode shape-aware safety, we formulate high-order control barrier function (HOCBF) constraints from geometric separation features (GSFs) based on support function transformation. A reinforcement learning (RL) framework then learns a neural policy that reads GSFs and outputs real-time MPC parameter updates, enabling the MPC solver to adapt to neighboring crowd geometries. The key advantage of SRL-MPC is that it preserves the safety structure and generalizability of MPC while integrating the adaptability and intelligence of RL. Experiments in randomized crowd scenarios with arbitrary shaped robot fleets demonstrate the effectiveness, scalability, and robustness of SRL-MPC. The results show that SRL-MPC substantially outperforms representative baselines in safety and adaptability. Project website: https://hanruihua.github.io/srl_mpc_project/

</details>

---

### [[20_Research/Papers/大模型/Is_Visual_Prompting_All_You_Need_Studying_VLM_Spatial_Reasoning_under_Progressive_Visual_Scaffolds|Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds]]

![[assets/2608.21170_first_page.png|800]]

- **arXiv**: [2608.21170](https://arxiv.org/abs/2608.21170)
- **PDF**: https://arxiv.org/pdf/2608.21170
- **详细分析**: [[20_Research/Papers/大模型/Is_Visual_Prompting_All_You_Need_Studying_VLM_Spatial_Reasoning_under_Progressive_Visual_Scaffolds|Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds]]
- **作者**: Lars Benedikt Kaesberg, Tianyu Yang, Florian Valentin Wunderlich, Terry Ruas, Jan Philip Wahle, Daniel Kurzawe, Bela Gipp
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet recent work shows that their failures often reflect an interaction between visual grounding and downstream reasoning. What remains less clear is how the visual presentation of a task shapes model performance and failure modes when the underlying reasoning problem is unchanged. We study this question in SPaRC, a benchmark for grid-based visual spatial planning, by introducing lightweight input-side scaffolds that preserve the visual modality while making spatial structure more accessible. Across multiple VLMs, these scaffolds improve task accuracy over the original visual setting by up to 34.0 percentage points and further complement GRPO-based training, yielding up to 4.6 additional accuracy points compared with near-zero gains on the original visual input. Analyses on both end-to-end task solving and object detection show that these gains are closely tied to reductions in grounding-related errors, while rule reasoning remains comparatively challenging. We find that visual presentation is a central factor that determines whether VLM benchmarks measure grounded perception, downstream reasoning, or a mixture of both.

</details>

---

### [[20_Research/Papers/大模型/Graph_Engineering_in_the_Era_of_LLM_Agents_From_Individual_Intelligence_to_System_Intelligence|Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence]]

![[assets/2608.21156_figure.png|800]]

- **arXiv**: [2608.21156](https://arxiv.org/abs/2608.21156)
- **PDF**: https://arxiv.org/pdf/2608.21156
- **详细分析**: [[20_Research/Papers/大模型/Graph_Engineering_in_the_Era_of_LLM_Agents_From_Individual_Intelligence_to_System_Intelligence|Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence]]
- **作者**: Yuyuan Feng, Zhishang Xiang, Chaobin Yang, Qichao Ma, Zerui Chen, Yujing Zhang, Ke Huang, Chuanjie Wu, Zhaoxu Liu, Yili Wang, Xin He, Jiapu Wang...
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement. Yet as tasks grow more complex, individual intelligence faces a fundamental limit: many tasks require heterogeneous expertise, interdependent subtasks, parallel execution, independent verification, and persistent state, exceeding any single agent's organizational capacity. Augmenting one agent's capabilities or context cannot resolve this architectural mismatch; intelligence must instead be distributed across specialized agents and organized at the system level. We call this System Intelligence: an agent system's ability to organize and coordinate multiple intelligent components into a coherent, adaptive whole pursuing a shared objective. Achieving it requires more than adding agents; it demands explicit structures to organize work, coordinate heterogeneous agents, and maintain evolving execution states. We introduce Graph Engineering, an emerging paradigm for next-generation agent systems. Unlike prior paradigms that mainly optimize individual interactions or agent-level behavior, Graph Engineering constructs explicit, dynamic, evolving graph structures representing tasks, agents, and system states. These abstractions provide a unified foundation for organizing complex objectives, orchestrating heterogeneous agents, modeling system dynamics, and enabling scalable agent evolution. We systematically review the principles, methodologies, and applications of Graph Engineering for LLM agents. Related papers, open-source data, and projects are collected at https://github.com/DEEP-JLU/Awesome-Graph-Engineering.

</details>

---

### [[20_Research/Papers/多模态技术/A_Modular_Agent_for_Reliable_and_Auditable_Spatial_Relation_Verification_in_CT_Scans|A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans]]

![[assets/2608.21140_figure.png|800]]

- **arXiv**: [2608.21140](https://arxiv.org/abs/2608.21140)
- **PDF**: https://arxiv.org/pdf/2608.21140
- **详细分析**: [[20_Research/Papers/多模态技术/A_Modular_Agent_for_Reliable_and_Auditable_Spatial_Relation_Verification_in_CT_Scans|A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans]]
- **作者**: Simon Vincent Abel, Heiko Hillenhagen, Michael Götz, Timo Ropinski, Ayhan Can Erdur, Daniel Santak Wolf
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the relative positions of anatomical structures and findings, this spatial weakness poses risks to diagnostic accuracy. We present a modular medical imaging agent for binary spatial relation verification in axial CT slices. Instead of directly predicting spatial answers end-to-end, the system decomposes the task into explicit stages: language parsing, anatomical localization, and deterministic geometric verification. Natural-language queries are converted into structured relation tuples, queried organs are localized with a YOLO-based detector, and the final spatial decision is computed from object centers using deterministic geometric rules. We evaluate the approach on the held-out MIRP spatial QA benchmark and compare it against representative end-to-end VLM baselines. The best-performing hybrid configuration reaches 94.1% accuracy and 94.2% F1, outperforming direct Qwen2-VL prompting by 42.5 percentage points in accuracy, while preserving interpretable intermediate representations and auditable reasoning stages. The results suggest that explicit modular spatial verification can serve as a promising building block for future report-oriented medical imaging agents.

</details>

---

### [[20_Research/Papers/大模型/ClawSentry_A_Progressive_Multi-Tier_Security_Monitor_for_Safeguarding_Autonomous_LLM_Agents|ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents]]

![[assets/2608.21101_figure.png|800]]

- **arXiv**: [2608.21101](https://arxiv.org/abs/2608.21101)
- **PDF**: https://arxiv.org/pdf/2608.21101
- **详细分析**: [[20_Research/Papers/大模型/ClawSentry_A_Progressive_Multi-Tier_Security_Monitor_for_Safeguarding_Autonomous_LLM_Agents|ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents]]
- **作者**: Kai Wang, Zeming Wei, BiaoJie Zeng, Chang Jin, An Wang, Xiaokun Luan, Zhixiao Lin, Jingjing Qu, Xia Hu, Xingcheng Xu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reappear across surface forms, tools, or turns; existing safeguards are typically local to one lifecycle boundary or one call. Guided by this threat model, we present ClawSentry, an open-source, framework-agnostic security supervision gateway for agent runtimes. Before a skill package is ever executed, First-use Skill Package Review (FSPR) audits it under a deterministic evidence floor, escalating unresolved cases to bounded read-only agentic review (locus A). At runtime, a three-tier progressive decision engine--a deterministic L1 layer, a rule-anchored L2 semantic reviewer, and a read-only L3 evidence-seeking agent--spends contextual review only on the residual ambiguity, while a session-level anti-bypass mechanism recognizes tool-switching and rephrased retries (loci B--C); a post-action path feeds high-severity evidence non-retroactively into later review (locus D). An Agent Harness Protocol (AHP) abstraction applies one policy across Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying agent internals. On SkillInject with Codex/GPT-5.4, contextual ASR falls from 39.55% to 2.61% while contextual TSR moves only from 83.78% to 83.05%. Across five Work Agents on the full SkillsSafety benchmark, ClawSentry confines ASR to 9.09--15.03% from 33.5--49.7% unprotected, and aggregate TSR on clean skills remains 98.7%.

</details>

---

### [[20_Research/Papers/大模型/ReFrame_Evidence-Guided_Test-Time_Safety_Alignment_in_Multimodal_Large_Language_Models|ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models]]

![[assets/2608.21100_figure.png|800]]

- **arXiv**: [2608.21100](https://arxiv.org/abs/2608.21100)
- **PDF**: https://arxiv.org/pdf/2608.21100
- **详细分析**: [[20_Research/Papers/大模型/ReFrame_Evidence-Guided_Test-Time_Safety_Alignment_in_Multimodal_Large_Language_Models|ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models]]
- **作者**: Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai, Dawei Feng, Huaimin Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two key obstacles, utility dominance and reasoning inertia, which cause models to overlook latent risks or follow malicious reasoning trajectories. Guided by these insights, we propose ReFrame, a training-free multimodal input reframing framework where two agents share a lightweight locally deployed MLLM: the evidence-generation agent constructs complementary risk and utility evidence, and the rewrite-and-routing agent converts it into a safe proxy prompt and image-routing decision before calling the downstream MLLM, without modifying it or accessing its internal information. Experiments across multiple MLLMs and benchmarks show that ReFrame improves jailbreak defense, safety awareness, and oversensitivity reduction while preserving multimodal utility.

</details>

---

### [[20_Research/Papers/大模型/Trustworthy_RAG_An_Evaluation_Agent_for_Detecting_Misinformation_and_Knowledge_Poisoning_in_Generative_AI_Systems|Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems]]

![[assets/2608.21095_first_page.png|800]]

- **arXiv**: [2608.21095](https://arxiv.org/abs/2608.21095)
- **PDF**: https://arxiv.org/pdf/2608.21095
- **详细分析**: [[20_Research/Papers/大模型/Trustworthy_RAG_An_Evaluation_Agent_for_Detecting_Misinformation_and_Knowledge_Poisoning_in_Generative_AI_Systems|Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems]]
- **作者**: Balkrishna Giri, Md Toufique Hasan, Jussi Rasku, Muhammad Waseem, Pekka Abrahamsson
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.IR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance does not guarantee factual truth. Adversaries exploit this through knowledge poisoning, inserting malicious documents to cause targeted misinformation. We propose an Evaluation Agent, middleware that combines Natural Language Inference (NLI) factual verification, a five-signal poison detector with relevance-weighted aggregation, and a Trust Index T = 0.4 F + 0.35 C + 0.25 (1 - P ) with a non-linear dampener for high-contamination contexts. On TruthfulQA with Llama 3.3 70B, the agent reaches 91% accuracy and 100% precision, with 100% recall on instruction injection, while in-place edits, such as entity swaps, remain hard to detect. Across three LLMs the Trust Index stays discriminative, with a Receiver Operating Characteristic Area Under the Curve (ROC-AUC) of 0.73 to 0.81; generation style matters more than model size, and per-LLM threshold calibration restores baseline competitive accuracy, whereas a weaker FEVER result shows that cross-dataset generalization requires domain-specific calibration. In a software-engineering use case, a secure-coding assistant over guidance from the Open Worldwide Application Security Project (OWASP) Top 10 and the Common Weakness Enumeration (CWE), the agent reliably blocks instruction injection of unsafe advice (F1 92%), while contradiction and subtle semantic weakening remain hard. Throughout, the agent measures detection of poisoned context before generation, not whether the LLM adopts the injected misinformation. We release the proposed approach, attack generator, and experimental artifacts at the link: https://github.com/GPT-Laboratory/TrustworthyRAG.

</details>

---

### [[20_Research/Papers/大模型/PromptResponse_Optimizing_Prompts_for_LLM_Coding_Tasks|PromptResponse: Optimizing Prompts for LLM Coding Tasks]]

![[assets/2608.21074_figure.png|800]]

- **arXiv**: [2608.21074](https://arxiv.org/abs/2608.21074)
- **PDF**: https://arxiv.org/pdf/2608.21074
- **详细分析**: [[20_Research/Papers/大模型/PromptResponse_Optimizing_Prompts_for_LLM_Coding_Tasks|PromptResponse: Optimizing Prompts for LLM Coding Tasks]]
- **作者**: Erik Thureck, Robert Kühnen, Tim Jacobowitz
- **cs 子类**: cs.AI, cs.CL, cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《PromptResponse: Optimizing Prompts for LLM Coding Tasks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlpacaEval, E-Bench, HotpotQA, HumanEval, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used in research workflows and software development pipelines, yet their output remains sensitive to input prompt variations. This paper presents $\unicode{x00AB}$PromptResponse$\unicode{x00BB}$, a controlled study examining how formatting and LLM-based tuning of coding task prompts affect the resulting code's performance, efficiency, and stability. Using five semantically identical yet syntactically distinct variants of the HumanEval dataset$\unicode{x2014}$baseline, JSON, Markdown, YAML, and an LLM-tuned version$\unicode{x2014}$we had GPT-4o solve its coding problems over 8200$\unicode{x00A0}$executions. Our results show that consistent formatting$\unicode{x2014}$especially JSON$\unicode{x2014}$improves generation efficiency and syntactic stability, with minor gains in task performance. Conversely, the LLM-tuned prompts resulted in significantly degraded task performance without significant improvements in any other dimension. These findings suggest that low-effort reformatting alone can yield measurable improvements, while tuning must account for model alignment. We conclude our work with providing a set of practical recommendations informed by our results as well as releasing our dataset variants and evaluation pipeline for future work.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_Large_Language_Model_Performance_on_International_Maritime_Dangerous_Goods_Code_Compliance|Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance]]

![[assets/2608.21036_first_page.png|800]]

- **arXiv**: [2608.21036](https://arxiv.org/abs/2608.21036)
- **PDF**: https://arxiv.org/pdf/2608.21036
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_Large_Language_Model_Performance_on_International_Maritime_Dangerous_Goods_Code_Compliance|Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance]]
- **作者**: Alexander Thomas, Hubert P. H. Shum, Darren Nellis, Manli Zhu, Phatpicha Yochum, William Bartle, Daniel Wrightson
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DGEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The transport of dangerous goods by sea is a high-consequence activity governed by the International Maritime Dangerous Goods (IMDG) Code, a complex regulatory framework where errors in classification, packaging, stowage, or segregation can result in fire, explosion, toxic release, or loss of life or vessel. Correct compliance requires accurately interpreting hundreds of pages of interacting provisions, updated on a two-year amendment cycle. Practitioners increasingly use Large Language Models (LLMs) as decision-support tools, yet no systematic evaluation exists of whether they can reliably interpret IMDG requirements for safety-critical use. This paper introduces DGEval, the first benchmark for evaluating LLM knowledge of IMDG Amendment 42-24. Built from expert-written questions on the NCB Hazcheck e-learning platform and structured lookups from the Dangerous Goods List (DGL), it comprises 1,678 questions across multiple-choice, open-ended, DGL lookup, and regulatory identification tasks. We evaluate 13 models from six providers across multiple thinking configurations, including one maritime domain-specific fine-tuned model, and test the effect of web search. Although the best-performing model exceeds the human practitioner baseline on multiple-choice questions, all models are weakest in the operationally safety-critical areas of stowage, segregation, and regulatory recall. These results indicate that LLMs may support compliance tasks, particularly structured DGL lookups with web search, but unreliability in operational areas and regulatory-text recall means human oversight and authoritative source verification remain necessary before deployment in any safety-critical context. DGEval is designed as a safety assurance instrument to be applied continuously as models evolve, not as a settled characterisation of current capability.

</details>

---

### [[20_Research/Papers/大模型/Don't_Solve,_Just_Compare_Tiny_Advisors_for_Runtime_Intervention_in_LLM_Agents|Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents]]

![[assets/2608.21027_first_page.png|800]]

- **arXiv**: [2608.21027](https://arxiv.org/abs/2608.21027)
- **PDF**: https://arxiv.org/pdf/2608.21027
- **详细分析**: [[20_Research/Papers/大模型/Don't_Solve,_Just_Compare_Tiny_Advisors_for_Runtime_Intervention_in_LLM_Agents|Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents]]
- **作者**: Yanze Jiang, Mingxuan Li, Yuhao Wang, Shengfang Zhai, Jiaheng Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are emerging as an important paradigm for real-world tasks that require reasoning, tool use, and sequential decision-making. As these agents operate over longer horizons, runtime intervention offers a way to improve reliability without retraining the underlying actor. Failure detection alone is insufficient. Effective intervention must also provide a useful direction for recovery. Existing approaches often rely on an expert solver or a critic that generates task-specific corrections, incurring either the cost of another capable solver or the capacity demands of a task-capable critic. We introduce Comparison-Only Tiny Advisor (COTA), a comparison-only framework for constructive runtime intervention. In COTA, a tiny comparator judges whether sampled alternatives lead to better continuations than the actor's proposal, and repeated comparisons determine when intervention is warranted. We train the comparator using pairwise supervision constructed from same-prefix counterfactual branches. Preferred alternatives are returned as non-binding advice, leaving the original actor to replan. Across WebShop, ALFWorld, and tau^3-Retail with three actors, COTA improves all nine evaluation settings and outperforms the compared baselines. These results show that constructive runtime intervention can remain effective even when the auxiliary model has substantially weaker task-solving capability than the actor.

</details>

---

### [[20_Research/Papers/大模型/Free-Text_Evaluation_of_LLMs_for_5G_Domain_Knowledge_and_Fault_Analysis_using_LLM-as-Judge|Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge]]

![[assets/2608.21021_first_page.png|800]]

- **arXiv**: [2608.21021](https://arxiv.org/abs/2608.21021)
- **PDF**: https://arxiv.org/pdf/2608.21021
- **详细分析**: [[20_Research/Papers/大模型/Free-Text_Evaluation_of_LLMs_for_5G_Domain_Knowledge_and_Fault_Analysis_using_LLM-as-Judge|Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge]]
- **作者**: Rishiraj Sengupta, Sotiris Chatzimiltis, Mohammad Shojafar, Xiatian Zhu
- **cs 子类**: cs.AI, cs.CL, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ORAN-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world fault analysis in 5G and emerging 6G networks demands domain expertise to analyze free-text diagnostics, including root-cause explanations and recommended actions. LLMs have emerged as a promising approach to automating this, yet whether lightweight, edge-deployable models are capable of performing in-depth free-text diagnostics remains an open question. While existing benchmarks rely on restrictive MCQs with fixed answer keys, this paper evaluates 5G domain understanding and fault analysis in a free-text generation format. Transitioning to this paradigm requires evaluating lightweight, edge-deployable AI models on open-ended diagnostic reasoning, alongside a dependable framework to validate these text outputs at scale. To address this we evaluate three lightweight LLMs, Claude-Haiku-4.5, GPT-5.4-Mini, and Gemini-3.1-Flash-Lite, on free-text 5G domain knowledge and fault-analysis tasks across three benchmarks, TeleQNA ORAN FT, 5G-Faults FT, and TeleInter FT. Three independent frontier judges score outputs, and pairwise inter-judge agreement is measured as an empirical test of the LLM-as-Judge methodology. All three models reach at least 90% accuracy on fault diagnosis, while zero-shot recall of 3GPP and O-RAN specifications remains the critical gap, with all models scoring below 60%. Mean inter-judge agreement is at least 0.90 across all runs, indicating that multi-judge LLM scoring produces consistent, reproducible grades for open-ended telecom responses. Operationally, Gemini-3.1-Flash-Lite offers the best efficiency trade-off, combining competitive accuracy with the lowest inference cost and latency, making it the most suitable candidate for production telecom deployments.

</details>

---

### [[20_Research/Papers/具身智能/Belief_Without_Behavior_Measuring_the_Translation_of_Theory_of_Mind_into_Coordinated_Social_Action_in_Vision-Language_Models|Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models]]

![[assets/2608.20975_figure.png|800]]

- **arXiv**: [2608.20975](https://arxiv.org/abs/2608.20975)
- **PDF**: https://arxiv.org/pdf/2608.20975
- **详细分析**: [[20_Research/Papers/具身智能/Belief_Without_Behavior_Measuring_the_Translation_of_Theory_of_Mind_into_Coordinated_Social_Action_in_Vision-Language_Models|Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models]]
- **作者**: Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.4）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap between social inference and social action. We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact across cooperative and competitive scenarios requiring integration of verbal statements, spatial trajectories, gaze direction, and facial expression under systematically varied ToM constraints. Evaluating 13 models, including 11 VLMs, across 200 trials per model, we find that VLMs fail to produce behaviors consistent with the expected outcomes under ToM-order constraints, and that imposing explicit ToM-order constraints produces no reliable behavioral change aligned with the specified reasoning level. Signal-level analysis reveals two sequential bottlenecks: most models cannot produce directionally coherent nonverbal signals, and even when signals are present, VLM agents fail to interpret others behaviors and react to them. PCM-LLM, included as a structured architectural reference point with an explicit ToM module, succeeds across all conditions, suggesting that explicit belief-action coupling is a sufficient ingredient for this class of tasks.

</details>

---

### [[20_Research/Papers/强化学习/Neural-Primitive_An_Efficient_End-to-end_Local_Planner_with_Primitive-based_Imitation_Learning_for_Autonomous_Flight|Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight]]

![[assets/2608.20948_figure.png|800]]

- **arXiv**: [2608.20948](https://arxiv.org/abs/2608.20948)
- **PDF**: https://arxiv.org/pdf/2608.20948
- **详细分析**: [[20_Research/Papers/强化学习/Neural-Primitive_An_Efficient_End-to-end_Local_Planner_with_Primitive-based_Imitation_Learning_for_Autonomous_Flight|Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight]]
- **作者**: Zhitao Liu, Guangtong Xu, Zihan Wang, Jialiang Hou, Chao Xu, Fei Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous flight in unknown cluttered environments is hindered by the computation-quality-memory trilemma of onboard trajectory generation. In this paper, we propose an efficient end-to-end local planner via imitation learning. A lightweight offline-primitive-based dataset collection framework is designed to produce safe and high-quality trajectory primitives in non-convex environments. A compact neural network directly maps sensory inputs to polynomial coefficients that inherently encode higher-order dynamical information. The learned policy generates smooth, empirically collision-free and dynamically feasible trajectories in real time without back-end solving. It achieves ultra-fast computation (below 1ms on a standard desktop and average 3.68ms during onboard flight), while maintaining low onboard memory requirements (less than 1.5MiB). Extensive simulation benchmarks demonstrate superiority in both planning latency and target-reaching progress quality. Zero-shot deployment in real-world experiments further validates the robust sim-to-real transfer capability of the proposed method.

</details>

---

### [[20_Research/Papers/强化学习/Graph-Operator_World_Models_for_Morphology-Parameter_Generalization_in_Continuous_Control|Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control]]

![[assets/2608.20936_first_page.png|800]]

- **arXiv**: [2608.20936](https://arxiv.org/abs/2608.20936)
- **PDF**: https://arxiv.org/pdf/2608.20936
- **详细分析**: [[20_Research/Papers/强化学习/Graph-Operator_World_Models_for_Morphology-Parameter_Generalization_in_Continuous_Control|Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control]]
- **作者**: Xu Yang, Yiqin Yang, Qianchuan Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NerveNet, WestWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for continuous control are commonly trained for a fixed physical system and can degrade when known morphology parameters such as link lengths, masses, damping, and actuation change. Existing approaches often provide these parameters as conditioning information, but leave unspecified which part of the learned transition should remain reusable and which part should change with morphology. We propose Graph-Operator World Models (GraphOp-WM), a structured world model for generalization across unseen morphology parameters within related articulated robot families. GraphOp-WM represents bodies and their kinematic relations as an attributed graph and factorizes each transition into a morphology-independent local dynamics basis and a morphology-conditioned structured operator. The operator combines node-local modulation, kinematic-tree coupling, and a low-rank global correction, while architectural information separation, basis normalization, and paired-morphology supervision encourage static morphology dependence to be carried by the operator pathway. Graph-level readout and edge-wise action representations provide a compatible interface for reward, value, and TD-MPC-style planning. We further define controlled MuJoCo parameter splits covering interpolation, extrapolation, and held-out compositions of link geometry, mass, damping, and actuation parameters in Hopper, Walker2d, and HalfCheetah.

</details>

---

### [[20_Research/Papers/强化学习/Advantage-level_Aggregation_Reinforcement_Learning_for_X-point_Target_Magnetic_Configuration_Control_in_an_EXL-50U_Experiment-Calibrated_Sim|Advantage-level Aggregation Reinforcement Learning for X-point Target Magnetic Configuration Control in an EXL-50U Experiment-Calibrated Simulation Environment]]

![[assets/2608.20834_figure.png|800]]

- **arXiv**: [2608.20834](https://arxiv.org/abs/2608.20834)
- **PDF**: https://arxiv.org/pdf/2608.20834
- **详细分析**: [[20_Research/Papers/强化学习/Advantage-level_Aggregation_Reinforcement_Learning_for_X-point_Target_Magnetic_Configuration_Control_in_an_EXL-50U_Experiment-Calibrated_Sim|Advantage-level Aggregation Reinforcement Learning for X-point Target Magnetic Configuration Control in an EXL-50U Experiment-Calibrated Simulation Environment]]
- **作者**: Siqi Ding, Xuanhe Wang, Pei Guo, Guoyang Shi, Changquan Yu, Yiting Wang, Xianming Song, Xiang Gu, Zhengyuan Chen, Lei Xing, Yapeng Zhang, Jianguo Chen...
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Advantage-level Aggregation Reinforcement Learning for X-point Target Magnetic Configuration Control in an EXL-50U Experiment-Calibrated Simulation Environment》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Managing divertor heat loads is a central challenge for compact, high-power tokamaks. To increase local flux expansion and decouple the dissipation volume from the core, EHL-2 adopts the X-point target (XPT) divertor. This requires the secondary X-point to remain on the divertor leg; displacement degrades the topology and exhaust geometry. Current experiments, including EXL-50U discharges, rely on precomputed feedforward waveforms with PID loops on global quantities. Lacking dedicated closed-loop feedback for the secondary null, XPT operation is repeatable but not routine. We formulate XPT feedback as a multi-objective reinforcement learning (RL) control problem in a free-boundary environment calibrated to EXL-50U discharge #13906. To address strong coupling among plasma current, shape, and null constraints - where reward scalarisation collapses objective-specific temporal credit - we develop Advantage Aggregation (AdvA). AdvA preserves objective-wise temporal credit before worst-objective-aware nonlinear scalarisation and introduces a residual correction to policy updates. AdvA-PPO is evaluated against Reward-PPO and a feedforward-plus-PID baseline under nominal operation, measurement uncertainties, and unseen initial equilibria. On a 500 ms rollout, AdvA-PPO raises the mean worst-channel score from 0.23 to 0.81 over Reward-PPO, reducing X-point flux RMSE by ~20x. Under combined measurement uncertainties, it is the only learned controller completing the horizon while retaining a usable XPT shape. Multi-initialization fine-tuning enables a single AdvA-PPO policy to complete full-horizon operation across divertor and limiter initial equilibria. These results provide a simulation-based foundation for future real-time XPT validation on EXL-50U.

</details>

---

### [[20_Research/Papers/大模型/Profiling_What_Matters_Context-Aware_Item_Profiles_from_Large-Scale_Metadata_for_LLM_Recommenders|Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders]]

![[assets/2608.20801_figure.png|800]]

- **arXiv**: [2608.20801](https://arxiv.org/abs/2608.20801)
- **PDF**: https://arxiv.org/pdf/2608.20801
- **详细分析**: [[20_Research/Papers/大模型/Profiling_What_Matters_Context-Aware_Item_Profiles_from_Large-Scale_Metadata_for_LLM_Recommenders|Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders]]
- **作者**: Dojun Hwang, Seunghan Lee, Cheonyoung Park, Sara Yu, SeongKu Kang
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Models (LLMs) have significantly advanced reranking in recommendation, effectively leveraging item-side information remains challenging. Real-world items are described by vast, heterogeneous, and unstructured metadata, where decision-relevant signals are often implicit, noisy, or buried in long descriptions. Moreover, feature salience is highly context-dependent, varying not only across items but also across users. Existing methods often rely on item titles, fixed attributes, or static item summaries, which limit personalized and fine-grained item understanding. To bridge this gap, we propose CAIRO, a user context-aware item profiling framework for LLM-based reranking. CAIRO first structures raw metadata and reviews into objective features and subjective traits, and employs a lightweight profiler to select the most relevant information for each user-item pair with limited serving-time overhead. The resulting profiles are concise and context-specific, providing relevant item-side evidence for the LLM's ranking decision. Experiments show that CAIRO consistently improves LLM-based reranking, highlighting the importance of item profiling that effectively exploits vast item-side information.

</details>

---

### [[20_Research/Papers/其他/Automated_Trajectory_Evaluation_for_Mobile_Agents_via_Step-Level_Consequence_Reasoning_and_Aggregation|Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation]]

![[assets/2608.20797_figure.png|800]]

- **arXiv**: [2608.20797](https://arxiv.org/abs/2608.20797)
- **PDF**: https://arxiv.org/pdf/2608.20797
- **详细分析**: [[20_Research/Papers/其他/Automated_Trajectory_Evaluation_for_Mobile_Agents_via_Step-Level_Consequence_Reasoning_and_Aggregation|Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation]]
- **作者**: Pengshuai Yang, Zijing Gao, Xue Yu, Benhui Zhuang, Bo Yuan, Junlan Feng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AndroidWorld, CRATEBench, MobileSafetyBench, SPA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating language-guided mobile agents has recently shifted from rule-based to model-based approaches to achieve scalable and automated assessments. However, existing holistic evaluation paradigms process entire trajectories at once, leading to substantial context overload. Moreover, they primarily focus on task completion while overlooking operational safety. To address these limitations, we introduce CRATE, a novel two-stage VLM-as-judge framework for automated mobile agent evaluation that is compatible with both open- and closed-source models. Leveraging a step-level consequence reasoning mechanism, CRATE independently extracts task-relevant visual clues and infers action-conditioned state changes at each step. The resulting step-level textual evidence is then synthesized through trajectory-level aggregation to deliver an evidence-grounded evaluation of task completion. Building upon this evaluation scheme, we further extend CRATE to CRATE-S for operational safety assessment. Extensive experiments validate the effectiveness and robustness of both CRATE and CRATE-S. Powered by Qwen2.5-VL-72B-Instruct, CRATE achieves an F1-score of 0.833 on AndroidWorld (outperforming SPA-Bench by 20%), while CRATE-S reaches an F1-score of 0.697 on MobileRisk, demonstrating strong alignment with benchmark ground truths. Code is available at https://anonymous.4open.science/r/CRATE-D580.

</details>

---

### [[20_Research/Papers/具身智能/CertVLA_Certified_Defense_against_Physical_Visual_Attacks_for_Vision-Language-Action_Models|CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models]]

![[assets/2608.20791_figure.png|800]]

- **arXiv**: [2608.20791](https://arxiv.org/abs/2608.20791)
- **PDF**: https://arxiv.org/pdf/2608.20791
- **详细分析**: [[20_Research/Papers/具身智能/CertVLA_Certified_Defense_against_Physical_Visual_Attacks_for_Vision-Language-Action_Models|CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models]]
- **作者**: Hui Lu, Zhijie Peng, Yuqi Lin, Zaijia Yang, Jiaming He, Shuhan Ye, Yi Yu, Hanwei Zhu, Bingquan Shen, Alex Kot, Xudong Jiang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Security

#### 研究背景与动机

《CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CertVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free. Specifically, CertVLA normalizes action disagreement by the benign variation of each mask pair and accepts a single-mask anchor only when it remains consistent under every second mask. It then calibrates the resulting max-min-max episode score to provide finite-sample clean coverage. Conjoining query-level decisions extends the action certificate to the complete closed-loop rollout. Furthermore, we prove that against any adaptive attacker satisfying the bounded-support threat model, every rollout certified by CertVLA executes only action chunks consistent with attack-erased clean predictions. Under dual-mask rollout correctness, this consistency certificate further guarantees task success. The certificate is independent of patch content, generation method, and physical transformation. Experiments in simulation and the real world demonstrate the empirical and certified effectiveness of CertVLA against patch attacks, with additional simulation validation on texture attacks.

</details>

---

### [[20_Research/Papers/强化学习/CAS_Conformalized_Agentic_Search_via_Adaptive_Retrieval_and_Policy_Weighting|CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting]]

![[assets/2608.20771_figure.png|800]]

- **arXiv**: [2608.20771](https://arxiv.org/abs/2608.20771)
- **PDF**: https://arxiv.org/pdf/2608.20771
- **详细分析**: [[20_Research/Papers/强化学习/CAS_Conformalized_Agentic_Search_via_Adaptive_Retrieval_and_Policy_Weighting|CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting]]
- **作者**: Zixi Zhu, Jiayuan Su, Jian Zhang, Yu Lin, Hongwei Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.6（加权：大模型 0.2，强化学习 0.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Search Agents face a severe reliability crisis during reinforcement learning (RL) fine-tuning. Heuristic Top-K retrieval often causes critical evidence loss or noise inclusion, while over-confidence induced by progressive RL leads to hallucinated answers and redundant searches. To build highly reliable agents, we introduce Conformal Prediction (CP) and propose Conformalized Agentic Search (CAS). This framework establishes reliability guarantees on both the retrieval and training sides: on the retrieval side, an Adaptive Prediction Set (APS), a specific CP realization, translates statistical coverage into dynamic document truncation to construct prediction sets that are adaptive in size; on the training side, Adaptive Conformal Inference (ACI), a dynamic CP algorithm, dynamically constructs prediction sets with controllable coverage to quantify answer confidence, which is then used to penalize low-confidence trajectories within the Group Relative Policy Optimization (GRPO) objective, ensuring the model learns only from reliable ones. Experiments across single-hop and multi-hop QA datasets demonstrate that our framework significantly improves reasoning accuracy while drastically reducing redundant tool invocations, establishing a highly reliable and efficient agent paradigm. Our code is available at https://github.com/S1llyBird/CAS.

</details>

---

### [[20_Research/Papers/大模型/Vis-Poison_Poisoning_Visual_Knowledge_in_Multimodal_Retrieval-Augmented_Generation|Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation]]

![[assets/2608.20756_figure.png|800]]

- **arXiv**: [2608.20756](https://arxiv.org/abs/2608.20756)
- **PDF**: https://arxiv.org/pdf/2608.20756
- **详细分析**: [[20_Research/Papers/大模型/Vis-Poison_Poisoning_Visual_Knowledge_in_Multimodal_Retrieval-Augmented_Generation|Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation]]
- **作者**: Rujin Liang, Zhongpu Chen, Yuhao Lei, Xin Miao
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：WebQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16\% to 65.40\% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60\%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

</details>

---

### [[20_Research/Papers/具身智能/Is_Multimodal_Speculative_Decoding_Ready_for_Diffusion-Based_Parallel_Drafting_A_Survey_and_Empirical_Diagnosis|Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis]]

![[assets/2608.20743_figure.png|800]]

- **arXiv**: [2608.20743](https://arxiv.org/abs/2608.20743)
- **PDF**: https://arxiv.org/pdf/2608.20743
- **详细分析**: [[20_Research/Papers/具身智能/Is_Multimodal_Speculative_Decoding_Ready_for_Diffusion-Based_Parallel_Drafting_A_Survey_and_Empirical_Diagnosis|Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis]]
- **作者**: Yantao Li, Huanlin Gao, Fang Zhao, Chao Tan, Qiang Hui, Shuting Liu, Fuyuan Shi, Ting Lu, Shaoan Zhao, Xueqiang Guo, Xinpei Su, Jianbing Zhang...
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.4）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Speculative decoding accelerates autoregressive generation by allowing a lightweight drafter to propose future tokens while a target model verifies them in parallel. Its lossless guarantee has motivated a line of work that pushes the drafter itself toward parallel generation. The most recent paradigm is block-parallel generative drafting, including diffusion-based methods such as DFlash and DSpark, achieving up to 3.6x speedup on common daily chatting tasks. While this transition is well studied in text-only LLMs, its applicability to multimodal models remains an open question. Existing multimodal speculative decoding efforts focus on input compression, adapter alignment, candidate coverage, or modality-specific verification; however, block-parallel generative drafting remains largely unexplored. To bridge this gap, this paper combines a modality-centered survey with a cross-architecture empirical study to ask: Is multimodal speculative decoding ready for diffusion-based parallel drafting? In this survey, we systematically analyze a wide spectrum of multimodal models, spanning Vision-Language, Video-Language, Audio, and Vision-Language-Action (VLA) architectures, from the dual perspectives of drafting parallelism and cross-modal information interaction. We introduce a unified taxonomy that isolates drafter-side parallelism from orthogonal design choices such as tree construction and verification strategies. Furthermore, we provide a comprehensive empirical comparison of existing methods under varying degrees of parallelism across standardized multimodal benchmarks, including OCR, VQA, visual reasoning, and image captioning. Finally, we summarize the limitations of current approaches, discuss open challenges, and outline promising future directions for this rapidly evolving field.

</details>

---

### [[20_Research/Papers/具身智能/ForeTime-VLA_Causal_Future-Token_Distillation_from_a_World_Action_Model_for_Conveyor-Belt_Manipulation|ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation]]

![[assets/2608.20735_figure.png|800]]

- **arXiv**: [2608.20735](https://arxiv.org/abs/2608.20735)
- **PDF**: https://arxiv.org/pdf/2608.20735
- **详细分析**: [[20_Research/Papers/具身智能/ForeTime-VLA_Causal_Future-Token_Distillation_from_a_World_Action_Model_for_Conveyor-Belt_Manipulation|ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation]]
- **作者**: Siyuan Ma, Yutian Zhang, Boshi Zhang, Qinglian Wu, Jiaqi Zhai, Dong Wei, Xiaojin Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ForeTime-VLA, OpenVLA, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating moving objects requires a policy to anticipate contact events, yet vision-language-action (VLA) policies are commonly fine-tuned from the current observation alone. World action models (WAMs) learn predictive dynamics, but running a video-scale teacher or explicitly imagining future frames at deployment is costly. We introduce ForeTime-VLA, a dense pi0.5 policy that distills a future-aware, action-equivalent representation from a frozen Fast-WAM-derived teacher while remaining causal at inference. Offline, current and future video latents are compressed into a whitened 64-D target. Online, an eight-frame history encoder predicts this target together with manipulation phase and normalized time-to-transition. Four future tokens and one phase token condition the VLM prefix, while the predicted future and transition horizon condition the action expert. Training retains the original flow-matching action target and adds cosine, relational geometry, phase, time-to-transition, and action-equivalence objectives. On a deduplicated conveyor-belt dataset, we compare 40k-step checkpoints on 768 matched windows per split. Test MAE decreases from 0.134119 to 0.130593 (2.63%; paired-bootstrap 95% CI: 0.82-4.48% improvement), and test L2 decreases by 3.02%, at a 2.46-2.93% latency cost. In quantitative real-robot evaluation, ForeTime-VLA achieves 81.1% stationary and 58.9% slow-moving grasp success, exceeding the next-best reference by 12.2 and 22.2 percentage points, respectively. Across three belt speeds, it completes 44/90 grasps versus 23/90 for pi0.5, including 11/30 versus 2/30 at fast speed. The agreement between offline orientation gains and reduced real-robot contact-pose failures supports causal future-token distillation as an effective way to improve dynamic manipulation without deploying the world-model teacher.

</details>

---

### [[20_Research/Papers/大模型/Calibrating_Criterion_Revision_in_LLM_Agents_Failure_Modes_and_a_Trace-Anchored_Protocol|Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol]]

![[assets/2608.20729_first_page.png|800]]

- **arXiv**: [2608.20729](https://arxiv.org/abs/2608.20729)
- **PDF**: https://arxiv.org/pdf/2608.20729
- **详细分析**: [[20_Research/Papers/大模型/Calibrating_Criterion_Revision_in_LLM_Agents_Failure_Modes_and_a_Trace-Anchored_Protocol|Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol]]
- **作者**: Guodong Xu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EvoMemBench, ImplicitMemBench, Mem2ActBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-model agents can improve after failure or carry text across episodes without revising what counts as success. We study the narrower attribution problem of criterion revision: when criterion K0 accepts an outcome violating a broader commitment B, what observations justify saying that the system formed and persistently used K1? We require five non-compensatory conditions: criterion-failure detection, a model-emitted proposal, new-episode transfer, intervention sensitivity on the claimed carrier, and preservation. We evaluate CMB-0.1 on twelve cross-domain cases and four arms: stateless inference, append-only history, model-generated but harness-committed state, and evaluator-written oracle state. Seven mechanism fixtures yield 84 deterministic scorer trials; four local quantized artifacts yield 96 calls and 192 model-case-arm trials. No model trial satisfies all five conditions, but this zero does not establish general capability absence. Eleven calls remain invalid after one retry; several commitments disclose the target distinction; the harness performs commits; deletion reuses a stateless call; and conflict changes multiple factors. Qwen2.5-7B answers every transfer and preservation item without revision state, exposing zero-state reconstruction. These failures make CMB-0.1 an instrument-calibration result rather than a model ranking. We derive a prospective, trace-anchored CMB-0.4 protocol requiring concealed transfer, explicit WRITE/NO-WRITE/ESCALATE actions, a separately logged policy-selected commit, matched interventions, repeated hidden items, and a frozen executable oracle. It is a successor design, not a completed confirmatory result. The paper contributes a measurement chain, an empirical diagnosis of its first implementation, and a more discriminating protocol for future tests of criterion revision.

</details>

---

### [[20_Research/Papers/强化学习/CDRL_Certification-Driven_Reinforcement_Learning_for_Neutrino_Flavor_Model_Discovery|CDRL: Certification-Driven Reinforcement Learning for Neutrino Flavor Model Discovery]]

![[assets/2608.20686_figure.png|800]]

- **arXiv**: [2608.20686](https://arxiv.org/abs/2608.20686)
- **PDF**: https://arxiv.org/pdf/2608.20686
- **详细分析**: [[20_Research/Papers/强化学习/CDRL_Certification-Driven_Reinforcement_Learning_for_Neutrino_Flavor_Model_Discovery|CDRL: Certification-Driven Reinforcement Learning for Neutrino Flavor Model Discovery]]
- **作者**: Piyush Jha, Jake Rudolph, Victoria Knapp-Pérez, Max Fieg, Aishik Ghosh, Vijay Ganesh
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CDRL: Certification-Driven Reinforcement Learning for Neutrino Flavor Model Discovery》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many scientific discovery problems require searching combinatorial hypothesis spaces under complex domain constraints. Reinforcement learning (RL) offers a promising approach, but existing methods rely on scalar rewards that provide limited information about why candidate solutions fail, leading agents to repeatedly explore invalid regions. We introduce Certification-Driven Reinforcement Learning (CDRL), a framework that leverages structured feedback from symbolic reasoning tools. When a candidate violates domain constraints, these tools produce certificates identifying the actions responsible for failure. CDRL converts these certificates into reusable constraints that eliminate classes of invalid solutions and guide exploration toward valid regions. We evaluate CDRL on neutrino flavor model discovery in theoretical particle physics, where the hypothesis space exceeds $10^{26}$ possible models, and compare it with the state-of-the-art RL approach previously used for this task. Across three theory spaces, CDRL achieves up to 1.95$\times$ higher valid model rates and up to 6.33$\times$ higher neutrino model rates while evaluating up to 4$\times$ fewer candidates. We further extract 40 interpretable rules from search trajectories using a post-hoc decision-tree framework and show that reusing them as soft constraints yields gains of up to 2$\times$ in valid model rates and 3$\times$ in neutrino model discovery across all three theory spaces. These results suggest that CDRL uncovers reusable structure in combinatorial search spaces and provides a general framework for scientific model discovery.

</details>

---

### [[20_Research/Papers/强化学习/Why2Speak_Faithful_Reasoning_for_Abstaining_Action_Policies|Why2Speak: Faithful Reasoning for Abstaining Action Policies]]

![[assets/2608.20670_first_page.png|800]]

- **arXiv**: [2608.20670](https://arxiv.org/abs/2608.20670)
- **PDF**: https://arxiv.org/pdf/2608.20670
- **详细分析**: [[20_Research/Papers/强化学习/Why2Speak_Faithful_Reasoning_for_Abstaining_Action_Policies|Why2Speak: Faithful Reasoning for Abstaining Action Policies]]
- **作者**: Shreya Mendi, Brinnae Bent
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.55（加权：大模型 0.35，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Why2Speak: Faithful Reasoning for Abstaining Action Policies》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an assistant must decide whether to speak or remain silent. This setting exposes class imbalance, asymmetric action costs, and the possibility that exposing reasoning changes the policy being audited. Using Qwen3-8B, decoded with or without chain-of-thought reasoning, we compare direct decision policies, reasoning policies, supervised fine-tuning, and reinforcement learning. We find a capability-auditability tradeoff: the strongest direct policy achieves higher quality but exposes no reasoning to inspect, while the reasoning policy provides a trace at the cost of lower performance, particularly recall of true intervention opportunities. Supervised fine-tuning either suppresses reasoning or preserves it without improving decision quality, while reinforcement learning also fails to improve the reasoning policy. We identify one mechanism underlying this failure: group relative objectives provide no learning signal on confidently wrong prompts when sampled rollouts all select the same action. Controlled activation probes and behavioral ablations show that standard faithfulness methods can overstate evidence that exposed reasoning reflects the underlying decision process. Probability-based metrics saturate under confident decisions, probes are vulnerable to class imbalance and textual leakage, and reasoning ablations can confound reasoning content with changes in inference mode. Together, these results show that exposing reasoning can change an agent's action policy rather than simply make it observable. We provide controls for evaluating reasoning-based oversight of agents that can act or abstain.

</details>

---

### [[20_Research/Papers/大模型/Auditable_by_Construction_An_Ontology-Driven_Framework_for_Trustworthy_LLM_Analytics_in_Enterprise_Finance|Auditable by Construction: An Ontology-Driven Framework for Trustworthy LLM Analytics in Enterprise Finance]]

![[assets/2608.20661_first_page.png|800]]

- **arXiv**: [2608.20661](https://arxiv.org/abs/2608.20661)
- **PDF**: https://arxiv.org/pdf/2608.20661
- **详细分析**: [[20_Research/Papers/大模型/Auditable_by_Construction_An_Ontology-Driven_Framework_for_Trustworthy_LLM_Analytics_in_Enterprise_Finance|Auditable by Construction: An Ontology-Driven Framework for Trustworthy LLM Analytics in Enterprise Finance]]
- **作者**: Sergiy Lunyakin
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Auditable by Construction: An Ontology-Driven Framework for Trustworthy LLM Analytics in Enterprise Finance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FinanceBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise adoption of large language models in finance is constrained less by fluency than by trust: in Financial Planning and Analysis (FP&amp;A) and other regulated workflows, an answer is usable only if it is traceable to authoritative sources and auditable after the fact. This paper argues that retrieval-augmented generation for enterprise finance should be evaluated on auditability alongside accuracy, and presents the Knowledge-Driven Analytics Framework (KDAF), which builds ontology-driven knowledge systems through six iterative stages and retrieves evidence via Context-Aware Relevance Propagation (CARP), so that every retrieved fact carries its relationship type, confidence, and source lineage. An evaluation on FinanceBench (145 questions) compares KDAF against zero-context inference, BM25, concept-weighted lexical retrieval, and ungrounded graph traversal. First, retrieval is necessary: zero-context inference reaches 4.1% correctness against 10-12% for retrieval-augmented conditions. Second, on answer correctness the retrieval conditions are statistically indistinguishable (KDAF vs BM25: -0.007, 95% CI [-0.021, 0.000]), so accuracy alone does not justify structured retrieval here -- a negative result we report explicitly. Third, on auditability the ordering reverses: KDAF attains the highest citation traceability F1 (0.515), exceeding ungrounded traversal by +0.027 (CI [0.006, 0.050]) and BM25 by +0.052 (CI [0.024, 0.083]), intervals excluding zero. Graph-structured retrieval also admits no evidence from outside the question subject entity (0 of 426 items, against 16.8% and 20.2% for lexical baselines), and every selected item resolves to a complete provenance chain. We argue that auditability, not accuracy, is the axis on which ontology-grounded retrieval earns its cost.

</details>

---

### [[20_Research/Papers/强化学习/AgentMercury_Your_Agent_Can_Synthesize_Verifiable_Environments_for_Business_Scenarios_at_scale|AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale]]

![[assets/2608.20634_figure.png|800]]

- **arXiv**: [2608.20634](https://arxiv.org/abs/2608.20634)
- **PDF**: https://arxiv.org/pdf/2608.20634
- **详细分析**: [[20_Research/Papers/强化学习/AgentMercury_Your_Agent_Can_Synthesize_Verifiable_Environments_for_Business_Scenarios_at_scale|AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale]]
- **作者**: Minbyul Jeong, Chanwoong Yoon
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EnterpriseOps-Gym, GPQA, LiveCodeBench, Scenario-to-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized around predefined tasks and benchmarks. This task-centric paradigm makes it difficult to scale environments that reflect realistic and evolving workflows where diverse tasks can naturally emerge from the underlying world. We introduce AgentMercury, a scalable framework for synthesizing executable environments from high-level business scenarios. Rather than constructing an environment for a specific task, AgentMercury first instantiates a persistent world with entities, services, tools, state, and executable cross-service invariants, from which diverse tasks and interaction trajectories can subsequently emerge. We construct 4,783 executable environments spanning 14 industries and 50 countries, and use them as training substrates for reinforcement learning. Despite being generated without targeting the evaluation benchmarks, policies trained on these business-oriented environments improve substantially on both enterprise workflows and out-of-domain benchmarks spanning reasoning, coding, scientific computing, and tool use. In our experiments, Qwen3.5-4B improves from 12.3 to 15.7 on EnterpriseOps-GYM and from 45.9 to 56.0 on AIME26 after training on AgentMercury environments. We further show that the construction process itself can be learned: fine-tuning Qwen3.5-35B-A3B on construction traces increases executable-world authoring success from 3.3% to 83.3% on held-out business scenarios. These results show that scenario-grounded environments can provide useful and generalizable learning signals beyond benchmark-specific training, while their construction can itself become a learnable capability.

</details>

---

### [[20_Research/Papers/大模型/Weighted_Memory_Tree_Remembering_What_Matters_for_Long-Horizon_LLM_Agents|Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents]]

![[assets/2608.20631_figure.png|800]]

- **arXiv**: [2608.20631](https://arxiv.org/abs/2608.20631)
- **PDF**: https://arxiv.org/pdf/2608.20631
- **详细分析**: [[20_Research/Papers/大模型/Weighted_Memory_Tree_Remembering_What_Matters_for_Long-Horizon_LLM_Agents|Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents]]
- **作者**: Quang Dao, Purvi Kathalkar, Kenneth Eaton
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

</details>

---

### [[20_Research/Papers/大模型/When_Failures_Propagate_Causal_Failure_Attribution_in_Agentic_Retrieval-Augmented_Generation|When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation]]

![[assets/2608.20627_first_page.png|800]]

- **arXiv**: [2608.20627](https://arxiv.org/abs/2608.20627)
- **PDF**: https://arxiv.org/pdf/2608.20627
- **详细分析**: [[20_Research/Papers/大模型/When_Failures_Propagate_Causal_Failure_Attribution_in_Agentic_Retrieval-Augmented_Generation|When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation]]
- **作者**: Lauren Pothuru
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.AI

#### 研究背景与动机

《When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the known intervention. Its central question is whether a post-hoc trace still identifies the injected hop after the suffix changes. In the completed strict dense Claude Haiku 4.5 sweep on 80 three-hop MuSiQue questions, coverage-based diagnosis is 0.91 at hop 1 and 0.00 at hops 2 and 3 (n=43,36,21 failed trajectories). A smaller content-corruption study changes an answer-bearing or bridge fact in topically intact evidence. At depth 2, where 18 failed cases remain after filtering, coverage-based diagnosis is 0.00 and a frozen-hop counterfactual probe is 0.67 in an exploratory pooled comparison. Depth-3 content estimates are descriptive only because they contain three failed cases. These results make propagation depth an explicit evaluation axis for diagnosing agentic RAG failures while distinguishing broad evidence of post-hoc signal loss from small-sample method comparisons.

</details>

---

### [[20_Research/Papers/大模型/Beyond_End-to-End_Success_Diagnosing_Failures_in_Long-Horizon_Security_LLM_Agents|Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents]]

![[assets/2608.20563_figure.png|800]]

- **arXiv**: [2608.20563](https://arxiv.org/abs/2608.20563)
- **PDF**: https://arxiv.org/pdf/2608.20563
- **详细分析**: [[20_Research/Papers/大模型/Beyond_End-to-End_Success_Diagnosing_Failures_in_Long-Horizon_Security_LLM_Agents|Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents]]
- **作者**: Wei Shao, Chongzhou Fang, Zuxiong Tan, Zequan Liang, Setareh Rafatirad, Avesta Sasan, Houman Homayoun
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AppWorld, AutoPenBench, CAIBench, CVE-Bench, CyberGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon security LLM agents must carry information and decisions across many dependent interactions, where later actions often depend on services, state, or access discovered much earlier. This makes final task success difficult to interpret: an agent may fail before it ever reaches the point where the capability of interest can be exercised. We present a diagnostic methodology that instruments security tasks with checkpoints, separates failures before and after capability exposure, and uses controlled interventions to test suspected upstream bottlenecks. We evaluate the methodology across four task families involving delayed reuse of discovered information, reuse of observed state, recovery from failed strategies, and decision making after uncertain outcomes. On observed state reuse, checkpoint analysis shows that many Gemini 2.5 Flash failures occur before the model observes the state it is later expected to reuse. In a pre-specified 92-seed study, targeted protocol-disambiguation guidance increases state observation from 65.5\% under a matched non-guidance control message to 95.4\%. Repeating the same design with Gemini 3.7 Flash produces the opposite effect, while state observation no longer reliably predicts task completion. These results show that the dominant source of failure can shift across model generations, motivating evaluation that diagnoses where and why long-horizon security agents fail rather than relying only on aggregate task success.

</details>

---

### [[20_Research/Papers/大模型/FL-MAESTRO_Multi-Agent_LLM_Orchestration_for_Resource-Constrained_Federated_Learning|FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning]]

![[assets/2608.20518_figure.png|800]]

- **arXiv**: [2608.20518](https://arxiv.org/abs/2608.20518)
- **PDF**: https://arxiv.org/pdf/2608.20518
- **详细分析**: [[20_Research/Papers/大模型/FL-MAESTRO_Multi-Agent_LLM_Orchestration_for_Resource-Constrained_Federated_Learning|FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning]]
- **作者**: Jiajun Wu, Zirui Wang, Jiayu Zhou, Qiang Ye, Steve Drew
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In Federated Learning (FL), the communication topology is a runtime variable rather than a fixed design choice, since links and edge devices drop in and out during training. Each round, the server must commit three coupled decisions, namely the communication topology, per-client resource allocation, and the aggregation rule for combining local updates. Recent agentic systems have begun bringing large language models (LLM) into FL, but the existing line of work either operates at setup time or handles a single runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent orchestrator that makes the joint runtime FL decision directly through three specialist LLM agents, one per decision dimension. A coordinator combines their analyses into a single decision, and a non-LLM feasibility check confirms it before the round executes. Because the orchestrator consumes the server's predicted-failure list, it withholds clients whose updates would never be aggregated, which removes the dominant source of wasted round energy in classical FL on volatile edge networks. Because client state is read as natural-text profiles, the same orchestrator extends to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero. Code is available at https://github.com/denoslab/FL-MAESTRO.

</details>

---

### [[20_Research/Papers/大模型/Terminal_Agents_A_Survey_of_AI_Agents_in_Command-Line_Environments|Terminal Agents: A Survey of AI Agents in Command-Line Environments]]

![[assets/2608.20485_figure.png|800]]

- **arXiv**: [2608.20485](https://arxiv.org/abs/2608.20485)
- **PDF**: https://arxiv.org/pdf/2608.20485
- **详细分析**: [[20_Research/Papers/大模型/Terminal_Agents_A_Survey_of_AI_Agents_in_Command-Line_Environments|Terminal Agents: A Survey of AI Agents in Command-Line Environments]]
- **作者**: Yi Bin, Xiaoyang Yuan, Haoxi Zeng, Wencheng Ye, Wenqi Shao, Chen Qian, Wei Ye, Yujuan Ding, Zheng Wang, Pengpeng Zeng, Jingkuan Song, Heng Tao Shen
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Terminal Agents: A Survey of AI Agents in Command-Line Environments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CLI-Gym, LongCLI-Bench, OSWorld, SetupBench, Terminal-Bench, TerminalWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents increasingly act through terminals, yet existing surveys disperse terminal-mediated behavior across software engineering, tool use, and computer-use research. We regard terminal agents as systems whose dominant progress-bearing action--observation loop is mediated by terminal command execution, textual feedback, and stateful environment interaction. Using terminal-mediated execution as an organizing lens, this survey establishes workload-level boundaries and connects system architecture, competence acquisition, and evaluation through a seven-dimensional terminal competence profile. Our synthesis shows that realized behavior is jointly shaped by the model, interface, harness, runtime, and environment. Executable trajectories ground learning in action consequences, verification, and recovery, whereas prevailing evaluations emphasize final outcomes and expose process quality, recovery, and governance unevenly. Bounded fixed-condition diagnostics illustrate two implications: benchmark families expose different process signals, and matched system comparisons reveal benchmark-dependent performance and limits of component attribution. These findings motivate explicit reporting of system and runtime conditions, supported by replayable traces and process-level evidence. The framework provides a unified basis for studying terminal-mediated agency across software engineering and emerging application domains.

</details>

---

### [[20_Research/Papers/大模型/Peer-Voted_LLM-Agent_Stress_Tests_Find_Feed-Induced_Lexical_Convergence_but_No_Reliable_Matched-Exposure_Advantage_for_Distributed_Sources|Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No Reliable Matched-Exposure Advantage for Distributed Sources]]

![[assets/2608.20438_figure.png|800]]

- **arXiv**: [2608.20438](https://arxiv.org/abs/2608.20438)
- **PDF**: https://arxiv.org/pdf/2608.20438
- **详细分析**: [[20_Research/Papers/大模型/Peer-Voted_LLM-Agent_Stress_Tests_Find_Feed-Induced_Lexical_Convergence_but_No_Reliable_Matched-Exposure_Advantage_for_Distributed_Sources|Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No Reliable Matched-Exposure Advantage for Distributed Sources]]
- **作者**: Rana Muhammad Usman, Dominic Williamson
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No Reliable Matched-Exposure Advantage for Distributed Sources》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Population-level behavior in large-language-model (LLM) agents cannot be characterized by single-agent benchmarks. We introduce PV-SST, a peer-voted social-platform testbed, and report a separately frozen, preregistered matched-exposure experiment spanning four topics, four unused seeds, four open-weight model families, and three prespecified larger variants. The experiment comprises 448 trials and 112 complete model-by-topic-by-seed blocks. Relative to a topic-only control, a feed of previous-round peer posts ranked by peer-generated likes increases final-round lexical similarity in both the four-family core panel (paired mean difference +0.0082 TF-IDF cosine units, 95% block-bootstrap CI [0.0043, 0.0121], randomization p=0.000105, n=64 blocks) and the three-variant size extension (+0.0109 [0.0069, 0.0151], p=0.000001, n=48). This contrast bundles peer-post exposure with ranking and therefore does not identify a ranking-only effect. Opposite-side survival falls in the core panel (-3.9 percentage points [-6.8, -1.6], p=0.0068) but not conclusively in the larger variants (-1.0 pp [-3.1, 0.4], p=0.50). Holding adversarial impressions fixed, four distributed sources do not reliably move honest-agent stance more than one source. The preregistered distributed-minus-single contrast is positive but inconclusive in the core panel (+0.057 [-0.009, 0.125], p=0.112) and negative in the larger variants (-0.040 [-0.113, 0.035], p=0.332), failing the prespecified cross-model and cross-topic consistency criterion. Thus the robust result is lexical convergence under the tested peer-ranked feed, not general opinion capture or a general coordination advantage. The study evaluates synthetic LLM-agent populations; it does not estimate effects on people or production platforms.

</details>

---

### [[20_Research/Papers/大模型/An_LLM_agent_for_end-to-end_computational_materials_discovery|An LLM agent for end-to-end computational materials discovery]]

![[assets/2608.20434_first_page.png|800]]

- **arXiv**: [2608.20434](https://arxiv.org/abs/2608.20434)
- **PDF**: https://arxiv.org/pdf/2608.20434
- **详细分析**: [[20_Research/Papers/大模型/An_LLM_agent_for_end-to-end_computational_materials_discovery|An LLM agent for end-to-end computational materials discovery]]
- **作者**: Chen Yuntong, Huang Ju, Liu Yu, Zhao Dan, Sun Mingqi, Ju Chentian, Liu Yanbing, Huang Lijiang, Zhao Guobin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《An LLM agent for end-to-end computational materials discovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The coordination of multi-scale tasks is an effective strategy for computational materials discovery, yet the repeated application of diverse algorithms and tools renders it challenging. We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs). It processes a large body of MOF literature, links relevant publications to their crystal structures, and curates the results into a computation-ready database, which is then screened through a strategy of progressively increasing computational cost. The promising candidates identified for separation under wet flue gas conditions all originate from unrelated studies. By connecting the heterogeneous stages of computational materials discovery, the LLM-based agents of MAESTRO can operate across application domains and uncover high-performance materials that conventional screening approaches would be unlikely to consider.

</details>

---

### [[20_Research/Papers/大模型/ProofJudge_Tool-Grounded_LLM_Evaluation_of_Formal_Proof_Quality_in_Mathlib|ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib]]

![[assets/2608.20432_first_page.png|800]]

- **arXiv**: [2608.20432](https://arxiv.org/abs/2608.20432)
- **PDF**: https://arxiv.org/pdf/2608.20432
- **详细分析**: [[20_Research/Papers/大模型/ProofJudge_Tool-Grounded_LLM_Evaluation_of_Formal_Proof_Quality_in_Mathlib|ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib]]
- **作者**: Shane Caldwell
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Formal proofs in Lean 4 that pass the kernel's type checker can nonetheless vary widely in quality. We introduce ProofJudge, an agentic LLM-as-judge system that scores formal proof quality along five dimensions beyond correctness: library leverage, automation fit, structural clarity, statement quality, and Mathlib conventions. We evaluate ProofJudge on a novel dataset of 218 declarations drawn from distinct Mathlib PRs. The judge agent is grounded by tool access to the commit the PR is applied to, enabling it to query the library state when scoring. A judge is considered aligned with human preferences when it rates the version of the PR Mathlib accepted above the initial version that was sent back for revision. All six judge models evaluated recover the reviewers' preference well above chance, from 80.8% to 63.5%, and two open-weight judges reach roughly 70% at a tenth of the best judge's cost. We release the judge harness, evaluation dataset, and evaluation traces as open-source artifacts to support further research.

</details>

---

### [[20_Research/Papers/大模型/From_Thermal_Preference_Prediction_to_Adaptive_Thermal_Intervention_A_Reinforcement_Learning_Approach_Using_Physiological_and_Environmental_|From Thermal Preference Prediction to Adaptive Thermal Intervention: A Reinforcement Learning Approach Using Physiological and Environmental Sensing]]

![[assets/2608.20423_figure.png|800]]

- **arXiv**: [2608.20423](https://arxiv.org/abs/2608.20423)
- **PDF**: https://arxiv.org/pdf/2608.20423
- **详细分析**: [[20_Research/Papers/大模型/From_Thermal_Preference_Prediction_to_Adaptive_Thermal_Intervention_A_Reinforcement_Learning_Approach_Using_Physiological_and_Environmental_|From Thermal Preference Prediction to Adaptive Thermal Intervention: A Reinforcement Learning Approach Using Physiological and Environmental Sensing]]
- **作者**: Isibor Kennedy Ihianle, Emmanuel Manu, Ehsan Asnaashari, Mojgan Jadidi, Pedro Machado, Amrit Sagoo, Ahmad Lotfi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《From Thermal Preference Prediction to Adaptive Thermal Intervention: A Reinforcement Learning Approach Using Physiological and Environmental Sensing》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalised thermal comfort is essential for occupant wellbeing and for the development of more responsive building-control strategies, yet conventional Heating, Ventilation, and Air Conditioning (HVAC) systems rely on static setpoints and population-level comfort models that fail to capture individual physiological variability. This paper presents a two-stage personalised thermal comfort approach integrating multimodal physiological and environmental sensing with reinforcement learning-based decision-making.

</details>

---

### [[20_Research/Papers/强化学习/World_models_of_environment,_agent_and_joint_agent-environment_systems|World models of environment, agent and joint agent-environment systems]]

![[assets/2608.20401_figure.jpg|800]]

- **arXiv**: [2608.20401](https://arxiv.org/abs/2608.20401)
- **PDF**: https://arxiv.org/pdf/2608.20401
- **详细分析**: [[20_Research/Papers/强化学习/World_models_of_environment,_agent_and_joint_agent-environment_systems|World models of environment, agent and joint agent-environment systems]]
- **作者**: Manuel Baltieri, Filippo Torresan, Yivan Zhang, Alexander Boyd, Fernando E. Rosas
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 2.12（加权：大模型 0.4，强化学习 0.56，世界模型 1.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《World models of environment, agent and joint agent-environment systems》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are a central component of model-based reinforcement learning. They are usually discussed in terms of what variables they predict, such as observations, rewards, states, latent or information states. We argue that there is a prior distinction: which channel they model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently viewed as a channel with no inputs. Using computational mechanics, we define canonical predictive models for these three cases as $ε$-transducers or $ε$-machines. Canonical environment models recover standard predictive state representations, while the other two give analogous notions of canonical models for the agent and the joint system. We then build canonical support-restricted environment and agent models induced by closed-loop coupling, whose predictive equivalences range over continuations supported by the realised interaction. The key structural result is that canonical support-restricted environment states factor through the canonical joint causal states, and their transition structure is induced directly from the joint model; the agent-side construction is dual. Finally, we give a POMDP/controller example in which the unrestricted environment model has infinitely many states while the canonical support-restricted model induced by the coupling is finite. The framework clarifies what different world models are models of, and how coupling and support restriction can change their canonical predictive structure and complexity.

</details>

---

### [[20_Research/Papers/大模型/Representation_Affects_Retrieval_A_Case_Study_of_Skill_Discovery_and_Routing_in_a_Multimodal_Agent_Harness|Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness]]

![[assets/2608.20389_first_page.png|800]]

- **arXiv**: [2608.20389](https://arxiv.org/abs/2608.20389)
- **PDF**: https://arxiv.org/pdf/2608.20389
- **详细分析**: [[20_Research/Papers/大模型/Representation_Affects_Retrieval_A_Case_Study_of_Skill_Discovery_and_Routing_in_a_Multimodal_Agent_Harness|Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness]]
- **作者**: Kevin Dela Rosa
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.

</details>

---

### [[20_Research/Papers/大模型/EditPPT_Faithful_Long-Deck_Slide_Editing_via_Structured_Tool-Using_Multi-Agent_with_Dual-Modal_Validators|EditPPT: Faithful Long-Deck Slide Editing via Structured Tool-Using Multi-Agent with Dual-Modal Validators]]

![[assets/2608.20381_figure.png|800]]

- **arXiv**: [2608.20381](https://arxiv.org/abs/2608.20381)
- **PDF**: https://arxiv.org/pdf/2608.20381
- **详细分析**: [[20_Research/Papers/大模型/EditPPT_Faithful_Long-Deck_Slide_Editing_via_Structured_Tool-Using_Multi-Agent_with_Dual-Modal_Validators|EditPPT: Faithful Long-Deck Slide Editing via Structured Tool-Using Multi-Agent with Dual-Modal Validators]]
- **作者**: Jiheon Kim, Kyudan Jung, Jaegul Choo
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《EditPPT: Faithful Long-Deck Slide Editing via Structured Tool-Using Multi-Agent with Dual-Modal Validators》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DECKBench, DeckEdit-Bench, TSBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating slide editing requires simultaneously satisfying modification accuracy, preservation fidelity, and robustness to deck length. Existing LLM-based systems often fail on real-world presentation files because they rely on idealized intermediate representations or open-ended code generation, which are prone to cascading errors in long decks. We introduce EditPPT, a multi-agent framework that reformulates slide editing as a constrained tool-selection problem. By executing localized shape-level operations through the native PowerPoint COM interface, EditPPT narrows the LLM action space while preserving the application-resolved structure of user-authored decks. By separating validation across modalities, our dual-modal validation provides more robust assessment of both instruction fidelity and visual quality. We also present DeckEdit-Bench, a benchmark with 28 human-authored decks, 582 slides, and 183 editing prompts across short, medium, and long deck tiers. Experiments show that EditPPT achieves a 99.5% execution rate, 88.7% slide-targeting F1, 82.5% instruction following, and 91.5% object preservation overall, while maintaining strong performance on long decks. Our code and benchmark are available at https://anonymous.4open.science/r/EditPPT-0E27/

</details>

---

### [[20_Research/Papers/具身智能/A_Survey_on_Foundations_and_Frontiers_of_Multimodal_Agentic_Frameworks_Techniques_and_Applications|A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks: Techniques and Applications]]

![[assets/2608.20379_figure.png|800]]

- **arXiv**: [2608.20379](https://arxiv.org/abs/2608.20379)
- **PDF**: https://arxiv.org/pdf/2608.20379
- **详细分析**: [[20_Research/Papers/具身智能/A_Survey_on_Foundations_and_Frontiers_of_Multimodal_Agentic_Frameworks_Techniques_and_Applications|A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks: Techniques and Applications]]
- **作者**: Neel Mokaria, Rishie Raj, Dheeraj Baiju, Xiaoqian Shen, Shraman Pramanick, Kevin Qinghong Lin, Arda Senocak, Mike Zheng Shou, Philip Torr, Mohamed Elhoseiny, Yapeng Tian, Ruohan Gao...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.9（加权：大模型 0.7，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks: Techniques and Applications》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Advances in large language models (LLMs) have fueled a wave of research into agency: the ability to reason, plan, and act. This effort has produced agentic frameworks that orchestrate perception, memory, and decision-making around powerful LLM backbones. With the advent of large multimodal models (LMMs), these systems can process and integrate diverse modalities, including images, audio, and video, thereby improving their real-world applicability. Yet, while surveys of LLM-based agents exist, the role of multimodality in shaping agency has not been systematically examined in recent years. This survey fills the gap by analyzing the impact of multimodality across the core functional modules of the agentic framework: perception, reasoning, planning, memory, and action. Using this lens, we trace the evolution from text-centric agents to multimodal frameworks, examine how modalities are integrated through delegated, late-fusion, and early-fusion architectures, and assess the emergence of agentic behaviors enabled by grounded perception and multimodal reasoning. We organize existing work through a modality-centric taxonomy that links architectural design choices to agent capabilities. Moreover, we review multimodal agentic systems across various application domains, including Robotics, GUI &amp; Web Navigation, Multimedia Content Generation &amp; Editing, and Long-form Video Understanding &amp; Retrieval. Beyond capabilities, we analyze performance across these settings and discuss efficiency-scalability trade-offs, including training and inference costs, latency, and deployment constraints. By focusing on the impact of multimodality in agentic design, we aim to identify key gaps and chart a roadmap toward robust and general-purpose intelligent systems.

</details>

---

### [[20_Research/Papers/大模型/ExpertIVS_Sociological_Expert_Driven_Individual_Value_Simulation_in_Large_Language_Models|ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models]]

![[assets/2608.20355_figure.png|800]]

- **arXiv**: [2608.20355](https://arxiv.org/abs/2608.20355)
- **PDF**: https://arxiv.org/pdf/2608.20355
- **详细分析**: [[20_Research/Papers/大模型/ExpertIVS_Sociological_Expert_Driven_Individual_Value_Simulation_in_Large_Language_Models|ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models]]
- **作者**: Zhen Wang, Yuqi Ren, Yuehan Cui, Hongxiang Wang, Jianxiang Peng, Zhaoxia Zhang, Bingkun Zhu, Tongxuan Zhang, Dezhi Tong, Deyi Xiong
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have demonstrated considerable potential for social simulation, yet struggle to accurately model individual value systems. Most existing methods mechanically stitch survey responses into prompts, which suffer from semantic fragmentation, failing to capture the internal coherence of human value systems. The value systems of LLMs are typically assessed using static multiple-choice questions, which fail to evaluate the value orientation in real-world dialogue interactions. To address these issues, we propose ExpertIVS, a framework employing 14 Sociological Expert Agents to interpret World Values Survey (WVS) responses through structured professional perspectives, rather than direct responses concatenation. These expert agents perform deep semantic reconstruction to generate robust and internally consistent individual profiles. To evaluate the consistency between LLMs and individual value systems during dynamic interactions, we further introduce a multi-agent debate mechanism. Extensive experiments across 480 individuals from 12 countries demonstrate that ExpertIVS achieves 90.78% value restoration fidelity and significantly outperforms baselines in value generalization (+5.3%). Moreover, ExpertIVS exhibits strong personality discriminability and behavioral consistency, enabling a shift from mere response concatenation to genuine sociological role-playing.

</details>

---

### [[20_Research/Papers/大模型/PrimeAgentOrchestrator_Memory-Primed_Agent_Spawning_for_Personal_AI_Infrastructure|PrimeAgentOrchestrator: Memory-Primed Agent Spawning for Personal AI Infrastructure]]

![[assets/2608.20342_first_page.png|800]]

- **arXiv**: [2608.20342](https://arxiv.org/abs/2608.20342)
- **PDF**: https://arxiv.org/pdf/2608.20342
- **详细分析**: [[20_Research/Papers/大模型/PrimeAgentOrchestrator_Memory-Primed_Agent_Spawning_for_Personal_AI_Infrastructure|PrimeAgentOrchestrator: Memory-Primed Agent Spawning for Personal AI Infrastructure]]
- **作者**: Myron Koch
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《PrimeAgentOrchestrator: Memory-Primed Agent Spawning for Personal AI Infrastructure》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) coding agents start each session with an empty context window, discarding accumulated knowledge from prior work. We present PrimeAgentOrchestrator (PAO), a system that spawns new instances of Claude Code -- Anthropic's terminal-based coding agent -- pre-loaded with relevant memories compiled from the user's existing personal databases. At spawn time, PAO queries two independently-operated memory backends in parallel (a PostgreSQL entity-observation database and a Cloudflare Worker semantic search index), fuses results using backend-specific retrieval strategies, and delivers the compiled briefing via filesystem injection that exploits the host agent's configuration auto-read behavior. PAO manages the full agent lifecycle including trust pre-seeding, readiness polling with error detection, and adaptive terminal text injection. We report on four months of regular deployment (December 2025 through March 2026) as an experience report, documenting three generations of context delivery mechanisms, the failure modes that motivated each redesign, and the engineering tradeoffs of bridging heterogeneous memory systems rather than building a unified one.

</details>

---
