# cs.NE | Neural and Evolutionary Computing | 2026-07-27

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/On_the_Runtime_Analysis_of_Reinforcement_Learning_Hyper-Heuristics|On the Runtime Analysis of Reinforcement Learning Hyper-Heuristics]]

![[assets/2607.22036_figure.png|800]]

- **arXiv**: [2607.22036](https://arxiv.org/abs/2607.22036)
- **PDF**: https://arxiv.org/pdf/2607.22036
- **详细分析**: [[20_Research/Papers/强化学习/On_the_Runtime_Analysis_of_Reinforcement_Learning_Hyper-Heuristics|On the Runtime Analysis of Reinforcement Learning Hyper-Heuristics]]
- **作者**: Pietro S. Oliveto, Zhenyu Wang, Peizhou Wu, Mengqing Xu
- **cs 子类**: cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《On the Runtime Analysis of Reinforcement Learning Hyper-Heuristics》归入 强化学习 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Selection Hyper-heuristics (HHs) automate algorithmic design by selecting from a set of low-level heuristics which one to apply at each stage of the optimisation process. Several impressive results have been recently rigorously proven regarding the performance of selection hyper-heuristics (HHs) for standard benchmark functions. However, the learning mechanisms employed by these HHs are considerably simplified compared to the machine learning techniques typically used in real world applications. In this paper we analyse a Reinforcement Learning Hyper-heuristic (RLHH) from the literature. The only previous result available proved that for a wide range of parameter settings, RLHH does not learn to select heuristics appropriately for the standard LeadingOnes benchmark function. In this paper, we rigorously prove that with appropriate parameter values RLHH equipped with two random local search operators, RLS_1 and RLS_2 optimises the LeadingOnes benchmark function in the best possible expected runtime achievable with the two operators up to lower order terms. Experiments show that for realistic problem sizes it is faster than the Generalised Random Gradient HH which was previously proven to also have optimal expected runtime up to lower order terms.

</details>

---

### [[20_Research/Papers/其他/Evolving_Self-Organising_Agents_Without_Fitness_Three_Falsifiable_Experiments_from_Constraint-Driven_Selection_to_Developmental_Encoding|Evolving Self-Organising Agents Without Fitness: Three Falsifiable Experiments from Constraint-Driven Selection to Developmental Encoding]]

![[assets/2607.21630_first_page.png|800]]

- **arXiv**: [2607.21630](https://arxiv.org/abs/2607.21630)
- **PDF**: https://arxiv.org/pdf/2607.21630
- **详细分析**: [[20_Research/Papers/其他/Evolving_Self-Organising_Agents_Without_Fitness_Three_Falsifiable_Experiments_from_Constraint-Driven_Selection_to_Developmental_Encoding|Evolving Self-Organising Agents Without Fitness: Three Falsifiable Experiments from Constraint-Driven Selection to Developmental Encoding]]
- **作者**: Anushka Sharma
- **cs 子类**: cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Evolving Self-Organising Agents Without Fitness: Three Falsifiable Experiments from Constraint-Driven Selection to Developmental Encoding》归入 大模型 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can evolutionary dynamics characteristic of biological development arise without a designer-specified fitness function? We present Genesis, a platform in which agents inhabit a Gray-Scott reaction-diffusion substrate and evolve under physical constraints alone. Three successive experimental cycles, each testing one falsifiable hypothesis, show: (1) constraint-driven selection sustains evolutionary activity after complete fitness removal but reaches a hard phenotypic complexity ceiling; (2) agent-mediated niche construction via chemical secretion is real but causally insufficient to break that ceiling; and (3) replacing the fixed-alphabet genome with a Compositional Pattern Producing Network (CPPN) indirect encoding, protected by NEAT-style speciation, produces the first evidence of progressive structural complexification in a fitness-free system. Null results are treated as precise, informative answers rather than failures, yielding reusable diagnostic tools and a sham-control protocol applicable to any open-ended evolution evaluation pipeline.

</details>

---
