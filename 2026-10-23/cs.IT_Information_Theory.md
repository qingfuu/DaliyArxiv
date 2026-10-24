# cs.IT | Information Theory | 2026-10-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Outage_Analysis_and_Bilevel_Resource_Optimization_in_RIS-Assisted_Clustered_UAV-NOMA_Networks|Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks]]

![[assets/2610.30410_figure.png|800]]

- **arXiv**: [2610.30410](https://arxiv.org/abs/2610.30410)
- **PDF**: https://arxiv.org/pdf/2610.30410
- **详细分析**: [[20_Research/Papers/机器人/Outage_Analysis_and_Bilevel_Resource_Optimization_in_RIS-Assisted_Clustered_UAV-NOMA_Networks|Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks]]
- **作者**: Masoud Ghazikor, Ly V. Nguyen, Morteza Hashemi
- **cs 子类**: cs.IT
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: cs.IT

#### 研究背景与动机

《Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks》归入 机器人 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates RIS-assisted downlink UAV communications based on NOMA. Since conventional NOMA becomes difficult to scale as the number of UAVs grows, we develop a cluster-based UAV-NOMA framework in which a BS serves multiple UAV groups with the aid of partitionable RISs. Within this framework, we consider direct, RIS-only indirect, and composite links, and develop an analytical model for the received SNR and outage performance under Nakagami-$m$ and double Nakagami-$m$ fading with imperfect SIC. To enable scalable transmission, we introduce a greedy RIS-aware (GRIS) clustering method, which groups UAVs according to spatial and channel-related features. Based on the resulting clusters and RIS assignment, we formulate an efficiency-reliability bilevel optimization problem that jointly optimizes inter-cluster BS power allocation, intra-cluster NOMA power coefficients, and RIS element assignment. Specifically, the outer efficiency problem maximizes the average throughput across clusters, while the inner reliability problem minimizes the worst-UAV outage probability within each cluster. To solve the formulated problem, we propose a two-level iterative framework consisting of an inter-cluster outer-efficiency solver (IOS) and an intra-cluster inner-reliability solver (I2S), where I2S combines a grid-based progressive search (GPS) for NOMA power refinement with reliability-guided RIS element reassignment, and IOS updates the BS power weights. Numerical results demonstrate the effectiveness of GRIS clustering, while pre-optimization analysis reveals efficiency-reliability trade-offs in power allocation. Baseline comparisons illustrate the ability of IOS-I2S to balance efficiency and reliability, while ablation studies highlight the importance of joint optimization.

</details>

---
