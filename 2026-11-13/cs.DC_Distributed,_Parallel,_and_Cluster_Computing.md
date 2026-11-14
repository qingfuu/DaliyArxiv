# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-13

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Scaling_VLA_Serving_Under_Robotic_Execution_Constraints|Scaling VLA Serving Under Robotic Execution Constraints]]

![[assets/2611.14969_figure.png|800]]

- **arXiv**: [2611.14969](https://arxiv.org/abs/2611.14969)
- **PDF**: https://arxiv.org/pdf/2611.14969
- **详细分析**: [[20_Research/Papers/具身智能/Scaling_VLA_Serving_Under_Robotic_Execution_Constraints|Scaling VLA Serving Under Robotic Execution Constraints]]
- **作者**: Yue Zhang, Zicong Ye, Lufang Chen, Dance Yang, Mingyang Li, Zhenwei Duan, Michael Zhao, Ziye Deng, Starrick Liu, Ruizhi Chengze, YongHua Chen, SongAo Han...
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Scaling VLA Serving Under Robotic Execution Constraints》归入 具身智能、机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation. In our production setting, hundreds of VLA-powered robots are already operating in real-world environments, creating an immediate need for efficient fleet serving. We present XInfer, a production-deployed VLA serving system designed to reduce the inference infrastructure cost of large-scale robotic deployments. XInfer jointly coordinates heterogeneous VLA computation with the evolving response requirements of robotic execution. By exploiting computational parallelism while managing interference, XInfer improves GPU efficiency while protecting time-critical robotic feedback. We evaluate XInfer across three VLA models using production-derived workloads, achieving 1.26-3.75 times the effective robot capacity (ERC) of state-of-the-art systems under physical-execution constraints. Our implementation is publicly available at https://github.com/X-Square-Robot/xinfer.

</details>

---
