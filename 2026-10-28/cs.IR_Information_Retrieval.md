# cs.IR | Information Retrieval | 2026-10-28

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/AutoRSE_Evaluating_LLM_Agents_as_Recommendation_Engineers_for_Self-Evolving_Recommender_Systems|AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems]]

![[assets/2610.37228_figure.png|800]]

- **arXiv**: [2610.37228](https://arxiv.org/abs/2610.37228)
- **PDF**: https://arxiv.org/pdf/2610.37228
- **详细分析**: [[20_Research/Papers/大模型/AutoRSE_Evaluating_LLM_Agents_as_Recommendation_Engineers_for_Self-Evolving_Recommender_Systems|AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems]]
- **作者**: Rui Tian, Yi Fang, Yejin Hua, Du Wang, Yuzhe Wang, Minxuan Shan, Zirui Ren, Xinyu Lin, Chongming Gao, Wenjie Wang, Fuli Feng
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AutoRSE: Evaluating LLM Agents as Recommendation Engineers for Self-Evolving Recommender Systems》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recommender Systems Engineer Agents (RSE-Agents), which use LLM-based agents to autonomously improve recommendation algorithms, are emerging as a promising paradigm. However, their capabilities and limitations remain poorly understood due to the lack of a unified, standardized evaluation framework and systematic trajectory-level analysis. To address this gap, we introduce AutoRSE, an evaluation framework spanning six representative industrial-grade recommendation tasks, and conduct a large-scale empirical study of three frontier LLMs across three widely used agent harnesses. Our results show that RSE-Agents consistently enhance the performance of backbones on five of the six tasks, with an average relative improvement of 16.1%, indicating that they can already autonomously improve recommendation performance. However, trajectory-level analysis also reveals that current RSE-Agents function primarily as engineering optimizers rather than algorithmic improvers: their gains are largely driven by hyperparameter tuning, training strategies, and model ensembling, while genuine algorithmic innovations are rare. Since the largest gains in recommender systems often stem from algorithmic advances, this behavior underscores a fundamental limitation of current RSE-Agents. To probe this limitation, we perform idea-injection experiments and show that agents equipped with innovative ideas from frontier research or human experts achieve substantially larger improvements than those relying on self-generated ideas. These results suggest that idea generation is a central bottleneck of current RSE-Agents, highlights a key direction for the future recommendation system research. Our implementation is publicly available on GitHub: https://github.com/Ray-Tiann/AutoRSE.

</details>

---
