# cs.CV | Computer Vision and Pattern Recognition | 2026-06-17

#arxiv #ComputerScience

**论文数**: 17

### [[20_Research/Papers/世界模型/Future_Dynamic_3D_Reconstruction_A_3D_World_Model_with_Disentangled_Ego-Motion|Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion]]

![[assets/2606.18250_figure.png|800]]

- **arXiv**: [2606.18250](https://arxiv.org/abs/2606.18250)
- **PDF**: https://arxiv.org/pdf/2606.18250
- **详细分析**: [[20_Research/Papers/世界模型/Future_Dynamic_3D_Reconstruction_A_3D_World_Model_with_Disentangled_Ego-Motion|Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion]]
- **作者**: Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.2，世界模型 1）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Drive-OccWorld, OccWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forecasting the evolution of dynamic environments is crucial for autonomous agents. While generative world models have recently achieved high photorealism in 2D video synthesis by mixing ego-motion and environmental dynamics within the image plane, they exhibit physical inconsistencies, such as morphing or vanishing objects, especially over long time horizons. In this paper, we propose FR3D, a world model that predicts a persistent 3D latent representation for future dynamic 3D reconstruction. Unlike prior works that treat the world as a sequence of image-based features, FR3D explicitly decouples the 3D evolution of the scene from the agent's trajectory, treating the inferred ego-motion as a latent proxy for action. This disentanglement resolves the ambiguities between self-motion and world-motion, ensuring geometric consistency into the future. Furthermore, we introduce a teacher-student distillation strategy that leverages the spatial "common sense" of off-the-shelf foundation models, leading to robust zero-shot generalization. Extensive experiments demonstrate FR3D's strong performance for future dynamic 3D reconstruction from monocular observations across multiple datasets, even 2 seconds into the future. Project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/EgoCS-400K_An_Egocentric_Gameplay_Dataset_for_World_Models|EgoCS-400K: An Egocentric Gameplay Dataset for World Models]]

![[assets/2606.18180_figure.png|800]]

