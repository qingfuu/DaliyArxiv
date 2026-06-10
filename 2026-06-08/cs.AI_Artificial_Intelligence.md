# cs.AI | Artificial Intelligence | 2026-06-08

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/机器人/Re-imagining_ISO_26262_in_the_Age_of_Autonomous_Vehicles_Enhancing_Controllability_through_Transferability_and_Predictability|Re-imagining ISO 26262 in the Age of Autonomous Vehicles: Enhancing Controllability through Transferability and Predictability]]

![[assets/2606.07437_first_page.png|800]]

- **arXiv**: [2606.07437](https://arxiv.org/abs/2606.07437)
- **PDF**: https://arxiv.org/pdf/2606.07437
- **详细分析**: [[20_Research/Papers/机器人/Re-imagining_ISO_26262_in_the_Age_of_Autonomous_Vehicles_Enhancing_Controllability_through_Transferability_and_Predictability|Re-imagining ISO 26262 in the Age of Autonomous Vehicles: Enhancing Controllability through Transferability and Predictability]]
- **作者**: Chaitanya Shinde, Hadi Hajieghrary, Paul Schmitt, Adam Shoemaker, Bodo Seifert, Steve Kenner
- **cs 子类**: cs.AI, cs.HC, cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Re-imagining ISO 26262 in the Age of Autonomous Vehicles: Enhancing Controllability through Transferability and Predictability》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The ISO 26262 standard defines functional safety for road vehicles through risk assessments based on Severity, Exposure, and Controllability, grounded in a human-driven vehicle paradigm. In the context of autonomous vehicles (AVs), the absence of a human driver necessitates revisiting these principles. This paper decomposes the Controllability placeholder into two auditable evidence dimensions of ISO 26262 by introducing two measurable sub-concepts: Transferability and Predictability. Transferability extends Controllability to capture AV systems' ability to hand off control to dedicated fallback safety mechanisms, while Predictability captures how easily external agents can anticipate AV behavior. Predictability is formally defined from human-robot interaction-inspired principles, and a mathematical framework is provided to quantify it. A designed-versus-achievable gap is introduced to distinguish architectural fallback claims from scene-conditioned achievable fallback capability. The proposed metrics align with ISO 26262 and ISO/PAS 21448 (SOTIF), rendering fallback and interaction claims falsifiable and traceable across ODD slices. These dimensions complement rather than replace existing standards, and the enhancements preserve the structure of ISO 26262 while extending its applicability to driverless automated systems operating at SAE Levels 4 and 5.

</details>

---

### [[20_Research/Papers/大模型/Socratic-SWE_Self-Evolving_Coding_Agents_via_Trace-Derived_Agent_Skills|Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills]]

![[assets/2606.07412_first_page.png|800]]

- **arXiv**: [2606.07412](https://arxiv.org/abs/2606.07412)
- **PDF**: https://arxiv.org/pdf/2606.07412
- **详细分析**: [[20_Research/Papers/大模型/Socratic-SWE_Self-Evolving_Coding_Agents_via_Trace-Derived_Agent_Skills|Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills]]
- **作者**: Chuan Xiao, Zhengbo Jiao, Shaobo Wang, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang, Lin Qu
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-driven software engineering agents have become a central testbed for real-world language-model capability, yet their training remains limited by the availability of high-quality SWE tasks. Existing synthetic data methods typically create tasks through fixed mutation or bug-injection procedures, making the resulting distributions largely independent of the agent's own weaknesses and training progress. We introduce Socratic-SWE, a closed-loop self-evolution framework that reuses the agent's historical solving traces as a source of training signal. Rather than treating traces only as evidence for reward computation, Socratic-SWE distills them into structured agent skills that summarize recurring failures and effective repair patterns. These skills then guide the generation of targeted repair tasks in real repositories. Candidate tasks are checked through execution-based validation and scored with a solver-gradient alignment reward, so that the retained tasks are both verifiable and useful for improving the Solver. The updated Solver produces new traces, enabling the task curriculum to adapt over successive rounds. Across SWE-bench Verified, SWE-bench Lite, SWE-bench Pro, and Terminal-Bench 2.0, Socratic-SWE consistently improves over self-evolving baselines under the same compute budget, reaching 50.40% on SWE-bench Verified after three iterations. These results suggest that solving traces can serve as a scalable substrate for self-evolving SWE agents.

</details>

---

### [[20_Research/Papers/大模型/Online_Pandora's_Box_for_Contextual_LLM_Cascading|Online Pandora's Box for Contextual LLM Cascading]]

![[assets/2606.07392_first_page.png|800]]

- **arXiv**: [2606.07392](https://arxiv.org/abs/2606.07392)
- **PDF**: https://arxiv.org/pdf/2606.07392
- **详细分析**: [[20_Research/Papers/大模型/Online_Pandora's_Box_for_Contextual_LLM_Cascading|Online Pandora's Box for Contextual LLM Cascading]]
- **作者**: Alexandre Belloni, Yan Chen, Yehua Wei
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Online Pandora's Box for Contextual LLM Cascading》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motivated by Large Language Model (LLM) cascading, we propose an online contextual Pandora's Box model for adaptively querying and selecting LLM APIs. In each period, a decision-maker observes a request context and faces a two-phase decision problem. In the query phase, the decision-maker sequentially queries APIs, where each query reveals a generated output and the decision-maker incurs an (output-dependent) cost. In the selection phase, the decision-maker selects one of the generated outputs to deploy and observes only the downstream reward of the deployed output. This output-mediated feedback structure differs from classical online contextual Pandora's Box models, in which opening a box directly reveals its reward. Rather than estimating the full conditional output and cost distributions of each API, we directly model the reservation index and develop a learning approach for the query phase. Specifically, we impose a parametric structure on the contextual reservation index functions induced by the classical Weitzman's policy. Our policy combines generalized method of moments (GMM) type estimation of these reservation indices with UCB-style confidence bounds for both these indices and the shared output-level reward evaluator. Under regularity conditions, we prove that the resulting policy achieves dimension-dependent $\widetilde O(\sqrt T)$ cumulative regret over a horizon of $T$ periods.

</details>

---

### [[20_Research/Papers/强化学习/Do_Coding_Agents_Deceive_Us_Detecting_and_Preventing_Cheating_via_Capped_Evaluation_with_Randomized_Tests|Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests]]

![[assets/2606.07379_figure.png|800]]

- **arXiv**: [2606.07379](https://arxiv.org/abs/2606.07379)
- **PDF**: https://arxiv.org/pdf/2606.07379
- **详细分析**: [[20_Research/Papers/强化学习/Do_Coding_Agents_Deceive_Us_Detecting_and_Preventing_Cheating_via_Capped_Evaluation_with_Randomized_Tests|Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests]]
- **作者**: Thanawat Lodkaew, Johannes Ackermann, Soichiro Nishimori, Nontawat Charoenphakdee, Masashi Sugiyama, Takashi Ishida
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A growing failure mode in agent evaluation and training is that models can achieve high evaluation scores by exploiting shortcuts instead of solving the intended task, producing deceptive performance. This makes evaluation scores unreliable as measures of true task-solving ability. We propose CapCode, a framework for constructing coding datasets with randomized tests whose best achievable non-cheating performance is deliberately capped below one. This capped-performance design gives evaluation scores a clearer interpretation: scores substantially above the cap are implausible and therefore provide evidence of cheating. To prevent cheating, we propose CapReward, a reward design based on the CapCode principle to discourage optimization beyond the cap. Experiments across multiple datasets show that CapCode detects cheating while preserving performance ranking of models, and CapReward reduces cheating behavior, yielding models that better follow the intended task specification.

</details>

---

### [[20_Research/Papers/大模型/A_robust_PPG_foundation_model_using_multimodal_physiological_supervision|A robust PPG foundation model using multimodal physiological supervision]]

![[assets/2606.07365_figure.png|800]]

- **arXiv**: [2606.07365](https://arxiv.org/abs/2606.07365)
- **PDF**: https://arxiv.org/pdf/2606.07365
- **详细分析**: [[20_Research/Papers/大模型/A_robust_PPG_foundation_model_using_multimodal_physiological_supervision|A robust PPG foundation model using multimodal physiological supervision]]
- **作者**: Eloy Geenjaar, Vince Calhoun, Scott Daly, Gouthaman KV, Lie Lu, Trisha Mittal, Daniel P. Darcy
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《A robust PPG foundation model using multimodal physiological supervision》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Photoplethysmography (PPG), a non-invasive measure of changes in blood volume, is widely used in both wearable devices and clinical settings. Recent PPG foundation models either use open-source ICU datasets with pretraining paradigms that require curated data and thus complicate generalization to field-like data, or use closed-source field-like PPG data. In contrast, we propose a PPG foundation model that does not require high-quality or field-like pretraining data, and instead leverages accompanying electrocardiogram and respiratory signals in ICU datasets to select contrastive samples during pretraining. Our approach allows the model to retain and learn from noisy PPG segments, improving robustness at inference. Our model, pretrained on 3x fewer subjects than existing state-of-the-art approaches, achieves performance improvements on 14 out of 15 diverse downstream tasks, including field-like daily activity and heart rate prediction. Our results demonstrate that multimodal supervision can integrate complementary physiological information to improve the robustness of PPG foundation models and enhance their generalization to consumer-grade data.

</details>

---

### [[20_Research/Papers/大模型/Hierarchical_Certified_Semantic_Commitment_for_Byzantine-Resilient_LLM-Agent_Collaboration|Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration]]

![[assets/2606.07316_figure.png|800]]

- **arXiv**: [2606.07316](https://arxiv.org/abs/2606.07316)
- **PDF**: https://arxiv.org/pdf/2606.07316
- **详细分析**: [[20_Research/Papers/大模型/Hierarchical_Certified_Semantic_Commitment_for_Byzantine-Resilient_LLM-Agent_Collaboration|Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration]]
- **作者**: Haoran Xu, Lei Zhang, Iadh Ounis, Xianbin Wang
- **cs 子类**: cs.AI, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Byzantine collaboration among large-language-model agents requires a finality-control primitive: given delivered stochastic, structured natural-language proposals, the protocol must decide whether the round supports a commit, what kind of commit, or a typed safe abort. Naive aggregation hides this choice behind a single verdict; classical Byzantine fault tolerance hides it behind byte-identity that LLM proposals do not satisfy. We introduce Hierarchical Certified Semantic Commitment (H-CSC), a BFT-inspired protocol that converts embedding-derived finality signals over verdict-conditioned proposal groups into one of three typed outcomes: a semantic_commit (a 2f+1 within-verdict semantic core backs the verdict, emitting a parameter-bound digest over the quantised aggregate), a verdict_commit (strong verdict margin but dispersed semantic rationale, emitting a verdict-level certificate without claiming a semantic aggregate), or an explicit abort with a typed reason. The contribution is typed finality, not raw commit accuracy. On a controlled semantic-poisoning diagnostic (BCS_v1, 120 episodes), H-CSC commits with low angular deviation on BFT-feasible buckets (0.31 to 2.04 degrees) and aborts 100% of beyond-BFT rounds (n&lt;3f+1) as intended. On a real LLM-agent claim-verification benchmark (MVR-50, 50 tasks) under paired static and rushing Byzantine attacks, H-CSC commits 0.90/0.92 with honest-reference-invalid rates of 0.02/0.00, statistically matching a strong certificate-emitting verdict-only baseline. Unlike that baseline, H-CSC also emits an embedding-backed semantic_commit digest on 74%/72% of rounds, supplying typed provenance. A strict-semantic ablation commits only 0.54/0.48, showing the verdict-level fallback is necessary for coverage (+0.36/+0.44) at the same &lt;=0.04 safety floor; a 100-task cross-model check across four LLMs preserves invalid_hmaj within 0.00 to 0.03.

</details>

---

### [[20_Research/Papers/机器人/An_Abstract_Architecture_for_Explainable_Autonomy_in_Hazardous_Environments|An Abstract Architecture for Explainable Autonomy in Hazardous Environments]]

![[assets/2606.07211_figure.png|800]]

- **arXiv**: [2606.07211](https://arxiv.org/abs/2606.07211)
- **PDF**: https://arxiv.org/pdf/2606.07211
- **详细分析**: [[20_Research/Papers/机器人/An_Abstract_Architecture_for_Explainable_Autonomy_in_Hazardous_Environments|An Abstract Architecture for Explainable Autonomy in Hazardous Environments]]
- **作者**: Matt Luckcuck, Hazel M Taylor, Marie Farrell
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Security, Systems

#### 研究背景与动机

《An Abstract Architecture for Explainable Autonomy in Hazardous Environments》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robotic systems are being proposed for use in hazardous environments, often to reduce the risks to human workers. In the immediate future, it is likely that human workers will continue to use and direct these autonomous robots, much like other computerised tools but with more sophisticated decision-making. Therefore, one important area on which to focus engineering effort is ensuring that these users trust the system. Recent literature suggests that explainability is closely related to how trustworthy a system is. Like safety and security properties, explainability should be designed into a system, instead of being added afterwards. This paper presents an abstract architecture that supports an autonomous system explaining its behaviour (explainable autonomy), providing a design template for implementing explainable autonomous systems. We present a worked example of how our architecture could be applied in the civil nuclear industry, where both workers and regulators need to trust the system's decision-making capabilities.

</details>

---

### [[20_Research/Papers/大模型/OffQ_Taming_Structured_Outliers_in_LLM_Quantization_by_Offsetting|OffQ: Taming Structured Outliers in LLM Quantization by Offsetting]]

![[assets/2606.07116_figure.png|800]]

- **arXiv**: [2606.07116](https://arxiv.org/abs/2606.07116)
- **PDF**: https://arxiv.org/pdf/2606.07116
- **详细分析**: [[20_Research/Papers/大模型/OffQ_Taming_Structured_Outliers_in_LLM_Quantization_by_Offsetting|OffQ: Taming Structured Outliers in LLM Quantization by Offsetting]]
- **作者**: Haoqi Wang, Lorenz K. Mueller, Jiawei Zhuang, Mathieu Salzmann, Lukas Cavigelli
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《OffQ: Taming Structured Outliers in LLM Quantization by Offsetting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-bit quantization has been widely adopted to accelerate the inference of large language models (LLMs) by significantly reducing computational cost and memory usage. However, activation outliers pose a major challenge to effective quantization, often leading to notable performance degradation. In this paper, we introduce OffQ, a method designed to mitigate activation outliers in low-bit quantization through a novel offsetting mechanism. Specifically, OffQ first identifies a low-dimensional outlier subspace in the activations using a proposed top-1 PCA, and then concentrates high-magnitude activations into 1 channel via rotation. OffQ then absorbs this concentrated outlier channel by converting its magnitude into a shared offset, thereby reducing the standard deviation of the activations. This offsetting strategy enables effective W4A4KV4 quantization of LLMs using deployment-friendly uniform-grid and uniform-precision quantization. Extensive experiments across diverse LLM architectures and benchmarks demonstrate that OffQ outperforms state-of-the-art baselines, consistently improving model accuracy while preserving low-bit efficiency.

</details>

---

### [[20_Research/Papers/大模型/On_the_Geometry_of_On-Policy_Distillation|On the Geometry of On-Policy Distillation]]

![[assets/2606.07082_figure.png|800]]

- **arXiv**: [2606.07082](https://arxiv.org/abs/2606.07082)
- **PDF**: https://arxiv.org/pdf/2606.07082
- **详细分析**: [[20_Research/Papers/大模型/On_the_Geometry_of_On-Policy_Distillation|On the Geometry of On-Policy Distillation]]
- **作者**: Zhennan Shen, Yanshu Li, Qingyu Yin, Chak Tou Leong, Zhilin Wang, Yanxu Chen, Rongduo Han, Sunbowen Lee, Yi R. Fung
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《On the Geometry of On-Policy Distillation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy distillation (OPD) is increasingly used to improve large language model reasoning, but its training dynamics remain poorly understood. We characterize the trajectory of OPD updates in parameter space and compare it with supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). A suite of parameter-space diagnostics consistently places OPD in a relaxed off-principal regime: compared with SFT, its updates affect fewer weights and avoid principal directions more strongly, while compared with RLVR, they remain less tightly constrained. Beyond this static localization, OPD exhibits subspace locking: its cumulative updates rapidly enter a narrow low-dimensional channel. Constraining training to the update subspace formed early in training preserves OPD performance but substantially degrades SFT, indicating that the locked subspace is functionally sufficient for OPD. Control experiments further show that sparsifying the update tokens and shifting rollout generation off-policy preserve the rank dynamics, whereas mixing the OPD objective with RLVR changes them. Overall, these results suggest that OPD is not merely an intermediate point between SFT and RLVR, but induces its own update geometry in parameter space.

</details>

---

### [[20_Research/Papers/强化学习/SlimSearcher_Training_Efficiency-Aware_Web_Agents_via_Adaptive_Reward_Gating|SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating]]

![[assets/2606.07074_figure.png|800]]

- **arXiv**: [2606.07074](https://arxiv.org/abs/2606.07074)
- **PDF**: https://arxiv.org/pdf/2606.07074
- **详细分析**: [[20_Research/Papers/强化学习/SlimSearcher_Training_Efficiency-Aware_Web_Agents_via_Adaptive_Reward_Gating|SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating]]
- **作者**: Zequn Xie, Junjie Wang, Dan Yang, Jie Feng, Yue Shen, Jian Wang, Jinjie Gu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：XBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep research agents have demonstrated remarkable capabilities in complex information-seeking tasks, yet this power comes at a steep computational cost. Driven by accuracy-focused training paradigms, current models adopt brute-force strategies characterized by blind tool dependency and performative reasoning-generating long, redundant trajectories that are far from necessary for resolving these tasks, leading to wasteful tool calls and excessive token consumption. To overcome this efficiency trap, we propose SlimSearcher, a principled framework that pushes the Pareto frontier between accuracy and computational cost across both Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). In the SFT stage, SlimSearcher employs Pareto-efficient filtration to distill trajectories that are both successful and economical, guiding the model toward inherently efficiency-aware search behaviors. During RL, we introduce Adaptive Reward Gating, a dynamic reward-shaping mechanism that evaluates relative tool and token efficiency within a sampled cohort. By cascading these adaptive efficiency metrics with a strict correctness gate, our approach effectively avoids the brevity bias associated with absolute penalties and mitigates reward hacking. Extensive experiments on long-horizon benchmarks, including GAIA, BrowseComp, and XBenchDeepSearch, demonstrate that SlimSearcher reduces average tool-call rounds by 17%-58% while maintaining or improving accuracy.

</details>

---

### [[20_Research/Papers/大模型/TRACE_Trajectory_Reasoning_through_Adaptive_Cross-Step_Evidence_Aggregation_for_LLM_Agents|TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents]]

![[assets/2606.07054_figure.png|800]]

- **arXiv**: [2606.07054](https://arxiv.org/abs/2606.07054)
- **PDF**: https://arxiv.org/pdf/2606.07054
- **详细分析**: [[20_Research/Papers/大模型/TRACE_Trajectory_Reasoning_through_Adaptive_Cross-Step_Evidence_Aggregation_for_LLM_Agents|TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents]]
- **作者**: Vijitha Mittapalli, Shreyaa Jayant Dani, Satya Srujana Pilli, Snigdha Ansu, Mohammadreza Teymoorianfard, Franck Dernoncourt, Hongjie Chen, Yu Wang, Ryan A. Rossi, Nesreen K. Ahmed
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous LLM agents can pursue hidden malicious objectives through sequences of individually benign actions, making sabotage difficult to detect using standard trajectory-level monitoring. Existing approaches either evaluate complete trajectories in a single pass or partition them into independently scored windows, limiting their ability to connect evidence across temporally distant actions. We propose TRACE, a monitoring framework for long-horizon LLM agent trajectories. TRACE operates through a TIJ (Triage-Inspect-Judge) loop that identifies high-signal regions, performs targeted inspection while maintaining accumulated evidence across reasoning steps, and synthesizes a trajectory-level verdict. We evaluate TRACE on ten task domains from SHADE-Arena against state-of-the-art baselines. TRACE achieves an aggregate F1 of 0.713 and recall of 0.844, with the largest gains on tasks requiring long-range evidence linking.

</details>

---

### [[20_Research/Papers/强化学习/StainFlow_Entity-Stain_Tracking_and_Evidence_Linking_for_Process_Rewards_in_GUI_Agents|StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents]]

![[assets/2606.07027_first_page.png|800]]

- **arXiv**: [2606.07027](https://arxiv.org/abs/2606.07027)
- **PDF**: https://arxiv.org/pdf/2606.07027
- **详细分析**: [[20_Research/Papers/强化学习/StainFlow_Entity-Stain_Tracking_and_Evidence_Linking_for_Process_Rewards_in_GUI_Agents|StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents]]
- **作者**: Haojie Hao, Longkun Hao, Yihang Lou, Yan Bai, Zhenyang Li, Zhichao Yang, Dongshuo Huang, Hongyu Lin, Lanqing Hong, Jiakai Wang, Xianglong Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.4，强化学习 0.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, OGRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has become a promising approach for improving GUI Agents in long-horizon, stochastic digital environments, but trajectory-level success feedback is too sparse to provide reliable credit assignment for intermediate exploration steps. To mitigate this issue, recent studies introduce Process Reward Models (PRMs), which provide finer-grained training feedback through global milestone verification or local step-level evaluation. However, these methods still suffer from two level-specific limitations: global milestone decomposition is subjective and singular, making it difficult to accommodate the multiple valid execution paths in real GUI tasks, while fixed local judging windows may miss long-range key evidence or dilute the decision signal with irrelevant frames. Inspired by stain-tracing mechanisms in network flow analysis, we propose StainFlow, an entity-stain-flow process reward model for GUI Agents. To reduce the subjectivity of global partitioning, we introduce the Global Entity Stain Tracking module, which extracts visually verifiable task entities and tracks how their stain concentrations and states evolve along the trajectory, allowing task phases to be objectively separated by changes in the entity evidence flow. To improve the accuracy of local verification, we introduce the Local Stain Evidence Linking module. Centered on the triggering entities of each candidate key node, it retrieves relevant steps based on their stain concentrations and state changes, and dynamically constructs high-density evidence windows for verifying true key nodes. Extensive experiments on AndroidWorld and OGRBench show that StainFlow relatively improves online RL success by 3.2% and trajectory completion judgment accuracy by 1.8%.

</details>

---

### [[20_Research/Papers/大模型/The_Sim-to-Real_Gap_of_Foundation_Model_Agents_A_Unified_MDP_Perspective|The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective]]

![[assets/2606.07017_figure.png|800]]

- **arXiv**: [2606.07017](https://arxiv.org/abs/2606.07017)
- **PDF**: https://arxiv.org/pdf/2606.07017
- **详细分析**: [[20_Research/Papers/大模型/The_Sim-to-Real_Gap_of_Foundation_Model_Agents_A_Unified_MDP_Perspective|The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective]]
- **作者**: Xiaoou Liu, Tiejin Chen, Weibo Li, Xiyang Hu, Hua Wei
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 机器人
- **相关性评分**: 3.05（加权：具身智能 1.2，大模型 1.05，强化学习 0.6，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation model agents are increasingly deployed for real-world decision-making, but suffer from the sim-to-real gap. While robotics and classical control have mature frameworks to address this gap, the foundation model community is treating agent robustness as an entirely novel phenomenon. Our paper proposes formalizing the foundation model agent evaluation and training gap as a classical sim-to-real problem structured entirely around the four elements of a Markov Decision Process, including Observation, Action, Transition, and Reward. In this paper, we set a comprehensive research agenda that translates classical discrepancies into the foundation model domain and advocates for adopting established solutions like domain randomization. We provide concrete examples, such as a multilingual tool calling to demonstrate how severe observation space gaps lead to operationally invalid actions despite correct semantic intent. Ultimately, this agenda aims to drive a paradigm shift, yielding a unified vocabulary and standardized stress test benchmarks to foster a new generation of highly trustworthy agents for reliable real-world applications.

</details>

---

### [[20_Research/Papers/大模型/Teaching_the_Way,_Not_the_Answer_Privileged_Tutoring_Distillation_for_Multimodal_Policy_Optimization|Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization]]

![[assets/2606.07000_figure.png|800]]

- **arXiv**: [2606.07000](https://arxiv.org/abs/2606.07000)
- **PDF**: https://arxiv.org/pdf/2606.07000
- **详细分析**: [[20_Research/Papers/大模型/Teaching_the_Way,_Not_the_Answer_Privileged_Tutoring_Distillation_for_Multimodal_Policy_Optimization|Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization]]
- **作者**: Shizhe Xiang, Ke An, Wenlong Yu, Yue Liu, Jian Luan, Pei Fu, Qilong Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent post-training methods, particularly Reinforcement Learning with Verifiable Rewards (RLVR), have significantly enhanced the reasoning ability of Large Vision-Language Models (LVLMs). However, the sparse nature of verifiable rewards provides little token-level supervision for failed rollouts, often leading to inefficient exploration in complex multimodal reasoning tasks. Although policy distillation can offer dense guidance, external teacher based methods introduce substantial computational overhead, while answer conditioned tuning methods may expose answer-level information and induce shortcut-like generation behavior. To address these limitations, we propose PTD-PO, a Privileged Tutoring Distillation Policy Optimization framework for RLVR that provides dense guidance without exposing the answer to the student policy. Specifically, PTD-PO constructs structured privileged hints from spatial attention guidance and intermediate textual reasoning steps, and uses them through in-context learning to produce step-wise token-distribution supervision. The student is still optimized under the original answer-free context, and its failed rollouts are aligned with the hint-augmented reference model at the token-distribution level. To further stabilize distillation under the distribution shift between guided and unguided contexts, we introduce a Top-K Jensen-Shannon divergence objective that focuses alignment on informative token probabilities while reducing memory overhead. Experiments on LVLMs ranging from 2B to 8B parameters show that PTD-PO consistently outperforms RLVR and distillation baselines, mitigates entropy collapse, and improves complex multimodal reasoning performance.

</details>

---

### [[20_Research/Papers/大模型/Exploring_Agentic_Tool-Calling_Decisions_via_Uncertainty-Aligned_Reinforcement_Learning|Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning]]

![[assets/2606.06976_figure.png|800]]

- **arXiv**: [2606.06976](https://arxiv.org/abs/2606.06976)
- **PDF**: https://arxiv.org/pdf/2606.06976
- **详细分析**: [[20_Research/Papers/大模型/Exploring_Agentic_Tool-Calling_Decisions_via_Uncertainty-Aligned_Reinforcement_Learning|Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning]]
- **作者**: Yijin Zhou, Linqian Zeng, Xiaoya Lu, Wenyuan Xie, Dongrui Liu, Junchi Yan, Jing Shao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agents often make suboptimal tool-use decisions, including unsupported tool invocation and hallucinated direct responses, which may accumulate errors throughout multi-step interactions. Existing approaches mainly improve these behaviors through inference-time correction or coarse-grained reward signals based on decision outcomes and structured checklists, leaving the uncertainty characteristics of agent decisions underexplored. We observe that decision-oriented reinforcement learning tends to weaken the uncertainty separation between correct and incorrect actions, resulting in overconfident mistakes and weaker exploration signals. Therefore, we propose TRUST, which incorporates uncertainty quantification into reward design as a repulsive force for maintaining uncertainty separation, and labels lightweight key-turn annotations for unified post-training of multi-turn trajectories. Experimental results across diverse tool-use benchmarks show that TRUST consistently enhances both decision quality and agent performance while maintaining more reliable uncertainty estimates during optimization.

</details>

---

### [[20_Research/Papers/大模型/ThinkBooster_A_Unified_Framework_for_Seamless_Test-Time_Scaling_of_LLM_Reasoning|ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning]]

![[assets/2606.06915_figure.png|800]]

- **arXiv**: [2606.06915](https://arxiv.org/abs/2606.06915)
- **PDF**: https://arxiv.org/pdf/2606.06915
- **详细分析**: [[20_Research/Papers/大模型/ThinkBooster_A_Unified_Framework_for_Seamless_Test-Time_Scaling_of_LLM_Reasoning|ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning]]
- **作者**: Vladislav Smirnov, Chieu Nguyen, Sergey Senichev, Minh Ngoc Ta, Ekaterina Fadeeva, Artem Vazhentsev, Daria Galimzianova, Nikolai Rozanov, Viktor Mazanov, Jingwei Ni, Tianyi Wu, Igor Kiselev...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time compute (TTC) scaling has emerged as a powerful paradigm for improving large language model (LLM) reasoning by allocating additional compute during inference, e.g., via multi-sample generation and verifier-based reranking. Existing TTC scaling strategies and reasoning scorers remain fragmented, evaluated under inconsistent protocols, and are rarely analyzed through the lens of quality-cost trade-offs. We introduce ThinkBooster, a unified framework for seamless test-time compute scaling of LLM reasoning, which consists of (i) a modular Python library implementing state-of-the-art TTC scaling strategy and scorer families, (ii) a benchmark that jointly evaluates performance and computational efficiency, and (iii) a deployable OpenAI-compatible proxy service that enables drop-in integration of adaptive reasoning into real-world applications. We further provide a demo visual debugger for inspecting the reasoning trajectories, intermediate selection decisions, and alternative reasoning paths. Empirical results on mathematical and coding tasks reveal the performance-compute trade-offs of TTC scaling strategies and scoring methods and demonstrate that ThinkBooster provides practical gains in real-world tasks. The code is available online under an MIT license.

</details>

---

### [[20_Research/Papers/机器人/Neuro-Symbolic_Learning_for_Long-Horizon_Task_Planning_Under_Complex_Logical_Constraints|Neuro-Symbolic Learning for Long-Horizon Task Planning Under Complex Logical Constraints]]

![[assets/2606.06877_figure.png|800]]

- **arXiv**: [2606.06877](https://arxiv.org/abs/2606.06877)
- **PDF**: https://arxiv.org/pdf/2606.06877
- **详细分析**: [[20_Research/Papers/机器人/Neuro-Symbolic_Learning_for_Long-Horizon_Task_Planning_Under_Complex_Logical_Constraints|Neuro-Symbolic Learning for Long-Horizon Task Planning Under Complex Logical Constraints]]
- **作者**: Qiwei Du, Zitong Zhan, Shaoshu Su, Bowen Li, Yi Du, Zhipeng Zhao, Taimeng Fu, Sebastian Scherer, Jiaoyang Li, Chen Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Neuro-Symbolic Learning for Long-Horizon Task Planning Under Complex Logical Constraints》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task planning often suffers from severe efficiency bottlenecks when robots must reason over long-horizon action sequences under complex logical constraints, including object affordances, spatial relationships, and sequential action dependencies. Recent neuro-symbolic methods improve planning efficiency by learning object-importance scores to prune task-irrelevant objects, but they typically rely on fixed offline supervision generated from full search spaces. This creates a train-test mismatch: at deployment, the planner operates in pruned search spaces induced by the model's own imperfect predictions, leading to exposure bias and degraded planning performance. To address this challenge, we formulate object-importance learning for task planning as an imperative learning-based bilevel optimization problem. The upper level optimizes a neural scorer, while the lower level solves a symbolic planning problem in the score-pruned search space. To stabilize this learning process, we introduce a 3R strategy into the lower-level planning, using parallel Repair, Restart, and Rollback recovery to provide reliable and adaptive feedback for upper-level learning. Experiments on three challenging benchmarks demonstrate state-of-the-art performance, including an 80.04% reduction in failure rate and a 57.14% reduction in planning time. We further validate the framework on a quadruped-based mobile manipulator in simulation and the real world, demonstrating its potential for efficient and deployable neuro-symbolic task planning.

</details>

---

### [[20_Research/Papers/大模型/Evidence-Based_Intelligent_Diagnostic_and_Therapeutic_Visualization_System_with_Large_Language_Models_Multi-Turn_Interaction_and_Multimodal_|Evidence-Based Intelligent Diagnostic and Therapeutic Visualization System with Large Language Models: Multi-Turn Interaction and Multimodal Treatment Plan Generation]]

![[assets/2606.06869_figure.png|800]]

- **arXiv**: [2606.06869](https://arxiv.org/abs/2606.06869)
- **PDF**: https://arxiv.org/pdf/2606.06869
- **详细分析**: [[20_Research/Papers/大模型/Evidence-Based_Intelligent_Diagnostic_and_Therapeutic_Visualization_System_with_Large_Language_Models_Multi-Turn_Interaction_and_Multimodal_|Evidence-Based Intelligent Diagnostic and Therapeutic Visualization System with Large Language Models: Multi-Turn Interaction and Multimodal Treatment Plan Generation]]
- **作者**: Yunhan Wang, Yuda Wang, Zhiying Tu, Mingqiang Song, Li Song, Kun Li, Dianhui Chu, Bolin Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Evidence-Based Intelligent Diagnostic and Therapeutic Visualization System with Large Language Models: Multi-Turn Interaction and Multimodal Treatment Plan Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aim: Existing AI-assisted traditional Chinese medicine diagnostic tools suffer from opaque reasoning processes, passive interaction, and limited treatment plan presentation. This study proposes a knowledge-enhanced visual diagnostic system to improve the transparency and interpretability of syndrome differentiation and treatment. Methods: The system is built upon a Neo4j knowledge graph comprising 241 syndromes, 1,263 symptoms, and 2,485 relations. It incorporates a four-stage symptom matching pipeline (exact, semantic, fuzzy, and large language model verification), an information gain-driven proactive questioning strategy optimized with genetic algorithms, and a multimodal treatment presentation integrating artificial intelligence-generated illustrations, three-dimensional meridian-acupoint models, and evidence-based literature. Results: Knowledge graph constraints reduced non-standard outputs by 32%. Case studies validated the effectiveness of the interactive workflow across patient self-assessment, clinician-assisted diagnosis, and traditional Chinese medicine education. Automated paired-comparison evaluation across 30 cases further demonstrated significant improvements in diagnostic trust (Cohen's d = 1.82, p &lt; 0.001), reduced cognitive load (improvements in four of five dimensions), and higher credibility of evidence-based references (4.21 vs. 2.95). Conclusions: The proposed system enhances the transparency of traditional Chinese medicine diagnostic reasoning and the interpretability of treatment plans through knowledge graph-driven visualization and multimodal interaction, offering a practical solution for trustworthy artificial intelligence-assisted traditional Chinese medicine applications.

</details>

---

### [[20_Research/Papers/大模型/LLM_Agent-Assisted_Reverse_Engineering_with_Quantitative_Readability_Metrics|LLM Agent-Assisted Reverse Engineering with Quantitative Readability Metrics]]

![[assets/2606.06838_figure.png|800]]

- **arXiv**: [2606.06838](https://arxiv.org/abs/2606.06838)
- **PDF**: https://arxiv.org/pdf/2606.06838
- **详细分析**: [[20_Research/Papers/大模型/LLM_Agent-Assisted_Reverse_Engineering_with_Quantitative_Readability_Metrics|LLM Agent-Assisted Reverse Engineering with Quantitative Readability Metrics]]
- **作者**: Neil Archibald, Ruben Thijssen
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Agent-Assisted Reverse Engineering with Quantitative Readability Metrics》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic decompilers produce functionally correct but often unreadable C code. This paper addresses one stage of the reverse engineering workflow: improving the readability of decompiled code using LLM agents guided by quantitative metrics. We present a three-phase research evolution. Phase 1 (tool-driven steering via Ghidra MCP) suffered from incomplete coverage and inconsistent improvements due to lack of quantitative guidance. Phase 2 (structural similarity validation alone) revealed that agents optimize for metrics in unintended ways, producing structurally equivalent but less readable code. Our contribution is the Quantitative Readability Score (QRS) framework, a composite metric combining a structural similarity gate with three independent readability sub-metrics (Lexical Surprisal, Structural Simplicity, and Idiomatic Quality). We demonstrate that QRS-guided refinement enables LLM agents to make targeted readability improvements without sacrificing correctness. We provide a discussion of the broader reverse engineering workflow (binary lifting, decompilation cleanup, and achieving functional equivalence) as context, however, it remains out of scope.

</details>

---

### [[20_Research/Papers/具身智能/Think_Like_a_Pilot_Fine-Grained_Long-Horizon_UAV_Navigation|Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation]]

![[assets/2606.06836_first_page.png|800]]

- **arXiv**: [2606.06836](https://arxiv.org/abs/2606.06836)
- **PDF**: https://arxiv.org/pdf/2606.06836
- **详细分析**: [[20_Research/Papers/具身智能/Think_Like_a_Pilot_Fine-Grained_Long-Horizon_UAV_Navigation|Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation]]
- **作者**: Xiangyi Zheng, Xiangyu Wang, Qinan Liao, Zimu Tang, Yue Liao, Dongyue Lyu, Guodong Wang, Junjie Liu, Si Liu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.9，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Think Like a Pilot: Fine-Grained Long-Horizon UAV Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-guided UAV agents must execute long-horizon semantic instructions while producing smooth, physically feasible continuous flight commands, yet existing Vision-Language Navigation (VLN) benchmarks typically use discrete or coarse actions and existing UAV Vision-Language-Action (VLA) tasks focus on short, atomic maneuvers. To address this gap in UAV task settings, we introduce \textbf{FLIGHT}, a \textbf{F}ine-grained \textbf{L}ong-horizon \textbf{I}nstruction-\textbf{G}uided benchmark for \textbf{H}ybrid UAV navigation and reasoning \textbf{T}asks, which combines multi-stage instructions with dense 6-DoF trajectory annotations across two dataset splits: Fine-grained VLN and Long-horizon Flow. To endow the UAV agent with the capability of real-time in-flight reasoning over task execution status and mission planning, while simultaneously accommodating high-frequency, real-time precise control, we further propose \textbf{FLIGHT VLA}, an asynchronous architecture that decouples a low-frequency Streaming Pilot Vision-Language Model (VLM) for task-state reasoning from a high-frequency diffusion action model for continuous control, supervised by explicit \textbf{Pilot Reasoning} texts that summarize the current flight state and anticipate the next subgoal. In closed-loop evaluation, FLIGHT VLA consistently surpasses representative VLN and VLA baselines on our FLIGHT benchmarks, achieving stronger multi-stage completion, subgoal adherence, and terminal control. Its trained Streaming Pilot Reasoning VLM further improves UAV video reasoning, validating the effectiveness of our design.

</details>

---

### [[20_Research/Papers/大模型/Hearing_the_Unspoken_Language_Model_Priors_for_Acoustic_Adversarial_Attacks|Hearing the Unspoken: Language Model Priors for Acoustic Adversarial Attacks]]

![[assets/2606.06833_figure.png|800]]

- **arXiv**: [2606.06833](https://arxiv.org/abs/2606.06833)
- **PDF**: https://arxiv.org/pdf/2606.06833
- **详细分析**: [[20_Research/Papers/大模型/Hearing_the_Unspoken_Language_Model_Priors_for_Acoustic_Adversarial_Attacks|Hearing the Unspoken: Language Model Priors for Acoustic Adversarial Attacks]]
- **作者**: Jiani Xie, Andrew C. Cullen, Paul Montague, Benjamin I. P. Rubinstein
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《Hearing the Unspoken: Language Model Priors for Acoustic Adversarial Attacks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic Speech Recognition (ASR) systems operating in real-time settings must process acoustic input under strict temporal constraints, where transcription decisions are inherently made on incomplete information. This causal constraint serves as an information bottleneck on attackers, significantly limiting attack performance. Our new Semantic Gambit attack breaks this causal limitation by augmenting the adversary with predictive context derived from a Large Language Model in real-time. Our experiments show that this form of augmentation can elevate the corpus-level Word Error Rate to 35.6% -- a three-fold increase over the current state-of-the-art. Ultimately, this work reveals how common, low-latency LLM tooling can be exploited to systematically subvert real-time ASR pipelines.

</details>

---

### [[20_Research/Papers/强化学习/Progress-SQL_Improving_Reinforcement_Learning_for_Text-to-SQL_via_Progressive_Rewards|Progress-SQL: Improving Reinforcement Learning for Text-to-SQL via Progressive Rewards]]

![[assets/2606.06825_figure.png|800]]

- **arXiv**: [2606.06825](https://arxiv.org/abs/2606.06825)
- **PDF**: https://arxiv.org/pdf/2606.06825
- **详细分析**: [[20_Research/Papers/强化学习/Progress-SQL_Improving_Reinforcement_Learning_for_Text-to-SQL_via_Progressive_Rewards|Progress-SQL: Improving Reinforcement Learning for Text-to-SQL via Progressive Rewards]]
- **作者**: Shihao Zhang, Xiaoman Wang, Yuan Liu, Yunshi Lan, Weining Qian
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Progress-SQL: Improving Reinforcement Learning for Text-to-SQL via Progressive Rewards》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkyRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has recently shown promise in improving large language models for Text-to-SQL generation, yet existing methods typically optimize one-shot rewards defined over a single SQL state. Such rewards provide limited guidance for iterative SQL correction and are insufficient to capture the improvement of multi-turn SQL refinement. In this paper, we propose Progress-SQL, a multi-turn reinforcement learning framework with progressive rewards for Text-to-SQL. Our approach introduces an Oracle-guided Diagnostic Tree (ODT), which abstracts SQL queries into clause-level structural profiles and produces diagnostic feedback for next-turn refinement. To provide dense and robust reward signals, we combine ODT-based structural alignment with lexical alignment and define a progressive reward that measures the improvement from the initial SQL to the final SQL. We further incorporate a progression latency reward that favors earlier correctness and an execution status reward that encourages recovery from the invalid SQL. Experiments on BIRD, Spider, and Spider robustness variants demonstrate that our method consistently improves Text-to-SQL performance across both primary and robustness evaluations.

</details>

---

### [[20_Research/Papers/大模型/SCALE_Scalable_Cross-Attention_Learning_with_Extrapolation_for_Agentic_Workflow_Scheduling|SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling]]

![[assets/2606.06820_figure.png|800]]

- **arXiv**: [2606.06820](https://arxiv.org/abs/2606.06820)
- **PDF**: https://arxiv.org/pdf/2606.06820
- **详细分析**: [[20_Research/Papers/大模型/SCALE_Scalable_Cross-Attention_Learning_with_Extrapolation_for_Agentic_Workflow_Scheduling|SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling]]
- **作者**: Zhifei Xu, Jierui Lan, Zixuan Liang, Aiji Liang, Jinxi He
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.3，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic Large Language Model (LLM) systems decompose complex tasks into workflow Directed Acyclic Graphs (DAGs) whose primitives must be scheduled on heterogeneous clusters. Existing deep reinforcement learning (DRL) schedulers are tied to a fixed cluster size and require retraining whenever the number of servers changes. We propose SCALE (Scalable Cross-Attention Learning with Extrapolation), a DRL scheduler that generalizes to unseen cluster scales without fine-tuning. SCALE employs a cross-attention pointer network where task features query against server features, so the architecture accepts any number of servers by construction. We observe, however, that permutation-invariant architecture alone does not guarantee good performance at new scales - the attention feature undergoes distribution shift as the server count grows. To counter this, we introduce Structured Representation Regularization (SRR): a decorrelation loss combined with a KL penalty toward the standard normal, which keeps feature statistics stable regardless of input size. Trained on 16 nodes and tested directly on 32 and 48 nodes, SCALE reduces average response time by 8.9% at N=48 relative to the same architecture without SRR, confirming that explicit regularization is necessary to close the scale-generalization gap.

</details>

---

### [[20_Research/Papers/强化学习/Exploring_Reinforcement_Learning_for_Fluid_Transitions_Between_Clinical_Mental_Healthcare_and_Everyday_Wellness_Support|Exploring Reinforcement Learning for Fluid Transitions Between Clinical Mental Healthcare and Everyday Wellness Support]]

![[assets/2606.06800_figure.png|800]]

- **arXiv**: [2606.06800](https://arxiv.org/abs/2606.06800)
- **PDF**: https://arxiv.org/pdf/2606.06800
- **详细分析**: [[20_Research/Papers/强化学习/Exploring_Reinforcement_Learning_for_Fluid_Transitions_Between_Clinical_Mental_Healthcare_and_Everyday_Wellness_Support|Exploring Reinforcement Learning for Fluid Transitions Between Clinical Mental Healthcare and Everyday Wellness Support]]
- **作者**: Tony Wang, Qian Yang
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Exploring Reinforcement Learning for Fluid Transitions Between Clinical Mental Healthcare and Everyday Wellness Support》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mental health struggles wax and wane, yet clinical and wellness interventions typically operate separately, causing frequent breakdowns at care transitions. We explore reinforcement learning (RL) as a means to build digital health systems that deliver clinical and wellness interventions proactively, as part of a coherent care journey. We ask: what complexities does designing such a system involve? We built a contextual bandit that dynamically selects journaling prompts from clinical and wellness repertoires to optimize for an overarching health goal (sustained journaling) and deployed it in a four-week exploratory study (N=38). We found that, first, many benefits of RL-optimized intervention sequences appeared only after interventions ended, raising the question: Should systems that offer coherent clinical-wellness care journeys include stepping-back periods? If so, when and how? Second, participants most engaged with RL-generated interventions deepened their engagement over time, while those most engaged with a constant intervention tended to burn out and drop out later. It raises the question: When should a system blending clinical and wellness interventions reduce intensity to prevent burnout in versus sustain it to maximize treatment gains?

</details>

---

### [[20_Research/Papers/大模型/AdMem_Advanced_Memory_for_Task-solving_Agents|AdMem: Advanced Memory for Task-solving Agents]]

![[assets/2606.06787_first_page.png|800]]

- **arXiv**: [2606.06787](https://arxiv.org/abs/2606.06787)
- **PDF**: https://arxiv.org/pdf/2606.06787
- **详细分析**: [[20_Research/Papers/大模型/AdMem_Advanced_Memory_for_Task-solving_Agents|AdMem: Advanced Memory for Task-solving Agents]]
- **作者**: Runzhe Wang, Huilin Lu, Shengjie Liu, Li Dong, Jason Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AdMem: Advanced Memory for Task-solving Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) show promise as tool-using agents but remain limited in long-horizon tasks that require remembering, organizing, and reusing knowledge. Prior memory approaches aim to resolve the situation, but mainly focus on storing factual information. Recent work on procedural memory improves task reuse, yet often reduces to replaying past successes without addressing failure cases or online scalability. We introduce a unified and automatic memory framework that integrates semantic, episodic, and procedural memory in a bi-level design combining short-term and long-term stores. A multi-agent architecture with actor, memory, and critic agents enables automatic memory generation, reward annotation, and adaptive retrieval. Long-term memory is managed through reward-based evaluation, merging, and pruning, ensuring scalability and continual improvement. Experiments across various environments show that our approach improves robustness and success on long multi-turn tasks compared to existing baselines. This work highlights the importance of comprehensive, adaptive memory for advancing LLM-based agents.

</details>

---

### [[20_Research/Papers/机器人/AxisGuide_Grounding_Robot_Action_Coordinate_System_in_RGB_Observations_for_Robust_Visuomotor_Manipulation|AxisGuide: Grounding Robot Action Coordinate System in RGB Observations for Robust Visuomotor Manipulation]]

![[assets/2606.06761_figure.png|800]]

- **arXiv**: [2606.06761](https://arxiv.org/abs/2606.06761)
- **PDF**: https://arxiv.org/pdf/2606.06761
- **详细分析**: [[20_Research/Papers/机器人/AxisGuide_Grounding_Robot_Action_Coordinate_System_in_RGB_Observations_for_Robust_Visuomotor_Manipulation|AxisGuide: Grounding Robot Action Coordinate System in RGB Observations for Robust Visuomotor Manipulation]]
- **作者**: Jiyun Jang, Yujin Sung, Woosung Joung, Daewon Chae, Sangwon Lee, Sohwi Kim, Jinkyu Kim, Jungbeom Lee
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《AxisGuide: Grounding Robot Action Coordinate System in RGB Observations for Robust Visuomotor Manipulation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, SmolVLA, TraceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor manipulation policies trained via large-scale behavior cloning have achieved strong semantic scene understanding, yet often fail to reliably execute correct low-level actions under distribution shifts. For example, even in a simple pickup task with identical scene layouts, camera viewpoints, and illumination, performance can degrade substantially when the object is placed at unseen locations. We argue that this gap arises from insufficient action understanding, namely the inability to interpret the robot's base-frame action coordinate system in image space. To address this issue, we introduce AxisGuide, a lightweight guidance method that bridges semantic scene understanding and action-coordinate interpretation. Using camera parameters and end-effector poses, AxisGuide renders the robot base-frame axes in each camera view and augments RGB observations with a small set of cue channels that explicitly visualize the meaning of the +x, +y, and +z motions in image space. Extensive evaluations in both the LIBERO simulation and real-world environments demonstrate that AxisGuide yields substantial performance gains and improved generalization, highlighting the effectiveness of explicit action-coordinate cues for learning reliable and transferable generalist visuomotor policies.

</details>

---

### [[20_Research/Papers/大模型/Evidence_Graph_Consistency_in_Retrieval-Augmented_Generation_A_Model-Dependent_Analysis_of_Hallucination_Detection|Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection]]

![[assets/2606.06748_figure.png|800]]

- **arXiv**: [2606.06748](https://arxiv.org/abs/2606.06748)
- **PDF**: https://arxiv.org/pdf/2606.06748
- **详细分析**: [[20_Research/Papers/大模型/Evidence_Graph_Consistency_in_Retrieval-Augmented_Generation_A_Model-Dependent_Analysis_of_Hallucination_Detection|Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection]]
- **作者**: Jianru Shen
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) reduces but does not eliminate hallucination in large language models. Existing detection methods rely on flat similarity between generated answers and retrieved passages, ignoring structural relationships among evidence pieces and answer claims. We propose Evidence Graph Consistency (EGC), a framework that constructs a local evidence graph per response and computes five structural consistency measures as hallucination indicators. Evaluated on the full question answering split of RAGTruth across six LLMs (5,767 responses), EGC reveals a consistent model-family split: graph consistency features show the expected diagnostic direction for hallucinations in Llama-2 models but exhibit systematic reversal in GPT-4, GPT-3.5, and Mistral-7B. This reversal suggests qualitatively different hallucination patterns across model families and indicates that embedding-based graph consistency cannot serve as a model-independent hallucination detection signal.

</details>

---

### [[20_Research/Papers/大模型/OpenSkill_Open-World_Self-Evolution_for_LLM_Agents|OpenSkill: Open-World Self-Evolution for LLM Agents]]

![[assets/2606.06741_figure.png|800]]

- **arXiv**: [2606.06741](https://arxiv.org/abs/2606.06741)
- **PDF**: https://arxiv.org/pdf/2606.06741
- **详细分析**: [[20_Research/Papers/大模型/OpenSkill_Open-World_Self-Evolution_for_LLM_Agents|OpenSkill: Open-World Self-Evolution for LLM Agents]]
- **作者**: Zhiling Yan, Dingjie Song, Hanrong Zhang, Wei Liang, Yuxuan Zhang, Yutong Dai, Lifang He, Philip S. Yu, Ran Xu, Xiang Li, Lichao Sun
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《OpenSkill: Open-World Self-Evolution for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving agents requires adaptation after deployment, but existing approaches assume a usable learning loop, such as curated skills, successful trajectories, or verifier signals. Real open-world deployments may provide none of these, offering only a task prompt. In this work, we study open-world self-evolution, where an agent must build both its skills and its own verification signals from scratch, using open-world resources but no target-task supervision. We propose OpenSkill, a framework that bootstraps this loop: it acquires grounded knowledge and verification anchors from documentation, repositories, and the web, synthesizes them into transferable skills, and refines those skills against self-built virtual tasks grounded in the anchors rather than in target answers. The open world thus supplies both the knowledge to be learned and a supervision-independent practice environment, with target-task supervision reserved for final evaluation. Across three benchmarks and two target agents, OpenSkill attains the best automated pass rate while satisfying the no-supervision constraint. Analysis shows its skills transfer across models without model-specific adaptation, and its self-built verifier aligns with ground-truth outcomes despite never accessing them.

</details>

---

### [[20_Research/Papers/机器人/SCOUT_Semantic_scene_COverage_via_Uncertainty-guided_Traversal|SCOUT: Semantic scene COverage via Uncertainty-guided Traversal]]

![[assets/2606.06721_figure.png|800]]

- **arXiv**: [2606.06721](https://arxiv.org/abs/2606.06721)
- **PDF**: https://arxiv.org/pdf/2606.06721
- **详细分析**: [[20_Research/Papers/机器人/SCOUT_Semantic_scene_COverage_via_Uncertainty-guided_Traversal|SCOUT: Semantic scene COverage via Uncertainty-guided Traversal]]
- **作者**: Junyu Mao, Sara Ayoubi, Vishnu D. Sharma, Ilija Hadžić, Matthew Andrews
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《SCOUT: Semantic scene COverage via Uncertainty-guided Traversal》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots that operate over extended periods should not merely visit space; they should progressively understand it. Yet most 3D scene graph pipelines treat perception as a post-processing stage over a fixed dataset, decoupling scene representation from the decisions that determine what is observed in the first place. We present SCOUT, an online semantic exploration framework that closes this loop by coupling active traversal with probabilistic scene graph construction. Given a prior 2D occupancy map and posed RGB-D observations, SCOUT incrementally builds an uncertainty-aware 3D scene graph whose nodes maintain fused geometry and posterior beliefs over open-vocabulary object labels, while edges encode structural relations such as on, inside, belong, and next to. These beliefs are fed back to an uncertainty-guided traversal planner, which selects viewpoints by balancing expected semantic certainty gain, geometric coverage gain, and travel cost. In this way, the robot revisits ambiguous objects when additional evidence matters and expands into unseen free space when the scene remains incomplete. The resulting system treats semantic scene completeness as an operational objective rather than a passive by-product of semantic mapping, moving toward autonomous agents that can patrol, update, and reason about evolving indoor environments with minimal human intervention.

</details>

---

### [[20_Research/Papers/具身智能/AEGIS_A_Backup_Reflex_for_Physical_AI|AEGIS: A Backup Reflex for Physical AI]]

![[assets/2606.06660_figure.png|800]]

- **arXiv**: [2606.06660](https://arxiv.org/abs/2606.06660)
- **PDF**: https://arxiv.org/pdf/2606.06660
- **详细分析**: [[20_Research/Papers/具身智能/AEGIS_A_Backup_Reflex_for_Physical_AI|AEGIS: A Backup Reflex for Physical AI]]
- **作者**: Josef Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《AEGIS: A Backup Reflex for Physical AI》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FARL, FPC-VLA, LiLo-VLA, OpenVLA, Pre-VLA, ReconVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot manipulation tends to fail gradually: one bad step degrades the state, and the policy spirals into a basin from which it cannot recover. The failure is often visible before it happens. We introduce AEGIS (Activation-probe Early-warning, Gated Inference Switching), a selective escalation method that uses a lightweight probe on a weak policy's frozen activations to detect high-risk steps while there is still time to act. When the probe flags a step, control switches to a stronger separate policy, but only for the steps that need it. On LIBERO-Spatial, AEGIS recovers 10.1% of the trajectories the weak policy alone loses, versus 4.6% for budget-matched blind escalation and 5.1% for a random-trigger placebo. These gains are significant under one-sided exact paired McNemar tests with Holm-Bonferroni adjustment over three pre-registered contrasts: +5.4pp over blind escalation, p=8.5e-6; +5.0pp over random triggering, p=1.0e-4; paired-trajectory bootstrap CIs exclude zero. AEGIS activates the stronger policy on only 38% of steps, so the lever is timing rather than compute. The probe clears its precondition with an early-window AUROC of 0.764, 95% CI [0.70, 0.84], read from the weak-policy path over the first 30% of trajectory steps before any handoff. We pre-register the full analysis plan, including a conditional recovered-task-rate estimand and explicit kill criteria, and confirm the result on 700 common-random-number episodes per arm, with nA-fail=646.

</details>

---

### [[20_Research/Papers/具身智能/What_Matters_When_Cotraining_Robot_Manipulation_Policies_on_Everyday_Human_Videos|What Matters When Cotraining Robot Manipulation Policies on Everyday Human Videos?]]

![[assets/2606.06627_figure.jpg|800]]

- **arXiv**: [2606.06627](https://arxiv.org/abs/2606.06627)
- **PDF**: https://arxiv.org/pdf/2606.06627
- **详细分析**: [[20_Research/Papers/具身智能/What_Matters_When_Cotraining_Robot_Manipulation_Policies_on_Everyday_Human_Videos|What Matters When Cotraining Robot Manipulation Policies on Everyday Human Videos?]]
- **作者**: Richard Li, Aditya Prakash, Andrew Wen, Saurabh Gupta, Yilun Du, Pulkit Agrawal
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《What Matters When Cotraining Robot Manipulation Policies on Everyday Human Videos?》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human video datasets used for cotraining robot manipulation policies largely consist of curated demonstrations where motions are orchestrated to resemble robot behavior and 3D hand poses are captured with specialized hardware. A more plentiful source of data is everyday Internet video, but it is an open question what factors enable transfer from such videos to robots. We investigate this using a new dataset of 532 human videos with 28 hours of high-quality triangulated hand labels and natural motions. We find that hand pose quality affects transfer, but even with accurate hands, the inherent motion gap hinders transfer unless the vision and policy networks specialize to each embodiment. Our cotraining recipe yields consistent improvements, with an absolute success rate gain of $29.7\%$ in the low-robot-data regime across six manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/MacArena_Benchmarking_Computer_Use_Agents_on_an_Online_macOS_Environment|MacArena: Benchmarking Computer Use Agents on an Online macOS Environment]]

![[assets/2606.06560_figure.png|800]]

- **arXiv**: [2606.06560](https://arxiv.org/abs/2606.06560)
- **PDF**: https://arxiv.org/pdf/2606.06560
- **详细分析**: [[20_Research/Papers/强化学习/MacArena_Benchmarking_Computer_Use_Agents_on_an_Online_macOS_Environment|MacArena: Benchmarking Computer Use Agents on an Online macOS Environment]]
- **作者**: Victor Muryn, Maksym Shamrai, Sofiia Mazepa, Yehor Khodysko
- **cs 子类**: cs.AI, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MacArena: Benchmarking Computer Use Agents on an Online macOS Environment》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AndroidWorld, ComputerRL, DigiRL, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents (CUAs) operate graphical user interfaces (GUIs) through vision and control primitives, and their capabilities have advanced rapidly, driven in part by standardized online evaluation benchmarks such as OSWorld, which serve both as evaluation tools and as training environments for reinforcement learning. However, macOS remains underserved in this landscape: the only existing benchmark, macOSWorld, covers a narrow slice of first-party applications with simpler tasks, and runs on x86 virtual machines incompatible with Apple Silicon. We introduce MacArena, a benchmark of 421 manually verified tasks spanning 50 applications that combines a curated port of OSWorld tasks, content sourced from macOSWorld, and 49 new macOS-native tasks, all running on Apple's native Virtualization framework on Apple Silicon. We argue that macOS presents distinct GUI challenges beyond what Linux-based benchmarks capture, and our evaluation supports this claim: strong model performance on existing benchmarks can reflect familiarity with task distributions rather than genuine cross-platform GUI competence. Notably, model rankings invert between ported and macOS-native tasks, with a leading model trailing by over 26% on the MacArena subset, suggesting that macOS poses a genuinely harder environment for current GUI agents.

</details>

---

### [[20_Research/Papers/大模型/Queen-Bee_Agents_A_BeeSpec-Centered_Architecture_for_Governed_Enterprise_MCP_Orchestration|Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration]]

![[assets/2606.06545_first_page.png|800]]

- **arXiv**: [2606.06545](https://arxiv.org/abs/2606.06545)
- **PDF**: https://arxiv.org/pdf/2606.06545
- **详细分析**: [[20_Research/Papers/大模型/Queen-Bee_Agents_A_BeeSpec-Centered_Architecture_for_Governed_Enterprise_MCP_Orchestration|Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration]]
- **作者**: Dutao Zhang, Liaotian
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise agent systems increasingly need to connect large language models to private tools, internal knowledge, and Model Context Protocol (MCP) interfaces. In this setting, raw task capability is insufficient: organizations also require policy enforcement, tenant-scoped isolation, and execution that remains within explicit operational boundaries. We present Queen-Bee, a governed multi-agent architecture in which a Queen control plane retrieves capabilities, plans task-scoped execution, and compiles a structured BeeSpec that is executed by specialized Bee agents under constrained tool access. We implement a working prototype with tenant-scoped MCP connectors, audit-backed execution-time governance, retrieval-driven weak incubation, and multiple provisioning backends. We evaluate the system on 59 enterprise-style tasks spanning governance-sensitive requests, retrieval-driven provisioning, scoped local execution, and chemistry workflow integration. The retrieval-driven Queen-Bee variant achieves a task success rate of 0.964, zero governance failures, and substantially better scoped execution quality than both a static Queen-Bee baseline and a permissive single-agent baseline. We further show a multi-Bee chemistry workflow with explicit approval gating and a concrete top-3 shortlist grounded in real upstream evidence and screening artifacts. Additional comparisons with hybrid retrieval and LLM-guided provisioning show that richer provisioning backends are viable but do not outperform the lightweight structured retriever on the current small, highly structured capability registry. The results provide prototype-level systems evidence rather than a production deployment study, and suggest that enterprise agent platforms should be evaluated not only by capability, but also by governed provisioning, isolation behavior, scoped execution quality, and artifact-aware workflow coordination.

</details>

---

### [[20_Research/Papers/机器人/Attention-Guided_Autoencoder_Fusion_for_Insulator_Defect_Detection_Using_UAV_Transmission-Line_Imaging|Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV Transmission-Line Imaging]]

![[assets/2606.06536_figure.png|800]]

- **arXiv**: [2606.06536](https://arxiv.org/abs/2606.06536)
- **PDF**: https://arxiv.org/pdf/2606.06536
- **详细分析**: [[20_Research/Papers/机器人/Attention-Guided_Autoencoder_Fusion_for_Insulator_Defect_Detection_Using_UAV_Transmission-Line_Imaging|Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV Transmission-Line Imaging]]
- **作者**: Malak Allam, Khaled Shaban, Ali Hamdi
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV Transmission-Line Imaging》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CenterNet, DenseNet, EfficientNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated defect detection in high-voltage transmission-line insulators remains challenging due to severe class imbalance, large scale variation, and the small spatial extent of defect instances in Unmanned Aerial Vehicle (UAV) imagery. To address these challenges, this paper proposes AE-YOLO, an Attention-Guided AutoEncoder-Enhanced YOLO framework for robust insulator defect detection. The architecture integrates lightweight bottleneck autoencoders within a Feature Pyramid Network-Path Aggregation Network (FPN-PAN) neck. This preserves anomaly-sensitive information during multi-scale feature fusion. Convolutional Block Attention Modules (CBAM) are used throughout the backbone, enhancing feature discrimination and suppressing background interference. The framework also introduces a variance-maximizing autoencoder regularization strategy, which encourages diverse, defect-discriminative latent representations. The network trains using a unified objective that combines focal loss, Complete IoU (CIoU) loss, and autoencoder regularization to address foreground-background imbalance and improve localization accuracy. During inference, Weighted Boxes Fusion (WBF) combines predictions from YOLOv8, YOLOv10, and YOLO11. An autoencoder-guided confidence boosting mechanism improves sensitivity to rare defect categories. Experiments on the Insulator-Defect Detection dataset show that AE-YOLO with an EfficientNetV2 backbone achieves 95.10 percent mAP at 0.5, 96.40 percent precision, and 93.80 percent recall. This performance surpasses the strongest YOLO-family baseline by 5.0 points in mAP at 0.5 and 6.7 points in recall. These results confirm the effectiveness and adaptability of the framework. The model is a practical and scalable solution for UAV-based transmission-line inspection and defect monitoring.

</details>

---

### [[20_Research/Papers/大模型/Autonomous_heterogeneous_catalyst_discovery_with_a_self-evolving_multi-agent_digital_twin|Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin]]

![[assets/2606.05050_figure.png|800]]

- **arXiv**: [2606.05050](https://arxiv.org/abs/2606.05050)
- **PDF**: https://arxiv.org/pdf/2606.05050
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_heterogeneous_catalyst_discovery_with_a_self-evolving_multi-agent_digital_twin|Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin]]
- **作者**: Zhilong Song, Zongmin Zhang, Lixue Cheng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Autonomous heterogeneous catalyst discovery with a self-evolving multi-agent digital twin》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DimeNet, GemNet, SchNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Theoretical heterogeneous catalysis promises rapid catalyst discovery, yet computational and machine-learning predictions often deviate from experiment and stay confined to narrow material families, for want of a faithful, condition-aware catalytic simulator. We present CatDT (Catalysis Digital Twin), a self-evolving multi-agent system that builds an autonomous digital twin of a working catalyst, unifying gas-solid and liquid-solid modeling. From only a bulk crystal and a natural-language reaction description, eight specialized agents and 27 scientific tools predict stable facets, reconstruct working surfaces, enumerate and rank reaction pathways, locate transition states, and compute kinetics in 5-30 min on a single GPU. Two innovations address the hardest steps: UniMech finds dominant pathways for novel materials at over $10^3\times$ lower cost than exhaustive enumeration by fusing agent-guided proposals with energy-cached graph search, and a memory-augmented reinforcement loop raises barrier-calculation success from 41\% to 84\% across 600 catalytic surfaces. Across seven gas-solid benchmarks -- stepped metals, single-atom catalysts, ordered intermetallics, vacancy-rich 2D sulfides and carbides, and a strong-metal--support-interaction (SMSI) interface -- every CatDT prediction lies within 0.5-2 times experiment over four orders of magnitude. For propane dehydrogenation, CatDT independently discovers non-precious candidates rivaling the Pt-based industrial benchmark, with a proposed Ni@ZrO$_2$ SMSI overlayer reaching a simulated TOF of $1.63~\text{s}^{-1}$ at $\sim$100\% selectivity. More broadly, the decisive factor for a faithful catalyst digital twin -- or any multi-stage scientific simulator -- is not raw LLM capability but the engineered harness around it: deterministic tools, persistent memory, and verified self-improvement that compound across models, tools, and runs.

</details>

---
