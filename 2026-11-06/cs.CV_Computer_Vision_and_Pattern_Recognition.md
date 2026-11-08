# cs.CV | Computer Vision and Pattern Recognition | 2026-11-06

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/机器人/VFlash_Fast,_Accurate_Visual_Planning_via_Flash_Primitive_Decoding|VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding]]

![[assets/2611.08449_figure.png|800]]

- **arXiv**: [2611.08449](https://arxiv.org/abs/2611.08449)
- **PDF**: https://arxiv.org/pdf/2611.08449
- **详细分析**: [[20_Research/Papers/机器人/VFlash_Fast,_Accurate_Visual_Planning_via_Flash_Primitive_Decoding|VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding]]
- **作者**: Yu-Cheng Chou, Shihao Wang, Jin Huang, Chi-Pin Huang, Chiao-An Yang, Xianzhe Fan, Jing Wang, Zhiqi Li, Yuanguo Kuang, Ruijie Zheng, Johan Bjorck, Sifei Liu...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly. We introduce VFlash, a method for fast, accurate visual planning through Flash Primitive Decoding. VFlash exploits the known structure of visual primitives to predict their coordinates jointly, using a lightweight drafter that generates an entire primitive in one forward pass. The layout adapts to the primitive's type, dimensionality, and length, supporting compact boxes and long, variable-length trajectories. Crucially, spatial accuracy need not require reproducing an autoregressive model's exact token sequence. VFlash therefore trains on annotated primitives and directly accepts structurally valid predictions without target-token agreement. Across the evaluated 2D and 3D robot trajectory tasks, VFlash consistently reduces prediction errors relative to autoregressive decoding. Preliminary single-rollout measurements indicate approximately 25x faster generation for 3D point motion forecasting. A world action model conditioned on VFlash plans achieves 70.2% average success across four MolmoSpaces task suites, compared with 62.6% for the baseline.

</details>

---

### [[20_Research/Papers/具身智能/T3R_Training-Free_Two-Stage_Token_Refinement_Towards_Efficient_and_Robust_VLA_Models|T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models]]

![[assets/2611.08413_figure.png|800]]

- **arXiv**: [2611.08413](https://arxiv.org/abs/2611.08413)
- **PDF**: https://arxiv.org/pdf/2611.08413
- **详细分析**: [[20_Research/Papers/具身智能/T3R_Training-Free_Two-Stage_Token_Refinement_Towards_Efficient_and_Robust_VLA_Models|T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models]]
- **作者**: Mohammed Hassan, Zhenyang Chen, Zheng Wang, Zhixin Zhu, Tianlong Chen, Yingyan, Lin, Chaojian Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EfficientVLA, LightVLA, OpenVLA, TeamVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable end-to-end robot control, but inference is increasingly expensive. Each decision processes hundreds of visual tokens, often across multiple cameras, leading to substantial computation while allowing irrelevant background content to distract action prediction under distribution shift. We argue that these issues stem from two complementary forms of redundancy: many visual tokens are spatially irrelevant, while attention over the remaining tokens is often misallocated. Based on this observation, we propose T3R, a Training-Free Two-Stage Token Refinement framework. In the first stage, segmentation-guided token pruning removes irrelevant visual patches to reduce computation and eliminate distracting context. In the second stage, saliency-guided attention biasing reallocates attention toward action-critical visual regions and language instructions within the retained tokens. Together, pruning produces a cleaner candidate set, while attention biasing further emphasizes the most decision-relevant evidence, yielding a better accuracy-efficiency frontier than either stage alone. On LIBERO-Spatial, T3R removes 85% of scene-camera visual tokens while essentially matching the unpruned success rate, and improves success by up to 7 percentage points under out-of-distribution object-placement perturbations. The timing comparison attributes 7.8 ms per inference call to pruning and attention-bias application. As input resolution increases, LLM-forward profiling shows up to a 3.3x speedup over the unpruned baseline. Evaluations across LIBERO, SIMPLER, and RoboTwin with three VLA backbones show the strongest accuracy-efficiency benefits in multi-camera settings. These results demonstrate that training-free token refinement is a practical approach to efficient and robust VLA inference.

</details>

---

### [[20_Research/Papers/强化学习/Social_Humanoid_Socially_Responsive_Human-Humanoid_Interaction|Social Humanoid: Socially Responsive Human-Humanoid Interaction]]

![[assets/2611.08407_figure.png|800]]

- **arXiv**: [2611.08407](https://arxiv.org/abs/2611.08407)
- **PDF**: https://arxiv.org/pdf/2611.08407
- **详细分析**: [[20_Research/Papers/强化学习/Social_Humanoid_Socially_Responsive_Human-Humanoid_Interaction|Social Humanoid: Socially Responsive Human-Humanoid Interaction]]
- **作者**: Vongani H. Maluleke, James Ni, Kie Horiuchi, Lea Wilken, Jiahui Lei, Evonne Ng, Roei Herzig, Jitendra Malik, Trevor Darrell, Angjoo Kanazawa
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Social Humanoid: Socially Responsive Human-Humanoid Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MAGNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots are typically trained as solitary agents, leaving them unable to coordinate physically with human partners who naturally anticipate and adjust to one another. To bridge this gap, we present Social Humanoid, a hierarchical system that generates and executes socially responsive whole-body motion on a 29-DoF Unitree G1 conditioned on a human partner's motion. Its high-level policy performs flexible sequence modeling of human and humanoid motion through a shared tokenized representation, generating reactive humanoid motion and anticipating the partner's motion when they are occluded, while a low-level whole-body tracking controller executes the generated motion on the robot. To train the system, we introduce a two-phase adaptive retargeting procedure that retargets one interaction partner to the robot while morphing the other partner to preserve contact dynamics, reachability, and relative body scale. We apply this procedure across five motion-capture datasets to produce a new Human-Humanoid Interaction (HHI) benchmark of 260 hours of human-humanoid interactions. Our results demonstrate that Social Humanoid produces coordinated, human-aligned behavior across diverse interaction types in simulation and the real world. Project page: https://von31.github.io/social-humanoid/

</details>

---

### [[20_Research/Papers/强化学习/FewStepRL_Fine-tuning_Few-step_Diffusion_Models_with_Reinforcement_Learning|FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning]]

![[assets/2611.08240_figure.png|800]]

- **arXiv**: [2611.08240](https://arxiv.org/abs/2611.08240)
- **PDF**: https://arxiv.org/pdf/2611.08240
- **详细分析**: [[20_Research/Papers/强化学习/FewStepRL_Fine-tuning_Few-step_Diffusion_Models_with_Reinforcement_Learning|FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning]]
- **作者**: Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, Tailin Wu
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FewStepRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become a standard post-training method for diffusion models, but most RL objectives roll out the current policy at every iteration, and with a many-step sampler these rollouts typically dominate the cost of training. Few-step models cut this cost, yet they model an average velocity over an interval, whereas existing RL objectives are built for an instantaneous velocity with a many-step sampler. We adapt RL objectives to few-step models systematically in three phases, namely a transformation, a decomposition and an adaptation. The transformation to $x$-space expresses each objective we consider through a common policy prediction, at the clean end by default and at an explicitly marked level for transition or flow-map objectives, so that objectives stated over densities, velocities or rewards become comparable. The decomposition writes the gradient of each of these objectives as the sum of a self-regression toward a reference and a reward augmentation, so that a method reduces, at the gradient level, to a choice of anchors and weights. The adaptation computes each anchor from a few-step model at the end of its transport or along its tangent, with the instantaneous velocity recovered from the network itself or from an auxiliary network. This yields few-step versions of FlowGRPO, AWM, DiffusionNFT, DiffusionOPSD and ReFL in one modular codebase. In our experiments, reward-gradient-based methods are the most effective when the reward is differentiable and its gradient is affordable; otherwise DiffusionNFT-style methods generally reach high rewards in relatively few iterations despite a sometimes higher per-iteration cost. Extra inference steps show no systematic aggregate benefit in our experiments, although selected outputs visibly improve with two to four times as many sampling steps as in training.

</details>

---

### [[20_Research/Papers/具身智能/La-JEPA_Compact_Robot_Policies_with_Latent_World_Modeling|La-JEPA: Compact Robot Policies with Latent World Modeling]]

![[assets/2611.08156_figure.png|800]]

- **arXiv**: [2611.08156](https://arxiv.org/abs/2611.08156)
- **PDF**: https://arxiv.org/pdf/2611.08156
- **详细分析**: [[20_Research/Papers/具身智能/La-JEPA_Compact_Robot_Policies_with_Latent_World_Modeling|La-JEPA: Compact Robot Policies with Latent World Modeling]]
- **作者**: Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang, Tongtong Cao, Zhanguang Zhang, Yingxue Zhang
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《La-JEPA: Compact Robot Policies with Latent World Modeling》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：JEPA-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. It remains unclear how much these generation-oriented choices affect control. In this work, we introduce Latent Action JEPA (La-JEPA), a compact world-action model whose policy transformer is trained from scratch in the feature space of a pretrained V-JEPA 2.1 encoder. Following Fast-WAM, La-JEPA learns to predict future features jointly with actions during training and generates only actions at inference. Among policies without embodied pretraining, La-JEPA achieves state-of-the-art performance in clean and randomized RoboTwin 2.0 scenes and on LIBERO-Plus with correct instructions, while using far fewer parameters than the strongest competing policies. It runs substantially faster than Fast-WAM at comparable performance and outperforms the closest JEPA-based methods, LeapBot-WA and JEPA-WAM, on LIBERO-Plus and RoboTwin 2.0 without their pretrained policy backbones. On four real-robot tasks, its average success is comparable to pi0.5 and above non-embodied-pretrained baselines. Through a design study of the choices behind La-JEPA, we show that JEPA features outperform video VAE latents, most clearly out of distribution, and that training-time future prediction choices significantly impact the policy even when future prediction is skipped at inference. We correct the LIBERO-Plus instructions, as the officially released evaluator corrupts them for most variants, and re-evaluate several strong open baselines. Without a generative pretrained policy backbone, La-JEPA is better and faster than far larger policies, suggesting that robot foundation models may benefit from architectures designed for control rather than inherited from generation.

</details>

---

### [[20_Research/Papers/大模型/WAM-Sim0.1_World_Anchored_Memory_Meets_Online_RL_for_Consistent_and_Realistic_Driving_Simulation|WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation]]

![[assets/2611.07939_figure.png|800]]

- **arXiv**: [2611.07939](https://arxiv.org/abs/2611.07939)
- **PDF**: https://arxiv.org/pdf/2611.07939
- **详细分析**: [[20_Research/Papers/大模型/WAM-Sim0.1_World_Anchored_Memory_Meets_Online_RL_for_Consistent_and_Realistic_Driving_Simulation|WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation]]
- **作者**: Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan, Quanhui Tang, Jianhua Han, Lin Cheng, Hang Xu, Siyu Zhu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.2，强化学习 0.2，世界模型 0.4）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation》归入 世界模型、大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLVR-World, WAM-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive driving world models systematically suffer from structural drift, identity drift, and quality decay over long rollout horizons due to transient conditioning signals that lack persistent state. We present WAM-Sim, a driving world model anchored by a persistent hierarchical memory and optimized via online flow-matching RL. WAM-Sim structures persistent context across three temporal and semantic scales: pose-aligned structural tokens encoding persistent road topology, read-only scene tokens supplying geolocated background appearance, and write-once instance tokens preserving individual traffic participant identities across occlusions and chunk boundaries. To restore visual sharpness and physical plausibility degraded by multi-scale conditioning, we introduce an online post-training framework that optimizes self-generated rollouts via flow-matching RL guided by hierarchy-aligned visual rewards and a vision-language model physical judge. The invariant memory empirically confines policy optimization within the anchored context, helping suppress semantic collapse and reward hacking, while online RL systematically enforces physical commonsense and fine-grained visual fidelity. On the nuScenes benchmark, WAM-Sim achieves a superior generation fidelity (FID=3.47, FVD=25.72) and strong downstream perception performance (24.16 mAP, 71.23 road mIoU). On minute-scale rollouts of self-collected data, WAM-Sim substantially mitigates structural and identity drift, preserving high scene similarity and subject identity coherence across extended horizons. Project page: https://fudan-generative-vision.github.io/WAM-Sim.

</details>

---

### [[20_Research/Papers/大模型/Learning_Robotic_World_Models_with_Semantic_and_Visual_Feedback|Learning Robotic World Models with Semantic and Visual Feedback]]

![[assets/2611.07850_figure.png|800]]

- **arXiv**: [2611.07850](https://arxiv.org/abs/2611.07850)
- **PDF**: https://arxiv.org/pdf/2611.07850
- **详细分析**: [[20_Research/Papers/大模型/Learning_Robotic_World_Models_with_Semantic_and_Visual_Feedback|Learning Robotic World Models with Semantic and Visual Feedback]]
- **作者**: Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo, Yu Cheng, Bo An, Yingli Tian, Laszlo A. Jeni, Ming-Hsuan Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，世界模型 0.8，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Learning Robotic World Models with Semantic and Visual Feedback》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRASim, RLVR-World, VBench, Vid2World, WorldModelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot world models predict action-conditioned future visual states to support robotic planning and decision making. However, visual reconstruction does not fully capture task progress, semantic evaluation alone provides limited constraints on fine-grained visual errors, and homogeneous predictions limit comparative feedback. We present RoboImagine, a framework for post-training autoregressive robotic world models through candidate-future comparisons with semantic and visual feedback. Diverse search promotes diversity among candidate trajectories under shared visual observations, action sequences, and task instructions. A frozen multimodal evaluator provides task-relevant semantic preferences through pairwise video comparisons in both presentation orders, complemented by pixel- and perceptual-level visual consistency feedback that constrains local structural and appearance errors. These signals drive policy optimization through group-relative advantages. Fixed initial context and branch-specific rolling histories support long-sequence generation with bounded context and consistent conditioning between candidate generation and policy optimization. Experiments with separately trained models on RT-1, BridgeV2, and RoboCasa cover real-world and simulated manipulation. On RT-1, under matched initialization, update counts, and evaluation protocols, RoboImagine improves PSNR by 1.26 dB and reduces LPIPS by 11.93% relative to continued supervised fine-tuning. Ablations show that diverse search improves prediction quality and that combined semantic and visual feedback yields higher external multimodal evaluation scores than visual feedback alone while maintaining comparable visual fidelity. Rolling histories further improve long-horizon prediction. These results support improving visual fidelity, task relevance, and long-horizon prediction through candidate comparison and complementary feedback.

</details>

---

### [[20_Research/Papers/机器人/FlyingDrones_A_Dataset_and_Benchmark_for_Optical_Flow_Estimation_from_UAV_motion|FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion]]

![[assets/2611.07705_figure.png|800]]

- **arXiv**: [2611.07705](https://arxiv.org/abs/2611.07705)
- **PDF**: https://arxiv.org/pdf/2611.07705
- **详细分析**: [[20_Research/Papers/机器人/FlyingDrones_A_Dataset_and_Benchmark_for_Optical_Flow_Estimation_from_UAV_motion|FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion]]
- **作者**: Laurenz Ruzicka, Roman Pflugfelder, Daniel Cremers
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FastFlowNet, FlowNet, LiteFlowNet, PWC-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Optical flow is an important cue for drone analysis in aerial surveillance, airspace monitoring, and long-range target tracking, where motion remains informative when appearance is weak. Estimating the motion of small Unmanned Aerial Vehicles, however, is difficult because distant targets occupy few pixels, have low contrast, and move against complex dynamic backgrounds. Standard optical-flow benchmarks emphasize large, object-centric motions and therefore do not characterize distant aerial targets well. We introduce FlyingDrones, a generated benchmark with dense ground-truth optical flow and segmentation masks derived from physically based rendering, and define resolution-normalized metrics (EPE Norm) that normalize flow by image dimensions. We evaluate 16 state-of-the-art model families on a motion- and size-stratified subset of 999 flow pairs at three resolutions. Every family recovers drone motion better than the zero-flow reference, but the gap between families widens with resolution: at 1920x1080, global-matching, recurrent, transformer, and short-window temporal models separate clearly from pyramid, classical, self-supervised, lightweight, and diffusion models. Within-family checkpoint spread is comparable to or larger than between-family spread, so the training curriculum is as important as the architecture. Two complementary studies test the benchmark beyond synthetic accuracy: a ground-truth-free motion-alignment evaluation on 21 cameras of real UAV footage shows that the synthetic ranking carries a moderate, significant signal about real-world performance (Spearman \r{ho} = 0.63 over 41 checkpoints) while the exact top ranks differ, and a fine-tuning study shows that 800 FlyingDrones pairs reduce held-out drone-region error by up to 37% and improve drone localization on the real footage for all four architectures tested.

</details>

---

### [[20_Research/Papers/强化学习/RLGPA_A_Reinforcement_Learning-Guided_Granularity_Planning_Attack_for_Decision-Based_Sparse_Adversarial_Examples|RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples]]

![[assets/2611.07512_figure.png|800]]

- **arXiv**: [2611.07512](https://arxiv.org/abs/2611.07512)
- **PDF**: https://arxiv.org/pdf/2611.07512
- **详细分析**: [[20_Research/Papers/强化学习/RLGPA_A_Reinforcement_Learning-Guided_Granularity_Planning_Attack_for_Decision-Based_Sparse_Adversarial_Examples|RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples]]
- **作者**: Chao Zhou, Shenghua He, Jiaxin Mo, Qiangguo Yu, Fengchuang Xing
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decision-based sparse attacks must reduce perturbation support using only the victim's predicted label. The best restoration strategy varies as support contracts: coarse removal works early, while tail states need finer, history-aware tests. We propose RLGPA, an online reinforcement learning method that schedules support-reduction executors and their granularity under a hard query budget. A masked Dueling Double DQN selects among seven stable policy--scale actions; each action produces support-relative restoration groups that are rebuilt after every macro decision. A feasibility-preserving executor commits only adversarial restorations and feeds support gain and query cost back to the planner. Under the matched top-1-label oracle, RLGPA reaches 61\% targeted ASR at sparsity 0.01 on CIFAR-10 (vs. 25\% SparseEvo, 0\% Pointwise), and 75.5\%/73.0\% on ResNet50/ViT at sparsity 0.005 (vs. 29.0\%/15.5\%). A fixed-probe test reduces median \(L_0\) from 165 to 23 after 40 images without any update. State-blind and state-shuffled controls degrade significantly, confirming that the learned policy uses attack state; the main gains come from state-conditioned executor scheduling and dynamic repartition. The source code is publicly available at https://github.com/Acui001/RLGPA.git.

</details>

---

### [[20_Research/Papers/具身智能/MessyNav_Zero-Shot_Navigation_via_Manipulation_in_Messy_Environments|MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments]]

![[assets/2611.07417_figure.jpeg|800]]

- **arXiv**: [2611.07417](https://arxiv.org/abs/2611.07417)
- **PDF**: https://arxiv.org/pdf/2611.07417
- **详细分析**: [[20_Research/Papers/具身智能/MessyNav_Zero-Shot_Navigation_via_Manipulation_in_Messy_Environments|MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments]]
- **作者**: Kenneth Llontop, Cherie Ho, Dylan Zhou, Anuva Banwasi, Priya Sundaresan, Carlota Parés-Morlans, Jeannette Bohg
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world environments are messy, with paths often blocked by everyday objects like chairs and toys, requiring robots to perform interactive navigation by manipulating obstacles to clear a path. Existing methods rely on extensive simulation-based learning or per-scene instructions specifying which objects to avoid or manipulate. They struggle to generalize across novel objects, diverse environments, and varied contexts such as a cart of fragile glassware that should be avoided while an empty one can be pushed. We formalize this problem as open-world interactive navigation and present MessyNav, a zero-shot framework based on vision-language models (VLMs). At its core, MessyNav performs explicit VLM-based affordance reasoning before task planning to decide whether to swipe, pick up, or avoid an object and produce a high-level plan. Evaluated on a mobile manipulator across real-world indoor and outdoor environments, MessyNav improves success rate by 27 percentage points (pp) over the strongest baseline in real-robot trials and achieves statistically significant gains in a larger-scale offline evaluation, without task-specific training.

</details>

---

### [[20_Research/Papers/具身智能/Kinematic_Hypothesis_Context_Embodiment-Conditioned_Learned_Video_Coding_for_Bandwidth-Limited_Robot_Policy_Uplinks|Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks]]

![[assets/2611.07411_figure.png|800]]

- **arXiv**: [2611.07411](https://arxiv.org/abs/2611.07411)
- **PDF**: https://arxiv.org/pdf/2611.07411
- **详细分析**: [[20_Research/Papers/具身智能/Kinematic_Hypothesis_Context_Embodiment-Conditioned_Learned_Video_Coding_for_Bandwidth-Limited_Robot_Policy_Uplinks|Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks]]
- **作者**: Yuze Lu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Kinematic Hypothesis Context: Embodiment-Conditioned Learned Video Coding for Bandwidth-Limited Robot Policy Uplinks》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots increasingly run large vision-language-action policies on remote servers, making the camera uplink the bottleneck. Existing video codecs spend bits on content the receiver could predict: the robot's own motion. We introduce the kinematic hypothesis context, a zero-rate conditioning signal that both ends build from joint states, the robot model and the camera calibration. Ego-motion homographies, per-link robot reprojections, an end-effector plane and a background memory warp the previous reconstruction into hypotheses that condition a learned video codec. We prove that history-only and global-pose conditioning with a limited receptive field cannot access this information under large motion, and that coding gains become task gains at the policy's success cliff. On LIBERO, the context saves 23.9% bit rate over a capacity-matched history-conditioned codec and 40-56% over x264, x265 and SVT-AV1, and needs 23.2% fewer bits than DCVC-RT at equal policy action deviation; trained to lower rates, it matches DCVC-RT in PSNR. In closed loop at equal rate, OpenVLA-OFT success nearly doubles from 22.8% to 43.1% at 6 kbps (72.6% with lower-rate training, 23.6 points above DCVC-RT), pi_0.5 success rises from 55.5% to 77.4%, and the gain grows under packet loss. The context transfers across three codec hosts and to real robot data.

</details>

---
