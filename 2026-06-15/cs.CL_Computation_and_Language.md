# cs.CL | Computation and Language | 2026-06-15

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/大模型/Gaze_Heads_How_VLMs_Look_at_What_They_Describe|Gaze Heads: How VLMs Look at What They Describe]]

![[assets/2606.14703_figure.png|800]]

- **arXiv**: [2606.14703](https://arxiv.org/abs/2606.14703)
- **PDF**: https://arxiv.org/pdf/2606.14703
- **详细分析**: [[20_Research/Papers/大模型/Gaze_Heads_How_VLMs_Look_at_What_They_Describe|Gaze Heads: How VLMs Look at What They Describe]]
- **作者**: Rohit Gandikota, David Bau
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Gaze Heads: How VLMs Look at What They Describe》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How a vision-language model internally solves the task of describing an image is far from obvious. We find that the model develops a specific mechanism for this: a small set of attention heads in its language-model backbone, which we call gaze heads, whose attention tracks the image region the model is currently describing. We find them with a simple correlation score from a few forward passes, using comic strips as a controlled testbed where narrative order is laid out spatially. These gaze heads do not just track the image tokens being described: redirecting their attention to a chosen region forces the VLM to describe that region instead. A single attention-mask intervention on the top-100 gaze heads, fewer than 9% of all heads, steers the model's answer to any chosen comic panel at 83.1% accuracy, while the same intervention on random heads fails to redirect the answer, and intervening on all heads destroys generation. The same lever also extends to continuous control: switching the gaze target mid-generation makes the model wrap up its current panel description and move to the new one within a few tokens. Beyond comics, the same intervention redirects answers to chosen regions in natural COCO images. The mechanism further recurs across model sizes from 2B to 32B parameters and across other VLM architectures, although some frozen-encoder families show no comparable head set. More broadly, this shows that targeted edits identified through mechanistic analysis can serve as practical inference-time levers for steering multimodal model behavior, without any retraining. Our code, interactive demo, and datasets are available at https://gaze.baulab.info/

</details>

---

### [[20_Research/Papers/强化学习/AdaSR_Adaptive_Streaming_Reasoning_with_Hierarchical_Relative_Policy_Optimization|AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization]]

![[assets/2606.14694_figure.png|800]]

- **arXiv**: [2606.14694](https://arxiv.org/abs/2606.14694)
- **PDF**: https://arxiv.org/pdf/2606.14694
- **详细分析**: [[20_Research/Papers/强化学习/AdaSR_Adaptive_Streaming_Reasoning_with_Hierarchical_Relative_Policy_Optimization|AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization]]
- **作者**: Junlong Tong, Wenqi Xu, Yingqi Fan, Anhao Zhao, Xuan Lu, Yang Tan, Xiaoyu Shen
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large reasoning models typically follow a read-then-think paradigm: they observe the complete input, reason over a static context, and then produce the answer. Yet many real-world scenarios are inherently dynamic, such as audio and video stream, where information arrives as a continuous stream and models must reason, update, and respond under partial observations. Recent streaming reasoning methods allow models to think while reading, but they largely rely on supervised imitation of pre-constructed trajectories, which limits their flexibility. In this paper, we propose AdaSR, an adaptive streaming reasoning framework that enables models to reason during input streaming and perform final deliberation once the stream is complete, learning when to think, and how much computation to allocate across different stages. To optimize this hierarchical reasoning process, we introduce Hierarchical Relative Policy Optimization (HRPO), which decomposes policy optimization into streaming reasoning and deep reasoning phases, providing more fine-grained advantage assignment instead of uniformly distributing a single sequence-level advantage over all tokens. HRPO integrates format, accuracy, and adaptive thinking rewards to enforce valid reasoning protocols, preserve final task performance, and encourage latency-aware computation allocation. Experiments show that AdaSR achieves a better balance among reasoning accuracy, computational efficiency, and streaming latency compared with supervised fine-tuning baseline. We release our code at https://github.com/EIT-NLP/StreamingLLM/tree/main/AdaSR.

</details>

---

### [[20_Research/Papers/大模型/CORA_Analyzing_and_bridging_thinking-answer_gap_in_Multimodal_RLVR_via_Consistency-Oriented_Reasoning_Alignment|CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment]]

![[assets/2606.14691_figure.png|800]]

- **arXiv**: [2606.14691](https://arxiv.org/abs/2606.14691)
- **PDF**: https://arxiv.org/pdf/2606.14691
- **详细分析**: [[20_Research/Papers/大模型/CORA_Analyzing_and_bridging_thinking-answer_gap_in_Multimodal_RLVR_via_Consistency-Oriented_Reasoning_Alignment|CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment]]
- **作者**: Jiayue Cao, Zhicong Lu, Xuehan Sun, Wei Jia, Hongling Zheng, Changyuan Tian, Zichuan Lin, Wenqian Lv, Nayu Liu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.15（加权：大模型 0.55，强化学习 0.6）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlgoPuzzleVQA, CVBench, PuzzleVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has successfully elicited the reasoning capabilities of large language models, motivating its extension to multimodal scenarios. Existing methods primarily focus on improving the visual coverage of reasoning traces and mitigating visual hallucinations, but underestimate the semantic inconsistency between the reasoning process and the final answer. In this paper, we delve into thinking-answer inconsistency in RLVR for large vision-language models (LVLMs), showing thorough analyses of rollouts collected throughout Group Relative Policy Optimization (GRPO) training process and post-RLVR evaluation outputs that this issue persists during training and remains present during inference. Motivated by the analysis, we propose Consistency-Oriented Reasoning Alignment (CORA), which introduces thinking-answer semantic consistency into RLVR through a lightweight plug-and-play consistency reward model, and further incorporates Hybrid Reward Advantage Splitting (HRAS) to stably coordinate task and consistency optimization. Extensive experiments across representative multimodal reasoning benchmarks and mainstream LVLMs show that CORA improves task performance while effectively mitigating thinking-answer inconsistency, leading to more faithful reasoning traces.

</details>

---

### [[20_Research/Papers/具身智能/AgentSpec_Understanding_Embodied_Agent_Scaffolds_Through_Controlled_Composition|AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition]]

![[assets/2606.14674_figure.png|800]]

- **arXiv**: [2606.14674](https://arxiv.org/abs/2606.14674)
- **PDF**: https://arxiv.org/pdf/2606.14674
- **详细分析**: [[20_Research/Papers/具身智能/AgentSpec_Understanding_Embodied_Agent_Scaffolds_Through_Controlled_Composition|AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition]]
- **作者**: Jixuan Chen, Jianzhi Shen, Haoqiang Kang, Zhi Hong, Qingyi Jiang, Soham Bose, Yiming Zhang, Leon Leng, Amit Vyas, Lingjun Mao, Siru Ouyang, Kun Zhou...
- **cs 子类**: cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.95（加权：具身智能 1.2，大模型 0.75）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentGym, DeliveryBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning. While such scaffolds often improve performance, they are often embedded in tightly coupled pipelines, making it difficult to isolate component contributions, compare alternative designs, or understand how module interactions shape agent behavior. We introduce AgentSpec, a modular specification framework that represents embodied agents as typed compositions of reusable policy components with standardized interfaces. AgentSpec standardizes the interfaces among perception, memory, reasoning, reflection, action, and optional learning, enabling components to be swapped and recombined under controlled conditions. We instantiate this framework across DeliveryBench, ALFRED, MiniGrid, and RoboTHOR, and analyze reasoning, memory, reflection, and reinforcement-learning modules across model backbones. Our results show that agent performance is governed by scaffold compatibility and interaction effects rather than isolated module strength. In particular, structured multi-granularity memory improves long-horizon state tracking, reasoning and memory interact non-uniformly across environments, reflection trades off correction and cost, and RL-trained policies compose best when optimized with deployment-time scaffold structure. AgentSpec provides a controlled foundation for studying, comparing, and designing composable LLM agents. Our code, baselines and interactive playground are publicly available at https://agentspec-embodied.github.io.

</details>

---

### [[20_Research/Papers/大模型/BayLing-Duplex_Native_Full-Duplex_Speech_Dialogue_with_a_Single_Autoregressive_LLM|BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM]]

![[assets/2606.14528_figure.png|800]]

- **arXiv**: [2606.14528](https://arxiv.org/abs/2606.14528)
- **PDF**: https://arxiv.org/pdf/2606.14528
- **详细分析**: [[20_Research/Papers/大模型/BayLing-Duplex_Native_Full-Duplex_Speech_Dialogue_with_a_Single_Autoregressive_LLM|BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM]]
- **作者**: Qingkai Fang, Shoutao Guo, Yang Feng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《BayLing-Duplex: Native Full-Duplex Speech Dialogue with a Single Autoregressive LLM》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Alpaca-Eval, InstructS2S-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time, full-duplex speech interaction is a key feature of next-generation spoken chatbots, allowing the model to listen and speak at the same time and to handle natural phenomena such as overlap, hesitation, and barge-in. Existing speech language models (SpeechLMs) such as LLaMA-Omni and GLM-4-Voice are still turn-based and rely on an external Voice Activity Detection (VAD) module to mark the end of the user's turn, which fundamentally limits their interactive ability. In this paper, we introduce BayLing-Duplex, a native full-duplex SpeechLM where a single autoregressive LLM decides when to listen, when to speak, and when to stop, with no auxiliary turn-taking module. The design adds only a few special tokens to the standard vocabulary, so it transfers across LLMs and reuses existing training and serving stacks with no architectural adaptation. Starting from the public GLM-4-Voice checkpoint and using only 400K full-duplex samples for fine-tuning followed by a lightweight DPO stage, BayLing-Duplex reaches 92% turn-taking success and 100% interruption success on InstructS2S-Eval, while improving the speech-response score from 2.17 to 3.39 over Moshi. BayLing-Duplex also matches or surpasses its turn-based counterpart on Llama Questions, Web Questions, and Alpaca-Eval, showing that simultaneous listen-and-speak modeling does not sacrifice response quality.

</details>

---

### [[20_Research/Papers/大模型/Be_My_Tutor_On-Policy_Co-Distillation_for_Mutual_LLM_Improvement_via_Peer_Feedback|Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback]]

![[assets/2606.14368_figure.png|800]]

- **arXiv**: [2606.14368](https://arxiv.org/abs/2606.14368)
- **PDF**: https://arxiv.org/pdf/2606.14368
- **详细分析**: [[20_Research/Papers/大模型/Be_My_Tutor_On-Policy_Co-Distillation_for_Mutual_LLM_Improvement_via_Peer_Feedback|Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback]]
- **作者**: Woohyeon Byeon, Jiwon Jeon, Jeonghye Kim, Youngchul Sung
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SciKnowEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study multi-domain LLM training in which two models, each stronger in a different domain, co-evolve by tutoring each other through on-policy feedback. Unlike one-way distillation or single-model fine-tuning, our goal is mutual Pareto improvement: each model improves across domains without losing its original strength. To this end, we propose On-Policy Co-Distillation (OPCoD), where each student's self-distillation is conditioned on its own correct rollout and feedback from its peer. To make feedback exchange effective, OPCoD uses cognizance-based gating to decide when to give feedback and feedback anchoring to ground feedback in the problem. On Science Q\&amp;A tasks, OPCoD consistently outperforms baselines and achieves Pareto improvement across all evaluated domain pairs and students.

</details>

---

### [[20_Research/Papers/大模型/Retrospective_Progress-Aware_Self-Refinement_for_LLM_Agent_Training|Retrospective Progress-Aware Self-Refinement for LLM Agent Training]]

![[assets/2606.14302_figure.png|800]]

- **arXiv**: [2606.14302](https://arxiv.org/abs/2606.14302)
- **PDF**: https://arxiv.org/pdf/2606.14302
- **详细分析**: [[20_Research/Papers/大模型/Retrospective_Progress-Aware_Self-Refinement_for_LLM_Agent_Training|Retrospective Progress-Aware Self-Refinement for LLM Agent Training]]
- **作者**: Xinbei Ma, Congmin Zheng, Jiyang Qiu, Jiale Hong, Yao Yao, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng Zhang...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.35（加权：大模型 1.15，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Retrospective Progress-Aware Self-Refinement for LLM Agent Training》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents trained with reinforcement learning optimize step-wise action prediction but lack metacognitive awareness of task progress, inducing a gap that hinders long-horizon scaling. A pilot study reveals that online progress prompting hurts performance while retrospective demonstrations help, yet this capability cannot emerge from outcome-reward training alone. We present RePro, Retrospective Progress-Aware Training, a framework that trains agents to self-generate progress signals via a forward-then-reflect rollout paradigm: the agent executes actions online, then retrospectively reassesses its step-wise progress given the completed trajectory and known outcome. RePro initializes with a Retrospection Warmup that teaches reflection format from minimal external demonstrations, then further trains through RePro-PO with a composite reward that produces self-generated signals without continuous external supervision. Experiments on WebShop, ALFWorld, and Sokoban show that RePro enhances the Qwen family's performance, with up to $12\%$ absolute success rate gains.

</details>

---

### [[20_Research/Papers/大模型/Detecting_undisclosed_LLM-generated_content_in_parliamentary_texts|Detecting undisclosed LLM-generated content in parliamentary texts]]

![[assets/2606.14209_figure.png|800]]

- **arXiv**: [2606.14209](https://arxiv.org/abs/2606.14209)
- **PDF**: https://arxiv.org/pdf/2606.14209
- **详细分析**: [[20_Research/Papers/大模型/Detecting_undisclosed_LLM-generated_content_in_parliamentary_texts|Detecting undisclosed LLM-generated content in parliamentary texts]]
- **作者**: Minerva Suvanto, Andrea McGlinchey, Peter J. Barclay, Mattias Wahde
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Detecting undisclosed LLM-generated content in parliamentary texts》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we evaluate the extent of undisclosed LLM-generated content in texts from the parliaments of the United Kingdom and Sweden. In many areas, such as in journalism or in academic writing, there are often requirements to clearly disclose whether AI tools, such as LLMs, have been used. In the case of parliamentary texts, the guidelines on disclosure of AI use are more vague. However, in order to maintain transparency and retain public trust, it is generally recommended that parliamentarians should state whether or not they have used AI when writing texts, such as parliamentary motions. Here, we train an interpretable (glass-box) text classifier using pre-LLM parliamentary texts and LLM-generated versions of such texts. We then apply the classifier to a test set containing recent parliamentary texts, finding a steady increase in undisclosed LLM use, in both parliaments, from 2022 onwards.

</details>

---

### [[20_Research/Papers/大模型/CacheRL_Multi-Turn_Tool-Calling_Agents_via_Cached_Rollouts_and_Hybrid_Reward|CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward]]

![[assets/2606.14179_figure.png|800]]

- **arXiv**: [2606.14179](https://arxiv.org/abs/2606.14179)
- **PDF**: https://arxiv.org/pdf/2606.14179
- **详细分析**: [[20_Research/Papers/大模型/CacheRL_Multi-Turn_Tool-Calling_Agents_via_Cached_Rollouts_and_Hybrid_Reward|CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward]]
- **作者**: Md Amirul Islam, Sumiran Thakur, Huancheng Chen, Su Min Park, Jiayun Wang, Gyuhak Kim
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.05（加权：大模型 0.65，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CacheRL, MT-Bench, SWE-RL, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less compute. Our approach addresses three challenges in practical agent training: transferring tool-calling knowledge from large models at scale, enabling reinforcement learning without costly live tool execution, and learning robustly from noisy cached environments. CacheRL introduces three key innovations. First, a hybrid thinking trajectory pipeline augments agent trajectories with LLM-generated reasoning traces, producing training examples that teach models not only what tools to call but also why. Second, the CacheAgentLoop eliminates live execution costs through a three-tier fuzzy cache while preserving trajectory fidelity using token-level masking. Third, a cache-tier-aware reward dynamically adjusts answer-quality weights to avoid penalizing models for cache-induced limitations. Through iterative supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO), CacheRL improves Qwen3-4B-Thinking's validation reward from 0.43 to 0.78. On public agentic tool-calling benchmarks, our model achieves competitive performance against frontier models such as GPT-5. Ablation studies show that removing knowledge transfer reduces performance by 41 percent, while cache-aware rewards contribute a 17 percent improvement. Interestingly, reinforcement learning improves training stability but yields limited gains beyond strong supervised fine-tuning, suggesting that data quality and reward design play a more important role than complex optimization methods in building practical small agent models.

</details>

---

### [[20_Research/Papers/大模型/CoRe_A_Continuously_Reward-Finetuned_LLM_Query_Rewriter_for_Multi-Stage_Context-Aware_Relevance_in_Web-Scale_Video_Search|CoRe: A Continuously Reward-Finetuned LLM Query Rewriter for Multi-Stage Context-Aware Relevance in Web-Scale Video Search]]

![[assets/2606.14127_figure.png|800]]

- **arXiv**: [2606.14127](https://arxiv.org/abs/2606.14127)
- **PDF**: https://arxiv.org/pdf/2606.14127
- **详细分析**: [[20_Research/Papers/大模型/CoRe_A_Continuously_Reward-Finetuned_LLM_Query_Rewriter_for_Multi-Stage_Context-Aware_Relevance_in_Web-Scale_Video_Search|CoRe: A Continuously Reward-Finetuned LLM Query Rewriter for Multi-Stage Context-Aware Relevance in Web-Scale Video Search]]
- **作者**: Yilin Wen, Rong Yang, Xiaojia Chang, Hong Sun, Gefu Tang, Chunhui Liu, Jeffrey Chen, Zeyu Ma, Lisong Qiu, Xiaochuan Fan, Congjia Yu, Quan Zhou...
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《CoRe: A Continuously Reward-Finetuned LLM Query Rewriter for Multi-Stage Context-Aware Relevance in Web-Scale Video Search》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based query rewriters in production face a tension: the training reward must reflect how the rewrite is consumed by the production ranker, yet the training procedure must be cheap enough to support continuous redeployment as data drifts. We present CoRe (Context Relevance), such a system, redeployed weekly for over five months in a major short-video search engine. Our reward uses the deployed multimodal relevance model as its source and a multiplicative ratio form mirroring the production fusion algebra, closing the simulation-production gap that offline reward proxies leave open. A semi-online Mixed Preference Optimization loop makes this reward affordable at multi-million-instance weekly scale: a DPO-style pairwise objective restricts the gradient pass to a small top-k/bottom-k subset of sampled trajectories, and a phase structure reduces trainer/inference-server parameter syncs from per-step to per-phase. An automated promotion gate over reward-like and stability metrics detected and recovered from a real reward-hacking incident in production. Rewriter output is consumed as parallel relevance signals at recall, rawrank, and finerank without displacing the original signals, bounding rewriter-failure blast radius. Online A/B from two sequential production launches, first deploying the rewriter at finerank, then extending consumption to recall and rawrank, delivers statistically significant reductions in change-query rate on rewrite-impacted queries, with all headline relevance and engagement metrics moving in the expected direction.

</details>

---

### [[20_Research/Papers/大模型/Dialogue_SWE-Bench_A_Benchmark_for_Dialogue-Driven_Coding_Agents|Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents]]

![[assets/2606.13995_figure.png|800]]

- **arXiv**: [2606.13995](https://arxiv.org/abs/2606.13995)
- **PDF**: https://arxiv.org/pdf/2606.13995
- **详细分析**: [[20_Research/Papers/大模型/Dialogue_SWE-Bench_A_Benchmark_for_Dialogue-Driven_Coding_Agents|Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents]]
- **作者**: Brendan King, Jeffrey Flanigan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Dialo-SWE-Bench, Dialogue-SWEBench, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI coding agents have rapidly transformed software engineering, powering widely used interactive coding assistants. Despite their interactive real-world use, existing benchmarks evaluate them as fully-autonomous systems. In this work, we introduce Dialogue SWE-Bench, an automatic benchmark dataset for evaluating the ability of coding agents to resolve real-world software engineering problems through dialogue with a user. We design a novel, persona-grounded user simulator to support our task evaluation, and augment our task evaluation with automatic evaluations of dialogue quality. We also propose a new schema-guided agent, aimed at improving the dialogue capabilities of off-the-shelf coding agents, which improves over strong baselines by 3-14%. Our results indicate that better coding models do not always correspond to better dialogue models, suggesting that dialogue capability is a distinct and currently understudied dimension of coding agent performance.

</details>

---

### [[20_Research/Papers/大模型/MedLatentDx_Latent_Multi-Agent_Communication_for_Cross-Hospital_Rare-Disease_Diagnosis|MedLatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis]]

![[assets/2606.13945_first_page.png|800]]

- **arXiv**: [2606.13945](https://arxiv.org/abs/2606.13945)
- **PDF**: https://arxiv.org/pdf/2606.13945
- **详细分析**: [[20_Research/Papers/大模型/MedLatentDx_Latent_Multi-Agent_Communication_for_Cross-Hospital_Rare-Disease_Diagnosis|MedLatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis]]
- **作者**: Ziqing Wang, Lili Zhao, Kaize Ding
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MedLatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：CrossRare-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rare diseases affect over $300$ million patients across more than $7{,}000$ conditions, yet no single hospital encounters enough cases of any one condition for reliable diagnosis. Cross-hospital collaboration could help by allowing a diagnosing institution to use distributed, case-specific diagnostic evidence, but privacy regulations restrict the transmission of identifiable clinical text across institutional boundaries. This setting raises two challenges: existing medical agent systems often rely on textual evidence exchange, while raw latent states such as hidden states and KV caches may still reveal prompt-derived clinical content. We introduce MedLatentDx, a latent multi-agent communication framework in which hospital agents keep private clinical records and retrieved cases local, and send compact latent KV blocks to a host agent for rare-disease diagnosis. MedLatentDx supports two deployment settings: same-backbone hospital agents use latent KV distillation, while hospitals with different LLM backbones use cross-family latent alignment. On CrossRare-Bench, a self-built large-scale rare-disease benchmark with hospital-level partitions, MedLatentDx improves cross-hospital diagnostic performance while reducing reconstructable clinical content relative to raw-latent communication baselines.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Speaker_Identification_in_Classroom_Environments|Multimodal Speaker Identification in Classroom Environments]]

![[assets/2606.13712_figure.png|800]]

- **arXiv**: [2606.13712](https://arxiv.org/abs/2606.13712)
- **PDF**: https://arxiv.org/pdf/2606.13712
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Speaker_Identification_in_Classroom_Environments|Multimodal Speaker Identification in Classroom Environments]]
- **作者**: Michael L. Chrzan, Meghavarshini Krishnaswamy, Robert Gibboni, Katie Wetstone, Wei Ai, Jing Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Multimodal Speaker Identification in Classroom Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated analysis of K-12 classroom dynamics faces challenges due to background noise and variable child speech, often confounding acoustic-only models. This study evaluates a multimodal speaker identification framework anchoring acoustic embeddings with LLM-derived semantic context. Using a subset of the EDSI dataset (8 math classrooms, N = 2,801 utterances), we found an acoustic baseline (ECAPA-TDNN) achieved only 39.0% accuracy. By integrating transcript-based "contextual anchoring" into a gradient boosting classifier, our multimodal approach raised student identification to 50.3%. Performance also improved for utterances over 5 seconds, reaching 76.9% accuracy (vs. 64.9% baseline) with a 90.9% Top-3 accuracy. Additionally, the model distinguished teacher vs. student roles with 99.3% accuracy. This approach advances the feasibility of automated feedback systems capable of considering individual student participation, a crucial step for supporting equitable instruction at scale.

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_Web_Agent_Safety_under_E-commerce_Deceptive_Interfaces|Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces]]

![[assets/2606.13686_figure.png|800]]

- **arXiv**: [2606.13686](https://arxiv.org/abs/2606.13686)
- **PDF**: https://arxiv.org/pdf/2606.13686
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_Web_Agent_Safety_under_E-commerce_Deceptive_Interfaces|Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces]]
- **作者**: Zijing Shi, Meng Fang, Ling Chen
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As autonomous web agents are increasingly deployed to perform real-world tasks, ensuring their safety has become a critical concern. In this work, we study web agent behavior under realistic deceptive interfaces in the e-commerce domain. We introduce WebDecept, a lightweight and configurable plugin framework that enables controlled injection of deceptive interface patterns into existing web environments. Using WebDecept, we instantiate seven deceptive patterns commonly observed on the open web, including targeted advertisements, domain redirection, and shopping manipulation. By injecting these patterns into the frontend during task execution, we perform controlled evaluation of multiple multimodal web agents. Our results show that current web agents are highly susceptible to multiple classes of deceptive interfaces, and that prompt-based constraints are often insufficient to mitigate these failures. We further analyze how the design choices of deceptive patterns influence the success of such manipulations. These findings highlight safety challenges that should be addressed as web agents are scaled toward real-world deployment.

</details>

---
