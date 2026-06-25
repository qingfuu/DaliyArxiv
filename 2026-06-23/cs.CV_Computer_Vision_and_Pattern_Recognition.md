# cs.CV | Computer Vision and Pattern Recognition | 2026-06-23

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/大模型/Real-Time_Multimodal_Activity-Aware_Error_Detection_in_Robot-Assisted_Surgery|Real-Time Multimodal Activity-Aware Error Detection in Robot-Assisted Surgery]]

![[assets/2606.23593_figure.png|800]]

- **arXiv**: [2606.23593](https://arxiv.org/abs/2606.23593)
- **PDF**: https://arxiv.org/pdf/2606.23593
- **详细分析**: [[20_Research/Papers/大模型/Real-Time_Multimodal_Activity-Aware_Error_Detection_in_Robot-Assisted_Surgery|Real-Time Multimodal Activity-Aware Error Detection in Robot-Assisted Surgery]]
- **作者**: Seyed Hamid Reza Roodabeh, Zongyu Li, Homa Alemzadeh
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Real-Time Multimodal Activity-Aware Error Detection in Robot-Assisted Surgery》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-assisted minimally invasive surgery improves surgical precision but introduces complexity, making technical error detection essential for ensuring patient safety. Current executional error detection methods using video data often overlook fine-grained contextual descriptions of activities and error types within the hierarchical structure of surgical procedures. They also under-utilize complementary multimodal information. We propose a unified framework for executional error detection that leverages multimodal input, including video, kinematics, and descriptive textual prompts. Through activity prompting, we integrate descriptive language in gesture-level activities, instrument-object interactions, and error definitions. We also introduce activity-aware visual embeddings derived from vision encoders pretrained on surgical activity labels to compare the effectiveness of contrastive language-image embeddings with traditional image-based embeddings for error detection. By seamlessly integrating kinematic data with video and textual modalities, our framework significantly improves error detection performance. Achieving up to 5\% and 16.6\% F1 score improvements over state-of-the-art baselines on the JIGSAWS and SAR-RARP50 datasets, respectively, we demonstrate the value of combining curated textual prompts with multimodal data for accurate error detection.

</details>

---

### [[20_Research/Papers/具身智能/HoloAgent-0_A_Unified_Embodied_Agent_Framework_with_3D_Spatial_Memory|HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory]]

![[assets/2606.23565_first_page.png|800]]

- **arXiv**: [2606.23565](https://arxiv.org/abs/2606.23565)
- **PDF**: https://arxiv.org/pdf/2606.23565
- **详细分析**: [[20_Research/Papers/具身智能/HoloAgent-0_A_Unified_Embodied_Agent_Framework_with_3D_Spatial_Memory|HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory]]
- **作者**: Xiaolin Zhou, Liu Liu, Tingyang Xiao, Wei Feng, Fa Fu, Xinrui Meng, Xinjie Wang, Jialiang Han, Boyang Yu, Yun Du, Wei Sui, Zhizhong Su
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.8，大模型 0.6，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents follow a practical execution loop in digital environments: they reason over structured states, invoke tools, inspect feedback, and revise actions. Extending this loop to physical robots is difficult because physical execution is continuous, embodiment-dependent, uncertain, and constrained by safety. Existing embodied-AI systems have advanced manipulation, spatial understanding, navigation, and humanoid control, but these capabilities often remain specialized modules or loosely coupled decision loops. In this work, we introduce HoloAgent-0, a unified embodied agent framework for real-world robot deployment. Embodied AgentOS converts language instructions into executable skill graphs, schedules robot resources, monitors execution, and triggers clarification or re-planning from runtime feedback. HoloAgent-0 organizes heterogeneous robot models and controllers through three coupled layers: Embodied AgentOS for closed-loop execution, 3D spatial memory for physical world grounding, and embodied skills for robot action. We deploy HoloAgent-0 on real hardware and evaluate its spatial memory, long-horizon navigation, and closed-loop execution across motion generation, object search, cross-robot coordination, and mobile manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Flow6D_Discrete-to-Continuous_Flow_Matching_for_Efficient_and_Accurate_Category-Level_6D_Pose_Estimation|Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation]]

