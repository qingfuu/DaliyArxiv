# cs.CV | Computer Vision and Pattern Recognition | 2026-09-25

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Ego-Exo4D_Human_Meshes_Dataset_4D_Human_Motion_Reconstruction_for_Ego-Exo_Captures|Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures]]

![[assets/2609.30187_figure.png|800]]

- **arXiv**: [2609.30187](https://arxiv.org/abs/2609.30187)
- **PDF**: https://arxiv.org/pdf/2609.30187
- **详细分析**: [[20_Research/Papers/具身智能/Ego-Exo4D_Human_Meshes_Dataset_4D_Human_Motion_Reconstruction_for_Ego-Exo_Captures|Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures]]
- **作者**: Abhiram Maddukuri, Georgios Pavlakos
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《Ego-Exo4D Human Meshes Dataset: 4D Human Motion Reconstruction for Ego-Exo Captures》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ego-Exo4D is a large-scale dataset providing synchronized egocentric and multi-view exocentric video, a rich resource for skill learning and assessment, procedural activity understanding, and embodied AI. However, the dataset ships with only sparse 3D human pose annotations, and reconstructing dense human motion from its multi-view captures is nontrivial. To this end, we present Ego-Exo4D-HM, a large-scale dataset of 4D human motion reconstructions for Ego-Exo4D's captures, and release the accompanying reconstruction pipeline. The code, dataset, and documentation can be found at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Self-Adaptive_VLA_for_Robust_Robot_Deployment|Self-Adaptive VLA for Robust Robot Deployment]]

![[assets/2609.30092_figure.png|800]]

- **arXiv**: [2609.30092](https://arxiv.org/abs/2609.30092)
- **PDF**: https://arxiv.org/pdf/2609.30092
- **详细分析**: [[20_Research/Papers/具身智能/Self-Adaptive_VLA_for_Robust_Robot_Deployment|Self-Adaptive VLA for Robust Robot Deployment]]
- **作者**: Hongxin Zhang, Chunru Lin, Tsun-Hsuan Wang, Zhenjia Xu, Chuang Gan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 2.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Self-Adaptive VLA for Robust Robot Deployment》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Vision-Language-Action (VLA) models demonstrate impressive capabilities in robotic manipulation, their memoryless nature renders them brittle to test-time environment shifts, particularly hardware shifts caused by wear or imperfect calibration. Enabling these models to self-adapt during deployment without requiring continuous on-site recalibration remains a critical bottleneck for real-world scalability. In this work, we introduce Self-Adaptive VLA, a novel post-training recipe that enables the policy to iteratively adapt to deployment-time hardware shifts leveraging its own rollouts as context. To do so, we first collect policy rollouts under deliberately injected hardware shifts. We then transform the base policy's training data into shift-conditioned expert demonstrations by pre-compensating the expert actions for these known shifts. Next, we introduce a lightweight, plug-in context encoder that compresses the context, including visual observation, proprioception, and actions in the shifted environment, into a latent context token. This token modulates the policy through adaptive layer normalization (AdaLN). Furthermore, we find that context tokens can be ensembled, allowing the policy to iteratively self-correct and mitigate failures step by step. Extensive experiments across four precision-critical bi-manual and dexterous manipulation tasks show that Self-Adaptive VLA recovers over 80% of the base policy's performance under hardware shifts, such as actuation bias and joint encoder offsets. Moreover, Self-Adaptive VLA enables more robust deployment to new workstations compared to the base policy. Our approach provides a pathway for robust large-scale real-world robot deployments and easier maintenance. See videos at this https URL .

</details>

---

### [[20_Research/Papers/大模型/M3GD_Multi-Modal_Multi-View_Geometric_Diffusion_for_Camera--LiDAR_Novel_View_Synthesis|M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis]]

![[assets/2609.30056_figure.png|800]]

- **arXiv**: [2609.30056](https://arxiv.org/abs/2609.30056)
- **PDF**: https://arxiv.org/pdf/2609.30056
- **详细分析**: [[20_Research/Papers/大模型/M3GD_Multi-Modal_Multi-View_Geometric_Diffusion_for_Camera--LiDAR_Novel_View_Synthesis|M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis]]
- **作者**: Yang Zhou, Jiuhong Xiao, Shizhao Ye, Long Quang, Carlos Nieto-Granda, Giuseppe Loianno
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NeuSim, Real-World, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic novel view synthesis (NVS) must recover both visual appearance and metric 3D structure, yet most generative NVS methods rely only on images, overlooking LiDAR, a complementary sensor common on robotic platforms. We present M3GD, a Camera--LiDAR multimodal representation for generative NVS that composes independently pretrained 2D image and 3D point-cloud foundation models without separately pretraining a cross-modal translator. We show that, after camera projection, frozen LiDAR and image features exhibit substantial shared spatial structure, providing a natural cross-modal representation. M3GD conditions generation on LiDAR through this structure: it combines explicit geometry statistics with learned point-cloud descriptors into view-aligned packets on the image-latent grid, injected through a lightweight residual adapter into a multi-view flow-matching generator whose latent space, decoders, and training objective remain intact. On the GrandTour dataset, M3GD improves target-view RGB and depth synthesis over an image-only version of the same backbone. Ablations show that the gains come from pixel-aligned LiDAR content and that target-view LiDAR acts as a geometric query linking the requested view to source observations. Deployment on a ground robot demonstrates practical real-world operation, with a configurable quality--cost trade-off controlled by the number of Euler integration steps.

</details>

---

### [[20_Research/Papers/具身智能/BeyondRetarget_Learning_Executable_Humanoid_Motions_Directly_from_Monocular_Video|BeyondRetarget: Learning Executable Humanoid Motions Directly from Monocular Video]]

![[assets/2609.29850_figure.png|800]]

- **arXiv**: [2609.29850](https://arxiv.org/abs/2609.29850)
- **PDF**: https://arxiv.org/pdf/2609.29850
- **详细分析**: [[20_Research/Papers/具身智能/BeyondRetarget_Learning_Executable_Humanoid_Motions_Directly_from_Monocular_Video|BeyondRetarget: Learning Executable Humanoid Motions Directly from Monocular Video]]
- **作者**: Tianyu Xiong, Yi Lu, Jinrui Wang, Ziqi Liang, Dandan Lei, Xiaoyang Zhou, Xiao-xiao Long, Qiu Shen, Xun Cao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《BeyondRetarget: Learning Executable Humanoid Motions Directly from Monocular Video》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning executable motions from human videos offers a scalable solution for humanoid robots to acquire demonstration motions. However, existing pipelines typically first construct an explicit human motion representation and then convert it into robot motions via motion retargeting. Although such methods can effectively leverage large volumes of existing human data for training, the substantial differences between humans and humanoid robots in locomotion mechanisms and joint degree-of-freedom configurations make motions generated by this human-representation-centric approach difficult to execute on robots. Furthermore, errors introduced during human motion estimation inevitably propagate to the retargeting stage and cannot be eliminated via joint optimization. We propose BeyondRetarget, an end-to-end framework that directly maps monocular RGB videos to robot motions. Discarding the explicit human representation, this framework learns robot-oriented implicit representations directly from visual observations, enabling the model to capture cross-morphology motion structures. To generate motions more suitable for robot execution, we further design a contact-aware motion optimization mechanism to improve temporal consistency and physical plausibility. Experiments show that BeyondRetarget significantly improves the accuracy and robustness of generated robot motions, while achieving higher execution success rates and lower latency in both simulation environments and real humanoid robots.

</details>

---

### [[20_Research/Papers/大模型/Retrieve-to-Localize_Bridging_Large_Language_Models_and_LiDAR_Geometry_for_Spatial_Grounding|Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding]]

![[assets/2609.29835_figure.png|800]]

- **arXiv**: [2609.29835](https://arxiv.org/abs/2609.29835)
- **PDF**: https://arxiv.org/pdf/2609.29835
- **详细分析**: [[20_Research/Papers/大模型/Retrieve-to-Localize_Bridging_Large_Language_Models_and_LiDAR_Geometry_for_Spatial_Grounding|Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding]]
- **作者**: Byounggun Park, Giyong Moon, Jusung Kim, Soonmin Hwang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《Retrieve-to-Localize: Bridging Large Language Models and LiDAR Geometry for Spatial Grounding》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：NuScenes-QA, NuScenes-SpatialQA, PRL, SpatialLiDAR-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LiDAR provides precise geometric information for spatial perception tasks such as object detection in autonomous driving and outdoor robotics. However, recognizing and localizing individual objects is not sufficient to answer questions that require composing spatial relations and grounding the intended target. Motivated by recent advances in large language models (LLMs) for autonomous driving, we leverage their language priors to interpret complex spatial questions and ground the referred target in LiDAR geometry. To support this spatial grounding capability, we introduce SpatialLiDAR-QA, which combines single- and multi-step relational grounding with complementary spatial understanding tasks. We further propose SpatialLiDAR-LM, which aligns LiDAR point features with an LLM and grounds target coordinates through language-conditioned, position-aware proposal retrieval and local point refinement. This design derives target coordinates directly from local LiDAR geometry rather than through textual language decoding. Experiments demonstrate substantial improvements over representative LiDAR--language models and multi-camera VLMs on precise coordinate prediction tasks. Our dataset and model training code will be publicly released.

</details>

---

### [[20_Research/Papers/具身智能/Visual_Representation_and_History_Modeling_for_Navigation_World_Models|Visual Representation and History Modeling for Navigation World Models]]

![[assets/2609.29555_figure.png|800]]

- **arXiv**: [2609.29555](https://arxiv.org/abs/2609.29555)
- **PDF**: https://arxiv.org/pdf/2609.29555
- **详细分析**: [[20_Research/Papers/具身智能/Visual_Representation_and_History_Modeling_for_Navigation_World_Models|Visual Representation and History Modeling for Navigation World Models]]
- **作者**: Guangfu Guo, Xiaoqian Lu, Rui Liu, Yutong Chen, Kunpeng Liu, Long Cheng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Visual Representation and History Modeling for Navigation World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeltaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation World Models (NWMs) predict action-conditioned visual futures for planning. Two practical challenges are central to their design: selecting a suitable visual representation and efficiently modeling observation history for repeated candidate queries. Standard Global-Softmax attention provides flexible interactions but repeatedly processes the same history, leading to increasing computation and memory costs for long contexts and multi-query planning. We study both problems within a unified conditional flow-transformer framework. We first compare five frozen visual representations under the same dynamics model and evaluation. To reduce redundant history computation, we design Cached-Linear, a hybrid architecture that combines local and shifted-window attention for target mixing with linear attention for reusable history access. We further develop Balanced Gated Delta Network (GDN), which augments this design with frame-wise recurrent memory for temporal history modeling. Experiments on RECON, SACSoN, and SCAND show that representation choice depends on the prediction objective: PAE-L performs best for reconstruction, RAE-B for direct prediction, and V-JEPA for long-horizon rollout. Under shared-history workloads, Cached-Linear substantially reduces computation and memory compared with Global-Softmax, while Balanced GDN improves selected direct-prediction endpoints with efficient context reuse. Overall, we systematically study visual representation and history modeling for NWMs and develop hybrid reusable-history architectures for efficient long-context and multi-query prediction.

</details>

---

### [[20_Research/Papers/具身智能/EgoSpeedUp_Transferring_Human_Manipulation_Tempo_to_Robot_Policies|EgoSpeedUp: Transferring Human Manipulation Tempo to Robot Policies]]

![[assets/2609.29310_figure.png|800]]

- **arXiv**: [2609.29310](https://arxiv.org/abs/2609.29310)
- **PDF**: https://arxiv.org/pdf/2609.29310
- **详细分析**: [[20_Research/Papers/具身智能/EgoSpeedUp_Transferring_Human_Manipulation_Tempo_to_Robot_Policies|EgoSpeedUp: Transferring Human Manipulation Tempo to Robot Policies]]
- **作者**: Hanbit Oh, Yukiyasu Domae, Takuma Yagi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《EgoSpeedUp: Transferring Human Manipulation Tempo to Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation policies trained through imitation learning inherit not only the demonstrated behavior but also the conservative execution tempo of robot demonstrations. Existing acceleration approaches can execute faster than the original demonstrations, but determine the appropriate acceleration primarily from robot-side information or a predefined set of tempo factors, leaving open how to obtain a task-appropriate reference for how fast each manipulation phase should progress. We introduce EgoSpeedUp, a framework that uses human manipulation as temporal supervision for robot imitation learning. Our key insight is that human demonstrations naturally reveal task-appropriate, phase-wise manipulation tempo. Given slow robot demonstrations and human demonstrations of the same task, EgoSpeedUp aligns corresponding manipulation phases, estimates their relative execution tempos from multiple human demonstrations, and transfers the resulting phase-wise tempo by retiming the robot demonstrations. The retimed demonstrations are then used for standard behavior cloning, allowing the robot to retain its executable manipulation behavior while learning to perform it at a human-informed tempo. Across two real-world manipulation tasks, EgoSpeedUp improves the task success rate by an average of 25 percentage points (pp) while reducing successful execution time by 36.5%. These results demonstrate that human manipulation tempo provides an effective temporal reference for learning faster and more reliable robot policies.

</details>

---

### [[20_Research/Papers/具身智能/Representation_World_Model_Learning_States,_Transition_and_Executable_Plans_in_Representation|Representation World Model: Learning States, Transition and Executable Plans in Representation]]

![[assets/2609.29171_first_page.png|800]]

- **arXiv**: [2609.29171](https://arxiv.org/abs/2609.29171)
- **PDF**: https://arxiv.org/pdf/2609.29171
- **详细分析**: [[20_Research/Papers/具身智能/Representation_World_Model_Learning_States,_Transition_and_Executable_Plans_in_Representation|Representation World Model: Learning States, Transition and Executable Plans in Representation]]
- **作者**: Yijun Yuan, Weicheng Zheng, Weibang Wang, Minghui Qin, Chang Sun, Junhao Huang, Kenan Li, Anmin Liu, Yicheng Yao, Hang Zhao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 0.9，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Representation World Model: Learning States, Transition and Executable Plans in Representation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose the Representation World Model (RWM), which learns states, transitions, and executable plans directly in representation space. Unlike existing world models that typically learn latent representations together with explicit dynamics models and perform planning through search, optimization, or policy-based prediction, RWM directly incorporates planning into the learned representation geometry. RWM learns the representation geometry by applying inverse-dynamics supervision locally along latent paths constructed from endpoint representations, requiring these paths to preserve task-relevant state and transition information. At inference, planning is performed by directly constructing a latent path between the current and goal representations, with inverse dynamics used to recover the corresponding actions, without recursive rollouts or action-space search. Experiments on continuous-control benchmarks demonstrate the effectiveness of RWM for direct planning, while results on robotic manipulation further show its potential to extend to more complex embodied control tasks. These results suggest that planning directly in representation space provides a promising alternative to conventional world-model planning.

</details>

---

### [[20_Research/Papers/世界模型/HelloWorld_Towards_Practical_Applications_of_Generative_Driving_World_Models|HelloWorld: Towards Practical Applications of Generative Driving World Models]]

![[assets/2609.28931_figure.png|800]]

- **arXiv**: [2609.28931](https://arxiv.org/abs/2609.28931)
- **PDF**: https://arxiv.org/pdf/2609.28931
- **详细分析**: [[20_Research/Papers/世界模型/HelloWorld_Towards_Practical_Applications_of_Generative_Driving_World_Models|HelloWorld: Towards Practical Applications of Generative Driving World Models]]
- **作者**: Fan Lu, Hanshi Wang, Zijing Wang, Quan Feng, Zhi Wang, Shijie Chen, Xianming Zeng, Yujian Zhang, Jiazhe Wang, Xin Zha, Kai Wang, Zhijie Zhao...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision, Systems

#### 研究背景与动机

《HelloWorld: Towards Practical Applications of Generative Driving World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DrivingWorld, HY-World, HelloWorld, LingBot-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs. Realizing this potential requires a system that can generalize across diverse scenes, respond faithfully to prescribed controls, generate coherent multi-sensor observations, and operate efficiently under repeated inference. We present \textbf{HelloWorld}, a 2B driving world model system designed around these requirements. HelloWorld progressively specializes broad visual and motion priors from heterogeneous video data into controllable driving generation using ego pose, HD maps, and 3D boxes. A block-causal generation interface, together with adaptation to self-generated context, aligns the model with sequential simulation. The system further supports synchronized seven-camera RGB generation and conditional LiDAR synthesis, and is distilled toward few-step inference for efficient deployment. Experiments evaluate visual quality, control fidelity, cross-view consistency, robustness under repeated generation, inference efficiency, and LiDAR synthesis. Together, HelloWorld provides a unified framework for scalable driving data generation and interactive simulation.

</details>

---

### [[20_Research/Papers/具身智能/Direction-Scale_Decomposition_in_Action_Representation_Rethinking_What_to_Tokenize_for_Vision-Language-Action_Models|Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models]]

![[assets/2609.28865_figure.png|800]]

- **arXiv**: [2609.28865](https://arxiv.org/abs/2609.28865)
- **PDF**: https://arxiv.org/pdf/2609.28865
- **详细分析**: [[20_Research/Papers/具身智能/Direction-Scale_Decomposition_in_Action_Representation_Rethinking_What_to_Tokenize_for_Vision-Language-Action_Models|Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models]]
- **作者**: Yufei Duan, Hang Yin, Alberta Longhini, Chao Tang, Danica Kragic
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, SpatialVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action representation plays a central role in discrete-token vision-language-action (VLA) learning but remains underexamined. Under conventional pose-increment representations, action tokens are sensitive to execution speed and dataset-specific normalization, potentially obscuring geometric structure shared across demonstrations and datasets. We introduce Direction-Scale Decomposition (DSD), an action representation that decomposes translation and rotation increments into direction and scale components before tokenization. DSD isolates motion direction while retaining magnitudes in separate scale channels. We evaluate DSD with uniform binning (BIN) and BEAST, a B-spline-based tokenizer, in simulation and real-world manipulation under both single-dataset and mixed-dataset training. On LIBERO, DSD improves average success rates with both tokenizers. On SimplerEnv, DSD-BIN outperforms BIN by 10.3 percentage points in overall success rate under mixed-dataset training. Real-robot experiments further show gains both with and without robotics pretraining. These results support DSD as an effective action representation for discrete-token VLA models and suggest its potential to mitigate performance degradation when training on large and diverse dataset mixtures. Our project page with additional resources is available at this https URL

</details>

---
