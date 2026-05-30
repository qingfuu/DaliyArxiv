# cs.CV | Computer Vision and Pattern Recognition | 2026-05-28

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/具身智能/Gamma-World_Generative_Multi-Agent_World_Modeling_Beyond_Two_Players|Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players]]

![[assets/2605.28816_first_page.png|800]]

- **arXiv**: [2605.28816](https://arxiv.org/abs/2605.28816)
- **PDF**: https://arxiv.org/pdf/2605.28816
- **详细分析**: [[20_Research/Papers/具身智能/Gamma-World_Generative_Multi-Agent_World_Modeling_Beyond_Two_Players|Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players]]
- **作者**: Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, Jun Gao, Igor Gilitschenski, Zian Wang, Xuanchi Ren
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.5，世界模型 0.4）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players》归入 大模型、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for interactive video generation have largely focused on single-agent settings, where future observations are generated from a single control signal. However, many generated environments require multi-agent interaction: multiple players, robots, or embodied agents act simultaneously within a shared space. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient inference while maintaining consistency across time and perspectives. In this paper, we present our generative multi-agent world model for interactive simulation. It introduces Simplex Rotary Agent Encoding, a parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space. This gives each agent a distinct phase while making all agents permutation-equivalent, enabling scalable agent identity without learned per-slot identities or a fixed agent ordering. To avoid dense all-to-all attention across agents, we further propose Sparse Hub Attention, where learnable hub tokens mediate token interaction across agents, reducing cross-agent attention cost from quadratic to linear in the number of agents. For real-time rollout, we distill a full-context diffusion teacher into a causal student that generates temporal blocks sequentially with KV caching, enabling action-responsive generation at 24 FPS. Experiments in multiplayer virtual environments show that our model improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines, while generalizing from two to four players without additional training.

</details>

---

### [[20_Research/Papers/具身智能/Ω-QVLA_Robust_Quantization_for_Vision-Language-Action_Models_via_Composite_Rotation_and_Per-step_Scaling|Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling]]

![[assets/2605.28803_figure.png|800]]

- **arXiv**: [2605.28803](https://arxiv.org/abs/2605.28803)
- **PDF**: https://arxiv.org/pdf/2605.28803
- **详细分析**: [[20_Research/Papers/具身智能/Ω-QVLA_Robust_Quantization_for_Vision-Language-Action_Models_via_Composite_Rotation_and_Per-step_Scaling|Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling]]
- **作者**: Xinyu Wang, Mingze Li, Sicheng Lyu, Dongxiu Liu, Kaicheng Yang, Ziyu Zhao, Yufei Cui, Xiao-Wen Chang, Peng Lu
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.5，大模型 0.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Omega-QVLA, QVLA, QuantVLA, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models unify perception, reasoning, and control within a single policy, yet their multi-billion-parameter backbones and diffusion-based action heads make on-device deployment prohibitively expensive. Prior quantization efforts offer only partial solutions, compressing the LLM backbone while leaving the DiT action head at full precision, or resorting to mixed-precision schemes, driven by the belief that uniformly quantizing the action head is inherently unstable. We challenge this assumption with Omega-QVLA, the first training-free post-training quantization framework that compresses both the language backbone and the entire diffusion action head of a VLA model to a uniform W4A4 precision, eliminating the need for mixed-precision allocation. Omega-QVLA combines a composite SVD-Hadamard rotation that equalizes per-channel weight energy while diffusing residual activation outliers with per-step DiT activation scaling quantization that absorbs dynamic-range drift across denoising steps. On LIBERO, Omega-QVLA compresses Pi 0.5 and GR00T N1.5 to W4A4 with 98.0% and 87.8% task success rates, matching or exceeding their FP16 references of 97.1% and 87.0%, while reducing the static memory footprint by 71.3%. Real-world manipulation experiments further confirm smooth, accurate manipulation where prior methods fail. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/GEM_Generative_Supervision_Helps_Embodied_Intelligence|GEM: Generative Supervision Helps Embodied Intelligence]]

![[assets/2605.28548_figure.png|800]]

