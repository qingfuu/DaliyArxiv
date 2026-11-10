# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-09

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Nebula_Distributed_Position-Independent_Caching_for_LLM_Serving|Nebula: Distributed Position-Independent Caching for LLM Serving]]

![[assets/2611.09474_figure.png|800]]

- **arXiv**: [2611.09474](https://arxiv.org/abs/2611.09474)
- **PDF**: https://arxiv.org/pdf/2611.09474
- **详细分析**: [[20_Research/Papers/大模型/Nebula_Distributed_Position-Independent_Caching_for_LLM_Serving|Nebula: Distributed Position-Independent Caching for LLM Serving]]
- **作者**: Yifei Liu, Junbin Pan, Junhao Hu, Yang Liu, Junyi Chen, Juntong Wu, Chen Chen, Haiyuan Zhao, Xiaoxu Chen, Weihang Chen
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Nebula: Distributed Position-Independent Caching for LLM Serving》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern LLM workflows, such as retrieval-augmented generation (RAG) and LLM agents, build long prompts from multiple independent text segments, making prefill a major source of computation. Reusing KV caches is therefore important for reducing serving costs and latency: distributed caching systems spread KV cache across a cluster to increase aggregate capacity, while position-independent caching (PIC) enables reuse of recurring segments under different prefixes. However, existing systems distribute KV caches but still rely on prefix caching (PC), while existing PIC methods enable position-independent reuse without cluster-wide resource management. We present Nebula, the first distributed LLM serving framework to treat PIC segments as first-class citizens, enabling remote PIC reuse and parallel prefill. To track PIC's fine-grained, asynchronous state changes, Nebula combines optimistic accounting with event-driven updates to provide a timely and truthful cluster view for cache management and prefill scheduling. To accommodate diverse reuse patterns across workloads, Nebula leverages cluster-wide ghost-hit feedback to automatically tune the allocation of shared cache capacity between PC and PIC. Finally, Nebula incorporates queueing, computation, and KV transfer costs into a unified prefill completion time model to guide elastic parallelism adjustment and locality-aware compute placement. Across four models and four real-world RAG and agentic workloads, Nebula reduces median TTFT by an average of 61.4% compared with the strongest existing baseline and recovers an average of 76.1% of the tokens missed by prefix caching.

</details>

---

### [[20_Research/Papers/大模型/Inside_the_Trap_A_Renewal_Law_for_Prefix-Cache_Collapse_in_LLM_Agent_Serving|Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving]]

![[assets/2611.08902_first_page.png|800]]

- **arXiv**: [2611.08902](https://arxiv.org/abs/2611.08902)
- **PDF**: https://arxiv.org/pdf/2611.08902
- **详细分析**: [[20_Research/Papers/大模型/Inside_the_Trap_A_Renewal_Law_for_Prefix-Cache_Collapse_in_LLM_Agent_Serving|Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving]]
- **作者**: Akshat Valse, Ali Jannesari
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Prefix caching lets an LLM agent's follow-up turns reuse cached KV, but a burst can tip an engine into a trap in which every turn misses and the backlog does not drain, at a load it served before. In registered paired tests on two engines, two GPUs and two models (passed at 9 of 10 rates), a 200-session burst left the engine at zero hits to the end in all 30 runs, while every matched no-burst run stayed good and a session cap prevented the trap in all 30 capped runs. We analyse an idealization of the trapped state exactly: for a fluid FIFO server on which every turn misses, we prove that along FIFO orbits its cycles obey a linear renewal recursion. As is classical, the trap drains if and only if arrivals are below the all-miss capacity; above it, a Perron root fixes the dynamics: every trapped state converges to a known self-similar regime in which the gap between turns grows linearly and the turns served are young and short. For our workload the backlog grows at 0.6 to 0.8 of the excess load and sessions complete faster than the all-miss capacity, a youth premium with turn-count and cost-growth factors, so in the model a trap's measured throughput overstates the recovery threshold. Retrospectively, with nothing fitted to trap data, the theory matches 57 stuck runs: the mean served prompt within 3% in 50 runs, completions above the all-miss capacity in every run, and the pooled gap growth. Blind in outcome, 4 runs trapped by a tool slowdown met 4 of 5 pre-set scores, cut traps persisted, and with a 20-step budget, trapped runs completed below the all-miss capacity, as predicted. Of two exits, refusing arrivals sheds sessions; a session cap restores reuse: in registered tests it rescued 9 of 9 established traps at the same load without shedding, and the engine stayed good after release. We do not prove that the engine converges to the model.

</details>

---
