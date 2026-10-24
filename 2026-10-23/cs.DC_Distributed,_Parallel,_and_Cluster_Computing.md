# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-10-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Know_When_to_Escalate_Critic-Guided_Adaptive_Execution_for_Cloud-Local_Embodied_Agents|Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents]]

![[assets/2610.30587_figure.png|800]]

- **arXiv**: [2610.30587](https://arxiv.org/abs/2610.30587)
- **PDF**: https://arxiv.org/pdf/2610.30587
- **详细分析**: [[20_Research/Papers/具身智能/Know_When_to_Escalate_Critic-Guided_Adaptive_Execution_for_Cloud-Local_Embodied_Agents|Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents]]
- **作者**: Wei Zhang, Lirong Xiang, Charles Fleming
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.5，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in foundation-model agents have enabled increasingly capable embodied systems for long-horizon planning and interaction. However, embodied agents require fast, closed-loop decisions as they continuously perceive and act on a changing environment. Deploying strong cloud agents leaves the platform idle for seconds between consecutive actions, while lightweight local models respond quickly but are more vulnerable to errors. Existing hierarchical architectures typically assign models fixed roles, whereas conventional model routers make stateless per-request decisions. We present CARE, a critic-guided adaptive execution framework that dynamically determines when to escalate control from a local executor to a stronger cloud model. A lightweight critic model monitors execution reliability and triggers escalation when local execution becomes unreliable; once escalated, control persists until the agent recovers, avoiding step-wise switching. To support such control transfer, a shared handoff memory maintains execution context and task-level progress across executors, enabling the model to intervene without restarting from scratch. Across diverse embodied benchmarks, CARE improves task success by 6.3-18.3 percentage points over the strongest evaluated collaboration baseline. CARE further approaches or exceeds Cloud-only success while reducing median time-between-action latency by 28.8-82.6%.

</details>

---
