# cs.CL | Computation and Language | 2026-07-29

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Forensic_Reproducibility_Audit_of_a_Radiology_Vision-Language_Model_Benchmark_From_Intended_Protocol_to_Released_Artifact|Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact]]

![[assets/2607.25589_figure.png|800]]

- **arXiv**: [2607.25589](https://arxiv.org/abs/2607.25589)
- **PDF**: https://arxiv.org/pdf/2607.25589
- **详细分析**: [[20_Research/Papers/大模型/Forensic_Reproducibility_Audit_of_a_Radiology_Vision-Language_Model_Benchmark_From_Intended_Protocol_to_Released_Artifact|Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact]]
- **作者**: Mateusz Kozłowski
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases. Agreement across these artifacts is usually assumed rather than tested. We performed a retrospective forensic reproducibility audit of a preserved chest-radiograph vision-language model (VLM) pilot; no model was called again and no image or report was newly annotated. We traced prompt bindings, DICOM metadata, output completeness, label extraction, matched analyses, and release propagation. Of 300 planned model-prompt calls, 297 yielded nonempty reports. Sixty Claude calls labeled A/B were executed with the same C prompt. The 30 studies represented 28 patients. Four MONOCHROME1 images were rendered without required polarity inversion, dataset split membership was not retained, and the unvalidated extractor truncated five reports to 4000 characters. Reconstructing one common cohort of 369 complete case-finding blocks changed Cochran's Q from 154.73 to 182.29. Of 45 McNemar comparisons, 27 had unadjusted p &lt; 0.05 and 20 remained below 0.05 after Holm adjustment. These values describe only the archived automated-label matrix; they do not recover the intended prompt comparison or establish clinical performance. We withdraw the original performance, ranking, prompt-effect, and clinical claims and specify machine-verifiable controls for cohort, DICOM rendering, prompt and model identity, call status, annotation provenance, keyed analysis, and derived artifacts.

</details>

---

### [[20_Research/Papers/强化学习/Temporal-Distance_JEPA_Plan-Aware_Representation_Learning_for_Latent_World_Model_Predictive_Control|Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control]]

![[assets/2607.25337_figure.png|800]]

- **arXiv**: [2607.25337](https://arxiv.org/abs/2607.25337)
- **PDF**: https://arxiv.org/pdf/2607.25337
- **详细分析**: [[20_Research/Papers/强化学习/Temporal-Distance_JEPA_Plan-Aware_Representation_Learning_for_Latent_World_Model_Predictive_Control|Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control]]
- **作者**: Jiaxin Bai, Jiaxuan Xiong
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control》归入 世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GCRL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, which arises as a byproduct of representation learning rather than as a progress cost mined from the logs. We propose temporal-distance JEPA (TD-JEPA), which retains the LeWM encoder--predictor backbone and mines a directed temporal cost from reward-free trajectories: same-trajectory step order supplies positive targets, cross-trajectory pairs act as heuristic negatives, and a rollout-consistency term matches the planner horizon. The mined supervision serves two roles: as the deployed planning cost when progress is topological, and as a representation signal that improves Euclidean planning when contact geometry dominates. Under locked evaluation, deploying the mined cost raises Two-Room success to 100.0% versus LeWM's 97.4%, while shared Euclidean planning on the same temporally trained checkpoint raises OGB-Cube by 14.2 points over LeWM and improves Push-T. Against LeWM and the concurrent RC-aux baseline under locked evaluation, TD-JEPA matches or exceeds both methods on every environment. Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute. TD-JEPA narrows the train--plan gap for JEPA world-model planners by discovering temporal progress structure in offline logs and co-designing cost form with plan-time deployment. Code is available at https://github.com/HKBU-KnowComp/TD-JEPA.

</details>

---

### [[20_Research/Papers/具身智能/VisualPatchWorld_Code_World_Models_as_Latent_Structured_Representations_for_Planning|VisualPatchWorld: Code World Models as Latent Structured Representations for Planning]]

![[assets/2607.25236_figure.png|800]]

- **arXiv**: [2607.25236](https://arxiv.org/abs/2607.25236)
- **PDF**: https://arxiv.org/pdf/2607.25236
- **详细分析**: [[20_Research/Papers/具身智能/VisualPatchWorld_Code_World_Models_as_Latent_Structured_Representations_for_Planning|VisualPatchWorld: Code World Models as Latent Structured Representations for Planning]]
- **作者**: Jiaxin Bai, Jiaxuan Xiong
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《VisualPatchWorld: Code World Models as Latent Structured Representations for Planning》归入 世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NewtonBench, PatchWorld, PoE-World, RLVR-World, VisualPatchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Different research lines use the term world model in different ways, yet they share a common aim: to capture how the world evolves under action in a form that supports perception, simulation, and planning. Two prominent realizations are neural predictors that learn dynamics in continuous vector spaces, and hand-built physics engines that expose explicit state and physical laws. Neural predictors scale from data but leave the form of the dynamics implicit; physics engines are inspectable and editable but difficult to construct at scale. We introduce VisualPatchWorld (VPW), which represents world dynamics as code. VPW first selects a qualitative dynamical form with short active probes, then fits that form's free parameters from recorded state-action traces by minimizing multi-step prediction error. The resulting programs can be rolled forward like a simulator, inspected in source form, and used inside model-predictive control; image-derived scene graphs can supply the live state at replan time. Across comparisons with prior code-based world models, VPW attains 69.0% mean planning success and exceeds the strongest code baseline by 23.5 points. The largest gains arise when choosing the correct qualitative dynamics is essential. Under the same planner, the induced models approach ground-truth engine success on navigation and grasp-rich control; a residual gap remains for contact-rich pushing, and checking a shortlist of promising plans in the engine closes most of that gap. These results establish a practical route toward automatically constructed code world models that are useful for planning. Code is available at https://github.com/HKBU-KnowComp/VisualPatchWorld/.

</details>

---

### [[20_Research/Papers/大模型/Mage-VL_An_Efficient_Codec-Native_Streaming_Multimodal_Foundation_Model|Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model]]

![[assets/2607.24904_figure.png|800]]

- **arXiv**: [2607.24904](https://arxiv.org/abs/2607.24904)
- **PDF**: https://arxiv.org/pdf/2607.24904
- **详细分析**: [[20_Research/Papers/大模型/Mage-VL_An_Efficient_Codec-Native_Streaming_Multimodal_Foundation_Model|Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model]]
- **作者**: Senqiao Yang, Kaichen Zhang, Zhaoyang Jia, Jinghao Guo, Yifei Shen, Xinjie Zhang, Xiaoyi Zhang, Haoqing Wang, Xiao Li, Peng Zhang, Xiang An, Yin Xie...
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VideoQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. At its core, our custom tokenizer, Mage-ViT, replaces uniform frame sampling by selectively encoding dynamic, entropy-rich regions using motion vectors and residual energy across sparse anchor (I) and predicted (P) frames. Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context. Trained from scratch on approximately 560M unlabeled images and 100M unlabeled video frames, Mage-ViT matches or outperforms flagship encoders trained on billions of image-text pairs. We establish AI4AI data pipelines encompassing prompt-code joint optimization for multimodal captioning and AI-driven performance diagnosis to guide training recipes. Furthermore, through a bio-inspired dual-system architecture - a lightweight System 1 event gate and a causal System 2 decoder - Mage-VL enables proactive streaming perception. Extensive evaluations show that Mage-VL-4B matches Qwen3-VL-4B on static tasks while achieving strong gains in video understanding and 2D/3D spatial reasoning, with up to a 3.5x wall-clock inference speedup, and comprehensively surpasses the 15B Phi-4-reasoning-vision baseline. Beyond model artifacts, we deliver seven key empirical findings covering pre-training data efficiency, variable-resolution scaling, codec system acceleration, VideoQA SFT redundancy, motion-spatial synergy, AI4AI data pipelines, and Zero-Vision SFT for multimodal RL.

</details>

---

### [[20_Research/Papers/大模型/Retrieval,_not_hallucinations,_will_be_the_limiting_factor_for_LLM-based_clinical_AI_tools|Retrieval, not hallucinations, will be the limiting factor for LLM-based clinical AI tools]]

![[assets/2607.24793_figure.png|800]]

- **arXiv**: [2607.24793](https://arxiv.org/abs/2607.24793)
- **PDF**: https://arxiv.org/pdf/2607.24793
- **详细分析**: [[20_Research/Papers/大模型/Retrieval,_not_hallucinations,_will_be_the_limiting_factor_for_LLM-based_clinical_AI_tools|Retrieval, not hallucinations, will be the limiting factor for LLM-based clinical AI tools]]
- **作者**: Kirk Roberts, Steven Bedrick, Kurt Miller, William R. Hersh, Hongfang Liu
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Retrieval, not hallucinations, will be the limiting factor for LLM-based clinical AI tools》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discussions around large language model (LLM) errors in clinical artificial intelligence (AI) generally center around precision errors like hallucinations. This perspective, targeting both clinicians and AI researchers, seeks to shift that discussion to recall errors, particularly in retrieval of patient-level data needed for many clinical AI tools. The perspective outlines types of errors and mitigation strategies, describes research directions in LLMs and retrieval, and provides an overview of retrieval evaluation.

</details>

---
