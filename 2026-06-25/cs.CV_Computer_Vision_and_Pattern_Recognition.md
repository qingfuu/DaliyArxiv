# cs.CV | Computer Vision and Pattern Recognition | 2026-06-25

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/具身智能/RoboAtlas_Contextual_Active_SLAM|RoboAtlas: Contextual Active SLAM]]

![[assets/2606.26046_figure.png|800]]

- **arXiv**: [2606.26046](https://arxiv.org/abs/2606.26046)
- **PDF**: https://arxiv.org/pdf/2606.26046
- **详细分析**: [[20_Research/Papers/具身智能/RoboAtlas_Contextual_Active_SLAM|RoboAtlas: Contextual Active SLAM]]
- **作者**: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《RoboAtlas: Contextual Active SLAM》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.

</details>

---

### [[20_Research/Papers/具身智能/In-Context_World_Modeling_for_Robotic_Control|In-Context World Modeling for Robotic Control]]

![[assets/2606.26025_first_page.png|800]]

- **arXiv**: [2606.26025](https://arxiv.org/abs/2606.26025)
- **PDF**: https://arxiv.org/pdf/2606.26025
- **详细分析**: [[20_Research/Papers/具身智能/In-Context_World_Modeling_for_Robotic_Control|In-Context World Modeling for Robotic Control]]
- **作者**: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《In-Context World Modeling for Robotic Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.

</details>

---

### [[20_Research/Papers/具身智能/DSP-SLAM++_A_Unified_Framework_for_Multi-Class,_High-Fidelity_Object_SLAM_in_the_Wild|DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild]]

![[assets/2606.25953_figure.png|800]]

- **arXiv**: [2606.25953](https://arxiv.org/abs/2606.25953)
- **PDF**: https://arxiv.org/pdf/2606.25953
- **详细分析**: [[20_Research/Papers/具身智能/DSP-SLAM++_A_Unified_Framework_for_Multi-Class,_High-Fidelity_Object_SLAM_in_the_Wild|DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild]]
- **作者**: Ahmad Kourani, Ghina Daoud, Daniel Asmar, Imad Elhajj
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AUBVRL, VRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing object-aware SLAM systems force a trade-off between real-time performance, multi-class support, and the generation of high-fidelity, semantically coherent object models. To address this trade-off, we present DSP-SLAM++, which extends the DSP-SLAM framework with an asynchronous mapping pipeline for real-time performance and dedicated sensor fusion adaptations for a monocular fisheye-LiDAR suite. Experiments demonstrate that our system generates fine-grained, geometrically-complete shapes for multiple object classes while eliminating severe mapping thread bottlenecks by reducing maximum object processing latency by up to 70\% compared to the state-of-the-art baseline, enabling robust, real-time performance on a challenging 25 Hz multi-class datasets. This work makes high-fidelity, multi-class object SLAM more practical for real-world applications like autonomous driving and robotic manipulation by enabling its use on platforms with common fisheye-LiDAR sensor setups. The open-source code is available at: [github.com/AUBVRL/DSP-SLAMpp].

</details>

---

### [[20_Research/Papers/具身智能/USS_Unified_Spatial-Semantic_Prompts_for_Embodied_Visual_Tracking_with_Latent_Dynamics_Learning|USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning]]

![[assets/2606.25880_figure.png|800]]

- **arXiv**: [2606.25880](https://arxiv.org/abs/2606.25880)
- **PDF**: https://arxiv.org/pdf/2606.25880
- **详细分析**: [[20_Research/Papers/具身智能/USS_Unified_Spatial-Semantic_Prompts_for_Embodied_Visual_Tracking_with_Latent_Dynamics_Learning|USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning]]
- **作者**: Yuchen Xie, Xinyu Zhou, Kuangji Zuo, Yanshuo Lu, Fengrui Huang, Boyu Ma, Jianfei Yang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.2，大模型 0.3，世界模型 1，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning》归入 具身智能、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GesVLA, Real-World, TraceVLA, VP-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only specification to unified spatial-semantic prompting. Based on this paradigm, we introduce Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning, USS, an end-to-end embodied tracking framework that supports text, point, bounding box, and mask prompts within a unified architecture. USS encodes heterogeneous prompts with modality-specific encoders, fuses prompt tokens with visual features through hybrid attention, and decodes compact prompt-conditioned representations into egocentric waypoints. To further improve temporal robustness, USS incorporates a latent world model that predicts future representations through self-supervised alignment. Real-robot experiments demonstrate that explicit spatial target cues yield higher success rates than text-only prompts, particularly in scenarios involving similar distractors and longer-horizon tracking where maintaining instance-level target identity is critical. In the simulation benchmark, USS also achieves state-of-the-art performance among non-MLLM-based methods and competitive results against recent MLLM-based approaches with faster inference speed. Our findings reveal that spatial-semantic prompting provides a more precise and flexible target indication interface for embodied visual tracking. Project site: https://arescheah.github.io/uss-project-page/.

</details>

---

### [[20_Research/Papers/机器人/1000_Rallies_An_Event-Camera_Dataset_and_Real-Time_Learned_Ball-State_Estimation_for_Robotic_Table_Tennis|1000 Rallies: An Event-Camera Dataset and Real-Time Learned Ball-State Estimation for Robotic Table Tennis]]

![[assets/2606.25620_figure.png|800]]

- **arXiv**: [2606.25620](https://arxiv.org/abs/2606.25620)
- **PDF**: https://arxiv.org/pdf/2606.25620
- **详细分析**: [[20_Research/Papers/机器人/1000_Rallies_An_Event-Camera_Dataset_and_Real-Time_Learned_Ball-State_Estimation_for_Robotic_Table_Tennis|1000 Rallies: An Event-Camera Dataset and Real-Time Learned Ball-State Estimation for Robotic Table Tennis]]
- **作者**: Raphaela Kreiser, Asude Aydin, Yin Bi, Claudio Fanconi, Peter Dürr, Naoya Takahashi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《1000 Rallies: An Event-Camera Dataset and Real-Time Learned Ball-State Estimation for Robotic Table Tennis》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic table tennis has emerged as a compelling benchmark for real-time robotic perception due to its fast ball dynamics and stringent timing requirements. Accurate, high-frequency, and low-latency ball state estimation is critical for reliable trajectory prediction and timely control. Traditional frame-based cameras face an inherent trade-off: low frame rates leave temporal blind spots that miss fast-moving objects and high frame rates raise data and computational cost. Event cameras instead offer microsecond temporal resolution and, under sufficient illumination, remain largely free of motion blur even at high ball speeds. However, the community lacks large-scale datasets to develop and benchmark event-based perception in realistic sports scenarios. We address this gap by introducing the first large-scale event-camera dataset for table tennis, comprising over 1000 rallies from a diverse group of players ranging from amateurs to elite-level athletes. Each recording captures the event stream alongside 14 synchronized high-speed frame-based cameras at 200 FPS, which we use to produce 1 kHz pseudo ground-truth labels for ball position, velocity, and spin. Building on this dataset, we train a convolutional neural network robust to background player motion that jointly estimates the ball's position and velocity in the image-plane from events. Treating the predicted velocity as an additional measurement in the Kalman filter reduces bounce-point prediction error by 36% relative to a position-only baseline. Finally, we close the perception-action loop by integrating the event-based system with a Stäubli robotic arm, enabling the first real-time human-robot table tennis rallies driven by event-based perception.

</details>

---

### [[20_Research/Papers/具身智能/AISPO_Enhancing_Depth_Reliability_for_Robotic_Manipulation_of_Non-Lambertian_Objects_via_Affine-Invariant_Shape_Prior|AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian Objects via Affine-Invariant Shape Prior]]

![[assets/2606.25503_figure.png|800]]

- **arXiv**: [2606.25503](https://arxiv.org/abs/2606.25503)
- **PDF**: https://arxiv.org/pdf/2606.25503
- **详细分析**: [[20_Research/Papers/具身智能/AISPO_Enhancing_Depth_Reliability_for_Robotic_Manipulation_of_Non-Lambertian_Objects_via_Affine-Invariant_Shape_Prior|AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian Objects via Affine-Invariant Shape Prior]]
- **作者**: Zhiming Chen, Linfang Zheng, Kun Zhang, Hyung Jin Chang, Wei Zhang, Hongyu Yu, Hua Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian Objects via Affine-Invariant Shape Prior》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DFNet, Real-World, SimNet, SwinDRNet, TransparentNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic depth failures. Unlike methods that focus primarily on average depth accuracy, our approach emphasizes physical plausibility and structural integrity of the predicted depth maps. Extensive benchmark evaluations demonstrate competitive performance and strong generalization to unseen objects and novel scenes. Real-world grasping experiments further show that enhanced depth reliability significantly improves manipulation success rates, particularly for transparent objects where many existing methods fail to produce physically usable depth estimates.

</details>

---

### [[20_Research/Papers/大模型/Causal-rCM_A_Unified_Teacher-Forcing_and_Self-Forcing_Open_Recipe_for_Autoregressive_Diffusion_Distillation_in_Streaming_Video_Generation_an|Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models]]

![[assets/2606.25473_figure.png|800]]

- **arXiv**: [2606.25473](https://arxiv.org/abs/2606.25473)
- **PDF**: https://arxiv.org/pdf/2606.25473
- **详细分析**: [[20_Research/Papers/大模型/Causal-rCM_A_Unified_Teacher-Forcing_and_Self-Forcing_Open_Recipe_for_Autoregressive_Diffusion_Distillation_in_Streaming_Video_Generation_an|Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models]]
- **作者**: Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen, Jianfei Chen, Chen-Hsuan Lin, Ming-Yu Liu, Jun Zhu, Qianli Ma
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.16，世界模型 1.16）
- **关联关键词**: LLM, RL, WorldModel

#### 研究背景与动机

《Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DDRL, HunyuanWorld, ImageNet, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models. In this work, we extend rCM, an advanced diffusion distillation framework, to autoregressive video diffusion. The core philosophy of rCM lies in the complementarity between forward and reverse divergences, represented by consistency models (CMs) and distribution matching distillation (DMD), respectively, in diffusion distillation. This philosophy naturally carries over to the autoregressive setting, where teacher-forcing (TF) provides an offline, forward-divergence causal training paradigm, while self-forcing (SF) corresponds to an on-policy, reverse-divergence refinement. Our contributions are: (1) through extensive experiments, we show that teacher-forcing CM is currently the best complement to self-forcing DMD as an initialization strategy (2) we present the first implementation of teacher-forcing-based continuous-time CMs (e.g., sCM/MeanFlow) for autoregressive video diffusion, enabled by our custom-mask FlashAttention-2 JVP kernel, achieving 10$\times$ faster convergence compared to discrete-time CMs (dCMs) (3) we introduce Causal-rCM, a leading, unified, and scalable algorithm-infrastructure open recipe for diffusion distillation and causal training (4) we achieve state-of-the-art streaming video generation performance in both frame-wise and chunk-wise settings, using only synthetic data for training. Notably, our distilled 2-step causal Wan2.1-1.3B model achieves a VBench-T2V score of 84.63 with only 1 or 2 sampling steps. We further apply Causal-rCM to Cosmos 3, an advanced omnimodal world foundation model for physical AI with action-conditioned generation capability, enabling an interactive world model.

</details>

---

### [[20_Research/Papers/机器人/An_Integrated_Hardware-Software_Design_for_Low-Data_Spatial_Defect_Detection_in_Robotic_Visual_Inspection_with_Hybrid_Optoelectronic_Neural_|An Integrated Hardware-Software Design for Low-Data Spatial Defect Detection in Robotic Visual Inspection with Hybrid Optoelectronic Neural Networks]]

![[assets/2606.25277_figure.png|800]]

- **arXiv**: [2606.25277](https://arxiv.org/abs/2606.25277)
- **PDF**: https://arxiv.org/pdf/2606.25277
- **详细分析**: [[20_Research/Papers/机器人/An_Integrated_Hardware-Software_Design_for_Low-Data_Spatial_Defect_Detection_in_Robotic_Visual_Inspection_with_Hybrid_Optoelectronic_Neural_|An Integrated Hardware-Software Design for Low-Data Spatial Defect Detection in Robotic Visual Inspection with Hybrid Optoelectronic Neural Networks]]
- **作者**: Chaoqing Tang, Jiaxuan Li, Huanze Zhuang, Guiyun Tian, Chao Wang, Yihao Ouyang, Wenzhong Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《An Integrated Hardware-Software Design for Low-Data Spatial Defect Detection in Robotic Visual Inspection with Hybrid Optoelectronic Neural Networks》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To address data overload and inefficient shape-level annotation in robotic visual inspection, this paper proposes a hardware-software integrated optoelectronic architecture. A non-imaging, low-data paradigm is established to minimize annotation dependency. First, a sensor-in-the-loop strategy reconfigures a Digital Micromirror Device (DMD) as a physical optical convolutional layer, enabling photonic-domain feature extraction that unifies sensing hardware and processing software. To suppress data volume at the source, a block-based compressed sensing strategy encodes spatial information into low-dimensional temporal signals, drastically reducing redundancy. Subsequently, to bypass laborious manual defect shape annotation, natural language descriptions guide the network to align with highly generalizable features from Contrastive Language-Image Pre-training (CLIP), steering the attention maps of the optoelectronic neural network toward defect shapes. Furthermore, a Localization Accuracy for Attention (LAA) metric is proposed to quantify shape-level defect localization performance. Experiments on transparent material defect detection validate the system's effectiveness. Parametric analysis reveals how measurement matrices, compression ratios, and block sizes affect accuracy. Results show that, compared to traditional imaging, the proposed architecture maintains equivalent accuracy while reducing data volume by 90% for Vision Transformers and computational workload by 60% for Convolutional Neural Networks. This low-data paradigm offers an efficient solution for industrial automation scenarios involving massive data streams, high acquisition costs, or constrained edge resources.

</details>

---

### [[20_Research/Papers/机器人/OrthoTrack_Continuous_6-DoF_UAV_Trajectory_Estimation_Anchored_in_Public_Orthophotos|OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos]]

![[assets/2606.25245_first_page.png|800]]

- **arXiv**: [2606.25245](https://arxiv.org/abs/2606.25245)
- **PDF**: https://arxiv.org/pdf/2606.25245
- **详细分析**: [[20_Research/Papers/机器人/OrthoTrack_Continuous_6-DoF_UAV_Trajectory_Estimation_Anchored_in_Public_Orthophotos|OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos]]
- **作者**: Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Olaf Wysocki, Marc Pollefeys, Daniel Cremers
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous 6-DoF pose estimation is essential for autonomous UAV operations. Yet, existing visual odometry and SLAM methods accumulate drift and yield only relative, up-to-scale trajectories. Single-frame geo-localization, in turn, discards temporal continuity and remains too slow for real-time use. We present OrthoTrack, a training-free system that estimates continuous 6-DoF UAV trajectories using only publicly available orthophotos and surface models as a map prior. OrthoTrack matches keyframes against the orthophoto and lifts correspondences to metric 3D via the surface model. It then propagates these map-anchored correspondences to intermediate frames with optical flow, producing absolute, metrically scaled poses at every frame without GPS or post-hoc alignment. We also introduce the MovingDrone Dataset, a large-scale benchmark pairing photorealistic UAV sequences with dense 6-DoF ground truth and co-registered multi-modal geodata including multi-temporal orthophotos. On MovingDrone and real-world benchmarks, OrthoTrack runs in real time on a single GPU. It outperforms all baselines by a large margin, even those receiving oracle scale and alignment. By relying on publicly available geodata, OrthoTrack enables deployment to new regions without site-specific adaptation.

</details>

---

### [[20_Research/Papers/具身智能/Reflective_VLA_In-Context_Action_Consequences_Make_VLAs_Generalize|Reflective VLA: In-Context Action Consequences Make VLAs Generalize]]

![[assets/2606.25215_figure.png|800]]

- **arXiv**: [2606.25215](https://arxiv.org/abs/2606.25215)
- **PDF**: https://arxiv.org/pdf/2606.25215
- **详细分析**: [[20_Research/Papers/具身智能/Reflective_VLA_In-Context_Action_Consequences_Make_VLAs_Generalize|Reflective VLA: In-Context Action Consequences Make VLAs Generalize]]
- **作者**: Qing Lian, Kent Yu, Lei Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Reflective VLA: In-Context Action Consequences Make VLAs Generalize》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgiBot-World, MemoryVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most vision-language-action (VLA) models are reactive: they predict the next action from the current instruction and observation, implicitly assuming that the current observation fully specifies the action-relevant state. In embodied control, however, embodiment-specific factors such as camera-to-robot geometry, robot calibration, or systematic actuation bias are often hard to identify from a single observation. As a result, reactive policies cannot reliably disambiguate these factors in general, overfitting to training environments and generalizing poorly at deployment. We propose Reflective VLA, which conditions each decision on a context of observation-action-consequence triplets. Each triplet records not only what the robot observed and executed, but also how the scene changed afterward, exposing the deployment-specific mapping from actions to observed effects. Architecturally, Reflective VLA routes all observation modalities through the VLM under shared attention, so the action expert reasons directly over past triplets and the current observation. A block-causal mask enables parallel multi-frame training without leakage and supports KV-cached real-time inference. On standard LIBERO and SimplerEnv-Bridge, Reflective VLA preserves strong in-distribution performance. Under distribution shift on LIBERO-Plus and the harder LIBERO-Plus-Hard, it improves average success rate by 5.4 and 4.2 percentage points over a matched reactive baseline. Ablations with a matched history-only baseline further show that action consequences -- rather than additional context length alone -- are the key to cross-environment generalization. Project page: https://lianqing11.github.io/reflective-vla-page/

</details>

---

### [[20_Research/Papers/机器人/fARfetch_Enabling_Collocated_AR-HRC_in_Large_Visually_Diverse_Environments_with_VLM-Driven_AR_Content_Adaptation|fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation]]

![[assets/2606.25162_figure.png|800]]

- **arXiv**: [2606.25162](https://arxiv.org/abs/2606.25162)
- **PDF**: https://arxiv.org/pdf/2606.25162
- **详细分析**: [[20_Research/Papers/机器人/fARfetch_Enabling_Collocated_AR-HRC_in_Large_Visually_Diverse_Environments_with_VLM-Driven_AR_Content_Adaptation|fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation]]
- **作者**: Christian Fronk, Hanting Ye, David Hunt, Miroslav Pajic, Maria Gorlatova
- **cs 子类**: cs.CV, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Augmented Reality (AR) can improve collocated human-robot collaboration by making robot state and intent visible and enabling intuitive control, yet large, visually diverse environments like the outdoors challenge both interaction and content legibility, especially at long distances and beyond visual line of sight. We present fARfetch, an AR-HRC system that integrates (i) shared semantic environment mapping across an AR headset and robot that visualizes detected landmarks in AR to support landmark-grounded go-to commands, (ii) a context-aware world-in-miniature representation of the shared environment for fine-grained path authoring, and (iii) vision-language-model driven AR view management that jointly adapts virtual content color, size, and orientation to maintain legibility in large visually diverse environments. We implement fARfetch with a Meta Quest 3 headset and Unitree Go2 quadruped robot, and conduct a within-subjects user study (N=13) on a real-world large-scale (30.5m) outdoor inspection task. fARfetch yielded significantly faster completion times than a non-AR baseline (66%) and significantly lower workload in mental demand (-43%), temporal demand (-34%), and frustration (-66%). A custom legibility survey indicated fARfetch effectively maintained virtual content legibility in the large outdoor environment.

</details>

---

### [[20_Research/Papers/具身智能/Toward_Low-Latency_Vision-Language_Models_with_Doubly-Correct_Predictions_in_Egocentric_Visual_Understanding|Toward Low-Latency Vision-Language Models with Doubly-Correct Predictions in Egocentric Visual Understanding]]

![[assets/2606.25160_figure.png|800]]

- **arXiv**: [2606.25160](https://arxiv.org/abs/2606.25160)
- **PDF**: https://arxiv.org/pdf/2606.25160
- **详细分析**: [[20_Research/Papers/具身智能/Toward_Low-Latency_Vision-Language_Models_with_Doubly-Correct_Predictions_in_Egocentric_Visual_Understanding|Toward Low-Latency Vision-Language Models with Doubly-Correct Predictions in Egocentric Visual Understanding]]
- **作者**: Qitong Wang, Fan Du, Pranav Maneriker, Jihui Jin, Christopher Rasmussen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Toward Low-Latency Vision-Language Models with Doubly-Correct Predictions in Egocentric Visual Understanding》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid rise of Vision-Language Models (VLMs) in egocentric visual understanding has made low-latency inference in human-robot collaborative (HRC) tasks increasingly critical. Weight pruning techniques developed for VLMs to shrink model size and computation can be readily applied to satisfy the efficiency demands of on-board processing and real-time interactive robotics. Moreover, safe human-robot interaction demands pruning strategies that preserve doubly-correct predictions; outputs must be both accurate and evidentially grounded to mitigate risks and ensure user trust. In this paper, we present a new study of VLM pruning through the lens of doubly-correct prediction. Our experiments surprisingly show that existing pruning methods often preserve the right evidence localization but undermine correct prediction. To address this, we propose a rationale-informed pruning strategy that better aligns evidence with decisions. Benchmark results on egocentric video datasets demonstrate that our method not only achieves the highest prediction accuracy but also outperforms existing approaches in attaining doubly-correct predictions. We aim to stimulate research on efficient and reliable VLMs, ensuring accuracy-driven advances align with the transparency, auditability, and safety required for responsible human-robot interaction and embodied intelligence.

</details>

---
