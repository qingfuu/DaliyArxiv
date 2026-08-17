# cs.AI | Artificial Intelligence | 2026-08-14

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/机器人/HumanTracker_Towards_Comprehensive_and_Human-Aligned_Motion_Tracking_Benchmark|HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark]]

![[assets/2608.13555_figure.png|800]]

- **arXiv**: [2608.13555](https://arxiv.org/abs/2608.13555)
- **PDF**: https://arxiv.org/pdf/2608.13555
- **详细分析**: [[20_Research/Papers/机器人/HumanTracker_Towards_Comprehensive_and_Human-Aligned_Motion_Tracking_Benchmark|HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark]]
- **作者**: Dairu Liu, Zekun Qi, Jiayu Zeng, Ruixi Yu, Yu Guan, Yintianrun Zhang, Xuchuan Chen, Sikai Liang, Zekai Li, Chenghuai Lin, Xinqiang Yu, Wenyao Zhang...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: cs.AI

#### 研究背景与动机

《HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion tracking is central to teleoperation and whole-body imitation, yet evaluation often disagrees with what people perceive in videos. Kinematic errors average per-frame pose differences but miss the physical artifacts that matter most, particularly unstable support and incorrect contacts such as foot skating and mistimed touch-downs. Meanwhile, widely used test suites are small and lack the diversity needed to stress contact-rich, long-horizon behaviors. We introduce HumanTracker to make humanoid tracking evaluation both perceptually aligned and scalable. The HumanTracker benchmark contains approximately 153 hours of optical motion trajectories from multiple professional performers, organized into four motion families with text labels for fine-grained diagnosis. We further propose HumanScore, a preference-aligned metric trained on 12K motion pairs containing 24K motions. Across representative state-of-the-art trackers, HumanScore better predicts human preferences and reveals contact and stability failures that kinematic metrics often miss.

</details>

---

### [[20_Research/Papers/大模型/MARC_v1_An_Open-Source_Multi-Agent_Framework_for_Clinical_AI_Reasoning_and_Coordination|MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination]]

![[assets/2608.13476_first_page.png|800]]

- **arXiv**: [2608.13476](https://arxiv.org/abs/2608.13476)
- **PDF**: https://arxiv.org/pdf/2608.13476
- **详细分析**: [[20_Research/Papers/大模型/MARC_v1_An_Open-Source_Multi-Agent_Framework_for_Clinical_AI_Reasoning_and_Coordination|MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination]]
- **作者**: Saisha Shetty, Satvik Tripathi, Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, Jacinta Arnold, Shahriar Faghani, Tessa S Cook
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. The framework supports both API-based and local CPU-compatible deployments and is entirely configurable via YAML, without code modifications. MARC is designed to be model-agnostic, interpretable, and accessible to clinical domain experts without programming expertise. The full framework is available at https://github.com/Penn-RAIL/MARC-v1.

</details>

---

### [[20_Research/Papers/大模型/MLLM-Routed_Heterogeneous_Ensembles_for_Robust_Cross-Dataset_Image_Classification|MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification]]

![[assets/2608.13463_figure.png|800]]

- **arXiv**: [2608.13463](https://arxiv.org/abs/2608.13463)
- **PDF**: https://arxiv.org/pdf/2608.13463
- **详细分析**: [[20_Research/Papers/大模型/MLLM-Routed_Heterogeneous_Ensembles_for_Robust_Cross-Dataset_Image_Classification|MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification]]
- **作者**: Daniel Perkins, John Squires, Janou Milligan, Chandra Raskoti, Linda Ungerboeck
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlexNet, ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learners (SSL), and vision-language models (VLMs), each trained on a unified label space constructed from multiple image datasets with differing distributions and characteristics. Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains. Crucially, we show that ARMDIL effectively navigates these trade-offs, performing competitively with specialized training-based routers. Furthermore, it drastically improves adaptability by allowing new information to be integrated via simple prompt modifications, while enhancing interpretability through natural language reasoning traces. These advances in cross-dataset image classification pave the way for more reliable general-purpose vision systems such as AI assistants and autonomous robots.

</details>

---

### [[20_Research/Papers/世界模型/A_Unifying_Perspective_on_Causal_World_Models_From_Observations_to_Representations_to_Structure|A Unifying Perspective on Causal World Models: From Observations to Representations to Structure]]

![[assets/2608.13456_figure.png|800]]

- **arXiv**: [2608.13456](https://arxiv.org/abs/2608.13456)
- **PDF**: https://arxiv.org/pdf/2608.13456
- **详细分析**: [[20_Research/Papers/世界模型/A_Unifying_Perspective_on_Causal_World_Models_From_Observations_to_Representations_to_Structure|A Unifying Perspective on Causal World Models: From Observations to Representations to Structure]]
- **作者**: Avinash Kori, Fabrizio Russo
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《A Unifying Perspective on Causal World Models: From Observations to Representations to Structure》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entity interactions, and entity-to-environment interactions that determine and explain the dynamics of a system. We provide a formal definition of Causal WMs (CWMs) grounded in the tasks they are intended to support, connecting world modelling with existing work in causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making. Finally, we relate CWMs to the literature on identifiability, clarifying when the components of a WM can be recovered from data and up to which equivalence. With this, we ground WMs in representations and structures that support causal reasoning and informed decision-making.

</details>

---

### [[20_Research/Papers/具身智能/UniTexture_Cross-Task_Universal_Adversarial_Textures_for_Vision-Language-Action_Models|UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models]]

![[assets/2608.13453_figure.png|800]]

- **arXiv**: [2608.13453](https://arxiv.org/abs/2608.13453)
- **PDF**: https://arxiv.org/pdf/2608.13453
- **详细分析**: [[20_Research/Papers/具身智能/UniTexture_Cross-Task_Universal_Adversarial_Textures_for_Vision-Language-Action_Models|UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models]]
- **作者**: Yukun Dai, Mingzhe Dai, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.8，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $π_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.

</details>

---

### [[20_Research/Papers/强化学习/ContactGuard_Pre-Contact_Execution_Monitoring_with_Action-Conditioned_Latent_World_Models|ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models]]

![[assets/2608.13438_figure.png|800]]

- **arXiv**: [2608.13438](https://arxiv.org/abs/2608.13438)
- **PDF**: https://arxiv.org/pdf/2608.13438
- **详细分析**: [[20_Research/Papers/强化学习/ContactGuard_Pre-Contact_Execution_Monitoring_with_Action-Conditioned_Latent_World_Models|ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models]]
- **作者**: Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon consequence in latent visual space and aborts if the predicted future latent indicates likely failure. Its latent world model is trained from unlabelled robot trajectories to predict compact multi-view visual embeddings under planned actions, avoiding pixel-level video prediction. A lightweight failure probe is then trained from a small labelled set of pre-contact clips. At deployment, ContactGuard anchors prediction before an imminent contact event, rolls the model forward under the policy's own actions, and verifies the predicted post-contact latent. Across real-world contact-rich manipulation tasks, ContactGuard predicts failure more accurately than direct and corrupted-action ablations, and transfers to live robot as a pre-contact abort signal without modifying the underlying policy.

</details>

---

### [[20_Research/Papers/大模型/Are_You_Sure_You're_Sure_On_the_Impact_of_Instruction_Tuning_on_Confidence_and_Lexical_Diversity|Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity]]

![[assets/2608.13430_first_page.png|800]]

- **arXiv**: [2608.13430](https://arxiv.org/abs/2608.13430)
- **PDF**: https://arxiv.org/pdf/2608.13430
- **详细分析**: [[20_Research/Papers/大模型/Are_You_Sure_You're_Sure_On_the_Impact_of_Instruction_Tuning_on_Confidence_and_Lexical_Diversity|Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity]]
- **作者**: Irina Proskurina, Mayank Kumar, Oyindolapo O. Komolafe
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: cs.AI

#### 研究背景与动机

《Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CSQA, CommonsenseQA, ConceptNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instruction-tuned language models achieve strong performance across a range of generation tasks, but have also recently been shown to exhibit verbalized overconfidence. In question answering, verbalized model overconfidence may be associated with the consistency of the generated supporting rationales. In this paper, we study whether corresponding changes in the lexical diversity of generated answer rationales accompany changes in model confidence induced by instruction tuning. We evaluate three matched base and instruction-tuned models across question-answering benchmarks and find that instruction tuning consistently alters answer confidence, despite limited changes in predictive accuracy and decreases in likelihood-based calibration. Secondly, we observe a non-uniform effect of instruction tuning on rationale diversity: cross-rationale diversity consistently decreases, whereas surface-level lexical diversity varies in both direction and magnitude across models and benchmarks. Finally, we find that these differences persist after controlling for answer selection and rationale length, confirming that confidence and rationale diversity capture distinct effects of instruction tuning.

</details>

---

### [[20_Research/Papers/大模型/Reduced_Matrix_Multiplication_Input-Adaptive_Matrix-Product_Reduction_for_LLM_Inference|Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference]]

![[assets/2608.13426_figure.png|800]]

- **arXiv**: [2608.13426](https://arxiv.org/abs/2608.13426)
- **PDF**: https://arxiv.org/pdf/2608.13426
- **详细分析**: [[20_Research/Papers/大模型/Reduced_Matrix_Multiplication_Input-Adaptive_Matrix-Product_Reduction_for_LLM_Inference|Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference]]
- **作者**: Zixuan Lan, Yanhong Li, Jiawei Zhou
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative slices along their contraction dimensions, without modifying model weights. Under a simple retention-ratio control, RMM provides a smooth and predictable accuracy-efficiency trade-off. Across language models ranging from 1B to 70B parameters, we find that reduction tolerance depends on the model family, task, component, and retention ratio, although it often improves with model scale. Under moderate reduction, RMM remains robust across the evaluated discriminative, autoregressive generation, and long-context settings. We further show that the same principle extends to multimodal vision-language inference. Mechanistic ablations reveal a structural asymmetry within Transformers: attention-side computations are substantially more reducible than MLP components. Finally, wall-clock benchmarks with custom kernels on an NVIDIA A100 show that these computational savings can translate into practical runtime gains, especially at longer sequence lengths. Together, these results position RMM as a scalable direction for input-adaptive inference-time optimization.

</details>

---

### [[20_Research/Papers/具身智能/Enhancing_Virtual_Agents_through_SLMs_and_Edge-Computing_An_Exploratory_Evaluation_of_Think_and_Memory_Processes|Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes]]

![[assets/2608.13420_figure.png|800]]

- **arXiv**: [2608.13420](https://arxiv.org/abs/2608.13420)
- **PDF**: https://arxiv.org/pdf/2608.13420
- **详细分析**: [[20_Research/Papers/具身智能/Enhancing_Virtual_Agents_through_SLMs_and_Edge-Computing_An_Exploratory_Evaluation_of_Think_and_Memory_Processes|Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes]]
- **作者**: Aimilios Hadjiliasi, Louis Nisiotis
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，大模型 0.5）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligent virtual agents are expected to operate as persistent, adaptive, and context-aware entities within complex virtual and Metaverse worlds. However, implementing cognitively capable agents in such environments is conceptually and technologically challenging. Among a range of blueprints and development approaches, the Cognitive Embodied Agent Architecture (CEAA) has been developed as an implementation-oriented framework for architecting components of perception, memory, reasoning, planning, and embodied action. Considering the recent advances in edge computing and generative AI language models, this paper explores the use of Small Language Models (SLMs) to support edge-based operation of selected CEAA components, focusing on "Think" and "Memory" as processes central to cognitive orchestration and persistence of virtual agents in interactive virtual worlds. An edge-based virtual agent gateway system was developed and evaluated on an NVIDIA Jetson Orin NX using Qwen2.5 models of different sizes, exploring the system's capability to process service requests and handle memory-driven conversations. A series of simulation experiments evaluated routing accuracy, memory-read performance, and latency, demonstrating an SLM-driven prototype agent system that partially implements selected CEAA processes to support the development of embodied agents whose cognitive "brain" can operate efficiently and contextually for interactive experiences in immersive virtual worlds.

</details>

---

### [[20_Research/Papers/强化学习/Deliberate_Practice_Learning_Robot_Skills_under_a_Budget|Deliberate Practice: Learning Robot Skills under a Budget]]

![[assets/2608.13415_first_page.png|800]]

- **arXiv**: [2608.13415](https://arxiv.org/abs/2608.13415)
- **PDF**: https://arxiv.org/pdf/2608.13415
- **详细分析**: [[20_Research/Papers/强化学习/Deliberate_Practice_Learning_Robot_Skills_under_a_Budget|Deliberate Practice: Learning Robot Skills under a Budget]]
- **作者**: Shivam Vats, Sudarshan Harithas, Mete Tuluhan Akbulut, Arvind Raghunathan, George Konidaris
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Deliberate Practice: Learning Robot Skills under a Budget》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the problem of autonomously learning robot skills under a limited practice budget for sequential tasks. We propose an active skill learning algorithm, \emph{Deliberate Practice (DP)}, that computes a provably \emph{budget-optimal} allocation---practicing skills that maximize expected cumulative reward while being learnable within the budget. DP estimates both the time needed to master skills and the cumulative reward of the task plans that the skills unlock. Computing a budget-optimal allocation is challenging as it requires reasoning about combinatorially many skill plans over a large practice budget. Our key contribution is a bilinear program that can compute this exactly using off-the-shelf solvers. Through simulated and real-world experiments on long-horizon manipulation tasks, we show that our approach allows robots to optimally use limited practice time to acquire useful policies and improve long-horizon planning.

</details>

---

### [[20_Research/Papers/大模型/StateBridge_Training-free_Hidden-state_Alignment_for_Latent_Communication_in_LLM_Multi-Agent_Systems|StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems]]

![[assets/2608.13317_first_page.png|800]]

- **arXiv**: [2608.13317](https://arxiv.org/abs/2608.13317)
- **PDF**: https://arxiv.org/pdf/2608.13317
- **详细分析**: [[20_Research/Papers/大模型/StateBridge_Training-free_Hidden-state_Alignment_for_Latent_Communication_in_LLM_Multi-Agent_Systems|StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems]]
- **作者**: Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

</details>

---

### [[20_Research/Papers/大模型/Keep,_Customize,_or_Exit_Default_Design_and_Token_Pricing_in_LLM_Reasoning_Services|Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services]]

![[assets/2608.13315_figure.png|800]]

- **arXiv**: [2608.13315](https://arxiv.org/abs/2608.13315)
- **PDF**: https://arxiv.org/pdf/2608.13315
- **详细分析**: [[20_Research/Papers/大模型/Keep,_Customize,_or_Exit_Default_Design_and_Token_Pricing_in_LLM_Reasoning_Services|Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services]]
- **作者**: Ahmet Bugra Gundogan, Yigit Turkmen, Melih Bastopcu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RouterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study a large language model (LLM) service in which a provider chooses a per-token price and a default reasoning-token allocation, while a user may accept the default, customize the allocation, or exit. Larger allocations can improve accuracy but increase token cost and latency. We model this interaction as a Stackelberg game and derive the user's unique optimal customized allocation in closed form. For any price, the acceptable defaults form either an empty set or a compact interval. We characterize the provider's optimal default through a three-regime rule, reduce equilibrium computation to a one-dimensional price optimization, and prove the existence of the equilibrium. We further show that defaults affect the implemented reasoning allocation only when users value the convenience of avoiding customization; otherwise, every service-providing outcome implements the user's optimal customized allocation. Experiments with two compact open-weight reasoning models on five mathematics and science benchmarks support the accuracy-token model and show how model and task characteristics determine equilibrium prices, defaults, and reasoning allocations.

</details>

---

### [[20_Research/Papers/大模型/Mixture_of_Training_Recombining_Small-Scale_Scaffolded_Pretraining_Runs_into_a_Larger_Language_Model|Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model]]

![[assets/2608.13277_figure.png|800]]

- **arXiv**: [2608.13277](https://arxiv.org/abs/2608.13277)
- **PDF**: https://arxiv.org/pdf/2608.13277
- **详细分析**: [[20_Research/Papers/大模型/Mixture_of_Training_Recombining_Small-Scale_Scaffolded_Pretraining_Runs_into_a_Larger_Language_Model|Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model]]
- **作者**: Mohammed Sabry, Sean Augenstein, Keith Rush, Lucio Dery
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We ask whether language-model pre-training can be decomposed into smaller, independently trainable jobs that can later be recomposed into a coherent larger model. We introduce Mixture of Training (MoT), a scaffolded modular pre-training procedure that partitions a target Transformer into contiguous layer blocks, trains each block inside a frozen pretrained aligner scaffold, and then recomposes the trained blocks with an optional short end-to-end adaptation pass. On a 1.3B-parameter Gemma-style model trained on C4, MoT provides a small-scale proof of mechanism: independently trained depth slices can be recomposed into a usable language model, and a quality-parity schedule reaches the same reported perplexity as the monolithic baseline. This parity setting processes more aggregate tokens and has a shorter idealized layer-equivalent critical path after aligner preparation; its effective compute advantage depends on reusing the aligner across runs. We therefore present MoT not as a general replacement for monolithic pre-training, but as a small-scale framework for studying whether scaffolded sub-runs can act as reusable training units.

</details>

---

### [[20_Research/Papers/大模型/Teach_the_Magnitude,_Not_the_Direction_Verifier-Bounded_Credit_Assignment_for_Multi-Turn_Multi-step_LLM_Agents|Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents]]

![[assets/2608.13179_first_page.png|800]]

- **arXiv**: [2608.13179](https://arxiv.org/abs/2608.13179)
- **PDF**: https://arxiv.org/pdf/2608.13179
- **详细分析**: [[20_Research/Papers/大模型/Teach_the_Magnitude,_Not_the_Direction_Verifier-Bounded_Credit_Assignment_for_Multi-Turn_Multi-step_LLM_Agents|Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents]]
- **作者**: Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.7，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：WildToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) offers a verifier-bounded performance ceiling for training multi-turn tool-use agents, yet its trajectory-level credit assignment conflates heterogeneous per-turn outcomes into a single reward signal. On-policy distillation provides dense per-token supervision but is either teacher-bounded or prone to gradient concentration collapse. We introduce $\textbf{CrEST}$, a hierarchical credit assignment framework that retains RL's verifier-bounded ceiling while incorporating dense token-level signals from a privileged self-teacher. $\textbf{CrEST}$ resolves credit at two levels: turn-segmented verified advantages address inter-turn dilution, while entropy-gated self-teacher modulation refines intra-turn token contributions. Experiments on BFCL V3 and WildToolBench show that $\textbf{CrEST}$ consistently outperforms both RL and distillation baselines across two model scales, with the largest gains on long-trajectory and strict session-level metrics. Our work demonstrates that the teacher's role in policy optimization can be reduced from determining update directions to modulating update magnitudes, unlocking dense credit assignment without sacrificing the verifier-bounded ceiling.

</details>

---

### [[20_Research/Papers/大模型/SkillShapley_Boundary-Adaptive_Shapley_Valuation_for_Skill_Step_Attribution_in_LLM_Agents|SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents]]

![[assets/2608.13173_figure.png|800]]

- **arXiv**: [2608.13173](https://arxiv.org/abs/2608.13173)
- **PDF**: https://arxiv.org/pdf/2608.13173
- **详细分析**: [[20_Research/Papers/大模型/SkillShapley_Boundary-Adaptive_Shapley_Valuation_for_Skill_Step_Attribution_in_LLM_Agents|SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents]]
- **作者**: Chang Liu, Yuqi Zhang, Yiman Zhong, Boyi Liu, Hengjun Wang, Shuyue Wei
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model skill-step attribution as a Shapley value-based contribution estimation problem, and then propose SkillShapley, a step-level attribution framework for agent skills. Notably, SkillShapley operates in two phases, motivated by key empirical insights, i.e., discretized benchmark rewards that create sharp performance cliffs, and step interactions that are largely additive rather than synergistic. Specifically, it first identifies informative coalitional regions, and then adaptively samples new coalitions that can yield reusable marginal evidence. Experiments on skills from the widely adopted SkillsBench demonstrate that our SkillShapley can effectively and efficiently identify high- or low-value skill steps, providing several key takeaways for agent skill creation.

</details>

---

### [[20_Research/Papers/大模型/LigBench_A_Unified_and_Human-Aligned_Benchmark_for_LLM-based_Research_Idea_Generation|LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation]]

![[assets/2608.13136_figure.png|800]]

- **arXiv**: [2608.13136](https://arxiv.org/abs/2608.13136)
- **PDF**: https://arxiv.org/pdf/2608.13136
- **详细分析**: [[20_Research/Papers/大模型/LigBench_A_Unified_and_Human-Aligned_Benchmark_for_LLM-based_Research_Idea_Generation|LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation]]
- **作者**: Chenrun Wang, Mingxuan Zhu, Tiancheng Huang, Wenjie Li, Yujie Zhang, Zichen Zhu, Zhiying Zou, Kai Yu, Lu Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LigBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid advancement of large language models (LLMs), research idea generation has attracted increasing attention. Existing approaches enable LLMs to retrieve relevant literature and propose novel ideas for research areas. However, current evaluation practices for idea generation remain fragmented and lack objective standards, often relying on direct LLM scoring, which limits their ability to provide unified and reliable assessments across a coherent distribution of generated ideas. To address this challenge, we propose LigBench, an automated evaluation benchmark that enables fine-grained and reliable evaluation of AI research ideas, consistently applicable across different generation distributions. In addition, we introduce PAIR-IQ, a dataset tailored for training pairwise idea judgment models and serving as an auxiliary reference to support more objective comparative evaluation. Extensive experiments demonstrate that LigBench achieves stable and interpretable evaluations, significantly improving alignment with expert judgments. Furthermore, models trained on PAIR-IQ exhibit enhanced ranking accuracy and robustness, establishing a principled standard for scalable and objective research idea assessment.

</details>

---

### [[20_Research/Papers/具身智能/OGR-MARL_Option-Guided_Residual_Multi-Agent_Reinforcement_Learning_for_Heterogeneous_USV_Cooperative_Pursuit_in_Constrained_Port_Waterways|OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways]]

![[assets/2608.12995_figure.png|800]]

- **arXiv**: [2608.12995](https://arxiv.org/abs/2608.12995)
- **PDF**: https://arxiv.org/pdf/2608.12995
- **详细分析**: [[20_Research/Papers/具身智能/OGR-MARL_Option-Guided_Residual_Multi-Agent_Reinforcement_Learning_for_Heterogeneous_USV_Cooperative_Pursuit_in_Constrained_Port_Waterways|OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways]]
- **作者**: Mao Jiayang, Wang Lanfeng, Peng Zhao-Han
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL, OGR-MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Heterogeneous USV cooperative pursuit in constrained port waterways requires evader interception under navigation, traffic, and role constraints. This paper proposes OGR-MARL, an option-guided residual multi-agent reinforcement learning framework that is decoupled from a specific MARL algorithm. OGR-MARL integrates shared evader belief, role-conditioned option targets, adaptive rule penalties, and residual policy learning, allowing different MARL algorithms to learn corrective actions on top of rule-guided behaviors rather than exploring constrained port environments from scratch. We instantiate OGR-MARL with representative continuous-control MARL backbones, including MADDPG, MATD3, MAPPO, and MASAC, yielding OGR-MADDPG, OGR-MATD3, OGR-MAPPO, and OGR-MASAC. Experiments in an abstract Xiazhimen port-waterway scenario show that the OGR-MASAC instantiation achieves a 75.0% capture rate, promising mission-effective rule compliance, and the best heterogeneous coordination among the tested methods. Without retraining, zero-shot transfer to a QGIS/AIS-informed Xiazhimen map achieves promising results, demonstrating the generalization potential of OGR-MARL in more complex port scenarios.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Handcrafted_Security_Towards_Self-Evolving_Defense_for_LLM_Agents|Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents]]

![[assets/2608.12977_figure.png|800]]

- **arXiv**: [2608.12977](https://arxiv.org/abs/2608.12977)
- **PDF**: https://arxiv.org/pdf/2608.12977
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Handcrafted_Security_Towards_Self-Evolving_Defense_for_LLM_Agents|Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents]]
- **作者**: Jiajun Ruan, Peiyang Li, Yukun Chen, Fengting Li, Chao Feng
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The expanding operational capabilities of large language model (LLM) agents introduce sophisticated security threats. Runtime defenses have emerged as an effective approach to mitigating these risks by integrating security mechanisms into the agent execution loop. However, existing runtime defenses rely heavily on manually designed interventions and lack a principled framework for their construction and maintenance. In this work, we first develop a harness-level formulation of runtime defense that systematically characterizes how harness mechanisms enable defense construction and provides a unified view of existing runtime defense interventions from a harness perspective. Building on this formulation, we propose HARD (Harness-based Autonomous Runtime Defense Evolution), a self-evolving runtime defense framework that automatically identifies appropriate intervention strategies and iteratively improves defense artifacts based on observed failure traces. HARD transforms runtime defense development from manual engineering into an autonomous evolution process, and extensive experiments demonstrate that it improves security performance over existing handcrafted defenses while preserving benign task utility. Our findings highlight autonomous defense evolution as a promising new paradigm for securing deployed LLM agents, enabling agents to identify defense weaknesses and continuously improve their protection mechanisms.

</details>

---

### [[20_Research/Papers/世界模型/The_Objective_Is_the_Bottleneck_Latent_World_Models_Encode_What_Their_Planners_Cannot_Use|The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use]]

![[assets/2608.12959_first_page.png|800]]

- **arXiv**: [2608.12959](https://arxiv.org/abs/2608.12959)
- **PDF**: https://arxiv.org/pdf/2608.12959
- **详细分析**: [[20_Research/Papers/世界模型/The_Objective_Is_the_Bottleneck_Latent_World_Models_Encode_What_Their_Planners_Cannot_Use|The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use]]
- **作者**: Joyjeet Singh
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent

#### 研究背景与动机

《The Objective Is the Bottleneck: Latent World Models Encode What Their Planners Cannot Use》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models are judged by how well they predict, so when planning fails at long horizons the natural reading is that the predictor degrades. On a reproduction of LeWorldModel on TwoRoom we show the binding constraint is the planner's objective instead. The predictor is not the limit: its imagined state seventy-five environment steps ahead is still only 0.189 as wrong as assuming the world froze, while the planner never imagines beyond twenty-five. The objective is. Cross-entropy-method planning minimises squared latent distance, which tracks true distance at r = 0.426, saturates by about eighty arena units and decreases beyond a hundred and twenty, so moving away from the goal can lower the cost. The information is present throughout: a ridge probe recovers position from the frozen embedding at R^2 0.9922. The pathology is the method's, not one reimplementation's. It is present in the authors' released weights, and across four checkpoints long-horizon success rank-orders exactly with metric quality and inversely with prediction accuracy. Replacing only the objective, with nothing retrained and no GPU, lifts goals reached at offset 100 from 26.0% to 98.0%, equals the 98.0% at offset 25, and reaches 92.0% under a third of the budget: planning stops depending on the horizon. The best cost is not the most accurate. A head learned from frame separation alone predicts spatial distance worse than a position probe (r = 0.819 against 0.9897) yet plans better, charging 24% more to cross the environment's dividing wall where squared latent distance charges 4% less. It has learned reachability, not proximity.

</details>

---

### [[20_Research/Papers/具身智能/FlashDrive_Flash_Vision-Language-Action_Inference_for_Autonomous_Driving|FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving]]

![[assets/2608.12932_figure.png|800]]

- **arXiv**: [2608.12932](https://arxiv.org/abs/2608.12932)
- **PDF**: https://arxiv.org/pdf/2608.12932
- **详细分析**: [[20_Research/Papers/具身智能/FlashDrive_Flash_Vision-Language-Action_Inference_for_Autonomous_Driving|FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving]]
- **作者**: Zekai Li, Yihao Liang, Hongfei Zhang, Jian Chen, Yesheng Liang, Zhijian Liu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AlpaSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-matching denoising applies uniform compute to a non-uniform velocity field. Addressing any one stage in isolation leaves the others untouched. We propose FlashDrive, an algorithm-system co-design framework that targets all four stages simultaneously. Our key insight is that each bottleneck admits a distinct, lightweight algorithmic shortcut: temporal overlap enables streaming KV-cache reuse across frames; the low per-token entropy and strong intra-block correlations of driving-domain reasoning make a non-autoregressive diffusion drafter highly effective for speculative decoding; and the velocity field's structure---sharp at the endpoints, flat in the middle---permits adaptive step caching that concentrates compute where it matters. Layered on system-level CUDA Graph compilation and kernel fusion, these techniques compound. Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rates improve in simulation. By raising a 10B-parameter reasoning VLA from 1.4~Hz to 6.6~Hz on a single GPU, FlashDrive moves end-to-end autonomous driving substantially closer to real-time deployment.

</details>

---

### [[20_Research/Papers/大模型/Discovering_Efficient_and_Explainable_Communication_Topologies_for_LLM-based_Multi-Agent_Systems_via_Causal_Inference|Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference]]

![[assets/2608.12921_figure.png|800]]

- **arXiv**: [2608.12921](https://arxiv.org/abs/2608.12921)
- **PDF**: https://arxiv.org/pdf/2608.12921
- **详细分析**: [[20_Research/Papers/大模型/Discovering_Efficient_and_Explainable_Communication_Topologies_for_LLM-based_Multi-Agent_Systems_via_Causal_Inference|Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference]]
- **作者**: Junzhi Li, Peng He, Qirui Ji, Wei Wang, Lixiang Liu, Chuxiong Sun
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. While effective, such optimization provides little insight into why particular communication edges are selected, making it difficult to identify the critical communication subgraphs responsible for successful collaboration. To address this limitation, we propose E2-Explainer, a model-agnostic framework for providing interpretable explanations of communication topologies produced by arbitrary topology generators. Specifically, we formulate topology explanation as a causal attribution problem that identifies compact communication subgraphs supported by edge-level evidence of task preservation. We obtain this evidence with a Granger-style objective that measures how masking each communication channel changes the task outcome and the stability of the final response. The resulting budgeted subgraphs are then distilled into an amortized explainer, enabling efficient post-hoc explanation without repeated edge-level evaluations at deployment. Extensive experiments on multiple reasoning and coding benchmarks demonstrate that E2-Explainer identifies critical communication subgraphs that preserve successful collaboration. These subgraphs can also be executed directly to prune redundant communication edges, substantially reducing communication costs while maintaining competitive task performance.

</details>

---

### [[20_Research/Papers/大模型/Agent_Behavioral_Contracts_II_Certifying_Compositional_Reliability_Without_Assuming_Independence|Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence]]

![[assets/2608.12895_first_page.png|800]]

- **arXiv**: [2608.12895](https://arxiv.org/abs/2608.12895)
- **PDF**: https://arxiv.org/pdf/2608.12895
- **详细分析**: [[20_Research/Papers/大模型/Agent_Behavioral_Contracts_II_Certifying_Compositional_Reliability_Without_Assuming_Independence|Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence]]
- **作者**: Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compositional reliability bounds for multi-agent systems multiply component reliabilities, a step licensed by a conditional-independence assumption that is routinely stated and rarely tested. We test it. Two instances of one model, in a two-agent handoff, co-fail on 90.0% of the missions on which either fails (log OR 6.66, 95% CI [6.38, 7.00]; phi 0.916), in a preregistered evaluation of 18,000 missions scored by deterministic code with no LLM judge. Substituting a different model reduces the association in six of six contrasts; substituting a different vendor, model already different, does not -- a registered hypothesis reported as a null. The error is signed and runs against the operator: positive dependence inflates joint failure above the independence product, so redundancy is over-credited exactly when components share a model. The assumption-free alternative is often vacuous, and fitting a dependence model is worse: we prove a bootstrap bound on a fitted model's functional loses coverage of the truth as n grows, the identification gap being O(1) while the bootstrap haircut is O(n^{-1/2}). More data makes such a certificate worse, with no visible symptom. We give a finite-sample certificate assuming no dependence structure: a linear program over the joint, over a Bonferroni-Clopper-Pearson box around measured co-execution moments. It is sound, sharp for the information supplied, and monotone in the moment family. Enriching ten moment functionals to fourteen narrows the identified interval by 85.7% and lifts the certified floor from 0.2455 to 0.4116. A companion anytime-valid certificate holds type-I error at 0.0471 under optional stopping. Common dependence statistics are marginal-bounded and can reverse an apparent ordering of conditions when the compared agents fail at different rates. Contracts, scoring code, analysis scripts, and the preregistration are released.

</details>

---

### [[20_Research/Papers/机器人/ReflectFact_Self-Reflective_Agents_for_Improving_Comprehension_and_Reasoning_in_Multi-Hop_Fact_Verification|ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification]]

![[assets/2608.12877_figure.png|800]]

- **arXiv**: [2608.12877](https://arxiv.org/abs/2608.12877)
- **PDF**: https://arxiv.org/pdf/2608.12877
- **详细分析**: [[20_Research/Papers/机器人/ReflectFact_Self-Reflective_Agents_for_Improving_Comprehension_and_Reasoning_in_Multi-Hop_Fact_Verification|ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification]]
- **作者**: Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, Dongyang Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.7（加权：大模型 0.5，机器人 0.2）
- **关联关键词**: Agent

#### 研究背景与动机

《ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However, these methods face two critical limitations: (1) agents may perform individual subtasks without sufficient awareness of the global verification objective, causing their reasoning to deviate from the intended direction; and (2) conflicts between parametric knowledge and the provided evidence may undermine evidence-grounded reasoning and lead to incorrect verdicts. To address these challenges, we propose ReflectFact, a novel self-reflective agent framework for multi-hop fact verification. ReflectFact introduces three key tasks. Explicit Reasoning Path Planning builds an evidence-grounded reasoning path by resolving implicit entities, decomposing the claim into sub-questions, and integrating the verified facts into a verdict. Evidence-Drift Verification makes the agent re-answer by quoting the supporting evidence when a grounded answer merely echoes its parametric prior, thereby calibrating evidence deviation to ensure grounded comprehension. Reasoning Reflection Verification re-examines each reasoning step and regenerates it once an inconsistency is detected, correcting reasoning flaws such as location bias and replacement bias through a global task perspective. Subsequently, the agent aggregates validated reasoning chains to yield reliable verdicts. Extensive experiments on HOVER and EX-FEVER demonstrate that ReflectFact effectively remedies the comprehension and reasoning defects of existing methods, achieving state-of-the-art performance and respectively outperforming the strongest baseline by 3.32\% and 2.78\% on the two datasets.

</details>

---

### [[20_Research/Papers/具身智能/BrainWAM_Action-Space_Coordination_of_Semantic_Priors_and_Predictive_Dynamics_for_Autonomous_Driving|BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving]]

![[assets/2608.12854_figure.png|800]]

- **arXiv**: [2608.12854](https://arxiv.org/abs/2608.12854)
- **PDF**: https://arxiv.org/pdf/2608.12854
- **详细分析**: [[20_Research/Papers/具身智能/BrainWAM_Action-Space_Coordination_of_Semantic_Priors_and_Predictive_Dynamics_for_Autonomous_Driving|BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving]]
- **作者**: Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu, Zhao Wang, Yida Wang, Xueyang Zhang, Kun Zhan, Lue Fan, Zhaoxiang Zhang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA, OpenDriveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous driving requires planning under both semantic constraints and predictive dynamics. Existing end-to-end driving approaches, however, typically emphasize only one side of this requirement: Vision-Language-Action (VLA) models exploit VLM priors for semantic reasoning, while World Action Models (WAMs) provide future-aware prediction through generative world modeling. This naturally motivates a unified planner that can leverage both semantic priors and predictive dynamics. However, we find that a naive combination through joint token-level attention suffers from an attention-allocation mismatch, where semantic shortcuts dominate the shared attention space and suppress predictive dynamics. Inspired by neuroscience evidence that complex behavior arises from coordination among functionally specialized systems, we propose BrainWAM, a structured action-space coordination framework that converts semantic reasoning and predictive world modeling into two specialized action-oriented pathways, and aligns them at the level of compact action representations. We further introduce an asynchronous rectified-flow inference strategy with decoupled video and action denoising, which shortens inference latency while preserving planning-relevant predictive context. BrainWAM reaches state-of-the-art performance on both NAVSIM v1 (89.5 PDMS) and NAVSIM v2 (89.6 EPDMS), consistently outperforming VLA-only or WAM-only methods, highlighting BrainWAM as a practical and promising direction for autonomous driving systems.

</details>

---

### [[20_Research/Papers/大模型/Practice_Makes_Unsafe_Skill_Misevolution_in_Self-Improving_LLM_Agents|Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents]]

![[assets/2608.12851_figure.png|800]]

- **arXiv**: [2608.12851](https://arxiv.org/abs/2608.12851)
- **PDF**: https://arxiv.org/pdf/2608.12851
- **详细分析**: [[20_Research/Papers/大模型/Practice_Makes_Unsafe_Skill_Misevolution_in_Self-Improving_LLM_Agents|Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents]]
- **作者**: Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillMisevo-Bench, SkillMisevo-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or static artifacts but cannot attribute risk across authoring, retrieval, and later execution. To expose this lifecycle, we introduce SkillMisevo-Gym, a lifecycle-aware harness that versions skill state across agent frameworks, and SkillMisevo-Bench, a frozen design from malicious exposure to carryover tasks, with concept-aligned benign tasks and nine lifecycle metrics. We also introduce SafeEvolve, a wrapper that repairs unsafe content and governs subsequent reuse. Across 25 agent-method configurations, each covering 525 tasks in 25 episodes, all 21 evolved configurations author unsafe artifacts, while only fifteen lead to fresh-session harm. In the exposure sweep, three malicious tasks raise carryover ASR from 16.0% to 35.3%. Across representative skill evolution methods, SafeEvolve reduces unsafe retrieval and fresh-session harm by 26.7 and 17.3 percentage points, respectively, while mean benign utility changes by only 0.4 points. Together, persistent-adaptation safety must govern what updates write and what future executors reuse. Code is available at https://github.com/henrymao2004/misevolve.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Retrieval_Query-Conditioned_Reuse_of_Long-Horizon_Agent_Trajectories|Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories]]

![[assets/2608.12847_figure.png|800]]

- **arXiv**: [2608.12847](https://arxiv.org/abs/2608.12847)
- **PDF**: https://arxiv.org/pdf/2608.12847
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Retrieval_Query-Conditioned_Reuse_of_Long-Horizon_Agent_Trajectories|Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories]]
- **作者**: Yifei Li, Heng Wang, Lingling Zhang, Muye Huang, Xinyu Zhang, Jiashuai Liu, Hang Yan, Rongman Xu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent

#### 研究背景与动机

《Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AndroidWorld, AppWorld, LongBench, LongMemEval, MemBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval can identify a past trajectory that may matter, yet it does not specify how an acting agent should use that trajectory after users, entities, constraints, or environment state have changed. We identify this post-retrieval reuse step as a distinct bottleneck for long-horizon trajectory memory and formulate an evaluation framework that holds candidate retrieval, target state, model, decoding, and tool budget fixed while varying the support delivered to the agent. We instantiate the framework with query-conditioned reuse (QCR), a deliberately simple target-bound note that records a reusable procedure, bindings to recover, applicability conditions, and verification requirements. QCR serves to test the reuse hypothesis rather than to claim a universally preferred memory format. Across 2,391 target instances in WebArena, WorkArena, and AppWorld, QCR reaches 62.3% average Success, 10.7 points above Full Trajectory, while using 48.9% fewer online tokens. Summary reranking selects a reusable memory for 94.8% of targets, placing end-task Success within 1.8 points of an oracle reusable selector. Analyses by trajectory length and source--target binding shift show that direct trajectory injection loses much of its utility as traces grow longer or source-specific values change, whereas target-bound support preserves a larger share of the measured gain. The resulting framework separates retrieval quality from the problem of turning retrieved experience into safe, useful support for a new task.

</details>

---

### [[20_Research/Papers/大模型/AQuA_Recursively_Self-Improving_Quantitative_Trading_Research_Agents|AQuA: Recursively Self-Improving Quantitative Trading Research Agents]]

![[assets/2608.12841_figure.png|800]]

- **arXiv**: [2608.12841](https://arxiv.org/abs/2608.12841)
- **PDF**: https://arxiv.org/pdf/2608.12841
- **详细分析**: [[20_Research/Papers/大模型/AQuA_Recursively_Self-Improving_Quantitative_Trading_Research_Agents|AQuA: Recursively Self-Improving Quantitative Trading Research Agents]]
- **作者**: Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《AQuA: Recursively Self-Improving Quantitative Trading Research Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study recursive self-improvement at the level of quantitative-investment research: whether an autonomous system can use evidence from earlier experiments to improve the hypotheses and candidates proposed in later iterations. We present AQuA, which comprises two separate language-model-driven research systems: one for symbolic factor discovery and one for trainable model development. The two systems do not share agents, memories, candidate spaces, or research state. Instead, each independently closes its own research loop by retaining validated evidence and using it to guide subsequent proposals. In this bounded sense, both systems implement recursive self-improvement at the level of the research process. Each system also uses its own sealed sandbox, which fixes the data splits, feature and label definitions, and evaluator while allowing the model to act only through constrained factor expressions or configuration diffs. The factor system, a manager-mediated multi-agent pipeline, discovers and combines factors into a signal that reaches a combined information coefficient of about $0.190$ on a crypto universe. The model system, a config-driven loop over a hybrid time-series architecture, reaches a per-stock information coefficient of $+0.0843$ on US equities and converts it into a threshold long/short strategy with a held-out Sharpe of up to $+2.50$ at a two-leg cost. The strategy is positive in every year from 2021 to 2025.

</details>

---

### [[20_Research/Papers/大模型/CRAFT_LLM-Based_Iterative_Refinement_for_Temporal_Reasoning_over_Clinical_Narratives|CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives]]

![[assets/2608.12779_figure.png|800]]

- **arXiv**: [2608.12779](https://arxiv.org/abs/2608.12779)
- **PDF**: https://arxiv.org/pdf/2608.12779
- **详细分析**: [[20_Research/Papers/大模型/CRAFT_LLM-Based_Iterative_Refinement_for_Temporal_Reasoning_over_Clinical_Narratives|CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives]]
- **作者**: Chengyang He, Tahreem Arif, Marko Zivkovic, Lijing Wang, Yue Ning, Ping Wang
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TempEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding the temporal progression of symptoms in clinical narratives is critical for disease monitoring, safety surveillance, and causality assessment. Clinical narratives, however, rarely provide explicit temporal anchors. Current approaches to temporal information reasoning focus predominantly on pairwise relation classification across multi-visit and timestamp-rich records, leaving the reconstruction of structured symptom trajectories from individual anchor-sparse reports largely unaddressed. We propose CRAFT, an LLM framework that pairs a generator with a constraint-based verifier to iteratively produce and refine stage-wise symptom timelines through targeted feedback. We conduct evaluation on MedTempo, a new benchmark of 5,347 vaccine adverse-event narratives spanning three COVID-19 vaccine types, with expert-validated temporal stage annotations for 3,166 reports. Experiments across four LLM backbones demonstrate that CRAFT consistently improves temporal ordering accuracy, with ablation analysis isolating the contribution of generator and verifier components across model capability levels.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Outcome_Rewards_Step-Level_Self-Distilled_Policy_Optimization_for_Deep_Search_Agents|Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents]]

![[assets/2608.12764_figure.png|800]]

- **arXiv**: [2608.12764](https://arxiv.org/abs/2608.12764)
- **PDF**: https://arxiv.org/pdf/2608.12764
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Outcome_Rewards_Step-Level_Self-Distilled_Policy_Optimization_for_Deep_Search_Agents|Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents]]
- **作者**: Haoze Wu, Chuqiao Kuang, Tianyi Zhuang, Xiaoguang Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Beyond Outcome Rewards: Step-Level Self-Distilled Policy Optimization for Deep Search Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep search agents operate over trajectories spanning dozens of steps, yet standard reinforcement learning provides only a single outcome reward per trajectory, which is far too sparse for effective credit assignment. On-policy self-distillation (OPSD) addresses this by using the model's own logits as dense token-level teachers, but extending it to search agents introduces a fundamental tension: the teacher, having access to privileged information such as the correct answer, produces a distribution that differs systematically from the student's exploration-based reasoning, and naive distillation causes the student to inherit this information asymmetry rather than learn better search strategies. We resolve this tension through two contributions. First, we construct Evidence Anchors, which are concise, step-level evidence snippets extracted from the web, as privileged information that captures key reasoning steps without revealing the entire answer path. Second, we propose Step-Level Self-Distilled Policy Optimization (SSPO), which converts teacher-student disagreement into step-level advantage weights within GRPO, applied exclusively to incorrect trajectories. This design decouples what to update from how much to update: the outcome reward determines the direction of policy change, while the teacher modulates its magnitude at each step. Correct trajectories are left untouched, preserving their diversity. On Qwen3-8B, SSPO consistently outperforms GRPO across BrowseComp, GAIA, and FRAMES, surpassing or matching GRPO trained with twice as many gradient steps while adding only about 5 percent overhead per step from a single additional forward pass.

</details>

---

### [[20_Research/Papers/大模型/SynAct_A_Reasoning-Acting_Large_Language_Model_Agent_for_Adaptive_Synthesis_Optimization|SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization]]

![[assets/2608.12751_first_page.png|800]]

- **arXiv**: [2608.12751](https://arxiv.org/abs/2608.12751)
- **PDF**: https://arxiv.org/pdf/2608.12751
- **详细分析**: [[20_Research/Papers/大模型/SynAct_A_Reasoning-Acting_Large_Language_Model_Agent_for_Adaptive_Synthesis_Optimization|SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization]]
- **作者**: Fangzhou Liu, Peiyi Han, Jiawei Liu, Yuan Pu, Zhuolun He, Rongliang Fu, Tsung-Yi Ho, Bei Yu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Logic synthesis transforms RTL designs into gate-level netlists, where PPA results are highly sensitive to the choice of optimization commands, making synthesis tuning both high-dimensional and expensive. Previous approaches fall into two categories: automated methods, which perform black-box search over fixed action spaces with limited decision-level interpretability, and LLM-based methods, which typically generate static scripts upfront and cannot adapt to evolving circuit states. We present SynAct, an adaptive closed-loop LLM reasoning--acting agent that iteratively diagnoses live synthesis reports and reasons over the current circuit state, retrieved tool knowledge, and historical optimization experience to issue targeted commands. SynAct focuses on improving timing, particularly worst negative slack (WNS), while maintaining balanced area and power trade-offs. Experiments on a commercial synthesis tool across 14 designs show that SynAct reduces average WNS to 27% of that from bootstrap synthesis.

</details>

---

### [[20_Research/Papers/具身智能/Spatial_Memory_Agent_Experience-Grounded_Procedure_Memory_for_Spatial_Intelligence|Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence]]

![[assets/2608.12743_figure.png|800]]

- **arXiv**: [2608.12743](https://arxiv.org/abs/2608.12743)
- **PDF**: https://arxiv.org/pdf/2608.12743
- **详细分析**: [[20_Research/Papers/具身智能/Spatial_Memory_Agent_Experience-Grounded_Procedure_Memory_for_Spatial_Intelligence|Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence]]
- **作者**: Haokai Zhang, Yuhang Ding, Yunshu Zhou, Xinze Du, Shengtao Zhang, Zhiyue Zhao, Yuling Xi, Hao Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 强化学习, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.7，强化学习 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence》归入 大模型、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ERQA, MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants. To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines. One line uses post-training methods, such as supervised fine-tuning and reinforcement learning. Another line adopts an agentic paradigm in which the model calls external spatial tools, such as depth estimation and 3D reconstruction tools, to gather intermediate spatial evidence. We study a complementary and underexplored route: Can a frozen VLM agent improve its spatial reasoning through \textbf{parameter-update-free self-evolution}, without depending on external expert spatial tools at inference time? We present \textbf{Spatial Memory Agent (SMA)}, an \textbf{experience-grounded runtime framework} that converts verified spatial experience into reusable transferable lessons. In a verifiable spatial environment, SMA queries the frozen VLM, obtains a predicted answer and reward, and uses \textbf{verifier-guided reflection} to distill compact transferable lessons from spatial experience. SMA further assigns each lesson a \textbf{Transfer Reliability Score (TRS)}, which is initialized uniformly and calibrated from later retrieval outcomes as visit evidence of future transfer reliability. During \textbf{read-only deployment}, SMA retrieves lessons by semantic filter and similarity-TRS combined ranking, allowing the retrieved memory to guide frozen model inference. Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free path for spatial self-evolution across the evaluated frozen model scales and environments.

</details>

---

### [[20_Research/Papers/大模型/ERSkill_Evolving_for_Skill-Guided_Adaptive_Memory_Retrieval|ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval]]

![[assets/2608.12720_figure.png|800]]

- **arXiv**: [2608.12720](https://arxiv.org/abs/2608.12720)
- **PDF**: https://arxiv.org/pdf/2608.12720
- **详细分析**: [[20_Research/Papers/大模型/ERSkill_Evolving_for_Skill-Guided_Adaptive_Memory_Retrieval|ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval]]
- **作者**: Haolong Chen, Liang Zhang, Zhuo Li, Lei Xue, Guanrxu Zhu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongMemEval, PerLTQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Model (LLM) agents increasingly rely on long-term memory for persistent interactions, the retrieval mechanisms governing this memory are rarely treated as evolvable components. This static approach limits performance on heterogeneous memory queries, which often demand diverse evidence construction strategies. To address this, we introduce \textbf{ERSkill}, a retrieval-centric framework for self-evolving, skill-guided memory access. ERSkill compiles interaction histories into a structured memory store and represents retrieval behaviors as executable skills composed of fundamental primitives. At inference time, a trained router dynamically matches each query to the optimal skill to construct tailored evidence for answer generation. To enable continuous improvement, ERSkill co-evolves the skill set and the router during training. It employs an experience trie to efficiently record explored retrieval paths, alongside a double-frontier mechanism that safely decouples the expansion of new skill capabilities from stable, router-facing deployment. Experiments across multiple agent memory benchmarks demonstrate that ERSkill substantially outperforms strong non-evolving and self-evolving baselines. Notably, it improves the overall average across F1, BLEU-1, and LLM-judge scores by 31.3\% with Qwen3-Next-80B-A3B-Instruct and by 28.1\% with GPT-5.4-nano.

</details>

---

### [[20_Research/Papers/大模型/Error-Aware_Reverse_Auction_Mechanism_for_Large_Language_Model_Routing|Error-Aware Reverse Auction Mechanism for Large Language Model Routing]]

![[assets/2608.12719_figure.png|800]]

- **arXiv**: [2608.12719](https://arxiv.org/abs/2608.12719)
- **PDF**: https://arxiv.org/pdf/2608.12719
- **详细分析**: [[20_Research/Papers/大模型/Error-Aware_Reverse_Auction_Mechanism_for_Large_Language_Model_Routing|Error-Aware Reverse Auction Mechanism for Large Language Model Routing]]
- **作者**: Haolong Chen, Zhengyuan Xin, Liang Zhang, Lei Xue, Guangxu Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Error-Aware Reverse Auction Mechanism for Large Language Model Routing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, RouterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Routing each query to a cost-effective large language model (LLM) is critical for balancing quality and cost, yet most routers rely on a centralized task center to predict model performance, creating an information-risk mismatch and a scalability bottleneck as the model pool grows. We propose a market-based routing paradigm that shifts ex-ante prediction to LLM providers via a reverse auction, where providers bid with self-predicted success probabilities and execution costs. To account for inherently noisy provider predictions and center evaluations, we introduce the \textit{\textbf{E}rror-\textbf{A}ware \textbf{R}everse \textbf{A}uction \textbf{M}echanism} (EA-RAM), which explicitly models this inherent Dual Error. We prove that EA-RAM is Bayesian incentive compatible and individually rational under the Dual Error, establish sufficient conditions for center rationality, and derive an explicit welfare-loss bound. We further identify robustness effects: opposite-signed errors can cancel, vanishing-tail link functions (e.g., logistic) stabilize clear-cut cases via saturation, and extra noise smooths belief maps, reducing the gains from marginal manipulation. Experiments on simulations and real-world benchmarks show that EA-RAM is robust to the Dual Error and achieves a better cost--performance Pareto frontier than centralized baselines, with additional gains when providers contribute local information, validating its practical effectiveness.

</details>

---

### [[20_Research/Papers/大模型/Tracing_Provenance_and_Detecting_Tampering_with_Complementary_LLM_Watermarks|Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks]]

![[assets/2608.12713_figure.png|800]]

- **arXiv**: [2608.12713](https://arxiv.org/abs/2608.12713)
- **PDF**: https://arxiv.org/pdf/2608.12713
- **详细分析**: [[20_Research/Papers/大模型/Tracing_Provenance_and_Detecting_Tampering_with_Complementary_LLM_Watermarks|Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks]]
- **作者**: Xiaoyan Feng, Yanjun Zhang, He Zhang, Leo Yu Zhang, Shirui Pan
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Watermarking LLM-generated text is an important task for tracing its provenance. Existing LLM watermarks preserve provenance under editing, but this same robustness allows an adversary to alter critical content while retaining attribution, a vulnerability known as piggyback spoofing. We introduce an innovative watermark that jointly provides provenance and tamper evidence. It co-embeds a robust signal and a fragile signal into each generated token. The signals share the same mechanism but use independent keys and different seeding windows over normalized text, making one resilient to edits and the other sensitive to reader-visible changes. Multiple rounds of unbiased tournament reweighting preserve the expected generation distribution, while a periodic round-allocation pattern controls the trade-off between the two signals. At detection, their scores form a two-dimensional space supporting three decisions: Intact, Tampered, and No-Watermark. Across two large language models and two prompt datasets, our method demonstrates the highest tamper-detection rate among the evaluated methods while maintaining competitive attribution robustness and perplexity. Ablation studies show that reliable three-state detection requires a well-defined notion of intactness, co-embedding of the two signals, and complementary sensitivity to edits.

</details>

---

### [[20_Research/Papers/大模型/Lines_and_Ladders_A_Context-Aware_Multi-Agent_Framework_for_Large-Scale_Retail_Price_Taxonomy|Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Price Taxonomy]]

![[assets/2608.12674_figure.png|800]]

- **arXiv**: [2608.12674](https://arxiv.org/abs/2608.12674)
- **PDF**: https://arxiv.org/pdf/2608.12674
- **详细分析**: [[20_Research/Papers/大模型/Lines_and_Ladders_A_Context-Aware_Multi-Agent_Framework_for_Large-Scale_Retail_Price_Taxonomy|Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Price Taxonomy]]
- **作者**: Ravi Teja Chunduri, Srikaran Reddy Boya, Deep Narayan Mishra, Ajay Kumar B, Karthik Kumaran, Pranay Kona
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Price Taxonomy》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maintaining price consistency and executing an Every Day Low Price strategy is critical for global retailers. However, with catalogs spanning millions of active items, manual governance of price relationships is infeasible. Inconsistent pricing across item variants distorts customer value perception and cannibalizes sales. To address this, we present a scalable, context-aware Multi-Agent Framework designed to automate the construction of "Lines and Ladders" pricing taxonomies. Our framework employs specialized LLM agents to construct these coherent pricing structures by identifying key attributes, extracting multi-modal values, and applying hierarchical grouping logic. Evaluated on real-world enterprise data and deployed in production, our 3-Agent system achieves an F1-score of 0.83 for Lines, outperforming single-agent baselines by mitigating cognitive overload. The system achieves &gt;90% precision and &gt;75% recall in Food &amp; Consumables, and 80.2% assignment accuracy in the unstructured General Merchandise catalog.

</details>

---

### [[20_Research/Papers/大模型/SteerBench-Work_A_Benchmark_for_Agent_Steering_at_Action_Boundaries|SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries]]

![[assets/2608.12654_figure.png|800]]

- **arXiv**: [2608.12654](https://arxiv.org/abs/2608.12654)
- **PDF**: https://arxiv.org/pdf/2608.12654
- **详细分析**: [[20_Research/Papers/大模型/SteerBench-Work_A_Benchmark_for_Agent_Steering_at_Action_Boundaries|SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries]]
- **作者**: Oguz Serdar, Cuneyt Mertayak
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, AmPermBench, AskBench, ClarifyBench, HarmBench, HiL-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-running LLM agents act through tools, and a single step can send an email, merge a pull request, or wire a payment. The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review. We introduce SteerBench-Work, an incident-anchored, bidirectional benchmark for that decision in workplace agents across developer operations, customer service, finance, legal, medical, HR, and security. Release v2026-05 contains 106 scenarios anchored in public incidents, paired evidence-reversed mirrors, and calibration controls, with labels split nearly evenly between proceed and hold so the two error directions get near-identical numbers of chances. A model sees the proposed action and the available evidence, returns a gate decision, and is scored on whether it crosses or holds the boundary correctly. Across 30 model conditions the failures run almost entirely in one direction: models wrongly hold authorized, evidence-cleared work on 28.1% of opportunities and wrongly allow unsafe work on 1.0%. The hardest cases are risk-resolved commits, where signed or structured evidence has already cleared a real risk trigger, and models score markedly worse on evidence-reversed mirrors of famous incidents (63.8%) than on the incidents themselves (98.5%). General capability is not the same as steering calibration: higher-capability models often over-refuse at the commit boundary, and more reasoning can repair a weak gate while leaving a calibrated one flat. The public leaderboard is at steerbench.com.

</details>

---

### [[20_Research/Papers/大模型/Governed_Persistent_Memory_Source-Bound_State_Semantics_and_Fail-Closed_Release_for_Long-Horizon_Agents|Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents]]

![[assets/2608.12476_first_page.png|800]]

- **arXiv**: [2608.12476](https://arxiv.org/abs/2608.12476)
- **PDF**: https://arxiv.org/pdf/2608.12476
- **详细分析**: [[20_Research/Papers/大模型/Governed_Persistent_Memory_Source-Bound_State_Semantics_and_Fail-Closed_Release_for_Long-Horizon_Agents|Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents]]
- **作者**: Guodong Xu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 0.9（加权：大模型 0.5，世界模型 0.4）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GPM-ReleaseBench, LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-revival after retraction or deletion, and exact claim closure over a fresh view at one verified head. On a prespecified hash-frozen 3,600-case GPM-ReleaseBench, GPM matches all complete outcomes; the strongest of three intentionally simple complete policies matches 1,800/3,600 and makes unmatched releases on 50% of violation cases. A separate sealed end-to-end service evaluation exercises real ingestion and release across eight query families. In its publicly disclosed V3 arm, the governed lane is correct on 2,400/2,400 clusters versus 600/2,400 for ungoverned local Qwen2.5-7B; it repairs all 1,800 baseline failures with no regression (one-sided 95% lower bounds 99.875% and 99.834%). A later V5 reseal over Chinese- and English-command arms, with generation-date pinning and no post-freeze reducer amendment, again obtains 2,400/2,400 per arm. A production-code-independent finite model explores 331,776 semantic and 1,990,656 query states without a full-contract counterexample, and a 100,000-trace three-engine differential yields zero mismatches. These are bounded contract and implementation results, not open-world model accuracy or evidence of world truth. Governed answers in the sealed service evaluation are deterministic service outputs; the 7B result is the ungoverned comparison, not a claim that a language model itself became perfectly accurate.

</details>

---

### [[20_Research/Papers/大模型/Multi-Agent_Scheduling_with_LLM-Assisted_Contract_Net_Negotiation_for_Stream_Processing_in_Mobile_Edge_Computing|Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing]]

![[assets/2608.12371_figure.png|800]]

- **arXiv**: [2608.12371](https://arxiv.org/abs/2608.12371)
- **PDF**: https://arxiv.org/pdf/2608.12371
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_Scheduling_with_LLM-Assisted_Contract_Net_Negotiation_for_Stream_Processing_in_Mobile_Edge_Computing|Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing]]
- **作者**: Sabeur Lajili, Zaki Brahmi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Multi-Agent Scheduling with LLM-Assisted Contract Net Negotiation for Stream Processing in Mobile Edge Computing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stream-processing systems increasingly operate across heterogeneous mobile edge--cloud infrastructures, where workload volatility, resource contention, and stringent quality-of-service (QoS) requirements complicate decentralized scheduling. This paper proposes \emph{MAS-DecStream}, whose main contribution is \emph{LLM-MR-CNP}: an extension of the classical Contract Net Protocol with semantic CFP formulation, progressive context disclosure, multi-round proposal revision, negotiation memory, and deterministic validation. Edge-cluster agents refine natural-language offloading proposals from local observations, predicted resource states, and qualitative runtime context, while hard resource and QoS constraints remain deterministic. Experiments derived from the Alibaba ASI Trace evaluate the extension at three levels: single- versus multi-round CNP, rule-based versus LLM-assisted refinement, and fixed-model single- versus multi-round negotiation. Under the evaluated configurations, MAS-DecStream reduces latency violations to 3\%, eliminates resource overcommitment, reaches a conflict-resolution rate of 0.91 with 20 agents, and improves utility by up to 22\% over the multi-round rule-based baseline. A separate 25-case evaluation shows model- and prompt-dependent accuracy--cost trade-offs. The results provide initial evidence that multi-round CNP refinement is the principal protocol-level gain, with LLM assistance adding value for qualitative and uncertain runtime context.

</details>

---

### [[20_Research/Papers/强化学习/EU-ETS_under_attack_The_impact_of_carbon_price_suppression_on_the_decarbonization_of_the_power_sector|EU-ETS under attack? The impact of carbon price suppression on the decarbonization of the power sector]]

![[assets/2608.12363_figure.png|800]]

- **arXiv**: [2608.12363](https://arxiv.org/abs/2608.12363)
- **PDF**: https://arxiv.org/pdf/2608.12363
- **详细分析**: [[20_Research/Papers/强化学习/EU-ETS_under_attack_The_impact_of_carbon_price_suppression_on_the_decarbonization_of_the_power_sector|EU-ETS under attack? The impact of carbon price suppression on the decarbonization of the power sector]]
- **作者**: Javier Gonzalez-Ruiz, Carlos Rodriguez-Pardo, Alice Di Bella, Paolo Mastropietro, Jose Pablo Chavez-Avila, Massimo Tavoni
- **cs 子类**: cs.AI, cs.CY, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《EU-ETS under attack? The impact of carbon price suppression on the decarbonization of the power sector》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

European countries are debating policies to mitigate the increased energy costs caused by renewed geopolitical tensions, while pursuing decarbonization and electrification. A notable example is Italy's 2026 Decreto Bollette package, which proposes to remove the carbon price equivalent from the bids of certain gas-driven power plants to wholesale electricity markets, among other provisions. We use this as a case study to assess the long-term implications of suppressing the carbon price signal in the electricity market for investment, emissions, and consumer costs. We employ a stylized Italian power system using MARLEY, a multi-agent reinforcement learning framework focused on long-term electricity market assessments. In this framework, we test this policy across configurations with varying levels of support for green investment, resource adequacy, and flexibility. Results show that partial suppression of the carbon price signal yields short-term cost reductions but only a minor long-term effect on total system costs, as the deferred emissions are ultimately repaid by consumers. CO$_2$ emissions rise across most configurations since suppressing the price signal erodes incentives for renewable and storage investment. Only the most ambitious configurations for supporting green investment avoid this outcome, but they do so by marginalizing the wholesale price signal itself, thereby requiring a commitment to a hybrid market paradigm that is in contradiction with the rationale of the proposed price intervention.

</details>

---

### [[20_Research/Papers/大模型/What_Drives_LLM_Self-Reflection_A_Controlled_Ablation_of_Uncertainty_Routing_in_Armed_Conflict_Forecasting|What Drives LLM Self-Reflection? A Controlled Ablation of Uncertainty Routing in Armed Conflict Forecasting]]

![[assets/2608.12322_first_page.png|800]]

- **arXiv**: [2608.12322](https://arxiv.org/abs/2608.12322)
- **PDF**: https://arxiv.org/pdf/2608.12322
- **详细分析**: [[20_Research/Papers/大模型/What_Drives_LLM_Self-Reflection_A_Controlled_Ablation_of_Uncertainty_Routing_in_Armed_Conflict_Forecasting|What Drives LLM Self-Reflection? A Controlled Ablation of Uncertainty Routing in Armed Conflict Forecasting]]
- **作者**: Poli Nemkova, Haeshitha Indukuri
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《What Drives LLM Self-Reflection? A Controlled Ablation of Uncertainty Routing in Armed Conflict Forecasting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-reflection is widely assumed to improve LLM reasoning, yet which component drives the gain remains poorly understood. We present a controlled six-condition ablation isolating four components of LLM self-reflection: evidence exposure, diagnostic scaffolding, taxonomy vocabulary, and action routing. Two precise null results converge on a single mechanism. First, structured diagnostic questions add no measurable value over unstructured reflection ($\text{F1} = 0.296$ vs $0.297$, $p = 1.000$, 95\% CI $[-0.041, +0.040]$). Second, presenting the full uncertainty taxonomy while collapsing the action space to a single generic action also adds no value ($Δ\text{F1} = +0.008$, overlapping 95\% CIs), ruling out taxonomy vocabulary as the mechanism. Typed action routing provides consistent directional gains ($\text{F1} = 0.379$ vs $0.296$); the conservative estimate controlling for taxonomy vocabulary is $Δ\text{F1} = +0.075$, and the overall gain over the single-shot baseline is significant by bootstrap CI ($Δ\text{F1} = +0.101$, 95\% CI $[+0.020, +0.185]$). The vocabulary-routing decomposition replicates on GPT-4o: taxonomy vocabulary adds no significant value over generic reflection ($p = 0.773$), while action routing provides significant gains ($p = 0.025$), confirming the mechanism holds across backbones. Gains concentrate on structurally novel conflicts: in Myanmar ($\text{F1}: 0.000 \rightarrow 0.353$) and Ukraine ($0.167 \rightarrow 0.500$), the vocabulary-only condition recovers no more than generic reflection while action routing breaks the degenerate prior. These findings identify typed action routing -- not diagnostic scaffolding or taxonomy vocabulary -- as a promising design principle for metacognitive LLM forecasting agents, while motivating larger-scale evaluation across conflict typologies.

</details>

---
