# cs.IR | Information Retrieval | 2026-05-28

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Affective_Music_Recommendation_A_Rollout-Based_World_Model_for_Offline_Preference_Optimization|Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization]]

![[assets/2605.28810_figure.png|800]]

- **arXiv**: [2605.28810](https://arxiv.org/abs/2605.28810)
- **PDF**: https://arxiv.org/pdf/2605.28810
- **详细分析**: [[20_Research/Papers/强化学习/Affective_Music_Recommendation_A_Rollout-Based_World_Model_for_Offline_Preference_Optimization|Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization]]
- **作者**: Audrey Chan, Aaron Labbé, Jacob Lavoie, Jordan Bannister, Arsène Fansi Tchango, Guillaume Lajoie, Laurent Charlin
- **cs 子类**: cs.IR, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization》归入 世界模型、强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KuaiSim, RecSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Functional music applications, from consumer focus and sleep aids to clinical interventions, share a distinctive recommendation problem: success is defined by the listener's affective state, but online experimentation on emotion is ethically constrained, particularly for clinical populations who cannot reliably skip a song or report distress. We describe AMRS, the Affective Music Recommendation System deployed on LUCID's health-and-wellness platforms, which serve clinical users (primarily older adults with neurocognitive conditions) and consumer-wellness users across energize, focus, calm, and sleep modes. AMRS is built around a rollout-based world model: a causal transformer trained on logged listening data to jointly predict engagement, binary rating, and self-reported valence and arousal. The world model serves both as an in-silico simulator for offline policy training and as a stress-testing tool before deployment. A recommender policy initialized by behaviour cloning is fine-tuned offline with Direct Preference Optimization (DPO) against a configurable multi-objective utility function. Under a strict cold-start protocol, the world model predicts both behavioural and affective signals with usable fidelity; DPO improves predicted valence and arousal over the cloned baseline while maintaining a similar diversity profile and avoiding the distributional collapse produced by greedy optimization. We position the work as an early deployed validation of a methodology for affective recommendation when online experimentation is ethically untenable.

</details>

---

### [[20_Research/Papers/大模型/Mixture-of-Experts_Knowledge_Graph_Retrieval-Augmented_Generation_for_Multi-Agent_LLM-based_Recommendation|Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent LLM-based Recommendation]]

![[assets/2605.28175_figure.png|800]]

- **arXiv**: [2605.28175](https://arxiv.org/abs/2605.28175)
- **PDF**: https://arxiv.org/pdf/2605.28175
- **详细分析**: [[20_Research/Papers/大模型/Mixture-of-Experts_Knowledge_Graph_Retrieval-Augmented_Generation_for_Multi-Agent_LLM-based_Recommendation|Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent LLM-based Recommendation]]
- **作者**: Shijie Wang, Chengyi Liu, Yujuan Ding, Shanru Lin, See-Kiong Ng, Xu Xin, Wenqi Fan
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 1.4，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent LLM-based Recommendation》归入 大模型、强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have recently been adopted for recommendations due to their ability to understand user intent and item semantics. However, LLM-based recommender systems often rely on parametric knowledge and suffer from outdated knowledge, motivating knowledge graph retrieval-augmented generation (KG-RAG) to ground recommendations on structured, up-to-date KGs. Despite this promise, effective KG-RAG in recommendations faces great challenges. First, users' queries vary in complexity and require KG knowledge at different granularities, whereas existing methods adopt a one-size-fits-all retrieval strategy, leading to over-retrieval for simple queries and under-retrieval for complex ones. In addition, augmenting LLMs with KG knowledge requires translating graph-structured data into linear text, which may introduce noise and cause structural information loss. Moreover, the selection of retrieval granularity lacks direct supervision and must be inferred from the final recommendation after alignment and downstream utilization, making query-aware retrieval hard to learn end-to-end. To address these issues, we propose MixRAGRec, a cooperative multi-agent framework for KG-RAG recommendations. MixRAGRec integrates a Mixture-of-Experts Retrieval Agent that routes each query to a KG retrieval expert with different granularities, a Knowledge Preference Alignment Agent that converts structured knowledge into LLM-friendly natural language, and a Contrastive Learning-reinforced Recommendation Agent trained with contrastive preference feedback. Notably, we introduce Mixture-of-Experts Multi-Agent Policy Optimization (MMAPO) to train three agents under a unified objective. Extensive experiments on real-world datasets demonstrate the effectiveness of our framework.

</details>

---
