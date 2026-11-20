# cs.AI | Artificial Intelligence | 2026-11-18

#arxiv #ComputerScience

**论文数**: 27

### [[20_Research/Papers/大模型/WoRD_Diffusion-Based_Posterior_Inference_for_Online_Goal_Recognition|WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition]]

![[assets/2611.23192_figure.png|800]]

- **arXiv**: [2611.23192](https://arxiv.org/abs/2611.23192)
- **PDF**: https://arxiv.org/pdf/2611.23192
- **详细分析**: [[20_Research/Papers/大模型/WoRD_Diffusion-Based_Posterior_Inference_for_Online_Goal_Recognition|WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition]]
- **作者**: Almog Anschel, Sarah Keren
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 大模型, 具身智能, 强化学习
- **相关性评分**: 1.62（加权：具身智能 0.3，大模型 0.3，强化学习 0.16，世界模型 0.36，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition》归入 机器人、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HPNet, QCNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous trajectories rely on an explicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous trajectory prefixes where such knowledge is most needed. We present WoRD (Waypoint Recognition with Diffusion), which uses a learned trajectory prior to infer the agent's goal from partial observations. At each step, WoRD runs one warm-started denoising chain per candidate goal, steers each chain toward the observed trajectory through a closed-form log-likelihood gradient, and reweights the resulting samples by Bayes' rule into a calibrated posterior over goals. We evaluate WoRD on simulated robot settings, pedestrian trajectories, and vehicle trajectories using four metrics targeting distinct failure modes. Across all three settings, the same inference procedure preserves calibrated multimodal beliefs through ambiguous prefixes where filter- and classifier-based observers collapse to a single mode or grow overconfident.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Undo_Transfer_Reinforcement_Learning_under_State_Space_Transformations|Learning to Undo: Transfer Reinforcement Learning under State Space Transformations]]

![[assets/2611.23081_figure.png|800]]

- **arXiv**: [2611.23081](https://arxiv.org/abs/2611.23081)
- **PDF**: https://arxiv.org/pdf/2611.23081
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Undo_Transfer_Reinforcement_Learning_under_State_Space_Transformations|Learning to Undo: Transfer Reinforcement Learning under State Space Transformations]]
- **作者**: Mridul Mahajan, Aldo Pacchiano, Xuezhou Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Learning to Undo: Transfer Reinforcement Learning under State Space Transformations》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transfer learning in reinforcement learning (RL) has shown strong empirical success. In this work, we take a more principled perspective by studying when and how transferring knowledge between MDPs (a source and a target) can be provably beneficial. Specifically, we consider the case where there exists an undo map such that applying this map to the target's state space recovers the source exactly. We propose an algorithm that learns this map by matching state feature statistics gathered from both MDPs, and then uses it to transfer the source policy to the target. We theoretically justify the algorithm by analyzing the setting when the undo map is linear and the source is linearly-$Q^\star$ realizable, where our approach has strictly better sample complexity than tabula rasa RL in the target MDP. Empirically, we demonstrate that these benefits extend beyond this regime: on challenging continuous control tasks and Atari games, our method achieves significantly better sample efficiency. Overall, our results highlight how shared structure between tasks can be leveraged for efficient transfer of policies across environments.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Heat_Pump_and_Underfloor_Heating_Control_An_End-to-End_Case_Study|Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study]]

![[assets/2611.23063_figure.png|800]]

- **arXiv**: [2611.23063](https://arxiv.org/abs/2611.23063)
- **PDF**: https://arxiv.org/pdf/2611.23063
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Heat_Pump_and_Underfloor_Heating_Control_An_End-to-End_Case_Study|Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study]]
- **作者**: Antonio Manjavacas, David Suárez-Caro, Alejandro Campoy-Nieves, Guillermo Rey, Gonzalo Satrústegui, Miguel Molina-Solana
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.8（加权：大模型 0.2，强化学习 1.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient control of underfloor heating (UFH) systems coupled with heat pumps (HPs) is challenging due to the high thermal inertia of buildings and the slow dynamic response of UFH systems. Deep Reinforcement Learning (DRL) offers a data-driven control approach capable of simultaneously optimizing energy consumption and thermal comfort. However, the application of DRL-based controllers in occupied buildings under real operating conditions remains limited. This work presents and end-to-end case study (development, evaluation, and real-world deployment) of a DRL-based controller for an integrated UFH-HP system. First, a simulation-based pilot study was conducted to assess different DRL algorithms, control strategies, and configurations. Subsequently, a digital twin of a real residential building was developed and used to train DRL agents under simulated operating conditions. The best-performing agent was then deployed in the physical building without additional online fine-tuning. The results show that the controller successfully maintained indoor temperatures within the prescribed comfort limits while dynamically adjusting the HP supply temperature and UFH valve positions. These findings demonstrate the feasibility of deploying DRL controllers in occupied buildings and highlight their robustness and the practical challenges associated with transferring control policies from digital environments to real heating systems.

</details>

---

### [[20_Research/Papers/强化学习/Residual-Guided_Lightweight_Reinforcement_Learning_for_Risk-Aware_Trajectory_Selection_with_a_Frozen_World_Model|Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model]]

![[assets/2611.22998_figure.png|800]]

- **arXiv**: [2611.22998](https://arxiv.org/abs/2611.22998)
- **PDF**: https://arxiv.org/pdf/2611.22998
- **详细分析**: [[20_Research/Papers/强化学习/Residual-Guided_Lightweight_Reinforcement_Learning_for_Risk-Aware_Trajectory_Selection_with_a_Frozen_World_Model|Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model]]
- **作者**: Jiaqi Wu, Yongqi Dong, Yijie Zhong, Maple Shao, Yide Tao, Linsen Cai, Weize Cai, Hai L. Vu, Alvaro Garcia Hernandez
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.32（加权：强化学习 1.16，世界模型 1.16）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ResWorld, RiskWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs. We propose a residual-guided reinforcement learning (RL) framework for lightweight trajectory selection with a frozen world model and a fixed candidate bank. The framework uses proximal policy optimization (PPO) to fine-tune a joint policy over candidate selection and bounded trajectory residuals. A context-conditioned ranking network learns candidate preferences from feedback obtained by evaluating local perturbations of the selected trajectories. At inference, the selector combines learned preference and predicted risk ranks using fixed weights and returns the selected candidate trajectory without modification. Fine-tuning updates 16,106 parameters across the actor and critic, while the deployed selector retains only the 11,725-parameter ranking network, with the residual branch and critic used exclusively during training. In open-loop evaluation on the nuScenes validation set, the method reduces average Euclidean trajectory error (L2) by 3.99% relative to the RiskWorld model baseline without RL-based selection. Under matched budgets for feedback accesses and actor updates, residual exploration reduces L2 by 0.83% relative to the categorical PPO variant trained without residuals. The method also maintains lower L2 than RiskWorld when risk features are removed or shuffled.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Agent-Centric_Vision-Language-Action_World_Models_for_Autonomous_Driving|Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving]]

