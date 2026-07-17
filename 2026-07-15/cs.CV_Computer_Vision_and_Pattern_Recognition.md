# cs.CV | Computer Vision and Pattern Recognition | 2026-07-15

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/FlowWAM_Optical_Flow_as_a_Unified_Action_Representation_for_World_Action_Models|FlowWAM: Optical Flow as a Unified Action Representation for World Action Models]]

![[assets/2607.13017_figure.png|800]]

- **arXiv**: [2607.13017](https://arxiv.org/abs/2607.13017)
- **PDF**: https://arxiv.org/pdf/2607.13017
- **详细分析**: [[20_Research/Papers/具身智能/FlowWAM_Optical_Flow_as_a_Unified_Action_Representation_for_World_Action_Models|FlowWAM: Optical Flow as a Unified Action Representation for World Action Models]]
- **作者**: Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang, Kai Wang, Jianhua Yang, Dong An, He Guan, Gaoteng Liu, Jianlou Si, Jun Huang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《FlowWAM: Optical Flow as a Unified Action Representation for World Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. Existing numerical actions fail to satisfy the former, and prior visual action representations overlook the temporal motion structure across frames. We address this issue with FlowWAM, a dual-stream diffusion framework that adopts optical flow as a unified, video-native action representation. Flow videos share the same format as RGB videos and encode rich per-pixel displacement. By jointly modeling them within a shared pretrained video generator, FlowWAM can naturally implement two modes of WAMs. In policy mode, FlowWAM generates flow for action prediction, while in world-model mode, it uses target flow sequences to guide future video generation. Moreover, since flow can be easily extracted from raw videos without action labels, FlowWAM can leverage large-scale action-unlabeled video datasets for pretraining. We empirically find that our flow-based action representation delivers gains across both modes. On RoboTwin manipulation, FlowWAM raises the success rate to 92.94% on the Clean setting and 92.14% on Random, outperforming both VLA and WAM baselines. On WorldArena world modeling, it achieves the best overall EWMScore (63.71) with an 18.4% relative improvement in trajectory accuracy. More results can be found on our project website: https://flow-wam.github.io .

</details>

---

### [[20_Research/Papers/具身智能/Hy-Embodied-VLM-1.0_Efficient_Physical-World_Agents|Hy-Embodied-VLM-1.0: Efficient Physical-World Agents]]

![[assets/2607.12894_figure.png|800]]

- **arXiv**: [2607.12894](https://arxiv.org/abs/2607.12894)
- **PDF**: https://arxiv.org/pdf/2607.12894
- **详细分析**: [[20_Research/Papers/具身智能/Hy-Embodied-VLM-1.0_Efficient_Physical-World_Agents|Hy-Embodied-VLM-1.0: Efficient Physical-World Agents]]
- **作者**: Ziyi Wang, Xumin Yu, Yongming Rao, Yonggen Ling, Yunheng Li, Oran Wang, Mingqi Gao, Yuchen Zhou, Yves Liang, Zuyan Liu, Yani Zhang, Rui Huang...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Hy-Embodied-VLM-1.0: Efficient Physical-World Agents》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Physical-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodied agents operating in the physical world. To cultivate such capabilities from the pre-training stage onward, we define an action-centric capability taxonomy comprising three progressive dimensions: Action-Relevant State Understanding, Action-Transition Reasoning, and Sequential and Adaptive Reasoning. Guided by this taxonomy, we develop a systematic data pipeline and curate data mixtures spanning both pre-training and post-training. To deliver strong physical-world understanding and interaction capabilities while supporting latency-sensitive deployment, we build our model on the Hy3-A3B language backbone and the Hy-ViT2 vision encoder. Its efficient Mixture-of-Experts architecture combines strong model capacity with high inference efficiency. We evaluate Hy-Embodied-VLM-1.0 on a comprehensive suite of 38 benchmarks covering embodied perception, physical-world understanding, and embodied reasoning. The model achieves the best performance among similarly sized models on 19 of the 38 benchmarks and substantially outperforms strong competitors, including Qwen3.6-A3B and Cosmos 3. Compared with the previous-generation Hy-Embodied-0.5 MoT-2B, Hy-Embodied-VLM-1.0 improves average performance by 8.4%. Despite activating only 3B parameters, it achieves performance close to that of the previous-generation model with 32B activated parameters. Beyond static benchmark evaluation, Hy-Embodied-VLM-1.0 also demonstrates strong performance on embodied agentic tasks requiring multi-turn interaction and long-horizon reasoning.

</details>

---

### [[20_Research/Papers/具身智能/Breaking_Déjà_Vu_Independent_Auditing_of_Visual_Place_Recognition_through_Vision-Language_Reasoning|Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning]]

![[assets/2607.12818_figure.png|800]]

- **arXiv**: [2607.12818](https://arxiv.org/abs/2607.12818)
- **PDF**: https://arxiv.org/pdf/2607.12818
- **详细分析**: [[20_Research/Papers/具身智能/Breaking_Déjà_Vu_Independent_Auditing_of_Visual_Place_Recognition_through_Vision-Language_Reasoning|Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning]]
- **作者**: Sania Waheed, Michael Milford, Sarvapali D. Ramchurn, Shoaib Ehsan
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，机器人 0.4）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual place recognition (VPR) is a key enabler of accurate localization and long-term autonomous navigation in robotics applications, such as loop closure detection for simultaneous localisation and mapping (SLAM). However, real-world VPR deployment relies on selecting an image matching threshold that balances precision and recall. These thresholds are typically tuned using labeled validation data and fixed during deployment, making them unreliable under environmental changes where ground truth is unavailable. This is particularly problematic in safety-critical robotics, where accepting a false loop closure can corrupt the estimated trajectory and map. In this work, we introduce Visual Place Recognition Auditing, an independent post-retrieval verification framework that leverages Vision-Language Models (VLMs) to assess retrieved matches by reasoning jointly over query and candidate images. Unlike conventional verification methods, our approach performs instance-level verification without requiring architecture-specific confidence measures, dataset-dependent thresholds, or prior knowledge of the deployment environment. We evaluate our method on six benchmark datasets using five state-of-the-art VPR methods and four VLMs. Results show that VLM-based auditing improves recall@1 by 13.6% on average as compared to state-of-the-art methods while reducing false acceptance rates to 12%, maintaining precision above 95% and coverage above 75%.

</details>

---

### [[20_Research/Papers/大模型/EvoGraph-R1_Self-Evolving_Multimodal_Knowledge_Hypergraphs_for_Agentic_Retrieval|EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval]]

![[assets/2607.12764_figure.png|800]]

- **arXiv**: [2607.12764](https://arxiv.org/abs/2607.12764)
- **PDF**: https://arxiv.org/pdf/2607.12764
- **详细分析**: [[20_Research/Papers/大模型/EvoGraph-R1_Self-Evolving_Multimodal_Knowledge_Hypergraphs_for_Agentic_Retrieval|EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval]]
- **作者**: Jiashi Lin, Changhong Jiang, Xiangru Lin, Ruifei Zhang, Xinyi Zhu, Jiyao Liu, Cheng Tang, Ye Du, Shujian Gao, Junzhi Ning, Lihao Liu, Ziyan Huang...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) has emerged as a critical paradigm for grounding Multimodal Large Language Models (MLLMs) in external knowledge. Recent GraphRAG methods introduce structured entity-relation graphs to improve retrieval and reasoning. However, they remain limited by treating knowledge graphs as static data structures built offline and queried in a single pass. This static paradigm misaligns with the interactive, iterative nature of knowledge-intensive reasoning, creating three bottlenecks: (i) text-centric fragmentation that impedes cross-modal reasoning, (ii) frozen structures unable to incorporate new evidence or correct errors, and (iii) rigid single-pass retrieval without adaptive refinement. To overcome these limitations, we introduce EvoGraph-R1, a self-evolving GraphRAG framework that reconceptualizes knowledge graphs as dynamic environments shaped through agent interactions. We formulate retrieval as a Markov Decision Process (MDP) where the agent observes the graph state and executes actions to query (GraphRetrieve), expand (WebSearch), refine (GraphEdit), or terminate (Answer) the reasoning. These actions reshape the hypergraph structure and generate feedback signals that guide subsequent evolution. Through this closed loop, the hypergraph evolves by integrating new evidence, correcting errors, and refining structure to support multi-hop reasoning. Experiments on multimodal VQA and text QA benchmarks demonstrate substantial improvements over existing RAG baselines in accuracy, coverage, and traceability, establishing self-evolving knowledge graphs as a fundamental paradigm across modalities.

</details>

---

### [[20_Research/Papers/具身智能/ReflectVLN_Training_Vision-Language_Navigation_Agents_with_Reflective_Reasoning|ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning]]

![[assets/2607.12680_figure.png|800]]

- **arXiv**: [2607.12680](https://arxiv.org/abs/2607.12680)
- **PDF**: https://arxiv.org/pdf/2607.12680
- **详细分析**: [[20_Research/Papers/具身智能/ReflectVLN_Training_Vision-Language_Navigation_Agents_with_Reflective_Reasoning|ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning]]
- **作者**: Jiahang Wang, Yirong Yang, Yanqing Zhu, Minghua Luo, Shichao Xie, Fei Liu, Mu Xu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACoT-VLA, CoT-VLA, DreamVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent performs subtask decomposition and reflection, generating executable subtask descriptions as corrective plans. Conditioned on these descriptions, the execution agent grounds them into short-horizon actions under current observations while monitoring sub-goal progress and detecting off-track behavior. Crucially, ReflectVLN enables closed-loop bidirectional communication: the execution agent emits progress and deviation signals to trigger reflection and subtask updates on demand, and the intention agent returns structured guidance that reconditions subsequent actions for recovery. To encourage temporally coherent decisions with interpretable intermediate rationales, we introduce Action Chain-of-Thought (Action-CoT), a path-conditioned dual-query training scheme for action generation. Experiments on standard VLN benchmarks show that ReflectVLN improves success rates and path efficiency under a constrained data budget, with favorable training cost and fewer high-level intention calls at inference time, while providing interpretable intermediate decisions for analysis and collaboration. Code is available at: https://github.com/AIprogrammer/ReflectVLN

</details>

---

### [[20_Research/Papers/具身智能/Instance-Enriched_Semantic_Maps_for_Visual_Language_Navigation|Instance-Enriched Semantic Maps for Visual Language Navigation]]

![[assets/2607.12630_figure.png|800]]

- **arXiv**: [2607.12630](https://arxiv.org/abs/2607.12630)
- **PDF**: https://arxiv.org/pdf/2607.12630
- **详细分析**: [[20_Research/Papers/具身智能/Instance-Enriched_Semantic_Maps_for_Visual_Language_Navigation|Instance-Enriched Semantic Maps for Visual Language Navigation]]
- **作者**: Jiho Hong, Eunae Kang, Sanghyun Kim, Young-Sik Shin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Instance-Enriched Semantic Maps for Visual Language Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual Language Navigation (VLN) aims to enable an embodied agent to navigate complex environments by following natural language instructions. Recent approaches build semantic spatial maps and leverage Large Language Models (LLMs) for reasoning and decision making. Despite these advances, existing systems lack instance-level object detail and robustness to diverse user queries, limiting reliable navigation in complex indoor environments. To address these limitations, we propose Instance-Enriched Semantic Maps, a unified framework with three key contributions: (1) Instance-level two-and-a-half-dimensional (2.5D) rich information mapping that constructs maps from color and depth observations via open-vocabulary panoptic segmentation, preserving vertical distinctions and capturing small objects, while storing diverse semantic attributes and natural language captions enriched with room-level context. (2) Robust query processing via LLM-based target selection, which dynamically routes queries across type-specialized experts and integrates their outputs through score-level fusion, enabling consistent goal selection across diverse query formulations. (3) Storage-efficient semantic representation that achieves approximately 96% reduction compared to three-dimensional (3D) scene-graph approaches while preserving sufficient spatial information for navigation. The proposed 2.5D representation outperforms the 3D baseline by over 27% in prediction-normalized Area Under the Curve (AUC). In navigation experiments, our method achieves over 17% improvement in object retrieval and over 23% in navigation success compared to the baseline across diverse query types. The project page is available at https://rcilab.github.io/iesm_vln.

</details>

---

### [[20_Research/Papers/大模型/Towards_Vision-Free_CIR_Attribute-Augmented_Scoring_and_LLM-Based_Reranking_for_Zero-Shot_Composed_Image_Retrieval|Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval]]

![[assets/2607.12621_figure.png|800]]

- **arXiv**: [2607.12621](https://arxiv.org/abs/2607.12621)
- **PDF**: https://arxiv.org/pdf/2607.12621
- **详细分析**: [[20_Research/Papers/大模型/Towards_Vision-Free_CIR_Attribute-Augmented_Scoring_and_LLM-Based_Reranking_for_Zero-Shot_Composed_Image_Retrieval|Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval]]
- **作者**: Ryotaro Shimada, Yu-Chieh Lin, Yuji Nozawa, Youyang Ng, Osamu Torii, Yusuke Matsui
- **cs 子类**: cs.CV, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has shown that "Vision-Free'' approaches (representing images as text) can be effective for standard image retrieval tasks. However, it remains unclear whether this paradigm can effectively handle a more complex, multimodal task, Composed Image Retrieval (CIR), due to the inherent information loss in textual descriptions. In this paper, we introduce a Vision-Free CIR framework that addresses this challenge through two key techniques: (1) Attribute-Augmented Hybrid Scoring, which compensates for lost visual details via explicit attribute matching, and (2) LLM-Based Reranking, which verifies semantic consistency of top candidates. Experiments on the open-domain CIRR dataset show that our approach outperforms existing Zero-shot CIR methods (44.04% R@1, +8.79%). On FashionIQ, our results highlight the trade-off between semantic reasoning and fine-grained visual matching. Ablation studies reveal that both attribute-augmented scoring and LLM-Based Reranking consistently improve performance.

</details>

---

### [[20_Research/Papers/机器人/Edge-Aware_Thermal_Infrared_UAV_Swarm_Tracking|Edge-Aware Thermal Infrared UAV Swarm Tracking]]

![[assets/2607.12544_figure.png|800]]

- **arXiv**: [2607.12544](https://arxiv.org/abs/2607.12544)
- **PDF**: https://arxiv.org/pdf/2607.12544
- **详细分析**: [[20_Research/Papers/机器人/Edge-Aware_Thermal_Infrared_UAV_Swarm_Tracking|Edge-Aware Thermal Infrared UAV Swarm Tracking]]
- **作者**: Yu-Hsi Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.CV

#### 研究背景与动机

《Edge-Aware Thermal Infrared UAV Swarm Tracking》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Thermal infrared (TIR) imaging is essential for UAV swarm operations in visually degraded environments. However, tracking tiny UAVs remains challenging due to limited appearance cues, frequent occlusions, and rapid maneuvers. Despite significant progress driven by benchmarks such as the Anti-UAV challenge, existing methods primarily prioritize accuracy while overlooking the computational constraints of real-time edge deployment. The standard Kalman Filter (KF) offers the efficiency required for edge devices, yet its constant-velocity assumption often breaks down under highly dynamic UAV motion and thermal sensor jitter. More sophisticated nonlinear estimators can improve robustness but often introduce additional computational costs. To address this gap, we propose an edge-aware online tracking pipeline centered on the Adaptive Kinematic Kalman Filter (AKKF), which augments the linear KF with state-dependent kinematic modeling while preserving real-time efficiency. Combined with transient false-positive suppression and kinematics-driven predictive coasting, the presented pipeline improves trajectory continuity under challenging TIR conditions. Experiments on the Beyond Strong Baseline (BSB) benchmark provide a starting point for edge-aware UAV tracking by jointly evaluating tracking performance and computational efficiency, offering insights toward future real-time deployment.

</details>

---

### [[20_Research/Papers/具身智能/Self_in_Space_Benchmarking_Self-Awareness_and_Spatial_Cognition_in_UAV_Embodied_Intelligence|Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence]]

![[assets/2607.12477_figure.png|800]]

- **arXiv**: [2607.12477](https://arxiv.org/abs/2607.12477)
- **PDF**: https://arxiv.org/pdf/2607.12477
- **详细分析**: [[20_Research/Papers/具身智能/Self_in_Space_Benchmarking_Self-Awareness_and_Spatial_Cognition_in_UAV_Embodied_Intelligence|Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence]]
- **作者**: Zhishan Zou, Guoyan Sun, Zhiwei Wei, Jiancheng Pan, Yujie Li, Mugen Peng, Wenjia Xu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.2，机器人 0.8）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenQA, SIS-Bench, UrbanVideo-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous UAV systems increasingly rely on multimodal large language models (MLLMs) to operate in complex real-world environments. Such embodied scenarios require not only understanding the surrounding space but also maintaining a coherent representation of the agent itself. However, existing UAV-oriented approaches and benchmarks remain largely environment-centric, primarily focusing on spatial understanding tasks, with the agent's self-awareness remaining implicit. To address this gap, we introduce SIS-Bench, a benchmark for evaluating embodied spatial intelligence in UAV scenarios under a unified self-in-space formulation. SIS-Bench organizes evaluation along two complementary dimensions, space and self, and a three-level hierarchy of perception, memory, and reasoning. It contains 4,856 question--answer pairs across 13 tasks derived from 1,646 real-world UAV videos through a task-conditioned construction pipeline with expert verification. Extensive evaluations reveal that current MLLMs exhibit fundamental limitations in modeling dynamic and agent-centered processes. In particular, we observe a clear imbalance between spatial cognition and self-awareness, as well as a progressive performance degradation across cognitive levels. Motivated by these findings, we further explore a motion-aware representation that incorporates self-related dynamics through optical flow and visual feature fusion. Experimental results show that modeling agent motion consistently improves perception and memory performance, not only in spatial cognition but also in self-awareness, and generalizes to downstream UAV decision-making tasks. Our results highlight the importance of self-awareness for advancing embodied spatial intelligence, and provide both a new benchmark and empirical evidence for motion-aware self-in-space modeling.

</details>

---

### [[20_Research/Papers/强化学习/Steering_Diffusion_Models_via_Class-Contrastive_Influence_for_Few-Shot_Medical_Classification|Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification]]

![[assets/2607.12464_figure.png|800]]

- **arXiv**: [2607.12464](https://arxiv.org/abs/2607.12464)
- **PDF**: https://arxiv.org/pdf/2607.12464
- **详细分析**: [[20_Research/Papers/强化学习/Steering_Diffusion_Models_via_Class-Contrastive_Influence_for_Few-Shot_Medical_Classification|Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification]]
- **作者**: Jeeyung Kim, Erfan Esmaeili, Qiang Qiu
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When labeled data are scarce, off-the-shelf diffusion models can augment training sets for few-shot medical image classification, but not all generated samples are equally useful for the downstream task. Existing approaches largely improve synthetic data by increasing realism, diversity, or domain adaptation, while overlooking a more fundamental question: how should sample usefulness for classification be measured and optimized? We address this with Class-Contrastive Influence (C2I), a criterion that quantifies a sample's usefulness through its gradient-based influence on the classifier. We find that effective samples exhibit a strong C2I gap: their loss gradients align with validation gradients from the same class and oppose those from other classes. Our analysis further suggests that such high-C2I samples are hard, boundary-proximal examples that help refine the decision boundary and improve robustness. Building on this insight, we fine-tune diffusion models with reinforcement learning using a C2I-based reward to steer generation toward class-informative samples. Across several few-shot medical imaging benchmarks, C2I-guided generation improves downstream accuracy and robustness over diffusion-based augmentation baselines, showing that synthetic augmentation is most effective when guided by task usefulness rather than image quality alone.

</details>

---

### [[20_Research/Papers/具身智能/MobileSAM2_Lightweight_Segment_Anything_for_Spatial_Intelligence|MobileSAM2: Lightweight Segment Anything for Spatial Intelligence]]

![[assets/2607.12297_figure.png|800]]

- **arXiv**: [2607.12297](https://arxiv.org/abs/2607.12297)
- **PDF**: https://arxiv.org/pdf/2607.12297
- **详细分析**: [[20_Research/Papers/具身智能/MobileSAM2_Lightweight_Segment_Anything_for_Spatial_Intelligence|MobileSAM2: Lightweight Segment Anything for Spatial Intelligence]]
- **作者**: Kai Jiang, Jiaxing Huang, Jingyi Zhang, Weiying Xie, Yunsong Li, Yufei Wang, Aoran Xiao, Dacheng Tao
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.7（加权：具身智能 0.6，大模型 0.1）
- **关联关键词**: LLM, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MobileSAM2: Lightweight Segment Anything for Spatial Intelligence》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The recent large video foundation model, SAM2, enables segment anything in both images and videos, serving as a powerful base model for various applications. However, many of such use cases require to operate on resource-constrained devices like mobile phones and laptops. In this work, we aim to make SAM2 more mobile-friendly by distilling the heavyweight SAM2 into a lightweight model, facilitating segment anything in both images and videos on mobile devices. To this end, we propose Hypergraphical Knowledge Distill (HyperKD), which introduces the idea of hypergraph into knowledge distillation, aiming to effectively model and transfer SAM2's generalizable and comprehensive knowledge. HyperKD consists of Temporal HyperKD and Granularity HyperKD that construct hypergraphs to explicitly model and extract the generalizable temporal knowledge and the comprehensive multi-granularity knowledge from SAM2 respectively, which are then distilled into the lightweight student model by aligning it with the constructed hypergraphs. Besides, we present MobileSAM2, a new family of lightweight SAM2 that balances efficiency and effectiveness via searching the best model architectures with HyperKD during model size reduction. Extensive experiments validate MobileSAM2 across multiple benchmarks and show promising generalization performance on embodied AI tasks.

</details>

---

### [[20_Research/Papers/大模型/How_to_Realize_Recursively_Self-Improving_Agents_and_Personal_Singularity_A_Goal-,_Scope-,_Tool-,_and_Benchmark-Driven_Multi-Agent_Architect|How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture]]

![[assets/2607.12254_first_page.png|800]]

- **arXiv**: [2607.12254](https://arxiv.org/abs/2607.12254)
- **PDF**: https://arxiv.org/pdf/2607.12254
- **详细分析**: [[20_Research/Papers/大模型/How_to_Realize_Recursively_Self-Improving_Agents_and_Personal_Singularity_A_Goal-,_Scope-,_Tool-,_and_Benchmark-Driven_Multi-Agent_Architect|How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture]]
- **作者**: Chengshuai Yang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, MLAgentBench, MathTutorBench, OSWorld, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents can increasingly plan, use tools, maintain memory, and execute long-horizon tasks. These advances motivate two linked questions: how can an agent improve the mechanisms by which it learns and acts, and how can that improvement increase the durable capabilities of its user rather than only the software itself? This paper proposes a governed multi-agent architecture for recursively self-improving agents and introduces personal singularity as a bounded human-AI co-development objective: helping a user approach an expanding, user-defined capability frontier across selected domains. Each agent is defined by a goal contract, bounded scope, validated tool registry, tool-level tests, end-to-end benchmarks, an owner-controlled autonomy policy, a routing policy, memory, and an improvement policy. Out-of-scope tasks are transferred to another accountable agent or to a newly created niche agent. A user-facing Auto-Index selects interactive, hybrid, autonomous, or scheduled operation without overriding external permissions. The architecture combines a fast planner-executor-verifier loop, a slower evidence-gated improvement loop, an external governance plane, decentralized agent lineages, an owner-directed agent foundry, and a Personal Singularity OS coordinating working, computational-imaging, process-learning, and personal-learning agents. We formalize scope, routing, improvement acceptance, bounded goal evolution, tool-first execution, and human capability transfer, and provide safety invariants, benchmark design, and an implementation roadmap. This is a position and systems-design paper, not evidence that unrestricted recursive self-improvement or personal singularity has already been achieved.

</details>

---

### [[20_Research/Papers/机器人/RegHead_Non-Humanoid_Head_Blendshapes_via_Feed-Forward_Registration|RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration]]

![[assets/2607.12206_figure.png|800]]

- **arXiv**: [2607.12206](https://arxiv.org/abs/2607.12206)
- **PDF**: https://arxiv.org/pdf/2607.12206
- **详细分析**: [[20_Research/Papers/机器人/RegHead_Non-Humanoid_Head_Blendshapes_via_Feed-Forward_Registration|RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration]]
- **作者**: Jiahao Luo, Hao Zhang, Jianqi Chen, Yijie He, Jiaxu Zou, Michael Vasilkovsky, Sergei Korolev, Sergey Tulyakov, Chaoyang Wang, Peter Wonka, James Davis, Jian Wang
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present RegHead, a framework for constructing semantic blendshape sets for animatable non-humanoid head avatars. With a fixed expression vocabulary, semantic blendshapes provide a low-dimensional and interpretable animation interface and support cross-identity retargeting. Building such blendshape sets remains expensive because (i) expression-consistent supervision is scarce, (ii) generated 4D assets typically lack correspondence, and (iii) facial motion is highly localized. We propose (1) a large-scale dataset of non-humanoid identities paired with a shared expression vocabulary, obtained by expanding a small artist-rigged library via fine-tuned image editing; (2) a dense stochastic anchor motion representation tailored to localized facial deformations; and (3) a fast feed-forward registration model that converts unregistered expression meshes into a corresponded blendshape basis by predicting anchor-based deformations from the neutral shape. Experiments show that our approach produces higher-fidelity expression meshes than baselines, while running orders of magnitude faster than optimization. We further demonstrate real-time retargeting from human face tracking signals to non-humanoid characters, capturing both head pose and localized facial motions. Our project page is available at https://snap-research.github.io/RegHead/.

</details>

---

### [[20_Research/Papers/大模型/Anomalous_Frame_Detection_Using_VLM-Based_Description_Comparison_for_Extracting_Expert-Specific_Actions_and_Contextual_Decision-Making_Scene|Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity]]

![[assets/2607.11957_first_page.png|800]]

- **arXiv**: [2607.11957](https://arxiv.org/abs/2607.11957)
- **PDF**: https://arxiv.org/pdf/2607.11957
- **详细分析**: [[20_Research/Papers/大模型/Anomalous_Frame_Detection_Using_VLM-Based_Description_Comparison_for_Extracting_Expert-Specific_Actions_and_Contextual_Decision-Making_Scene|Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity]]
- **作者**: Ryo Sakai, Kaname Yokoyama
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maintenance of critical infrastructures, such as railways and power plants, is essential for ensuring operational safety and reliability. However, the declining number of skilled maintenance workers highlights the need to transfer expert know-how to less experienced workers. Previous studies have attempted to extract candidates of expert knowledge by comparing videos of manual-based work with those of expert workers, mainly focusing on differences in observable actions. However, expert know-how is often embedded not only in actions but also in contextual decision-making during task execution. This paper proposes a method that detects anomalous frames between two task videos to automatically extract candidate scenes containing expert-specific actions and contextual decision-making scenes. The method generates frame-wise visual descriptions using a vision-language model (VLM). Expert-specific actions are extracted based on frame similarities computed from description comparisons between two videos, while contextual decision-making scenes are extracted using segment similarities derived from intra-video self-similarity of the descriptions. In simulated distribution board maintenance experiments involving 27 task scenarios, the proposed method achieved extraction rates of 65% for action candidates and 61% for decision-scene candidates, improving over conventional methods that achieved 59% and 33%, respectively. These results demonstrate the effectiveness of the proposed approach in discovering candidate scenes containing expert know-how.

</details>

---

### [[20_Research/Papers/大模型/TSCA-Net_Temporal-Spatial_Clique_Attention_for_Interpretable_Multimodal_Pedestrian_Trajectory_Prediction|TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction]]

![[assets/2607.11939_figure.png|800]]

- **arXiv**: [2607.11939](https://arxiv.org/abs/2607.11939)
- **PDF**: https://arxiv.org/pdf/2607.11939
- **详细分析**: [[20_Research/Papers/大模型/TSCA-Net_Temporal-Spatial_Clique_Attention_for_Interpretable_Multimodal_Pedestrian_Trajectory_Prediction|TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction]]
- **作者**: Md Mustafizur Rahman, Guangchao Yang, A F M Abdun Noor, Md Imam Ahasan, Md Mahfuzur Rahman, Md Ariful Islam
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.7（加权：大模型 0.5，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction》归入 大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MCK-Net, PECNet, TSCA-Net, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate pedestrian trajectory prediction in crowded environments remains challenging due to the multimodal uncertainty of human motion and the variable complexity of motion dynamics across different scene contexts. Existing goal-conditioned models rely on static displacement structures that assign equal weight to all historical time steps, standard graph attention mechanisms, and fixed-capacity motion decoders that cannot adapt to local prediction complexity. To address these limitations, we propose TSCA-Net, a trajectory prediction framework built upon three complementary modules. The Temporal-Spatial Clique Attention (TSCA) module introduces learnable temporal gating into clique-based goal-history interaction, enabling time-aware modulation of historical observations relative to each candidate goal. The Cross-Pedestrian Clique Potential (CPCP) module models asymmetric pairwise agent relationships through a dynamic clique potential framework with a time-varying social graph. The Adaptive KAN Grid Refinement (AKGR) mechanism dynamically adjusts the B-spline grid resolution of a Kolmogorov-Arnold Network-augmented LSTM decoder based on per-agent goal distribution entropy, balancing model expressiveness against overfitting across varying motion complexities. Extensive experiments on the ETH/UCY and Stanford Drone Dataset benchmarks demonstrate that TSCA-Net achieves state-of-the-art performance, with average ADE/FDE of 0.13/0.20 m on ETH/UCY and 6.95/10.43 pixels on SDD. Comprehensive ablation studies confirm the complementary contributions of all three proposed modules.

</details>

---
