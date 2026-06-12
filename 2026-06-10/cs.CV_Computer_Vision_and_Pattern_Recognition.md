# cs.CV | Computer Vision and Pattern Recognition | 2026-06-10

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/ARM_An_AutoRegressive_Large_Multimodal_Model_with_Unified_Discrete_Representations|ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations]]

![[assets/2606.11188_figure.png|800]]

- **arXiv**: [2606.11188](https://arxiv.org/abs/2606.11188)
- **PDF**: https://arxiv.org/pdf/2606.11188
- **详细分析**: [[20_Research/Papers/大模型/ARM_An_AutoRegressive_Large_Multimodal_Model_with_Unified_Discrete_Representations|ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations]]
- **作者**: Junke Wang, Xiao Wang, Jiacheng Pan, Xuefeng Hu, Feng Li, Jingxiang Sun, Chaorui Deng, Zilong Chen, Yunpeng Chen, Kaibin Tian, Matthew Gwilliam, Hao Chen...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.2（加权：大模型 1，强化学习 0.2）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GEdit-Bench, GenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces ARM, a discrete representation-based AutoRegressive Model that unifies image understanding, generation, and editing within a next-token prediction framework. ARM is built on three efforts: first, we train a discrete semantic visual tokenizer that maps images into compact token sequences. Our tokenizer is supervised with multiple objectives that jointly promote semantic discriminability, language alignment and faithful reconstruction, thereby supporting diverse tasks in a shared latent space. With this, we train a 7B autoregressive model over large-scale text and image token sequences, seamlessly developing vision-language perception and generation capabilities. Finally, to further improve preference-aligned behavior for text-to-image generation and instruction-guided editing, ARM applies reinforcement learning (RL) to optimize task-level objectives such as visual quality, instruction adherence, and edit consistency. Surprisingly, the results show that RL not only substantially improves performance on the target tasks (e.g., raising WISE overall from 0.50 to 0.56, GEdit-Bench-EN G_O from 5.75 to 6.68), but also induces cross-task synergy between text-to-image generation and editing. Collectively, these findings highlight autoregressive modeling, when paired with strong representations and preference optimization, as a scalable foundation for multimodal intelligence. Code: https://github.com/wdrink/ARM.

</details>

---

### [[20_Research/Papers/具身智能/WorldOlympiad_Can_Your_World_Model_Survive_a_Triathlon|WorldOlympiad: Can Your World Model Survive a Triathlon?]]

![[assets/2606.11129_figure.png|800]]

- **arXiv**: [2606.11129](https://arxiv.org/abs/2606.11129)
- **PDF**: https://arxiv.org/pdf/2606.11129
- **详细分析**: [[20_Research/Papers/具身智能/WorldOlympiad_Can_Your_World_Model_Survive_a_Triathlon|WorldOlympiad: Can Your World Model Survive a Triathlon?]]
- **作者**: Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.1，世界模型 0.8，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《WorldOlympiad: Can Your World Model Survive a Triathlon?》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EWMBench, LingBot-World, VBench, WorldEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-term temporal coherence, they provide limited insight into whether generated videos obey physical rules, preserve coherent 3D structure, and sustain controllable interactions over long horizons. To address this gap, WorldOlympiad decomposes world-model evaluation into three complementary dimensions. The physical track uses object segmentation and MLLM-as-judge to assess whether generated videos follow interpretable rules in mechanics, thermal phenomena, and material properties. The geometry track reconstructs generated videos with Gaussian splatting and evaluates structural consistency, cross-view coherence, and camera-trajectory alignment. The interaction track assesses whether generated rollouts follow complex action prompts and maintain smooth, coherent transitions across consecutive video chunks. WorldOlympiad further covers three major downstream scenarios, including gaming, robotics, and general real-world videos, capturing diverse challenges from interactive control and embodied manipulation to open-domain motion and camera dynamics. Together, these tracks and scenarios form a scalable and interpretable evaluation suite that exposes failure modes beyond generic video quality. Experiments on state-of-the-art models reveal substantial gaps in physical reasoning, 3D consistency, and long-horizon interaction, underscoring the need for more structured evaluation protocols for generative world models.

</details>

---

### [[20_Research/Papers/具身智能/IMPACT_Learning_Internal-Model_Predictive_Control_for_Forceful_Robotic_Manipulation|IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation]]

![[assets/2606.10818_figure.png|800]]

- **arXiv**: [2606.10818](https://arxiv.org/abs/2606.10818)
- **PDF**: https://arxiv.org/pdf/2606.10818
- **详细分析**: [[20_Research/Papers/具身智能/IMPACT_Learning_Internal-Model_Predictive_Control_for_Forceful_Robotic_Manipulation|IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation]]
- **作者**: Jiawei Gao, Chaoqi Liu, Peilin Wu, Haonan Chen, Yilun Du
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world robotic manipulation tasks often involve forceful interactions with the environment, such as using tools of varying weights, transporting objects with different masses, and performing contact-rich tasks like table wiping. Previous learning-based approaches typically employ imitation learning policies that output target end-effector poses tracked by low-level impedance controllers. In these systems, forceful interactions are either implicitly realized through steady-state tracking errors or explicitly commanded using wrist force/torque or tactile sensors. However, implicit approaches generalize poorly across object weights, while explicit approaches require specialized hardware and increase system complexity. In this work, we propose IMPACT, a framework that decouples these forceful tasks into task-planning and internal-model-based predictive control. Extensive simulation and real-world experiments demonstrate that the proposed framework achieves higher success rates and improved generalization to unseen object weights, as well as better safety and energy efficiency.

</details>

---

### [[20_Research/Papers/具身智能/Dexterous_Point_Policy_Learning_Point-based_Dexterous_Hand_Policies_from_Human_Demonstrations|Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations]]

![[assets/2606.10614_first_page.png|800]]

- **arXiv**: [2606.10614](https://arxiv.org/abs/2606.10614)
- **PDF**: https://arxiv.org/pdf/2606.10614
- **详细分析**: [[20_Research/Papers/具身智能/Dexterous_Point_Policy_Learning_Point-based_Dexterous_Hand_Policies_from_Human_Demonstrations|Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations]]
- **作者**: Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee, Jinwoo Shin
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic foundation models pre-trained on human demonstration videos have shown promise, but a significant embodiment gap remains when the resulting policies are deployed on real robots. A common remedy is to fine-tune these models on robot-specific demonstrations. However, robot data collection can be prohibitively expensive and time-consuming, which is particularly acute in dexterous manipulation, e.g., teleoperating a multi-fingered hand for even a single atomic task can take days. To address this, we introduce Dexterous Point Policy, a framework that learns dexterous manipulation policies directly from human videos and requires no robot demonstrations. Our core insight is that a unified 3D keypoint representation can bridge human and robot embodiments when used for both observations and actions. Specifically, we extract 3D keypoints of task-relevant objects and human hands from raw videos, and train an autoregressive transformer over these keypoints. We observe that at the keypoint level, specifically the wrist and fingertips, human and robot behaviors closely align, enabling direct policy transfer. On a suite of real-robot tasks spanning pick-and-place and tool use, Dexterous Point Policy attains 75.0% success, whereas a state-of-the-art VLA baseline reaches only 1.0%. Furthermore, our method generalizes strongly to unseen scenarios, including multi-object environments and novel object categories.

</details>

---

### [[20_Research/Papers/强化学习/Geometry-Aware_Reinforcement_Learning_for_2D_Irregular_Nesting|Geometry-Aware Reinforcement Learning for 2D Irregular Nesting]]

![[assets/2606.10611_figure.png|800]]

- **arXiv**: [2606.10611](https://arxiv.org/abs/2606.10611)
- **PDF**: https://arxiv.org/pdf/2606.10611
- **详细分析**: [[20_Research/Papers/强化学习/Geometry-Aware_Reinforcement_Learning_for_2D_Irregular_Nesting|Geometry-Aware Reinforcement Learning for 2D Irregular Nesting]]
- **作者**: Auguste Lehuger, Guillaume Henon-Just
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Geometry-Aware Reinforcement Learning for 2D Irregular Nesting》归入 强化学习、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional heuristic solvers for the 2D irregular nesting problem share a fundamental limitation: they are blind to polygon geometry, relying on guided brute-force to navigate the continuous placement space with minimal geometrical guidance. In this paper, we argue that Reinforcement Learning is uniquely positioned to overcome this bottleneck. By pairing an optimization policy with a geometry-aware neural encoder, an agent can automatically discover rich geometric priors directly from data, utilizing these learned intuitions to strategically guide exploration. To realize this, we introduce the Polygons Transformer (PoT), a novel architecture that encodes 2D continuous vector geometries while allowing cross-polygons attention. We couple this novel architecture with a Combinatorial Optimization Reinforcement Learning (CORL) training framework to find optimal solutions. To support this paradigm, we release an open-source training dataset derived from complex geographic contours alongside a dedicated evaluation benchmark. Our empirical validation demonstrates that our trained agent achieves area utilization performance highly competitive with Sparrow, the state-of-the-art heuristic solver, proving that reinforcement learning can successfully discover and exploit geometric awareness for precise spatial tasks.

</details>

---

### [[20_Research/Papers/具身智能/GHOST_Hierarchical_Sub-Goal_Policies_for_Generalizing_Robot_Manipulation|GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation]]

![[assets/2606.10025_figure.png|800]]

- **arXiv**: [2606.10025](https://arxiv.org/abs/2606.10025)
- **PDF**: https://arxiv.org/pdf/2606.10025
- **详细分析**: [[20_Research/Papers/具身智能/GHOST_Hierarchical_Sub-Goal_Policies_for_Generalizing_Robot_Manipulation|GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation]]
- **作者**: Sriram Krishna, Ben Eisner, Haotian Zhan, Ying Yuan, Haoyu Zhen, Chuang Gan, Shubham Tulsiani, David Held
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《GHOST: Hierarchical Sub-Goal Policies for Generalizing Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present GHOST, a framework for learning visuomotor manipulation policies that generalize beyond the training distribution. GHOST factorizes control into (i) a high-level policy that predicts the next sub-goal as a distribution over 3D end-effector poses from multi-view RGB-D observations, and (ii) a low-level goal-conditioned controller that executes embodiment-specific actions. To condition image-based policies on 3D goals, we introduce a simple spatial interface that projects predicted goals into the image plane and represents them as end-effector heatmaps. Across a suite of manipulation tasks, this hierarchical factorization consistently improves performance and robustness compared to a flat Diffusion Policy. Further, we show that this hierarchical interface also makes it easy to incorporate human demonstrations without relying on (noisy) action retargeting. As sub-goals are largely embodiment-agnostic, we train the high-level policy on human video to specify how learned skills should be applied and composed, while keeping the low-level policy trained purely on robot data. This hierarchy enables adaptation to novel objects and task variations using a small number of human demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/ABot-Earth_0.5_Generative_3D_Earth_Model|ABot-Earth 0.5: Generative 3D Earth Model]]

![[assets/2606.09967_figure.jpg|800]]

- **arXiv**: [2606.09967](https://arxiv.org/abs/2606.09967)
- **PDF**: https://arxiv.org/pdf/2606.09967
- **详细分析**: [[20_Research/Papers/具身智能/ABot-Earth_0.5_Generative_3D_Earth_Model|ABot-Earth 0.5: Generative 3D Earth Model]]
- **作者**: Ming Qian, Tianjian Ouyang, Mingchao Sun, Zijian Wang, Jincheng Xiong, Jiarong Han, Yongchang Zhang, Jiawei Zhang, Xu Wang, Yu Liu, Luyang Tang, Fei Yu...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.9，机器人 0.2）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《ABot-Earth 0.5: Generative 3D Earth Model》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ABot-Earth 0.5, a generative 3D framework designed to synthesize vast, seamless 3D environments from ubiquitous, geospatially referenced satellite imagery. To achieve this, we propose a novel generative model formulated directly with the 3D Gaussian Splatting (3DGS) representation. The model is trained on a diverse corpus of existing real-world urban reconstructions, learning to generate realistic geometry and textures. At inference, it synthesizes novel 3D scenes conditioned solely on satellite imagery at a scalable rate of under 10 minutes per square kilometer, while demonstrating exceptional realism. The framework is designed for accessibility, with integrated hierarchical level-of-detail (LOD) structures that permit real-time, interactive visualization on web-based map engines. This high-fidelity simulation sandbox effectively mitigates the sim-to-real domain gap, enabling critical downstream Embodied AI applications like closed-loop UAV navigation. By providing an ultra-low-cost and high-efficiency solution, ABot-Earth 0.5 significantly lowers the technical and financial barriers to large-scale 3D reconstruction and empowers the future of global digital earth visualization.

</details>

---

### [[20_Research/Papers/具身智能/SAFE-Pruner_Semantic_Attention-Guided_Future-Aware_Token_Pruning_for_Efficient_Vision-Language-Action_Manipulation|SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation]]

![[assets/2605.29662_figure.png|800]]

- **arXiv**: [2605.29662](https://arxiv.org/abs/2605.29662)
- **PDF**: https://arxiv.org/pdf/2605.29662
- **详细分析**: [[20_Research/Papers/具身智能/SAFE-Pruner_Semantic_Attention-Guided_Future-Aware_Token_Pruning_for_Efficient_Vision-Language-Action_Manipulation|SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation]]
- **作者**: Shilin Ma, Chubin Zhang, Changyuan Wang, Yuji Wang, Yue Wu, Zixuan Wang, Jingqi Tian, Zheng Zhu, Yansong Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time inference of vision-language-action (VLA) models is essential for robotic control. While visual token pruning has shown strong potential for accelerating inference, most existing methods mainly base pruning decisions on shallow-layer cues and risk discarding visual information required by deep layers. To address this issue, we propose SAFE-Pruner, a plug-and-play pruning framework that incorporates attention cues of future layers into pruning decisions. Specifically, we identify semantic attention consistency, the tendency that VLA models concentrate their attention probability mass on the same semantic entity across execution steps. Based on this observation, we design a forward-looking strategy to forecast the token saliency in deep layers, which prevents the premature removal of critical tokens and leads to more stable acceleration. We further introduce an adaptive subtask division strategy to detect abrupt attention shifts, thereby improving forecasting accuracy and pruning reliability. Extensive experiments in simulation and real-world settings demonstrate that our method achieves up to 1.89x speedup with a minimal degradation in success rate of less than 1.7%, while outperforming state-of-the-art methods by up to 1.9%.

</details>

---
