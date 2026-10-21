# cs.NI | Networking and Internet Architecture | 2026-10-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/LLM-Guided_Dual-Stage_Latency_Optimization_for_Closed-Loop_6G_V2I_Digital_Twins|LLM-Guided Dual-Stage Latency Optimization for Closed-Loop 6G V2I Digital Twins]]

![[assets/2610.22848_figure.png|800]]

- **arXiv**: [2610.22848](https://arxiv.org/abs/2610.22848)
- **PDF**: https://arxiv.org/pdf/2610.22848
- **详细分析**: [[20_Research/Papers/大模型/LLM-Guided_Dual-Stage_Latency_Optimization_for_Closed-Loop_6G_V2I_Digital_Twins|LLM-Guided Dual-Stage Latency Optimization for Closed-Loop 6G V2I Digital Twins]]
- **作者**: Liu Cao, Peide Li, Yuan Yang, Zhaoyu Liu, Lyutianyang Zhang, Jinke Ren, Shuguang Cui
- **cs 子类**: cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.6，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《LLM-Guided Dual-Stage Latency Optimization for Closed-Loop 6G V2I Digital Twins》归入 大模型、强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LLM-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wireless Digital Twins are emerging as a key enabler for predictive network control in 6G Vehicle-to-Infrastructure (V2I) systems. However, closed-loop V2I DTs face two dual-stage communication bottlenecks arising from model parameter exchange for V2I DT reconstruction and multi-service V2I traffic delivery after each reconstruction. This paper proposes a closed-loop dual-stage End-to-End (E2E) latency optimization framework that integrates Compressed Personalized Federated Learning with a unified Large-Language-Model-guided Multi-Agent Reinforcement Learning approach. A CPFL-enabled decision-oriented V2I DT is first constructed by jointly predicting Path Loss (PL) and Quality-of-Experience (QoE)-oriented Key Performance Indicators (KPIs). Then the framework comprises two temporally coupled but latency-wise distinct optimization stages: Stage I minimizes the joint Uplink (UL) and Downlink (DL) E2E transmission latency of compressed shared backbone's parameters, and Stage II minimizes the service-aware E2E latency of multi-service V2I traffic. As the two stages share aligned agent roles and action space, we develop a unified Semantic-Aware Guidance-Enhanced Multi-Agent Proximal Policy Optimization framework, in which the LLM acts as a training-time semantic planner that provides high-level traffic splitting and power allocation guidance to reduce inefficient exploration, while the MARL agents execute feasible low-level actions. Simulation results demonstrate that the proposed framework enables efficient V2I DT reconstruction and significantly reduces both E2E latency for DT reconstruction and multi-service V2I traffic. The proposed SAGE-MAPPO supports cross-stage policy reuse by sequentially solving the two stages within each DT update cycle, which accelerates convergence relative to the existing baselines and facilitates timely DT updates in dynamic V2I scenarios.

</details>

---
