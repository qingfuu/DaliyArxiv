# cs.RO | Robotics | 2026-09-25

#arxiv #ComputerScience

**论文数**: 43

### [[20_Research/Papers/机器人/ReVAMP_Vector-Accelerated_Motion_Planning_for_Kinematically-Constrained_Systems_via_Reparameterization|ReVAMP: Vector-Accelerated Motion Planning for Kinematically-Constrained Systems via Reparameterization]]

![[assets/2609.30213_figure.png|800]]

- **arXiv**: [2609.30213](https://arxiv.org/abs/2609.30213)
- **PDF**: https://arxiv.org/pdf/2609.30213
- **详细分析**: [[20_Research/Papers/机器人/ReVAMP_Vector-Accelerated_Motion_Planning_for_Kinematically-Constrained_Systems_via_Reparameterization|ReVAMP: Vector-Accelerated Motion Planning for Kinematically-Constrained Systems via Reparameterization]]
- **作者**: Shrutheesh R. Iyer, Thomas Cohn, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《ReVAMP: Vector-Accelerated Motion Planning for Kinematically-Constrained Systems via Reparameterization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots often must satisfy one or more constraints during motion planning for real-world tasks. When such constraints reduce the valid configuration space to a measure-zero subset, sampling based planning algorithms require modifications to draw feasible samples. For many common end-effector constraints, parameterizations built on inverse kinematics (IK) provide an alternate formulation where the constraints are satisfied by construction, allowing directly sampling the feasible set. Despite their elegant approach, parameterized planners have remained slower than vector-accelerated implementations of projection-based approaches, leaving their performance ceiling an open question. We explore a new axis of vectorization built upon reparameterizing the planning space through analytic IK. This approach addresses existing inefficiencies in vectorized projection-based planners and exposes new opportunities for parallelism within the planner. We show that the planner can synthesize plans in microseconds to milliseconds for high dimensional systems (up to 20 dimensions), with complex constraints, up to 10x faster than the current state-of-the-art. Furthermore, we demonstrate how such planning speeds open up avenues for restructuring sequential manipulation pipelines.

</details>

---

### [[20_Research/Papers/机器人/Contact_as_a_Decision_Variable_Capability-Tradeoff_Contact_Selection_for_Legged_Loco-Manipulation|Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation]]

![[assets/2609.30140_figure.png|800]]

- **arXiv**: [2609.30140](https://arxiv.org/abs/2609.30140)
- **PDF**: https://arxiv.org/pdf/2609.30140
- **详细分析**: [[20_Research/Papers/机器人/Contact_as_a_Decision_Variable_Capability-Tradeoff_Contact_Selection_for_Legged_Loco-Manipulation|Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation]]
- **作者**: Al Jaber Mahmud, Shuai Li, Xuan Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Contact as a Decision Variable: Capability-Tradeoff Contact Selection for Legged Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we study the joint selection of an environmental support contact and a whole-body configuration for a prescribed loco-manipulation task. A contact may provide greater physical support while restricting the motion required for the task. We formulate this problem through three capability measures: residual wrench, end-effector reach, and base mobility available after satisfying the task requirements, and we balance them against contact acquisition cost. Evaluating these capabilities for every candidate requires repeated whole-body optimizations. To reduce this computational cost, we propose Capability-Tradeoff Contact Selection (CTCS). CTCS screens candidates for contact and task feasibility, groups similar candidates within each surface, and predicts their capabilities from exact anchor evaluations using local sensitivity analysis. It checks these predictions through selective exact evaluations, ranks candidates by capability, and evaluates a shortlist exactly for final selection. We evaluate CTCS in simulations and hardware experiments using a Unitree Go2 quadruped with an AgileX NERO arm across $392$ task conditions with nine available support surfaces. Results show that CTCS outperforms ground-only and fixed-contact support, as it can select support surfaces that provide favorable capability trade-offs for the task. Compared with evaluating every candidate exactly, CTCS achieves approximately $3\times$ speedup while closely matching the resulting mean objective value.

</details>

---

### [[20_Research/Papers/具身智能/Faster_Visuomotor_Policy_Learning_on_Action_Manifolds_via_Riemannian_MeanFlow|Faster Visuomotor Policy Learning on Action Manifolds via Riemannian MeanFlow]]

![[assets/2609.30127_figure.png|800]]

- **arXiv**: [2609.30127](https://arxiv.org/abs/2609.30127)
- **PDF**: https://arxiv.org/pdf/2609.30127
- **详细分析**: [[20_Research/Papers/具身智能/Faster_Visuomotor_Policy_Learning_on_Action_Manifolds_via_Riemannian_MeanFlow|Faster Visuomotor Policy Learning on Action Manifolds via Riemannian MeanFlow]]
- **作者**: S. Talha Bukhari, Austin Garrett, Yi Wei, Ruiqi Ni, Zachary Kingston, Aniket Bera
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Faster Visuomotor Policy Learning on Action Manifolds via Riemannian MeanFlow》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies learn a direct map from raw sensory observations to robot action sequences. Policies based on Diffusion and Flow Matching capture the multimodal distribution over action sequences in an end-to-end manner. This expressivity comes at the cost of multi-step numerical integration of the learned vector field for action generation, which can be expensive and time-consuming, impeding fast control rates required in robotics applications. Furthermore, robot action sequences are usually defined on a smooth, differentiable manifold, requiring that the learned policy respects the intrinsic geometry of the robot's action space. Here, we present Riemannian MeanFlow Policy (RMFP), which learns the conditioned flow map of the probability path on the robot action manifold. Our formulation employs a flow map consistency objective grounded in the data by a Riemannian Conditional Flow Matching anchor. The flow map consistency condition is stable to train and constrains the learned model to finite-time transport, which yields on-manifold action sequence generation with as few as one network function evaluation. We present results on the spherical LASA and Push-T benchmarks, on the Tool Hang and Transport tasks of the Robomimic suite, and on the Franka Kitchen task with manifold-constrained action generation, and demonstrate that RMFP attains performance competitive with prior work at a lower sampling cost. We also employ RMFP on a real-world robotic manipulation task to demonstrate fast action generation under imperfect sensor measurements in the physical world.

</details>

---

### [[20_Research/Papers/具身智能/Real-Time_Force_Regulation_for_Whole-Hand_Dexterous_Grasping|Real-Time Force Regulation for Whole-Hand Dexterous Grasping]]

![[assets/2609.30082_figure.png|800]]

- **arXiv**: [2609.30082](https://arxiv.org/abs/2609.30082)
- **PDF**: https://arxiv.org/pdf/2609.30082
- **详细分析**: [[20_Research/Papers/具身智能/Real-Time_Force_Regulation_for_Whole-Hand_Dexterous_Grasping|Real-Time Force Regulation for Whole-Hand Dexterous Grasping]]
- **作者**: Sang Min Kim, Alexander Alexiev, Tzu-Yuan Lin, Sangbae Kim, Young Min Kim, Yonghyeon Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.7，机器人 0.3）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《Real-Time Force Regulation for Whole-Hand Dexterous Grasping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust dexterous grasping requires maintaining physical stability despite contacts interactively evolving across the entire hand. A precomputed force distribution can easily fail under object motion, modeling errors, or external disturbances. In this paper, we present a framework for real-time force regulation over dynamically changing whole-hand contacts. Our method geometrically estimates contacts across all hand links using a tracked object model and proprioception, without requiring tactile sensing at those contacts. It repeatedly recomputes the desired contact-force distribution subject to friction constraints, actuator limits, and an actuation-consistency constraint motivated by classical whole-limb force analysis. We integrate this force-regulation controller with reactive reaching, enabling the hand to acquire a grasp, maintain it under disturbances, and regrasp after losing the object. Simulation experiments without gravity demonstrate improved grasp retention over fixed-allocation and fingertip-only execution under controlled perturbations, while real-world experiments on a 27-DoF arm-hand system demonstrate grasp maintenance and recovery under human-applied disturbances as contacts evolve across the whole hand. Project page: this https URL

</details>

---

### [[20_Research/Papers/大模型/Body-Grounded_Replanning_for_Physically_Adaptive_Manipulation|Body-Grounded Replanning for Physically Adaptive Manipulation]]

![[assets/2609.30024_figure.png|800]]

- **arXiv**: [2609.30024](https://arxiv.org/abs/2609.30024)
- **PDF**: https://arxiv.org/pdf/2609.30024
- **详细分析**: [[20_Research/Papers/大模型/Body-Grounded_Replanning_for_Physically_Adaptive_Manipulation|Body-Grounded Replanning for Physically Adaptive Manipulation]]
- **作者**: Namiko Saito, Hiroshi Kera
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Body-Grounded Replanning for Physically Adaptive Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulation requires not only reasoning about the external environment, but also about the robot's physical condition. A strategy may remain geometrically feasible while becoming physically unsuitable due to increased joint load or limited mobility, yet internal physical state is typically used only for low-level control. We propose body-grounded high-level replanning, which uses internal physical state to adapt manipulation strategies during execution. Body-state events trigger strategy replanning, and an LLM interprets the underlying joint-level state, recent execution statistics, and execution history to select a context-dependent alternative, while leaving the task objective and low-level controller unchanged. We evaluate the framework on a reaching task under controlled load and asymmetric mobility constraints in simulation and on a real robot. Our experiments show that body-grounded replanning maintains high task success while reducing physical effort and enabling more efficient strategy adaptation. Additional contact-rich manipulation experiments demonstrate the applicability of the same replanning interface beyond reaching. These results show that internal physical state can inform not only low-level control, but also high-level decisions about how a manipulation task should be performed.

</details>

---

### [[20_Research/Papers/强化学习/Res-HIL_Human-Guided_Residual_Reinforcement_Learning_for_Sample-Efficient_Dexterous_Manipulation|Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation]]

![[assets/2609.30023_figure.png|800]]

- **arXiv**: [2609.30023](https://arxiv.org/abs/2609.30023)
- **PDF**: https://arxiv.org/pdf/2609.30023
- **详细分析**: [[20_Research/Papers/强化学习/Res-HIL_Human-Guided_Residual_Reinforcement_Learning_for_Sample-Efficient_Dexterous_Manipulation|Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation]]
- **作者**: Mariia Iavorskaia, Christian Dietz, Sebastian Albrecht, Majid Khadiv
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，强化学习 0.8，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Res-HIL: Human-Guided Residual Reinforcement Learning for Sample-Efficient Dexterous Manipulation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HIL-RL, HIL-SERL, HiL-ResRL, OHP-RL, SHaRe-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning enables robots to acquire manipulation skills from demonstrations, but the resulting policies can fail outside the training data, while collecting more demonstrations requires substantial human effort. Human-in-the-loop reinforcement learning uses corrective feedback during online training, but typically learns the complete task policy rather than refining a pretrained imitation policy. We introduce Res-HIL, a human-in-the-loop residual reinforcement learning framework that learns corrective actions on top of a frozen imitation policy. Each human intervention provides two complementary learning signals: direct supervision of the residual policy and reward shaping of preceding autonomous behavior. Res-HIL combines these signals with zero initialization of the residual policy to stabilize and accelerate online learning. We evaluate Res-HIL on five contact-rich manipulation tasks spanning high-precision and long-horizon behaviors. With only 20 initial demonstrations, Res-HIL outperforms state-of-the-art full-policy human-in-the-loop reinforcement learning and residual fine-tuning without human guidance on every task after ten minutes of online training. Res-HIL improves its pretrained base policies and outperforms imitation policies trained with five times more demonstrations. An ablation study shows that direct residual supervision is critical to performance, while intervention-aware reward shaping substantially improves training efficiency.

</details>

---

### [[20_Research/Papers/机器人/Pairwise_Approximation_Can_Select_the_Wrong_Multi-Robot_Plan|Pairwise Approximation Can Select the Wrong Multi-Robot Plan]]

![[assets/2609.29929_first_page.png|800]]

- **arXiv**: [2609.29929](https://arxiv.org/abs/2609.29929)
- **PDF**: https://arxiv.org/pdf/2609.29929
- **详细分析**: [[20_Research/Papers/机器人/Pairwise_Approximation_Can_Select_the_Wrong_Multi-Robot_Plan|Pairwise Approximation Can Select the Wrong Multi-Robot Plan]]
- **作者**: William Teo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Pairwise Approximation Can Select the Wrong Multi-Robot Plan》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot coordination methods often score a joint plan from singleton and pairwise terms, leaving out the terms that involve three or more robots. We measure the plan-selection regret of two pairwise approximations to delivered coverage using frozen multi-robot trajectories. For each four-robot plan on an indoor exploration benchmark, replaying all 16 robot subsets gives the exact delivered-coverage set function $F$. From the same subset values we compute two pairwise scores: the exact order-2 Möbius truncation $F_2$, which depends only on the singleton and pair values, and an equal-weight least-squares two-additive fit $G$. Ranking by $F_2$ instead of $F$ changes the selected plan on six of seven maps at the 15 m candidate-generation range in each of two candidate families, with regret up to 0.337 of map coverage. Switching to $G$ reduces the regret but still changes the selection on three of seven maps in each family. The additive score $F_1$, which keeps only the singleton terms, selects the exact winner on six of seven maps in one family and four of seven in the other, against one of seven for $F_2$. We also find that lower average reconstruction error does not guarantee lower selection regret.

</details>

---

### [[20_Research/Papers/具身智能/GPT-6-Astra_Lights_Up_Embodied_Navigation_Evaluation_in_Zero-Shot_Vision-and-Language_Navigation_in_Continuous_Environments|GPT-6-Astra Lights Up Embodied Navigation: Evaluation in Zero-Shot Vision-and-Language Navigation in Continuous Environments]]

![[assets/2609.29861_figure.png|800]]

- **arXiv**: [2609.29861](https://arxiv.org/abs/2609.29861)
- **PDF**: https://arxiv.org/pdf/2609.29861
- **详细分析**: [[20_Research/Papers/具身智能/GPT-6-Astra_Lights_Up_Embodied_Navigation_Evaluation_in_Zero-Shot_Vision-and-Language_Navigation_in_Continuous_Environments|GPT-6-Astra Lights Up Embodied Navigation: Evaluation in Zero-Shot Vision-and-Language Navigation in Continuous Environments]]
- **作者**: Guangzhao Dai, Qianru Sun, Qi Wu, Bin Zhu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, EmbodiedAI

#### 研究背景与动机

《GPT-6-Astra Lights Up Embodied Navigation: Evaluation in Zero-Shot Vision-and-Language Navigation in Continuous Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AstraNav-World, CoRL, InternVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate whether GPT-6-Astra, a general-purpose foundation model, can navigate unfamiliar environments using its own perception, reasoning, and decision-making capabilities. Our evaluation focues on zero-shot vision-and-language navigation in continuous environments (VLN-CE) through a minimal interface in the Codex harness, aiming to unleash GPT-6-Astra's full potential for navigation. Using monocular RGB, GPT-6-Astra decides when to observe, how to move, and when to stop, without navigation-specific fine-tuning, a trained waypoint predictor, or a pre-built scene map. Our evaluation yields four main findings. First, \textbf{\textit{GPT-6-Astra achieves strong zero-shot navigation performance using only monocular RGB observations}}. On the common-adopted zero-shot R2R-CE benchmark, ultra reasoning achieves a success rate of \textbf{\textit{79.0\%}}, exceeding the strongest reported zero-shot and supervised success rates by \textbf{\textit{13.0}} and \textbf{\textit{6.9}} percentage points, respectively. Second, \textbf{\textit{GPT-6-Astra advances multi-stage language instructions into coherent, adaptive navigation}} by grounding spatial relations, tracking task progress, and revising its actions. Third, \textbf{\textit{reliable route execution and goal verification remain challenging, even with ultra reasoning}}. Plausible local landmark matches do not consistently lead to correct task completion. Fourth, \textbf{\textit{these capabilities motivate rethinking the role of embodied learning}}. Future VLN research should build on foundation models to advance generalizable and reliable embodied intelligence.

</details>

---

### [[20_Research/Papers/强化学习/Self-Supervised_Anchoring_of_Fingertip_Sensing_to_Proprioception_and_Proactive_Actions_for_Robot_Imitation_Learning|Self-Supervised Anchoring of Fingertip Sensing to Proprioception and Proactive Actions for Robot Imitation Learning]]

![[assets/2609.29822_figure.png|800]]

- **arXiv**: [2609.29822](https://arxiv.org/abs/2609.29822)
- **PDF**: https://arxiv.org/pdf/2609.29822
- **详细分析**: [[20_Research/Papers/强化学习/Self-Supervised_Anchoring_of_Fingertip_Sensing_to_Proprioception_and_Proactive_Actions_for_Robot_Imitation_Learning|Self-Supervised Anchoring of Fingertip Sensing to Proprioception and Proactive Actions for Robot Imitation Learning]]
- **作者**: Tomohiro Motoda, Masaki Murooka, Keisuke Shirai, Hanbit Oh, Ryoichi Nakajo, Shotaro Miwa, Roman Mykhailyshyn, Hugo Duarte, Yukiyasu Domae
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Self-Supervised Anchoring of Fingertip Sensing to Proprioception and Proactive Actions for Robot Imitation Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL, JRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic imitation learning often relies on external cameras, yet local interaction cues such as object proximity, contact onset, and grasp state are difficult to observe near the fingertips because of occlusion and limited temporal resolution. We study how to effectively incorporate complementary fingertip sensing into imitation learning using pressure-sensitive tactile and reflective proximity sensors, along with pretrained sensor encoders. The two modalities provide information at different manipulation phases: proximity sensing is informative before contact, whereas tactile sensing becomes informative after contact. However, naively adding these signals to a policy does not consistently improve performance and can even underperform vision-only policies, suggesting that sparse, phase-dependent sensor signals are difficult to exploit from limited demonstrations. We therefore propose a proprioception-anchored pretraining method, PROprioceptive-and-PRoactive Anchoring (PROPRA), which independently aligns each fingertip sensor history with proprioceptive and action segments. This provides a continuously available sensorimotor reference, allowing each sensor to be aligned independently during its informative phases. Experiments on real-world manipulation tasks show that our pretraining method improves average success rates over vision-only policies and image-anchored pretraining baselines. Representation analysis further shows that it preserves richer information about pre-contact states, enabling more effective use of complementary fingertip sensing. Please refer to our project page: this https URL

</details>

---

### [[20_Research/Papers/大模型/Markerless_Multi-Modal_Autonomous_Robotic_Inspection_of_Large_Space_Structures|Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures]]

![[assets/2609.29644_figure.png|800]]

- **arXiv**: [2609.29644](https://arxiv.org/abs/2609.29644)
- **PDF**: https://arxiv.org/pdf/2609.29644
- **详细分析**: [[20_Research/Papers/大模型/Markerless_Multi-Modal_Autonomous_Robotic_Inspection_of_Large_Space_Structures|Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures]]
- **作者**: Juan De Dios Alfaro, Arturo Ríos, David Rodríguez-Martínez, Carlos Pérez-del-Pulgar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CasMVSNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Future orbital infrastructures, such as deployable antennas, solar farms, and large orbital platforms will require autonomous inspection systems able to operate with limited prior knowledge and without cooperative markers. Current on-orbit servicing approaches often rely on predefined trajectories, standard interfaces, fiducial markers or accurate target models, which limits scalability for large, heterogeneous or partially unknown structures. This paper presents a markerless autonomous robotic inspection pipeline in which 3D reconstruction is used as an inspection-support representation. The system integrates a Kinova Gen2 manipulator with an end-effector-mounted multimodal sensor head composed of an RGB-D camera, a thermal camera and a 2D LiDAR. The pipeline estimates an approximate inspection volume, generates viewpoints, plans collision-free motions with MoveIt, and synchronously records RGB-D images, thermal data, and robot poses in ROS2. Candidate reconstruction methods were evaluated to select a practical method for this pipeline, with Nerfacto used for geometric reconstruction and Thermal-Nerfacto used to demonstrate thermal-aware rendering for inspection. Validation in a Gazebo-based simulator and preliminary laboratory tests reveal that the proposed system can autonomously acquire spatially coherent inspection data and produce reconstructions suitable for visual and geometric assessment, representing a step towards inspection of large non-cooperative space structures.

</details>

---

### [[20_Research/Papers/强化学习/Temperament_Engineering_Designing_Strategic_Behavioural_Diversity_in_Robot_Swarms|Temperament Engineering: Designing Strategic Behavioural Diversity in Robot Swarms]]

![[assets/2609.29423_figure.png|800]]

- **arXiv**: [2609.29423](https://arxiv.org/abs/2609.29423)
- **PDF**: https://arxiv.org/pdf/2609.29423
- **详细分析**: [[20_Research/Papers/强化学习/Temperament_Engineering_Designing_Strategic_Behavioural_Diversity_in_Robot_Swarms|Temperament Engineering: Designing Strategic Behavioural Diversity in Robot Swarms]]
- **作者**: Edmund R. Hunt
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Temperament Engineering: Designing Strategic Behavioural Diversity in Robot Swarms》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

No two robots are truly identical: calibration, battery state, sensor drift and wear give every swarm a distribution of behaviour rather than a single point, usually treated as an imperfection to be minimised. In animal collectives the reverse holds: consistent individual differences in behaviour ('temperament') are shaped by natural selection and often decisive for group performance. This perspective proposes 'temperament engineering', a bio-inspired framework that treats the swarm's distribution of temperaments, rather than the individual controller, as the design object. It borrows five evolutionarily validated axes of animal temperament (shyness-boldness, exploration-avoidance, activity, aggressiveness and sociability) as a design vocabulary, rendering each as a continuous control parameter $\tau \in [0,1]$ above the controller, realisable as a module threshold, a policy-conditioning vector in multi-agent reinforcement learning, or a constraint on a foundation-model planner. A three-phase workflow maps mission success criteria onto relevant axes, plans the shape of the $\tau$ distribution, and tunes reaction norms governing how temperament responds to environmental cues. The payoff is greatest under decentralisation: where a central planner can reassign behaviour online, a temperament distribution is a planner output, but in a swarm without global knowledge it must be an offline, anticipatory design input. Behavioural and platform heterogeneity are thereby co-design variables, and I sketch tentative robot-native axes (self-model plasticity, forcefulness, initiative and expressiveness) arising from features robots have and animals do not. Engineered heterogeneity has been shown to outperform homogeneous swarms in tasks such as aggregation and exploration; establishing when, and how much, heterogeneity repays its cost is the work the field can now take forward.

</details>

---

### [[20_Research/Papers/机器人/WRAP_Fixtureless_Wrench-aware_Multi-Robot_Assembly_Planning|WRAP: Fixtureless Wrench-aware Multi-Robot Assembly Planning]]

![[assets/2609.29407_figure.png|800]]

- **arXiv**: [2609.29407](https://arxiv.org/abs/2609.29407)
- **PDF**: https://arxiv.org/pdf/2609.29407
- **详细分析**: [[20_Research/Papers/机器人/WRAP_Fixtureless_Wrench-aware_Multi-Robot_Assembly_Planning|WRAP: Fixtureless Wrench-aware Multi-Robot Assembly Planning]]
- **作者**: Valentin N. Hartmann, Huang Su, Yijiang Huang, Stelian Coros
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《WRAP: Fixtureless Wrench-aware Multi-Robot Assembly Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assembly using robots often requires specially designed fixtures, or relies on top-down only assembly strategies. Using multiple robots, we can avoid using fixtures and make robotic assembly more flexible. Planning assembly sequences for multiple robots is challenging due to the high number of possible task assignments and orders. In addition, we need to reason over forces that occur during the assembly process, e.g., to decide if multiple robots are required for support, or if external support such as a table should be used. We present Wrap, a multi-robot assembly planner for multi-part assemblies, given the inter-part ordering-dependencies, the part meshes, and their initial state. We formulate a linear program to reason about valid grasps for supporting the forces that occur during assembly. The search leverages the assembly sequence, and greedily finds a feasible solution per assembly step by computing a heuristic via a cheap backwards search, and using the heuristic in the more expensive forward search. We then solve the multi-robot, multi-goal motion planning problem, and for execution, we split the plan into contact-rich assembly skills, and free space motion. We benchmark the planner on a variety of multi-part assemblies, and apply the planner to groups of robots differing in size and kinematics. We validate the work both in a physics simulation, and in real. Videos and code are available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/RACaP_Agentic_Reasoning,_Acting,_and_Coding_as_Policies_for_Evolvable_Robot_Learning|RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning]]

![[assets/2609.29394_figure.png|800]]

- **arXiv**: [2609.29394](https://arxiv.org/abs/2609.29394)
- **PDF**: https://arxiv.org/pdf/2609.29394
- **详细分析**: [[20_Research/Papers/强化学习/RACaP_Agentic_Reasoning,_Acting,_and_Coding_as_Policies_for_Evolvable_Robot_Learning|RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning]]
- **作者**: Zexi Li, Yehang Zhang, Haojian Huang, Bohan Zhou, Wenqian Li, Chenxu Wang, Yifan Chang, Yangkai Wei, Tianyi Zhang, Ying-Cong Chen, Kaiwen Zhou, Yinchuan Li...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robot agents must learn from experience, transfer to new tasks, and act efficiently. Code as Policies (CaP) methods generate and repair programs at runtime, incurring latency and entangling reusable mechanisms with task-specific decisions. We introduce RACaP, an agentic framework that moves coding to evolution and uses a Reasoning-and-Acting (ReAct) loop to call frozen, typed Policy APIs at deployment. A two-phase strategy combines capability curriculum learning with autonomous self-evolution to improve the APIs, the ReAct harness, and experience memory. The APIs encode reusable physical mechanisms while exposing arguments for runtime adaptation. ReAct combines task-specific working memory, long-term experience memory, and visual feedback to select actions, verify outcomes, and recover from failures without modifying source code. RACaP achieves 54.4% success on LIBERO-90, 45.0% on zero-shot LIBERO-PRO, and 46.0% on LIBERO-Long, compared with at most 4.0% for CaP baselines on long-horizon tasks. On LIBERO-PRO, it achieves 2.5 times the success rate of CaP baselines and a 1.9-fold speedup in median policy time. For efficient on-robot deployment, rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into Qwen3-VL-8B-Instruct, yielding a 13.2-fold per-decision inference speedup and reducing repeated physical calls from 16 to 4. These results show that separating reusable code from runtime decisions supports continued evolution, effective transfer, and efficient long-horizon control.

</details>

---

### [[20_Research/Papers/具身智能/Robo-Harness_K1_Harnessing_Robot-Use_Agents_via_Perception_Augmentation|Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation]]

![[assets/2609.29389_figure.png|800]]

- **arXiv**: [2609.29389](https://arxiv.org/abs/2609.29389)
- **PDF**: https://arxiv.org/pdf/2609.29389
- **详细分析**: [[20_Research/Papers/具身智能/Robo-Harness_K1_Harnessing_Robot-Use_Agents_via_Perception_Augmentation|Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation]]
- **作者**: Zexi Li, Yehang Zhang, Wenqian Li, Haojian Huang, Chenxu Wang, Shiyuan Deng, Yangkai Wei, Tianyi Zhang, Binghui Xie, Bohan Zhou, Yifan Chang, Kaiwen Zhou...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.2，大模型 0.5，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Harness-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation vision-language models (VLMs) understand objects, instructions, and spatial relations, yet translating this capability into robotic manipulation remains difficult. Vision-language-action (VLA) models require extensive demonstrations and may compromise pretrained understanding, while direct RGB-only VLM control is costly and strongly dependent on model capability. We introduce Robo-Harness K1, a robot-use agent (RUA) framework that exposes perception as tools. The agent queries calibrated depth, persistent visual anchors, spatial measurements, and grasp hypotheses, then selects generic motions from the returned evidence. This interface makes 3D geometry accessible without changing the VLM architecture or training a depth encoder. On matched LIBERO-PRO tasks, Gemini 3.7 Flash with K1 reaches 77.8% accuracy, surpassing GPT-6 Astra's 61.1% with an RGB-only harness; K1 further improves Astra to 88.9%. Without target fine-tuning, Gemini with K1 transfers to three RoboSuite arms and dual-arm RoboTwin tasks. On RoboTwin, it achieves 32.0% on Easy and 28.0% on Hard, showing resilience to visual and environmental perturbations. K1 also produces tool-call traces aligned with next-token training. A Qwen3.5-9B student trained on only 107 teacher episodes reaches 44.2% accuracy on new initial states versus 30.2% for OpenVLA, and 13.9% on held-out task conditions versus 0.0% for OpenVLA. These results suggest that perception-augmented RUAs offer a promising route to sample-efficient, generalizable robotic policies that leverage VLM capabilities through an accessible tool interface.

</details>

---

### [[20_Research/Papers/具身智能/A_Simple_Gripper_Interface_for_Simulator-Agnostic_Cloth_Manipulation|A Simple Gripper Interface for Simulator-Agnostic Cloth Manipulation]]

![[assets/2609.29340_figure.png|800]]

- **arXiv**: [2609.29340](https://arxiv.org/abs/2609.29340)
- **PDF**: https://arxiv.org/pdf/2609.29340
- **详细分析**: [[20_Research/Papers/具身智能/A_Simple_Gripper_Interface_for_Simulator-Agnostic_Cloth_Manipulation|A Simple Gripper Interface for Simulator-Agnostic Cloth Manipulation]]
- **作者**: Abhilash Nayak, Franco Coltraro, Maria Alberich-Carramiñana, Carme Torras
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《A Simple Gripper Interface for Simulator-Agnostic Cloth Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a grasping model for cloth manipulation specifically tailored to ease the deployment of robotic control methods. The model is robust, fast and easy to implement avoiding at the same time contact and friction considerations between the gripper and the cloth in favor of simple positional constraints. The gripper is described by its pose, jaw state, and an attached grasping volume. Two kinds of grasping volumes are considered: an axis-aligned box to simulate a pinch grasping and a square pyramidal volume to simulate point grasping. When the gripper closes, the discrete cloth positions lying inside this volume are selected, stored in the local gripper frame, and then transported with the gripper motion. A simple squeezing step is also included to progressively move the selected cloth positions toward the center of the grasping region, avoiding an instantaneous displacement at closure. The model can be used in any simulator as it only requires access to discrete cloth positions and a mechanism for imposing target positions as constraints. We implement our grasping model in conjunction with a constraint-based inextensible cloth simulator, where grasping is implemented as moving positional equality constraints coupled with stretch, shear, collision, and table contact projection steps. The same gripper trajectory is applied on a robot arm to fold a real piece of cloth, serving as a simple bridge between simulation and physical cloth manipulation and showcasing the realism and practicality of our idealized grasping model.

</details>

---

### [[20_Research/Papers/具身智能/Dense-Joint-Based_Obstacle-Aided_Locomotion_with_a_Joint-Repositionable_Snake_Robot|Dense-Joint-Based Obstacle-Aided Locomotion with a Joint-Repositionable Snake Robot]]

![[assets/2609.29261_figure.png|800]]

- **arXiv**: [2609.29261](https://arxiv.org/abs/2609.29261)
- **PDF**: https://arxiv.org/pdf/2609.29261
- **详细分析**: [[20_Research/Papers/具身智能/Dense-Joint-Based_Obstacle-Aided_Locomotion_with_a_Joint-Repositionable_Snake_Robot|Dense-Joint-Based Obstacle-Aided Locomotion with a Joint-Repositionable Snake Robot]]
- **作者**: Kyosuke Minomo, Ryo Takahashi, Kotaro Yasui, Yasutaka Nakashima, Motoji Yamamoto, Ayato Kanada
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Dense-Joint-Based Obstacle-Aided Locomotion with a Joint-Repositionable Snake Robot》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Obstacle-aided locomotion is a fundamental capability for snake robots to traverse complex environments. However, conventional rigid-link snake robots often suffer from stagnation or jamming caused by their low joint density (i.e., the number of joints per unit length). This results in discontinuous contact with obstacles, unlike the continuous adaptation of biological snakes. To investigate the effect of joint density on obstacle-aided locomotion performance, we utilized a joint-repositionable snake robot mechanism that decouples actuators from joints, enabling a high-density architecture. We developed two experimental models with identical total lengths but different joint densities (high-density and low-density) and conducted comparative propulsion experiments in obstacle environments with varying obstacle diameters. The experimental results demonstrate that the high-density model substantially suppresses the abrupt shifts in reaction forces that cause stagnation in the low-density model. By maintaining smooth contact points, the high-density configuration reduces power consumption and achieves stable, continuous propulsion. These results highlight high joint density as a key factor in improving the environmental adaptability of snake robots in complex terrains.

</details>

---

### [[20_Research/Papers/具身智能/AdaHVLA_Adaptive_Harnesses_for_Long-Horizon_Vision-Language-Action_Execution|AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution]]

![[assets/2609.29204_figure.png|800]]

- **arXiv**: [2609.29204](https://arxiv.org/abs/2609.29204)
- **PDF**: https://arxiv.org/pdf/2609.29204
- **详细分析**: [[20_Research/Papers/具身智能/AdaHVLA_Adaptive_Harnesses_for_Long-Horizon_Vision-Language-Action_Execution|AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution]]
- **作者**: Junyi Tang, Jie Peng, Zezhen Ding, Yuan Shen, Tianlong Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《AdaHVLA: Adaptive Harnesses for Long-Horizon Vision-Language-Action Execution》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AdaHVLA, AdaHVLA-Adaptive_Harness_VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models offer strong local control and instruction following but often struggle with long-horizon tasks requiring persistent memory and planning. Task harnesses provide persistent context for agent reasoning by retaining task history and tracking progress across execution stages. To bring these complementary capabilities together, we introduce AdaHVLA, an adaptive harness that refines code-based coordination policies through robot experience to better align agent reasoning and memory with VLA execution. Its decoupled multiagent adaptation process separates evidence analysis, harness revision, and behavioral assessment into distinct working contexts, using testable coordination hypotheses to guide revisions and subsequent rollouts to assess their predicted effects. A stateful revision graph links execution evidence, hypotheses, revisions, and observed effects, preserving alternative harnesses and adaptation memory to guide refinement across repeated attempts and continued adaptation across tasks and environments. In simulation, AdaHVLA raises mean test success on NaVILA-LH from 22.5\% to as high as 57.5\% and improves manipulation test success across three VLA backbones by up to 30.8 percentage points over the initial harness. Real-world deployment further illustrates how the adapted policies support stable execution across task stages.

</details>

---

### [[20_Research/Papers/机器人/Anthropomimetic_Soft_Robotic_Forearm_with_Independently_Articulated_Carpal_Bones_Enabling_Human-Like_Adaptive_Stiffness_Modulability|Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness Modulability]]

![[assets/2609.29176_first_page.png|800]]

- **arXiv**: [2609.29176](https://arxiv.org/abs/2609.29176)
- **PDF**: https://arxiv.org/pdf/2609.29176
- **详细分析**: [[20_Research/Papers/机器人/Anthropomimetic_Soft_Robotic_Forearm_with_Independently_Articulated_Carpal_Bones_Enabling_Human-Like_Adaptive_Stiffness_Modulability|Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness Modulability]]
- **作者**: Yoshinobu Obata, Yinlai Jiang, Hiroshi Yokoi, Shunta Togo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Anthropomimetic Soft Robotic Forearm with Independently Articulated Carpal Bones Enabling Human-Like Adaptive Stiffness Modulability》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ECRL, OpenSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The human wrist exhibits adaptive stiffness modulability: joint stiffness anisotropy can be actively regulated through muscle co-contraction. This functionality is essential for stable manipulation, yet the underlying morphological factors remain unclear. To identify these factors, we developed an anatomically accurate anthropomimetic soft robotic forearm comprising eight independently movable carpal bones interconnected by ligaments, 22 actuated muscles, and compliant fingertips. We measured wrist joint stiffness under four muscle activation patterns across three skeletal configurations: anatomically normal carpal bones, a fused proximal carpal row, and a geometric ellipsoidal skeleton. The stiffness ellipse exhibited low stiffness along the dart-throwing motion (DTM) direction when finger muscles were activated, but high stiffness along the same direction when wrist and finger muscles were activated simultaneously. These results agree with previously reported human measurements, demonstrating that precise anatomical replication reproduces human-like stiffness modulability. Fusing the proximal carpal row eliminated the low DTM-direction stiffness under finger muscle activation, while the geometric ellipsoidal skeleton showed poor stiffness ellipse reorientation across all conditions. Carpal bone motion analysis revealed significantly opposing coupling patterns between wrist and finger muscles at the proximal carpal row, accompanied by a consistent but non-significant trend at the midcarpal joint, providing a mechanical explanation for this modulation. These findings demonstrate that carpal bone morphology plays a dominant role in human wrist stiffness modulation and provide design principles for humanoid robot wrists.

</details>

---

### [[20_Research/Papers/具身智能/A_Tendon-Driven_Robotic_Jellyfish_with_Constrained_Soft_Actuation_and_Depth_Control_via_Reinforcement_Learning|A Tendon-Driven Robotic Jellyfish with Constrained Soft Actuation and Depth Control via Reinforcement Learning]]

![[assets/2609.29132_figure.jpg|800]]

- **arXiv**: [2609.29132](https://arxiv.org/abs/2609.29132)
- **PDF**: https://arxiv.org/pdf/2609.29132
- **详细分析**: [[20_Research/Papers/具身智能/A_Tendon-Driven_Robotic_Jellyfish_with_Constrained_Soft_Actuation_and_Depth_Control_via_Reinforcement_Learning|A Tendon-Driven Robotic Jellyfish with Constrained Soft Actuation and Depth Control via Reinforcement Learning]]
- **作者**: Jiarui Peng, Yutong Wu, Zelong Wang, Ping Deng, Xiaotian Zhang, Xian Chen, Kecheng Qin, Zhongyi Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.6，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《A Tendon-Driven Robotic Jellyfish with Constrained Soft Actuation and Depth Control via Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Jellyfish-inspired robots offer a compliant and efficient approach to underwater locomotion, but achieving large deformation together with repeatable actuation and closed-loop control remains challenging. In this work, we present a tendon-driven robotic jellyfish with constrained soft actuation. Each actuator combines a flexible substrate with discrete constraints, enabling bending up to \(150^\circ\) with an approximately linear tendon displacement-bending relationship. Eight actuators driven by four servos allow the robot to perform stable swimming, attitude adjustment, and self-righting. Based on the linear actuation, a reinforcement-learning controller is further developed, enabling closed-loop depth regulation in both simulation and physical experiments. These results show that mechanical constraints can improve the controllability of soft actuation while preserving compliant jellyfish-like motion, providing a route toward manoeuvrable and autonomous jellyfish robots.

</details>

---

### [[20_Research/Papers/具身智能/A_Support-Enhanced_Granular-Jamming_Gripper_for_RL-based_Grasping_with_Continuum_Manipulators|A Support-Enhanced Granular-Jamming Gripper for RL-based Grasping with Continuum Manipulators]]

![[assets/2609.29093_figure.jpg|800]]

- **arXiv**: [2609.29093](https://arxiv.org/abs/2609.29093)
- **PDF**: https://arxiv.org/pdf/2609.29093
- **详细分析**: [[20_Research/Papers/具身智能/A_Support-Enhanced_Granular-Jamming_Gripper_for_RL-based_Grasping_with_Continuum_Manipulators|A Support-Enhanced Granular-Jamming Gripper for RL-based Grasping with Continuum Manipulators]]
- **作者**: Danyu Liu, Tianlin Zhang, Wei Chen, Wei Tang, Kecheng Qin, Zhongyu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《A Support-Enhanced Granular-Jamming Gripper for RL-based Grasping with Continuum Manipulators》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuum manipulators provide dexterous motion in confined spaces, but structural compliance, hysteresis, and load-dependent deformation leave residual position and orientation errors that can undermine reliable contact with rigid grippers. To address this limitation, this paper presents a lightweight support-enhanced granular-jamming gripper tailored to a continuum manipulator. The gripper maintains compliance before jamming while establishing a direct load path to the continuum manipulator tip after jamming. To improve its grasping performance, we systematically designed membrane materials, particles, filling ratios, and the internal support structure, and further identify geometry-dependent grasp boundaries with respect to contact offset and object shape. Building on these results, we construct a physical manipulation system integrating the continuum manipulator, granular-jamming gripper, visual feedback, tendon actuation, and pneumatic control. We then train a reinforcement-learning-based reaching controller in a randomized simulation and deploy it on the physical system, demonstrating how positioning control and contact level mechanical adaptation can complement each other in a modular grasp-and-release task. By introducing an adaptive structure that relaxes the need for highly accurate modeling and positioning control, this work explores a design paradigm that integrates physical and embodied intelligence.

</details>

---

### [[20_Research/Papers/具身智能/From_Passive_Execution_to_Active_Exploration_Agentic_Embodied_Manipulation_in_Realistic_Environments|From Passive Execution to Active Exploration: Agentic Embodied Manipulation in Realistic Environments]]

![[assets/2609.29091_figure.png|800]]

- **arXiv**: [2609.29091](https://arxiv.org/abs/2609.29091)
- **PDF**: https://arxiv.org/pdf/2609.29091
- **详细分析**: [[20_Research/Papers/具身智能/From_Passive_Execution_to_Active_Exploration_Agentic_Embodied_Manipulation_in_Realistic_Environments|From Passive Execution to Active Exploration: Agentic Embodied Manipulation in Realistic Environments]]
- **作者**: Shilin Ma, Chubin Zhang, Xulong Bai, Zifeng Gao, Shiyi Zhang, Yansong Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From Passive Execution to Active Exploration: Agentic Embodied Manipulation in Realistic Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in agentic systems have substantially enhanced the long-horizon capability of embodied manipulation. However, many existing frameworks still follow a passive execution paradigm, which limits their applicability to real-world scenarios involving textual semantic cues, distractors, and initially invisible targets. To bridge this gap, we propose an agent-based active exploration framework that enables robots to dynamically interact with the environment rather than merely execute predefined instructions. Specifically, our framework consists of three collaborative modules: a planning module for high-level task reasoning, a perception module for visual scene understanding, and an execution module for low-level manipulation. This design allows the robot to actively acquire task-relevant information, adapt its behavior based on environmental feedback, and complete manipulation tasks under partial observability. Furthermore, we introduce a fine-grained perception-execution interleaving strategy, which tightly couples visual feedback with skill execution to improve exploration robustness. We evaluate our method on a realistic Find-and-Place task, demonstrating its effectiveness in challenging environments where target objects must be actively discovered before manipulation.

</details>

---

### [[20_Research/Papers/具身智能/DA-GRD_Decision-Aware_Grasp-Relevant_Disambiguation_for_tactile_recovery_under_perception-to-execution_mismatches|DA-GRD: Decision-Aware Grasp-Relevant Disambiguation for tactile recovery under perception-to-execution mismatches]]

![[assets/2609.29065_figure.png|800]]

- **arXiv**: [2609.29065](https://arxiv.org/abs/2609.29065)
- **PDF**: https://arxiv.org/pdf/2609.29065
- **详细分析**: [[20_Research/Papers/具身智能/DA-GRD_Decision-Aware_Grasp-Relevant_Disambiguation_for_tactile_recovery_under_perception-to-execution_mismatches|DA-GRD: Decision-Aware Grasp-Relevant Disambiguation for tactile recovery under perception-to-execution mismatches]]
- **作者**: Haoran Wang, Yuteng Sun, Yuanjie Li, Ruofei Bai, Meng Yee, Chuah, Wenyu Liang, Jun Li, Wei-Yun Yau
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DA-GRD: Decision-Aware Grasp-Relevant Disambiguation for tactile recovery under perception-to-execution mismatches》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Grasping is a fundamental robotic capability that bridges perception and physical task execution. This paper studies grasp pose recovery under a perception-to-execution mismatch, where a grasp generated from visual perception may become spatially stale if the object moves before execution, using only sparse tactile interactions and no further visual observations. We propose DA-GRD, Decision-Aware Grasp-Relevant Disambiguation, which maintains a weighted planar belief over possible object configurations and selects tactile probes according to their ability to eliminate hypotheses and improve agreement among candidate task grasps. Rather than fully relocalizing the object, DA-GRD stops when the remaining hypotheses support a common executable grasp. In MuJoCo experiments on ten rigid objects with translations up to 5~cm and yaw perturbations up to $\pm45^\circ$, DA-GRD achieves an 84.7% physical lift success rate, compared with 9.1% for stale AnyGrasp, 21.2% for the original fix-scan baseline, and 63.7% for fix-scan method adapted with an SE(2) belief. DA-GRD also achieves a 57.3% Task conditioned Success rate. Across objects, it uses a success-average of 4.13 tactile probes over the ten per-object means, corresponding to a 72.5% reduction relative to the fixed 15-probe baselines. Real-world experiments on six objects achieve 71.7% physical lift success and 38.3% task-conditioned success with 4.20 probes on average. These results show that tactile sensing can recover task-relevant grasps under vision-off conditions with limited physical interaction, without requiring complete object localization.

</details>

---

### [[20_Research/Papers/具身智能/Simple_Torque-Observation_Alignment_for_Zero-Shot_Sim-to-Real_Grasping_with_a_Direct-Drive_Gripper|Simple Torque-Observation Alignment for Zero-Shot Sim-to-Real Grasping with a Direct-Drive Gripper]]

![[assets/2609.29031_figure.png|800]]

- **arXiv**: [2609.29031](https://arxiv.org/abs/2609.29031)
- **PDF**: https://arxiv.org/pdf/2609.29031
- **详细分析**: [[20_Research/Papers/具身智能/Simple_Torque-Observation_Alignment_for_Zero-Shot_Sim-to-Real_Grasping_with_a_Direct-Drive_Gripper|Simple Torque-Observation Alignment for Zero-Shot Sim-to-Real Grasping with a Direct-Drive Gripper]]
- **作者**: Doyoung Kim, Edgar Lee, Hyeonsun Park, Chunghyeon Lee, Chihyun Han, Uisu Hwang, Seokhwan Jeong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 2.4，强化学习 0.2，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Simple Torque-Observation Alignment for Zero-Shot Sim-to-Real Grasping with a Direct-Drive Gripper》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Torque observations in reinforcement learning remain challenging because simulated and measured torque differ in scale, offset, and noise. In this paper, we propose a simple torque observation alignment method for robots with direct-drive (DD) actuators, in which motor current maps linearly to joint torque through a motor-type-specific torque constant K_tau. First, dynamometer calibration identifies K_tau* and corrects the scale mismatch between simulated and real torque. Second, the method uses delta_tau(t) = tau(t) - tau(t-1) as the observation in both domains to eliminate the constant offset instead of using the direct torque tau(t), which carries a domain-dependent bias. Third, Gaussian noise obtained from the dynamometer measurement data is injected during the learning process. To validate the proposed method, we train a teacher-student grasping policy entirely in simulation and deploy the distilled student on a multifingered DD gripper. The deployed policy performs proprioceptive grasping using only joint positions and torque differences. We conduct an ablation study comparing the proposed method with alternative alignment variants on nine in-distribution (ID) objects. The proposed method achieves 100% grasp success. These results demonstrate that the proposed alignment method improves the robustness of zero-shot policy transfer on the DD gripper against real-world torque-observation mismatches.

</details>

---

### [[20_Research/Papers/具身智能/CAMP_Cooperative_Arm-Hand_Motion_Planning_in_Constrained_Spaces|CAMP: Cooperative Arm-Hand Motion Planning in Constrained Spaces]]

![[assets/2609.29021_figure.png|800]]

- **arXiv**: [2609.29021](https://arxiv.org/abs/2609.29021)
- **PDF**: https://arxiv.org/pdf/2609.29021
- **详细分析**: [[20_Research/Papers/具身智能/CAMP_Cooperative_Arm-Hand_Motion_Planning_in_Constrained_Spaces|CAMP: Cooperative Arm-Hand Motion Planning in Constrained Spaces]]
- **作者**: Ziyuan Wang, Yunlong Shan, Fei Mo, Sichao Liu, David Navarro-Alarcon, Jia Pan, Kosta Jovanovic, Xin Jiang, Peng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.9，机器人 1.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CAMP: Cooperative Arm-Hand Motion Planning in Constrained Spaces》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coordinated arm-hand motion planning is fundamental to dexterous robotic manipulation in complex and constrained environments. A straightforward solution is to decompose the problem into separate arm path planning and hand motion generation; however, this poses a dilemma: decomposition can miss feasible solutions that require coordinated arm-hand adaptation along the path. Alternatively, directly planning in the high-dimensional joint arm-hand configuration space captures such coupling but faces a substantially enlarged search space and nonconvex collision constraints. To characterize this coupling, we formulate feasible hand fibers that capture collision-free hand configurations for each arm configuration. Based on this formulation, we propose CAMP, a high-success and efficient cooperative arm-hand motion planner for constrained environments. CAMP constructs candidate trajectories through layered hand search with local arm relaxation, then compactly represents them using endpoint-preserving via-point movement primitives (VMPs) for coarse-to-fine joint optimization. Across six constrained simulation tasks, CAMP achieves 84.2-98.5% planning success, outperforming alternative planners with competitive efficiency. Ablation studies verify the contributions of arm relaxation, VMP representation, and coarse-to-fine optimization, while real-robot experiments demonstrate CAMP on constrained manipulation tasks. The project website is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Outcome-Sensitive_Motion_Search_for_Impact-Aware_Dexterous_Catching|Outcome-Sensitive Motion Search for Impact-Aware Dexterous Catching]]

![[assets/2609.29020_figure.png|800]]

- **arXiv**: [2609.29020](https://arxiv.org/abs/2609.29020)
- **PDF**: https://arxiv.org/pdf/2609.29020
- **详细分析**: [[20_Research/Papers/具身智能/Outcome-Sensitive_Motion_Search_for_Impact-Aware_Dexterous_Catching|Outcome-Sensitive Motion Search for Impact-Aware Dexterous Catching]]
- **作者**: Guorui Pei, Jinsong Wu, Songyuan Su, Jiaming Qi, Sichao Liu, David Navarro-Alarcon, Bin Liu, Peng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Outcome-Sensitive Motion Search for Impact-Aware Dexterous Catching》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skilled humans can catch fast-moving objects softly by coordinating interception, velocity matching, and follow-through to mitigate impact. Learning such impact-aware catching with reinforcement learning (RL), however, is challenging, as the policy must achieve reliable interception and grasping while regulating the sensitive transition into contact. Moreover, even a capable privileged-state RL teacher may not provide ideal demonstrations for a deployable imitation-learning (IL) student: teacher failures limit task coverage, while small variations in pre-contact motion can produce substantially different impact and grasping outcomes. We characterize this phenomenon through interventional outcome sensitivity and introduce the outcome-sensitive window (OSW) to guide targeted demonstration construction. Building on this formulation, we propose Outcome-Sensitive Motion Search, which learns a task-conditioned manifold of successful OSW motions and performs local geodesic search to refine successful teacher rollouts and repair task conditions where the teacher fails. We then validate candidate motions through complete rollouts under a calibrated IL-student action-error model and retain only successful executions as demonstrations. Extensive simulation experiments demonstrate that our method effectively repairs task conditions where the teacher fails and enables the resulting IL policy to outperform the privileged RL teacher in both catching success and impact mitigation.

</details>

---

### [[20_Research/Papers/具身智能/CALM_Current_Aligned_Link_Manipulation_for_Single_Arm_Oversized_Object_Lifting|CALM: Current Aligned Link Manipulation for Single Arm Oversized Object Lifting]]

![[assets/2609.29017_figure.png|800]]

- **arXiv**: [2609.29017](https://arxiv.org/abs/2609.29017)
- **PDF**: https://arxiv.org/pdf/2609.29017
- **详细分析**: [[20_Research/Papers/具身智能/CALM_Current_Aligned_Link_Manipulation_for_Single_Arm_Oversized_Object_Lifting|CALM: Current Aligned Link Manipulation for Single Arm Oversized Object Lifting]]
- **作者**: Jun Hu, Sihan Chen, Kosta Jovanovic, David Navarro-Alarcon, Xueqian Wang, Jia Pan, Peng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《CALM: Current Aligned Link Manipulation for Single Arm Oversized Object Lifting》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most robots manipulate objects solely with their end effectors, whereas humans flexibly leverage different body parts, such as the forearm and elbow, especially when handling oversized objects. Learning such whole-arm manipulation is chal-lenging due to long-horizon sparse rewards, limited contact sens-ing, and the sim-to-real gap in contact and actuator dynamics. To address these challenges, we propose Current-Aligned Link Manipulation, a framework for learning long-horizon contact-rich manipulation using motor current as joint load related feedback. Three stage-specific policies first learn repositioning, grasping, and lifting using privileged simulation information, and a stage router sequences them to generate complete task demonstrations. For sim-to-real transfer, a causal current mapper predicts physical motor current from simulated joint histories, aligning the actuator current observation between simulation and hardware. A unified student policy then learns from these demonstrations using only deployable sensor observations and is further refined with DAgger. The task policies are trained entirely in simulation, and the final student is deployed on hardware. Experiments demonstrate 76.2% (762/1000 trials) complete-task success in simulation and 73.3% success (22/30 trials) on the physical robot for sequential oversized-object lifting.

</details>

---

### [[20_Research/Papers/具身智能/ReVNM_Learning-Based_Visual_Navigation_from_a_Remote_Camera|ReVNM: Learning-Based Visual Navigation from a Remote Camera]]

![[assets/2609.28976_figure.png|800]]

- **arXiv**: [2609.28976](https://arxiv.org/abs/2609.28976)
- **PDF**: https://arxiv.org/pdf/2609.28976
- **详细分析**: [[20_Research/Papers/具身智能/ReVNM_Learning-Based_Visual_Navigation_from_a_Remote_Camera|ReVNM: Learning-Based Visual Navigation from a Remote Camera]]
- **作者**: Michikuni Eguchi, Kohei Honda, Masafumi Endo, Yasuhiro Yoshimura, Ryo Yonetani
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ReVNM: Learning-Based Visual Navigation from a Remote Camera》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual Navigation Models (VNMs) enable robots to navigate from egocentric visual observations without geometric localization and planning, but long-range navigation still requires pre-built maps. This paper presents the Remote Visual Navigation Model (ReVNM), which uses a single remote surveillance camera to serve as both an observation source and an implicit environmental map for visual navigation. While the use of remote cameras could eliminate the need for pre-built maps as well as onboard vision processing, their limited field of view instead of egocentric observations makes it hard to achieve collision-free navigation. The lack of existing data with diverse remote viewpoints, which are crucial for training robust VNMs, further complicates the challenge. In this work, we propose a learning-by-synthesis approach to address this two-fold challenge. Our ReVNM extends a state-of-the-art VNM architecture with an exocentric-to-egocentric (exo2ego) module that predicts an egocentric depth observation from remote-camera observations. This helps the VNM to plan a path while considering obstacles in front of the robot. Trained only on randomly generated worlds with diverse obstacle layouts and camera viewpoints, ReVNM can generalize well to real robot navigation without additional fine-tuning. Experiments in both simulation and real-world environments confirmed the effectiveness of the proposed approach.

</details>

---

### [[20_Research/Papers/具身智能/AquaMend_Minimal_Re-probing_and_Conditional_Rollback_for_Latent-Belief_Failures_in_Embodied_Agents|AquaMend: Minimal Re-probing and Conditional Rollback for Latent-Belief Failures in Embodied Agents]]

![[assets/2609.28973_first_page.png|800]]

- **arXiv**: [2609.28973](https://arxiv.org/abs/2609.28973)
- **PDF**: https://arxiv.org/pdf/2609.28973
- **详细分析**: [[20_Research/Papers/具身智能/AquaMend_Minimal_Re-probing_and_Conditional_Rollback_for_Latent-Belief_Failures_in_Embodied_Agents|AquaMend: Minimal Re-probing and Conditional Rollback for Latent-Belief Failures in Embodied Agents]]
- **作者**: Yufan Liu, Shang Luo, Yang Liu, Haoxuan Jia, Feiyu Han, Qian Li, Chen Li, Yingguang Yang, Chongyang Zhang, Hao Zheng, Kefu Xu, Bin Chong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《AquaMend: Minimal Re-probing and Conditional Rollback for Latent-Belief Failures in Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LatentProp-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical changes or sensing errors can invalidate embodied agents' task-relevant beliefs. AquaMend compares re-probing, rollback, and supported continuation on a probe-belief-action graph under an expected-loss objective covering sensing, physical recovery, and uncorrected failures. A joint posterior guides a one-step policy with conditional detection-power screening. The per-belief three-way optimum requires independence, separability, and fully resolving probes; the general policy has no global optimality guarantee. Across 32 paired scenarios in a self-constructed simulation benchmark, AquaMend recovers in 28/32 cases and reduces mean complete loss by 21.6% versus restart. Its paired loss difference from decision-theoretic troubleshooting (DTT) is not statistically significant after Holm correction. Against the all-candidate ablation, online decision time decreases by 12.3% overall but increases by 3.4% in the uncovered late stage.

</details>

---

### [[20_Research/Papers/强化学习/Sim-to-Real_Aware_End-to-End_Learning_Environment_for_Micromobility|Sim-to-Real Aware End-to-End Learning Environment for Micromobility]]

![[assets/2609.28969_figure.png|800]]

- **arXiv**: [2609.28969](https://arxiv.org/abs/2609.28969)
- **PDF**: https://arxiv.org/pdf/2609.28969
- **详细分析**: [[20_Research/Papers/强化学习/Sim-to-Real_Aware_End-to-End_Learning_Environment_for_Micromobility|Sim-to-Real Aware End-to-End Learning Environment for Micromobility]]
- **作者**: Shouma Amano, Takuya Azumi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Sim-to-Real Aware End-to-End Learning Environment for Micromobility》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While end-to-end autonomous driving systems show promise, their application to micromobility vehicles is hindered by simulators failing to capture specific kinematics, such as differential drives and omni-wheels. This paper pro- poses a sim-to-real-aware, vehicle-specific end-to-end learning environment for the WHILL Model CR on AWSIM and ROS 2. To minimize the sim-to-real gap, physical parameters are optimized via Bayesian optimization using real-world data, reducing trajectory errors across various driving scenarios. Additionally, this study introduces a synchronized architecture tailored for the stable training of world model-based agents. An end-to-end policy trained with DreamerV3 exhibited learning progress and achieved task completion in a simulated obstacle avoidance setting. Furthermore, this policy demonstrated direct sim-to-real transfer to the physical vehicle, enabling the vehicle to navigate around a cardboard box in a real-world corridor replica without fine-tuning. This paper provides a practical foundation for sim-to-real micromobility policy studies.

</details>

---

### [[20_Research/Papers/具身智能/Echo_in_the_Steps_Learning_Perceptive_Humanoid_Parkour_with_Gated_Memory|Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory]]

![[assets/2609.28960_figure.png|800]]

- **arXiv**: [2609.28960](https://arxiv.org/abs/2609.28960)
- **PDF**: https://arxiv.org/pdf/2609.28960
- **详细分析**: [[20_Research/Papers/具身智能/Echo_in_the_Steps_Learning_Perceptive_Humanoid_Parkour_with_Gated_Memory|Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory]]
- **作者**: Ming-Ju Lee, Zizhuo Wang, Shaoting Zhu, Haozhe Lou, Hang Zhao, Yiming Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Echo in the Steps: Learning Perceptive Humanoid Parkour with Gated Memory》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While recent advances in perceptive locomotion have enabled humanoid robots to traverse structured terrains, agile parkour in highly discontinuous environments remains an open challenge. In particular, crossing sparse footholds and narrow support regions requires precise foothold selection, effective use of visual observations, and consistent alternating foot placement during fast transitions. In this paper, we present a perceptive humanoid parkour framework that enables stable traversal across terrains with limited foothold availability using only onboard depth observations. The framework features a saliency-guided temporal perception module that combines a saliency prior with gated memory. It retains informative depth features across frames, enabling reliable foot placement from partial observations. By introducing an alternation loss, our symmetry regularization encourages alternating gait patterns and improves traversal robustness. Extensive experiments show that our method significantly improves success rate and foothold accuracy on challenging terrains in both simulation and the real world.

</details>

---

### [[20_Research/Papers/具身智能/TactileStep_Sole_Tactile_Learning_for_Regulating_Foot-Terrain_Interaction_in_Humanoid_Locomotion|TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion]]

![[assets/2609.28959_figure.png|800]]

- **arXiv**: [2609.28959](https://arxiv.org/abs/2609.28959)
- **PDF**: https://arxiv.org/pdf/2609.28959
- **详细分析**: [[20_Research/Papers/具身智能/TactileStep_Sole_Tactile_Learning_for_Regulating_Foot-Terrain_Interaction_in_Humanoid_Locomotion|TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion]]
- **作者**: Zizhuo Wang, Ming-ju Lee, Shaoting Zhu, Haozhe Lou, Hang Zhao, Yiming Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TactileStep: Sole Tactile Learning for Regulating Foot-Terrain Interaction in Humanoid Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid parkour policies can traverse various terrains, but task completion may mask challenges of harsh landings, edge contacts, and unstable stance contacts. Humans naturally regulate foot-terrain interaction through tactile feedback, modulating contact compliance according to terrain stiffness. This highlights a key domain gap between humans and humanoid robots: the absence of rich tactile sensing in most humanoid systems. We address this problem with TactileStep, a deployable tactile learning framework that brings sole pressure sensing into humanoid locomotion control for softer touchdowns and more stable support. TactileStep aligns tactile simulation with the real pressure insole, allowing the policy to learn from the same contact features available on hardware. During training, we use tactile and motion cues to recognize different foot-contact phases and apply phase-aware rewards that encourage safer landing and more stable stance. Evaluated in simulation and on a Unitree G1 humanoid across diverse terrains, TactileStep reduces peak touchdown force by up to 48.8% and peak A-weighted impact noise by up to 30.1 dB over a strong perceptive baseline, while increasing stance contact area by up to 23.8%.

</details>

---

### [[20_Research/Papers/具身智能/ActGaze_Learning_Action-Grounded_Gaze_through_Counterfactual_Visual_Interventions_for_High-Precision_Manipulation|ActGaze: Learning Action-Grounded Gaze through Counterfactual Visual Interventions for High-Precision Manipulation]]

![[assets/2609.28955_figure.png|800]]

- **arXiv**: [2609.28955](https://arxiv.org/abs/2609.28955)
- **PDF**: https://arxiv.org/pdf/2609.28955
- **详细分析**: [[20_Research/Papers/具身智能/ActGaze_Learning_Action-Grounded_Gaze_through_Counterfactual_Visual_Interventions_for_High-Precision_Manipulation|ActGaze: Learning Action-Grounded Gaze through Counterfactual Visual Interventions for High-Precision Manipulation]]
- **作者**: Jinxuan Zhu, Jiaheng Wang, Chao Tang, Mengfan Wang, Hao Wei, Shengbao Li, Hong Yin, Yiwen Gao, Chenrui Tie, Tingguang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ActGaze: Learning Action-Grounded Gaze through Counterfactual Visual Interventions for High-Precision Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language-Action (VLA) models often struggle with high-precision robotic manipulation. We attribute this limitation primarily to their visual attention being dispersed across task-irrelevant regions. To address this issue, we propose ActGaze, a training approach that guides VLA policies to gaze on task-relevant regions, much like humans gaze on critical visual cues while executing precise movements. Unlike prior methods that rely on external labels for gaze supervision, ActGaze derives spatial supervision directly from the VLA's own action objective by using counterfactual visual interventions to identify regions that are critical for action prediction. Extensive real-robot experiments on four high-precision robotic manipulation tasks demonstrate that ActGaze induces more focused visual attention on task-relevant regions and consistently outperforms the base VLA policy and other visual-grounding approaches.

</details>

---

### [[20_Research/Papers/强化学习/RoboRecover_Benchmarking_Robot_Policy_Recovery_under_Execution_Deviations|RoboRecover: Benchmarking Robot Policy Recovery under Execution Deviations]]

![[assets/2609.28952_figure.png|800]]

- **arXiv**: [2609.28952](https://arxiv.org/abs/2609.28952)
- **PDF**: https://arxiv.org/pdf/2609.28952
- **详细分析**: [[20_Research/Papers/强化学习/RoboRecover_Benchmarking_Robot_Policy_Recovery_under_Execution_Deviations|RoboRecover: Benchmarking Robot Policy Recovery under Execution Deviations]]
- **作者**: Yang Li, Chen Zhao, Zhuoran Wang, Jiankang Wang, Chao Shao, Yihan Lin, Haitao Shen, Jing Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《RoboRecover: Benchmarking Robot Policy Recovery under Execution Deviations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FRBench, LingBot-VLA, RePO-VLA, RoboEval, SmolVLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-policy benchmarks increasingly cover diverse tasks and preset out-of-distribution conditions, but typically evaluate complete trajectories from predefined initial states. These evaluations often focus on the initialized scene and the final outcome, while paying less attention to the dynamic interaction process. During closed-loop execution, actions and contacts can alter object relations and task progress, producing off-nominal intermediate states that need recovery. Recovery requires a policy to infer how task progress has changed, correct the relevant relations, and continue the original goal. We introduce RoboRecover, a benchmark for robot policy recovery under execution deviations. RoboRecover selects deviation states from trajectories, reconstructs them by replaying action prefixes, and evaluates policies on the original task. RoboRecover contains 2,000 scenarios across RoboTwin and LIBERO, with 1,000 scenarios and a fixed 800/200 train/test split on each platform. Results show that initial-state performance does not determine recovery performance and policies exhibit different recovery strengths across scenarios. Using its training split, RoboRecover further supports study on recovery interventions. RoboRecover establishes recovery from execution-induced intermediate states as a distinct dimension of robot policy evaluation.

</details>

---

### [[20_Research/Papers/具身智能/Streaming-WAM_Action-Conditioned_World-Action_Model_for_Asynchronous_Robot_Manipulation|Streaming-WAM: Action-Conditioned World-Action Model for Asynchronous Robot Manipulation]]

![[assets/2609.28927_figure.png|800]]

- **arXiv**: [2609.28927](https://arxiv.org/abs/2609.28927)
- **PDF**: https://arxiv.org/pdf/2609.28927
- **详细分析**: [[20_Research/Papers/具身智能/Streaming-WAM_Action-Conditioned_World-Action_Model_for_Asynchronous_Robot_Manipulation|Streaming-WAM: Action-Conditioned World-Action Model for Asynchronous Robot Manipulation]]
- **作者**: Xuyao Huang, Yixuan Wang, Zengyao Ye, Boyuan Zhao, Chenyang Yu, Haoran Wen, Zhijie Deng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Streaming-WAM: Action-Conditioned World-Action Model for Asynchronous Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GigaWorld, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models (WAMs) that use future visual prediction at inference time incur substantial generation costs. Asynchronous execution reduces waiting by overlapping inference with robot motion, but visual predictions used for subsequent action generation must anticipate the effects of actions already scheduled for execution during inference. We introduce Streaming-WAM, which couples action-conditioned world modeling with asynchronous robot control to account for committed actions in future visual prediction. At each streaming update, the model conditions future visual prediction on the latest observation and the committed actions, which form the fixed prefix of the next action chunk. The resulting action-conditioned visual features guide generation of the remaining actions within the same joint update, so the continuation is informed by the scene changes expected during execution of the fixed prefix. On LIBERO, Streaming-WAM achieves an average success rate of 98.35\% and reduces mean episode time by a factor of 2.93 relative to Fast-WAM. On the real-world Stamp Paper task, mean episode time falls from 90 s with synchronous Joint-WAM to 38 s with Streaming-WAM. These results show that Streaming-WAM supports efficient asynchronous control while maintaining high task success rates.

</details>

---

### [[20_Research/Papers/机器人/Koopman-Accelerated_Model-Based_Diffusion_for_Real-Time_Robot_Control|Koopman-Accelerated Model-Based Diffusion for Real-Time Robot Control]]

![[assets/2609.28920_figure.png|800]]

- **arXiv**: [2609.28920](https://arxiv.org/abs/2609.28920)
- **PDF**: https://arxiv.org/pdf/2609.28920
- **详细分析**: [[20_Research/Papers/机器人/Koopman-Accelerated_Model-Based_Diffusion_for_Real-Time_Robot_Control|Koopman-Accelerated Model-Based Diffusion for Real-Time Robot Control]]
- **作者**: Bohyeong Pak, Kangmin Lee, Sanghyun Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Koopman-Accelerated Model-Based Diffusion for Real-Time Robot Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional model-based diffusion (MBD) achieves effective trajectory optimization by leveraging noise annealing. However, its high computational cost, primarily arising from repeated rollouts of the plant dynamics, has largely confined its use to offline settings. To address this limitation, this paper proposes bilinear Koopman model-based diffusion (BK-MBD). The proposed method lifts the robot's state into a high-dimensional space only once per control step and propagates all candidates in the lifted space thereafter, so each rollout reduces to a fixed number of matrix-vector multiplications. The lifted dynamics are bilinear, allowing the predicted input gain to vary with the robot's configuration, which a linear lifted model cannot represent. In simulation, BK-MBD completed each planning update in at most 14.7 ms within a 50 ms control period and reached the goal on every trial, whereas a linear lift almost never did. The annealed schedule improves closed-loop accuracy over fixed-noise schedules under the learned rollout. Under the exact rollout, both the annealed and fixed-narrow schedules reach every goal, indicating that annealing reduces sensitivity to surrogate-model error. BK-MBD also threaded a passage that no single convex region covers, whereas a convexified bilinear controller rarely succeeded. On a physical manipulator, BK-MBD tracked an initially unknown moving target within the control period and was the only method that met both the tracking task and the deadline. The project page is available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/Fly,_Drive,_Reconfigure_A_Modular_Reconfigurable_Aerial-Ground_Platform_for_Field_Operations|Fly, Drive, Reconfigure: A Modular Reconfigurable Aerial-Ground Platform for Field Operations]]

![[assets/2609.28887_figure.png|800]]

- **arXiv**: [2609.28887](https://arxiv.org/abs/2609.28887)
- **PDF**: https://arxiv.org/pdf/2609.28887
- **详细分析**: [[20_Research/Papers/机器人/Fly,_Drive,_Reconfigure_A_Modular_Reconfigurable_Aerial-Ground_Platform_for_Field_Operations|Fly, Drive, Reconfigure: A Modular Reconfigurable Aerial-Ground Platform for Field Operations]]
- **作者**: Li-Yu Lo, Yanbaihui Liu, Chengchuan Shu, Tyler Harris, Jonathan Ryan, Boyuan Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Fly, Drive, Reconfigure: A Modular Reconfigurable Aerial-Ground Platform for Field Operations》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Heterogeneous robot teams distribute complementary capabilities across specialized agents, but their physical roles and capacities typically remain fixed throughout a mission. We present HARP, a Heterogeneous Aerial Robotic modules Platform in which independently deployable aerial robots physically reconfigure to compose their capabilities for field operations. HARP comprises sensor-equipped scouts, flydrive rover modules, and task-specific payload modules. Scouts map the environment and inform an energy-aware planner that jointly selects routes and air-ground mobility modes. Rover and payload modules fly independently across terrain that constrains ground travel, then autonomously assemble into a cooperative ground vehicle for energy-efficient payload transport. Motivated by environmental sampling in remote and difficult-to-traverse regions, we evaluate HARP through field experiments spanning sensing, planning, reconfiguration, airground mobility, payload transport, and task execution. We further conduct module-level deployment tests on the Greenland Ice Sheet toward future autonomous missions. HARP demonstrates how heterogeneous robot teams can adapt not only their actions, but also how their physical capabilities are composed during a mission.

</details>

---

### [[20_Research/Papers/强化学习/Online_Sim-to-Real_Adaptation_via_Closed-Loop_System_Modeling|Online Sim-to-Real Adaptation via Closed-Loop System Modeling]]

![[assets/2609.28878_figure.png|800]]

- **arXiv**: [2609.28878](https://arxiv.org/abs/2609.28878)
- **PDF**: https://arxiv.org/pdf/2609.28878
- **详细分析**: [[20_Research/Papers/强化学习/Online_Sim-to-Real_Adaptation_via_Closed-Loop_System_Modeling|Online Sim-to-Real Adaptation via Closed-Loop System Modeling]]
- **作者**: Yuhao Huang, Samuel A. Moore, Boyuan Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.2（加权：具身智能 1.5，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Online Sim-to-Real Adaptation via Closed-Loop System Modeling》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sim-to-real transfer has made substantial progress, but can still produce controllers that remain stable and functional on hardware while suffering from degraded tracking accuracy due to residual dynamics mismatch. Correcting these errors typically requires identifying the underlying system dynamics, adapting the control policy, or returning to simulation for additional training and finetuning, all of which can require substantial data and computation. We propose OSRAM (Online Sim-to-Real Adaptation via Closed-Loop System Modeling), a framework that instead adapts the reference commands provided to an existing controller. OSRAM treats the deployed robot and its policy as a unified closed-loop dynamical system and learns its task-level command-response behavior directly from tracking observations. A closed-loop dynamics model is meta-trained across randomized dynamics in simulation and rapidly finetuned after deployment using limited real-world interaction. The adapted model is then used to optimize future reference commands while leaving the underlying control policy unchanged. We evaluate OSRAM on bipedal velocity tracking and loco-manipulation in simulation and on hardware. Results show that closed-loop modeling improves prediction and tracking accuracy under unseen dynamics, while online reference adaptation reduces residual sim-to-real tracking errors across different control objectives and hardware configurations. These results demonstrate that adapting the behavior of the robot-policy closed loop provides a practical alternative to finetuning the policy or identifying the full physical dynamics for sim-to-real transfer. More information can be found at this http URL .

</details>

---

### [[20_Research/Papers/具身智能/FlyCNS_Connectome-Grounded_Information_Organization_for_Communication-Constrained_Embodied_Control|FlyCNS: Connectome-Grounded Information Organization for Communication-Constrained Embodied Control]]

![[assets/2609.28816_figure.png|800]]

- **arXiv**: [2609.28816](https://arxiv.org/abs/2609.28816)
- **PDF**: https://arxiv.org/pdf/2609.28816
- **详细分析**: [[20_Research/Papers/具身智能/FlyCNS_Connectome-Grounded_Information_Organization_for_Communication-Constrained_Embodied_Control|FlyCNS: Connectome-Grounded Information Organization for Communication-Constrained Embodied Control]]
- **作者**: Jinchang Zhang, Jiakai Lin, Guoyu Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《FlyCNS: Connectome-Grounded Information Organization for Communication-Constrained Embodied Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic bodies are inherently distributed in sensing and actuation, yet learning-based control still commonly relies on centralized information processing. This work studies the problem of information organization in communication-constrained embodied control: which computations should remain local, and which information is worth transmitting for whole-body coordination. We propose FlyCNS, an embodied information-organization framework inspired by the Drosophila brain--nerve-cord connectome. FlyCNS preserves local sensorimotor computation within each limb and enables selective long-range communication through separate ascending and descending routing pathways. From a real connectome, FlyCNS extracts the directional structural complexity of these two pathway types and uses it as a weak prior over communication allocation, while message content, transmission timing, and locomotion policies remain task-adaptive and are learned through reinforcement learning. In Unitree Go1 simulation, FlyCNS exhibits more graceful performance degradation as the communication budget is tightened. Under the most restrictive setting, it uses only about 21--22\% of the communication of the full-communication reference, while still maintaining a tracking score of approximately 0.882 under both command protocols, with a gap of no more than 6.1\% from the full-communication reference. These results indicate that real neural connectomes can inform not only the structural design of control networks, but also provide transferable inductive biases for information organization across embodiments, guiding robots in balancing local computation and long-range coordination under limited communication resources.

</details>

---

### [[20_Research/Papers/具身智能/An_Analysis_of_Streaming_Deep_Reinforcement_Learning_for_Adaptive_Continual_Learning_in_Robotics|An Analysis of Streaming Deep Reinforcement Learning for Adaptive Continual Learning in Robotics]]

![[assets/2609.28807_figure.png|800]]

- **arXiv**: [2609.28807](https://arxiv.org/abs/2609.28807)
- **PDF**: https://arxiv.org/pdf/2609.28807
- **详细分析**: [[20_Research/Papers/具身智能/An_Analysis_of_Streaming_Deep_Reinforcement_Learning_for_Adaptive_Continual_Learning_in_Robotics|An Analysis of Streaming Deep Reinforcement Learning for Adaptive Continual Learning in Robotics]]
- **作者**: Teeratham Vitchutripop, Alyssa Quarles, Wenhe Zhang, Richard Xue, Daniel Rakita
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 4.5（加权：具身智能 1.2，强化学习 1.6，机器人 1.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《An Analysis of Streaming Deep Reinforcement Learning for Adaptive Continual Learning in Robotics》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Over the course of a lifetime, robots may encounter novel scenarios unaccounted for in its original training that result in performance degradation. One common approach to mitigating this issue is to further grow the offline training dataset in hopes of producing a policy robust to these changes. In contrast, biological learning occurs moment-to-moment via a stream of experience, unlike the predominantly batch-based and offline nature of deep learning. Although recent works show the feasibility of stream-based deep reinforcement learning, where updates use only the latest experience, none have shown it to be a viable continual learning framework for adapting robotic policies to unseen changes. In this paper, we present the first analysis of streaming deep reinforcement learning for adaptive continual learning in robotics. In particular, we show that, following an initial pretraining phase, streaming deep RL can enable a robot to successfully adapt to unforeseen changes to itself, its environment, or goals. Our primary experiments within quadruped locomotion demonstrate that a deep neural network robotic policy with certain optimizers and plasticity loss mitigation techniques can successfully leverage domain task knowledge from its pretraining to quickly adapt online to diverse changes via stream learning, outperforming batch-based on-policy methods and improving task success rates by up to 90% over the pretrained policy. Furthermore, we perform additional evaluations on robotic manipulation tasks to determine if our previous observations extend to different robotic morphologies and scenarios. Our results show that the successes observed in quadruped locomotion can be partially realized in manipulation with stability and performance limitations. We conclude with a discussion on the limitations of our work and its implications for the future of continual robot learning.

</details>

---

### [[20_Research/Papers/机器人/Human-in-the-Loop_Geospatial_Annotation_for_Rapid_Dataset_Construction_in_Field-Deployed_UAV_Systems|Human-in-the-Loop Geospatial Annotation for Rapid Dataset Construction in Field-Deployed UAV Systems]]

![[assets/2609.28767_figure.png|800]]

- **arXiv**: [2609.28767](https://arxiv.org/abs/2609.28767)
- **PDF**: https://arxiv.org/pdf/2609.28767
- **详细分析**: [[20_Research/Papers/机器人/Human-in-the-Loop_Geospatial_Annotation_for_Rapid_Dataset_Construction_in_Field-Deployed_UAV_Systems|Human-in-the-Loop Geospatial Annotation for Rapid Dataset Construction in Field-Deployed UAV Systems]]
- **作者**: Morgan Masters, Nikolaas Bender, T. Luca Altaffer, Colleen Josephson, Steve McGuire
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Human-in-the-Loop Geospatial Annotation for Rapid Dataset Construction in Field-Deployed UAV Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world perception systems must adapt to changing environments, but manual image annotation cannot scale to field data volumes. We present BirdsEye, which shifts expert annotation from images to the field: an operator records target locations in world coordinates using RTK positioning and calibrated projective geometry propagates each observation to all frames where the target is visible. To quantify how well physical annotations align with image observations, we derive a first-order mapping from camera-pose uncertainty to pixel uncertainty and validate it against Monte Carlo simulation. This mapping is linear in the six per-axis pose variances, so it inverts into a sensor design tool: we give a sufficient condition converting an annotation tolerance into a convex set of admissible pose-noise budgets, a closed-form largest admissible scaling of a deployed sensor suite, and a unique per-axis pose specification under an equal-budget-share allocation. We also analyze the planar-surface approximation underlying the projection, which holds up to 10 degrees of terrain slope. By direct measurement, we show that system projection accuracy is sub-decimeter (sub-30 pixel) at AGL altitudes of 10-20m under conditions excluding sustained yawing. During an in-field case study across three agricultural sites, two field workers produced 12,524 annotated frames carrying 55,600 labels in roughly 12 hours (25.5x per-worker rate increase over manual labeling). Detectors trained on imagery collected by this workflow recovered 56-89% of in-view surveyed targets at a geographically distinct farm, at pre-registered operating points; human review of the leading configuration estimates detection precision at 83-87%, spanning three tie-break conventions for clusters carrying contradictory human verdicts.

</details>

---

### [[20_Research/Papers/机器人/OA-MPPI_Occlusion-Aware_Model_Predictive_Path_Integral_Control_for_UAV_Flight|OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight]]

![[assets/2609.28709_figure.png|800]]

- **arXiv**: [2609.28709](https://arxiv.org/abs/2609.28709)
- **PDF**: https://arxiv.org/pdf/2609.28709
- **详细分析**: [[20_Research/Papers/机器人/OA-MPPI_Occlusion-Aware_Model_Predictive_Path_Integral_Control_for_UAV_Flight|OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight]]
- **作者**: Vittorio Palladino, Teaya Yang, Ruiqi Zhang, Mark W. Mueller
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《OA-MPPI: Occlusion-Aware Model Predictive Path Integral Control for UAV Flight》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous UAV flight through cluttered and partially unknown environments requires reasoning not only about observed obstacles but also about occluded regions that the sensor cannot observe. We present OA-MPPI, an obstacle- and occlusion-aware extension of Model Predictive Path Integral (MPPI) control for quadrotor flight that accounts for potential moving agents emerging from these regions into the vehicle's path. At every planning step, we extract a 3D occlusion boundary from the online occupancy map and use it to model the regions that hidden agents could reach over the prediction horizon. We penalize trajectories that enter these expanding regions within MPPI rollouts generated using nonlinear quadrotor dynamics and accounting for individual rotor thrust limits. We validate the proposed approach in simulation and hardware flight experiments, with the complete pipeline running onboard the vehicle in real time. Results show increased clearance from occlusion boundaries compared to baseline MPPI in both settings, as well as avoidance of an agent emerging from occlusion in simulation.

</details>

---

### [[20_Research/Papers/强化学习/Morphometric_Imitation_From_Morphology_and_Contact_Aware_Hand_Retargeting_to_Sim-to-Real_Visuomotor_Policy|Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy]]

![[assets/2609.28660_figure.png|800]]

- **arXiv**: [2609.28660](https://arxiv.org/abs/2609.28660)
- **PDF**: https://arxiv.org/pdf/2609.28660
- **详细分析**: [[20_Research/Papers/强化学习/Morphometric_Imitation_From_Morphology_and_Contact_Aware_Hand_Retargeting_to_Sim-to-Real_Visuomotor_Policy|Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy]]
- **作者**: Tara Sadjadpour, Siming He, C.K. Wolfe, Haozhi Qi, Lea Wilken, S. Shankar Sastry, Claire Tomlin, Jitendra Malik
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Morphometric Imitation: From Morphology and Contact Aware Hand Retargeting to Sim-to-Real Visuomotor Policy》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human hand-object interactions (HOIs) provide a rich source of demonstrations for dexterous manipulation, but learning directly from them presents challenges in bridging morphology gaps, ensuring dynamical feasibility, and sim-to-real deployment. We present Morphometric Imitation, a three-stage framework that transforms reconstructed HOIs into zero-shot sim-to-real visuomotor policies. First, morphometric optimization (MMO) kinematically retargets human motion across hand morphologies while preserving demonstrated contacts. Second, residual reinforcement learning (RL) refines the kinematic reference using object pose and contact information from the human motion to produce dynamically feasible robot demonstrations. Third, these demonstrations are distilled into visuomotor policies. Across three robot hands and ten HOIs, MMO improves contact F1 over the strongest of five baselines by at least 8 points for every hand, while also improving the success rate of downstream dynamic retargeting by as much as 35 points. Ablations on the residual RL show complementary benefits from using object pose and contact information. Finally, the visuomotor policies achieve 89.3% zero-shot success in 300 real-world trials on 30 objects. Project page: $\href{ this https URL }{\text{this https URL}}$

</details>

---

### [[20_Research/Papers/大模型/Know_Your_Body_A_Harness_for_Direct_and_Self-Improving_Robot_Control_with_VLMs|Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs]]

![[assets/2609.28530_figure.png|800]]

- **arXiv**: [2609.28530](https://arxiv.org/abs/2609.28530)
- **PDF**: https://arxiv.org/pdf/2609.28530
- **详细分析**: [[20_Research/Papers/大模型/Know_Your_Body_A_Harness_for_Direct_and_Self-Improving_Robot_Control_with_VLMs|Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs]]
- **作者**: Zeyu Lou, Yanhong Zeng, Yong Wang, Chenyang Si
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A general-purpose vision-language model can understand a task goal without knowing how a particular robot's motion and functional parts produce the intended effect. We introduce KnowBody, a harness that makes these action-relevant body relations explicit, queryable, and revisable while keeping the model weights frozen. Initialized from one off-task trajectory, a partial body model guides action selection and the interpretation of past interactions. New evidence refines the model, and knowledge dependent on revised body estimates is rechecked before reuse. Across 32 fixed-budget trials on four real-robot tasks, initialized KnowBody achieves 75% completion versus 25% for the native harness and requires fewer planner rounds on successful trials in tasks completed by both. With persistent updates enabled, planner rounds decrease by 29-53% from the first to the fifth recorded success.

</details>

---
