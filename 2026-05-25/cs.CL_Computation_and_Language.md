# cs.CL | Computation and Language | 2026-05-25

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/大模型/Strong_Teacher_Not_Needed_On_Distillation_in_LLM_Pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]]

![[assets/2605.23857_first_page.png|800]]

- **arXiv**: [2605.23857](https://arxiv.org/abs/2605.23857)
- **PDF**: https://arxiv.org/pdf/2605.23857
- **详细分析**: [[20_Research/Papers/大模型/Strong_Teacher_Not_Needed_On_Distillation_in_LLM_Pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]]
- **作者**: Taiming Lu, Zhuang Liu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

知识蒸馏常被视为一种“强教师带弱学生”的训练范式，尤其在大模型预训练中，人们通常默认教师模型越强，学生模型收益越大。但这一经验判断是否始终成立，尤其在教师与学生规模差异、训练 token 预算不同的情况下，并没有被系统验证。本文聚焦大语言模型预训练中的蒸馏机制，关注教师强弱与蒸馏收益之间的真实关系，因此具有较强的理论辨析价值和实践参考意义。

#### 方法概述和架构

作者在大语言模型预训练场景下，系统构造了三类教师—学生关系：强教师带弱学生、同等水平师生、以及弱教师带强学生。实验中通过改变模型架构规模与训练 token 预算，控制教师和学生的训练充分程度，从而检验不同设置下知识蒸馏的有效性。训练目标上，将语言建模损失与知识蒸馏损失进行混合，并考察不同混合方式对学生模型学习效果的影响。通过比较不同师生配置的预训练结果，作者分析了蒸馏对拟合训练域、泛化能力以及下游表现的作用差异。

#### 实验结果分析

实验表明，在合适的语言建模损失与蒸馏损失混合策略下，教师模型不一定需要很强；即使是较小、训练不足的教师，也能帮助更大的学生模型获得提升。进一步地，教师并非越强越好：当教师通过增加参数量或训练 token 继续“变强”时，蒸馏收益可能出现饱和，甚至反向下降。作者还观察到，蒸馏更容易提升模型的泛化能力，包括 OOD 表现和下游任务表现，而对训练域内拟合的改善相对不那么直接。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

知识蒸馏通常默认存在一种“强到弱”的关系，即更强的教师会带来更好的学生。在这项工作中，我们在大语言模型预训练中检验了这一假设。通过改变架构规模和训练 token 预算，我们构造了强到弱、同水平以及弱到强的教师—学生关系，并研究蒸馏在这些不同关系下的有效性。我们发现，教师并不一定需要很强：只要对语言建模损失与知识蒸馏损失进行适当混合，即使是较小且训练不足的教师，也能提升更大的学生模型。与此同时，更强的教师也不总是更好：继续通过增加参数量或训练 token 来强化教师，可能会使蒸馏收益饱和，甚至出现反转。我们还进一步观察到，蒸馏更容易改善泛化能力（包括分布外表现和下游任务表现），而不是提升训练域内拟合。综合来看，这些结果挑战了“蒸馏预训练总是需要强教师”这一常见观点。

</details>

---

### [[20_Research/Papers/大模型/ChartFI_Benchmarking_Faithfulness_and_Insightfulness_of_Chart_Descriptions_from_Multimodal_Large_Language_Models|ChartFI: Benchmarking Faithfulness and Insightfulness of Chart Descriptions from Multimodal Large Language Models]]

![[assets/2605.23694_figure.png|800]]

- **arXiv**: [2605.23694](https://arxiv.org/abs/2605.23694)
- **PDF**: https://arxiv.org/pdf/2605.23694
- **详细分析**: [[20_Research/Papers/大模型/ChartFI_Benchmarking_Faithfulness_and_Insightfulness_of_Chart_Descriptions_from_Multimodal_Large_Language_Models|ChartFI: Benchmarking Faithfulness and Insightfulness of Chart Descriptions from Multimodal Large Language Models]]
- **作者**: Fen Wang, Zekai Shao, Qiman Kang, Chunran Hu, Zhixuan Zhang, Lexu Xie, Chao Liu, Siming Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

图表描述是无障碍阅读、跨模态检索以及辅助读者从复杂可视化中提取洞见的重要能力，尤其适用于科学论文、数据报告等场景。随着多模态大模型（MLLMs）被用于自动生成图表描述，核心问题不再只是“能否说出来”，而是“是否忠实于图表、是否真的提供了分析价值”。现有基准主要存在两类不足：一是数据集多为简单、同质化图表，配套描述也往往停留在罗列事实的浅层文本；二是常用评价指标偏重表面文本相似度，难以刻画图表描述在事实准确性、关键信息覆盖和洞见表达上的综合质量。因此，这篇工作值得关注，因为它直接针对图表理解与描述生成中最难也最容易被忽视的评测缺口，尝试建立更贴近真实应用的基准和指标体系。

#### 方法概述和架构

作者提出 ChartFI-Bench（Chart Faithfulness and Insightfulness Benchmark），先从高质量图表描述的特征出发，总结出四个维度：事实准确性、突出关键信息、领域知识引导以及图文互补性。基于这些原则，构建了一个包含896组图表—描述对的基准，数据来自 arXiv，并经过系统筛选和人工核验，强调图表本身的复杂性与文本的语义丰富性。为了对应这四个维度，论文进一步设计了四个评价指标：Faithfulness、Coverage、Informativeness 和 Acuity。其中文本会先被分解为原子级数据事实，并表示为结构化的6元组，以便在不受措辞差异影响的情况下做细粒度比较。Faithfulness 部分通过2×2对比研究评估四种验证策略，最终采用仅依赖图像与描述的直接 MLLM-as-a-Judge 方案；Coverage 通过面向不同洞见类型的匹配规则对参考事实与生成事实进行对齐；Informativeness 则采用随图表复杂度自适应加权的方式衡量语义层级重要性；Acuity 用五个递进子维度评估模型是否有效利用了领域知识。

#### 实验结果分析

作者使用 ChartFI-Bench 对主流 MLLMs 进行评测，包括 GPT-5.4、Gemini-3-Flash、Qwen3.5-Plus、Qwen3.5-27B 和 InternVL3.5-14B，并结合自动评测与人工评测验证所提框架的有效性。实验表明，新的基准和指标能够更系统地揭示现有模型在图表描述中的共性弱点，特别是在事实忠实性、洞见覆盖和领域推理方面。节选文本中没有给出具体数值结果，因此可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

图表描述对于无障碍访问、跨模态检索以及帮助读者从复杂可视化中提取洞见都至关重要。随着多模态大语言模型（MLLMs）越来越多地被用于自动生成图表描述，一个关键问题随之出现：这些模型到底能在多大程度上忠实且富有洞见地描述图表？现有基准在两个方面存在不足：其一，已有数据集通常由简单、同质化的图表组成，并配有浅层、以罗列事实为主的描述；其二，现行指标无法捕捉描述质量的多维特性。为了解决这些问题，我们提出了 Chart Faithfulness and Insightfulness Benchmark（ChartFI-Bench）。我们首先总结出刻画高质量图表描述的四个维度：事实准确性、突出显著特征、领域知识引导，以及图文互补性。基于这些维度，我们构建了一个高质量基准，包含896组图表—描述对，这些样本具有视觉上更复杂的图表和语义上更丰富的描述。此外，我们设计了四个对应的评价指标——Faithfulness、Coverage、Informativeness 和 Acuity，用于系统地评估描述在这些维度上的质量。在主流 MLLMs 上进行的实验表明，所提出框架是有效的，并揭示了现有模型中的常见弱点。

</details>

---

### [[20_Research/Papers/大模型/OpenSkillEval_Automatically_Auditing_the_Open_Skill_Ecosystem_for_LLM_Agents|OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents]]

![[assets/2605.23657_figure.png|800]]

- **arXiv**: [2605.23657](https://arxiv.org/abs/2605.23657)
- **PDF**: https://arxiv.org/pdf/2605.23657
- **详细分析**: [[20_Research/Papers/大模型/OpenSkillEval_Automatically_Auditing_the_Open_Skill_Ecosystem_for_LLM_Agents|OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents]]
- **作者**: Jiahao Ying, Boxian Ai, Wei Tang, Siyuan Liu, Yixin Cao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

随着 LLM Agent 在报告生成、网页设计、数据可视化等真实任务中的应用增多，社区开始把可复用的流程经验整理为“技能（skill）”来增强 Agent 的执行能力。然而，开源技能生态扩张很快，但不同模型与不同 Agent 框架到底能否真正有效利用技能、技能本身质量如何、以及在性能与成本之间该如何选技能，仍缺乏系统评估。本文关注的是一个非常现实的问题：在动态变化的真实应用场景中，技能是否真的能带来稳定收益，而不是只在静态基准上看起来有用。

#### 方法概述和架构

论文提出 OpenSkillEval，一个面向技能增强型 LLM Agent 与技能本身的自动评测框架。框架包含三个核心部分：自动测试用例生成、开源技能收集与组织、以及自动评估流水线。首先，它不依赖静态题库，而是从真实世界不断变化的工件中反向构造任务实例，覆盖演示文稿生成、前端网页设计、海报生成、数据可视化和报告生成五类任务；每个任务同时产出源材料、结构化任务规格和自然语言指令。其次，作者从多个社区仓库汇集技能，并按任务类别筛选出 30 个较高采用度的技能，保证在统一任务设置下进行对比。最后，评测不仅看最终生成结果，还分析 Agent 的轨迹和中间行为，检查模型是否真正调用并遵循技能，从而同时评估“Agent 如何用技能”和“技能是否有用”。

#### 实验结果分析

作者使用 600+ 动态生成任务实例和 30 个开源技能，对多种 SOTA 模型与 Agent 框架进行了系统评测；从节选文本看，可见文本未给出具体数值。结果显示，技能可用并不意味着 Agent 一定会有效使用，很多情况下模型没有在合适阶段调用技能，甚至没有严格遵循技能说明。实验还表明，技能增益强烈依赖底层模型与框架组合：某些较弱模型在合适技能和框架下可接近更强模型，但如果模型本身任务能力不足，单纯增加技能通常难以带来可靠提升。与此同时，许多在社区中较受欢迎的技能并不能稳定超过不使用技能的基线，说明开源技能生态中存在明显的质量参差与冗余问题。

<details>
<summary>完整摘要</summary>

技能，即为大语言模型（LLMs）提炼出的结构化工作流指令，正在成为提升智能体在真实下游任务上性能的重要机制。随着开源技能生态迅速扩张，人们仍不清楚不同模型与智能体框架如何与技能交互、如何评估技能质量，以及在实际的成本—性能权衡下用户应如何选择技能。本文提出 OpenSkillEval，一个面向技能增强型智能体系统以及技能本身的自动化评测框架。不同于依赖静态基准，OpenSkillEval 会自动从不断演化的真实世界工件中构造现实任务实例，覆盖五类下游应用：演示文稿生成、前端网页设计、海报生成、数据可视化和报告生成。它还收集并整理社区贡献的技能，以便在统一任务设置下进行受控比较。基于 600 多个动态生成的任务实例和 30 个开源技能，我们对当前最先进的模型与智能体框架进行了系统评测。结果表明，具备技能并不意味着能够有效使用技能；技能增强带来的收益高度依赖底层模型和智能体框架；而且许多公开热门技能并不能稳定优于不使用技能的基础智能体。这些发现凸显了开展动态、任务驱动评测的必要性，并为技能的设计、选择与部署提供了实用见解。更多案例和基准资源可在项目网站获取：https://yingjiahao14.github.io/OpenSkillEval-Web/。

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_Google_Embeddings_2_against_Open-Source_Models_for_Multilingual_Dense_Retrieval_and_RAG_Systems|Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems]]

![[assets/2605.23618_figure.png|800]]

- **arXiv**: [2605.23618](https://arxiv.org/abs/2605.23618)
- **PDF**: https://arxiv.org/pdf/2605.23618
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_Google_Embeddings_2_against_Open-Source_Models_for_Multilingual_Dense_Retrieval_and_RAG_Systems|Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems]]
- **作者**: Stefano Cirillo, Domenico Desiato, Giuseppe Polese, Giandomenico Solimando
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: cs.CL

