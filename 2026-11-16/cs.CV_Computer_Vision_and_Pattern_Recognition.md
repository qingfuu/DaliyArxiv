# cs.CV | Computer Vision and Pattern Recognition | 2026-11-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Real-Time_Diffusion_Relighting_as_a_Neural_Sensor_Closing_the_Low-Light_Domain_Gap_for_Robotic_Perception|Real-Time Diffusion Relighting as a Neural Sensor: Closing the Low-Light Domain Gap for Robotic Perception]]

![[assets/2611.17438_figure.png|800]]

- **arXiv**: [2611.17438](https://arxiv.org/abs/2611.17438)
- **PDF**: https://arxiv.org/pdf/2611.17438
- **详细分析**: [[20_Research/Papers/具身智能/Real-Time_Diffusion_Relighting_as_a_Neural_Sensor_Closing_the_Low-Light_Domain_Gap_for_Robotic_Perception|Real-Time Diffusion Relighting as a Neural Sensor: Closing the Low-Light Domain Gap for Robotic Perception]]
- **作者**: Shengjie Xu, Alexander Gao, Anshul Rai, Dae Yeol Lee, Guan-Ming Su, Ming C. Lin
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Real-Time Diffusion Relighting as a Neural Sensor: Closing the Low-Light Domain Gap for Robotic Perception》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DiLightNet, MambaSFLNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-light conditions severely degrade robotic perception: object detectors trained on daylight imagery are prone to failure under dark and adverse weather conditions that fall outside of their training distribution. Furthermore, from an efficiency standpoint, existing Low-Light Image Enhancement (LLIE) methods are designed for offline processing and are therefore impractical to integrate into live control loops. To address these issues, we propose to embed a Generative Neural Sensor within the control loop that treats illumination as a generative prior rather than a signal processing problem, enabling task-relevant semantic recovery. We further propose an Real-Time Perceptual Architecture that decouples high-latency semantic recovery from low-latency robotic control. Rather than blocking the control loop, our system runs a large-scale image-to-image diffusion model in a background thread, and is activated only when a drop in detection confidence signals a perceptual uncertainty event, significantly reducing computational overhead. Our method sets a new state-of-the-art performance on the ExDark low-light benchmark with 87.1% mAP, and under adverse weather conditions, significantly boosts detection rates over competing methods. On a navigation task in a closed-loop autonomous driving simulator (CARLA), we achieve a 100% lap completion rate, establishing a simulation-based proof-of-concept for integrating high-latency generative models with standard robotic control autonomy stacks.

</details>

---
