# cs.SE | Software Engineering | 2026-08-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/CausalRepair_Bridging_the_Causality_Gap_in_Large_Language_Model-Based_Automated_Program_Repair_via_Dual-Slicing|CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing]]

![[assets/2608.10613_figure.png|800]]

- **arXiv**: [2608.10613](https://arxiv.org/abs/2608.10613)
- **PDF**: https://arxiv.org/pdf/2608.10613
- **详细分析**: [[20_Research/Papers/大模型/CausalRepair_Bridging_the_Causality_Gap_in_Large_Language_Model-Based_Automated_Program_Repair_via_Dual-Slicing|CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing]]
- **作者**: Linhao Wu, Yizhou Chen, Zhen Yang, Pengyu Xue, Dan Hao
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated Program Repair (APR) has recently benefited from Large Language Models (LLMs), yet their effectiveness heavily depends on repair context. Existing LLM-based APR methods suffer from a causality gap: test contexts can be noisy or incomplete, while source contexts derived from static analysis often contain irrelevant and unexecuted code, misleading LLMs from identifying the true root cause. To address this issue, we propose CausalRepair, a conversation-driven APR framework based on minimal causal context, i.e., the essential dependencies required to explain a failure. CausalRepair employs a dual-slicing strategy: context-aware static slicing purifies test semantics, while execution-trace-based dynamic slicing captures precise runtime dependencies in source code. Together, they construct compact, causally relevant contexts to guide iterative repair. We evaluate CausalRepair on Defects4J V1.2, V2.0, and Defects4J-Trans using DeepSeek-V3. CausalRepair correctly fixes 313 bugs on Defects4J, outperforming state-of-the-art approaches such as ReinFix and TSAPR, while reducing the average repair cost to $0.029 per bug.

</details>

---
