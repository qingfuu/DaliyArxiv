# cs.CR | Cryptography and Security | 2026-11-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/When_Coding_Agents_Get_Arms_Safety_Risks_Across_the_Digital-Physical_Boundary|When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary]]

![[assets/2611.11438_figure.png|800]]

- **arXiv**: [2611.11438](https://arxiv.org/abs/2611.11438)
- **PDF**: https://arxiv.org/pdf/2611.11438
- **详细分析**: [[20_Research/Papers/具身智能/When_Coding_Agents_Get_Arms_Safety_Risks_Across_the_Digital-Physical_Boundary|When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary]]
- **作者**: Yiming Sun, Mi Zhang
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary》归入 具身智能、大模型、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IS-Bench, OpenVLA, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Advances in spatial understanding have enabled frontier models to power coding agents that control a real robot arm zero-shot and end-to-end, without task-specific demonstrations or retraining. This brings two new safety challenges. First, the extensive knowledge of frontier models lets these agents perform tasks that earlier VLA and WAM paradigms could not, opening the door to new forms of capability misuse. Second, coding agents can access digital resources such as web pages and emails. Threats in these resources, such as indirect prompt injection, can carry over into the physical world when the agent controls a robot. We therefore introduce ArmedAgent, the first systematic benchmark to evaluate both risks for coding agents performing zero-shot robot control. It covers robustness, malicious use, and indirect injection across 36 tasks in 5 scenarios, evaluated in simulation and validated on a physical robot arm. A distinctive portion of the tasks target harmful behaviors that earlier VLA paradigms could not perform. Testing several frontier models, including GPT-6-Astra, under widely used agent frameworks, we find substantial safety risks in current systems.

</details>

---
