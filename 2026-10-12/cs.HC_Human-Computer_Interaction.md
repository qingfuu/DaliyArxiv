# cs.HC | Human-Computer Interaction | 2026-10-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/JitterVLA_A_Replay_Benchmark_for_Motion_Quality_in_VLA-Driven_Human-Robot_Manipulation|JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation]]

![[assets/2610.13628_figure.png|800]]

- **arXiv**: [2610.13628](https://arxiv.org/abs/2610.13628)
- **PDF**: https://arxiv.org/pdf/2610.13628
- **详细分析**: [[20_Research/Papers/具身智能/JitterVLA_A_Replay_Benchmark_for_Motion_Quality_in_VLA-Driven_Human-Robot_Manipulation|JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation]]
- **作者**: Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov, Dzmitry Tsetserukou
- **cs 子类**: cs.HC, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：JitterVLA, OpenVLA, URSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isolating the controller's effect. We apply it to synthetic reaches, hand trajectories from 20 people, three open VLA pipelines (838 episodes) and a physical UR3. Interpolation lowered modeled p99 jerk for every source, by 83% (615 to 106 m/s^3) on human motion with 200 ms delay, at a 2.0 cm tracking cost, and the effect replicated on 598 new episodes; jerk-limited generation lowered jerk further at a larger cost. Entropy-discontinuity associations had opposite, replicated signs in two pipelines, and entropy gating helped in one but not the other. On the UR3, interpolation lowered accelerometer-derived jerk by 3.0-14.0% in all six exploratory pairs, while a position-derived metric did not resolve the contrast. JitterVLA supports screening before human-centred studies; code and data will be released.

</details>

---
