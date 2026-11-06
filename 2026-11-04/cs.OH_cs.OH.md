# cs.OH | cs.OH | 2026-11-04

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/TriMedium_A_Cross-Medium_Simulator_for_Embodied_Networking_Across_Air-Ground-Sea|TriMedium: A Cross-Medium Simulator for Embodied Networking Across Air-Ground-Sea]]

![[assets/2611.04763_figure.png|800]]

- **arXiv**: [2611.04763](https://arxiv.org/abs/2611.04763)
- **PDF**: https://arxiv.org/pdf/2611.04763
- **详细分析**: [[20_Research/Papers/具身智能/TriMedium_A_Cross-Medium_Simulator_for_Embodied_Networking_Across_Air-Ground-Sea|TriMedium: A Cross-Medium Simulator for Embodied Networking Across Air-Ground-Sea]]
- **作者**: Ruizhe Dang, Jiayi Su, Wenlihan Lu, Weijie Yuan, Shijian Gao
- **cs 子类**: 
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 1.2，大模型 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《TriMedium: A Cross-Medium Simulator for Embodied Networking Across Air-Ground-Sea》归入 具身智能、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirSim, UNav-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligent applications have expanded from air and ground into maritime environments, where missions such as coastal reporting require coordination among underwater sensing, surface gateways, and aerial relays. Yet field trials remain costly, and existing simulation tools make it difficult to study how cross-medium communication affects cooperation among these platforms. We present TriMedium, an integrated Air-Ground-Sea simulator for cross-medium embodied networking. TriMedium has three design elements. First, it provides a shared three-dimensional world where aerial, terrestrial, and underwater entities coexist, so underwater agent motion and visual observations stay geometrically consistent with air and ground nodes. Second, it uses a common simulation clock that preserves observation timestamps while scheduling delayed communication and computation, clarifying when the shore receiver obtains each observation. Third, modular quantization and compression interfaces accommodate heterogeneous telemetry and image pipelines, while integrity checks separate intentional lossy distortion from incomplete or corrupted delivery. Three case studies validate TriMedium. Multimodal data delivery tests telemetry and image pipelines, scene construction examines cross-domain spatial consistency, and positioning assesses geometric accuracy under delayed communication. Together, they show TriMedium enables embodied networking by quantifying cross-medium delivery dynamics and fidelity across heterogeneous payloads.

</details>

---