- **arXiv**: [2605.28548](https://arxiv.org/abs/2605.28548)
- **PDF**: https://arxiv.org/pdf/2605.28548
- **详细分析**: [[20_Research/Papers/具身智能/GEM_Generative_Supervision_Helps_Embodied_Intelligence|GEM: Generative Supervision Helps Embodied Intelligence]]
- **作者**: Ruowen Zhao, Bangguo Li, Zuyan Liu, Yinan Liang, Junliang Ye, Fangfu Liu, Diankun Wu, Zhengyi Wang, Xumin Yu, Yongming Rao, Han Hu, Jun Zhu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.3，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《GEM: Generative Supervision Helps Embodied Intelligence》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GEM-VLA, Real-World, URL, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Vision-Language Models (VLMs) have demonstrated impressive performance and generalization in robotics, particularly within Vision-Language-Action frameworks. However, a significant gap remains between the high-level semantic focus of standard text-guided pre-training paradigms and the low-level spatial and physical knowledge critical for execution in embodied environments. In this paper, we introduce GEM, a Generative-supervised Embodied vision-language Model designed to bridge this divide. We propose integrating a depth map generation task directly into the VLM pre-training phase. By training this generative objective jointly with the main model, we observe substantial improvements in embodied intelligence, significantly enhancing both semantic understanding and physical operation capabilities. To support this paradigm, we curate and release GEM-4M, a comprehensive large-scale dataset featuring a mixture of grounding, reasoning, and planning data paired with high-quality depth supervision. Extensive experiments demonstrate that GEM achieves state-of-the-art results across diverse embodied benchmarks. Furthermore, our deployed action model, GEM-VLA, exhibits vastly superior task execution abilities in both simulation environments and real-world evaluations. Code, models, and datasets are available at this https URL

</details>

---

### [[20_Research/Papers/具身智能/Self-Supervised_Online_Robot-Agnostic_Traversability_Estimation_for_Open-World_Environments|Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments]]

![[assets/2605.28442_first_page.png|800]]

- **arXiv**: [2605.28442](https://arxiv.org/abs/2605.28442)
- **PDF**: https://arxiv.org/pdf/2605.28442
- **详细分析**: [[20_Research/Papers/具身智能/Self-Supervised_Online_Robot-Agnostic_Traversability_Estimation_for_Open-World_Environments|Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments]]
- **作者**: Julia Hindel, Simon Bultmann, Houman Masnavi, Daniele Cattaneo, Abhinav Valada
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-supervised online traversability estimation enables robots to continuously learn from unlabeled open-world experiences and adapt their navigation behavior toward safe and efficient trajectories. Existing approaches either rely on handcrafted proprioceptive traversability scores, limiting robot-agnosticism, or cluster prior data, preventing online learning. Moreover, many continual learning methods incur substantial memory and computational costs, hindering onboard deployment. We introduce COTRATE, an online learning framework for continuous traversability estimation from multimodal, unlabeled robot experience. Our method first infers robust traversability scores using a robot-agnostic, learning-based online terrain assessment module operating on proprioceptiveand inertial signals. These scores then supervise a visual traversability network through a novel alignment loss that associates visual embeddings with online terrain this http URL mitigate forgetting during continual learning with minimal overhead, we propose a diversity-aware feature selection strategythat preserves performance using a compact replay memory. We further show that the learned traversability representation supports knowledge transfer across different robot platforms with different locomotion kinematics. We evaluate COTRATE on a dataset of \approx 50,000 images collected with two robotic platforms across 11 outdoor terrains, and benchmark it on navigation tasks in three representative outdoor environments. We make the dataset, code, and trained models publicly available.

</details>

---

### [[20_Research/Papers/具身智能/POINav_Benchmarking_and_Enhancing_Final-Meters_Arrival_in_Real-World_Vision-Language_Navigation|POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation]]

![[assets/2605.28237_figure.jpg|800]]

- **arXiv**: [2605.28237](https://arxiv.org/abs/2605.28237)
- **PDF**: https://arxiv.org/pdf/2605.28237
- **详细分析**: [[20_Research/Papers/具身智能/POINav_Benchmarking_and_Enhancing_Final-Meters_Arrival_in_Real-World_Vision-Language_Navigation|POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation]]
- **作者**: Ruiyan Gong, Meisheng Zhang, Yuxiang Zhao, Mingchao Sun, Yanfen Shen, Zedong Chu, Zhining Gu, Wei Guo, Xiaolong Cheng, Qiming Li, Kangning Niu, Yanqing Zhu...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：POINav-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world navigation is fundamentally driven by Points of Interest (POIs), yet reaching a precise POI remains a critical "final-meters" challenge. Existing Vision-Language Navigation (VLN) benchmarks of POI-goal navigation often suffer from coarse granularity or significant sim-to-real gaps due to generated scene. To bridge this gap, we present POINav-Bench, the first benchmark designed for closed-loop evaluation of real-world POI-goal navigation. It comprises 11 commercial areas reconstructed from real-world captures using 3D Gaussian Splatting (3DGS), covering 126,398 $m^{2}$ in total and spanning 163 distinct POIs. With traversability-aware annotations and reference trajectories, POINav-Bench enables high-fidelity evaluation of navigation agents in realistic, POI-rich real-world environments. Building on this, we propose the POINav Brain-Action Framework where a Brain module performs POI-grounded reasoning to guide an Action module in predicting continuous waypoints for real-world execution. We further curate the POINav-Dataset, containing 70K real-world signage-entrance pairs. Experiments show that our framework provides a viable path toward refining real-world POI-goal navigation.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Hijack_A_Transferable_Patch_Attack_against_Vision-Language-Action_Models_via_Visual_Proprioception_Hijacking|VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking]]

![[assets/2605.28083_figure.png|800]]

- **arXiv**: [2605.28083](https://arxiv.org/abs/2605.28083)
- **PDF**: https://arxiv.org/pdf/2605.28083
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Hijack_A_Transferable_Patch_Attack_against_Vision-Language-Action_Models_via_Visual_Proprioception_Hijacking|VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking]]
- **作者**: Jiyuan Fu, Kaixun Jiang, Jingkai Jia, Zhaoyu Chen, Xueyao Chen, Lingyi Hong, Shuyong Gao, Chenzhi Tan, Dingkang Yang, Wenqiang Zhang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.4，大模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CronusVLA, OpenVLA, Real-to-Sim, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Vision-Language-Action (VLA) models have emerged as powerful generalist policies, their severe vulnerability to adversarial patches significantly hinders their deployment in safety-critical domains. Moreover, existing patch attacks primarily focus on white-box settings, heavily overfitting to the specific action output space of the target model, which results in poor cross-architecture transferability. To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment. Targeting this shared visual self-localization process, our approach concurrently optimizes Attention-Guided Proprioceptive Suppression to inhibit the real robotic arm's features, and Multimodal Proprioceptive Injection to establish the patch as a surrogate "phantom embodiment". By alternating between semantic concept anchoring and visual prototype projection, VLA-Hijack effectively severs the semantic relationship between the agent's true embodiment and its control policy. Extensive experiments across diverse architectures (OpenVLA, UniVLA, and CronusVLA) demonstrate that VLA-Hijack achieves superior optimization efficiency in white-box settings and sets a new SOTA for cross-architecture and cross-domain black-box transferability.

