# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-06-17

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Verified_Detection_and_Prevention_of_Concurrency_Anomalies_in_Multi-Agent_Large_Language_Model_Systems|Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems]]

![[assets/2606.17182_figure.png|800]]

- **arXiv**: [2606.17182](https://arxiv.org/abs/2606.17182)
- **PDF**: https://arxiv.org/pdf/2606.17182
- **详细分析**: [[20_Research/Papers/大模型/Verified_Detection_and_Prevention_of_Concurrency_Anomalies_in_Multi-Agent_Large_Language_Model_Systems|Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems]]
- **作者**: Sajjad Khan
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems share state through memory stores, vector indices, and tool registries. We model such sharing as long-running read-generate-write operations under deterministic-generation semantics -- the regime durable-execution engines enforce by deterministic replay -- and formalize four concurrency anomalies in TLA+: stale-generation, phantom-tool, causal-cascade, and tool-effect reordering, structural analogues of classical isolation anomalies, each with a TLC counter-example. The exclusion lattice over these anomalies is trivial; the contribution is the mechanically verified realizability and strict separation of one maximal chain within it, $L_0 \subsetneq \cdots \subsetneq L_4$, to our knowledge the first machine-checked consistency hierarchy for such runtimes. A development of 274 Verus obligations (zero assume, zero admit; trust base: two structural axioms and a mutex correspondence) proves the detectors sound and complete against the specifications and each runtime its avoidance set. Three deployed Rust runtimes realize L0-L1 (pessimistic locking, serializable snapshot isolation, default-SI), each verified against stale-generation and refined to its state machine; L2-L4 are exec-mode-verified with dependency-free prevention twins (A3, A6, A2: 0/1000 versus 1000/1000), and L2 is run live across three model families (A3 prevented in all 120 retracted sessions). We reproduce a silent lost update in ByteDance's deer-flow, formalizing its fix as a verified $L_0 \to L_1$ refinement, and exhibit tool-effect reordering in LangGraph's ToolNode on unmodified output, removed by an L3 commit-order sequencer. The verified detector, refinements, and realizability artifacts are the contribution; the phenomena and lattice are classical.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_LLM_Coding_Agents_on_SZ-Family_Lossy_Compression_Across_Architectures|Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures]]

![[assets/2606.17058_figure.png|800]]

- **arXiv**: [2606.17058](https://arxiv.org/abs/2606.17058)
- **PDF**: https://arxiv.org/pdf/2606.17058
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_LLM_Coding_Agents_on_SZ-Family_Lossy_Compression_Across_Architectures|Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures]]
- **作者**: Changqing Li, Shouwei Gao, Kai Zhao, Sheng Di, Wenqian Dong
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Evaluating LLM Coding Agents on SZ-Family Lossy Compression Across Architectures》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) coding agents are increasingly applied to code translation and optimization, yet their effectiveness in performance-critical high-performance computing (HPC) settings remains poorly characterized. This paper evaluates LLM-based coding workflows on SZ-family error-bounded lossy compression kernels, which combine numerical constraints with memory-intensive and control-flow-heavy implementations. We study two representative CUDA workloads (SZp and SZx) and target two heterogeneous execution platforms: NVIDIA GPUs and Cerebras wafer-scale accelerators. Focusing on single-agent iterative generation, we analyze not only final throughput but also agent runtime behavior, including iteration patterns, sensitivity to prompt specification, and characteristic failure modes. Our results reveal a pronounced cross-architecture divergence. On GPUs, stronger models can achieve substantially higher throughput but exhibit increased sensitivity to prompt precision and optimization guidance, whereas on Cerebras the dominant challenge lies in producing runnable programs under a PE-centric spatial execution model. We further observe that LLM agents are more effective on modular kernels (SZx) than on tightly coupled bit-level pipelines (SZp), where structural dependencies hinder optimization progress. These findings suggest that evaluating LLM coding agents for HPC requires accounting for both performance outcomes and architecture-specific robustness, and that success on thread-based platforms does not directly transfer to spatial accelerators.

</details>

---
