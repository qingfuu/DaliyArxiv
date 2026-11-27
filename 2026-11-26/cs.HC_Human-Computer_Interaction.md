# cs.HC | Human-Computer Interaction | 2026-11-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/RoboJackVR_Turning_Robot_Tasks_into_VR_Games_for_Scalable_Demonstration_Collection|RoboJackVR: Turning Robot Tasks into VR Games for Scalable Demonstration Collection]]

![[assets/2611.33731_figure.png|800]]

- **arXiv**: [2611.33731](https://arxiv.org/abs/2611.33731)
- **PDF**: https://arxiv.org/pdf/2611.33731
- **详细分析**: [[20_Research/Papers/强化学习/RoboJackVR_Turning_Robot_Tasks_into_VR_Games_for_Scalable_Demonstration_Collection|RoboJackVR: Turning Robot Tasks into VR Games for Scalable Demonstration Collection]]
- **作者**: Ben Ma, Jixuan Cai
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《RoboJackVR: Turning Robot Tasks into VR Games for Scalable Demonstration Collection》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MetaSim, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling robot demonstration datasets requires collection systems that accommodate more participants and diverse tasks, yet teleoperation barriers and task-adaptation effort limit this expansion. We present RoboJackVR, a standalone virtual reality (VR) game in which players manipulate simulated robots to execute combat skills and contribute demonstrations. MuJoCo simulation and demonstration recording run locally on the headset, removing the need for an external PC or simulation server during collection. Tutorials, skill selection, combat consequences, and character progression organize repeated task attempts within a continuing game. Task contracts declare assets, controls, resets, success criteria, and recording semantics; separate game configurations specify guidance, attempt groups, skill effects, and course placement. Shared bindings connect these declarations to task execution, outcome handling, and recording, allowing tasks to reuse the game flow while retaining their control and success semantics. Batch tools package supported resources and generate configurations, with manual adaptation and review for new interfaces and unsupported predicates. We instantiate the approach with SO101-Nexus-derived and LIBERO tasks. On the 66 LIBERO-90 tasks covered by the collected data, ACT policies trained solely on VR demonstrations retain approximately 91% of the full-standard simulation-demonstration baseline's success rate on held-out initial states, averaged over four training seeds. These results support the utility of play-collected VR demonstrations for policy learning in this setting.

</details>

---
