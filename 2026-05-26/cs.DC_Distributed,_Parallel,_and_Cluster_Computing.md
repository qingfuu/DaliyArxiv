# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-05-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Joint_Optimization_of_Training_and_Inference_in_Federated_Edge_Learning_via_Constrained_Multi-Objective_Deep_Reinforcement_Learning|Joint Optimization of Training and Inference in Federated Edge Learning via Constrained Multi-Objective Deep Reinforcement Learning]]

![[assets/2605.25916_figure.png|800]]

- **arXiv**: [2605.25916](https://arxiv.org/abs/2605.25916)
- **PDF**: https://arxiv.org/pdf/2605.25916
- **详细分析**: [[20_Research/Papers/强化学习/Joint_Optimization_of_Training_and_Inference_in_Federated_Edge_Learning_via_Constrained_Multi-Objective_Deep_Reinforcement_Learning|Joint Optimization of Training and Inference in Federated Edge Learning via Constrained Multi-Objective Deep Reinforcement Learning]]
- **作者**: Zhen Li, Jun Cai, Chao Yang, Haoran Gao
- **cs 子类**: cs.DC, cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《Joint Optimization of Training and Inference in Federated Edge Learning via Constrained Multi-Objective Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MODRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated edge learning (FEEL) has recently emerged as a promising paradigm for achieving edge intelligence (EI) via enabling collaborative model training across edge devices while protecting data privacy. In this paper, we put forth an online optimization framework that jointly manages federated training and inference on resource-constrained edge devices. We introduce a tandem-queue-inspired conversion mechanism that bridges inference requests and training data, and further incorporate both data and model freshness into the accuracy formulation to capture temporal dynamics in real-world environments. To maximize inference accuracy while minimizing latency and energy consumption, the mode selections, communication, and computation resource allocations of edge devices are jointly optimized. We formulate this optimization as a multi-objective optimization problem, which is NP-hard and further complicated by the online setting. To address these challenges, we transform the problem into a multi-objective Markov decision process (MOMDP) and develop a \underline{c}onstrained \underline{m}ulti-\underline{o}bjective \underline{p}roximal \underline{p}olicy \underline{o}ptimization (C-MOPPO) algorithm. Specifically, C-MOPPO first learns a set of policies with different preferences across three objectives, then leverages constrained policy optimization to enrich the Pareto front and obtain high-quality, dense solutions. Extensive experiments demonstrate that C-MOPPO achieves well-balanced trade-offs among objectives and significantly outperforms baselines under various system configurations.

</details>

---
