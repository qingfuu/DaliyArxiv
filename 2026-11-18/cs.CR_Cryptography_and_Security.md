# cs.CR | Cryptography and Security | 2026-11-18

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/机器人/Guarded_Swarms_in_the_Loop_A_ROS_2_PX4_Digital_Twin_for_Hybrid_Digital-Analog_Coordination_of_UAV_UGV_Swarms|Guarded Swarms in the Loop: A ROS 2/PX4 Digital Twin for Hybrid Digital-Analog Coordination of UAV/UGV Swarms]]

![[assets/2611.22773_first_page.png|800]]

- **arXiv**: [2611.22773](https://arxiv.org/abs/2611.22773)
- **PDF**: https://arxiv.org/pdf/2611.22773
- **详细分析**: [[20_Research/Papers/机器人/Guarded_Swarms_in_the_Loop_A_ROS_2_PX4_Digital_Twin_for_Hybrid_Digital-Analog_Coordination_of_UAV_UGV_Swarms|Guarded Swarms in the Loop: A ROS 2/PX4 Digital Twin for Hybrid Digital-Analog Coordination of UAV/UGV Swarms]]
- **作者**: Uwe M. Borghoff, Paolo Bottoni, Luca D'Aurizio, Remo Pareschi
- **cs 子类**: cs.CR
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.6（加权：机器人 1.6）
- **关联关键词**: Security, Systems

#### 研究背景与动机

《Guarded Swarms in the Loop: A ROS 2/PX4 Digital Twin for Hybrid Digital-Analog Coordination of UAV/UGV Swarms》归入 机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Swarms of unmanned aerial and ground vehicles (UAV/UGV) operating in contested environments cannot rely on software alone for physical safety, since the software stack and its networks are part of the attack surface. The Guarded Swarms architecture addresses this by pairing a digital coordination layer, built on Topic-Based Communication Space Petri Nets (TB-CSPN), with an independent analog safety layer that can veto unsafe actuation commands. So far, the architecture has been specified and argued for, but not executed. We present the first executable instantiation of Guarded Swarms as a digital twin built on ROS 2, the PX4 autopilot in software-in-the-loop mode, and Gazebo, with two UAVs and one UGV in a coastal counter-UAS scenario. The TB-CSPN transition chain, from multi-modal sensing through human authorization to vehicle tasking, is mapped one-to-one onto ROS 2 nodes, and the analog layer is modeled as a per-vehicle Virtual Safety Board that gates every command. Eight groups of experiments show that the three negative guarantees of the architecture (no mission from conflicting, temporally incoherent, or unauthorized evidence) hold at three distinct stages of the chain in all 60 counterfactual runs; that threat confirmation is bounded by the narrowest sensing modality; that the safety layer exercises its full modeled envelope independently of the coordination layer; and, under fault injection, that it prevents every collision caused by a forged mission or a compromised worker once its veto is enforced by an independent gate, whereas a veto left to the compromised worker prevents none. The twin also exposes implementation-level hazards that the architectural specification does not address, and it draws an explicit line between the properties that simulation can validate and those that only hardware can.

</details>

---

### [[20_Research/Papers/机器人/From_Attack_Tree_to_Model_Checker_Binding_CAPEC_Patterns_to_Verify_Robotic_System_Security|From Attack Tree to Model Checker: Binding CAPEC Patterns to Verify Robotic System Security]]

![[assets/2611.22408_first_page.png|800]]

- **arXiv**: [2611.22408](https://arxiv.org/abs/2611.22408)
- **PDF**: https://arxiv.org/pdf/2611.22408
- **详细分析**: [[20_Research/Papers/机器人/From_Attack_Tree_to_Model_Checker_Binding_CAPEC_Patterns_to_Verify_Robotic_System_Security|From Attack Tree to Model Checker: Binding CAPEC Patterns to Verify Robotic System Security]]
- **作者**: Juel Hussain, Louise A. Dennis, Clare Dixon, Marie Farrell
- **cs 子类**: cs.CR
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, Security, Systems

#### 研究背景与动机

《From Attack Tree to Model Checker: Binding CAPEC Patterns to Verify Robotic System Security》归入 机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Security-minded verification of autonomous and robotic systems presupposes an attacker, yet the path from a threat catalogue to a checkable attacker model is still traversed by hand. This research preview presents the theory and construction of a pipeline that mechanises it. Each leaf of an attack tree is mapped to a CAPEC attack pattern and written in first-order logic as a rule: the attacker's prerequisites imply the attack's effect. Casting the pattern as such a rule is what makes it operational - its variables can be bound to a specific system's parts, and its prerequisites can then be tested against that system under a chosen configuration of security controls. Binding is our means of verifying whether a system is vulnerable to a given attack: from a bound pattern we derive an attacker model, turn its effect into a temporal-logic property, and check that property against the system with and without a countermeasure, reporting the control that defeats the attack. We describe the signature, schemas, profiles for approach, and explore how CAPEC can support reasoning about robotics security.

</details>

---

### [[20_Research/Papers/大模型/GapLeak_When_Privacy-Preserving_LLM-based_Web_Agents_Become_a_Privacy_Risk|GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk]]

![[assets/2611.22223_figure.png|800]]

- **arXiv**: [2611.22223](https://arxiv.org/abs/2611.22223)
- **PDF**: https://arxiv.org/pdf/2611.22223
- **详细分析**: [[20_Research/Papers/大模型/GapLeak_When_Privacy-Preserving_LLM-based_Web_Agents_Become_a_Privacy_Risk|GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk]]
- **作者**: Chaklam Cheong, Tiancong Cao, Qi Li, Zelin Zhang, Jianbing Ni, Rongxing Lu, Mohammad Zulkernine
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based web agents rely on data minimization and least privilege to protect user privacy. We show that these principles are necessary but insufficient: they constrain authorized sources, but not higher-sensitivity sources that remain reachable. A website can request a field unavailable from authorized sources, creating an information gap. To complete the task, a goal-driven agent may escalate to reachable but unauthorized sources and disclose accumulated sensitive information. We formalize this vulnerability as GapLeak, where an adversary exploits a legitimate web form without prompt injection or other malicious instructions. We evaluate GapLeak on three web-agent frameworks and six LLMs from Anthropic, Google, and OpenAI across recruitment, e-commerce, travel, and healthcare. GapLeak induces an average unauthorized disclosure of approximately 37%. The information gap is the primary driver: eliminating it reduces disclosure by more than 50%. Existing instruction-level defenses based on least privilege partially mitigate the vulnerability but often reduce task success. We propose submission-time verification, which filters unauthorized content before form submission, eliminating over 96% of unauthorized disclosures while preserving task success.

</details>

---
