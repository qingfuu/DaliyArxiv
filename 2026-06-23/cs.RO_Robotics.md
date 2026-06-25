# cs.RO | Robotics | 2026-06-23

#arxiv #ComputerScience

**论文数**: 55

### [[20_Research/Papers/具身智能/LIBERO-Safety_A_Comprehensive_Benchmark_for_Physical_and_Semantic_Safety_in_Vision-Language-Action_Models|LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models]]

![[assets/2606.23686_figure.png|800]]

- **arXiv**: [2606.23686](https://arxiv.org/abs/2606.23686)
- **PDF**: https://arxiv.org/pdf/2606.23686
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-Safety_A_Comprehensive_Benchmark_for_Physical_and_Semantic_Safety_in_Vision-Language-Action_Models|LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models]]
- **作者**: Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo, Saining Zhang, Shaoxuan Xie, Xin Jin, Yao Mu, Jiaolong Yang, Guocai Yao, Xianyuan Zhan...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, RLBench, SafeLIBERO, SafeVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the impressive manipulation capabilities of Vision-Language-Action (VLA) models, their operational safety under strict constraints remains largely unverified. To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. Leveraging this infrastructure, we curate a large-scale dataset of 19,664 strictly collision-free demonstrations with extensive domain randomization. We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment. By providing a scalable pipeline, a robust dataset, and profound failure-mode insights, LIBERO-Safety establishes a crucial foundation for developing safe and reliable VLA models.

</details>

---

### [[20_Research/Papers/具身智能/LaST-HD_Learning_Latent_Physical_Reasoning_from_Scalable_Human_Data_for_Robot_Manipulation|LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation]]

![[assets/2606.23685_figure.png|800]]

