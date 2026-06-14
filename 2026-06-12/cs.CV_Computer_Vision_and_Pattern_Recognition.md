# cs.CV | Computer Vision and Pattern Recognition | 2026-06-12

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/强化学习/MaskWAM_Unifying_Mask_Prompting_and_Prediction_for_World-Action_Models|MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models]]

![[assets/2606.13515_figure.png|800]]

- **arXiv**: [2606.13515](https://arxiv.org/abs/2606.13515)
- **PDF**: https://arxiv.org/pdf/2606.13515
- **详细分析**: [[20_Research/Papers/强化学习/MaskWAM_Unifying_Mask_Prompting_and_Prediction_for_World-Action_Models|MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models]]
- **作者**: Hanyang Yu, Haitao Lin, Jingbo Zhang, Wenyao Zhang, Chenghao Gu, Heng Li, Ping Tan
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) present a promising paradigm for robotic control via video prediction. However, current WAMs suffer from fundamental spatial bottlenecks: standard text inputs introduce referential ambiguity in cluttered scenes, while unstructured RGB predictions lack semantic grounding and remain biased by task-irrelevant backgrounds. To overcome these limitations, we introduce MaskWAM, an object-centric world-action model. By jointly integrating masks as both explicit inputs and predictions via a unified Mixture of Transformers (MoT), MaskWAM unlocks robust policy generalization. This design provides two key benefits: (1) predicting future masks yields object-centric semantic supervision that suppresses visual noise, significantly enhancing even standard text-conditioned WAMs; and (2) coupling this predictive supervision with first-frame visual prompts, such as target object masks, establishes a precise spatial anchor that substantially reduces language ambiguity. Crucially, as WAMs are inherently vision-driven architectures, direct mask conditioning yields substantially stronger guidance than text alone, establishing a precise and robust paradigm for manipulating unseen objects. Evaluations on LIBERO, RoboTwin, and real-world tasks demonstrate that MaskWAM significantly outperforms baselines in both language-clear and language-ambiguous tasks.

</details>

---

### [[20_Research/Papers/具身智能/SPARC_Reliable_Spatial_Annotations_from_Robot_Demonstrations_at_Scale|SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale]]

![[assets/2606.13497_figure.png|800]]

- **arXiv**: [2606.13497](https://arxiv.org/abs/2606.13497)
- **PDF**: https://arxiv.org/pdf/2606.13497
- **详细分析**: [[20_Research/Papers/具身智能/SPARC_Reliable_Spatial_Annotations_from_Robot_Demonstrations_at_Scale|SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale]]
- **作者**: Nils Blank, Paul Mattes, Maximilian Xiling Li, Jakub Suliga, Thomas Roth, Moritz Reuss, Pankhuri Vanjani, Rudolf Lioutikov
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SPARC: Reliable Spatial Annotations from Robot Demonstrations at Scale》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IA-Bench, Real-World, VABench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work introduces Spatial Annotations from Robot Demonstrations with Reliability Calibration (SPARC), a risk-aware framework that automatically labels robot demonstrations with structured spatial annotations and assigns each annotation a reliability score. Structured spatial annotations, such as bounding boxes, object trajectories, and manipulation phase labels, benefit a broad range of robotics applications from training grounded robot policies and embodied foundation models to motion planning and hierarchical task composition. Existing automated pipelines generate such annotations at scale but provide no reliable quality signal: detector confidence is poorly calibrated for annotation correctness, forcing a choice between accepting noisy labels or discarding useful samples. In contrast to existing automated pipelines, SPARC leverages the spatio-temporal structure inherent to robot tasks to generate a reliability signal, reducing noisy labels and retaining more useful samples. We further introduce Interaction-Aware Bench (IA-Bench), a benchmark that measures model accuracy in grounding the locations of interacted objects in robot demonstrations. On 1.7k human-annotated demonstrations spanning diverse embodiments and scenarios, SPARC significantly outperforms detection-only baselines in localization accuracy while retaining three times more samples at high-precision operating points. Our experiments demonstrate that models finetuned on our annotations achieve state-of-the-art results on object-grounding and pointing benchmarks among similarly sized models, while remaining competitive on broader spatial-reasoning suites without manually verified or annotated training data. Furthermore, policies trained on SPARC-generated annotations outperform baselines in cluttered, visually ambiguous real-world scenes. Code, data, and models are available at intuitive-robots.github.io/sparc-labeling.

</details>

---

### [[20_Research/Papers/具身智能/NavWAM_A_Navigation_World_Action_Model_for_Goal-Conditioned_Visual_Navigation|NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation]]

![[assets/2606.13494_figure.png|800]]

- **arXiv**: [2606.13494](https://arxiv.org/abs/2606.13494)
- **PDF**: https://arxiv.org/pdf/2606.13494
- **详细分析**: [[20_Research/Papers/具身智能/NavWAM_A_Navigation_World_Action_Model_for_Goal-Conditioned_Visual_Navigation|NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation]]
- **作者**: Daichi Azuma, Taiki Miyanishi, Koya Sakamoto, Shuhei Kurita, Yaonan Zhu, Petr Khrapchenkov, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.3，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OmniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Goal-conditioned visual navigation requires a robot to act under partial observability by anticipating how its motion will change the future egocentric view and whether that change brings it closer to the goal. Navigation world models provide such visual foresight, but they remain prediction modules that require an external planner to convert predicted futures into closed-loop control. We propose Navigation World Action Model (NavWAM), a diffusion-transformer policy that turns navigation world-model prediction into executable action by representing future observations, goal-progress values, and action chunks in a shared latent sequence. By learning future prediction jointly with the action and value targets that determine closed-loop behavior, NavWAM makes visual foresight directly usable for robot control. We build NavWAM through simulation pretraining and real-robot adaptation, and evaluate it on image-goal navigation against planning-based world models and a representative direct navigation policy. Across offline benchmarks and closed-loop real-robot deployment, NavWAM improves over planning-based world-model baselines in our evaluations while using the default policy mode without CEM-style action search. Project page: https://dachii-azm.github.io/navwam/

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Neural_Model_Editing|Reinforcement Learning for Neural Model Editing]]

