# cs.CV | Computer Vision and Pattern Recognition | 2026-08-24

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/具身智能/Just_Noticeable_Difference_Modeling_for_Token_Compression_in_Vision-Language-Action_Models|Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models]]

![[assets/2608.21247_figure.png|800]]

- **arXiv**: [2608.21247](https://arxiv.org/abs/2608.21247)
- **PDF**: https://arxiv.org/pdf/2608.21247
- **详细分析**: [[20_Research/Papers/具身智能/Just_Noticeable_Difference_Modeling_for_Token_Compression_in_Vision-Language-Action_Models|Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models]]
- **作者**: Zhuoyuan Li, Rui Zhao, Jin Wang, Hanwei Zhu, Cong Zhang, Giuseppe Valenzise, Weisi Lin, Kin-Man Lam
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Token compression has become a key technique for reducing the inference cost of large foundation models, with approaches such as token pruning and KV-cache reuse widely adopted in vision-language models and recently explored for embodied agents. In embodied agents, tokens not only support perception and semantic understanding but also directly affect latency-sensitive closed-loop robot action prediction. Existing schemes typically guide compression using redundancy or importance cues, such as visual similarity, attention scores, and saliency. However, these cues only indirectly measure the key factor for safe compression: how much a token can change before causing an unacceptable deviation in downstream actions. This receiver-dependent tolerance is closely related to the principle of just noticeable difference (JND). Classical JND characterizes signal tolerance in the human visual system, while machine-oriented JND extends this concept to downstream machine responses. Building on this progression, we introduce Action-JND, which extends JND modeling to embodied perception by defining noticeability through the language-conditioned action response of a vision-language-action (VLA) policy in closed-loop control. A token change is considered admissible only when the induced action deviation remains within a tolerated margin. To realize this concept, we develop a lightweight token-wise JND estimator in deep visual-feature space to predict the maximum tolerable perturbation while preserving policy responses. The resulting action-tolerance score serves as a plug-and-play criterion for VLA compression paradigms, including stale-KV reuse and token pruning, prioritizing action-tolerant tokens for compression. Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.

</details>

---

### [[20_Research/Papers/大模型/Recognition-Conditioned_Reasoning_A_Training-Free_Multimodal-LLM_Pipeline_for_Fine-Grained_Micro-Action_Understanding|Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding]]

![[assets/2608.21022_figure.png|800]]

- **arXiv**: [2608.21022](https://arxiv.org/abs/2608.21022)
- **PDF**: https://arxiv.org/pdf/2608.21022
- **详细分析**: [[20_Research/Papers/大模型/Recognition-Conditioned_Reasoning_A_Training-Free_Multimodal-LLM_Pipeline_for_Fine-Grained_Micro-Action_Understanding|Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding]]
- **作者**: Fengshun Wang, Jin'ang Han, Zhigang Tu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MA-Bench, MVBench, Micro-DualNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Micro-actions are subtle, short, low-amplitude body movements, such as a fidgeting hand or a slight head tilt, that humans perform with little conscious intent yet that reliably leak emotional and psychological state. Understanding them goes beyond assigning a label: a model must also describe which body parts move and reason, faithfully, about why a clip warrants a particular fine-grained category. We present the training-free, prompt-only system that won first place in the fine-grained understanding track (MA-Bench) of the MAC~2026 Micro-Action Challenge, where both fine-tuning and ground-truth supervision are disallowed. Built entirely upon frozen multimodal large language models (MLLMs), the system dynamically routes each of the eight sub-tasks to the MLLM empirically best suited for that task: a discriminative MLLM for closed-ended recognition tasks and a generative MLLM for open-ended description and reasoning tasks. This architecture achieves a statistically significant performance advantage on open-ended tasks, attaining an average score of 2.68 (on a five-point scale) compared to 1.44 for the second-best approach.

</details>

---

### [[20_Research/Papers/大模型/Latent_Ordinal_Evidence,_Misaligned_Outputs_Inference-Time_Ordinal_Lens_Alignment_for_Multimodal_LLMs|Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs]]

![[assets/2608.20999_figure.png|800]]

- **arXiv**: [2608.20999](https://arxiv.org/abs/2608.20999)
- **PDF**: https://arxiv.org/pdf/2608.20999
- **详细分析**: [[20_Research/Papers/大模型/Latent_Ordinal_Evidence,_Misaligned_Outputs_Inference-Time_Ordinal_Lens_Alignment_for_Multimodal_LLMs|Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs]]
- **作者**: Haiming Li, Yingsheng Liu, Jingmin Zhu, Siyuan Yan, Xieji Li, Jiajun Sun, Zhen Yu, Zongyuan Ge
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs. Across four ordinal benchmarks and four MLLM backbones, ordinal labels are linearly recoverable from hidden states with Spearman correlation up to 0.938, and a task-designed prompt further sharpens this structure. Yet native digit-token outputs weakly expose it: the unembedding matrix filters the ordinal direction, and the digit-token row space retains below 1.15% across all 16 model-dataset combinations, with a 16 to 77 absolute-point accuracy gap between linear-probe and native outputs. We introduce Ordinal Lens Alignment (OLA), a frozen-backbone inference-time method that trains lightweight W_S-anchored lenses on mid-to-deep decoder layers, fuses them into an ordinal distribution, and corrects only digit-token logits at generation. OLA outperforms the SOTA LoRA-tuned OrderChain baseline in most settings while keeping the MLLM frozen, surpasses discriminative ordinal baselines in most cells, and improves over an offline lens in every setting.

</details>

---

### [[20_Research/Papers/具身智能/A_Collaborative_Multi-Modality_Interaction_for_VLA-based_End-to-End_Autonomous_Driving|A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving]]

![[assets/2608.20890_figure.png|800]]

- **arXiv**: [2608.20890](https://arxiv.org/abs/2608.20890)
- **PDF**: https://arxiv.org/pdf/2608.20890
- **详细分析**: [[20_Research/Papers/具身智能/A_Collaborative_Multi-Modality_Interaction_for_VLA-based_End-to-End_Autonomous_Driving|A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving]]
- **作者**: Jingtao Sun, Xiaohai He, Yike Zhang, Dong Huang, Yaonan Wang, Ajmal Mian, Mike Zheng Shou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for end-to-end autonomous driving by jointly integrating perception, reasoning, and decision making within a unified multimodal framework. However, most existing VLA models formulate end-to-end autonomous driving as a visual question answering task, leading to unreliable and less interpretable decision reasoning. In addition, they fail to establish effective multi-modal interaction across heterogeneous sensors, thereby limiting robust scene perception and reliable driving reasoning in long-tail driving scenarios. To this end, we propose a robust VLA-based end-to-end autonomous driving system that combines multi-modality interaction with multi-trajectory planning and optimization, enabling more reliable, interpretable, and safer driving decisions. Our method comprises three core components: (1) Affinity-Guided Optimal Transport for main-auxiliary modality two-way interaction; (2) Distribution-Consistent Modality Transfer for heterogeneous modality distribution transfer and cross-modal interaction; (3) Multi-modal Multi-Trajectory Planning along with Perception-Oriented Trajectory Refinement for better driving decisions to long-tail driving scenarios. Experimental results in open-loop and closed-loop datasets demonstrate improvements in safety long-horizon driving reasoning and road scene perception over existing driving systems, highlighting the ability of our mutli-modality interaction and multi-trajectory planning and optimization for scalable VLA-based systems.

</details>

---

### [[20_Research/Papers/大模型/Annotations_as_Rollouts_Efficient_and_Scalable_Reinforcement_Learning_for_Video_MLLMs|Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs]]

![[assets/2608.20492_figure.png|800]]

- **arXiv**: [2608.20492](https://arxiv.org/abs/2608.20492)
- **PDF**: https://arxiv.org/pdf/2608.20492
- **详细分析**: [[20_Research/Papers/大模型/Annotations_as_Rollouts_Efficient_and_Scalable_Reinforcement_Learning_for_Video_MLLMs|Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs]]
- **作者**: Yunheng Li, Guohong Mu, Hao Li, Shengsheng Qian, Dingwen Zhang, Qibin Hou, Ming-Ming Cheng
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MMSI-Bench, OraRL, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have become a prevailing paradigm for unified video perception. However, post-training on large multi-task datasets remains challenging, as existing reinforcement learning methods sample on-policy groups with few high-quality rollouts even with costly chain-of-thought (CoT) generation. In this paper, we study the sample efficiency and scalability of RL post-training for video MLLMs and introduce OraRL. We identify an overlooked role for annotations: Beyond scoring rollouts, each can enter its on-policy group as an oracle rollout, a direct positive optimization target. Direct oracle integration, however, is nontrivial: a high-reward oracle raises the group baseline and inverts otherwise positive policy advantages, a failure we term advantage inversion. At the core of OraRL is a decoupled advantage estimator: policy rollouts determine an oracle-free baseline, while the oracle-policy gap modulates both a directional gain and a separate detached oracle advantage. Sign-balanced pruning improves efficiency: by retaining only the oracle and the strongest rollouts of each sign, OraRL requires just 2.2x the step time of SFT, less than half the 4.9x required by GRPO with CoT. OraRL scales with model size and data, surpassing its backbone from 0.8B to 9B and GRPO up to 100k prompts. Without chain-of-thought, Video-ORA-9B decodes in 130 ms instead of 4,780 ms. Compared with the respective prior best models, it raises temporal mIoU from 62.5 to 66.0, tracking AO from 73.0 to 78.2, segmentation from 64.3 to 70.4, and the three-benchmark spatial-intelligence macro average from 51.0 to 56.1; on VSI-Bench, it scores 73.1 against 55.0 for GPT-5 and 55.1 for Gemini-3-Pro.

</details>

---
