# cs.HC | Human-Computer Interaction | 2026-05-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/PACT_Proactive_Asking_for_Continual_Task_Assistance_in_Human-Robot_Collaboration|PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration]]

![[assets/2605.24350_figure.png|800]]

- **arXiv**: [2605.24350](https://arxiv.org/abs/2605.24350)
- **PDF**: https://arxiv.org/pdf/2605.24350
- **详细分析**: [[20_Research/Papers/具身智能/PACT_Proactive_Asking_for_Continual_Task_Assistance_in_Human-Robot_Collaboration|PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration]]
- **作者**: Chengbo He, Sheng Li, Chenyang Ma, Bochao Zou, Li Sun, Jiansheng Chen, Junliang Xing, Yuanchun Shi, Huimin Ma
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration》归入 机器人、具身智能、强化学习 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ASK-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic assistants in long-term human-robot collaboration need to assist users under partial observations while leveraging cross-day interaction history. However, human traits and routines are often unknown at the beginning of collaboration, making passive infer-then-act assistance ineffective and inefficient. To address this challenge, we study a cross-day proactive asking setting for continual task assistance and propose PACT (Proactive Asking for Continual Task Assistance), an ask-or-act framework that determines whether clarification should be sought before taking action. PACT leverages current observations together with accumulated interaction history to evaluate contextual sufficiency, enabling the robot to provide more reliable assistance and progressively adapt to the user over time. We implement its primary learned instantiation using reinforcement learning and evaluate alternative instantiations under the same framework. To assess such behavior, we further introduce a clarification utility metric that quantifies the trade-off between assistance accuracy and the frequency of clarification requests. Experiments in multi-day embodied collaboration scenarios demonstrate that, compared with passive inference baselines, PACT consistently improves both assistance accuracy and clarification utility, highlighting the importance of proactive asking in continual human-robot collaboration.

</details>

---
