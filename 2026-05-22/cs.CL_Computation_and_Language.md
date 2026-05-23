# cs.CL | Computation and Language | 2026-05-22

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/强化学习/LANG_Reinforcement_Learning_for_Multilingual_Reasoning_with_Language-Adaptive_Hint_Guidance|LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance]]

![[assets/2605.22567_first_page.png|800]]

- **arXiv**: [2605.22567](https://arxiv.org/abs/2605.22567)
- **PDF**: https://arxiv.org/pdf/2605.22567
- **详细分析**: [[20_Research/Papers/强化学习/LANG_Reinforcement_Learning_for_Multilingual_Reasoning_with_Language-Adaptive_Hint_Guidance|LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance]]
- **作者**: Yuchun Fan, Bei Li, Peiguang Li, Yilin Wang, Yongyu Mu, Jian Yang, Xin Chen, Rongxiang Weng, Jingang Wang, Xunliang Cai, Jingbo Zhu, Tong Xiao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

大语言模型在多步推理任务上借助强化学习已经表现出明显优势，但这种收益在多语言场景中并没有充分体现出来。对于非英语推理，现有方法面临一个核心矛盾：如果过度强调输入语言一致性，推理质量会明显下降；如果更重视推理能力，模型又容易在生成过程中不自觉地“漂移”到英语。本文聚焦多语言推理中的这一瓶颈，尝试在保持目标语言一致性的同时提升复杂推理能力，因此具有较强的现实应用价值，尤其适用于多语种数学解题与跨语言推理系统。

#### 方法概述和架构

论文提出 LANG，一个面向多语言推理的强化学习框架，核心思路是利用“与语言相关的提示信息”来引导模型在非英语任务中的探索。具体来说，模型在训练阶段会接收语言条件化的 hint，帮助其更稳定地进入正确推理轨道，从而减少早期探索时的无效搜索。为了避免模型过度依赖这些提示，方法中加入了渐进式衰减机制，随着训练推进逐步撤去脚手架，让模型逐渐独立完成推理。与此同时，框架还设计了 language-adaptive switch，根据不同语言的学习难度动态调整学习跨度或训练视野，使模型能够针对不同语言采取不同强度的优化策略。整体上，LANG 将语言约束、推理探索与自适应训练节奏结合起来，以同时兼顾推理正确性和语言一致性。

#### 实验结果分析

作者在具有挑战性的多语言数学基准上验证了 LANG，实验表明该方法能够显著提升推理性能，同时不会损害输出语言的一致性。与现有方法相比，LANG 更好地缓解了“推理变强但语言漂移到英语”的问题，说明语言自适应提示确实能改善多语言强化学习中的探索过程。除此之外，论文还展示了该框架不仅适用于数学任务，也能推广到更广泛的场景，并在模型不同层之间带来更一致的语言对齐效果。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

强化学习已被证明能有效增强大语言模型（LLMs）的多步推理能力，但这种收益尚未完全迁移到多语言场景中。现有方法面临一个根本性的权衡：若优先保证输入语言一致性，推理质量会严重受损；若优先提升推理能力，模型往往会意外地向英语漂移。为了解决这一问题，我们提出 LANG，一个新的框架，它利用与语言条件相关的提示信息来引导非英语推理任务中的探索。我们的方法包含两个关键机制，以防止模型过度依赖这些提示：一种渐进式衰减策略，逐步撤去脚手架；以及一个语言自适应开关，针对不同语言的难度设定不同的学习跨度。基于具有挑战性的多语言数学基准的实验证明，LANG 能在不牺牲语言一致性的前提下显著提升推理性能。此外，我们还表明该框架不仅可推广到数学任务，还能促进模型各层之间更一致的语言对齐。

</details>

---

### [[20_Research/Papers/大模型/Maestro_Reinforcement_Learning_to_Orchestrate_Hierarchical_Model-Skill_Ensembles|Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles]]

![[assets/2605.22177_figure.png|800]]

- **arXiv**: [2605.22177](https://arxiv.org/abs/2605.22177)
- **PDF**: https://arxiv.org/pdf/2605.22177
- **详细分析**: [[20_Research/Papers/大模型/Maestro_Reinforcement_Learning_to_Orchestrate_Hierarchical_Model-Skill_Ensembles|Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles]]
- **作者**: Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, Zhengxi Lu, Fan Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.45，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

随着大模型和模块化技能库的发展，自治智能体已经具备更强的推理、感知和调用工具的能力，但现有系统往往依赖单一主模型和固定的调度逻辑来使用这些能力。问题在于，不同LLM在数学推理、视觉理解、代码生成、领域分析等场景各有优势，静态路由无法充分发挥模型与技能之间的互补性。本文关注的是如何在复杂多模态任务中，让智能体根据当前上下文动态选择合适的专家模型与技能组合，这一问题对通用智能体、协作式工具调用和多模态推理系统都很关键。

#### 方法概述和架构

论文提出 Maestro（Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration），把多模态任务重写为一个在分层模型-技能注册表上的序列决策问题。系统由一个轻量级编排策略模型负责决策，它在每一步根据当前上下文决定是否调用外部专家、选择哪个模型-技能对，以及何时终止。Maestro 的注册表包含两层结构：上层是供编排器直接使用的粗粒度技能，下层是通过关键词触发或专家模型分类来激活的细粒度技能，同时还维护一个由冻结专家LLM组成的候选模型池。训练时，策略通过基于结果的强化学习优化，不需要逐步标注的监督信号；推理时，策略在环境反馈驱动下逐步构造模型与技能的组合，并形成最终答案。作者还将该过程形式化为有限时域POMDP，并设计多维奖励来同时鼓励正确性、逻辑一致性与多模态对齐。

#### 实验结果分析

论文在10个代表性多模态基准上评估了 Maestro，覆盖数学推理、图表理解、高分辨率感知和领域分析等任务，并与 GPT-5、Gemini-2.5-Pro 等强基线比较。结果显示，仅用一个4B的编排器，Maestro 的平均准确率达到70.1%，超过 GPT-5 的69.3% 和 Gemini-2.5-Pro 的68.7%。此外，作者还报告了对未见过的模型和技能的泛化能力：在加入域外专家后，系统在4个困难基准上的平均结果达到59.5%，优于所有闭源基线。文中还分析了效率与可扩展性，指出该方法在低延迟和较少 token 消耗下仍能保持较强性能。

<details>
<summary>完整摘要</summary>

大语言模型（LLM）与模块化技能的迅速普及，已经为自治智能体赋予了越来越强的能力。现有框架通常依赖单一大模型以及固定逻辑来连接这些技能，这带来了一个关键瓶颈：不同LLM在不同领域各有优势，而当前框架却无法充分利用模型与技能的互补长处，从而限制了它们在下游任务上的表现。本文提出 Maestro（Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration），这是一个由强化学习驱动的编排框架，它将异构多模态任务重构为在分层模型-技能注册表上的序列决策过程。与把所有知识整合进单一模型不同，Maestro 训练一个轻量级策略，动态组合冻结的专家模型与两层技能库，并在每一步决定是否调用外部专家、选择哪个模型-技能对，以及何时终止。该策略通过基于结果的强化学习进行优化，不需要逐步监督。我们在十个具有代表性的多模态基准上评估 Maestro，覆盖数学推理、图表理解、高分辨率感知和领域特定分析等任务。仅使用一个4B的编排器，Maestro 的平均准确率达到70.1%，超过 GPT-5（69.3%）和 Gemini-2.5-Pro（68.7%）。更重要的是，学习到的协调策略能够在无需重新训练的情况下泛化到未见过的模型和技能：在注册表中加入域外专家后，系统在四个高难度基准上的平均成绩达到59.5%，优于所有闭源基线。Maestro 还保持了较高的计算效率和较低的延迟。代码已开源于 https://github.com/jinyangwu/Maestro 。

</details>

---

### [[20_Research/Papers/大模型/A_Comparative_Study_of_Language_Models_for_Khmer_Retrieval-Augmented_Question_Answering|A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering]]

![[assets/2605.22099_figure.png|800]]

- **arXiv**: [2605.22099](https://arxiv.org/abs/2605.22099)
- **PDF**: https://arxiv.org/pdf/2605.22099
- **详细分析**: [[20_Research/Papers/大模型/A_Comparative_Study_of_Language_Models_for_Khmer_Retrieval-Augmented_Question_Answering|A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering]]
- **作者**: Sereiwathna Ros, Phannet Pov, Ratanaktepi Chhor, Kimleang Ly, Wan-Sup Cho, Saksonita Khoeurn
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

这篇论文聚焦柬埔寨语（Khmer）电信领域文档问答中的检索增强生成（RAG）系统，目标是让大模型回答能够严格依据检索到的证据，减少幻觉并提升事实可靠性。与英语或高资源语言不同，Khmer 属于低资源、非拉丁字母脚本，存在分词标准不稳定、OCR 噪声和可用标注数据稀缺等问题，使得检索、生成和评估都更困难。作者认为，现有 RAG 评测与模型选择经验大多来自英语环境，是否能直接迁移到 Khmer 仍不清楚，因此有必要系统比较检索器、生成器和评估指标在这一场景下的表现。

#### 方法概述和架构

论文构建了一个面向 Khmer 电信领域文档的 RAG 问答系统，整体流程为：用户问题输入后，先通过稠密检索从文档库中召回相关片段，再将问题与检索上下文一起送入生成模型回答。检索阶段比较了三个嵌入模型：BGE-M3、Jina-Embeddings-v3 和 Qwen3-Embedding，使用余弦相似度在文档分块向量中选取 top-k 片段并拼接为上下文。生成阶段固定采用表现最好的检索器 BGE-M3，进一步比较五个后端模型：Qwen3、Qwen3.5、Sailor2-8B-Chat、SeaLLMs-v3-7B-Chat 和 Llama-SEA-LION-v2-8B-IT。实验数据来自官方 ICT/电信相关公开文档，预处理后形成超过 7000 个 chunk，并人工整理了 200 对 Khmer 问答作为 gold 数据集。评估上，作者采用六个受 RAGAS 启发的指标：faithfulness、answer relevance、context relevance、factual correctness、answer similarity 和 answer correctness，同时用 GPT-4o-mini 作为裁判模型、BGE-M3 计算语义相似度。

#### 实验结果分析

实验表明，在 Khmer 文档的稠密检索任务上，BGE-M3 明显优于 Jina-Embeddings-v3 和 Qwen3-Embedding，Hit Rate@3、File Hit Rate@3、MRR@3 和 Precision@3 均为三者中最佳。以 BGE-M3 作为检索器后，不同生成模型没有出现“全指标通吃”的单一最优模型：Qwen3.5-9B 在 faithfulness 和 context relevance 上最好，Qwen3-8B 的 factual correctness 最高，而 SeaLLMs-v3-7B-Chat 在 answer relevance、answer similarity 和 answer correctness 上领先。整体结论是，Khmer RAG 的主要瓶颈仍在检索端，而生成端模型的强项取决于更看重证据对齐、事实精度还是语义相似度。文中节选未给出更多超参数、泛化实验或消融的具体数值细节。

<details>
<summary>完整摘要</summary>

检索增强生成（RAG）已成为一种很有前景的范式，它能够将大语言模型（LLM）的输出建立在检索到的证据之上，从而减少幻觉并提高事实准确性。然而，对于像 Khmer 这样低资源、非拉丁字母脚本的语言，其有效性仍然几乎没有被系统研究。本文提出了一个面向 Khmer 语电信领域文档的基于 RAG 的问答系统，并进行两阶段比较评估。第一阶段，我们对三种嵌入模型进行基准测试：BGE-M3（567M）、Jina-Embeddings-v3（570M）和 Qwen3-Embedding（597M），用于 Khmer 文档的稠密检索。BGE-M3 始终表现最佳，Hit Rate@3 达到 0.285，File Hit Rate@3 达到 0.700，MRR@3 达到 0.221，Precision@3 达到 0.112，明显优于其他检索器。第二阶段，在选定 BGE-M3 作为检索器后，我们在一个精心构建的 200 对 Khmer 问答黄金数据集上评估五个生成后端：Qwen3（8B）、Qwen3.5（9B）、Sailor2-8B-Chat、SeaLLMs-v3-7B-Chat 和 Llama-SEA-LION-v2-8B-IT。为量化系统性能，我们采用六个受 RAGAS 启发的指标：faithfulness、answer relevance、context relevance、factual correctness、answer similarity 和 answer correctness。结果表明，没有单一模型能够在所有指标上全面领先：Qwen3.5-9B 在 faithfulness（0.859）和 context relevance（0.726）上最高，Qwen3-8B 在 factual correctness（0.380）上最高，而 SeaLLMs-v3-7B-Chat 在 answer relevance（0.867）、answer similarity（0.836）和 answer correctness（0.599）上表现最佳。这些发现表明，对于 Khmer RAG 而言，检索器选择仍然是主要瓶颈；而生成器的优势则取决于任务更强调证据对齐、事实精度还是语义相似性。

</details>

---

### [[20_Research/Papers/大模型/Faithful-MR1_Faithful_Multimodal_Reasoning_via_Anchoring_and_Reinforcing_Visual_Attention|Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention]]

![[assets/2605.22072_first_page.png|800]]

- **arXiv**: [2605.22072](https://arxiv.org/abs/2605.22072)
- **PDF**: https://arxiv.org/pdf/2605.22072
- **详细分析**: [[20_Research/Papers/大模型/Faithful-MR1_Faithful_Multimodal_Reasoning_via_Anchoring_and_Reinforcing_Visual_Attention|Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention]]
- **作者**: Changyuan Tian, Zhicong Lu, Huaxing Liu, Xiang Wang, Shuai Li, Yu Chen, Wenqian Lv, Zichuan Lin, Juncheng Diao, Deheng Ye
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

随着 RLVR（可验证奖励强化学习）在大模型复杂推理中的应用，研究者开始将其扩展到多模态大语言模型（MLLMs），用于提升图文联合推理能力。然而，现有方法在多模态场景中暴露出“忠实性”问题：模型不仅需要准确感知与任务相关的视觉证据，还需要在后续推理中持续、正确地使用这些证据。已有感知监督往往依赖文本描述而非直接作用于图像区域，且对“证据被感知后又在推理中被丢弃或与答案矛盾”的问题关注不足，因此多模态基准上的收益并不理想。

#### 方法概述和架构

论文提出 Faithful-MR1，一个通过“锚定”和“强化”视觉注意力来实现忠实多模态推理的训练框架。第一阶段是 Anchoring，将感知显式化为推理前的一个子任务，使用专门的 <Focus> token，并直接以图像区域作为监督对象，而不是通过文本描述间接对齐。第二阶段是 Reinforcing，通过反事实图像干预来暴露“忠实使用”是否发生：当视觉信息在因果上确实影响答案时，模型会因为把注意力集中到关键区域而获得奖励。整个流程将“先看准”与“再用对”串联起来，分别约束感知和推理两个环节，从而缓解感知-推理脱节问题。

#### 实验结果分析

实验在 Qwen2.5-VL-Instruct 3B 和 7B 两种骨干模型上进行，并与近期多模态推理基线比较。结果表明，Faithful-MR1 在多个多模态推理基准上均取得更优表现，同时使用的训练数据显著更少。摘要未给出具体数值，因此可见文本未给出具体数值。整体结论显示，该方法不仅提升了性能，也更有效地约束了模型对视觉证据的忠实使用。

<details>
<summary>完整摘要</summary>

基于可验证奖励的强化学习（RLVR）已成为推动大语言模型复杂推理能力提升的一种有前景的范式，近期工作也将 RLVR 扩展到了多模态大语言模型（MLLMs）。然而，这一迁移带来了一个忠实性挑战：模型需要对任务相关的视觉证据进行忠实感知，并在推理过程中忠实使用这些证据，这导致多模态基准上的提升并不理想。具体而言，现有感知监督通常作用于文本描述，而不是原生地作用于图像区域；与此同时，对“忠实使用”的关注大多被忽视，这暴露出感知与推理之间的脱节问题——即使证据被正确感知，也可能在推理中被丢弃或与结论相矛盾。为了弥合这些缺口，我们提出 Faithful-MR1，一种通过锚定并强化视觉注意力来同时解决忠实多模态推理两方面问题的训练框架。Anchoring 阶段将感知转化为一个显式的推理前子任务，使用专门的 &lt;Focus&gt; token，并直接以图像区域而非文本描述来监督其注意力。Reinforcing 阶段则通过反事实图像干预来显式暴露“忠实使用”，并奖励那些答案正确、且视觉注意力集中在视觉因果关键位置上的轨迹。大量实验表明，Faithful-MR1 在 Qwen2.5-VL-Instruct 3B 和 7B 骨干模型上都优于近期多模态推理基线，同时所需训练数据明显更少。

</details>

---

### [[20_Research/Papers/大模型/FlyRoute_Self-Evolving_Agent_Profiling_via_Data_Flywheel_for_Adaptive_Task_Routing|FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing]]

![[assets/2605.22057_figure.png|800]]

- **arXiv**: [2605.22057](https://arxiv.org/abs/2605.22057)
- **PDF**: https://arxiv.org/pdf/2605.22057
- **详细分析**: [[20_Research/Papers/大模型/FlyRoute_Self-Evolving_Agent_Profiling_via_Data_Flywheel_for_Adaptive_Task_Routing|FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing]]
- **作者**: Rongjun Li, Ziyu Zhou, Yihang Wu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

在企业级多智能体系统中，路由器需要把用户查询分发给最合适的专家 agent，以保证回答质量、时延和成本的平衡。但现实里 agent 的能力会随着 prompt、工具和底层模型的更新不断变化，而部署时登记的能力描述和示例往往长期不更新，导致路由依据逐渐失真。本文关注的正是“静态画像”与“动态 agent 能力”之间的矛盾，尤其适合企业开发支持、任务分发和专家选择等场景。

#### 方法概述和架构

论文提出 FlyRoute，一个基于数据飞轮的自进化 agent profiling 框架。系统为每个 agent 维护三部分画像：注册时的 seed description、从真实成功样本中蒸馏得到的 learned description，以及 success store 中累积的高质量 query-response 证据。路由时，LLM 路由器会同时接收当前画像描述和通过 BM25 检索到的历史成功样本，用于完成专家选择；训练/在线流式阶段则对已分发查询进行质量门控，只有高质量的 query-agent 对才会进入成功库并周期性蒸馏为新的能力描述。为提高数据效率，FlyRoute 还设计了 uncertainty-driven exploration 策略：结合画像不确定性、查询与 agent 的 BM25 相关性以及新颖性权重，优先探索“画像不足但又可能相关”的 agent，减少无效试探和重复采样。

#### 实验结果分析

实验在作者自建的企业开发支持数据集上进行，采用同一 backbone 的 zero-shot LLM router 作为基线，并在标准 routing accuracy 上评估。结果显示，FlyRoute 在每个 agent 仅提供 5 条 seed query 的冷启动条件下，就能把准确率从 72.57% 提升到 78.04%，说明检索成功样本与画像信息本身就能显著增强冷启动路由。进一步将 7,211 条带标注训练查询流式输入飞轮后，准确率提升到 89.83%，相较 zero-shot 提升 17.26 个百分点、相较 cold start 提升 11.79 个百分点。论文还报告了在四个专家领域上的一致增益，以及探索策略与消融实验的对比结果，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

企业级路由器负责将查询分配给专家 agent，但已部署的画像保持静态，而 agent 本身会不断演化（例如 prompt、工具、模型发生变化），开发者也很少持续更新描述或示例。为此，我们提出 FlyRoute，一个自进化画像框架，它从真实流量中持续积累能力证据：先分发候选查询，再通过质量门控把成功的 query-agent 对写入各自的成功库，随后周期性地将这些证据蒸馏为学习得到的能力描述，并将这些描述与通过 BM25 检索到的成功样本一起注入 LLM 路由器。为了让这个飞轮更具数据效率，FlyRoute 设计了定向探索策略，将画像不确定性、BM25 相关性和词汇新颖性结合起来，只优先关注那些画像不足但对当前查询“有可能相关”的 agent，从而避免重复采集证据。在我们基于真实路由查询构建的专有企业开发支持数据集上，FlyRoute 在相同 backbone 的 zero-shot LLM router 上取得了提升：仅使用每个 agent 五条 seed query 时，准确率从 72.57% 提高到 78.04%，说明仅引入画像检索就已经能增强冷启动路由；当将 7,211 条带标注训练查询流式输入飞轮后，准确率进一步提升到 89.83%，相较 zero-shot 提升 17.26 个百分点、相较 cold start 提升 11.79 个百分点，并且在四个专家领域上都取得了稳定增益，评价指标为单金标准测试样本上的标准 routing accuracy。

</details>

---

### [[20_Research/Papers/大模型/Check_Your_LLM's_Secret_Dictionary!_Five_Lines_of_Code_Reveal_What_Your_LLM_Learned_(Including_What_It_Shouldn't_Have)|Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)]]

![[assets/2605.22005_figure.png|800]]

- **arXiv**: [2605.22005](https://arxiv.org/abs/2605.22005)
- **PDF**: https://arxiv.org/pdf/2605.22005
- **详细分析**: [[20_Research/Papers/大模型/Check_Your_LLM's_Secret_Dictionary!_Five_Lines_of_Code_Reveal_What_Your_LLM_Learned_(Including_What_It_Shouldn't_Have)|Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)]]
- **作者**: Hisashi Miyashita
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

这篇工作关注一个很直接但常被忽略的问题：不经过推理、仅看大模型输出层权重本身，能否判断模型到底“学会了什么”。作者指出，transformer 的 lm_head 是模型生成任何 token 的最后一道门，但它很少被单独分析，因此训练数据构成、数据清洗偏好以及潜在安全风险都可能被隐藏在权重里。该研究之所以值得关注，是因为它只需少量代码和权重文件，就能静态审计模型能力结构，甚至发现训练中不该出现的词汇簇与 glitch token。

#### 方法概述和架构

论文对 transformer 大模型的 lm_head 权重矩阵做奇异值分解（SVD），将 W 分解为 U、S、V^T，并把左奇异向量对应的高分词元视为模型在某个语义/结构方向上的“秘密词典”。作者通过读取每个奇异向量 top-k 的 token 聚类来解释模型的词汇子空间，并比较 GPT-OSS-120B、Gemma-2-2B、Qwen2.5-1.5B 的结构差异。为了把这种“看起来像簇”的现象量化，论文提出 Vocabulary Cluster Score（VCS），用 top token 的 lm_head 行向量之间平均余弦相似度衡量簇的几何一致性。进一步地，作者定义 Weighted Projection Score（WPS），利用奇异值与左奇异向量权重对 token 打分，作为静态 glitch token 检测器。整个流程不需要模型推理，也不需要输入样本，只依赖 lm_head 权重和 tokenizer；作者还比较了 base 与 instruct 版本，观察后训练对这些子空间的影响。

#### 实验结果分析

实验在 GPT-OSS-120B、Gemma-2-2B、Qwen2.5-1.5B 上进行，采用 top 30 个奇异向量、每个向量取 20 个 token 进行分析；可见文本未给出具体数值以外的完整实验表格。结果显示，不同模型的 lm_head 子空间结构差异显著：GPT 呈现从标点/结构词到规范、软件工程词汇的分层体系，Gemma 的高一致性簇主要由十九世纪前英语拼写和 long-s 相关词元主导，Qwen 则表现出更广泛的多语种覆盖。VCS 说明这些主导方向在几何上非常紧凑，而 base–instruct 对比显示，部分“伦理上不适合公开”的词汇子空间在预训练阶段就已形成，后训练对齐并未消除其结构。WPS 还在 GPT-OSS-120B 上恢复出一个广为人知的 CJK glitch token（ID 137606），证明该方法可用于预发布安全审计。

<details>
<summary>完整摘要</summary>

我们证明：对基于 transformer 的大语言模型的 lm_head 权重矩阵做奇异值分解，只需五行 PyTorch 代码，而且无需任何模型推理，就能直接从模型权重中揭示出可解释的语义子空间。每个左奇异向量都会标识出在隐藏状态与该奇异方向对齐时最容易被选中的词汇 token；检查这些聚类可以暴露模型训练数据的构成以及数据筛选的理念。我们分析了 GPT-OSS-120B、Gemma-2-2B 和 Qwen2.5-1.5B，发现奇异值谱和词汇簇结构在不同模型之间存在系统性差异：GPT 呈现功能上分化的分层子空间；Gemma 主要由十九世纪前的英语拼写构成，形成阶梯式聚类结构，这可能有助于提高输出可控性；Qwen 则表现出广泛的多语种覆盖，同时存在一些其作者认为不适合直接公开的词汇子空间。base 与 instruct 的比较表明，具有伦理风险的子空间起源于预训练阶段，并不会被后训练对齐移除。我们提出 Vocabulary Cluster Score（VCS）来量化子空间的一致性，并提出 Weighted Projection Score（WPS）作为一种静态 glitch token 检测器；将 WPS 应用于 GPT-OSS-120B，无需任何模型推理就恢复出了 shokubutsu-hyakka-tsu（ID 137606），这是 CJK 语言社区广为报道的著名 glitch token。我们提出了问题词汇内容的根因分类法，并呼吁将 lm_head 的 SVD 分析作为标准的发布前安全审计步骤。我们的结果还表明，未来可以探索由 SVD 引导的 tokenizer 优化，以及更可控的大语言模型设计。

</details>

---

### [[20_Research/Papers/强化学习/Why_Semantic_Entropy_Fails_Geometry-Aware_and_Calibrated_Uncertainty_for_Policy_Optimization|Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization]]

![[assets/2605.21801_figure.png|800]]

- **arXiv**: [2605.21801](https://arxiv.org/abs/2605.21801)
- **PDF**: https://arxiv.org/pdf/2605.21801
- **详细分析**: [[20_Research/Papers/强化学习/Why_Semantic_Entropy_Fails_Geometry-Aware_and_Calibrated_Uncertainty_for_Policy_Optimization|Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization]]
- **作者**: Zheyuan Zhang, Kaiwen Shi, Han Bao, Zehong Wang, Tianyi Ma, Yanfang Ye
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

近年来，大语言模型的后训练已成为提升推理能力与对齐效果的关键环节，尤其是在无需 critic 的群体式策略优化方法中，模型会利用自身生成的样本继续学习。问题在于，这类方法虽然可扩展，但很难区分“有信息量的学习信号”和“噪声较大的无效波动”，从而影响梯度更新质量与训练稳定性。已有做法常用语义熵一类的响应级不确定性来调节优化过程，但它们与真实梯度方差和奖励信息之间的关系并不清晰，因此这篇工作关注的是一个很实际但长期被经验化处理的问题：不确定性信号到底该如何设计，才能真正服务于策略优化。

#### 方法概述和架构

本文提出 Geometric-aware Calibrated Policy Optimization（GCPO），把不确定性显式建模为“刻画并调节梯度方差与学习信号质量”的机制。作者首先从理论与统计分析出发，指出现有熵类估计存在两个缺口：其一是“各向异性缺口”，即只看语义簇的概率分布，忽略了不同语义误差在几何上造成的方向与幅度差异；其二是“校准缺口”，即不确定性与奖励是否真的能提供有效学习信号并不一致。为弥补前者，GCPO引入几何感知的分歧度量，包括 Cosine Dispersion（CD）和 Barycentric Transport（BoT），用于捕捉语义层面的结构性差异，而不只是熵值大小。为弥补后者，方法再加入 Reward Dispersion（RD）模块，用奖励分散度来衡量样本是否真的携带可学习的区分信息，并据此调节更新强度。整体上，GCPO在GRPO式训练流程中，对每个输入的多条采样响应先计算几何不确定性与奖励校准信号，再联合调制策略梯度更新，从而抑制无信息噪声、保留有价值的梯度方向。

#### 实验结果分析

作者在多个基准上验证了方法效果，重点包括问答与数学推理任务，并将 GCPO 与熵类基线及 GRPO 风格方法进行比较。实验表明，几何感知指标（CD、BoT）比传统熵更能跟踪样本级梯度方差，且在后训练性能上更稳定地带来提升。文中还提到做了消融实验与统计分析，用于验证各模块对性能与梯度预测能力的贡献；可见文本未给出具体数值。整体结论是：将不确定性设计成与优化动力学对齐的信号，比单纯使用语义熵更可靠。

<details>
<summary>完整摘要</summary>

后训练已成为提升大语言模型推理能力与对齐能力的核心环节。在这一过程中，无需 critic 的模型可以利用模型自身生成的输出进行可扩展学习，但缺乏一种有原则的方法来区分有信息的信号与噪声。近期方法开始使用响应级度量作为不确定性信号，以调节 GRPO 等基于群体的优化方法。然而，这些方法的经验效果并不稳定，而且其对优化动力学的影响机制也并不清楚。本文据我们所知，首次给出一种有原则的表述，将不确定性信号解释为用于刻画和调节梯度方差以及学习信号质量的机制。基于经验与理论分析，我们识别出当前基于熵的估计器存在两个关键缺口：各向异性缺口和校准缺口。受此分析启发，我们提出 Geometric-aware Calibrated Policy Optimization（GCPO），这是一个新的框架，它将几何感知度量与奖励校准相结合：前者用于捕捉语义分歧，后者用于将不确定性与学习信号强度对齐。多项基准实验表明，该方法能够更准确地跟踪梯度变化，并持续提升后训练性能。我们的结果强调，设计与优化动力学一致的不确定性信号至关重要，也为稳健的后训练提供了一种有原则的视角。

</details>

---
