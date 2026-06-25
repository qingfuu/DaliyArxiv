# cs.AI | Artificial Intelligence | 2026-06-23

#arxiv #ComputerScience

**论文数**: 21

### [[20_Research/Papers/具身智能/CoorDex_Coordinating_Body_and_Hand_Priors_for_Continuous_Dexterous_Humanoid_Loco-Manipulation|CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation]]

![[assets/2606.23680_figure.png|800]]

- **arXiv**: [2606.23680](https://arxiv.org/abs/2606.23680)
- **PDF**: https://arxiv.org/pdf/2606.23680
- **详细分析**: [[20_Research/Papers/具身智能/CoorDex_Coordinating_Body_and_Hand_Priors_for_Continuous_Dexterous_Humanoid_Loco-Manipulation|CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation]]
- **作者**: Sikai Li, Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.92（加权：具身智能 3.3，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

</details>

---

### [[20_Research/Papers/具身智能/RECALL_Recovery_Experience_Collection_for_Active_Lifelong_Learning_in_Vision-Language-Action_Models|RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models]]

![[assets/2606.23617_figure.png|800]]

- **arXiv**: [2606.23617](https://arxiv.org/abs/2606.23617)
- **PDF**: https://arxiv.org/pdf/2606.23617
- **详细分析**: [[20_Research/Papers/具身智能/RECALL_Recovery_Experience_Collection_for_Active_Lifelong_Learning_in_Vision-Language-Action_Models|RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models]]
- **作者**: Ulas Berk Karli, Tesca Fitzgerald
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation learning, where additional demonstrations are collected for tasks where the policy performs poorly. This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. In this paper, we propose an active, continual learning paradigm for VLAs. We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations. However, we also find that fine-tuning only on actively-collected recovery data leads to catastrophic forgetting. We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. Overall, our work contributes an empirical study of active continual learning for autoregressive VLAs, establishing that uncertainty-guided recovery demonstrations can improve adaptation efficiency while also revealing open challenges when targeted new data is incorporated into large robot policies.

</details>

---

### [[20_Research/Papers/大模型/Dynamic_multi-agent_deep_reinforcement_learning-based_pricing_and_incentivization_approach_in_multimodal_transportation_networks|Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks]]

![[assets/2606.23257_figure.png|800]]

- **arXiv**: [2606.23257](https://arxiv.org/abs/2606.23257)
- **PDF**: https://arxiv.org/pdf/2606.23257
- **详细分析**: [[20_Research/Papers/大模型/Dynamic_multi-agent_deep_reinforcement_learning-based_pricing_and_incentivization_approach_in_multimodal_transportation_networks|Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks]]
- **作者**: Khadidja Kadem, Mostafa Ameli, Carlos Lima Azevedo, Mahdi Zargayouna, Latifa Oukhellou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.82（加权：大模型 0.9，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MATSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In multimodal transportation systems, shared mobility services (SMSs) are promoted for their potential to enhance flexibility and reduce congestion. However, SMS demand is often concentrated in high-density areas, which can limit the effectiveness and accessibility for various commuter groups. This uneven integration challenges transportation system efficiency, especially in terms of emissions and spatial equity. Addressing these issues requires coordination among multiple stakeholders whose objectives frequently conflict. Whereas authorities aim to ensure sustainable and equitable mobility, SMS providers focus on revenue maximization, and travelers seek to minimize personal travel costs. This paper proposes a multi-agent deep reinforcement learning framework that captures these interactions through dynamic pricing and incentivization strategies for SMSs and public transport. The framework integrates two reinforcement learning (RL) agents: (i) a public authority that allocates spatio-temporal public transport incentives to improve equity, emissions, and efficiency, and (ii) an SMS provider that dynamically adjusts fares to optimize revenue. The agents interact with the transportation system and adapt strategies in response to evolving demand, congestion, and network conditions. Numerical experiments conducted over a three-hour morning peak period show that dynamic incentivization effectively reduces congestion peaks, lowers commuters' costs by around 20% and emissions by approximately 10%, while nearly doubling public transport profit and supporting a more equitable distribution of benefits. When combined with dynamic SMS pricing, the two RL agents demonstrate the ability to balance conflicting objectives between private providers and public authorities. The proposed approach provides a decision-support tool for sustainable and equitable multimodal mobility planning.

</details>

---

### [[20_Research/Papers/具身智能/AdaReP_Adaptive_Re-Planning_under_Model_Mismatch_for_Neural_World-Model_Predictive_Control|AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control]]

![[assets/2606.23079_figure.png|800]]

- **arXiv**: [2606.23079](https://arxiv.org/abs/2606.23079)
- **PDF**: https://arxiv.org/pdf/2606.23079
- **详细分析**: [[20_Research/Papers/具身智能/AdaReP_Adaptive_Re-Planning_under_Model_Mismatch_for_Neural_World-Model_Predictive_Control|AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control]]
- **作者**: Yutian Cheng, Xiaojian Ma, Xianhao Wang, Min Yang, Rongpeng Su, Hangxin Liu, Xi Chen, Shuai Li, Qing Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 0.6，世界模型 0.4，机器人 0.7）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《AdaReP:Adaptive Re-Planning under Model Mismatch for Neural World-Model Predictive Control》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlaNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neural world models coupled with model predictive control (MPC) replan at every environment step to bound accumulated prediction error, but this incurs substantial computational overhead. Reusing a cached plan reduces this overhead, yet its effectiveness depends on how prediction mismatch propagates through the local dynamics. We analyze this trade-off with a perturbation-based dynamic-regret framework and show that stale-plan penalties scale with the reuse tolerance, the accumulated mismatch since the last replanning step, and the local dynamics sensitivity. Based on this structure, we propose AdaReP, a training-free wrapper that adapts the replanning tolerance online using the current deviation from the cached rollout and a local sensitivity estimate, without modifying the learned world model or planner. Across image-space planning, latent-space control, and real-world robotic manipulation, AdaReP substantially reduces planner-side computation while maintaining comparable task performance, including over 80% fewer queries on a 50-trial physical robot study.

</details>

---

### [[20_Research/Papers/大模型/EvoRubrics_Dynamic_Rubrics_as_Rewards_via_Adversarial_Co-Evolution_for_LLM_Reinforcement_Learning|EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning]]

![[assets/2606.23038_figure.png|800]]

- **arXiv**: [2606.23038](https://arxiv.org/abs/2606.23038)
- **PDF**: https://arxiv.org/pdf/2606.23038
- **详细分析**: [[20_Research/Papers/大模型/EvoRubrics_Dynamic_Rubrics_as_Rewards_via_Adversarial_Co-Evolution_for_LLM_Reinforcement_Learning|EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning]]
- **作者**: Hongxin Ding, Baixiang Huang, Yue Fang, Weibin Liao, Zheng Li, Jinyang Zhang, Zhijing Wu, Junfeng Zhao, Yasha Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rubric-based rewards offer interpretable and fine-grained optimization signals for reinforcement learning in open-ended tasks where verifiable answers are unavailable. However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. Recent dynamic rubric methods partially address this but rely on external frontier models or ground-truth answers, and update rubrics only at coarse granularity. We propose EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator jointly improve through adversarial interaction within each training step. As the policy improves under the rubric generator's guidance, the rubric generator adapts its criteria to remain discriminative and informative, enabling evaluation to track the policy in real time and naturally inducing an automatic curriculum. Experiments show that EvoRubrics consistently outperforms static and dynamic rubric baselines across benchmarks. The learned Rubric Generator further generalizes as a transferable reward model. Notably, even a fully self-supervised variant without any external supervision achieves meaningful gains, suggesting that co-evolution between generation and evaluation alone can provide sufficiently rich learning signals. Our code is publicly available at https://anonymous.4open.science/r/EvoRubrics-2155/.

</details>

---

### [[20_Research/Papers/强化学习/Group-Graph_Policy_Optimization_for_Long-Horizon_Agentic_Reinforcement_Learning|Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning]]

![[assets/2606.22995_figure.png|800]]

- **arXiv**: [2606.22995](https://arxiv.org/abs/2606.22995)
- **PDF**: https://arxiv.org/pdf/2606.22995
- **详细分析**: [[20_Research/Papers/强化学习/Group-Graph_Policy_Optimization_for_Long-Horizon_Agentic_Reinforcement_Learning|Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning]]
- **作者**: Yunan Wang, Minghui Song, Zihan Zhang, Shaohan Huang, Haizhen Huang, Furu Wei, Weiwei Deng, Feng Sun, Qi Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.17（加权：大模型 0.25，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, AlfWorld, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-based Reinforcement Learning (RL) has significantly enhanced Large Language Models (LLMs) in agentic scenarios. To achieve finer-grained policy updates, recent agentic RL frameworks have shifted from trajectory-level to step-level training. However, long-horizon agentic RL suffers from severe reward sparsity and delay, as feedback is often deferred for dozens of interaction steps. While existing step-level frameworks refine training granularity, their credit assignment remains coarse-grained and still treats agent exploration as isolated, linear trajectories. This oversimplified perspective ignores the inherent graph structure of state transitions, leading to high-variance state-value estimation and myopic, localized credit assignment. To overcome these critical bottlenecks, we propose Group-Graph Policy Optimization (G2PO), a novel group-based RL algorithm tailored for multi-turn agentic tasks. G2PO explicitly transforms linear interaction trajectories into a global state-transition graph. By aggregating identical observations across different trajectories, we introduce group-aggregation state-value estimation that reduces sampling variance and trajectory-dependent bias. Furthermore, we redefine agent actions as transitions between state nodes and propose an edge-centric advantage estimation strategy. By globally standardizing Temporal Difference (TD) errors across the entire graph, G2PO explicitly identifies and prioritizes critical transitions that drive absolute task progress. Extensive experiments on representative long-horizon benchmarks-WebShop, ALFWorld, and AppWorld-demonstrate that G2PO substantially outperforms state-of-the-art prompt-based and RL baselines, achieving remarkable success rate improvements of up to 22.2% over GRPO.

</details>

---

### [[20_Research/Papers/具身智能/Self-Evolving_Cognitive_Framework_via_Causal_World_Modeling_for_Embodied_Scientific_Intelligence|Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence]]

![[assets/2606.22449_figure.png|800]]

- **arXiv**: [2606.22449](https://arxiv.org/abs/2606.22449)
- **PDF**: https://arxiv.org/pdf/2606.22449
- **详细分析**: [[20_Research/Papers/具身智能/Self-Evolving_Cognitive_Framework_via_Causal_World_Modeling_for_Embodied_Scientific_Intelligence|Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence]]
- **作者**: Yi Yu, Tetsunari Inamura
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，世界模型 0.4，机器人 0.3）
- **关联关键词**: EmbodiedAI, WorldModel

#### 研究背景与动机

《Self-Evolving Cognitive Framework via Causal World Modeling for Embodied Scientific Intelligence》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current embodied world models are primarily optimized for predictive objectives, limiting their ability to generalize under distribution shifts and reason systematically about unseen situations and hypothetical interventions. We argue that embodied intelligence should move beyond predictive world modeling toward self-evolving cognitive systems that continually construct and refine internal causal representations through interaction with the environment. To this end, we propose a self-evolving cognitive framework via causal world modeling for embodied scientific intelligence, which integrates three complementary components: causal world modeling, intervention-driven causal reasoning, and continual cognitive refinement. The proposed framework continuously revises and expands its internal causal world model through causal discovery, intervention-driven feedback, and counterfactual reasoning, supporting continual cognitive refinement and enabling cognition itself to evolve over time. Furthermore, we reinterpret embodied interaction not merely as a means of trajectory optimization, but as an epistemic process for causal hypothesis generation, intervention-driven experimentation, and continual knowledge acquisition. This work provides a conceptual and theoretical foundation for a transition from predictive intelligence toward epistemic intelligence, in which intelligence emerges through the continual construction, revision, and refinement of causal world models via interaction with the environment. Accordingly, an intervention-driven causal-epistemic benchmarking paradigm is suggested for evaluating self-evolving embodied scientific intelligence.

</details>

---

### [[20_Research/Papers/大模型/Reinforcement_learning_to_improve_large_language_model-based_automated_code_compliance_systems|Reinforcement learning to improve large language model-based automated code compliance systems]]

![[assets/2606.22402_figure.png|800]]

- **arXiv**: [2606.22402](https://arxiv.org/abs/2606.22402)
- **PDF**: https://arxiv.org/pdf/2606.22402
- **详细分析**: [[20_Research/Papers/大模型/Reinforcement_learning_to_improve_large_language_model-based_automated_code_compliance_systems|Reinforcement learning to improve large language model-based automated code compliance systems]]
- **作者**: Jack Wei Lun Shi, Minghao Dang, Wawan Solihin, Leong Hien Poh, Justin K. W. Yeoh
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 2.27（加权：大模型 1.15，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reinforcement learning to improve large language model-based automated code compliance systems》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based approaches for automated code compliance (ACC) of building regulations are prone to generating incorrect and hallucinated computer-processable rules. This paper introduces P4IR, a two-stage framework that uses supervised fine-tuning (SFT) to instill domain knowledge in an LLM, followed by Group Relative Policy Optimization (GRPO) to improve the accuracy of the generated intermediate representations in the form of high-level code skeletons. The framework achieved reductions of up to 23.8% and 38.6% in tree edit distance and token-level Levenshtein distance respectively, relative to the SFT baselines. Comparative analysis demonstrates that this approach in a zero-shot setting outperforms leading LLMs in both code structure and semantics, specifically Claude Opus and Sonnet 4.5, GPT-5.2, Qwen-3-Max, and GLM-4.7, evaluated via few-shot prompting. Additionally, the GRPO stage produced a small yet statistically significant reduction in false positives. By combining SFT with GRPO to optimize directly for domain-specific objectives, this approach offers a path toward more accurate and reliable LLM-based ACC systems.

</details>

---

### [[20_Research/Papers/具身智能/Reference-Free_Assessment_of_Physical_Consistency_in_World_Model-based_Video_Generation|Reference-Free Assessment of Physical Consistency in World Model-based Video Generation]]

![[assets/2606.22363_figure.png|800]]

- **arXiv**: [2606.22363](https://arxiv.org/abs/2606.22363)
- **PDF**: https://arxiv.org/pdf/2606.22363
- **详细分析**: [[20_Research/Papers/具身智能/Reference-Free_Assessment_of_Physical_Consistency_in_World_Model-based_Video_Generation|Reference-Free Assessment of Physical Consistency in World Model-based Video Generation]]
- **作者**: Yun Oh, Sukmin Yun
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.16，世界模型 0.76，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《Reference-Free Assessment of Physical Consistency in World Model-based Video Generation》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, WorldEval, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD), our approach utilizes DROID-SLAM and SEA-RAFT to quantify physical inconsistencies, motivated by WorldScore. Videos filtered using our relative consistency assessment show an improvement in task success rates of over 8%, effectively narrowing the simulation-to-reality gap. Furthermore, our absolute assessment enables spatio-temporal localization, providing visualization of when and where physical artifacts occur.

</details>

---

### [[20_Research/Papers/具身智能/Benchmarking_Robot_Memory_Under_Interference|Benchmarking Robot Memory Under Interference]]

![[assets/2606.22338_figure.png|800]]

- **arXiv**: [2606.22338](https://arxiv.org/abs/2606.22338)
- **PDF**: https://arxiv.org/pdf/2606.22338
- **详细分析**: [[20_Research/Papers/具身智能/Benchmarking_Robot_Memory_Under_Interference|Benchmarking Robot Memory Under Interference]]
- **作者**: Soumil Rathi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Benchmarking Robot Memory Under Interference》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment. The robot's tasks may often require it to remember information from multiple sessions ago, making long-context robot memory important for real-world deployments. However, most robot-memory benchmarks today are based on single episodes or a short context. To measure how current robot memory systems perform on longer sessions with more distractions, we introduce RoboMME-Interference, a cross-session benchmark built on RoboMME. For each query episode, we construct a session history using the query's relevant prior demonstration followed by a controlled number of unrelated sessions, which we provide to the VLA as memory and measure accuracy. Running RoboMME's released memory-augmented $π_{0.5}$ variants unmodified through this benchmark, we find that while perceptual memory variants improve success when given the history without any distractors, they decay strongly and steadily as unrelated sessions accumulate. With this release, we emphasize the importance of long-context memory and robustness to interference and show that current systems largely fail on such capabilities. The project page, videos, code, and data are at https://robotmemorybench.com.

</details>

---

### [[20_Research/Papers/世界模型/Nous_A_Predictive_World_Model_for_Long-Term_Agent_Memory|Nous: A Predictive World Model for Long-Term Agent Memory]]

![[assets/2606.22030_first_page.png|800]]

- **arXiv**: [2606.22030](https://arxiv.org/abs/2606.22030)
- **PDF**: https://arxiv.org/pdf/2606.22030
- **详细分析**: [[20_Research/Papers/世界模型/Nous_A_Predictive_World_Model_for_Long-Term_Agent_Memory|Nous: A Predictive World Model for Long-Term Agent Memory]]
- **作者**: Pranav Singh
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel, Systems

#### 研究背景与动机

《Nous: A Predictive World Model for Long-Term Agent Memory》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Nous, a novel agent memory architecture grounded in the principle that knowledge is prediction, not storage. Rather than persisting facts as database records, vector embeddings, or knowledge-graph triples, Nous maintains a predictive world model: a collection of categorical probability distributions, called dimensions, one per entity-attribute pair observed in conversation. Each incoming observation is scored by its information-theoretic surprise S = -log2 P(obs | D), and the distribution is updated via a closed-form Bayesian posterior. The primary stored artifact is the delta, a record of the shift from prior to posterior belief, rather than the fact itself. Forgetting emerges naturally as entropy decay toward the uniform distribution, and identity resolution is handled through mutual information between entity dimension sets. Evaluated on the LoCoMo long-term conversational memory benchmark across ten conversations (1,540 questions) using GPT-4o-mini as backbone, Nous achieves F1 of 63.50 (single-hop), 55.32 (multi-hop), 58.57 (temporal), and 62.50 (open-domain). Against A-MEM's self-reported GPT-4o-mini numbers, Nous shows substantial gains in three of four categories, though we note that independent citations of A-MEM's results disagree with each other on category assignment, a reproducibility issue we discuss openly rather than resolve unilaterally. We additionally compare against BeliefMem, a concurrently developed system built on the same core premise of belief-based rather than deterministic memory; on the same benchmark and backbone, Nous's self-reported numbers exceed BeliefMem's self-reported numbers on all four categories, though we flag several uncontrolled differences between the two evaluation pipelines that prevent this from being a fully controlled comparison. Nous requires no external vector database or graph engine.

</details>

---

### [[20_Research/Papers/大模型/Modularized_Reinforcement_Learning_on_LLMs_From_MDP_Creation_to_Exploration_and_Learning|Modularized Reinforcement Learning on LLMs: From MDP Creation to Exploration and Learning]]

![[assets/2606.21943_figure.png|800]]

- **arXiv**: [2606.21943](https://arxiv.org/abs/2606.21943)
- **PDF**: https://arxiv.org/pdf/2606.21943
- **详细分析**: [[20_Research/Papers/大模型/Modularized_Reinforcement_Learning_on_LLMs_From_MDP_Creation_to_Exploration_and_Learning|Modularized Reinforcement Learning on LLMs: From MDP Creation to Exploration and Learning]]
- **作者**: Zhao Yang, Yuxuan Jiang, Ting-Chih Chen, Lincen Yang, Annie Wong, Chao Gao, Jacob E. Kooi, Zhong Li, Jiayang Shi, Kevin Qiu, Qi Huang, Xinrui Zu...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.22（加权：大模型 0.1，强化学习 1.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Modularized Reinforcement Learning on LLMs: From MDP Creation to Exploration and Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HRL, MARL, Meta-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become central to LLM post-training, yet the methods that dominate current pipelines, PPO and GRPO, represent only a narrow slice of what RL offers. Understanding why these methods prevail, and what alternatives exist, requires a principled examination of the design decisions that underlie any RL algorithm. This survey organizes that examination around three stages of algorithm construction. We begin with MDP creation: how the reward function, state space, action space, termination condition, and discount factor are, or could be, defined for LLM training. We then turn to exploration, covering temperature sampling, entropy regularization, intrinsic motivation, tree search, and curriculum learning. Finally, we address learning along four classical RL dimensions: model-free versus model-based, value-based versus policy-based versus actor-critic, on-policy versus off-policy, and credit assignment, including both Monte Carlo methods, which rely on full return estimates, and bootstrapping methods, which update estimates using other learned predictions. Mapping the LLM literature onto this taxonomy reveals a strikingly non-uniform distribution of research effort. Critic-free policy gradients and Monte Carlo credit assignment are densely populated, while value-based methods, off-policy actor-critic training, and bootstrapping-based credit assignment remain largely unexplored despite well-established counterparts in classical RL. These gaps represent concrete opportunities for transferring proven RL techniques to LLM training. By making these gaps explicit alongside the methods that have proven effective, this survey offers researchers in both RL and LLMs a shared framework for understanding current practice and identifying promising directions for future work.

</details>

---

### [[20_Research/Papers/世界模型/Imitation_from_Heterogeneous_Demonstrations_using_Grounded_Latent-Action_World_Models|Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models]]

![[assets/2606.21672_figure.png|800]]

- **arXiv**: [2606.21672](https://arxiv.org/abs/2606.21672)
- **PDF**: https://arxiv.org/pdf/2606.21672
- **详细分析**: [[20_Research/Papers/世界模型/Imitation_from_Heterogeneous_Demonstrations_using_Grounded_Latent-Action_World_Models|Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models]]
- **作者**: Tianyou Wang, Anson Lei, Joe Watson, Ingmar Posner
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《Imitation from Heterogeneous Demonstrations using Grounded Latent-Action World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning has emerged as a powerful paradigm for learning visuomotor policies, but its generalisation and stability are limited by the scale and quality of demonstration data needed. A promising direction is to leverage more abundant but heterogeneous data sources, which differ in action space and often lack action labels altogether. Existing co-training approaches that combine heterogeneous data sources rely on heuristic and hand-engineered alignment techniques. In contrast, we argue that action representations should be grounded in prediction: actions that produce the same effect on the environment should share the same representation, regardless of their sources. To this end, we instantiate this principle by using a grounded latent-action world model (GLAM), a pair of generative models with a shared latent action space across data sources that is grounded by predicting future observations consistently across sources. This latent action space is used to train downstream behavioural cloning (BC) policies which map observations to latent actions and decode them back to robot actions, providing a paradigm for learning from heterogeneous data. Empirically, we demonstrate that GLAM successfully learns an aligned latent action space that facilitates action transfer across data sources with and without action labels. Across five manipulation tasks in simulation and in the real world, GLAM-aligned policies significantly outperform BC baselines and prior latent-action methods, achieving an average of +48% improvement in task success rate with the same data-scarce setting. Videos and code are available at https://viccccciv.github.io/glam/.

</details>

---

### [[20_Research/Papers/具身智能/Decoupling_the_Declarative_from_the_Procedural_in_Vision-Language-Action_Models|Decoupling the Declarative from the Procedural in Vision-Language-Action Models]]

![[assets/2606.21496_figure.png|800]]

- **arXiv**: [2606.21496](https://arxiv.org/abs/2606.21496)
- **PDF**: https://arxiv.org/pdf/2606.21496
- **详细分析**: [[20_Research/Papers/具身智能/Decoupling_the_Declarative_from_the_Procedural_in_Vision-Language-Action_Models|Decoupling the Declarative from the Procedural in Vision-Language-Action Models]]
- **作者**: Nikolaos Tsagkas, Andreas Sochopoulos, Chris Xiaoxuan Lu, Oisin Mac Aodha, Alexandros Kouris
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Decoupling the Declarative from the Procedural in Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying generalist robotic agents in the real world requires transferable skills. Specifically, a policy trained to clone a behavior from object-specific demonstrations must generalize beyond that object, otherwise data collection requirements become intractable. Recently, fine-tuning of pre-trained billion-parameter Vision-Language Models (VLMs), initially on large-scale robot datasets and then on fewer scenario-specific demonstrations, has emerged as the predominant paradigm for designing Vision-Language-Action (VLA) models. While these policies achieve state-of-the-art manipulation performance in-distribution, they remain brittle to minor spatial, semantic, and task variations. In this work, we address the inability of current models to decouple the declarative (i.e., concepts and entity semantics) from the procedural knowledge (i.e., how to do something) encoded in their parameters, which is a fundamental bottleneck for zero-shot skill transfer to novel objects. To address this, we propose w$^{2}$VLA, a new VLA model with restructured information flow. Rather than feeding all multimodal tokens from the VLM encoder into a large, opaque transformer-based action expert, our approach modulates the robot state sequence with visual, spatial, and skill information in a compositional and interpretable manner. Unlike popular, state-of-the-art VLAs, we show that our modular approach successfully decouples knowledge representations, enabling robust behavior cloning and unprecedented zero-shot skill transfer capabilities across dissimilar, unseen objects.

</details>

---

### [[20_Research/Papers/具身智能/Vesta_A_Generalist_Embodied_Reasoning_Model|Vesta: A Generalist Embodied Reasoning Model]]

![[assets/2606.20905_figure.png|800]]

- **arXiv**: [2606.20905](https://arxiv.org/abs/2606.20905)
- **PDF**: https://arxiv.org/pdf/2606.20905
- **详细分析**: [[20_Research/Papers/具身智能/Vesta_A_Generalist_Embodied_Reasoning_Model|Vesta: A Generalist Embodied Reasoning Model]]
- **作者**: Johan Bjorck, Zhiqi Li, Yunze Man, Jing Wang, An-Chieh Cheng, Sifei Liu, Shihao Wang, Zhiding Yu, Abhishek Badki, Stan Birchfield, Valts Blukis, Yevgen Chebotar...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Vesta: A Generalist Embodied Reasoning Model》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CV-Bench, ERQA, EgoTaskQA, InternVLA, MMSI-Bench, PointBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in open-world environments must seamlessly integrate localization, spatial reasoning, navigation, and long-horizon planning. While specialist models excel at individual tasks, deploying a multi-model stack is computationally expensive and prone to cascading errors. We present Vesta, a unified embodied generalist that consolidates these capabilities into a single foundation model. Our approach combines a diverse and massive curated corpus designed to induce spatial grounding and a simple multimodal memory harness that enables reasoning over extended time horizons. Across diverse benchmarks, Vesta on average beats individual SOTA baselines by &gt;$20\%$ and beats an ensemble of per-category-best baselines by $&gt;10\%$ -- thus demonstrating that a generalist model can match or exceed specialists. On real-world robotic tasks requiring memory and reasoning, Vesta improves task success by &gt;35\%. Our work thus demonstrates that a single generalist is a feasible, scalable, and arguably preferable alternative to combining specialists.

</details>

---

### [[20_Research/Papers/具身智能/FOCA_Future-Oriented_Conditioning_for_Data-Efficient_Vision-Language-Action_Adaptation|FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation]]

![[assets/2606.20867_first_page.png|800]]

- **arXiv**: [2606.20867](https://arxiv.org/abs/2606.20867)
- **PDF**: https://arxiv.org/pdf/2606.20867
- **详细分析**: [[20_Research/Papers/具身智能/FOCA_Future-Oriented_Conditioning_for_Data-Efficient_Vision-Language-Action_Adaptation|FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation]]
- **作者**: Duc Minh Nguyen, Nghiem Tuong Diep, Binh Gia Nguyen, Trong-Bao Ho, Doanh Le, Tan Q. Nguyen, Thien-Loc Ha, Nhiem Tran, Bao Thach, Nhat X. Tran, Tuan A. Tran, Artur Habuda...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.5，大模型 0.1，世界模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable general-purpose robotic control via large-scale multimodal pretraining, yet their effectiveness under few-shot imitation learning remains limited. We conduct a systematic stress test of state-of-the-art VLA models and show that performance degrades sharply as demonstrations are reduced, revealing a key weakness of existing adaptation strategies. To address this, we introduce FOCA, a future-oriented conditioning framework for data-efficient VLA adaptation. FOCA combines explicit prediction of task-grounded future interaction embeddings with implicit alignment to future goal observations, enabling long-horizon reasoning in latent space without pixel-level prediction. This formulation naturally supports action-free co-training with synthetic videos from video world models and can be interpreted as learning a future-conditioned value-like representation. Extensive experiments demonstrate FOCA achieves 95.7% success with 20 demonstrations on LIBERO, improves 7-12% on RoboCasa, and delivers up to 26% absolute gains on real robots, establishing a new state of the art in few-shot VLA adaptation.

</details>

---

### [[20_Research/Papers/具身智能/SignVLA_Real-Time_Sign_Language-Guided_Robotic_Manipulation_via_Attention_LSTM_and_Vision-Language-Action_Models|SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models]]

![[assets/2606.20857_figure.png|800]]

- **arXiv**: [2606.20857](https://arxiv.org/abs/2606.20857)
- **PDF**: https://arxiv.org/pdf/2606.20857
- **详细分析**: [[20_Research/Papers/具身智能/SignVLA_Real-Time_Sign_Language-Guided_Robotic_Manipulation_via_Attention_LSTM_and_Vision-Language-Action_Models|SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models]]
- **作者**: Ningwei Bai, Xinyu Tan, Harry Gardner, Zhengyang Zhong, Liuhaichen Yang, Luoyu Zhang, Zhekai Duan, Monkgogi Galeitsiwe, Zezhi Tang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.7（加权：具身智能 3.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《SignVLA: Real-Time Sign Language-Guided Robotic Manipulation via Attention LSTM and Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, SignVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable robots to execute manipulation tasks from natural-language instructions grounded in visual observations. However, existing VLA interfaces primarily rely on speech or text input, limiting accessibility for deaf, hard-of-hearing, and speech-impaired users. We present SignVLA, a real-time sign-language-guided VLA framework for accessible human-robot interaction. The system introduces a modular sign-to-text interface that converts visual sign gestures into semantic instructions compatible with downstream VLA policies. Given video streams, SignVLA extracts hand landmark features and employs an attention-enhanced Long Short-Term Memory (LSTM) network to capture temporal gesture dynamics for alphabet- and command-level sign recognition. A temporal stabilization module further improves prediction consistency in real-time interaction settings.The generated instruction sequence is then passed to a downstream VLA policy for sign-conditioned robotic manipulation. Experimental results demonstrate stable real-time sign recognition and successful execution of manipulation tasks driven by sign-language inputs. Our findings suggest that lightweight temporal sign recognition can serve as an effective and practical accessibility layer for multimodal embodied intelligence.

</details>

---

### [[20_Research/Papers/大模型/One_Image_is_All_You_Need_Agentic_One-Shot_Image_Generation_via_Text-Based_World_Models_for_Long-Tail_Spatial_Perception|One Image is All You Need: Agentic One-Shot Image Generation via Text-Based World Models for Long-Tail Spatial Perception]]

![[assets/2606.20764_figure.png|800]]

- **arXiv**: [2606.20764](https://arxiv.org/abs/2606.20764)
- **PDF**: https://arxiv.org/pdf/2606.20764
- **详细分析**: [[20_Research/Papers/大模型/One_Image_is_All_You_Need_Agentic_One-Shot_Image_Generation_via_Text-Based_World_Models_for_Long-Tail_Spatial_Perception|One Image is All You Need: Agentic One-Shot Image Generation via Text-Based World Models for Long-Tail Spatial Perception]]
- **作者**: Keqin Zeng, Shuting Su, Shihao Lin, Ziyue Li, Rui Zhao
- **cs 子类**: cs.AI, cs.CV, cs.GR, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM, Multimodal, WorldModel

#### 研究背景与动机

《One Image is All You Need: Agentic One-Shot Image Generation via Text-Based World Models for Long-Tail Spatial Perception》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable spatial decision automation, such as autonomous driving and maritime surveillance, critically depends on robust visual perception. However, real-world spatiotemporal data exhibits severe heterogeneity, often manifesting as extreme long-tail distributions for safety-critical scenarios. This data scarcity induces dataset shift that degrades detection performance and pose safety risks. While synthetic data generation offers a potential solution, existing generative approaches, such as diffusion models and Generative Adversarial Networks (GANs), often lack explicit spatial grounding and structural constraints, resulting in spatial and physical inconsistencies in generated scenes. To address these challenges, we introduce WMGen-v1, an agentic text-based world model framework for long-tail spatial data generation. WMGen-v1 employs a Large Vision-Language Model (LVLM) to construct a structured scene representation from a single reference image, while a Large Language Model (LLM) performs guidance-based scene expansion under physical plausibility and commonsense constraints. Subsequently, conditioned on the structured semantic representations produced by this reasoning process, a diffusion model generates diverse and physically grounded long-tail training data. Experiments on internal industrial datasets, ROADWork, and LaRS benchmarks demonstrate that WMGen-v1 outperforms baseline approaches. Notably, detectors trained solely on WMGen-v1 synthetic data approach real-only performance on aggregate dataset-level metrics, highlighting its potential to alleviate long-tail data scarcity for downstream spatial perception.

</details>

---

### [[20_Research/Papers/具身智能/MemoryVAM_Integrating_Memory_into_Video_Action_Model_for_Robot_Manipulation|MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation]]

![[assets/2606.20679_figure.png|800]]

- **arXiv**: [2606.20679](https://arxiv.org/abs/2606.20679)
- **PDF**: https://arxiv.org/pdf/2606.20679
- **详细分析**: [[20_Research/Papers/具身智能/MemoryVAM_Integrating_Memory_into_Video_Action_Model_for_Robot_Manipulation|MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation]]
- **作者**: Yuxin Jiang, Chang Yu, Yunuo Chen, Xiang Feng, Yin Yang, Nishank Gite, Chenfanfu Jiang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MemoryVLA, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video-world-model policies learn action-relevant representations by predicting future observations. However, they condition on only a short observation window, which renders long-horizon manipulation non-Markovian when the correct action depends on earlier events that are no longer visible. We present MemoryVAM, an episodic memory mechanism for video-world-model policies. We employ a Recap-Cue (RC) module, in which a Perceiver-based Recap Compressor maps per-frame CLIP embeddings into compact memory tokens, and a lightweight Cue Gate estimates task completion from memory and language. These tokens are injected into both the video backbone and the action decoder, aligning policy imagination with episode progress and conditioning actions on history. Our model trains the memory module with video prediction, a delta-reconstruction auxiliary loss, and episode-boundary supervision, requiring no per-frame progress labels. The same mechanism applies to UNet and Diffusion Transformer (DiT) backbones by changing only the cross-attention injection interface. On LIBERO-Mem, our model improves average success from 5% to 42.5%. On real robots, it achieves 78.3% success on counting tasks, 80.0% on spatial recall, and 75.0% on sequential tracking. Project page: https://MemoryVAM.github.io/

</details>

---

### [[20_Research/Papers/强化学习/Platooning_Connected,_Autonomous,_and_Human-Driven_Vehicles_A_Deep_Reinforcement_Learning-based_Approach|Platooning Connected, Autonomous, and Human-Driven Vehicles: A Deep Reinforcement Learning-based Approach]]

![[assets/2606.20648_figure.png|800]]

- **arXiv**: [2606.20648](https://arxiv.org/abs/2606.20648)
- **PDF**: https://arxiv.org/pdf/2606.20648
- **详细分析**: [[20_Research/Papers/强化学习/Platooning_Connected,_Autonomous,_and_Human-Driven_Vehicles_A_Deep_Reinforcement_Learning-based_Approach|Platooning Connected, Autonomous, and Human-Driven Vehicles: A Deep Reinforcement Learning-based Approach]]
- **作者**: Zhen Qina, Dong-Fan Xie, Heng Ma, Xiaomei Zhao, Zhengbing He
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Platooning Connected, Autonomous, and Human-Driven Vehicles: A Deep Reinforcement Learning-based Approach》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventionally, existing vehicle platooning approaches are designed for connected vehicles, typically including connected autonomous vehicles and connected human-driven vehicles. Non-connected vehicles, such as non-connected autonomous or human-driven vehicles, are not incorporated. As a result, these platooning approaches may not properly reflect real-world mixed traffic conditions at the current stage. To address this limitation, this study proposes a hybrid platooning pattern that conditionally permits non-connected vehicles to join platoons, thereby enhancing platooning diversity and flexibility. However, it was found that the unregulated integration of non-connected vehicles can trigger rapid platoon expansion, significantly amplifying the risk of disturbance propagation in traffic flow. This, in turn, exacerbates the inherent conflict between traffic throughput and stability. To mitigate these challenges, this paper further develops a hybrid platooning control strategy based on deep reinforcement learning (DRL). This strategy integrates vehicle dynamics, platoon topology, and traffic flow states through a multi-level state representation network, enabling a dynamic trade-off between traffic capacity and stability. Numerical simulations demonstrate that the proposed strategy effectively suppresses velocity disturbance propagation by dynamically optimizing platoon structures, thereby significantly enhancing the stability and safety of mixed traffic while reducing fuel consumption and emissions.

</details>

---

### [[20_Research/Papers/大模型/MAGNIFIED_RL_Fine-tuning_of_Multimodal_Large_Language_Models_for_Motion_Planning|MAGNIFIED: RL Fine-tuning of Multimodal Large Language Models for Motion Planning]]

![[assets/2606.20641_figure.png|800]]

- **arXiv**: [2606.20641](https://arxiv.org/abs/2606.20641)
- **PDF**: https://arxiv.org/pdf/2606.20641
- **详细分析**: [[20_Research/Papers/大模型/MAGNIFIED_RL_Fine-tuning_of_Multimodal_Large_Language_Models_for_Motion_Planning|MAGNIFIED: RL Fine-tuning of Multimodal Large Language Models for Motion Planning]]
- **作者**: Letian Chen, Yiren Lu, Justin Fu, Yichen Xie, Runsheng Xu, Jyh-Jing Hwang, Ben Sapp, Drago Anguelov
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.5，强化学习 0.36，世界模型 0.16，机器人 0.9）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《MAGNIFIED: RL Fine-tuning of Multimodal Large Language Models for Motion Planning》归入 机器人、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-modal Large Language Models (MLLMs) have demonstrated remarkable capabilities in semantic understanding and common sense reasoning, making them promising candidates for solving planning problems in autonomous driving. However, the next-token text prediction objectives traditionally used in pre-training and supervised fine-tuning (SFT) of MLLMs may fall short of fulfilling the planning objectives for autonomous vehicles. The next-token prediction objective merely encourages per-token imitation in text, often irrespective of multi-step consequences and the alignment with crucial planning considerations such as giving space to other road actors. To overcome these limitations, we propose a reinforcement learning fine-tuning (RLFT) approach, MAGNIFIED, that aligns the MLLM-based driving agent with planning objectives by learning from token-level rewards. By mapping a sequence of predicted tokens to corresponding vehicle trajectories and learning from planning rewards, MAGNIFIED optimizes for the true planning objectives rather than focusing solely on token prediction accuracy, enabling the model to refine its understanding of the planning task beyond simple imitation. We validate our approach on the Waymo Open Motion Dataset with a novel setup incorporating rasterized birds-eye views and tokenized trajectories as inputs and planning-oriented outputs. An initial SFT phase establishes a strong baseline in outputting plan trajectories as sequences of X-Y coordinates in text, while subsequent RL fine-tuning substantially enhances planning performance relative to the SFT baseline (demonstrating over a 10.5% reduction in overlap rate and a 38.9% reduction in off-road rate), underscoring the potential of RLFT on MLLMs to achieve vehicle planning that is better aligned with compliant, comfortable, and efficient driving.

</details>

---
