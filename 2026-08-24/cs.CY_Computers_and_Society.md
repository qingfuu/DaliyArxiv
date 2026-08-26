# cs.CY | Computers and Society | 2026-08-24

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/其他/Invisible_Agents,_Uninformed_Patients_Towards_Responsible_Deployment_Of_Autonomous_AI_Diagnostic_Agents_In_Sub-Saharan_Africa|Invisible Agents, Uninformed Patients: Towards Responsible Deployment Of Autonomous AI Diagnostic Agents In Sub-Saharan Africa]]

![[assets/2608.21326_figure.png|800]]

- **arXiv**: [2608.21326](https://arxiv.org/abs/2608.21326)
- **PDF**: https://arxiv.org/pdf/2608.21326
- **详细分析**: [[20_Research/Papers/其他/Invisible_Agents,_Uninformed_Patients_Towards_Responsible_Deployment_Of_Autonomous_AI_Diagnostic_Agents_In_Sub-Saharan_Africa|Invisible Agents, Uninformed Patients: Towards Responsible Deployment Of Autonomous AI Diagnostic Agents In Sub-Saharan Africa]]
- **作者**: Percy Brown, Kweku Yamoah
- **cs 子类**: cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, ComputerVision, Systems

#### 研究背景与动机

《Invisible Agents, Uninformed Patients: Towards Responsible Deployment Of Autonomous AI Diagnostic Agents In Sub-Saharan Africa》归入 大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous AI diagnostic agents, systems that analyse patient-specific clinical data and produce diagnostic outputs or triage decisions without mandatory real-time human review, are increasingly deployed across eHealth platforms in sub-Saharan Africa at a pace that has outrun the governance infrastructure needed to oversee them. While significant bodies of work address AI accountability, transparency and explainability in healthcare, existing frameworks are largely clinician-centered and assume regulatory conditions that do not uniformly exist in low-resource settings. A patient-centered analysis of the disparity in patient awareness regarding autonomous agents, which results in a structural accountability gap, is mostly missing from the literature. This paper synthesizes existing research on informed consent, algorithmic accountability, and explainable AI to highlight three distinct challenges introduced by deploying AI agents in the sub-Saharan African context. Drawing on three documented deployment cases, including computer-aided tuberculosis detection in Tanzania, diabetic retinopathy and TB screening in Zambia, and mobile health chat-bot triage in Ghana, it demonstrates that these gaps are already present in active deployments across the region. In response, the paper proposes three foundational principles; agent-aware informed consent, human override as a structural requirement and contextually adapted explainability. This triad of principles lays a practical minimum standard for developers, health system administrators and policymakers in contexts where formal AI regulation remains nascent.

</details>

---

### [[20_Research/Papers/大模型/Distilling_Black-Box_Machine_Learning_into_a_Small,_Self-Explaining_Language_Model_for_Learning_Analytics|Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics]]

![[assets/2608.21165_figure.png|800]]

- **arXiv**: [2608.21165](https://arxiv.org/abs/2608.21165)
- **PDF**: https://arxiv.org/pdf/2608.21165
- **详细分析**: [[20_Research/Papers/大模型/Distilling_Black-Box_Machine_Learning_into_a_Small,_Self-Explaining_Language_Model_for_Learning_Analytics|Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics]]
- **作者**: Chenguang Pan, Airui Meng, Youmi Suk
- **cs 子类**: cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics》归入 大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning analytics increasingly relies on flexible machine learning (ML), but the model opacity and the burden of deployment prevent these tools from reaching educational practice. We propose a two-stage fine-tuning pipeline that distills a fitted black-box estimator and its post hoc interpretation (the mentor) into a small, open-weight large language model (LLM; the mentee) that returns an individual-level estimate and explains in natural language. The design is estimator-agnostic and paired with a faithfulness-first evaluation framework that audits every narration against the attribution it claims to describe. We design a simulation study that separates distillation loss from estimator loss by comparing an oracle mentor with a realistic ML mentor. Given an oracle signal, distillation with a two-billion-parameter LLM model is nearly lossless in recovering the effect surface (r &gt; .90), perfectly ranking the important variables, and citing no spurious covariate. Under a realistic estimator, almost all remaining error originates upstream. We find that fluency is no evidence of correctness since narration quality is independent of signal quality, and decision quality collapses toward the majority action in severely imbalanced settings. Applied to a nationally representative dataset, the pipeline recovers the finding that advanced mathematics coursework benefits students least likely to enroll in four-year college the most, with 98.8% of narrations passing the audit and no fabricated quantities. The result is a single fine-tuned LLM that predicts and explains offline on a commodity laptop, so student records never leave the machine.

</details>

---
