# cs.CV | Computer Vision and Pattern Recognition | 2026-10-09

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/强化学习/Dex-One2Many_Learning_Dexterous_Manipulation_from_a_Single_Human_Demonstration|Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration]]

![[assets/2610.12470_figure.png|800]]

- **arXiv**: [2610.12470](https://arxiv.org/abs/2610.12470)
- **PDF**: https://arxiv.org/pdf/2610.12470
- **详细分析**: [[20_Research/Papers/强化学习/Dex-One2Many_Learning_Dexterous_Manipulation_from_a_Single_Human_Demonstration|Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration]]
- **作者**: Jusuk Lee, Sungha Kim, Yeonsoo Park, Jonguk Cheon, Yoonkyo Jung, Yongjun You, H. Jin Kim, Jia-Bin Huang, Furong Huang, Youngseok Jang, Seungjae Lee
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Dex-One2Many: Learning Dexterous Manipulation from a Single Human Demonstration》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While learning dexterous manipulation from a single human video offers a promising alternative to costly robot demonstrations, many recent methods predominantly imitate demonstrated motions. Such strict motion matching often limits generalization to initial object poses, goal poses, and grasps not shown in the video. Alternatively, discovering a policy via reinforcement learning (RL) allows for broad generalization, but without prior guidance, it struggles with high-dimensional exploration in complex, multi-stage tasks. To address these coupled generalization and exploration challenges, we present Dex-One2Many, a real-to-sim-to-real framework that learns a generalizable dexterous manipulation policy from a single human video. Our key insight is to abstract the video into sequential scene graphs that guide RL, enabling efficient exploration while preserving broad generalizability. The graphs serve as generative constraints for sampling diverse reset states and provide dense rewards for each stage. Because the graphs constrain relations rather than exact poses, these reset states cover object poses and grasps beyond the video, while initializing each stage from them with dense rewards keeps exploration short and guided. Trained entirely in simulation, Dex-One2Many transfers zero-shot to a real multi-fingered hand. Across five tool-use and manipulation tasks, Dex-One2Many exceeds baselines by 6.5% in seen configurations, while its robust generalization widens this gap to 71% in unseen scenarios.

</details>

---

### [[20_Research/Papers/具身智能/DreamTrue_Action-Faithful_Robot_World_Model_with_Counterfactual_Post-Training|DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training]]

![[assets/2610.12468_figure.png|800]]

- **arXiv**: [2610.12468](https://arxiv.org/abs/2610.12468)
- **PDF**: https://arxiv.org/pdf/2610.12468
- **详细分析**: [[20_Research/Papers/具身智能/DreamTrue_Action-Faithful_Robot_World_Model_with_Counterfactual_Post-Training|DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training]]
- **作者**: Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习
- **相关性评分**: 2.7（加权：具身智能 0.6，强化学习 0.2，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, EWMBench, GE-Sim, PlayWorld, PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render action trajectories into image-space conditions and introduce offline geometric calibration to align these conditions with the target videos. To broaden interaction coverage, we introduce counterfactual post-training, modifying recorded action trajectories and generating future videos under a wider range of actions and contact configurations. To provide feedback on these predictions without paired ground-truth futures, we construct a human-annotated video dataset covering robot, object, and interaction defects and use it to train an embodied video reward model. Its scores guide reinforcement-learning post-training toward more physically plausible interaction outcomes. On AgiBot, DreamTrue attains state-of-the-art action following, while reducing the human-assessed interaction defect rate from from 48.12% to 6.25%. Notably, our model ranks first in the world model track of the AgiBot World Challenge 2026. The project page can be found at https://brave-eai.github.io/DreamTrue.

</details>

---

### [[20_Research/Papers/具身智能/VersaCamVLA_Camera-Configurable_VLA_Policies_for_Robotic_Manipulation|VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation]]

![[assets/2610.12451_figure.png|800]]

- **arXiv**: [2610.12451](https://arxiv.org/abs/2610.12451)
- **PDF**: https://arxiv.org/pdf/2610.12451
- **详细分析**: [[20_Research/Papers/具身智能/VersaCamVLA_Camera-Configurable_VLA_Policies_for_Robotic_Manipulation|VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation]]
- **作者**: Boyao Han, Chen Shi, Jingjing Qian, ZhuoTan Tian, Li Jiang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.3（加权：具身智能 3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VersaCamVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-Augmented Pose Sampling (WAPS), which leverages natural wrist-camera motion for free pose diversity. At deployment, a lightweight spatial encoder injects these compact scene tokens into a pretrained base VLA as a supplementary visual condition, requiring no explicit 3D sensing or novel-view rendering. Experiments on RoboTwin, LIBERO, and a real-robot platform demonstrate that VersaCamVLA consistently outperforms prior VLA methods and direct multi-view baselines, maintaining robust performance across varying camera counts and unseen camera poses.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Turing_Machines_Stateful_Code_for_Robot_Recursive_Self-Improvement|Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement]]

![[assets/2610.12369_figure.png|800]]

- **arXiv**: [2610.12369](https://arxiv.org/abs/2610.12369)
- **PDF**: https://arxiv.org/pdf/2610.12369
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Turing_Machines_Stateful_Code_for_Robot_Recursive_Self-Improvement|Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement]]
- **作者**: Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most robot policies keep a model in the control loop: a VLA maps observations to actions, and an Agent Harness, such as Agent-as-Policy or Harness VLA queries a VLM for decision making at run time. We propose a different view: the embodied world is an Embodied Turing Machine, whose tape is the robot and environment state and rules are the policy. If this state can be represented accurately, the decision making can be written entirely in code. We therefore propose Code-Only-as-Policy (COAP): code measures and tracks the robot, environment, and task state from camera images and proprioception, and makes every decision from it. The same code applies across episodes, and different tasks share one library without a VLM or VLA in the loop. Compared with VLAs and Agent Harnesses, we analyze three advantages of COAP: (i) Explicit State: the state can be stored in code; (ii) Execution: code makes decision making controllable, recovers from failures flexibly, and runs fast and cheaply online; (iii) Extensibility: new tasks reuse, inherit, or extend the shared library, so capabilities can accumulate over tasks. These advantages make COAP a suitable medium for recursive self-improvement (RSI): coding agents develop the library in a closed loop, and each change is explicit and controllable. On RoboDojo's 42 bimanual tasks, the resulting library reaches a success rate of 70.24% without a model at test time. The upper bound of COAP lies in how accurately the state is represented for decision making and how robust the code logic is. We thus propose COAP as a new paradigm for embodied tasks; since it applies across episodes, it can also serve as an efficient data engine for VLAs and Agent Harnesses.

