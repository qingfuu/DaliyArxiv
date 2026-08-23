# cs.CV | Computer Vision and Pattern Recognition | 2026-08-21

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/Inter-X++_A_Comprehensive_Benchmark_for_Multimodal_Human-Human_Interaction_Analysis|Inter-X++: A Comprehensive Benchmark for Multimodal Human-Human Interaction Analysis]]

![[assets/2608.20312_figure.png|800]]

- **arXiv**: [2608.20312](https://arxiv.org/abs/2608.20312)
- **PDF**: https://arxiv.org/pdf/2608.20312
- **详细分析**: [[20_Research/Papers/大模型/Inter-X++_A_Comprehensive_Benchmark_for_Multimodal_Human-Human_Interaction_Analysis|Inter-X++: A Comprehensive Benchmark for Multimodal Human-Human Interaction Analysis]]
- **作者**: Liang Xu, Chengqun Yang, Zili Lin, Xintao Lv, Yichao Yan, Xin Jin, Zhibo Chen, Xiaokang Yang, Wenjun Zeng
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.4）
- **关联关键词**: Multimodal, EmbodiedAI, Systems

#### 研究背景与动机

《Inter-X++: A Comprehensive Benchmark for Multimodal Human-Human Interaction Analysis》归入 大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The capability to perceive and synthesize human-human interactions is fundamental to developing intelligent digital human systems. However, existing datasets and modeling approaches are fundamentally constrained by low-fidelity kinematics, the omission of dexterous hand gestures and a severe lack of rich multimodal annotations. Furthermore, fragmented interaction representations and inconsistent evaluation protocols also impede fair and rigorous benchmarking. To systematically address these bottlenecks, we present Inter-X++, a comprehensive and large-scale benchmark designed to empower versatile HHI analysis. Captured via a novel hybrid motion capture system, Inter-X++ provides 11,388 high-fidelity interaction sequences and over 8.1M frames, featuring precise whole-body movements and detailed finger articulations. Meanwhile, we enrich the data foundation with multifaceted annotations, including hierarchical fine-grained textual descriptions, interaction categories, causal interaction orders, the relationship and personality of the subjects, as well as vertex-level contact maps and physically regularized constraints. Leveraging these elaborate annotations, we formulate a unified testing ground comprising four categories of downstream tasks that symmetrically span both generative and perceptive paradigms. To eliminate benchmarking ambiguities, we systematically standardize the interaction representations and evaluation protocols. Finally, we go beyond dataset construction to propose OpenHHI, a single and unified HHI representation and modeling framework that jointly optimizes interaction reconstruction and semantic understanding. Extensive experiments reveal that OpenHHI achieves state-of-the-art performance on both generation and perception tasks. This definitively proves that our unified representation successfully bridges interaction understanding and generation simultaneously.

</details>

---

### [[20_Research/Papers/具身智能/DreamHand_Repurposing_Video_Diffusion_Models_for_Occlusion-Robust_Egocentric_3D_Hand_Motion_Recovery|DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery]]

![[assets/2608.20308_figure.png|800]]

- **arXiv**: [2608.20308](https://arxiv.org/abs/2608.20308)
- **PDF**: https://arxiv.org/pdf/2608.20308
- **详细分析**: [[20_Research/Papers/具身智能/DreamHand_Repurposing_Video_Diffusion_Models_for_Occlusion-Robust_Egocentric_3D_Hand_Motion_Recovery|DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery]]
- **作者**: Yufei Liu, Xixi Wang, Hao Li, Ganlong Zhao, Kaitong Cai, Chengkai Jin, Chunxiao Liu, Jianbo Liu, Siyuan Huang, Xingang Pan, Hongsheng Li
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.9，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DreamHand: Repurposing Video Diffusion Models for Occlusion-Robust Egocentric 3D Hand Motion Recovery》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric video offers scalable manipulation data for embodied AI, yet recovering metric 3D hand trajectories remains challenging due to severe object occlusion and frequent out-of-sight gaps. Existing single-frame and windowed temporal regressors fail when hand shortly leaves the frame, while recent video diffusion models (VDMs) rely on heavy, stochastic multi-step sampling as pixel-space renderers. We instead repurpose VDM into a deterministic geometry encoder. A single forward pass over the clean latent exposes scene content beyond current observations, including occluded and out-of-sight hands. We introduce DreamHand, an offline clip-level framework that extracts features via a Deterministic Clean-Latent Encoder and decodes them with a Bidirectional Spatiotemporal Decoder. DreamHand recovers continuous bimanual trajectories with metric placement and no external detector, while a Ray-Based Camera Solver supports a second configuration that needs no test-time camera intrinsics. Across five egocentric benchmarks, DreamHand sets a new state of the art, cutting MPJPE-p by 30% on occlusion-heavy ARCTIC and 40% on HOT3D. These gains reach 46%-61% once out-of-sight hands are included in the evaluation, offering a scalable path from everyday human video to robot manipulation data.

</details>

---

### [[20_Research/Papers/机器人/Towards_Surgical_World-Action_Modeling_A_Preliminary_Joint_Visual-Trajectory_Forecasting_for_Surgical_Motion_Planning|Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning]]

![[assets/2608.20284_figure.png|800]]

- **arXiv**: [2608.20284](https://arxiv.org/abs/2608.20284)
- **PDF**: https://arxiv.org/pdf/2608.20284
- **详细分析**: [[20_Research/Papers/机器人/Towards_Surgical_World-Action_Modeling_A_Preliminary_Joint_Visual-Trajectory_Forecasting_for_Surgical_Motion_Planning|Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning]]
- **作者**: Weiliang Huang, Huanrong Liu, Bob Zhang, Qi Dou, Zhen Chen, Yun Gu, Guy Rosman, Qingbiao Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Towards Surgical World-Action Modeling: A Preliminary Joint Visual-Trajectory Forecasting for Surgical Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SurgWMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable surgical planning requires models to anticipate not only how instruments will move, but also how the operative visual state will evolve together with such motion. Existing approaches typically treat future scene generation and instrument trajectory prediction as two separate tasks. Scene-only models cannot directly evaluate the accuracy of future instrument motion at the trajectory level, while trajectory-only models fail to capture the visual consequences of instrument movement, leaving the consistency between predicted trajectories and future scene evolution unaddressed. Jointly forecasting both provides a more complete account of surgical action-scene dynamics by enabling explicit trajectory-level evaluation while simultaneously modeling the corresponding visual evolution. To bridge this gap, we present a preliminary joint visual-trajectory world-action model that simultaneously forecasts future visual states and instrument trajectories from historical surgical observations. Specifically, we encode historical video frames and tool trajectories into latent representations, which are processed by a temporal-spatial encoder and subsequently decoded through separate visual-state and trajectory prediction heads. Based on this preliminary architecture, a chunked autoregressive rollout is repeatedly applied to predict fifteen future steps. The chunked strategy consistently outperforms direct one-shot prediction across all evaluated horizons, improving first-segment PSNR from 18.86 to 23.11 dB and reducing ADE from 45.77 to 22.22 pixels. These results demonstrate the initial feasibility of joint visual-motion forecasting. However, we observe progressive visual degradation and accumulated trajectory errors over longer prediction horizons, which remain important challenges for future surgical world-action modeling.

</details>

---

### [[20_Research/Papers/具身智能/RoMAN-Flow_Taming_Autoregressive_Normalizing_Flows_for_Offline_Reinforcement_Learning_in_Robotic_Manipulation|RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation]]

![[assets/2608.20208_figure.png|800]]

- **arXiv**: [2608.20208](https://arxiv.org/abs/2608.20208)
- **PDF**: https://arxiv.org/pdf/2608.20208
- **详细分析**: [[20_Research/Papers/具身智能/RoMAN-Flow_Taming_Autoregressive_Normalizing_Flows_for_Offline_Reinforcement_Learning_in_Robotic_Manipulation|RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation]]
- **作者**: Shaoxuan Wang, Guangting Zheng, Rui Huang, Zhipeng Tang, Sha Zhang, Jiajun Deng, Yanyong Zhang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 1.2，强化学习 1.2，机器人 1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《RoMAN-Flow: Taming Autoregressive Normalizing Flows for Offline Reinforcement Learning in Robotic Manipulation》归入 强化学习、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning improves robotic policies using previously collected data without further environment interaction. Yet prevalent diffusion- and flow-matching robot policies lack tractable likelihoods, limiting their use in likelihood-based offline RL post-training. AR-NFs offer both expressive action modeling and exact likelihood evaluation, but their sequential sampling incurs substantial sampling overhead during policy optimization and deployment. We present RoMAN-Flow (Robotic Manipulation with Autoregressive Normalizing Flows), an offline reinforcement learning framework that makes AR-NF policies practical for robotic manipulation by addressing this sampling bottleneck in both stages. During policy optimization, RoMAN-Flow employs a sampling-free, advantage-weighted likelihood objective that assigns higher likelihood to high-advantage actions from the offline dataset without sampling from the autoregressive policy. For efficient deployment, it distills the optimized autoregressive policy into a one-step action generator, enabling low-latency action prediction. Experiments across multiple simulated manipulation benchmarks and real-world robotic platforms demonstrate that RoMAN-Flow achieves competitive policy performance while substantially reducing inference latency. Code is available at https://github.com/konnyaku28/RoMAN-Flow.

</details>

---

### [[20_Research/Papers/机器人/PVRA_A_Pointwise_Key-point_Voting_Framework_for_Robotic_Assembly|PVRA: A Pointwise Key-point Voting Framework for Robotic Assembly]]

![[assets/2608.19968_figure.png|800]]

- **arXiv**: [2608.19968](https://arxiv.org/abs/2608.19968)
- **PDF**: https://arxiv.org/pdf/2608.19968
- **详细分析**: [[20_Research/Papers/机器人/PVRA_A_Pointwise_Key-point_Voting_Framework_for_Robotic_Assembly|PVRA: A Pointwise Key-point Voting Framework for Robotic Assembly]]
- **作者**: Kulunu Samarawickrama, Roel Pieters
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《PVRA: A Pointwise Key-point Voting Framework for Robotic Assembly》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PVNet, PartNet, RGL-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern computer vision has enabled partial autonomy in robotic assembly manipulation. However, performing autonomous manipulation of a progressive assembly demands a more specific set of skills, in addition to perceiving the objects. Through a comparative analysis of research in the associated domains, we deduce that object-centric perception must advance towards learning assembly dependencies to predict meaningful actionable outputs for autonomous assembly manipulation. Subsequently, we present a 3D keypoint-based modular learning framework to learn assembly dependencies to infer actionable outputs given a RGB-D input of an assembly scene. We train and evaluate our trained network on an assembly pose estimation dataset and compare it against object-centric baselines with an augmented set of metrics for progressive assemblies.

</details>

---

### [[20_Research/Papers/强化学习/RIPE++_Reinforced_Keypoint_Learning_from_Positive_Pairs_Only|RIPE++: Reinforced Keypoint Learning from Positive Pairs Only]]

![[assets/2608.19693_figure.png|800]]

- **arXiv**: [2608.19693](https://arxiv.org/abs/2608.19693)
- **PDF**: https://arxiv.org/pdf/2608.19693
- **详细分析**: [[20_Research/Papers/强化学习/RIPE++_Reinforced_Keypoint_Learning_from_Positive_Pairs_Only|RIPE++: Reinforced Keypoint Learning from Positive Pairs Only]]
- **作者**: Johannes Künzel, Peter Eisert, Anna Hilsmann
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《RIPE++: Reinforced Keypoint Learning from Positive Pairs Only》归入 强化学习、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：D2-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sparse keypoint extraction and matching underpin core tasks in geometric computer vision, including structure-from-motion, visual SLAM, augmented reality, and medical image registration. Learning robust local feature representations, however, typically requires accurate camera poses or depth supervision, which are often unavailable in real-world settings. Reinforcement learning (RL) has recently emerged as a promising alternative, requiring only the information if two images show the same scene or not. However, existing RL formulations such as RIPE rely on coarse binary rewards and carefully constructed negative training pairs, limiting training stability and descriptor discriminability. In this paper, we revisit RL-based keypoint learning and propose a reward that fully exploits the geometric consistency signal, deriving both reward and penalty from a single positive pair without contrasting against negatives. This richer signal provides sufficient supervisory contrast to learn discriminative detectors and descriptors from positive image pairs alone, enabling representation learning under extremely limited supervision. Furthermore, we show that the same RL objective can be extended to the matching stage by adapting LightGlue, raising AUC@5 on MegaDepth1500 from 56.58 to 59.65 and enabling weakly-supervised training of the full sparse matching pipeline from image pairs with partial visual overlap. We validate our approach on established benchmarks, demonstrating competitive results compared to fully-supervised methods. We further show that the method can be even trained on low texture medical video sequences, where camera poses are usually unavailable and standard SfM pipelines often fail. Code and data are available at https://github.com/fraunhoferhhi/RIPEpp .

</details>

---

### [[20_Research/Papers/大模型/Scaffolding_Minds_Optimizing_Latent_Visual_Target_Representations_for_Multimodal_Reasoning|Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning]]

![[assets/2608.19669_figure.png|800]]

- **arXiv**: [2608.19669](https://arxiv.org/abs/2608.19669)
- **PDF**: https://arxiv.org/pdf/2608.19669
- **详细分析**: [[20_Research/Papers/大模型/Scaffolding_Minds_Optimizing_Latent_Visual_Target_Representations_for_Multimodal_Reasoning|Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning]]
- **作者**: Haoqiang Kang, Yinpeng Chen, Luyang Liu, Jesper Sparre Andersen, Abhijit Ogale, Baochen Sun, Lichan Hong, Ed H. Chi
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CV-Bench, HRBench, MME-RealWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning (RL) stage. In this paper, we identify two key limitations of this framework, one in each stage. First, the SFT stage typically relies on an off-the-shelf vision encoder to encode the helper image, yielding suboptimal latent representations that may not be well aligned with the downstream reasoning task. Second, existing RL methods treat the latent component only through deterministic regularization, which constrains policy drift but does not create alternative latent trajectories for exploration. To address these limitations, we propose Scaffolding Minds. Our approach learns a dedicated scaffolding encoder that provides an optimized target in latent space, and learns both the mean and variance of the RL sampler. We further show that these two improvements are complementary, together yielding substantial gains over strong baselines. Empirically, our method improves over the strongest latent-reasoning baseline by +9.5% on FrozenLake spatial planning, with the gain widening to +19% at 32x32 grid map, and by +5.2% on average across nine visual-centric reasoning benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/What_Matters_for_Latent_Actions_in_Robot_Learning|What Matters for Latent Actions in Robot Learning]]

![[assets/2608.19613_figure.png|800]]

- **arXiv**: [2608.19613](https://arxiv.org/abs/2608.19613)
- **PDF**: https://arxiv.org/pdf/2608.19613
- **详细分析**: [[20_Research/Papers/具身智能/What_Matters_for_Latent_Actions_in_Robot_Learning|What Matters for Latent Actions in Robot Learning]]
- **作者**: Xizhou Bu, Qingda Hu, Lei Zhou, Lingfeng Zhang, Yingbo Tang, Zihao Liu, Xinyi Tao, Zhiqiang Ma, Qingqiu Huang, Chufeng Tang, Hongbo Wang, Jing Zhang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.9，大模型 0.3，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《What Matters for Latent Actions in Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent Action Models (LAMs) have emerged as a promising paradigm for enabling robot learning to leverage large-scale unlabeled videos through latent actions that serve as compact surrogates for physical actions. Despite rapid progress, research on LAM remains highly fragmented, with existing methods evaluating different design choices in isolation under inconsistent experimental settings, making it difficult to identify the factors that truly determine downstream robotic manipulation performance. In this work, we present the first comprehensive empirical study of latent action learning for robotic manipulation. We unify representative LAM methods within a common autoencoding framework and systematically investigate 41 LAM design choices across three dimensions, including latent action modeling paradigms, learning objectives and regularization methods, and latent action integration strategies. We further examine four proxy metrics for evaluating latent action quality and assess their ability to reliably predict downstream robotic manipulation performance. Extensive experiments on three widely used benchmarks provide strong empirical evidence that fine-tuning vision-language model (VLM) backbones with latent actions provides a stronger initialization for downstream policy learning, with further validation on real-world robot manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/OrthoSkillVLA_Continual_Skill_Learning_via_Gradient-Informed_Skill_Subspace_Adaptation|OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation]]

![[assets/2608.19589_figure.png|800]]

- **arXiv**: [2608.19589](https://arxiv.org/abs/2608.19589)
- **PDF**: https://arxiv.org/pdf/2608.19589
- **详细分析**: [[20_Research/Papers/具身智能/OrthoSkillVLA_Continual_Skill_Learning_via_Gradient-Informed_Skill_Subspace_Adaptation|OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation]]
- **作者**: Jiaqi Wang, Zhou Fang, Qiongfeng Shi, Yi Zhou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OrthoSkillVLA, Real-World, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained Vision-Language-Action models provide a strong foundation for robot learning, but sequentially adapting them to diverse skills can perturb the representations and velocity mappings used by previous skills, leading to catastrophic forgetting. Architecture-based approaches improve retention by isolating skills but lead to increased inference footprint. Recent subspace-constrained methods restrict parameter updates in an orthogonal subspace to minimize interference but impose a unified constraint on the entire model. We analyze the distinct roles of internal VLA components and identify two VLA-specific challenges. First, the VLM maintains broad semantic representations, making it vulnerable to capacity exhaustion, whereas the ActionHead refines semantics into localized velocity patterns that are highly sensitive to perturbations. Second, the final velocity decoder serves as a readout layer. Freezing it forms an output-stage expressivity bottleneck, while updating it risks overwriting previous velocity mappings. To this end, we propose OrthoSkillVLA, a parameter-efficient framework for continual skill learning in pretrained VLA models without demonstration replay. Given the representation heterogeneity, we impose separate subspace constraints on the VLM and ActionHead, preserving reusable semantic capacity while protecting localized velocity patterns. For the output layer, we introduce a lightweight feature-aware MoE decoder, where each skill is allocated a compact expert and a training-free router selects the expert according to feature-space affinity. Extensive simulated and real-world evaluations, together with ablations, demonstrate that OrthoSkillVLA better preserves prior skills while acquiring new ones.

</details>

---

### [[20_Research/Papers/具身智能/Fine-Tuning_VLAs_with_Self-Demonstrated_Generative_Control_for_Multi-Task_Manipulation|Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation]]

![[assets/2608.19490_figure.png|800]]

- **arXiv**: [2608.19490](https://arxiv.org/abs/2608.19490)
- **PDF**: https://arxiv.org/pdf/2608.19490
- **详细分析**: [[20_Research/Papers/具身智能/Fine-Tuning_VLAs_with_Self-Demonstrated_Generative_Control_for_Multi-Task_Manipulation|Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation]]
- **作者**: Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State-of-the-art vision-language-action (VLA) models such as $π_{0.5}$ exhibit strong semantic understanding, instruction following and task behavior. However, when deployed on new robots, even minor mismatches in hardware configuration relative to pretraining can cause severe performance drops. Finetuning the VLA on in-domain expert data from the new embodiment improves performance on the expert task but leads to a loss in its original instruction following and behavioral priors. In this paper, we propose a self-supervised method that generates online interaction rollouts from the zero-shot VLA as additional training data for finetuning. Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data with improved sample efficiency. We demonstrate the success of our approach across test sets probing generalization on a real ALOHA robot and a new simulation benchmark in RoboTwin. Video results are available at https://self-supervised-control.pages.dev/

</details>

---