- **arXiv**: [2606.18180](https://arxiv.org/abs/2606.18180)
- **PDF**: https://arxiv.org/pdf/2606.18180
- **详细分析**: [[20_Research/Papers/具身智能/EgoCS-400K_An_Egocentric_Gameplay_Dataset_for_World_Models|EgoCS-400K: An Egocentric Gameplay Dataset for World Models]]
- **作者**: Rongjin Guo, Dong Liang, Yuhao Liu, Fang Liu, Tianyu Huang, Gerhard P. Hancke, Rynson W. H. Lau
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.1，世界模型 0.8，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《EgoCS-400K: An Egocentric Gameplay Dataset for World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ActivityNet, MineRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The shift from video generation to interactive world modeling places new demands on data: beyond captioned videos, world models require temporally aligned video-action-language trajectories grounded in the actions, camera motion, states, and events that drive future scene changes. However, such data is difficult to obtain at scale. Web video datasets offer broad visual coverage but lack executable actions and reliable states; robotic datasets provide action and state supervision but are costly and limited in scene diversity; and existing simulators often lack large-scale human-driven interaction trajectories. In this paper, we introduce EgoCS-400K, a large-scale replay-grounded egocentric Counter-Strike dataset for world models, built from public professional CS and CS2 match demos that preserve human gameplay trajectories and enable parsing, replaying, rendering, and temporal alignment. We extract player states, view directions, movements, keyboard/button inputs, view-angle changes, weapon usage, game events, and round-level context, and render clean first-person videos from the same trajectories. EgoCS-400K contains over 400,000 first-person videos and 10,000 hours of gameplay from more than 1,000 matches and 40,000 rounds, covering 13 maps and 10 player viewpoints per round. It supports a range of interactive visual modeling tasks, including action-conditioned future prediction, state- and event-aware scene rollout, replay-grounded captioning, and agent egocentric action understanding. By connecting visual observations with human actions, camera motion, game states, and events at scale, EgoCS-400K serves as a practical bridge between passive web videos, controllable game simulation, and costly real-world embodied data.

</details>

---

### [[20_Research/Papers/具身智能/Qwen-RobotManip_Technical_Report_Alignment_Unlocks_Scale_for_Robotic_Manipulation_Foundation_Models|Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models]]

![[assets/2606.17846_first_page.png|800]]

- **arXiv**: [2606.17846](https://arxiv.org/abs/2606.17846)
- **PDF**: https://arxiv.org/pdf/2606.17846
- **详细分析**: [[20_Research/Papers/具身智能/Qwen-RobotManip_Technical_Report_Alignment_Unlocks_Scale_for_Robotic_Manipulation_Foundation_Models|Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models]]
- **作者**: Haoqi Yuan, Zhixuan Liang, Anzhe Chen, Ye Wang, Haoyang Li, Pei Lin, Yiyang Huang, Zixing Lei, Tong Zhang, Jiazhao Zhang, Jie Zhang, Jingyang Fan...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models in language and multimodality achieve strong generalization by aligning heterogeneous data under a unified formulation and training at scale. In this report, we investigate whether this scaling recipe can be applied to robotic manipulation to achieve genuine generalization. This is challenging because, unlike text, manipulation data is heterogeneous by nature, expensive to collect, and narrow in diversity, making alignment and scale simultaneously difficult. We present Qwen-RobotManip, a generalizable Vision-Language-Action foundation model built on Qwen-VL. Qwen-RobotManip introduces a unified alignment framework across the representation, motion, and behavioral dimensions of manipulation, making large-scale multi-source training coherent rather than conflicting. This alignment capability in turn enables Qwen-RobotManip to absorb manipulation data at a scale that prior training regimes could not sustain. A human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, and a rigorous curation pipeline harmonizes heterogeneous datasets. Using only open-source datasets and human videos without proprietary data collection, Qwen-RobotManip constructs a ~38,100-hour pretraining corpus and exhibits emergent generalization capabilities, including zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer. We find that standard benchmarks fail to capture pretraining quality and instead adopt OOD settings including RoboCasa365, LIBERO-Plus, EBench, RoboTwin-Clean2Rand, RoboTwin-IF, and RoboTwin-XE. Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $\pi$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real-robot platforms including AgileX ALOHA, Franka, UR, and ARX.

</details>

---

### [[20_Research/Papers/强化学习/MaineCoon_Pursuing_A_Real-Time_Audio-Visual_Social_World_Model|MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model]]

![[assets/2606.17800_first_page.png|800]]

- **arXiv**: [2606.17800](https://arxiv.org/abs/2606.17800)
- **PDF**: https://arxiv.org/pdf/2606.17800
- **详细分析**: [[20_Research/Papers/强化学习/MaineCoon_Pursuing_A_Real-Time_Audio-Visual_Social_World_Model|MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model]]
- **作者**: Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong, Zhengpeng Xie, Haopeng Li, Qinghao Huang, Dandan Shen, Tengjiao Ji, Wei Wang, Peicheng Wu...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies. In this work, we define the position of social world models and build a prototype model as the first step towards this goal. While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric social dynamics. To bridge this gap as the first step to social world models, we present MaineCoon, the first real-time audio-visual autoregressive model that has 22B parameters and is capable of real-time streaming generation and sub-second interaction, with a record-breaking frame rate of up to 47.5 FPS, on a single GPU. To the best of our knowledge, MaineCoon is also the first real-time audio-visual generation model specifically optimized for social-interactive applications. To enable efficient and stable training, we introduce several novel techniques into MaineCoon, including self-resampling, cross-modal representation alignment, domain-aware preference optimization, and reinforced online-policy distillation (ROPD). We also design the first agentic streaming inference framework that supports thousand-second-scale or even longer generation while mitigating drift with agentic cache management and prompt planing. These innovations significantly accelerate training while optimizing real-time inference performance. We believe this work not only sets a new state-of-the-art (SOTA) performance benchmark for high-quality, low-latency, and long-horizon audio-visual autoregressive models, but also points out the paradigm shift desired for next-generation AI-native social platforms.

</details>

---

### [[20_Research/Papers/具身智能/ActWorld_From_Explorable_to_Interactive_World_Model_via_Action-Aware_Memory|ActWorld: From Explorable to Interactive World Model via Action-Aware Memory]]

![[assets/2606.17730_figure.png|800]]

- **arXiv**: [2606.17730](https://arxiv.org/abs/2606.17730)
- **PDF**: https://arxiv.org/pdf/2606.17730
- **详细分析**: [[20_Research/Papers/具身智能/ActWorld_From_Explorable_to_Interactive_World_Model_via_Action-Aware_Memory|ActWorld: From Explorable to Interactive World Model via Action-Aware Memory]]
- **作者**: Zhexiao Xiong, Yizhi Song, Hao Kang, Qing Yan, Liming Jiang, Jenson Yang, Zhoujie Fu, Stathi Fotiadis, Angtian Wang, Zichuan Liu, Bo Liu, Yiding Yang...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《ActWorld: From Explorable to Interactive World Model via Action-Aware Memory》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ActWorld, I-Bench, Infinite-World, LingBot-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable. In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework. We argue that the navigation-interaction gap stems from two bottlenecks. First, a data bottleneck: the lack of human-object interaction data with accurate, dense labels. Second, a memory bottleneck: recency-biased history compression in existing world models discards the event-transition frames that causally determine subsequent object states, leading to an action-forgetting pathology. On the data side, we construct a 100K interaction video dataset, each annotated with per-chunk captions via chain-of-thought reasoning. On the model side, we introduce a hierarchical action-aware memory design that routes history compression by interaction importance, complemented by a persistent memory bank that maintains event-update and object-identity tokens across long rollouts. Experiments show that ActWorld supports both flexible navigation and rich object interaction within a single model, substantially improving interaction fidelity over navigation-only baselines without sacrificing viewpoint control. Project page is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/ERQA-Plus_A_Diagnostic_Benchmark_for_Reasoning_in_Embodied_AI|ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI]]

![[assets/2606.17639_figure.png|800]]

- **arXiv**: [2606.17639](https://arxiv.org/abs/2606.17639)
- **PDF**: https://arxiv.org/pdf/2606.17639
- **详细分析**: [[20_Research/Papers/具身智能/ERQA-Plus_A_Diagnostic_Benchmark_for_Reasoning_in_Embodied_AI|ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI]]
- **作者**: Hong Yang, Basura Fernando
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.7，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EQA, ERQA, URL, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist embodied agents require more than object recognition: they must reason about spatial relations, actions, procedures, human intentions, environmental constraints, and commonsense consequences from situated visual observations. Yet existing visual and embodied question answering benchmarks often provide limited control over the reasoning dependencies being tested, making it difficult to distinguish grounded embodied reasoning from shortcut-driven visual or linguistic pattern matching. We present ERQA-Plus, a diagnostic benchmark for reasoning in embodied AI. ERQA-Plus contains 1,766 question-answer instances grounded in 711 robot-centric images and organized according to a structured taxonomy spanning perceptual, action-centric, social-interaction, navigation-environmental, and contextual commonsense reasoning. The dataset is constructed using a multi-stage generation and validation pipeline that combines taxonomy-guided question generation, automatic quality judging, iterative revision, and human assessment to improve visual grounding, answer validity, and reasoning quality. We benchmark representative general-purpose vision-language models and embodied models, including LLaVA-NeXT-8B, Prismatic-7B, MiniCPM-V-4.5-8B, Qwen3-VL, RoboRefer-8B, and RoboBrain2.5-8B. Although the strongest model, Qwen3-VL-32B, achieves 83.4% overall accuracy and 61.4 SBERT score, category-level results reveal persistent weaknesses in spatial reasoning, procedural reasoning, event prediction, and intention inference. ERQA-Plus therefore provides a fine-grained evaluation framework for measuring not only whether embodied agents answer correctly, but also which forms of embodied reasoning they can and cannot perform reliably. The dataset is available this https URL and the project page at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/MuseVLA_An_Adaptive_Multimodal_Sensing_Vision-Language-Action_Model_for_Robotic_Manipulation|MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation]]

![[assets/2606.17598_figure.png|800]]

- **arXiv**: [2606.17598](https://arxiv.org/abs/2606.17598)
- **PDF**: https://arxiv.org/pdf/2606.17598
- **详细分析**: [[20_Research/Papers/具身智能/MuseVLA_An_Adaptive_Multimodal_Sensing_Vision-Language-Action_Model_for_Robotic_Manipulation|MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation]]
- **作者**: Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 5.2（加权：具身智能 3.3，大模型 0.4，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MuseVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans naturally leverage diverse sensing modalities to interact with the physical world, while most Vision-Language-Action (VLA) models for robotics rely solely on RGB observations. This limits their ability to perceive physical properties that are difficult or impossible to infer from RGB cameras, such as temperature, sound, or radar response. We present MuseVLA, an adaptive multimodal sensing VLA model that integrates novel sensors as on-demand tools for robotic manipulation. Given a task instruction and visual context, MuseVLA first generates a sensor token and target description that select the sensing modality to invoke and what to attend to, analogous to a tool call with arguments. It then converts the selected sensor measurement into a grounded sensor image, a unified intermediate representation that encodes heterogeneous readings for multimodal fusion and action generation. This design decouples sensor-specific processing from the VLA backbone, enabling efficient integration of diverse modalities. To reduce the need for expensive multisensory robot datasets, we further introduce a data synthesis pipeline that augments existing RGB video datasets with grounded sensor images, enabling generalization to unseen sensor-guided tasks. We evaluate MuseVLA on a real-world robot across challenging dexterous hand manipulation tasks that require multimodal sensing inputs, including temperature-guided pick-and-place, audio-driven object search, and radar-assisted hidden object retrieval. MuseVLA achieves 80.6% success rate on average, outperforming RGB-only and multisensory VLA baselines significantly, and exhibits strong zero-shot capabilities on unseen tasks.

</details>

---

### [[20_Research/Papers/具身智能/GASE_Gaussian_Splatting-Based_Automated_System_for_Reconstructing_Embodied-Simulation_Environments|GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments]]

![[assets/2606.17520_figure.png|800]]

- **arXiv**: [2606.17520](https://arxiv.org/abs/2606.17520)
- **PDF**: https://arxiv.org/pdf/2606.17520
- **详细分析**: [[20_Research/Papers/具身智能/GASE_Gaussian_Splatting-Based_Automated_System_for_Reconstructing_Embodied-Simulation_Environments|GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments]]
- **作者**: Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FlexWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training embodied agents in the real world requires skilled operators and expensive hardware. Simulation environments offer a compelling alternative by enabling large-scale, cost-effective data augmentation. Consequently, rapidly constructing high-fidelity simulation scenes with a minimal sim-to-real gap has become a critical objective in robot learning. While reconstruction-based methods provide superior visual quality, current workflows are hindered by inefficient data acquisition and subpar foreground object extraction. We thus propose GASE, a highly automated system for simulation scene construction. GASE leverages multi-view video streams from panoramic camera arrays to enable rapid environment scanning. To ensure high-quality asset generation, our pipeline introduces a camera-pose-based strategy that robustly extracts objects across frames in the 2D domain, followed by high-fidelity scene inpainting. Foreground objects and the static background are then reconstructed independently and seamlessly imported into physics simulators for policy training. Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore, real-robot deployments across manipulation and navigation tasks maintains a performance gap of less than 10\% compared to policies trained purely on real-world data. These results confirm that GASE provides an efficient and highly effective solution for bridging the sim-to-real gap. Code will be released.

</details>

---

### [[20_Research/Papers/具身智能/GeneralVLA-2_Geometry-Aware_Reconstruction_and_Governed_Memory_for_Robot_Planning|GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning]]

![[assets/2606.17480_figure.png|800]]

- **arXiv**: [2606.17480](https://arxiv.org/abs/2606.17480)
- **PDF**: https://arxiv.org/pdf/2606.17480
- **详细分析**: [[20_Research/Papers/具身智能/GeneralVLA-2_Geometry-Aware_Reconstruction_and_Governed_Memory_for_Robot_Planning|GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning]]
- **作者**: Haoyu Wang, Guoqing Ma, Zeyu Zhang, Yandong Guo, Boxin Shi, Hao Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GeneralVLA, OpenVLA, Real-World, SWE-Bench, Terminal-Bench, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: this https URL . Website: this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Theoretical_Grounding_of_Out-Of-Distribution_Detection_With_Reinforcement_Learning_Optimizer|Theoretical Grounding of Out-Of-Distribution Detection With Reinforcement Learning Optimizer]]

![[assets/2606.17477_first_page.png|800]]

- **arXiv**: [2606.17477](https://arxiv.org/abs/2606.17477)
- **PDF**: https://arxiv.org/pdf/2606.17477
- **详细分析**: [[20_Research/Papers/强化学习/Theoretical_Grounding_of_Out-Of-Distribution_Detection_With_Reinforcement_Learning_Optimizer|Theoretical Grounding of Out-Of-Distribution Detection With Reinforcement Learning Optimizer]]
- **作者**: Salimeh Sekeh, Xin Zhang
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Theoretical Grounding of Out-Of-Distribution Detection With Reinforcement Learning Optimizer》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Out-of-distribution (OOD) detection in dynamic open-world environments requires a model to continually adapt to evolving data distributions while generalizing to covariate-shifted inputs and rejecting semantic-shifted OOD examples. Most existing OOD detection methods optimize only the current-step objective and do not explicitly account for how post-deployment environment changes affect future OOD behavior. In this paper, we establish a theoretical grounding for dynamic OOD detection using a reinforcement learning (RL)-guided optimizer that explicitly favors updates that reduce the semantic OOD false positive rate over time. We develop a novel augmented optimizer that uses an RL-guided correction term on top of standard gradient descent (GD) and show its improvement over both future-domain generalization and semantic-OOD rejection. We analyze temporal error decomposition in terms of model-change and environment-change generalization errors and develop a new theoretical framework for comparing the generalization errors under both GD and RL-guided optimizers.

</details>

---

### [[20_Research/Papers/具身智能/WeaveLA_Event_Driven_Cross-Subtask_Latent_Memory_Weaving_for_Repetitive_Robot_Manipulation|WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation]]

![[assets/2606.17463_figure.png|800]]

- **arXiv**: [2606.17463](https://arxiv.org/abs/2606.17463)
- **PDF**: https://arxiv.org/pdf/2606.17463
- **详细分析**: [[20_Research/Papers/具身智能/WeaveLA_Event_Driven_Cross-Subtask_Latent_Memory_Weaving_for_Repetitive_Robot_Manipulation|WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation]]
- **作者**: Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue, Guiliang Liu, Simo Wu, Xiangyang Xue, Taiping Zeng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off into the action expert. We identify the sub-goal completion event as the natural temporal unit for cross-subtask memory hand-off, and present WeaveLA (Weave Latent memory for Vision-Language-Action policies), a cross-subtask memory interface that, on top of a frozen VLA backbone, compresses each completed segment into latent tokens via query-driven attention pooling and routes them directly into the action-generation path of the next sub-task. This event-triggered, action-side design preserves the base policy's short-window interface while adding a lightweight cross-subtask channel. Through stratified evaluation on RoboMME with a $\pi_{0.5}$ backbone, WeaveLA's gains land exactly where the channel is needed: on the hardest repetition slice (SwingXtimes, $N{=}3$), success rises from $0\%$ to $47.8\%$, while single-execution episodes remain unchanged. Per-episode paired analysis confirms the gains are confined to tasks whose causal structure requires cross-subtask information.

</details>

---

### [[20_Research/Papers/具身智能/AnnotateAnything_Automatic_Annotation_of_3D_Assets_for_Robot_Manipulation|AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation]]

![[assets/2606.17446_figure.png|800]]

- **arXiv**: [2606.17446](https://arxiv.org/abs/2606.17446)
- **PDF**: https://arxiv.org/pdf/2606.17446
- **详细分析**: [[20_Research/Papers/具身智能/AnnotateAnything_Automatic_Annotation_of_3D_Assets_for_Robot_Manipulation|AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation]]
- **作者**: Haoran Lu, Mutian Shen, Shuyang Yu, Yu Xiao, Songling Liu, Jianshu Zhang, Shang Wu, Yue Chen, Guo Ye, Jiayi Wang, Zhaoran Wang, Han Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《AnnotateAnything: Automatic Annotation of 3D Assets for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GenieSim, PartNet, Real-World, ShapeNet, URL, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation enables scalable robot data collection, but raw 3D assets provide only geometry, lacking the semantic, interactive, and physical knowledge needed to specify where and how robots should act. In this work, we present AnnotateAnything, a general automatic annotation framework that converts passive 3D assets into manipulation-ready assets with structured, diverse, and executable manipulation labels. AnnotateAnything is built around two complementary pipelines. First, a unified visual-language annotation pipeline using vision-language reasoning to infer object semantics, interaction constraints, and 3D-grounded cues, providing human-prior guidance for identifying meaningful interaction regions. Second, a fully automatic and massively parallel physics annotation pipeline grounds these priors in each asset's geometry and physical constraints through candidate generation, geometry optimization and trajectory generation. This pipeline produces diverse and executable action annotations, including grasp poses, dexterous contacts, articulation waypoints, insertion directions, hanging affordances, and navigation targets. Using the generated annotations, we further build an asynchronous parallel simulation data-collection system across diverse objects, tasks, and robot embodiments. Experiments demonstrate that AnnotateAnything achieves superior annotation efficiency, data-collection efficiency, and task success rates over existing annotation and data-generation pipelines, while also supporting downstream tasks such as affordance detection, robotic VQA, and visual instruction finetuning. We provide project materials on the project page and plan to release the full code, annotations, and benchmark to facilitate future research. Videos, code, demo assets, and annotations are provided in supplementary materials Project page: this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Where_Should_Action_Generation_Begin_A_Learnable_Source_Prior_for_Generative_Robot_Policies|Where Should Action Generation Begin? A Learnable Source Prior for Generative Robot Policies]]

![[assets/2606.17408_figure.png|800]]

- **arXiv**: [2606.17408](https://arxiv.org/abs/2606.17408)
- **PDF**: https://arxiv.org/pdf/2606.17408
- **详细分析**: [[20_Research/Papers/强化学习/Where_Should_Action_Generation_Begin_A_Learnable_Source_Prior_for_Generative_Robot_Policies|Where Should Action Generation Begin? A Learnable Source Prior for Generative Robot Policies]]
- **作者**: Meipo Dai, Qiyuan Zhuang, He-Yang Xu, Ying-Jie Shuai, Yijun Wang, Qi Dou, Xiu-Shen Wei
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Where Should Action Generation Begin? A Learnable Source Prior for Generative Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative robot policies typically begin action generation from an observation-independent standard Gaussian distribution, leaving the choice of source distribution underexplored. This work asks a simple question: where should action generation begin? We propose LeaP, a Learnable source Prior that replaces the standard Gaussian with a proprioception-conditioned diagonal Gaussian over action chunks. Parameterized by a lightweight MLP, LeaP jointly predicts the mean and state-adaptive variance of the source distribution, while keeping the downstream generator architecture and inference solver unchanged. This design provides an observation-informed yet stochastic initialization, allowing the generator to focus on precise action refinement rather than transporting samples from an uninformed noise source. On 15 RoboTwin manipulation tasks, LeaP achieves an average success rate of 81.6%, outperforming four representative baselines -- including deterministic-source methods, a no-prior counterpart, and a diffusion-bridge policy -- by 6.5 to 25.5 percentage points. The same prior consistently improves both flow-matching and diffusion-bridge generators, while using fewer parameters and converging faster. The advantage carries over to real-world deployment, where LeaP attains the best performance. These results suggest that the source distribution is an independent and reusable design axis for generative robot policies, complementary to the choice of generative dynamics.

</details>

---

### [[20_Research/Papers/具身智能/Contactless_Respiratory_Monitoring_on_Heterogeneous_Mobile_Robots_A_Multimodal_Edge-Computing_Framework|Contactless Respiratory Monitoring on Heterogeneous Mobile Robots: A Multimodal Edge-Computing Framework]]

![[assets/2606.17376_figure.png|800]]

- **arXiv**: [2606.17376](https://arxiv.org/abs/2606.17376)
- **PDF**: https://arxiv.org/pdf/2606.17376
- **详细分析**: [[20_Research/Papers/具身智能/Contactless_Respiratory_Monitoring_on_Heterogeneous_Mobile_Robots_A_Multimodal_Edge-Computing_Framework|Contactless Respiratory Monitoring on Heterogeneous Mobile Robots: A Multimodal Edge-Computing Framework]]
- **作者**: Milind Rampure, Shadman Sakib, Haley Patel, Zahid Hasan, Nirmalya Roy
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.9，大模型 0.4，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Contactless Respiratory Monitoring on Heterogeneous Mobile Robots: A Multimodal Edge-Computing Framework》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Respiratory-rate (RR) monitoring is a critical component of remote triage and victim assessment in emergency response, disaster recovery, and infectious-disease scenarios, where minimizing physical contact can reduce responder risk and improve operational safety. However, field deployment of contactless RR monitoring remains challenging due to variable illumination, posture changes, platform heterogeneity, and the impracticality of wearable sensors in hazardous environments. In this paper, we present a modality-adaptive contactless RR monitoring framework for heterogeneous mobile robots with onboard edge computing. The proposed system combines brightness-adaptive sensor selection across RGB, thermal, near-infrared (NIR), and low-light cameras, keypoint-guided chest ROI extraction for posture-robust monitoring, and a signal-quality-index (SQI)-based filtering mechanism for reliable respiratory estimation. We implement and evaluate the framework on three robotic platforms spanning quadruped and wheeled locomotion and multiple edge-computing architectures. Experiments conducted across diverse lighting conditions, subject poses, and robot-to-subject distances demonstrate that the framework generalizes across platforms without per-platform algorithmic retuning, while revealing modality-specific operational boundaries. RGB provides the broadest coverage up to 8m, NIR remains effective up to 6m, thermal is reliable only at short range, and low-light sensing supports monitoring in complete darkness up to 8m. Overall, the results demonstrate the feasibility of multimodal contactless RR monitoring on mobile robots and support its use as a foundation for autonomous triage and victim assessment in hazardous search-and-rescue settings.

</details>

---

### [[20_Research/Papers/强化学习/Training_LLMs_with_Reinforcement_Learning_over_Digital_Twin_Representations_for_Reasoning-Intensive_Surgical_VideoQA|Training LLMs with Reinforcement Learning over Digital Twin Representations for Reasoning-Intensive Surgical VideoQA]]

![[assets/2606.17279_figure.png|800]]

- **arXiv**: [2606.17279](https://arxiv.org/abs/2606.17279)
- **PDF**: https://arxiv.org/pdf/2606.17279
- **详细分析**: [[20_Research/Papers/强化学习/Training_LLMs_with_Reinforcement_Learning_over_Digital_Twin_Representations_for_Reasoning-Intensive_Surgical_VideoQA|Training LLMs with Reinforcement Learning over Digital Twin Representations for Reasoning-Intensive Surgical VideoQA]]
- **作者**: Yiqing Shen, Han Zhang, Mathias Unberath
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision, Systems

#### 研究背景与动机

《Training LLMs with Reinforcement Learning over Digital Twin Representations for Reasoning-Intensive Surgical VideoQA》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EndoVis18-VQA, PitVQA, REAL-Colon-VQA, SSG-VQA, SurgViVQA, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Surgical video question answering requires multi-step reasoning across semantic, spatial, and temporal dimensions. Existing methods architecturally compress videos into discrete token representations and couple visual perception with reasoning. This approach fragments continuous spatial-temporal relationships and has been shown to restrict multi-step reasoning capabilities. We introduce a reinforcement learning (RL) framework that trains large language models (LLMs) to decouple perception from reasoning by operating over digital twin representations constructed from surgical foundation models. Additionally, we introduce hierarchical representations across frame, temporal window, and procedure levels with probabilistic uncertainty estimates. Finally, we propose a novel reward that combines format validation with accuracy assessment through clinical plausibility evaluation and uncertainty-aware calibration for training. To demonstrate the capabilities of this approach, we introduce REAL-Colon-Reason, a colonoscopic benchmark with 2000 question-answer pairs across three complexity levels. We achieve state-of-the-art performance on REAL-Colon-Reason and two existing surgical VideoQA benchmarks REAL-Colon-VQA and EndoVis18-VQA.

</details>

---

### [[20_Research/Papers/具身智能/Contrastive_Action-Image_Pre-training_for_Visuomotor_Control|Contrastive Action-Image Pre-training for Visuomotor Control]]

![[assets/2606.17256_figure.png|800]]

- **arXiv**: [2606.17256](https://arxiv.org/abs/2606.17256)
- **PDF**: https://arxiv.org/pdf/2606.17256
- **详细分析**: [[20_Research/Papers/具身智能/Contrastive_Action-Image_Pre-training_for_Visuomotor_Control|Contrastive Action-Image Pre-training for Visuomotor Control]]
- **作者**: Yuvan Sharma, Dantong Niu, Anirudh Pai, Zekai Wang, Zhuoyang Liu, Baifeng Shi, Stefano Saravalle, Boning Shao, Ruijie Zheng, Jing Wang, Konstantinos Kallidromitis, Yusuke Kato...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Contrastive Action-Image Pre-training for Visuomotor Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing vision encoders for robotics face a fundamental bottleneck: robotic datasets lack the scale necessary for large-scale pre-training. Prior work circumvents this data scarcity by turning to internet-scale image and language data or egocentric human video. While these models show promise, neither paradigm learns from paired vision and action data, which downstream visuomotor control policies require. However, robot trajectories, the most direct source of this paired signal, are not available at pre-training scale, motivating us to extract action signals from abundant human video instead. To this end, we introduce CAIP (Contrastive Action-Image Pre-training), a vision encoder that treats human hand poses from large-scale egocentric video as a proxy for end-effector actions. By extracting 3D hand keypoints, a representation that aligns naturally with downstream robot action spaces, CAIP learns a unified action-image representation through a contrastive objective. Leveraging 32,041 hours of egocentric human video and only 88 hours of robotic manipulation data, CAIP outperforms state-of-the-art vision encoders including DINOv2, SigLIP, MVP, and R3M. Evaluated on a challenging real-world dexterous manipulation setup using Dexmate Vega and Sharpa Wave hands, CAIP yields performance gains of more than 30% on tasks involving folding, pouring, and fine-grained manipulation. Our results show that our method of contrastive action-centric pre-training yields a scalable path to achieving robust visual representations better suited for physical interaction.

</details>

---

### [[20_Research/Papers/强化学习/GeoDisaster_Benchmarking_Orchestrated_Agents_for_Operational_Disaster_Geo-Intelligence|GeoDisaster: Benchmarking Orchestrated Agents for Operational Disaster Geo-Intelligence]]

![[assets/2606.17246_figure.png|800]]

- **arXiv**: [2606.17246](https://arxiv.org/abs/2606.17246)
- **PDF**: https://arxiv.org/pdf/2606.17246
- **详细分析**: [[20_Research/Papers/强化学习/GeoDisaster_Benchmarking_Orchestrated_Agents_for_Operational_Disaster_Geo-Intelligence|GeoDisaster: Benchmarking Orchestrated Agents for Operational Disaster Geo-Intelligence]]
- **作者**: Maram Hasan, Aman Verma, Savitra Roy, Hariseetharam Gunduboina, Daksh Jain, Muhammad Haris Khan, Subhasis Chaudhuri, Biplab Banerjee
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《GeoDisaster: Benchmarking Orchestrated Agents for Operational Disaster Geo-Intelligence》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FloodNet, FloodNet-VQA, GeoLLM-QA, GeoMMBench, HRVQA, RSVLM-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Remote-sensing vision-language models (RS-VLMs) have advanced Earth-observation analysis toward visual interpretation and instruction-following, yet fall short of operational geo-intelligence, which demands tool-grounded spatial reasoning and structured, evidence-backed decisions. We introduce GeoDisaster, an operational geospatial disaster reasoning benchmark with 2,921 verified instances across 43 question types and five task families: deforestation monitoring, multi-hazard analysis, building-damage assessment, flood-safe routing, and Sentinel-1 SAR flood monitoring. Instances integrate heterogeneous EO/GIS evidence-optical and SAR imagery, raster masks, vector geometries, road networks, and exposure layers-spanning hazard detection, damage assessment, exposure estimation, and diagnostic report generation. Ground-truth answers are grounded in executable geospatial workflows and deterministic consistency checks, removing the need for language-model annotation. We further propose an orchestrated multi-agent framework with 18 disaster-oriented tools, where role-specialized agents coordinate through explicit execution contracts, aligned via Role-Contract Expectation Alignment (RCEA): failure-aware supervised fine-tuning combined with contract-grounded reinforcement learning over dense step-level signals. Experiments show that GeoDisaster challenges existing RS-VLMs and agentic systems, while RCEA improves tool use, evidence grounding, state consistency, and decision generation.

</details>

---
