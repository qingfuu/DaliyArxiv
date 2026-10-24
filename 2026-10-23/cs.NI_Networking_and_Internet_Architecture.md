# cs.NI | Networking and Internet Architecture | 2026-10-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/AERIAL_Mission-Aware_LLM_Selection_for_Language-Driven_UAV_Control_in_Flying_Networks|AERIAL: Mission-Aware LLM Selection for Language-Driven UAV Control in Flying Networks]]

![[assets/2610.31029_figure.png|800]]

- **arXiv**: [2610.31029](https://arxiv.org/abs/2610.31029)
- **PDF**: https://arxiv.org/pdf/2610.31029
- **详细分析**: [[20_Research/Papers/具身智能/AERIAL_Mission-Aware_LLM_Selection_for_Language-Driven_UAV_Control_in_Flying_Networks|AERIAL: Mission-Aware LLM Selection for Language-Driven UAV Control in Flying Networks]]
- **作者**: Diana Nunes, Ricardo Amorim, Pedro Ribeiro, André Coelho, Rui Campos
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，机器人 0.8）
- **关联关键词**: LLM, EmbodiedAI

#### 研究背景与动机

《AERIAL: Mission-Aware LLM Selection for Language-Driven UAV Control in Flying Networks》归入 机器人、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned Aerial Vehicles (UAVs) in Flying Networks (FNs) increasingly require mechanisms to translate high-level natural language objectives into executable missions. Although Large Language Models (LLMs) have demonstrated the feasibility of language-driven UAV control, existing approaches typically rely on static model configurations and overlook mission-aware performance variability. This paper presents AERIAL, a benchmark-driven framework for adaptive LLM selection in hybrid edge-cloud UAV control. AERIAL separates systematic model benchmarking from mission execution, deriving empirical scenario-model mappings and applying them at runtime for mission-aware selection. Evaluation across 720 automated simulation runs spanning navigation, spatial reasoning, and algorithm invocation revealed significant performance variability depending on scenario-model pairing. A case study integrating AERIAL with a FNs placement algorithm further validated the framework's ability to interface with domain-specific optimization modules through natural language. These results validate the effectiveness of AERIAL's adaptive model selection in improving reliability and operational robustness for autonomous UAV control in FNs.

</details>

---
