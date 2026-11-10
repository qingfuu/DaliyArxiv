# cs.HC | Human-Computer Interaction | 2026-11-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/What_Limits_mmWave_Human-State_Sensing_for_Robot_Perception|What Limits mmWave Human-State Sensing for Robot Perception?]]

![[assets/2611.08863_figure.png|800]]

- **arXiv**: [2611.08863](https://arxiv.org/abs/2611.08863)
- **PDF**: https://arxiv.org/pdf/2611.08863
- **详细分析**: [[20_Research/Papers/机器人/What_Limits_mmWave_Human-State_Sensing_for_Robot_Perception|What Limits mmWave Human-State Sensing for Robot Perception?]]
- **作者**: Shuntian Zheng, Guangming Wang, Hongyang He, Shuai He, Yu Guan
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Security

#### 研究背景与动机

《What Limits mmWave Human-State Sensing for Robot Perception?》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assistive robots and search-and-rescue platforms require reliable human state sensing in smoke, darkness, and privacy-sensitive environments, where cameras and LiDAR may be unreliable Millimeter-wave radar offers an alternative that works without ambient light, penetrates smoke, and does not capture visual appearance. However, the compact arrays that fit robot size, power, and cost budgets have limited apertures, producing joint-localization errors on the order of decimeters at a few meters, large enough to compromise the safety margins and tracking accuracy a robot depends on. Existing pipelines reduce pose error through frame fusion, multiple viewpoints, return selection, or stronger estimators, but examine one technique at a time, without relating its effect to a shared measurement limit or separating gains from added information from gains from estimator completion. We address this gap with a framework that models the human and environment as one time-varying scattering field and states a Cramer-Rao type error floor for joint localization as a function of bandwidth, aperture, signal-to-noise ratio, fused frame count, phase coherence, and visibility of retained returns. We then use existing frame fusion, multi viewpoint, return selection, and pose estimation methods as matched probes of this floor rather than as competing pipelines. Under the evaluated conditions, experiments on three datasets and a live deployment show these strategies move joint localization error in the predicted directions, for example lowering mean per-joint position error from about 97 to 65 mm with a second viewpoint, while a stronger estimator mainly lowers overall error by completing joints the measurement cannot resolve. These results give the robotics community a principled basis for deciding whether to prioritize observation design or estimator capacity when deploying reliable mmWave human sensing.

</details>

---
