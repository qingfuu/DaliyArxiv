# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-05

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/Flying_over_The_Uncertain_Nature_(FORTUNE)_Intelligent_and_Humanistic_3D_Path_Planning_for_Low-Altitude_Collaboration|Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration]]

![[assets/2608.03408_figure.png|800]]

- **arXiv**: [2608.03408](https://arxiv.org/abs/2608.03408)
- **PDF**: https://arxiv.org/pdf/2608.03408
- **详细分析**: [[20_Research/Papers/机器人/Flying_over_The_Uncertain_Nature_(FORTUNE)_Intelligent_and_Humanistic_3D_Path_Planning_for_Low-Altitude_Collaboration|Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration]]
- **作者**: Minghui Liwang, Wenhan Jia, Xinlei Yi, Wenbo Zhu, Yuhan Su, Xianbin Wang
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Flying over The Uncertain Nature (FORTUNE): Intelligent and Humanistic 3D Path Planning for Low-Altitude Collaboration》归入 机器人、具身智能、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MADRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The proliferation of low-altitude intelligent agents is increasing the demand for timely and socially responsible collaborative sensing in dynamic urban environments. However, jointly addressing heterogeneous spatiotemporal demands, environmental uncertainty, and human-centered operational constraints remains challenging. This paper studies 3D multi-UAV path planning and task assignment under uncertain ground PoI demands. Unlike existing work assuming static and fully known PoIs, we model persistent, temporally predictable, and emergent demands within a unified framework. We further incorporate altitude-dependent societal and environmental costs, including noise exposure and public safety risks, to balance sensing performance with socially compliant operations. To solve the resulting large-scale mixed-integer nonlinear problem, we propose FORTUNE, a hierarchical offline-online framework. Offline, a Transformer predicts Type-II PoI activation windows, while an enhanced sparrow search algorithm generates coordinated flight plans through priority-aware decoding and danger-aware evolution. Online, a lightweight refinement module accommodates emerging Type-III PoIs while preserving global mission coherence. Experiments on real-world traffic data and synthetic scenarios show that FORTUNE consistently outperforms state-of-the-art methods in effectiveness, scalability, and practical applicability.

</details>

---

### [[20_Research/Papers/机器人/CUDA_MPC_A_GPU-Native_Solver_for_Model_Predictive_Control|CUDA MPC: A GPU-Native Solver for Model Predictive Control]]

![[assets/2608.03051_figure.jpg|800]]

- **arXiv**: [2608.03051](https://arxiv.org/abs/2608.03051)
- **PDF**: https://arxiv.org/pdf/2608.03051
- **详细分析**: [[20_Research/Papers/机器人/CUDA_MPC_A_GPU-Native_Solver_for_Model_Predictive_Control|CUDA MPC: A GPU-Native Solver for Model Predictive Control]]
- **作者**: Babak Akbari, Melissa Greeff
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《CUDA MPC: A GPU-Native Solver for Model Predictive Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model Predictive Control (MPC) delivers constraint-aware control, but its reliance on online optimization limits its use on systems with fast dynamics, high-dimensional models, or long horizons. Existing GPU implementations typically treat the device as a linear-algebra accelerator, leaving the optimization loop dependent on repeated kernel launches and high-latency memory transfers. This paper introduces CUDA MPC, a GPU-native MPC framework that co-designs the optimization algorithm, execution model, and memory architecture for CUDA hardware. CUDA MPC pairs a parallel-in-horizon alternating direction method of multipliers (ADMM) splitting with a fused CUDA kernel that runs the entire iterative solve on the device. Intermediate optimization variables stay in low-latency, on-chip shared memory, and a localized atomic-flag protocol synchronizes only adjacent horizon blocks, minimizing host intervention, kernel-dispatch overhead, and global-memory traffic. Across six nonlinear robotics benchmarks spanning increasing state dimension and constraint density, CUDA MPC sustains real-time rates at horizons one to two orders of magnitude longer than CPU solvers: it solves an optimization-based collision-avoidance parking problem with 100 s of lookahead within a 0.1 s sampling interval, and is the only solver evaluated that achieves both real-time execution and collision-free coordination for a centralized 10-agent swarm, where acados and CasADi return no feasible solution and require 3.5 s and 4.5 s per solve. Against tensor-framework implementations of the same ADMM splitting, the fused kernel is up to $965\times$ faster.

</details>

---