![[assets/2606.13461_figure.png|800]]

- **arXiv**: [2606.13461](https://arxiv.org/abs/2606.13461)
- **PDF**: https://arxiv.org/pdf/2606.13461
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Neural_Model_Editing|Reinforcement Learning for Neural Model Editing]]
- **作者**: Shaivi Malik
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Reinforcement Learning for Neural Model Editing》归入 强化学习、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MaskWorld, ShiftWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Editing pretrained neural networks requires specialized algorithms tailored to specific objectives. Designing such algorithms is often time-consuming and demands significant effort. We present an exploratory framework that formulates neural model editing as a reinforcement learning problem, where agents modify models using reward feedback. We introduce two environments: MaskWorld, where agents scale weights multiplicatively, and ShiftWorld, where agents apply additive weight updates. The reward function combines a utility-preservation objective with a task-specific editing objective, enabling agents to learn targeted modifications while maintaining overall model performance. We evaluate the framework on bias mitigation in text classification and machine unlearning in image classification, both of which traditionally rely on specialized algorithms. Our results show that the learned policies reduce forget set accuracy to nearly 0% while preserving over 90% retain set accuracy on the unlearning task. In the bias mitigation setting, the learned policies improve bias-related performance by more than 5% while maintaining general classification utility. Our findings show that neural model editing can be cast as a reinforcement learning problem, allowing editing policies to be learned from reward feedback rather than manually engineered for each task.

</details>

---

### [[20_Research/Papers/世界模型/VISA_VLM-Guided_Instance_Semantic_Auditing_for_3D_Occupancy_World_Models|VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models]]

![[assets/2606.13460_figure.png|800]]

