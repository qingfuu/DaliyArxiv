# cs.CV | Computer Vision and Pattern Recognition | 2026-11-02

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/具身智能/REA_A_Routed_Embodied_Agent_Runtime_for_Asynchronous_Brain-Cerebellum_Control|REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control]]

![[assets/2610.42053_figure.png|800]]

- **arXiv**: [2610.42053](https://arxiv.org/abs/2610.42053)
- **PDF**: https://arxiv.org/pdf/2610.42053
- **详细分析**: [[20_Research/Papers/具身智能/REA_A_Routed_Embodied_Agent_Runtime_for_Asynchronous_Brain-Cerebellum_Control|REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control]]
- **作者**: Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, Haoyuan Chen, Zhenglin Wan, Hexin Wang, Wangbo Zhao, Yang You
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 2.1，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ContactGraspNet, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative brain (foundation models) with a reactive cerebellum (fast policies) seems natural for embodied systems, two obstacles remain: methods are built and scored on incompatible stacks, and their asynchronous coordination is difficult. For example, an agent that calls the VLA in the agentic loop can stall the fast execution, while a VLA that calls the agent on errors tends to re-trigger fallbacks repeatedly or completely miss silent failures. To address this, we propose REA (Routed Embodied Agent), a unified runtime where a deliberative System 2, an embodied router System 1 and reactive System 0 policies cooperate under a single golden rule - no running policy waits on the brain. Instead of querying the brain at each failure, REA employs a route memory that stores each policy's measured success ahead of time, a boundary-triggered judge gate that consults the brain on policy execution, and a shared-budget escalation ladder for bounded recovery. Evaluated on 3,000 test episodes across 60 LIBERO-Pro tasks, REA reaches 95.9% success and beats the best single-agent baseline in its own policy pool (94.7%) while reducing control steps by 25% and control time by 17%. In a separate 100-episode RoboTwin 2.0 study, REA achieves 84% success with VLA policies and 86% with VLA+code, compared with 80% for the strongest single VLA baseline MEDex. These results demonstrate learned and programmatic policies operating within the same runtime. REA also transfers to BEHAVIOR-1K and a real Unitree G1 humanoid, achieving the highest observed success among the compared methods.

</details>

---

### [[20_Research/Papers/大模型/Movens-Zero_Scaling_Humanoid_Motion_Foundation_Models_with_Large-Scale_Human_Videos|Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos]]

![[assets/2610.41877_figure.png|800]]

- **arXiv**: [2610.41877](https://arxiv.org/abs/2610.41877)
- **PDF**: https://arxiv.org/pdf/2610.41877
- **详细分析**: [[20_Research/Papers/大模型/Movens-Zero_Scaling_Humanoid_Motion_Foundation_Models_with_Large-Scale_Human_Videos|Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos]]
- **作者**: Wendong Bu, Tinghong Ye, Qizhou Wang, Jiacheng Li, Zhiqi Ge, Yuze Lin, Zhongqi Yue, Yi Su, Jingyu Wang, Kai Shen, Jingdong Liu, Chengyuan Deng...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling humanoid motion foundation models is constrained by the scarcity of diverse, robot-executable data and by the difficulty of jointly learning from heterogeneous multimodal inputs while supporting real-time closed-loop control. We present Movens-5M, constructed from raw Internet videos through clip generation, quality filtering, semantic annotation, motion recovery, and physical refinement with humanoid retargeting and execution verification. It contains 15 million human-motion sequences and 5 million physically executable humanoid-motion sequences spanning over 10,000 hours, aligned with text, RGB video, speech, and music. Building on this data, we introduce Movens-Zero, a scalable understanding-generation-execution architecture that supports joint learning across modalities and real-time closed-loop execution. Task-mixed flow-matching training jointly optimizes a single action expert across seven generation tasks, enabling direct motion generation from text, speech, music, and video. Multimodal Real-Time Chunking connects overlapping chunks under continuously updated instructions and robot states for continuous closed-loop execution. We further introduce Movens-Intent, a four-track benchmark with 8,192 expert-verified condition-motion pairs across text, speech, music, and video. Experiments show consistent gains across all four modalities when scaling execution-verified data from 1% to 100% and action-expert capacity from 64M to 911M parameters, while demonstrating that data quality and cross-modal supervision improve generation and execution.

</details>

---

### [[20_Research/Papers/机器人/DrawSplat_Atlanta_World-Guided_Implicit_Gaussian_SLAM_for_Indoor_Reconstruction|DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction]]

![[assets/2610.41602_figure.png|800]]

- **arXiv**: [2610.41602](https://arxiv.org/abs/2610.41602)
- **PDF**: https://arxiv.org/pdf/2610.41602
- **详细分析**: [[20_Research/Papers/机器人/DrawSplat_Atlanta_World-Guided_Implicit_Gaussian_SLAM_for_Indoor_Reconstruction|DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction]]
- **作者**: Fan Zhu, Zhisong Xu, Ziyu Chen, Zhenjun Zhao, Takayuki Okatani
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.CV

#### 研究背景与动机

《DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

RGB-D SLAM requires accurate online tracking, high-quality rendering, and geometrically consistent reconstruction. Existing Gaussian SLAM methods mainly optimize Gaussian primitives with photometric, depth, or local frame-to-model constraints, which are often insufficient in indoor scenes with weak textures, large planar structures, noisy depth, and long trajectories. The resulting maps may suffer from pose drift, surface thickness artifacts, noisy normals, and blurred structural boundaries. We propose DrawSplat, an Atlanta World-guided implicit Gaussian SLAM framework for indoor reconstruction. DrawSplat follows a drawing-like process: explicit point-line geometry first sketches the structural layout, and implicit neural Gaussians then fill in high-fidelity appearance and continuous geometric details. It estimates camera poses, sparse geometry, and gravity direction through point-line joint tracking, infers structural planes from tracked lines using the shared-gravity component of the Atlanta World prior, and converts them into differentiable regularization terms on Gaussian centers and normals. To improve compactness and efficiency, DrawSplat further combines an anchor-based implicit neural Gaussian representation with adaptive structural sampling, which allocates Gaussian capacity to structurally informative regions. Experiments on multiple datasets show that DrawSplat achieves robust tracking, high-fidelity rendering, and strong geometric reconstruction among Gaussian-based SLAM systems, while maintaining a practical balance among quality, efficiency, and model size.

</details>

---

### [[20_Research/Papers/具身智能/SACQ_Structure-Aware_Codebook_Quantization_for_Ultra-Low-Bit_Vision-Language-Action_Models|SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models]]

![[assets/2610.41408_figure.png|800]]

- **arXiv**: [2610.41408](https://arxiv.org/abs/2610.41408)
- **PDF**: https://arxiv.org/pdf/2610.41408
- **详细分析**: [[20_Research/Papers/具身智能/SACQ_Structure-Aware_Codebook_Quantization_for_Ultra-Low-Bit_Vision-Language-Action_Models|SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models]]
- **作者**: Haesung Lee, Insu Han
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HBVLA, OpenVLA, QVLA, QuantVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms. Weight quantization is a natural remedy, yet post-training quantization (PTQ) recipes inherited from large language models degrade when applied to VLAs at ultra-low precision. Existing low-bit PTQ methods often fail to explicitly account for the structure of downstream operations and allocate precision without considering its effect on the policy actions. We introduce SACQ, an ultra- low-bit weight-only vector-codebook quantization framework for VLAs. SACQ combines (1) structure-aware codebook fitting with role-specific quadratic metrics that reflect input statistics and downstream sensitivity; (2) action-aware mixed-bit allocation based on the increase in final-action error as individual layers are compressed; and (3) two-stage post-quantization refinement that reassigns codeword indices with second-order error compensation and calibrates codebooks and row-group scales against the decoded action. Using GR00T N1.7, SACQ achieves 93.85% average success across four LIBERO suites at 1.5 bits per language/action weight while reducing model memory by 4.83x. With INT8 activation quantization and low-precision attention, it retains 93.55% success while running 1.51x faster than BF16. On SimplER, SACQ further achieves 63.76% and 52.27% success under Visual Matching and Variant Aggregation at 2 bits per language/action weight, compared to 58.90% and 53.45% for BF16, respectively.

</details>

---

### [[20_Research/Papers/具身智能/Joint-Health-Aware_Reinforcement_Learning_for_Robust_Robot_Control_Under_Actuator_Degradation|Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation]]

![[assets/2610.41348_figure.png|800]]

- **arXiv**: [2610.41348](https://arxiv.org/abs/2610.41348)
- **PDF**: https://arxiv.org/pdf/2610.41348
- **详细分析**: [[20_Research/Papers/具身智能/Joint-Health-Aware_Reinforcement_Learning_for_Robust_Robot_Control_Under_Actuator_Degradation|Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation]]
- **作者**: Haifa Zhang, Yijing Wang, Zhiqiang Zuo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HealthNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots deployed in unstructured environments are susceptible to actuator-authority degradation, which reduces the effective control authority of individual actuators and can cause reinforcement learning policies trained under nominal dynamics to fail. Existing robustness approaches rely on discrete fault labels, broad domain randomization, or global latent variables, often without explicitly modeling continuous per-joint residual actuation capability. We propose a joint-health-aware reinforcement learning framework for robust robot control under simulated actuator degradation. Our framework encodes actuator condition in a continuous joint-health vector and models degradation as multiplicative attenuation of executed actions. A dedicated HealthNet estimator infers per-joint health from recent observations and actions, allowing the policy to redistribute control effort across healthy and degraded joints. We evaluate the method on Walker, Go2, Cassie, and Panda-based ManiSkill manipulation tasks under diverse degradation masks and severity levels. The method outperforms nominal and degradation-trained no-health baselines on the main evaluated metrics. Relative to the nominal baseline, task-level locomotion returns improve by up to 250.1\% and manipulation success rates by up to 15.2 percentage points; in the high-degradation Cassie group, return increases from 3.94 to 40.50 (+928.0\%). Ablations support the contribution of per-joint health estimation, action-degradation modeling, and health-conditioned control.

</details>

---

### [[20_Research/Papers/大模型/TinyAstral_Transferring_Self-Evolving_Harnesses_to_Tiny_Generalist_Manipulation_Agents|TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents]]

![[assets/2610.41216_figure.png|800]]

- **arXiv**: [2610.41216](https://arxiv.org/abs/2610.41216)
- **PDF**: https://arxiv.org/pdf/2610.41216
- **详细分析**: [[20_Research/Papers/大模型/TinyAstral_Transferring_Self-Evolving_Harnesses_to_Tiny_Generalist_Manipulation_Agents|TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents]]
- **作者**: Kehong Gong, Xiaoxu Zheng, Guanli Hou, Seunghun Lee, Mengqi Guo, Runjia Tan, Zhengyu Wen, Qi Wang, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents》归入 大模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot agents built on vision-language models depend on both the planner and its harness: the tools, feedback, memory, and recovery logic around it. Can improvements to a large teacher's harness be carried into a compact agent with lower inference compute cost? We present TinyAstral, a two-stage approach. We first freeze an open-weight teacher and improve its harness through recursive self-improvement (RSI): frontier LLM agents read the teacher's trajectories and propose harness edits, and each edit is accepted only if it passes a paired statistical test. We then freeze the final harness, collect teacher trajectories with reasoning and failure recovery, and distill a small student that replaces the teacher in the same harness. On RoboTwin, harness evolution raises the teacher's success from 33.4% to 63.6%; the final 4B student reaches 62.8%. Across four harness versions, distilled 4B students score close to their corresponding teachers, and later versions yield stronger students, showing that harness evolution gains carry into compact models. The harness gains also transfer to other frozen planners without retraining. On identical episodes, the final 4B student outperforms open 4B agents, the open 27B harness-RSI model SenseNova-RoboRSI, and our own teacher model placed in three competitors' harnesses. It stays close to its teacher on all three training benchmarks, and on three benchmarks never used for RSI or training it scores close to a 552B planner running the same harness. On the measured deployment episodes, it uses about one fifth of its teacher's accelerator time.

</details>

---

### [[20_Research/Papers/机器人/FlowMoDE_Coarse-to-fine_Flow_Matching_for_Detail-aware_Sim-to-Real_Monocular_Depth_Estimation|FlowMoDE: Coarse-to-fine Flow Matching for Detail-aware Sim-to-Real Monocular Depth Estimation]]

![[assets/2610.41190_figure.png|800]]

- **arXiv**: [2610.41190](https://arxiv.org/abs/2610.41190)
- **PDF**: https://arxiv.org/pdf/2610.41190
- **详细分析**: [[20_Research/Papers/机器人/FlowMoDE_Coarse-to-fine_Flow_Matching_for_Detail-aware_Sim-to-Real_Monocular_Depth_Estimation|FlowMoDE: Coarse-to-fine Flow Matching for Detail-aware Sim-to-Real Monocular Depth Estimation]]
- **作者**: Liangjing Shao, Wanhao Liu, Jinsong Lin, Zhiwei Fang, Hongliang Ren
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《FlowMoDE: Coarse-to-fine Flow Matching for Detail-aware Sim-to-Real Monocular Depth Estimation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular depth estimation is a fundamental capability for 3D spatial perception in robotic and intelligent systems. While data-driven discriminative methods have achieved compelling performance for monocular depth estimation, generative approaches can reconstruct fine structural details with stronger generalization. However, most existing generative diffusion models suffer from low inference efficiency caused by multi-step sampling, whereas single-step diffusion models struggle to recover high-fidelity depth maps. To mitigate these drawbacks, this paper presents FlowMoDE, a coarse-to-fine flow-matching-based framework for efficient, structure-aware monocular depth estimation supporting sim-to-real and cross-scene generalization. The core architecture first conducts coarse-level decoding conditioned on diffused features extracted from a pre-trained semantic encoder, and subsequently restores fine-grained structural patterns via expanded decoding layers. Trained exclusively on a single synthetic indoor dataset, our proposed method outperforms prior methods across five real-world indoor and outdoor datasets, yielding an average 14.1% reduction in relative error against state-of-the-art works as well as 9.9\% reduction in chamfer distance for point cloud reconstruction. We further validate the generalization capability of FlowMoDE on realistic robotic scenes, with qualitative comparisons against state-of-the-art methods. The project page is https://flowmode-shao.netlify.app/

</details>

---

### [[20_Research/Papers/具身智能/MotorSense_A_Video-EMG_Dataset_of_Motoric_Representations_for_Action_Understanding|MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding]]

![[assets/2610.41127_figure.png|800]]

- **arXiv**: [2610.41127](https://arxiv.org/abs/2610.41127)
- **PDF**: https://arxiv.org/pdf/2610.41127
- **详细分析**: [[20_Research/Papers/具身智能/MotorSense_A_Video-EMG_Dataset_of_Motoric_Representations_for_Action_Understanding|MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding]]
- **作者**: Eadom Dessalene, Michael Maynord, Amir-Hossein Shahidzadeh, Botao He, Yasamin Tabatabaee, Ruoshi Liu, Ruohan Gao, Paul Pu Liang, Yiannis Aloimonos
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer vision models learn hand action only from its visual consequences, without access to the underlying embodied motor signals. We address this absence with MotorSense, the first large-scale paired egocentric video and surface electromyography (EMG) dataset. MotorSense pairs bimanual EMG bands with egocentric video and yields synchronized video, bimanual EMG and IMU, and audio across 100 hours of unscripted manipulation. EMG offers a powerful scalable alternative to manual annotation: it captures finger movement, hand configuration, and the forces exerted between hand and environment as a dense signal free of occlusion and labeler bias, whereas manual annotation is costly, subjective, and unreliable under occlusion. We use MotorSense to learn sensorimotor alignment, producing an organization of action that is shared across the visual and motoric spaces, through cross-modal pre-training between video and EMG. The resultant vision models are then transferred to downstream tasks that benefit from sensorimotor alignment: in this case, action recognition, 3D hand reconstruction, and 3D contact reconstruction. We further demonstrate a generative application in which EMG motor signals are used to condition a video diffusion model, yielding videos of fine-grained hand manipulation. Across four action-centric computer vision tasks and eight popular video datasets, we demonstrate that sensorimotor alignment provides a stronger foundation for visual representation learning than conventional self-supervised learning methods over video, outperforming every baseline across all tasks and datasets evaluated.

</details>

---

### [[20_Research/Papers/机器人/Drone-PUR_From_Visual_Clue_Discovery_to_Understanding_and_Reasoning_in_UAV_Scenes|Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes]]

![[assets/2610.40801_figure.png|800]]

- **arXiv**: [2610.40801](https://arxiv.org/abs/2610.40801)
- **PDF**: https://arxiv.org/pdf/2610.40801
- **详细分析**: [[20_Research/Papers/机器人/Drone-PUR_From_Visual_Clue_Discovery_to_Understanding_and_Reasoning_in_UAV_Scenes|Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes]]
- **作者**: Jiahe Wu, Bing Cao, Xingyue Guo, Ruipu Zhao, Beiming Yu, Jiekang Feng, Qinghua Hu, Pengfei Zhu
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.6（加权：机器人 1.6）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Drone-PUR: From Visual Clue Discovery to Understanding and Reasoning in UAV Scenes》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DVGBench, GQA, MLLM-CompBench, MM-UAVBench, MMSI-Bench, UAVBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The reasoning capabilities of vision-language models (VLMs) can be limited by incomplete or inaccurate visual observations in the general domain. In unmanned aerial vehicle (UAV) scenes, small targets, subtle attributes, and changing viewpoints further complicate perception and understanding. Therefore, we introduce Drone-PUR, a dataset and benchmark organized around visual clue discovery, interpretation, and integration, corresponding to the three capability dimensions of perception, understanding, and reasoning. Reasoning samples are designed to require models to combine multiple visual clues to derive visually grounded conclusions. Its 11 tasks provide 175k training and 20k test samples spanning single images, image sequences, cross-modal images, and multiple viewpoints. All test samples undergo human review. Evaluating 22 general-purpose VLMs reveals persistent limitations in spatial judgment and cross-modal and cross-view reasoning. Across models, stronger perception is associated with better reasoning, while single-task fine-tuning further reveals selective bidirectional transfer between these capabilities. To examine domain adaptation, we develop UAV-PUR from Qwen3-VL through staged fine-tuning with auxiliary supervision. Its 4B and 8B variants improve overall multiple-choice accuracy by 18.33 and 17.52 percentage points over their pretrained counterparts, respectively. The dataset and project resources are available at https://drone-pur.github.io.

</details>

---
