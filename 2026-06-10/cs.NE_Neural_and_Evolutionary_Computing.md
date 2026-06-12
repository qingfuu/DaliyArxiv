# cs.NE | Neural and Evolutionary Computing | 2026-06-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/A_Spiking_Neural_Architecture_for_Coordinating_Arm_and_Locomotor_Control|A Spiking Neural Architecture for Coordinating Arm and Locomotor Control]]

![[assets/2606.11034_figure.png|800]]

- **arXiv**: [2606.11034](https://arxiv.org/abs/2606.11034)
- **PDF**: https://arxiv.org/pdf/2606.11034
- **详细分析**: [[20_Research/Papers/具身智能/A_Spiking_Neural_Architecture_for_Coordinating_Arm_and_Locomotor_Control|A Spiking Neural Architecture for Coordinating Arm and Locomotor Control]]
- **作者**: Lea Steffen, Kathryn Simone, Graeme Damberger, Travis DeWolf, Hudson Ly, Chris Eliasmith
- **cs 子类**: cs.NE, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Spiking Neural Architecture for Coordinating Arm and Locomotor Control》归入 具身智能、机器人 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spiking Neural Networks (SNNs) coupled with neuromorphic hardware offer energy-efficient solutions for humanoid robot control. However, existing SNN-based motor control systems address bipedal locomotion and arm control in isolation, leaving integrated control of both unaddressed. We present a spiking architecture that coordinates force-based arm control and bipedal locomotion in a simulated humanoid, using the Neural Engineering Framework (NEF) and Semantic Pointer Architecture (SPA). High-level action selection between locomotor and arm control is mediated by a biologically grounded spiking basal ganglia model. We validate the system through co-simulation of Nengo, for the neural control, and Isaac Sim, demonstrating successful target reaching, continuous digit drawing, path-following locomotion, and finally, switching between walking and arm control via basal ganglia disinhibition. To our knowledge, this is the first integrated spiking controller to combine bipedal locomotion and arm control on a full-scale humanoid platform. The full spike-based implementation enables future deployment on low-power neuromorphic hardware.

</details>

---