![[assets/2611.22880_figure.png|800]]

- **arXiv**: [2611.22880](https://arxiv.org/abs/2611.22880)
- **PDF**: https://arxiv.org/pdf/2611.22880
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Agent-Centric_Vision-Language-Action_World_Models_for_Autonomous_Driving|Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving]]
- **作者**: Guoqing Wang, Pin Tang, Xiangxuan Ren, Chao Ma
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型, 强化学习
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.4，强化学习 0.2，世界模型 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving》归入 具身智能、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portion of the tokens directly encode critical planning-relevant factors, such as agent geometry, motion dynamics, and interactions. This introduces a significant performance bottleneck. An important question thus arises: what world state should a world VLA model reason over to support planning beyond pixel-level prediction? We argue that planning-oriented world modeling should focus on a compact and structured agent-centric latent state that captures the interactions between objects in the driving scene over time. As such, we introduce AgentWorld, an agent-centric VLA world model that uses discrete agent tokens jointly for reasoning and trajectory planning. Each token is dynamically grounded to a surrounding agent associated with its object's state, such as semantic identity, 3D geometry, motion, and interaction context. AgentWorld learns these tokens through three key processes: explicit geometric grounding, reasoning-oriented supervised fine-tuning, and agent-oriented reinforcement learning. Extensive open-loop and closed-loop experiments under diverse driving scenarios show that AgentWorld enhances planning capabilities, fully exploits visual evidence and agent dynamics, and yields interpretable agent-centric world states.

</details>

---

### [[20_Research/Papers/具身智能/Outcome-Balanced_PPO_and_Policy-Induced_Flow_Rectification_for_Flow-Based_VLA_Policies|Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies]]

![[assets/2611.22878_figure.png|800]]

- **arXiv**: [2611.22878](https://arxiv.org/abs/2611.22878)
- **PDF**: https://arxiv.org/pdf/2611.22878
- **详细分析**: [[20_Research/Papers/具身智能/Outcome-Balanced_PPO_and_Policy-Induced_Flow_Rectification_for_Flow-Based_VLA_Policies|Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies]]
- **作者**: Yuhan Wang, Ruiyang Wang, Jiaguan Zhu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.22（加权：具身智能 1.5，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction. However, this optimization raises two challenges: policy updates can alter the velocity-field geometry underlying the score approximation used for stochastic transitions, and sparse multi-task rollouts can yield uneven learning signals across tasks and advantage signs. We introduce an RL framework that combines Outcome-Balanced Proximal Policy Optimization (PPO) with policy-induced flow rectification. Outcome-Balanced PPO reweights positive advantages using task success-rate estimates and rescales positive and negative advantages while preserving their signs. Policy-induced rectification periodically fits a linear-bridge flow to ODE endpoint pairs generated by the current policy, refreshing the representation used in subsequent stochastic optimization. We evaluate the framework on simulated manipulation benchmarks and additionally study a component combination in a Real2Sim2Real task, examining task performance, optimization behavior, and flow consistency. The proposed framework improves success rates over the evaluated baselines across the simulated benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/Network-Exposed_Configuration_Attacks_on_LLM-Controlled_Social_Robots|Network-Exposed Configuration Attacks on LLM-Controlled Social Robots]]

![[assets/2611.22761_figure.jpeg|800]]

- **arXiv**: [2611.22761](https://arxiv.org/abs/2611.22761)
- **PDF**: https://arxiv.org/pdf/2611.22761
- **详细分析**: [[20_Research/Papers/具身智能/Network-Exposed_Configuration_Attacks_on_LLM-Controlled_Social_Robots|Network-Exposed Configuration Attacks on LLM-Controlled Social Robots]]
- **作者**: Stanley Akingbola, Ugbede Ibrahim, Yan Lin Aung, Quang Dan Le, Hong Qing Yu
- **cs 子类**: cs.AI, cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.9，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Network-Exposed Configuration Attacks on LLM-Controlled Social Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) in embodied robots create security dependencies beyond inference. We investigate a network-exposed configuration attack on the Pollen Robotics Reachy Mini Lite, allowing an unauthenticated attacker to replace personality settings and the cloud LLM's system prompt through a management interface, without adversarial conversational input. Eleven prompt-injection attempts across five categories were reported as resisted, whereas both configuration-layer attack paths produced observable behavioural changes on physical hardware. We demonstrate local and network-adjacent access, mapping the weakness to CWE-306 (Missing Authentication for a Critical Function) and CWE-1327 (Binding to an Unrestricted IP Address), with a reported CVSS v3.1 score of 6.5 (Medium). A configuration endpoint also accepts cross-origin requests without a CORS preflight (CWE-352; 6.5 Medium), while the persistent-memory sink stores content without enforcing its stated restrictions. A source review of 59 public repositories identifies missing authentication in 10 of 11 source-verifiable genuine applications, or 11 of 11 including a framework-default case. These findings indicate recurrence within the sampled repositories, not prevalence in commercial products. We characterise a deployment gap between developer-oriented network assumptions and consumer-facing embodied AI security: inference-layer refusal cannot prevent unauthorised changes to model instructions. Potential consequences include surveillance through onboard cameras and microphones and social engineering of nearby users. Proof-of-concept code, evidence and the survey are available at https://bit.ly/reachypi.

</details>

---

### [[20_Research/Papers/大模型/Stress_Testing_a_Multimodal_Large_Language_Model_Grading_Assistant_on_Kinematics_Graph_Reading|Stress Testing a Multimodal Large Language Model Grading Assistant on Kinematics Graph Reading]]

![[assets/2611.22726_figure.png|800]]

