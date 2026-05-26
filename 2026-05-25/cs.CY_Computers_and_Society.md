# cs.CY | Computers and Society | 2026-05-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/IyàwóBench_A_Benchmark_for_Evaluating_Large_Language_Model_Clinical_Triage_Accuracy_on_Undifferentiated_Febrile_Illness_in_Nigerian_Primary_|IyàwóBench: A Benchmark for Evaluating Large Language Model Clinical Triage Accuracy on Undifferentiated Febrile Illness in Nigerian Primary Health Settings]]

![[assets/2605.23465_first_page.png|800]]

- **arXiv**: [2605.23465](https://arxiv.org/abs/2605.23465)
- **PDF**: https://arxiv.org/pdf/2605.23465
- **详细分析**: [[20_Research/Papers/大模型/IyàwóBench_A_Benchmark_for_Evaluating_Large_Language_Model_Clinical_Triage_Accuracy_on_Undifferentiated_Febrile_Illness_in_Nigerian_Primary_|IyàwóBench: A Benchmark for Evaluating Large Language Model Clinical Triage Accuracy on Undifferentiated Febrile Illness in Nigerian Primary Health Settings]]
- **作者**: Anthonio Oladimeji Gabriel, Dimeji Abdulsobur Olawuyi, Oloruntoba Ajayi, Temiloluwa Aderemi
- **cs 子类**: cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM

#### 研究背景与动机

在尼日利亚基层医疗场景中，发热但病因未明的患者是最常见的门诊就诊人群之一，分诊是否准确直接关系到是否需要立即转诊。现有面向医学问答或通用医疗任务的基准，多来自高收入国家或特定考试语料，难以反映西非基层卫生中心中由社区卫生工作者执行的真实分诊需求。作者指出，LLM 虽然在医学知识题上表现突出，但在本地疾病谱、指南约束和低资源就医环境下的临床分诊准确性仍缺少可复现评测，因此有必要构建贴近尼日利亚实际的 benchmark。

#### 方法概述和架构

论文提出 IyàwóBench v1.0，一个用于评估 LLM 在尼日利亚基层卫生场景中对“未分化发热”进行临床分诊的基准数据集。该基准包含 200 条合成临床病例，覆盖 8 类发热相关疾病，病例分布由在奥约州 19 个基层卫生中心收集的 1,200 例真实患者就诊统计特征生成，输入字段包括年龄、性别、体重、体温、心率、呼吸频率、血压、血氧、危险征象清单、疟疾快速检测结果、妊娠状态和自由文本备注。模型被要求基于 WHO IMCI、疟疾指南、脓毒症管理建议和尼日利亚标准治疗指南输出三类分诊结果之一：REFER_NOW、REFER_TODAY 或 TREAT_HERE，并给出主要诊断与一句推理说明。评测了 6 个模型，使用两个指标：triage accuracy 衡量分诊标签是否完全匹配，safety score 衡量在高危 REFER NOW 病例中是否把本该转诊的病例错误降级为 TREAT HERE。

#### 实验结果分析

在 6 个模型上，所有模型的 safety score 都达到 100%，说明它们都没有把任何一个高危 REFER NOW 病例误判为可在基层治疗。分诊准确率差异较大：Claude Sonnet 最高，为 67.5%；Llama 4 Scout 为 59.5%；Llama 3.3 70B 为 43.0%；Llama 3.1 8B 为 39.0%；Qwen 3 32B 和 GPT OSS 20B 的准确率接近于零，原因是输出格式不符合结构化解析要求。论文还指出，带有嵌入式 WHO 指南和专门临床工程设计的系统比通用模型最高可提升 28.5 个百分点，说明结构化输出约束与本地临床知识注入同样关键。

<details>
<summary>完整摘要</summary>

背景：未分化发热是尼日利亚基层医疗门诊就诊的首要原因，但目前尚无经过验证的基准，可用于评估大型语言模型（LLM）在西非基层卫生场景中的临床分诊推理能力。方法：我们提出 IyàwóBench v1.0，这是一个包含 200 条合成临床病例的数据库，覆盖 8 类发热性疾病，其分布依据在尼日利亚奥约州 19 个基层卫生中心收集的 1,200 例真实患者接诊记录的统计分布生成。我们评估了 6 个 LLM 在结构化分诊分类任务上的表现，使用两个指标：分诊准确率和安全评分。结果：6 个模型的安全评分均为 100%（95% CI：96.4–100.0%），在所有关键的 REFER NOW 病例中，没有模型将其错误降级为 TREAT HERE。分诊准确率差异显著：Claude Sonnet（claude-sonnet-4-5）为 67.5%（95% CI：60.8–73.7%），Llama 4 Scout 为 59.5%（52.5–66.2%），Llama 3.3 70B 为 43.0%（36.2–50.0%），Llama 3.1 8B 为 39.0%（32.4–45.9%）。其中两个模型由于不遵循结构化输出格式，表现出接近零的准确率。结论：现代 LLM 在分诊中表现出安全的行为，但其结构化临床准确性差异很大。嵌入 WHO 指南的临床工程化系统优于通用模型，最高可提升 28.5 个百分点。IyàwóBench 为西非基层医疗中的 LLM 临床决策支持提供了首个可复现的评测框架。

</details>

---
