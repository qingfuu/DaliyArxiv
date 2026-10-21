# cs.OH | cs.OH | 2026-10-19

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/机器人/Net-Zero_Power_UAVs_Facilitating_Quantum_HRLLC_in_Multi-Hop_UAV_Repeaters|Net-Zero Power UAVs: Facilitating Quantum HRLLC in Multi-Hop UAV Repeaters]]

![[assets/2610.23540_figure.jpg|800]]

- **arXiv**: [2610.23540](https://arxiv.org/abs/2610.23540)
- **PDF**: https://arxiv.org/pdf/2610.23540
- **详细分析**: [[20_Research/Papers/机器人/Net-Zero_Power_UAVs_Facilitating_Quantum_HRLLC_in_Multi-Hop_UAV_Repeaters|Net-Zero Power UAVs: Facilitating Quantum HRLLC in Multi-Hop UAV Repeaters]]
- **作者**: Ali Ranjha, Georges Kaddoum, Halim Yanikomeroglu
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Systems

#### 研究背景与动机

《Net-Zero Power UAVs: Facilitating Quantum HRLLC in Multi-Hop UAV Repeaters》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose a novel joint optimization framework for autonomous, quantum-enabled UAV repeater networks designed to support hyper-reliable low-latency communications (HRLLC) in challenging environments such as post-explosion chemical plant operations. The proposed system uses a symmetric dual-UAV architecture with three sequential quantum channels operating under strict energy harvesting (EH) constraints. We formulate a highly challenging non-convex mixed-integer non-linear programming (MINLP) problem. This model jointly determines qubit allocation, 2-D uncrewed aerial vehicle (UAV) spatial positioning (distance and altitude), and transmit powers to minimize the total decoding error. Crucially, our framework explicitly models real-world quantum physics, including decoherence, gate imperfections, and entanglement degradation. Since the objective function is demonstrably non-convex, to efficiently solve the MINLP, we propose a quantum-resource-optimized GA (QRO-GA). The results of our numerical simulations show that the QRO-GA yields better results than benchmark methods and it is highly efficient, with the convergence speed significantly increasing with the total qubit allocation. Convergence is achieved in as few as 5 iterations for higher qubit allocation. Moreover, the results reveal a critical U-shaped tradeoff, proving that an optimal latency distribution within a strict $80\ μ$s transmission window is strictly required to maintain HRLLC reliability. In addition, we find that the QRO-GA successfully optimizes the 2-D UAV positioning to minimize total decoding error. Finally, it balances consumed and harvested power to achieve net-zero power UAVs system.

</details>

---

### [[20_Research/Papers/机器人/QIEN_Quantum-Inspired_Energy-Neutral_UAV_Trajectory_for_WPT-Enabled_Industrial_HRLLC|QIEN: Quantum-Inspired Energy-Neutral UAV Trajectory for WPT-Enabled Industrial HRLLC]]

![[assets/2610.23524_figure.png|800]]

- **arXiv**: [2610.23524](https://arxiv.org/abs/2610.23524)
- **PDF**: https://arxiv.org/pdf/2610.23524
- **详细分析**: [[20_Research/Papers/机器人/QIEN_Quantum-Inspired_Energy-Neutral_UAV_Trajectory_for_WPT-Enabled_Industrial_HRLLC|QIEN: Quantum-Inspired Energy-Neutral UAV Trajectory for WPT-Enabled Industrial HRLLC]]
- **作者**: Ali Ranjha, Georges Kaddoum, Halim Yanikomeroglu
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《QIEN: Quantum-Inspired Energy-Neutral UAV Trajectory for WPT-Enabled Industrial HRLLC》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces Quantum-Inspired Energy-Neutral (QIEN) UAV Trajectory for WPT-Enabled Industrial HRLLC, a novel framework for mobility-integrated trajectory and resource optimization in solar-powered uncrewed aerial vehicle (UAV) relay systems supporting autonomous mining robots in post-disaster environments. We formulate a mixed-integer nonlinear program (MINLP) that jointly optimizes UAV trajectory, finite blocklength allocation, transmit power, and wireless power transfer (WPT) over discrete time horizons to maximize aggregate data throughput. The system operates under strict extreme hyper-reliable low-latency communication (HRLLC) constraints, energy sustainability requirements via solar harvesting, and continuous robot power delivery. To solve this large-scale optimization problem, QIEN employs a hybrid Cooperative Quantum-behaved Particle Swarm Optimization (Co-QPSO) algorithm using quantum tunneling mechanisms and a heterogeneous swarm architecture. Our simulation results demonstrate that the proposed QIEN framework significantly outperforms benchmark algorithms, achieving successful convergence while maintaining energy-neutral operation and satisfying all reliability, power, and mobility constraints.

</details>

---

### [[20_Research/Papers/强化学习/Filter-Augmented_Reinforcement_Learning_for_Battery_Fast_Charging_with_State_of_Health_and_Plating-Aware_Reward_Design|Filter-Augmented Reinforcement Learning for Battery Fast Charging with State of Health and Plating-Aware Reward Design]]

![[assets/2610.22787_figure.png|800]]

- **arXiv**: [2610.22787](https://arxiv.org/abs/2610.22787)
- **PDF**: https://arxiv.org/pdf/2610.22787
- **详细分析**: [[20_Research/Papers/强化学习/Filter-Augmented_Reinforcement_Learning_for_Battery_Fast_Charging_with_State_of_Health_and_Plating-Aware_Reward_Design|Filter-Augmented Reinforcement Learning for Battery Fast Charging with State of Health and Plating-Aware Reward Design]]
- **作者**: Meng Yuan, Yang Li, Changfu Zou
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Filter-Augmented Reinforcement Learning for Battery Fast Charging with State of Health and Plating-Aware Reward Design》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fast charging of lithium-ion batteries is crucial for electric vehicle adoption, yet it increases safety risks and accelerates battery ageing. To address this, we propose a filter-augmented reinforcement learning (RL) framework for lifelong health-aware fast charging, based on the twin-delayed deep deterministic policy gradient (TD3) algorithm. The RL agent is guided by a reward function that balances charging speed and battery longevity through the incorporation of state of health (SoH) information and an SoH-dependent voltage penalty term derived from a constant--current constant--overpotential charging strategy. Since onboard SoH estimates are inevitably corrupted by noise, two filtering strategies are integrated: an exponential moving average (EMA) filter when noise statistics are unknown, and a Kalman filter when they are available, with the filtered estimate embedded in both the agent's state and reward computation. The RL policy is trained using data from high-fidelity life-cycle simulations. The evaluation uses a published electrochemical and degradation parameterisation for a commercial LG M50 cell. Results show that the proposed method achieves up to 21.4\% more equivalent full cycles (EFCs) than conventional constant current--constant voltage (CC--CV) charging under 2\% SoH estimation noise, and maintains this lifetime advantage even under 5\% noise, while sustaining comparable charging speed.

</details>

---
