# cs.CV | Computer Vision and Pattern Recognition | 2026-06-04

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Food-R1_A_Unified_Multi-Task_Food_Vision-Language_Model_with_Reinforcement_Learning|Food-R1: A Unified Multi-Task Food Vision-Language Model with Reinforcement Learning]]

![[assets/2606.04986_figure.png|800]]

- **arXiv**: [2606.04986](https://arxiv.org/abs/2606.04986)
- **PDF**: https://arxiv.org/pdf/2606.04986
- **详细分析**: [[20_Research/Papers/大模型/Food-R1_A_Unified_Multi-Task_Food_Vision-Language_Model_with_Reinforcement_Learning|Food-R1: A Unified Multi-Task Food Vision-Language Model with Reinforcement Learning]]
- **作者**: Yu Zhu, Yongkang Li, Wenjie Zhu, Haoyi Jiang, Wenyu Liu, Wei Yang, Bin Li, Xinggang Wang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 0.8，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Food-R1: A Unified Multi-Task Food Vision-Language Model with Reinforcement Learning》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CalorieBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies have explored Vision-Language Models (VLMs) for food analysis. However, most existing methods rely primarily on supervised fine-tuning (SFT), which often limits reasoning and generalization capabilities. Moreover, high-quality large-scale nutritional annotations remain scarce. To address these issues, we introduce CalorieBench-80K, a large-scale benchmark with curated calorie labels and dietary advice annotations. To the best of our knowledge, it is the first food image benchmark to incorporate Chain-of-Thought (CoT) annotations for calorie reasoning. We also propose Food-R1, a unified food VLM trained in a multi-task learning paradigm to equip the model with broad capabilities. Food-R1 undergoes CoT-based cold-start instruction tuning, followed by reinforcement fine-tuning (RFT) using Group Relative Policy Optimization (GRPO) to improve reasoning and performance. Experiments on CalorieBench-80K and representative benchmarks show that Food-R1 consistently outperforms strong baselines across food-related tasks. The code, model weights, and benchmark annotations are available at the project repository.

</details>

---

### [[20_Research/Papers/具身智能/Dream.exe_Can_Video_Generation_Models_Dream_Executable_Robot_Manipulation|Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?]]

![[assets/2606.04811_figure.png|800]]

- **arXiv**: [2606.04811](https://arxiv.org/abs/2606.04811)
- **PDF**: https://arxiv.org/pdf/2606.04811
- **详细分析**: [[20_Research/Papers/具身智能/Dream.exe_Can_Video_Generation_Models_Dream_Executable_Robot_Manipulation|Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?]]
- **作者**: Rui Zhao, Kaiming Yang, Jifeng Zhu, Siyang Chen, Ziqi Wang, Weijia Wu, Kevin Qinghong Lin, Heng Wang, Mike Zheng Shou
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.2，机器人 1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PhyGenBench, T2V-CompBench, URL, VBench, VideoVLA, WorldSimBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation models have made impressive strides in synthesizing visually compelling content, yet their outputs remain confined to the virtual domain. A natural question follows: how well do these models reflect the physical world when their generated videos leave the screen and enter reality? We propose robotic manipulation as a concrete, measurable window onto this question: if a model has truly internalized physical laws, the motion it depicts should translate into executable robot behavior. We introduce this http URL , an evaluation framework that operationalizes this criterion through a video-to-execution pipeline. Given a scene image and a task description, this http URL synthesizes a manipulation video, converts the generated motion into robot trajectories, and executes them in a physics simulator, yielding a grounding signal that purely visual metrics cannot offer. Using this pipeline, we evaluate 8 models spanning frontier closed-source generators, open-source generators, and robot-specific models. Our benchmark covers 101 manually curated manipulation tasks at three levels of physical complexity, measured across visual quality, trajectory fidelity, and execution success. Encouragingly, several models achieve measurable execution success, suggesting that generative priors learned from internet-scale data already encode meaningful physical knowledge. Yet visual quality proves a poor predictor of executability, exposing a dimension of model capability that standard visual evaluations do not capture. this http URL will be open-sourced at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/3DThinkVLA_Endowing_Vision-Language-Action_Models_with_Latent_3D_Priors_via_3D-Thinking-Guided_Co-training|3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training]]

![[assets/2606.04436_figure.png|800]]

- **arXiv**: [2606.04436](https://arxiv.org/abs/2606.04436)
- **PDF**: https://arxiv.org/pdf/2606.04436
- **详细分析**: [[20_Research/Papers/具身智能/3DThinkVLA_Endowing_Vision-Language-Action_Models_with_Latent_3D_Priors_via_3D-Thinking-Guided_Co-training|3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training]]
- **作者**: Jiaxin Shi, Xidong Zhang, Fucai Zhu, Zhe Li, Siyu Zhu, Weihao Yuan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EvoDriveVLA, VITA-VLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction. Our core insight is that 3D geometry perception and 3D spatial reasoning are distinct capabilities that can be disentangled and injected at different feature hierarchies. During training, three tightly coupled components work in concert primarily within the latent space: (1) To gain geometric priors, a latent 3D geometry perception module aligns intermediate visual features with a 3D foundation model, acquiring low-level geometric cues without architectural modifications to the VLM backbone. (2) Complementing this, an online 3D reasoning distillation module mitigates the prompt-induced reasoning gap via a shared reasoning anchor token. During 3D VLM co-training, this anchor is emitted as the first output token to robustly encode spatial priors. During VLA training, it serves as an input token inserted between the task and action instructions, transferring high-level spatial thinking from explicit teacher reasoning prompts to student action prompts without chain-of-thought text generation. (3) These disentangled geometric and reasoning features are then united by a spatially augmented action integration, which jointly injects them into the action-query tokens as hierarchical spatial conditions to prevent action shortcuts. At deployment, our method retains only its lightweight adapters to perform implicit 3D reasoning, discarding the 3D foundation model and the teacher branch used for supervision. Consequently, it operates purely on 2D images without 3D sensors, external models, or explicit text generation while preventing catastrophic forgetting of the pretrained VLM, achieving state-of-the-art performance on LIBERO, LIBERO-PLUS, SimplerEnv, and real-world manipulation tasks.

</details>

---
