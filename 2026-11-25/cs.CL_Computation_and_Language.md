# cs.CL | Computation and Language | 2026-11-25

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/ARS-VLM_Visually_Aligned_Augmented_Random_Search_for_Vision-Language_Models|ARS-VLM: Visually Aligned Augmented Random Search for Vision-Language Models]]

![[assets/2611.32147_figure.png|800]]

- **arXiv**: [2611.32147](https://arxiv.org/abs/2611.32147)
- **PDF**: https://arxiv.org/pdf/2611.32147
- **详细分析**: [[20_Research/Papers/大模型/ARS-VLM_Visually_Aligned_Augmented_Random_Search_for_Vision-Language_Models|ARS-VLM: Visually Aligned Augmented Random Search for Vision-Language Models]]
- **作者**: Xiangwei Wang, Jianyuan Lin, Peng Wang, Saman Halgamuge
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.65，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, RL, Systems

#### 研究背景与动机

《ARS-VLM: Visually Aligned Augmented Random Search for Vision-Language Models》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

First-order reinforcement learning, such as Group Relative Policy Optimization (GRPO), is widely used to post-train Vision-Language Models (VLMs) for multimodal reasoning. However, it incurs heavy memory and system overhead from backpropagation, optimizer states, and a reference model. Forward-only zeroth-order (ZO) methods, such as Evolution Strategies (ES) and its top-k variant Augmented Random Search (ARS), avoid these overheads via reward-guided weight perturbations, yet remain unexplored for VLM reasoning. We find that directly applying standard ES or vanilla ARS to VLMs suffers from two fundamental failure modes: (i) patch-grid overfitting, fitting fragile grid-specific visual token artifacts while ignoring spatial invariants, and (ii) catastrophic forgetting, degrading general perception and out-of-distribution (OOD) tasks due to unbounded high-rank parameter and policy drift. We propose ARS-VLM, a visually aligned Augmented Random Search framework for forward-only VLM post-training. First, ARS-VLM extracts a contrastive visual basis from bilinearly paired cross-grid views, concentrating perturbations on shared visual signals while suppressing patch-shift artifacts. Second, ARS-VLM anchors shallow visual-fusion layers with a soft subspace prior while freeing deep reasoning layers, restraining policy drift without a reference model. Third, ARS-VLM scores perturbations on paired views to discard view-fragile directions during top-k selection. We evaluate ARS-VLM on Qwen3-VL-4B and Qwen3-VL-8B on multimodal reasoning tasks. On 8B, ARS-VLM reaches 61.0% validation accuracy in 20 steps versus 150 for GRPO (7.5x fewer optimization steps) and avoids the late OOD collapse of vanilla ARS and ES. Moreover, ARS-VLM achieves 75.41% single-view micro accuracy across seven OOD vision reasoning benchmarks, compared with 75.31% for full-parameter GRPO, using forward-only post-training.

</details>

---

### [[20_Research/Papers/大模型/fork()_for_Agents_Agent_Kernel_for_Non-blocking_LLM_Orchestration|fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration]]

![[assets/2611.31727_first_page.png|800]]

- **arXiv**: [2611.31727](https://arxiv.org/abs/2611.31727)
- **PDF**: https://arxiv.org/pdf/2611.31727
- **详细分析**: [[20_Research/Papers/大模型/fork()_for_Agents_Agent_Kernel_for_Non-blocking_LLM_Orchestration|fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration]]
- **作者**: Ankit Chadha, Pratyay Banerjee
- **cs 子类**: cs.CL, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《fork() for Agents: Agent Kernel for Non-blocking LLM Orchestration》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutomationBench, InterruptBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents typically execute tool calls synchronously and discard completed work upon failure. Subgraph-selective recovery, re-executing only a failed node's transitive descendants, is a well-established pattern in distributed systems (Spark, Erlang/OTP, Dryad), and recent agent runtimes (Sherlock, AgentGit, Atomix) preserve completed work through verifiers, version control, or transactional tool boundaries. We present \textbf{Agent-Kernel}, a non-blocking runtime that ports this pattern to the LLM \emph{content plane}: its primitive, \textbf{Sub-Graph Recovery (SGR)}, fires on a raw exception with no trained verifier or planner, resets a failed node's descendants while preserving completed siblings, and composes each parent's text into its children's prompts (context inheritance), all on a durable substrate with a formal state-preservation guarantee. Across 14{,}434 runs on synthetic and standard benchmarks (tau-bench, Gaia2, AutomationBench, InterruptBench), SGR reaches full recovery within budget=3 where whole-trajectory replay exhausts (100\% vs.\ 55\%), and is roughly 10$\times$ faster than an adapted Sherlock rollback that also recovers. It matches ReAct-serial accuracy within noise on linear workloads while adding recovery and parallelism (up to 12.7$\times$ speedup) where structure permits. Ablation isolates SGR: removing it collapses success to 39.4\%.

</details>

---
