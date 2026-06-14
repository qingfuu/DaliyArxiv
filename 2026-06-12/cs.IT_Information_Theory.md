# cs.IT | Information Theory | 2026-06-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Active_Sensing-assisted_UAV_Communications_with_Jittering_Framework_and_Performance_Analysis|Active Sensing-assisted UAV Communications with Jittering: Framework and Performance Analysis]]

![[assets/2606.13036_figure.png|800]]

- **arXiv**: [2606.13036](https://arxiv.org/abs/2606.13036)
- **PDF**: https://arxiv.org/pdf/2606.13036
- **详细分析**: [[20_Research/Papers/机器人/Active_Sensing-assisted_UAV_Communications_with_Jittering_Framework_and_Performance_Analysis|Active Sensing-assisted UAV Communications with Jittering: Framework and Performance Analysis]]
- **作者**: Guangji Chen, Long Shi, Qingqing Wu, Qiaoyan Peng, Caihong Kai
- **cs 子类**: cs.IT
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: cs.IT

#### 研究背景与动机

《Active Sensing-assisted UAV Communications with Jittering: Framework and Performance Analysis》归入 机器人 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Providing reliable communication for unmanned aerial vehicles (UAVs) via existing cellular networks is crucial for enabling the rapid growth of the low-altitude economy. However, UAV jittering significantly degrades communication quality due to induced beam misalignment. Inspired by recent advances in integrated sensing and communication, we propose a novel two-stage active sensing-assisted communication framework tailored for ground-to-UAV links with jittering. Specifically, two schemes are conceived to leverage sensing for enhancing communication performance, namely the communication-oriented scheme and the sensing-oriented scheme. For the sensing-oriented scheme, deterministic signals are employed in the first stage to facilitate angle-of-arrival (AoA) acquisition at the UAV side, followed by pure communication service in the second stage by using the estimated AoA. In contrast, the communication-oriented scheme employs Gaussian information-bearing signals throughout both stages, with AoA estimation relying on Gaussian random signals. For both schemes, we provide maximum likelihood estimators for AoA, along with analytical results characterizing the Cramér-Rao bound. To capture the performance limit, closed-form expressions for the achievable rates of the two schemes are derived, unveiling a fundamental tradeoff between sensing and communication quality across the two stages by tuning the time allocated to the first stage. The optimal time allocation that maximizes the overall rate is obtained in semi-closed-form. Based on these results, we unveil a sufficient condition under which the communication-oriented scheme outperforms the sensing-oriented scheme, which admits an interesting threshold-based structure. Asymptotic analysis demonstrates that the performance loss of the proposed schemes relative to the jitter-free upper bound approaches zero in the high transmit power regime.

</details>

---
