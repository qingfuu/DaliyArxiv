# cs.CL | Computation and Language | 2026-09-21

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/An_Interpretable_Memory_Decision_Controller_for_LLM_Agents_Based_on_Three-Signal_Complementarity_Decoupling_Confidence_and_Consistency|An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency]]

![[assets/2609.22043_figure.png|800]]

- **arXiv**: [2609.22043](https://arxiv.org/abs/2609.22043)
- **PDF**: https://arxiv.org/pdf/2609.22043
- **详细分析**: [[20_Research/Papers/大模型/An_Interpretable_Memory_Decision_Controller_for_LLM_Agents_Based_on_Three-Signal_Complementarity_Decoupling_Confidence_and_Consistency|An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency]]
- **作者**: Yiming Zhang, Jinghong Zhang, Haoran Zhao, Yiren Ma, Chunlei Zhao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HaluEval, TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memory store contains conflicting positions, standard retrieval-augmented generation (RAG) blindly injects memories and amplifies hallucinations: in models susceptible to memory injection, the RAG hallucination rate under conflicting memories is markedly higher than that of a memory-free baseline. Inspired by memory signaling mechanisms in the prefrontal cortex, we propose the Memory Decision Layer (MDL), a zero-parameter memory decision controller situated between the retrieval and generation stages. Its core is a three-signal complementary encoder that fuses relevance, reliability, and task risk through QR-based orthogonal subspace projection and a meta-working-memory signal into an interpretable decision representation that quantifies the trustworthiness of retrieved memories. Building on this encoder, MDL explicitly decouples confidence from consistency and introduces risk inversion and explicit abstention. Evaluations on mainstream large language models and multiple open-source datasets show that MDL reduces the hallucination rate under conflicting memories by about 56.04% in general scenarios and approaches zero hallucination in high-risk scenarios. The controller is fully white-box: it relies purely on geometric operations, requires no trained parameters, and adds only about 0.14 ms per decision -- roughly 50x faster than the embedding-retrieval step that precedes it and four to five orders of magnitude faster than an LLM self-evaluation call.

</details>

---

### [[20_Research/Papers/大模型/MIRAGE_Multi-Perspective_Creative_Language_Model_Reasoning_with_Reinforcement_Learning_Guidance|MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance]]

![[assets/2609.21554_figure.png|800]]

- **arXiv**: [2609.21554](https://arxiv.org/abs/2609.21554)
- **PDF**: https://arxiv.org/pdf/2609.21554
- **详细分析**: [[20_Research/Papers/大模型/MIRAGE_Multi-Perspective_Creative_Language_Model_Reasoning_with_Reinforcement_Learning_Guidance|MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance]]
- **作者**: Arash Lagzian, Srinivas Anumasa, Dianbo Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 0.65，强化学习 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in Large Language Models (LLMs) have revolutionized artificial intelligence and how human interact with AIs. Despite impressive advancements, LLMs struggle with complex mathematical, scientific, and logical tasks. Inspired by human cognitive flexibility - our ability to dynamically switch mental perspectives - we propose MIRAGE (Multi-perspective Inference-time Reasoning via Agent-Guided Exploration), a novel inference-time creative thinking framework. MIRAGE includes a Selector that prioritizes effective conceptual perspectives (e.g., algebraic, probabilistic) and a Reasoner that sequentially solves tasks until a confident solution emerges, otherwise aggregating multiple perspectives. Tested on GSM8K, MATH500, MMLU-Pro, and Game-of-24 benchmarks, MIRAGE consistently outperforms methods like Chain-of-Thought and diverse prompting ensembles, significantly boosting accuracy with minimal inference overhead, providing a scalable solution for practical applications.

</details>

---

### [[20_Research/Papers/大模型/ArenaFlow_From_Trajectory_Ranking_to_Hierarchical_Credit_Propagation_for_Open-Ended_Agent_RL|ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL]]

![[assets/2609.21378_figure.png|800]]

- **arXiv**: [2609.21378](https://arxiv.org/abs/2609.21378)
- **PDF**: https://arxiv.org/pdf/2609.21378
- **详细分析**: [[20_Research/Papers/大模型/ArenaFlow_From_Trajectory_Ranking_to_Hierarchical_Credit_Propagation_for_Open-Ended_Agent_RL|ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL]]
- **作者**: Qiang Zhang, Ruixue Ding, Fanrui Zhang, Xi Chen, Boli Chen, Shihang Wang, Yinfeng Huang, Yi Zheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.15（加权：大模型 0.95，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ArenaRL, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain. Recent pairwise evaluation methods alleviate reward discrimination collapse by replacing pointwise scoring with relative preferences. However, they still compress rich comparative feedback into a single trajectory-level reward, obscuring decisive intermediate steps and preventing successful behaviors from being consolidated into reusable skills. We propose ArenaFlow, a hierarchical credit propagation framework for open-ended agent reinforcement learning. ArenaFlow leverages tournament-based relative ranking to derive trajectory-level reward signals. Each comparison is further equipped with structured reflective evaluation, which reveals three types of supervision: pivotal success steps, reusable strategy skills, and usage attribution of retrieved skills. At the step level, ArenaFlow propagates trajectory-level advantages to high-confidence pivotal steps according to tournament survival depth, enabling more targeted optimization of local reasoning behaviors. At the skill level, ArenaFlow estimates skill utility from group-level usage attribution and maintains a global skill memory through utility-aware updating, pruning, and retrieval. The resulting high-utility skills further serve as policy priors for future exploration. Extensive experiments validate ArenaFlow's effectiveness on open-ended agent tasks.

</details>

---