</details>

---

### [[20_Research/Papers/具身智能/SuperNav_An_Agentic_Navigation_System_for_Any_Task_in_Any_Scene|SuperNav: An Agentic Navigation System for Any Task in Any Scene]]

![[assets/2610.12126_figure.png|800]]

- **arXiv**: [2610.12126](https://arxiv.org/abs/2610.12126)
- **PDF**: https://arxiv.org/pdf/2610.12126
- **详细分析**: [[20_Research/Papers/具身智能/SuperNav_An_Agentic_Navigation_System_for_Any_Task_in_Any_Scene|SuperNav: An Agentic Navigation System for Any Task in Any Scene]]
- **作者**: Jinkai Zhang, Jingyi Xu, Yuanhong Yu, Jiarui Guo, Ruizhen Hu, Hujun Bao, Xiaowei Zhou, Sida Peng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SuperNav: An Agentic Navigation System for Any Task in Any Scene》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Demand-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose service robots need navigation systems that can handle diverse human requests in unfamiliar environments, combining task generality with scene generality. Some existing methods fine-tune multimodal large language models (MLLMs) to predict navigation actions, making their behavior dependent on the coverage of navigation training data and potentially limiting generalization to new requests and environments. Our key insight is to let the MLLM focus on interpreting requests, understanding scenes, and making decisions while preserving its general-purpose capabilities and delegating motion execution to navigation tools. To realize this idea, we introduce SuperNav, which equips a pretrained MLLM with a specialized agent harness without navigation-specific fine-tuning of the MLLM. Our harness supports these decisions with Navigation Skills, agent-oriented Tools for physical interaction, and task-progress and context management. A unified visual-point interface connects decision-making to motion by allowing the model to specify destinations directly in images and revise its decisions from execution feedback. Together, these components support sustained navigation across different task requirements and environments. SuperNav outperforms four evaluated baselines on instance-level, multi-object, and demand-driven tasks. Category-level evaluation on HM3D and deployment on a real quadruped robot further demonstrate its applicability across environments. Project Page: https://zju3dv.github.io/SuperNav/

</details>

---

### [[20_Research/Papers/具身智能/A_Minimal_Optical-Flow_Representation_for_Vision-Based_Tactile_Rotation_Classification_in_Robotic_Manipulation_Across_Gravity_Domains|A Minimal Optical-Flow Representation for Vision-Based Tactile Rotation Classification in Robotic Manipulation Across Gravity Domains]]

![[assets/2610.12073_figure.png|800]]

- **arXiv**: [2610.12073](https://arxiv.org/abs/2610.12073)
- **PDF**: https://arxiv.org/pdf/2610.12073
- **详细分析**: [[20_Research/Papers/具身智能/A_Minimal_Optical-Flow_Representation_for_Vision-Based_Tactile_Rotation_Classification_in_Robotic_Manipulation_Across_Gravity_Domains|A Minimal Optical-Flow Representation for Vision-Based Tactile Rotation Classification in Robotic Manipulation Across Gravity Domains]]
- **作者**: Oscar Martinez-Bernal, Mario Cavero-Vidal, Francesco Grella, Carol Martinez
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Minimal Optical-Flow Representation for Vision-Based Tactile Rotation Classification in Robotic Manipulation Across Gravity Domains》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based tactile sensors provide rich contact information, but processing high-resolution images can be costly for resource-constrained platforms such as space robots. This work investigates whether a compact representation of tactile motion can classify object rotation across different gravity conditions. Dense optical flow from a simulated GelSight Mini is aggregated over a 7x9 grid into 126 features and used to classify the direction of load-induced rotation under Earth, Mars, Moon, and orbital gravity. Gravity causes a small but significant shift in these features, accounting for 1.6% of their variance (R2 = 0.016). Despite its small magnitude, this shift affects models trained only on Earth data: XGBoost accuracy decreases from 94.4% on Earth to 75.9% in orbit. In contrast, a single model trained across all four gravity domains achieves 96.3% overall accuracy and 95.1%-97.0% across individual domains, without using gravity as an input. The representation can also be reduced to 40 features while retaining 95.7% accuracy, with XGBoost requiring only 0.14 ms per inference. These findings show that Earth-gravity performance alone is insufficient to establish the transferability of tactile perception for space robotic manipulation, highlighting the need to account for gravity-induced domain shifts during training and validation.

</details>

---

### [[20_Research/Papers/具身智能/LIVIN_Benchmarking_Spatial_and_Embodied_Intelligence_in_Digital_Twins_of_Lived-In_Homes|LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes]]

![[assets/2610.12069_figure.png|800]]

- **arXiv**: [2610.12069](https://arxiv.org/abs/2610.12069)
- **PDF**: https://arxiv.org/pdf/2610.12069
- **详细分析**: [[20_Research/Papers/具身智能/LIVIN_Benchmarking_Spatial_and_Embodied_Intelligence_in_Digital_Twins_of_Lived-In_Homes|LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes]]
- **作者**: Peijun Xu, Chuansen Nie, Yiyang He, Yinuo Bai, Jingyang Liu, Kuixiang Shao, Yuyang Jiao, Kuanhao Xia, Jiayi Zhu, Zitian Yang, Yanqi Zhang, Tianye Tan...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.5，机器人 0.4）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《LIVIN: Benchmarking Spatial and Embodied Intelligence in Digital Twins of Lived-In Homes》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BiGym, HumanoidBench, LIVIN-Bench, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Realistic household simulation must capture not only diverse environments but also the lived-in object arrangements and spatial constraints that shape robot motion and interaction. Existing resources often trade off scale, real-world correspondence, and interaction readiness, leaving a gap in faithful, interactive replicas of how real homes are actually arranged. To this end, we introduce LIVIN, a benchmark for spatial and embodied intelligence built on digital twins of 30 diverse lived-in homes. These replicas preserve observed room layouts, furniture configurations, and everyday belongings. To construct them, we design a human-in-the-loop workflow comprising instance recognition, architectural reconstruction, and object generation and placement, with intermediate results reviewed and corrected by humans against the source observations at each stage. We evaluate four tasks in LIVIN: 3D detection, 3D reconstruction, navigation, and loco-manipulation. Our evaluations show that current methods remain challenged by the dense object arrangements, occlusions, limited free space, and constrained interaction regions found in realistic lived-in homes. We hope LIVIN will help advance embodied AI in real-world homes, from spatial understanding to robotic interaction, and ultimately bring embodied intelligence into everyday home environments.

</details>

---

### [[20_Research/Papers/世界模型/Right_Screen,_Wrong_Transition_World_Models_as_Verifiers_for_GUI_Agents|Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents]]

![[assets/2610.11942_figure.png|800]]

- **arXiv**: [2610.11942](https://arxiv.org/abs/2610.11942)
- **PDF**: https://arxiv.org/pdf/2610.11942
- **详细分析**: [[20_Research/Papers/世界模型/Right_Screen,_Wrong_Transition_World_Models_as_Verifiers_for_GUI_Agents|Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents]]
- **作者**: Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu, Wei Yang Bryan Lim
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，世界模型 1）
- **关联关键词**: Agent, WorldModel, Security

#### 研究背景与动机

《Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Code2World, RSWT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the observed screen requires a second model to judge the two. We argue that a world model meant for verification should instead predict in the space in which observations are encoded, and present LGWM, a decoder-free, action-conditioned world model that predicts the representation of the next screen directly, trained without semantic annotation on 1.85M real GUI transitions. Verification reduces to a vector comparison, and the same signal reveals whether a mismatch is harmful. We evaluate on RSWT-BENCH, a diagnostic where each credential screen appears under both a legitimate and a hijacked transition, so detectors that see only the screen are at chance by construction. The training-free score reaches 0.987 AUC at 17 ms per decision, on par with the strongest closed-source VLMs and about ten AUC points above generative GUI world models at over three orders of magnitude lower latency. The residual direction reaches 0.953 AUC at separating harmful from benign violations, where prompted VLMs are near chance. Further analyses show that the prediction is a usable future state rather than an anomaly score. World models have mostly served as simulators or planners; our results point to a third role, verification, for which predicting in representation space is the natural design.

</details>

---

### [[20_Research/Papers/具身智能/WARP-VLA_Wrist-Camera_Adaptation_for_View-Robust_Policy_Execution_in_Vision-Language-Action_Models|WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models]]

![[assets/2610.11508_figure.png|800]]

- **arXiv**: [2610.11508](https://arxiv.org/abs/2610.11508)
- **PDF**: https://arxiv.org/pdf/2610.11508
- **详细分析**: [[20_Research/Papers/具身智能/WARP-VLA_Wrist-Camera_Adaptation_for_View-Robust_Policy_Execution_in_Vision-Language-Action_Models|WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models]]
- **作者**: Junmyeong Lee, Dongmin Shin, Min-Gyu Park, Wooseok Jeon, Inho Chang, Hae-Gon Jeon
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Any3D-VLA, AnyCamVLA, CamVLA, GeoAware-VLA, GeoVLA, OC-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite recent advances in Vision-Language-Action models (VLAs) for robotic manipulation, their performance remains sensitive to changes in camera configuration. The problem becomes more evident in cross-setup deployment, as reproducing the exact camera pose used for training is nearly impossible. Unlike fixed external views, wrist views are more challenging because the camera moves with the robot, causing even small mounting variations to alter fine-grained geometric cues. To address this, we propose WARP-VLA, a camera-view robust VLA for diverse wrist camera configurations. WARP-VLA adopts a Mixture-of-Experts (MoE) architecture where individual experts learn view-specific feature transformations, and a router combines them based on implicit view information. This allows the policy to be deployed without requiring camera extrinsic parameters as additional input. Through experiments on the LIBERO benchmark, WARP-VLA improves the average success rate of pi-0.5 from 39.2% to 78.3% under wrist-view perturbations. The real-robot experiments further show that the feature-level adaptation learned in simulation successfully transfers to diverse deployment settings. To facilitate reproducibility and future research, we release our wrist viewpoint robustness benchmark and a plug-and-play implementation.

</details>

---

### [[20_Research/Papers/具身智能/Being-M0.7_A_Latent_World-Action_Model_for_Humanoid_Robots|Being-M0.7: A Latent World-Action Model for Humanoid Robots]]

![[assets/2610.11283_figure.png|800]]

- **arXiv**: [2610.11283](https://arxiv.org/abs/2610.11283)
- **PDF**: https://arxiv.org/pdf/2610.11283
- **详细分析**: [[20_Research/Papers/具身智能/Being-M0.7_A_Latent_World-Action_Model_for_Humanoid_Robots|Being-M0.7: A Latent World-Action Model for Humanoid Robots]]
- **作者**: Junpeng Yue, Boyuan Li, Yuxuan Wang, Zepeng Wang, Yuhui Fu, Feiyang Xie, Yu Zhang, Jing Zhang, Xianqi Zhang, Weibo Li, Xiaofei Zheng, Yuming Fang...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Being-M0.7: A Latent World-Action Model for Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires coordinated locomotion and manipulation informed by future scene evolution and whole-body motion, yet learning these capabilities is constrained by scarce robot demonstrations. Human video and motion datasets offer scalable supervision, but many contain only video or motion rather than paired video-motion data. Moreover, human motion does not directly specify executable robot actions. We present Being-M0.7, a latent world-action model that transfers visual-motion priors learned from mixed-modality human data to humanoid control through pre-training, robot mid-training, and action post-training. We curate a corpus from more than 10,000 hours of raw human-centric data, integrating video-only, motion-only, and paired video-motion streams to learn complementary visual dynamics and whole-body kinematic structure. Joint prediction of future latent visual states and motion encourages visual representations to encode future kinematics. Robot mid-training adapts this coarse-grained prior to robot viewpoints and body dynamics. During action post-training, an action expert combines visual predictive representations from the frozen, adapted prior with current images and proprioception through gated cross-attention, grounding predictive context in executable whole-body commands. Being-M0.7 achieves the highest aggregate success rate among the compared baselines on SIMPLE and matches the strongest baseline on real-world Unitree G1 loco-manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/OmniDex_Scaling_Dexterous_Hand_Grasping_to_Diverse_Cluttered_Scenes|OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes]]

![[assets/2610.11194_figure.png|800]]

- **arXiv**: [2610.11194](https://arxiv.org/abs/2610.11194)
- **PDF**: https://arxiv.org/pdf/2610.11194
- **详细分析**: [[20_Research/Papers/具身智能/OmniDex_Scaling_Dexterous_Hand_Grasping_to_Diverse_Cluttered_Scenes|OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes]]
- **作者**: Naiyu Fang, Zhongjin Luo, Yuxin Mo, Siyuan Huang, Jianbo Liu, Yufei Liu, Zheyuan Zhou, Chenkai Jin, Xiaogang Wang, Hongsheng Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.6（加权：具身智能 3.3，机器人 0.3）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《OmniDex: Scaling Dexterous Hand Grasping to Diverse Cluttered Scenes》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DexGraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous grasping is the foundational primitive in embodied AI, demanding massive data to train robust models. As real-world data collection is expensive, simulation has become the mainstream paradigm. Yet, while cluttered scenes best reflect real-world applications, learning to grasp within them is bottlenecked by a critical scarcity of large-scale data. To resolve this, we curate high-quality 3D objects and supporting bases, proposing a scalable seed-and-filter strategy that bypasses sluggish scene-level optimization. This yields an unprecedented benchmark comprising over 2.6 million scenes and 0.4B scene-specific grasp ground truths, featuring diverse realistic layouts paired with rich semantic and geometric observations. Furthermore, we introduce the OmniDex model to overcome the grasp multimodality and last-millimeter precision errors plaguing current generative models. By coupling Soft Winner-Takes-All learning with human-inspired physical constraints during training, and utilizing physics-driven ranking, our approach achieves robust dexterous grasping without the latency of post-optimization. Experimental results show that OmniDex model achieves state-of-the-art performance and strong generalization across diverse scenes, views, and unseen objects.

</details>

---

### [[20_Research/Papers/具身智能/VGGTWorld-VLA_Intent-Conditioned_3D_World_Evolution_for_Autonomous_Driving|VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving]]

![[assets/2610.11161_figure.png|800]]

- **arXiv**: [2610.11161](https://arxiv.org/abs/2610.11161)
- **PDF**: https://arxiv.org/pdf/2610.11161
- **详细分析**: [[20_Research/Papers/具身智能/VGGTWorld-VLA_Intent-Conditioned_3D_World_Evolution_for_Autonomous_Driving|VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving]]
- **作者**: Zhaoyang Liu, Kun Jiang, Ziying Song, Diange Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.0（加权：具身智能 1.5，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AutoVLA, CoWorld-VLA, DiffVLA, DriveVLA, OpenDriveVLA, VGGT-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations. Although recent extensions enable temporal 3D prediction, their future evolution remains weakly conditioned on driving intentions and actions, limiting their ability to model alternative action-dependent futures. We propose VGGTWorld-VLA, an intention-conditioned extension of VGGT-World for controllable 3D world evolution in autonomous driving. First, we introduce an action--semantic conditioning mechanism that injects complementary driving semantics and ego-motion representations into the future-token stream, enabling different future geometry predictions for the same observed scene under alternative ego actions. Second, we develop a geometry--language--action bridge that adapts historical geometry, VLA semantic features, and maneuver and trajectory representations for joint conditioning of future geometry prediction. We evaluate future geometry prediction on NAVSIM, while conditioning ablations further examine the contributions of semantic and action information. Compared with the baseline, our method demonstrates competitive geometry prediction performance. Ablation studies further support the effectiveness of semantic and action conditioning. These results demonstrate the potential of semantic and action conditioning for controllable VGGT-based world prediction in autonomous driving.

</details>

---

### [[20_Research/Papers/具身智能/When_Listening_Becomes_Easier_Scrubbing_Visual_Cues_for_Shortcut-Free_VLAs|When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs]]

![[assets/2610.10912_figure.png|800]]

- **arXiv**: [2610.10912](https://arxiv.org/abs/2610.10912)
- **PDF**: https://arxiv.org/pdf/2610.10912
- **详细分析**: [[20_Research/Papers/具身智能/When_Listening_Becomes_Easier_Scrubbing_Visual_Cues_for_Shortcut-Free_VLAs|When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs]]
- **作者**: Jasper Gerigk, Kenzo Aspuru-Takata, Chin-Hsuan Wu, Mohammad Mohammadi, Shuhong Zheng, Igor Gilitschenski
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.9，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《When Listening Becomes Easier: Scrubbing Visual Cues for Shortcut-Free VLAs》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AC-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shortcut learning is a prevalent issue in robot learning. The limited diversity of robot demonstration datasets can mislead policies into exploiting spurious correlations between tasks and irrelevant features, such as viewpoint or background. Collecting sufficiently diverse robot demonstrations is costly and inefficient, motivating algorithmic alternatives. We focus on vision-language-action (VLA) models and discover that different vision-language model backbones exhibit substantially different levels of susceptibility to visual shortcut learning. We find that model behavior correlates with our proposed representation-level metric, action margin, which requires no policy rollouts. Visual shortcuts consistently enter action representations in early layers, with models differing in the extent to which later layers correct them by incorporating language information. To boost models' attention to language, we introduce task scrubbing, a new domain-adversarial training method that decreases models' likelihood of using visual shortcuts and improves VLAs' generalization. Experiments in both simulation and the real world across multiple VLAs and visual cues show that task scrubbing improves out-of-distribution robustness and often eliminates visual shortcut learning.

</details>

---