- **arXiv**: [2606.23685](https://arxiv.org/abs/2606.23685)
- **PDF**: https://arxiv.org/pdf/2606.23685
- **详细分析**: [[20_Research/Papers/具身智能/LaST-HD_Learning_Latent_Physical_Reasoning_from_Scalable_Human_Data_for_Robot_Manipulation|LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation]]
- **作者**: Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.4（加权：具身智能 2.1，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EgoVLA, OpenVLA, Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space. Rather than mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model on unpaired human-hand and robot trajectories to synthesize unified latent targets. After aligning cross-embodiment representations in this shared forward-dynamics space, these targets supervise LaST-HD's latent reasoning process, enabling it to internalize shared physical dynamics and drive efficient human-hand action learning. Moreover, we develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for human-hand data collection. The captured human data provide precise keypoints and serve as universal action supervision across grippers and dexterous hands. Armed with the aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-to-human training recipe comprising mixed human-robot co-training and human-hand online correction post-training. Through mixed co-training, LaST-HD improves generalization to novel objects, scenes, and positions using only human-hand demonstrations. With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

</details>

---

### [[20_Research/Papers/具身智能/Flatness_Preserves_Instruction_Following_in_Vision-Language-Action_Models|Flatness Preserves Instruction Following in Vision-Language-Action Models]]

![[assets/2606.23641_figure.png|800]]

- **arXiv**: [2606.23641](https://arxiv.org/abs/2606.23641)
- **PDF**: https://arxiv.org/pdf/2606.23641
- **详细分析**: [[20_Research/Papers/具身智能/Flatness_Preserves_Instruction_Following_in_Vision-Language-Action_Models|Flatness Preserves Instruction Following in Vision-Language-Action Models]]
- **作者**: Haochen Zhang, Yonatan Bisk
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Flatness Preserves Instruction Following in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have the potential for open-world generalization by leveraging pretrained vision-language representations, yet downstream finetuning on limited robot data often degrades these representations, leading to brittle policies that ignore language instructions in favor of visual shortcuts, a failure mode we term instruction blindness. We hypothesize that standard finetuning with limited data applies gradients to a sparse set of points, which manifests as a sharp loss landscape with high-curvature minima. We propose to address this directly through flatness-preserving optimization while finetuning on the exact same data, where learning a flatter landscape results in a model more robust to perturbations in the weight space. Specifically, we demonstrate that simply applying sharpness-aware minimization during VLA finetuning significantly improves instruction following by over 60% across multiple simulation and real-world benchmarks without additional data, architectural modification, or retraining. We further analyze the effect of selective sharpness, quantify its effects, and show that our approach is complementary to existing guidance techniques. Project page can be found at https://haochenz11.github.io/papers/flatness-vla/.

</details>

---

### [[20_Research/Papers/具身智能/dVLA-RL_Reinforcement_Learning_over_Denoising_Trajectories_for_Discrete_Diffusion_Vision-Language-Action_Models|dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models]]

![[assets/2606.23623_first_page.png|800]]

- **arXiv**: [2606.23623](https://arxiv.org/abs/2606.23623)
- **PDF**: https://arxiv.org/pdf/2606.23623
- **详细分析**: [[20_Research/Papers/具身智能/dVLA-RL_Reinforcement_Learning_over_Denoising_Trajectories_for_Discrete_Diffusion_Vision-Language-Action_Models|dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models]]
- **作者**: Yuhao Wu, Yitian Liu, Weijie Shen, Mishuo Han, Wenjie Xu, Haotian Liang, Zhongshan Liu, Yinan Mao, Lei Xu, Xinping Guan, Ru Ying, Ran Zheng...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.6（加权：具身智能 2.1，强化学习 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have established a powerful paradigm for generalist robotic manipulation by grounding control into the semantic reasoning of VLMs. Prevailing architectures typically model actions continuously via diffusion or flow processes, or discretely through either autoregressive generation or parallel decoding. Recently, Discrete Diffusion VLAs (dVLAs) have emerged as a distinct alternative, unifying vision, language, and action into a single discrete token space via masked generative modeling. While combining iterative refinement with unified representations, its training has thus far been restricted to Supervised Fine-Tuning (SFT), leaving the potential of Reinforcement Learning (RL) for further policy refinement largely unexplored. A fundamental challenge in RL for dVLAs is that the marginal probability of the final action generated by dVLAs remains intractable. To solve this problem, we propose \textbf{dVLA-RL}, shifting the learning objective from the marginal action probability to the joint probability of the sampled generation path. Specifically, by modeling the denoising process as a Markov Decision Process (MDP), we mathematically formulate this path probability as a product of step-wise transitions. This trajectory-level objective provides a unified formulation that natively accommodates variable denoising steps. Leveraging this intrinsic fexibility, we introduce a unified step scheduling approach for complex multi-task learning, tailoring denoising steps to specific task complexities to maximize both success rates and computational effciency. Extensive evaluations demonstrate that our approach achieves a success rate of \textbf{99.7\%} on LIBERO. Furthermore, it establishes strong VLA-based results on RoboTwin 2.0 by delivering a \textbf{30.6\%} improvement over the SFT baseline, remaining competitive with strong World-Action Model baselines.

</details>

---

### [[20_Research/Papers/具身智能/KEMO_Event-Driven_Keyframe_Memory_for_Long-Horizon_Robot_Manipulation_with_VLA_Policies|KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies]]

![[assets/2606.23589_figure.png|800]]

- **arXiv**: [2606.23589](https://arxiv.org/abs/2606.23589)
- **PDF**: https://arxiv.org/pdf/2606.23589
- **详细分析**: [[20_Research/Papers/具身智能/KEMO_Event-Driven_Keyframe_Memory_for_Long-Horizon_Robot_Manipulation_with_VLA_Policies|KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies]]
- **作者**: Yihan Zeng, Minghao Ye, Yiyuan Chen, Yide Shentu, Philipp Wu, Zike Yan, Zhongyu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《KEMO: Event-Driven Keyframe Memory for Long-Horizon Robot Manipulation with VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ContextVLA, MemoryVLA, ReMem-VLA, Real-World, TGM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot manipulation remains challenging because similar observations may occur at different execution stages, while the appropriate action depends on previously completed operations. Memory can address this ambiguity by enabling policies to infer task progress from execution history. However, existing memory-augmented approaches often either retain dense histories that require compression or rely primarily on recent context that may discard earlier task-relevant events. In this work, we propose propose KEMO, a lightweight plug-in memory framework that automatically selectively preserves keyframes associated with task-relevant state changes for VLA policies. KEMO combines robot kinematics with visual filtering to detect events, encodes the selected keyframes as compact temporally ordered memory tokens, and integrates them with current visual features through cross-attention and gated residual fusion for VLA training. The detected events also define higher-weight training samples near critical transitions. We evaluate KEMO on various real-world dual-arm manipulation tasks spanning 2 to 6 scored subtasks, and trajectory length ranging from 830 steps to 2846 execution steps (durations from 28 to 95 seconds). Compared with the memory-free baseline (e.g., $π_{0.5}$), KEMO improves aggregate Task Success Rate by 23.6\% and Stage Completion Rate by 34.1\%. Ablations show that event-driven keyframe selection outperforms uniform sampling and recent-frame retention, while the proposed gated fusion and keyframe-aligned loss weighting provide complementary gains.

</details>

---

### [[20_Research/Papers/具身智能/BiliVLA_Scene-Aware_Vision-Language-Action_Model_with_Reinforcement_Learning_for_Autonomous_Biliary_Endoscopic_Navigation|BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation]]

![[assets/2606.23531_figure.png|800]]

- **arXiv**: [2606.23531](https://arxiv.org/abs/2606.23531)
- **PDF**: https://arxiv.org/pdf/2606.23531
- **详细分析**: [[20_Research/Papers/具身智能/BiliVLA_Scene-Aware_Vision-Language-Action_Model_with_Reinforcement_Learning_for_Autonomous_Biliary_Endoscopic_Navigation|BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation]]
- **作者**: Jinsong Lin, Chi kit Ng, Zhiyong Xiong, Zikang Pan, Yihan Hu, Tabassum Tamima, Ziyi Hao, Eddie Cheung, Jiewen Lai, Huxin Gao, Hongliang Ren
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BiliVLA, EndoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic navigation.

</details>

---

### [[20_Research/Papers/具身智能/DexTeleop-0_Force-Aware_Bimanual_Dexterous_Teleoperation_with_Ego-Centric_Perception_towards_Shared_Autonomy|DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy]]

![[assets/2606.23431_figure.png|800]]

- **arXiv**: [2606.23431](https://arxiv.org/abs/2606.23431)
- **PDF**: https://arxiv.org/pdf/2606.23431
- **详细分析**: [[20_Research/Papers/具身智能/DexTeleop-0_Force-Aware_Bimanual_Dexterous_Teleoperation_with_Ego-Centric_Perception_towards_Shared_Autonomy|DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy]]
- **作者**: Haichao Liu, Yuyao Jiang, Hyunsun Park, Yuanjiang Xue, Ziwei Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《DexTeleop-0: Force-Aware Bimanual Dexterous Teleoperation with Ego-Centric Perception towards Shared Autonomy》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-grained, bimanual dexterous manipulation remains a foundational challenge in robotics. Traditional teleoperation systems often fail in contact-rich tasks because embodiment gaps hinder accurate kinematic mapping, while tactile and force feedback remain absent. Consequently, data collection efficiency for high-precision tasks remains prohibitively low. To address these limitations, we propose a tactile-driven adaptation strategy designed to enable fine-grained manipulation on top of teleoperation pipelines. Instantiated within our bimanual dexterous framework, DexTeleop-0, this strategy introduces a real-time optimization loop that bridges the embodiment gap by translating coarse human tracking intents into precise, force-compliant robotic commands with tactile sensing. By estimating accurate contact points and leveraging a tactile-enabled fingertip force-sensing profile, the system dynamically computes localized corrections using the operational space Jacobian with respect to joint angle updates. We rigorously evaluate this tactile-driven adaptation strategy across both simulated environments and real-world hardware. Compared with representative baselines, the proposed method consistently achieves higher task success rates and improved execution efficiency in robust grasping, disturbance-resilient manipulation, and complex dexterous tasks.

</details>

---

### [[20_Research/Papers/具身智能/Flowing_With_Purpose_Latent_Action_Guided_Flow_Matching_Policies_For_Robotic_Manipulation|Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation]]

![[assets/2606.23420_figure.png|800]]

- **arXiv**: [2606.23420](https://arxiv.org/abs/2606.23420)
- **PDF**: https://arxiv.org/pdf/2606.23420
- **详细分析**: [[20_Research/Papers/具身智能/Flowing_With_Purpose_Latent_Action_Guided_Flow_Matching_Policies_For_Robotic_Manipulation|Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation]]
- **作者**: Bruno Machado, Alexandre Chapin, Emmanuel Dellandrea, Liming Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Flowing With Purpose: Latent Action Guided Flow Matching Policies For Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching has recently become a new standard for behavior cloning in robotic manipulation. However, state-of-the-art flow matching policies suffer from a systematic structural mismatch: they rely on a globally fixed isotropic source distribution despite the strongly fragmented and heteroscedastic structure of robotic action spaces. This agnostic initialization forces the model to learn highly entangled vector fields, bottlenecking training efficiency and limiting overall policy performance. To address this limitation, we introduce Latent Action Guided Flow Matching (LAFM), a novel framework that replaces the monolithic Gaussian with an adaptive library of learned prior distributions. By grounding these distributions using a latent action model, LAFM maps current observations to discrete motion primitives, selecting a specialized base distribution that provides an informed, structurally aligned initialization for the denoising process. This dynamic adaptivity naturally accommodates heteroscedasticity in human demonstrations and makes transport trajectories shorter and less entangled. Empirically, LAFM substantially outperforms standard flow matching formulations, increasing task success rates by 23.4% in real-world robotic deployments and by 10.4% on the LIBERO-90 benchmark. Furthermore, we demonstrate that LAFM achieves state-of-the-art results, surpassing massively pre-trained vision-language-action models while utilizing significantly smaller architectures.

</details>

---

### [[20_Research/Papers/具身智能/IOI_Decoupling_Kinematics_and_Physics_for_Interactive_World_Models|IOI: Decoupling Kinematics and Physics for Interactive World Models]]

![[assets/2606.23296_figure.png|800]]

- **arXiv**: [2606.23296](https://arxiv.org/abs/2606.23296)
- **PDF**: https://arxiv.org/pdf/2606.23296
- **详细分析**: [[20_Research/Papers/具身智能/IOI_Decoupling_Kinematics_and_Physics_for_Interactive_World_Models|IOI: Decoupling Kinematics and Physics for Interactive World Models]]
- **作者**: Chengyu Bai, Peidong Jia, Tiecheng Guo, Yukai Wang, Rui Ma, Fangyuan Zhao, Chunkai Fan, Xiaobao Wei, Jintao Chen, Hao Wang, Ying Li, Xiaozhu Ju...
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，世界模型 1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《IOI: Decoupling Kinematics and Physics for Interactive World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ControlNet, Ctrl-World, IRASim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Developing generalist embodied agents requires interactive environments providing visually realistic feedback and accurate action-conditioned dynamics. Interactive world models address this by simulating such complex dynamics. However, purely data-driven methods struggle to ensure precise control alignment and physically plausible visual feedback due to a lack of explicit structural constraints. To address this, we propose IOI, a hybrid interactive world model integrating analytical kinematic priors with learned physical dynamics. Unlike data-driven approaches prone to spatiotemporal drift, IOI introduces explicit kinematic guidance, computing forward kinematics from action sequences for accurate motion trajectories. These trajectories are rendered into synchronized front, side, and top orthographic projections, eliminating the need for extrinsic camera calibration. A Multi-view Kinematic Aggregation and Injection module fuses these geometric cues and injects them into the video generator, providing geometry-consistent guidance. Conditioning video generation on these deterministic trajectories establishes a synergy between the analytical simulator and the world model. Decoupling deterministic motion into the kinematic prior frees the generator to model stochastic physical interactions. Experiments on the RoboTwin benchmark validate IOI across kinematic fidelity, out-of-distribution (OOD) generalization, and policy evaluation. IOI achieves state-of-the-art simulation performance and robust zero-shot generalization to unseen OOD tasks. Furthermore, IOI serves as a reliable policy evaluator, yielding success rates closely aligning with ground-truth physics simulators. On real-world platforms, policies trained on IOI-synthesized data match those trained on teleoperation demonstrations, solidifying its practical value for embodied policy learning.

</details>

---

### [[20_Research/Papers/强化学习/Causal_Reward_World_Models_Zero-shot_Reward_Design_for_Automated_Skill_Generation|Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation]]

![[assets/2606.23280_figure.png|800]]

- **arXiv**: [2606.23280](https://arxiv.org/abs/2606.23280)
- **PDF**: https://arxiv.org/pdf/2606.23280
- **详细分析**: [[20_Research/Papers/强化学习/Causal_Reward_World_Models_Zero-shot_Reward_Design_for_Automated_Skill_Generation|Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation]]
- **作者**: Yang Yang, Yuchuang Tong, Zhengtao Zhang, Xu Ding, Ning Yang, Yifan Zhang, Haipeng Li, Kehu Yang, Miao Xin
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.2，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated Reward Design (ARD) aims to replace manual reward engineering in reinforcement learning with language-driven reward function synthesis. However, existing approaches based on large language models (LLMs) remain inherently correlation-driven, relying on iterative environmental feedback to refine reward hypotheses for each specific task. This paradigm not only results in inefficient reasoning but also makes LLMs susceptible to semantically plausible yet causally spurious reward components, leading to ineffective optimization. To address these limitations, we propose the Causal Reward World Model (CRWM), which explicitly models the causal topological relationships between candidate reward components and task-targeted physical variables through offline pre-training on multi-task interaction data. Based on a coarse-to-fine pre-training strategy, we introduce a joint optimization module that integrates Explicit Mechanism Decoupling with Confidence-Aware Soft Fusion to refine coarse structural priors using micro-level trajectories, thereby constructing a robust and interpretable causal skeleton. During inference, LLMs leverage CRWM as a task-irrelevant causal prior to constrain the reward generation, enabling zero-shot reward function design. Our work opens up a new white-box paradigm for the ARD problem. Extensive experiments on complex continuous control benchmarks demonstrate that CRWM generates executable reward functions without feedback-driven reward refinement, significantly reducing the design latency for acquiring new robotic skills while matching or surpassing state-of-the-art performance, and further exhibits strong generalization capabilities across unseen tasks and diverse robotic embodiments.

</details>

---

### [[20_Research/Papers/具身智能/LP-NavOA_Integrated_Local_Navigation_and_Obstacle_Avoidance_for_Humanoid_Robots_under_Limited_Perception|LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception]]

![[assets/2606.23249_figure.png|800]]

- **arXiv**: [2606.23249](https://arxiv.org/abs/2606.23249)
- **PDF**: https://arxiv.org/pdf/2606.23249
- **详细分析**: [[20_Research/Papers/具身智能/LP-NavOA_Integrated_Local_Navigation_and_Obstacle_Avoidance_for_Humanoid_Robots_under_Limited_Perception|LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception]]
- **作者**: Yukun Luo, Jianjun Ma, Yuyao Min, Jinzhe Li, Kaihong Huang, Peng Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid local navigation in cluttered environments must jointly resolve obstacle avoidance, sparse-goal recovery, and stable whole-body locomotion under short-range and partially observable sensing. Explicit planner-control decompositions introduce latency and can mismatch agile humanoid command-tracking limits, while purely reactive controllers may lose the goal after obstacle occlusion. We present LP-NavOA, a limited-perception navigation and obstacle-avoidance framework for humanoid robots. A raycast-conditioned perception-action proximal policy optimization (PPO) locomotion backbone is first trained with a robot-centered circular heading-speed command and a shared command-side safety filter. With this backbone frozen, A-star and waypoint teachers generate rollouts for distilling a recurrent local planner that overwrites only the heading command at deployment, leaving the whole-body policy intact. At runtime, LP-NavOA uses proprioception, short-range local range sensing, and a body-frame goal direction, requiring no global map, waypoint stream, or external planner. In MuJoCo open-wall and indoor layouts, the distilled planner produces obstacle bypassing and post-avoidance goal recovery, raising teacher-calibrated on-time arrival from 38--40\% to 85--97\% and reducing brush/contact-heavy progress relative to a backbone-only controller. Ablations show that dynamic route shaping, teacher-active data collection, and the circular command interface are important for navigation efficiency and for training the 3.0\,m/s backbone. A Unitree G1 deployment analysis demonstrates hardware executability without continuous joystick steering.

</details>

---

### [[20_Research/Papers/机器人/Lessons_from_the_Field_A_Case_Study_of_Robotic_Intervention_in_an_Industrial_Emergency|Lessons from the Field: A Case Study of Robotic Intervention in an Industrial Emergency]]

![[assets/2606.23246_figure.jpg|800]]

- **arXiv**: [2606.23246](https://arxiv.org/abs/2606.23246)
- **PDF**: https://arxiv.org/pdf/2606.23246
- **详细分析**: [[20_Research/Papers/机器人/Lessons_from_the_Field_A_Case_Study_of_Robotic_Intervention_in_an_Industrial_Emergency|Lessons from the Field: A Case Study of Robotic Intervention in an Industrial Emergency]]
- **作者**: Jonathan Lichtenfeld, Frederik Bark, Robert Grafe, Oskar von Stryk
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Lessons from the Field: A Case Study of Robotic Intervention in an Industrial Emergency》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Incidents in chemical plants can pose a high level of risk and harsh environments for first responders. Contamination and explosion hazards can deny human access to the affected infrastructure, underscoring the need for capable robot systems. This field report documents the successful deployment of a robotic task force to neutralize an explosive gas hazard at a chemical plant after a fire incident. An Unmanned Ground Vehicle (UGV) with a custom manipulation tool opened a critical valve under hazardous conditions, averting the threat of a large-scale explosion. We provide insights into robot deployment and use the mission results to highlight both the importance of rescue robotics and limitations of using research platforms in real emergency deployments, such as communication constraints and the need for enhanced operator-assistance functions.

</details>

---

### [[20_Research/Papers/具身智能/Bridging_Semantics_and_Kinematics_A_Modular_Framework_for_Zero-Shot_Robotic_Manipulation|Bridging Semantics and Kinematics: A Modular Framework for Zero-Shot Robotic Manipulation]]

![[assets/2606.23157_figure.png|800]]

- **arXiv**: [2606.23157](https://arxiv.org/abs/2606.23157)
- **PDF**: https://arxiv.org/pdf/2606.23157
- **详细分析**: [[20_Research/Papers/具身智能/Bridging_Semantics_and_Kinematics_A_Modular_Framework_for_Zero-Shot_Robotic_Manipulation|Bridging Semantics and Kinematics: A Modular Framework for Zero-Shot Robotic Manipulation]]
- **作者**: Ali Alabbas, Dipshikha Das, Camillo Murgia, Sainul Ansary, Alaa Elkamash, Philip Long
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.5，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Bridging Semantics and Kinematics: A Modular Framework for Zero-Shot Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a modular training-free framework for zero-shot, language-guided robotic manipulation in semi-structured environments. The architecture bridges the gap between high-level reasoning and low-level kinematics by decomposing the vision-action pipeline into three stages: visual perception, semantic interpretation, and task execution. To overcome the spatial ambiguity and semantic hallucinations inherent in standard Vision-Language Models (VLMs), the perception module employs FastSAM and Set-of-Mark (SoM) prompting to dynamically generate grounded, alphanumeric visual anchors. The same foundation model then operates purely as a Large Language Model (LLM) to act as a semantic router, translating unconstrained human directives into verifiable, reconfigurable configurations. Finally, these configurations are dynamically parsed by a Task Orchestrator into MoveIt Task Constructor (MTC) to generate collision-free trajectories. The framework is evaluated across two zero-shot experimental setups: unconstrained open-world sequential manipulation and dense relational spatial reasoning, achieving a 62% end-to-end task success rate across both scenarios, demonstrating its capacity to reliably execute complex physical actions without domain-specific training or manual coordinate programming.

</details>

---

### [[20_Research/Papers/具身智能/Asymmetric_physics_enables_efficient_learning_in_quadrupedal_robot_swarms|Asymmetric physics enables efficient learning in quadrupedal robot swarms]]

![[assets/2606.23153_figure.jpg|800]]

- **arXiv**: [2606.23153](https://arxiv.org/abs/2606.23153)
- **PDF**: https://arxiv.org/pdf/2606.23153
- **详细分析**: [[20_Research/Papers/具身智能/Asymmetric_physics_enables_efficient_learning_in_quadrupedal_robot_swarms|Asymmetric physics enables efficient learning in quadrupedal robot swarms]]
- **作者**: Yuang Zhang, Yunlong Song, Zhihao He, Zelin Ni, Kangyu Wang, Tianchi Liu, Yu Hu, Feng Yu, Danping Zou, Weiyao Lin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.2（加权：具身智能 0.9，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Asymmetric physics enables efficient learning in quadrupedal robot swarms》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Animal collectives navigate cluttered environments through local coordination, yet robot swarms still struggle to reproduce this capability in the physical world. End-to-end learning offers a route to such coordination, but scaling it to embodied swarms remains difficult: standard sampling-based reinforcement learning becomes inefficient when visual perception, dense robot-robot interaction, and contact-rich locomotion must be learned together. Here we show that asymmetric physics enables efficient end-to-end learning of vision-based, decentralized control in large swarms of quadrupedal robots. During training, quadrupeds interact in shared environments, where a high-fidelity, non-differentiable simulator generates realistic motion and contact dynamics, and differentiable surrogate models provide gradients for navigation and locomotion policies. This separation enables up to 512 quadrupeds to learn coordinated navigation policies in obstacle-rich environments. At deployment, each robot acts from a single forward-facing depth camera, without explicit communication, centralized planning, or global maps. The policies generalize across forests, bridges, enclosures, narrow passages, and mazes, and zero-shot transfer to six physical quadrupeds across five real-world scenarios. The resulting swarms exhibit predictive avoidance, right-side yielding, pausing before bottlenecks, and wall following, showing that asymmetric physics enables efficient training of scalable decentralized control policies for quadrupedal robot swarms.

</details>

---

### [[20_Research/Papers/具身智能/Assistron_Bayesian_Shared_Autonomy_with_Off-the-shelf_Vision-Language-Action_Models|Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models]]

![[assets/2606.23147_figure.png|800]]

- **arXiv**: [2606.23147](https://arxiv.org/abs/2606.23147)
- **PDF**: https://arxiv.org/pdf/2606.23147
- **详细分析**: [[20_Research/Papers/具身智能/Assistron_Bayesian_Shared_Autonomy_with_Off-the-shelf_Vision-Language-Action_Models|Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models]]
- **作者**: Pinhao Song, Ze Fu, Yutong Hu, Renaud Detry
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Assistron: Bayesian Shared Autonomy with Off-the-shelf Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose Assistron, a shared autonomy model that leverages Vision-Language-Action (VLA) models to assist the user in daily activities. Our approach is grounded in two core principles: (1)~minimizing human cognitive and physical effort by leveraging VLA-driven autonomy for macro-movements, and (2)~prioritizing human intervention specifically at critical failure points. Driven by the user's verbal language commands, Assistron utilizes the VLA to autonomously execute macro-reaching trajectories, saving users' effort. In contact-rich interactions where VLAs tend to fail, Assistron employs a phase-aware interaction detection mechanism and solicits the user to intervene, in turn adjusting the VLA's action generation via flow matching guidance. Critically, our formulation eliminates the need for VLA fine-tuning, protecting its broad behavioral priors from catastrophic forgetting and ensuring the model does not become a narrow specialist. We validate our approach on a comprehensive multi-task scene recovery benchmark encompassing diverse daily manipulation skills. Empirical results demonstrate that Assistron significantly improves task success rates over pure autonomous baselines while significantly reducing human cognitive and physical workload compared to traditional teleoperation, offering a scalable, smooth, and effortless paradigm for assistive manipulation. The code is available in https://github.com/mousecpn/Assistron.git.

</details>

---

### [[20_Research/Papers/机器人/Flow_as_Flow_Modeling_Robot_Velocity_Fields_as_Probability_Velocity_Fields_for_Flow-Based_Object_Manipulation|Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation]]

![[assets/2606.23090_figure.png|800]]

- **arXiv**: [2606.23090](https://arxiv.org/abs/2606.23090)
- **PDF**: https://arxiv.org/pdf/2606.23090
- **详细分析**: [[20_Research/Papers/机器人/Flow_as_Flow_Modeling_Robot_Velocity_Fields_as_Probability_Velocity_Fields_for_Flow-Based_Object_Manipulation|Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation]]
- **作者**: Koki Seno, Daichi Yashima, Yusuke Takagi, Kento Tokura, Komei Sugiura
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Flow as Flow: Modeling Robot Velocity Fields as Probability Velocity Fields for Flow-Based Object Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-embodiment data have become central to training robotic foundation models. To leverage such heterogeneous data, we focus on flow-based object manipulation, where robot flows (robot velocity fields) serve as embodiment-agnostic motion representations. Previous studies do not formulate robot flows as dense velocity fields, but as displacements of sparse keypoints, while such velocity fields better match the continuous-time nature of motions. We propose Flow as Flow, a framework that models robot flows as probability flows based on a flow matching formulation. By naturally modeling such velocity fields within this formulation, our method achieves efficient and high-quality robot flow generation. Across standard benchmarks, our method outperforms representative baseline methods on standard metrics, while achieving approximately 33$\times$ faster generation. Furthermore, through real-world experiments evaluating 9 methods with 260 trials per method across 13 manipulation tasks, we show that our method achieves a higher average success rate than the baseline methods. Our project page is available at https://flow-as-flow-u0n5y.kinsta.page.

</details>

---

### [[20_Research/Papers/具身智能/Foresight_Failure_Detection_for_Long-Horizon_Robotic_Manipulation_with_Action-Conditioned_World_Model_Latents|Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents]]

![[assets/2606.23085_figure.png|800]]

- **arXiv**: [2606.23085](https://arxiv.org/abs/2606.23085)
- **PDF**: https://arxiv.org/pdf/2606.23085
- **详细分析**: [[20_Research/Papers/具身智能/Foresight_Failure_Detection_for_Long-Horizon_Robotic_Manipulation_with_Action-Conditioned_World_Model_Latents|Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents]]
- **作者**: Haoran Zhang, Yifu Lu, Boyang Wang, Xuhui Kang, Yen-Ling Kuo, Zezhou Cheng, Mengdi Wang, Odest Chadwicke Jenkins
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.4（加权：具身智能 1.5，世界模型 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored. Detecting failures in long-horizon robotic tasks is particularly challenging because failure onset is often ambiguous and dense temporal annotations are typically unavailable. We present Foresight, a failure detection framework that monitors manipulation trajectories using latent representations from an action-conditioned world model. Foresight is trained using only final task-level success or failure labels. By leveraging predictive world-model embeddings, our method provides a unified framework for failure detection across different policies. We further use functional conformal prediction (FCP) to calibrate detection thresholds adaptively. We evaluate Foresight with state-of-the-art vision-language-action policies in simulation on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K, compare it against state-of-the-artfailure detection methods, and validate it on real robots with three long-horizon tasks on a ReactorX-200 arm and one task on a Franka arm. Our results suggest that action-conditioned world-model embeddings provide a scalable representation for reliable failure monitoring in long-horizon manipulation.

</details>

---

### [[20_Research/Papers/强化学习/TEXEDO_Test_Time_Scaling_for_Controller-aware_Language-conditioned_Humanoid_Motion_Generation|TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation]]

![[assets/2606.22998_figure.png|800]]

- **arXiv**: [2606.22998](https://arxiv.org/abs/2606.22998)
- **PDF**: https://arxiv.org/pdf/2606.22998
- **详细分析**: [[20_Research/Papers/强化学习/TEXEDO_Test_Time_Scaling_for_Controller-aware_Language-conditioned_Humanoid_Motion_Generation|TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation]]
- **作者**: Jianuo Cao, Yuxin Chen, Yuzhen Song, Masayoshi Tomizuka, Chenran Li, Thomas Tian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TEXEDO : Test Time Scaling for Controller-aware Language-conditioned Humanoid Motion Generation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-conditioned motion generation is a promising interface for programming humanoid robots, yet current generators are often trained on human motion datasets retargeted to robot morphologies. Although such data provides rich semantic and kinematic priors, it fails to capture the nuances of whole-body tracking controllers, including balance, contact dynamics, actuation limits, and controller-specific failure modes. As a result, generated motions can be semantically plausible but difficult or impossible for the robot to execute. We introduce TEXEDO, a test-time scaling framework for humanoid motion generation that improves motion quality without requiring a stronger underlying generator. Given a text prompt, TEXEDO samples multiple candidate motions from a pretrained text-conditioned generator and selects the best motion that is both executable and task-aligned. The reward model combines a dynamic feasibility verifier, distilled from whole-body tracking rollouts to predict physical executability, with a semantic alignment verifier that measures text-motion alignment in a learned co-embedding space. Our pipeline treats dynamic feasibility as a hard constraint and semantic alignment as the selection objective within the feasible set. Through large-scale simulation studies and real-world deployment on a Unitree G1 humanoid robot, we show that TEXEDO consistently improves both tracking fidelity and text alignment. These results demonstrate that grounded verification is an effective path toward deployable language-guided humanoid motion generation. Project website: https://jianuocao.github.io/TEXEDO/

</details>

---

### [[20_Research/Papers/具身智能/HiL-ResRL_A_Model-Agnostic_Finetuning_Adapter_via_Human-in-the-loop_Residual_Reinforcement_Learning|HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning]]

![[assets/2606.22860_figure.png|800]]

- **arXiv**: [2606.22860](https://arxiv.org/abs/2606.22860)
- **PDF**: https://arxiv.org/pdf/2606.22860
- **详细分析**: [[20_Research/Papers/具身智能/HiL-ResRL_A_Model-Agnostic_Finetuning_Adapter_via_Human-in-the-loop_Residual_Reinforcement_Learning|HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning]]
- **作者**: Jingyi Liu, Zhaohong Mai, ShunSen He, Hang Ren, Chao Wang, Shunbo Zhou, XiaoDong Wu, Heng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.2，强化学习 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HiL-ResRL: A Model-Agnostic Finetuning Adapter via Human-in-the-loop Residual Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GR-RL, HIL-ResRL, HIL-SERL, HiL-ResRL, RL4VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in generative imitation learning have significantly propelled the field of robotic manipulation. However, the majority of existing models rely heavily on Behavior Cloning (BC), a paradigm that suffers from compounding errors and distributional shift. Consequently, the efficacy of these models in practical industrial deployments remains limited. To address these challenges, we introduce a novel, plug-and-play fine-tuning pipeline designed to facilitate the robust deployment of Vision-Language-Action (VLA) models in real-world environments. In contrast to contemporary reinforcement learning (RL) fine-tuning strategies, which are often constrained by specific model architectures, our proposed framework is model-agnostic and adaptable to a diverse range of VLA models. We conceptualize VLA-generated actions as a unified interface, upon which we train a residual policy. This policy is designed to rectify suboptimal actions and address the distributional shift inherent in imitation learning. Additionally, we incorporate human-in-the-loop guidance to ensure safe exploration and maximize training efficiency. We conduct experiments directly in real-world robotic settings. The results demonstrate that within only 1.5 hour of real-world online RL training, the average success rate exceeds 95% on real robots. Our work presents a practical solution for deploying behavior cloning models in industrial scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Cloak_Zero-Shot_Cross-Embodiment_Manipulation_by_Masking_the_End-Effector_from_the_VLA|Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA]]

![[assets/2606.22836_figure.png|800]]

- **arXiv**: [2606.22836](https://arxiv.org/abs/2606.22836)
- **PDF**: https://arxiv.org/pdf/2606.22836
- **详细分析**: [[20_Research/Papers/具身智能/Cloak_Zero-Shot_Cross-Embodiment_Manipulation_by_Masking_the_End-Effector_from_the_VLA|Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA]]
- **作者**: Michael Piseno, Guy Tevet, C. Karen Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Cloak-VLA, LAP-VLA, OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Cloak, a training recipe that endows a Vision-Language-Action (VLA) model with zero-shot cross-embodiment transfer by cloaking the end-effector from its own wrist camera. The end-effector occupies a large and consistent region of the wrist view and masking it allows for embodiment-agnostic visual reasoning. Cloak renders a mask in simulation from the robot's known geometry, accurately and in real time, with no segmentation or generative models. During training, we augment the mask so the model generalizes to embodiments unseen at training time. We demonstrate the recipe with Cloak-VLA, a VLA trained with Cloak on a single parallel-jaw gripper dataset. No data of new embodiments is ever collected. Cloak-VLA transfers zero-shot to various unseen embodiments, including another gripper, another arm, and a five-fingered hand, while preserving the source embodiment's performance. By decoupling the wrist view from its own embodiment, Cloak allows data to outlive the hardware it was collected on.

</details>

---

### [[20_Research/Papers/具身智能/UniFS_Unified_Fast-to-Slow_Hierarchical_Architecture_for_Vision-Language-Action_Models|UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models]]

![[assets/2606.22794_figure.png|800]]

- **arXiv**: [2606.22794](https://arxiv.org/abs/2606.22794)
- **PDF**: https://arxiv.org/pdf/2606.22794
- **详细分析**: [[20_Research/Papers/具身智能/UniFS_Unified_Fast-to-Slow_Hierarchical_Architecture_for_Vision-Language-Action_Models|UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models]]
- **作者**: Lin Sun, Zhiwei Guan, Conglin Wang, Zihong Chen, Jianhai Yu, Zongsheng Li, Boyong He, Tao Sun, Jiale Cao, Lige Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CogVLA, Deer-VLA, GraspVLA, MemoryVLA, OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational savings. Moreover, because the action expert receives only the VLM's final-layer representation at a single fixed frequency, rich intermediate features are discarded, limiting both information coupling and manipulation precision. Inspired by multi-timescale neural processing in the human brain, we introduce UniFS, a unified fast-to-slow architecture that resolves these challenges through three key designs. First, we stratify the VLM layers into groups with progressively decreasing update frequencies, enabling shallow layers to capture fast-changing dynamics while deeper layers cache stable semantic context. Second, a latent vector inversion mechanism re-routes the interaction order between multi-scale VLM features and the action expert, aligning fast-varying representations with fine-grained action decoding and slow-varying ones with coarse planning. Third, a multi-level supervision strategy enforces a coarse-to-fine learning hierarchy across temporal scales. Together, these designs enable richer cross-frequency information transfer within a single backbone, while the low-frequency pathways additionally preserve temporal context across steps. Experiments on LIBERO show that UniFS achieves state-of-the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup). Real-robot experiments on a Franka platform further validate its practical applicability. Code is opensourced at https://github.com/linsun449/UniFS.

</details>

---

### [[20_Research/Papers/大模型/Temporal_Logic_Guidance_for_Action-Only_Diffusion_Policies_with_World_Models|Temporal Logic Guidance for Action-Only Diffusion Policies with World Models]]

![[assets/2606.22729_figure.png|800]]

- **arXiv**: [2606.22729](https://arxiv.org/abs/2606.22729)
- **PDF**: https://arxiv.org/pdf/2606.22729
- **详细分析**: [[20_Research/Papers/大模型/Temporal_Logic_Guidance_for_Action-Only_Diffusion_Policies_with_World_Models|Temporal Logic Guidance for Action-Only Diffusion Policies with World Models]]
- **作者**: Moritz Zoellner, Anastasios Manganaris, Rohan Paleja
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，世界模型 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Temporal Logic Guidance for Action-Only Diffusion Policies with World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies enable multimodal robot behavior but offer limited ability to choose among behavior modes at inference time, even though such control is desirable in human-robot settings. Prior solutions to this lack of control have utilized Signal Temporal Logic (STL) to express human intentions and provide corresponding guidance for diffusion policy inference. However, these approaches can only guide diffusion policies that jointly generate future actions and states, increasing both complexity and runtime. We propose a novel guidance method for action-only diffusion policies that uses a separate learned world model to enable differentiable evaluation of STL robustness, with its gradient then injected into the diffusion process. This steers behavior toward constraint satisfaction without retraining, improving constraint adherence while preserving task performance. On the Can Transport task from Robomimic, our method maintains 100% task success while reducing constraint violations from over 80% for baseline methods to 4%. We also discuss extensions toward improved robustness and more complex constraints.

</details>

---

### [[20_Research/Papers/机器人/Integrated_cloud-based_architecture_for_robot-robot_and_human-robot_collaboration_using_ROS_2--MQTT_in_Mediterranean_Greenhouses|Integrated cloud-based architecture for robot-robot and human-robot collaboration using ROS 2--MQTT in Mediterranean Greenhouses]]

![[assets/2606.22682_figure.png|800]]

- **arXiv**: [2606.22682](https://arxiv.org/abs/2606.22682)
- **PDF**: https://arxiv.org/pdf/2606.22682
- **详细分析**: [[20_Research/Papers/机器人/Integrated_cloud-based_architecture_for_robot-robot_and_human-robot_collaboration_using_ROS_2--MQTT_in_Mediterranean_Greenhouses|Integrated cloud-based architecture for robot-robot and human-robot collaboration using ROS 2--MQTT in Mediterranean Greenhouses]]
- **作者**: F. Cañadas-Aránega, M. Muñoz, J. C. Moreno, J. L. Blanco-Claraco
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.3，大模型 0.1，机器人 2.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Integrated cloud-based architecture for robot-robot and human-robot collaboration using ROS 2--MQTT in Mediterranean Greenhouses》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MVSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The imperative to develop more sustainable agriculture demands a transition from isolated automation toward the deployment of multi-robot systems (MRS) in agrifood environments. However, Mediterranean greenhouse settings-characterized by narrow corridors, dense biomass, and structural metallic interference-pose significant challenges for robust and scalable communication between agents. Traditional robotic frameworks, such as ROS 2, frequently encounter node discovery issues and latency spikes due to dynamic obstacles, dense foliage, and other characteristic greenhouse elements, creating a critical bottleneck for real-time coordination. This paper proposes an innovative cloud-based hybrid architecture that establishes a two-way communication bridge between ROS 2, acting as an edge computing platform, and iVeg as a Decision Support System (DSS), using MQTT and the European FIWARE platform. The proposed framework enables seamless interoperability between fleets of multiple robots in environments with communication constraints, facilitating the synchronised exchange of high-level telemetry, point cloud data and farmer identification for collaboration, amongst other critical data. The architecture was validated in a high-fidelity simulation environment and subsequently tested in a real-world greenhouse scenario, demonstrating its ability to maintain persistent connectivity and data integrity under adverse network conditions. The results indicate that the integration of MQTT effectively eliminates information silos, providing a scalable and decentralised solution for managing complex robotic missions, which are executed locally via Edge Computing. This work sets a new methodological precedent for the concept of Greenhouse Models as a Service (GMaaS), bridging the gap between low-level robotic control and high-level, cloud-based IoT decision-making.

</details>

---

### [[20_Research/Papers/具身智能/PenduMorph_Development_and_Motion_Analysis_of_Pendulum-Actuated_Rolling_Reconfigurable_Spherical_Robot_with_Magnetic-Coupling|PenduMorph: Development and Motion Analysis of Pendulum-Actuated Rolling Reconfigurable Spherical Robot with Magnetic-Coupling]]

![[assets/2606.22491_figure.png|800]]

- **arXiv**: [2606.22491](https://arxiv.org/abs/2606.22491)
- **PDF**: https://arxiv.org/pdf/2606.22491
- **详细分析**: [[20_Research/Papers/具身智能/PenduMorph_Development_and_Motion_Analysis_of_Pendulum-Actuated_Rolling_Reconfigurable_Spherical_Robot_with_Magnetic-Coupling|PenduMorph: Development and Motion Analysis of Pendulum-Actuated Rolling Reconfigurable Spherical Robot with Magnetic-Coupling]]
- **作者**: Aung Myat, Peter Noyce, May Forgan, Qing Yu, Seyed Amir Tafrishi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《PenduMorph: Development and Motion Analysis of Pendulum-Actuated Rolling Reconfigurable Spherical Robot with Magnetic-Coupling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents "PenduMorph", a wireless reconfigurable rolling spherical robot designed as a modular platform for enclosed locomotion and inter-module interaction in challenging environments. The proposed robot extends our previous pendulum-actuated rolling disk concept to a fully enclosed spherical architecture integrating a 2-DoF internal pendulum, onboard control, battery-powered operation, and magnetic docking. The design aims to combine independent rolling mobility with protected hardware and reliable reconfigurability. We first present the robot design and an analytical study of the magnetic coupling mechanism to evaluate retention and interaction between coupled modules. We then experimentally investigate key motion behaviors at both the single-module and dual-module levels, including independent rolling, magnetic coupling, and coordinated coupled motion. The results show that the proposed platform enables stable wireless operation and a set of distinctive reconfigurable rolling behaviors, providing a useful foundation for future modular spherical robots operating in contact-rich and demanding environments.

</details>

---

### [[20_Research/Papers/具身智能/ARP_Enhancing_Quantized_Skill_Abstractions_via_Visual_Alignment_and_Iterative_Refinement_for_Robotic_Manipulation|ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation]]

![[assets/2606.22480_figure.png|800]]

- **arXiv**: [2606.22480](https://arxiv.org/abs/2606.22480)
- **PDF**: https://arxiv.org/pdf/2606.22480
- **详细分析**: [[20_Research/Papers/具身智能/ARP_Enhancing_Quantized_Skill_Abstractions_via_Visual_Alignment_and_Iterative_Refinement_for_Robotic_Manipulation|ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation]]
- **作者**: Yuntian Wang, Zesheng Jia, Yuhui Duan, Qibing Wang, Yang Liu, Song Wang, Siao Liu, Jin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ARP: Enhancing Quantized Skill Abstractions via Visual Alignment and Iterative Refinement for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning visuomotor policies for long-horizon manipulation remains a fundamental challenge. Recent skill-based imitation learning methods based on discrete quantization have shown promising results by representing complex behaviors as temporally extended skills. However, most existing approaches primarily encode action trajectories into latent skills, yielding weak visual-semantic grounding and limiting the ability to leverage visual observations for skill selection. Moreover, discrete tokenization inevitably incurs precision errors during continuous action generation. To alleviate these issues, we propose Aligned Refinement Policy (ARP), a discrete-skill framework that couples semantic grounding with execution-level refinement. Specifically, ARP introduces (i) a visual--action alignment objective that contrastively aligns visual embeddings with pre-quantized action representations in a shared latent space while preserving a state-independent skill decoder, and (ii) a lightweight Iterative Residual Head (IRH) that performs a two-step refinement to recover fine-grained control for precise execution. Extensive experiments show that ARP achieves state-of-the-art performance on the LIBERO and Meta-World benchmarks. Moreover, real-robot experiments on the Kuavo 4 Pro humanoid platform further validate its effectiveness, yielding consistent performance gains over several baselines on two challenging manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/Scalable_Multi-Task_Data_Generation_via_Reinforcement_Learning_for_Language-Conditioned_Bimanual_Dexterous_Manipulation|Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation]]

![[assets/2606.22471_figure.png|800]]

- **arXiv**: [2606.22471](https://arxiv.org/abs/2606.22471)
- **PDF**: https://arxiv.org/pdf/2606.22471
- **详细分析**: [[20_Research/Papers/强化学习/Scalable_Multi-Task_Data_Generation_via_Reinforcement_Learning_for_Language-Conditioned_Bimanual_Dexterous_Manipulation|Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation]]
- **作者**: Zechu Li, Yufeng Jin, Puze Liu, Jan Peters, Georgia Chalvatzaki
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A key bottleneck in training generalist policies for bimanual dexterous manipulation is the lack of large-scale, high-quality datasets. Synthetic data generation in simulation provides a scalable alternative to human video demonstrations by overcoming challenges such as morphology mismatch, missing physical interactions, and the generation of robot actions. However, existing approaches based on human teleoperation offer limited task diversity, as object-centric trajectory matching often neglects the feasibility of robot execution. Reinforcement learning (RL) enables broader scalability but is often constrained by handcrafted, task-specific rewards. In this work, we propose a systematic RL-based data generation pipeline that integrates generalizable reward design, effective domain randomization, and language-conditioned task annotations. This pipeline synthesizes diverse, high-quality datasets for dexterous bimanual manipulation and enables training of language-conditioned multi-task policies. Our experiments show that the generated data significantly improves generalization across three representative manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/Tactile_Genesis_Exploring_Tactile_Sensors_at_Scale_for_Learning_Dexterous_Tasks|Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks]]

![[assets/2606.22332_first_page.png|800]]

- **arXiv**: [2606.22332](https://arxiv.org/abs/2606.22332)
- **PDF**: https://arxiv.org/pdf/2606.22332
- **详细分析**: [[20_Research/Papers/强化学习/Tactile_Genesis_Exploring_Tactile_Sensors_at_Scale_for_Learning_Dexterous_Tasks|Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks]]
- **作者**: Trinity Chung, Kashu Yamazaki, Dhruv Patel, Alexis Duburcq, Yiling Qiao, Katerina Fragkiadaki, Aran Nayebi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/2026-tactile-genesis/

</details>

---

### [[20_Research/Papers/具身智能/FlowDPG_Deterministic_Policy_Gradient_on_Flow_Matching_Policies_for_Real-World_Manipulation|FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation]]

![[assets/2606.22303_figure.png|800]]

- **arXiv**: [2606.22303](https://arxiv.org/abs/2606.22303)
- **PDF**: https://arxiv.org/pdf/2606.22303
- **详细分析**: [[20_Research/Papers/具身智能/FlowDPG_Deterministic_Policy_Gradient_on_Flow_Matching_Policies_for_Real-World_Manipulation|FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation]]
- **作者**: Kexin Shi, Junyao Shi, Poorvi Hebbar, Zhuolun Zhao, Tarun Amarnath, Yifan Su, Shikhar Bahl, Deepak Pathak
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 1，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FlowDPG: Deterministic Policy Gradient on Flow Matching Policies for Real-World Manipulation》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world reinforcement learning for robotic manipulation remains challenging, and this difficulty is amplified for flow matching policies: applying policy gradient methods to these policies is fundamentally limited by the need to backpropagate through time(BPTT) along the multi-step ODE that maps noise to actions, which is computationally prohibitive and numerically fragile. We propose FlowDPG, a DDPG-style method specifically designed for flow matching policies that distills the critic gradient into the velocity field at training time, bypassing BPTT entirely. Intuitively, FlowDPG combines two complementary vectors: the demonstration-driven velocity that keeps the action feasible, and the critic-driven correction that steers it toward higher value. Our contributions are threefold: (1) a BPTT-free distillation framework that enables stable DDPG-style policy improvement on flow matching policies, (2) a formal connection between the FlowDPG update direction and vanilla Deterministic Policy Gradient via three explicit approximations, and (3) real-world validation on a long-horizon, multi-stage, dual-arm AirPods assembly task, where FlowDPG attains a 92% end-to-end success rate, substantially outperforming recent RL methods spanning value-conditioning, auxiliary-module adaptation, and adjoint-based critic-gradient approaches. Videos and more results are provided on the project page https://flowdpg.github.io.

</details>

---

### [[20_Research/Papers/具身智能/OpenHLM_An_Empirical_Recipe_for_Whole-Body_Humanoid_Loco-Manipulation|OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation]]

![[assets/2606.22174_figure.png|800]]

- **arXiv**: [2606.22174](https://arxiv.org/abs/2606.22174)
- **PDF**: https://arxiv.org/pdf/2606.22174
- **详细分析**: [[20_Research/Papers/具身智能/OpenHLM_An_Empirical_Recipe_for_Whole-Body_Humanoid_Loco-Manipulation|OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation]]
- **作者**: Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, Junming Zhao, Ruiqian Nai, Yang Gao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body humanoid loco-manipulation requires coordinating the robot's entire kinematic chain. However, most existing systems typically decouple the upper and lower bodies into separate controllers, limiting such coordination and yielding behaviors similar to those of a wheeled dual-arm platform. In this paper, we ask what it takes to build a whole-body native vision-language-action (VLA) model that maps language and pixels directly to all of the humanoid's degrees of freedom. We conduct a systematic empirical study organized as a roadmap of one-variable-at-a-time experiments across three phases: whole-body teleoperation, VLA model design, and heterogeneous co-training. Our study yields several intriguing findings: a joint-based whole-body teleoperation interface outperforms alternatives that only partially expose the humanoid's degrees of freedom; a VLA pretrained on static and wheeled dual-arm platforms transfers surprisingly well to a humanoid's full action space; and co-training with HuMI, the humanoid analog of UMI, extends the policy to new objects and instructions without additional whole-body teleoperation on those targets. Following this roadmap yields OpenHLM, an open-source recipe for whole-body humanoid loco-manipulation. In a challenging long-horizon task that spans a wide vertical range of the humanoid, OpenHLM outperforms two state-of-the-art humanoid VLA baselines (GR00T N1.6 and $Ψ_0$) using less than half the total demonstration time. Our code, training data, and model checkpoints are available at [https://openhlm-project.github.io/].

</details>

---

### [[20_Research/Papers/具身智能/Full_Nonlinear_Nonholonomic_Dynamics_and_Motion_Analysis_of_a_3-DoF_Underactuated_Spherical_Rolling_Robot|Full Nonlinear Nonholonomic Dynamics and Motion Analysis of a 3-DoF Underactuated Spherical Rolling Robot]]

![[assets/2606.22169_figure.png|800]]

- **arXiv**: [2606.22169](https://arxiv.org/abs/2606.22169)
- **PDF**: https://arxiv.org/pdf/2606.22169
- **详细分析**: [[20_Research/Papers/具身智能/Full_Nonlinear_Nonholonomic_Dynamics_and_Motion_Analysis_of_a_3-DoF_Underactuated_Spherical_Rolling_Robot|Full Nonlinear Nonholonomic Dynamics and Motion Analysis of a 3-DoF Underactuated Spherical Rolling Robot]]
- **作者**: Lakshmesha Krishnapa, Ahnaf Sharaar Mazahar, Seyed Amir Tafrishi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Full Nonlinear Nonholonomic Dynamics and Motion Analysis of a 3-DoF Underactuated Spherical Rolling Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a full nonlinear constrained dynamic model of MonoRollBot, a novel 3-DoF spherical rolling robot driven by a single motor, a lead-screw transmission, and a spring-coupled internal moving mass, together with motion analysis of its behavior. To the best of our knowledge, this is one of the first full nonlinear nonholonomic models reported for a mono-actuated, super-underactuated spherical rolling robot of this kind. Because rolling without slipping is nonholonomic, the dynamics are derived using the Lagrange--d'Alembert formulation, with the lead-screw relation imposed as a holonomic constraint and the rolling condition imposed in Pfaffian form. The formulation retains the complete generalized coordinates of shell translation, shell attitude, screw travel, nut rotation, and radial mass motion. Simulations and representative motion studies show qualitative agreement with prototype behavior and reveal how gravity, compliance, and inertia jointly shape the locomotion and motion capabilities of this strongly underactuated robot. The resulting model also provides a mechanically consistent basis for future state estimation and hybrid controller design for this nonholonomic mono-actuated rolling robot.

</details>

---

### [[20_Research/Papers/具身智能/RoboLineage_Agent-Native_Data_Lifecycle_Governance_Across_Robot_Policy_Iterations|RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations]]

![[assets/2606.22142_figure.png|800]]

- **arXiv**: [2606.22142](https://arxiv.org/abs/2606.22142)
- **PDF**: https://arxiv.org/pdf/2606.22142
- **详细分析**: [[20_Research/Papers/具身智能/RoboLineage_Agent-Native_Data_Lifecycle_Governance_Across_Robot_Policy_Iterations|RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations]]
- **作者**: Qian Luo, Wentao Guo, Zhennan Qin, Nanchun Guo, Yunhan Zhao, Yi Ma, Yanchao Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.9，大模型 0.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RoboNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present RoboLineage, an agent-native data lifecycle governance system for robot policy iteration. Modern robot policies improve through repeated data collection, review, retraining, evaluation, and release decisions, but the evidence connecting these steps is often scattered across local tools, scripts, and expert memory. RoboLineage makes this lifecycle explicit by representing rollouts, reviews, dataset decisions, training runs, policy metadata, evaluations, deployment recommendations, and next-collection plans as typed lineage artifacts. Agents interpret embodied rollout evidence, adapt accepted data to existing training stacks, maintain data health, and summarize cross-iteration state under explicit artifact boundaries. In real-robot manipulation workflows, RoboLineage makes routine policy iteration faster and more auditable while maintaining downstream policy performance. We open source RoboLineage as a lightweight lifecycle layer for different robot embodiments and training families. Project page: https://robolineage.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Wh0_Generative_World_Models_as_Scalable_Sources_of_Egocentric_Human_Hand_Manipulation_Data|Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data]]

![[assets/2606.22136_figure.png|800]]

- **arXiv**: [2606.22136](https://arxiv.org/abs/2606.22136)
- **PDF**: https://arxiv.org/pdf/2606.22136
- **详细分析**: [[20_Research/Papers/具身智能/Wh0_Generative_World_Models_as_Scalable_Sources_of_Egocentric_Human_Hand_Manipulation_Data|Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data]]
- **作者**: Yangtao Chen, Zixuan Chen, Peiyang Wang, Yong-Lu Li, Jing Huo, Jieqi Shi, Yang Gao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.2，世界模型 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GigaWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling dexterous manipulation requires generalization across objects, scenes, and tasks, yet existing data sources face a trade-off between scale and scene/embodiment alignment: teleoperation data is well aligned with robot deployment but expensive to collect; simulation is scalable but limited by the sim-to-real gap; and real egocentric videos scale effectively but remain misaligned with robot deployment. We propose Wh0, a framework that uses generative video world models as scalable and controllable sources of egocentric human-hand manipulation data to unlock the manipulation capabilities of pretrained dexterous VLA models. Conditioned on language, objects, and scenes, Wh0 uses a generative world model to produce WM-H, a 50k-episode dataset of egocentric human-object interaction videos. Wh0 then converts the generated videos into robot-trainable supervision through hand motion reconstruction and visual editing. Co-trained with a limited amount of real robot data, WM-H adapts pretrained VLA models to dexterous manipulation deployment. Across 18 real-world dexterous manipulation tasks, compared with a model post-trained only on robot data, Wh0 improves zero-shot success on unseen tasks from 8.3% to 38.9%. Ablation studies further show that scalable generation and scene/embodiment alignment are key drivers of performance gains. Videos and open-source code can be found on our project website: https://chenyt31.github.io/wh0.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/DeformX_A_Versatile_Co-Simulation_Framework_for_Deformable_Linear_Objects|DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects]]

![[assets/2606.22116_figure.png|800]]

- **arXiv**: [2606.22116](https://arxiv.org/abs/2606.22116)
- **PDF**: https://arxiv.org/pdf/2606.22116
- **详细分析**: [[20_Research/Papers/具身智能/DeformX_A_Versatile_Co-Simulation_Framework_for_Deformable_Linear_Objects|DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects]]
- **作者**: Yi Yang, Xiang Fei, Lehong Wang, Chenhao Li, Zilin Dai, Henry Kou, Lu Li, Howie Choset
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《DeformX: A Versatile Co-Simulation Framework for Deformable Linear Objects》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deformable linear objects (DLOs) such as wires, cables, and ropes are common in robotic manipulation tasks, yet simulating them with both visual realism and physical accuracy remains challenging. Existing visual simulation methods typically rely on procedural geometric primitives that lack physically grounded deformation behavior, while physics-based approaches with robot learning support often approximate DLOs as rigid-link chains or generic soft bodies, failing to accurately capture the bending, twisting, and shear mechanics of slender elastic structures. In this work, we introduce DeformX, a co-simulation framework that integrates a dedicated Cosserat rod physics engine with NVIDIA Isaac Sim, enabling DLO simulations that are both physically faithful and visually realistic. Our Cosserat rod engine simulates the dynamics and self-collisions of DLOs, and contact interactions with arbitrary free-form meshes. To achieve high-fidelity visualization, we employ mesh skinning to map discrete rod deformations onto imported CAD models. To the best of our knowledge, DeformX is the one of the first frameworks for DLO simulation that unifies realistic visualization, principled physics, and compatibility with robot learning pipelines. We demonstrate its versatility across synthetic data generation and policy learning for DLO manipulation, and validate visual and physical fidelity through comparisons against real-world experiments. Notably, fine-tuning Segment Anything Model 3 (SAM3) on DeformX-generated data yields a 10.2% mAP@75 improvement in real-image wire segmentation, and a rope-swinging policy trained entirely in DeformX achieves a mean target-hitting error of 6.6 cm on a UR5e manipulator in real-world trials, highlighting its strong sim-to-real transfer capability.

</details>

---

### [[20_Research/Papers/具身智能/CoRDE_Concept-Prior_Routed_Diffusion_Experts_for_Structural_Generalization_in_Robot_Manipulation|CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation]]

![[assets/2606.21935_figure.png|800]]

- **arXiv**: [2606.21935](https://arxiv.org/abs/2606.21935)
- **PDF**: https://arxiv.org/pdf/2606.21935
- **详细分析**: [[20_Research/Papers/具身智能/CoRDE_Concept-Prior_Routed_Diffusion_Experts_for_Structural_Generalization_in_Robot_Manipulation|CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation]]
- **作者**: Haidong Huang, Xixin Zhao, Yaohua Zhou, Jiayu Song, Jiayi Zhang, Jun Ma, Haiyue Zhu, Xiaocong Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《CoRDE: Concept-Prior Routed Diffusion Experts for Structural Generalization in Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ForceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models excel at capturing multi-modal action distributions in robot imitation learning. However, in multi-task and long-horizon scenarios, monolithic architectures lack structural generalization capabilities, suffering from gradient conflicts between distinct semantic sub-stages. While pure data-driven Mixture-of-Experts (MoE) methods introduce labor division, they frequently trigger routing collapse, and instantiating full-scale experts causes parameter explosion and high expansion costs. To address these issues, we propose Concept-prior Routed Diffusion Experts (CoRDE), a structure-guided variational distillation framework. CoRDE extracts semantic distributions from a frozen concept encoder to guide the variational posterior responsibility via a learnable soft mapping matrix. This mechanism introduces an entropy-controlled responsibility inference process that encourages confident routing under reliable semantic predictions while preserving the stochastic diffusion term for behavioral diversity. To overcome parameter inflation, CoRDE employs a parameter-efficient expert pool using Low-Rank Adaptation (LoRA) on a shared frozen backbone. Theoretical analysis shows that the mixture score discrepancy is bounded by responsibility-weighted local expert errors, supporting high-fidelity generation under low-rank expert adaptation. Empirical evaluations confirm that, compared to existing baselines, CoRDE systematically reduces routing collapse, forming robust, semantically aligned expert allocations while achieving superior action quality and incremental learning efficiency.

</details>

---

### [[20_Research/Papers/机器人/Predictive_Gaze_Is_Preserved_but_Reorganized_toward_Monitoring_during_Robot-Mediated_Manipulation|Predictive Gaze Is Preserved but Reorganized toward Monitoring during Robot-Mediated Manipulation]]

![[assets/2606.21920_first_page.png|800]]

- **arXiv**: [2606.21920](https://arxiv.org/abs/2606.21920)
- **PDF**: https://arxiv.org/pdf/2606.21920
- **详细分析**: [[20_Research/Papers/机器人/Predictive_Gaze_Is_Preserved_but_Reorganized_toward_Monitoring_during_Robot-Mediated_Manipulation|Predictive Gaze Is Preserved but Reorganized toward Monitoring during Robot-Mediated Manipulation]]
- **作者**: Manuela Uliano, Silvia Fattorini, Marco Controzzi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Predictive Gaze Is Preserved but Reorganized toward Monitoring during Robot-Mediated Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Goal-directed eye movements are a fundamental component of visuomotor control, enabling humans to anticipate and guide their actions. Whether this anticipatory and task-driven behavior is preserved when actions are executed through a robot rather than through one's own body remains unclear. Here we address this question by investigating gaze behavior during goal-directed telemanipulation to determine how visuomotor control adapts to altered embodiment. Our findings show that gaze remains strongly aligned with task goals, preserving its predictive role even during robot-mediated manipulation. At the same time, teleoperation systematically redistributes visual attention toward the robotic end-effector and manipulated objects, increasing online monitoring. These findings show that predictive gaze is not lost under altered embodiment, but reorganized in response to changes in sensory feedback and control demands. More broadly, they reveal the flexibility of the human visuomotor system when the natural sensorimotor coupling is disrupted and identify gaze as an informative signal for inferring action intentions in human-robot interaction.

</details>

---

### [[20_Research/Papers/机器人/A_Novel_Bio-Inspired_Fish_Robot_with_Tunable_Stiffness_via_Particle_Jamming|A Novel Bio-Inspired Fish Robot with Tunable Stiffness via Particle Jamming]]

![[assets/2606.21771_figure.png|800]]

- **arXiv**: [2606.21771](https://arxiv.org/abs/2606.21771)
- **PDF**: https://arxiv.org/pdf/2606.21771
- **详细分析**: [[20_Research/Papers/机器人/A_Novel_Bio-Inspired_Fish_Robot_with_Tunable_Stiffness_via_Particle_Jamming|A Novel Bio-Inspired Fish Robot with Tunable Stiffness via Particle Jamming]]
- **作者**: Jack Stonecipher, Allen Gao, Wei Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Novel Bio-Inspired Fish Robot with Tunable Stiffness via Particle Jamming》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fish achieve efficient swimming across varied speeds through active modulation of their body flexibility. To explore the effects of tunable stiffness on swimming performance, we present a bio-inspired freely swimming fish robot with a rapidly tunable particle-jamming body. This design enables rapid stiffness adjustments with negligible changes in shape or volume, achieving a 54% variation in flexural rigidity across vacuum pressures of 0 to -40 kPa. We visualize the midline of the oscillating body under both low- and high-stiffness conditions, and the comparison confirms that the body curvature varies with stiffness. We further experimentally evaluate the tunable stiffness body's effects on swimming performance using velocity and cost of transport (CoT) measurements obtained via a motion tracking system. Results show that active stiffness tuning is essential for sustaining efficient and high-speed swimming across beating frequencies of 1-3 Hz. At low frequencies (1-1.5 Hz), a softer body (0 kPa) maximizes velocity and minimizes CoT, whereas at high frequencies (2.5-3 Hz), a stiffer body (-40 kPa) delivers superior velocity and reduced transport cost. These findings highlight stiffness modulation as a key strategy for adaptive and efficient propulsion in bio-inspired robotic swimmers.

</details>

---

### [[20_Research/Papers/具身智能/Programmable_magnetic_soft_robots_with_controlled_locomotion_and_directional_liquid_cargo_release|Programmable magnetic soft robots with controlled locomotion and directional liquid cargo release]]

![[assets/2606.21737_first_page.png|800]]

- **arXiv**: [2606.21737](https://arxiv.org/abs/2606.21737)
- **PDF**: https://arxiv.org/pdf/2606.21737
- **详细分析**: [[20_Research/Papers/具身智能/Programmable_magnetic_soft_robots_with_controlled_locomotion_and_directional_liquid_cargo_release|Programmable magnetic soft robots with controlled locomotion and directional liquid cargo release]]
- **作者**: Youyi Zhou, Zoe Evelyn Gureno, Meghna Majumder, Yunus Alapan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Programmable magnetic soft robots with controlled locomotion and directional liquid cargo release》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Magnetically programmable soft elastomers enable complex shape morphing and locomotion dynamics in small scale soft robots under external magnetic fields. Benefiting from their programmed deformation and wireless actuation capabilities, magnetic soft robots have emerged as promising platforms for targeted drug delivery, especially in human gastrointestinal tract. However, achieving controlled directional liquid cargo release toward desired tissue interface while preserving the encoded shape morphing and locomotion capabilities remain a significant challenge. Here, we report a new design strategy that employs an optimized magnetization profile to enable controlled directional release of aqueous cargo without compromising shape morphing and locomotion capabilities. Magnetic soft robots with a specific spatially distributed magnetization profile allow directional alignment of the release interface with the orientation of the external magnetic field. This orientation control ensures active alignment of the release interface toward the intestinal wall prior to drug release. An interconnected microporous elastomer is embedded within the robot for aqueous cargo storage, while a thin microcrystalline wax layer seals the release opening hole to isolate the stored liquid cargo from external environment during transport. Triggered release is achieved by mechanically rupturing the wax sealing layer under a higher magnitude external magnetic field. Controlled directional flipping, locomotion, and triggered release are decoupled through external magnetic field's direction and strength. The controlled directional release strategy reported here integrates directional targeted liquid cargo release, shape morphing, and locomotion, which establishes the groundwork for target drug delivery in gastrointestinal tract applications.

</details>

---

### [[20_Research/Papers/具身智能/VQActFlow_Vector-Quantized_Action_Mode_Steering_for_Multi-Task_Robot_Manipulation|VQActFlow: Vector-Quantized Action Mode Steering for Multi-Task Robot Manipulation]]

![[assets/2606.21600_figure.png|800]]

- **arXiv**: [2606.21600](https://arxiv.org/abs/2606.21600)
- **PDF**: https://arxiv.org/pdf/2606.21600
- **详细分析**: [[20_Research/Papers/具身智能/VQActFlow_Vector-Quantized_Action_Mode_Steering_for_Multi-Task_Robot_Manipulation|VQActFlow: Vector-Quantized Action Mode Steering for Multi-Task Robot Manipulation]]
- **作者**: Zhigen Zhao, Mark Leggiero, Yipu Chen, Haoran Liu, Yifan Wu, Huishu Xue, Sirui Zhan, Ye Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VQActFlow: Vector-Quantized Action Mode Steering for Multi-Task Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-task robot manipulation policies are challenging to learn from demonstration because traditionally a single network must select among qualitatively different action modes from a multimodal demonstration distribution, conditioned on language and visual context. A wrong mode selection means executing the wrong task or an action infeasible in the scene. Tokenizing continuous actions into a learned discrete codebook separates these modes at the representation level, offering structural advantages for multi-task learning. We propose VQActFlow, a multi-task manipulation policy that tokenizes action chunks and generates code sequences via Variational Flow Matching. VQActFlow maintains an explicit preference over action modes throughout generation. Inference-time guidance acts on this preference to steer mode commitment. We instantiate this with classifier-free guidance over language conditioning, which steers the policy toward the instructed action mode, and a learned codebook critic that supplies a complementary feasibility signal. We evaluate VQActFlow on three platforms: the LIBERO simulation benchmarks, a Unitree G1 humanoid performing whole-body pick-and-place, and an ALOHA-style bimanual platform performing contact-rich tasks. Across these benchmarks, VQActFlow outperforms both continuous and discrete baselines.

</details>

---

### [[20_Research/Papers/具身智能/Robot_Critics_that_Sweat_the_Small_Stuff|Robot Critics that Sweat the Small Stuff]]

![[assets/2606.21572_figure.png|800]]

- **arXiv**: [2606.21572](https://arxiv.org/abs/2606.21572)
- **PDF**: https://arxiv.org/pdf/2606.21572
- **详细分析**: [[20_Research/Papers/具身智能/Robot_Critics_that_Sweat_the_Small_Stuff|Robot Critics that Sweat the Small Stuff]]
- **作者**: Sruthi Sudhakar, Junbang Liang, Sreehari Rammohan, Pavel Tokmakov, Richard Zemel, Carl Vondrick
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Robot Critics that Sweat the Small Stuff》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large vision-language models contain several priors about the world and object interactions, making them useful critics during inference to steer robot policies towards success. However, closed-loop robot manipulation requires judging small visual differences between success and failure, which remains a challenge for current VLMs. We introduce a method to fine-tune critics by constructing pairwise progress supervision using success and failure rollouts obtained from a policy. Our fine-tuned critic excels at fine-grained progress reasoning and subtle failure detection, outperforming prior progress reasoning baselines. Additionally, we use an action-conditioned video model to predict the visual effect of several candidate actions sampled from a policy, and show that our critic can correctly identify successful candidates to execute, improving the average policy success rate by 11% across real-world tasks and 5.9% across simulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/UniviewVLA_A_Unified_Multiview_Vision-Language-Action_Model_with_World_Modeling|UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling]]

![[assets/2606.21501_figure.png|800]]

- **arXiv**: [2606.21501](https://arxiv.org/abs/2606.21501)
- **PDF**: https://arxiv.org/pdf/2606.21501
- **详细分析**: [[20_Research/Papers/具身智能/UniviewVLA_A_Unified_Multiview_Vision-Language-Action_Model_with_World_Modeling|UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling]]
- **作者**: Tao Xu, Runhao Zhang, Zhijian Huang, Jiayi Guan, Jiaxin Wang, Yifan Ding, Yong-Lu Li, Long Chen, Guang Chen, Jinghui Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《UniviewVLA: A Unified Multiview Vision-Language-Action Model with World Modeling》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL, UniVLA, UniviewVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Occluded tasks remain a bottleneck in robot manipulation. Existing solutions either deploy additional physical cameras requiring training-inference camera parity, or rely on explicit 3D reconstruction with high computational cost. Moreover, both approaches rely on standard agent-view and wrist-view observations, while failing to capture occlusion information and future scene evolution. To this end, we propose UniviewVLA, a unified multiview Vision-Language-Action model with world modeling, which infers multiview scene evolution for action prediction from only standard two-camera observations. We demonstrate that by leveraging generated multiview future views from the world model, UniviewVLA reveals occluded cues and models future scene evolution, improving action prediction and removing the need for extra hardware or explicit reconstruction. Besides, to accelerate inference while preserving prediction accuracy, UniviewVLA develops Motion-Informative Token Compression, which compresses each generated view from 625 to 16 tokens and reduces per-view latency from 6-7s to 0.2-0.3s. UniviewVLA also proposes training-free Action-Entropy View Selection, which dynamically identifies the most action-informative view at different inference stages. Extensive experiments show that UniviewVLA achieves 95.8% on LIBERO and 4.60 on CALVIN ABCD to D, both standard occlusion-free benchmarks. On customized occlusion-focused tasks, it improves success rate from 40.0% to 73.3%, and average real-robot success rate by 33.4 points, demonstrating stronger occlusion-focused performance without sacrificing standard occlusion-free benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Manipulider_A_Multi-Engine_Buoyancy-Controlled_Robot_for_Thrusterless_Underwater_Gliding_and_Manipulation|Manipulider: A Multi-Engine Buoyancy-Controlled Robot for Thrusterless Underwater Gliding and Manipulation]]

![[assets/2606.21461_figure.png|800]]

- **arXiv**: [2606.21461](https://arxiv.org/abs/2606.21461)
- **PDF**: https://arxiv.org/pdf/2606.21461
- **详细分析**: [[20_Research/Papers/具身智能/Manipulider_A_Multi-Engine_Buoyancy-Controlled_Robot_for_Thrusterless_Underwater_Gliding_and_Manipulation|Manipulider: A Multi-Engine Buoyancy-Controlled Robot for Thrusterless Underwater Gliding and Manipulation]]
- **作者**: Yitao Jiang, Yewei Huang, Weizhi Cao, Mingi Jeong, Alberto Quattrini Li, Luyang Zhao, Muhao Chen, Devin Balkcom
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Manipulider: A Multi-Engine Buoyancy-Controlled Robot for Thrusterless Underwater Gliding and Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Manipulider is a buoyancy-actuated underwater robot that enables thrusterless, glide-like locomotion and attitude-based manipulation, while providing a magnetic modular interface for rapid payload swapping (e.g., a gripper or sensors). Four syringe-based buoyancy engines distributed around the body jointly regulate net buoyancy and the center of buoyancy, allowing the vehicle to maintain large tilt angles through static force balance without continuous thrust and to avoid propeller entanglement risks. We present the mechanical and electrical design, calibration procedure, and control architecture. Experiments with a gripper attached (no external payload) show a controllable buoyancy-displacement range of 40 mL per engine ({\approx}160 g total buoyancy authority), maximum statically stable tilts of 64.6° (single-engine) and 61.8° (dual-engine), and representative vertical and tilt-transition dynamics. We further demonstrate tilt regulation, controlled ascent/descent primitives, and a proof-of-concept gripper-based payload-transport sequence without thrusters.

</details>

---

### [[20_Research/Papers/机器人/Temporal_logics_and_formal_synthesis_for_robot_planning_and_control|Temporal logics and formal synthesis for robot planning and control]]

![[assets/2606.21438_first_page.png|800]]

- **arXiv**: [2606.21438](https://arxiv.org/abs/2606.21438)
- **PDF**: https://arxiv.org/pdf/2606.21438
- **详细分析**: [[20_Research/Papers/机器人/Temporal_logics_and_formal_synthesis_for_robot_planning_and_control|Temporal logics and formal synthesis for robot planning and control]]
- **作者**: Jana Tumova, Joris Verhagen, Matti Vahs
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Temporal logics and formal synthesis for robot planning and control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robots move from controlled environments into real-world settings, it becomes increasingly crucial to ensure that they perform as expected. A key step toward that goal is a rigorous specification of the desired robot behavior, capturing intricate temporal, spatial, and logical requirements. Complementing this, plan and control synthesis methods are needed to fulfill these specifications with provable guarantees. This manuscript presents temporal logics - particularly linear and signal temporal logic - as expressive specification languages for robot behavior over time. We then discuss principles of formal synthesis, from discrete graph- and game-based approaches to sampling-based motion planning, trajectory optimization, and control-certificate-based synthesis. Finally, we outline challenges in deploying formal synthesis in real-world robotics, emphasizing the interplay between modeling fidelity, computational tractability, and the types of rigorous guarantees that can be achieved.

</details>

---

### [[20_Research/Papers/具身智能/BIT-Nav_Brain-Inspired_Trajectory_Memory_for_Embodied_Navigation|BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation]]

![[assets/2606.21398_figure.png|800]]

- **arXiv**: [2606.21398](https://arxiv.org/abs/2606.21398)
- **PDF**: https://arxiv.org/pdf/2606.21398
- **详细分析**: [[20_Research/Papers/具身智能/BIT-Nav_Brain-Inspired_Trajectory_Memory_for_Embodied_Navigation|BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation]]
- **作者**: Rithvik Jonna, Aakash Gurram, Man Namgung, Wyatt Mackey, Tinoosh Mohsenin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《BIT-Nav: Brain-Inspired Trajectory Memory for Embodied Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CURL, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Models (VLMs) for embodied navigation rely on selecting a fixed number of frames from a growing trajectory history. As episodes extend, this selection grows increasingly sparse, yet prior work shows no accuracy gain when scaling from 8 to 64 frames, suggesting the bottleneck is not frame quantity but the representation itself. Sparse frame selection cannot capture the structured behavioral signal that long-horizon reasoning requires: turning patterns, cumulative displacement, and path topology. We introduce BIT-Nav (Brain-Inspired Trajectory Memory for Navigation), a framework that augments frozen VLM navigation pipelines with a compact learned trajectory memory. Motivated by hippocampal path integration, where spatial experience is compressed into structured episodic traces rather than stored as raw sensory replay, BIT-Nav trains a Bi-GRU encoder over action and relative pose sequences via a multi-positive InfoNCE contrastive objective on trajectory prefixes sharing the same behavioral intent. The resulting embedding is projected into the VLM token space via a lightweight MLP and injected as a single memory token at each decision step, conditioning the model on structured motion history at constant token cost regardless of episode length

</details>

---

### [[20_Research/Papers/强化学习/Overcoming_Imperfect_Kinematics_in_Surgical_Robotics_Through_Sim-to-Real_Visuomotor_Learning|Overcoming Imperfect Kinematics in Surgical Robotics Through Sim-to-Real Visuomotor Learning]]

![[assets/2606.21396_figure.png|800]]

- **arXiv**: [2606.21396](https://arxiv.org/abs/2606.21396)
- **PDF**: https://arxiv.org/pdf/2606.21396
- **详细分析**: [[20_Research/Papers/强化学习/Overcoming_Imperfect_Kinematics_in_Surgical_Robotics_Through_Sim-to-Real_Visuomotor_Learning|Overcoming Imperfect Kinematics in Surgical Robotics Through Sim-to-Real Visuomotor Learning]]
- **作者**: Zhaoxuan Yan, Kaizhong Deng, Zhaoyang Jacopo Hu, George P. Mylonas, Daniel S. Elson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Overcoming Imperfect Kinematics in Surgical Robotics Through Sim-to-Real Visuomotor Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-Assisted Surgery is integral to modern minimally invasive procedures, with automation emerging as the next frontier to enhance precision and reduce surgeon fatigue. This evolution is largely impeded by the inherent kinematic inaccuracies of surgical robots, where unreliable internal sensors lead to significant control errors. While previous methods attempted to mitigate these issues through complex model-based calibration, they often suffer from high cost and limited effectiveness. This work utilises a learning-policy to actively compensate for hardware inaccuracies using closed-loop visual feedback that was trained from a teacher-student learning framework. The policy can fuse unreliable internal readings with precise external visual data, allowing it to correct for kinematic errors in real time without needing a perfect physical model. The learned policy was successfully deployed on the da Vinci Research Kit, where experiments validated the fundamental feasibility of using external vision to overcome internal sensor deficits. This research provides a foundational and reliable control methodology, paving the way for more advanced and robust surgical automation.

</details>

---

### [[20_Research/Papers/具身智能/Long-Distance_Real-World_Navigation_of_the_Legged-Wheeled_Robot_Go2-W_Using_Deep_Reinforcement_Learning|Long-Distance Real-World Navigation of the Legged-Wheeled Robot Go2-W Using Deep Reinforcement Learning]]

![[assets/2606.21387_figure.png|800]]

- **arXiv**: [2606.21387](https://arxiv.org/abs/2606.21387)
- **PDF**: https://arxiv.org/pdf/2606.21387
- **详细分析**: [[20_Research/Papers/具身智能/Long-Distance_Real-World_Navigation_of_the_Legged-Wheeled_Robot_Go2-W_Using_Deep_Reinforcement_Learning|Long-Distance Real-World Navigation of the Legged-Wheeled Robot Go2-W Using Deep Reinforcement Learning]]
- **作者**: Takaaki Matsuzawa, Kiyoshi Irie, Tomoaki Yoshida, Taro Suzuki, Yoshitaka Hara, Masahiro Tomono
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 3.8（加权：具身智能 0.9，强化学习 1.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Long-Distance Real-World Navigation of the Legged-Wheeled Robot Go2-W Using Deep Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, IsaacGym, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged-wheeled robots have long been studied for their potential to combine the efficient flat-ground mobility of wheels with the rough-terrain capability of legs. However, examples of their application to long-range autonomous navigation in real environments remain limited. This paper reports our effort to build a deep reinforcement learning (DRL) based locomotion controller and an autonomous navigation system for the commercially available legged-wheeled robot Go2-W, and to apply them to long-range autonomous navigation in a real environment. For locomotion control, we extended a proprioception-only policy, which we had previously developed for quadruped robots, to the 16-DoF legged-wheeled robot. We also found that wheeled locomotion concentrates the load on the hip joints and causes heat concentration that hinders sustained travel, and obtained a policy that suppresses it by distributing the load. We evaluated the system at the Tsukuba Challenge 2025, demonstrating that it can autonomously traverse an approximately 2.8 km route including sidewalks, a park, and stairs without stopping due to overheating.

</details>

---

### [[20_Research/Papers/具身智能/A_Human-Inspired_Thumb-Index_Robotic_Hand_with_Strain_Gauges_Embedded_in_Soft_Joints|A Human-Inspired Thumb-Index Robotic Hand with Strain Gauges Embedded in Soft Joints]]

![[assets/2606.21245_figure.png|800]]

- **arXiv**: [2606.21245](https://arxiv.org/abs/2606.21245)
- **PDF**: https://arxiv.org/pdf/2606.21245
- **详细分析**: [[20_Research/Papers/具身智能/A_Human-Inspired_Thumb-Index_Robotic_Hand_with_Strain_Gauges_Embedded_in_Soft_Joints|A Human-Inspired Thumb-Index Robotic Hand with Strain Gauges Embedded in Soft Joints]]
- **作者**: Jonas Papenbrock, Shubhan Patni, Tomaso Lisini Baldi, Michele Guerri, Elia Landi, Ada Fort, Matej Hoffmann
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《A Human-Inspired Thumb-Index Robotic Hand with Strain Gauges Embedded in Soft Joints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human hand grasp adaptation depends mainly on the synergy between physical structure and biological feedback. Inspired by this biomechanical principle, the Safe Thumb-Index Robotic (STIR) Hand was developed as a minimal, lightweight, and low-cost two-digit prototype featuring an asymmetric thumb-index configuration. By pairing an underactuated, tendon-driven mechanical design with flexible strain gauges embedded into silicone-encapsulated soft joints, the system achieves passive grasp adaptation while establishing both internal proprioception and external perception. Unsupervised analysis was carried out on a dataset of the STIR hand grasping 20 different objects, along with an object classification task and an ablation study to highlight the contribution of the soft joint sensors. The object classification task discriminated object size, shape, and material stiffness with a high classification accuracy. In contrast to traditional industrial grippers and robotic hands, the STIR Hand demonstrates that sensorized compliant joints significantly improve overall sensitivity and ensure safe grasping, while remaining independent of additional fingertip tactile elements or external vision systems. Finally, a comparison to similar devices grasping identical objects validates the utility of the STIR Hand.

</details>

---

### [[20_Research/Papers/机器人/Ultra-Fusion_A_Resilient_Tightly-Coupled_Multi-Sensor_Fusion_SLAM_Framework_under_Sensor_Degradation_and_Spatiotemporal_Perturbation_for_Int|Ultra-Fusion: A Resilient Tightly-Coupled Multi-Sensor Fusion SLAM Framework under Sensor Degradation and Spatiotemporal Perturbation for Intelligent Transportation Systems]]

![[assets/2606.21223_figure.png|800]]

- **arXiv**: [2606.21223](https://arxiv.org/abs/2606.21223)
- **PDF**: https://arxiv.org/pdf/2606.21223
- **详细分析**: [[20_Research/Papers/机器人/Ultra-Fusion_A_Resilient_Tightly-Coupled_Multi-Sensor_Fusion_SLAM_Framework_under_Sensor_Degradation_and_Spatiotemporal_Perturbation_for_Int|Ultra-Fusion: A Resilient Tightly-Coupled Multi-Sensor Fusion SLAM Framework under Sensor Degradation and Spatiotemporal Perturbation for Intelligent Transportation Systems]]
- **作者**: Yihong Tian, Junjie Zhang, Liuyang Li, Deteng Zhang, Yunfei Zuo, Jie Yin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Ultra-Fusion: A Resilient Tightly-Coupled Multi-Sensor Fusion SLAM Framework under Sensor Degradation and Spatiotemporal Perturbation for Intelligent Transportation Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable localization is essential for intelligent transportation systems (ITS), including autonomous vehicles, quadruped last-mile carriers, and infrastructure-inspection unmanned aerial vehicles (UAVs). Although tightly-coupled multi-sensor fusion improves accuracy in favorable conditions, deployed systems remain vulnerable to sensor degradation -- poor illumination, LiDAR degeneracy, wheel slippage, and GNSS outage -- and to spatiotemporal calibration errors. These failures are common in urban canyons, tunnels, and high-speed corridors, where localization drift can degrade route tracking, tunnel passage continuity, and local map alignment. This paper presents Ultra-Fusion, a tightly-coupled multi-sensor localization framework based on a unified sliding-window estimator. Asynchronous measurements are timestamp-ordered and converted into optional factors within one optimization window, supporting WIO, VIO, LIO, and LVIO with optional wheel and GNSS augmentation. Observability-aware initialization selects the bootstrap mode, factor-wise reliability scheduling gates degraded measurements, and online LiDAR--IMU spatiotemporal calibration refines temporal offsets and rotational extrinsics during operation. We extend the M3DGR benchmark with simulation trajectories and evaluate more than 60 open-source SLAM systems on M3DGR, M2DGR-Plus, KAIST, GrandTour, and MARS-LVIG. The results show competitive accuracy across wheeled, legged, and aerial platforms under long-duration and high-speed operation, degradation, and calibration perturbation, improving localization availability for road-level autonomy, campus and warehouse mobility, and low-altitude aerial inspection. To benefit the industrial and academic community, we will release source code and datasets upon paper acceptance.

</details>

---

### [[20_Research/Papers/具身智能/Pose-Agnostic_Robotic_Functional_Grasping_via_Observation-Action_Canonicalization|Pose-Agnostic Robotic Functional Grasping via Observation-Action Canonicalization]]

![[assets/2606.21148_figure.png|800]]

- **arXiv**: [2606.21148](https://arxiv.org/abs/2606.21148)
- **PDF**: https://arxiv.org/pdf/2606.21148
- **详细分析**: [[20_Research/Papers/具身智能/Pose-Agnostic_Robotic_Functional_Grasping_via_Observation-Action_Canonicalization|Pose-Agnostic Robotic Functional Grasping via Observation-Action Canonicalization]]
- **作者**: Le Qiu, Cole Harrison, Jiankai Sun, Yao Liu, Suning Huang, Qianzhong Chen, Yang You, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Pose-Agnostic Robotic Functional Grasping via Observation-Action Canonicalization》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Functional robotic grasping requires a policy that generalizes across diverse object geometries and poses while maintaining task-specific contact precision. We study this challenge through mug-handle grasping, where thin handles, instance variation, and upright or inverted placements make both perception and control sensitive to object configuration. Grasp pose detection methods operate open-loop and are sensitive to estimation errors on thin handle structures. Learned visuomotor policies must implicitly learn to handle the coupled variation in visual appearance and action direction induced by different object placements, limiting generalization. We propose AnyMug, a canonicalized visuomotor reinforcement learning framework for functional grasping that trains a single closed-loop policy entirely in simulation and deploys it zero-shot on a real robot. AnyMug introduces observation-action canonicalization, which transforms both the depth observation and the predicted end-effector action into a shared object-centric frame. The policy therefore sees a consistent mug-centered view and emits actions in a canonical direction regardless of mug placement, allowing the same grasping behavior to be reused across configurations. A handle-aware reward further encourages precise approach, gripper alignment, and opposing-finger placement, while a pose curriculum and domain randomization improve training stability and sim-to-real transfer. In simulation, AnyMug achieves over 93% success rate on both unseen upright and inverted mugs and transfers zero-shot to a real Franka Panda, reaching 80% success rate on 5 held-out physical mugs across both pose categories.

</details>

---

### [[20_Research/Papers/具身智能/MV-WAM_Manifold-Aware_World_Action_Model_with_Value_Augmentation|MV-WAM: Manifold-Aware World Action Model with Value Augmentation]]

![[assets/2606.21088_figure.png|800]]

- **arXiv**: [2606.21088](https://arxiv.org/abs/2606.21088)
- **PDF**: https://arxiv.org/pdf/2606.21088
- **详细分析**: [[20_Research/Papers/具身智能/MV-WAM_Manifold-Aware_World_Action_Model_with_Value_Augmentation|MV-WAM: Manifold-Aware World Action Model with Value Augmentation]]
- **作者**: Jintao Chen, Peidong Jia, Qingpo Wuwu, Jiaming Liu, Mengfei Du, Chun-Kai Fan, Xiaowei Chi, Hao Chen, Chengyu Bai, Zezhong Qian, Hao Wang, Jiajun Cao...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《MV-WAM: Manifold-Aware World Action Model with Value Augmentation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving robust and generalizable manipulation across diverse environments remains a fundamental challenge in embodied robotics. Recent world action models achieve strong in-domain performance, yet their gains do not extend proportionally to out-of-distribution scenarios. We attribute this to a structural mismatch between visual and action modalities, whose intrinsically heterogeneous manifolds cause joint optimization to disproportionately degrade action robustness under distribution shift. To address this, we propose MV-WAM, a novel end-to-end framework that jointly models visual prediction, action generation, and value estimation designed to effectively leverage video priors during both training and inference for enhanced action generalization. Key to this unification is a cross-modality causal mask that hierarchically grounds actions in predicted video frames and value function tokens in both modalities. To further narrow the generalization gap, MV-WAM adopts a manifold-aware optimization scheme that explicitly accounts for the structural heterogeneity across modalities. Finally, MV-WAM introduces a progress-value regulation mechanism that estimates task completion and detects misalignment between predicted frames and generated actions, enabling the policy to autonomously identify execution deviations and recover through value-guided rollback. On the RoboTwin simulation, MV-WAM achieves a 55.7% mean success rate on random scenarios without any randomized action supervision, outperforming the strongest baseline by 29.3%. MV-WAM achieves a 77.5% mean success rate across four real-world tasks of varying difficulty on a dual-arm robot. Our results demonstrate that manifold-aware cross-modal alignment is essential for robust policy generalization, offering a path toward deployable robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Duet_Dual-Robot_Understanding_via_Efficient_Teaching|Duet: Dual-Robot Understanding via Efficient Teaching]]

![[assets/2606.20990_figure.png|800]]

- **arXiv**: [2606.20990](https://arxiv.org/abs/2606.20990)
- **PDF**: https://arxiv.org/pdf/2606.20990
- **详细分析**: [[20_Research/Papers/机器人/Duet_Dual-Robot_Understanding_via_Efficient_Teaching|Duet: Dual-Robot Understanding via Efficient Teaching]]
- **作者**: Yiqi Zhao, Ruohai Ge, Celina Shiyu Wang, Junjie Ye, Muchen Xu, Minhao Li, Sergey Zakharov, Basile Van Hoorick, Vitor Campagnolo Guizilini, Leonidas Guibas, Gaurav S. Sukhatme, Jyotirmoy V. Deshmukh...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Duet: Dual-Robot Understanding via Efficient Teaching》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dual-robot collaboration enables tasks that exceed the reach and payload of a single robot, such as collaboratively transporting objects across environments and executing coordinated handovers. Data acquisition is the primary bottleneck for training these systems. To this end, we introduce DUET, a dual-robot learning framework for mobile manipulation. For efficient data collection, we create a unified dual-embodiment synchronized VR-based teleoperation system for in-domain heterogeneous robot data collection. We further develop a complementary tracking pipeline that records human-human coordination and collaborative mobile manipulation priors. To allow efficient learning, we introduce an Action Chunking Transformer based architecture that first pretrains collaborative policies on efficient human-human demonstrations, before finetuning them on a minimal set of real-robot teleoperation trajectories. We develop a benchmark of four collaborative tasks to evaluate our framework using a Unitree G1 humanoid and a Dexmate Vega1 mobile manipulator. The results demonstrate that harnessing human priors not only yields superior task performance compared to baselines trained only on robot data, but also reduces the total human effort required for data collection. Our human data collection pipeline achieves 5.4x acceleration on average from teleoperation, but we perform equally or better than robot-only data trained policies across all tasks. Our project page is available at https://zhaoy37.github.io/Duet/.

</details>

---

### [[20_Research/Papers/强化学习/Heterogeneous_Policy_Networks_for_Composite_Robot_Team_Communication_and_Coordination|Heterogeneous Policy Networks for Composite Robot Team Communication and Coordination]]

![[assets/2606.20962_figure.png|800]]

- **arXiv**: [2606.20962](https://arxiv.org/abs/2606.20962)
- **PDF**: https://arxiv.org/pdf/2606.20962
- **详细分析**: [[20_Research/Papers/强化学习/Heterogeneous_Policy_Networks_for_Composite_Robot_Team_Communication_and_Coordination|Heterogeneous Policy Networks for Composite Robot Team Communication and Coordination]]
- **作者**: Esmaeil Seraj, Rohan Paleja, Luis Pimentel, Kin Man Lee, Zheyuan Wang, Daniel Martin, Matthew Sklar, John Zhang, Zahi Kakish, Matthew Gombolay
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Heterogeneous Policy Networks for Composite Robot Team Communication and Coordination》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CommNet, G2ANet, HMAGQ-Net, HetNet, MARL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-performing human-human teams learn intelligent and efficient communication and coordination strategies to maximize their joint utility. These teams implicitly understand the different roles of heterogeneous team members and adapt their communication protocols accordingly. Multi-Agent Reinforcement Learning (MARL) has attempted to develop computational methods for synthesizing such joint coordination-communication strategies, but emulating heterogeneous communication patterns across agents with different state, action, and observation spaces has remained a challenge. Without properly modeling agent heterogeneity, as in prior MARL work that leverages homogeneous graph networks, communication becomes less helpful and can even deteriorate the team's performance. In the past, we proposed Heterogeneous Policy Networks (HetNet) to learn efficient and diverse communication models for coordinating cooperative heterogeneous teams. In this extended work, we extend Heterogeneous Policy Networks (HetNet) to support scaling heterogeneous robot teams. Building on heterogeneous graph-attention networks, we show that HetNet not only facilitates learning heterogeneous collaborative policies but also enables end-to-end training for learning highly efficient binarized messaging. Our empirical evaluation shows that HetNet sets a new state of the art in learning coordination and communication strategies for heterogeneous multi-agent teams by achieving an 5.84% to 707.65% performance improvement over the next-best baseline across multiple domains while simultaneously achieving a 200x reduction in the required communication bandwidth.

</details>

---

### [[20_Research/Papers/具身智能/Perturbation-Based_Uncertainty_for_Failure_Detection_in_Vision-Language-Action_Models|Perturbation-Based Uncertainty for Failure Detection in Vision-Language-Action Models]]

![[assets/2606.20754_figure.png|800]]

- **arXiv**: [2606.20754](https://arxiv.org/abs/2606.20754)
- **PDF**: https://arxiv.org/pdf/2606.20754
- **详细分析**: [[20_Research/Papers/具身智能/Perturbation-Based_Uncertainty_for_Failure_Detection_in_Vision-Language-Action_Models|Perturbation-Based Uncertainty for Failure Detection in Vision-Language-Action Models]]
- **作者**: Yousung Lee, Dongsoo Har
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Perturbation-Based Uncertainty for Failure Detection in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but reliable uncertainty quantification remains challenging, particularly under distribution shift. Unlike autoregressive policies, many modern VLA models generate continuous actions through regression or flow-based generation, where explicit predictive probabilities are unavailable. Moreover, existing approaches often rely on stochastic action sampling or supervised failure labels, limiting their applicability across diverse pretrained VLA models. In this work, we propose a label-free and model-agnostic framework for inference-time uncertainty estimation through hidden activation perturbations, motivated by Bayesian perspectives on local model variations. Specifically, we inject Gaussian perturbations into transformer hidden activations and estimate epistemic signals from disagreement across perturbed action predictions. Experiments on LIBERO and LIBERO-PRO show that perturbation-based uncertainty consistently improves failure detection under distribution shift compared to sampling-based uncertainty, providing a practical uncertainty signal for VLA models.

</details>

---

### [[20_Research/Papers/具身智能/SafeDojo_Safe_Reinforcement_Learning_for_VLA_via_Interactive_World_Model|SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model]]

![[assets/2606.20698_figure.png|800]]

- **arXiv**: [2606.20698](https://arxiv.org/abs/2606.20698)
- **PDF**: https://arxiv.org/pdf/2606.20698
- **详细分析**: [[20_Research/Papers/具身智能/SafeDojo_Safe_Reinforcement_Learning_for_VLA_via_Interactive_World_Model|SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model]]
- **作者**: Kai Tang, Peidong Jia, Zhong Chu, Jixian Wu, Rui Ma, Jiajun Cao, Fangyuan Zhao, Sixiang Chen, Yichen Guo, Xiaowei Chi, Chun-Kai Fan, Kevin Zhang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型, 机器人
- **相关性评分**: 3.7（加权：具身智能 1.8，强化学习 0.8，世界模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, ResNet, SafeLIBERO。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe control is a prerequisite for real-world embodied intelligence, for which safe reinforcement learning has emerged as a promising paradigm. However, existing safe reinforcement learning methods either require costly real-world exploration or depend on hand-crafted safety functions. Neither scales to vision-language-action models deployed in open-world physical environments. We propose SafeDojo, the first model-based safe reinforcement learning framework for vision-language-action policies designed to learn safe actions through world model-based imagination. Specifically, SafeDojo performs online reinforcement learning on top of an interactive video world model. The world model generates action-conditioned future predictions, from which a tailored ResNet success classifier estimates per-step task progress from imagined frames and a lightweight safety head predicts per-step safety costs from latent context together with the proposed action chunk, enabling simultaneous assessment of task execution and trajectory safety. The decoupled task-reward and safety-cost signals are balanced through a Lagrangian-based constrained GRPO objective, enabling coordinated improvement of task success and safety under explicit constraints. On SafeLIBERO, SafeDojo achieves the best aggregate task success, safe success, and execution efficiency among inference-time safety, model-free RL, and model-based RL baselines, with the best average safe-success rate on both levels and an 8.25 percentage-point improvement over the strongest baseline on Level I. Real-world Franka deployment further shows the best average task and safe-success rates across five tasks. Our results position world model-based safe reinforcement learning as a scalable and generalizable path toward safe embodied intelligence.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Control_as_Enabling_Layer_for_Embodied_Intelligence_Research_explored_with_Soft_Robotic_Swimming_in_diverse_Flow_Speeds|Learning Control as Enabling Layer for Embodied Intelligence Research explored with Soft Robotic Swimming in diverse Flow Speeds]]

![[assets/2606.20660_first_page.png|800]]

- **arXiv**: [2606.20660](https://arxiv.org/abs/2606.20660)
- **PDF**: https://arxiv.org/pdf/2606.20660
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Control_as_Enabling_Layer_for_Embodied_Intelligence_Research_explored_with_Soft_Robotic_Swimming_in_diverse_Flow_Speeds|Learning Control as Enabling Layer for Embodied Intelligence Research explored with Soft Robotic Swimming in diverse Flow Speeds]]
- **作者**: Fabian Schwab, Federico Allione, Bingcheng Wang, Mohamed El Arayshi, Claudio Mucignat, Ivan Lunati, Cristiano Verrelli, Ardian Jusufi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Learning Control as Enabling Layer for Embodied Intelligence Research explored with Soft Robotic Swimming in diverse Flow Speeds》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft robots are valuable robophysical platforms for studying body-caudal undulatory locomotion, but their compliant bodies are difficult to control precisely under changing hydrodynamic loading. Conventional proportional-integral-derivative (PID) feedback stabilizes periodic undulation in static water, but can accumulate flow-dependent tracking delay and increasing inter-trial variability when environmental flow becomes non-trivial. Here, we evaluate whether augmenting PID control with a Linear Repetitive Learning Estimation Scheme (PID-LRLES) recovers tracking accuracy and repeatability under dynamic flow. The LRLES generalizes classical integral action from constant to periodic, non-constant references, while using a stable transfer-function realization whose poles have negative real parts to avoid the long-term instability issues of classical repetitive control. Closed-loop experiments were carried out in a recirculating flow tank at five bulk flow speeds spanning 0 to 32.6 cm s^-1, using an embedded soft capacitive bending sensor at a 1 kHz control-loop rate. With controller gains tuned once in static water and then held fixed across all conditions, PID-LRLES tracked the periodic bending-envelope reference more closely than the PID baseline and significantly reduced the inter-trial spread of the per-trial RMSE (paired Wilcoxon signed-rank test, p = 1.8 x 10^-4, n = 25). Embedded soft proprioception and cycle-to-cycle learning act as complementary contributors to robustness: the sensor exposes the periodic hydrodynamic bias in body deformation, while the learning term absorbs it over recent oscillation cycles. By reducing flow-dependent control-induced variability, the approach provides an enabling layer for future robophysical studies seeking to isolate the effects of morphology, sensing, and environmental flow on aquatic locomotion.

</details>

---

### [[20_Research/Papers/具身智能/TACT-ful_Multi-Channel_Terrain_Affordance_and_Compliance_Training_for_Payload-Robust_Perceptive_Humanoid_Locomotion|TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion]]

![[assets/2606.20645_figure.png|800]]

- **arXiv**: [2606.20645](https://arxiv.org/abs/2606.20645)
- **PDF**: https://arxiv.org/pdf/2606.20645
- **详细分析**: [[20_Research/Papers/具身智能/TACT-ful_Multi-Channel_Terrain_Affordance_and_Compliance_Training_for_Payload-Robust_Perceptive_Humanoid_Locomotion|TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion]]
- **作者**: Thanh Ly, Truong-Duy Dang, Chien Le, Tan-Dzung Do, Phuong Tuan Dat, Cuc T. Trinh, Vien Anh Ngo, An T. Le
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.4，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《TACT-ful: Multi-Channel Terrain Affordance and Compliance Training for Payload-Robust Perceptive Humanoid Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foothold selection on structured terrain requires explicit reasoning about contact planarity, surface steepness, and kinematic reachability, properties not captured by a single height-based terrain signal. We propose a multi-channel terrain cost combining flatness, steepness, and velocity-aware height feasibility, plus a forward climb reward, that simultaneously drives a GPU-parallel divergent component of motion (DCM) foothold planner and shapes a dense per-step affordance reward for an asymmetric actor-critic policy trained with proximal policy optimization (PPO) from depth images. A Bézier swing trajectory with adaptive apex bias extends foothold tracking to joint position-and-orientation, using the arc tangent to guide sole orientation through riser crossings and tread landings. To support payload tasks, we introduce a lower-body compliance training procedure in which a virtual wrench is injected at a sampled load attachment point, generating physically consistent force and moment; wrench-aware compliance targets replace rigid pose penalties, and the policy learns to yield to load-induced perturbations without force sensing. The full system trains end-to-end with standard PPO, no distillation, and no teacher-student staging, and is deployed on a humanoid directly from simulation with configuration changes only. In simulation, the policy reaches $1.0~\mathrm{m/s}$ on stairs with risers up to $0.20~\mathrm{m}$ and improves payload robustness up to ${\sim}15~\mathrm{kg}$ centered load and for moment-dominated wrist loads without fine-tuning. We also provide a qualitative hardware demonstration on structured terrain. Project website: https://fai-rl-tech.github.io/tact-locomotion.github.io/

</details>

---
