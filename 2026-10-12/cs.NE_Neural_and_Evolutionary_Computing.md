# cs.NE | Neural and Evolutionary Computing | 2026-10-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/The_value_of_information_and_the_emergence_of_communication_in_evolved_e-puck_robots|The value of information and the emergence of communication in evolved e-puck robots]]

![[assets/2610.13118_first_page.png|800]]

- **arXiv**: [2610.13118](https://arxiv.org/abs/2610.13118)
- **PDF**: https://arxiv.org/pdf/2610.13118
- **详细分析**: [[20_Research/Papers/机器人/The_value_of_information_and_the_emergence_of_communication_in_evolved_e-puck_robots|The value of information and the emergence of communication in evolved e-puck robots]]
- **作者**: Fernando Montes-Gonzalez
- **cs 子类**: cs.NE, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《The value of information and the emergence of communication in evolved e-puck robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Neural and Evolutionary Computing 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Embedded Action Selection Architecture (EASA). Fitness measures only the time the robots spend over the food. When the robots receive a compass pointing to the food, use of the signal disappears completely. Without a compass, in a small arena, three independent runs achieved similar performance using different strategies: a referential signal, a permanent beacon, or no use of the signal. As the arena expands, the strategy based on a referential signal generalizes best. In contrast, evolving directly in the large arena does not increase the frequency of communication, but it does separate the strategies, and the referential signal clearly outperforms solitary searching. Within EASA, innate reflexes constrain the network and reduce performance. As its priorities evolve, evolution consistently weakens those reflexes. The results suggest that communication emerges in proportion to the value of the information it transmits, and that an innate scaffolding designed for isolated agents can be an impediment in a social task.

</details>

---
