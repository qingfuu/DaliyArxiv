# cs.IR | Information Retrieval | 2026-07-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/PCTD_Preference-Guided_Counterfactual_Task_Decomposition_for_Agent_Tool_Retrieval|PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval]]

![[assets/2607.15696_figure.png|800]]

- **arXiv**: [2607.15696](https://arxiv.org/abs/2607.15696)
- **PDF**: https://arxiv.org/pdf/2607.15696
- **详细分析**: [[20_Research/Papers/强化学习/PCTD_Preference-Guided_Counterfactual_Task_Decomposition_for_Agent_Tool_Retrieval|PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval]]
- **作者**: Chu Zhao, Lei Tang, Minghang Li, Jianzhe Zhao, Guibing Guo, Zhengzong Chen, Yuanyuan Zhao, Fei Huang
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.5（加权：大模型 0.3，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval》归入 大模型、强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HammerBench, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task decomposition aims to transform ambiguous instructions into executable atomic subtasks, thereby guiding high-precision tool retrieval. However, our analysis reveals that directly adopting tool retrieval metrics, i.e., Recall or NDCG, as rewards for task decomposition can easily induce reward hacking in reinforcement learning-based methods. Specifically, models tend to maximize retrieval matching through strategies such as repetitive decomposition. This spurious correlation between the shallow features of decomposition results and retrieval metric impairs generalization in Out-of-Domain (OOD) scenarios involving unseen tools. To address this issue, we propose PCTD, a Preference-guided Counterfactual Task Decomposition framework. PCTD quantifies the marginal causal gain of decomposition on retrieval ranking through a counterfactual reward, thereby cutting off spurious correlations at their source. Meanwhile, it introduces a preference reward to impose fine-grained structural supervision on logical coherence and atomicity, encouraging the model to generate high-quality decompositions. In addition, we construct MTDTool, the task decomposition benchmark specifically designed for mobile multi-turn interactions. Extensive experiments demonstrate that PCTD alleviates repetitive decomposition and surpasses SOTA methods in retrieval, decomposition quality, and OOD generalization.

</details>

---
