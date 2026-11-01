# cs.CV | Computer Vision and Pattern Recognition | 2026-10-30

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/世界模型/Continuous-Action_World_Models_Learning_Cross-Embodiment_Spatiotemporal_Dynamics_Priors|Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors]]

![[assets/2610.40401_figure.png|800]]

- **arXiv**: [2610.40401](https://arxiv.org/abs/2610.40401)
- **PDF**: https://arxiv.org/pdf/2610.40401
- **详细分析**: [[20_Research/Papers/世界模型/Continuous-Action_World_Models_Learning_Cross-Embodiment_Spatiotemporal_Dynamics_Priors|Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors]]
- **作者**: Liangyu Li, Qingwen Liu
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Continuous-Action World Models (CoAWM), a framework for learning cross-embodiment spatiotemporal dynamics priors that support robot action generation across embodiments and execution frequencies. At its core is a shared latent function space that captures the spatial and temporal structure of robot actions. We learn this space through two stages. First, function pretraining brings trajectories from different embodiments and sampling frequencies into a common representation, learning shared dynamics priors through action reconstruction and consistency across temporal sampling views. By accommodating heterogeneous robot trajectories, this stage broadens the range of data sources available for pretraining and facilitates scaling to larger and more diverse datasets. Second, we connect the pretrained function space to a world-model backbone, enabling observations, language instructions, and the current robot state to condition the prediction of a latent action function. A single decoder takes any query time and returns the corresponding end-effector action. By separating shared dynamics priors from task-conditioned action selection and temporal sampling, our approach provides a unified foundation for transferring robot experience across embodiments and control frequencies.

</details>

---

### [[20_Research/Papers/具身智能/HiFOR_Hierarchical_Foresight_with_Action-Guided_World_Grounding_for_Vision-Language-Action_Model|HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model]]

![[assets/2610.40373_figure.png|800]]

- **arXiv**: [2610.40373](https://arxiv.org/abs/2610.40373)
- **PDF**: https://arxiv.org/pdf/2610.40373
- **详细分析**: [[20_Research/Papers/具身智能/HiFOR_Hierarchical_Foresight_with_Action-Guided_World_Grounding_for_Vision-Language-Action_Model|HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model]]
- **作者**: Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately, while directly incorporating predicted futures into action policies without sufficiently considering their relevance to current action requirements. To address these limitations, we propose HiFOR, a hierarchical foresight framework with action-guided world retrieval. Specifically, Hierarchical Foresight Prediction jointly predicts short-term state evolution, semantic milestones, and final goal states through a Hierarchical Dependency Mask (HDM), establishing dependencies across temporal horizons. Building upon these predictions, Structure-Aware Latent World Modeling organizes future latent representations along the horizon, view, and spatial dimensions to facilitate fine-grained retrieval. Furthermore, Action-Guided Factorized World Retrieval adaptively retrieves relevant future information from the structured latent world based on evolving action representations during denoising, providing targeted guidance for action generation. Extensive experiments on two simulation benchmarks and six real-world robotic manipulation tasks demonstrate the effectiveness of our approach.

</details>

---

### [[20_Research/Papers/具身智能/Decision-Level_Error_Attribution_and_Depth-Aware_Safety_Evaluation_of_Monocular_RGB_Human_Tracking_for_Autonomous_Robot_Navigation|Decision-Level Error Attribution and Depth-Aware Safety Evaluation of Monocular RGB Human Tracking for Autonomous Robot Navigation]]

![[assets/2610.40199_first_page.png|800]]

- **arXiv**: [2610.40199](https://arxiv.org/abs/2610.40199)
- **PDF**: https://arxiv.org/pdf/2610.40199
- **详细分析**: [[20_Research/Papers/具身智能/Decision-Level_Error_Attribution_and_Depth-Aware_Safety_Evaluation_of_Monocular_RGB_Human_Tracking_for_Autonomous_Robot_Navigation|Decision-Level Error Attribution and Depth-Aware Safety Evaluation of Monocular RGB Human Tracking for Autonomous Robot Navigation]]
- **作者**: Abdulahi Taiwo, Chijioke Cyriacus Ekechi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Decision-Level Error Attribution and Depth-Aware Safety Evaluation of Monocular RGB Human Tracking for Autonomous Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular RGB tracking is useful for robots operating near people, but perception errors affect binary stop/proceed decisions in ways that geometric accuracy metrics do not capture. We examine how much decision error arises from the safety rule versus perception. We prove that lateral-only distance is a lower bound on planar distance: with accurate positions, it cannot miss dangers identified by the planar rule, but it produces unnecessary stops. We introduce a two-factor Shapley attribution separating rule and perception contributions, and further distinguish missed detections from localization errors. Experiments use ETH and UCY pedestrian videos with simulated stationary robots, disjoint calibration and evaluation pedestrians, and time-block bootstrap intervals. Across 898 pedestrians in three scenes, the lateral rule missed no dangers on annotated positions but achieved only 5.6-31.9% stop precision. In two scenes with RGB perception, calibrated ground-plane localization achieved 0.59 m and 0.51 m planar RMSE, compared with 1.72 m and 1.39 m for a geometric baseline and 0.81 m and 0.68 m for calibrated Depth Anything V2. Detection recall of 0.43 and 0.26 made missed detections the leading source of missed danger. A two-standard-deviation safety margin with ground-plane localization matched or improved on the lateral rule's missed-danger rate in all eight scene-threshold settings and reduced unnecessary stops in seven. All robot interactions are simulated, and outcomes are offline decision classifications, not demonstrations of collision avoidance.

</details>

---

### [[20_Research/Papers/具身智能/How_Much_Should_a_VLA_Trust_Its_Reasoning_Step-Level_Guidance_as_a_Measured_Action-Value_Function|How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function]]

![[assets/2610.40002_figure.png|800]]

- **arXiv**: [2610.40002](https://arxiv.org/abs/2610.40002)
- **PDF**: https://arxiv.org/pdf/2610.40002
- **详细分析**: [[20_Research/Papers/具身智能/How_Much_Should_a_VLA_Trust_Its_Reasoning_Step-Level_Guidance_as_a_Measured_Action-Value_Function|How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function]]
- **作者**: Dabin Seo, Eunhyek Joa
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning vision-language-action (VLA) policies write a reasoning trace and then decode the action from it. A wrong trace yields a wrong action, and even a correct-looking trace can mislead the plan. Existing remedies ask whether the reasoning is right. We ask how strongly it should steer. CoC-CFG applies classifier-free guidance between the policy's context and the same context without the reasoning span. One weight per Euler step attenuates or amplifies the reasoning, and w=1 recovers the original policy. We treat the choice of this weight as a Markov decision process whose action values are measured, not bootstrapped. With the expert frozen and the noise fixed, applying a weight for one step and finishing the plan under the current controller returns that weight's value exactly. Q-adaptive guidance fits these values with small critics and improves the controller conservatively. In the Alpasim driving simulator it outperforms every fixed weight and online RL (SAC, GRPO) in open loop, and in closed loop it passes 262 of 300 scenes, against 252 for the original policy. On held-out frames of the Waymo end-to-end driving benchmark, its first three stages outperform every fixed weight, four adaptive-guidance methods, SAC and GRPO. On the hidden test set, a frozen Alpamayo 1.5 with rule-based camera and vehicle conversions and Q-adaptive guidance sets a new state of the art among published methods: 8.135159 rater feedback score, against 8.079 for the best published method.

</details>

---

### [[20_Research/Papers/大模型/MLLM-GS_Multimodal_Large_Language_Model_Prior-Guided_Fast_Novel_View_Synthesis_in_Extreme_Environments|MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments]]

![[assets/2610.39936_figure.png|800]]

- **arXiv**: [2610.39936](https://arxiv.org/abs/2610.39936)
- **PDF**: https://arxiv.org/pdf/2610.39936
- **详细分析**: [[20_Research/Papers/大模型/MLLM-GS_Multimodal_Large_Language_Model_Prior-Guided_Fast_Novel_View_Synthesis_in_Extreme_Environments|MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments]]
- **作者**: Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.6（加权：大模型 1.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their outputs often suffer from pixel misalignment and color deviations, which can propagate into the reconstructed 3D scene and compromise reconstruction quality. Furthermore, the high computational and memory costs of 3D reconstruction hinder the practical application of NVS in extreme environments. To this end, we propose MLLM-GS, a multimodal large language model (MLLM) prior-guided framework for fast NVS in extreme environments. MLLM-GS consists of two branches: MLLM prior-guided view enhancement and fast 3D scene reconstruction. The former leverages the rich visual priors of a frozen MLLM to enhance views under different severe degradations and introduces a lightweight correction network to reduce pixel shifts and color distortions in MLLM outputs. With supervision from only a few paired clean views, this branch produces reliable enhanced views for all degraded observations, providing pseudo-GT views for subsequent 3D reconstruction. The latter improves 3DGS efficiency by optimizing rasterization, Gaussian memory layout, and parameter updates, reducing redundant computation, memory-access overhead, and optimization costs. Extensive experiments on multiple degraded scenes demonstrate that MLLM-GS effectively handles various severe degradations and achieves high-quality NVS with significantly lower reconstruction time and memory consumption. Project Page: https://wzlwlm13.github.io/MLLM-GS

</details>

---

### [[20_Research/Papers/机器人/Decoding_Geometry,_Not_Tokens_Efficient_VLMs_for_Robot_Affordance_and_Trajectory_Prediction|Decoding Geometry, Not Tokens: Efficient VLMs for Robot Affordance and Trajectory Prediction]]

![[assets/2610.39416_figure.png|800]]

- **arXiv**: [2610.39416](https://arxiv.org/abs/2610.39416)
- **PDF**: https://arxiv.org/pdf/2610.39416
- **详细分析**: [[20_Research/Papers/机器人/Decoding_Geometry,_Not_Tokens_Efficient_VLMs_for_Robot_Affordance_and_Trajectory_Prediction|Decoding Geometry, Not Tokens: Efficient VLMs for Robot Affordance and Trajectory Prediction]]
- **作者**: Akila Ayanthi, Darshana Priyasad, Tharindu Fernando, Dimity Miller, Sridha Sridharan, Clinton Fookes, Peyman Moghadam
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Decoding Geometry, Not Tokens: Efficient VLMs for Robot Affordance and Trajectory Prediction》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EdgeVLA, ShareRobot-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting where to grasp and how to move is fundamentally a geometry problem. Vision-language models treat it as language generation instead. They tokenize spatial coordinates into text and decode them autoregressively. This mechanism ignores spatial structure and truncates continuous precision. Errors compound across coordinate tokens during decoding. In this paper, we show that compact off-the-shelf VLMs with 0.5-2B parameters already encode rich spatial information in their intermediate hidden states. Autoregressive decoding is the dominant bottleneck for trajectory prediction, while affordance prediction depends additionally on feature depth and decoder architecture. We expose the latent spatial information with a lightweight, geometry-compatible prediction head that attaches to a frozen backbone. It reads features from an intermediate hidden layer, conditions a learned query on the task instruction and refines it via cross-attention over the visual tokens to regress affordance boxes and trajectory waypoints directly as continuous values, without modifying the backbone. We evaluate on ShareRobot-Bench and AGD20K. Our 2B variant reduces trajectory error by over 60% and improves ShareRobot-Bench affordance mAP by 85% relative to the autoregressive baseline. It approaches RoboBrain on trajectory prediction (0.251 vs 0.191 DFD) at 3.8x higher throughput. These results demonstrate a favorable accuracy-efficiency trade-off for instruction-conditioned 2D geometric prediction.

</details>

---

### [[20_Research/Papers/大模型/MRC-MMAgent_Reinforcement_Learning_for_Multi-Role_Collaboration_in_Multimodal_Tool-Using_Agents|MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents]]

![[assets/2610.39324_figure.png|800]]

- **arXiv**: [2610.39324](https://arxiv.org/abs/2610.39324)
- **PDF**: https://arxiv.org/pdf/2610.39324
- **详细分析**: [[20_Research/Papers/大模型/MRC-MMAgent_Reinforcement_Learning_for_Multi-Role_Collaboration_in_Multimodal_Tool-Using_Agents|MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents]]
- **作者**: Shengqin Wang, Jie Jin, Xiaofan Li, Wentao Yan, Yu Cheng, Qingsong HuYihang Chen, Weilin Luo, Jingyu Gong, Xin Tan, Yuan Xie, Zhizhong Zhang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.9，强化学习 1）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FVQA, LiveVQA, SimpleVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal tool-using agents augment vision-language models with access to external information and capabilities, enabling them to solve knowledge-intensive and visually complex tasks that cannot be addressed using visual context alone. However, existing reinforcement learning pipelines largely train single-role agents to search and answer using terminal rewards, overlooking how humans inspect retrieved evidence, reformulate queries, and revise conclusions during search. Consequently, they fail to optimize this self-corrective process over complete interaction trajectories. We propose MRC-MMAgent, a multi-role collaborative reinforcement learning framework that incorporates trajectory assessment and continuation directly into the executable agent loop. First, the framework establishes a multi-role collaborative loop that integrates solving, inspection, and continuation, enabling the agent to acquire evidence through tools, evaluate the preceding trajectory, and resume problem solving when the current answer is insufficiently supported. Second, we introduce a role-coupled learning objective that combines task success, interaction validity, and successful correction with full-trajectory policy optimization across the decisions generated by all roles. Extensive experiments show that, using only the original baseline training set without constructing additional datasets, our method consistently outperforms the corresponding base models and achieves leading or highly competitive performance across benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Seeing_and_Imagining_as_One_Unified_Video_Generation_and_4D_Perception_for_Embodied_World_Modeling|Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling]]

![[assets/2610.39232_figure.png|800]]

- **arXiv**: [2610.39232](https://arxiv.org/abs/2610.39232)
- **PDF**: https://arxiv.org/pdf/2610.39232
- **详细分析**: [[20_Research/Papers/具身智能/Seeing_and_Imagining_as_One_Unified_Video_Generation_and_4D_Perception_for_Embodied_World_Modeling|Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling]]
- **作者**: Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.4（加权：具身智能 1.5，世界模型 0.4，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RynnWorld, Track4World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world. We present GenSight, a unified embodied world model that brings future video generation and dense perception into a single pretrained video diffusion transformer. GenSight uses a unified spatiotemporal representation for video, depth, embodiment segmentation, and first-frame-relative 2D flow. Built on a shared DiT backbone, GenSight uses lightweight task modulation to predict all modalities within the same architecture. All tasks are jointly optimized within a unified velocity prediction space. At inference, GenSight supports two complementary modes: multi-step future video generation with aligned dense predictions and single-step dense perception from an observed video. By unifying modality representation, model architecture, and prediction space, GenSight avoids separate modality-specific pipelines and couples appearance, geometry, semantics, and motion in a shared representation. It promotes cross-modal consistency and allows dense perception to benefit from the spatiotemporal priors learned through video generation. Trained on embodied manipulation data spanning multiple robot embodiments and human-hand interactions, GenSight demonstrates strong performance in both video generation and dense 4D perception, highlighting the effectiveness of unifying seeing and imagining for embodied world modeling.

</details>

---

### [[20_Research/Papers/具身智能/EgoContact_Evaluating_Physical_Intelligence_with_Egocentric_Video|EgoContact: Evaluating Physical Intelligence with Egocentric Video]]

![[assets/2610.39167_figure.png|800]]

- **arXiv**: [2610.39167](https://arxiv.org/abs/2610.39167)
- **PDF**: https://arxiv.org/pdf/2610.39167
- **详细分析**: [[20_Research/Papers/具身智能/EgoContact_Evaluating_Physical_Intelligence_with_Egocentric_Video|EgoContact: Evaluating Physical Intelligence with Egocentric Video]]
- **作者**: Adam Deryło, Alexey Gavryushin, Daniel Cremers, Marc Pollefeys, Xi Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《EgoContact: Evaluating Physical Intelligence with Egocentric Video》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric video has emerged as one of the most scalable sources of data for learning generalizable manipulation priors. Yet, despite its growing use in pretraining robotic policies, it has been underutilized as a validation tool for physical intelligence, a key component of which is understanding where to make contact with an object to achieve an intended interaction. We present EgoContact, a large-scale egocentric dataset for evaluating the generalizability and precision of learned manipulation priors through future contact-point prediction. EgoContact contains 22.5K manually verified interaction events, each with a pre-contact observation, semantic intent, and pixel-precise contact locations. We find that current methods often struggle to predict precise interaction contacts and sometimes fail to localize the target object in diverse, in-the-wild scenes, even when allowed multiple predictions. Furthermore, we demonstrate the usefulness of EgoContact's annotated interactions for robotic manipulation: simply using EgoContact as the memory bank of an existing affordance-transfer policy improves grasp success from 14.2% to 31.2% in simulation and from 16% to 58% on a real robot.

</details>

---