#### 研究背景与动机

在检索增强生成（RAG）系统中，检索器是否能把相关证据找准，直接决定后续生成是否可靠，因此嵌入模型的选择不仅影响效果，也影响部署成本与响应延迟。本文聚焦多语言稠密检索与RAG场景，对比 Google Embeddings 2（GE2）与多种主流开源向量模型，特别关注长上下文支持、任务类型条件化、多语言覆盖以及 chunking 策略这些真实部署中常被忽视的因素。作者指出，像 LaBSE 这类原本用于句子对齐的模型常被误用为通用检索器，而这一类“任务目标不匹配”可能带来显著质量损失，因此值得系统评测。

#### 方法概述和架构

论文以 GE2 作为核心对象，将其与 BGE-M3、E5-large、Multilingual-E5-large（mE5-L）、LaBSE 和 Paraphrase-Multilingual-MPNet（mMPNet）进行零样本对比。GE2 是部署在 Vertex AI 上的双编码器，具有 2,048 token 的上下文窗口，并通过显式的任务类型条件化区分检索查询与文档表示。实验流程是：先将文档按不同 chunk 大小和策略切分，再对 chunk 编码建库；查询端编码后用 FAISS 做近邻检索，取回 top-k chunk 并映射回原始文档评估。研究还额外设计了 chunking 消融实验，比较 5 种 token 长度、3 种切分策略，并在 CPU 机器上测量单查询延迟，以观察质量与时延之间的权衡。

#### 实验结果分析

实验覆盖 BEIR 的 4 个子集、一个合成的意大利语 RAG 语料 IT-RAG-Bench，以及 chunking 消融和推理时延测试，指标主要是 nDCG@10。结果显示 GE2 在所有任务上都排名第一，BEIR 平均 nDCG@10 达到 0.638，IT-RAG-Bench 的 nDCG@10 为 0.282，但其延迟明显更高，median latency 为 231.6 ms，约为最快本地模型的 14 倍。mE5-L 在意大利语任务上与 GE2 仅相差 0.003 nDCG，却只需 31 ms，因此在对 SLA 要求较严、需要亚百毫秒响应的场景中更具性价比。作者还发现 LaBSE 在 BEIR 上的平均 nDCG@10 仅为 0.188，低于所有专门为检索设计的模型；chunking 方面，各模型在 32 token 左右已趋于饱和，而语义切分只在 16 token 时带来可测增益。

<details>
<summary>完整摘要</summary>

本文对 Google Embeddings 2（GE2）与五种开源替代方案进行了基准评测，这五种模型分别是 BGE-M3、E5-large、Multilingual-E5-large（mE5-L）、LaBSE 和 Paraphrase-Multilingual-MPNet（mMPNet）。GE2 是一种托管在 Vertex AI 上的双编码器，支持 2,048 token 的上下文长度，并通过显式的任务类型条件化进行控制。评测覆盖了 BEIR 的四个子集、一个合成的意大利语 RAG 语料库、一个 chunking 消融实验（包含 5 种 token 长度和 3 种策略），以及在普通 CPU 硬件上的单查询延迟测试。结果显示，GE2 在所有任务上都取得第一名，在 BEIR 上平均 nDCG@10 达到 0.638，在 IT-RAG-Bench 上 nDCG@10 达到 0.282；但其 median latency 为 231.6 ms，约比最快的本地模型慢 14 倍。mE5-L 在意大利语任务上的表现与 GE2 的差距仅为 0.003 nDCG，同时延迟只有 31 ms，因此在需要低于 100 ms 服务级别目标的场景中是更优选择。一个更值得注意的发现是，LaBSE 虽然被广泛用于多语言部署，但在 BEIR 上的平均 nDCG@10 只有 0.188，低于所有专门用于检索的模型，包括 mMPNet。chunking 实验表明，在本文语料上，六种模型都在 32 token 的 chunk 大小附近达到饱和，而语义切分只在 16 token 时带来可测量的提升。代码和数据集已公开发布。

</details>

---

### [[20_Research/Papers/大模型/Asking_For_An_Old_Friend_Diagnosing_and_Mitigating_Temporal_Failure_Modes_in_LLM-based_Statutory_Question_Answering|Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering]]

![[assets/2605.23497_figure.png|800]]

