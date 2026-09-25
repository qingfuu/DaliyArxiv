# cs.CL | Computation and Language | 2026-09-23

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Behavior_is_Not_Enough_A_Mechanism-Based_Evaluation_of_Social_Norm_Emergence_in_LLM_Societies|Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies]]

![[assets/2609.26481_first_page.png|800]]

- **arXiv**: [2609.26481](https://arxiv.org/abs/2609.26481)
- **PDF**: https://arxiv.org/pdf/2609.26481
- **详细分析**: [[20_Research/Papers/大模型/Behavior_is_Not_Enough_A_Mechanism-Based_Evaluation_of_Social_Norm_Emergence_in_LLM_Societies|Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies]]
- **作者**: Rasika Muralidharan, Haewoon Kwak, Jisun An
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect of expectation elicitation and isolate two collective mechanisms central to theories of norm formation---social learning through interaction and social selection through network-based group formation. We further test the stability of these resulting dynamics under adversarial disruption across four LLM families. We find that eliciting expectations increases cooperative contributions, while social learning stabilizes behavior, and social selection reliably identifies cooperators but provides limited behavioral reinforcement. Following disruption, normative expectations and behavioral coordination recover differently. Together, these results show that similar cooperative outcomes can arise from different underlying social processes. By making expectations observable, our framework allows us to attribute each mechanism's contribution separately, offering designers of multi-agent systems a principled basis for selecting the social processes that sustain cooperation.

</details>

---

### [[20_Research/Papers/大模型/Matryoshka_attribution_Learning_to_attribute_language_model_outputs_to_representations_and_weights|Matryoshka attribution: Learning to attribute language model outputs to representations and weights]]

![[assets/2609.25518_figure.png|800]]

- **arXiv**: [2609.25518](https://arxiv.org/abs/2609.25518)
- **PDF**: https://arxiv.org/pdf/2609.25518
- **详细分析**: [[20_Research/Papers/大模型/Matryoshka_attribution_Learning_to_attribute_language_model_outputs_to_representations_and_weights|Matryoshka attribution: Learning to attribute language model outputs to representations and weights]]
- **作者**: Aryaman Arora, Kirill Acharya, Nathan Hu, Yanzhe Zhang, Noah Goodman, Dan Jurafsky, Christopher Potts
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.65，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Matryoshka attribution: Learning to attribute language model outputs to representations and weights》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Attributing language model outputs to their internal computations is an open problem in interpretability. Existing methods, which use causal interventions, gradients, or learnable masks, either are infeasibly expensive or struggle to identify actual causally-important internal computations. We propose framing attribution as the problem of identifying nested subsets of internal components which minimise a downstream loss. To learn this task, we introduce Matryoshka Attribution (MAttr), a mask learning method that parametrises the mask with a simple differentiable sigmoid top-$k$ operator. We supervise training over all sparsities simultaneously by randomising $k$ over training, resulting in a learned ordering of components by attribution score. MAttr achieves number 1 on the official leaderboard of the Mechanistic Interpretability Benchmark (Mueller et al., 2025); our method identifies sparse and task-transferrable circuits across varying circuit bases. As a practical application, we show that MAttr can be trained with reinforcement learning to identify weight changes responsible for downstream behaviours in LLM finetuning. We train MAttr on refusal judge scores and find that restoring $1\%$ of Llama 3.1 8B Instruct's weights to their base model state is sufficient to remove refusals while maintaining capabilities. We view MAttr as a successful formulation of interpretability into a learnable objective that we can tackle with gradient descent, and encourage future work along these lines.

</details>

---
