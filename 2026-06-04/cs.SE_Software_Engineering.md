# cs.SE | Software Engineering | 2026-06-04

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Token_Budgets_An_Empirical_Catalog_of_63_LLM-Agent_Budget-Overrun_Incidents,_with_an_Affine-Typed_Rust_Mitigation_as_a_Case_Study|Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study]]

![[assets/2606.04056_first_page.png|800]]

- **arXiv**: [2606.04056](https://arxiv.org/abs/2606.04056)
- **PDF**: https://arxiv.org/pdf/2606.04056
- **详细分析**: [[20_Research/Papers/大模型/Token_Budgets_An_Empirical_Catalog_of_63_LLM-Agent_Budget-Overrun_Incidents,_with_an_Affine-Typed_Rust_Mitigation_as_a_Case_Study|Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study]]
- **作者**: Sajjad Khan
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-agent budget overruns are a documented production failure class: a single retry loop can spend thousands of dollars before an operator notices, and the in-process integrity properties that would prevent it (no aliasing, no double-spend, no use-after-delegation of a cost-bearing value) are enforced, if at all, by ad-hoc wrappers rather than by the type system. Our central contribution is empirical: a catalog of 63 confirmed production incidents from 21 orchestration frameworks (2023-2026), each backed by a quoted GitHub issue and, where reported, a dollar loss, organized into an eight-cluster failure taxonomy (inter-rater Cohen's kappa = 0.837, N = 113), plus 47 supplementary structural entries. As one mitigation evaluated against this taxonomy, we build token-budgets, an 1,180-line Rust crate (no unsafe) that operationalizes affine ownership so that cloning, double-spending, or using a budget after delegating it are compile errors rather than runtime hazards an operator must remember to avoid. The dollar cap is runtime arithmetic under an estimator assumption; the affine layer makes that arithmetic non-bypassable. On single-agent workloads a 4-line Python counter matches the crate at 0/30 overshoot, so the distinguishing value is non-bypassability under operator error in multi-agent delegation: the delegation-fanout race documented in 11 incidents is rejected by the borrow checker at compile time, while the same pattern under asyncio overshoots 30/30 and three disciplined alternatives overshoot 0/30. Across five runtimes, three providers, and a temperature-stratified live-API test (N = 160), the approach reports zero cap violations and zero false refusals, at operational parity with concurrent work. Static over-reservation is 4-6x (2.11x adaptive). Binary-level cap-soundness on the running binary is left open.

</details>

---
