# cs.CV | Computer Vision and Pattern Recognition | 2026-08-07

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/世界模型/MASS_Multiplayer_World_Models_with_Authoritative_Shared_State|MASS: Multiplayer World Models with Authoritative Shared State]]

![[assets/2608.06257_figure.png|800]]

- **arXiv**: [2608.06257](https://arxiv.org/abs/2608.06257)
- **PDF**: https://arxiv.org/pdf/2608.06257
- **详细分析**: [[20_Research/Papers/世界模型/MASS_Multiplayer_World_Models_with_Authoritative_Shared_State|MASS: Multiplayer World Models with Authoritative Shared State]]
- **作者**: Ziqi Cai, Siqi Yang, Yimu Wang, Zixian Gao, Yunheng Liu, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
- **cs 子类**: cs.CV, cs.HC
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《MASS: Multiplayer World Models with Authoritative Shared State》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Gamma-World, MultiWorld, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current video world models struggle in multiplayer environments because they entangle world state with view-dependent visual latents, leading to redundant compute, view inconsistencies, and poor scalability. We propose MAS (Multiplayer world models with Authoritative Shared State) to resolve this limitation. Inspired by multiplayer game architectures, MAS disentangles world dynamics and view rendering. A learned Logic Engine advances a global, authoritative typed state from joint actions without any hand-written transition function, acting as the sole recurrent memory and synchronization reference. From this shared state, a learned Rendering Engine generates independent and consistent views for any requested camera on demand. This explicit disentangling allows MAS to achieve superior state accuracy and lower cross-view inconsistency compared to state-of-the-art multi-view baselines on a matched multiplayer Snake benchmark. It advances predicted worlds with 1,024 concurrent players for 10,000 recurrent steps. Our results show that explicit, authoritative state modeling provides a practical foundation for scalable and consistent multi-agent world simulation.

</details>

---

### [[20_Research/Papers/大模型/Prior-SG_Task_and_Prior_Driven_Region_Segmentation_for_Scene_Graphs_in_Arbitrarily-Structured_Environments|Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments]]

![[assets/2608.06170_figure.png|800]]

- **arXiv**: [2608.06170](https://arxiv.org/abs/2608.06170)
- **PDF**: https://arxiv.org/pdf/2608.06170
- **详细分析**: [[20_Research/Papers/大模型/Prior-SG_Task_and_Prior_Driven_Region_Segmentation_for_Scene_Graphs_in_Arbitrarily-Structured_Environments|Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments]]
- **作者**: Giorgio Tonetti, Laurent Kneip, Abel Gawel, Marco Hutter
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《Prior-SG: Task and Prior Driven Region Segmentation for Scene Graphs in Arbitrarily-Structured Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Open-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical 3D scene graphs are a promising representation for high-level spatial reasoning in autonomous mobile platforms. However, existing extraction frameworks typically rely on purely local visual clustering or strict geometric heuristics, such as wall-separated rooms, which fail in open-plan or arbitrarily-structured environments. We propose Prior-SG, a task- and prior-driven framework that casts scene graph generation fundamentally as a probabilistic alignment problem. As the robot explores, it continuously aggregates an incoming RGB-D sensor stream into a physically grounded Instance Graph utilizing a multi-scale, open-vocabulary feature fusion strategy. The system then infers the high-level functional semantics of this map through a Maximum A Posteriori (MAP) estimate, guided by a Prior Graph-a logical expectation of the environment's structure and task-relevant vocabulary synthesized dynamically by a Large Language Model. By optimizing a Markov Random Field that fuses heterogeneous experts (visual, geometric, and discrete objects) with these topological priors, the system resolves local perceptual ambiguities. We validate this approach across diverse simulated residential datasets and large, open-plan real-world environments. Prior-SG achieves state-of-the-art semantic region segmentation accuracy compared to recent baselines, robustly delineates distant functional boundaries in the absence of physical walls, and uniquely provides zero-shot ontological flexibility, enabling the robot to entirely restructure its spatial partitioning based on a given high-level task.

</details>

---

### [[20_Research/Papers/大模型/Learning_from_Failures_Retrieval-Centric_CoT_via_Hard_Negatives_for_Unified_Multimodal_Retrieval|Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval]]

![[assets/2608.06060_first_page.png|800]]

- **arXiv**: [2608.06060](https://arxiv.org/abs/2608.06060)
- **PDF**: https://arxiv.org/pdf/2608.06060
- **详细分析**: [[20_Research/Papers/大模型/Learning_from_Failures_Retrieval-Centric_CoT_via_Hard_Negatives_for_Unified_Multimodal_Retrieval|Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval]]
- **作者**: Zelong Sun, Jun Wang, Kaicheng Yang, Tiancheng Gu, Ziyong Feng, Zhiwu Lu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates. Recent methods mitigate this limitation by generating Chain-of-Thought (CoT) rationales to enrich the query representation. However, such reasoning is typically derived from the query alone: it explains what the query describes, but not what the retriever misunderstands. We argue that effective retrieval reasoning should instead be conditioned on retrieval feedback. Based on this insight, we introduce UniME-R1, an embedder-adviser framework that learns to reason over initially retrieved candidates and generate Retrieval-Centric Chain-of-Thought (RC-CoT). The adviser analyzes candidates individually to identify the discriminative cues confused by the embedder. If the target appears in the initial top-k set, UniME-R1 directly reranks the candidates; otherwise, it generates RC-CoT to refine the retrieval direction and performs full-corpus re-retrieval with a dual-mode embedder. To train the framework, we mine hard negatives to simulate realistic retrieval failures, jointly optimize direct retrieval and RC-CoT-augmented retrieval, and align the adviser with retrieval outcomes through supervised learning and retrieval-oriented reinforcement learning. Extensive experiments on MMEB-V2 and a diverse set of general multimodal retrieval benchmarks demonstrate that UniME-R1 consistently improves retrieval performance over strong baselines.

</details>

---

### [[20_Research/Papers/世界模型/Robust-WAM_Bridging_Generative_Pretraining_and_Semantic_Foresight_in_World-Action_Models|Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models]]

![[assets/2608.05903_figure.png|800]]

- **arXiv**: [2608.05903](https://arxiv.org/abs/2608.05903)
- **PDF**: https://arxiv.org/pdf/2608.05903
- **详细分析**: [[20_Research/Papers/世界模型/Robust-WAM_Bridging_Generative_Pretraining_and_Semantic_Foresight_in_World-Action_Models|Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models]]
- **作者**: Haodong Yan, Junfeng Li, Junjie He, Zhide Zhong, MingMing Yu, Wenxuan Song, Jiaguan Zhu, Yangyang Zheng, Yuqiao Du, Jiadi You, Yingjie Cai, Xu Yan...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FutureVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mainstream World-Action Models (WAMs) adapt pretrained video generation models (VGMs) for robot control, transferring their learned dynamics prior for action prediction. These VGMs are typically trained in a variational autoencoder (VAE) latent space. However, the VAE latent space is optimized for pixel reconstruction, which rewards fine appearance detail and leaves the action prediction fragile under visual shifts. Recent works build WAMs in semantic latent space, which are more robust to appearance shifts. However, these models cannot leverage the large-scale VGM pretraining that exists only in VAE space. To overcome this dilemma, we propose Robust-WAM, a general post-training method for video-generation-based WAMs that preserves the VAE-based generative path and adds a lightweight semantic foresight alignment objective on the action stream. This retains the large-scale VGM pretraining while grounding actions in appearance-invariant dynamics that stay reliable under illumination shifts and other visual out-of-distribution conditions. Specifically, we employ learnable query tokens to bring future-scene semantics into the action stream by aligning their output hidden states with the semantic foresight of future ground-truth frames. To establish the temporal correspondence between each query and the future step it describes, we give it the positional encoding of the matching action tokens. Experiments on out-of-distribution generalization simulation benchmarks and a real-robot setup show that our Robust-WAM consistently improves the success rates of multiple WAM baselines without sacrificing in-distribution performance.

</details>

---

### [[20_Research/Papers/具身智能/XEWorld_Can_Action-Conditioned_World_Models_Generalize_to_Unseen_Robot_Embodiments|XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?]]

![[assets/2608.05799_figure.png|800]]

- **arXiv**: [2608.05799](https://arxiv.org/abs/2608.05799)
- **PDF**: https://arxiv.org/pdf/2608.05799
- **详细分析**: [[20_Research/Papers/具身智能/XEWorld_Can_Action-Conditioned_World_Models_Generalize_to_Unseen_Robot_Embodiments|XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?]]
- **作者**: Yixiang Chen, Jiabing Yang, Yuan Xu, Qisen Ma, Keji He, Peiyan Li, Kai Wang, Ziheng He, Xiangnan Wu, Jing Liu, Nianfeng Liu, Yan Huang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，世界模型 0.8，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《XEWorld: Can Action-Conditioned World Models Generalize to Unseen Robot Embodiments?》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：XEWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models are promising learned simulators for robotic manipulation, yet evaluating them exclusively on training robots fails to reveal whether they capture physical dynamics or merely memorize visual patterns. To answer whether a model can faithfully render a robot it has never seen, we introduce XEWorld, a controlled cross-embodiment testbed for world models that isolates embodiments by evaluating held-out robots within physically identical scenes. Our systematic analysis uncovers a shared architectural bottleneck: current models act primarily as 2D visual pattern matchers whose generalization is governed by visual similarity rather than physical kinematic similarity. Driven by this limitation, they struggle to translate abstract numeric joint actions into coherent visual trajectories, and fail to predict dynamic visual changes from static initial observations. Consequently, successfully rendering an unseen embodiment zero-shot strictly requires heavily grounded cues, specifically pixel-space actions and explicit spatial-temporal alignment. Even when bypassing this zero-shot barrier via few-shot adaptation, the forced appearance recovery triggers catastrophic forgetting of seen embodiments. Together, these failures expose a critical inability to apply learned physical dynamics to novel visual appearances, highlighting that achieving true cross-embodiment generalization requires architectural innovations that decouple visual appearance from underlying physical dynamics.

</details>

---

### [[20_Research/Papers/世界模型/PhyLatent_Learning_Dynamics-Relevant_Representations_for_JEPA_World_Models|PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models]]

![[assets/2608.05720_figure.png|800]]

- **arXiv**: [2608.05720](https://arxiv.org/abs/2608.05720)
- **PDF**: https://arxiv.org/pdf/2608.05720
- **详细分析**: [[20_Research/Papers/世界模型/PhyLatent_Learning_Dynamics-Relevant_Representations_for_JEPA_World_Models|PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models]]
- **作者**: Xi Zeng, Haojie Ren, Ziying Song
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: cs.CV

#### 研究背景与动机

《PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose PhyLatent, a dynamics-relevant training objective for JointEmbedding Predictive Architecture (JEPA) world models. Our key observation is that preventing global latent collapse does not ensure that a representation preserves physical states and action consequences. We identify three failure modes in JEPA world models: physical invariance collapse, physical identifiability collapse, and counterfactual dynamics collapse. PhyLatent addresses them through three training pathways: physical invariance, physical identifiability, and counterfactual dynamics, implemented with physical state grounding, future representation alignment, static visual invariance, counterfactual branch separation, and latent denoising. On OGBench-Cube, PhyLatent reduces the three failure rates from 15.60%, 6.71%, and 8.41% to 7.53%, 0.95%, and 4.62%, respectively, and improves model predictive control (MPC) success from 70.0% to 78.1%. With the same architecture and planner, it further improves success from 81.0% to 98.0% on TwoRooms and remains competitive on Reacher and PushT. These results show that global non-collapse alone is insufficient for learning a reliable JEPA worldmodel state space.

</details>

---

### [[20_Research/Papers/机器人/Iterative_Hybrid_Discrete-Continuous_Viewpoint_Planning_for_UAV_Photogrammetry|Iterative Hybrid Discrete-Continuous Viewpoint Planning for UAV Photogrammetry]]

![[assets/2608.05718_figure.png|800]]

- **arXiv**: [2608.05718](https://arxiv.org/abs/2608.05718)
- **PDF**: https://arxiv.org/pdf/2608.05718
- **详细分析**: [[20_Research/Papers/机器人/Iterative_Hybrid_Discrete-Continuous_Viewpoint_Planning_for_UAV_Photogrammetry|Iterative Hybrid Discrete-Continuous Viewpoint Planning for UAV Photogrammetry]]
- **作者**: Alan Grech, Daniel Pisani, Andre Grima, Carl James Debono, Saviour Formosa, Dylan Seychell
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Agent, ComputerVision, Systems

#### 研究背景与动机

《Iterative Hybrid Discrete-Continuous Viewpoint Planning for UAV Photogrammetry》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Viewpoint-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) photogrammetry requires camera networks that provide sufficient surface coverage, image overlap, parallax, and resolution, yet conventional flight patterns are often poorly adapted to scene geometry resulting in local reconstruction errors. This paper proposes an iterative hybrid discrete-continuous viewpoint planning method for targeted UAV photogrammetry from a proxy reconstruction. The method scores sampled surface points using photogrammetric heuristics based on frontality, imaging distance, parallax, and multi-view observation count, while also evaluating the full viewpoint set in terms of visibility, pairwise overlap, and graph connectivity. Candidate viewpoints are generated around weakly observed regions, refined using clustered Covariance matrix adaptation evolution strategy (CMA-ES) optimisation, and removed when redundant. The final flight path combines close-range detail viewpoints with wider model-coverage viewpoints, balancing local reconstruction quality with global image-network robustness. Evaluation on three synthetic scenes shows that the proposed method improves both reconstruction accuracy and completeness compared with prior UAV path-planning methods.

</details>

---

### [[20_Research/Papers/具身智能/LAWM-3D_Learning_3D-Aware_Latent_Actions_from_Human_Videos_for_Generalizable_Robot_World_Models|LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models]]

![[assets/2608.05706_figure.png|800]]

- **arXiv**: [2608.05706](https://arxiv.org/abs/2608.05706)
- **PDF**: https://arxiv.org/pdf/2608.05706
- **详细分析**: [[20_Research/Papers/具身智能/LAWM-3D_Learning_3D-Aware_Latent_Actions_from_Human_Videos_for_Generalizable_Robot_World_Models|LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models]]
- **作者**: Jiarui Yang, Jiale Zhange, Jiawei Li, Hang Guo, Wen Huang, Jinpeng Wang, Peidong Liu, Shu-Tao Xia
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.2，世界模型 1，机器人 0.8）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《LAWM-3D: Learning 3D-Aware Latent Actions from Human Videos for Generalizable Robot World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FantasyWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models enable agents to perform forward rollout and planning without real-world interaction. However, their application in open-world embodied intelligence remains limited by the high cost of action annotations and the heterogeneity of action spaces across platforms. Recently, latent action models (LAMs) have alleviated this bottleneck by learning action representations directly from unlabeled human videos in a self-supervised manner. Nevertheless, most existing LAMs rely on single-view inputs and operate primarily in 2D pixel space, raising a fundamental question: can simply incorporating multi-view videos into LAM training endow the learned latent actions with 3D-aware perception? Our study shows that the answer is negative. The primary reasons lie in future-frame appearance leakage as well as inter-camera appearance discrepancies and viewpoint variations. To address these issues, we propose LAWM-3D, which introduces three tightly coupled key designs: (1) a multi-view invariant unified action tokenization scheme for learning 3D-aware latent actions; (2) a geometric alignment constraint that anchors intermediate encoder features to a pretrained 3D foundation model, thereby explicitly providing cross-view geometric correspondences; and (3) a non-injective RGB-D joint reconstruction objective that prevents shortcut learning from future-frame appearance information, forcing the LAM to focus supervision on motion cues with geometric significance. Importantly, these components are not simply stacked but are tightly coupled through a unified motivation. Built upon a two-stage paradigm of large-scale human video pretraining followed by robot fine-tuning, extensive experiments demonstrate that the proposed 3D-aware latent actions significantly improve world model performance, achieving SOTA results in generation quality, physical consistency, and generalization ability.

</details>

---

### [[20_Research/Papers/多模态技术/Dual-Attention_and_Adversarial_Transfer_Networks_for_Sim-to-Real_Cross-Orientation_Wireless_Sensing|Dual-Attention and Adversarial Transfer Networks for Sim-to-Real Cross-Orientation Wireless Sensing]]

![[assets/2608.05664_figure.png|800]]

- **arXiv**: [2608.05664](https://arxiv.org/abs/2608.05664)
- **PDF**: https://arxiv.org/pdf/2608.05664
- **详细分析**: [[20_Research/Papers/多模态技术/Dual-Attention_and_Adversarial_Transfer_Networks_for_Sim-to-Real_Cross-Orientation_Wireless_Sensing|Dual-Attention and Adversarial Transfer Networks for Sim-to-Real Cross-Orientation Wireless Sensing]]
- **作者**: Linfeng Du, Kehan Wu, Tong Zhang, Rui Wang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.9）
- **关联关键词**: Security, Systems

#### 研究背景与动机

《Dual-Attention and Adversarial Transfer Networks for Sim-to-Real Cross-Orientation Wireless Sensing》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DANet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Millimeter-wave human activity recognition suffers significant performance degradation when the user's orientation changes relative to the sensing system, yet collecting labeled multi-orientation data is labor-intensive and costly. To eliminate the need for exhaustive multi-orientation measured data, we develop a physics-guided simulator that synthesizes orientation-diverse wireless training data from single-orientation motion. Specifically, to suppress orientation-induced feature variations, we propose a dual-attention network that extracts activity-discriminative and orientation-robust representations from dual-link Doppler spectrograms. To bridge the simulation-to-reality gap, we introduce an adversarial unsupervised transfer learning mechanism that aligns feature distributions using only a small number of unlabeled target-domain samples. The S2M-Sense platform shows high fidelity in reproducing real-world signatures, validated against 60.48 GHz mmWave measured data with an average structural similarity index measure (SSIM) of 0.84 between simulated and measured Doppler spectrograms across all 4 activities and 4 orientations. Experimental results show that S2M-Sense achieves 88.33% recognition accuracy using only the dual-link multi-orientation simulated dataset, which improves to 95% after simulation-to-reality transfer learning with as few as 16 unlabeled measured samples. Both cases with and without transfer learning outperform state-of-the-art cross-domain sensing methods.

</details>

---

### [[20_Research/Papers/具身智能/Uncertainty-Aware_World_Model_for_Aerial_Image-Goal_Navigation|Uncertainty-Aware World Model for Aerial Image-Goal Navigation]]

![[assets/2608.05597_figure.png|800]]

- **arXiv**: [2608.05597](https://arxiv.org/abs/2608.05597)
- **PDF**: https://arxiv.org/pdf/2608.05597
- **详细分析**: [[20_Research/Papers/具身智能/Uncertainty-Aware_World_Model_for_Aerial_Image-Goal_Navigation|Uncertainty-Aware World Model for Aerial Image-Goal Navigation]]
- **作者**: Deyi Zhu, Haoyu Fan, Yinan Zhu, Weichen Zhang, Shilin Ma, Xinlei Chen, Yansong Tang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.2（加权：世界模型 1，机器人 0.2）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《Uncertainty-Aware World Model for Aerial Image-Goal Navigation》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial image-goal navigation requires an unmanned aerial vehicle (UAV) to reach a target location specified by a goal image. Existing world-model-based methods rank candidate trajectories using predicted futures, but typically rely on only one or a few point predictions, which is inadequate for large-scale outdoor environments with substantial future-state uncertainty. To address this limitation, we propose the Uncertainty-Aware Navigation World Model (UA-NWM), an efficient latent world model for aerial image-goal navigation, which formulates trajectory scoring as conditional out-of-distribution detection. UA-NWM represents plausible futures with an uncertainty subspace and decomposes the prediction--goal discrepancy into uncertainty-explainable and unexplainable components. Only the unexplainable residual is used for scoring, enabling robust selection without multiple future samples. Extensive experiments demonstrate that UA-NWM consistently outperforms existing navigation world models while maintaining low inference latency. Real-world UAV experiments further validate its practical applicability. Project page: https://duryi.github.io/UA-NWM-Project-Page

</details>

---

### [[20_Research/Papers/世界模型/HERA_Historical_Evidence_Routing_Adapter_for_Physical_Prediction_in_Latent_World_Models|HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models]]

![[assets/2608.05523_figure.png|800]]

- **arXiv**: [2608.05523](https://arxiv.org/abs/2608.05523)
- **PDF**: https://arxiv.org/pdf/2608.05523
- **详细分析**: [[20_Research/Papers/世界模型/HERA_Historical_Evidence_Routing_Adapter_for_Physical_Prediction_in_Latent_World_Models|HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models]]
- **作者**: Yuanruyi, Yue Cao, Haojia Gao, Guanqiu Guo, Ziyuezhang, Shangqin, Junbo Tan, Bokui Chen, Zhuo Zou, Xueqian Wang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《HERA: Historical Evidence Routing Adapter for Physical Prediction in Latent World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predictive video models have emerged as promising world models by learning latent visual dynamics from large-scale video. Yet these models remain challenged by physical events under occlusion, where later predictions may depend on object evidence that is no longer available in the current view. Addressing this challenge requires historical evidence not only to be preserved but also to remain accessible when it becomes relevant to a subsequent prediction. Existing approaches mainly enlarge the temporal context, cache generic video features, or impose explicit object-centric states, thereby improving the capacity or structure of retained history. However, they do not directly address how relevant historical evidence can be selectively retrieved and integrated into a pretrained predictor without interfering with its native latent workspace. Accordingly, we introduce HERA (Historical Evidence Routing Adapter), a framework for routing retained historical evidence into a frozen latent predictor, and instantiate it with Register-Routed Patch Memory (RRPM), a lightweight adapter comprising a Structured Memory Bank, Memory Registers, and Workspace Registers. On the IntPhys2 Main split, HERA with RRPM improves the pairwise AvgSurprise accuracy of V-JEPA 2-G from 52.57% to 54.35%. Subgroup analysis shows particularly strong improvements on fixed-camera continuity, from 46.15% to 57.69%, and fixed-camera immutability, from 46.15% to 63.46%. These results support historical evidence routing as a practical adaptation strategy for physical prediction in latent world models.

</details>

---

### [[20_Research/Papers/具身智能/World-to-Wrist_Task-Conditioned_Future_Wrist_Modeling_for_Fine-Grained_Robot_Manipulation|World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation]]

![[assets/2608.05369_figure.png|800]]

- **arXiv**: [2608.05369](https://arxiv.org/abs/2608.05369)
- **PDF**: https://arxiv.org/pdf/2608.05369
- **详细分析**: [[20_Research/Papers/具身智能/World-to-Wrist_Task-Conditioned_Future_Wrist_Modeling_for_Fine-Grained_Robot_Manipulation|World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation]]
- **作者**: Yuhao Pan, Haosong Peng, Zhengshen Zhang, Zhengyang Yan, Yalun Dai, Fushuo Huo, Chujie Wang, Tianyu Qi, Xiucheng Wang, Nan Cheng, Wenchao Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.4（加权：具身智能 2.1，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamVLA, GraphCoT-VLA, LaRA-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context. To address this limitation, we present World-to-Wrist VLA (W2-VLA), a VLA model for fine-grained robot manipulation with task-conditioned future wrist modeling. Given current multi-view observations and a task instruction, W2-VLA contextualizes a set of latent modeling tokens as a compact interface between the vision-language model and the wrist predictor. Conditioned on this interface and the observed wrist history, the predictor forecasts future wrist latents, which are transformed into future-aware context for action prediction. In addition, we introduce W2-CoT, a synthesis pipeline that produces structured annotations describing manipulation progress, physical transition cues, and wrist-local evidence. These annotations provide auxiliary supervision that shapes the task-conditioned latent interface. Experiments on LIBERO, RoboTwin 2.0, and real-world manipulation tasks demonstrate improved fine-grained and contact-sensitive manipulation across both single-arm and bimanual settings, while maintaining action-generation rates above 80 Hz.

</details>

---

### [[20_Research/Papers/大模型/VLAff_Vision-Language-Affordance_Model_for_Unified_Actionable_Affordances|VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances]]

![[assets/2608.05215_figure.png|800]]

- **arXiv**: [2608.05215](https://arxiv.org/abs/2608.05215)
- **PDF**: https://arxiv.org/pdf/2608.05215
- **详细分析**: [[20_Research/Papers/大模型/VLAff_Vision-Language-Affordance_Model_for_Unified_Actionable_Affordances|VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances]]
- **作者**: Jihoon Oh, Kento Kawaharazuka, Kei Okada
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning manipulation skills from human videos is promising for scalable robot learning. However, the embodiment mismatch between humans and robots makes this challenging. One promising solution is to learn object-centric actionable affordances that are embodiment-agnostic. In this work, we propose a framework that leverages egocentric human videos with state-of-the-art 3D Structure-from-Motion and hand mesh reconstruction to extract actionable affordances such as visual, grasp, and trajectory affordances that explicitly encode where to interact, how to grasp, and how to move. We construct EgoAffordance, a large-scale dataset comprising 204K episodes with 5.6M visual affordances and 11.6M grasp and trajectory affordances. Building on this, we introduce VLAff, a large vision-language model-based unified foundation model that learns cross-modal correlations across all actionable affordances. Given a visual observation and instruction, VLAff generates visual affordance heatmaps, grasp poses, and trajectories, which are then converted into directly executable actions by utilizing 3D scene information. Through extensive experiments, we demonstrate that VLAff not only achieves state-of-the-art performance on visual affordance prediction, but can also be effectively applied to real robot applications such as zero-shot manipulation and affordance-guided robot learning.

</details>

---
