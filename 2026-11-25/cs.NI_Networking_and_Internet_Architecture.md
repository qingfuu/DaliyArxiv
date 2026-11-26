# cs.NI | Networking and Internet Architecture | 2026-11-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Embodied_Intelligence_for_Spectrum_Map_Construction_in_Low-Altitude_Wireless_Networks|Embodied Intelligence for Spectrum Map Construction in Low-Altitude Wireless Networks]]

![[assets/2611.32799_figure.png|800]]

- **arXiv**: [2611.32799](https://arxiv.org/abs/2611.32799)
- **PDF**: https://arxiv.org/pdf/2611.32799
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Intelligence_for_Spectrum_Map_Construction_in_Low-Altitude_Wireless_Networks|Embodied Intelligence for Spectrum Map Construction in Low-Altitude Wireless Networks]]
- **作者**: Hongtao Liang, Yiyao Wan, Jiahuan Ji, Lingda Meng, Fuhui Zhou, Qihui Wu
- **cs 子类**: cs.NI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《Embodied Intelligence for Spectrum Map Construction in Low-Altitude Wireless Networks》归入 具身智能、机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, ECDNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate spectrum map construction by unmanned aerial vehicles (UAVs) is crucial for intelligent resource management in low-altitude wireless networks (LAWNs). Although various construction approaches have been investigated, their performance often degrades under extremely sparse sampling because purely data-driven models may not capture the underlying propagation physics. To address these challenges, an embodied intelligence framework is proposed, which synergistically integrates closed-loop perception-cognition-execution (PCE) coupling and embodied exploration to achieve precise and efficient spectrum construction. Based on this framework, a corresponding embodied cognition and decision network (ECDNet) with three tightly coupled modules is designed. Specifically, by leveraging distance-aware convolutions, the semantic bridge, and adaptive feature alignment mechanisms, ECDNet establishes the bidirectional information flow between construction and decision-making. Simulation results show that ECDNet achieves a root mean square error (RMSE) of 2.787 dBm at 4.00% sampling under the non-revisiting spiral protocol. Furthermore, a practical UAV-based spectrum construction platform is developed and field-deployed to provide prototype-level evidence that the sensing, cognition, and action modules execute as a closed loop on size, weight, and power constrained UAV edge devices.

</details>

---
