# cs.HC | Human-Computer Interaction | 2026-07-03

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/When_Do_LLM_Personas_Support_Visualization_Design_A_Cross-Model_Study_of_Color_Assignment_and_Chart_Choice|When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice]]

![[assets/2607.02455_figure.png|800]]

- **arXiv**: [2607.02455](https://arxiv.org/abs/2607.02455)
- **PDF**: https://arxiv.org/pdf/2607.02455
- **详细分析**: [[20_Research/Papers/大模型/When_Do_LLM_Personas_Support_Visualization_Design_A_Cross-Model_Study_of_Color_Assignment_and_Chart_Choice|When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice]]
- **作者**: Shahreen Salim, Klaus Mueller
- **cs 子类**: cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice》归入 大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model personas are increasingly used to approximate diverse users during early-stage visualization design, but it remains unclear whether persona-conditioned outputs reflect stable personality effects or artifacts of model choice and task framing. We examine this question across two visualization-relevant tasks: color assignment for abstract and concrete concepts, and chart-idiom preference ratings across task contexts. Using 43 Big Five profiles across GPT-4o-mini, GPT-4.1-mini, and GPT-5-mini, we find that personality-color coupling is highly model-configuration dependent: absent in GPT-4o-mini for all six concepts, consistent in GPT-4.1-mini across all six, and partial in GPT-5-mini for two of six. Concept type further shapes the signal: for abstract concepts, personality explains more hue variance than model identity, while concrete concepts show smaller and comparable effects. In chart choice, trait-aligned cluster aggregation produces stable top-idiom rankings across all nine cluster-context combinations, but a no-persona baseline recovers the same top choice in 8 of 9 model-context cells, indicating that task context drives rank-1 selection more than personality. These findings position LLM personas as exploratory probes for visualization design, not substitutes for human participants, and motivate multi-model testing, concept-type disaggregation, and no-persona baselines in future studies.

</details>

---

### [[20_Research/Papers/机器人/Choreographing_the_Way_of_Water_A_Computational_Framework_for_Aquatic_Robotic_Art|Choreographing the Way of Water: A Computational Framework for Aquatic Robotic Art]]

![[assets/2607.02174_figure.jpg|800]]

- **arXiv**: [2607.02174](https://arxiv.org/abs/2607.02174)
- **PDF**: https://arxiv.org/pdf/2607.02174
- **详细分析**: [[20_Research/Papers/机器人/Choreographing_the_Way_of_Water_A_Computational_Framework_for_Aquatic_Robotic_Art|Choreographing the Way of Water: A Computational Framework for Aquatic Robotic Art]]
- **作者**: Aswin Ramachandran, Christopher Golling, Sebastian Burmester, Noa Sendlhofer, Jan Kamm, Ruiheng Jiang, Raffaello D'Andrea
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Choreographing the Way of Water: A Computational Framework for Aquatic Robotic Art》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic choreography in open water is governed by nonlinear fluid dynamics, which impose significant challenges due to environmental disturbances and nonlinear system dynamics. This paper presents the cyber-physical architecture of Way of Water, a vertically integrated framework that orchestrates a fleet of autonomous surface vessels as a distributed choreographic platform. Moving beyond the surface-pixel paradigm, these vessels use laminar nozzles and multi-zone lighting to extend their expressive range from the 2D water plane into the 3D volumetric domain. Our primary contribution is the Way of Water Studio, a browser-based, timeline-compositing authoring paradigm that treats the fleet as a DAW-like instrument for music-responsive choreography. The Studio encapsulates Sequential Convex Programming for trajectory generation and Model Predictive Control for disturbance rejection presented through a visual timeline, broadening access to high-performance aquatic robotics for non-programmer artists. Grounding the Studio is the full cyber-physical stack: a custom holonomic chassis, a state-estimation and control stack tuned for the aquatic domain, and an LTE/MQTT fleet link with RTK-GPS time synchronization. We report on the system's validation across two distinct deployments: an 18-vessel Swan Lake interpretation at Lake Zurich and an 8-vessel Time Space Existence 2025 Venice Biennale demonstration at Forte Marghera, establishing a foundational reference for the design and deployment of fluidic robotic swarms.

</details>

---
