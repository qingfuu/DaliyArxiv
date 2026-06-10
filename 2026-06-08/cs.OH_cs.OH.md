# cs.OH | cs.OH | 2026-06-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/OPENPATH_A_Supervisor--Specialist_Agent_System_for_Personalized,_Accessible,_and_Multi-stop_Urban_Trip_Planning|OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning]]

![[assets/2606.07486_figure.png|800]]

- **arXiv**: [2606.07486](https://arxiv.org/abs/2606.07486)
- **PDF**: https://arxiv.org/pdf/2606.07486
- **详细分析**: [[20_Research/Papers/大模型/OPENPATH_A_Supervisor--Specialist_Agent_System_for_Personalized,_Accessible,_and_Multi-stop_Urban_Trip_Planning|OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning]]
- **作者**: Ziyang Xiong, He Zong, Zhiyuan Xue, Manxi Wu
- **cs 子类**: 
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning》归入 大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Urban trip-planning systems are commonly optimized for travel time and cost, but they offer limited support for the heterogeneous needs that real travelers bring, such as personalized preferences, multi-stop itinerary construction, and end-to-end wheelchair accessibility. We present openpaths, a supervisor-specialist multi-agent system that handles all of these tasks within a single architecture. openpaths adopts a deliberate division of labor: LLM agents parse natural-language input, classify request intent, and orchestrate execution, while classical algorithms perform route optimization over curated mobility and accessibility data. This design ensures that the resulting trip honors heterogeneous user preferences and enforces strict accessibility requirements when requested. Beyond per-user planning, openpaths doubles as a measurement instrument for city-scale accessibility analysis: applied to NYC, the system reveals substantial ADA infrastructure gaps and quantifies their effect on job accessibility for wheelchair users. Overall, this study shows how a supervisor-specialist LLM agentic framework can support heterogeneous trip planning and transparent, equitable transportation analysis in real urban environments.

</details>

---
