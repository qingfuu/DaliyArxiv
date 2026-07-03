# cs.CL | Computation and Language | 2026-07-01

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Generative_Skill_Composition_for_LLM_Agents|Generative Skill Composition for LLM Agents]]

![[assets/2606.32025_figure.png|800]]

- **arXiv**: [2606.32025](https://arxiv.org/abs/2606.32025)
- **PDF**: https://arxiv.org/pdf/2606.32025
- **详细分析**: [[20_Research/Papers/大模型/Generative_Skill_Composition_for_LLM_Agents|Generative Skill Composition for LLM Agents]]
- **作者**: Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi, Nakul Agarwal, Kwonjoon Lee, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Tianlong Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Generative Skill Composition for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent LLM agents benefit from skills for solving complex tasks. Skills encapsulate modular packages of procedural knowledge and instructions for performing specialized tasks, such as setting up a sandboxed environment, running a test suite, or refactoring a function across multiple files. As skill libraries grow and become reusable across tasks and domains, selecting an appropriate skill composition has emerged as a central bottleneck. Existing approaches fall into two categories. One exposes the agent's reasoning to the entire skill collection; the other performs skill retrieval via embeddings or LLM-based rerankers. Both provide useful insights; however, they miss the structural nature of skill composition, which is a joint decision over which skills, how many, and in what order -- three dimensions that cannot be decoupled. We formalize this as structured skill composition: given a task and a skill library, predict an executable skill plan that jointly specifies the activated subset, count, and execution order. We propose SkillComposer, which instantiates structured skill composition as task-conditioned skill sequence prediction. SkillComposer uses a constrained autoregressive decoder over skill identifiers, so subset, count, and order emerge jointly from a single decoding pass, and dependencies between successive skills are captured naturally. We build a training set of task-composition pairs from a real, human-curated skill library. We then evaluate SkillComposer along two axes: composition quality on a held-out test set, and downstream task success on SkillsBench across two production-grade coding agents. On GPT-5.2-Codex, Gemini-3-Pro-Preview, SkillComposer raises the pass rate by +23.1, +18.2pp over the no-skill baseline, surpassing top-3 retrieval and matching the gold-skill retrieval upper bound at lower prompt-token cost.

</details>

---

### [[20_Research/Papers/大模型/When_the_Database_Fails_Prompting_LLM_Dialogue_Agents_for_Safe_Recovery_in_Task-Oriented_Dialogue|When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue]]

![[assets/2606.31307_figure.png|800]]

- **arXiv**: [2606.31307](https://arxiv.org/abs/2606.31307)
- **PDF**: https://arxiv.org/pdf/2606.31307
- **详细分析**: [[20_Research/Papers/大模型/When_the_Database_Fails_Prompting_LLM_Dialogue_Agents_for_Safe_Recovery_in_Task-Oriented_Dialogue|When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue]]
- **作者**: Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Jiann Shiun Yuan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ReliabilityBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models used in task-oriented dialogue often produce fluent but unsafe responses when backend database calls fail, return empty results, or surface mismatched information, inventing venues, confirmations, or booking details not grounded in the database. We study a lightweight prompting-based recovery approach that improves robustness without retraining or additional model calls. We compare three response strategies, including a guided recovery prompt conditioned on structured database status, across six open-weight model families (DeepSeek-R1, Gemma-2, Llama-3, Mistral, Phi-3, and Qwen-2.5) and four database conditions: empty result, wrong-domain retrieval, API error, and clean retrieval. Using fault-injected benchmarks built on two structurally different datasets, MultiWOZ 2.2 (5 domains) and SGD (20 domains), we find that naive agents hallucinate on 30.5% of failure turns on MultiWOZ and 20.9% on SGD. Our Guided-Retry strategy reduces hallucination by 50% on MultiWOZ (30.5 to 15.3%) and by 42% on SGD (20.9 to 12.2%) without retraining. However, residual hallucination remains substantial (6-37% across models), with wrong-domain failures the hardest case. Results are consistent across both datasets and all six model families, and human annotation shows substantial agreement while supporting the validity of the automatic commitment-safety metric.

</details>

---

### [[20_Research/Papers/大模型/CORTEX_Token-Level_Hallucination_Detection_in_RAG_via_Comparative_Internal_Representations|CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations]]

![[assets/2606.31033_figure.png|800]]

- **arXiv**: [2606.31033](https://arxiv.org/abs/2606.31033)
- **PDF**: https://arxiv.org/pdf/2606.31033
- **详细分析**: [[20_Research/Papers/大模型/CORTEX_Token-Level_Hallucination_Detection_in_RAG_via_Comparative_Internal_Representations|CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations]]
- **作者**: Kazuaki Furumai, Shuichiro Haruta, Kazunori Matsumoto, Daisuke Kamisaka
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose CORTEX, a token-level hallucination detection method for Retrieval-Augmented Generation (RAG). In long-form RAG outputs, hallucinations often arise in localized spans rather than throughout an entire response. CORTEX therefore identifies ungrounded content at the token level, enabling fine-grained localization of hallucinations. The key intuition behind CORTEX is that tokens grounded in retrieved documents should be more strongly influenced by those documents than hallucinated tokens. To capture this document-induced effect, CORTEX compares internal representations of a large language model (LLM) under two conditions: with and without the retrieved documents. Instead of relying solely on each token's immediate sensitivity to the retrieved documents, CORTEX also leverages the propagation of document-grounded information through preceding tokens, reducing false positives for tokens whose evidence has already been absorbed into the context. Finally, CORTEX applies post-processing smoothing step that models the tendency of hallucination labels to persist over contiguous spans, reducing local noise and encouraging span-consistent predictions. Experiments on two RAG benchmarks and three LLMs show that CORTEX substantially improves token-level hallucination detection, with each component consistently contributing to performance gains.

</details>

---

### [[20_Research/Papers/大模型/From_Propositional_to_Perceptual_Asymmetry_Extending_Frictive_Policy_Optimization_to_Asymmetric_Partial_Information_Dialogue|From Propositional to Perceptual Asymmetry: Extending Frictive Policy Optimization to Asymmetric Partial Information Dialogue]]

![[assets/2606.30973_first_page.png|800]]

- **arXiv**: [2606.30973](https://arxiv.org/abs/2606.30973)
- **PDF**: https://arxiv.org/pdf/2606.30973
- **详细分析**: [[20_Research/Papers/大模型/From_Propositional_to_Perceptual_Asymmetry_Extending_Frictive_Policy_Optimization_to_Asymmetric_Partial_Information_Dialogue|From Propositional to Perceptual Asymmetry: Extending Frictive Policy Optimization to Asymmetric Partial Information Dialogue]]
- **作者**: Yifan Zhu, Kyeongmin Rim, James Pustejovsky
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《From Propositional to Perceptual Asymmetry: Extending Frictive Policy Optimization to Asymmetric Partial Information Dialogue》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frictive Policy Optimization (FPO; Pustejovsky et al., 2025) treats friction in collaborative dialogue -- misalignment, misunderstanding, repair -- as an epistemic signal essential to common-ground construction, rather than noise to be minimized. However, FPO and its implementations assume shared perceptual contexts, where friction arises from differently interpreted propositions over the same scene, which we define as propositional asymmetry. We extend FPO to perceptual asymmetry, where participants hold asymmetric partial information and the same referring expression yields different denotations depending on whose information state grounds the reference. We evaluate this through cross-corpora analysis and LLM probing on referentially asymmetric dialogue tasks, primarily the HCRC MapTask (Anderson et al., 1991). We find that FPO's friction functional is empirically valid only when evaluated from within each participant's information horizon: different landmark configurations produce qualitatively distinct grounding failure modes, with a small class of ambiguous configurations driving a disproportionate share of misunderstandings through trajectories that appear successful but silently diverge. The LLM probe confirms that having the "right perspective" matters more than having all perspectives: the informed single viewpoint outperforms omniscient access to both participants' contexts. We propose two annotation refinements: subtype decomposition of pending grounding states and accommodation-aware alignment classification.

</details>

---

### [[20_Research/Papers/具身智能/ViTL_Temporal_Logic-Guided_Zero-Shot_Natural_Language_Navigation_via_Vision-Language_Models|ViTL: Temporal Logic-Guided Zero-Shot Natural Language Navigation via Vision-Language Models]]

![[assets/2606.30696_figure.png|800]]

- **arXiv**: [2606.30696](https://arxiv.org/abs/2606.30696)
- **PDF**: https://arxiv.org/pdf/2606.30696
- **详细分析**: [[20_Research/Papers/具身智能/ViTL_Temporal_Logic-Guided_Zero-Shot_Natural_Language_Navigation_via_Vision-Language_Models|ViTL: Temporal Logic-Guided Zero-Shot Natural Language Navigation via Vision-Language Models]]
- **作者**: Kaier Liang, Hengde Dai, Cristian-Ioan Vasile
- **cs 子类**: cs.CL, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.45（加权：具身智能 0.6，大模型 0.55，机器人 0.3）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《ViTL: Temporal Logic-Guided Zero-Shot Natural Language Navigation via Vision-Language Models》归入 具身智能、大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling robots to follow natural language commands to complete zero-shot long-horizon tasks remains challenging. It requires extracting implicit temporal and logical constraints from natural language commands and executing multiple sub-tasks accordingly. Recent zero-shot object navigation methods use vision-language models (VLMs) to guide frontier-based exploration in unknown environments, but they are limited to single-target tasks. Real-world commands such as "Clean either the chair or the couch, then turn on the tv." require navigating to multiple targets in a temporally constrained order, which no existing zero-shot system can handle. We present ViTL, a framework that addresses this gap at two levels. At the task level, we use a large language model (LLM) to compile natural language commands into Linear Temporal Logic (LTL) formulas, which are then converted into Deterministic Finite Automata~(DFA) that coordinate multi-channel value maps and trigger dynamic replanning when new objects are detected. At the navigation level, we introduce directional score: rather than producing a direction-agnostic value across the entire field of view, we label frontier directions on the observation image and extract per-direction scores from the VLM. Experiments on Habitat-Matterport 3D (HM3D) show that the full framework enables zero-shot long-horizon completion of natural language navigation tasks with temporal constraints, and that directional score improves single-target navigation accuracy and efficiency over the baseline.

</details>

---