- **arXiv**: [2605.23497](https://arxiv.org/abs/2605.23497)
- **PDF**: https://arxiv.org/pdf/2605.23497
- **详细分析**: [[20_Research/Papers/大模型/Asking_For_An_Old_Friend_Diagnosing_and_Mitigating_Temporal_Failure_Modes_in_LLM-based_Statutory_Question_Answering|Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering]]
- **作者**: Max Prior, Andreas Schultz, Matthias Grabmair
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

大模型正在被越来越多地用于法律检索与法条问答，但法律条文会随时间修订，而模型参数知识却是静态的，因此很容易出现“知识截止后仍沿用旧法”和“在历史场景下过度偏好新法”这两类时间性错误。本文关注的是德国语境下的成文法问答，尤其是需要根据案件发生时点选择对应法条版本的场景。作者指出，现有法律问答评测很少专门诊断这类时间失配问题，因此可靠的法律问答不能只看语义匹配，还必须把“时间有效性”当作硬约束。

#### 方法概述和架构

论文构建了一个包含312个经专家验证的时间敏感德语成文法问答基准，分为三类：知识截止后修订题、修订前历史题，以及多条款的修订前历史题。数据来源于德国六部法律的历史合并版本，并基于条文修订前后差异合成问答，用于区分模型到底是在“知道当前法”还是“会用历史法”。实验评估了来自 OpenAI、Anthropic 和 DeepSeek 的5个大模型，在4种推理设置下对比：纯模型回答、Web搜索、以及两种带检索增强的方案。两种RAG方案都通过“事实日期抽取”和“版本过滤”来强制只检索在案件时间上有效的法条版本，其中一个思路是先识别题目中的事实日期，再据此筛选可用条文，再由模型生成答案。结果评估使用LLM-as-a-judge，并先通过人工专家打分进行了验证。

#### 实验结果分析

实验显示，在不接入外部检索的Vanilla设置下，模型在知识截止后修订题上性能显著下降，说明静态参数知识面对法条更新非常脆弱。两种RAG方案在所有题型上都带来明显改善，说明只要把时间有效性显式约束进检索流程，就能有效缓解这类错误。相比之下，Web搜索虽然有时能提升结果，但表现不稳定，并且在历史锚定任务上呈现明显的“偏新”倾向。可见文本未给出具体数值，但整体结论很明确：法律问答中，时间过滤比单纯联网更可靠。

<details>
<summary>完整摘要</summary>

大语言模型正越来越多地被用于法律研究，但其固定的训练截止点以及对静态参数知识的依赖，与成文法不断演进的特性并不相容。本文研究两类时间性失效模式：一是知识截止后的陈旧性，即模型在立法修订后仍套用已被废止的规则；二是近因偏置，即即便事实模式应适用历史版本，模型仍偏向更新的法条。为此，我们提出了一个包含312个经专家验证、具有时间敏感性的德国成文法问答基准，覆盖三类任务：知识截止后修订问题、修订前问题，以及多条款修订前问题。我们在四种推理设置下评估了5个来自 OpenAI、Anthropic 和 DeepSeek 的大模型：纯模型回答、Web搜索，以及两种通过事实日期抽取和版本过滤来强制保证时间有效性的检索增强变体。借助经人工专家评分验证的 LLM-as-a-judge，我们发现纯模型在知识截止后场景中性能严重退化；两种RAG方法都能在所有题型上显著提升表现，而Web搜索带来的增益不稳定，并且在历史锚定任务上表现出明显的近因偏置。我们的结果表明，可靠的法律问答必须把时间有效性视为一条硬约束。

</details>

---

### [[20_Research/Papers/大模型/ARES_Automated_Rubric_Synthesis_for_Scalable_LLM_Reinforcement_Learning|ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning]]

![[assets/2605.23454_figure.png|800]]

- **arXiv**: [2605.23454](https://arxiv.org/abs/2605.23454)
- **PDF**: https://arxiv.org/pdf/2605.23454
- **详细分析**: [[20_Research/Papers/大模型/ARES_Automated_Rubric_Synthesis_for_Scalable_LLM_Reinforcement_Learning|ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning]]
- **作者**: Xiaoyuan Li, Keqin Bao, Moxin Li, Yubo Ma, Yichang Zhang, Wenjie Wang, Fuli Feng, Dayiheng Liu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.45，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

大模型强化学习（RL）正在从只适用于“答案可自动验证”的任务，扩展到更开放、更复杂的场景，如医疗问答、指令遵循和长文本生成。但现有 RLVR 主要依赖可直接判定对错的结果奖励，奖励信号往往稀疏且偏二值，难以覆盖开放式任务中“是否完整、是否准确、是否符合要求”等多维目标。基于 rubric 的奖励能够把评估拆解为多个可加权的标准，更适合开放式回答，但传统做法往往需要专家手写 rubric 和人工构造题目，规模化很困难。

#### 方法概述和架构

论文提出 ARES（Automated Rubric synthEsis for Scalable RL），目标是从原始预训练文档自动合成可用于 RL 的 rubric 数据。整体流程分为三步：先对文档进行过滤，去掉低质量、模板化或上下文不足的内容；再结合领域标签与 persona 信息，共同生成自包含问题、参考答案和该问题专属的加权 rubric；最后通过质量控制与验证过滤，检查问题是否自包含、答案是否忠实于原文、rubric 是否有效。方法输出的是三元组（问题、参考答案、rubric），其中 rubric 由若干带权重的正向/负向评价标准组成，训练时用这些标准为每个采样回答计算 reward。论文在 RL 阶段采用 GRPO 作为优化器，把 rubric reward 直接作为每个响应的奖励信号，从而把开放式任务的监督从“结果对错”转成“多维质量评估”。

#### 实验结果分析

作者用 ARES 构建了 10 万条带 rubric 标注的样本，覆盖 10 个领域，并在 7 个基准上评估其效果。对比方法包括 continual pretraining、supervised fine-tuning 以及 binary-reward RL，结果显示 ARES 训练得到的 rubric-based RL 整体表现最好，尤其在医疗和指令遵循等多维开放式任务上优势更明显。文中还提到，在这些任务上提升幅度最大；具体数值方面，摘要给出了医疗任务 +6.4、指令遵循 +15.5 的增益。消融分析表明，结构化 rubric 平均优于整体式判断，问题级 rubric 有助于跨任务鲁棒性，而基于参考答案的评估虽然较强但稳定性较差。

<details>
<summary>完整摘要</summary>

基于 rubric 的奖励提供了一条有前景的路径，使大模型强化学习（RL）能够超越那些答案可自动验证的任务。然而，规模化的 rubric-based RL 仍然面临挑战：现有方法往往依赖专家手工撰写的 rubric 和人工构造的问题集合，而固定的任务级 rubric 可能无法捕捉单个问题的具体评估要求。为此，我们提出 ARES（Automated Rubric synthEsis for Scalable RL），这是一个用于大规模自动构建基于 rubric 的 RL 数据的框架。ARES 从原始预训练文档出发，将源知识转换为自包含的问答对，并同时生成与问题对应的加权 rubric，从而为开放式回答提供实例级奖励监督。为了提升多样性和质量，ARES 在生成过程中引入领域标签和 persona 信息作为条件，并通过验证过滤器检查问题是否自包含、答案是否忠实于原文以及 rubric 是否有效。利用 ARES，我们构建了 10 万条带 rubric 标注的实例，覆盖十个领域。七个基准上的实验表明，使用 ARES 训练的 rubric-based RL 优于 continual pretraining、supervised fine-tuning 和 binary-reward RL，并且在医疗和指令遵循等多维开放式任务上获得了最大的提升。

</details>

---

### [[20_Research/Papers/强化学习/From_Correctness_to_Preference_A_Framework_for_Personalized_Agentic_Reinforcement_Learning|From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning]]

![[assets/2605.23382_figure.png|800]]

- **arXiv**: [2605.23382](https://arxiv.org/abs/2605.23382)
- **PDF**: https://arxiv.org/pdf/2605.23382
- **详细分析**: [[20_Research/Papers/强化学习/From_Correctness_to_Preference_A_Framework_for_Personalized_Agentic_Reinforcement_Learning|From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning]]
- **作者**: Ranxu zhang, zeyang li, Jiacheng Huang, Rui Zhang, Xiaozhou Xu, sun zhe, Yanyong Zhang, Chao Wang
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.45（加权：大模型 0.25，强化学习 1.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

Agentic RL 近年来在代码生成、网页操作、工具调用和长程规划等任务上进展很快，但这些进展大多建立在“答案可验证”的场景中。现实中的很多智能体应用，如电商推荐、旅行规划和日程安排，并不存在唯一正确答案，而是会因不同用户的偏好、习惯和约束而产生不同的最优行为。现有方法要么只优化通用质量奖励，难以表达用户差异；要么只做推理时个性化，缺少训练阶段的原生优化框架，因此这篇工作值得关注。该论文试图把“正确性优化”推进到“偏好对齐”的个性化 Agentic RL。

#### 方法概述和架构

论文提出一个统一的个性化 Agentic RL 框架，核心算法是 PARPO（Personalized Anchor Reward-Decoupled Policy Optimization）。PARPO 将通用任务质量奖励与个性化偏好奖励解耦，并引入用户特定的 anchor 来稳定不同用户奖励尺度不一致时的训练过程，从而以双轨方式更新策略。为提供更干净的个性化监督，作者设计了一个两阶段的偏好解耦奖励模型：先学习多视图用户画像表示，再通过协同解耦把真实兴趣与从众/上下文效应分离开。与此同时，作者提出 PSGM（Preference-Aligned Skill Evolution Graph Memory），把用户、技能、工具、场景和轨迹组织成演化式图记忆，用于偏好对齐的技能检索与积累。整体流程是：根据用户画像和查询先从图记忆中检索相关技能，增强 rollout 上下文；策略生成决策轨迹后，由双奖励系统分别评估通用质量与个性化偏好；随后用 PARPO 更新策略，并把高价值轨迹回灌到记忆中，形成“偏好识别—策略优化—技能沉淀”的闭环。

#### 实验结果分析

作者在 ETAPP、ETAPP-Hard 和 SJAgent 上进行了实验，并与多种强记忆方法和强化学习基线比较。结果表明，所提框架在个性化决策与过程质量上均能稳定优于基线，同时保持事实性与逻辑性；正文节选中未给出具体数值。论文还包含消融实验、Rollout 评测、训练动态与技能演化分析，以及人类和 LLM 评审，说明个性化奖励优化和技能演化模块都对最终性能有贡献。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning（Agentic RL）在具有明确成功信号的任务上取得了很大进展。然而，许多现实世界中的智能体应用需要基于用户条件来决定行为：同一个查询，对于不同用户可能需要不同的规划策略和工具使用决策。这种设置带来了几个关键挑战：通用奖励无法刻画异质的用户偏好，观测到的行为又会与从众效应相互纠缠，而扁平化的记忆结构也无法支持个性化技能检索。为此，我们提出一个统一的个性化 Agentic RL 框架，将个性化嵌入到训练阶段的优化过程中。该框架的核心是 Personalized Anchor Reward-Decoupled Policy Optimization（PARPO），它将通用任务质量奖励与个性化偏好奖励解耦，并使用用户特定的 anchor 在异质奖励尺度下稳定学习。我们还引入了一个两阶段的偏好解耦奖励模型，以及用于个性化监督和偏好对齐技能检索的 Preference-Aligned Skill Evolution Graph Memory（PSGM）。这些组件共同构成了一个偏好识别、策略优化与结构化技能积累的闭环。我们在 ETAPP、ETAPP-Hard 和 SJAgent 上的实验表明，该框架能够持续优于强大的记忆和强化学习基线。代码和数据已包含在补充材料中。

</details>

---

### [[20_Research/Papers/大模型/When_Is_Next-Token_Prediction_Useful_Marginalization,_Ergodicity,_Mixture_Identifiability,_Local_Sufficiency,_RAG,_Tools,_and_Programming|When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming]]

![[assets/2605.23278_first_page.png|800]]

- **arXiv**: [2605.23278](https://arxiv.org/abs/2605.23278)
- **PDF**: https://arxiv.org/pdf/2605.23278
- **详细分析**: [[20_Research/Papers/大模型/When_Is_Next-Token_Prediction_Useful_Marginalization,_Ergodicity,_Mixture_Identifiability,_Local_Sufficiency,_RAG,_Tools,_and_Programming|When Is Next-Token Prediction Useful? Marginalization, Ergodicity, Mixture Identifiability, Local Sufficiency, RAG, Tools, and Programming]]
- **作者**: Francesco Corielli
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent

#### 研究背景与动机

大模型通常被描述为“学习下一个 token 的条件分布”，但这一定义隐含了一个关键前提：训练数据中的文本序列能够代表真实生成过程中的全部相关信息。本文关注的是，当语言生成还受到事实、事件、意图、任务约束、社会语境等非文本因素影响时，单纯做 next-token prediction 到底在什么条件下才真正“有用”。作者指出，现有大模型训练往往把真实条件分布、边缘化后的文本分布以及模型从有限语料中学到的预测分布混为一谈，这会导致我们对模型能力的理解过于乐观或过于简化。

#### 方法概述和架构

论文不是提出一个新的训练架构，而是给出一个概念与信息论分析框架，用来区分三类对象：带有潜变量条件的完整语言过程、对潜变量积分后的文本边缘条件分布，以及模型参数化后得到的预测分布。作者首先分析标准 next-token 训练实际观察到的是“已实现的续写 token”，而不是完整条件概率；随后讨论若要把经验语料解释为边缘分布估计，必须满足类似平稳性、代表性、遍历性和支持覆盖的假设。接着，论文提出“有用性”判据：观察到的文本前缀必须对后续 token 所依赖的潜在情境近似充分，即给定文本后，遗漏情境对下一个 token 的条件互信息应足够小。最后，作者把这一框架推广到混合训练语料中的局部机制，并将 RAG 与工具调用解释为“条件充分性装置”——通过检索或外部工具把原本隐含的非文本状态文本化或外部化，从而提高后续预测的可用性。

#### 实验结果分析

由于这篇工作是理论分析型论文，正文节选中没有给出具体实验数值，且可见文本未给出具体数值。论文的核心结论是：next-token prediction 并不天然等同于学习真实语言规律，只有在语料近似平稳、可代表、可遍历，且文本前缀对相关潜在因素近似充分时，这种学习才具有实际用处。作者进一步指出，在异质语料上，即使模型学到了某个正确的混合边缘分布，也未必在具体任务中有认识论上的可用性；而编程、RAG 与工具使用之所以更适合这套框架，是因为这些场景更容易把关键上下文显式写入或通过外部接口获取。

<details>
<summary>完整摘要</summary>

在观察到的序列上训练语言模型时，人们常把它们描述为学习“给定前文时下一个 token 的条件分布”。这种说法只有在特定条件下才是正确的。一个基于已实现 token 轨迹训练的模型并不会直接观察到完整的条件定律；它接收到的是采样得到的续写结果。此外，真实的语言生成不仅由前面的词语决定，还受到非文本情境的影响：事实、事件、意图、目标、信念、社会语境以及任务特定约束等。本文区分了三个经常被混淆的对象：其一是由潜在情境条件化后的完整条件语言过程；其二是把这些情境积分消去后得到的边缘文本过程；其三是由有限观测语料学习到的模型诱导分布。本文论证，要把模型训练理解为对边缘文本定律的估计，需要满足平稳性、代表性和遍历性等强假设，而这些假设在异质语言语料上应用时往往并不理想。即便这些假设成立，边缘文本定律只有在观测到的前缀对与续写相关的潜在情境近似充分时才有用。用信息论术语来说，这要求在给定已观测文本后，下一 token 与被省略情境之间的残余条件互信息足够小。随后，本文把这一论证扩展到异质训练语料。最后，本文将检索增强生成（RAG）和工具使用解释为条件充分性装置。

</details>

---

### [[20_Research/Papers/大模型/CultivAgents_Cultivating_Relationship-Centered_Multi-Agent_Systems_for_Personalized_Gardening|CultivAgents: Cultivating Relationship-Centered Multi-Agent Systems for Personalized Gardening]]

![[assets/2605.23193_figure.png|800]]

- **arXiv**: [2605.23193](https://arxiv.org/abs/2605.23193)
- **PDF**: https://arxiv.org/pdf/2605.23193
- **详细分析**: [[20_Research/Papers/大模型/CultivAgents_Cultivating_Relationship-Centered_Multi-Agent_Systems_for_Personalized_Gardening|CultivAgents: Cultivating Relationship-Centered Multi-Agent Systems for Personalized Gardening]]
- **作者**: Yiyang Wang, Moeiini Reilly, Britney Johnson, Kefei Yan, Alex Cabral, Josiah Hester
- **cs 子类**: cs.CL, cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

园艺不仅关系到日常生活品质，也与身心健康、文化传承和食物自主密切相关，但现有数字化园艺工具往往只给出通用建议，难以同时考虑用户的园艺经验、所在地生态、季节变化以及文化语境。对于新手、异地迁移人群或社区园丁而言，这类“脱离情境”的建议容易导致操作无效、作物失败，甚至影响对AI建议的信任。该工作值得关注之处在于，它把大模型从“单轮问答式植物助手”推进到更强调关系、关怀与在地性的多智能体系统。

#### 方法概述和架构

论文提出 CultivAgents，一个面向个性化园艺支持的关系中心型多智能体系统，基于关怀伦理来组织不同来源的知识与建议。系统在用户进入时收集园艺经验、地理位置、当前月份和文化背景，并将这些信息注入到各个智能体的提示词中。核心由三个专门智能体组成：Experience Agent 根据用户熟练度调整建议的深度和表达方式；Environmental Agent 结合本地气候、季节、土壤和霜冻日期等信息提供在地化指导；Ethnobotanical Agent 补充植物的文化历史、传统用途和民族植物学知识。推理时，系统通过一个基于 LLM 的选择器在多个智能体之间轮流调度，每轮最多生成 3 条消息，以保证观点互补并控制上下文长度。前端采用网页聊天界面，后端通过 FastAPI/WebSocket 与 AutoGen AgentChat 流式交互，支持对话导出。

#### 实验结果分析

作者采用三阶段混合方法研究，对 3 位领域专家、7 位 HCI 研究者和 5 位社区园丁进行了评估，包括专家反馈、前后测问卷和参与式设计活动。结果表明，CultivAgents 能帮助园丁把兴趣转化为更具体、可执行的行动；社区园丁的信心、动机以及对AI建议的行动信任均有所提升。参与者尤其认可“超本地化”的生态建议和多个智能体提供的互补视角，但也指出文化细节、生态落地和智能体协同方面仍有局限。可见文本未给出具体基线对比数值与消融结果。

<details>
<summary>完整摘要</summary>

园艺对于支持身心健康、文化延续和食物自主至关重要，但现有数字工具通常只提供通用建议，忽视了园丁的技能水平、当地生态、季节变化以及文化语境。为此，我们提出 CultivAgents，这是一个关系中心型的多智能体系统，旨在提供个性化、具有社会文化基础的园艺支持。CultivAgents 以关怀伦理为基础，协调多个专门智能体：Experience Agent 会根据用户技能水平调整指导内容，Environmental Agent 会依据本地与季节条件来锚定建议，Ethnobotanical Agent 则将植物与文化知识和历史联系起来。我们通过三阶段混合方法研究对 CultivAgents 进行了评估，参与者包括领域专家（n=3）、HCI 研究者（n=7）和社区园丁（n=5），并分析了专家反馈、前后测问卷以及参与式设计活动。结果表明，CultivAgents 帮助园丁将兴趣转化为在地化行动：社区园丁报告其信心从 3.00 提升到 3.60，动机从 4.00 提升到 4.40，对依据AI建议采取行动的信任从 3.20 提升到 4.00。参与者认可超本地化的生态指导以及多个智能体提供的互补视角，但同时也指出系统在文化特异性、生态锚定和智能体协调方面仍存在局限。该研究推进了关系中心型AI的发展，并为支持食物主权、社区韧性与文化保存的多智能体系统提供了设计启示。

</details>

---

### [[20_Research/Papers/大模型/Robust_LLM_Watermarking_with_Minimal_Semantic_Distortion_for_IP_Protection|Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection]]

![[assets/2605.23175_first_page.png|800]]

- **arXiv**: [2605.23175](https://arxiv.org/abs/2605.23175)
- **PDF**: https://arxiv.org/pdf/2605.23175
- **详细分析**: [[20_Research/Papers/大模型/Robust_LLM_Watermarking_with_Minimal_Semantic_Distortion_for_IP_Protection|Robust LLM Watermarking with Minimal Semantic Distortion for IP Protection]]
- **作者**: Kieu Dang, Phung Lai, NhatHai Phan, Yelong Shen, Ruoming Jin
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

大模型厂商面临模型被“蒸馏式复制”的风险：攻击者通过收集输入输出对，训练出功能相近的替代模型，从而造成知识产权与商业利益损失。水印技术因此成为重要防护手段，但现有方法往往会带来语义偏移、事实不一致，且在面对对抗攻击时鲁棒性不足。另一方面，面向特定提供方的、可按密钥区分的水印方法，尤其是在跨提供方和多用户场景中的研究仍然不充分。这篇工作值得关注之处在于，它试图同时兼顾可检测性、文本可用性与鲁棒性，并进一步考虑真实部署中的提供方身份验证需求。

#### 方法概述和架构

作者提出了 SAFESEAL，这是一种密钥条件化的水印框架，用于在生成文本时嵌入可验证的水印信号。其核心生成机制是一个密钥条件化的 Tournament 采样：系统尽量保留命名实体，同时将普通语言词替换为与上下文相符的同义词，以减少语义扰动并维持事实一致性。检测端则设计了一个密钥条件化的对比式检测器，将文本与密钥共同编码，从而实现提供方特定的水印识别。整体流程上，生成阶段负责在不明显损伤文本质量的前提下嵌入水印，检测阶段负责在给定密钥条件下判断文本是否带有对应水印。作者还从理论上推导了效用与可检测性之间的权衡界限，并通过轻量模型、批处理与并行化来降低检测延迟。

#### 实验结果分析

实验表明，SAFESEAL 在文本质量、可检测性和鲁棒性三方面都优于现有基线，并且检测延迟可与最快的基线相当。论文报告的关键指标包括 BERTScore 0.983、entity similarity 0.963、检测率 98.2%，同时在人类评测中的文本质量与内容保真度也取得了最高评价。作者还发布了首个公开的水印排行榜和交互式演示，以促进透明比较与社区协作。由于正文节选未提供更完整的实验设置细节，这里无法进一步补充具体数据集或消融结果。

<details>
<summary>完整摘要</summary>

专有大语言模型（LLM）面临知识产权被侵犯的风险：对手可以通过收集输入输出对来复制一个LLM，并据此训练替代模型，从而造成经济损失。水印是一种有前景的防御手段，可用于验证模型所有权，但现有方法通常难以避免语义扭曲、事实不一致以及对抗攻击。此外，面向提供方特定检测的密钥条件化水印，尤其是在跨提供方和多用户场景中，仍然缺乏充分研究。为了解决这些挑战，我们提出 SAFESEAL，这是一种新的密钥条件化水印框架，能够在几乎不影响模型效用的前提下实现很强的可检测性，从而在可检测性、效用和鲁棒性之间取得平衡。SAFESEAL 通过一个密钥条件化的 Tournament 采样机制保留命名实体，同时用上下文感知的同义词替换语言词项，从而保持语义一致性和事实一致性。在检测方面，我们引入了一个密钥条件化的对比式检测器，它将文本与密钥联合编码，从而支持提供方特定且鲁棒的水印验证。我们推导了效用-可检测性权衡的理论界限，并通过轻量模型、批处理和并行化显著降低了延迟。大量实验表明，SAFESEAL 在效用、可检测性和鲁棒性方面都优于基线方法，BERTScore 达到 0.983，实体相似度达到 0.963，检测率达到 98.2%，并在人类评分中的文本质量和内容保真度上获得最高评价，其延迟与最快的基线相当。为促进透明度和社区驱动的进展，我们发布了首个公开的水印排行榜和一个交互式演示。

</details>

---

### [[20_Research/Papers/具身智能/Fast-dDrive_Efficient_Block-Diffusion_VLM_for_Autonomous_Driving|Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving]]

![[assets/2605.23163_figure.png|800]]

- **arXiv**: [2605.23163](https://arxiv.org/abs/2605.23163)
- **PDF**: https://arxiv.org/pdf/2605.23163
- **详细分析**: [[20_Research/Papers/具身智能/Fast-dDrive_Efficient_Block-Diffusion_VLM_for_Autonomous_Driving|Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving]]
- **作者**: Kewei Zhang, Jin Wang, Sensen Gao, Chengyue Wu, Yulong Cao, Songyang Han, Boris Ivanovic, Langechuan Liu, Marco Pavone, Song Han, Daquan Zhou, Enze Xie
- **cs 子类**: cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.15（加权：具身智能 0.6，大模型 0.55）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

端到端自动驾驶中的 Vision-Language-Action（VLA）模型，需要同时输出高质量轨迹规划和足够快的推理速度，才能在车端实时部署。现有自回归（AR）VLA 虽然结构清晰，但在 batch size=1 的边缘硬件上容易受内存带宽限制，且存在曝光偏差导致的轨迹误差累积；而全序列扩散式方法虽然具备全局上下文建模能力，却难以复用 KV-cache，并可能出现“逻辑泄漏”，破坏先感知后规划的因果顺序。因此，如何在保持规划精度的同时显著提升推理效率，是这篇工作关注的核心问题。

#### 方法概述和架构

论文提出 Fast-dDrive，一种面向自动驾驶的 block-diffusion VLM/VLA 框架，将输出按语义单元切分为多个 section，并在 section 内进行双向细化、在 section 之间保持严格因果顺序。作者观察到自动驾驶模型的输出通常是结构化的 JSON 风格结果，因此将固定的结构化符号（如键名和语法）冻结为 scaffold，只对真正需要预测的 value tokens 进行去噪与生成。训练阶段采用 section-aware 的方案，把安全关键部分的学习权重提高，并结合分段对齐的 block 设计与噪声调度，使模型在结构正确性和驾驶决策上更稳健。推理阶段，Fast-dDrive 进一步使用 Scaffold Speculative Decoding，让 scaffold token 直接自动接受，再用 AR verifier 验证扩散草稿，从而在接近 AR 质量的前提下提升吞吐；此外还提出共享前缀的多轨迹采样，在只解码一次确定性前缀的基础上，针对轨迹段分叉多个随机 rollouts 并做平均，以较低额外成本降低预测方差。

#### 实验结果分析

实验在 WOD-E2E 和 nuScenes 上验证了方法有效性，并与 AR 基线和全序列扩散式 VLA 进行对比。结果显示，Fast-dDrive 在 WOD-E2E 测试集上取得了 ADE@3s 和 ADE@5s 的 SOTA，同时在扩散式 VLA 中获得最高 RFS；在 nuScenes 上将平均 L2 误差降至 0.32m，较前方法提升约 22%。效率方面，与 SGLang 结合后，该框架相较 AR 基线实现了 12× 吞吐提升，说明其更接近真实车载实时部署需求。

<details>
<summary>完整摘要</summary>

端到端自动驾驶中的 Vision-Language-Action（VLA）模型，需要在高保真轨迹规划和高效推理之间取得微妙平衡。现有范式通常难以兼顾两者：自回归（AR）VLA 在边缘硬件上受内存带宽限制，且容易受到曝光偏差漂移影响；而全序列扩散模型无法复用 KV-cache，并且会出现“逻辑泄漏”，违背先感知后规划的因果关系。我们提出 Fast-dDrive，一种 block-diffusion VLA，它在语义单元内部进行双向细化，同时在单元之间强制严格的因果顺序。基于自动驾驶 VLA 往往输出结构化 JSON 风格结果这一观察，Fast-dDrive 将结构化 token 冻结为一个 section scaffold，并采用面向 section 的训练策略，优先强化安全关键的规划部分。我们进一步提出 Scaffold Speculative Decoding，以显著更高的吞吐实现与 AR 等价的输出质量。最后，我们提出一种低开销的测试时扩展方案：从单个共享前缀的 KV cache 中分叉出 N 个随机轨迹 rollout 并对其平均，从而以极低的额外计算成本有效抑制预测方差。实验结果表明，Fast-dDrive 重新定义了驾驶智能体的速度-精度边界。在 WOD-E2E 测试集上，Fast-dDrive 同时取得了 SOTA 的 ADE@3s 和 ADE@5s，并且在扩散式 VLA 中获得最高 RFS；在 nuScenes 上，其平均 L2 误差降至 0.32m，提升了 22%。当与 SGLang 集成时，我们的方法相较 AR 基线实现了 12× 的吞吐加速，缩小了高容量 VLA 与车载实时部署效率需求之间的差距。

</details>

---

### [[20_Research/Papers/大模型/Same_Model,_Different_Weakness_How_Language_and_Modality_Reshape_the_Jailbreak_Attack_Surface_in_Frontier_MLLMs|Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs]]

![[assets/2605.23157_figure.png|800]]

- **arXiv**: [2605.23157](https://arxiv.org/abs/2605.23157)
- **PDF**: https://arxiv.org/pdf/2605.23157
- **详细分析**: [[20_Research/Papers/大模型/Same_Model,_Different_Weakness_How_Language_and_Modality_Reshape_the_Jailbreak_Attack_Surface_in_Frontier_MLLMs|Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs]]
- **作者**: Casey Ford, Madison Van Doren, Sicheng Jin, Emily Dix
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal, Security

#### 研究背景与动机

多模态大模型（MLLM）在全球部署时，安全性不仅取决于模型本身，还会受到输入语言和模态的共同影响。现有红队评测往往默认英文条件下的脆弱性可以外推到其他语言，但这篇工作指出，语言切换会改变 jailbreak 的攻击面，甚至让不同攻击手法的有效性发生方向相反的变化。该问题对跨语言产品安全、统一安全基准和模型排序都很关键，因此值得关注。

#### 方法概述和架构

本文首次系统比较了 US English（en-US）与 Mexican Spanish（es-MX）下，四个前沿 MLLMs——Claude Sonnet 4.5、GPT-5、Pixtral Large 和 Qwen Omni——的 jailbreak 脆弱性。作者使用同一套 363 个多样化对抗提示场景，在纯文本与多模态两种条件下分别施测，构成四种输入组合：英文文本、英文多模态、西语文本、西语多模态。所有英文提示被人工翻译为墨西哥西班牙语，并保持攻击意图一致；模型输出由两组母语标注者分别评估，每组 9 人，共收集 52,272 条伤害评分与二元攻击成功判定。分析上采用 Bayesian mixed-effects model，同时显式建模提示项与标注者的随机效应，以区分语言、模态及其交互带来的真实差异。

#### 实验结果分析

实验在 363 个对抗场景、四个模型、两种语言和两种模态上展开，指标包括 harm rating 与 ASR（attack success rate）。结果显示，语言不会均匀放大脆弱性：在西班牙语提示下，角色扮演、策略性包装等语言型攻击明显变弱，而视觉上更明确的多模态攻击反而更强；这说明语言侧与视觉侧的对齐失败机制并不相同。模型安全排序在不同语言间并不保持一致，Qwen Omni 在 es-MX 参与者中超过 Pixtral Large，发生了英文条件下难以通过简单分数校正恢复的名次翻转；同时，虽然绝对攻击成功率随模型代际有所下降，但模型之间的差距并未缩小。可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

多模态大语言模型（MLLM）的攻击面在不同语言下并不相同，这种差异揭示了对齐失败的机械结构。我们开展了首个系统性的跨语言、多模态红队研究，对四个前沿 MLLMs——Claude Sonnet 4.5、GPT-5、Pixtral Large 和 Qwen Omni——在 US English（en-US）与 Mexican Spanish（es-MX）中的 jailbreak 脆弱性进行比较。我们使用一套固定的对抗基准，共包含 363 个多样化提示场景，并分别在纯文本和多模态条件下施测；由每种语言组中 9 名母语者组成的匹配标注小组，累计收集了 52,272 条伤害评分与二元攻击成功判断。我们的核心发现是：语言不会以统一方式放大脆弱性。贝叶斯混合效应分析表明，角色扮演等语言性框架攻击在西班牙语提示下会显著失效，而视觉上更明确的多模态攻击则会更有效，这直接指向提示语言接口，而非整体标注宽松度。该分化说明，语言对齐失败与视觉对齐失败由不同机制驱动，而切换语言足以把这种分离暴露出来。其实际后果是，安全性排序并不能跨语言保持一致。在 es-MX 参与者中，Qwen Omni 超过 Pixtral Large，成为最脆弱的模型；这种名次翻转无法通过对英文条件得分做任何标量校正来恢复。与此同时，尽管各模型代际的绝对攻击成功率有所下降，模型之间的差距并未缩小。以上结果表明，将语言与模态视为彼此独立维度的安全评测框架，根本上误设了全球部署 MLLMs 的攻击面，因此必须重新设计。

</details>

---

### [[20_Research/Papers/大模型/When_Symptoms_Are_Not_Enough_Evidence-Weighting_Patterns_in_Large_Language_Model_Psychiatric_Screening|When Symptoms Are Not Enough: Evidence-Weighting Patterns in Large Language Model Psychiatric Screening]]

![[assets/2605.23148_first_page.png|800]]

- **arXiv**: [2605.23148](https://arxiv.org/abs/2605.23148)
- **PDF**: https://arxiv.org/pdf/2605.23148
- **详细分析**: [[20_Research/Papers/大模型/When_Symptoms_Are_Not_Enough_Evidence-Weighting_Patterns_in_Large_Language_Model_Psychiatric_Screening|When Symptoms Are Not Enough: Evidence-Weighting Patterns in Large Language Model Psychiatric Screening]]
- **作者**: Jianfeng Zhu, Megan Korhummel, Ruoming Jin, Karin G. Coifman
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

随着心理健康服务需求超过临床评估供给，如何用可扩展、低成本的方式做精神障碍筛查成为现实问题。大型语言模型有望从患者叙述中识别心理风险，但其在不同诊断、不同人口子群以及不同证据使用方式上的稳定性仍不清楚。尤其值得关注的是，模型可能并不是“看不见症状”，而是会在症状、功能受损和保护性背景线索之间做出不一致的权重分配，从而影响筛查可靠性。

#### 方法概述和架构

论文构建了一个以 SCID 为锚点的基准数据集，包含555段半结构化的经历访谈，并配有诊断参考标签，覆盖焦虑障碍、重度抑郁障碍、创伤后应激障碍以及“当前存在任意心理健康障碍”四个任务。研究采用 zero-shot 的任务定制提示，对5个当前较强的 LLM 进行精神科筛查评估，不进行专门微调。模型输入为患者叙述文本，输出为相应诊断任务的阳性或阴性判断，并据此计算分类性能。作者进一步分析误判样本，检验假阴性是否源于遗漏症状证据，还是由于模型更看重功能保持、应对能力和社会支持等保护性线索。通过对比这些线索在输出中的作用方向，研究揭示模型证据整合的偏置模式。

#### 实验结果分析

实验表明，不同任务与不同模型之间性能差异明显，准确率介于0.49到0.86之间，MCC 介于0.16到0.38之间。GPT-4.1 Mini 和 GPT-5 Mini 在各具体障碍任务上表现最稳定。分组分析显示，抑郁分类在男性样本上的准确率高于女性样本；年龄未呈现一致规律；不同种族分层之间仅观察到轻微且不完全一致的波动。证据分析还发现，焦虑和 PTSD 的假阴性中经常存在明确症状，但模型会因“功能仍保留”“能够应对”或“有社会支持”等信息而倾向于给出阴性；相反，功能受损证据会推动模型转向阳性，保护性背景证据则会把输出拉回阴性。

<details>
<summary>完整摘要</summary>

随着临床医生主导的评估需求赶不上心理健康服务的需求，具有可扩展性的筛查工具变得越来越必要。大型语言模型（LLM）可能能够从患者叙述中识别精神科风险，但它们在不同诊断、人口子群以及证据使用模式上的可靠性仍不明确。我们提出了一个以 SCID 为锚点的基准，包含555段半结构化经历访谈，并配有焦虑障碍、重度抑郁障碍、创伤后应激障碍以及当前是否存在任意心理健康障碍的诊断参考标签。采用 zero-shot 的任务特定提示后，我们评估了5个最先进的 LLM，并考察假阴性错误是否反映了对精神科证据的遗漏，或是对症状、功能受损与保护性背景线索的差异化加权。不同任务和模型的表现存在差异，准确率范围为0.49到0.86，Matthews correlation coefficient 范围为0.16到0.38。GPT-4.1 Mini 和 GPT-5 Mini 在各具体障碍任务上表现出最一致的准确性。子群分析发现，男性参与者的抑郁分类准确率高于女性参与者；年龄相关模式没有一致结论；在种族分层上仅存在轻微且不均匀的变化。证据整合分析表明，焦虑和 PTSD 的假阴性分类中，往往包含明确的症状证据，但同时伴随功能保持、应对能力或社会支持等信息。功能受损证据会将模型输出推向阳性分类，而保护性背景证据会将其推向阴性。上述发现表明，LLM 可能支持可扩展的精神科筛查，但在临床部署前，需要谨慎验证其在面对“症状存在但功能尚可或背景具保护性”时倾向于低估症状证据的问题。

</details>

---

### [[20_Research/Papers/大模型/The_Efficiency_Frontier_A_Unified_Framework_for_Cost-Performance_Optimization_in_LLM_Context_Management|The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management]]

![[assets/2605.23071_figure.png|800]]

- **arXiv**: [2605.23071](https://arxiv.org/abs/2605.23071)
- **PDF**: https://arxiv.org/pdf/2605.23071
- **详细分析**: [[20_Research/Papers/大模型/The_Efficiency_Frontier_A_Unified_Framework_for_Cost-Performance_Optimization_in_LLM_Context_Management|The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management]]
- **作者**: Binqi Shen, Lier Jin, Hanyu Cai, Lan Hu, Yuting Xin
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

大模型在问答、检索和知识工作中越来越依赖长上下文，但上下文窗口变长会显著抬高推理算力、延迟和金钱成本，而且带来的性能增益往往并不线性。现有的检索、摘要和记忆压缩等上下文裁剪方法，通常分别看效果和效率，缺少一个能直接指导部署取舍的统一评估方式。本文之所以值得关注，是因为它把“选哪种上下文管理策略”明确建模为一个面向部署的成本—性能优化问题，更贴近真实系统落地。

#### 方法概述和架构

论文提出 The Efficiency Frontier，用于统一评估大模型上下文管理中的成本与性能权衡。其核心是一个三阶段决策流程：先在单一策略内部枚举不同配置（如检索深度、压缩比例），筛掉被支配的点；再把保留下来的候选方案放到统一的成本模型下比较；最后在全局层面寻找使效率得分最高的策略与配置。方法中显式区分了两类成本：阶段一的预处理成本和阶段二的每次查询推理成本，并用复用次数 N 将预处理成本摊销到多次请求中，从而刻画缓存、共享记忆等真实部署场景。效率得分由 F1 和 token 成本共同决定，其中性能项与对数形式的成本惩罚按权重 w 组合，w 越大越偏向准确率，w 越小越偏向低成本。输出结果不仅是最优策略，还包括不同偏好区间下的策略切换边界，以及目标性能对应的最小可达成本。

#### 实验结果分析

作者在 HotpotQA 的 5,000 个样本上验证了该框架，并比较了全上下文提示、Oracle Retrieval、记忆压缩，以及 TF-IDF、语义检索等检索式方法。结果显示，不同策略在不同部署条件下存在清晰的运作区间和切换边界，说明“哪种方法更好”高度依赖于是否能复用预处理以及系统对性能/成本的偏好。总体上，部署感知优化在保持相近性能（F1 约 0.78）时，可将有效 token 使用量降低约 25%；在更强调高性能的设置下，摊销后的记忆压缩相比全上下文提示可减少超过 50% 的 token 成本。可见文本未给出更细的消融或泛化数值。

<details>
<summary>完整摘要</summary>

大型语言模型（LLM）越来越依赖长上下文处理，但扩展上下文窗口会带来显著的计算和资金成本。现有的上下文压缩方法，包括检索和记忆压缩方法，通常分别用性能指标和效率指标进行评估，这限制了系统性的比较以及面向部署的决策制定。本文提出 The Efficiency Frontier，这是一个用于 LLM 上下文管理中成本—性能优化的统一框架。该框架将上下文策略选择建模为一个面向部署的优化问题，联合考虑任务性能、token 成本以及通过摊销成本建模得到的预处理复用。与以往将方法孤立比较的评估方式不同，该框架能够在不同运行条件下，分析何时不同的上下文管理策略更具优势，从而支持面向决策的判断。基于 5,000 个 HotpotQA 样本的评估表明，该框架揭示了检索式策略与预处理式策略之间清晰的运行区间和切换边界。结果显示，在相近性能（F1≈0.78）下，部署感知优化可将有效 token 使用量降低约 25%；而在更高性能设定下，摊销后的记忆压缩相较于全上下文提示可将 token 成本降低 50% 以上。总体而言，该框架为评估和部署可扩展、高效率、可持续的大模型系统提供了原则性且实用的基础。

</details>

---

### [[20_Research/Papers/大模型/What_Training_Data_Teaches_RL_Memory_Agents_An_Empirical_Study_of_Curriculum_Effects_in_Memory-Augmented_QA|What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA]]

![[assets/2605.23067_figure.png|800]]

- **arXiv**: [2605.23067](https://arxiv.org/abs/2605.23067)
- **PDF**: https://arxiv.org/pdf/2605.23067
- **详细分析**: [[20_Research/Papers/大模型/What_Training_Data_Teaches_RL_Memory_Agents_An_Empirical_Study_of_Curriculum_Effects_in_Memory-Augmented_QA|What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA]]
- **作者**: Xinjie He, Zhiyuan Lin, Su Liu, Jialun Wu, Qiyang Xie, Weikai Zhou, Shuai Xiao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.95（加权：大模型 0.75，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

这篇论文关注的是“带外部记忆的多轮问答”中的强化学习训练问题，场景主要来自多轮对话系统需要跨会话记住用户偏好、事件和关系。以往工作通常只在单一基准上训练并报告总分，但记忆增强问答本身包含检索、跨记忆推理、时间顺序判断和知识更新等多种能力，单一数据源可能会把强化学习信号偏向某些技能。作者因此想回答一个关键问题：训练数据的组成，究竟是在“提升整体能力”，还是在“塑造模型会哪些具体技能”。

#### 方法概述和架构

论文以 Qwen-2.5-7B-Instruct 为底座，使用 LoRA 做参数高效微调，并采用 GRPO 进行强化学习训练。核心自变量不是模型结构或算法，而是训练课程（curriculum）来源：A 只用 LoCoMo，B 混合 LoCoMo 与 LongMemEval，C 只用 LongMemEval，其余超参数、训练流程和推理设置全部固定。输入是多会话对话历史和问题，先通过相似度检索从记忆库中取出 top-k 记忆条目，再由模型生成结构化输出，包含 selected_memories、reasoning 和 answer 三部分。训练时用 token-level F1 作为主要奖励，并加入少量格式奖励；作者还分析了在单卡、小组大小 G=4 的 GRPO 设定下，二元完全匹配奖励几乎不给出学习信号，因此需要连续型奖励。推理阶段则在构建记忆库时过滤短无效轮次，对 LongMemEval 这类聊天格式数据还会去掉过长的助手回复，以降低格式噪声并提升检索质量。

#### 实验结果分析

实验在 LoCoMo 和 LongMemEval 两个基准上进行，评价指标是 token-level F1，并辅以 LLM-as-Judge 作为兼容性检查。总体上，混合课程 B 在两个测试集上的 F1 都最好，说明把两个数据源混合训练更有利于获得更强的泛化表现；但提升幅度不大，节选中可见文本未给出更多消融数值。更重要的是，按题型拆分后，不同课程带来的差异明显大于总体分数差异，说明单一总分会掩盖课程效应。作者还发现，较窄的外域训练虽然整体弱，但能针对性迁移某些技能，尤其是 temporal reasoning；同时，混合跨基准训练时需要清理记忆库中的格式噪声，而二元奖励在单卡小组规模下几乎无法学习。

<details>
<summary>完整摘要</summary>

强化学习（RL）已经成为训练大语言模型（LLM）智能体在多轮会话中推理外部记忆库的一种可行方案。现有工作几乎都只在单一基准上训练，因此仍不清楚训练数据的组成会如何塑造记忆智能体获得的能力。本文开展了一项受控的实证研究：保持模型架构、RL 算法以及所有超参数完全不变，只改变训练课程，设置为三种条件：域内训练（LoCoMo）、混合基准训练（LoCoMo + LongMemEval）以及域外训练（仅 LongMemEval）。在两个基准和十种问题类型上，课程组成起到的更像是对模型“专长”的细粒度调节作用，而不是对性能的统一放大。混合课程在两个评测集上都取得了最强的整体 F1。仅用一个较窄的域外数据集训练，虽然总体表现较弱，却迁移出了一个有针对性的技能——时间推理。并且，按题型拆分后的差异远大于总体差异，说明只看单一数值的基准比较会系统性低估课程效应。我们还报告了将 GRPO 适配到单卡训练时的两个实践经验：跨基准混合训练需要过滤记忆库中与格式相关的噪声，以保留训练信号；在单卡所需的小组规模（G=4）下，二元完全匹配奖励不会产生学习信号，因此在这种设定下更适合使用连续型奖励函数。

</details>

---

### [[20_Research/Papers/大模型/ModeSwitch-LLM_A_Lightweight_Phase-Aware_Controller_for_Cross-Mode_LLM_Inference_on_a_Single_GPU|ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU]]

![[assets/2605.23057_figure.jpeg|800]]

- **arXiv**: [2605.23057](https://arxiv.org/abs/2605.23057)
- **PDF**: https://arxiv.org/pdf/2605.23057
- **详细分析**: [[20_Research/Papers/大模型/ModeSwitch-LLM_A_Lightweight_Phase-Aware_Controller_for_Cross-Mode_LLM_Inference_on_a_Single_GPU|ModeSwitch-LLM: A Lightweight Phase-Aware Controller for Cross-Mode LLM Inference on a Single GPU]]
- **作者**: Aman Sunesh, Ali Alshehhi, Hivansh Dhakne
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

大模型在单卡部署时，推理效率往往比模型能力更先成为瓶颈：不同请求在提示长度、生成长度、共享前缀、批量压力和显存压力上的差异很大，而固定的推理配置很难同时兼顾低延迟、低能耗和质量。现有系统通常把 FP16、量化、speculative decoding、prefix caching、continuous batching 等优化当作全局配置统一使用，但这会导致某些请求受益、另一些请求反而受损。ModeSwitch-LLM 关注的正是“按请求选择推理模式”这一实际部署问题，试图用很低的路由开销从已有推理优化中重新挖掘效率。

#### 方法概述和架构

作者提出 ModeSwitch-LLM，一种轻量级、请求边界感知的控制器，在每个请求开始生成前，根据廉价的工作负载特征选择一种固定推理模式。系统输入包括提示词长度、预期输出长度、共享前缀状态、批量压力、显存压力以及任务标签，输出则是在 FP16、INT8、GPTQ 4-bit、speculative decoding、GPTQ+prefix caching、INT8+continuous batching 等模式中的一个。整体流程分为特征抽取、轻量分类和模式路由三步：先根据请求属性判断其更偏向批量、共享前缀、prefill-heavy 还是 decode-heavy，再按规则映射到最合适的模式。作者同时训练了 decision tree、random forest 和 logistic regression 等学习型路由器，去模仿一个满足质量、能耗和显存约束的 oracle，并与规则路由器进行对比。该方法不修改模型结构，也不重新训练 LLM，仅在单卡推理层面做请求级调度。

#### 实验结果分析

实验在单张 NVIDIA A100 40GB 上，使用 Meta-Llama-3.1-8B-Instruct 和 vLLM 进行评估，包含合成的部署风格工作负载以及 MMLU-Pro、GSM8K、TruthfulQA、GPQA、MLU 等自动基准。结果显示，在线控制器在合成负载上相对 FP16 达到平均 2.10× 的延迟加速和 0.48× 的能耗比，对应每个 token 的能耗降低 51.7%，而在质量门控基准上准确率与 FP16 基本持平，平均仅有 +0.17 个百分点的变化。作者还发现，学习型路由器并没有明显优于规则控制器，因为其增加了路由开销，并且更容易选择违反质量、能耗或显存约束的模式。可见文本未给出更完整的表格数值，但整体结论很明确：简单的请求感知路由即可在不改模型的前提下显著提升单卡推理效率。

<details>
<summary>完整摘要</summary>

ModeSwitch-LLM 是一种轻量级的请求边界控制器，旨在通过将每个请求路由到合适的固定推理模式，提升单 GPU 上大语言模型推理的效率。该系统不依赖单一静态服务配置，而是利用代价很低的工作负载级特征，在 FP16、量化模式、speculative decoding 以及 GPTQ + prefix caching、INT8 + continuous batching 这类混合模式之间进行选择。我们在单张 NVIDIA A100 GPU 上，对 Meta-Llama-3.1-8B-Instruct 进行了评测。在面向部署场景的合成工作负载上，在线控制器相较 FP16 平均实现了 2.10 倍的延迟加速，平均能耗比为 0.48 倍，对应每个 token 的能耗降低 51.7%。在作为质量门控的自动基准上，准确率与 FP16 基本接近，平均仅提高 0.17 个百分点。我们还评估了轻量级的学习型路由器，但发现它们并没有明显优于基于规则的控制器，因为它们增加了路由开销，并且更频繁地选择会违反质量、能耗或显存约束的模式。上述结果表明，无需重新训练模型或改变其架构，仅通过简单的请求感知路由，就能从现有推理模式中恢复出可观的效率收益。

</details>

---

### [[20_Research/Papers/大模型/AI-Friendly_LaTeX_Using_LaTeX_Code_as_a_Knowledge_Source_for_Retrieval-Augmented_Generation|AI-Friendly LaTeX: Using LaTeX Code as a Knowledge Source for Retrieval-Augmented Generation]]

![[assets/2605.22923_figure.png|800]]

- **arXiv**: [2605.22923](https://arxiv.org/abs/2605.22923)
- **PDF**: https://arxiv.org/pdf/2605.22923
- **详细分析**: [[20_Research/Papers/大模型/AI-Friendly_LaTeX_Using_LaTeX_Code_as_a_Knowledge_Source_for_Retrieval-Augmented_Generation|AI-Friendly LaTeX: Using LaTeX Code as a Knowledge Source for Retrieval-Augmented Generation]]
- **作者**: Tom Verhoeff
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Systems

#### 研究背景与动机

大模型在回答教材、讲义和编程练习相关问题时，若能依托明确的知识源，通常会比直接生成更可靠，因此检索增强生成（RAG）成为常用方案。对于数学和技术类文档，PDF 往往会丢失结构、标签、宏定义和作者意图，而 LaTeX 源码天然保留这些信息，更适合作为知识来源。问题在于，LaTeX 源码并不能直接喂给检索系统：交叉引用、定制宏、图表以及练习/例题的语义标注都需要额外处理。这篇论文值得关注的地方在于，它从“让 LaTeX 成为可检索知识源”的角度，系统梳理了面向 RAG 的预处理问题与工程化解决思路。

#### 方法概述和架构

论文提出了一套面向 AI 的 LaTeX 预处理流程，用于把 LaTeX 源码及其编译辅助文件、可选作者注释转换为适合向量数据库索引的 Markdown 和 JSONL 分块。整体流程包括：递归读取主文件及被引入的子文件，解析 .aux 文件中的 \\newlabel 等信息建立标签表，加载可选 YAML 注释，再将选定的 LaTeX 结构转换为 Markdown，并把 \\ref、\\eqref、\\pageref 等引用解析为可读文本。对于宏定义，方法区分了排版型宏、语义符号宏和结构型宏：前者可按 Markdown 规范展开，中间类宏保留符号同时补充语义说明，后者则直接解释为章节、练习等结构块并附带元数据。对于图像和 TikZ 图，论文主张把它们当作独立知识对象处理，提取标题、上下文、页码和作者提供的语义描述，必要时由 \\AIDescription、\\AIDeclareNotation 等注释宏提供机器可读语义。最终输出包括可读 Markdown、标签表以及按 section/definition/example/exercise 等粒度切分的 JSONL chunk，每个 chunk 含有用于检索的 embedding_text 和元数据。

#### 实验结果分析

这是一篇方法与系统论文，正文节选中未展示具体实验数据、数据集名称或量化指标，因此可见文本未给出具体数值。作者通过多个示例说明，该预处理器能把指向章节和页码的引用解析成更适合学生与教师提问习惯的文本，并把练习、例题、图表和语义宏转成更利于检索的知识块。论文还强调，该方法采用保守策略：当遇到不确定内容时不会强行展开，而是保留原文并给出警告，以提高在技术文档场景中的稳健性。

<details>
<summary>完整摘要</summary>

当大语言模型在回答教材、讲义和编程练习相关问题时，如果答案建立在明确的知识源之上，通常会更可靠。检索增强生成（RAG）是一种常见方法：先检索文档中的相关片段，再将其插入模型上下文中进行回答。对于数学和技术类材料，原始 LaTeX 源码往往比 PDF 更适合作为起点，因为它包含结构信息、标签、章节命令、宏以及作者意图，而这些内容在 PDF 提取中常常丢失或被扭曲。然而，LaTeX 源码并不能自动成为“AI 友好”的形式。交叉引用必须被解析，自定义宏必须被解释，练习和例子需要被识别，此外还可能需要作者提供的语义元数据。本文描述了一种聚焦式预处理方法：将 LaTeX 源码、其编译生成的辅助文件以及可选的作者注释，转换为适合在向量数据库中索引的 Markdown 和 JSONL 分块。

</details>

---

### [[20_Research/Papers/大模型/Query-Adaptive_Semantic_Chunking_for_Retrieval-Augmented_Generation_A_Dynamic_Strategy_with_Contextual_Window_Expansion|Query-Adaptive Semantic Chunking for Retrieval-Augmented Generation: A Dynamic Strategy with Contextual Window Expansion]]

![[assets/2605.22834_first_page.png|800]]

- **arXiv**: [2605.22834](https://arxiv.org/abs/2605.22834)
- **PDF**: https://arxiv.org/pdf/2605.22834
- **详细分析**: [[20_Research/Papers/大模型/Query-Adaptive_Semantic_Chunking_for_Retrieval-Augmented_Generation_A_Dynamic_Strategy_with_Contextual_Window_Expansion|Query-Adaptive Semantic Chunking for Retrieval-Augmented Generation: A Dynamic Strategy with Contextual Window Expansion]]
- **作者**: Mudit Rastogi
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision

#### 研究背景与动机

在 Retrieval-Augmented Generation（RAG）系统中，文档如何切分成 chunk 会直接影响检索到的上下文质量，进而影响生成结果的准确性与完整性。现有固定长度切分方法往往忽略语义边界和用户查询意图，只能在“切得更细”和“保留更多上下文”之间做粗糙权衡，难以同时兼顾召回与精度。已有语义切分和 agentic 切分虽然改善了部分问题，但通常仍没有把查询信息前置到切分阶段，因此在面向具体问题时不够自适应。这篇工作值得关注的地方在于，它把“如何切分文档”从静态预处理问题推进为与查询相关的动态决策问题。

#### 方法概述和架构

论文提出 Query-Adaptive Semantic Chunking（QASC），核心思想是在切分时直接利用用户查询来指导 chunk 的构造。具体来说，方法先将句子与查询分别编码为向量，并通过余弦相似度找出与查询最相关的种子句子；然后以这些种子句子为中心进行上下文窗口扩展，以保留局部语义连贯性和必要背景信息。接着，方法在 chunk 层面做分数聚合，确保最终形成的片段不仅包含高相关内容，也在整体上保持主题一致。整体流程是：输入文档和查询，先定位种子句，再扩展邻域形成候选 chunk，最后依据聚合得分确定输出 chunk，用于后续检索与生成。该方法不依赖固定粒度，而是根据查询动态构造更契合任务需求的切分结果。

#### 实验结果分析

作者在 100 篇技术文档、200 个跨四类问题的查询上评测了 QASC，并与五种固定切分粒度、recursive splitting、semantic chunking 和 agentic chunking 等方法比较。实验以 F1-score 为主要指标，QASC 达到 0.85，相比固定切分获得 18%–27% 的相对提升，相比语义切分和 agentic 切分提升 8%–12%。消融实验表明，种子句定位、窗口扩展和 chunk 级聚合三个组件都对性能有显著贡献。三位标注者的人类评估也支持该方法在相关性与连贯性方面优于现有切分策略，Cohen kappa = 0.82，说明一致性较高。

<details>
<summary>完整摘要</summary>

检索增强生成（RAG）系统的性能在很大程度上依赖于文档切分质量，因为它决定了检索阶段能否找到相关上下文。固定切分会把文档划分为统一大小的片段，而不考虑语义结构或用户意图，因此仅靠调整 chunk 大小并不能消除精度与召回之间的权衡。语义切分和 agentic 方法虽然在一定程度上缓解了这些问题，但它们并没有在切分阶段引入用户查询。我们提出 Query-Adaptive Semantic Chunking（QASC），它通过三种机制将查询动态融入切分过程：一是利用句子与查询嵌入之间的余弦相似度来识别种子句；二是在种子句周围进行上下文窗口扩展，以保持语义连贯性；三是在 chunk 层面进行分数聚合，以确保整体相关性。我们在 100 篇技术文档和 200 个查询上评估了 QASC，这些查询覆盖四种类型，并将其与五种固定粒度的切分方法、recursive splitting、semantic chunking 和 agentic chunking 进行比较。结果显示，QASC 的 F1-score 达到 0.85，相比固定切分方法取得 18%–27% 的相对提升，相比语义切分和 agentic 替代方法取得 8%–12% 的提升。消融研究证实，每个组件都对性能有显著贡献。由三位标注者进行的人类评估（Cohen kappa = 0.82）进一步表明，QASC 生成的 chunk 比现有方法更相关、也更连贯。

</details>

---
