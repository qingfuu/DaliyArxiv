# cs.LG | Machine Learning | 2026-10-28

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/强化学习/Pushing_Dexterity_and_Safety_for_In-Hand_Object_Pose_Reaching_That_Works_Remarkably_Well|Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well]]

![[assets/2610.37652_figure.png|800]]

- **arXiv**: [2610.37652](https://arxiv.org/abs/2610.37652)
- **PDF**: https://arxiv.org/pdf/2610.37652
- **详细分析**: [[20_Research/Papers/强化学习/Pushing_Dexterity_and_Safety_for_In-Hand_Object_Pose_Reaching_That_Works_Remarkably_Well|Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well]]
- **作者**: Ian Chuang, Hiya Shah, Vamsi Chilamkur, Iman Soltani, Claire Tomlin
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation with multi-fingered hands is the next frontier of robotics, yet learned hand skills remain limited to simple grasps or basic repeated motions, such as rotating an object. As robots attempt more demanding in-hand maneuvers, safety, such as not dropping the object, becomes critical, yet it is rarely measured. We study in-hand object pose reaching, a task that demands diverse and difficult grasps: moving an object to almost any position and orientation within reach of the fingers, at any wrist orientation, through long sequences of consecutive goals. We present a recipe for training such policies for a LEAP hand in simulation without human data, built on a range of insights, from diverse resets and goals via generated grasp datasets to an adaptive friction curriculum. With careful system identification, the policies transfer zero-shot to the real hand, using either motion capture or a single wrist-mounted depth camera, and prove remarkably capable and robust. On top of the task policy, we add a learned residual safety filter with adjustable conservativeness, letting us tune the balance between performance and safety and greatly reduce object drops. In 13.3 hours of real-robot evaluation over 4,800 unseen goals across 4 objects and diverse wrist orientations, the state-based policy reaches 95.2% of goals within 2 cm and 0.4 rad, and the filter cuts its drops by 75% while still reaching 91.5% of goals. The policies can also spin a lightbulb held in an arbitrary pose, reach out-of-distribution goals, withstand fast arm motion and perturbations, and, needing only a wrist camera, serve as portable skills such as screwing in a lightbulb. We release the full recipe as a platform for studying performance, reliability, and safety in high-dimensional dexterous systems. Videos and more are available at https://ian-chuang.github.io/dexsafe/.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_of_Co-Adaptive_Hip_Exoskeleton_Control_(MARL-Exo)_for_Metabolic_Energy_Reduction|Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction]]

![[assets/2610.37441_figure.png|800]]

- **arXiv**: [2610.37441](https://arxiv.org/abs/2610.37441)
- **PDF**: https://arxiv.org/pdf/2610.37441
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_of_Co-Adaptive_Hip_Exoskeleton_Control_(MARL-Exo)_for_Metabolic_Energy_Reduction|Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction]]
- **作者**: Yifei Yuan, Jakob Wolf, Ghaith Androwis, Xianlian Zhou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Objective: This study aims to determine whether a hip-exoskeleton policy trained in simulation, by co-adapting with a musculoskeletal human model under a metabolic-energy reward, reduces the metabolic cost of walking in new users without per-user tuning, and how mechanical-power shaping affects the learned assistance. Methods: We developed MARL-Exo, a multi-agent reinforcement learning framework in which a full-body human model (304 muscle actuators; randomized anatomy, gait, and speed) and a bilateral hip-exoskeleton policy are trained concurrently in two stages. The exoskeleton observes only delayed hip kinematics and its past commands; its reward includes muscle metabolic power from a physiologically based energetics model, alone (Metabolic) or with mechanical-power shaping (Metabolic + Power). The Metabolic policy was deployed and tested without retraining in eight healthy adults walking at 1.25 m/s, using indirect calorimetry. Results: In simulation, the Metabolic policy reduced modeled muscle metabolic power by 13.8% relative to no-device walking, versus 8.8% for Metabolic + Power. On hardware, MARL-Exo reduced net metabolic rate by 18.3 $\pm$ 6.6% relative to Passive in all eight participants. Relative to No-Exo, the mean reduction was 7.4 $\pm$ 10.0%; six participants more than offset the 13.1% device-wearing penalty, walking up to 24.2% below their No-Exo cost. Conclusion: A metabolically informed policy co-adapted in simulation transferred to users without per-user tuning and consistently reduced the metabolic cost of walking with the device, while explicit power shaping reduced the simulated benefit. Significance: Unlike per-user human-in-the-loop optimization, this approach yields a single population-level controller and allows assistance objectives to be screened in simulation before human testing.