- **arXiv**: [2611.22726](https://arxiv.org/abs/2611.22726)
- **PDF**: https://arxiv.org/pdf/2611.22726
- **详细分析**: [[20_Research/Papers/大模型/Stress_Testing_a_Multimodal_Large_Language_Model_Grading_Assistant_on_Kinematics_Graph_Reading|Stress Testing a Multimodal Large Language Model Grading Assistant on Kinematics Graph Reading]]
- **作者**: Ons Zammel, Carlos Soares, Flávia Carvalhido, Gerd Kortemeyer
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Stress Testing a Multimodal Large Language Model Grading Assistant on Kinematics Graph Reading》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) can recognize graph features yet award credit without sufficient graphical support. This exploratory study examines selected grading outputs for synthetic responses to four kinematics exercises, generated through visual distortion and progressive transformation toward reference graphs. Different model and prompt configurations were used. Some judgments correctly distinguished instantaneous zero velocity from rest over a finite interval and recognized positive curvature. Yet a severely distorted velocity--time graph received full credit despite disconnected and branching traces and an unclear zero-velocity reference. Other submissions graded under the same configuration lost substantial credit. Numerical cutoffs intended to distinguish meaningful features from drawing irregularities were supplied without a coordinate convention for unnumbered graphs, leaving the basis of exact partial-credit awards unresolved. Stress testing can expose unsupported awards before classroom use. For the configurations examined, we do not recommend accepting scores as final grades without instructor review, including review of full-credit responses.

</details>

---

### [[20_Research/Papers/强化学习/Making_the_World_React_Realistically_A_Closed-Loop_Interactive_World_Model_for_Autonomous_Driving|Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving]]

![[assets/2611.22691_figure.png|800]]

