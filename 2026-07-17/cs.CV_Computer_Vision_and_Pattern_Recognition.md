# cs.CV | Computer Vision and Pattern Recognition | 2026-07-17

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/具身智能/DriftWorld_Fast_World_Modeling_through_Drifting|DriftWorld: Fast World Modeling through Drifting]]

![[assets/2607.15065_figure.png|800]]

- **arXiv**: [2607.15065](https://arxiv.org/abs/2607.15065)
- **PDF**: https://arxiv.org/pdf/2607.15065
- **详细分析**: [[20_Research/Papers/具身智能/DriftWorld_Fast_World_Modeling_through_Drifting|DriftWorld: Fast World Modeling through Drifting]]
- **作者**: Susie Lu, Haonan Chen, Weirui Ye, Yilun Du
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 强化学习
- **相关性评分**: 2.02（加权：具身智能 0.6，强化学习 0.16，世界模型 0.56，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《DriftWorld: Fast World Modeling through Drifting》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, DriftWorld, IRASim, U-Net, UniSim, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predictive world models enable robots to plan by imagining the outcomes of their actions, but their value for control hinges on generating many rollouts quickly. This creates a bottleneck for diffusion-based world models: multistep sampling makes each rollout expensive, limiting large-scale action search at inference time. We introduce DriftWorld, an action-conditioned world model based on drifting generative models. Rather than denoising iteratively at inference, DriftWorld learns an action-conditioned drift during training, allowing it to generate future frames from the current observation and a candidate action sequence in a single forward pass at 30+ fps, which is 17x faster on average than diffusion based baselines. We evaluate DriftWorld on standard vision-based robotic manipulation benchmarks, including Bridge-V2, RT-1, Language Table, Push-T, and Robomimic. By producing rollouts that are both accurate and fast, DriftWorld achieves state-of-the-art decision-making performance with far less inference time than diffusion-based world model baselines. Beyond online control, DriftWorld can also serve as an offline simulator for ranking real-world robot policies, with rollout-based scores correlating with ground truth at up to 0.99. These results show that drifting models are a strong fit for robot world modeling, where fast, high-quality imagination directly supports planning and policy evaluation.

</details>

---

### [[20_Research/Papers/机器人/SUFLECA_Scaling_Up_Feature_Learning_for_CAD-to-image_Alignment|SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment]]

![[assets/2607.15058_figure.png|800]]

- **arXiv**: [2607.15058](https://arxiv.org/abs/2607.15058)
- **PDF**: https://arxiv.org/pdf/2607.15058
- **详细分析**: [[20_Research/Papers/机器人/SUFLECA_Scaling_Up_Feature_Learning_for_CAD-to-image_Alignment|SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment]]
- **作者**: Saad Ejaz, Miguel Fernandez-Cortizas, Javier Civera, Holger Voos, Jose Luis Sanchez-Lopez
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet, ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

CAD-to-image alignment aims to estimate an object's 9D pose (rotation, translation, and anisotropic scale) from a single RGB image, enabling applications in robotics and augmented reality. Recent zero-shot methods use visual foundation models to match image regions to CAD models, yet typically their correspondences are appearance-driven and degrade under occlusion or sim-to-real domain shift. To address these limitations, we introduce SUFLECA (Scaling Up Feature LEarning for CAD Alignment), a weakly-supervised framework for zero-shot CAD alignment with two key contributions. First, SUFLECA scales up geometry-grounded feature learning from pretrained visual representations through Normalized Object Coordinates (NOCs) supervision on 674K images spanning 12 real and synthetic datasets, learning compact geometry-aware features that generalize across domains. Second, we propose a geometrically consistent matching algorithm that establishes reliable one-to-one CAD-to-image correspondences. Together, these contributions enable accurate, sub-second alignment per object instance without iterative pose refinement. On ScanNet25k, SUFLECA achieves 33.4%/42.3% category/instance accuracy, outperforming, with a smaller computational footprint, the strongest zero-shot baseline by 10.3/12.2 percentage points and, for the first time on this benchmark, even surpassing fully supervised methods. Code is available at: https://github.com/snt-arg/SUFLECA

</details>

---

### [[20_Research/Papers/大模型/An_LLM-Based_Automatic_Sportscast_Solution_for_Robot_Soccer_Matches|An LLM-Based Automatic Sportscast Solution for Robot Soccer Matches]]

![[assets/2607.14809_figure.png|800]]

- **arXiv**: [2607.14809](https://arxiv.org/abs/2607.14809)
- **PDF**: https://arxiv.org/pdf/2607.14809
- **详细分析**: [[20_Research/Papers/大模型/An_LLM-Based_Automatic_Sportscast_Solution_for_Robot_Soccer_Matches|An LLM-Based Automatic Sportscast Solution for Robot Soccer Matches]]
- **作者**: Francesco Petri, Michele Brienza, Daniele Nardi, Domenico Daniele Bloisi, Aldo Gangemi, Vincenzo Suriani
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.3，机器人 0.8）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《An LLM-Based Automatic Sportscast Solution for Robot Soccer Matches》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

RoboCup has always been a scenario to develop systems that solve real-world problems. Driven by the main goal of playing against the 2050 FIFA World Cup champions, the RoboCup Soccer leagues need to constantly measure how the research community is progressing. Computing visual statistics from match videos is a crucial way to track this evolution. To address this challenge, this paper introduces a fully autonomous, real-time sports commentator for RoboCup matches. By bridging the gap between raw kinematic tracking and natural language generation, our neuro-symbolic architecture extracts precise statistics from video streams and turns them into fluent, hallucination-free narration. The proposed system is capable of generating statistics and commentary both during live match streaming and in post-game analysis, easily adapting to the new dynamism of the league where different humanoid robots of different sizes share the field. Supplemental materials are available at https://lab-rococo-sapienza.github.io/MARIO/

</details>

---

### [[20_Research/Papers/大模型/VQ-Touch_A_Data-Efficient_Tactile_Generation_Framework_Across_Sensors_and_Scenarios|VQ-Touch: A Data-Efficient Tactile Generation Framework Across Sensors and Scenarios]]

![[assets/2607.14728_first_page.png|800]]

- **arXiv**: [2607.14728](https://arxiv.org/abs/2607.14728)
- **PDF**: https://arxiv.org/pdf/2607.14728
- **详细分析**: [[20_Research/Papers/大模型/VQ-Touch_A_Data-Efficient_Tactile_Generation_Framework_Across_Sensors_and_Scenarios|VQ-Touch: A Data-Efficient Tactile Generation Framework Across Sensors and Scenarios]]
- **作者**: Kailin Lyu, Long Xiao, Jianing Zeng, Di Wu, Lin Shu, Jie Hao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VQ-Touch: A Data-Efficient Tactile Generation Framework Across Sensors and Scenarios》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile image generation significantly reduces the dependency on expensive and wear-prone sensors by synthesizing high-fidelity tactile data, offering an efficient solution for tactile information acquisition in robotic perception and human-machine interaction systems. However, existing methods depend on large-scale, diverse datasets from specific sensors and lack efficient data utilization and robust generalization capabilities, struggling in vision-limited environments. To address this, we introduce VQ-Touch, a tactile generation framework that supports both cross-sensor and multi-scenario applications. Specifically, to efficiently extract complex deformation and texture features from the data, we propose DM-VQGAN, an effective tactile representation learner. Furthermore, we introduce a discrete diffusion decoder with a unified conditioning interface, supporting multimodal generation tasks such as images and labels, and enhances the model's generalization capability through few-shot mixed training, thus achieving compatibility with current mainstream sensors and their variants. Experiments show that VQ-Touch surpasses state-of-the-art methods in multiple tasks.

</details>

---

### [[20_Research/Papers/机器人/AE-UAV_An_Air-to-Air_Event-Based_UAV_Tracking_Benchmark_and_a_Real-Time_Frequency-Domain_Tracker|AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker]]

![[assets/2607.14726_figure.png|800]]

- **arXiv**: [2607.14726](https://arxiv.org/abs/2607.14726)
- **PDF**: https://arxiv.org/pdf/2607.14726
- **详细分析**: [[20_Research/Papers/机器人/AE-UAV_An_Air-to-Air_Event-Based_UAV_Tracking_Benchmark_and_a_Real-Time_Frequency-Domain_Tracker|AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker]]
- **作者**: Zixin Jiang, Bing He, Chaoran Xiong, Zhenzhen Wang, Xin Zhao, Ling Pei
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《AE-UAV: An Air-to-Air Event-Based UAV Tracking Benchmark and a Real-Time Frequency-Domain Tracker》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Air-to-air (A2A) unmanned aerial vehicle (UAV) tracking is fundamental to airborne remote sensing of low-altitude aerial targets. However, the deployment of continuous, real-time tracking systems on UAVs presents significant challenges. In A2A scenarios, traditional frame-based cameras suffer from severe performance degradation under low illumination, overexposure, and high-speed motion owing to their limited dynamic range and fixed temporal sampling. Although event cameras offer a promising alternative with microsecond temporal resolution and a high dynamic range, current research is bottlenecked by two primary issues: 1) the absence of dedicated A2A event-based datasets, and 2) the heavy reliance of existing trackers on GPU acceleration and extensive training data, rendering them impractical for resource-constrained UAVs. To bridge these gaps, we introduce AE-UAV, an air-to-air event-based UAV tracking benchmark. To the best of our knowledge, this is the first airborne-captured event camera dataset for A2A tracking, comprising 178 flight sequences with continuous-time cubic B-spline annotations. Furthermore, we propose the Fast-Slow Frequency-domain Tracking (FSFT) method. This lightweight, training-free framework seamlessly integrates frequency-domain template matching with search region prediction and detection-based drift correction. Extensive experiments demonstrate that FSFT operates at an ultra-fast 420 frames per second (FPS) on CPU-only hardware. It retains 93.97% of the accuracy of state-of-the-art GPU-dependent methods while delivering a 5.32-fold effective speedup and exhibiting superior temporal resolution generalization, thereby providing a highly efficient and robust solution for airborne remote sensing of aerial targets. The dataset and source code are available at https://github.com/MSP-xEN/AE-UAV.

</details>

---

### [[20_Research/Papers/具身智能/HyMobileAgent_Data-Environment_Co-Scaling_for_Efficient_GUI_Agents|HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents]]

![[assets/2607.14548_figure.png|800]]

- **arXiv**: [2607.14548](https://arxiv.org/abs/2607.14548)
- **PDF**: https://arxiv.org/pdf/2607.14548
- **详细分析**: [[20_Research/Papers/具身智能/HyMobileAgent_Data-Environment_Co-Scaling_for_Efficient_GUI_Agents|HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents]]
- **作者**: Hy Vision Team, Huawen Shen, Zhengyang Tang, Shangpin Peng, Liang Wu, Anran Zhang, Weinong Wang, Yiduo Guo, Chenxin Li, Zhengyao Fang, Yang Ding, Junyi Li...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 强化学习
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents》归入 大模型、具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, HyMobileQA, HyMobileWorld, MMBench, Offline-RL, Online-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large multimodal models move from understanding content to operating on digital environments, mobile GUI has emerged as a challenging and consequential testbed for digital embodied intelligence. Mobile agents operate under three coupled constraints: precise perception of complex interfaces, scalable acquisition of high-quality interaction data, and robust long-horizon decision making under compounding execution errors. This report presents HyMobileAgent, a mobile GUI agent built on Hy3.0-VL-A3B, a vision-native foundation model featuring native any-resolution input, an A3B-scale deployment budget, and a 32K context window to model extended interaction histories. Rather than relying solely on model scaling, we develop a joint data and environment centric scaling framework to address the key bottlenecks of mobile interaction. Our framework integrates a GUI perception flywheel combining mock-interface synthesis, rejection sampling, and icon-specific augmentation; a knowledge pipeline that transforms tutorial videos into structured interaction data; a million-scale action data pipeline deployed across more than 2000 sandbox and real-device instances with automated failure attribution; the PhoneWorld Mock App Factory, providing a resettable training environment with 34 mock applications and over 34000 tasks; and a structured Planning-and-Reflection mechanism with explicit dead-loop detection for reliable long-horizon execution. We also introduce a progressive training recipe consisting of mid-training, supervised fine-tuning, and reinforcement learning with task-specific reward designs.

</details>

---

### [[20_Research/Papers/强化学习/3D_Geometric_Tooth_Alignment_Planning_via_Deep_Reinforcement_Learning|3D Geometric Tooth Alignment Planning via Deep Reinforcement Learning]]

![[assets/2607.14544_figure.png|800]]

- **arXiv**: [2607.14544](https://arxiv.org/abs/2607.14544)
- **PDF**: https://arxiv.org/pdf/2607.14544
- **详细分析**: [[20_Research/Papers/强化学习/3D_Geometric_Tooth_Alignment_Planning_via_Deep_Reinforcement_Learning|3D Geometric Tooth Alignment Planning via Deep Reinforcement Learning]]
- **作者**: Yong Li, Jianwen Lou, Jiayue Ma, Yao-Xiang Ding, Youyi Zheng, Haihua Zhu
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.1（加权：大模型 0.1，强化学习 2）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《3D Geometric Tooth Alignment Planning via Deep Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D geometric tooth alignment planning, which determines sequential trajectories from initial malocclusion to the final target alignment, is a cornerstone of modern digital orthodontics. This paper presents a novel deep reinforcement learning (DRL) framework to automate the generation of these alignment paths. We formulate the planning process as a Markov Decision Process (MDP) to capture its sequential decision-making nature, focusing on optimizing geometric trajectories while integrating essential spatial constraints, such as inter-dental collision avoidance and path efficiency. The proposed method leverages the Deep Deterministic Policy Gradient (DDPG) algorithm, enhanced by three key innovations: (1) a Transformer-based agent to model complex spatial interactions between teeth and manage high-dimensional state-action spaces; (2) a dynamic masking scheme that restricts movement to a sparse subset of teeth per step, better reflecting the clinical logic of sequential alignment; and (3) a two-stage curriculum learning strategy that gradually increases task difficulty to ensure training stability and efficient path discovery. We evaluate our approach on a dataset of 10K expert-designed treatment plans based on clinical data. Experimental results demonstrate that our method outperforms existing baselines in terms of path safety and geometric efficiency, providing a robust and automated solution for 3D geometric orthodontic alignment planning.

</details>

---

### [[20_Research/Papers/具身智能/Open-AoE_An_Open_Egocentric_Manipulation_Dataset_and_Toolchain_for_Embodied_Learning|Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning]]

![[assets/2607.14183_figure.png|800]]

- **arXiv**: [2607.14183](https://arxiv.org/abs/2607.14183)
- **PDF**: https://arxiv.org/pdf/2607.14183
- **详细分析**: [[20_Research/Papers/具身智能/Open-AoE_An_Open_Egocentric_Manipulation_Dataset_and_Toolchain_for_Embodied_Learning|Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning]]
- **作者**: Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.5（加权：具身智能 1.8，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, EgoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in natural environments by 500+ contributors using 400+ smartphones. The dataset provides text annotations, MANO-based hand poses, camera trajectories, and temporally localized atomic actions. Open-AoE further includes a data processing pipeline that transforms raw recordings into structured samples through temporal action segmentation, semantic annotation, hand reconstruction, and camera trajectory reconstruction. Meanwhile, we provide a separate downstream toolchain supports visualization, cross-embodiment retargeting, model-specific data conversion, and training recipes for VLA policies, WAMs, and World Models. By integrating scalable capture, structured processing, and downstream adaptation, Open-AoE reduces the barriers to both data contribution and reuse, providing practical open infrastructure for embodied model training, human-to-robot transfer, and world modeling.

</details>

---