- **arXiv**: [2606.13460](https://arxiv.org/abs/2606.13460)
- **PDF**: https://arxiv.org/pdf/2606.13460
- **详细分析**: [[20_Research/Papers/世界模型/VISA_VLM-Guided_Instance_Semantic_Auditing_for_3D_Occupancy_World_Models|VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models]]
- **作者**: Ruiqi Xian, Yuehan Xian, Jing Liang, Xuewei Qi, Dinesh Manocha
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 机器人
- **相关性评分**: 1.4（加权：大模型 0.4，世界模型 0.8，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models》归入 世界模型、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GaussianWorld, OccWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semantic 3D occupancy provides a voxelized world state for autonomous driving and robot decision making, but object and rare-class errors can affect free-space interpretation, collision checking, and temporal state propagation. We show that a common VLM strategy, aligning 3D voxel or object features with crop-caption embeddings, improves text-space similarity without reliably improving closed-set occupancy mIoU. Motivated by this mismatch, we propose VISA, a training-time semantic auditing approach for existing occupancy world models. VISA queries an offline VLM on a representative crop of each physical object instance, obtains a structured audit with class hypotheses, plausible confusions, reliability, attributes, and evidence, and propagates it along the object track. The audit is grounded to matched 3D object voxels and distilled into semantic logits through reliability-weighted taxonomy, attribute-factor, and scene-level audit graph losses, while inference remains unchanged and requires no VLM. On nuScenes, averaged across three runs, VISA improves OccWorld from 19.06 to 20.05 mIoU and GaussianWorld from 21.36 to 21.91 mIoU; on GaussianWorld, object mIoU improves from 18.18 to 19.16 and rare-class mIoU from 15.60 to 16.79. These results suggest that VLMs are better suited to closed-set occupancy as reliability-aware semantic auditors than as generic caption-embedding targets.

</details>

---

### [[20_Research/Papers/机器人/GeoCFNet_Geometry-Aware_Confidence_Field_Network_for_Robot-Assisted_Endoscopic_Submucosal_Dissection|GeoCFNet: Geometry-Aware Confidence Field Network for Robot-Assisted Endoscopic Submucosal Dissection]]

![[assets/2606.13032_figure.png|800]]

- **arXiv**: [2606.13032](https://arxiv.org/abs/2606.13032)
- **PDF**: https://arxiv.org/pdf/2606.13032
- **详细分析**: [[20_Research/Papers/机器人/GeoCFNet_Geometry-Aware_Confidence_Field_Network_for_Robot-Assisted_Endoscopic_Submucosal_Dissection|GeoCFNet: Geometry-Aware Confidence Field Network for Robot-Assisted Endoscopic Submucosal Dissection]]
- **作者**: Rui Tang, Guankun Wang, Long Bai, Haochen Yin, Huxin Gao, Jiewen Lai, Jiazheng Wang, Hongliang Ren
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《GeoCFNet: Geometry-Aware Confidence Field Network for Robot-Assisted Endoscopic Submucosal Dissection》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GeoCFNet, TransUNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Advanced surgical robotics has made robot-assisted endoscopic submucosal dissection (ESD) a promising approach for the en-bloc resection of large lesions, with the potential to reduce recurrence and improve long-term outcomes. However, the technical complexity and risk of complications in ESD demand stable and precise visual guidance to maintain an accurate dissection corridor and a safe tissue margin. Dense confidence fields provide an effective representation for this purpose by describing both the preferred dissection region and its spatial transition to surrounding tissue. However, reliable confidence field estimation remains challenging in dynamic endoscopic scenes due to smoke, specular highlights, tissue deformation, weak texture, and the thin geometric structure of the target region. To address these challenges, we formulate dissection guidance as a geometry-aware confidence field estimation problem and propose GeoCFNet, a geometry-aware confidence field network built on a pretrained DINOv3 backbone. GeoCFNet integrates a Token-Differentiated Fusion module to aggregate class-token context with dense patch representations, a SegFormer decoder for confidence regression, and Geometry-Aware Spatial Regularization (GASR) to preserve spatial coherence and local geometric transitions. Experimental results show that GeoCFNet achieves RMSE 0.0480, PSNR 27.1995, SSIM 0.3397, and CC 0.2466, indicating accurate and geometrically stable confidence field estimation for robot-assisted ESD guidance.

</details>

---

### [[20_Research/Papers/具身智能/Trajectory-Level_Redirection_Attacks_on_Vision-Language-Action_Models|Trajectory-Level Redirection Attacks on Vision-Language-Action Models]]

![[assets/2606.12978_figure.png|800]]

- **arXiv**: [2606.12978](https://arxiv.org/abs/2606.12978)
- **PDF**: https://arxiv.org/pdf/2606.12978
- **详细分析**: [[20_Research/Papers/具身智能/Trajectory-Level_Redirection_Attacks_on_Vision-Language-Action_Models|Trajectory-Level Redirection Attacks on Vision-Language-Action Models]]
- **作者**: Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür, Melkior Ornik
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Trajectory-Level Redirection Attacks on Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies bring natural language into closed-loop robot control, enabling robots to execute manipulation tasks directly from text instructions. The same interface gives text a recurring role in control because the prompt is reused at every replanning step, and each prompt-conditioned action changes the future observations on which the policy acts. Existing VLA attacks study adversarial prompts that elicit targeted low-level actions or make such actions persist across changing images. We identify a stronger trajectory-level failure mode: a prompt that still $\textit{appears}$ to specify the intended task but redirects the final physical outcome. We mathematically formalize this setting as $\textit{command-preserving trajectory redirection}$, a prompt-only threat model in which the attacker chooses one prompt before the episode, all policy and environment components remain fixed, and the prompt must stay close to the benign instruction while omitting target words and correction language. To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints. Experiments in simulation and on hardware show that near-benign prompt perturbations can redirect VLA rollouts to attacker-specified targets. These results expose a trajectory-level vulnerability in VLA instruction grounding: text that appears to preserve the intended command can still give an adversary control over the robot's final physical outcome. Project website: https://vla-redirection-attack.github.io/

</details>

---

### [[20_Research/Papers/机器人/EquiDexFlow_Contact-Grounded_SE(3)-Equivariant_Dexterous_Grasp_Generative_Flows|EquiDexFlow: Contact-Grounded SE(3)-Equivariant Dexterous Grasp Generative Flows]]

![[assets/2606.12728_figure.png|800]]

- **arXiv**: [2606.12728](https://arxiv.org/abs/2606.12728)
- **PDF**: https://arxiv.org/pdf/2606.12728
- **详细分析**: [[20_Research/Papers/机器人/EquiDexFlow_Contact-Grounded_SE(3)-Equivariant_Dexterous_Grasp_Generative_Flows|EquiDexFlow: Contact-Grounded SE(3)-Equivariant Dexterous Grasp Generative Flows]]
- **作者**: Clinton Enwerem, John S. Baras, Calin Belta
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《EquiDexFlow: Contact-Grounded SE(3)-Equivariant Dexterous Grasp Generative Flows》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most learned dexterous grasp generators relegate contact forces to a downstream verification step, so a kinematically-plausible pose can still violate the conditions for a stable physical grasp. We address this with EquiDexFlow, an SE(3)-equivariant flow-matching model that jointly predicts wrist pose, joint angles, fingertip contacts, surface normals, and contact forces from an object point cloud. Our architecture projects contacts onto the object surface and forces into the Coulomb friction cone by construction, so placement and friction compliance hold without loss penalties. We prove end-to-end SE(3) equivariance and verify it empirically over 200 rotations, with wrist residuals below $0.04^\circ$ and exactly zero joint deviation. Trained on 8,100 force-closure grasps across 81 objects for the 16-DoF Allegro Hand, our model achieves zero friction violations, the best composite score, and the lowest wrench residual among all ablation variants. We retarget decoded fingertip contacts to a 16-DoF LEAP Hand via per-finger inverse kinematics, and our hardware-feasible refinement places every joint at least 5% inside its actuator envelope while preserving wrench balance. On the physical robot, retargeted EquiDexFlow-decoded grasps complete open-loop pick-and-hold trials on all six test objects, with every asymmetric object succeeding at both the canonical pose and a $120^\circ$ co-rotation. Videos, code, and checkpoints are available at https://equidexflow.github.io.

</details>

---

### [[20_Research/Papers/具身智能/VLADriveBench_Evaluating_CoT-Action_Relationship_in_VLA_for_Autonomous_Driving|VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving]]

![[assets/2606.12706_figure.png|800]]

- **arXiv**: [2606.12706](https://arxiv.org/abs/2606.12706)
- **PDF**: https://arxiv.org/pdf/2606.12706
- **详细分析**: [[20_Research/Papers/具身智能/VLADriveBench_Evaluating_CoT-Action_Relationship_in_VLA_for_Autonomous_Driving|VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving]]
- **作者**: Thach Nguyen, Danhua Guo, Tom Lampo, Fei Wu, Burhan Yaman
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal

#### 研究背景与动机

《VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CF-VLA, LingoQA, VLADriveBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside driving trajectories, but existing benchmarks evaluate only trajectory quality and do not assess whether the CoT is relevant, consistent, or causally connected to the driving action. We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationship. Applying VLADriveBench to three models across two architectures, we find that the two analyses can diverge sharply: ORION scores highest on observational alignment yet its CoT is epiphenomenal, while Alpamayo v1.5 scores lower yet its CoT is strongly causal, with visual salience gating the extent of CoT influence.

</details>

---
