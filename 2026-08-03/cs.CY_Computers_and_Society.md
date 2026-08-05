# cs.CY | Computers and Society | 2026-08-03

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/IyawoBench_v2.0_Extended_Diagnostic_Evaluation_of_Large_Language_Model_Clinical_Triage_in_Nigerian_Primary_Care|IyawoBench v2.0: Extended Diagnostic Evaluation of Large Language Model Clinical Triage in Nigerian Primary Care]]

![[assets/2607.29085_figure.png|800]]

- **arXiv**: [2607.29085](https://arxiv.org/abs/2607.29085)
- **PDF**: https://arxiv.org/pdf/2607.29085
- **详细分析**: [[20_Research/Papers/大模型/IyawoBench_v2.0_Extended_Diagnostic_Evaluation_of_Large_Language_Model_Clinical_Triage_in_Nigerian_Primary_Care|IyawoBench v2.0: Extended Diagnostic Evaluation of Large Language Model Clinical Triage in Nigerian Primary Care]]
- **作者**: Anthonio Oladimeji Gabriel, Dimeji Olawuyi
- **cs 子类**: cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《IyawoBench v2.0: Extended Diagnostic Evaluation of Large Language Model Clinical Triage in Nigerian Primary Care》归入 大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IyawoBench, MamaBench, MedMCQA, MedQA, PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are being deployed as clinical triage tools in low and middle income countries where trained physicians are scarce. Existing safety metrics, however, produce misleading confidence: models scoring 100% on binary "did not send an emergency home" safety measures may nevertheless exhibit systematic failure modes that render them undeployable at scale. We present IyawoBench v2.0, an extended diagnostic evaluation of large language model clinical triage on 200 synthetic vignettes derived from 1,200 real patient encounters at 19 Nigerian primary health centres. We introduce a formal mathematical framework comprising fourteen definitions and two theorems that decompose triage safety into three distinct failure modes: Conservative Escalation Bias, Systematic Downgrade Bias, and Middle-Tier Instability. We propose the Escalation Bias Index and Expected Deployment Cost as novel metrics that expose failure modes hidden by conventional accuracy and sensitivity scores. Evaluated on three frontier models (Claude Sonnet 4.6, Llama 3.3 70B, Llama 3.1 8B) plus five naive baselines, we show that: (1) all three models exhibit at least one formal failure mode; (2) traditional sensitivity metrics conceal a 77 percentage point under-triage gap in Llama 3.1 8B; (3) the optimal model varies across three deployment scenarios (Emergency-Focused, System-Sustainability, Balanced), demonstrating that single-ranking benchmarks are inadequate for LMIC clinical AI selection. IyawoBench v2.0 provides both a rigorous benchmark and a diagnostic framework transferable to any triage-style clinical AI evaluation. All code, data, and analysis pipelines are publicly available.

</details>

---
