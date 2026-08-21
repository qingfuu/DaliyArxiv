# cs.CV | Computer Vision and Pattern Recognition | 2026-08-19

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/具身智能/Plug-and-Play_Traffic_Element_Awareness_for_End-to-End_Autonomous_Driving|Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving]]

![[assets/2608.18035_figure.png|800]]

- **arXiv**: [2608.18035](https://arxiv.org/abs/2608.18035)
- **PDF**: https://arxiv.org/pdf/2608.18035
- **详细分析**: [[20_Research/Papers/具身智能/Plug-and-Play_Traffic_Element_Awareness_for_End-to-End_Autonomous_Driving|Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving]]
- **作者**: Zongzheng Zhang, Jijun Wang, Saining Zhang, Shuo Wang, Yiru Wang, Hai Yang, Yang Chen, Yuwen Heng, Hao Sun, Anqing Jiang, Hao Zhao
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.6（加权：具身智能 0.6）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end driving research predominantly focuses on dynamic road participants (e.g., vehicles and pedestrians), while the role of traffic elements remains largely unexplored. The community still lacks a systematic study quantifying their impact, largely because public datasets rarely provide structured traffic-element annotations and modern driving systems vary widely in architecture and training paradigm. In this work, we present the first systematic investigation of traffic element awareness for end-to-end autonomous driving. We construct a unified research infrastructure by augmenting multiple public driving datasets with comprehensive traffic-element annotations. To support diverse model families, we adopt a minimal and universal integration design that incorporates traffic-element signals into existing pipelines in a plug-and-play manner with negligible architectural modification. We evaluate this design across modern paradigms, including perception-prediction-planning pipelines, vision-language-action models (VLA), regression-based planners, diffusion-based policies, and trajectory-scoring frameworks, on nuScenes, NAVSIM-v1, NAVSIM-v2, and Bench2Drive. Across all paradigms and datasets, this simple integration consistently improves driving performance, demonstrating that traffic element awareness provides a robust and generalizable signal for end-to-end driving systems. Notably, on the challenging NAVSIM-v2 benchmark, our approach significantly improves state-of-the-art architectures and data pipelines, establishing a new state of the art.

</details>

---

### [[20_Research/Papers/具身智能/Memory_Tree_Guided_Key_Frame_Querying_for_Efficient_3D_Question_Answering|Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering]]

![[assets/2608.18009_figure.png|800]]

- **arXiv**: [2608.18009](https://arxiv.org/abs/2608.18009)
- **PDF**: https://arxiv.org/pdf/2608.18009
- **详细分析**: [[20_Research/Papers/具身智能/Memory_Tree_Guided_Key_Frame_Querying_for_Efficient_3D_Question_Answering|Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering]]
- **作者**: Hsiang-Wei Huang, Fu-Chen Chen, Li-Wu Tsao, Cheng-Han Lee, Che-Chun Su, Lu Xia, Ronghui Peng, Jenq-Neng Hwang, Min Sun, Cheng-Hao Kuo
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.4）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering》归入 大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenEQA, ScanQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Answering questions accurately and efficiently in embodied scenarios presents significant challenges due to limited computational and memory resources for Vision Language Model (VLM) inference. Existing methods adopt visual search key frame retrieval method to select critical question-related key frames for VLM input. However, visual search methods are inefficient because they require visual search among thousands of video frames for each individual user query. In this work, we propose a memory tree guided key frame selection paradigm for efficient 3D question answering in embodied scenarios. Our method leverages a compact and reusable 3D scene representation, termed MemTree3D, which supports real-time online construction leveraging camera 6-DoF poses. MemTree3D captures multi-level 3D scene information, enabling a Large Language Model to efficiently query and retrieve question-relevant key frames through our scoring-based frame selection without reprocessing the entire video stream. On OpenEQA, our method improves the LLM-Match of GPT-4o by 17.4%, LLaVA-OneVision-7B by 5.8%, outperforms existing visual search methods. Our code is available at https://github.com/hsiangwei0903/MemTree3D

</details>

---

### [[20_Research/Papers/大模型/aDSL_Agentic_3D_Creation_via_Joint_Agent-Program_Design|aDSL: Agentic 3D Creation via Joint Agent-Program Design]]

![[assets/2608.17975_figure.png|800]]

- **arXiv**: [2608.17975](https://arxiv.org/abs/2608.17975)
- **PDF**: https://arxiv.org/pdf/2608.17975
- **详细分析**: [[20_Research/Papers/大模型/aDSL_Agentic_3D_Creation_via_Joint_Agent-Program_Design|aDSL: Agentic 3D Creation via Joint Agent-Program Design]]
- **作者**: Rui-Huan Wang, Si-Tong Wei, Jia-Qi He, Heng-Yi Wei, Baoquan Chen, Peng-Shuai Wang
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《aDSL: Agentic 3D Creation via Joint Agent-Program Design》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Programmatic representations provide a compelling paradigm for 3D content creation, enabling fine-grained edits, interpretability, and explicit structural control. Yet, agentic workflows that rely on large language models (LLMs) to author 3D programs remain brittle, often failing to translate high-level intent into consistent low-level geometry. We attribute this fragility to a mismatch between existing programmatic interfaces and the reasoning strengths of LLMs, which favor semantic structure and spatial relations over fragile numeric choices. In this paper, we jointly design an Agent-centric Domain-Specific Language (aDSL) and a role-specialized multi-agent system to close this gap. aDSL bridges semantic logic and geometric constraints by emphasizing composability and spatial reasoning; it enables agents to manipulate geometry through relational operators instead of brittle absolute coordinates. Building on aDSL, our training-free multi-agent system follows a Plan-Execute-Critic loop to decompose requests, synthesize code, and iteratively repair errors and constraint violations using execution feedback. Experiments show that this co-design improves robustness, controllability, and faithfulness to user intent. Our method outperforms prior LLM-based baselines on text-to-shape and image-to-shape tasks while preserving explicit structure, editability, and interpretability. It also enables downstream applications such as articulated object creation and structured scene composition. Our code is available at https://github.com/sig-pku/aDSL.

</details>

---

### [[20_Research/Papers/具身智能/GroupForward_Building_Referable_3D_Scenes_via_Instance-Grouped_Feed-Forward_Gaussian_Splatting|GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting]]

![[assets/2608.17535_figure.png|800]]

- **arXiv**: [2608.17535](https://arxiv.org/abs/2608.17535)
- **PDF**: https://arxiv.org/pdf/2608.17535
- **详细分析**: [[20_Research/Papers/具身智能/GroupForward_Building_Referable_3D_Scenes_via_Instance-Grouped_Feed-Forward_Gaussian_Splatting|GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting]]
- **作者**: Qijian Tian, Zimeng Wu, Xuhong Wang, Lizhuang Ma, Xin Tan
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.6（加权：具身智能 0.3，大模型 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting》归入 大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phrase-based semantic queries. To this end, we propose GroupForward, an instance-grouped feed-forward Gaussian splatting model that reconstructs geometry, appearance, instance structure, and semantics from sparse, unposed, and uncalibrated multi-view images. Unlike existing methods that attach high-dimensional semantic features to each Gaussian, GroupForward learns compact instance embeddings that group Gaussians into cross-view consistent 3D instances, reformulating feed-forward semantic 3DGS from per-Gaussian semantic feature rendering to instance-level semantic aggregation and propagation. Building on these instance groups, we further propose a Referential Scene Reasoning Framework (RSRF) for complex 3D referring segmentation. RSRF constructs an instance-grouped 3D scene graph and retrieves candidate instances for a given referring expression. A vision-language model then reasons over structured instance evidence and multi-view observations to identify the referred instance among the candidates. RSRF thereby extends language interaction from simple semantic querying to complex referential scene reasoning. Experiments on semantic reconstruction and referential reasoning demonstrate the effectiveness of our instance-grouped reconstruction and reasoning framework.

</details>

---

### [[20_Research/Papers/具身智能/If,_Then,_Otherwise_Diagnosing_Conditional_Branching_in_Vision-Language_Navigation|If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation]]

![[assets/2608.17318_figure.png|800]]

- **arXiv**: [2608.17318](https://arxiv.org/abs/2608.17318)
- **PDF**: https://arxiv.org/pdf/2608.17318
- **详细分析**: [[20_Research/Papers/具身智能/If,_Then,_Otherwise_Diagnosing_Conditional_Branching_in_Vision-Language_Navigation|If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation]]
- **作者**: Seoyoung Lee, Neel P. Bhatt, Pranay Samineni, Cong Liu, S P Sharan, Timothy Barclay, Gregory M. Wagner, Daniel Milan, Sandeep Chinchali, Ufuk Topcu, Atlas Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《If, Then, Otherwise: Diagnosing Conditional Branching in Vision-Language Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoNavBench, OmniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language navigation agents are often evaluated on their ability to follow route-like instructions toward a fixed goal. Yet, real navigation instructions often depend on observed states of the environment: if a condition holds, then follow one path, otherwise take another. Such instructions require an agent to evaluate scene evidence, select the correct logical branch, and execute the corresponding navigation behavior. Existing evaluations provide limited control over conditional branch execution, making it difficult to determine whether agents fail because of perception, grounding, navigation, or logical decision-making. We introduce CondVLN, a scene-graph-grounded benchmark for diagnosing conditional branching in vision-language navigation. CondVLN programmatically generates instructions whose branch conditions are grounded in verifiable 3D scene-graph predicates, with controlled variation in branch depth, dependency chain length, spatial composition, evidence observability, and instruction horizon. CondVLN contains over 11,500 generated conditional instructions across AI2-THOR, Matterport3D, Gibson, and ReplicaCAD, and evaluates agents using standard VLN metrics and branch-specific diagnostics: Branch Selection Accuracy and Conditional Success Rate. Evaluating four state-of-the-art VLN agents (VLN-Zero, NaVid, NaVILA, and Open-Nav) shows that conditional branching exposes failures that are not captured by standard success rate or path length alone: agents can navigate plausibly while committing to a branch inconsistent with the observed scene condition. We also present a lightweight neurosymbolic branch-selection model that separates condition grounding from navigation execution, improving performance by 2x. CondVLN provides a reusable testbed for measuring whether embodied agents can not only follow instructions, but follow the right instruction under the right condition.

</details>

---

### [[20_Research/Papers/具身智能/PROBE_Manipulation-Grounded_Visual_Question_Answering_with_VLM_Agents|PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents]]

![[assets/2608.17129_figure.png|800]]

- **arXiv**: [2608.17129](https://arxiv.org/abs/2608.17129)
- **PDF**: https://arxiv.org/pdf/2608.17129
- **详细分析**: [[20_Research/Papers/具身智能/PROBE_Manipulation-Grounded_Visual_Question_Answering_with_VLM_Agents|PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents]]
- **作者**: Vineet Bhat, Siyi Chen, Alex Zook, Xuning Yang, Stan Birchfield, Valts Blukis, Jonathan Tremblay
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 0.9，大模型 1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PROBE: Manipulation-Grounded Visual Question Answering with VLM Agents》归入 大模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ESIBench, MG-VQA, MQA, PROBE-Bench, PROBE-Sim, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language Models (VLMs) excel at 2D grounding, spatial reasoning and agentic tool-based planning in static scenes. However, consider asking a home robot "Is my medication still in the cabinet?" The answer may be physically hidden behind a row of containers that must first be moved aside. Answering such questions in real-world cluttered environments requires reasoning in dynamic scenes: distractors must be manipulated to reveal occluded objects, and each action changes the scene the model must reason over. We formalize this setting as Manipulation-Grounded Visual Question Answering (MG-VQA) and introduce PROBE, a framework for benchmarking and finetuning VLM agents on such tasks. We first develop PROBE-Sim, a high-fidelity tabletop simulator with everyday objects and a robot manipulator equipped with grasping and pushing tools. PROBE-Sim is used to create PROBE-Bench: an evaluation suite of 150 tasks across 6 question types on cluttered tabletop scenes, where a VLM perceives, picks up or pushes objects before answering. We observe consistent trend across all frontier VLMs: agentic tool-based methods outperform their perception-only baselines (8.0% on average) across all task types. We further design PROBE-Agent, a finetuning recipe to distill successful trajectories from a powerful teacher foundation model to a smaller open-weight model using a mixed data recipe that encourages manipulation-efficient question answering. PROBE Agent finetuned models outperform their off-the-shelf agent baseline (11.5% on average) and demonstrate positive transfer to unseen objects and a held-out task. We validate sim-to-real transfer by deploying PROBE-Agent finetuned policies in real-world tabletop environments.

</details>

---

### [[20_Research/Papers/具身智能/Inference-Time_Attention_Steering_for_Vision-Language-Action_Driving_Models|Inference-Time Attention Steering for Vision-Language-Action Driving Models]]

![[assets/2608.17095_figure.png|800]]

- **arXiv**: [2608.17095](https://arxiv.org/abs/2608.17095)
- **PDF**: https://arxiv.org/pdf/2608.17095
- **详细分析**: [[20_Research/Papers/具身智能/Inference-Time_Attention_Steering_for_Vision-Language-Action_Driving_Models|Inference-Time Attention Steering for Vision-Language-Action Driving Models]]
- **作者**: Darshan Nagendra Prasad, Lars Ullrich, Knut Graichen
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 1.5，世界模型 0.2）
- **关联关键词**: Multimodal, WorldModel

#### 研究背景与动机

《Inference-Time Attention Steering for Vision-Language-Action Driving Models》归入 具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) driving models couple a reasoning stage with a diffusion-based trajectory decoder, but do not give a direct way to redirect attention toward safety-critical actors at inference time without retraining. We studied a bounded additive pre-softmax attention bias on the visual tokens of detector localized traffic actors on Alpamayo-R1's Qwen3-VL backbone. It is applied as a fail open forward pre-hook with no weight changes. On 50 lane-change scenarios from the Physical AI World Model Synthetic dataset. The trajectory decoder shows a monotonic dose response in the bias magnitude, separate from a paired zero bias control at every tested magnitude. It reaches $\approx 17$\,cm mean displacement with lateral shifts up to $\sim 140$\ cm at the clamp. A layer ablation places the action-relevant signal in late layers, where the effect increases with the number of hooked layers (2.0cm for the first 8 layers; 67.6cm for all 36). A per call injection audit explains why the Chain-of-Causation text never changes. The mask based bias never reaches the reasoning pathway in this serving stack, so the invariance is verified exposure, not robustness. Steered trajectories tend to shift toward the attended actor, suggesting the bias governs where the model looks rather than encoding a target behavior.

</details>

---
