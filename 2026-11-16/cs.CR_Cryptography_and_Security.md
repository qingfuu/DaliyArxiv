# cs.CR | Cryptography and Security | 2026-11-16

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Forget_the_Lineage_Forward-Secure,_Lineage-Complete_Cryptographic_Erasure_for_LLM-Agent_Memory|Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory]]

![[assets/2611.18133_first_page.png|800]]

- **arXiv**: [2611.18133](https://arxiv.org/abs/2611.18133)
- **PDF**: https://arxiv.org/pdf/2611.18133
- **详细分析**: [[20_Research/Papers/大模型/Forget_the_Lineage_Forward-Secure,_Lineage-Complete_Cryptographic_Erasure_for_LLM-Agent_Memory|Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory]]
- **作者**: Yulliwas Ameur, Billal Mokhtari, Samia Bouzefrane
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents keep a long-term memory that the model itself writes: summaries, extracted facts and embeddings derived from what users said. Deleting a message is therefore not enough: its derivatives, storage residue and backups survive. We define lineage-complete forward-secure erasure: after a forget request, an adversary that later obtains all storage and the agent's current keys learns nothing about the forgotten input or any memory derived from it. We present LinEra, which encrypts each memory under a key derived from its parents' keys along the derivation graph; source keys come from a puncturable pseudorandom function, so forgetting is a single puncture and every descendant becomes unreadable without being located. A sound lineage rule records as parents everything the writer saw, which confines all influence of a source to its descendants. We prove security and lineage integrity and integrate LinEra with mem0. With real LLMs from two families (1.5B to 7B parameters) writing the memory of LoCoMo conversations, an attacker holding every file and the current keys recovers, on all ten conversations written by the largest model, 70 of 71 forgotten secrets after logical deletion, 67 with per-object or epoch keys, and none with LinEra; the same holds for every writer tested. The price is a larger forgetting radius, which follows a simple law in the writer's fan-in: forgetting 1% of turns erases 73.0% of derived memories with session-level summaries but only 3.8% with four-turn windows, which also answer better; re-deriving restores what is lost.

</details>

---

### [[20_Research/Papers/大模型/I2C-GRPO_Insight_Importance_Checklist_for_Reinforcement_Learning_in_a_Multi-Agent_DDoS_Alert_Triage_Workflow|I2C-GRPO: Insight Importance Checklist for Reinforcement Learning in a Multi-Agent DDoS Alert Triage Workflow]]

![[assets/2611.17534_figure.png|800]]

- **arXiv**: [2611.17534](https://arxiv.org/abs/2611.17534)
- **PDF**: https://arxiv.org/pdf/2611.17534
- **详细分析**: [[20_Research/Papers/大模型/I2C-GRPO_Insight_Importance_Checklist_for_Reinforcement_Learning_in_a_Multi-Agent_DDoS_Alert_Triage_Workflow|I2C-GRPO: Insight Importance Checklist for Reinforcement Learning in a Multi-Agent DDoS Alert Triage Workflow]]
- **作者**: Eyal Zloof, Shaun Shuster, Aviram Zilberman, Chen Frydman, Inderjeet Singh, Andrés Murilo, Asaf Shabtai, Yuval Elovici, Rami Puzis
- **cs 子类**: cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.8（加权：大模型 0.8，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《I2C-GRPO: Insight Importance Checklist for Reinforcement Learning in a Multi-Agent DDoS Alert Triage Workflow》归入 强化学习、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly used for investigative tasks over incomplete evidence, such as cybersecurity alert triage, but reinforcement learning (RL) for such tasks is difficult: intermediate steps have no verifiable labels, rollouts are costly, and outcome rewards are sparse. We propose Insight Importance Checklist (I2C)-GRPO, a checklist reward for intermediate investigation steps. For each decision point, a panel of expert LLMs proposes investigative actions, their atomic forensic insights are extracted, and a separate three-model ranker panel orders the insights by importance. A reward model checks which ranked insights a candidate action targets and returns their consensus-weighted coverage. Because actions are scored without being executed, the reward is a proxy for expected investigative value, and training reduces to a one-step contextual bandit over fixed investigation prefixes. From a soft-computing perspective, the reward is an additive fuzzy measure whose rank-exponent weights act as an ordered weighted averaging (OWA)-type operator; one exponent sets its orness, i.e., how strongly the reward concentrates on the top of the judges' consensus. We train an open-weight Qwen3-4B Triage Agent within a fixed multi-agent Distributed Denial of Service (DDoS) alert-triage workflow on DARPA 2000 LLDOS 1.0 and test it on an independent CSE-CIC-IDS2018 DDoS trace. Across three training seeds, the agent reaches a mean F1-score of 0.869, 5.9 and 9.7 points above uniform insight weights and DIVA, and a false-positive rate of 4.9% versus 16.4% for GPT-5-mini. Within the weighting family, false positives fall only at the highest-orness weighting evaluated. All claims are limited to DDoS alert triage; the code, task contexts, and ranked insight dataset will be released.

</details>

---
