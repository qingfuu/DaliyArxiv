# cs.HC | Human-Computer Interaction | 2026-08-17

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Designing_Mobile_and_Wearable_Sensor-Fused_Conversational_Agents_for_Health_and_Wellbeing|Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing]]

![[assets/2608.14273_figure.png|800]]

- **arXiv**: [2608.14273](https://arxiv.org/abs/2608.14273)
- **PDF**: https://arxiv.org/pdf/2608.14273
- **详细分析**: [[20_Research/Papers/大模型/Designing_Mobile_and_Wearable_Sensor-Fused_Conversational_Agents_for_Health_and_Wellbeing|Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing]]
- **作者**: Hansoo Lee, Pablo Fonseca, Md Haseen Akhtar
- **cs 子类**: cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing》归入 大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile and wearable devices increasingly collect continuous wellbeing data, including sleep, activity, heart rate, stress, blood glucose, and blood pressure. Yet access to such data does not automatically help people interpret their condition or change behavior. Many health applications remain dashboard-first, presenting charts, thresholds, goals, and alerts while leaving users to decide what a change means and what action should follow. Conversely, generic LLM-based conversational agents (CAs) can provide fluent advice, but without personal sensor grounding, they cannot detect individualized patterns or provide contextual guidance. This three-hour tutorial teaches participants how to move from passive monitoring to actionable wellbeing dialogue. Participants examine a dashboard that combines wearable health-data visualization with conversational-agent feedback, then use Wearable Sensor-Dialogue Wellbeing Agent Studio (WSDWAS) to simulate wearables, generate sensor snapshots, configure agent personas and prompt blocks, and compare dialogue styles. Grounded in Positive Computing, the tutorial emphasizes autonomy, competence, privacy, safety, and boundaries between wellbeing support and medical advice.

</details>

---

### [[20_Research/Papers/大模型/FactorFlow_A_Visual_Analytics_Workspace_with_Large_Language_Model-Assisted_Interpretation_for_Factor_Analysis|FactorFlow: A Visual Analytics Workspace with Large Language Model-Assisted Interpretation for Factor Analysis]]

![[assets/2608.13585_figure.png|800]]

- **arXiv**: [2608.13585](https://arxiv.org/abs/2608.13585)
- **PDF**: https://arxiv.org/pdf/2608.13585
- **详细分析**: [[20_Research/Papers/大模型/FactorFlow_A_Visual_Analytics_Workspace_with_Large_Language_Model-Assisted_Interpretation_for_Factor_Analysis|FactorFlow: A Visual Analytics Workspace with Large Language Model-Assisted Interpretation for Factor Analysis]]
- **作者**: Justin Philip Tuazon, Joemari Olea, Richelle Ann Juayong
- **cs 子类**: cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《FactorFlow: A Visual Analytics Workspace with Large Language Model-Assisted Interpretation for Factor Analysis》归入 大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In exploratory factor analysis (EFA), one typically aims to extract and describe a small number of factors (i.e., latent variables) based on the relationships among numerous manifest variables (i.e., directly observable variables). In practice, performing EFA entails examining different factor models (and rotations) to identify the underlying latent structure. Now, the primary criterion for evaluating a factor model is interpretability. That is, the preferred model is the one that yields a meaningful, coherent, and theoretically defensible factor structure. However, gauging a model's interpretability is not a trivial task, as it is subjective and often requires keeping track of large amounts of information simultaneously. Because of this, researchers typically employ various visualizations to interpret models and determine the "best" one. Hence, we introduce FactorFlow, a visual analytics workspace for performing EFA end-to-end. Using FactorFlow, one can fit and rotate factor models, perform model diagnostics, and more. The main component of the tool is a dashboard with a comprehensive set of interactive visualizations, where a user can easily dissect a factor model and even compare two models side-by-side at the same time. Moreover, several large language models are integrated with FactorFlow, enabling the user to generate and assess automated factor interpretations written in natural language. With multiple views and readily available calculations, FactorFlow can enable the researcher to efficiently and effectively understand factors and ultimately, perform EFA. Finally, we conducted a usability study to identify strengths and weaknesses, and capture feedback to incorporate in the app.

</details>

---
