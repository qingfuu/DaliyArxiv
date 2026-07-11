# cs.CR | Cryptography and Security | 2026-07-09

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/强化学习/Unlearning_to_Protect_A_Distilled_Reinforcement_Learning_Framework_with_Privacy-Preserving_Feature_Unlearning_and_XAI_for_IoT_Security|Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security]]

![[assets/2607.07635_figure.png|800]]

- **arXiv**: [2607.07635](https://arxiv.org/abs/2607.07635)
- **PDF**: https://arxiv.org/pdf/2607.07635
- **详细分析**: [[20_Research/Papers/强化学习/Unlearning_to_Protect_A_Distilled_Reinforcement_Learning_Framework_with_Privacy-Preserving_Feature_Unlearning_and_XAI_for_IoT_Security|Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security]]
- **作者**: Md. Nahid Hasan, Golam Rabiul Alam
- **cs 子类**: cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security》归入 强化学习 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Botnets pose a significant cybersecurity threat, enabling attacks such as DDoS, data theft, and service disruptions on IoT devices. These devices often lack built-in botnet traffic filtering, leaving them highly exposed. Existing AI-based solutions improve detection capabilities but have limitations: (i) they are too heavy for IoT deployment, and (ii) they lack unlearning capabilities to forget sensitive or outdated features without retraining. To address these challenges, we propose DiRLU, a lightweight, reinforcement learning driven framework, while ensuring privacy by selectively unlearning sensitive or outdated features without requiring retraining. The framework leverages knowledge distillation to transfer knowledge from a teacher model into a lightweight student model, with both models trained using A2C. A post-hoc unlearning mechanism modifies weights to remove targeted features, while restored features show negligible performance loss, confirming reversibility. Unlike many benchmark models that used only 5% of the BoT-IoT dataset, this research leverages 25%, allowing us to develop a strong teacher model. Both the teacher and student models were trained using the A2C reinforcement learning algorithm, achieving impressive results, with the student model achieving 99.60% accuracy and a 99.80% F1 score. To enhance transparency, we integrated Explainable AI (XAI), particularly LIME, which helps interpret the model's decisions and identify the key features influencing its predictions. Moreover, DiRLU requires only 2,370 FLOPS, approximately 3.87x more efficient than the state-of-the-art model, highlighting its efficiency for edge deployment. DiRLU combines efficiency with privacy, aligning with GDPR standards (right to be forgotten) to provide practical and scalable IoT security solution.

</details>

---

### [[20_Research/Papers/机器人/Certifying_Ghosts_How_Cybersecurity_AI_Agents_Break_the_EU_Cyber_Resilience_Act|Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act]]

![[assets/2607.07109_first_page.png|800]]

- **arXiv**: [2607.07109](https://arxiv.org/abs/2607.07109)
- **PDF**: https://arxiv.org/pdf/2607.07109
- **详细分析**: [[20_Research/Papers/机器人/Certifying_Ghosts_How_Cybersecurity_AI_Agents_Break_the_EU_Cyber_Resilience_Act|Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act]]
- **作者**: Víctor Mayoral-Vilches
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.5，机器人 0.2）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act》归入 大模型、具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The EU Cyber Resilience Act (CRA) makes a smart bet. It does not demand that products be free of vulnerabilities, but only that manufacturers run a process: assess risk, handle flaws, ship updates. The bet pays off if four things about the world stay true: (P1) finding vulnerabilities is slow, skilled, human work; (P2) a product's exploitable flaws are knowable the day it ships; (P3) exploitation is rare enough to notice; and (P4) fixes keep pace with discovery. Cybersecurity AI (CAI) agents, AI put to work finding and exploiting flaws in other products, falsify all four. The regime answers in two opposite ways. Against the sheer volume of flaws that agents surface it bends (P1): built for scarce attention, it re-centres compliance on defensible, documented prioritisation, and holds. But agents also collapse the speed and economics of the vulnerability lifecycle, and here it breaks (P2, P3, P4): a product that passed every check becomes exploitable without anyone touching it, so its market-entry test, its reporting trigger, and its one-and-done certificate vouch for a security that has quietly expired. The fault is in the landscape, not the product, so running the process more diligently cannot repair it. We map each mechanism to the force that strains or snaps it, and find the cure and the disease cut from the same cloth: because defenders and attackers wield the same AI, the only conformity that survives is one that never stops running. We also carry the remedy from proposal to proof on two CRA-scope robots, a humanoid and a lawn mower, where an agentic defender holds a line their undefended selves cannot. On the evidence already in hand, the CRA reaches full force in December 2027 certifying products against a world that has already changed. Static, human-paced security is finished; what replaces it must be continuous and agent-operated, and that is no longer a matter of taste.

</details>

---

### [[20_Research/Papers/强化学习/SA-DRL_Security-Aware_Deep_Reinforcement_Learning_for_Ransomware_Detection_with_Asymmetric_Reward_Design|SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design]]

![[assets/2607.06880_figure.png|800]]

- **arXiv**: [2607.06880](https://arxiv.org/abs/2607.06880)
- **PDF**: https://arxiv.org/pdf/2607.06880
- **详细分析**: [[20_Research/Papers/强化学习/SA-DRL_Security-Aware_Deep_Reinforcement_Learning_for_Ransomware_Detection_with_Asymmetric_Reward_Design|SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design]]
- **作者**: Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam
- **cs 子类**: cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.1，强化学习 1.6）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design》归入 强化学习、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, SA-DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ransomware detection is a security-critical task in which false negatives and false positives have unequal operational consequences. Conventional machine learning detectors often use symmetric objectives that penalize missed ransomware detections and benign false alarms equally, although a false negative can cause irreversible encryption, operational disruption, and high recovery cost, whereas a false positive is usually reversible. This study proposes a Security-Aware Deep Reinforcement Learning (SA-DRL) framework that embeds false-negative and false-positive cost asymmetry into the reinforcement learning reward signal to prioritize missed-detection reduction. The framework also introduces a Security-Optimal Model Selection (SOMS) criterion and an adaptive episode-level sample-ordering mechanism. Four deep reinforcement learning agents, DQN, DDQN, PPO, and A2C, were evaluated using a symmetric baseline reward (R1) and a security-aware asymmetric reward (R2). Experiments used four discount factors, five-fold cross-validation, and three random seeds, resulting in 480 training runs on a balanced ransomware detection dataset. The SOMS criterion selects models by prioritizing false-negative rate, followed by F1-score and training time. Results show that asymmetric reward shaping improves security-oriented detection performance. The SOMS-selected configuration, DDQN with R2 and gamma = 0.1, achieved a false-negative rate of 0.0080, an F1-score of 0.9915, and an AUC of 0.998, reducing missed detections by 67.6% compared with the best supervised baseline. Across all configurations, R2 reduced the mean false-negative rate by 43% relative to R1. These findings show that reward-function design is important for security-sensitive ransomware detection.

</details>

---

### [[20_Research/Papers/强化学习/Auditable_Machine_Unlearning_for_Privacy-Compliant_Ransomware_Detection_Using_Multi-Shard_SISA_and_Deep_Reinforcement_Learning|Auditable Machine Unlearning for Privacy-Compliant Ransomware Detection Using Multi-Shard SISA and Deep Reinforcement Learning]]

![[assets/2607.06860_figure.png|800]]

- **arXiv**: [2607.06860](https://arxiv.org/abs/2607.06860)
- **PDF**: https://arxiv.org/pdf/2607.06860
- **详细分析**: [[20_Research/Papers/强化学习/Auditable_Machine_Unlearning_for_Privacy-Compliant_Ransomware_Detection_Using_Multi-Shard_SISA_and_Deep_Reinforcement_Learning|Auditable Machine Unlearning for Privacy-Compliant Ransomware Detection Using Multi-Shard SISA and Deep Reinforcement Learning]]
- **作者**: Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam
- **cs 子类**: cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《Auditable Machine Unlearning for Privacy-Compliant Ransomware Detection Using Multi-Shard SISA and Deep Reinforcement Learning》归入 强化学习 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ransomware poses an escalating cybersecurity threat as attackers continuously modify behavioral patterns to evade static defenses. Although existing machine learning-based detectors often achieve strong predictive performance, they generally assume fixed training data and do not support the selective removal of previously learned samples. This limitation conflicts with privacy regulations such as the GDPR and CCPA, which require the removal of sensitive user data upon request. To address this challenge, we propose an auditable ransomware detection and unlearning framework that integrates deep reinforcement learning with multi-shard SISA retraining. In the proposed system, a Double Deep Q-Network (DDQN) learns a reward-guided detection policy from behavioral features under asymmetric security costs, while multi-shard SISA enables privacy-compliant selective sample removal through shard-level retraining. The framework was evaluated using four criteria: utility preservation, oracle-based forgetting validation, membership inference auditing, and computational efficiency. On a balanced Windows 11 behavioral dataset comprising 2,000 samples and 103 features, the baseline DDQN detector achieved an F1 score of 0.9925 and an AUC of 0.9983. The experimental results show that single-shard unlearning maintains minimal utility degradation and low oracle disagreement, whereas moderate shard counts (M = 5-10) provide the best efficiency-performance trade-off, reducing retraining time to 5-30 s compared with 80-330 s for full retraining. In addition, the membership inference scores remain close to 0.5 across most configurations, indicating limited privacy leakage after unlearning. These findings demonstrate that a privacy-compliant ransomware detection framework can jointly achieve high detection performance, auditable deletion verification, and efficient sample removal.

</details>

---

### [[20_Research/Papers/强化学习/ORAN-DEFEND_Subspace_Detection_and_Sanitization_of_Backdoor_DRL_xApps_in_Open_RAN|ORAN-DEFEND: Subspace Detection and Sanitization of Backdoor DRL xApps in Open RAN]]

![[assets/2607.06647_figure.png|800]]

- **arXiv**: [2607.06647](https://arxiv.org/abs/2607.06647)
- **PDF**: https://arxiv.org/pdf/2607.06647
- **详细分析**: [[20_Research/Papers/强化学习/ORAN-DEFEND_Subspace_Detection_and_Sanitization_of_Backdoor_DRL_xApps_in_Open_RAN|ORAN-DEFEND: Subspace Detection and Sanitization of Backdoor DRL xApps in Open RAN]]
- **作者**: Md Raihan Uddin, Fatemeh Lotfi, Tolunay Seyfi, Fatemeh Afghah
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《ORAN-DEFEND: Subspace Detection and Sanitization of Backdoor DRL xApps in Open RAN》归入 强化学习、世界模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BadRL, DRL, TrojDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open Radio Access Networks (O-RAN) increasingly delegate near-real-time control to deep reinforcement learning (DRL) xApps obtained from third-party vendors, creating a new supply-chain attack surface. A backdoor policy behaves optimally until an adversary injects a covert trigger into the observed key performance indicator (KPI) telemetry, at which point it issues harmful control actions that degrade quality of service (QoS). We present ORAN-DEFEND, a retraining-free wrapper that sanitizes a frozen, potentially compromised xApp by projecting each KPI window onto a safe subspace estimated from a small number of trusted clean rollouts via singular value decomposition (SVD). We establish, both analytically and empirically, a precise recovery condition: the defense succeeds if the trigger energy concentrates in the orthogonal complement of the safe subspace, and we quantify this boundary through the trigger's $\Eperp$ energy fraction. On the Colosseum COLORAN dataset, we evaluate four structurally distinct DRL backdoor attacks, like TrojDRL, SleeperNets, BadRL, and Q-Incept, spanning inner-loop and outer-loop poisoning regimes and demonstrate $100\%$ return recovery and $\geq99.5\%$ defense success rate across all four when the subspace assumption holds. A geometry ablation reveals an intrinsic and previously uncharacterized limit of any linear projection defense: when the trigger collocates with the legitimate signal, the $\Eperp$ energy fraction governs recovery monotonically, and the linear residual detector collapses to chance even while a nonlinear classifier retains perfect separability.

</details>

---
