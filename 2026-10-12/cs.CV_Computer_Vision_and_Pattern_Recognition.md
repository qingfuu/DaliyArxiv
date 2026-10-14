# cs.CV | Computer Vision and Pattern Recognition | 2026-10-12

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/具身智能/Splat2Act_From_Captured_Scenes_to_Personalized_VLA_Manipulation|Splat2Act: From Captured Scenes to Personalized VLA Manipulation]]

![[assets/2610.13945_figure.png|800]]

- **arXiv**: [2610.13945](https://arxiv.org/abs/2610.13945)
- **PDF**: https://arxiv.org/pdf/2610.13945
- **详细分析**: [[20_Research/Papers/具身智能/Splat2Act_From_Captured_Scenes_to_Personalized_VLA_Manipulation|Splat2Act: From Captured Scenes to Personalized VLA Manipulation]]
- **作者**: Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim, Gunjan Chhablani, Muhammad Zubair Irshad, Zsolt Kira
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Splat2Act: From Captured Scenes to Personalized VLA Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GSWorld, GenSim, OpenVLA, Real-World, Real-to-Sim, Real2Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy to a specific scene and object set using only a handheld phone scan and images of the user's objects. Unlike prior real-to-sim work that reconstructs individual tabletops, Splat2Act operates on building-scale indoor environments: it builds a photorealistic digital twin with 3D Gaussian Splatting and collision geometry, automatically discovers tabletop and non-tabletop receptacles, constructs feasible pickup tasks, and generates successful demonstrations with a privileged simulation oracle, with only scene and object capture required from a human. Applied to 101 scanned campus environments with a median navigable area of 104.87 m$^2$ and 7 receptacles, the pipeline yields 852 receptacles and over 68,000 pickup demonstrations. We fine-tune $π_{0.5}$ in two stages: Stage 1 adapts to hundreds of public object assets, drawn either from the deployment scene alone or from all 101 scenes; Stage 2 personalizes to the user's own objects on the deployment scene's receptacles. Our strongest personalized policy reaches 62.5% aggregate pickup success in the target scene. Deployed on a real Stretch 3, the same policy achieves 63.9% success on a 12-task subset, closely tracking its 66.7% simulated success on those tasks. These results suggest that automated real-to-sim-to-real training can personalize VLA manipulation policies using only simulation-oracle data.

</details>

---

### [[20_Research/Papers/强化学习/Chronos_Policy_Learning_Robot_Policies_on_Physical_Time|Chronos Policy: Learning Robot Policies on Physical Time]]

![[assets/2610.13929_figure.png|800]]

- **arXiv**: [2610.13929](https://arxiv.org/abs/2610.13929)
- **PDF**: https://arxiv.org/pdf/2610.13929
- **详细分析**: [[20_Research/Papers/强化学习/Chronos_Policy_Learning_Robot_Policies_on_Physical_Time|Chronos Policy: Learning Robot Policies on Physical Time]]
- **作者**: Changhao Wang, Jaden Clark, Shuran Song
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Chronos Policy: Learning Robot Policies on Physical Time》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes. We introduce Chronos Policy, which makes physical time explicit by conditioning on observation capture times and desired action execution times. We study two ways to incorporate time into a diffusion transformer: adding timestamp embeddings to token features, or encoding physical time in positional encoding through time-aware rotary positional encodings (time-aware RoPE). We find that time-aware RoPE is more robust, allowing attention to depend directly on physical time while keeping token content unchanged. During training, we temporally randomize which observations are sampled and when the action chunk begins, exposing the policy to a wider range of sensing and execution schedules that may occur during deployments. This also enables learning from asynchronous, multi-rate data without forcing all measurements onto a fixed temporal grid. Across simulation and real-world experiments, Chronos Policy improves performance on dynamic tasks, where observation-to-action timing is critical, and on multisensory tasks, where the relative timing between observations matters. On standard quasi-static tasks, it preserves nominal performance while improving robustness to changes in sensing and inference timing.

</details>

---

### [[20_Research/Papers/强化学习/Dream_to_Remember_Continual_Steering_of_Generalist_Robot_Policies_with_World_Models|Dream to Remember: Continual Steering of Generalist Robot Policies with World Models]]

![[assets/2610.13816_first_page.png|800]]

- **arXiv**: [2610.13816](https://arxiv.org/abs/2610.13816)
- **PDF**: https://arxiv.org/pdf/2610.13816
- **详细分析**: [[20_Research/Papers/强化学习/Dream_to_Remember_Continual_Steering_of_Generalist_Robot_Policies_with_World_Models|Dream to Remember: Continual Steering of Generalist Robot Policies with World Models]]
- **作者**: Bahey Tharwat, Iman Nematollahi, Marvin Alles, Xingyuan Zhang, Akshay L Chandra, Abhinav Valada
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 强化学习, 具身智能
- **相关性评分**: 2.92（加权：具身智能 0.3，强化学习 0.56，世界模型 0.96，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Dream to Remember: Continual Steering of Generalist Robot Policies with World Models》归入 机器人、世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：A2World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies are trained with imitation learning and are bounded by the quality and coverage of their demonstrations. Reinforcement learning can improve and extend them, either by fine-tuning the policy weights or by training a small module to steer the input noise of a frozen generative policy. When tasks arrive sequentially, both approaches suffer from catastrophic forgetting. Fine-tuning on a task degrades prior tasks, and steering only shifts forgetting to the shared steering module. We propose Dream to Remember (D2R), which continually steers a frozen generalist policy toward new tasks, while retaining its earlier skills. As the steering module learns a new task, a frozen pretrained world model rehearses prior tasks through imagined rollouts, anchoring the module to its earlier behavior without a replay buffer or new data. When the world model is faithful enough, D2R learns the new task entirely in imagination. Otherwise, it learns the task in the environment while using the world model only to rehearse prior tasks. On CALVIN, D2R improves eight tasks in sequence entirely in imagination, raising average success from 63.7% to 74.8%, while LoRA fine-tuning on the same sequence drops it to 11.7%. With a frozen off-the-shelf generalist policy and world model, $π_0$ and A2World, D2R learns unseen LIBERO-90 tasks in the environment while keeping $π_0$'s performance on the LIBERO suites it was fine-tuned on, even though the world model is not accurate enough for policy optimization. Finally, on a real Franka robot, D2R improves three tasks in sequence entirely in imagination while retaining the earlier improvements.

</details>

---

### [[20_Research/Papers/具身智能/RARA_Robust_Policy_Fine-Tuning_through_Retrieval-Anchored_Representation_Alignment_for_Robotic_Manipulation|RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation]]

![[assets/2610.13578_figure.png|800]]

- **arXiv**: [2610.13578](https://arxiv.org/abs/2610.13578)
- **PDF**: https://arxiv.org/pdf/2610.13578
- **详细分析**: [[20_Research/Papers/具身智能/RARA_Robust_Policy_Fine-Tuning_through_Retrieval-Anchored_Representation_Alignment_for_Robotic_Manipulation|RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation]]
- **作者**: Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves representation features from pretraining with similar task intent and motion, and aligns the policy's representations of the target demonstrations with the pre-trained representations of the retrieved demonstrations. Second, RARA fine-tunes the policy on the target demonstrations while limiting how much its representations of the retrieved demonstrations change during fine-tuning. By reducing the representation mismatch before action learning and preserving pre-trained knowledge during adaptation, RARA limits unnecessary representation drift during fine-tuning. Experiments with Diffusion Policy and GR00T on 13 tasks in RoboTwin, RoboCasa, and on a real robot show that RARA improves the average success of fine-tuning by 9.5 points in-distribution and 13.6 points out-of-distribution, and outperforms all compared baselines. Project page: https://shua-kang.github.io/RARA_robot/

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Successful_Robot_Demonstrations_Learning_from_Human_Interactions_and_Modeling_Failure_Dynamics|Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics]]

![[assets/2610.13522_figure.png|800]]

- **arXiv**: [2610.13522](https://arxiv.org/abs/2610.13522)
- **PDF**: https://arxiv.org/pdf/2610.13522
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Successful_Robot_Demonstrations_Learning_from_Human_Interactions_and_Modeling_Failure_Dynamics|Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics]]
- **作者**: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.2，世界模型 0.4，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, Ctrl-World, IRASim, SC3-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions. However, existing robotic datasets provide limited coverage of the diverse interaction dynamics required for generalizable world modeling. Large-scale egocentric human videos offer complementary interaction experience, yet the embodiment gap between human hands and robotic manipulators hinders effective cross-embodiment learning. Meanwhile, the predominance of successful demonstrations leaves failure dynamics substantially underrepresented, limiting the ability of world models to anticipate unsuccessful executions. To address these limitations, we introduce HF-WM, an action-conditioned world model that combines Human interaction learning with Failure-aware post-training. To bridge the embodiment gap, we develop a dual-branch framework that couples video generation with auxiliary pointflow prediction, using stabilized pointflow as a unified motion representation across human and robot interactions while suppressing egocentric camera motion. To improve failure modeling, we further perform Group Relative Policy Optimization (GRPO) post-training on perturbed actions derived from successful demonstrations, guided by action alignment and physical plausibility rewards, enabling the model to learn plausible failure dynamics without paired ground-truth videos. Extensive experiments demonstrate that HF-WM achieves state-of-the-art performance in action-conditioned video generation and exhibits strong utility for policy evaluation in downstream robotic tasks.

</details>

---

### [[20_Research/Papers/具身智能/Dual-Stream_Memory_for_Vision-Language-Action_Policies|Dual-Stream Memory for Vision-Language-Action Policies]]

![[assets/2610.13262_figure.png|800]]

- **arXiv**: [2610.13262](https://arxiv.org/abs/2610.13262)
- **PDF**: https://arxiv.org/pdf/2610.13262
- **详细分析**: [[20_Research/Papers/具身智能/Dual-Stream_Memory_for_Vision-Language-Action_Policies|Dual-Stream Memory for Vision-Language-Action Policies]]
- **作者**: Yang Wang, Ping Liu, Ruiyu Wang, Xuhua Chen, Lingfeng Zhang, Tao Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Dual-Stream Memory for Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeltaNet, MemoryVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-dependent manipulation requires a policy to track execution state and recover visual evidence that is no longer observable. We propose dual-stream memory for vision-language-action policies, assigning these requirements to complementary representations. A task-agnostic Gated DeltaNet compresses history into one temporal token, supervised by progress prediction and action-conditioned feature reconstruction. A task-conditioned retriever retains frames above a fixed relevance threshold; linear multi-scale fusion encodes each frame into sixteen spatial tokens. We then freeze the temporal compressor and jointly optimize retrieval and policy learning. Across sixteen RoboMME tasks, the complete model achieves 49.22% mean success versus 44.51% for the published FrameSamp+Modul reference, improving fourteen tasks and all four suite means. On four real-robot tasks, mean success reaches 62.5% versus 37.5%, with the largest gains on repeated actions requiring execution-stage discrimination. These results support combining execution context with selective visual access, while failures under cup swaps expose persistent identity tracking as an unresolved requirement.

</details>

---

### [[20_Research/Papers/具身智能/StereoEngine_Scaling_Stereo_Bimanual_Robot_Data_without_Stereo_Cameras|StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras]]

![[assets/2610.12734_figure.png|800]]

- **arXiv**: [2610.12734](https://arxiv.org/abs/2610.12734)
- **PDF**: https://arxiv.org/pdf/2610.12734
- **详细分析**: [[20_Research/Papers/具身智能/StereoEngine_Scaling_Stereo_Bimanual_Robot_Data_without_Stereo_Cameras|StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras]]
- **作者**: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, StereoVLA, StereoWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stereo vision is increasingly used for robotic manipulation, with a growing body of work incorporating it into Vision-Language-Action (VLA) models. However, the scarcity of large-scale, real-world stereo datasets remains a fundamental bottleneck for scaling such policies. Recent generative monocular-to-stereo methods target settings such as VR content and autonomous driving. No prior work produces realistic synthetic stereo data for robotic manipulation, where stereo supervision has come predominantly from simulation. We propose StereoEngine, which introduces two complementary methods to synthesize stereo data for robotic manipulation. In the first, we warp a monocular (left) video into the right view using estimated depth and inpaint the disoccluded regions with a video diffusion model, lifting monocular demonstrations into stereo pairs without training on real stereo. In the second, we render a stereo pair in simulation and jointly generate both photorealistic views, producing consistent left-right data without any real video as input. StereoEngine outperforms existing baselines in generated stereo quality, and using its synthetic data for policy mid-training or task-specific fine-tuning substantially improves downstream bimanual manipulation. Project website: https://stereoengine.github.io

</details>

---

### [[20_Research/Papers/具身智能/Fly-by-Code_Embodied_Coding_Agents_for_Aerial_Manipulation_with_Active_Visual_and_Physical_Feedback|Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback]]

![[assets/2610.12549_figure.png|800]]

- **arXiv**: [2610.12549](https://arxiv.org/abs/2610.12549)
- **PDF**: https://arxiv.org/pdf/2610.12549
- **详细分析**: [[20_Research/Papers/具身智能/Fly-by-Code_Embodied_Coding_Agents_for_Aerial_Manipulation_with_Active_Visual_and_Physical_Feedback|Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback]]
- **作者**: Jaewoo Lee, Jeongyeon Seo, Sihyun Cho, Gyeongrak Choe, Yutong Wang, Bavin Saravanan, Jia-Bin Huang, Furong Huang, Sebastian Scherer, Guanya Shi, H. Jin Kim, Seungjae Lee...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied coding agents construct robot policies from natural-language instructions by generating executable programs and refining them from execution feedback. This refinement assumes that execution feedback reveals whether the task succeeded and, after a failure, provides sufficient evidence to guide program revision. Aerial manipulation violates this assumption in two ways. Payload constraints restrict onboard camera coverage and leave task-critical outcomes outside the robot's view (partial observability), while strong dynamic coupling and limited control margins make physical interactions fragile (limited interaction robustness) and leave failure causes unresolved. Re-examining the same feedback cannot recover observations that were never collected or separate failure causes that the available evidence does not distinguish. To acquire this missing evidence, we introduce Active Feedback (AF), an active "View and Probe" framework. When execution feedback leaves unresolved questions, the agent synthesizes a separate diagnostic program that runs in simulation to inspect unseen outcomes from informative viewpoints (View) or test hypotheses about failure causes through targeted physical interactions (Probe). Across six simulated aerial manipulation tasks with 60 trials per condition, AF reduces false completion declarations from 25 to 5 and raises final task success from 31.7% to 75% compared with terminal feedback under the same coding-agent configuration and task-execution limit. Using shared robot APIs, task programs refined with AF in simulation run on a physical aerial manipulator without task-program source-code modification and complete multi-stage manipulation tasks in the real world. These results show that executable diagnosis fills gaps in execution feedback for embodied coding agents, improving both completion assessment and program refinement in aerial manipulation.

</details>

---
