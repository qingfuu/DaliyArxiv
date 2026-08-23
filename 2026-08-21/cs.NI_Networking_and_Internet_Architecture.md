# cs.NI | Networking and Internet Architecture | 2026-08-21

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/RFWM_Physics-Guided_World_Model_for_Dynamic_Wireless_Radiance_Field_Generation|RFWM: Physics-Guided World Model for Dynamic Wireless Radiance Field Generation]]

![[assets/2608.19709_figure.png|800]]

- **arXiv**: [2608.19709](https://arxiv.org/abs/2608.19709)
- **PDF**: https://arxiv.org/pdf/2608.19709
- **详细分析**: [[20_Research/Papers/大模型/RFWM_Physics-Guided_World_Model_for_Dynamic_Wireless_Radiance_Field_Generation|RFWM: Physics-Guided World Model for Dynamic Wireless Radiance Field Generation]]
- **作者**: Zijiu Yang, Qianqian Yang
- **cs 子类**: cs.NI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Multimodal, WorldModel, Systems

#### 研究背景与动机

《RFWM: Physics-Guided World Model for Dynamic Wireless Radiance Field Generation》归入 世界模型、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Radio-frequency (RF) radiance-field modeling is essential for wireless network optimization and sensing, yet remains challenging in dynamic and unseen environments. Existing learning-based methods synthesize RF fields from sparse measurements, but most struggle to generalize to dynamic and unseen environments. To address this limitation, we propose RFWM, a physics-guided RF world model that maps multimodal physical conditions like visual dynamics and AP configurations to spatiotemporal RF fields. RFWM adopts a two-stage training strategy with physics-guided priors and constraints. In the first stage, RFWM adapts a pretrained visual diffusion backbone to RF trajectories to predict RF sequences from a few past RF inputs, while conditioning the backbone on a Friis-guided prior for coarse attenuation guidance. In the second stage, RFWM learns the physical-to-RF mapping by training a ControlNet from scratch and fine-tuning the RF-adapted backbone, while six physics-guided regularizers enforce fine-grained propagation consistency. Cross-height heads then jointly generate RF trajectories at queried receiver heights in one forward pass. We construct a new benchmark of 7,715 sequences averaging 33 frames across 115 environments for dynamic RF-field generation. Experimental results show that RFWM improves MSE by approximately 7 dB and 3 dB over the state of the art under in-distribution and out-of-distribution settings, respectively.

</details>

---

### [[20_Research/Papers/机器人/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks|Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks]]

![[assets/2608.19638_figure.png|800]]

- **arXiv**: [2608.19638](https://arxiv.org/abs/2608.19638)
- **PDF**: https://arxiv.org/pdf/2608.19638
- **详细分析**: [[20_Research/Papers/机器人/Digital_Tides_A_Fluid-Dynamic_Framework_for_Flux-Aware_Infrastructure_Provisioning_in_UAV_Logistics_Networks|Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks]]
- **作者**: Wen-Yu Dong, Song Zhao, Rui-Si Han, Qi Bi, Sheng Chen
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: cs.NI

#### 研究背景与动机

《Digital Tides: A Fluid-Dynamic Framework for Flux-Aware Infrastructure Provisioning in UAV Logistics Networks》归入 机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The emergence of high-frequency pulsating logistics unmanned aerial vehicle (UAV) swarms gives rise to ``Digital Tides'', i.e., complex traffic dynamics that challenge sustainable resource provisioning in mobile computing networks. Conventional infrastructure provisioning strategies, which typically rely on static snapshot-based analysis and localized density estimation, fail to capture the macroscopic advection of computational workloads. As a result, reactive resource activation suffers from inherent hysteresis, yielding nominal efficiency gains at the cost of mission-critical service loss at the advancing wavefront. To address this issue, we develop a fluid-based spatiotemporal framework by explicitly solving the continuity equation to characterize the macroscopic velocity field of the workload flow. Building on this framework, we propose a flux-aware asymmetric activation strategy that leverages the derived information flux vector as a kinematic precursor of demand propagation. Unlike symmetric thresholding, the proposed control logic decouples activation and deactivation dynamics. Theoretical analysis confirms the intrinsic spatial phase-lead of the flux signal and shows that the proposed strategy generates a proactive guard ring to compensate for service setup latency, including delays caused by mobile edge computing container cold-starts. We further derive closed-form expressions for instantaneous service availability and period-average energy efficiency. In addition, we formulate a quality-of-service-penalized metric to evaluate effective energy efficiency under strict outage constraints. Numerical results show that the proposed flux-driven strategy enables zero-latency tracking of the mobile wavefront and achieves a Pareto-optimal trade-off between service reliability and energy consumption, outperforming reactive baselines in dynamic logistics corridors.

</details>

---
