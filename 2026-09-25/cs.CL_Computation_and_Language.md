# cs.CL | Computation and Language | 2026-09-25

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/具身智能/Free_the_Language_Model_From_the_Vision_Encoder_Semantic_Serialization_as_a_Perception_Interface_for_Small_Language_Models|Free the Language Model From the Vision Encoder: Semantic Serialization as a Perception Interface for Small Language Models]]

![[assets/2609.29601_figure.png|800]]

- **arXiv**: [2609.29601](https://arxiv.org/abs/2609.29601)
- **PDF**: https://arxiv.org/pdf/2609.29601
- **详细分析**: [[20_Research/Papers/具身智能/Free_the_Language_Model_From_the_Vision_Encoder_Semantic_Serialization_as_a_Perception_Interface_for_Small_Language_Models|Free the Language Model From the Vision Encoder: Semantic Serialization as a Perception Interface for Small Language Models]]
- **作者**: Cong Xu, Ravi Sankar
- **cs 子类**: cs.CL, cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.95（加权：具身智能 0.6，大模型 0.85，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Free the Language Model From the Vision Encoder: Semantic Serialization as a Perception Interface for Small Language Models》归入 大模型、具身智能、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end vision-language models (VLMs) bind visual competence to the scale of their language model: as the language model shrinks, perception and reasoning degrade together. We study an embodied scene question-answering (QA) interface in which vision never enters the language model. A frozen perception stack detects and ranges objects; a deterministic semantic serializer compiles the perceived state, errors included, into decision-aligned text; an unmodified text-only large language model (LLM) answers. On a visible-scope-matched, occlusion-audited campus-robot benchmark, under a prospectively frozen criterion, the serialized interface, using detectors fine-tuned in-domain within each fold, outperforms a zero-shot VLM whose language model has the same 7B scale (0.7892 vs 0.7462), with a larger margin at 3B (0.7673 vs 0.6913). Preregistered decoupling experiments show the gain survives paraphrase, attributing it to decision-aligned computation rather than answer-string leakage, while novel judgment vocabularies bound its scope. The advantage grows as the reader shrinks to 1.5B and reverses at 0.5B, and a ground-truth oracle locates the reader-capability floor. Under matched task supervision the interfaces converge: a VLM fine-tuned with low-rank adaptation (LoRA) overtakes the zero-shot system but only ties an equally supervised text reader (0.8441 vs 0.8396, no statistically resolved difference), and both routes remain perception-bound. Reported perception parameters are comparable to those of the VLM's vision tower, and total compute is not smaller.

</details>

---

### [[20_Research/Papers/强化学习/EAGER_Enhancing_Generative_Event_Extraction_via_Reinforcement_Learning_with_Verifiable_Rewards|EAGER: Enhancing Generative Event Extraction via Reinforcement Learning with Verifiable Rewards]]

![[assets/2609.29230_first_page.png|800]]

- **arXiv**: [2609.29230](https://arxiv.org/abs/2609.29230)
- **PDF**: https://arxiv.org/pdf/2609.29230
- **详细分析**: [[20_Research/Papers/强化学习/EAGER_Enhancing_Generative_Event_Extraction_via_Reinforcement_Learning_with_Verifiable_Rewards|EAGER: Enhancing Generative Event Extraction via Reinforcement Learning with Verifiable Rewards]]
- **作者**: Omar Adjali, Siting Liang, Omair Shahzad Bhatti, Daniel Sonntag
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《EAGER: Enhancing Generative Event Extraction via Reinforcement Learning with Verifiable Rewards》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EventRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end event extraction remains challenging for large language models as it requires simultaneous identification of event triggers, classification of event types, and extraction of schema-grounded argument spans. We present EAGER, a reinforcement learning framework for generative event extraction that combines fine-grained verifiable rewards with Schema-Contrastive Advantage Estimation to alleviate advantage collapse under sparse binary rewards. Our reward design explicitly targets structural validity, extraction accuracy, groundedness, coverage, over-generation, and span precision. Experiments across seven benchmark datasets show that EAGER consistently outperforms prompting, supervised fine-tuning, and prior reinforcement learning baselines, achieving a substantial improvement over the strongest prior method. Results demonstrate that task-aligned verifiable rewards and contrastive advantage estimation substantially improve structured extraction.

</details>

---
