# cs.LG | Machine Learning | 2026-08-12

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/Efficient_Hypergradient_Descent_for_Inverse_Reinforcement_Learning|Efficient Hypergradient Descent for Inverse Reinforcement Learning]]

![[assets/2608.11052_figure.png|800]]

- **arXiv**: [2608.11052](https://arxiv.org/abs/2608.11052)
- **PDF**: https://arxiv.org/pdf/2608.11052
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_Hypergradient_Descent_for_Inverse_Reinforcement_Learning|Efficient Hypergradient Descent for Inverse Reinforcement Learning]]
- **作者**: Nikita Sevriukov, Anna Barabanova, Uliana Gagarina, Karina Ivanova, Sofiia Kasaeva, Ilya Levin, Marina Sheshukova
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Efficient Hypergradient Descent for Inverse Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL, ML-IRL, PARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inverse reinforcement learning (IRL) aims to recover a reward function under which the resulting policy reproduces the behavior observed in expert demonstrations. A natural approach is to formulate IRL as a bilevel optimization problem, in which the inner level corresponds to policy optimization under the learned reward and the outer level measures the discrepancy between the induced policy and expert data. However, this formulation is computationally challenging in practice because the outer update requires a hypergradient involving an inverse-Hessian-vector product for the inner objective. We address this challenge by showing that, at the inner optimum, the Hessian of the inner objective is proportional to the Fisher information matrix of the policy, yielding a structured Fisher-based hypergradient closely related to Natural Hypergradient Descent. To address the resulting scalability bottleneck associated with large Fisher matrices, we approximate the required inverse-Fisher-vector product using a streaming spectral sketch, avoiding explicit construction of the Fisher matrix. We evaluate our approach against a first-order stochastic bilevel baseline across discrete- and continuous-control environments. The results demonstrate competitive policy performance and strong reward-ranking quality, while Fisher sketching reduces curvature-storage complexity and can improve computational efficiency relative to an explicit Fisher solver.

</details>

---

### [[20_Research/Papers/强化学习/Threshold_Structure_of_Optimal_Policies_in_Restart_POMDPs|Threshold Structure of Optimal Policies in Restart POMDPs]]

![[assets/2608.10936_first_page.png|800]]

