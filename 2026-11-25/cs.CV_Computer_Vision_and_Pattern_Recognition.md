# cs.CV | Computer Vision and Pattern Recognition | 2026-11-25

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/具身智能/Lost_on_Campus_Evaluating_Embodied_Spatial_Reasoning_of_Vision-Language_Models_in_the_Wild|Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild]]

![[assets/2611.33145_figure.png|800]]

- **arXiv**: [2611.33145](https://arxiv.org/abs/2611.33145)
- **PDF**: https://arxiv.org/pdf/2611.33145
- **详细分析**: [[20_Research/Papers/具身智能/Lost_on_Campus_Evaluating_Embodied_Spatial_Reasoning_of_Vision-Language_Models_in_the_Wild|Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild]]
- **作者**: Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Ego3D-Bench, GOAT-Bench, NavBench, OpenBench, STI-Bench, Sage-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Spatial Reasoning (ESR) is central to deploying Vision-Language Models (VLMs) in real-world embodied tasks, yet remains inadequately evaluated. Existing benchmarks primarily assess spatial reasoning in static images or synthetic indoor environments, where semantic shortcuts often suffice, making it difficult to faithfully evaluate spatial reasoning capabilities in the wild. In light of this, we present Lost on Campus, a benchmark for evaluating ESR in large-scale real-world outdoor 3D environments reconstructed by 3D Gaussian Splatting. Our benchmark introduces a unified reasoning-action evaluation framework that seamlessly integrates diagnostic QA for isolated reasoning with closed-loop interactive navigation for active reasoning under multimodal instructions. To enable fine-grained diagnosis, we evaluate six capability aspects of ESR: action grounding, spatial foresight, metric awareness, goal-directed planning, ego-allocentric localization, and spatio-temporal consistency. Extensive experiments reveal that: (i) Compared to indoor settings, real-world outdoor environments impose substantially higher demands on spatial reasoning, where existing models exhibit poor performance; (ii) VLMs still struggle with fine-grained visual alignment, with failures in spatial foresight and ego-allocentric localization emerging as primary bottlenecks; (iii) Improving multimodal interaction capabilities and long-term spatial reasoning is crucial for advancing embodied intelligence. These findings highlight that faithful evaluation of ESR demands benchmarks tightly coupling perception, reasoning and action within realistic and continuous environments.

</details>

---

### [[20_Research/Papers/具身智能/ROAM-Bench_Evaluating_Embodied_Active_Spatial_Intelligence_through_Evidence_Verification|ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification]]

![[assets/2611.33143_figure.png|800]]

- **arXiv**: [2611.33143](https://arxiv.org/abs/2611.33143)
- **PDF**: https://arxiv.org/pdf/2611.33143
- **详细分析**: [[20_Research/Papers/具身智能/ROAM-Bench_Evaluating_Embodied_Active_Spatial_Intelligence_through_Evidence_Verification|ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification]]
- **作者**: Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：E3VS-Bench, EQA, ESI-Bench, EXPRESS-Bench, EfficientEQA, EmbodiedBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied spatial intelligence requires agents to gather information through exploration and interaction, then use it to reason and act. Existing benchmarks insufficiently distinguish correct outcomes from completion of these task requirements. We introduce ROAM-Bench to evaluate these abilities under robot motion and collision constraints. Independent checks use simulation state and episode records to assess outcomes and task requirements, with stronger checks of geometry, coverage, or placement. It comprises 250 manually validated tasks across 11 types in five groups and 27 indoor environments, covering object and room search, counting, geometric judgments, direction reasoning, and relocation. Human evaluators achieve 84% strict task success on 100 sampled tasks, with every correct outcome satisfying the required checks. Across seven frontier vision-language models, we identify two complementary failure modes: correct outcomes with unmet task requirements, and incorrect outcomes despite passing stronger checks. Oracle-input diagnostics show that more complete target observations and calibrated feedback improve final spatial judgments.

</details>

---

### [[20_Research/Papers/具身智能/RFW-W_Scaling_Physical_Asset_Universes_for_Generative_Embodied_Simulation|RFW-W: Scaling Physical Asset Universes for Generative Embodied Simulation]]

![[assets/2611.33013_figure.png|800]]

- **arXiv**: [2611.33013](https://arxiv.org/abs/2611.33013)
- **PDF**: https://arxiv.org/pdf/2611.33013
- **详细分析**: [[20_Research/Papers/具身智能/RFW-W_Scaling_Physical_Asset_Universes_for_Generative_Embodied_Simulation|RFW-W: Scaling Physical Asset Universes for Generative Embodied Simulation]]
- **作者**: Jiawei Weng, Rui Zhang, Saining Zhang, Changjian Pan, Yuanbo Lyu, Jiarui Guo, Yongzhi Li, Guolin Liu, Jialu Liu, Jiankun Wang, Yi Yang, Peishuo Li...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《RFW-W: Scaling Physical Asset Universes for Generative Embodied Simulation》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexGraspNet, GAPartNet, PartNet, RoboFlywheel-World, ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling embodied simulation requires diverse objects with executable physical representations. We present RFW-W, a physical asset universe connecting rigid, articulated, and deformable asset sources to task-conditioned scene composition. Its reported inventories comprise 1,010,386 asset records: 524,611 rigid assets in 1,212 categories (RFW-R), 402,410 articulated assets in 531 categories (RFW-A), and 83,365 jointly verified deformables in 485 categories (RFW-S). These taxonomies contribute 2,228 dataset--category entries. RFW-R couples category-guided generation with collision geometry, composed physical properties, and interaction annotations; RFW-A uses reusable agent-authored procedural generators with explicit part and joint structure; RFW-S uses structure-aware simulation representations, calibration, and independent testing. A common interface preserves physical requirements specific to each asset type for retrieval and scene assembly. Quantitative evaluations demonstrate that RFW-R provides broader asset coverage and stronger scene-fulfillment capabilities than existing datasets. Across five RoboTwin tasks, using 100 demonstrations per task for each asset source, policies trained on RFW-R achieve macro success rates of 71.2% in clean settings and 41.8% under randomization, exceeding the strongest baseline by 15.8 and 10.6 percentage points, respectively. RFW-W provides a scalable and unified asset foundation for generating physically grounded, task-conditioned embodied worlds.

</details>

---

### [[20_Research/Papers/具身智能/VidForce_Predicting_Force-Aware_Articulation_by_Observing_Humans|VidForce: Predicting Force-Aware Articulation by Observing Humans]]

![[assets/2611.32967_figure.png|800]]

- **arXiv**: [2611.32967](https://arxiv.org/abs/2611.32967)
- **PDF**: https://arxiv.org/pdf/2611.32967
- **详细分析**: [[20_Research/Papers/具身智能/VidForce_Predicting_Force-Aware_Articulation_by_Observing_Humans|VidForce: Predicting Force-Aware Articulation by Observing Humans]]
- **作者**: Rafay Mohiuddin, Jiaqi Chen, Marc Pollefeys, Hermann Blum
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VidForce: Predicting Force-Aware Articulation by Observing Humans》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

People can anticipate how an object moves and the effort an interaction may require by watching others. How can embodied agents acquire this understanding from video? Force measurements provide direct sensory supervision, but require specialized equipment and remain limited in quantity. We introduce VidForce, which estimates an interaction trajectory together with a force profile from a third-person RGB video; 2D contact clicks and textual object-action prompts are optional. Our approach makes limited instrumented measurements useful for interpreting human interactions through learned physical prototypes as a prior. The prototypes share learned force levels and temporal profiles across interactions of comparable effort, with visual and semantic cues determining their contribution to each observation. Geometric and vision-language features adapt this prior to the observed interaction, while a joint conditional flow refines an initial tracked trajectory together with the force profile. Paired human and instrumented-gripper recordings provide measured force references for supervising human video, and a separately trained torque model demonstrates that the formulation extends to other sensory quantities. We evaluate trajectory recovery and force estimation through baseline comparisons and controlled ablations on held-out interactions from the Hoi! dataset. On this evaluation subset, VidForce achieves 6.6 cm ATE, peak-force MAE and RMSE of 4.81 N and 5.92 N, respectively, and force-profile RMSE of 5.52 N. On real-world videos, VidForce infers motion and force reliably and consistently despite the variability in human execution. We further deploy VidForce on a Spot robot, where trajectories and force profiles estimated from human demonstrations drive real-world articulated-object manipulation, and report success rates across repeated trials. Project page: https://rafaymhddn.github.io/vidforce

</details>

---

### [[20_Research/Papers/具身智能/Simulator-as-Proxy_World_Model_for_Robot_Manipulation|Simulator-as-Proxy World Model for Robot Manipulation]]

![[assets/2611.32786_figure.png|800]]

- **arXiv**: [2611.32786](https://arxiv.org/abs/2611.32786)
- **PDF**: https://arxiv.org/pdf/2611.32786
- **详细分析**: [[20_Research/Papers/具身智能/Simulator-as-Proxy_World_Model_for_Robot_Manipulation|Simulator-as-Proxy World Model for Robot Manipulation]]
- **作者**: Tingting Liao, Mingjia Huo, Hao Li, Zhengzhong Liu, Eric P. Xing, Guangyi Liu
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 3.62（加权：具身智能 1.2，强化学习 0.16，世界模型 1.16，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Simulator-as-Proxy World Model for Robot Manipulation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, PointWorld, Real-to-Sim, Real2Sim, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models for robots are increasingly conditioned on a simulated or rendered proxy of the scene, on the assumption that the video will show what the proxy shows. Testing this assumption requires a proxy whose state is explicit and can be perturbed. We present SimPWM (Simulator-as-Proxy World Model): given a calibrated camera, it represents, from the first frame alone, the robot by its 3D model and the objects the gripper may touch as 3D points; a rule-based simulator with no trained parameters moves them under the actions, and a video model renders the result. SimPWM returns the realistic video together with the simulated state. We then freeze the simulated objects while the arm moves as recorded and check whether the video still shows the object lifted. On DROID episodes from unseen setups, the answer differs for the arm and for the objects. With each of three base video models, the arm follows the proxy (robot IoU 0.75-0.78, against at most 0.69 for end-to-end models); rendering the robot alone already gives this. What the simulated objects add is the object state: against a robot-only proxy, they cut missed pick-ups from 54% to 38%, and the video follows them only with some base models: on rigid objects, freezing them lowers the lift rate of MiniMax-H3, fine-tuned on episodes whose simulation agrees with the real video, from 42% to 10%, but that of LTX-2.3, trained on the same episodes, only from 57% to 49%, as if it inferred the grasp from the arm motion; more than half of the remaining lifts of MiniMax-H3 are of cloth and rope, which the simulator carries rigidly. With any base model, the simulated state records what the simulation did; under perturbed actions, a video that disagrees with it reveals that the video ignores the simulated state.

</details>

---

### [[20_Research/Papers/具身智能/Seeing_to_Drive_on_a_Single_Board_Attention-Free_Depth_for_Onboard_Robot_Navigation|Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation]]

![[assets/2611.32718_figure.png|800]]

- **arXiv**: [2611.32718](https://arxiv.org/abs/2611.32718)
- **PDF**: https://arxiv.org/pdf/2611.32718
- **详细分析**: [[20_Research/Papers/具身智能/Seeing_to_Drive_on_a_Single_Board_Attention-Free_Depth_for_Onboard_Robot_Navigation|Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation]]
- **作者**: Itai Mizlish, Boaz Ben-Moshe
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 1.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, MobileNet, ResNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A small ground robot can carry one camera and a few watts of compute, but the depth foundation models that could turn that camera into a range sensor are vision transformers sized for GPUs. We bring one to a Raspberry Pi 5 with the Hailo-8L, an accelerator that runs every layer in integer arithmetic, attention included. Quantised for it, Depth Anything V2 loses large parts of the scene, and we measure why: at 449 tokens, 91% of softmax weights fall below one int8 step while carrying 17-33% of the attention mass. Our answer is to distil, not quantise. An attention-free ResNet-34 U-Net student of Depth Anything V2-Large (24.5M parameters) runs at 27.1 FPS on the chip, its int8 output matches its float twin (Pearson 0.99993), and on held-out scenes of its simulated yard it is the most accurate depth network on the chip (AbsRel 0.269 against 0.354-0.530). On 1,000 stereo-verified points of a real outdoor drive it is not resolvably different from the vendor's Depth Anything V2-Small build, while running faster (27.1 vs 21.6 FPS). Ranging obstacles by where they meet the floor needs only the camera height, so mapping, hybrid-A* planning and SLAM run on the Pi's own CPU. In real-time hardware-in-the-loop tests in a Gaussian-splat reconstruction of a real yard, the stack reaches the goal without contact in 7.9$\pm$1.1 of 10 scenes, against 9.2$\pm$0.4 with exact obstacles, and in 7.7$\pm$0.7 on its own pose with simulated wheel odometry (ten seeds each; 8.2$\pm$0.4 with the real Pi and Hailo-8L in the loop, five seeds). The source code, pre-trained models and data are available at https://github.com/itaim18/DANIEL.

</details>

---

### [[20_Research/Papers/具身智能/Knocked_Off_Course_Tracing_Uncommanded_Motion_from_Perception_to_Action_in_Embodied_VLAs|Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs]]

![[assets/2611.32705_figure.png|800]]

- **arXiv**: [2611.32705](https://arxiv.org/abs/2611.32705)
- **PDF**: https://arxiv.org/pdf/2611.32705
- **详细分析**: [[20_Research/Papers/具身智能/Knocked_Off_Course_Tracing_Uncommanded_Motion_from_Perception_to_Action_in_Embodied_VLAs|Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs]]
- **作者**: Dan Zlotnikov, Nadav Alali, Ohad Ben-Shahar
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Knocked Off Course: Tracing Uncommanded Motion from Perception to Action in Embodied VLAs》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CameraBench, EVT-Bench, EgoDyn-Bench, OmTrackVLA, RobustVLA, TIC-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs) enable simultaneous processing of egocentric video and textual target descriptions to produce action commands for embodied tracking platforms. However, these platforms rarely move exactly as commanded, in part due to unexpected environmental disturbances such as wind, unleveled terrain, and road bumps. Here we study how such models handle uncommanded egomotion. First, we explore performance across diverse disturbances by benchmarking three tracking VLAs on three datasets. We find that models differ in which environmental disturbances hurt them most, but all are sensitive to sudden target loss. Tracing egomotion from pixels to emitted actions, we identify two gaps. In representation, motion is reliably recovered through explicit relations between frames, but aggressive compression of past frames weakens small-motion readouts. In action, large rotations do reach the decision state, yet the decoded direction carries only a few percent of a mirrored rotation's effect on the turn. Targeting both gaps, we fine-tune one model, Uni-NaVid, on data amounting to just 1.7% of its original training set in a ladder of analysis-motivated variants. These gain 5-22 points after target-loss without degrading clean success; after a smooth loss, the best one improves success by 72% (relative), recovering 76% of its gap to clean. We also show that targeted fine-tuning improves recovery partly via a text-mediated action dependency, without new architecture, large-scale data collection or training from scratch.

</details>

---

### [[20_Research/Papers/机器人/GOLD-SLAM_Gaussian-splatting_Omnidirectional_LiDAR-Depth_SLAM|GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM]]

![[assets/2611.32335_figure.png|800]]

- **arXiv**: [2611.32335](https://arxiv.org/abs/2611.32335)
- **PDF**: https://arxiv.org/pdf/2611.32335
- **详细分析**: [[20_Research/Papers/机器人/GOLD-SLAM_Gaussian-splatting_Omnidirectional_LiDAR-Depth_SLAM|GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM]]
- **作者**: Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Systems

#### 研究背景与动机

《GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate geometric reconstruction. It performs tracking and mapping in the spherical domain and uses tracked visual features in regions without LiDAR coverage to improve pose estimation. To address insufficient coverage of newly observed surfaces and floating artifacts during incremental mapping, we introduce Depth-Aware Map Extension and Pruning (DAEP). To enable broader evaluation, we collect a new dataset, WHOLE, using a UAV platform across Weak-geometry, High-dynamic, Omnidirectional, Low-light, and Easy scenarios. Extensive experiments on public benchmarks and WHOLE demonstrate competitive rendering quality and improved geometric accuracy relative to perspective systems. Compared with existing panoramic baselines, GOLD-SLAM improves mean PSNR by 5.56-9.10 dB and reduces mean Depth-L1 by 71.9-83.9%. To assess deployment feasibility on resource-constrained platforms such as UAVs, we evaluate an embedded configuration of GOLD-SLAM on a Jetson Orin NX (16 GB), demonstrating online operation at the cost of reconstruction quality.

</details>

---

### [[20_Research/Papers/具身智能/Motion_Chain_of_Thought_Disentangling_Motion_Semantics_from_Visual_Appearance_for_Robotic_Manipulation|Motion Chain of Thought: Disentangling Motion Semantics from Visual Appearance for Robotic Manipulation]]

![[assets/2611.32241_figure.png|800]]

- **arXiv**: [2611.32241](https://arxiv.org/abs/2611.32241)
- **PDF**: https://arxiv.org/pdf/2611.32241
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Chain_of_Thought_Disentangling_Motion_Semantics_from_Visual_Appearance_for_Robotic_Manipulation|Motion Chain of Thought: Disentangling Motion Semantics from Visual Appearance for Robotic Manipulation]]
- **作者**: Xiangkai Ma, Xinyi Wang, Junjie Wang, Sheng Xu, Mingyang Li, Yue Ma, Han Zhang, Yuzheng Zhuang, Wenzhong Li, Zhihao Yuan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Motion Chain of Thought: Disentangling Motion Semantics from Visual Appearance for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) aim to construct a unified architecture capable of understanding world state evolution and guiding action generation. However, existing visual branches focus on predicting static visual observation, rather than reflecting potential transition information that captures the evolution of world states under motion interactions. This leads to representational entanglement between high-level physical condition evolution and low-level action trajectory generation within the Action Model, creating a structural bottleneck while weakening the predictive capability of world evolution modeling for action generation. We propose PILOT (Physical Inference for Latent Optimized Trajectories), whose core Representational Deduction (RD) bridges this gap by integrating motion chain-of-thought (CoT) guidance as a native model capability. Specifically, RD aims to encourage the action branch to explicitly model potential state transition tokens, which are retained as CoT in the reasoning space to guide fine-grained motion trajectory. Experiments demonstrate that RD not only improves the success rate and generalization ability of WAMs in complex robotic manipulation tasks but also enhances the model's physical interpretability by decoupling high-level motion semantics from low-level trajectory details. Furthermore, the abundant state transition supervision signals introduced by RD effectively alleviate the sparse supervision in action generation, supporting data-efficient real-robot adaptation with reduced demonstration sets.

</details>

---

### [[20_Research/Papers/具身智能/Seeing_Is_Not_Reaching_Instruction_Shortcuts_Override_Visual_Grounding_in_Vision-Language-Action_Models|Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models]]

![[assets/2611.32206_figure.png|800]]

- **arXiv**: [2611.32206](https://arxiv.org/abs/2611.32206)
- **PDF**: https://arxiv.org/pdf/2611.32206
- **详细分析**: [[20_Research/Papers/具身智能/Seeing_Is_Not_Reaching_Instruction_Shortcuts_Override_Visual_Grounding_in_Vision-Language-Action_Models|Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models]]
- **作者**: Qing Zhang, Xuesong Li, Zhaoyuan Yang, Changlin Song, Xinyu Tian, Jing Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA, TurboVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) are expected to inherit visual grounding from vision-language models, yet often reach for an object's training location after it has been moved. Across six VLAs, we identify two shortcuts: a scene shortcut, where the arm follows the scene's original task despite a new instruction, and an instruction shortcut, where the instruction retrieves the requested object's training location. In $π_{0.5}$, the instruction shortcut persists even though object-name attention follows the moved target. We call this Seeing Is Not Reaching. To determine whether this grounding is unused or overridden, we separately mask an image-mediated grounding pathway and a direct instruction-to-action pathway. Masking the grounding pathway eliminates reaches to moved targets, whereas masking the direct pathway increases them. Thus, grounding already guides action but is often overridden by the instruction shortcut, which acts through the direct pathway. We introduce Pathway-Separated Guidance (PSG), which amplifies grounding and suppresses the shortcut without training or external target locations. On LIBERO-PRO Object under Position perturbations, PSG raises the target-reaching rate from 22.0% to 52.6% and task success from 16.6% to 40.8%, while largely preserving performance on the original tasks.

</details>

---

### [[20_Research/Papers/机器人/OVOK_A_Recursive_Self-Improving_Agentic_Framework_for_Video-Based_Articulated_Robot_State_Estimation|OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation]]

![[assets/2611.32185_figure.jpg|800]]

- **arXiv**: [2611.32185](https://arxiv.org/abs/2611.32185)
- **PDF**: https://arxiv.org/pdf/2611.32185
- **详细分析**: [[20_Research/Papers/机器人/OVOK_A_Recursive_Self-Improving_Agentic_Framework_for_Video-Based_Articulated_Robot_State_Estimation|OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation]]
- **作者**: Cheng Dai, Renkai Luo, Guanfeng Tang, Siming Li, Hao Zhao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《OVOK: A Recursive Self-Improving Agentic Framework for Video-Based Articulated Robot State Estimation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CtRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recovering articulated robot state from video supports metric spatial sensing for manipulation, scene reconstruction, and action planning. Yet the problem is ill-posed: different intrinsics, camera-to-robot poses, and joint angles can explain similar observations. Prior task-specific regressors typically assume known intrinsics, fit one robot through laborious data collection and robot-specific training, and still transfer poorly across scenes. Foundation models apply to any robot zero-shot, but their estimates have large errors. We present OVOK (One Video to Kinetics), a recursive self-improving agentic framework for this task. Under a human-authored protocol, an agentic initializer constructs robot-specific OVOK-4k; a proposer--executor--verifier loop then jointly evolves tools and executable workflows from feedback. Updated tools and workflows are accepted only when the verifier judges a positive improvement. The retained workflow is frozen for accurate inference. Experiments demonstrate that the evolved workflow achieves state-of-the-art results on DREAM-V and RoboKeyGen-V, delivering robust and accurate estimates.

</details>

---

### [[20_Research/Papers/世界模型/RoboProbe_Benchmarking_Physical_Plausibility_of_Robot_World_Models|RoboProbe: Benchmarking Physical Plausibility of Robot World Models]]

![[assets/2611.32152_figure.png|800]]

- **arXiv**: [2611.32152](https://arxiv.org/abs/2611.32152)
- **PDF**: https://arxiv.org/pdf/2611.32152
- **详细分析**: [[20_Research/Papers/世界模型/RoboProbe_Benchmarking_Physical_Plausibility_of_Robot_World_Models|RoboProbe: Benchmarking Physical Plausibility of Robot World Models]]
- **作者**: Zhuoying Yang, Jiachen Ni, Yichen Guo, Xiaoshan Wu, Mengyu Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.3，大模型 0.1，世界模型 0.8，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboProbe: Benchmarking Physical Plausibility of Robot World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KineBench, PAI-Bench, PDI-Bench, RBench, RP-Bench, World-in-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating the physical plausibility of generated videos is critical for reliable robotic planning with world models. These videos inform action proposal and assessment before real-world execution, so undetected physical violations can lead to erroneous assessments of action feasibility and safety. Yet current video generators often produce physically implausible interactions. Detecting such violations directly with vision-language models (VLMs) remains challenging as physical verification requires evidence-grounded spatiotemporal reasoning beyond high-level semantic understanding. We develop five law-specific metrics for evaluating physical plausibility by combining spatiotemporal evidence from segmentation, tracking, 3D geometry, or appearance comparisons with targeted VLM reasoning: Contact fidelity, Object persistence, Solidity, Robot deformation, and Object deformation. Building on this metric suite, we introduce RoboProbe, an agentic evaluation framework that coordinates metric execution and selectively refines evaluations through constrained actions. To evaluate the physical plausibility of robot world models, we further introduce RP-Bench, with 761 human-labeled generated videos and 130 real demonstrations of 239 manipulation tasks from 12 robot datasets. On RP-Bench, all five metrics achieve AUROCs above 0.85 and outperform the evaluated learned judges, prior evaluators, and a frames-only Gemini baseline. Applying these metrics to five video generators reveals distinct patterns of physical violations across models, in both violation types and frequencies.

</details>

---

### [[20_Research/Papers/大模型/PhysRF-WorldJEPA_Transforming_Heterogeneous_Large_Language_Models_into_Manifold-Decoupled_Millimeter-Wave_Radar_World_Models|PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models]]

![[assets/2611.32113_figure.png|800]]

- **arXiv**: [2611.32113](https://arxiv.org/abs/2611.32113)
- **PDF**: https://arxiv.org/pdf/2611.32113
- **详细分析**: [[20_Research/Papers/大模型/PhysRF-WorldJEPA_Transforming_Heterogeneous_Large_Language_Models_into_Manifold-Decoupled_Millimeter-Wave_Radar_World_Models|PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models]]
- **作者**: Yicheng Huang, Feng Ke, Linhan Chen, Ziyi Jiang, Xiu Yin Zhang
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 机器人, 强化学习
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.16，世界模型 0.76，机器人 0.2）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《PhysRF-WorldJEPA: Transforming Heterogeneous Large Language Models into Manifold-Decoupled Millimeter-Wave Radar World Models》归入 世界模型、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting Large Language Models (LLMs) to millimeter-wave (mmWave) radar enables privacy-preserving, all-weather physical scene understanding across darkness, smoke, and walls. However, standard instruction tuning treats continuous radar streams as static text-like tokens, causing near-random global radar-to-text retrieval and severe physical drift under sensor blackouts. Conversely, coupling pairwise contrastive losses (e.g., SigLIP) directly into the shared backbone improves retrieval but injects $O(B^2)$ repulsive gradients that fracture continuous coordinate manifolds ($R^2 &lt; 0$). We present PhysRF-WorldJEPA, a manifold-decoupled Joint-Embedding Predictive Architecture (JEPA) that separates continuous electromagnetic state prediction from cross-modal language alignment. An unattenuated 1.0x clock anchor and parallel dual-scale RF encoder feed a lean ~3% LoRA LLM trained with two-step state-space EMA-JEPA (Denoise -&gt; Rollout) and sample-axis Batch-VICReg to predict +3.0 s physical states; a stop-gradient alignment head then maps frozen prompt states onto the text hypersphere with false-negative masking. On a 4,541-window tri-domain suite (77/60.25/60 GHz) against 10 baselines, freezing the physical backbone and training only the decoupled head lifts R-&gt;T R@10 from 5.95% to 15.01% and improves MedRank from 107.0 to 60.0 while preserving identical physical readout: 3.37 deg ($R^2=+0.961$) blackout +3.0 s torso tilt, 1.89 m ($R^2=+0.679$; 1.19 m/+0.863 at the RF front-end) cluttered UAV altitude, 2.04 m ($R^2=+0.461$) behind-wall NLOS range, 0.9976 virtual-RIS invariance, and 100% fall recall. Across five 0.5B-1.8B LLM families (15 zero-overhead models), World-JEPA improves retrieval and 75%-drop completion in 10/10 runs and blackout tilt in 4/5 (Span-Euc), 2/5 (Scatter), and 5/5 (per-family best) over SFT.

</details>

---

### [[20_Research/Papers/具身智能/RoboHarness-RL_Agentic_Reinforcement_Learning_for_VLM-Based_Robot_Manipulation|RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation]]

![[assets/2611.32016_figure.png|800]]

- **arXiv**: [2611.32016](https://arxiv.org/abs/2611.32016)
- **PDF**: https://arxiv.org/pdf/2611.32016
- **详细分析**: [[20_Research/Papers/具身智能/RoboHarness-RL_Agentic_Reinforcement_Learning_for_VLM-Based_Robot_Manipulation|RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation]]
- **作者**: Liyang Li, Mingyu Liu, Xiaoman Li, Zhiyue Zhao, Jin-Chuan Shi, Canyu Zhao, Haokai Zhang, Jinyuan Tian, Linhao Zhong, Hao Chen, Chunhua Shen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 4.1（加权：具身智能 1.8，大模型 0.4，强化学习 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboHarness-RL: Agentic Reinforcement Learning for VLM-Based Robot Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgenticRoboRL, CaP-RL, Contact-GraspNet, RoboHarness-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic harnesses enable frontier vision-language models (VLMs) to manipulate robots through perception, planning, and control tools, yet achieving comparable performance with compact open-weight VLMs remains challenging. We present RoboHarness-RL, an agentic reinforcement learning framework for improving VLM-based robot manipulation through tool calls. Starting from supervised fine-tuning on successful teacher demonstrations, the VLM further improves through multi-turn reinforcement learning with task-outcome rewards, without relying on vision-language-action models or world action models. To support efficient multi-turn training, we develop LiteHarness, which uses hierarchical memory to keep interaction contexts compact while preserving task performance. With Qwen3.5-9B, RL raises success from 31.2% to 44.0% on RoboTwin 2.0 and from 57.8% to 73.3% on LIBERO-Pro; these gains extend to randomized RoboTwin scenes unseen during training (26.4% to 38.0%). Behavioral analysis further shows that RL reduces repetitive-call rates by up to $4\times$, shortens successful executions, and improves recovery from negative feedback. Project page: https://aim-uofa.github.io/RoboHarness-RL/

</details>

---

### [[20_Research/Papers/具身智能/DUALingo_A_Dual-Hand_Instruction-Guided_Dataset_for_Affordance_Grounding_on_3D_Objects|DUALingo: A Dual-Hand Instruction-Guided Dataset for Affordance Grounding on 3D Objects]]

![[assets/2611.31919_figure.png|800]]

- **arXiv**: [2611.31919](https://arxiv.org/abs/2611.31919)
- **PDF**: https://arxiv.org/pdf/2611.31919
- **详细分析**: [[20_Research/Papers/具身智能/DUALingo_A_Dual-Hand_Instruction-Guided_Dataset_for_Affordance_Grounding_on_3D_Objects|DUALingo: A Dual-Hand Instruction-Guided Dataset for Affordance Grounding on 3D Objects]]
- **作者**: Ming-Lun Lee, Yi-En Li, Feng-Dian Su, Ming-Han Lee, Kun-Ru Wu, Krzysztof Czarnecki, Yu-Chee Tseng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《DUALingo: A Dual-Hand Instruction-Guided Dataset for Affordance Grounding on 3D Objects》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AffordanceNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Affordance grounding localizes where an agent should interact with an object to perform a task. Many everyday manipulation tasks, however, require bimanual affordance, in which two hands assume complementary and cooperative roles to accomplish a shared goal. Existing 3D affordance datasets primarily ground single interaction regions, and manually annotating dual-hand, cooperative contacts does not scale. To address this gap, we introduce DUALingo, a large-scale dataset for task-conditioned, role-aware bimanual 3D affordance grounding on diverse everyday objects. DUALingo represents each task as two cooperative, hand-agnostic roles, each grounded as a heatmap on the object surface. It contains 271K free-form tasks on 71K objects, generated by a fully automated pipeline of open-weight foundation models without human labeling. Expert ratings and a validated LLM judge confirm the quality of the resulting annotations. Trained on DUALingo, existing 3D affordance models learn to ground both cooperative roles from natural-language instructions, with the best-performing model achieving a more than threefold improvement in aIoU over the zero-shot baseline, from 10.3 to 37.8. Robotic manipulation demonstrations illustrate the actionability of the predicted bimanual affordances in performing cooperative tasks. These results position DUALingo as a scalable foundation for learning everyday bimanual affordances. Project page: https://nycu-pair-labs.github.io/DUALingo/

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Expert_Replay_Cross-Instruction_Anchoring_for_Continual_Vision-Language-Action_Learning|Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning]]

![[assets/2611.31903_figure.png|800]]

- **arXiv**: [2611.31903](https://arxiv.org/abs/2611.31903)
- **PDF**: https://arxiv.org/pdf/2611.31903
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Expert_Replay_Cross-Instruction_Anchoring_for_Continual_Vision-Language-Action_Learning|Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning]]
- **作者**: Ziyang Chen, Dehua Chen, Shaoguang Wang, Xu Yan, Hao Huang, Tao Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Beyond Expert Replay: Cross-Instruction Anchoring for Continual Vision-Language-Action Learning》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, Info-VLA, OpenVLA, QwenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models need to continually acquire new manipulation skills while retaining the ability to follow previously learned instructions. Experience replay (ER) can mitigate catastrophic forgetting, but retaining only a small number of historical expert frames per task leaves many old-instruction responses without direct supervision. Under limited replay, we observe a structured failure mode in which an earlier instruction can trigger a subsequently learned, competing goal. To address this gap, we propose Cross-Instruction Anchoring (XIA), which supplements expert replay with instruction-conditioned response preservation. At each task boundary, XIA freezes the previous policy as a teacher and matches its responses to old instructions paired with current observations. This extends supervision beyond stored historical examples without requiring additional expert replay data. Experiments across multiple VLA architectures and three LIBERO suites demonstrate improved success rates and reduced forgetting compared with ER under identical historical expert-data budgets. Additional RoboCasa and real-world experiments further support the effectiveness of XIA.

</details>

---

### [[20_Research/Papers/具身智能/LeanWAM_Learning_Latent_World_Action_Models_from_Frozen_Video_Models|LeanWAM: Learning Latent World Action Models from Frozen Video Models]]

![[assets/2611.31740_figure.png|800]]

- **arXiv**: [2611.31740](https://arxiv.org/abs/2611.31740)
- **PDF**: https://arxiv.org/pdf/2611.31740
- **详细分析**: [[20_Research/Papers/具身智能/LeanWAM_Learning_Latent_World_Action_Models_from_Frozen_Video_Models|LeanWAM: Learning Latent World Action Models from Frozen Video Models]]
- **作者**: Shaolong Li, Hongze Fu, Joyce Chai, Yinpei Dai
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LeanWAM: Learning Latent World Action Models from Frozen Video Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：InternVLA, OpenVLA, PDRVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models (WAMs) typically adapt large pretrained video generators to jointly predict future observations and robot actions, incurring substantial training and deployment costs. However, it remains unclear which future representations a policy actually needs and how compactly they can be represented. Our probing study shows that complementary future representations can be compressed into a few tokens while retaining most of their action-decoding performance. Motivated by this finding, we introduce LeanWAM, a latent WAM that transfers video priors from a frozen video generator to a lightweight policy via two-stage training. In the first stage, a Future Extractor compresses observed transitions into 32 predictive tokens. These tokens condition the frozen generator and are jointly shaped by action, RGB, semantic, and geometric supervision, while a compact readout of the generator's hidden states supplies complementary world tokens. The second stage distills both representations into the policy, which learns to predict them from current observations while generating actions. With 1.4B parameters and no large-scale embodied pretraining, LeanWAM outperforms strong vision-language-action (VLA) and WAM baselines on LIBERO, LIBERO-Plus, and RoboTwin~2.0. It predicts an action chunk in 25.1\,ms on an A100 GPU, 12.3--41.5$\times$ faster than representative WAMs. These results demonstrate that compact predictive supervision can transfer video priors to robust and efficient control.

</details>

---

### [[20_Research/Papers/具身智能/GeoMVGen_Joint_Appearance-Geometry_Modeling_for_Multi-View_Video_Generation_in_Robotic_Manipulation|GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation]]

![[assets/2611.31689_figure.png|800]]

- **arXiv**: [2611.31689](https://arxiv.org/abs/2611.31689)
- **PDF**: https://arxiv.org/pdf/2611.31689
- **详细分析**: [[20_Research/Papers/具身智能/GeoMVGen_Joint_Appearance-Geometry_Modeling_for_Multi-View_Video_Generation_in_Robotic_Manipulation|GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation]]
- **作者**: Qiaoqiao Jia, Guile Wu, Dongfeng Bai
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.2，大模型 0.1，机器人 1）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation requires predicting how robot-object interactions evolve over time, encompassing both visual appearance and scene geometry. In multi-camera settings, such predictions need to capture the evolving 3D scene consistently across viewpoints, while supporting controllable generation under different robot actions and camera configurations. Existing video generation models provide strong priors for visual appearance and motion but typically lack explicit geometric modeling. Meanwhile, recent advances in geometry-aware and multi-view generation have explored joint appearance-geometry modeling and cross-view consistency, yet generating temporally coherent appearance and geometry across multiple viewpoints under robotic manipulation conditions remains challenging. In this work, we propose GeoMVGen, a framework for joint multi-view RGB and pointmap video generation in robotic manipulation. Built on a video diffusion transformer, our framework employs modality-specific adaptation modules to capture the distinct characteristics of appearance and geometry, while using cross-modal residual connections to facilitate information exchange between the two modalities. To establish geometric correspondences across viewpoints, we further introduce a cross-view projection mechanism with complementary geometric supervisions, combining pointmap consistency with geometry foundation model-guided feature alignment. These designs enable controllable generation of temporally evolving multi-view observations with coherent appearance and geometrically consistent scene structures. Extensive experiments on 4D video generation dataset comprising simulated and real-world robotic manipulation scenarios demonstrate that GeoMVGen outperforms state-of-the-art methods in video quality, geometric accuracy, and cross-view consistency.

</details>

---

### [[20_Research/Papers/具身智能/Hi3R-VLA_Grounding_Semantics_and_Actions_in_3D|Hi3R-VLA: Grounding Semantics and Actions in 3D]]

![[assets/2611.31535_figure.png|800]]

- **arXiv**: [2611.31535](https://arxiv.org/abs/2611.31535)
- **PDF**: https://arxiv.org/pdf/2611.31535
- **详细分析**: [[20_Research/Papers/具身智能/Hi3R-VLA_Grounding_Semantics_and_Actions_in_3D|Hi3R-VLA: Grounding Semantics and Actions in 3D]]
- **作者**: Shizhe Chen, Paul Pacaud, Cordelia Schmid
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 2.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Hi3R-VLA: Grounding Semantics and Actions in 3D》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Hi3R-VLA, OpenVLA, PointWorld, RLBench, Real-World, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While recent vision-language-action (VLA) models increasingly incorporate 3D geometry, how to effectively exploit it for precise and generalizable action prediction remains a central challenge. We introduce Hi3R-VLA, a 3D policy that grounds heterogeneous modalities - vision, language, and action - in explicit 3D geometry for robotic manipulation. Our model integrates spatially-aligned visual features and language conditioning into point cloud representations, enriching scene geometry with fine-grained, task-relevant semantics. It then anchors low-level control commands in the same 3D coordinate frame and uses 3D-RoPE enhanced action-to-point attention over coarse-to-fine point features to model geometric relationships between action targets and observed points. Our analysis demonstrates the importance of semantic fusion within 3D and spatial alignment between observations and actions. With fewer than 250M trainable parameters, Hi3R-VLA achieves state-of-the-art performance on RoboCasa, RLBench, RoboTwin2, DexJoCo and DexSuite across diverse manipulation tasks and embodiments, from single-arm and dual-arm grippers to dexterous hands. Real-robot evaluations further demonstrate its effectiveness in the physical world. The model, code and dataset are publicly released at https://cshizhe.github.io/projects/hi3r_vla.html.

</details>

---

### [[20_Research/Papers/具身智能/Ground,_Guide,_Act_Improving_VLA_Spatial_Generalization_with_Multimodal_Foundation_Models|Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models]]

![[assets/2611.31452_figure.png|800]]

- **arXiv**: [2611.31452](https://arxiv.org/abs/2611.31452)
- **PDF**: https://arxiv.org/pdf/2611.31452
- **详细分析**: [[20_Research/Papers/具身智能/Ground,_Guide,_Act_Improving_VLA_Spatial_Generalization_with_Multimodal_Foundation_Models|Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models]]
- **作者**: Guangting Zheng, Shaoxuan Wang, Yu Yuan, Zhipeng Tang, Jiajun Deng, Yanyong Zhang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.4，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Ground, Guide, Act: Improving VLA Spatial Generalization with Multimodal Foundation Models》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALOHA-Sim, MFM-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models effectively learn action policies from robot demonstrations, but struggle to generalize to changes in object positions and task goals. General multimodal foundation models (MFMs) offer complementary scene understanding and spatial reasoning, but remain slow and unreliable for direct fine-grained control. To understand how MFMs can improve VLA spatial generalization, we conduct a systematic capability analysis across multiple VLA architectures using atomic-stage interventions, revealing that many failures stem from poor target grounding and global spatial routing, while local manipulation skills remain largely usable. Based on these findings, we propose MFM-VLA, a selective collaboration framework in which an MFM provides target grounding and spatial guidance, controllers execute free-space motion, and the VLA retains control over fine-grained manipulation. We fine-tune the VLA with action-chunk-level dense geometric captions and perturbed-state recovery data to improve local guidance following and recovery from unfamiliar handoff states. A development-calibrated capability router selects between direct VLA execution and MFM-assisted execution to avoid unnecessary intervention. Across LIBERO-PRO, ALOHA-Sim-PRO, RoboCasa365, and real-world chemistry tasks, MFM-VLA improves success rates by 14.9, 74.0, 3.6, and 30.9 percentage points, respectively, over the corresponding base VLA. The project page is available at https://tom-zgt.github.io/MFM-VLA

</details>

---
