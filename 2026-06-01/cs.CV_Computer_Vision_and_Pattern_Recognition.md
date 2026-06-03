# cs.CV | Computer Vision and Pattern Recognition | 2026-06-01

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/机器人/Triangle_Splatting_SLAM|Triangle Splatting SLAM]]

![[assets/2605.31419_figure.png|800]]

- **arXiv**: [2605.31419](https://arxiv.org/abs/2605.31419)
- **PDF**: https://arxiv.org/pdf/2605.31419
- **详细分析**: [[20_Research/Papers/机器人/Triangle_Splatting_SLAM|Triangle Splatting SLAM]]
- **作者**: Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Triangle Splatting SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a dense RGB-D SLAM system using differentiable triangles as the 3D map representation. While 3D Gaussian Splatting has emerged as the leading method for novel-view synthesis, triangles remain the standard primitive for traditional rendering hardware, game engines, and downstream tasks requiring explicit geometry such as simulation, collision, and editing. Recent offline methods have demonstrated that an unstructured 'triangle soup' can be optimised into a photorealistic mesh via Delaunay triangulation across a set of posed images. Building upon this insight, we present the first dense SLAM system to employ Triangle Splatting to perform both tracking and mapping through online differentiable rendering of a triangle soup. The map can be converted into a connected mesh on-the-fly via restricted Delaunay triangulation, enabling new online capabilities such as mesh deformation and collision checking. On Replica and TUM-RGBD, our system outperforms baselines on 3D geometry, matches the camera-tracking accuracy, and enables online mesh-based scene editing.

</details>

---

### [[20_Research/Papers/具身智能/LiftNav_Path_Planning_via_Semantic_Lifting_in_TSDF-Guided_Gaussian_Splatting|LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting]]

![[assets/2605.31376_figure.png|800]]

- **arXiv**: [2605.31376](https://arxiv.org/abs/2605.31376)
- **PDF**: https://arxiv.org/pdf/2605.31376
- **详细分析**: [[20_Research/Papers/具身智能/LiftNav_Path_Planning_via_Semantic_Lifting_in_TSDF-Guided_Gaussian_Splatting|LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting]]
- **作者**: Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth
- **cs 子类**: cs.CV, cs.GR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots in unknown indoor environments require both reliable collision avoidance and object-level understanding. Classical representations such as TSDF support safe planning but lack semantics, while photorealistic methods like Gaussian Splatting (GS) provide rich appearance yet suffer from soft geometry, limiting precise obstacle avoidance. We present LiftNav, a hybrid navigation framework built on GSFusion's TSDF+GS dual map, augmented with a real-time pipeline of YOLO-based detection, TSDF-based 3D lifting, and B-spline trajectory optimization. This design enables flexible semantic navigation without dense 3D embeddings. We further introduce a hinge-loss-based collision penalty that improves trajectory smoothness and safety. We evaluate our approach in a simulation using the Replica dataset. Compared against a state-of-the-art radiance field baseline we show a 100% feasibility rate and shorter trajectories.

</details>

---

### [[20_Research/Papers/具身智能/DriveMA_Driving_Vision-Language-Action_Models_with_verifiable_Meta-Actions|DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions]]

![[assets/2605.31271_figure.png|800]]

- **arXiv**: [2605.31271](https://arxiv.org/abs/2605.31271)
- **PDF**: https://arxiv.org/pdf/2605.31271
- **详细分析**: [[20_Research/Papers/具身智能/DriveMA_Driving_Vision-Language-Action_Models_with_verifiable_Meta-Actions|DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions]]
- **作者**: Weicheng Zheng, Yixin Huang, Qiao Sun, Derun Li, Hang Zhao
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习
- **相关性评分**: 1.7（加权：具身智能 1.5，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions》归入 具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA, LinkVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Driving Vision-Language-Action Models (Driving VLAs) aim to use language to improve end-to-end planning, but the language-action gap limits this promise. We propose DriveMA, a Driving VLA framework built on verifiable meta-actions, which summarize future ego motion into compact language-domain intentions and can be constructed from expert trajectories with a trajectory-grounded annotation pipeline and can be verified against generated trajectories through rule-based projection. DriveMA exploits this verifiability with action-centric supervised training and a data-efficient turn-level credit assignment reinforcement learning framework, explicitly aligning high-level decisions with low-level trajectory planning through dense rewards and precise credit assignment. DriveMA sets a new state of the art on the Waymo Open Dataset Vision-based E2E Driving, achieving a Rater Feedback Score of 8.060 with a 2B model and further improving it to 8.079 with a 4B model; it also obtains competitive closed-loop planning performance on NAVSIM. These results show that even a simple meta-action interface can achieve state-of-the-art planning when made verifiable and optimized for language-action alignment. Code, data, and models will be released to facilitate future research.

</details>

---

### [[20_Research/Papers/具身智能/Light_Interaction_Training-Free_Inference_Acceleration_for_Interactive_Video_World_Models|Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models]]

![[assets/2605.31158_figure.png|800]]

- **arXiv**: [2605.31158](https://arxiv.org/abs/2605.31158)
- **PDF**: https://arxiv.org/pdf/2605.31158
- **详细分析**: [[20_Research/Papers/具身智能/Light_Interaction_Training-Free_Inference_Acceleration_for_Interactive_Video_World_Models|Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models]]
- **作者**: Jiacheng Lu, Haoyi Zhu, Sipei Yi, Enze Xie, Yu Li, Cheng Zhuo
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.6，强化学习 0.16，世界模型 1.16）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models》归入 世界模型、具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training. However, scaling to long interactive trajectories is prohibitively expensive due to growing context memory, quadratic attention complexity, and repeated denoising steps. We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Our key insight is that interaction naturally enables trajectory-dependent adaptive computation: retrieved spatial memory can be discarded during novel exploration, temporal context can be adjusted according to local latent dynamics, and early-step model outputs can be reused when the camera revisits familiar regions. Based on this insight, Light Interaction combines adaptive context management, denoising cache acceleration, and hardware-software co-designed 3D block sparse attention with fused Triton kernels. Evaluated on HY-WorldPlay and Matrix-Game-3.0, Light Interaction achieves up to 2.59x speedup without model retraining while maintaining competitive visual quality.

</details>

---

### [[20_Research/Papers/大模型/iVGR_Internalizing_Visually_Grounded_Reasoning_for_MLLMs_with_Reinforcement_Learning|iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning]]

![[assets/2605.31096_figure.png|800]]

- **arXiv**: [2605.31096](https://arxiv.org/abs/2605.31096)
- **PDF**: https://arxiv.org/pdf/2605.31096
- **详细分析**: [[20_Research/Papers/大模型/iVGR_Internalizing_Visually_Grounded_Reasoning_for_MLLMs_with_Reinforcement_Learning|iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning]]
- **作者**: Chang-Bin Zhang, Yujie Zhong, Qiang Zhang, Kai Han
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CV-Bench, RealWorldQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While visually grounded Chain-of-Thought (CoT) has emerged as a promising paradigm to enhance fine-grained perception in multimodal large language models (MLLMs), its efficacy during the inference phase remains underexplored. In this work, we empirically find that mandating explicit object boxes in visually grounded CoT during inference often degrades performance compared to standard textual CoT, which reasons without explicit visual grounding. We hypothesize that the visual localization capability can be internalized into the textual CoT and that the mandatory explicit grounding introduces unnecessary interference with the model's primary objective of answer prediction. To address this problem, we propose Internalizing Visually Grounded Reasoning (\textbf{iVGR}), a novel reinforcement learning framework that transfers localization capabilities into the textual reasoning process. We employ a dual-stream training strategy, where a textual stream is aligned with a high-quality visually grounded stream via a proposed consistency reward, enabling the model to localize accurately without explicit grounding during inference. Extensive experiments demonstrate that our method significantly outperforms existing baselines on fine-grained benchmarks, while maintaining the flexibility to support tool-assisted inference workflows.

</details>

---

### [[20_Research/Papers/具身智能/Task-Focused_Memorization_for_Multimodal_Agents|Task-Focused Memorization for Multimodal Agents]]

![[assets/2605.31075_figure.png|800]]

- **arXiv**: [2605.31075](https://arxiv.org/abs/2605.31075)
- **PDF**: https://arxiv.org/pdf/2605.31075
- **详细分析**: [[20_Research/Papers/具身智能/Task-Focused_Memorization_for_Multimodal_Agents|Task-Focused Memorization for Multimodal Agents]]
- **作者**: Tao Zou, Yichen He, Tian Qiu, Yuan Lin, Hang Li
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 1，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Task-Focused Memorization for Multimodal Agents》归入 大模型、具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory is essential for multimodal agents to build coherent experience, accumulate world knowledge, and achieve continual learning. However, constructing effective memory goes beyond memory module design and basic requirements such as accuracy and fidelity; the key challenge lies in determining what to memorize. Multimodal agents, such as embodied agents, continuously perceive, reason, and act in real or virtual environments, receiving an unbounded stream of multimodal observations. From this combinatorial explosion of information, an agent must selectively retain content that is relevant to its role in the environment and valuable for future tasks. To bridge this gap, we frame memory generation as a learnable memorization policy and introduce TaskMem (Task-focused Memorization Policy Learning), a reinforcement-learning-based framework that enables the policy to dynamically adjust its focus to the demands of real tasks encountered in the environment. TaskMem adopts a two-phase training paradigm: Phase One learns how to memorize by optimizing memory quality under fundamental fidelity requirements; Phase Two occurs after deployment, where the agent learns what to memorize by tuning an adapter on its base MLLM, using recent environment tasks to define a reward model that guides the memorization policy toward task-relevant content. To evaluate our approach, we reformulate VideoMME, EgoLife, and EgoTempo into streaming benchmarks that simulate a realistic setting in which an agent processes streaming observations and handles tasks arriving online. To isolate memory assessment, the questions must be answered using only the agent's memory, without access to raw video. Built on Qwen3-VL-30B-A3B, TaskMem improves VQA accuracy by 6.3%, 7.0%, and 5.3% on these benchmarks, respectively.

</details>

---

### [[20_Research/Papers/强化学习/GUI-C$^2$_Coarse-to-Fine_GUI_Grounding_via_Difficulty-Aware_Reinforcement_Learning|GUI-C$^2$: Coarse-to-Fine GUI Grounding via Difficulty-Aware Reinforcement Learning]]

![[assets/2605.30884_figure.png|800]]

- **arXiv**: [2605.30884](https://arxiv.org/abs/2605.30884)
- **PDF**: https://arxiv.org/pdf/2605.30884
- **详细分析**: [[20_Research/Papers/强化学习/GUI-C$^2$_Coarse-to-Fine_GUI_Grounding_via_Difficulty-Aware_Reinforcement_Learning|GUI-C$^2$: Coarse-to-Fine GUI Grounding via Difficulty-Aware Reinforcement Learning]]
- **作者**: Junlong Li, Chao Hao, Lap-Pui Chau, Yi Wang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《GUI-C$^2$: Coarse-to-Fine GUI Grounding via Difficulty-Aware Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing agentic reinforcement learning methods for GUI grounding have limitations at two levels. At the data level, current approaches typically treat all training samples equally, although their training value to the baseline model varies with difficulty. Overlooking this can greatly reduce training efficiency or even cause collapse. At the strategy level, existing frameworks struggle to balance the trade-off between cropping larger regions for sufficient context and smaller ones for reduced redundancy, a tension inherent to tool-augmented grounding agents. In addition, overly complex decision-making is difficult for small-parameter models and significantly increases inference time. To address these issues, at the data level, we propose GUI-D, a data mining and difficulty scoring pipeline that identifies the training-worthy samples by proper testing and assigns difficulty scores to guide subsequent training weights. At the strategy level, we propose GUI-C$^2$, which employs an area-gated coarse-to-fine refinement mechanism that progressively narrows the visual field via model-internal uncertainty signals, adaptively reserving context for large targets while amplifying precision for small ones, reinforced by improvement-aware stage rewards that ensure each refinement genuinely advances grounding. Meanwhile, we simplify the decision-making process to greatly reduce additional inference time. Finally, extensive experiments show that our method achieves state-of-the-art performance. The code and data will be publicly available.

</details>

---

### [[20_Research/Papers/大模型/VLM-GLoc_Vision-Language_Model_Enhanced_Monte_Carlo_Localization_for_Robust_Semantic_Global_Localization_in_Cluttered_Quasi-Static_Environme|VLM-GLoc: Vision-Language Model Enhanced Monte Carlo Localization for Robust Semantic Global Localization in Cluttered Quasi-Static Environments]]

![[assets/2605.30506_figure.png|800]]

- **arXiv**: [2605.30506](https://arxiv.org/abs/2605.30506)
- **PDF**: https://arxiv.org/pdf/2605.30506
- **详细分析**: [[20_Research/Papers/大模型/VLM-GLoc_Vision-Language_Model_Enhanced_Monte_Carlo_Localization_for_Robust_Semantic_Global_Localization_in_Cluttered_Quasi-Static_Environme|VLM-GLoc: Vision-Language Model Enhanced Monte Carlo Localization for Robust Semantic Global Localization in Cluttered Quasi-Static Environments]]
- **作者**: Shivendra Agrawal, Bradley Hayes
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，大模型 1，机器人 0.5）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《VLM-GLoc: Vision-Language Model Enhanced Monte Carlo Localization for Robust Semantic Global Localization in Cluttered Quasi-Static Environments》归入 大模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Global localization in geometrically aliased, quasi-static environments such as grocery stores, offices, schools, and hospitals poses a significant challenge for mobile robots. Grocery stores with parallel aisles and a long tailed distribution of products, as well as offices and labs with repetitive furniture such as chairs, desks, monitors, and doors, exemplify common indoor environments that present geometric and even semantic ambiguity. Traditional approaches rely either on distinct geometric features or on domain-specific vision pipelines that struggle with long-tail semantic distributions and transient visual clutter. We present VLM-GLoc, a method for hierarchical semantic Monte Carlo Localization (MCL) that leverages open-vocabulary Vision-Language Models (VLMs) as a unified semantic observation front-end. We hypothesize a three-fold benefit from VLMs: (1) extracting highly discriminative rich text features, (2) implicit quality filtering of blurry or dynamic objects, and (3) permanence reasoning for targeted data augmentation. We introduce an inverse semantic proposal mechanism that seeds particles via text-to-map retrieval. Evaluated across two real-world environments with different characteristics and two different platforms: a 3,500 sq. ft. grocery store with a cellphone and a 3,700 sq. ft. lab space with a quadruped, VLM-GLoc achieves 70% and 74% global localization success respectively, substantially outperforming traditional geometry-only and domain-specific baselines.

</details>

---
