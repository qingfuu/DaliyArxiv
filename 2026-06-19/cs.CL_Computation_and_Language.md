# cs.CL | Computation and Language | 2026-06-19

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Your_Mouse_and_Eyes_Secretly_Leak_Your_Preference_LLM_Alignment_using_Implicit_Feedback_from_Users|Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users]]

![[assets/2606.20482_figure.png|800]]

- **arXiv**: [2606.20482](https://arxiv.org/abs/2606.20482)
- **PDF**: https://arxiv.org/pdf/2606.20482
- **详细分析**: [[20_Research/Papers/大模型/Your_Mouse_and_Eyes_Secretly_Leak_Your_Preference_LLM_Alignment_using_Implicit_Feedback_from_Users|Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users]]
- **作者**: Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari, Aryan Sajith, Hamed Zamani
- **cs 子类**: cs.CL, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.75，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Post-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To align a Large Language Model (LLM), most existing methods collect explicit human feedback and train a reward model to predict the human preference based on the response text. These existing methods have two key limitations. First, the users rarely provide explicit feedback for LLM responses, which makes the high-quality preference annotation expensive to collect. Second, the methods do not leverage implicit human feedback, which has proven vital to the economic moats of Internet giants. To quantify the value of implicit feedback, we build a new dataset called IFLLM, which collects 1336 multi-turn questions from the 59 Mechanical Turk workers, their mouse trajectories, and eye gazing points to the LLMs' responses from their webcams. IFLLM shows that the users have very diverse types of gazing behavior and mouse trajectories. Our reward model based on the implicit user feedback boosts the accuracy of the text-based reward model from 55% to 64% and nearly triples the relative response quality improvements after applying the DPO to eight LLMs, demonstrating the value of implicit feedback in the wild. Our data collection website, dataset, and codes can be found at https://github.com/themehulpatwari/llm-implicit-feedback/.

</details>

---

### [[20_Research/Papers/大模型/AtomMem_Building_Simple_and_Effective_Memory_System_for_LLM_Agents_via_Atomic_Facts|AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts]]

![[assets/2606.19847_figure.png|800]]

- **arXiv**: [2606.19847](https://arxiv.org/abs/2606.19847)
- **PDF**: https://arxiv.org/pdf/2606.19847
- **详细分析**: [[20_Research/Papers/大模型/AtomMem_Building_Simple_and_Effective_Memory_System_for_LLM_Agents_via_Atomic_Facts|AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts]]
- **作者**: Yanyu Yao, Shangze Li, Zhi Zheng, Hui Zheng, Qi Liu, Tong Xu, Enhong Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-augmented systems often construct memory in a coarse and unstable manner, relying on inefficient memory representations or unstable unconstrained updates. To address these challenges, we propose AtomMem, a long-term memory system designed for value-dense storage and stable memory evolution. AtomMem introduces a Fact Executor, which selectively extracts high value atomic facts from long form interactions to serve as highly efficient memory representations. Subsequently, AtomMem organizes these facts into hierarchical event structures and temporal profiles, capturing coherent episodic contexts and tracking dynamically evolving user attributes over time. During retrieval, the system activates an associative memory graph to connect fragmented memories. Experiments on the LoCoMo benchmark confirm that AtomMem achieves state-of-the-art performance across various reasoning tasks, offering a scalable and economically viable solution for deploying intelligent personalized agents.

</details>

---

### [[20_Research/Papers/大模型/A_Layered_Security_Framework_Against_Prompt_Injection_in_RAG-Based_Chatbots|A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots]]

![[assets/2606.19660_figure.jpg|800]]

- **arXiv**: [2606.19660](https://arxiv.org/abs/2606.19660)
- **PDF**: https://arxiv.org/pdf/2606.19660
- **详细分析**: [[20_Research/Papers/大模型/A_Layered_Security_Framework_Against_Prompt_Injection_in_RAG-Based_Chatbots|A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots]]
- **作者**: Gulshan Saleem, Nisar Ahmed, Muhammad Imran Zaman, Ali Hassan
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《A Layered Security Framework Against Prompt Injection in RAG-Based Chatbots》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PromptBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Prompt injection is ranked as the most critical vulnerability in large language model (LLM) deployments by the OWASP Top 10 for LLM Applications, yet existing defenses operate at isolated pipeline stages and remain incomplete. Input filters cannot inspect retrieved documents, while output monitors cannot prevent malicious payloads from reaching the model. Consequently, retrieval-augmented generation (RAG) chatbots remain vulnerable to indirect injection, where a poisoned knowledge-base document compromises every user whose query retrieves it. We present a three-layer framework that intercepts both direct and indirect prompt injection throughout the inference pipeline. Layer 1 screens user input using a rule-based pattern library and a fine-tuned semantic anomaly classifier. Layer 2 enforces a provenance-based instruction hierarchy during context assembly, preventing retrieved content from overriding operator policy. Layer 3 audits model output using a policy rule engine and semantic drift detector before delivery. A continuous audit loop aggregates structured logs and supports retraining to adapt the classifier to emerging attack patterns. The framework is model-agnostic and deploys as middleware without modifying the underlying LLM. Evaluation on 5,080 samples across GPT-4o, Llama 3, and Mistral 7B shows that the framework reduces Attack Success Rate (ASR) from 71.4\% to 11.3\%, outperforming the best single-layer baseline by 27.3 percentage points and a published guardrail system by 23.8 percentage points, while maintaining a 4.8\% false positive rate and a median latency overhead of 61.2 ms. Ablation studies confirm that all three layers provide complementary protection and that their combined effect exceeds the sum of individual contributions.

</details>

---
