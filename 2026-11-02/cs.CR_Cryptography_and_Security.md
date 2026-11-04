# cs.CR | Cryptography and Security | 2026-11-02

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/What_Standard_Evaluations_Hide_About_Detectors_of_Hijacked_LLM_Agents_Rare_Attacks,_Unseen_Tools_and_Benchmark_Transfer|What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer]]

![[assets/2610.41803_first_page.png|800]]

- **arXiv**: [2610.41803](https://arxiv.org/abs/2610.41803)
- **PDF**: https://arxiv.org/pdf/2610.41803
- **详细分析**: [[20_Research/Papers/大模型/What_Standard_Evaluations_Hide_About_Detectors_of_Hijacked_LLM_Agents_Rare_Attacks,_Unseen_Tools_and_Benchmark_Transfer|What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer]]
- **作者**: Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ATBench, DriftNet, RAS-Eval, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited, attacks or anomalies make up 16% to 86% of the test samples, no evaluation varies that share, and six report no test on data from a second benchmark or source. We ask what such evaluations hide. On the AgentDrift and AgentDojo benchmarks we test trained detectors that read tool identities, behavior, call sequences, step embeddings or text, and a released LLM action monitor, AlignmentCheck, with thresholds fixed on training data or set by the monitor's released decision rule. First, at a 2% attack rate a detector with an area under the receiver operating characteristic curve (AUROC) of 0.879 reaches a precision of 0.076, and the mix of negatives alone moves that precision between 0.039 and 0.117. Second, as tool coverage, the share of test tool calls whose tool was seen in training, falls, detector rankings cross near 50% coverage and reverse below it, because unseen tools map to inputs that training never reached. Dropout on tool inputs largely removes the reversal. Third, no detector trained on AgentDrift ranks AgentDojo traces better than chance (AUROC 0.47 to 0.52), including one that reaches 0.996 within AgentDojo. The monitor, trained on neither, reaches 0.930, but with its open backbone its released decision rule would still mostly raise false alerts at a 2% attack rate (precision 0.096). We turn these findings into a checklist for evaluating trace detectors.

</details>

---

### [[20_Research/Papers/强化学习/Communication-Efficient_Private_Federated_Reinforcement_Learning_with_Post-Quantum_Authentication_for_Vehicular_Networks|Communication-Efficient Private Federated Reinforcement Learning with Post-Quantum Authentication for Vehicular Networks]]

![[assets/2610.41055_figure.png|800]]

- **arXiv**: [2610.41055](https://arxiv.org/abs/2610.41055)
- **PDF**: https://arxiv.org/pdf/2610.41055
- **详细分析**: [[20_Research/Papers/强化学习/Communication-Efficient_Private_Federated_Reinforcement_Learning_with_Post-Quantum_Authentication_for_Vehicular_Networks|Communication-Efficient Private Federated Reinforcement Learning with Post-Quantum Authentication for Vehicular Networks]]
- **作者**: Hojat Allah Salehi, Devrim Aras, Md Jueal Mia, M. Hadi Amini, Imtiaz Karim, Mashrur Chowdhury, Bhavani Thuraisingham
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Communication-Efficient Private Federated Reinforcement Learning with Post-Quantum Authentication for Vehicular Networks》归入 强化学习、世界模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated reinforcement learning supports cooperative vehicular routing without centralizing trajectory data, but model updates may reveal private information and incur communication overhead over intermittent vehicle-to-infrastructure links, particularly when post-quantum authentication is required. We study correlated private quantization, using complementary shared randomness between paired vehicles to reduce aggregation mean squared error while preserving the marginal parameter-level local differential privacy and one-bit communication cost of independent quantization. A tunable extension mixes shared and independent randomness to bound privacy leakage given paired outputs and shared-randomness side information. For this extension, Rényi differential privacy accounting establishes vector-level local differential privacy for one model upload even when pairings are revealed. Under matched vector-level privacy and identical local and global parameters, the extension yields 16.5% lower analytical aggregation mean squared error than independent quantization. We evaluate cooperative routing by coupling traffic simulation with packet-level simulation of post-quantum-authenticated vehicle-to-infrastructure communication. Compared to full-precision updates, one-bit uploads reduce authenticated uplink size by 92.4% and increase mean verified updates aggregated per round from 19.6 to 26.5. Under mobility-constrained communication at a parameter-level privacy budget of 1, correlated private quantization reduces mean travel time by 14.3% relative to independent quantization at the same budget and communication cost. At a parameter-level privacy budget of 0.3, a vehicle-origin inference attack trained on independent simulations reaches 30% accuracy with correlated private quantization and 22% with independent quantization after 100 rounds, versus 91% without privacy and 10% for random guessing.

</details>

---
