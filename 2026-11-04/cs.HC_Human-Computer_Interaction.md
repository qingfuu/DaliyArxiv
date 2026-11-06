# cs.HC | Human-Computer Interaction | 2026-11-04

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/机器人/Haptic_Shared_Control_for_Multi-Robot_Systems|Haptic Shared Control for Multi-Robot Systems]]

![[assets/2611.05027_figure.png|800]]

- **arXiv**: [2611.05027](https://arxiv.org/abs/2611.05027)
- **PDF**: https://arxiv.org/pdf/2611.05027
- **详细分析**: [[20_Research/Papers/机器人/Haptic_Shared_Control_for_Multi-Robot_Systems|Haptic Shared Control for Multi-Robot Systems]]
- **作者**: Maxime Bernard
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Haptic Shared Control for Multi-Robot Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent systems offer significant advantages in terms of flexibility and redundancy, enabling the efficient distribution of complex tasks among multiple robots. However, their deployment requires advanced control strategies to ensure optimal cooperation between autonomous agents and human operators. We propose a modification of the global connectivity maintenance algorithm to incorporate measurements taken in agent's local frame, using sensors with limited fields of view. This algorithm, responsible for the autonomous behavior of the multi-robot system, is combined with different adaptive supervision strategies, allowing the user to exert control at varying scales over the entire group. (i) Single Agent Control (S): The operator directly controls a single robot, (ii) Pinning Control (P): The operator imposes constraints on multiple robots to influence the group, (iii) Centroid Control (C): The operator acts on the system's center of mass to steer the entire fleet. In conjunction with the connectivity maintenance algorithm, these methods ensure compliance with inter-agent constraints while providing haptic feedback to the user regarding the system's connectivity state. The effectiveness of these approaches was evaluated through a user study, comparing performance with and without haptic feedback across multiple scenarios tailored to the different control modes.

</details>

---

### [[20_Research/Papers/机器人/For_You,_Not_for_Everyone_Bystander-Aware_Delivery_of_Critical_Feedback_in_Robot_Tutoring|For You, Not for Everyone: Bystander-Aware Delivery of Critical Feedback in Robot Tutoring]]

![[assets/2611.05001_figure.png|800]]

- **arXiv**: [2611.05001](https://arxiv.org/abs/2611.05001)
- **PDF**: https://arxiv.org/pdf/2611.05001
- **详细分析**: [[20_Research/Papers/机器人/For_You,_Not_for_Everyone_Bystander-Aware_Delivery_of_Critical_Feedback_in_Robot_Tutoring|For You, Not for Everyone: Bystander-Aware Delivery of Critical Feedback in Robot Tutoring]]
- **作者**: Atikkhan Faridkhan Nilgar, Manuel Dietrich, Kristof Van Laerhoven
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Security

#### 研究背景与动机

《For You, Not for Everyone: Bystander-Aware Delivery of Critical Feedback in Robot Tutoring》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots in shared settings may expose information intended for an individual user to nearby bystanders. Robot tutoring makes this concern particularly salient: critical feedback is directed at an individual learner, yet bystanders may overhear or see it. To address this, we compared context-invariant and context-adaptive robot behaviors in a between-subjects study with 40 participants. Following an initial phase without a bystander, a bystander entered the setting. Participants then received two scripted critical feedback messages concerning their pronunciation and handwriting, independent of their actual performance. With the context-invariant behavior, the robot tutor delivered both messages aloud. With the context-adaptive behavior, the robot tutor scanned for the bystander, turned its body and display away after detecting them, gave a spoken attention cue, and presented the same feedback messages silently on its display. Participants rated the robot tutor higher in perceived privacy awareness and perceived social competence in the context-adaptive condition than in the context-invariant condition, while evidence for reduced experienced embarrassment was inconclusive. These findings inform the design and evaluation of robots that respond to bystander presence by adapting how they communicate potentially sensitive information.

</details>

---

### [[20_Research/Papers/机器人/Just_Between_Us_Exploring_a_Wearable-Mediated_Channel_for_Discreet_Human-Agent_Interaction_in_a_Shared_Game_Setting|Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting]]

![[assets/2611.04692_figure.png|800]]

- **arXiv**: [2611.04692](https://arxiv.org/abs/2611.04692)
- **PDF**: https://arxiv.org/pdf/2611.04692
- **详细分析**: [[20_Research/Papers/机器人/Just_Between_Us_Exploring_a_Wearable-Mediated_Channel_for_Discreet_Human-Agent_Interaction_in_a_Shared_Game_Setting|Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting]]
- **作者**: Atikkhan Faridkhan Nilgar, Manuel Dietrich, Kristof Van Laerhoven
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting》归入 机器人、大模型、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In shared settings, social robots may need to exchange information with an individual while limiting co-present others' access to or interpretation of that information. Publicly observable speech and gestures may not adequately support such exchanges. We investigate a wearable-mediated channel for discreet interaction that combines in-ear audio messages with deliberate rightward head tilts as responses. To examine its feasibility and participants' experiences, we studied 20 pairs (40 participants) playing a card game with a screen-based conversational agent representing a social robot, controlled by a researcher in a Wizard-of-Oz setup. Each pair played with and without the channel. One participant wore the device (the wearer), while the other (the non-wearer) was informed about the channel after gameplay. The channel conveyed information that could help the wearer or robot character select an opponent they could defeat. The information exchange and subsequent opponent selection occurred as intended in 39 of 40 channel-mediated turns. Wearers reported low perceived pressure/tension in both conditions, with no statistically significant difference between conditions, and favorable usability immediately after use. Retrospective interviews, however, revealed varied accounts of noticing the interaction among non-wearers and contrasting perceptions of teamwork and unfairness. These findings support the feasibility of wearable-mediated exchanges within this game and identify awareness and fairness as considerations for future designs.

</details>

---