- **arXiv**: [2608.10936](https://arxiv.org/abs/2608.10936)
- **PDF**: https://arxiv.org/pdf/2608.10936
- **详细分析**: [[20_Research/Papers/强化学习/Threshold_Structure_of_Optimal_Policies_in_Restart_POMDPs|Threshold Structure of Optimal Policies in Restart POMDPs]]
- **作者**: Konstantin Avrachenkov, Alexey Piunovskiy, Yi Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Threshold Structure of Optimal Policies in Restart POMDPs》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study a Restart POMDP (Partially Observable Markov Decision Process) on a general Borel state space, where the controller either lets the hidden state evolve unobserved or restarts the system and observes the new state. Exploiting a sufficient-statistic representation consisting of the last observed state and the elapsed time since restart, we reduce the problem to a fully observed MDP. Under a natural one-step cost deterioration condition, we prove that optimal policies have a threshold structure in the elapsed time for both the discounted and total undiscounted cost criteria. When the state space is partially ordered and the kernel is stochastically monotone, we further show that the optimal threshold is nonincreasing in the state. For the average cost criterion, under additional assumptions of geometric ergodicity and domination of the transient gain, we establish analogous threshold results via the vanishing discount approach, after showing the uniform boundedness of the optimal thresholds and relative value functions.

</details>

---

### [[20_Research/Papers/强化学习/Partially_Observable_Learning_for_Multi-Platform_Dispatch_Optimization|Partially Observable Learning for Multi-Platform Dispatch Optimization]]

![[assets/2608.10897_figure.png|800]]

- **arXiv**: [2608.10897](https://arxiv.org/abs/2608.10897)
- **PDF**: https://arxiv.org/pdf/2608.10897
- **详细分析**: [[20_Research/Papers/强化学习/Partially_Observable_Learning_for_Multi-Platform_Dispatch_Optimization|Partially Observable Learning for Multi-Platform Dispatch Optimization]]
- **作者**: Fengming Yao, Man Luo
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Partially Observable Learning for Multi-Platform Dispatch Optimization》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instant delivery platforms have become a critical component of urban logistics, increasingly relying on crowdsourced couriers to fulfill highly dynamic orders. In real-world systems, couriers are not exclusive to a single platform and may concurrently serve multiple platforms, while each platform can only observe its own orders and couriers' interactions due to privacy and operational constraints. This results in a multi-platform dispatch environment with inherent partial observability. However, most existing works on dispatch optimization assume full courier observability and mandatory assignment acceptance, causing substantial performance degradation when deployed in realistic multi-platform settings. In this paper, we propose POLO, a partially observable multi-agent reinforcement learning framework for dispatching optimization in multi-platform instant delivery systems. POLO firstly models each platform-grid pair as an independent agent that learns dispatch policies solely from platform-local observations, aligning the learning process with real-world privacy and operational constraints. To support effective decision-making under incomplete and heterogeneous courier information, POLO introduces a novel attention-based policy representation that selectively aggregates inter-courier information. Moreover, we design a counterfactual reward shaping mechanism to mitigate the non-stationarity induced by joint actions across grids, leading to more stable and scalable learning. We develop a high-fidelity simulator to evaluate dispatch performance under varying numbers of platforms and system scales. Extensive experiments demonstrate that POLO consistently outperforms strong baselines in terms of platform revenue and courier travel efficiency, highlighting its robustness and effectiveness in realistic multi-platform settings.

</details>

---

### [[20_Research/Papers/大模型/MoE_Proxy_Models_for_Low-Cost_Failure_Reproduction_and_Diagnosis_in_LLM_RL_Post-Training|MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training]]

![[assets/2608.10823_figure.png|800]]

- **arXiv**: [2608.10823](https://arxiv.org/abs/2608.10823)
- **PDF**: https://arxiv.org/pdf/2608.10823
- **详细分析**: [[20_Research/Papers/大模型/MoE_Proxy_Models_for_Low-Cost_Failure_Reproduction_and_Diagnosis_in_LLM_RL_Post-Training|MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training]]
- **作者**: Yikai Wang, Chuansai Zhou, Yuhang Zhou, Weiqiang Wu, Cong Wu, Yue Deng, Ben Feng, Mingming Zhu, Beirong Zhou, Zhibin Wang, Sheng Zhong, Chen Tian...
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead. In practice, factors such as framework adaptation, numerical precision, and operator implementation can cause failures, including gradient overflow and loss divergence. Reproducing such failures directly on large models requires considerable time and computational resources. This paper systematically analyzes failures encountered during large-scale RL training on the Huawei Ascend platform, summarizes representative failure types, and identifies three model-side factors relevant to fault reproduction. Based on these factors, we propose a proxy-model construction method for low-cost fault investigation and auxiliary diagnosis. It employs structure-preserving, clustering-based expert pruning to select representative experts while retaining the model's backbone architecture, routing mechanism, and basic task capabilities. Our experimental results show that the proxy models reduce accelerator requirements by 50%-87.5% and achieve up to a 33.3x reduction in per-step NPU-hour cost, while preserving major training dynamics and reproducing fault responses consistent with the original models. Overall, the proxy models can serve as low-cost surrogates for fault reproduction, targeted validation, and auxiliary diagnosis in RL post-training.

</details>

---

### [[20_Research/Papers/强化学习/IADD-TR_Intervention-Aware_Dynamics_Decoupling_with_Targeted_Regularization_for_Model-Based_Reinforcement_Learning|IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning]]

![[assets/2608.10634_figure.png|800]]

- **arXiv**: [2608.10634](https://arxiv.org/abs/2608.10634)
- **PDF**: https://arxiv.org/pdf/2608.10634
- **详细分析**: [[20_Research/Papers/强化学习/IADD-TR_Intervention-Aware_Dynamics_Decoupling_with_Targeted_Regularization_for_Model-Based_Reinforcement_Learning|IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning]]
- **作者**: Zefeng Liang, Jie Qiao, Ruichu Cai, Weilin Chen, Zhifeng Hao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.32（加权：强化学习 1.16，世界模型 1.16）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《IADD-TR: Intervention-Aware Dynamics Decoupling with Targeted Regularization for Model-Based Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning (MBRL), which learns environment dynamics to generate synthetic experience, is a promising approach to sample-efficient decision making. Numerous methods have been developed to improve dynamics prediction and policy optimization for MBRL through uncertainty estimation, model regularization, and conservative value learning. However, these methods typically treat the transition model and critic as monolithic predictors, overlooking the policy-induced data bias. Consequently, action can become entangled with environmental evolution, while uneven action coverage may distort the counterfactual value estimates used for policy improvement. To address this, we propose IADD-TR, a unified framework combining Intervention-Aware Dynamics Decoupling (IADD) and Targeted Regularization (TR). IADD factorizes transitions into an action-intervention stage and an action-free natural evolution stage, using a zero-action anchor to resolve the non-uniqueness of this two-stage factorization for robust generalization. Its latent and state-aligned components are identifiable up to an invertible within-block transformation and pointwise, respectively. For policy learning, we derive TR from the efficient influence function of a replay-state policy-gradient functional. TR augments the critic with an action-density-scaled residual correction and optimizes a targeted loss, yielding doubly robust policy-gradient estimation when either the critic or the replay action density is consistently specified. Extensive experiments on five MuJoCo tasks show that IADD-TR achieves competitive returns with improved sample efficiency.

</details>

---

### [[20_Research/Papers/大模型/ProbGuard_Calibrated_Safety_Risk_Estimation_from_LLM_Output_Distributions|ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions]]

![[assets/2608.10621_figure.png|800]]

- **arXiv**: [2608.10621](https://arxiv.org/abs/2608.10621)
- **PDF**: https://arxiv.org/pdf/2608.10621
- **详细分析**: [[20_Research/Papers/大模型/ProbGuard_Calibrated_Safety_Risk_Estimation_from_LLM_Output_Distributions|ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions]]
- **作者**: Xinzhe Huang, Biwu Yao, Kedong Xiu, Mengnan Zhao, Di Wang, Puning Zhao, Tianhang Zheng
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CalibEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent research on Large Language Model (LLM) safety has widely adopted guardrails to identify unsafe LLM outputs. Existing guardrails typically formulate safety assessment as a deterministic classification task, mapping a discrete token sequence to a discrete safety label. However, this paradigm has two limitations: First, safety assessment is inherently an uncertain problem, particularly during the early generation state. Second, relying solely on discrete token sequences discards the rich probabilistic information embedded in the LLM output distribution. To address these limitations, we propose the first completely probabilistic architecture-agnostic guardrail \textsc{ProbGuard} to leverage the LLM early output distributional signals for estimating and calibrating the safety probability, thereby enabling early stopping of unsafe ongoing outputs. Specifically, given an LLM's generated prefix distribution, we formulate the safety risk as the unsafe probability of its continued generation dynamics and estimate this risk by Monte-Carlo sampling. Through post-training on the distributional signals and calibrated safety risk, \textsc{ProbGuard} achieves the best calibration performance across all nine model--dataset combination settings, reducing the average Brier score and ECE by 79.6\% and 71.9\%, respectively, over the best baseline. \textsc{ProbGuard} further limits the attack success rate to at most 1\% across six representative jailbreak attacks after observing the LLM early output distributions from only the first ten decoding steps.

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_LLM-Guided_Control-Plane_Policies_for_Backend_Fault_Isolation_in_HAProxy|Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy]]

![[assets/2608.10532_figure.png|800]]

- **arXiv**: [2608.10532](https://arxiv.org/abs/2608.10532)
- **PDF**: https://arxiv.org/pdf/2608.10532
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_LLM-Guided_Control-Plane_Policies_for_Backend_Fault_Isolation_in_HAProxy|Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy]]
- **作者**: Aman Chauhan, Vishnu Pendyala
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, LLNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes. We ask whether a Large Language Model can replace the static routing policy itself, reading HAProxy and Prometheus telemetry every 10 seconds and isolating faulty servers through guardrailed calls to the HAProxy Data Plane API. On a reproducible benchmark with a persistent structural fault built into roughly one-third of a heterogeneous fleet, we sweep 15 open-weight models across five families (0.35B to 35B total parameters; dense, mixture-of-experts, and efficient-sparse architectures), reasoning modes, fleet scales of 3 to 9 backends, and two routing algorithms, totaling 240 runs. We find a capability threshold near 3B active parameters. Below it, LLM policies are typically unreliable and sometimes worse than no policy; above it, every model, regardless of architecture, saturates near an 88% reduction in client-perceived 5xx errors over the static baseline. The threshold is approximate: Gemma 4 E2B clears it with 2B active parameters, while the dense 3B Granite 4.0 Micro does not. The availability gain has costs. Draining concentrates load onto surviving servers, inflating tail latency 2.6 to 2.8 times, and enabling reasoning multiplies token spend roughly tenfold, overrunning the control interval and degrading effectiveness. The efficient operating point is a supra-threshold model in its cheapest non-reasoning mode, wrapped inside deterministic guardrails.

</details>

---

### [[20_Research/Papers/强化学习/Dreamer-SAC_Off-Policy_Learning_in_Latent_World_Models_for_Sample-Efficient_Autonomous_Driving|Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving]]

![[assets/2608.10386_figure.png|800]]

- **arXiv**: [2608.10386](https://arxiv.org/abs/2608.10386)
- **PDF**: https://arxiv.org/pdf/2608.10386
- **详细分析**: [[20_Research/Papers/强化学习/Dreamer-SAC_Off-Policy_Learning_in_Latent_World_Models_for_Sample-Efficient_Autonomous_Driving|Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving]]
- **作者**: Jiazhuo Li, Linjiang Cao, Qi Liu, Xi Xiong
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 2.72（加权：强化学习 0.76，世界模型 1.96）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Dreamer-SAC: Off-Policy Learning in Latent World Models for Sample-Efficient Autonomous Driving》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sample-efficient reinforcement learning for autonomous driving is often limited by the trade-off between data efficiency and model bias. While world models reduce the reliance on costly environment interactions, policy optimization over learned dynamics remains sensitive to prediction errors. This paper proposes the Dreamer-SAC framework, which integrates a recurrent state-space world model with an off-policy soft actor-critic algorithm trained directly in latent space. The framework uses a combination of real interactions and short-horizon generated trajectories with n-step target estimation and multi-objective supervision. Evaluated in autonomous driving scenarios with objectives encompassing driving efficiency and safety, the proposed framework consistently outperforms representative reinforcement learning baselines, including DreamerV3, SAC, and PPO, while achieving improved performance with substantially fewer real environment interactions. Experiments reveal an inverted-U relationship between rollout horizon and policy performance, where short-horizon latent rollouts achieve the best trade-off between additional training signals and accumulated model bias. Furthermore, n-step target estimation demonstrates more effectiveness over one-step temporal-difference targets in exploiting predicted experience for value learning.

</details>

---

### [[20_Research/Papers/强化学习/Topological_Feasibility_Guarantees_for_Differentiable_Predictive_Control|Topological Feasibility Guarantees for Differentiable Predictive Control]]

![[assets/2608.10332_figure.png|800]]

- **arXiv**: [2608.10332](https://arxiv.org/abs/2608.10332)
- **PDF**: https://arxiv.org/pdf/2608.10332
- **详细分析**: [[20_Research/Papers/强化学习/Topological_Feasibility_Guarantees_for_Differentiable_Predictive_Control|Topological Feasibility Guarantees for Differentiable Predictive Control]]
- **作者**: Guangyu Wu, Ján Drgoňa
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Topological Feasibility Guarantees for Differentiable Predictive Control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Differentiable predictive control (DPC), a self-supervised learning approach for approximating explicit model predictive control (MPC) policies, offers significant computational advantages over online optimization-based MPC. However, feasibility guarantees, a core requirement for safe control, are currently provided either probabilistically or via online safety filters. The lack of rigorous feasibility guarantees for offline policy optimization remains an open problem. This paper establishes deterministic feasibility guarantees for DPC using a novel topological analysis of the induced reachable safe set, without requiring online safety filters. By exploiting the inherent model-based nature of DPC, in which differentiable system dynamics are embedded directly into the computational graph, we analyze the properties of the learned control policies and the corresponding system states from topological and geometric perspectives. Inspired by our theoretical analysis, we propose a novel self-supervised offline policy learning strategy that utilizes a proxy loss with Control Barrier Functions (CBFs). Crucially, these properties not only significantly improve policy training but also enable the derivation of strict, deterministic feasibility guarantees from a finite number of training samples. Extensive closed-loop simulations validate our theoretical findings, demonstrating that the empirical constraint violations monotonically decrease to zero as the training sample size increases. Ultimately, this work illustrates that DPC policy optimization yields formal safety certificates that are structurally unattainable with conventional black-box methods, e.g., reinforcement learning (RL) or supervised learning-based approximate MPC, thereby providing a new perspective on feasibility guarantees in learning-based control.

</details>

---

### [[20_Research/Papers/具身智能/Boundary-Seeking_Policy_Gradient_for_Safe_Reinforcement_Learning|Boundary-Seeking Policy Gradient for Safe Reinforcement Learning]]

![[assets/2608.10204_figure.png|800]]

- **arXiv**: [2608.10204](https://arxiv.org/abs/2608.10204)
- **PDF**: https://arxiv.org/pdf/2608.10204
- **详细分析**: [[20_Research/Papers/具身智能/Boundary-Seeking_Policy_Gradient_for_Safe_Reinforcement_Learning|Boundary-Seeking Policy Gradient for Safe Reinforcement Learning]]
- **作者**: Chenhua Fan, Jiahui Zhu, Yuhang Zhang, Honghao Wei
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Boundary-Seeking Policy Gradient for Safe Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe reinforcement learning maximizes reward subject to safety constraints. For Constrained Markov Decision Processes, the linear-programming view over occupancy measures implies that whenever the constraint is active at optimality, the optimal policy lies exactly on the constraint boundary, yet standard gradient-based methods do not exploit this structure and often settle in the feasible interior. We introduce Boundary-Seeking Policy Gradient (BSPG), a first-order method whose update combines a tangential component that improves reward while preserving cost to first order with a signed, residual-driven normal component that regulates the policy toward the active boundary from either side; the combined direction admits an algebraic Lagrangian form with an induced coefficient and no learned dual variable. Under exact gradients and stated regularity conditions, the constraint residual converges to zero from either side with a finite-horizon $O(1/\sqrt{T})$ bound, the tangential component is a reward-ascent direction on the boundary, and any convergent parameter sequence is stationary on the active constraint set, satisfying the KKT conditions when the limit is also a local maximizer over the feasible set. This complements existing analyses, which certify feasibility but do not characterize the constraint value at convergence. On a standard Safety-Gymnasium navigation task, BSPG attains higher reward while tracking the boundary more tightly than the compared baselines.

</details>

---

### [[20_Research/Papers/强化学习/An_adaptive_and_evolvable_deep_reinforcement_learning_framework_for_weather_prediction|An adaptive and evolvable deep reinforcement learning framework for weather prediction]]

![[assets/2608.09948_figure.png|800]]

- **arXiv**: [2608.09948](https://arxiv.org/abs/2608.09948)
- **PDF**: https://arxiv.org/pdf/2608.09948
- **详细分析**: [[20_Research/Papers/强化学习/An_adaptive_and_evolvable_deep_reinforcement_learning_framework_for_weather_prediction|An adaptive and evolvable deep reinforcement learning framework for weather prediction]]
- **作者**: Qiang Wu, Han Li, Jianping Huang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《An adaptive and evolvable deep reinforcement learning framework for weather prediction》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, FourCastNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

No single AI weather model excels at all variables, pressure levels, and lead times. Rather than building yet another architecture, we reframe the forecasting problem as one of coordination. Here we present Feitian Adaptive Ensemble Weather (FTAE-Weather), a lightweight framework that learns, through deep reinforcement learning, when and where to trust each member of an open pool of pretrained forecasters. A tactical Weight-Agent reads the current atmospheric state and assigns variable- and horizon-specific fusion weights, while a strategic Evolve-Agent periodically prunes underperforming models and absorbs newly released ones. Asynchronous prediction caching keeps training cost independent of the slowest constituent model. Adding fewer than 0.01 percent extra parameters, FTAE-Weather reduces RMSE by from 17.2 percent to 78.3 percent over the best individual model in 10 atmospheric variables and outperforms conventional ensemble baselines across lead times from 72 to 360 hours. The framework thus converts a growing, fragmented inventory of specialist models into a single prediction system that strengthens as the field of AI weather forecasting releases new architectures-turning model diversity from a coordination challenge into a compounding scientific advantage.

</details>

---
