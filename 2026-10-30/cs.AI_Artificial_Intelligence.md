# cs.AI | Artificial Intelligence | 2026-10-30

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/具身智能/Gym-Anything_for_Robotics_Scaling_physical_simulations_with_digital_agents|Gym-Anything for Robotics: Scaling physical simulations with digital agents]]

![[assets/2610.40565_figure.jpg|800]]

- **arXiv**: [2610.40565](https://arxiv.org/abs/2610.40565)
- **PDF**: https://arxiv.org/pdf/2610.40565
- **详细分析**: [[20_Research/Papers/具身智能/Gym-Anything_for_Robotics_Scaling_physical_simulations_with_digital_agents|Gym-Anything for Robotics: Scaling physical simulations with digital agents]]
- **作者**: Pranjal Aggarwal, Sean Welleck
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Gym-Anything for Robotics: Scaling physical simulations with digital agents》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RoboWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything for Robotics, a framework in which coding agents create realistic robotics simulations. Our core insight is that simulation creation is a coding agent task, so improvements in coding agents translate directly into richer and more faithful simulations. We select simulations based on U.S. GDP data to cover economically valuable physical work, define what makes a good simulation and a good task, and develop an adversarial creation-audit loop that checks each simulation and task against these definitions. Using this pipeline, we build RoboWorld, a set of 25 simulations with 25 test and 175 training RL environments of varying difficulty. Even the best frontier models fail on every RoboWorld test task, achieving an average reward of only 0.06. Building on RoboWorld, we introduce several new ways for frontier models to improve, including in-context learning across repeated attempts, a privileged teacher that reads the simulator state and teaches a student in context, self-assisted learning from the model's own privileged experience, and code policies that generate demonstrations across varied scenes to train vision-language-action models (VLAs) such as $π_{0.5}$. Each of these substantially improves performance. We release our pipeline, RL environments, and benchmark to facilitate future research. Code and data are available at https://gym-anything.github.io/robotics

</details>

---

### [[20_Research/Papers/具身智能/BURGER_Benchmarking_and_Understanding_Robotic_Generalization_via_Embodied_Drawing|BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing]]

![[assets/2610.40532_figure.png|800]]

- **arXiv**: [2610.40532](https://arxiv.org/abs/2610.40532)
- **PDF**: https://arxiv.org/pdf/2610.40532
- **详细分析**: [[20_Research/Papers/具身智能/BURGER_Benchmarking_and_Understanding_Robotic_Generalization_via_Embodied_Drawing|BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing]]
- **作者**: Xiangyu Xu, Bangshuai Peng, Ziyi Liu, Mengjie Zhao, Chenhao Lu, Zhengyang Fan, Huazhe Xu, Kaizhe Hu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.8，大模型 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DiffusionVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How effectively can vision-language-action (VLA) models learn diverse language-conditioned behaviors as training data scales? Investigating this question requires large and varied robot datasets, whose collection on physical robots remains costly. We introduce BURGER, a language-conditioned robotic drawing benchmark with a scalable, prompt-driven pipeline for generating continuous drawing trajectories, both in simulation and the real world. In BURGER, an agent starts from the same blank canvas and controls a robot arm to draw the object or spatial composition specified by language, while each instruction allows an open-ended variety of valid drawings and stroke orders. Using 28,200 simulated demonstrations spanning 282 drawing tasks, we evaluate five representative VLA models across data scales, language grounding, and multimodal behavior. BURGER supports fine-grained analysis of language grounding, spatial composition, and action generation, revealing distinct failure patterns across VLA models. Our experiments suggest that some VLA models can benefit from greater task diversity and demonstration scale, capture multimodal drawing behaviors, and generalize to unseen compositions of familiar objects. Finally, we deploy a trained policy on a Franka Panda arm, demonstrating the ability to draw reactively under human intervention. Project homepage and code can be found at https://siyingzhao.github.io/BURGER/.

</details>

---

### [[20_Research/Papers/大模型/EpiAgent_Epistemic_Self-Play_for_LLM_Agents|EpiAgent: Epistemic Self-Play for LLM Agents]]

![[assets/2610.40227_first_page.png|800]]

- **arXiv**: [2610.40227](https://arxiv.org/abs/2610.40227)
- **PDF**: https://arxiv.org/pdf/2610.40227
- **详细分析**: [[20_Research/Papers/大模型/EpiAgent_Epistemic_Self-Play_for_LLM_Agents|EpiAgent: Epistemic Self-Play for LLM Agents]]
- **作者**: Xuanfa Jin, Xinyu Cui, Zhijian Ma, Xue Yan, Jian Zhao, Haifeng Zhang, Jun Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EpiAgent: Epistemic Self-Play for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Epistemic game theory explains an agent's strategic behavior via the beliefs it holds about others and how these beliefs are updated as the interactions unfold. Modern LLM-based agents, however, often lack an explicit mechanism for learning and updating such beliefs to guide decisions under incomplete information. To bridge this gap, we propose EpiAgent, a framework that equips LLM-based agents with an explicit, learnable epistemic layer, which maintains beliefs over others' private information and combines these beliefs with the agent's available information into an epistemic state for action selection. Concretely, the agent's policy is decomposed into two coupled stages: Epistemic Update, which updates these beliefs from interaction histories, and Action Planning, which selects actions conditioned on the updated epistemic state. By formulating their dependency as a bi-level optimization problem, we introduce Epistemic Self-Play, an algorithm that alternately optimizes the two stages through self-play, utilizing an intrinsic prediction reward to evaluate how well inferred beliefs predict subsequent observations. Empirical results across both mixed and competitive scenarios show that EpiAgent consistently outperforms prompting-based and RL-based baselines. Further analyses reveal the benefits of dedicated epistemic training, improvements in belief inference accuracy, and the contribution of learned beliefs to action planning. These results demonstrate the value of an explicit, learnable epistemic layer for effective multi-agent interactions.

</details>

---

### [[20_Research/Papers/强化学习/Escaping_Path_Mirages_in_Offline_Goal-Conditioned_Reinforcement_Learning|Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2610.40130_figure.png|800]]

- **arXiv**: [2610.40130](https://arxiv.org/abs/2610.40130)
- **PDF**: https://arxiv.org/pdf/2610.40130
- **详细分析**: [[20_Research/Papers/强化学习/Escaping_Path_Mirages_in_Offline_Goal-Conditioned_Reinforcement_Learning|Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Junhyeon Bae, Jaebak Hwang, Gwanwoo Choi, Minung Kim, Seungyul Han
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning remains challenging in stochastic long-horizon settings, where compounding value estimation errors hinder reliable goal reaching. While prior methods have sought to address this challenge through various approaches, a key challenge remains path mirage, where agents overcommit to spuriously successful trajectories in offline datasets induced by stochasticity, often leading to failure on difficult tasks. To address this issue, we propose Branch-aware Graph Planning (BGP), which captures stochastic branching structures by identifying high-variability points as graph nodes and designing goal-conditioned edges with segmented learning to avoid unreliable branches and reduce unnecessary stochasticity along paths. As a result, BGP enables reliable goal reaching even in highly stochastic long-horizon environments, and experiments on diverse OGBench tasks show that it substantially outperforms prior state-of-the-art offline goal-conditioned RL methods. Our implementation is available at https://umlic.github.io/papers/BGP/.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Safe_Flow_Matching_Robot_Policies_from_Binary_Feasibility_Oracles|Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles]]

![[assets/2610.40075_figure.png|800]]

- **arXiv**: [2610.40075](https://arxiv.org/abs/2610.40075)
- **PDF**: https://arxiv.org/pdf/2610.40075
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Safe_Flow_Matching_Robot_Policies_from_Binary_Feasibility_Oracles|Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles]]
- **作者**: Jianming Ma, Rongjun Jin, Yizhi Chen, Yue Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot foundation models increasingly rely on flow-based action generation for general-purpose manipulation, yet the generated actions are not guaranteed to satisfy physical constraints such as joint limits and collision avoidance. This problem is especially challenging when the feasible set cannot be described analytically and is accessible only through black-box feasibility oracles. We study this practical oracle-only setting and propose an oracle-guided differentiable safeguard for safe flow-matching robot policies. The safeguard uses binary feasibility queries to correct unsafe updates in the forward pass, while extracting local boundary information to provide constraint-aware learning signals in the backward pass. Combined with discrete-time flow matching, the same safeguard is used during training and inference, enabling forward--backward aligned policy learning without explicit or differentiable constraint models. Experiments on obstacle-aware robotic manipulation demonstrate 100% constraint satisfaction while preserving task performance.

</details>

---

### [[20_Research/Papers/强化学习/Sandman_Building_and_Operating_Sandboxes_for_Agentic_Reinforcement_Learning_on_Shared_Kubernetes|Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes]]

![[assets/2610.39711_first_page.png|800]]

- **arXiv**: [2610.39711](https://arxiv.org/abs/2610.39711)
- **PDF**: https://arxiv.org/pdf/2610.39711
- **详细分析**: [[20_Research/Papers/强化学习/Sandman_Building_and_Operating_Sandboxes_for_Agentic_Reinforcement_Learning_on_Shared_Kubernetes|Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes]]
- **作者**: Yiming Yan, Hongyang Wang, Wenbo Chen, Xuan Wang, Jingguo Liu, Xian Li, Chen Qi, Leo Fan, Siwei Li, Qianli Wu, Yichuan Li, Ruochen Wen...
- **cs 子类**: cs.AI, cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Sandman: Building and Operating Sandboxes for Agentic Reinforcement Learning on Shared Kubernetes》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：SWE-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning (RL) often requires repeated tool calls in task-specific environments. A training job may create thousands of these environments in bursts while sharing a cluster with other jobs. We present Sandman, a sandbox service built and operated at Amazon for agent tool execution and evaluation. It serves multiple production agentic RL workloads on shared Kubernetes. A training framework supplies a task image and uses commands and file operations in the returned sandbox. Files and processes persist across calls until the framework releases the environment. Sandman manages creation, readiness and cleanup. Each sandbox is a Kubernetes pod with a small daemon mounted into the unmodified image. In a scale test, Sandman held 11,858 concurrent tiny sandboxes. Four production SWE-bench Verified training campaigns created 3.1 million sandboxes in October 2026. We report the design trade-offs and operational lessons from handling creation bursts, preparing task environments, reclaiming abandoned sandboxes, and running evaluation under controlled conditions. We will open-source Sandman's daemon, provider and pool.

</details>

---

### [[20_Research/Papers/具身智能/UMI-Live_for_In-The-Wild_Bimanual_Robotics_Data_Collection|UMI-Live for In-The-Wild Bimanual Robotics Data Collection]]

![[assets/2610.39385_figure.jpg|800]]

- **arXiv**: [2610.39385](https://arxiv.org/abs/2610.39385)
- **PDF**: https://arxiv.org/pdf/2610.39385
- **详细分析**: [[20_Research/Papers/具身智能/UMI-Live_for_In-The-Wild_Bimanual_Robotics_Data_Collection|UMI-Live for In-The-Wild Bimanual Robotics Data Collection]]
- **作者**: Govind Velamoor, Adrian Lin, Sam Jung, Spencer Mateega, Brandon Y. Yang, Amish Sethi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《UMI-Live for In-The-Wild Bimanual Robotics Data Collection》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Universal Manipulation Interface (UMI) devices allow human experts to demonstrate tasks for robot learning without teleoperating physical robots. Using these demonstrations as training data still requires a consistent hardware setup, calibration, and data processing. We present UMI-Live, a full-stack open-source bimanual UMI system for in-the-wild data collection. We design our custom UMI-Live hardware to integrate camera and LiDAR--inertial sensing, onboard compute, and power, without external tracking equipment or calibration within the collection environment. We implement a simple user interface for recording data while an asynchronous pipeline performs parallel SLAM reconstruction and publishes training-ready datasets. We also release software that supports dual-YAM teleoperation and VLA policy training and inference. We validate UMI-Live data quality by fine-tuning $π_{0.5}$ and MolmoAct2, achieving success rates of 10/10 and 8/10, respectively on a bimanual pick-and-place task. Furthermore, we release 40 hours of UMI-Live data across three tasks, and complete hardware designs, software, and reproduction guides at our $\href{https://umi-live.github.io/}{\text{project website}}$.

</details>

---

### [[20_Research/Papers/具身智能/WorldFlow_Joint_Video_and_3D_Motion_Prediction_via_Large-Scale_Pretraining|WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining]]

![[assets/2610.39278_figure.png|800]]

- **arXiv**: [2610.39278](https://arxiv.org/abs/2610.39278)
- **PDF**: https://arxiv.org/pdf/2610.39278
- **详细分析**: [[20_Research/Papers/具身智能/WorldFlow_Joint_Video_and_3D_Motion_Prediction_via_Large-Scale_Pretraining|WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining]]
- **作者**: Yuhao Lu, Jiongxu Chen, Hexiang Wei, Jiajin Wu, Juelin Li, Mingjian Liang, Fan Yang, Zhuowei Liang, Zihao Liu, Zhennan Wang, Sheng Wang, Lin Shao
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.5（加权：具身智能 0.6，世界模型 0.4，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointWorld, WorldFlowBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce \method{}, a generative world model that jointly predicts future video and query-based 3D trajectories. By parameterizing 3D motion as continuous displacement tokens aligned with the video grid, a unified Mixture-of-Transformers (MoT) backbone jointly denoises both modalities under a rectified-flow objective. This formulation couples explicit geometric dynamics with visual evolution, effectively unlocking the physical commonsense embedded within pretrained video models. To empirically scale and validate this unified architecture, we train \method{} on a heterogeneous mixture of 1.44 million object-level samples spanning simulated and real-world domains. We further introduce WorldFlowBench, comprising 1,678 evaluation samples from 11 data sources across simulated and real-world interactions, including spatial reasoning tasks. Across all three evaluation sets, WorldFlow achieves the lowest average displacement error (ADE) and final displacement error (FDE) among the evaluated learning-based methods. Notably, on the challenging SpatialCog set, WorldFlow achieves an ADE of 0.060 m, a 54.2\% reduction compared with the strongest external baseline. It also reduces ADE and FDE by 55.9\% and 68.5\%, respectively, compared with its flow-only variant. Project page: https://worldflow-rbs.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Online_Dense_Reinforcement_Learning_with_Planning-Grounding_Agent_for_UI_Navigation_on_Live_IOS_Apps|Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps]]

![[assets/2610.39264_figure.png|800]]

- **arXiv**: [2610.39264](https://arxiv.org/abs/2610.39264)
- **PDF**: https://arxiv.org/pdf/2610.39264
- **详细分析**: [[20_Research/Papers/具身智能/Online_Dense_Reinforcement_Learning_with_Planning-Grounding_Agent_for_UI_Navigation_on_Live_IOS_Apps|Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps]]
- **作者**: Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols, Samy Bengio, Emmanuel Abbe
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.6（加权：大模型 0.6，强化学习 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AndroidWorld, ClawGUI-RL, MobileWorld, OSWorld, UINavBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static trajectories, leading to brittle execution and an inability to recover from errors. To address these limitations, we propose a novel online reinforcement learning framework that trains UI navigation agents directly on live iOS applications. Our framework decouples the agent into two specialized components: a Planning agent and a UI Grounding model. We rely on an LLM-as-a-Judge to provide comprehensive reward signals, combining dense, step-level feedback to evaluate intermediate progress with a terminal reward for overall task completion. To effectively leverage this dual reward structure, we optimize the agent using Proximal Policy Optimization (PPO) with step-level advantage estimation. Furthermore, we introduce GiGPPO, a novel neighbor-conditioned value estimation method that improves critic stability by leveraging reward signals from visually similar states across concurrent trajectories. To support this online training paradigm at scale, we introduce an efficient infrastructure that orchestrates hundreds of concurrent virtual iOS devices. Evaluations on rigorous benchmarks, including UINavBench, iOSWorld, and AndroidWorld, demonstrate that our online RL trained agents substantially outperform both SFT and terminal-only RL baselines while accelerating training convergence. Notably, our 8B RL agents achieve nearly a sevenfold improvement over the SFT baseline in out-of-distribution generalization to Android environments, while outperforming Gemini-3.5-Flash and tying with Gemini-3.1-Pro on real iOS applications.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiExp_Compositional_Experience_Transfer_for_Embodied_Agents|EmbodiExp: Compositional Experience Transfer for Embodied Agents]]

![[assets/2610.39180_first_page.png|800]]

- **arXiv**: [2610.39180](https://arxiv.org/abs/2610.39180)
- **PDF**: https://arxiv.org/pdf/2610.39180
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiExp_Compositional_Experience_Transfer_for_Embodied_Agents|EmbodiExp: Compositional Experience Transfer for Embodied Agents]]
- **作者**: Zhifeng Gu, Ying Chen, Rui Jiang, Lei Yi, Bing Wang
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《EmbodiExp: Compositional Experience Transfer for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experience can help embodied agents turn high-level plans into grounded actions, but transferring it across tasks remains challenging: previously effective strategies may be inapplicable to the current state or fail to produce their intended outcomes. We present EmbodiExp, a framework for constructing transferable experiences and composing them online during embodied task execution. Our key observation is that tasks often share subgoals whose completion can be assessed independently of overall task success. We therefore introduce an outcome-grounded subgoal experience that specifies a subgoal, applicability conditions, an adaptable policy, and a verifiable outcome. During execution, applicable experiences guide action generation, while verified outcomes can establish the conditions required by subsequent experiences, enabling online composition. Subgoal-level outcome attribution further enables failure utilization: failed trajectories can still contribute verified local successes and condition-specific guidance on actions to avoid. Experiments on multiple embodied benchmarks under a fold-based protocol with frozen experience banks demonstrate the effectiveness of EmbodiExp.

</details>

---

### [[20_Research/Papers/强化学习/Generating_Critic-Guided_Synthetic_Experience_in_Latent_World_Models|Generating Critic-Guided Synthetic Experience in Latent World Models]]

![[assets/2610.39100_figure.png|800]]

- **arXiv**: [2610.39100](https://arxiv.org/abs/2610.39100)
- **PDF**: https://arxiv.org/pdf/2610.39100
- **详细分析**: [[20_Research/Papers/强化学习/Generating_Critic-Guided_Synthetic_Experience_in_Latent_World_Models|Generating Critic-Guided Synthetic Experience in Latent World Models]]
- **作者**: Jorge de Freitas, Christos Ziakas, Alessandra Russo
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.16，世界模型 1.36）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Generating Critic-Guided Synthetic Experience in Latent World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from offline datasets is limited in scalability, as collecting new experience is often costly or unsafe in the real world. World models offer an alternative way to generate new experience through a learned dynamics model, yet learning policies in latent space is limited due to compounding errors in imagined rollouts. To this end, we propose using the world model as a local transition generator, leveraging critic guidance to choose actions inside that model to generate synthetic experiences. We study action refinement methodologies, introducing Critic-Guided Synthetic Experience (CGSE) generation in world models. Specifically, CGSE augments an existing offline dataset by sampling candidate actions using an offline policy and refining each to maximize a first-order approximation of the $Q$-function within a trust region. We then use a frozen latent world model to imagine the future state given each updated action, and use the critic to choose the best one, appending this synthetic transition to the replay buffer. Our method requires no additional real-environment interaction or test-time planner, as it generates synthetic experience offline using the world model. On three OGBench manipulation tasks, CGSE improves an offline policy by a relative improvement of $7.1\%$ on the average success rate.

</details>

---

### [[20_Research/Papers/强化学习/Tactus_Tactile_&_Pose_Sensing_Glove_for_Natural_Dexterity_Data_Collection|Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection]]

![[assets/2610.39076_figure.jpg|800]]

- **arXiv**: [2610.39076](https://arxiv.org/abs/2610.39076)
- **PDF**: https://arxiv.org/pdf/2610.39076
- **详细分析**: [[20_Research/Papers/强化学习/Tactus_Tactile_&_Pose_Sensing_Glove_for_Natural_Dexterity_Data_Collection|Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection]]
- **作者**: Li Guan, Rachael Granberry, Sahar Aseeri, Sahar Rostami, Taylor Niehues, Sai Dhanooshi Marri, Mia Huang, Dingtian Zhang, Ziyi Kou, Jason Pursel, Eric Whitmire, Vatsal Mehta...
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 1.82（加权：具身智能 0.6，强化学习 0.16，世界模型 0.56，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting naturalistic human manipulation demonstrations with accurate contact force and hand pose is essential for robot dexterous manipulation policy and foundational world model learning - yet no existing wearable platform provides both calibrated fingertip force sensing and occlusion-resilient hand tracking in a form factor that preserves natural manipulation behavior. We present Tactus, a textile-integrated sensing glove that co-optimizes three design pillars: (1) a thin, conformal 3D-knit form factor (1.5 mm fingertip stackup) designed to minimize interference with natural manipulation, (2) strategically placed capacitive tactile sensors at manipulation-relevant regions informed by empirical contact studies, and (3) IMU-fused pose tracking that maintains accuracy through the hand-object occlusions where manipulation data is most valuable. Tactus includes a documented calibration pipeline for cross-glove consistency and per-session calibration for subject-dependent correction. To enable objective comparison, we introduce standardized benchmarking protocols for tactile force regression and hand pose estimation, and apply them to Tactus and two commercially available tactile gloves - to our knowledge the first quantitative cross-platform evaluation of this kind. Tactus resolves a minimum detectable force of 0.59 N at 95% confidence, 1.6 - 2.7x lower than the commercial baselines, and with 0.87 cross-participant consistency, while our pose tracking sustains 11.0 mm fingertip keypoint relative error during manipulation, when occlusion is heaviest. We show that these combined signals support object property estimation, slip detection, and representative recording of hand-object interaction - yielding demonstration data with the fidelity required for contact-aware manipulation policies and world models.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_the_Game_of_Balatro_A_Fast_Simulator_and_Two-Policy_Training_Approach|Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach]]

![[assets/2610.39049_figure.png|800]]

- **arXiv**: [2610.39049](https://arxiv.org/abs/2610.39049)
- **PDF**: https://arxiv.org/pdf/2610.39049
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_the_Game_of_Balatro_A_Fast_Simulator_and_Two-Policy_Training_Approach|Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach]]
- **作者**: Ajay Vikram Periasami, Anjaneya Gupta, Ethan Cheng, Ivan Rosales
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BalatroBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Balatro, a 2024 roguelike deckbuilder, presents three difficulties that have historically derailed reinforcement learning methods: a 3,000-action state-dependent action space, horizons of several hundred decisions with sparse rewards, and pervasive stochasticity in both card draws and shop generation. Published RL results on the game remain scarce. We introduce an end-to-end pipeline comprising (i) a high-throughput Rust simulator that is automatically state-diffed against the live game client via BalatroBot, (ii) a condensed observation-action interface with dynamic per-step masking of legal moves, and (iii) a multi-agent PPO architecture that decomposes play into a tactical blind policy and a strategic shop policy that share the full game state but act in disjoint phases. Long-horizon credit assignment is partially addressed by per-agent reward routing with explicit cross-agent credit. On the main joint run, training metrics show a sharp phase transition in which the first-blind clear rate converges above 99% and mean episode return increases by roughly an order of magnitude, plateauing at a mean maximum ante of 3 out of 8; single-agent baselines under identical rewards oscillated between greedy and hoarding failure modes and did not stably clear the first blind. These results establish the two-policy decomposition as a strong reactive baseline for Balatro and localise the remaining gap to long-horizon strategic planning rather than tactical blind play.

</details>

---

### [[20_Research/Papers/大模型/Context_Compaction_for_World_Models|Context Compaction for World Models]]

![[assets/2610.38980_figure.png|800]]

- **arXiv**: [2610.38980](https://arxiv.org/abs/2610.38980)
- **PDF**: https://arxiv.org/pdf/2610.38980
- **详细分析**: [[20_Research/Papers/大模型/Context_Compaction_for_World_Models|Context Compaction for World Models]]
- **作者**: Hayder Tirmazi
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.3（加权：大模型 0.3，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《Context Compaction for World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models let observers explore and interact with generated worlds. Recent work shows that when observers revisit a region, current models often fail to regenerate it consistently. We view this as a context retrieval problem. LLM agents manage context retrieval at two layers of their stack. At the model layer, the KV cache design determines how much context fits in memory. At the agent harness layer, harnesses such as Claude Code pick the context sent to the LLM. Prior work on world models has mostly focused only on the model layer. In this paper, we make three contributions. First, we build a benchmark to measure world model context retrieval. It generates new worlds for every episode, preventing a model from recalling rooms using training data. It also separates context retrieval from guesses based on nearby frames. Second, we build an agent harness that performs context compaction for world models, which to our knowledge no prior work has studied. Third, we use our benchmark to study four world model designs. Context compaction lets our world models retrieve rooms up to 4 times beyond their context window without retraining. However, world models with sliding-window attention lose most of their context retrieval when dreaming. Therefore, a dreaming world agent benefits more from extending the reach of its world model using context compaction than switching to sliding window attention at the model layer.

</details>

---

### [[20_Research/Papers/具身智能/AtomTree_A_Hierarchical_Framework_for_State-Aware_Embodied_Instruction_Following_with_LLMs|AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following with LLMs]]

![[assets/2610.38744_figure.png|800]]

- **arXiv**: [2610.38744](https://arxiv.org/abs/2610.38744)
- **PDF**: https://arxiv.org/pdf/2610.38744
- **详细分析**: [[20_Research/Papers/具身智能/AtomTree_A_Hierarchical_Framework_for_State-Aware_Embodied_Instruction_Following_with_LLMs|AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following with LLMs]]
- **作者**: Haotian Zhai, Tianming Sha, Junnan Li
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.25（加权：具身智能 1.5，大模型 0.45，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《AtomTree: A Hierarchical Framework for State-Aware Embodied Instruction Following with LLMs》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied instruction following in interactive environments requires agents to interpret natural language commands and complete long-horizon tasks. Existing planners either rely on large labeled trajectories, or use few-shot and zero-shot LLM prompting that produces a whole plan in a single serial reasoning process. These approaches depend on linguistic common sense, commit to a plan from the initial instruction, and only update after failures, which weakens robustness and state awareness. We present AtomTree, a hierarchical framework for state-aware task planning with LLMs. AtomTree incrementally builds a tree of subgoals and actions, where the LLM decides at each step, from the current symbolic state, whether to further decompose or to output a grounded low-level action. A lightweight memory module summarizes past outcomes for reuse in later decisions. When a low-level action stalls, AtomTree triggers hierarchical backtracking replanning to return to the parent node and regenerate the subtree plan from the latest state, preventing continued drift along an incorrect trajectory. In zero-shot evaluation on the ALFRED benchmark, AtomTree outperforms prior LLM-based planners. Project page: https://zhaihaotian.github.io/atomtree-website/.

</details>

---

### [[20_Research/Papers/具身智能/Explore_Where_It_Matters_Targeted_Exploration_for_Efficient_Rover_Adaptation|Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation]]

![[assets/2610.38657_figure.png|800]]

- **arXiv**: [2610.38657](https://arxiv.org/abs/2610.38657)
- **PDF**: https://arxiv.org/pdf/2610.38657
- **详细分析**: [[20_Research/Papers/具身智能/Explore_Where_It_Matters_Targeted_Exploration_for_Efficient_Rover_Adaptation|Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation]]
- **作者**: Jacob Levy, Arthur Bouton, Tristan D. Hassler, Hari Nayar, David Fridovich-Keil
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 1.72（加权：具身智能 0.9，强化学习 0.16，世界模型 0.36，机器人 0.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Future planetary rovers will traverse steep, deformable terrain where slip, sinkage, and terrain deformation can threaten mobility. Although simulation can capture some wheel-soil effects, unmodeled deformable-terrain phenomena create sim-to-real gaps requiring deployment-time adaptation. Yet, rover operations leave little room for extensive trial-and-error. We introduce TERRA (Targeted Exploration for Reward-Relevant Adaptation), an online adaptation framework that efficiently seeks deployment data exposing task-relevant model errors and corrects them. TERRA adapts a simulation-trained world model with a reward-weighted prediction loss and trains a loss predictor to estimate where future performance-relevant errors are likely to occur, using this signal to guide exploration during MPC. In simulation, TERRA reaches approximately 90% slope-climbing success within five trials under severe out-of-distribution pretraining conditions, outperforming exploration baselines in reward, completion time, and energy to first success. On the ERNEST rover, TERRA recovers coordinated active-suspension locomotion on a deformable Mars-simulant slope within three to five real-world trials. Project website: https://terra-explore.github.io

</details>

---

### [[20_Research/Papers/具身智能/Curriculum-Based_Deep_Reinforcement_Learning_for_Robust_Autonomous_Rocket_Landing_under_Atmospheric_Uncertainty|Curriculum-Based Deep Reinforcement Learning for Robust Autonomous Rocket Landing under Atmospheric Uncertainty]]

![[assets/2610.38636_figure.jpg|800]]

- **arXiv**: [2610.38636](https://arxiv.org/abs/2610.38636)
- **PDF**: https://arxiv.org/pdf/2610.38636
- **详细分析**: [[20_Research/Papers/具身智能/Curriculum-Based_Deep_Reinforcement_Learning_for_Robust_Autonomous_Rocket_Landing_under_Atmospheric_Uncertainty|Curriculum-Based Deep Reinforcement Learning for Robust Autonomous Rocket Landing under Atmospheric Uncertainty]]
- **作者**: Atin Chowdhury, Piyush Joshi
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.4（加权：强化学习 1.4）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Curriculum-Based Deep Reinforcement Learning for Robust Autonomous Rocket Landing under Atmospheric Uncertainty》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RocketSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous far-range rocket landing is a challenging control problem because navigation, descent-rate regulation, attitude management, and fuel use must be coordinated in the presence of uncertain atmospheric and vehicle dynamics. This paper presents a curriculum-driven proximal policy optimization (PPO) framework for three-dimensional rocket landing in a stochastic environment incorporating altitude-dependent aerodynamic drag, wind shear, temporally correlated turbulence, discrete gusts, uncertain propulsion and aerodynamic parameters, thrust-vector misalignment, engine lag, actuator-gain variation, noisy observations, and command latency. Learning is organised into far-range approach, soft descent, and integrated landing stages. Policy transfer, critic warm-up after reward changes, rehearsal of earlier tasks, and progressive expansion of weather severity are used to support learning across these coupled phases. Across 100,000 evaluation episodes, the policy achieves 96,656 successful landings, corresponding to a success rate of 96.656\% and a 95\% Wilson confidence interval of 96.543--96.766\%. Success decreases from 98.84\% under zero-disturbance conditions to 88.07\% in the highest weather-severity band. Successful touchdowns exhibit small miss distances and low residual horizontal and vertical velocities. An exploratory logistic-regression analysis identifies mean wind speed as the strongest measured correlate of success, with initial distance, initial altitude, initial vertical velocity, and wind-shear exponent also associated with outcomes. The results quantify both the effectiveness of the learned policy over the evaluated disturbance distribution and the degradation that occurs under severe compound atmospheric conditions.

</details>

---

### [[20_Research/Papers/具身智能/SaiVLA-JEPA_Evaluating_Future_Latent_Prediction_in_JEPA-Conditioned_VLA_Control|SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control]]

![[assets/2610.38508_first_page.png|800]]

- **arXiv**: [2610.38508](https://arxiv.org/abs/2610.38508)
- **PDF**: https://arxiv.org/pdf/2610.38508
- **详细分析**: [[20_Research/Papers/具身智能/SaiVLA-JEPA_Evaluating_Future_Latent_Prediction_in_JEPA-Conditioned_VLA_Control|SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control]]
- **作者**: Rufeng Xiao, Ruihao Xiao, Wei Chen, Xinhai Sun
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SaiVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) learn to predict representations rather than pixels, offering a compact way to model how visual scenes evolve. We ask whether this predictive objective improves closed-loop control when a vision-language-action (VLA) policy already uses V-JEPA features. We call our JEPA-conditioned flow policy family SaiVLA-JEPA. It combines a vision-language model with a diffusion transformer action expert and receives features from a frozen V-JEPA encoder. Two lightweight auxiliary heads predict future representations during training and are omitted at inference, leaving the action sampler unchanged. We compare policies without JEPA features, with current JEPA conditioning, and with additional future supervision on 10,030 paired LIBERO-Plus episodes. Current JEPA conditioning reaches about 82.5% success versus 71.6% without JEPA, while future supervision provides no detectable aggregate gain at the evaluated training budget. We separately evaluate SaiVLA-JEPA-TCA, which adapts latent context, and SaiVLA-JEPA-TPA, which adapts selected parameters. The context-retry gain is a system-level result under a larger attempt budget; parameter adaptation shows no consistent advantage over the frozen policy and target controls. These results motivate assessing latent-prediction objectives through paired closed-loop rollouts rather than latent loss alone.

</details>

---

### [[20_Research/Papers/强化学习/CuraEval_Evaluating_Demonstration_Curation_on_Mixed-Skill_Robot_Data|CuraEval: Evaluating Demonstration Curation on Mixed-Skill Robot Data]]

![[assets/2610.38221_figure.png|800]]

- **arXiv**: [2610.38221](https://arxiv.org/abs/2610.38221)
- **PDF**: https://arxiv.org/pdf/2610.38221
- **详细分析**: [[20_Research/Papers/强化学习/CuraEval_Evaluating_Demonstration_Curation_on_Mixed-Skill_Robot_Data|CuraEval: Evaluating Demonstration Curation on Mixed-Skill Robot Data]]
- **作者**: Jiuyi Xu, Meida Chen, Yang Ye, Yangming Shi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CuraEval: Evaluating Demonstration Curation on Mixed-Skill Robot Data》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CuraEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot imitation learning uses demonstrations from operators of varying skill, but selecting training data remains challenging. Existing methods score demonstrations using smoothness, diversity, or estimated influence on policy performance, but differences in selection and evaluation protocols make it difficult to determine whether they outperform simple baselines. We introduce \textbf{CuraEval}, a framework combining mathematical analysis of demonstration scores with controlled comparisons against fixed size-matched random subsets and full-data training on mixed-skill robomimic data using Diffusion Policy and BC-RNN. We show that the evaluated PSD score depends only on episode length and squared position magnitudes, and produces nearly the same ranking as episode length on \textit{square} ($ρ=0.999$). With Diffusion Policy, selecting the shortest 50\% of demonstrations improves \textit{square} success from 70.7\% under random selection to 76.5\%. Compared with random selection, our adapted geometric-entropy LOO selector reduces success at 25\% retention from 94.7\% to 74.0\% on \textit{can} and achieves 41.7\% on \textit{square}, below the mean success rates of all three independently sampled random subsets (59.8--62.5\%). On the same 3 \textit{square} Diffusion Policy training seeds, length-based selection at 75\% retention improves success over full-data training from 76.7\% to 86.7\% under the original protocol, but lowers it from 80.5\% to 79.5\% after checkpoint reporting, rollout count, and evaluation seed change jointly. No evaluated curated condition significantly outperforms full-data training after Holm correction, although confidence intervals still permit useful gains. Code is available at https://github.com/jiuyixu25/CuraEval.

</details>

---

### [[20_Research/Papers/机器人/EARS-Info_Information-Aware_Event-Driven_Reallocation_for_Multi-Robot_Exploration|EARS-Info: Information-Aware Event-Driven Reallocation for Multi-Robot Exploration]]

![[assets/2610.38040_figure.png|800]]

- **arXiv**: [2610.38040](https://arxiv.org/abs/2610.38040)
- **PDF**: https://arxiv.org/pdf/2610.38040
- **详细分析**: [[20_Research/Papers/机器人/EARS-Info_Information-Aware_Event-Driven_Reallocation_for_Multi-Robot_Exploration|EARS-Info: Information-Aware Event-Driven Reallocation for Multi-Robot Exploration]]
- **作者**: Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《EARS-Info: Information-Aware Event-Driven Reallocation for Multi-Robot Exploration》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce EARS-Info, an information-aware extension of Event-Driven Ant Reallocation Search for multi-robot exploration on OpenStreetMap-derived grids. It combines marginal sensing gain, feasible relocation, return-aware routing, sensing reservations, and cached shortest paths. Across 168,000 episodes comparing 30 implementations on eight city maps, EARS-Info achieves the highest mean operational score in every evaluation panel. With eight robots and 3% communication dropout, it improves the score over EARS-Safe by 5.43%, increases weighted discovery from 88.88% to 98.46%, and reduces mean energy use by 2.62%. Score differences are positive in all eight cities ($p=0.0078125$; descriptive 95% city-bootstrap interval $[0.0159,0.0694]$), with no simulated incidents across 5,600 EARS-Info episodes. These results support the complete controller; individual component advantages remain uncertain. Generalization is limited by reused geography, one training replicate, coarse maps, and adapted comparison methods.

</details>

---

### [[20_Research/Papers/强化学习/METATRON_A_Promptable_Whole-Body_Execution_Layer_for_Humanoids|METATRON: A Promptable Whole-Body Execution Layer for Humanoids]]

![[assets/2610.38027_figure.png|800]]

- **arXiv**: [2610.38027](https://arxiv.org/abs/2610.38027)
- **PDF**: https://arxiv.org/pdf/2610.38027
- **详细分析**: [[20_Research/Papers/强化学习/METATRON_A_Promptable_Whole-Body_Execution_Layer_for_Humanoids|METATRON: A Promptable Whole-Body Execution Layer for Humanoids]]
- **作者**: Chen Tessler, Yifeng Jiang, Alec Otto, Yi Shi, Umar Iqbal, Gal Chechik, Xue Bin Peng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《METATRON: A Promptable Whole-Body Execution Layer for Humanoids》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid controllers often require task-specific training despite sharing the need for balance and whole-body coordination. We present Metatron, a promptable whole-body execution layer combining a generative base policy with a programmable skill layer. The base policy receives partial goals, collectively called a prompt, that can combine timed body-part targets, velocity commands, and style cues. It produces diverse whole-body motions consistent with these goals. Training combines motion capture, synthetic recovery trajectories, and retargeted scene-interaction motions. After training, the policy is frozen. Stateful programs called skills express task intent as prompts at each control step, drawing rough geometric sketches that the policy turns into coordinated movement. Skills are ordinary code, refined by coding agents that analyze motion data and fit compact rules without task-specific policy training. On the physical Unitree G1, one frozen checkpoint supports walking, recovery, teleoperated object pickup, and sitting on furniture. Comparative evaluations show higher reaching success and push robustness than the tested reference-tracking pipelines. The same recipe produces climbing and acrobatics on a simulated character. Metatron enables coding agents to turn learned motor capabilities into new skills through code, without further policy training.

</details>

---

### [[20_Research/Papers/具身智能/GARDEN_Generalist_Autonomous_Reward_Design_Through_Evidence_Navigation_for_Cooperative_Multi-Agent_Reinforcement_Learning|GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2610.37926_figure.png|800]]

- **arXiv**: [2610.37926](https://arxiv.org/abs/2610.37926)
- **PDF**: https://arxiv.org/pdf/2610.37926
- **详细分析**: [[20_Research/Papers/具身智能/GARDEN_Generalist_Autonomous_Reward_Design_Through_Evidence_Navigation_for_Cooperative_Multi-Agent_Reinforcement_Learning|GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Dogan Urgun
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent reinforcement learning (MARL) enables teams of agents, such as robots and autonomous vehicles, to learn coordinated behavior, but what such teams learn is largely determined by their reward function. Because task success alone provides too little guidance for learning, intermediate rewards are usually designed by hand, and this effort must often be repeated whenever the environment or the team changes. Large language models (LLMs) can automate the effort by writing reward functions as code, yet the resulting rewards are typically designed and tested in a single setting. To enable their reuse across settings, GARDEN (Generalist Autonomous Reward Design through Evidence Navigation) is proposed, in which one reward program is developed for a family of related scenarios and transferred, unchanged, to scenarios that were not available during its design. During development, environment code, training records, and agent behavior are investigated by an LLM reward engineer, and draft rewards are tested in trial training runs, while the learning algorithm and the rule for selecting the final reward are held fixed. On unseen scenarios of the Overcooked and SMAX benchmarks, task returns were increased by 58.2% and 52.5% over the default rewards on two kitchen layouts, and the mean win rate in two combat scenarios was raised from 51.0% to 89.9%. Under matched candidate and probe budgets, this exceeded the 84.2% and 79.2% obtained with fixed diagnostic feedback and Eureka-inspired reward reflection. These results show that a single autonomously engineered reward can be reused effectively across related cooperative scenarios.

</details>

---

### [[20_Research/Papers/具身智能/What_Actually_Matters_A_Paired_Evaluation_of_Inference_Settings_for_$π_{0.5}$_on_BEHAVIOR-1K|What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K]]

![[assets/2610.37917_first_page.png|800]]

- **arXiv**: [2610.37917](https://arxiv.org/abs/2610.37917)
- **PDF**: https://arxiv.org/pdf/2610.37917
- **详细分析**: [[20_Research/Papers/具身智能/What_Actually_Matters_A_Paired_Evaluation_of_Inference_Settings_for_$π_{0.5}$_on_BEHAVIOR-1K|What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K]]
- **作者**: Ruben Hammele, Samira Huber, Mohammad Nazeri, Amirreza Payandeh, Alexandyr T. Card, Aaron Nguyen, Anuj Pokhrel, Daeun Song, Xuesu Xiao, Sören Pirk
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《What Actually Matters? A Paired Evaluation of Inference Settings for $π_{0.5}$ on BEHAVIOR-1K》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for general-purpose household robotics. However, inference and data-collection strategies that have been deployed in smaller-scale settings do not necessarily generalize to large-scale, diverse task suites. To address this gap, we conduct a systematic, paired evaluation of previously proposed inference and data-collection strategies across all 100 tasks. Our evaluation uses a fine-tuned $π_{0.5}$ model based on the 2025 BEHAVIOR Challenge winner, which achieves a Q-score of 0.39 on the public test set. These results show that proposed strategies do not transfer uniformly to new environments and tasks. Project page, videos, and detailed analysis: https://rubenhammele.github.io/behavior2026

</details>

---

### [[20_Research/Papers/具身智能/Echo_Scaling_Visual_Reinforcement_Learning_with_Off-policy_Experience|Echo: Scaling Visual Reinforcement Learning with Off-policy Experience]]

![[assets/2610.37865_figure.png|800]]

- **arXiv**: [2610.37865](https://arxiv.org/abs/2610.37865)
- **PDF**: https://arxiv.org/pdf/2610.37865
- **详细分析**: [[20_Research/Papers/具身智能/Echo_Scaling_Visual_Reinforcement_Learning_with_Off-policy_Experience|Echo: Scaling Visual Reinforcement Learning with Off-policy Experience]]
- **作者**: Gagan Khandate
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.0（加权：具身智能 0.9，强化学习 0.8，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Echo: Scaling Visual Reinforcement Learning with Off-policy Experience》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling visual reinforcement learning (RL) with GPU-accelerated simulation is computationally expensive due to rendering and visual-policy inference costs. Consequently, two-stage teacher--student distillation is commonly used to train visual policies, but introduces an imitation gap. In this preliminary study, we introduce \echomethod{}, \textbf{a single-stage off-policy RL framework that scales experience collection without proportionally increasing visual computation}. Through \textbf{inverse distillation}, a state-based auxiliary policy imitates the evolving visual policy and collects inexpensive, unrendered experience. Echo leverages this experience for off-policy value learning, directly improving the visual policy through a shared privileged critic. We instantiate \echomethod{} with FastTD3 and evaluate it on three visual control tasks and two dexterous manipulation tasks in Genesis. Relative to \sdpgmethod{} under the evaluated configurations, Echo reduces time to reference returns by an average of \textbf{60\% across the three locomotion tasks} and \textbf{56\% across both hand tasks}, while improving peak mean returns by \textbf{62\% and 12\%}, respectively. Both hand tasks also achieve higher mean returns at matched simulator-transition budgets. These initial results suggest that scaling off-policy experience is a promising approach to efficient direct visual RL.

</details>

---

### [[20_Research/Papers/具身智能/LaWAM_Latent_World_Action_Models_for_Efficient_Dynamics-Aware_Robot_Policies|LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies]]

![[assets/2606.15768_figure.png|800]]

- **arXiv**: [2606.15768](https://arxiv.org/abs/2606.15768)
- **PDF**: https://arxiv.org/pdf/2606.15768
- **详细分析**: [[20_Research/Papers/具身智能/LaWAM_Latent_World_Action_Models_for_Efficient_Dynamics-Aware_Robot_Policies|LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies]]
- **作者**: Jialei Chen, Kai Wang, Kang Chen, Shuaihang Chen, Feng Gao, Wenhao Tang, Zhiyuan Li, Weilin Liu, Zhuyu Yao, Boxun Li, Yuanbo Xu, Chao Yu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，世界模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Giga-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs) leverage large-scale vision-language pretraining for semantic robot control, but often lack explicit foresight into how robot actions change the scene. World-Action Models (WAMs) address this limitation by conditioning policies on predicted futures, yet existing approaches typically rely on computationally expensive video generation with substantial pixel-level redundancy. We present LaWAM, a Latent World Action Model that exposes predictive dynamics to robot policies through compact latent visual subgoals instead of reconstructed future video. At the core of LaWAM is a latent-action-conditioned Latent World Model (LaWM). We obtain LaWM by training a latent action model in the latent space of a pretrained vision foundation model and repurposing its forward decoder to predict future observation features for scene evolution. LaWAM then conditions action generation on these predicted latent visual subgoals to enable dynamics-aware robot control. LaWAM achieves state-of-the-art or competitive success rates (SRs) across LIBERO (98.6% SR), RoboTwin (91.22% SR), and real-world manipulation tasks while retaining low-latency inference. LaWAM runs in 187 ms per action-chunk prediction and achieves up to 24x lower wall-clock latency than pixel-space WAMs.

</details>

---
