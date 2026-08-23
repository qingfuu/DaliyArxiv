# cs.SE | Software Engineering | 2026-08-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/A_Fully_Automated,_Deployment-Aware_Testing_Pipeline_for_IoT-Based_Automotive_Applications|A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications]]

![[assets/2608.19752_figure.png|800]]

- **arXiv**: [2608.19752](https://arxiv.org/abs/2608.19752)
- **PDF**: https://arxiv.org/pdf/2608.19752
- **详细分析**: [[20_Research/Papers/大模型/A_Fully_Automated,_Deployment-Aware_Testing_Pipeline_for_IoT-Based_Automotive_Applications|A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications]]
- **作者**: Denesa Zyberaj, Roman Vintonyak, Pascal Hirmer, Marco Aiello
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Testing embedded software in modern vehicles is challenging due to system complexity, decentralized architectures, and strict safety and performance constraints. In this work, we present an end-to-end, deployment-aware testing pipeline for IoT-based automotive applications. The pipeline combines requirement-driven test and code generation with large language model (LLM) and vision-language model (VLM) assistance, and human-in-the-loop curation to reduce manual effort and improve consistency. Using Eclipse openDuT, it supports flexible, distributed deployment across geographically separated cyber-physical and IoT infrastructures, optimizing for node availability and cross-organizational coordination. For validation, we conduct a case study using a Child Presence Detection System (CPDS), achieving full functional requirement coverage across all 9 requirements and 100% Gherkin generation accuracy on the controlled requirement set. Distributed test execution across geographically separated ECUs via Eclipse openDuT confirms the pipeline's applicability to OEM--supplier testing workflows.

</details>

---
