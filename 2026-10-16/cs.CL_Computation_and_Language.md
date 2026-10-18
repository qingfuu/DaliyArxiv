# cs.CL | Computation and Language | 2026-10-16

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/Hy-Memory-30B-A3B_Attributed_Reinforcement_Learning_for_Long-Term_Memory_Writing|Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing]]

![[assets/2610.22196_first_page.png|800]]

- **arXiv**: [2610.22196](https://arxiv.org/abs/2610.22196)
- **PDF**: https://arxiv.org/pdf/2610.22196
- **详细分析**: [[20_Research/Papers/大模型/Hy-Memory-30B-A3B_Attributed_Reinforcement_Learning_for_Long-Term_Memory_Writing|Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing]]
- **作者**: Tianxiang Fei, Jiazheng Kang, Mao Zheng, Xingyan He, Xiang Yu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.95（加权：大模型 0.35，强化学习 0.6）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

External-memory systems extend language-model applications beyond a context window, but their quality depends critically on the model executing the write path: deciding what to retain, how precisely to represent it, and how new evidence should update persistent state. Existing frameworks typically place a general-purpose large language model behind framework-specific prompts. This raises serving cost, and a writer specialized for one protocol does not transfer directly to another; a unified model that can operate across established memory frameworks remains largely unexplored. We present Hy-Memory-30B-A3B, a compact long-term-memory writer trained across Mem0, MemOS, and Hy-Memory. Memory On-Policy Distillation teaches framework-specific write protocols on student-generated states; Memory RL then optimizes downstream answerability using dense per-chunk probes, attributed cross-chunk rewards, over-storage controls, and chunk-level GRPO. Carrying policy-written banks across windows keeps training aligned with deployment. On fixed 20% benchmark subsamples, Hy-Memory-30B-A3B ranks first on all four evaluated harnesses, including held-out EverMemOS, with a 55.49% macro average versus 54.62% for Claude Opus 5.

</details>

---

### [[20_Research/Papers/大模型/TEM_Temporal_State_Tracking_Memory_for_Large_Language_Model_Agents|TEM: Temporal State Tracking Memory for Large Language Model Agents]]

![[assets/2610.21900_first_page.png|800]]

- **arXiv**: [2610.21900](https://arxiv.org/abs/2610.21900)
- **PDF**: https://arxiv.org/pdf/2610.21900
- **详细分析**: [[20_Research/Papers/大模型/TEM_Temporal_State_Tracking_Memory_for_Large_Language_Model_Agents|TEM: Temporal State Tracking Memory for Large Language Model Agents]]
- **作者**: Pengfeng Song, Yunkai Zhuang, Liye Shi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TEM: Temporal State Tracking Memory for Large Language Model Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongBench, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An agent's memory must remain useful as information changes across conversations. A new fact may replace an earlier value without making that value irrelevant to a later question. We present Temporal State Tracking Memory (TEM), a training-free framework for tracking these changes. TEM stores facts as versioned records linked to their sources. It retrieves relevant versions, places them in source order and labels historical records before passing the evidence to the answer model. Event memory and original dialogue turns provide details missing from structured facts. We evaluated TEM on 420 questions drawn from 600 sessions involving 60 personas. Across four open-weight models, key-entity hit rates reached 75.71-97.62% overall and 96.67-100.00% on the historical-residence subset. Adding historical labels to otherwise identical, source-ordered facts increased overall hit rates by 17.14-55.95 percentage points. The evidence was compact: 94-118 tokens per answer, or 48.75-56.73% less than session-aware retrieval-augmented generation (RAG). A further evaluation on 1,540 LoCoMo questions tested hybrid memory under a fixed evidence budget. TEM exceeded session-aware RAG with both backbones; conservative score differences were 7.92 and 10.58 percentage points. The results support preserving fact versions and exposing their temporal status to the generator when answering questions about repeatedly updated information.

</details>

---

### [[20_Research/Papers/强化学习/Ranking_and_Partitioning_of_Attention_Heads_for_Sparse_and_Continual_Reinforcement_Learning_Fine-tuning|Ranking and Partitioning of Attention Heads for Sparse and Continual Reinforcement Learning Fine-tuning]]

![[assets/2610.21336_first_page.png|800]]

- **arXiv**: [2610.21336](https://arxiv.org/abs/2610.21336)
- **PDF**: https://arxiv.org/pdf/2610.21336
- **详细分析**: [[20_Research/Papers/强化学习/Ranking_and_Partitioning_of_Attention_Heads_for_Sparse_and_Continual_Reinforcement_Learning_Fine-tuning|Ranking and Partitioning of Attention Heads for Sparse and Continual Reinforcement Learning Fine-tuning]]
- **作者**: Ruizhe Shi, Zaiwen Yang, Qiubo Wang, Banghua Zhu, Maryam Fazel
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Ranking and Partitioning of Attention Heads for Sparse and Continual Reinforcement Learning Fine-tuning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study sparse and continual reinforcement learning fine-tuning of language models through attention-head ranking and partitioning. For sparse learning, we rank attention heads by gradient norm to identify a small subset of heads that can be trained effectively. For continual learning, we partition heads across tasks to reduce cross-task interference and preserve previously learned capabilities. Theoretically, we relate gradient norm to training effectiveness, and further characterize why sparse, separated head updates can remain stable. Empirically, across math, instruction-following, and coding tasks, tuning higher-ranked heads consistently outperforms tuning lower-ranked ones while often matching denser baselines, and head partitioning improves retention while preserving adaptation to new tasks.

</details>

---

### [[20_Research/Papers/强化学习/Gibbs-Gap_Policy_Optimization_for_Off-Policy_RL_with_Verifiable_Rewards|Gibbs-Gap Policy Optimization for Off-Policy RL with Verifiable Rewards]]

![[assets/2610.20814_first_page.png|800]]

- **arXiv**: [2610.20814](https://arxiv.org/abs/2610.20814)
- **PDF**: https://arxiv.org/pdf/2610.20814
- **详细分析**: [[20_Research/Papers/强化学习/Gibbs-Gap_Policy_Optimization_for_Off-Policy_RL_with_Verifiable_Rewards|Gibbs-Gap Policy Optimization for Off-Policy RL with Verifiable Rewards]]
- **作者**: Xuanchang Zhang, Tong Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Gibbs-Gap Policy Optimization for Off-Policy RL with Verifiable Rewards》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MaxRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards often trains language models on responses generated by a different, possibly stale behavior policy. Correcting this mismatch with learner-to-behavior importance weights can introduce high variance for long responses. We introduce Gibbs-Gap Policy Optimization (GGPO), which minimizes a log-mean-exp contrast of KL-adjusted rewards among responses to the same prompt, without learner-to-behavior importance weights. We derive GGPO from KL-regularized policy optimization: on policy, its population loss is exactly the KL-regularized optimality gap, and under suitable coverage the learner's single-response expected reward is at least the behavior policy's best-of-$K$ reward, minus terms for the raw finite-group loss, regularization, and finite training data. We characterize reference refresh through exact Gibbs-target composition and a finite-data final-policy reward bound under local reference control and tokenwise behavior mismatch. This refresh is empirically important: in an ablation, fixed-reference GGPO scores $32.96$ on the five-benchmark problem-weighted average, versus $46.58$ with the default refresh schedule. Experiments on mathematical reasoning further show that GGPO outperforms GRPO and AGRO under training-inference mismatch and on fixed offline data, while maintaining its performance as controlled policy staleness grows.

</details>

---
