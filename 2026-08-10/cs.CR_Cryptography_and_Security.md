# cs.CR | Cryptography and Security | 2026-08-10

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/机器人/Rigid-Covert_GNSS_Spoofing_of_UAV_Swarms_A_Structural_Blind_Spot,_Its_Detection_Limit,_and_Absolute-Anchor_Defenses|Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses]]

![[assets/2608.06885_figure.png|800]]

- **arXiv**: [2608.06885](https://arxiv.org/abs/2608.06885)
- **PDF**: https://arxiv.org/pdf/2608.06885
- **详细分析**: [[20_Research/Papers/机器人/Rigid-Covert_GNSS_Spoofing_of_UAV_Swarms_A_Structural_Blind_Spot,_Its_Detection_Limit,_and_Absolute-Anchor_Defenses|Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses]]
- **作者**: Minseok Park, Joon Soo Yoo
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: ComputerVision, Security

#### 研究背景与动机

《Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses》归入 机器人、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OrbitGuardNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative UAV-swarm defenses commonly cross-check GNSS positions against measured inter-drone geometry. We show that this relative-geometry channel has a structural blind spot: a common, slowly varying translation (a rigid-covert shift, RigidShift) preserves all pairwise distances and is therefore unobservable to any relative-only detector (a gauge-freedom argument). We validate this blindness on distance-verification and semidefinite-feasibility baselines, while explicitly distinguishing it from onboard inertial/GNSS monitors that can raise a bare alarm but cannot recover the swarm's true position. To quantify when an external reference restores observability, we derive the drift-dependent detection floor $2\gamma/(1-t_s/T)$ for a calibrated anchor-residual detector and empirically identify an additional detector-specific noise floor (measured slope 2.66 vs. predicted 2.67). We then present a centralized anchor-rooted recovery pipeline that reconstructs swarm geometry from inter-drone ranges, aligns it to a trusted-anchor subset with Byzantine-robust fitting, and recovers the absolute positions of non-anchored drones. A segmented estimator jointly estimates anchor drift, attack rate, and onset when no clean-epoch label is available. Across statistical simulations, ArduPilot software-in-the-loop experiments, and Gazebo experiments with rendered vision anchors, the method recovers the positions of non-anchored drones to a median error of 0.39 m (20 seeds) under approximately 10.1 m of GNSS drift, and to 7.1 cm (5 seeds) in the rendered-vision multi-SITL setting. We also characterize the explicit limits imposed by non-collinear anchor geometry, anchor coverage, $\tau\to0$ drift-attack aliasing, and majority anchor compromise. All evaluations are simulation-based and use no RF spoofing hardware or physical swarm.

</details>

---

### [[20_Research/Papers/具身智能/When_Coordination_Becomes_a_Threat_Communication_Attacks_in_LLM-Controlled_Multi-Robot_Systems|When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems]]

![[assets/2608.06830_figure.png|800]]

- **arXiv**: [2608.06830](https://arxiv.org/abs/2608.06830)
- **PDF**: https://arxiv.org/pdf/2608.06830
- **详细分析**: [[20_Research/Papers/具身智能/When_Coordination_Becomes_a_Threat_Communication_Attacks_in_LLM-Controlled_Multi-Robot_Systems|When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems]]
- **作者**: Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) are increasingly used as high-level planners in embodied multi-robot systems, enabling robots to interpret natural language instructions and coordinate executable actions. Yet, this growing reliance on LLM planners also raises security concerns. Prior work has focused mainly on individual robots, while communication risks in multi-robot collaboration remain insufficiently understood. Existing multi-robot studies are further limited to preliminary analysis under the Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether these risks persist across other common communication architectures and how attacker access settings shape their propagation. To fill this gap, we formulate two communication attacks corresponding to distinct attacker access settings: the External Entry Point Attack and the Privileged In-System Attack. We evaluate both attacks across DMAS, HMAS-1, and HMAS-2 using three LLMs and five embodied multi-robot tasks. Results show that unsafe information can turn into unsafe actions across all three architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers 88.3\% of task defined unsafe action slots. To mitigate risks from trusted information flow, we introduce the Claim Provenance and Verification (CPV) Gate, which verifies communicated claims before downstream reuse and reduces the violation rate from 70.0\% to 36.6\%.

</details>

---

### [[20_Research/Papers/大模型/CyberLLM_A_Multi-Agent_LLM_Framework_for_Autonomous_Detection_and_Guarded_Response_in_Automotive_Cybersecurity|CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity]]

![[assets/2608.06651_first_page.png|800]]

- **arXiv**: [2608.06651](https://arxiv.org/abs/2608.06651)
- **PDF**: https://arxiv.org/pdf/2608.06651
- **详细分析**: [[20_Research/Papers/大模型/CyberLLM_A_Multi-Agent_LLM_Framework_for_Autonomous_Detection_and_Guarded_Response_in_Automotive_Cybersecurity|CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity]]
- **作者**: Nenad Petrovic, Oussama Jeddou, Feres Ben Fraj, Vahid Zolfaghari, Fengjunjie Pan, Andre Schamschurko, Alois Knoll
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《CyberLLM: A Multi-Agent LLM Framework for Autonomous Detection and Guarded Response in Automotive Cybersecurity》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software-Defined Vehicles (SDVs) expand the automotive attack surface across source code, runtime logs, and deployment topologies, while safety constraints forbid autonomous agents from acting without oversight. This paper presents CyberLLM, a multi-agent, LLM-orchestrated framework that autonomously detects vulnerabilities and executes remediations under a formal, runtime safety guard. Detection combines a deterministic layer (regex rules, AST analyzers, and topology graph checks) with an LLM refinement pass, so a high-recall floor is complemented by high-precision reasoning. A decision agent aggregates findings, tags them with a human-centric asset taxonomy, and selects a tiered response, ratcheting its confidence with signed cross-session memory and re-planning feedback. Every action is validated against four contextual security properties and an independent action-alignment oracle before it is allowed to run, and refused actions trigger escalation and re-planning. A symmetric attack pipeline generates and replays exploits so both sides can be exercised on the same scenarios. On an independent, ground-truthed benchmark of nine original automotive ECU modules in C, C++, and Rust seeding 47 layered vulnerabilities plus clean controls, the always-on deterministic layer covers 34\% of the labeled vulnerabilities at perfect precision, and adding the grounded LLM refinement and completeness passes roughly doubles coverage to about 70\% (F1 $0.83$) while producing zero false positives on the clean controls. The results indicate that LLM agents can perform useful autonomous cyber-defense when wrapped in a deterministic, auditable safety envelope.

</details>

---
