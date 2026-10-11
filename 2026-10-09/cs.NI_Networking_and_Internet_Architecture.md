# cs.NI | Networking and Internet Architecture | 2026-10-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Adaptive_E2E_Monitoring_Path_Selection_with_Deep_Reinforcement_Learning_in_Multi-domain_Optical_Networks|Adaptive E2E Monitoring Path Selection with Deep Reinforcement Learning in Multi-domain Optical Networks]]

![[assets/2610.10753_figure.png|800]]

- **arXiv**: [2610.10753](https://arxiv.org/abs/2610.10753)
- **PDF**: https://arxiv.org/pdf/2610.10753
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_E2E_Monitoring_Path_Selection_with_Deep_Reinforcement_Learning_in_Multi-domain_Optical_Networks|Adaptive E2E Monitoring Path Selection with Deep Reinforcement Learning in Multi-domain Optical Networks]]
- **作者**: Soham Choudhury, Martin Bojinov, Jason P. Jue, Genya Ishigaki
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Adaptive E2E Monitoring Path Selection with Deep Reinforcement Learning in Multi-domain Optical Networks》归入 强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Network slicing over multi-domain optical networks enables resource isolation for high-bandwidth, virtually-dedicated networks. However, guaranteeing end-to-end (E2E) performance remains challenging when domains withhold internal topology and performance metrics from external entities. Under this limited visibility, a control function (slice coordinator) needs to select E2E monitoring paths to detect and localize link failures. This paper formulates two complementary optimization problems, the initial and progressive monitoring path selection problems, which together realize closed-loop autonomous monitoring at the slice coordinator level. The initial problem maximizes failure coverage without prior information, while the progressive problem concentrates additional paths around suspected failure locations identified from prior monitoring. We propose a deep reinforcement learning (DRL) algorithm that adaptively selects an optimal set of monitoring paths for each phase. Experiments using the GNPy optical network simulator demonstrate that our approach outperforms baseline algorithms for both problems and achieves near-optimal localization in the initial selection, suggesting the feasibility of AI-driven closed-loop failure localization in future multi-domain optical network architectures.

</details>

---