</details>

---

### [[20_Research/Papers/大模型/Mags-RL_Wearing_Multimodal_LLMs_a_Magnifying_Glass_via_Agentic_Reinforcement_Learning_For_Complex_Scene_Reasoning|Mags-RL: Wearing Multimodal LLMs a Magnifying Glass via Agentic Reinforcement Learning For Complex Scene Reasoning]]

![[assets/2605.27960_figure.png|800]]

- **arXiv**: [2605.27960](https://arxiv.org/abs/2605.27960)
- **PDF**: https://arxiv.org/pdf/2605.27960
- **详细分析**: [[20_Research/Papers/大模型/Mags-RL_Wearing_Multimodal_LLMs_a_Magnifying_Glass_via_Agentic_Reinforcement_Learning_For_Complex_Scene_Reasoning|Mags-RL: Wearing Multimodal LLMs a Magnifying Glass via Agentic Reinforcement Learning For Complex Scene Reasoning]]
- **作者**: Xuanzhao Dong, Wenhui Zhu, Peijie Qiu, Xiwen Chen, Xiaobing Yu, Xin Li, Zhipeng Wang, Shao Tang, Gen Li, Yujian Xiong, Hao Wang, Yanxi Chen...
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Mags-RL: Wearing Multimodal LLMs a Magnifying Glass via Agentic Reinforcement Learning For Complex Scene Reasoning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GQA, Mags-RL, TallyQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite their popularity and success, Multimodal Large Language Models (MLLMs) often struggle to interpret images accurately, which limits their reasoning capability in complex scenarios (e.g., high object density and complex background clutter). Prior work mainly addresses this limitation by incorporating explicit visual cues like bounding boxes that require extra annotations. In addition, the resulting low-resolution crops often miss fine-grained details that MLLMs require for accurate reasoning. Therefore, we propose Mags-RL, an Agentic Reinforcement Learning (RL) framework that equips MLLMs with an external super-resolution "magnifying glass" agent for high-resolution fine-grained inspection. Specifically, the model performs two-round reasoning: in the first round, it generates an initial rationale and autonomously identifies regions of interest without relying on additional annotations; in the second round, it invokes a super-resolution agent to crop and upscale those regions, then revisits and verifies its earlier reasoning to produce the final answer. We also introduce a novel curriculum learning strategy that enables data-efficient RL training, needing as few as only 40 training samples to achieve reasonable performance. Experiments on VSR, TallyQA, and GQA subsets show its superior performance against recent strong competing methods, demonstrating high-quality reasoning with precise visual grounding. Code and weights will be released soon.

</details>

---

### [[20_Research/Papers/具身智能/What-If_World_A_Causal_Benchmark_for_General_World_Models_in_Embodied_Scenarios|What-If World: A Causal Benchmark for General World Models in Embodied Scenarios]]

![[assets/2605.27589_figure.png|800]]

- **arXiv**: [2605.27589](https://arxiv.org/abs/2605.27589)
- **PDF**: https://arxiv.org/pdf/2605.27589
- **详细分析**: [[20_Research/Papers/具身智能/What-If_World_A_Causal_Benchmark_for_General_World_Models_in_Embodied_Scenarios|What-If World: A Causal Benchmark for General World Models in Embodied Scenarios]]
- **作者**: Kunlin Cai, Rui Song, Jinghuai Zhang, Kaiyuan Zhang, Pranav Bodapati, Alicia Yu, Fnu Suya, Mohammad Rostami, Jiaqi Ma, Yuan Tian
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，世界模型 0.6，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《What-If World: A Causal Benchmark for General World Models in Embodied Scenarios》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：NExT-QA, PhyGenBench, VBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation models are increasingly used as world simulators for tasks like driving and robotic manipulation. What matters in these settings is not whether a single video looks right, but whether the model's output changes when its input changes. We test this by giving a model two prompts describing the same scene with one physical detail varied, and checking whether the two videos diverge the way physics predicts. The wording difference between the prompts is small by design, since only one variable is changed, but the correct physical difference is not. A model that misses this can still produce two videos that each look plausible individually, and existing benchmarks score videos one at a time and cannot detect this failure. We introduce What-If World, 319 such prompt pairs built on real frames from nuScenes and DROID, organized by a taxonomy of six physical variables shared across driving and manipulation. Each pair is scored with APEO, a four-part rubric checking whether each video follows its prompt (Adherence), is physically consistent (Physics), preserves the shared scene (Environment), and ends in the correct difference (Outcome). Across nine state-of-the-art models, no system exceeds 52% on the paired score, and open-source models cluster near 28%. Every model tested fails on a large fraction of causal interventions, indicating substantial room before these models can reliably support action-conditioned simulation or model-based planning. Where models do score well, performance appears to track the visual prominence of the intervention rather than the tractability of its underlying physics. Some visually subtle interventions score as low as 14.2%, while visually pronounced ones reach 40.4%.

</details>

---

### [[20_Research/Papers/具身智能/Uni-LaViRA_Language-Vision-Robot_Actions_Translation_for_Unified_Embodied_Navigation|Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation]]

![[assets/2605.27582_figure.png|800]]

- **arXiv**: [2605.27582](https://arxiv.org/abs/2605.27582)
- **PDF**: https://arxiv.org/pdf/2605.27582
- **详细分析**: [[20_Research/Papers/具身智能/Uni-LaViRA_Language-Vision-Robot_Actions_Translation_for_Unified_Embodied_Navigation|Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation]]
- **作者**: Hongyu Ding, Sizhuo Zhang, Ziming Xu, Jinwen Guo, Hongxiu Liu, Xingzhi Cheng, Zixuan Chen, Haifei Qi, Duo Wang, Hao Xu, Jieqi Shi, Yifan Zhang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.6（加权：具身智能 2.7，大模型 0.2，机器人 1.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Uni-LaViRA: Language-Vision-Robot Actions Translation for Unified Embodied Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EQA, MP3D-EQA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied navigation requires an agent to map language and visual observations to a stream of spatial actions that drive a real robot through environments it has never seen. The dominant approach has been to scale vision-language-action (VLA) foundation models on ever-larger collections of robot trajectories. This paper argues that, for navigation specifically, generality can be obtained structurally, not only through data scale. The underlying decision structure of navigation reduces to a single Language-Vision-Robot Actions Translation. The language action emits semantic-level directional command and the vision action emits a pixel-level visual target. Both outputs lie inside the natural output manifold of pretrained multimodal large language models (MLLMs), so the task can be reasoned about by an agent rather than learned from robot data. Therefore, we present Uni-LaViRA, a unified agentic architecture that extends the same insight to four task families (VLN-CE, ObjectNav, EQA, and Aerial-VLN) and to four heterogeneous real robots (Wheeled, Quadruped, Humanoid robot, and a self-built UAV) in a zero-shot manner. Two agent-loop mechanisms make this unification practical. TODO List Memory (TDM) rewrites a structured checklist of pending sub-goals at every step, reciting the unfinished items back into the agent's most recent attention window. Second Chance Backtrack (SCB) rolls the robot back to the pre-error state and conditions the agent's next plan on the failed sub-trajectory, turning single-pass navigation into a self-correcting process. With zero training effort, Uni-LaViRA reaches 60.7% SR on VLN-CE R2R, 51.3% on VLN-CE RxR, 77.7% on HM3D-v2, 60.0% on HM3D-OVON, 54.7% on MP3D-EQA, and 40.0% on OpenUAV, matching or even surpassing recent training navigation foundation models that consume millions of samples and thousands of GPU-hours.

</details>

---
