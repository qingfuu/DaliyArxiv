# cs.CR | Cryptography and Security | 2026-09-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/RobResilience_Implementing_and_Evaluating_a_Resilience_Framework_for_Cyber-Physical_Embodied_Systems|RobResilience: Implementing and Evaluating a Resilience Framework for Cyber-Physical Embodied Systems]]

![[assets/2609.17349_figure.png|800]]

- **arXiv**: [2609.17349](https://arxiv.org/abs/2609.17349)
- **PDF**: https://arxiv.org/pdf/2609.17349
- **详细分析**: [[20_Research/Papers/具身智能/RobResilience_Implementing_and_Evaluating_a_Resilience_Framework_for_Cyber-Physical_Embodied_Systems|RobResilience: Implementing and Evaluating a Resilience Framework for Cyber-Physical Embodied Systems]]
- **作者**: Gysella Imrell, Emanuele Miotto, Mahya Mohammadi Kashani, Mauro Conti, Alberto Giaretta
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《RobResilience: Implementing and Evaluating a Resilience Framework for Cyber-Physical Embodied Systems》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In embodied cyber-physical systems, active cyberattacks pose an immediate threat not just to data, but to physical integrity and human safety. While existing security approaches excel at detection, they lack the runtime mechanisms to determine whether a disruption is tolerable or if performance degradation remains within safe operational bounds. This gap leaves autonomous systems vulnerable to graceful failure paralysis, where they cannot distinguish between a safe, degraded state and a catastrophic hazard during an ongoing attack. This paper presents RobResilience, an implementation of a formal resilience framework for embodied cyber-physical systems in a Webots simulation environment, using a PR2 robot and ROS2. The framework evaluates three predicates at runtime: tolerable disruption ($\delta$), tolerable degradation ($\gamma$), and mitigation feasibility ($\mu$), over a compromised device set derived from IDS confidence scores. When resilience is lost, the framework triggers available mitigation strategies. We evaluate our implementation through eight attack scenarios that systematically cover all possible combinations of the predicate state space, varying attack targets, degradation rates, and mitigation availability. Results confirm that the runtime behaviour of the implementation is consistent with the theoretical definitions.

</details>

---
