# cs.CL | Computation and Language | 2026-08-03

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/大模型/TokTier_Exact_Stateful_Tokenization_for_Agentic_LLM_Serving|TokTier: Exact Stateful Tokenization for Agentic LLM Serving]]

![[assets/2607.29678_figure.png|800]]

- **arXiv**: [2607.29678](https://arxiv.org/abs/2607.29678)
- **PDF**: https://arxiv.org/pdf/2607.29678
- **详细分析**: [[20_Research/Papers/大模型/TokTier_Exact_Stateful_Tokenization_for_Agentic_LLM_Serving|TokTier: Exact Stateful Tokenization for Agentic LLM Serving]]
- **作者**: Zhenyu Zhang, Zhichao Cao
- **cs 子类**: cs.CL, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TokTier: Exact Stateful Tokenization for Agentic LLM Serving》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM serving systems cache prompt KV state, yet most front ends still re-tokenize the full request text on every call. The cost lands on coding agents, which resubmit a long transcript after each small tool result, and reuse is hard because even a short append can change token boundaries near the end of the previous sequence. Across 153,951 calls from two agent ecosystems, the median call appends about 1.4K characters, and only 1.0-3.6% of calls start or rebuild a session with contexts of millions of characters. At a 94.1% fleet prompt-cache hit rate, tokenization reaches up to 64% of time to first token. TokTier is a stateful tokenization service with one contract: emitted token IDs are always identical to full reference tokenization of the request text. For a session continuation, it re-tokenizes a small window around the append and splices only after a per-request stable-boundary check, widening the window or falling back to full tokenization on failure. For a call without a reusable prefix, it decomposes GPT-family regex pre-tokenization into run-local rules and runs exact pre-tokenization and BPE on a GPU. A sampled shadow verifier re-checks live traffic. Across 17 tokenizer families, differential campaigns cover 1.5x10^10 split checks, a 12.4 TB real-text corpus, and 93,000+ replayed agent steps, with zero divergence. Incremental repair takes 0.5-1.1 ms from 100K to 3M characters, up to 437x faster than HF tokenization and 2.1x faster at 1M than the strongest cache-based baseline (Gigatoken) fully prewarmed. GPU full tokenization encodes a 1M-character request in 0.87 ms, up to 491x below HF and 23.4x below the fastest published CPU method. With vLLM, median time to first token drops 16-34% and P99 drops 23% under recorded bursts. Under a 50 ms P99 objective, four repair cores plus one GPU sustain 1,821 requests/s where a 16-core stateless front end saturates at 40.

</details>

---

### [[20_Research/Papers/具身智能/WCM_A_World_Critic_Model_for_Vision-Language-Action_Reinforcement_Learning|WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning]]

![[assets/2607.29613_figure.png|800]]

- **arXiv**: [2607.29613](https://arxiv.org/abs/2607.29613)
- **PDF**: https://arxiv.org/pdf/2607.29613
- **详细分析**: [[20_Research/Papers/具身智能/WCM_A_World_Critic_Model_for_Vision-Language-Action_Reinforcement_Learning|WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning]]
- **作者**: Senyu Fei, Xiaopeng Yu, Siyin Wang, Xianzhong Zhao, Jingjing Gong, Xipeng Qiu
- **cs 子类**: cs.CL, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 大模型
- **相关性评分**: 3.85（加权：具身智能 2.1，大模型 0.25，强化学习 0.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature of robot control. A naive approach to incorporate observation history into the critic incurs exponential complexity with high-dimensional visual space, and still fails because pure scalar-return regression provides insufficient supervision for learning cross-temporal dynamics. We identify the root cause as a state approximation problem: without an explicit world modeling objective, the critic's representation cannot capture the temporal structure needed for accurate value estimation. To address this, we propose the World Critic Model (WCM), built on a lightweight LeJEPA architecture; WCM jointly predicts future latent state and estimates values, such that the critic's representation is explicitly trained to capture temporal dynamics rather than merely regress scalar returns. WCM integrates seamlessly into both on-policy and off-policy training pipelines and is compatible with state-of-the-art VLA backbones including Pi0, Pi0.5, and OpenVLA-OFT. Extensive experiments on 149 tasks across four benchmarks demonstrate that WCM consistently achieves state-of-the-art performance in both in-distribution and out-of-distribution settings, with particularly strong generalization gains. We further validate WCM on seven real-world manipulation tasks using OpenVLA-OFT and Pi0.5 with off-policy RL, confirming stable deployment across diverse settings.

</details>

---

### [[20_Research/Papers/大模型/Know_It,_Act_on_It_Investigating_Memory_Utilization_in_LLM_Personalization|Know It, Act on It: Investigating Memory Utilization in LLM Personalization]]

![[assets/2607.29433_figure.png|800]]

- **arXiv**: [2607.29433](https://arxiv.org/abs/2607.29433)
- **PDF**: https://arxiv.org/pdf/2607.29433
- **详细分析**: [[20_Research/Papers/大模型/Know_It,_Act_on_It_Investigating_Memory_Utilization_in_LLM_Personalization|Know It, Act on It: Investigating Memory Utilization in LLM Personalization]]
- **作者**: Zhaoxin Feng, Jianfei Ma, Emmanuele Chersoni
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Know It, Act on It: Investigating Memory Utilization in LLM Personalization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model (LLM) agents evolve into personalized companions, memory has emerged as a core capability. However, LLMs face a knowledge utilization problem: they may fail to act on relevant user preferences even when they are fully present in context. When an agent fails to tailor its response in a context where previously shared user preferences should matter, it is unclear whether the model failed to remember that information or remembered it but failed to use it. To isolate this breakdown, we introduce a decoupled evaluation paradigm that administers paired Know and Act tests to the same user preference. We conduct large-scale experiments across 16 systems and five memory architectures, evaluating 1,000 preferences embedded at three levels of expression strength. Our results show a large gap between Know and Act outcomes: agents often pass the recall test for a user preference but fail to reflect that same preference in the paired behavioral scenario. While memory architectures reduce this gap, utilization remains especially weak for health and therapy-related preferences, where failures to act carry the greatest real-world stakes.

</details>

---

### [[20_Research/Papers/大模型/Bridging_the_Question-Answer_Gap_in_Retrieval-Augmented_Generation_Hypothetical_Prompt_Embeddings|Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical Prompt Embeddings]]

![[assets/2607.29402_figure.png|800]]

- **arXiv**: [2607.29402](https://arxiv.org/abs/2607.29402)
- **PDF**: https://arxiv.org/pdf/2607.29402
- **详细分析**: [[20_Research/Papers/大模型/Bridging_the_Question-Answer_Gap_in_Retrieval-Augmented_Generation_Hypothetical_Prompt_Embeddings|Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical Prompt Embeddings]]
- **作者**: Domen Vake, Jernej Vičič, Aleksandar Tošić
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.CL

#### 研究背景与动机

《Bridging the Question-Answer Gap in Retrieval-Augmented Generation: Hypothetical Prompt Embeddings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) systems synergize retrieval mechanisms with generative language models to enhance the accuracy and relevance of responses. However, bridging the style gap between user queries and relevant information in document text remains a persistent challenge in retrieval-augmented systems, often addressed by runtime solutions (e.g., Hypothetical Document Embeddings (HyDE)) that attempt to improve alignment but introduce extra computational overhead at query time. To address these challenges, we propose Hypothetical Prompt Embeddings (HyPE), a framework that shifts the generation of hypothetical content from query time to the indexing phase. By precomputing multiple hypothetical prompts for each data chunk and embedding the chunk in place of the prompt, HyPE transforms retrieval into a question-question matching task, bypassing the need for runtime synthetic answer generation. This approach does not introduce latency but also strengthens the alignment between queries and relevant context. Our experimental results on six common datasets show that HyPE can improve retrieval context precision by up to 42 percentage points and claim recall by up to 45 percentage points, compared to standard approaches, while remaining compatible with re-ranking, multi-vector retrieval, query decomposition, and other RAG advancements

</details>

---

### [[20_Research/Papers/大模型/PTP_Previous-Token_Prediction_based_LLM_Inversion_for_Near-Exact_Prompt_Reconstruction|PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction]]

![[assets/2607.29378_figure.png|800]]

- **arXiv**: [2607.29378](https://arxiv.org/abs/2607.29378)
- **PDF**: https://arxiv.org/pdf/2607.29378
- **详细分析**: [[20_Research/Papers/大模型/PTP_Previous-Token_Prediction_based_LLM_Inversion_for_Near-Exact_Prompt_Reconstruction|PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction]]
- **作者**: Pirzada Suhail, Nagasai Saketh Naidu, Atanu R Sinha, Amit Sethi
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《PTP: Previous-Token Prediction based LLM Inversion for Near-Exact Prompt Reconstruction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) generate text by auto-regressively sampling the next token. This inherently leads to a many-to-many mapping between prompts and responses, complicating the task of inferring prompts from observed outputs. Prior work on LLM inversion frames prompt recovery as a semantic reconstruction task. They rely on fine-tuning pretrained sequence-to-sequence models on large external datasets--and requiring access to model weights or logits--to generate semantically plausible prompts. In contrast, we present a functional approach to inverting a given LLM in a black-box setting, without auxiliary aids. We train an explicit inverse language model entirely from scratch on data synthetically generated from the target LLM itself. Analogous to forward next-token prediction, our inverse model is trained using previous-token prediction, establishing a generative link between the forward and inverse processes that enables faithful prompt reconstruction. Moreover, it naturally supports diverse prompt reconstructions through sampling, whereby all such prompts induce similar responses under the forward, target LLM. Our approach generalises across datasets and exhibits transferability in reconstructing prompts from responses generated by different LLMs. Further, across the set of token based evaluation metrics for prompt and response reconstructions, our approach outperforms prior work.

</details>

---

### [[20_Research/Papers/大模型/Zero-Mem_Zero-Token_Memory_Operations_for_LLM_Agents|Zero-Mem: Zero-Token Memory Operations for LLM Agents]]

![[assets/2607.29377_figure.png|800]]

- **arXiv**: [2607.29377](https://arxiv.org/abs/2607.29377)
- **PDF**: https://arxiv.org/pdf/2607.29377
- **详细分析**: [[20_Research/Papers/大模型/Zero-Mem_Zero-Token_Memory_Operations_for_LLM_Agents|Zero-Mem: Zero-Token Memory Operations for LLM Agents]]
- **作者**: Yilin Xiao, Zhehan Zhu, Yujing Zhang, Jin Chen, Zijin Hong, Luyao Zhuang, Qinggang Zhang, Shengyuan Chen, Xiaocao Ouyang, Lingfei Ren, Xiao Huang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Zero-Mem: Zero-Token Memory Operations for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents need memory to act consistently over long interactions, yet many systems use additional LLM calls to operate that memory. Generating intermediate records and mediating their retrieval adds recurring token and time costs, while omitted or merged details can obscure the original evidence. We ask whether structured memory access requires generation at all. Zero-Mem introduces \emph{zero-token memory operations}: no step outside final question answering invokes an LLM or consumes LLM input or output tokens; encoder computation is accounted for separately. Zero-Mem preserves original interaction traces as its source of record. It organizes the traces in two complementary ways. An entity--context graph exposes connections across interactions, while a temporal hierarchy preserves conversational locality and session state. For each query, Zero-Mem weighs the two views, retrieves from both, and follows their structure to recover supporting relations or surrounding context. Deterministic calibration first discards conflicting evidence and then keeps the reader's answer grounded in the retrieved traces. Only the final-QA reader invokes an LLM. Across long-memory and long-context question-answering benchmarks, Zero-Mem achieves competitive performance while eliminating LLM calls and LLM-token consumption from memory operations. With the same final-QA reader and context budget, it reduces memory-operation time cost by 57.6\% relative to the fastest compared baseline. Ablations support the contribution of the two views and their query-dependent coordination. Overall, the results show that structured agent memory need not generate an intermediate representation of the past. After peer review, the code and implementation details will be available at \textcolor{blue}{https://github.com/TheMoon0815/Zero-mem}.

</details>

---

### [[20_Research/Papers/大模型/Faster_but_Different_Diagnosing_and_Controlling_Content_Drift_in_Accelerated_Multimodal_Diffusion_Language_Models|Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models]]

![[assets/2607.29079_figure.png|800]]

- **arXiv**: [2607.29079](https://arxiv.org/abs/2607.29079)
- **PDF**: https://arxiv.org/pdf/2607.29079
- **详细分析**: [[20_Research/Papers/大模型/Faster_but_Different_Diagnosing_and_Controlling_Content_Drift_in_Accelerated_Multimodal_Diffusion_Language_Models|Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models]]
- **作者**: Yaoxuan Dou, Yang Shu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ParallelBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training-free acceleration makes diffusion-based multimodal large language models (dMLLMs) more deployable, but it may silently change generated content. We study this serving-time consistency problem on 300 real images, comparing Fast-dLLM outputs with the same model's unaccelerated outputs. Across the mild parallelism induced in our long-form setting (1.05--1.25 committed tokens per step), confidence-threshold tuning changes decoding behavior but not baseline agreement. State-refresh ablations and an image-swap intervention instead identify stale visual and generated-text states as contributors to drift. For the tested Fast-dLLM implementation, shortening the KV-cache refresh interval yields a monotonic speed--agreement frontier and near-exact agreement at a measured 1.3x speedup. The initial diagnosis also appears with dLLM-Cache and LaViDa, although dLLM-Cache recovers agreement only after both caches are tightened, which removes its speed advantage. Independent prompts and images reproduce the threshold-insensitivity and refresh recovery. A targeted audit finds genuine content substitution in half of 50 low-agreement pairs. In a separate blinded two-annotator evaluation, the pooled accelerated-minus-baseline factual-error difference is 0.00 (95% CI [-0.17,+0.17]); this sample detects no difference but does not establish factual equivalence. Finally, none of the tested adaptive or smoothed-refresh variants beats the fixed interval at matched compute. Our contribution is a paired diagnostic and an implementation-scoped consistency control, not an accuracy or safety guarantee.

</details>

---

### [[20_Research/Papers/大模型/TransMem_Transforming_Hidden_States_into_Memory_for_Large_Language_Models|TransMem: Transforming Hidden States into Memory for Large Language Models]]

![[assets/2607.29032_figure.png|800]]

- **arXiv**: [2607.29032](https://arxiv.org/abs/2607.29032)
- **PDF**: https://arxiv.org/pdf/2607.29032
- **详细分析**: [[20_Research/Papers/大模型/TransMem_Transforming_Hidden_States_into_Memory_for_Large_Language_Models|TransMem: Transforming Hidden States into Memory for Large Language Models]]
- **作者**: Haodong Lei, Junming Liu, Yirong Chen, Pinlong Cai, Botian Shi, Ding Wang, Hongsong Wang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《TransMem: Transforming Hidden States into Memory for Large Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and actions. However, useful information encoded in previously computed representations is often underutilized during subsequent generation. We propose \textbf{TransMem}, a lightweight inference-time parametric memory module that transforms sparse historical hidden states from a frozen LLM backbone into reusable memory representations. TransMem uses a lightweight gating network to dynamically apply the latent intervention to the current hidden states, without repeatedly encoding the preceding context. To learn transferable memory utilization rather than task-specific knowledge, we introduce evidence-conditioned self-distillation. A memory-augmented student processes the full context and matches the predictive distribution of an evidence-only teacher that shares the same frozen backbone. Experiments on LoCoMo, HotpotQA, and MemoryAgentBench demonstrate consistent improvements across different model architectures and scales. TransMem yields gains of 11.58--29.25 $F_1$ on LoCoMo and 10.20--13.03 $F_1$ on HotpotQA, while improving the average MemoryAgentBench accuracy from 29.54\% to 40.00\%. These results establish sparse historical hidden states as an effective and efficient memory substrate for long-context LLM agents. Our code is available at https://github.com/Haodong-Lei-Ray/TransMem.

</details>

---

### [[20_Research/Papers/大模型/GoldenRetriever_Non-Interactive_Homomorphic_Encrypted_Retrieval_for_Privacy-Preserving_RAG|GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG]]

![[assets/2607.29019_figure.png|800]]

- **arXiv**: [2607.29019](https://arxiv.org/abs/2607.29019)
- **PDF**: https://arxiv.org/pdf/2607.29019
- **详细分析**: [[20_Research/Papers/大模型/GoldenRetriever_Non-Interactive_Homomorphic_Encrypted_Retrieval_for_Privacy-Preserving_RAG|GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG]]
- **作者**: Yang Gao, Gang Quan, Scott Piersall, Qian Lou, Dongdong Wang, Liqiang Wang
- **cs 子类**: cs.CL, cs.CR, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Security

#### 研究背景与动机

《GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) enhances large language models by incorporating external knowledge, but existing pipelines typically operate on plaintext data, raising significant privacy concerns. Prior work on privacy-preserving retrieval leverages cryptographic techniques such as homomorphic encryption (HE) and private information retrieval (PIR), but often relies on interactive protocols or ranking-based selection mechanisms that incur high latency and potential information leakage. In this paper, we propose a practical non-interactive encrypted retrieval framework for RAG based on threshold selection. Instead of performing expensive top-$k$ ranking under encryption, our approach selects documents whose similarity scores exceed a predefined threshold, reducing computational complexity from quadratic to linear in the corpus size. We implement this design using CKKS-based homomorphic computation, enabling fully encrypted similarity evaluation and document selection without revealing query content, intermediate scores, or selected indices. To bridge the gap between approximate encrypted computation and discrete token reconstruction, we introduce a precision-stable mask polarization method that ensures accurate recovery of selected documents. Experiments on standard retrieval benchmarks demonstrate that our approach achieves competitive retrieval effectiveness while significantly reducing latency compared to ranking-based encrypted methods. These results highlight threshold-based selection as a practical foundation for scalable and secure RAG systems.

</details>

---

### [[20_Research/Papers/大模型/Mixture-of-Translators_Translating_KV_Caches_Across_Heterogeneous_Large_Language_Models|Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models]]

![[assets/2607.28979_first_page.png|800]]

- **arXiv**: [2607.28979](https://arxiv.org/abs/2607.28979)
- **PDF**: https://arxiv.org/pdf/2607.28979
- **详细分析**: [[20_Research/Papers/大模型/Mixture-of-Translators_Translating_KV_Caches_Across_Heterogeneous_Large_Language_Models|Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models]]
- **作者**: Jin-woo Lee, Minkyung Song, Junghyun Oh, Seunghoon Han, Soyoung Park, Gwangseon Jang, Sungsu Lim
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Heterogeneous Large Language Model (LLM) systems increasingly rely on shared contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or store caches for the same context, limiting the scalability of multi-model reasoning and long-context generation. We propose Mixture-of-Translators(MoT), a cache translation framework that maps context KV caches from a source LLM into the cache space of a target LLM. Unlike prior approaches that depend on a single projection path or global shared latent space, MoT uses multiple translator modules to capture diverse source--target mappings. To further reduce residual translation error, we introduce a Context Correction Loss that aligns the replayed target trajectory with the native target trajectory. We reveal two competing failure modes in cache translation: propagated translation shift from early injection and last-state shift from late injection. MoT addresses them through translator mixtures and target-side correction. Across homogeneous and heterogeneous translations among Qwen2.5, GPT-2, and OPT models, MoT preserves downstream QA performance, including Qwen2.5-7B-scale translation with 51.0% average closed-set QA accuracy and 0.43 average extractive QA F1. In practical case studies, MoT enables quality-preserving memory reuse for multi-agent reasoning and retains 96.3% of direct-context quality in long-context cache-augmented generation, demonstrating scalable KV cache reuse across heterogeneous LLMs.

</details>

---

### [[20_Research/Papers/大模型/BLADE_Boundary-Expanded_and_Layer-Adaptive_Dynamic_Exit_for_Efficient_LLM_Reasoning|BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning]]

![[assets/2607.28966_figure.png|800]]

- **arXiv**: [2607.28966](https://arxiv.org/abs/2607.28966)
- **PDF**: https://arxiv.org/pdf/2607.28966
- **详细分析**: [[20_Research/Papers/大模型/BLADE_Boundary-Expanded_and_Layer-Adaptive_Dynamic_Exit_for_Efficient_LLM_Reasoning|BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning]]
- **作者**: Keshu Fu, Keqin Peng, Jun Bai, Shuhan Qin, Chen Li, Junzhu Liang, Yefei Chen, Jiaqi Li, Yuanxin Ouyang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models often improve task performance by generating long reasoning traces, but the resulting computation is frequently wasted on redundant verification and revision. Existing probe-based early-exit approaches mainly inspect explicit self-doubt expressions, leaving many earlier termination opportunities undetected. Expanding inspection to ordinary reasoning boundaries improves coverage, but also exposes highly diverse intermediate states whose predictive information may reside in different hidden layers. We present Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning (BLADE), a lightweight framework that dynamically terminates reasoning by estimating whether the generated prefix is sufficient for correct answering. BLADE constructs multi-granular checkpoints from sentence, self-doubt, and paragraph boundaries, and derives robust training labels through repeated answer completions. It further learns a compact subset of informative probe layers instead of relying on fixed choices or expensive representations from all layers. At inference time, calibrated predictions are combined with checkpoint-specific confirmation rules to balance responsiveness and premature-exit risk. Experiments on five benchmarks and two Qwen3 reasoning models show that BLADE preserves near-baseline accuracy while reducing generated tokens by 24.8% on Qwen3-8B and 15.8% on Qwen3-4B. Ablation studies further confirm the benefits of diverse checkpoints and automatic layer selection, demonstrating an effective approach to more efficient LLM reasoning.

</details>

---

### [[20_Research/Papers/大模型/Benchmarks_Are_Not_Validation_A_System-Level_View_of_Financial_LLM_Applications|Benchmarks Are Not Validation: A System-Level View of Financial LLM Applications]]

![[assets/2607.28840_first_page.png|800]]

- **arXiv**: [2607.28840](https://arxiv.org/abs/2607.28840)
- **PDF**: https://arxiv.org/pdf/2607.28840
- **详细分析**: [[20_Research/Papers/大模型/Benchmarks_Are_Not_Validation_A_System-Level_View_of_Financial_LLM_Applications|Benchmarks Are Not Validation: A System-Level View of Financial LLM Applications]]
- **作者**: Burak Payzun, İrem Demirtaş, Simona Scala, Elena Ferretti, Seçil Arslan
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Benchmarks Are Not Validation: A System-Level View of Financial LLM Applications》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, ConvFinQA, FinQA, FinanceBench, StableToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly deployed in financial applications that combine retrieval, proprietary data, tool use, orchestration logic, monitoring, and human escalation. Yet evaluation often remains model-centric: benchmark scores, task accuracy, or one-off qualitative reviews are treated as evidence of readiness. In financial settings, this is insufficient. We take the position that financial LLM systems should not be approved for production based on benchmark performance alone. They require system-level validation evidence across the application stack: data, model design, retrieval and generation performance, agent behavior, governance, and implementation. Drawing on industry experience validating GenAI applications in financial institutions, we outline a multi-layer validation view and explain why hybrid evaluation is necessary. We discuss where LLM-as-a-judge methods are useful and why they require controls such as multiple judges, rubrics, agreement, and auditability checks. We also highlight failure modes poorly captured by static benchmarks, including retrieval failures, unfaithful generation, tool misuse, escalation errors, and operational instability. Our position is that financial LLM validation should be an ongoing system discipline rather than a one-time model scoring exercise. Validation should produce decision-ready evidence, not only scores. We conclude with a research agenda for system-aware benchmarks, agent trace validation, judge alignment protocols, and lifecycle validation standards.

</details>

---

### [[20_Research/Papers/大模型/Self-Supervised_Skill_Optimization|Self-Supervised Skill Optimization]]

![[assets/2607.28777_figure.png|800]]

- **arXiv**: [2607.28777](https://arxiv.org/abs/2607.28777)
- **PDF**: https://arxiv.org/pdf/2607.28777
- **详细分析**: [[20_Research/Papers/大模型/Self-Supervised_Skill_Optimization|Self-Supervised Skill Optimization]]
- **作者**: Siran Peng, Cuiyu Yang, Tianyu Fu, Tianshuo Zhang, Haoyuan Zhang, Weisong Zhao, Anyang Su, Minghui Wu, Huiying Li, Xiangyu Zhu, Chenxu Zhao, Zhen Lei
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Self-Supervised Skill Optimization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills provide frozen large language model (LLM) agents with reusable procedural guidance, and recent work shows that such skills can be optimized with ground-truth (GT) feedback. Many applications, however, lack GT labels, task scores, rewards, or reliable task-specific evaluators. We therefore introduce Self-Supervised Skill Optimization (SSO), a comparative framework that learns a reusable skill from unlabeled task instances alone. At each step, SSO runs the current skill on an unlabeled batch, uses a subset of the resulting executions to generate complete skill probes, and runs the probes on the same batch. An LLM judge compares the resulting answers, trajectories, artifacts, or terminal states. A separate behavior extractor identifies behavioral differences without seeing the judge's decisions. SSO uses these decisions to aggregate evidence for and against the observed behaviors across instances. It then ranks the behaviors by the resulting evidence and renders a new complete skill from the highest-ranked behaviors. The update is accepted only if the new skill outperforms the current one on an unlabeled validation set. SSO outperforms existing GT-free prompt optimizers on both closed-ended and open-ended tasks. On closed-ended benchmarks, it approaches and sometimes exceeds the strongest GT-based skill optimizer without using any GT feedback.

</details>

---

### [[20_Research/Papers/大模型/Measuring_Cognitive_Engagement_in_Collaborative_Discourse_with_an_Extended_ICAP_Framework_Comparing_Human_Annotation,_In-Context_Learning,_a|Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents]]

![[assets/2607.28651_figure.png|800]]

- **arXiv**: [2607.28651](https://arxiv.org/abs/2607.28651)
- **PDF**: https://arxiv.org/pdf/2607.28651
- **详细分析**: [[20_Research/Papers/大模型/Measuring_Cognitive_Engagement_in_Collaborative_Discourse_with_an_Extended_ICAP_Framework_Comparing_Human_Annotation,_In-Context_Learning,_a|Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents]]
- **作者**: Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas
- **cs 子类**: cs.CL, cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaboration supports learning and problem-solving, but its effectiveness depends on cognitive engagement during discourse. This study applies an extended 7-point ICAP framework based on the Interactive, Constructive, Active, and Passive modes to characterize variation in cognitive engagement during collaborative dialogue. Engagement was coded by trained human annotators and compared with large language model (LLM)-based labeling approaches, including in-context learning (ICL), zero-shot prompting, and self-reflective agents. Interrater reliability among human annotators was robust across framework refinement stages (kappa = 0.906-0.998), higher than the moderate agreement observed for ICL-based annotation (kappa = 0.541-0.609). The human-refined framework improved agreement among human annotators (Delta kappa = 0.10), but produced only modest gains for ICL-based LLMs (Delta kappa less than 0.04). Agent-refined frameworks improved cross-model agreement but remained below the human-refined framework. These findings highlight the promise of agent-based approaches and the importance of continued interaction between theory-guided human annotation and LLM-based methods in future work.

</details>

---

### [[20_Research/Papers/大模型/To_Facilitate_or_not_to_Facilitate_Human_and_LLM_Facilitator_Tendencies_in_Online_Discussions|To Facilitate or not to Facilitate: Human and LLM Facilitator Tendencies in Online Discussions]]

![[assets/2607.28643_figure.png|800]]

- **arXiv**: [2607.28643](https://arxiv.org/abs/2607.28643)
- **PDF**: https://arxiv.org/pdf/2607.28643
- **详细分析**: [[20_Research/Papers/大模型/To_Facilitate_or_not_to_Facilitate_Human_and_LLM_Facilitator_Tendencies_in_Online_Discussions|To Facilitate or not to Facilitate: Human and LLM Facilitator Tendencies in Online Discussions]]
- **作者**: Dimitris Tsirmpas, Katerina Korre, John Pavlopoulos
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《To Facilitate or not to Facilitate: Human and LLM Facilitator Tendencies in Online Discussions》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating facilitation in online discussions is a long-standing social concern given the increasing time we spend on online spaces and the failure of content moderation approaches. While studies have been conducted on how to facilitate, none have answered the essential question of when to do so. A potential answer is using LLMs, which ostensibly make automated, large-scale intervention increasingly feasible. In this study, we examine when LLMs decide to facilitate by defining what facilitation is, observing when humans decide to facilitate, and comparing their decisions with those made by LLMs. To this end, we create PEFK, a corpus standardizing and aggregating all relevant facilitation datasets. We are the first to run a survey on facilitation timing, which we execute using expert facilitative participants and LLM-as-a-judge models. We discover that while humans are more cautious, LLMs are excessively eager to facilitate, although both are more certain when judging that facilitation is not needed. We then investigate whether this behavior can be corrected using alternative setups for LLMs and training ModernBert classifiers on established datasets, finding that the latter perform more reliably than the former, although current datasets impose a relatively low performance ceiling.

</details>

---

### [[20_Research/Papers/大模型/TokenSwap_Benchmarking_and_Reducing_the_Modality_Gap_in_Multimodal_LLMs|TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs]]

![[assets/2607.28640_figure.png|800]]

- **arXiv**: [2607.28640](https://arxiv.org/abs/2607.28640)
- **PDF**: https://arxiv.org/pdf/2607.28640
- **详细分析**: [[20_Research/Papers/大模型/TokenSwap_Benchmarking_and_Reducing_the_Modality_Gap_in_Multimodal_LLMs|TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs]]
- **作者**: Andong Hua, Colton Bishop, Igor Mordatch, Arian Hosseini, Jindong Gu, Aleksandra Faust, Rebecca Roelofs, Yao Qin
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TokenSwap-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) should generate consistent responses given semantically equivalent inputs across modalities. However, we observe a systematic discrepancy in model predictions under such cross-modal variations. Specifically, we define the modality gap as the difference in model performance under semantically equivalent textual and multimodal inputs. We introduce TokenSwap, a method that constructs such inputs by replacing textual concepts with semantically aligned images, resulting in sequences where visual tokens are interleaved with text tokens. Based on TokenSwap, we transform existing text-based benchmarks such as MMLU into image-interleaved counterparts, resulting in TokenSwap-Bench. Across 42 MLLMs, we observe a pervasive modality gap, with performance decreasing by 4.2% to 47.4% when moving from text-only to image-interleaved inputs, averaging 19.6% +/- 3.3% across models. Notably, we observe that reasoning models exhibit consistently smaller gaps, achieving an average gap of 10.1% compared to 25.5% for non-reasoning models. In contrast, neither prompting strategies nor scaling training compute alone reliably reduces the modality gap. Finally, we demonstrate that incorporating TokenSwap during training effectively mitigates this gap while preserving strong text-only and vision-language performance.

</details>

---

### [[20_Research/Papers/大模型/Learning_Stateful_Predictive_Knowledge_From_Experience|Learning Stateful Predictive Knowledge From Experience]]

![[assets/2607.28638_figure.png|800]]

- **arXiv**: [2607.28638](https://arxiv.org/abs/2607.28638)
- **PDF**: https://arxiv.org/pdf/2607.28638
- **详细分析**: [[20_Research/Papers/大模型/Learning_Stateful_Predictive_Knowledge_From_Experience|Learning Stateful Predictive Knowledge From Experience]]
- **作者**: Yan Song, Xidong Feng, Bo Liu, Xinyu Cui, Haotian Fu, Zichen Liu, Mengyue Yang, Cheng Deng, Jian Zhao, Jun Wang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.65，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Learning Stateful Predictive Knowledge From Experience》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SKL-RL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model (LLM) agents increasingly learn from experience, they primarily rely on trajectory-level reflection to extract insights. Viewed through the lens of predictive knowledge, we argue that this approach operates on episodic hindsight rather than predictive foresight, yielding brittle, path-dependent heuristics. To address this, we propose Stateful Knowledge Learning (SKL). SKL shifts the agent's focus from trajectory-level summarization to maintaining Stateful Knowledge: explicit, declarative predictive assessments anchored to state. We first demonstrate a motivating example showing how stateful knowledge provides granularity, enhances generalization, and enables knowledge bootstrapping. To further scale up the idea, we introduce two algorithms via self-distillation (SKL-SD) and reinforcement learning (SKL-RL), training agents to autonomously extract state-grounded predictive knowledge from experience and learn to leverage it for policy making. Experiments on interactive environments (WebShop, ScienceWorld) and a complex reasoning task (ChessPuzzles) demonstrate that equipping models with the inherent ability to learn stateful predictive knowledge significantly outpaces current reflection-based training paradigms.

</details>

---

### [[20_Research/Papers/大模型/Chain-of-Models_Cross-Model_Auditing_for_Bias-Robust_LLM_Judges|Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges]]

![[assets/2607.28636_figure.png|800]]

- **arXiv**: [2607.28636](https://arxiv.org/abs/2607.28636)
- **PDF**: https://arxiv.org/pdf/2607.28636
- **详细分析**: [[20_Research/Papers/大模型/Chain-of-Models_Cross-Model_Auditing_for_Bias-Robust_LLM_Judges|Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges]]
- **作者**: Qian Wang, Zhanzhi Lou, Zhenheng Tang, Nuo Chen, Bingsheng He
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs increasingly serve as automated judges, but their judgments remain vulnerable to cognitive biases. Existing mitigations mostly rely on prompt-driven debiasing, which is brittle across bias types, or human evaluation, which does not scale. We study \emph{Chain-of-Models} (CoM), an automated audit pipeline in which a second model inspects the first model's reasoning trace before producing the final judgment. The key design question is whether the auditor should be the same model, a same-family model, or a different-family model. Across 9 models from 6 families, 4 cognitive biases, and 4 factual datasets, we find that auditor identity matters in two ways. First, standalone bias resistance does not predict audit effectiveness: Kimi-K2.5 is the strongest standalone model on several biases, yet is a weak auditor for Qwen2.5-72B's biased traces. Second, the best auditor is bias-specific: GPT-4o is strongest on bandwagon, authority, and distraction, while GLM-5 is strongest on sycophancy. We operationalize these findings with a per-bias auditor selection rule that, given the bias type, scores candidates along functional diversity, per-bias standalone resistance, and calibrated audit effectiveness. Under a calibration/test split, the selector reaches the highest accuracy across the four biased slices ($0.884$ vs.\ $0.824$ for the strongest single fixed auditor and $0.805$ for the no-audit baseline). We release data, configurations, and an LLM-agent skill at https://anonymous.4open.science/r/chain-of-models-B585 .

</details>

---
