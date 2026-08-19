# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-17

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Validating_LLM-Modernized_Scientific_Software_Through_Differential_Fault_Injection|Validating LLM-Modernized Scientific Software Through Differential Fault Injection]]

![[assets/2608.14527_first_page.png|800]]

- **arXiv**: [2608.14527](https://arxiv.org/abs/2608.14527)
- **PDF**: https://arxiv.org/pdf/2608.14527
- **详细分析**: [[20_Research/Papers/大模型/Validating_LLM-Modernized_Scientific_Software_Through_Differential_Fault_Injection|Validating LLM-Modernized Scientific Software Through Differential Fault Injection]]
- **作者**: Evan Coleman, Yuzhong Shen, Masha Sosonkina, Peng Xu
- **cs 子类**: cs.DC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Validating LLM-Modernized Scientific Software Through Differential Fault Injection》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly used to modernize the legacy Fortran underlying production scientific software, but validation of these transformations emphasizes nominal executions and may not test whether a modernization preserves the original code's response to faults, perturbations, and reduced precision. We present a differential fault-injection validation method: a harness instruments the shared self-consistent-field driver of GAMESS at twelve sites and applies identical, deterministic faults to the original and LLM-modernized implementations, isolating the converted integral kernels. Across more than 2,200 runs, transient-fault absorption costs match a contraction-based model (predicted slopes 0.74 and 1.49 iterations per bit; measured 0.82 and 1.50), persistent perturbations halve final-energy error per additional bit, and the campaigns expose phase-dependent parallel deadlocks and false convergence under reduced precision. The original and modernized kernels agree in all 200 paired injections, and a measurement-guided synchronization change composes with the modernization, matching in all 40 pairs.

</details>

---

### [[20_Research/Papers/具身智能/Rollplex_Cross-Phase_GPU_Spatial_Sharing_for_Vision_Language_Model_Post-Training|Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training]]

![[assets/2608.14498_figure.png|800]]

- **arXiv**: [2608.14498](https://arxiv.org/abs/2608.14498)
- **PDF**: https://arxiv.org/pdf/2608.14498
- **详细分析**: [[20_Research/Papers/具身智能/Rollplex_Cross-Phase_GPU_Spatial_Sharing_for_Vision_Language_Model_Post-Training|Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training]]
- **作者**: Hanfeng Lu, Tianyu Feng, Suyi Li, Yuheng Zhao, Wei Gao, Shaopan Xiong, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Wei Wang
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.22（加权：具身智能 0.3，大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training》归入 大模型、强化学习、具身智能 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) enable embodied agents to reason and act from visual observations and language instructions. Reinforcement learning (RL) post-training enhances these capabilities using task feedback, but current on-policy RL runtimes execute rollout, reference scoring, and actor training in strict serial phases. While effective for text-only RL, this phase-granular execution is wasteful for VLMs, where processing dense video inputs and prompt prefixes occupies a large fraction of each phase. Because prefix processing is independent of the generated response, it can be run alongside rollout decoding, which leaves GPU compute capacity underutilized, without breaking synchronous on-policy semantics. We present Rollplex, a runtime that decomposes the reference and training phase and moves the prefix computation into the rollout decode window. Realizing this schedule requires more than concurrent kernel launches: naive colocation of Qwen2.5-VL-32\,B requires roughly 165\,GiB per GPU, while rollout and training prefer different tensor-parallel (TP) degrees and weight layouts. Rollplex addresses these constraints with two mechanisms. Phase-aware memory management controls HBM residency according to producer--consumer lifetimes. Parallelism-aware weight sharing uses the same physical storage for layout-compatible tensors across distinct TP degrees and reconstructs only incompatible tensors, avoiding a complete second actor copy. On 32 H800 GPUs, Rollplex achieves $1.23\times$--$1.30\times$ speedup over serial colocation and $1.57\times$--$2.24\times$ over disaggregation under the same GPU budget, while preserving the synchronous RL update.

</details>

---
