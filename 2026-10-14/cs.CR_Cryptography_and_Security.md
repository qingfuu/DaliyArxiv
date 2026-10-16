# cs.CR | Cryptography and Security | 2026-10-14

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/RoboFake_Are_Deepfake_Detectors_Ready_for_Humanoid_Face_Robots|RoboFake: Are Deepfake Detectors Ready for Humanoid Face Robots?]]

![[assets/2610.14269_figure.png|800]]

- **arXiv**: [2610.14269](https://arxiv.org/abs/2610.14269)
- **PDF**: https://arxiv.org/pdf/2610.14269
- **详细分析**: [[20_Research/Papers/机器人/RoboFake_Are_Deepfake_Detectors_Ready_for_Humanoid_Face_Robots|RoboFake: Are Deepfake Detectors Ready for Humanoid Face Robots?]]
- **作者**: Hao Chen, Junnan Xu
- **cs 子类**: cs.CR, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《RoboFake: Are Deepfake Detectors Ready for Humanoid Face Robots?》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepfakeBench, EfficientNet, F3Net, YuNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid face robots can now move their lips in sync with speech and show detailed facial expressions. Give such a robot the face of a real person and drive it with generated speech, and you get a face forgery that happens in front of the camera: the camera records a real object, and no pixel is edited. We call this a RoboFake. In this paper we ask what current deepfake detectors do when they see a robot face. We test six public detectors trained on FaceForensics++ on video of a physical lip-syncing face robot, on a synthesized video of the same robot, and on rendered robot faces. All thresholds are fixed on FaceForensics++, and every result is compared with real human faces that went through the same processing as the robot videos. At a threshold that flags 5% of real faces, three detectors flag almost every physical robot frame, while two flag fewer than 7%. A matched human control and masking show that the response comes from the face, not from the processing or the background. However, it does not track synthesis: with only the face visible, three of the six detectors give the physical robot a higher fake score than its synthesized video. The response is also fragile, and light JPEG compression is enough to push most robot frames below the threshold for some detectors. Our results suggest that current detectors flag today's robots because their faces do not look human, not because they recognize a forgery. We release our evaluation protocol and code, and state three testable hypotheses about realistic, interactive RoboFakes.

</details>

---