</details>

---

### [[20_Research/Papers/强化学习/Hyperparameter_and_Neural_Architecture_Search_via_Evolutionary_Optimization_for_Reinforcement_Learning_HPNAS-RL|Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL]]

![[assets/2610.36882_figure.PNG|800]]

- **arXiv**: [2610.36882](https://arxiv.org/abs/2610.36882)
- **PDF**: https://arxiv.org/pdf/2610.36882
- **详细分析**: [[20_Research/Papers/强化学习/Hyperparameter_and_Neural_Architecture_Search_via_Evolutionary_Optimization_for_Reinforcement_Learning_HPNAS-RL|Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL]]
- **作者**: Nihal Acharya Adde, Hanno Gottschalk
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Hyperparameter and Neural Architecture Search via Evolutionary Optimization for Reinforcement Learning: HPNAS-RL》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AmoebaNet, EEEANet, HPNAS-RL, NASNet, NSGA-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this study, we propose a dual-branch evolutionary framework that simultaneously performs Neural Architecture Search (NAS) and Hyperparameter Optimization (HPO) for Reinforcement Learning (RL) in Autonomous Driving (AD) tasks. While NAS has shown strong potential in automating architecture design for Convolutional Neural Networks (CNNs), its application to RL remains limited, especially in scenarios that require joint optimization of architectural and training dynamics. Building on our prior work on Evolutionary Multi-Objective NAS (EMNAS), the proposed framework evolves discrete network architectures and continuous hyperparameters in parallel under a unified multi-objective search strategy. In this setup, NAS targets the convolutional layers of the RL policy network - responsible for visual feature extraction, while HPO focuses on optimizing critical RL hyperparameters. To accelerate convergence and improve generalization, we incorporate parallel evaluation and a teacher-student policy transfer mechanism. Experiments in a high-fidelity driving simulator show that the joint NAS-HPO framework consistently outperforms standalone NAS, yielding policies with higher rewards, fewer parameters, and improved stability. These results highlight the benefits of jointly optimizing model structure and training dynamics for scalable and effective RL agent design.

</details>

---

### [[20_Research/Papers/强化学习/Frequency-Uniform_Log-Regret_Reinforcement_Learning_for_Diffusions|Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions]]

![[assets/2610.36758_figure.png|800]]

- **arXiv**: [2610.36758](https://arxiv.org/abs/2610.36758)
- **PDF**: https://arxiv.org/pdf/2610.36758
- **详细分析**: [[20_Research/Papers/强化学习/Frequency-Uniform_Log-Regret_Reinforcement_Learning_for_Diffusions|Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions]]
- **作者**: Jose Blanchet, Lutong Hao, Renyuan Xu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-frequency control problems are often studied through time discretization, but refining the timestep $δ$ increases the discrete horizon $H=T/δ$ and can make standard finite-horizon regret guarantees deteriorate even when the physical horizon $T$ is fixed. We study episodic value-based reinforcement learning for Euler discretizations of controlled diffusions. The performance is measured as the cumulative regret over $K$ episodes relative to the optimal policy of the corresponding Euler model. Under stability and regularity conditions on value function gradients, Bellman residual derivatives, and fitted critics, we prove an $\mathcal{O}(\log K)$ regret bound with constants uniform in $δ$. For dynamics with drift linear in unknown parameters and unknown constant diffusion covariance, we verify localized versions of these conditions for a constrained, model-based controlled-diffusion fitted-$Q$ algorithm (CD-FQ) and obtain high-probability $\mathcal{O}(\log K\log\log K)$ regret for fixed and finite $T$, again with constants uniform in $δ$.

</details>

---

### [[20_Research/Papers/机器人/From_Biological_Curves_to_Soft_Modular_Robots_Learning-Based_Inverse_Design_with_Uncertainty-Guided_Refinement|From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement]]

![[assets/2610.36681_figure.png|800]]

- **arXiv**: [2610.36681](https://arxiv.org/abs/2610.36681)
- **PDF**: https://arxiv.org/pdf/2610.36681
- **详细分析**: [[20_Research/Papers/机器人/From_Biological_Curves_to_Soft_Modular_Robots_Learning-Based_Inverse_Design_with_Uncertainty-Guided_Refinement|From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement]]
- **作者**: Dixiang Wang, Minghao Zha, Arifur Rahman, Yinhong Qin, Yitao Jiang, Shiyang Lu, Zebing Mao, Muhao Chen, Luyang Zhao
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《From Biological Curves to Soft Modular Robots: Learning-Based Inverse Design with Uncertainty-Guided Refinement》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Animals exhibit diverse shape-changing behaviors, from the undulatory swimming of eels to the arching movements of inchworms. Reproducing these biological shapes with modular soft robots offers a promising approach to developing versatile bioinspired robotic systems. However, translating a desired shape into a feasible robotic configuration remains challenging. Existing cable-driven modular soft robots rely on computationally expensive physics-based modeling and combinatorial search for inverse design, making it difficult to efficiently reproduce diverse target shapes. To address this challenge, we present a learning-based real-to-sim-to-real framework that translates biological curves into robotic configurations through surrogate-assisted inverse design and uncertainty-guided refinement. The proposed method combines learned inverse prediction with targeted candidate exploration, using a fast forward surrogate to evaluate and select suitable designs. The learned forward surrogate reduces deformation prediction time from $1.53 \times 10^5$ ms to 0.0008 ms, achieving approximately a $1.9 \times 10^8$-fold speedup. At the same time, the proposed inverse design method reduces design time from $1.99 \times 10^6$ ms to 4.18 ms. On 5,000 test samples generated from previously unseen threading patterns, the method achieves a 93% shape reconstruction success rate under surrogate-based evaluation. Physical demonstrations with four bioinspired robots further illustrate the translation of biological curves into realizable robotic shapes.

</details>

---

### [[20_Research/Papers/大模型/CoHARL_Co-Evolving_Agent_Policies_and_Executable_Harnesses_with_Reinforcement_Learning|CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning]]

![[assets/2610.36469_figure.png|800]]

- **arXiv**: [2610.36469](https://arxiv.org/abs/2610.36469)
- **PDF**: https://arxiv.org/pdf/2610.36469
- **详细分析**: [[20_Research/Papers/大模型/CoHARL_Co-Evolving_Agent_Policies_and_Executable_Harnesses_with_Reinforcement_Learning|CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning]]
- **作者**: Jianwen Chen, Peng Xia, Kaide Zeng, Siwei Han, Zhen-Yu Zhang, Charles Fleming, Xinyu Ye, Huaxiu Yao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.7，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoHARL, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents interact with their environments through executable harnesses that govern tool use and feedback. Optimizing a harness for a fixed policy overlooks how its behavior changes during learning, while training a policy under a fixed harness leaves the interface that generates its training experience unchanged. This motivates adapting the harness throughout policy training. We introduce CoHARL, a population-based reinforcement learning framework that co-evolves a shared policy and a population of executable harnesses. The policy learns from rollouts across the population, and a proposer uses its execution traces to revise harness code during training. CoHARL achieves a 27.6% mean resolved rate on SWE-rebench, improving over harness-only search by 6.4 percentage points. Experiments on SWE-bench Verified and Terminal-Bench 2.0 show gains in software engineering and terminal-based tasks. Under matched training budgets, CoHARL also outperforms searching for a harness once before RL and alternating policy updates with revisions to a single active harness.

</details>

---

### [[20_Research/Papers/强化学习/Whole-Body_Humanoid_Control_via_Stochastic_Motion_Tokenization|Whole-Body Humanoid Control via Stochastic Motion Tokenization]]

![[assets/2610.36452_figure.png|800]]

- **arXiv**: [2610.36452](https://arxiv.org/abs/2610.36452)
- **PDF**: https://arxiv.org/pdf/2610.36452
- **详细分析**: [[20_Research/Papers/强化学习/Whole-Body_Humanoid_Control_via_Stochastic_Motion_Tokenization|Whole-Body Humanoid Control via Stochastic Motion Tokenization]]
- **作者**: Michael Drolet, Oleg Arenz, Jan Peters
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Whole-Body Humanoid Control via Stochastic Motion Tokenization》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While velocity-commanded RL policies are effective for controlling quadrupeds, they are a limited interface for humanoids that need to perform complex whole-body motions. Furthermore, RL tracking policies for whole-body motions typically have limited information about the desired future motion, preventing them from performing controlled deviations to achieve long-term task success; such information is particularly relevant when a controller must prepare for transitions between behaviors. We address these challenges using concise motion representations that can be generated by a high-level controller, given a behavior label or text command. These representations can be fed directly into a tracking policy to provide a detailed motion reference. Our method exhibits a high degree of flexibility in performing real-world robot motions such as dancing, fighting, or walking based on conditional information. At matched capacity, our adopted stochastic motion tokenizer reconstructs motions from the Unitree G1 at a level that exceeds state-of-the-art approaches such as finite scalar quantization (FSQ) and the vector-quantized autoencoder (VQ-VAE). The resulting discrete interface conditions whole-body tracking policies that execute generated dance, fight, and walk motions lasting 16.8 s each and a 35 s fight-to-dance sequence on a physical Unitree G1.

</details>

---

### [[20_Research/Papers/强化学习/Bridging_Exploration_and_Loss_of_Plasticity_in_On-Policy_Reinforcement_Learning|Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning]]

![[assets/2610.36309_figure.png|800]]

- **arXiv**: [2610.36309](https://arxiv.org/abs/2610.36309)
- **PDF**: https://arxiv.org/pdf/2610.36309
- **详细分析**: [[20_Research/Papers/强化学习/Bridging_Exploration_and_Loss_of_Plasticity_in_On-Policy_Reinforcement_Learning|Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning]]
- **作者**: Andrea Vasco Grieco, Evelyn D'Elia, Edoardo Caldarelli, Raffaello Camoriano
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.32（加权：具身智能 0.3，强化学习 1.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (RL) algorithms have been observed to lose the ability to adaptively learn from new data, a phenomenon termed Loss of Plasticity (LoP). While many metrics have been shown to correlate with it, the causal mechanisms and the geometric conditions from which it can arise have not been clearly identified. We analyze LoP in Proximal Policy Optimization with isotropic Gaussian policies, the state-of-the-art formulation for many continuous action spaces in RL. We report multiple metrics which characterize the effect that the policy standard deviation $σ$ has on LoP, and we also suggest related explanations for the effectiveness of widely adopted LoP mitigation techniques. We observe a significant effect of $σ$ on the extent of LoP, and accompany this with both theoretical and experimental supporting arguments. Our experimental validation consists of LoP benchmark evaluations against standard baselines as well as real-world policy deployment on a 7-DoF robotic arm.

</details>

---

### [[20_Research/Papers/强化学习/Jaxnasium_Embracing_PyTrees_For_Any-Agent,_Cross-Suite_Reinforcement_Learning|Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning]]

![[assets/2610.36075_first_page.png|800]]

- **arXiv**: [2610.36075](https://arxiv.org/abs/2610.36075)
- **PDF**: https://arxiv.org/pdf/2610.36075
- **详细分析**: [[20_Research/Papers/强化学习/Jaxnasium_Embracing_PyTrees_For_Any-Agent,_Cross-Suite_Reinforcement_Learning|Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning]]
- **作者**: Koen Ponse, Aske Plaat, Thomas M. Moerland
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CleanRL, ImageNet, JaxMARL, PureJAXRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and algorithm implementations are typically written for a single suite, a single type of space, and either JAX-native or host-based environments. Here we present Jaxnasium, a library for JAX-based reinforcement learning, aiming to make the field more accessible. Jaxnasium represents observation and action spaces as PyTrees, and uses this structure to build networks and support multi-agent processing. Through this, its near-single-file implementations run on discrete, continuous, image, and composite spaces, as well as in multi-agent environments, without any changes to the algorithm code. The same files serve as readable, research-friendly algorithms, as well as importable algorithms for more applied workloads. Through a minimal Gymnasium-style interface and wrappers for 11 suites, over 300 environments are available on which a small PPO implementation with default hyperparameters is able to run. Additionally, through a simple wrapper, we can run Gymnasium and EnvPool environments with the same algorithm and training loop, with no performance loss compared to architectures specifically built for training JAX algorithms on host-based environments. Jaxnasium further provides tools for multi-seed evaluation, hyperparameter sweeps, and project scaffolding. Jaxnasium is open-sourced at https://github.com/ponseko/jaxnasium

</details>

---

### [[20_Research/Papers/强化学习/Causal_DAG-Guided_Reinforcement_Learning_for_Long-Term_Physical_Activity_Maintenance_Using_Prior_Data_to_Inform_Future_Deployment|Causal DAG-Guided Reinforcement Learning for Long-Term Physical Activity Maintenance: Using Prior Data to Inform Future Deployment]]

![[assets/2610.36019_figure.png|800]]

- **arXiv**: [2610.36019](https://arxiv.org/abs/2610.36019)
- **PDF**: https://arxiv.org/pdf/2610.36019
- **详细分析**: [[20_Research/Papers/强化学习/Causal_DAG-Guided_Reinforcement_Learning_for_Long-Term_Physical_Activity_Maintenance_Using_Prior_Data_to_Inform_Future_Deployment|Causal DAG-Guided Reinforcement Learning for Long-Term Physical Activity Maintenance: Using Prior Data to Inform Future Deployment]]
- **作者**: Xueqing Liu, Young Hyun Cho, Bhanu Teja Gullapalli, Predrag Klasnja, Susan Murphy
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Causal DAG-Guided Reinforcement Learning for Long-Term Physical Activity Maintenance: Using Prior Data to Inform Future Deployment》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Digital health interventions can provide scalable, personalized support for physical activity (PA), yet sustaining PA over the long-term remains difficult. Because affective experiences with PA are important for activity sustainment, we developed an online reinforcement learning (RL) system for the forthcoming ADAPT factorial trial that personalizes twice-daily activity suggestions aimed at improving affective associations with PA. This setting poses several challenges: participant-specific data are scarce relative to the candidate state space, important states and rewards are partially observed, interventions are frequent while the primary outcome is measured weekly, and activity suggestions can both improve PA-related experiences and increase intervention burden. We address these challenges using an expert-specified causal directed acyclic graph as an integrated RL design tool, guiding state construction, estimation of partially observed states, delayed credit assignment, and representation of beneficial and adverse intervention pathways. We further construct a longitudinal simulator calibrated from a prior micro-randomized trial to compare candidate RL designs under realistic state evolution, missingness, and participant heterogeneity before deployment. Together, this work illustrates how causal domain knowledge and prior trial data can make long-horizon, participant-specific RL more practical for digital health interventions targeting sustained behavior change.

</details>

---

### [[20_Research/Papers/强化学习/Calibrated_for_Which_Policy_Conformal_Uncertainty_for_Fixed_World_Models_Under_Intervention|Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention]]

![[assets/2610.35877_first_page.png|800]]

- **arXiv**: [2610.35877](https://arxiv.org/abs/2610.35877)
- **PDF**: https://arxiv.org/pdf/2610.35877
- **详细分析**: [[20_Research/Papers/强化学习/Calibrated_for_Which_Policy_Conformal_Uncertainty_for_Fixed_World_Models_Under_Intervention|Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention]]
- **作者**: Ayush Mittal, Dhruv Gupta
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Changing a deployment policy can invalidate a world model's uncertainty while leaving the physical transition mechanism and predictor unchanged. For one-step prediction, if source and target laws share the conditional mechanism $P(Y|X)=Q(Y|X)$, then the intervention is identified by the pre-outcome change of measure $w(X)=dQ_X/dP_X$. For policy-controlled dynamics this ratio factors into state-occupancy and action-propensity terms. Weighted conformal calibration transports marginal coverage to the target law; with an estimated ratio $\hat w$, $P_Q\{Y \in C_{\hat w}(X)\} \ge 1-α-TV(Q,\hat Q) \ge 1-α-E_P|w-\hat w|$. Population log-loss regret for a source-versus-target domain classifier bounds the same ratio error. If $h$ is its clipped target posterior, $ρ$ is the target-domain prior, and $Δ(h)$ is population log-loss regret, then $E_P|w-\hat w_h| \le (1/(ργ))\sqrt{Δ(h)/2}$. An exact cancellation improves the dependence from a generic odds-map bound of order $γ^{-2}$ to $(ργ)^{-1}$. Our experiments use a released DINO-feature world model and physical Franka trajectories. Under the strongest controlled state-action shift, ordinary 90% conformal sets cover 55.0%, whereas oracle and learned-ratio calibration cover 91.0% and 90.9%. The learned surrogate remains within 0.9% total variation of the target law. Calibration is relative to the deployment law: the model can remain fixed while calibration follows the intervention. We machine-check in Lean 4 the finite-support algebraic and causal identities used in the classifier-regret argument, including its coverage-composition step.

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Exploit_Passive_Dynamics_for_Energy-Efficient_Target_Hopping_of_a_Spring-Legged_Quadcopter|Learning to Exploit Passive Dynamics for Energy-Efficient Target Hopping of a Spring-Legged Quadcopter]]

![[assets/2609.15447_figure.png|800]]

- **arXiv**: [2609.15447](https://arxiv.org/abs/2609.15447)
- **PDF**: https://arxiv.org/pdf/2609.15447
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Exploit_Passive_Dynamics_for_Energy-Efficient_Target_Hopping_of_a_Spring-Legged_Quadcopter|Learning to Exploit Passive Dynamics for Energy-Efficient Target Hopping of a Spring-Legged Quadcopter]]
- **作者**: Ruigang Chen, Qi Zhang, Zhicheng Zhong, Zhuorui Yun, Yizhar Or, Mingyi Liu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning to Exploit Passive Dynamics for Energy-Efficient Target Hopping of a Spring-Legged Quadcopter》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RSL-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Combining aerial thrust with spring-loaded hopping makes monopedal quadcopters promising for locomotion over complex terrain, but heuristic proportional-integral-derivative (PID) tuning limits coordination between active thrust and passive contact dynamics. We present a direct estimated-state-to-motor Proximal Policy Optimization (PPO) policy that commands four motors without an explicit hopping state machine or low-level attitude PID. Its reward combines Energy-Manifold Shaping for mass-normalized vertical-energy tracking and apex-state anchoring with Efficiency Shaping, which uses a history-aware power estimator to penalize general power use, impose an additional airborne-power cost, and penalize airborne near-stationarity. In representative hardware runs, the PPO-based control stack reduced cycle-averaged measured electrical power by 30.7% and mean total normalized thrust by 49.8% relative to the tuned PID-based control stack, while retaining repeatable commanded-height hopping and more concentrated landings. These observations are consistent with improved use of passive dynamics and reduced measured electrical demand.

</details>

---