- **arXiv**: [2611.22691](https://arxiv.org/abs/2611.22691)
- **PDF**: https://arxiv.org/pdf/2611.22691
- **详细分析**: [[20_Research/Papers/强化学习/Making_the_World_React_Realistically_A_Closed-Loop_Interactive_World_Model_for_Autonomous_Driving|Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving]]
- **作者**: Jia Hu, Yang Chang, Panqu Wang, Zhijun Fu, Chang Liu, Changjian Yu, Jintao Lai
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 0.2，世界模型 0.8）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and the ego visual observations. We propose a closed-loop interactive WM that couples behavior modeling and visual rendering. First, imitation-learned background-vehicle (BV) policies are fine-tuned with multi-agent reinforcement learning in the closed loop against an end-to-end ego planner that reacts to the rendered images, so that their interaction behaviors match those in real logs. Second, the viewpoints exposed by these interactions guide a per-Gaussian diagnosis of each 3D Gaussian vehicle asset, which attenuates view-dependent colors on under-observed Gaussians and fills never-observed surfaces with generated Gaussians, while preserving the observed appearance. Third, signal lights are rendered according to the driving intentions of the vehicles, by an editor that learns the light states unobserved for a vehicle through counterfactual fine-tuning with a light-state classifier. On long-tail closed-loop scenarios, our method reduces the divergence from real-world interaction behaviors by 85% and improves novel-view vehicle PSNR by 2.0dB over the state-of-the-art WM. The significance of BV light signaling in WMs is shown, as the rendered signal lights conveying BV driving intentions indirectly impact ego driving behaviors in a quarter of the scenarios.

</details>

---

### [[20_Research/Papers/世界模型/JointGV_Structure-Aware_Correction_of_Visual_World_Models_with_Parallel_Graph_Dynamics_for_Long-Horizon_Modeling|JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling]]

![[assets/2611.22543_figure.png|800]]

- **arXiv**: [2611.22543](https://arxiv.org/abs/2611.22543)
- **PDF**: https://arxiv.org/pdf/2611.22543
- **详细分析**: [[20_Research/Papers/世界模型/JointGV_Structure-Aware_Correction_of_Visual_World_Models_with_Parallel_Graph_Dynamics_for_Long-Horizon_Modeling|JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling]]
- **作者**: Tian Lyu, Yichen Jiang, Ziyuan Cheng, Yunda Yan, Xiangyu Pan, Junjie Jiang, Jialin Yu, Boyu Ning, Pietro Liò, Fan Mo
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DAFT-RL, GeoWorld, IRASim, PhyDNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models predict future visual states conditioned on actions, but recursive errors in entity poses and spatial relations limit their long-horizon prediction for robot planning and control. We ask whether a separately predicted relational state can correct this drift without restructuring the visual model. This is challenging because graph nodes and visual states share neither elements nor a feature space. We propose Joint Graph--Visual Dynamics Correction (JointGV), a plug-in based on a cross-granularity dynamics hypothesis: despite their different representations, graph-node and visual-state changes describe the same physical transition. JointGV rolls out a task-conditioned scene graph alongside the visual world model, couples their predicted changes, and combines the resulting graph-motion context with graph-predicted node positions to compute a bounded residual. Graph-learning and correction gradients do not propagate into the original visual dynamics. We attach JointGV to DINO-WM (spatial tokens) and DreamerV3 (a global latent state), evaluating both on DMC Cheetah Run and Walker Walk across three seeds and extending the evaluation to contact-rich manipulation with DMC Finger Turn Hard. Across 32-step rollouts, JointGV improves structural and visual-prediction accuracy, reducing joint-position error by 11--28\%. For spatial tokens, learned graph--visual change coupling gives lower error than broadcasting the same mean graph-motion context to every token, particularly when non-adjacent parts appear close together in the image. On real-robot inverted-pendulum sequences, JointGV reduces DINO-WM's 32-step pole-angle error from $12.56^\circ$ to $6.69^\circ$ and improves DreamerV3 and LeWorldModel as well. In simulated inverted-pendulum control, an actor trained with JointGV-corrected rollouts completes 46 of 50 episodes, compared with none using the original rollouts.

</details>

---

### [[20_Research/Papers/世界模型/Testing_World_Models_on_Actions_They_Have_Never_Seen_Held-Out_Plans,_Forecast_Accuracy_and_Price_Rules_in_Retail|Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail]]

![[assets/2611.22537_first_page.png|800]]

- **arXiv**: [2611.22537](https://arxiv.org/abs/2611.22537)
- **PDF**: https://arxiv.org/pdf/2611.22537
- **详细分析**: [[20_Research/Papers/世界模型/Testing_World_Models_on_Actions_They_Have_Never_Seen_Held-Out_Plans,_Forecast_Accuracy_and_Price_Rules_in_Retail|Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail]]
- **作者**: Karthik Iyer
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A world model is trusted to answer "what if": how its world responds to an action it has never seen. We give a test of that trust for any action-conditioned world model: actions held out of training by design and scored against a known answer; whether forecast accuracy predicts accuracy on those actions; and the same structure given to simpler models. We run it in retail, where the action is a price and promotion plan, across 2,853 fitted models. First, forecast accuracy is a fair guide between kinds of model (rank correlation with error on new plans 0.32 to 0.66) and a poor guide between versions of one world model: where merchants plan into high-demand weeks the link reverses, down to -0.69. Second, training the world model to learn the effect of actions (JEPA pretraining, a latent consistency check, adaptation at the plan date) leaves its error on new plans unchanged. Third, in generated worlds the recorded regular price and three price rules improve it. Given the same rules, a log-linear model is best when its curve can match the truth; in a world whose curve lies outside the rules, the world model with the rules is ahead of the log-linear model with the rules in 36 of 40 worlds, and does as well without its recurrent cell. On real data (Breakfast at the Frat, The Complete Journey and M5) the rules lower the world model's error on pure price cuts deeper than any it saw (0.63 to 0.56 on the Frat; 0.45 to 0.44, within chance, on The Complete Journey), but not on lasting price moves. Fourth, a small share of random test plans helps every model a little. In a generated dosing world, a stress test in a second domain, the first finding repeats, and the built-up drug level lowers the world model's error (2.86 to 1.91) though it still predicts only 0.12 to 0.32 of the true gain. The test carries to any domain where a world model is asked about actions outside its history.

</details>

---

### [[20_Research/Papers/大模型/LMLineage_Content_Lineage_and_Context_Governance_for_LLM_Agents|LMLineage: Content Lineage and Context Governance for LLM Agents]]

![[assets/2611.22511_figure.png|800]]

- **arXiv**: [2611.22511](https://arxiv.org/abs/2611.22511)
- **PDF**: https://arxiv.org/pdf/2611.22511
- **详细分析**: [[20_Research/Papers/大模型/LMLineage_Content_Lineage_and_Context_Governance_for_LLM_Agents|LMLineage: Content Lineage and Context Governance for LLM Agents]]
- **作者**: Wei Hou, Jingxin Geng, Xin Chen, Zheqing Jiang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《LMLineage: Content Lineage and Context Governance for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any additional inference passes. On top of the lineage metadata, we build concept-drift micro compaction: instead of waiting for the context-length limit and summarizing everything, the system detects when previously used input documents have stopped being referenced ("drifted") and surgically compacts only those, preserving user instructions verbatim. We evaluate on a multi-tier corpus: 71 gold annotated sentences from 10 Chinese web-QA cases, plus 90 turns of independently collected multi-turn sessions across three generator models (gpt-4o-mini, qwen3.8-27b, deepseek-v4-flash). Results show that (i) window-level embedding similarity is far better aligned with LLM paraphrasing than whole document or lexical matching; (ii) the greedy-window fast path is both faster and more accurate on average than exhaustive line-matching (a multiple-comparisons bias in the latter inflates web recall at the cost of overall accuracy); (iii) per-turn attribution completes in 1s on a single GPU, remaining stable as context accumulates to 40 turns; and (iv) concept-drift detection is conservative (0% false compaction) with recall bounded by attribution accuracy. We further describe the concept-drift micro compaction design and an interactive incident-tracing/memory-cleaning case study. A companion patent application covers the lineage construction method.

</details>

---

### [[20_Research/Papers/世界模型/Towards_Data-Efficient,_Real-Time_World_Models|Towards Data-Efficient, Real-Time World Models]]

![[assets/2611.22497_figure.png|800]]

- **arXiv**: [2611.22497](https://arxiv.org/abs/2611.22497)
- **PDF**: https://arxiv.org/pdf/2611.22497
- **详细分析**: [[20_Research/Papers/世界模型/Towards_Data-Efficient,_Real-Time_World_Models|Towards Data-Efficient, Real-Time World Models]]
- **作者**: Raluca Stevenson, David Bignell, Jennifer C. White, Tabish Rashid, Emanuele Aiello, Mariya Hendriksen, Junha Hyung, Sadegh Aliakbarian, Abdelhak Lemkhenter, Marko Tot, Katja Hofmann, Sarah Parisot
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Towards Data-Efficient, Real-Time World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MineWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State-of-the-art world models have been used to produce sequences of gameplay that accord with provided user-input actions. However, high quality, consistent gameplay generation often comes at the cost of inference speed, making real-time interactive play and ideation challenging. The substantial quantities of data used to train state-of-the-art models have also made custom training of these models appear impractical, limiting many of their potential uses in creative fields. In this work we demonstrate a major step towards efficient world models: achieving both fast high-quality inference, and improved data efficiency. This is done by replacing the next-token prediction paradigm with a two-stage discrete diffusion-based approach, introducing a lightweight refinement transformer which carries out iterative masked predictions. Building on an autoregressive world model capable of generating highly consistent and complex sequences over minutes (Kanervisto et al., 2025), we achieve substantial model speed-up (79x) with a modest quality trade-off. Additionally, we demonstrate that this model can be trained to reproduce high-quality, consistent gameplay using a dataset containing approximately one day (28 hours) of gameplay data. Our results demonstrate progress towards removing barriers to the use of world models in settings where real-time inference and data efficiency are essential.

</details>

---

### [[20_Research/Papers/具身智能/Manufacturing_Differential_Sparsity_Planner-Hardware_Co-Design_for_Efficient_World_Model_Planning|Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning]]

![[assets/2611.22483_figure.png|800]]

- **arXiv**: [2611.22483](https://arxiv.org/abs/2611.22483)
- **PDF**: https://arxiv.org/pdf/2611.22483
- **详细分析**: [[20_Research/Papers/具身智能/Manufacturing_Differential_Sparsity_Planner-Hardware_Co-Design_for_Efficient_World_Model_Planning|Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning]]
- **作者**: Wenbo Zhu, Paul Yi-Chia Chen, Yuanhan Li, Zishen Wan, Christopher Torng
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.12（加权：具身智能 0.6，大模型 0.1，强化学习 0.16，世界模型 0.96，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

JEPA-style latent world models let embodied agents plan toward new goals with model predictive control, but they are still too slow for real-life embodied control: sampling-based MPC repeats predictor inference tens of thousands of times per plan, and even on high-end GPUs one planning step can take tens of seconds. We observe substantial latent locality in this repeated-inference workload: the predictor maps close actions to close latents, and inside a quantized predictor this closeness takes a form that hardware can exploit, differential bit-level sparsity. Unlike an input stream, whose temporal similarity is given, a planner itself decides which candidates it evaluates together, so the planner can choose its own references and, with reference forest sampling, manufacture more sparsity: it couples the sampled action sequences of each group to a shared root, with competitive planning quality. We build the accelerator on the insights of the rich line of bit-level sparsity accelerators and design it and the planner tightly coupled as a single co-design: the planner increases sparsity and exposes structure for hardware scheduling, and the bit-exact hardware effectively uses the sparsity that the planner creates. On three JEPA world models, our co-design is 1.28-1.80x faster than a dense accelerator and uses 38-52% less energy, and it is 1.22-1.58x faster than prior bit-sparse design and uses 16-36% less energy, with the same area. To our knowledge, our planner is the first planner that manufactures differential bit-level sparsity across its candidates and exposes its structure for hardware scheduling, and our co-design is the first algorithm-hardware co-design for JEPA-style world-model planning.

</details>

---

### [[20_Research/Papers/大模型/Eyes_in_the_Update_Learning_Where_Rewards_Land_in_Multimodal_Reasoning|Eyes in the Update? Learning Where Rewards Land in Multimodal Reasoning]]

![[assets/2611.22438_figure.png|800]]

- **arXiv**: [2611.22438](https://arxiv.org/abs/2611.22438)
- **PDF**: https://arxiv.org/pdf/2611.22438
- **详细分析**: [[20_Research/Papers/大模型/Eyes_in_the_Update_Learning_Where_Rewards_Land_in_Multimodal_Reasoning|Eyes in the Update? Learning Where Rewards Land in Multimodal Reasoning]]
- **作者**: Lixuan He, Tianzhe Chu, Shulin Tian, Shikang Zheng, Feng Chen, Yi Ma
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.5，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Eyes in the Update? Learning Where Rewards Land in Multimodal Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：Gaze-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal post-training has moved from broad instruction tuning toward reinforcement learning for image and video reasoning, where outcome rewards can improve final-answer accuracy. Yet these rewards are assigned to complete generated trajectories, while visual evidence is used only at sparse and uneven positions inside the response. Recent work has begun to make multimodal RL more token-sensitive through grounding signals or external token-level weighting. We ask a more specific question: can the allocation of the same trajectory-level reward be inferred from the model's own multimodal computation, rather than from an auxiliary annotator, perception module, or process label? We propose Gaze-RL, a representation-driven policy optimization method that redistributes completion-level advantage through a latent reward landing field. The field is computed from internal cross-modal geometry and local predictive uncertainty, assigning larger update weight to positions that are both visually anchored and decision-bearing while remaining mean-one, so the total credit of each rollout is preserved and only its positionwise allocation changes. Gaze-RL requires no process supervision, auxiliary perception module, or architectural modification, and improves both Qwen2.5-VL and InternVL3.5 across a broad range of image and video benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/ROSMonitoring_in_Action_Runtime_Monitoring_and_Enforcement_for_ROS_2_Actions|ROSMonitoring in Action: Runtime Monitoring and Enforcement for ROS 2 Actions]]

![[assets/2611.22407_first_page.png|800]]

- **arXiv**: [2611.22407](https://arxiv.org/abs/2611.22407)
- **PDF**: https://arxiv.org/pdf/2611.22407
- **详细分析**: [[20_Research/Papers/具身智能/ROSMonitoring_in_Action_Runtime_Monitoring_and_Enforcement_for_ROS_2_Actions|ROSMonitoring in Action: Runtime Monitoring and Enforcement for ROS 2 Actions]]
- **作者**: Giacomo Paltrinieri, Angelo Ferrando
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ROSMonitoring in Action: Runtime Monitoring and Enforcement for ROS 2 Actions》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic applications often rely on long-running operations, such as navigation, manipulation, and inspection, which in ROS~2 are commonly implemented as actions. Unlike topics and services, actions involve a structured lifecycle comprising goal submission and acceptance, feedback, status updates, result retrieval, and cancellation. Existing versions of ROSMonitoring support topics and services, but do not reconstruct this lifecycle or expose action-level events to a runtime-verification oracle. In this paper, we extend ROSMonitoring with runtime monitoring and enforcement for ROS~2 actions. Actions are declared directly in the monitoring configuration and automatically instrumented through the underlying ROS~2 communication endpoints. The generated monitor reconstructs action-level events, correlates them through goal identifiers, maintains the state of active goals, and translates violations into protocol-aware enforcement operations. These include goal rejection, cancellation, message suppression, and protocol-compliant responses generated directly by the monitor when the original communication cannot be forwarded. We evaluate the implementation through controlled stress tests that vary the number of action invocations, workload size, and clientâserver topology. The results show approximately linear growth in monitoring cost with repeated action invocations under a fixed workload, while larger action workloads and a greater number of configured clientâserver pairs introduce additional overhead. These results characterise the scaling behaviour of the current implementation under the tested sequential workloads while highlighting the main performance limitations of the current synchronous implementation.

</details>

---

### [[20_Research/Papers/世界模型/FailureGen_Scalable_Robot_Failure_Data_Generation_with_World_Models|FailureGen: Scalable Robot Failure Data Generation with World Models]]

![[assets/2611.22367_figure.png|800]]

- **arXiv**: [2611.22367](https://arxiv.org/abs/2611.22367)
- **PDF**: https://arxiv.org/pdf/2611.22367
- **详细分析**: [[20_Research/Papers/世界模型/FailureGen_Scalable_Robot_Failure_Data_Generation_with_World_Models|FailureGen: Scalable Robot Failure Data Generation with World Models]]
- **作者**: Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《FailureGen: Scalable Robot Failure Data Generation with World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, MiraBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot failures are difficult to collect at scale, limiting the range of failure scenarios represented in robot learning datasets. We present FailureGen, a method for generating synthetic videos with temporal event annotations by reusing action trajectories from recorded failures. The method comprises four stages: (1) fine-tuning an action-conditioned Cosmos world model on successful and failed real executions; (2) annotating source recordings to identify failure-associated donor segments and compatible successful hosts; (3) transferring donor motion into host contexts, with optional spatial offsets, to generate continuous video rollouts; and (4) annotating and filtering the generated samples according to observed events and visual quality. We study two implementations with different tasks and robot configurations, with visual failure detection serving as one downstream application. In a preliminary comparison, a detector trained on real and generated data achieves an average precision of 0.51, compared with 0.41 using real data alone, and detects 33 of 36 failure intervals, compared with 28 of 36. By reusing observed failures in additional contexts, FailureGen expands the data available for studying robot failures and developing downstream learning methods.

</details>

---

### [[20_Research/Papers/大模型/EviDARL_Evidence-Centric_Dual-Agent_Reasoning_via_Alternating_Reinforcement_Learning_for_Multi-Table_Question_Answering|EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering]]

![[assets/2611.22310_figure.png|800]]

- **arXiv**: [2611.22310](https://arxiv.org/abs/2611.22310)
- **PDF**: https://arxiv.org/pdf/2611.22310
- **详细分析**: [[20_Research/Papers/大模型/EviDARL_Evidence-Centric_Dual-Agent_Reasoning_via_Alternating_Reinforcement_Learning_for_Multi-Table_Question_Answering|EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering]]
- **作者**: Dunhan Li, Leilei Gan, Lirong Gao, Wenyan Fan, Yongwei Wang, Sheng Guo, Fei Wu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EviDARL, MMQA, MultiTabQA, TQA-Bench, TQABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite advances in LLM-based table reasoning, most studies focus on single-table settings. Multi-table QA requires multi-hop reasoning over complex table relationships and evidence dispersed across long contexts, often without verifiable intermediate traces. To address these challenges, we introduce EviDA, an evidence-centric dual-agent framework comprising an Evidence Construction Agent and a Reasoning and Answering Agent. The Evidence Construction Agent generates and executes table-manipulation programs over complete tables to produce question-specific evidence and verifiable intermediate traces, simplifying subsequent reasoning. The Reasoning and Answering Agent then performs multi-hop reasoning over this evidence to derive final answers. We further introduce EviDARL, which combines agent-specific fine-grained rewards with parameter-efficient alternating reinforcement learning to improve collaboration between the agents. By optimizing each agent in turn while holding the other fixed, EviDARL enables bidirectional adaptation between evidence construction and answer reasoning. Experiments on MMQA and TQA-Bench demonstrate that EviDARL substantially outperforms competitive open-model and multi-table reasoning baselines under constrained model and training budgets.

</details>

---

### [[20_Research/Papers/强化学习/Perception_into_Imagination_Executable_Memory_for_World_Models|Perception into Imagination: Executable Memory for World Models]]

![[assets/2611.22294_figure.png|800]]

- **arXiv**: [2611.22294](https://arxiv.org/abs/2611.22294)
- **PDF**: https://arxiv.org/pdf/2611.22294
- **详细分析**: [[20_Research/Papers/强化学习/Perception_into_Imagination_Executable_Memory_for_World_Models|Perception into Imagination: Executable Memory for World Models]]
- **作者**: Xianyao Li, Ruitong Tian, Rui Min, Fang Xu, Jing Du
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Perception into Imagination: Executable Memory for World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MiniWorld, PlaNet, SearchWorld, TT-MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical agents must use what they previously saw or touched after visibility or contact is lost. Their actions change the implications of these remembered facts. We introduce executable perceptual memory (EPM), a world-model framework that advances explicit perceptual state alongside neural latent dynamics during imagination. Its evolving read-out informs reward prediction, value estimation and policy learning. We align reward inputs with the transitions that produced them and supervise the reward head on open-loop rollouts of recorded actions. On Memory Maze $13\times13$, EPM reaches 30.37 return at 1M interactions, compared with 23.37 when the same evolving read-out informs only policy and value on a common perceptual front end: a gain of 7.00 [3.80, 10.21]. The complete method also improves control on $9\times9$ and in MiniWorld. Probes of remembered, out-of-view arrivals show stronger reward anticipation in both visual implementations. Concentration, tactile recovery and real tactile frames demonstrate complementary roles of remembered facts in imagined-policy training, motion-dependent decisions and sensory-content retention. EPM connects persistent perception to the predicted consequences and learning signals of a world model for Physical AI.

</details>

---

### [[20_Research/Papers/大模型/Multi-Agent_Memory_Inconsistency_Where_Factual_Conflicts_Disappear_in_LLM_Agents|Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents]]

![[assets/2611.22245_figure.png|800]]

- **arXiv**: [2611.22245](https://arxiv.org/abs/2611.22245)
- **PDF**: https://arxiv.org/pdf/2611.22245
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_Memory_Inconsistency_Where_Factual_Conflicts_Disappear_in_LLM_Agents|Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents]]
- **作者**: Hejia Zhang, Zhongming Yu, Yimin Ding, Wei-Ting Chen, Hengjia Yu, Wentao Ni, Yijun Liu, Cong Xu, Xin Chen, Matrix Yao, Fan Zhao, Jishen Zhao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HiddenBench, HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

</details>

---

### [[20_Research/Papers/大模型/The_Only_Edge_Was_Memorized_in_Training_LLM_Trading_Agents_Around_Earnings_and_Bad_News|The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News]]

![[assets/2611.22177_figure.png|800]]

- **arXiv**: [2611.22177](https://arxiv.org/abs/2611.22177)
- **PDF**: https://arxiv.org/pdf/2611.22177
- **详细分析**: [[20_Research/Papers/大模型/The_Only_Edge_Was_Memorized_in_Training_LLM_Trading_Agents_Around_Earnings_and_Bad_News|The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News]]
- **作者**: Jackson Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) trading agents are tested on news, but news reaches stock prices within minutes, and a benchmark that replays headlines at their publication time finds no alpha in trading on them. Money can then remain in two places, before news whose date is known, such as earnings announcements, and after bad news, if the market's fall went too far. However, studies of LLMs and earnings read documents published with or after the announcement, and studies of reversal sort monthly portfolios, so neither tells whether an agent can trade these moments after costs. In this paper, we test LLM agents at both moments on the same look-ahead-free benchmark, before 598 earnings announcements and after 409 bad-news drops of large US stocks. Every input is cut at the decision close, staged agents are compared with single calls, simple rules and a logistic regression, and every decision is made with and without the stock's name. Across five models from four vendors, no agent beat the simple bets. Before earnings, the agents mostly bought and earned what buying before every announcement earned, and after bad news, a Gemini-based agent called almost every fall an overreaction while no agent picked better dips than buying them all. The only gains came from what the models had memorized in training. Given only the ticker and the dates, a GPT-based model called the direction of 59.2% of the announcements before its training cutoff and 53.3% after it. Agent builders should therefore compare an event agent with the simple bet and test it blind after the training cutoff.

</details>

---

### [[20_Research/Papers/强化学习/When_does_deep_reinforcement_learning_pay_off_in_HVAC_supervisory_control_Four_small_Modelica_case_studies_trained_directly_on_FMUs|When does deep reinforcement learning pay off in HVAC supervisory control? Four small Modelica case studies trained directly on FMUs]]

![[assets/2611.22144_figure.png|800]]

- **arXiv**: [2611.22144](https://arxiv.org/abs/2611.22144)
- **PDF**: https://arxiv.org/pdf/2611.22144
- **详细分析**: [[20_Research/Papers/强化学习/When_does_deep_reinforcement_learning_pay_off_in_HVAC_supervisory_control_Four_small_Modelica_case_studies_trained_directly_on_FMUs|When does deep reinforcement learning pay off in HVAC supervisory control? Four small Modelica case studies trained directly on FMUs]]
- **作者**: Bingnan Zhao, Harshala Gammulle, Tharindu Fernando
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.22（加权：大模型 0.1，强化学习 1.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《When does deep reinforcement learning pay off in HVAC supervisory control? Four small Modelica case studies trained directly on FMUs》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BOPTEST-Gym, DRL, ModelicaGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) is often proposed for the supervisory control of heating, ventilation and air-conditioning (HVAC) systems. The reported gains are, however, difficult to interpret, because the baselines are often weak and the attainable optimum is seldom known. This paper examines four small, reproducible case studies based on an office building in Brisbane, Australia: pre-cooling under a time-of-use tariff; chiller staging with condenser water reset; chilled water supply temperature reset with a wet cooling coil; and chilled water storage under time-of-use prices and a demand charge. The plants were modelled with the Modelica Buildings library, and in three of the cases a soft actor-critic agent was trained directly on the exported functional mock-up unit (FMU). Each agent was compared with tuned rule-based controllers and, where practicable, with a near-optimal reference from hourly exhaustive search or dynamic programming with perfect foresight. In the two cases without storage the agent reached the near-optimal reference, but the margin above a well-chosen rule was small: 1.3% for condenser water reset and 0.18% for chilled water reset. In the latter case two common reset rules consumed more energy than a fixed set point. With a chilled water storage tank the margin was considerably larger. The agent outperformed both rules (-7.8%, compared with -3.9% and -6.3%) and adopted midday charging during the solar off-peak period, yet it obtained only about 45% of the saving achieved by the perfect-foresight schedule and did little to limit the demand peak. In the pre-cooling case a hand-tuned rule remained superior (-12.0% compared with -5.6%). These results suggest that studies of DRL for HVAC control should state the margin between the best rule and a near-optimal reference. Some practical difficulties encountered in training on co-simulation FMUs are also reported.

</details>

---

### [[20_Research/Papers/大模型/RoboTeam_Benchmarking_Vision-Based_Multi-Agent_Control_of_Many_Robot_Arms_in_Real_Time|RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time]]

![[assets/2611.22138_figure.png|800]]

- **arXiv**: [2611.22138](https://arxiv.org/abs/2611.22138)
- **PDF**: https://arxiv.org/pdf/2611.22138
- **详细分析**: [[20_Research/Papers/大模型/RoboTeam_Benchmarking_Vision-Based_Multi-Agent_Control_of_Many_Robot_Arms_in_Real_Time|RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time]]
- **作者**: Changxuan Fan, Zhongwei Xie, Boyi Zhang, Shaoli Hu, Chang Xu, Xiyu Ren, Yufei Li, Qiao Xiao, Huihao Jing, Kawai Chung, Wenbin Hu, Hongyu Luo...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CLiMBench, EmbodiedBench, ReflexBench, RoCoBench, RobotWorld, VIKI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal agents can now control robot arms by calling tools and writing code. Existing benchmarks fall short in three ways: most test one or two arms on short tasks, many pause the world while the agent thinks, and many give it ground-truth object positions. We present RoboTeam, a simulated benchmark where agents control 4 to 16 robot arms in real time from camera images alone. Its 36 tasks are long jobs that the arms must do together, such as passing timbers or building a picture from hundreds of cubes. We start from the most flexible agent system, the adaptive system, where one agent decides when to fork delegates. With it, gpt-6.1-sol and opus-5.5 complete 28 and 27 tasks, and four other models at most 3. But at a high price: a typical task takes gpt-6.1-sol 3.5 hours and 218 million input tokens, and a third of its steps fail at least once and must be retried. We then compare it with three fixed systems: single-agent, hierarchical, and decentralized. All four complete a similar number of tasks but differ in time and tokens. The hierarchical and decentralized systems are faster but use up to 1.9 times the tokens, and the single agent uses fewer tokens but takes 1.6 times as long, so the adaptive system lies between them. Even so, no model or system is yet fast, cheap, and reliable at once. RoboTeam measures these limits where earlier benchmarks cannot: long multi-arm jobs, camera images only, and a world that never pauses.

</details>

---

### [[20_Research/Papers/强化学习/RLDE_A_Reinforcement_Learning_Framework_for_Interpretable_Iterative_Document_Editing|RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing]]

![[assets/2611.22039_figure.png|800]]

- **arXiv**: [2611.22039](https://arxiv.org/abs/2611.22039)
- **PDF**: https://arxiv.org/pdf/2611.22039
- **详细分析**: [[20_Research/Papers/强化学习/RLDE_A_Reinforcement_Learning_Framework_for_Interpretable_Iterative_Document_Editing|RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing]]
- **作者**: Nikhil Parkar, M. Marimuthu, Riya Joshi, Karthikeyan N
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RLDE: A Reinforcement Learning Framework for Interpretable Iterative Document Editing》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ptr-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improving the quality, clarity, and flow of long documents remains a challenging problem in NLP, as human editing typically occurs through iterative refinement rather than a single-pass rewrite. Most existing automated systems act as black-box generators or rely on supervised learning, limiting interpretability and failing to capture the sequential nature of revisions. In this paper, we propose RLDE, an automated end-to-end metric-driven RL framework that formulates document revision as a reference-free MDP problem (unsupervised with respect to paired document-revision targets). Working with a limited action space (NOOP, INSERT, DELETE, REPLACE), RLDE leverages Pointer Networks for dynamic span selection at the token level and sends generative actions to the frozen BART-base model to obtain context-aware suggestions. PPO agents learn to optimize a multi-objective reward function based on readability, perplexity, and grammar metrics with the help of a novel SBERT-based Semantic Preservation Penalty constraint to avoid deletion degeneracy. Evaluations on the BEA-2019 dataset showed statistically significant results (p &lt; 0.01) across all metrics, where Flesch Reading Ease increased from 49.8 to 59.4, perplexity decreased from 63.7 to 39.8, while preserving 93% of semantic information. When compared to Chain-of-Thought (CoT) prompt-engineered models like GPT-4 and LLaMA-2, RLDE shows high performance at a very low computational inference cost. Moreover, the quality of edits generated by RLDE has been verified via human evaluations, scoring 4.9/5 for meaning preservation and 4.4/5 for edit quality.

</details>

---

### [[20_Research/Papers/具身智能/ALOHA_Lightning_Learning_Fast_and_Precise_Manipulation|ALOHA Lightning: Learning Fast and Precise Manipulation]]

![[assets/2611.21919_figure.png|800]]

- **arXiv**: [2611.21919](https://arxiv.org/abs/2611.21919)
- **PDF**: https://arxiv.org/pdf/2611.21919
- **详细分析**: [[20_Research/Papers/具身智能/ALOHA_Lightning_Learning_Fast_and_Precise_Manipulation|ALOHA Lightning: Learning Fast and Precise Manipulation]]
- **作者**: John Hua Yao. Qi Wu, Yihuai Gao, Chelsea Finn, Zipeng Fu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《ALOHA Lightning: Learning Fast and Precise Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from human demonstrations has enabled robots to acquire a wide range of manipulation skills, but learned policies typically execute far slower than ordinary humans. This speed gap is mainly due to lack of an interface for collecting demonstration data at high speed, and the difficulty in training policies that can robustly execute high-speed motions. In this paper, we present ALOHA Lightning (Flash ALOHA), a system for learning fast and precise robotic manipulation. Our system uses kinesthetic teaching to intuitively collect near-human-speed demonstrations on a backdrivable bimanual platform, yielding natural and fast trajectories. We also present a learning pipeline that enables smooth high-speed execution through test-time action smoothing and aligns the visual data distribution between data collection and deployment with masking. Given 50 demonstrations for each task, ALOHA Lightning autonomously completes bimanual tasks such as ball tossing and catching, folding shorts, battery insertion, and bussing tables for over 80% success rates while close to human speed. Project website: https://flash-aloha.github.io/

</details>

---

### [[20_Research/Papers/大模型/LLM_Trading_Agents_Earn_Beta,_Not_Alpha_A_Look-Ahead-Free_Benchmark|LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark]]

![[assets/2611.19530_first_page.png|800]]

- **arXiv**: [2611.19530](https://arxiv.org/abs/2611.19530)
- **PDF**: https://arxiv.org/pdf/2611.19530
- **详细分析**: [[20_Research/Papers/大模型/LLM_Trading_Agents_Earn_Beta,_Not_Alpha_A_Look-Ahead-Free_Benchmark|LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark]]
- **作者**: Jackson Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Trading Agents Earn Beta, Not Alpha: A Look-Ahead-Free Benchmark》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InvestorBench, LiveTradeBench, StockBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) trading agents now trade stocks for their users, and benchmarks rank models by their agents' returns. Yet a single run's return says little about skill. In our study, two runs of the same model that differed only in the random seed ended 5.2 points apart on average, so telling skill from luck takes many backtests across markets, models and seeds. However, live arenas trade each day only once, and backtests either use the few months after a model's training cutoff or run on years the model may remember, often with news joined to prices by calendar date. In this paper, we present rta-bench-1, a backtest over three US markets (a rally, a bear market and a crash). It shows each headline only after its publication minute, plays each period blind and named, and checks every run for look-ahead. It also splits each return into factor exposure and alpha and scores every decision against random choices of the same day and sector. In 91 runs of six models from four vendors, no alpha was significant, market and style exposure accounted for a median 78% of the return, and the decisions did no better than random stocks of the same sector. The agents bought the stocks with the most positive news, yet in ablations they earned as much without their headlines. Still, the agents carried out rules reliably, since a single cash rule in the prompt cut a GPT-based agent's share in stocks by 30.3 points in all six pairs. Builders should therefore supply the edge themselves and report exposures and alpha, and benchmarks should replay news by publication time.

</details>

---

### [[20_Research/Papers/机器人/ARC_Autonomous_Robotics_Compliance_A_Three-Layer_Governance_Architecture_for_Deployed_Autonomous_Systems|ARC: Autonomous Robotics Compliance A Three-Layer Governance Architecture for Deployed Autonomous Systems]]

![[assets/2609.12932_first_page.png|800]]

- **arXiv**: [2609.12932](https://arxiv.org/abs/2609.12932)
- **PDF**: https://arxiv.org/pdf/2609.12932
- **详细分析**: [[20_Research/Papers/机器人/ARC_Autonomous_Robotics_Compliance_A_Three-Layer_Governance_Architecture_for_Deployed_Autonomous_Systems|ARC: Autonomous Robotics Compliance A Three-Layer Governance Architecture for Deployed Autonomous Systems]]
- **作者**: Tord Eide, Einar Holt
- **cs 子类**: cs.AI, cs.CY, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《ARC: Autonomous Robotics Compliance A Three-Layer Governance Architecture for Deployed Autonomous Systems》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proposed governance framework for autonomous robotic systems, introducing a three-layer compliance architecture (ARC) instantiated through model safety validation, cognitive certification benchmarks, and operational authorization standards.

</details>

---
