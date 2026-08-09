# cs.SE | Software Engineering | 2026-08-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Agent-Based_Test_Assertion_Generation_via_Diverse_Perspective_Aggregation|Agent-Based Test Assertion Generation via Diverse Perspective Aggregation]]

![[assets/2608.05822_figure.png|800]]

- **arXiv**: [2608.05822](https://arxiv.org/abs/2608.05822)
- **PDF**: https://arxiv.org/pdf/2608.05822
- **详细分析**: [[20_Research/Papers/大模型/Agent-Based_Test_Assertion_Generation_via_Diverse_Perspective_Aggregation|Agent-Based Test Assertion Generation via Diverse Perspective Aggregation]]
- **作者**: Dong Wang, Qiaoyu Han, Lin Yang, Jianyi Zhou, Guangtai Liang, Junjie Chen
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Agent-Based Test Assertion Generation via Diverse Perspective Aggregation》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test assertions are critical elements of unit tests, serving as checkpoints to validate expected behavior and ensure software correctness. Numerous techniques have been proposed to automate assertion generation, with recent progress notably driven by large language models (LLMs). Despite the promise, existing approaches such as ChatAssert suffer from modest accuracy, heavy reliance on oversampling, and vulnerability to model randomness due to one-shot prompting. To address these limitations, we propose AssertMate, a novel agent-based assertion generation framework that enhances the quality and reliability of LLM-generated assertions through three key components: (1) actual value construction that identifies assertion targets via static analysis and type-aware heuristics; (2) multi-perspective expected value prediction using code generation, retrieval-augmented generation (RAG), and chain-of-thought (CoT) reasoning agents; and (3) an LLM-as-a-Judge collaboration mechanism to select the most appropriate assertion. Evaluation on the Defects4J benchmark demonstrates that AssertMate significantly outperforms state-of-the-art techniques in compilation success and pass rates, along with substantially higher bug detection capabilities. Integration with EvoSuite further validates AssertMate's practicality, yielding superior mutation coverage and kill counts. Ablation studies reveal that each of the three components makes a significant and complementary contribution to the overall performance. This work affirms the great potential of aggregating diverse perspectives to enhance the effectiveness of LLM-based assertion generation.

</details>

---
