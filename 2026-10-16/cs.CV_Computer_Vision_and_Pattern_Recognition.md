# cs.CV | Computer Vision and Pattern Recognition | 2026-10-16

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/大模型/Perceive,_Predict,_and_Plan_a_Unified_World_Action_Model_for_Egocentric_Dexterous_Manipulation|Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation]]

![[assets/2610.22363_figure.png|800]]

- **arXiv**: [2610.22363](https://arxiv.org/abs/2610.22363)
- **PDF**: https://arxiv.org/pdf/2610.22363
- **详细分析**: [[20_Research/Papers/大模型/Perceive,_Predict,_and_Plan_a_Unified_World_Action_Model_for_Egocentric_Dexterous_Manipulation|Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation]]
- **作者**: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.5，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EgoSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce P$^{3}$-WAM, a unified world action model for egocentric dexterous manipulation that learns 3D perception, action-conditioned prediction, and goal-directed planning through three complementary modes: Perceive, which reconstructs articulated hand motion and camera trajectories from video; Predict, which generates visual futures under prescribed actions; and Plan, which jointly generates action trajectories and their anticipated visual consequences conditioned on an initial image, a language instruction, and an optional visual goal. Our model integrates a compact, structured 3D action representation into a pretrained video diffusion transformer through a mixture-of-transformers architecture with shared base weights, modality-specific adaptation, and bidirectional visual-action attention. Randomized modality visibility lets video and 3D actions serve as either conditioning context or prediction targets across the three modes. Experiments show that unified training improves all three capabilities over single-mode training, including gains in planning quality under a vision-language model evaluation. Through unified training, our model outperforms specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, while producing goal-directed manipulation videos with stronger instruction adherence and action progression than video-generation baselines. Project Page: https://p3-wam.pages.dev/

</details>

---

### [[20_Research/Papers/强化学习/Routing_Policy_Optimization_for_Online_Diffusion_Reinforcement_Learning|Routing Policy Optimization for Online Diffusion Reinforcement Learning]]

![[assets/2610.22282_figure.png|800]]

- **arXiv**: [2610.22282](https://arxiv.org/abs/2610.22282)
- **PDF**: https://arxiv.org/pdf/2610.22282
- **详细分析**: [[20_Research/Papers/强化学习/Routing_Policy_Optimization_for_Online_Diffusion_Reinforcement_Learning|Routing Policy Optimization for Online Diffusion Reinforcement Learning]]
- **作者**: Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Routing Policy Optimization for Online Diffusion Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reverse denoising trajectory, leading to costly rollout-based optimization. We instead ask whether stochastic exploration can be introduced inside the generator while preserving its original sampler. Routing Policy Optimization (RPO) answers this question by turning attention routing into a stochastic exploration action. At a few selected denoising levels, each query block keeps its own block and samples further key blocks in proportion to the generator's native attention mass, or keeps dense attention. The sampled route perturbs the velocity of that transition, and a Gaussian likelihood around the dense velocity scores the perturbation with a score-function objective. RPO further uses a controlled two-rollout estimator: two rollouts share the same prompt, initial latent, routed denoising levels, and dense anchor layers, differing only in their sampled attention routes. Their reward difference provides an advantage signal for the routed transitions. Because the likelihood differentiates the dense velocity itself, the learned updates remain effective after routing is removed. At inference, RPO restores dense attention and retains the original deterministic sampler. Experiments on text-to-image and text-to-video generation show that RPO improves generation quality while achieving nearly 4x higher training efficiency than Flow-GRPO-style methods. Please see our project page at https://velox-world.com/rpo for visual results.

</details>

---

### [[20_Research/Papers/大模型/MMSearch-OPD_Easy_Made_Hard,_Hard_Made_Learnable_for_Long-Horizon_Multimodal_Search_Agents|MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents]]

![[assets/2610.22240_figure.png|800]]

- **arXiv**: [2610.22240](https://arxiv.org/abs/2610.22240)
- **PDF**: https://arxiv.org/pdf/2610.22240
- **详细分析**: [[20_Research/Papers/大模型/MMSearch-OPD_Easy_Made_Hard,_Hard_Made_Learnable_for_Long-Horizon_Multimodal_Search_Agents|MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents]]
- **作者**: Huanyao Zhang, Jiepeng Zhou, Jiaye Lin, Ontai Tang, Jingtian Hao, Mugeng Liu, Ru Peng, Lang Mei, Xiaohan Yu, Liyan Liu, Chong Chen, Wentao Zhang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FVQA, LiveVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal deep search is moving from short queries to long-horizon investigations that continually acquire evidence. However, training such agents remains constrained by limited challenging training questions and insufficient process feedback. We introduce MMSearch-OPD, combining controllable data refinement with joint reinforcement learning (RL) and on-policy distillation (OPD). Our Refine pipeline performs targeted expansion of reasoning chains derived from existing simple multimodal questions. Parameterized transformations control search depth and cross-modal evidence requirements while reusing existing image--question pairs. For training, answer rewards and lightweight behavior penalties guide RL, while the reward gap modulates token-level teacher guidance on imperfect student trajectories. An exponentially decaying distillation coefficient reduces teacher dependence as training proceeds. Experiments show gains from data refinement and further improvements from joint training after SFT, indicating stronger long-horizon multimodal deep search capabilities.

</details>

---

### [[20_Research/Papers/具身智能/REKI_Registering_Knowledge_in_VLAs|REKI: Registering Knowledge in VLAs]]

![[assets/2610.22178_figure.png|800]]

- **arXiv**: [2610.22178](https://arxiv.org/abs/2610.22178)
- **PDF**: https://arxiv.org/pdf/2610.22178
- **详细分析**: [[20_Research/Papers/具身智能/REKI_Registering_Knowledge_in_VLAs|REKI: Registering Knowledge in VLAs]]
- **作者**: Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary, Shizhe Chen, Moritz Böhle
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《REKI: Registering Knowledge in VLAs》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MemoryVLA, OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in the action expert summarise the output of the VLM at each frame and persist in the expert's cache. This memory improves success in simulation and on real robots, and makes oscillations between poses about four times rarer. REKI uses a simple model design and training paradigm, and is optimised to be efficient at training and inference. We release the full code across data curation, training, inference and evaluation, deployment, and all pretrained and finetuned model weights: https://github.com/kyutai-labs/reki.

</details>

---

### [[20_Research/Papers/机器人/Training-Free_Target-Aware_Refinement_of_3D_Gaussian_Language_Map|Training-Free Target-Aware Refinement of 3D Gaussian Language Map]]

![[assets/2610.21619_figure.png|800]]

- **arXiv**: [2610.21619](https://arxiv.org/abs/2610.21619)
- **PDF**: https://arxiv.org/pdf/2610.21619
- **详细分析**: [[20_Research/Papers/机器人/Training-Free_Target-Aware_Refinement_of_3D_Gaussian_Language_Map|Training-Free Target-Aware Refinement of 3D Gaussian Language Map]]
- **作者**: Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Training-Free Target-Aware Refinement of 3D Gaussian Language Map》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distilling vision-language features into 3D Gaussian Splatting yields a language map that can be queried with arbitrary text. In deployment, however, a small set of user-specified targets must be reliably located, which current distilled maps often miss, while open-vocabulary queryability for other words must remain intact. We propose a training-free, target-aware refinement of an already-distilled language map. Guided by a text-promptable segmenter, the visual embedding inside each detected target region is blended with the target text embedding, a convex combination whose coefficient sets the amount of injected prior, while non-target regions are left untouched. Injecting too much overwrites appearance cues and general queryability, so we seek, for each target, the smallest coefficient that still lets it win, and we obtain every coefficient in closed form, leaving no hyperparameters to tune. We further identify a failure mode of injection in language-goal localization. Text embeddings share a common component, and injecting them makes the standard cosine read-out query-agnostic, which a centering step in the read-out removes. Across three benchmarks, the refinement consistently improves open-vocabulary segmentation, roughly doubling the base mIoU on Replica, and localizes language goals more reliably than the base map. It also transfers as a plug-in to off-the-shelf field-based and object-level language maps and supports a real-world demonstration in which a legged robot navigates to natural-language goals. Project page and code: https://lab-of-ai-and-robotics.github.io/target-aware-langmap/

</details>

---

### [[20_Research/Papers/具身智能/CarryOn_A_Dual-Loop_Harness_for_Personalized_and_Reliable_Robot_Assistance|CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance]]

![[assets/2610.21453_figure.png|800]]

- **arXiv**: [2610.21453](https://arxiv.org/abs/2610.21453)
- **PDF**: https://arxiv.org/pdf/2610.21453
- **详细分析**: [[20_Research/Papers/具身智能/CarryOn_A_Dual-Loop_Harness_for_Personalized_and_Reliable_Robot_Assistance|CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance]]
- **作者**: Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Bei Yu, Jiaya Jia
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution. Second, reliable deployment demands explainable safety assurance that proactively prevents hazards and gracefully recovers from occasional physical failures. To address these gaps, we present CarryOn, a dual-loop harness designed to augment a frozen VLA policy. The planning loop maintains persistent user-level and scene-level context that is continually grounded against new observations and revised through interaction, enabling personalized task selection and execution grounding across conversations and changing scenes. The execution loop actively supervises policy rollouts, shielding actions from predicted hazardous contact. When execution fails, the system invokes reusable control-based recovery skills that restore task progress and are refined through reflection on earlier failures. On a real robot and in simulation, CarryOn dispatches preference-consistent subtasks across users and scenes, reduces the violation rate of an already safety-finetuned VLA from 52.6% to 6.1%, and increases recovery success from 13% to 80% when refined skills are reused.

</details>

---

### [[20_Research/Papers/大模型/Perception_or_Reasoning_Diagnosing_and_Tackling_Reinforcement_Learning_Bottlenecks_in_VLMs|Perception or Reasoning? Diagnosing and Tackling Reinforcement Learning Bottlenecks in VLMs]]

![[assets/2610.21380_figure.png|800]]

- **arXiv**: [2610.21380](https://arxiv.org/abs/2610.21380)
- **PDF**: https://arxiv.org/pdf/2610.21380
- **详细分析**: [[20_Research/Papers/大模型/Perception_or_Reasoning_Diagnosing_and_Tackling_Reinforcement_Learning_Bottlenecks_in_VLMs|Perception or Reasoning? Diagnosing and Tackling Reinforcement Learning Bottlenecks in VLMs]]
- **作者**: Zeyuan Yang, Zhuohao Chen, Jiaben Chen, Yao Zhang, Maohao Shen, Chuang Gan
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Perception or Reasoning? Diagnosing and Tackling Reinforcement Learning Bottlenecks in VLMs》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has brought strong gains to language model reasoning, but its improvements on visual tasks remain less consistent. One difficulty is that visual task failures can arise from different sources: the same benchmark may be limited by perception for one model and by reasoning for another. We introduce Perception and Reasoning Attribution (PARA), which measures the remaining perceptual and reasoning headroom of each model--benchmark pair by comparing how many current errors are recovered with more accurate visual information versus a stronger reasoner. Across 4 vision-language models and 17 multimodal benchmarks, PARA broadly agrees with the expected characteristics of existing benchmarks while revealing substantial model-specific variation. More importantly, it shows that RL gains become smaller as perceptual headroom increases, but larger when reasoning explains more of the recoverable errors, suggesting that current RL exploits reasoning headroom more effectively than perceptual headroom. Motivated by this gap, we analyze how existing RL objectives affect visual perception and find that reward- and token-level signals influence visual attention only indirectly. We therefore propose GRAD, a group-relative attention distillation objective that uses the best rollout in each group to directly guide the visual attention of weaker rollouts. GRAD consistently improves performance across two model scales and seven benchmarks, and further complements existing RL methods.

</details>

---

### [[20_Research/Papers/具身智能/VLA-$Δ$_Learning_Physical_State_Transition_for_Vision-Language-Action_Models|VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models]]

![[assets/2610.21306_figure.png|800]]

- **arXiv**: [2610.21306](https://arxiv.org/abs/2610.21306)
- **PDF**: https://arxiv.org/pdf/2610.21306
- **详细分析**: [[20_Research/Papers/具身智能/VLA-$Δ$_Learning_Physical_State_Transition_for_Vision-Language-Action_Models|VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models]]
- **作者**: Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan, Xu Wang, Wenqi Zhang, Xuhong Zhang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.4，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models transfer semantic knowledge acquired through vision-language pretraining to robot control, achieving strong performance across various benchmarks. However, most VLAs directly map observations to demonstrated actions without explicit supervision of intermediate physical state changes, making them prone to overfitting observation-action correspondences. Some methods introduce intermediate reasoning or future-state prediction in language, visual, or latent spaces to guide action generation, but do not explicitly supervise the physical state transition itself. We therefore propose VLA-$Δ$, a general framework that uses physical changes between current and future states as explicit learning targets. To support this objective, we construct a large-scale pretraining dataset and derive physical state-transition annotations covering task-relevant semantics and visual motion changes, providing more direct supervision for continuous action generation. During inference, the model generates actions directly from current observations without additional inference overhead. VLA-$Δ$ achieves performance competitive with the state of the art on LIBERO and RoboTwin, and outperforms $π_{0.5}$ in real-robot experiments. Our code is available at https://github.com/ZJU-OmniAI/VLA-Delta

</details>

---

### [[20_Research/Papers/具身智能/LICOA_Learning_Instruction-Conditioned_Optical_Actions_for_Mobile_Spatial_Augmented_Reality|LICOA: Learning Instruction-Conditioned Optical Actions for Mobile Spatial Augmented Reality]]

![[assets/2610.21282_figure.png|800]]

- **arXiv**: [2610.21282](https://arxiv.org/abs/2610.21282)
- **PDF**: https://arxiv.org/pdf/2610.21282
- **详细分析**: [[20_Research/Papers/具身智能/LICOA_Learning_Instruction-Conditioned_Optical_Actions_for_Mobile_Spatial_Augmented_Reality|LICOA: Learning Instruction-Conditioned Optical Actions for Mobile Spatial Augmented Reality]]
- **作者**: Yuchen Deng, Shunkai Zhou, Ruixuan Zhu, Haibin Ling, Bingyao Huang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《LICOA: Learning Instruction-Conditioned Optical Actions for Mobile Spatial Augmented Reality》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial augmented reality (SAR) augments physical environments with projected content, but most systems assume that the projector pose, target region, or motion path has been fixed or specified. We instead make projected light an embodied action: given a language instruction and current visual observations, a system must decide how to move and where and at what scale to place the projection. We introduce LICOA to realize this capability. Its differential-drive chassis provides room-scale approach and repositioning, while a steerable mirror with two degrees of freedom (2DoF) and projection scale provide rapid local control of the beam. A shared interface maps synchronized external and onboard RGB cameras with robot control state to physical optical actions across pretrained action models. Because instruction-conditioned optical action lacks dedicated training data and a common evaluation protocol, we construct a matched simulation embodiment and a corpus with 150 tasks and 7,500 rendered episodes, then evaluate models trained only on this corpus in previously unseen real-world environments. Across 480 complete closed-loop real-world execution trials (rollouts) on 12 tasks, the best adapted action model achieves a 57.50% success rate and 40.64% success weighted by path length, compared with 8.33% and 5.15% for the same architecture trained from scratch. A further 150 real-world ablation rollouts support the need for both camera views and coordinated control of the chassis and mirror. These results establish a physical platform, shared perception and optical action interface, corpus, and real-world evaluation protocol for treating projected light as an embodied action.

</details>

---

### [[20_Research/Papers/具身智能/Do_VLAs_Really_Follow_Instructions_Diagnosing_How-Level_Instruction_Following_in_Vision-Language-Action_Models|Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models]]

![[assets/2610.21251_figure.png|800]]

- **arXiv**: [2610.21251](https://arxiv.org/abs/2610.21251)
- **PDF**: https://arxiv.org/pdf/2610.21251
- **详细分析**: [[20_Research/Papers/具身智能/Do_VLAs_Really_Follow_Instructions_Diagnosing_How-Level_Instruction_Following_in_Vision-Language-Action_Models|Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models]]
- **作者**: Sangwu Park, Wonjoong Kim, Yeonjun In, Chanyoung Park
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChatVLA, InstructVLA, InternVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are expected to follow instructions like their language backbones, yet prior work has focused on What-level instructions that specify the task rather than How-level instructions that specify how to carry it out. Through our diagnoses, we find that How-level instructions do not help current VLAs and lower task success. We hypothesize that pairing each training episode with a single instruction limits How-level instruction following, and show that training with segment-level enriched instructions makes actions respond to such instructions without consistently raising task success. To measure How-level instruction following beyond standard benchmarks, we introduce SIMPLER-IN, where success requires conditions given only in the instruction. It shows that the gained responsiveness does not extend to demanding or out-of-distribution How-level instructions. How-level instruction following thus remains an open challenge.

</details>

---

### [[20_Research/Papers/具身智能/RoPE-Flow_Monocular_Vision-based_Robot_Pose_Estimation_via_2D_Graph-Conditioned_3D_Flow_Matching|RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching]]

![[assets/2610.21086_figure.png|800]]

- **arXiv**: [2610.21086](https://arxiv.org/abs/2610.21086)
- **PDF**: https://arxiv.org/pdf/2610.21086
- **详细分析**: [[20_Research/Papers/具身智能/RoPE-Flow_Monocular_Vision-based_Robot_Pose_Estimation_via_2D_Graph-Conditioned_3D_Flow_Matching|RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching]]
- **作者**: Liangjing Shao, Wanhao Liu, Zhiwei Fang, Rulin Zhou, Quanlu Zhang, Changjing Liu, Beilei Cui, Yiming Huang, Hongliang Ren
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CtRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Camera-to-robot pose estimation from a monocular image is significant for vision-based robot navigation and control. However, recovering 3D structural features from 2D observations remains a challenging task. Existing camera-to-robot pose estimation methods either rely on time-consuming iterative rendering or involve sophisticated 2D-3D registration which suffers from projection ambiguity, accumulated errors for distal joints and imbalanced learning for different joints. In this work, we propose RoPE-Flow, an end-to-end flow matching-based framework for camera-to-robot pose estimation. From the predicted 2D heatmaps, we propose a Keypoint-centered Feature Extractor to obtain positional features along with contextual representations from keypoints-centered multi-scale patches. Moreover, we introduce Graph-guided Condition Generator, which embeds a learnable adjacency map to generate condition for flow matching based on correlation among keypoints. Besides, we introduce Bone Length Loss and Ray-Depth Loss for topological consistency and scale stability, with joint-wise weighting to mitigate varied prediction difficulty across joints. The proposed method outperforms state-of-the-art methods for pose estimation across different types of robots with mutiple cameras. Besides, we establish a novel cross-scene benchmark to demonstrate the outstanding performance of RoPE-Flow on zero-shot cross-scene robot pose estimation. Meanwhile, animated visualizations are shown on the website: ropeflow.netlify.app

</details>

---

### [[20_Research/Papers/机器人/EgoJEPA_Beyond_Retargeting_for_Dexterous_Manipulation_from_Egocentric_Videos|EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos]]

![[assets/2610.20904_figure.png|800]]

- **arXiv**: [2610.20904](https://arxiv.org/abs/2610.20904)
- **PDF**: https://arxiv.org/pdf/2610.20904
- **详细分析**: [[20_Research/Papers/机器人/EgoJEPA_Beyond_Retargeting_for_Dexterous_Manipulation_from_Egocentric_Videos|EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos]]
- **作者**: Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappings require meticulous recal- ibration across different embodiments and risk propagating hand-tracking errors into downstream robot control pipelines. To this end, we propose EgoJEPA, a three-stage framework that learns embodiment-agnostic representations from ego- centric human videos without rule-based human-to-robot retargeting: 1) Human- action pre-training learns effect-aware latent actions through JEPA-style visual prediction conditioned on hand-motion differences; 2) Latent-action-based world modeling jointly predicts future visual dynamics and latent actions, which decou- ples human prior pre-training from robot-specific control parameterizations; 3) Embodiment-specific tuning adapts the pretrained model to diverse robots through lightweight action adapters. Experiments on five real-world manipulation tasks across three robot embodiments demonstrate the effectiveness and efficiency of EgoJEPA. It achieves a 74% average success rate under the out-of-domain evalu- ation, compared with 65% for the retargeting baseline, while reducing cumulative cross-embodiment wall-clock cost by 47.2%, from 743.2 to 392.7 hours.

</details>

---
