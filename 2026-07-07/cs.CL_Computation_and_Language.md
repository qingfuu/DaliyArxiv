# cs.CL | Computation and Language | 2026-07-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Spinning_Straw_into_Gold_Relabeling_LLM_Agent_Trajectories_in_Hindsight_for_Successful_Demonstrations|Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations]]

![[assets/2607.04235_figure.png|800]]

- **arXiv**: [2607.04235](https://arxiv.org/abs/2607.04235)
- **PDF**: https://arxiv.org/pdf/2607.04235
- **详细分析**: [[20_Research/Papers/大模型/Spinning_Straw_into_Gold_Relabeling_LLM_Agent_Trajectories_in_Hindsight_for_Successful_Demonstrations|Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations]]
- **作者**: Zichao Li, Gang Wu, Zichao Wang, Ruiyi Zhang, Wanrong Zhu, Ryan A. Rossi, Vlad I Morariu, Jihyung Kil
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, BigBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents operate in partially observable, long-horizon settings where obtaining supervision remains a major bottleneck. We address this by utilizing a source of supervision overlooked in existing post-training methods: unintended yet successful goals embedded within agent rollouts. Specifically, we introduce Hindsight Supervised Learning (HSL), where an auxiliary LLM reviews each completed trajectory and relabels it with all of the natural-language goals the agent actually achieved. HSL then pairs the trajectory with its relabeled goals and uses these pairs for additional fine-tuning. To mitigate suboptimality in the relabeled data, we propose two learning techniques for HSL, irrelevant-action masking and sample reweighting. Our experiments show that HSL is flexible and compatible with existing post-training pipelines. It improves both SFT and DPO, with larger gains on long-horizon tasks with more diverse goal spaces. Moreover, HSL is sample-efficient: on ALFWorld, it surpasses baselines trained on the full dataset while using only one quarter of the ground-truth demonstrations.

</details>

---
