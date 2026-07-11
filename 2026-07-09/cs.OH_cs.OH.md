# cs.OH | cs.OH | 2026-07-09

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/强化学习/Improving_greenhouse_fruit-production_control_by_integrating_reinforcement_learning_into_short-horizon_model_predictive_control|Improving greenhouse fruit-production control by integrating reinforcement learning into short-horizon model predictive control]]

![[assets/2607.07365_first_page.png|800]]

- **arXiv**: [2607.07365](https://arxiv.org/abs/2607.07365)
- **PDF**: https://arxiv.org/pdf/2607.07365
- **详细分析**: [[20_Research/Papers/强化学习/Improving_greenhouse_fruit-production_control_by_integrating_reinforcement_learning_into_short-horizon_model_predictive_control|Improving greenhouse fruit-production control by integrating reinforcement learning into short-horizon model predictive control]]
- **作者**: Bart van Laatum, Salim Msaad, Eldert J. van Henten, Robert D. McAllister, Sjoerd Boersma
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Improving greenhouse fruit-production control by integrating reinforcement learning into short-horizon model predictive control》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GL-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Greenhouse fruit-production control aims to maximize the economic performance (fruit revenue minus operating costs) while operating within system constraints under external weather disturbances. Control methods need to balance the delayed economic benefit of fruit yield with current operating costs. For such problems, model predictive control (MPC) can explicitly handle system constraints under future weather disturbances, but can become computationally demanding when using sufficiently long prediction horizons for (relatively large) nonlinear greenhouse fruit production models. In contrast, reinforcement learning (RL) can learn control policies offline while considering longer-term economic performance, but struggles to enforce system constraints, and performance may degrade under unseen weather trajectories. This work proposes trajectory-selection RL-MPC, a framework that incorporates longer-term economic information of fruit yield into a short-horizon MPC optimization problem. The framework uses an RL rollout trajectory to define a terminal region constraint and terminal cost. Next, a nonlinear MPC solves a short-horizon optimization problem with these terminal ingredients to find a local optimum. Finally, the framework selects and executes the first input from the trajectory with the better objective value, either from the MPC-predicted or the RL rollout trajectory. The method is applied to GreenLight, a large-scale greenhouse tomato production model that exhibits stiff dynamics. The simulation results show that trajectory-selection RL-MPC with a one-hour prediction horizon matches the closed-loop performance of a high-performing guiding policy while significantly improving over standalone MPC with the same horizon.

</details>

---

### [[20_Research/Papers/机器人/Design_and_Deployment_Guidelines_for_UAV-Mounted_RIS_Under_Position_Uncertainty|Design and Deployment Guidelines for UAV-Mounted RIS Under Position Uncertainty]]

![[assets/2607.07298_figure.png|800]]

- **arXiv**: [2607.07298](https://arxiv.org/abs/2607.07298)
- **PDF**: https://arxiv.org/pdf/2607.07298
- **详细分析**: [[20_Research/Papers/机器人/Design_and_Deployment_Guidelines_for_UAV-Mounted_RIS_Under_Position_Uncertainty|Design and Deployment Guidelines for UAV-Mounted RIS Under Position Uncertainty]]
- **作者**: Kevin Weinberger, David Müller, Martin Mönnigmann, Aydin Sezgin
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: 未提取到

#### 研究背景与动机

《Design and Deployment Guidelines for UAV-Mounted RIS Under Position Uncertainty》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

UAV-mounted reconfigurable intelligent surfaces (RIS) are a promising enabler for 6G networks, offering dynamic control of wireless propagation for coverage enhancement, integrated sensing and communication (ISAC), and localization. By exploiting UAV mobility, RIS can maintain favorable line-of-sight links, improving channel quality in dynamic environments. However, UAV positioning uncertainties introduce channel distortions that degrade RIS phase alignment and coherent combining. This work develops a GUM-based uncertainty propagation framework for UAV-mounted RIS channels, mapping UAV position uncertainty through the geometric Tx-RIS-Rx model into the complex cascaded channel. We derive a closed-form stochastic propagation model capturing nonlinear phase uncertainty effects and quantify their impact on channel coherence. The results show that phase uncertainty induces exponential coherence loss, dominating performance degradation. To characterize this transition, we introduce a performance-driven coherence threshold (PCT) that defines the boundary where incoherent combining results in a predetermined performance loss. Results based on analytical scaling laws and Monte Carlo simulations confirm the tightness of the PCT in accurately capturing the coherence transition. This validated threshold is then leveraged to derive optimal UAV-mounted RIS placement, revealing that realistic positioning conditions significantly deviate from the conventional RIS intuition, which typically favors placement close to either the transmitter or receiver.

</details>

---

### [[20_Research/Papers/大模型/A_Physics-guided_Fine-tuned_LLM-based_Framework_for_Customized_Power_Distribution_System_Feeder_Generation|A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation]]

![[assets/2607.07237_first_page.png|800]]

- **arXiv**: [2607.07237](https://arxiv.org/abs/2607.07237)
- **PDF**: https://arxiv.org/pdf/2607.07237
- **详细分析**: [[20_Research/Papers/大模型/A_Physics-guided_Fine-tuned_LLM-based_Framework_for_Customized_Power_Distribution_System_Feeder_Generation|A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation]]
- **作者**: Zhenghao Zhou, Yiyan Li, Tao Xu, Yike Guo, Zheng Yan, Mo-Yuen Chow
- **cs 子类**: 
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation》归入 大模型、强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 cs.OH 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Power distribution system feeder models (e.g., IEEE 33-bus system, IEEE 13-bus system, etc.) are cornerstones for conducting power distribution system studies. As real-world feeder models are hard to acquire due to energy security concerns, generating high-quality synthetic feeders becomes an important alternative to satisfy the fast-growing and diversified needs of power system researchers and engineers. In this paper, we propose an LLM-based synthetic feeder generation framework that can achieve end-to-end generation from natural language specifications to physically consistent feeder models. First, Supervised Fine-Tuning (SFT) is performed on a dataset created following physical laws to empower the LLM with syntactic understanding of complex feeder structures. Second, Group Relative Policy Optimization (GRPO) with a specially-designed multi-stage gated reward function is introduced to better align the generation results with user intent and physical constraints. Third, a dual-agent architecture is deployed to refine and evaluate the generated feeders. Specifically, a refinement agent calibrates the feeder model parameters referring to the industrial feeder design standards, while a judge agent provides quality assessments. Case studies demonstrate that the proposed framework generates customizable feeders with valid formats, physical consistency and high engineering applicability.

</details>

---

### [[20_Research/Papers/强化学习/Degradation-Aware_Pumping_Control_of_Variable-Speed_Pumped_Storage_via_Residual_Reinforcement_Learning|Degradation-Aware Pumping Control of Variable-Speed Pumped Storage via Residual Reinforcement Learning]]

![[assets/2607.06911_figure.png|800]]

- **arXiv**: [2607.06911](https://arxiv.org/abs/2607.06911)
- **PDF**: https://arxiv.org/pdf/2607.06911
- **详细分析**: [[20_Research/Papers/强化学习/Degradation-Aware_Pumping_Control_of_Variable-Speed_Pumped_Storage_via_Residual_Reinforcement_Learning|Degradation-Aware Pumping Control of Variable-Speed Pumped Storage via Residual Reinforcement Learning]]
- **作者**: Kyung-bin Kwon, SangWoo Park, Dam Kim
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Degradation-Aware Pumping Control of Variable-Speed Pumped Storage via Residual Reinforcement Learning》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Variable-speed pumped storage hydropower (VS-PSH) must honor short-block dispatch commitments while limiting the operational degradation that intensified regulation duty inflicts on its components. When a single controller pursues both aims at once, every tracking gain is paid for in degradation, a conflict that persists even under full model knowledge and look-ahead. This paper proposes a two-layer control architecture that separates the guaranteed commitment from the bounded learning. A deterministic feedforward-PI gate controller, auditable and certifiable for grid-connected operation, secures average power delivery over each five-minute block, while a residual reinforcement learning policy adjusts only the rotor speed within a fixed bound the gate loop can always absorb, so the worst-case command is bounded by construction. The speed policy tracks a demand-dependent best-efficiency-point reference and is trained against an operation-degradation index that combines off-best-efficiency hydraulic loss with power and actuation variation into one physically interpretable signal. Across normal and stressed dispatch, the proposed policy lowers best-efficiency-point tracking error by roughly 96\% relative to a fixed-speed baseline and cuts total degradation by up to about 56\% under the most demanding dispatch. It matches or slightly exceeds a full-information model-based optimizer in efficiency while preserving substantially tighter block tracking.

</details>

---
