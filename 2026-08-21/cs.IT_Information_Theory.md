# cs.IT | Information Theory | 2026-08-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/RMWorld_Task-Aware_Radio_World_Models_with_Value-of-Information_Guided_Multi-Trial_Learning_for_Multi-UAV_Communication_Control|RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control]]

![[assets/2608.20126_figure.png|800]]

- **arXiv**: [2608.20126](https://arxiv.org/abs/2608.20126)
- **PDF**: https://arxiv.org/pdf/2608.20126
- **详细分析**: [[20_Research/Papers/强化学习/RMWorld_Task-Aware_Radio_World_Models_with_Value-of-Information_Guided_Multi-Trial_Learning_for_Multi-UAV_Communication_Control|RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control]]
- **作者**: Xiucheng Wang, Nan Cheng, Junxi Huan
- **cs 子类**: cs.IT
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.6（加权：世界模型 0.8，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RMWorld: Task-Aware Radio World Models with Value-of-Information Guided Multi-Trial Learning for Multi-UAV Communication Control》归入 世界模型、机器人 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RMWorld, RadioUNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable multi-UAV communication control depends on predicting which aerial links will serve traffic before measurements are available. Radio world models (radio WMs) make such planning tractable, but their errors are nonuniform: a globally accurate model may still fail along high-demand corridors or association boundaries where rate errors reverse control decisions. This mismatch creates a learning challenge. Link queries must reduce decision-relevant channel uncertainty, while counterfactual trials must be filtered so that biased rollouts do not corrupt the policy. Existing acquisition and model-based control treat these budgets separately, valuing uncertainty, coverage, or optimistic return rather than risk reduction. We present RMWorld, a task-aware radio-WM framework that couples value-of-information channel calibration with credibility-diversity multi-trial selection. A biased propagation formula is corrected by a Bayesian residual, and each link is valued by its exact one-label reduction in locally linearized task-integrated posterior rate variance. Counterfactual branches are selected by a task-gated log-determinant objective, followed by conflict projection and fixed-batch validation. We derive the variance-reduction identity, prove posterior task-risk equivalence and the submodular greedy guarantee, and establish a scoped first-order non-interference result. Across 100 paired 3GPP trials RMWorld reaches 0.949~bit/s/Hz task-weighted RMSE, and across 30 severe-load DeepMIMO trials it reduces median backlog by 0.967 versus Ensemble UCB at 37.5\% more offline rollouts.

</details>

---
