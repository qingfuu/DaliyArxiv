# cs.RO | Robotics | 2026-05-22

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/强化学习/N3P_Accelerated_Automated_Parking_via_a_Learning-Based_Naturalistic_Three-Stage_Scheme|N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme]]

![[assets/2605.22722_figure.png|800]]

- **arXiv**: [2605.22722](https://arxiv.org/abs/2605.22722)
- **PDF**: https://arxiv.org/pdf/2605.22722
- **详细分析**: [[20_Research/Papers/强化学习/N3P_Accelerated_Automated_Parking_via_a_Learning-Based_Naturalistic_Three-Stage_Scheme|N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme]]
- **作者**: Yifan Xue, Toktam Mohammadnejad, Faizan M Tariq, Sangjae Bae, David Isele, Yosuke Sakamoto, Nadia Figueroa, Jovin D'sa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《N3P: Accelerated Automated Parking via a Learning-Based Naturalistic Three-Stage Scheme》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous parking requires efficient path planning that ensures kinematic feasibility and collision avoidance in constrained environments. Hybrid A* is widely used but computationally expensive, while reinforcement learning (RL) methods lack reliability and often struggle with long-horizon geometric constraints, leading to suboptimal trajectories. We present N3P, a fast learning-based three-stage framework for automated parking. By introducing an intermediate preparatory pose and using a learning module to predict it, N3P decomposes the maneuver into simpler subproblems, thereby reducing computational complexity and accelerating path generation. We validate the framework by integrating it with Hybrid A* algorithms. Experiments in perpendicular and parallel parking scenarios show that N3P-enhanced Hybrid A* speeds up planning by more than 80%. It also outperforms RL baselines in success rate and trajectory quality, producing shorter trajectories with fewer gear changes, while achieving comparable or lower planning time in most cases.

</details>

---

### [[20_Research/Papers/机器人/TriSweep_A_Four-Drone_Swarm_Framework_for_Electromagnetic_Side-Channel_Analysis|TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis]]

![[assets/2605.22709_figure.png|800]]

- **arXiv**: [2605.22709](https://arxiv.org/abs/2605.22709)
- **PDF**: https://arxiv.org/pdf/2605.22709
- **详细分析**: [[20_Research/Papers/机器人/TriSweep_A_Four-Drone_Swarm_Framework_for_Electromagnetic_Side-Channel_Analysis|TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis]]
- **作者**: Eric Yocam, Varghese Vaidyan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《TriSweep: A Four-Drone Swarm Framework for Electromagnetic Side-Channel Analysis》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Electromagnetic (EM) side-channel analysis traditionally assumes a stationary, close-proximity probe - a threat model that underestimates aerial adversaries. TriSweep is a simulation framework that designs and evaluates a four-drone swarm architecture for autonomous standoff EM-SCA of embedded microcontrollers at 0.25-1.5 m. Three spatially specialized collector drones - Anchor (full-spectrum), Mask Probe (mask-register loading leakage), and Cipher Probe (masked SubBytes output leakage) - feed a stationary Accumulator drone that performs coherent combining (+4.8 dB SNR gain) and second-order mask cancellation via a centered product of the two spatially separated leakage streams. Evaluated against three real ANSSI ASCAD datasets (ATmega8515 masked AES-128 and 50/100-sample desynchronized variants), the framework achieves a simulated key rank of 18 +/- 1.7 (five-seed) at 0.25 m on the primary masked dataset. Profiling-trace cross-correlation alignment reduces single-drone rank from 89 to 21 on the 100-sample-jitter variant, demonstrating compensation for drone hover vibration. A two-channel CNN in the Accumulator converges to a loss of 0.454 (vs. random baseline 5.545) and improves rank on desynchronized datasets. No physical hardware has been fabricated; prototype construction is the planned next step.

</details>

---

### [[20_Research/Papers/机器人/Symmetries_Here_and_There,_Combined_Everywhere_Cross-space_Symmetry_Compositions_in_Robotics|Symmetries Here and There, Combined Everywhere: Cross-space Symmetry Compositions in Robotics]]

![[assets/2605.22639_figure.png|800]]

- **arXiv**: [2605.22639](https://arxiv.org/abs/2605.22639)
- **PDF**: https://arxiv.org/pdf/2605.22639
- **详细分析**: [[20_Research/Papers/机器人/Symmetries_Here_and_There,_Combined_Everywhere_Cross-space_Symmetry_Compositions_in_Robotics|Symmetries Here and There, Combined Everywhere: Cross-space Symmetry Compositions in Robotics]]
- **作者**: Loizos Hadjiloizou, Rodrigo Pérez-Dattari, Noémie Jaquier
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Symmetries Here and There, Combined Everywhere: Cross-space Symmetry Compositions in Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots exhibit a rich variety of symmetries arising from their mechanical structure and the properties of their tasks. Although many robotics problems exhibit several symmetries simultaneously, existing approaches typically treat them in isolation, failing to exploit their combined potential. This paper introduces cross-space symmetry compositions, a framework for learning robot policies that are jointly equivariant to multiple symmetries across configuration and task spaces. Leveraging the differential-geometric structure of the forward kinematics map, we both descend symmetries from configuration to task space and lift symmetries from task to configuration space, enabling their composition within a unified representation space. We validate our framework on simulated and real-world experiments on a dual-arm robot, demonstrating that jointly leveraging multiple symmetries yields improved generalization.

</details>

---

### [[20_Research/Papers/机器人/SE3Kit_A_Lightweight_Python_Library_for_Specialized_Geometric_Primitives_in_Robotics|SE3Kit: A Lightweight Python Library for Specialized Geometric Primitives in Robotics]]

![[assets/2605.22633_first_page.png|800]]

- **arXiv**: [2605.22633](https://arxiv.org/abs/2605.22633)
- **PDF**: https://arxiv.org/pdf/2605.22633
- **详细分析**: [[20_Research/Papers/机器人/SE3Kit_A_Lightweight_Python_Library_for_Specialized_Geometric_Primitives_in_Robotics|SE3Kit: A Lightweight Python Library for Specialized Geometric Primitives in Robotics]]
- **作者**: Daniyal Maroufi, Omid Rezayof, Farshid Alambeigi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《SE3Kit: A Lightweight Python Library for Specialized Geometric Primitives in Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Python robotics ecosystem faces a challenge: while many libraries exist for rigid body transformations, few are both lightweight and mathematically strict. This paper introduces SE3Kit, a lightweight Python library efficient operations on the Special Euclidean Group SE(3) and the Special Orthogonal Group SO(3). Unlike established frameworks that require heavy dependencies (e.g., SpatialMath, PyPose) or general tools that lack robotics-specific features (e.g., SciPy), SE3Kit targets the gap between these extremes. It is designed for embedded deployment, rapid prototyping, and education while providing rigorous mathematical implementation. It provides a pure-Python, NumPy-only implementation of Lie Group operations, without the overhead of deep learning or other visualization software.

</details>

---

### [[20_Research/Papers/机器人/Branch-Stochastic_Model_Predictive_Control_for_Motion_Planning_under_Multi-Modal_Uncertainty_with_Scenario_Clustering|Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering]]

![[assets/2605.22600_first_page.png|800]]

- **arXiv**: [2605.22600](https://arxiv.org/abs/2605.22600)
- **PDF**: https://arxiv.org/pdf/2605.22600
- **详细分析**: [[20_Research/Papers/机器人/Branch-Stochastic_Model_Predictive_Control_for_Motion_Planning_under_Multi-Modal_Uncertainty_with_Scenario_Clustering|Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering]]
- **作者**: Zekun Xing, Ramkrishna Chaudhari, Marion Leibold, Dirk Wollherr, Martin Buss
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Branch-Stochastic Model Predictive Control for Motion Planning under Multi-Modal Uncertainty with Scenario Clustering》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning for autonomous driving must account for multi-modal uncertainty in both the intentions and trajectories of surrounding vehicles. Handling uncertainty in a worst-case manner guarantees robustness but often leads to excessive conservatism. Stochastic Model Predictive Control (SMPC) reduces trajectory-level conservatism through chance constraints, yet remains conservative with respect to intention uncertainty since constraints must hold across all intentions. We present a novel combination of SMPC and the branching structure, enabling the planner to generate distinct trajectories for different possible intentions while maintaining safety under trajectory uncertainty. A novel scenario clustering is proposed to merge prediction scenarios based on high-level decision similarity, thereby ensuring real-time tractability. Furthermore, an adaptive branching-time computation postpones commitment to separate plans until intention uncertainty is sufficiently reduced. Simulation studies in challenging highway scenarios demonstrate that the proposed method improves safety, reduces conservatism, and achieves real-time computational performance.

</details>

---

### [[20_Research/Papers/机器人/Quantifying_Full-Body_Immersion|Quantifying Full-Body Immersion]]

![[assets/2605.22521_figure.png|800]]

- **arXiv**: [2605.22521](https://arxiv.org/abs/2605.22521)
- **PDF**: https://arxiv.org/pdf/2605.22521
- **详细分析**: [[20_Research/Papers/机器人/Quantifying_Full-Body_Immersion|Quantifying Full-Body Immersion]]
- **作者**: Alihan Bakir, Ekrem Yüksel, Fabio Zuliani, Neil Chennoufi, Francesco Bruno, Jamie Paik
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Quantifying Full-Body Immersion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanity is at the forefront of yet another digital revolution, where the lines between real and virtual worlds are dissolving, reshaping how we perceive and interact with our surroundings. In this context, we introduce a transformative paradigm for immersive virtual experiences centered around whole-body kinetic interactions. Our approach redefines immersion through three distinct levels: audio-visual immersion, capturing sensory realism; physical immersion, delivering haptic feedback; and full-body immersion (FBI), where dynamic bodily interaction integrates seamlessly with virtual environments. At the core of this innovation lies a scalable, distributable platform based on modular robotic surface units inspired by the adaptive designs of nature. These units enable the rendering of immersive environments at any scale, from intimate personal experiences to expansive multi-user settings, dynamically adapting to interactions in real-time. The modular system distributes force, shape, and motion feedback throughout entire spaces, replicating the physical characteristics of the environment and enabling new depth of engagement through FBI. By combining scalability, adaptability, and dynamic physical engagement, this framework bridges the gap between real and virtual worlds. It offers an unprecedented level of immersion where users can engage their entire bodies in symbiotic interactions with the virtual space. This work not only advances immersive technology but also redefines how humans and virtual environments coexist, setting a foundation for a new era of human-environment synthesis.

</details>

---

### [[20_Research/Papers/机器人/Terminal_Constraint_Model_Predictive_Control_for_Image-Based_Visual_Servoing_of_UAVs_with_Kalman_Filter-Based_Moment_Loss_Compensation|Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation]]

![[assets/2605.22443_figure.png|800]]

- **arXiv**: [2605.22443](https://arxiv.org/abs/2605.22443)
- **PDF**: https://arxiv.org/pdf/2605.22443
- **详细分析**: [[20_Research/Papers/机器人/Terminal_Constraint_Model_Predictive_Control_for_Image-Based_Visual_Servoing_of_UAVs_with_Kalman_Filter-Based_Moment_Loss_Compensation|Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation]]
- **作者**: X. Wang, Y. Cao, W. L. W. Leong, Y. R. Tan, S. Huang, S. H. R. Teo, C. Xiang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Terminal Constraint Model Predictive Control for Image-Based Visual Servoing of UAVs with Kalman Filter-Based Moment Loss Compensation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Image-Based Visual Servoing (IBVS) provides an efficient vision-guided control paradigm for unmanned aerial vehicles (UAVs) by directly regulating image-space errors. However, conventional IBVS controllers are vulnerable to two critical issues: loss of closed-loop stability near the target due to input and state constraints, and control failure caused by intermittent loss of moment-based visual features under aggressive motion. To address these challenges, this paper proposes a terminal-constraint model predictive control (TC-MPC) framework for IBVS, integrated with a Kalman filter (KF)-based state-prediction mechanism. The TC-MPC explicitly incorporates terminal-state constraints and a terminal cost into the IBVS error dynamics, ensuring recursive feasibility, improved convergence behavior, and closed-loop stability under control and state constraints. In parallel, the Kalman filter predicts the temporal evolution of image moments during short-term visual degradation, enabling the controller to preserve control continuity when moment measurements are partially unavailable. The proposed approach is validated through real-time UAV visual servoing experiments.

</details>

---

### [[20_Research/Papers/具身智能/How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery|How can reasoning capability empower the AI copilot robot in endoscopic surgery]]

![[assets/2605.22322_figure.png|800]]

- **arXiv**: [2605.22322](https://arxiv.org/abs/2605.22322)
- **PDF**: https://arxiv.org/pdf/2605.22322
- **详细分析**: [[20_Research/Papers/具身智能/How_can_reasoning_capability_empower_the_AI_copilot_robot_in_endoscopic_surgery|How can reasoning capability empower the AI copilot robot in endoscopic surgery]]
- **作者**: Guankun Wang, Long Bai, Hongliang Ren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《How can reasoning capability empower the AI copilot robot in endoscopic surgery》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning capability has significantly advanced complex logical inference and robotic decision-making in general domains. However, its potential in the Artificial Intelligence (AI) copilot robot-particularly implemented based on the Vision-Language-Action (VLA) model-remains unexplored in endoscopic surgery. Effective reasoning should enable AI copilot robots to integrate multimodal cues, interpret surgical intent, and infer hidden tissue dynamics, thereby alleviating intraoperative uncertainty and cognitive burden on surgeons. Properly implemented, reasoning-driven autonomy can transform AI copilot robots from reactive executors into cognitive collaborators, enhancing precision, safety, and sustainability in clinical practice.

</details>

---

### [[20_Research/Papers/具身智能/Spatial_Memory_for_Out-of-Vision_Manipulation_in_Vision-Language-Action|Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action]]

![[assets/2605.22283_figure.png|800]]

- **arXiv**: [2605.22283](https://arxiv.org/abs/2605.22283)
- **PDF**: https://arxiv.org/pdf/2605.22283
- **详细分析**: [[20_Research/Papers/具身智能/Spatial_Memory_for_Out-of-Vision_Manipulation_in_Vision-Language-Action|Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action]]
- **作者**: Pengteng Li, Weiyu Guo, He Zhang, Tiefu Cai, Xiao He, Yandong Guo, Hui Xiong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of view. SOMA addresses this limitation by equipping VLAs with a persistent spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond the current visual frustum. The framework consists of three components: Spatial Memory Construction, which aggregates angular-wise observations into a unified spatial-semantic representation through scanning; Dynamic Memory Refinement, which maintains global consistency over time; and Contextual Memory Retrieval, which activates instruction-relevant spatial cues during manipulation. We evaluate SOMA on five challenging real-world out-of-vision manipulation tasks, including multi-step and dual-arm scenarios where target objects are initially invisible. Experimental results show that SOMA not only improves task success rates, but also induces qualitatively different manipulation behaviors, with faster target localization, reduced viewpoint search, and near one-shot grasping under partial observability. Additional experiments on RoboCasa GR1 and SimplerEnv further validate the effectiveness of SOMA's memory design under conventional fully observable settings. Code will be released soon.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Pixels_Learning_Invariant_Rewards_for_Real-World_Robotics_From_a_Few_Demonstrations|Beyond Pixels: Learning Invariant Rewards for Real-World Robotics From a Few Demonstrations]]

![[assets/2605.22123_figure.png|800]]

- **arXiv**: [2605.22123](https://arxiv.org/abs/2605.22123)
- **PDF**: https://arxiv.org/pdf/2605.22123
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Pixels_Learning_Invariant_Rewards_for_Real-World_Robotics_From_a_Few_Demonstrations|Beyond Pixels: Learning Invariant Rewards for Real-World Robotics From a Few Demonstrations]]
- **作者**: Tengye Xu, Yangting Sun, Ziju Shen, Guanqi Chen, Zhen Fu, Chen yizhou, Hua Chen, Jia Pan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Beyond Pixels: Learning Invariant Rewards for Real-World Robotics From a Few Demonstrations》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GENFLOWRL, IRL, Meta-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing reward functions that generalize beyond controlled laboratory settings remains a fundamental challenge in reinforcement learning for robotics. In open-world manipulation problems, a single task can appear in numerous variants through different object instances, positions, and camera viewpoints. Recent vision-based reward models tend to memorize specific pixel distributions and fail to generalize beyond their training conditions. To address this, we propose a framework that learns invariant symbolic reward functions from as few as five demonstrations. The insight is to shift from visual feature-fitting to the discovery of behavioral invariants: task-level properties that remain constant across diverse visual instantiations. The framework has two coupled components: a structural reward formulation that encodes task-level strategies and physical constraints while preserving optimal policy invariance, and a hybrid symbolic-numerical procedure that distills these invariants from demonstrations without online interaction. Experiments on eight Meta-World tasks and three Franka manipulation tasks demonstrate that our method achieves stronger process alignment and policy rollout ranking abilities compared to baselines, accelerating downstream policy learning. Three real-world out-of-distribution experiments further show that the same learned reward generalizes zero-shot to position, viewpoint, and object variations, enabling a single reward representation to be reused across diverse task variants in practice.

</details>

---

### [[20_Research/Papers/机器人/Industrial_Dual-Arm_Box_Handling_via_Online_Inertial_Estimation_and_Convex_Wrench_Optimization|Industrial Dual-Arm Box Handling via Online Inertial Estimation and Convex Wrench Optimization]]

![[assets/2605.22021_figure.png|800]]

- **arXiv**: [2605.22021](https://arxiv.org/abs/2605.22021)
- **PDF**: https://arxiv.org/pdf/2605.22021
- **详细分析**: [[20_Research/Papers/机器人/Industrial_Dual-Arm_Box_Handling_via_Online_Inertial_Estimation_and_Convex_Wrench_Optimization|Industrial Dual-Arm Box Handling via Online Inertial Estimation and Convex Wrench Optimization]]
- **作者**: Kenzhi Iskandar Wong, Lin Yang, Qian Ying Lee, Domenico Campolo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Industrial Dual-Arm Box Handling via Online Inertial Estimation and Convex Wrench Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial robotic object handling often involves boxes and packages whose mass and center of mass are not known in advance. These uncertainties affect the force--moment balance required for stable lifting, and improper regulation of contact wrenches can lead to slip, object drop, orientation deviation, or excessive squeezing. This paper presents a friction-aware dual-arm box-handling framework for objects with unknown inertial properties. The proposed approach estimates the object mass and center of mass online from measured contact wrenches, and computes friction-feasible contact forces and torsional moments through a second-order cone program (SOCP) under ellipsoidal friction-limit-surface constraints. An offline trajectory refinement stage is also included to reduce undesired object--environment contact when geometric constraints are present. By enforcing friction feasibility as a hard constraint and minimizing contact effort within the feasible region, the framework achieves stable lifting without treating slip avoidance and excessive squeezing as separately tuned objectives. Experiments on a real dual-arm robotic system under different center-of-mass configurations demonstrate that the method lifts objects with unknown inertial properties while maintaining stable frictional contact.

</details>

---

### [[20_Research/Papers/具身智能/TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation|TacO: Benchmarking Tactile Sensors for Object Manipulation]]

![[assets/2605.21976_figure.png|800]]

- **arXiv**: [2605.21976](https://arxiv.org/abs/2605.21976)
- **PDF**: https://arxiv.org/pdf/2605.21976
- **详细分析**: [[20_Research/Papers/具身智能/TacO_Benchmarking_Tactile_Sensors_for_Object_Manipulation|TacO: Benchmarking Tactile Sensors for Object Manipulation]]
- **作者**: Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, Alexiy Buynitsky, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TacO: Benchmarking Tactile Sensors for Object Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based learning from demonstrations has achieved remarkable success in enabling robots to perform manipulation tasks and high-level semantic reasoning, yet it remains insufficient for complex, contact-rich manipulation. While there is broad agreement that tactile sensing improves manipulation, there is no empirical guidance on which tactile sensors are best suited for which manipulation tasks. In this paper, we provide a systematic, task-driven evaluation of tactile sensors for robot manipulation and propose a framework for selecting and evaluating sensors based on manipulation policy performance. Separate manipulation policies are trained for tactile sensors of four distinct modalities: visual, acoustic, magnetic, and resistive, across three tasks: pick-and-place with unknown mass, object reorientation, and plug insertion. For each task, an analysis of how sensor properties such as spatial resolution, shear sensing, and tactile representation, and the inherent material friction affect task performances is done. Rather than tactile sensing being universally beneficial in the same way, our results show that the usefulness of tactile information depends strongly on sensor modality, material properties, and the specific manipulation tasks. All of the tactile sensors, code, data, and hardware setup will be publicly available on the project website.

</details>

---

### [[20_Research/Papers/机器人/A_Visitation_Grid_for_Complete_Coverage_Foraging_in_Robot_Swarms|A Visitation Grid for Complete Coverage Foraging in Robot Swarms]]

![[assets/2605.21947_figure.jpg|800]]

- **arXiv**: [2605.21947](https://arxiv.org/abs/2605.21947)
- **PDF**: https://arxiv.org/pdf/2605.21947
- **详细分析**: [[20_Research/Papers/机器人/A_Visitation_Grid_for_Complete_Coverage_Foraging_in_Robot_Swarms|A Visitation Grid for Complete Coverage Foraging in Robot Swarms]]
- **作者**: Qi Arturo Gonzalez, Yifeng Gao, Li Zhang, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Visitation Grid for Complete Coverage Foraging in Robot Swarms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The complete collection of sparse resources in large, unknown environments remains a challenging problem for autonomous robot swarms. Previous studies have shown that a substantial portion of total mission time is consumed during the final stage of collection, where only a small fraction of randomly scattered resources remain. Consequently, many existing swarm foraging algorithms (search and collection) focus on collecting most resources within a limited time window, rather than improving end-stage efficiency for collecting all resources. We propose a grid-based stochastic foraging strategy that explicitly reduces redundant visits and accelerates late-stage collection. The unknown search area is partitioned into a grid map, which is maintained by a lightweight central server. To maintain scalability, both robots and the server operate within limited memory and computational constraints. The server updates the grid-level visitation counts based on robot-reported locations, producing a global estimate of the exploration density. For each new foraging trip, a robot selects its next search area from a local 3 X 3 neighborhood of grids probabilistically with the lowest visitation count, thus biasing exploration toward under-visited regions while maintaining stochasticity. Extensive simulation experiments demonstrate that the proposed strategy consistently outperforms the canonical centrally placed baseline foraging algorithm (CPFA). Compared to CPFA, the proposed method reduces the total collection time by up to 33% and improves collection efficiency by more than 48% during the final stage of the mission. These results indicate that the proposed strategy is robust, flexible, and scalable for near-complete and complete resource collection in robot swarms and can serve as a general enhancement for stochastic swarm foraging methods under limited onboard resources.

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Evolve_Multi-modal_Interactive_Fields_for_Robust_Humanoid_Navigation_in_Dynamic_Environments|Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments]]

![[assets/2605.21935_figure.png|800]]

- **arXiv**: [2605.21935](https://arxiv.org/abs/2605.21935)
- **PDF**: https://arxiv.org/pdf/2605.21935
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Evolve_Multi-modal_Interactive_Fields_for_Robust_Humanoid_Navigation_in_Dynamic_Environments|Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments]]
- **作者**: Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AtlasNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe manipulation-oriented navigation for humanoid robots requires scene memory that remains reliable under locomotion-induced perceptual distortion, environmental changes, and interaction-level geometric safety constraints. Existing semantic mapping and scene-graph systems are difficult to deploy directly in this setting because they often assume stable camera trajectories, static environments, or coarse object geometry. We introduce the Multi-modal Interactive Field (MIF), a humanoid-oriented system that integrates confidence-aware semantic 3D Gaussian Splatting, discrepancy-triggered spatial memory updates, and task-driven geometric reconstruction within a closed-loop perception-adaptation pipeline. MIF couples three fields: an uncertainty-aware 3DGS Appearance Field that suppresses gait-induced blur, a Spatial Field that maintains topological memory, and a Geometry Field that supports Interaction Pose Safety (IPS) before manipulation. A discrepancy detection score is introduced to separate locomotion-induced false-positive changes from persistent changes and updates only locally inconsistent regions. On a Unitree-G1 humanoid in a real dynamic office, MIF improves relocation success in non-static environments from 12% to 94% compared with static scene-graph memory, while reducing semantic memory footprint by 91.4% through feature distillation for practical online operation. Project page and code: https://ziya-jiang.github.io/MIF-homepage/

</details>

---

### [[20_Research/Papers/强化学习/Auction-Consensus_Algorithm_with_Learned_Bidding_Scheme_for_Multi-Robot_Systems|Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems]]

![[assets/2605.21932_figure.png|800]]

- **arXiv**: [2605.21932](https://arxiv.org/abs/2605.21932)
- **PDF**: https://arxiv.org/pdf/2605.21932
- **详细分析**: [[20_Research/Papers/强化学习/Auction-Consensus_Algorithm_with_Learned_Bidding_Scheme_for_Multi-Robot_Systems|Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems]]
- **作者**: Jose Rodriguez, Constantine Tarawneh, Sven Koenig, Wenjie Dong, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.2，强化学习 0.4，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Auction-Consensus Algorithm with Learned Bidding Scheme for Multi-Robot Systems》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Robot Task Allocation (MRTA) is a central challenge in decentralized multi-agent systems, where teams of robots must cooperatively assign and execute tasks under limited communication while optimizing global performance objectives. Auction-consensus algorithms, such as the Consensus-Based Bundle Algorithm (CBBA), provide scalable decentralized coordination with provable convergence, but rely on hand-crafted greedy scoring functions that often lead to suboptimal task allocations. This paper proposes a learning-enhanced auction-consensus framework in which CBBA's deterministic bidding mechanism is replaced by a neural bidding policy trained using reinforcement learning. Under a centralized training and decentralized execution paradigm, agents learn to compute task bids from partial local observations while retaining the standard auction and consensus phases for decentralized coordination. The learned bidding policy is trained using Proximal Policy Optimization with rewards shaped by proximity to globally optimal solutions obtained via mixed-integer linear programming. Multiple neural architectures are evaluated, including a Neural Additive Model, the Long Short-Term Memory (LSTM) model, and the Set Transformer Model. Experimental results across varying swarm sizes demonstrate that learned bidding policies can improve solution quality over classical CBBA while preserving decentralized execution. The proposed approach highlights the effectiveness of integrating reinforcement learning with classical distributed coordination algorithms, offering a scalable pathway toward higher-quality decentralized multi-robot task allocation.

</details>

---

### [[20_Research/Papers/机器人/Non-Contact_Vibration-Based_Damage_Detection_of_Civil_Structures_Using_a_Cost-Effective_Autonomous_UAV|Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV]]

![[assets/2605.21914_figure.jpg|800]]

- **arXiv**: [2605.21914](https://arxiv.org/abs/2605.21914)
- **PDF**: https://arxiv.org/pdf/2605.21914
- **详细分析**: [[20_Research/Papers/机器人/Non-Contact_Vibration-Based_Damage_Detection_of_Civil_Structures_Using_a_Cost-Effective_Autonomous_UAV|Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV]]
- **作者**: Javier Becerril, Maximiliano Vargas, Jennifer Herrera, Joanna Gutierrez, Jorge Rios, Mohsen Amjadian, Constantine Tarawneh, Jinghao Yang, Qi Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Non-Contact Vibration-Based Damage Detection of Civil Structures Using a Cost-Effective Autonomous UAV》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a non-contact approach for vibration-based structural damage detection using an autonomous and customized cost-effective unmanned aerial vehicle (UAV). Vibration signals are extracted from video recordings through vision-based motion tracking to identify shifts in natural frequencies indicative of structural degradation. A laboratory-scale frame structure is evaluated under healthy and simulated-damage conditions. The proposed system is validated through an experimental study involving two smartphones, a USB camera, and a custom-built low-cost UAV equipped with an onboard camera and an autonomous alignment system for operation in GPS-denied environments. The displacement time is extracted and analyzed in the frequency domain and compared to reference measurements from contact accelerometers and a finite element model. Experimental results show that all platforms successfully capture the fundamental frequency and its shift due to damage. Although the UAV exhibits slightly higher errors (up to 5.7%) due to platform-induced disturbances and sensing limitations, it reliably detects damage-induced frequency changes. Compared to commercial UAV systems, the proposed platform achieves comparable inspection performance at significantly lower cost. These results demonstrate that low-cost autonomous UAVs provide a practical, flexible, and scalable solution for structural health monitoring, particularly in scenarios where contact-based sensing is impractical. The findings also support the potential for the deployment of multiple cooperative UAVs to further enhance inspection coverage and robustness.

</details>

---

### [[20_Research/Papers/机器人/Higher_Order_Reasoning_for_Collaborative_Communicationless_Mobile_Robot_Operations|Higher Order Reasoning for Collaborative Communicationless Mobile Robot Operations]]

![[assets/2605.21901_figure.png|800]]

- **arXiv**: [2605.21901](https://arxiv.org/abs/2605.21901)
- **PDF**: https://arxiv.org/pdf/2605.21901
- **详细分析**: [[20_Research/Papers/机器人/Higher_Order_Reasoning_for_Collaborative_Communicationless_Mobile_Robot_Operations|Higher Order Reasoning for Collaborative Communicationless Mobile Robot Operations]]
- **作者**: Jonathan Reasoner, Nicola Bezzo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Higher Order Reasoning for Collaborative Communicationless Mobile Robot Operations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In communicationless environments, multi-robot systems must operate without the constant information exchange that many coordination strategies typically assume. This paper presents a novel dynamic epistemic planning framework that enables implicit coordination and long horizon planning through higher-order reasoning among robots. With our approach, robots form and propagate higher-order belief particles, update world beliefs using Bayesian inference, and select actions via a behavior tree that anticipates teammates' likely decisions. A temporally aware Model Predictive Path Integral (MPPI) controller integrates this reasoning into low-level execution, allowing robots to plan intercepts and adapt trajectories under partial observability. The proposed framework is evaluated in both simulations and physical experiments, where it consistently reduces task completion time compared to a first-order baseline, demonstrating that epistemic logic can serve as a robust foundation for resilient coordination in communication-restricted domains.

</details>

---

### [[20_Research/Papers/机器人/OCELOT_Odometry_and_Contact_Estimation_for_Legged_Robots|OCELOT: Odometry and Contact Estimation for Legged Robots]]

![[assets/2605.21863_figure.png|800]]

- **arXiv**: [2605.21863](https://arxiv.org/abs/2605.21863)
- **PDF**: https://arxiv.org/pdf/2605.21863
- **详细分析**: [[20_Research/Papers/机器人/OCELOT_Odometry_and_Contact_Estimation_for_Legged_Robots|OCELOT: Odometry and Contact Estimation for Legged Robots]]
- **作者**: Emre Girgin, Cagri Kilic
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《OCELOT: Odometry and Contact Estimation for Legged Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

One of the significant challenges in legged robotics is achieving accurate odometry using only onboard proprioceptive sensors. In this study, we present a complete leg odometry pipeline based on an Error-State EKF (ESEKF) that relies exclusively on proprioceptive data: a body fixed IMU, joint encoders, and force sensors, where filter's state is corrected by feet determined to be in a stationary stance. The core of our contribution is fused contact detection and an uncertainty quantification module designed to explicitly identify and reject slippage. This module runs two detectors in parallel for each foot, 1) a debounced, force-based Gaussian Mixture Model (GMM) guided Finite State Machine (FSM) to confirm physical contact, and 2) a kinematic-based Generalized Likelihood Ratio Test (GLRT) on the estimated velocity of the foot. The continuous quality scores from both estimators are fused to detect if the foot is both physically loaded and kinematically stationary and served as an uncertainty signal for each contact. To validate our approach, we collected a multi-modal dataset of 29 sequences spanning diverse indoor and outdoor terrains (e.g., concrete, grass, pebble, and rock) total of 2.4 km long. We benchmarked our approach against both proprioceptive and exteroceptive methods. The results demonstrate our method's efficacy in providing accurate odometry estimates, robustly handling slippage-prone environments. We also share our code and real-time ROS2 package as open-source.

</details>

---

### [[20_Research/Papers/机器人/Analytical_and_Experimental_Force_Analysis_of_a_Soft_Linear_Pneumatic_Actuator|Analytical and Experimental Force Analysis of a Soft Linear Pneumatic Actuator]]

![[assets/2605.21836_first_page.png|800]]

- **arXiv**: [2605.21836](https://arxiv.org/abs/2605.21836)
- **PDF**: https://arxiv.org/pdf/2605.21836
- **详细分析**: [[20_Research/Papers/机器人/Analytical_and_Experimental_Force_Analysis_of_a_Soft_Linear_Pneumatic_Actuator|Analytical and Experimental Force Analysis of a Soft Linear Pneumatic Actuator]]
- **作者**: Mohammed Abboodi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Analytical and Experimental Force Analysis of a Soft Linear Pneumatic Actuator》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft sleeve actuators (SSAs) have recently been developed as a pneumatic actuation approach for wearable and assistive robotic systems. By integrating the actuation structure into a sleeve-like geometry, these actuators can reduce reliance on external attachment layers and transmission mechanisms while maintaining compliance with limb-shaped surfaces. However, the force-generation behavior of SSAs remains insufficiently explained, particularly with respect to the variation of output force during extension, the influence of external loading, and the mechanical role of axial stiffness. This paper presents an analytical and experimental force analysis of a linear soft sleeve actuator (LSSA). A quasi-static analytical model was developed by expressing the net axial force as the pressure-generated contribution from the cap and folded walls, reduced by the force associated with axial stiffness. The model incorporates internal pressure, projected pressure areas, folded wall geometry, axial displacement, and an experimentally fitted axial stiffness relation. Prescribed-extension and static-load experiments were conducted to evaluate the actuator response. At 125 kPa, the generated force decreased from approximately 112 N at zero extension to nearly zero at 40 mm. Static loading delayed measurable force generation and reduced force output, particularly at low and intermediate pressures. The results show that LSSA force generation is governed by coupled effects of pressure, geometry, displacement, loading, and axial stiffness.

</details>

---

### [[20_Research/Papers/具身智能/Safe_and_Steerable_Geometric_Motion_Policies_for_Robotic_Dexterous_Manipulation|Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation]]

![[assets/2605.21811_figure.png|800]]

- **arXiv**: [2605.21811](https://arxiv.org/abs/2605.21811)
- **PDF**: https://arxiv.org/pdf/2605.21811
- **详细分析**: [[20_Research/Papers/具身智能/Safe_and_Steerable_Geometric_Motion_Policies_for_Robotic_Dexterous_Manipulation|Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation]]
- **作者**: Albert Wu, Riccardo Bonalli, Thomas Lew, C. Karen Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic dexterous manipulation requires continuously reconciling objectives and constraints defined on heterogeneous geometric spaces: a robot controlled on a $\mathbb{R}^7$ configuration manifold may need to track end effector poses on $\mathrm{SE}(3)$ while satisfying obstacle avoidance margins in $\mathbb{R}$. We present Safe Pullback Bundle Dynamical Systems (SafePBDS), a geometrically consistent framework that computes optimal, certifiably safe configuration manifold accelerations from objectives and safety requirements on arbitrary task manifolds. SafePBDS builds on prior work that combines predefined task manifold dynamical systems to produce autonomous motion. Its first innovation is a pullback control barrier function construction, which converts task manifold safety conditions into linear constraints on configuration manifold accelerations. The second innovation is a task manifold action interface that allows a high-level policy to inject low dimensional residual motions; zero input recovers the autonomous behavior, while safety is preserved under arbitrary inputs. This lets high-level policies efficiently steer exploration while leaving precise motion to the autonomous behavior. We validate SafePBDS in simulation and on a 23-DOF Franka Panda-Allegro Hand platform. On dexterous grasping, SafePBDS achieves a $92.5\%$ success rate across 20 household objects and 120 trials. Using the action interface, the method can exclude any one of the four fingers during grasping via a one-dimensional action, achieving $94.4\%$ 3-finger grasp success across 3 objects and 36 trials. The efficient planning and safety guarantee of SafePBDS also enables the first model-based, fully actuated palm-down in-hand reorientation, exceeding $360^\circ$ of yaw rotation in both directions under varying object weight and wrist motion. Demo video and details: https://tml.stanford.edu/safe-pbds

</details>

---

### [[20_Research/Papers/机器人/Mind_the_Gaps_Multi-Robot_Feedback-Driven_Ergodic_Coverage_in_Unknown_Environments|Mind the Gaps: Multi-Robot Feedback-Driven Ergodic Coverage in Unknown Environments]]

![[assets/2605.21719_figure.png|800]]

- **arXiv**: [2605.21719](https://arxiv.org/abs/2605.21719)
- **PDF**: https://arxiv.org/pdf/2605.21719
- **详细分析**: [[20_Research/Papers/机器人/Mind_the_Gaps_Multi-Robot_Feedback-Driven_Ergodic_Coverage_in_Unknown_Environments|Mind the Gaps: Multi-Robot Feedback-Driven Ergodic Coverage in Unknown Environments]]
- **作者**: Thales Costa Silva, Nora Ayanian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Mind the Gaps: Multi-Robot Feedback-Driven Ergodic Coverage in Unknown Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we address the problem of multi-robot adaptive coverage, where teams of robots perform dynamic sampling by continuously adjusting their positions to collect data in an environment. This task can be challenging, particularly when robots must be efficiently allocated to new sampling locations over time. Ergodic search methods optimize robot trajectories by ensuring that the robots' time-averaged spatial distribution aligns with the spatial distribution of environmental information. While these methods promote effective exploration provided a target distribution, they often fail to account for unknown prior distributions of the environment. To overcome this limitation, we propose an adaptive coverage strategy that utilizes real-time feedback from an environmental model to adjust robot sampling behavior in response to unknown conditions. Our approach enhances traditional ergodic trajectory optimization by constructing a target spatial information distribution based on parametric models of the environment, which are updated online. This strategy assumes that the environment is either static or changes slowly compared to the robot's motion. Our framework allows robots to dynamically prioritize regions of high interest, improving coverage efficiency, synthesizing effective control policies for individual agents, and optimizing resource use in settings with unknown prior distributions. We validate our approach through simulations, demonstrating its effectiveness in enhancing coverage and resource allocation.

</details>

---

### [[20_Research/Papers/具身智能/Motion_Design_for_Grasp-Based_Dynamic_Locomotion_in_Microgravity|Motion Design for Grasp-Based Dynamic Locomotion in Microgravity]]

![[assets/2605.21704_figure.png|800]]

- **arXiv**: [2605.21704](https://arxiv.org/abs/2605.21704)
- **PDF**: https://arxiv.org/pdf/2605.21704
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Design_for_Grasp-Based_Dynamic_Locomotion_in_Microgravity|Motion Design for Grasp-Based Dynamic Locomotion in Microgravity]]
- **作者**: Chaerim Moon, Joohyung Kim, Justin K. Yim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Motion Design for Grasp-Based Dynamic Locomotion in Microgravity》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Locomotion in microgravity often relies on sparsely and irregularly arranged anchors, motivating grasp-based mobility with multiple limbs. In this setting, dynamic locomotion is feasible only through deliberate regulation of both anchored interactions and whole-body coordination under coupled dynamic and kinematic constraints. This paper presents design insights for grasp-based dynamic locomotion with multi-limbed robotic systems in microgravity, targeting scenarios that require 6D limb manipulation to establish contacts with candidate anchors. The investigated design parameters include gait pattern, stride length, locomotion speed, and nominal posture. A parameterizable locomotion planning framework is proposed to support variations of these parameters and to evaluate the resulting locomotion performance in terms of stability and actuation demand. Two representative quadruped morphologies are adopted for evaluation in physics-based simulation. The results demonstrate that enlarging the feasible contact wrench space and attenuating impulsive whole-body dynamics improve locomotion performance. These findings inform strategies for contact configuration selection and whole-body coordination in microgravity locomotion with multi-limbed systems.

</details>

---

### [[20_Research/Papers/强化学习/Closed-Loop_Sim-to-Real_Reinforcement_Learning_for_Deformable_Microfiber_Shape_Control|Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control]]

![[assets/2605.21688_first_page.png|800]]

- **arXiv**: [2605.21688](https://arxiv.org/abs/2605.21688)
- **PDF**: https://arxiv.org/pdf/2605.21688
- **详细分析**: [[20_Research/Papers/强化学习/Closed-Loop_Sim-to-Real_Reinforcement_Learning_for_Deformable_Microfiber_Shape_Control|Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control]]
- **作者**: Alessandro Amici, Houari Bettahar, Veeti Jaakkola, Quan Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，强化学习 0.8，机器人 0.3）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous contact-based micromanipulation is challenging because surface and interfacial interactions at the microscale are difficult to model accurately, limiting the use of conventional model-based control and sim-to-real learning. We present a closed-loop sim-to-real reinforcement learning (RL) approach for microfiber shape control on a surface. The central idea is to train geometric shape regulation in a simplified frictionless simulator and rely on real-time visual feedback during deployment to iteratively correct the observed effects of unmodeled surface interactions. An RL policy trained entirely in simulation is transferred directly to a physical dual-gripper micromanipulation system operating at 40 Hz, without retraining or domain adaptation. Using silk microfibers as a testbed, the policy achieves a mean point-wise shape error of 270 $\pm$ 80 $μ$m across twenty-four diverse initial configurations. Across nine specimens covering all combinations of three fiber diameters (50, 80, and 120 $μ$m) and three manipulated lengths (10 mm, 15mm, and 20 mm), the same policy achieves sub-millimeter final shape error without any retraining or retuning. These results show that a policy learned in a simplified simulator can achieve repeatable real-world microfiber shape regulation under surface contact, provided that the task-relevant effects of the sim-to-real mismatch remain observable and correctable within the closed feedback loop.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Multi-Coverage_for_Robot_Swarms|Distributed Multi-Coverage for Robot Swarms]]

![[assets/2605.21686_figure.png|800]]

- **arXiv**: [2605.21686](https://arxiv.org/abs/2605.21686)
- **PDF**: https://arxiv.org/pdf/2605.21686
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Multi-Coverage_for_Robot_Swarms|Distributed Multi-Coverage for Robot Swarms]]
- **作者**: Mariem Guitouni, Aaron T. Becker
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Distributed Multi-Coverage for Robot Swarms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous drone swarms deployed for surveillance, environmental monitoring, and infrastructure inspection must maintain reliable coverage of critical assets despite robot failures. This requires multicoverage: each asset must be observed by multiple robots for redundancy, with coverage requirements varying by asset importance. While recent work has solved the centralized problem optimally using integer programming, practical deployments face constraints that demand distributed solutions: robots operate with limited communication ranges, onboard computation restricts global planning, and partial system failures must not cause mission abort. We present a distributed multicoverage algorithm for robot swarms operating with local sensing, local communication, and no global coordination.

</details>

---

### [[20_Research/Papers/具身智能/Flying_Together_Human-Guided_Immersive_Shared_Control_for_Aerial_Robot_Teams_in_Unknown_Environments|Flying Together: Human-Guided Immersive Shared Control for Aerial Robot Teams in Unknown Environments]]

![[assets/2605.21680_figure.png|800]]

- **arXiv**: [2605.21680](https://arxiv.org/abs/2605.21680)
- **PDF**: https://arxiv.org/pdf/2605.21680
- **详细分析**: [[20_Research/Papers/具身智能/Flying_Together_Human-Guided_Immersive_Shared_Control_for_Aerial_Robot_Teams_in_Unknown_Environments|Flying Together: Human-Guided Immersive Shared Control for Aerial Robot Teams in Unknown Environments]]
- **作者**: Lou De Bel-Air, Luca Morando, Ruitao Chen, Keru Wang, Benjamin Jarvis, Charbel Toumieh, Yang Zhou, Ken Perlin, Dario Floreano, Giuseppe Loianno
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Flying Together: Human-Guided Immersive Shared Control for Aerial Robot Teams in Unknown Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While autonomous multi-robots can achieve safe and coordinated navigation, they often struggle to adapt to unforeseen conditions and to capture operator-driven objectives in unstructured environments. We present a Virtual Reality (VR)-based shared control framework for teams of drones operating in constrained and unknown environments, enabling real-time, user-guided exploration. At the core of our approach is a novel, user-guided motion-primitive-based planner that computes continuous, collision-free trajectories while continuously integrating operator input. This planner is coupled with an admittance controller, allowing the operator to flexibly influence team behavior and guide drones toward regions of interest that autonomous planners may overlook. The system supports mixed-reality operations with both physical and simulated drones, and implements a bilateral VR-based interface, allowing the operator to guide the robot team via migration points while receiving immediate visual feedback of the team state. Experimental results show that shared control improves obstacle avoidance, maintains inter-agent spacing, and reduces operator effort, demonstrating the feasibility and advantages of immersive, human-in-the-loop multi-robot navigation.

</details>

---