![[assets/2606.23293_figure.jpeg|800]]

- **arXiv**: [2606.23293](https://arxiv.org/abs/2606.23293)
- **PDF**: https://arxiv.org/pdf/2606.23293
- **详细分析**: [[20_Research/Papers/具身智能/Flow6D_Discrete-to-Continuous_Flow_Matching_for_Efficient_and_Accurate_Category-Level_6D_Pose_Estimation|Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation]]
- **作者**: Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

6D pose estimation is a key task in computer vision and embodied AI, widely used in robotic manipulation, augmented reality, etc. Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance. This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy. Rotation and translation parameters are first discretized into bins, with a discrete flow matching model locking the latent space around the true pose to reduce search complexity. Then, by sampling in the latent space, a continuous flow matching model predicts local pose residuals to optimize the estimate and regress to an accurate pose. The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS. Project website: https://flow6d.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Can_Single-View_Mesh_Reconstruction_Generalize_to_Robot_Camera_Rotation|Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?]]

![[assets/2606.22987_figure.png|800]]

- **arXiv**: [2606.22987](https://arxiv.org/abs/2606.22987)
- **PDF**: https://arxiv.org/pdf/2606.22987
- **详细分析**: [[20_Research/Papers/具身智能/Can_Single-View_Mesh_Reconstruction_Generalize_to_Robot_Camera_Rotation|Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?]]
- **作者**: Yu Zhan, Guangcheng Chen, Hanjing Ye, Zhiqin Cheng, Zanjia Tong, Wenjun Xu, Hong Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Single-view mesh reconstruction predicts object meshes and spatial layouts from a single observation, making it attractive for fast robot spatial reasoning and real-to-sim digital twins. However, robot-mounted cameras naturally rotate during manipulation and navigation, while learned single-view reconstruction models often rely on view-dependent priors and may generalize poorly to out-of-distribution camera rotations. Such rotations can introduce 3D inconsistencies, incorrect layouts, and violations of physical constraints, but this failure mode remains under-evaluated. We introduce an evaluation protocol with controlled axis-wise roll, pitch, and yaw sweeps to trace errors in monocular depth estimation (MDE), canonical object meshes, camera-space layout, and physical plausibility within a representative SAM3D-style pipeline. On the Aria Digital Twin dataset and a real Franka wrist-camera sequence, camera rotations induce MDE distortion, layout drift, and collision penetration, while canonical mesh predictions remain relatively stable. A two-stage SAM3D+FoundationPose pipeline is more robust than one-stage feed-forward layout prediction, and our Gravity-Aware Refinement reduces one-stage pairwise ICP-based layout-orientation error by 47.1$\%$. Our evaluation reveals that current single-view mesh reconstruction methods generalize poorly to robot camera rotation, and suggests that explicit gravity cues are important for reliable robotic single-view mesh reconstruction.

</details>

---

### [[20_Research/Papers/具身智能/Humanoid-OmniOcc_Stereo-Based_Full-View_Occupancy_Dataset_for_Embodied_AI|Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI]]

![[assets/2606.22971_figure.png|800]]

- **arXiv**: [2606.22971](https://arxiv.org/abs/2606.22971)
- **PDF**: https://arxiv.org/pdf/2606.22971
- **详细分析**: [[20_Research/Papers/具身智能/Humanoid-OmniOcc_Stereo-Based_Full-View_Occupancy_Dataset_for_Embodied_AI|Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI]]
- **作者**: Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 5.4（加权：具身智能 3.9，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Occ-ScanNet, StereoVoxelNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Occupancy prediction at voxel-level granularity is essential for safe robotic navigation and interaction in complex environments. Existing occupancy datasets, however, are predominantly designed for autonomous driving with vehicle-centric biases -- forward-facing cameras, far-field geometry, and static road priors -- limiting their applicability to embodied humanoid perception. We present Humanoid-OmniOcc, a large-scale panoramic stereo-based occupancy dataset tailored for humanoid robots. The dataset encompasses 15 diverse simulated indoor scenes and 5 real-world environments, yielding over 155K samples with broad scene and style diversity. Importantly, the dataset is designed around a Real2Sim2Real closed-loop paradigm: real sensor specifications drive physically accurate simulation, simulation produces large-scale annotated training data, and models trained in simulation are directly evaluated on real-world captures -- enabling iterative refinement of the sim-to-real pipeline. We further propose \textbf{H}umanoid \textbf{S}urround \textbf{S}tereo-guided \textbf{Occ}upancy model (Humanoid-OmniOcc) that exploits robust depth priors for accurate 2D-to-3D lifting. Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design. Code and data will be available upon acceptance at https://d-robotics-ai-lab.github.io/humanoid-omniocc.

</details>

---

### [[20_Research/Papers/具身智能/Improving_Robotic_Imitation_Learning_via_Trajectory_Standardization|Improving Robotic Imitation Learning via Trajectory Standardization]]

![[assets/2606.22907_figure.png|800]]

- **arXiv**: [2606.22907](https://arxiv.org/abs/2606.22907)
- **PDF**: https://arxiv.org/pdf/2606.22907
- **详细分析**: [[20_Research/Papers/具身智能/Improving_Robotic_Imitation_Learning_via_Trajectory_Standardization|Improving Robotic Imitation Learning via Trajectory Standardization]]
- **作者**: Licheng Yang, Lingfeng Qian, Fei Zheng, Yonghao He, Wei Sui, Shuangshuang Li, Hu Su
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Improving Robotic Imitation Learning via Trajectory Standardization》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning for robotic manipulation relies on large sets of human demonstration trajectories, which are often noisy and temporally irregular due to variable operator speed, intermittent pauses, and inconsistent action density. A common preprocessing strategy is time-uniform downsampling to shorten sequences, but it cannot effectively remove speed-induced non-uniformity or redundant pauses. This mismatch degrades data quality and hinders policy learning. To address this issue, we propose Information-Standardized Trajectory Resampling (ISR), an offline preprocessing method for effective imitation learning. ISR resamples each trajectory by enforcing approximately equal information distance between adjacent points. Specifically, we map trajectories onto an information-modulated Riemannian manifold and perform geodesic-equidistant parameterization. We construct an information-intensity field from velocity and acceleration norms: the velocity term removes small-motion redundancy, while the acceleration term preserves high-curvature and fine-manipulation phases. We evaluate ISR on three real-world manipulation tasks with mainstream imitation learning policies. Compared with the baseline time-uniform 3x downsampling, ISR improves task success rates by about 25%, remains robust across datasets collected from different operators, and reduces both dataset size and training cost. The code and videos are publicly available at https://d-robotics-ai-lab.github.io/isr.page.

</details>

---

### [[20_Research/Papers/具身智能/HERCULES_An_Open-Source_Simulation_Framework_for_Heterogeneous_Multi-Robot_SLAM,_Collaborative_Perception,_and_Exploration|HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration]]

![[assets/2606.22756_figure.jpg|800]]

- **arXiv**: [2606.22756](https://arxiv.org/abs/2606.22756)
- **PDF**: https://arxiv.org/pdf/2606.22756
- **详细分析**: [[20_Research/Papers/具身智能/HERCULES_An_Open-Source_Simulation_Framework_for_Heterogeneous_Multi-Robot_SLAM,_Collaborative_Perception,_and_Exploration|HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration]]
- **作者**: Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.9（加权：具身智能 0.3，大模型 0.1，机器人 2.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AirSim, Cosys-AirSim, FastSim, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present HERCULES, an open-source simulator and data-collection pipeline for heterogeneous multi-robot autonomy. Built upon the Unreal Engine 5 (UE5)-based simulators AirSim and Cosys-AirSim, HERCULES resolves key architectural limitations of prior frameworks to enable concurrent unmanned aerial and ground vehicle (UAV-UGV) operation in large-scale, photorealistic, dynamic environments. It introduces a new waypoint-tracking UGV controller that mirrors existing UAV control interfaces, and provides a shared navigation stack for mapping, traversability analysis, planning, and control across heterogeneous platforms. Expanding inherited sensor suites, it adds physics-based long-wave infrared (LWIR) cameras and configurable night-vision modes for degraded visual environments. HERCULES provides lightweight APIs, ROS 2 wrappers, and rigorous time synchronization across sensors and platforms, and brings state-of-the-art game-engine capabilities into robotics simulation, integrating intelligent agents such as pedestrians, traffic, and wildlife with high-fidelity dynamic phenomena, including fire, flooding, and crop disease spread. HERCULES runs in two modes: passively, replaying offline-designed trajectories to generate reproducible multi-modal datasets, and actively, running an online planner in closed loop from live observations. Our experiments in heterogeneous multi-robot SLAM, collaborative perception, and exploration, using both HERCULES-generated data and active closed-loop execution, demonstrate its utility for advancing heterogeneous multi-robot autonomy. We publicly release our source code, experiment code, documentation, and datasets, including a heterogeneous multi-robot SLAM benchmark collected with two UAVs and two UGVs across kilometer-scale desert, forest, and city environments, at https://lunarlab-gatech.github.io/HERCULES-website.

</details>

---

### [[20_Research/Papers/具身智能/PolicyTrim_Boosting_Intrinsic_Policy_Efficiency_of_Vision-Language-Action_Models|PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models]]

![[assets/2606.22540_figure.png|800]]

- **arXiv**: [2606.22540](https://arxiv.org/abs/2606.22540)
- **PDF**: https://arxiv.org/pdf/2606.22540
- **详细分析**: [[20_Research/Papers/具身智能/PolicyTrim_Boosting_Intrinsic_Policy_Efficiency_of_Vision-Language-Action_Models|PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models]]
- **作者**: Xianghui Wang, Feng Chen, Wenbo Zhang, Hua Yan, Zixuan Wang, Changsheng Li, Yinjie Lei
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.8，强化学习 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency. While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic \textbf{policy efficiency} of these models remains largely unexplored. Policy efficiency is fundamentally affected by two factors, namely the effective executable length of predicted action chunks and the total physical steps required to complete a task. These two factors jointly determine the total number of forward inference calls during execution. We observe that current VLA policies struggle with planning unreliability and action redundancy, suffering from severe prediction degradation at the tail of action chunks and tending to generate unnecessarily redundant physical steps. To address this, we propose \textbf{PolicyTrim}, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps. For reliable chunk extension, we employ a dynamic exploration strategy that explicitly rewards the successful completion of longer executable lengths, progressively pushing the trustworthy prediction horizon to its empirical limit. For step efficiency, we design a redundancy-aware reward that directly favors successful task completions with fewer steps while penalizing unreproducible shortcuts, effectively eliminating redundant physical actions. Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%. Ultimately, our framework delivers up to a 5.83$\times$ end-to-end deployment speedup without compromising task success rates.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedUS-FS_Fast_Slow_Intelligence_for_Ultrasound_Robotics|EmbodiedUS-FS: Fast Slow Intelligence for Ultrasound Robotics]]

![[assets/2606.22319_figure.png|800]]

- **arXiv**: [2606.22319](https://arxiv.org/abs/2606.22319)
- **PDF**: https://arxiv.org/pdf/2606.22319
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedUS-FS_Fast_Slow_Intelligence_for_Ultrasound_Robotics|EmbodiedUS-FS: Fast Slow Intelligence for Ultrasound Robotics]]
- **作者**: Fangzhuo Zhang, Xinyu Wang, Xiao Yang, Jinchang Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《EmbodiedUS-FS: Fast Slow Intelligence for Ultrasound Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic ultrasound scanning in real clinical environments requires both high-level clinical workflow reasoning and low-level closed-loop execution. Physicians natural-language instructions often contain implicit anatomical targets, procedural logic, image-quality requirements, and safety constraints, while execution is affected by patient motion, contact variations, and target drift. We propose a fast and slow hierarchical embodied ultrasound system for safe and interpretable robotic ultrasound assistance. The Slow Brain performs intent parsing and stage-wise task planning with knowledge augmentation from an API and handbook corpus, and generates executable plans through task-graph construction and structured plan verification. The Fast Brain fuses multimodal feedback, including ultrasound images, robot pose and force states, and patient-motion information, to refine local actions and perform image-quality-guided recovery behaviors. The system further integrates a Safety Shield and a hierarchical escalation policy to constrain risky actions and trigger replanning or human confirmation under persistent failures or safety-bound violations. Experiments on planning evaluation, closed-loop execution under dynamic perturbations, and safety-mechanism validation demonstrate that the proposed hierarchical design improves task success rates while reducing safety violations.

</details>

---

### [[20_Research/Papers/具身智能/Semi-Supervised_Vision-Language-Action_Model|Semi-Supervised Vision-Language-Action Model]]

![[assets/2606.21493_figure.png|800]]

- **arXiv**: [2606.21493](https://arxiv.org/abs/2606.21493)
- **PDF**: https://arxiv.org/pdf/2606.21493
- **详细分析**: [[20_Research/Papers/具身智能/Semi-Supervised_Vision-Language-Action_Model|Semi-Supervised Vision-Language-Action Model]]
- **作者**: Hongyang He, Jiuming Liu, Victor Sanchez
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.8，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Semi-Supervised Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, SemiVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable robots to predict actions directly from visual observations and language instructions, but adapting them to new environments still depends on costly action-labeled demonstrations. To reduce this dependence, we study semi-supervised VLA adaptation under limited supervision signals, where only a small portion of trajectories contain robot actions and the remaining trajectories provide action-unlabeled vision-language observations. Unlike standard semi-supervised learning, the missing supervision is an embodied action signal that must be visually grounded, language-consistent, physically feasible, and temporally stable. To address this problem, we propose SemiVLA, a self-distilled teacher-student framework that learns from reliable pseudo-actions on unlabeled trajectories. SemiVLA introduces a VLA-specific reliability controller to assess vision-language alignment, action feasibility, and temporal transition consistency, and further updates the teacher through a Bottleneck-Projected Alignment Update to avoid noisy feedback contamination. With OpenVLA as the backbone, SemiVLA consistently improves multiple PEFT strategies across LIBERO and CALVIN. Under 10\% labeled trajectories, SemiVLA with Selective LoRA achieves 89.0\% average success on LIBERO, outperforming supervised LoRA by 8.0 points without extra inference cost.

</details>

---

### [[20_Research/Papers/具身智能/ASCII_Art_Turns_LLMs_into_VLA_Controllers|ASCII Art Turns LLMs into VLA Controllers]]

![[assets/2606.21470_figure.png|800]]

- **arXiv**: [2606.21470](https://arxiv.org/abs/2606.21470)
- **PDF**: https://arxiv.org/pdf/2606.21470
- **详细分析**: [[20_Research/Papers/具身智能/ASCII_Art_Turns_LLMs_into_VLA_Controllers|ASCII Art Turns LLMs into VLA Controllers]]
- **作者**: Yitao Jiang, Roy Xing, Luyang Zhao, Brian Plancher, Muhao Chen, Devin Balkcom
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《ASCII Art Turns LLMs into VLA Controllers》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ASCIIBench, ASCIIEval, CoT-VLA, NanoVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision--Language--Action (VLA) controllers are often built by extending vision--language models (VLMs) with action supervision, relying on multimodal backbones with large data and compute requirements. We demonstrate that a text-only large language model (LLM) can be adapted into a VLA-style controller when visual observations are rendered into a text input using an ASCII representation. This ASCII-as-vision interface enables existing training and deployment stacks for LLMs to efficiently condition on visual state, follow natural-language instructions, and produce constrained, executable actions. We fine-tune and compare multiple LLMs and VLMs across model families and scales, using both expert demonstrations from a planning-based teacher, as well as DAgger for iterative improvement. In a 2D manipulation benchmark, in both simulation and on a physical manipulator, the resulting controllers can identify task-relevant entities and plan feasible action sequences. Our results suggest that ASCII rendering can serve as a lightweight, interpretable modality bridge from images to text, complementing conventional VLA pipelines, and opening directions for VLA research with text-only backbones.

</details>

---

### [[20_Research/Papers/具身智能/Robot_Self-Improvement_via_Human-Video_Dynamics_Models|Robot Self-Improvement via Human-Video Dynamics Models]]

![[assets/2606.21406_figure.png|800]]

- **arXiv**: [2606.21406](https://arxiv.org/abs/2606.21406)
- **PDF**: https://arxiv.org/pdf/2606.21406
- **详细分析**: [[20_Research/Papers/具身智能/Robot_Self-Improvement_via_Human-Video_Dynamics_Models|Robot Self-Improvement via Human-Video Dynamics Models]]
- **作者**: Hanzhi Chen, Anran Zhang, Simon Schaefer, Kejia Chen, Shi Chen, Daniel Cremers, Oier Mees, Stefan Leutenegger
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Robot Self-Improvement via Human-Video Dynamics Models》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CFGRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A central question in robot learning is how to acquire skills from the kinds of data that humans learn from: passive observation, embodied practice, and the experience of failure. Human videos provide the first of these in abundance, and prior work has shown they can initialize useful policies. Far less clear is whether they can support the second and third: whether priors extracted from human videos can ground a robot's own attempts well enough to evaluate them, correct them, and improve from them. In this work, we show that human videos can be used to learn embodiment-agnostic action, dynamics, and value representations that transfer across robot embodiments, providing the predictive foundation required for robots to autonomously improve from their own rollouts and failures. We introduce Dynamics-Guided Action Correction (DGAC), a training-free approach that leverages these adapted models to repair failed states: each failure becomes a query for which the learned models propose and rank corrective actions, turning failures into supervision for the next policy update. Across seven real-world manipulation tasks spanning both a mobile manipulator and a static manipulator arm, our approach improves success rates from 40% to 81% across multiple policy backbones, demonstrating cross-embodiment robot self-improvement from human-video priors. These results show that human priors and robot failures can be combined to enable scalable autonomous policy improvement. Project page: https://ethz-mrl.github.io/robot-self-improvement-website/.

</details>

---

### [[20_Research/Papers/具身智能/VLA-FAIL_Efficient_Task_Failure_Detection_for_Finetuned_Vision-Language-Action_Models|VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models]]

![[assets/2606.21386_first_page.png|800]]

- **arXiv**: [2606.21386](https://arxiv.org/abs/2606.21386)
- **PDF**: https://arxiv.org/pdf/2606.21386
- **详细分析**: [[20_Research/Papers/具身智能/VLA-FAIL_Efficient_Task_Failure_Detection_for_Finetuned_Vision-Language-Action_Models|VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models]]
- **作者**: Florian Seligmann, Emiliyan Gospodinov, Enes Ulas Dincer, Gerhard Neumann
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 2.7，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) achieve state-of-the-art performance on many robotic manipulation tasks, yet they can still behave unpredictably in out-of-distribution scenarios. Runtime failure detection is therefore essential for the safe real-world deployment of VLAs. However, existing task failure detectors require computationally expensive action sampling, are based on architectural assumptions that limit their applicability to VLAs, or need access to failure rollouts. We propose VLA-FAIL, a lightweight and broadly applicable failure detection framework for VLAs that combines two novel failure detectors with minimal overhead, without requiring failure data. The first, last-layer Mahalanobis distance (LLMD), detects out-of-distribution states by measuring token-wise deviations in last-layer features relative to the training data. The second, action chunk consistency (ACC), exploits the temporal overlap induced by receding-horizon control and detects failures when consecutive action chunks become inconsistent. To capture the trade-off between detection accuracy and detection latency, we introduce AUCPDT, a threshold-independent metric that jointly evaluates precision, recall, and detection time. Through extensive real-world and simulation experiments, we demonstrate that LLMD and ACC capture complementary failure modes whose combination enables reliable and early failure detection across diverse tasks, frequently outperforming significantly more expensive baseline methods.

</details>

---
