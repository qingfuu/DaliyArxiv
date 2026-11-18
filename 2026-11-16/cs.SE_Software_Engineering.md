# cs.SE | Software Engineering | 2026-11-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/其他/HerAgent_A_Block-Level_Checkpointing_Harness_for_Coding-Agent_Environment_Setup|HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup]]

![[assets/2611.18443_figure.png|800]]

- **arXiv**: [2611.18443](https://arxiv.org/abs/2611.18443)
- **PDF**: https://arxiv.org/pdf/2611.18443
- **详细分析**: [[20_Research/Papers/其他/HerAgent_A_Block-Level_Checkpointing_Harness_for_Coding-Agent_Environment_Setup|HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup]]
- **作者**: Xiang Li, Siyu Lu, Federica Sarro, Claire Le Goues, He Ye
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《HerAgent: A Block-Level Checkpointing Harness for Coding-Agent Environment Setup》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Installamatic-Bench, SetupBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern coding agents rely on establishing executable software environments before they can perform software engineering tasks such as testing, debugging, and patch validation. Existing setup agents typically control progress at either single-command or whole-script granularity, making recovery either too local to remove polluted state or too coarse to preserve useful progress. We present HerAgent (Harness EnviRonment Setup Agent), a block-level harness for coding-agent environment setup. HerAgent's main contribution is semantic setup blocks: a single progress-control abstraction used for execution, validation, checkpointing, repair, and rollback. Evaluated against six prior agents on four environment-setup datasets, HerAgent improves setup success in every comparison, achieving the largest gains on Installamatic-Bench (52.0% to 85.0%) and SetupBench (46.3% to 70.4%). It also reduces setup costs by up to 94.5%, showing that block-level progress control improves reliability and efficiency.

</details>

---
