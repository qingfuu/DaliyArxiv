# cs.CL | Computation and Language | 2026-06-04

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/大模型/GARL_Game-Theoretic_Reinforcement_Learning_for_Multi-Agent_Strategic_Prioritisation|GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation]]

![[assets/2606.05002_figure.png|800]]

- **arXiv**: [2606.05002](https://arxiv.org/abs/2606.05002)
- **PDF**: https://arxiv.org/pdf/2606.05002
- **详细分析**: [[20_Research/Papers/大模型/GARL_Game-Theoretic_Reinforcement_Learning_for_Multi-Agent_Strategic_Prioritisation|GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation]]
- **作者**: Yuxiao Ye, Yiwen Zhang, Huiyuan Xie, Yuqin Huang, Zhiyuan Liu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.55（加权：大模型 0.75，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《GARL: Game-Theoretic Reinforcement Learning for Multi-Agent Strategic Prioritisation》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based multi-agent systems are increasingly used for strategic decision-making tasks. In such settings, performance depends not only on individual model capabilities, but also on the policies by which agents interact and adapt. Multi-agent reinforcement learning can optimise these interaction policies, but its reward design often remains task-specific and weakly grounded in interaction structure. To address this gap, we propose GARL, a GAme-theoretic Reinforcement Learning framework for multi-agent strategic prioritisation. GARL formalises strategic prioritisation as a two-stage game: competing agents first allocate strategic resources over a shared candidate set, and a higher-level arbiter then produces the final ranking. The resulting game-theoretic utilities are converted into role-specific reinforcement signals, allowing policy optimisation to be guided by structured interaction. We instantiate GARL on issues-in-dispute ranking, where the goal is to prioritise core issues in legal proceedings. Experiments show that GARL improves ranking performance, enables small open-source LLMs to become competitive with a strong closed-source LLM under the same candidate-ranking setting, and yields gains in legal-domain competence and broader strategic decision-making. Overall, GARL demonstrates how game-theoretic interaction structure can be turned into reinforcement-learning objectives, providing a principled approach to policy optimisation in multi-agent strategic prioritisation.

</details>

---

### [[20_Research/Papers/大模型/Probing_Outcome-Level_Resemblance_and_Mechanism-Level_Alignment_in_LLM_Risk_Decisions_Evidence_from_the_St._Petersburg_Game|Probing Outcome-Level Resemblance and Mechanism-Level Alignment in LLM Risk Decisions: Evidence from the St. Petersburg Game]]

![[assets/2606.04978_figure.png|800]]

- **arXiv**: [2606.04978](https://arxiv.org/abs/2606.04978)
- **PDF**: https://arxiv.org/pdf/2606.04978
- **详细分析**: [[20_Research/Papers/大模型/Probing_Outcome-Level_Resemblance_and_Mechanism-Level_Alignment_in_LLM_Risk_Decisions_Evidence_from_the_St._Petersburg_Game|Probing Outcome-Level Resemblance and Mechanism-Level Alignment in LLM Risk Decisions: Evidence from the St. Petersburg Game]]
- **作者**: Chensong Huang, Changyu Chen, Chenwei Lin, Hanjia Lyu, Xian Xu, Jiebo Luo
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Probing Outcome-Level Resemblance and Mechanism-Level Alignment in LLM Risk Decisions: Evidence from the St. Petersburg Game》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs can appear cautious in risk decision-making tasks, yet cautious-looking outputs do not necessarily indicate alignment with human decision-making mechanisms. We investigate this distinction using the St. Petersburg game as a controlled testbed, a classical paradox in which the expected payoff is infinite, yet humans typically report low, finite willingness to pay. We evaluate 28 LLMs with a structured prompt suite that includes the original game; controlled decision variants that perturb truncation, repeated play, numeric endowment, and occupational identity; a human-perspective prompt that asks models to reason as human decision makers; and paired comparisons between base models and their instruction-tuned counterparts. In the original game, most models generate finite bids, creating the appearance of human-like risk behavior. However, this outcome-level resemblance masks substantial mechanism-level differences. The controlled variants reveal that rather than maintaining human-like behavior seen in the original game, models often shift to conditionally and computationally rational behavior. Human-cue prompting and instruction tuning often lower bids and reduce some visible pathologies, but most mechanism-level response patterns remain largely unchanged. These findings show that behavioral alignment in risk decision-making can be surface-level: LLMs may produce human-like risk decisions without exhibiting human-consistent mechanisms. High-stakes evaluations of LLM decision-making should therefore move beyond outcome similarity and examine whether the alignment is supported by mechanism-level consistency.

</details>

---

### [[20_Research/Papers/大模型/BreastGPT_A_Multimodal_Large_Language_Model_for_the_Full_Spectrum_of_Breast_Cancer_Clinical_Routine|BreastGPT: A Multimodal Large Language Model for the Full Spectrum of Breast Cancer Clinical Routine]]

![[assets/2606.04911_figure.png|800]]

- **arXiv**: [2606.04911](https://arxiv.org/abs/2606.04911)
- **PDF**: https://arxiv.org/pdf/2606.04911
- **详细分析**: [[20_Research/Papers/大模型/BreastGPT_A_Multimodal_Large_Language_Model_for_the_Full_Spectrum_of_Breast_Cancer_Clinical_Routine|BreastGPT: A Multimodal Large Language Model for the Full Spectrum of Breast Cancer Clinical Routine]]
- **作者**: Yang Liu, Jiajin Zhang, Danyang Tu, Yaojun Hu, Jiao Qu, Jiuyu Zhang, Yu Shi, Wei Fang, Shi Gu, Ling Zhang, Yingda Xia
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《BreastGPT: A Multimodal Large Language Model for the Full Spectrum of Breast Cancer Clinical Routine》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BreastStage-Bench, GMAI-MMBench, LongNet, MMBench, MammoVQA, OmniMedVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Breast cancer remains a leading cause of cancer-related mortality among women. Its clinical management requires multimodal reasoning across a clinical workflow that spans \textit{screening}, \textit{diagnosis} and \textit{treatment planning}, where each stage involves distinct imaging modalities, task objectives, and reasoning patterns. However, constrained by data scarcity and model versatility, existing medical MLLMs are typically evaluated on isolated modalities or narrow task families, limiting their ability to support workflow-level clinical reasoning. In this work, we first introduce \textbf{BreastStage}, a workflow-aligned breast imaging instruction corpus comprising 1.86M instruction-following pairs curated from 17 sub-datasets across 5 imaging modalities and 136 task templates. Its held-out split, \textbf{BreastStage-Bench}, provides a comprehensive benchmark for evaluating multimodal reasoning across the breast cancer care continuum. Building on this corpus, we propose \textbf{BreastGPT}, a unified MLLM equipped with a dual-branch visual encoder and concept-preserving token compression to bridge the scale gap between standard radiology and gigapixel pathology. On BreastStage-Bench, BreastGPT achieves 75.66\% closed-ended accuracy and 89.92\% open-ended score, outperforming both general-purpose and medical-specific MLLMs across clinical stages and task formats. These results suggest that workflow-aligned data and cross-scale visual modeling are critical for clinically grounded medical MLLMs. All data, code, and model checkpoints are released at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learning_with_Verifiable_Rewards|GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards]]

![[assets/2606.04889_first_page.png|800]]

- **arXiv**: [2606.04889](https://arxiv.org/abs/2606.04889)
- **PDF**: https://arxiv.org/pdf/2606.04889
- **详细分析**: [[20_Research/Papers/强化学习/GRAIL_Gradient-Reweighted_Advantages_for_Reinforcement_Learning_with_Verifiable_Rewards|GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Tej Deep Pala, Vernon Toh, Soujanya Poria
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《GRAIL: Gradient-Reweighted Advantages for Reinforcement Learning with Verifiable Rewards》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (e.g. GRPO) is now a common way to improve mathematical reasoning in Large Language Models (LLMs). However, current methods usually broadcast one sequence-level advantage to all tokens, or use costly process reward models (PRMs) for step-level supervision. Uniform advantage distribution assumes that all tokens contribute equally to the final reward. This dilutes the gradient signal, since flawed reasoning steps and filler words are updated as strongly as valid logical inferences. To address this, we introduce Gradient-Reweighted Advantage (GRAIL), an intrinsic token-wise advantage reweighting method. GRAIL uses gradient-activation saliency to place more weight on tokens that are more locally sensitive to the final answer. Evaluations across five models from the Qwen3, R1-distilled and OctoThinker families show that GRAIL consistently outperforms GRPO. GRAIL achieved an average improvement of 3.60% in accuracy and 3.05% in Pass@3, demonstrating that fine-grained reasoning alignment can be achieved without process-level supervision.

</details>

---

### [[20_Research/Papers/大模型/Agent_Planning_Benchmark_A_Diagnostic_Framework_for_Planning_Capabilities_in_LLM_Agents|Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents]]

![[assets/2606.04874_figure.png|800]]

- **arXiv**: [2606.04874](https://arxiv.org/abs/2606.04874)
- **PDF**: https://arxiv.org/pdf/2606.04874
- **详细分析**: [[20_Research/Papers/大模型/Agent_Planning_Benchmark_A_Diagnostic_Framework_for_Planning_Capabilities_in_LLM_Agents|Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents]]
- **作者**: Haoyu Sun, Wenxuan Wang, Mingyang Song, Jujie He, Weinan Zhang, Yang Liu, Yang Yang, Yu Cheng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.45（加权：大模型 1.45）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning is central to LLM agents: before acting, an agent must decompose goals, select tools, reason over constraints, and decide when a task is infeasible. Yet existing agent evaluations often report only end-to-end success, making it difficult to determine whether failures stem from planning or execution. We introduce \textbf{Agent Planning Benchmark (APB)}, a planning-specific diagnostic benchmark with 4,209 multimodal cases across 22 domains and five settings, covering holistic planning, feedback-conditioned step-wise planning, and robustness under extraneous tools, broken tools, and unsolvable tasks. Across 12 MLLMs, APB reveals systematic weaknesses in long-horizon planning, tool-noise robustness, calibrated refusal, and inference-time refinement. We further validate APB on 200 ToolSandbox tasks and 200 $\tau^2$-bench tasks, where APB-guided refinement consistently improves plan correctness, plan grade, and downstream execution metrics across three representative models. APB thus serves as an upstream diagnostic complement to execution benchmarks.

</details>

---

### [[20_Research/Papers/大模型/MusaCoder_Native_GPU_Kernel_Generation_with_Full-Stack_Training_on_Moore_Threads_GPU|MusaCoder: Native GPU Kernel Generation with Full-Stack Training on Moore Threads GPU]]

![[assets/2606.04847_figure.png|800]]

- **arXiv**: [2606.04847](https://arxiv.org/abs/2606.04847)
- **PDF**: https://arxiv.org/pdf/2606.04847
- **详细分析**: [[20_Research/Papers/大模型/MusaCoder_Native_GPU_Kernel_Generation_with_Full-Stack_Training_on_Moore_Threads_GPU|MusaCoder: Native GPU Kernel Generation with Full-Stack Training on Moore Threads GPU]]
- **作者**: Kun Cheng, Songshuo Lu, Sicong Liao, Tankun Li, Yafei Zhang, Dong Yang, Qiheng Lv, Hua Wang, Zhi Chen, Yaohua Tang
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《MusaCoder: Native GPU Kernel Generation with Full-Stack Training on Moore Threads GPU》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：KernelBench, MooreEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Native GPU kernel generation turns high-level tensor programs into executable, efficient low-level code. Existing Large Language Models (LLMs) struggle with this task, while execution-based reinforcement learning suffers from sparse rewards, reward hacking, and training instability. We present MusaCoder, a full-stack training framework for native GPU kernel generation on CUDA and MUSA backends. MusaCoder combines progressive kernel-oriented data synthesis, diversity-preserving rejection fine-tuning, and execution-feedback Reinforcement Learning (RL) through MooreEval, a distributed verifier and reward environment. To stabilize RL, MusaCoder introduces PrimeEcho for first-turn-anchored multi-turn rewards, Buffered Dynamic Retry for recovering signals from all-failed hard samples, and MirrorPop for off-policy sequence filtering. Experiments on KernelBench and a MUSA-ported variant show that MusaCoder outperforms strong open-source and proprietary baselines in both correctness and empirical speedup, with the 9B model matching or exceeding frontier closed-source models and the 27B model establishing a new state of the art. These results demonstrate not only the effectiveness of full-stack execution-feedback training for native kernel generation, but also the capability of Moore Threads GPUs to support the complete LLM post-training stack, providing a practical foundation for large-model training and optimization on emerging accelerators.

</details>

---

### [[20_Research/Papers/大模型/PersonaTree_Structured_Lifecycle_Memory_for_Person_Understanding_in_LLM_Agents|PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents]]

![[assets/2606.04780_figure.png|800]]

- **arXiv**: [2606.04780](https://arxiv.org/abs/2606.04780)
- **PDF**: https://arxiv.org/pdf/2606.04780
- **详细分析**: [[20_Research/Papers/大模型/PersonaTree_Structured_Lifecycle_Memory_for_Person_Understanding_in_LLM_Agents|PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents]]
- **作者**: Yubo Hou, Jingwei Song, Hongbo Zhang, Zhisheng Chen, Bang Xiao, Tao Wan, Zengchang Qin
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent LLM agents require memory representations that make the formation of person understanding explicit across long term interaction. Existing agent memory methods emphasize information retention and retrieval, yet give limited account of how accumulated interaction evidence is abstracted into person understanding. We view this process as schema formation, where situated evidence is abstracted into reusable patterns and stable person level claims. We introduce PersonaTree, a structured lifecycle memory framework that realizes this view as a three level persona tree with explicit support paths from evidence to claims. PersonaTree maintains the tree through conservative writing, confidence guided consolidation, and query conditioned path retrieval, returning only the evidence depth required by each query. Across six person understanding and persistent memory benchmarks with three answer backbones, PersonaTree ranks first in 12 of 18 compact scores and reaches the top two in 16 settings. Ablations show that hierarchy improves abstract person understanding on KnowMe, while support path retrieval improves RealPref alignment under a comparable context budget.

</details>

---

### [[20_Research/Papers/具身智能/NextMotionQA_Benchmarking_and_Judging_Human_Motion_Understanding_with_Vision-Language_Models|NextMotionQA: Benchmarking and Judging Human Motion Understanding with Vision-Language Models]]

![[assets/2606.04773_first_page.png|800]]

- **arXiv**: [2606.04773](https://arxiv.org/abs/2606.04773)
- **PDF**: https://arxiv.org/pdf/2606.04773
- **详细分析**: [[20_Research/Papers/具身智能/NextMotionQA_Benchmarking_and_Judging_Human_Motion_Understanding_with_Vision-Language_Models|NextMotionQA: Benchmarking and Judging Human Motion Understanding with Vision-Language Models]]
- **作者**: Yong Cao, Chuqiao Li, Xianghui Xie, Gerard Pons-Moll, Andreas Geiger
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《NextMotionQA: Benchmarking and Judging Human Motion Understanding with Vision-Language Models》归入 具身智能、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NextMotionQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable evaluation of human motion understanding is fundamental to advancing embodied AI, robotics, and animation. However, existing benchmarks suffer from coarse semantic granularity, undifferentiated difficulty, limited annotation quality, and pervasive answer ambiguity, leaving them unable to diagnose where current models fail. To bridge this gap, we introduce NextMotionQA, a comprehensive benchmark that leverages vision-language models (VLMs) for semi-automated, expert-verified dataset. NextMotionQA features three complementary tasks: multiple-choice question answering, video captioning, and fine-grained error correction. Each task is systematically structured across three core semantic axes and stratified into three task complexity levels. Our extensive evaluation of twelve representative VLMs uncovers critical capability gaps and weakness that remain invisible under conventional, single-task evaluations. In a complementary direction, recent work has begun using VLMs as judges for text-to-motion evaluation; we ask whether they show the same degradation under harder tasks. We find that VLMs align strongly with expert ratings on coarse criteria (Cohen's \kappa=0.70) but break down on fine-grained, part-level judgment (\kappa=0.10), validating the paradigm in its strong regime while clarifying its limits.

</details>

---

### [[20_Research/Papers/大模型/Query-based_Cross-Modal_Projector_Bolstering_Mamba_Multimodal_LLM|Query-based Cross-Modal Projector Bolstering Mamba Multimodal LLM]]

![[assets/2606.04719_figure.png|800]]

- **arXiv**: [2606.04719](https://arxiv.org/abs/2606.04719)
- **PDF**: https://arxiv.org/pdf/2606.04719
- **详细分析**: [[20_Research/Papers/大模型/Query-based_Cross-Modal_Projector_Bolstering_Mamba_Multimodal_LLM|Query-based Cross-Modal Projector Bolstering Mamba Multimodal LLM]]
- **作者**: SooHwan Eom, Jay Shim, Gwanhyeong Koo, Haebin Na, Mark A. Hasegawa-Johnson, Sungwoong Kim, Chang D. Yoo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Query-based Cross-Modal Projector Bolstering Mamba Multimodal LLM》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Transformer's quadratic complexity with input length imposes an unsustainable computational load on large language models (LLMs). In contrast, the Selective Scan Structured State-Space Model, or Mamba, addresses this computational challenge effectively. This paper explores a query-based cross-modal projector designed to bolster Mamba's efficiency for vision-language modeling by compressing visual tokens based on input through the cross-attention mechanism. This innovative projector also removes the need for manually designing the 2D scan order of original image features when converting them into an input sequence for Mamba LLM. Experimental results across various vision-language understanding benchmarks show that the proposed cross-modal projector enhances Mamba-based multimodal LLMs, boosting both performance and throughput.

</details>

---

### [[20_Research/Papers/大模型/Rethinking_Continual_Experience_Internalization_for_Self-Evolving_LLM_Agents|Rethinking Continual Experience Internalization for Self-Evolving LLM Agents]]

![[assets/2606.04703_figure.png|800]]

- **arXiv**: [2606.04703](https://arxiv.org/abs/2606.04703)
- **PDF**: https://arxiv.org/pdf/2606.04703
- **详细分析**: [[20_Research/Papers/大模型/Rethinking_Continual_Experience_Internalization_for_Self-Evolving_LLM_Agents|Rethinking Continual Experience Internalization for Self-Evolving LLM Agents]]
- **作者**: Jingwen Chen, Wenkai Yang, Shengda Fan, Wenbo Nie, Chenxing Sun, Shaodong Zheng, Yangen Hu, Lu Pan, Ke Zeng, Yankai Lin
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Rethinking Continual Experience Internalization for Self-Evolving LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SailorFog-QA, WebWalkerQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experience internalization converts contextual experience from past interactions into reusable parametric capability, offering a promising path toward continual learning in large language models (LLMs). While prior work has predominantly focused on single-iteration transfer, we discover that under multi-iteration experience learning, existing methods suffer from a progressive capability collapse rather than compounding improvement. We systematically examine this failure through three vital dimensions of experience internalization: (1) Experience Granularity: We find that principle-level experience is more durable than instance-level experience, as it effectively abstracts transferable strategies away from trajectory-specific details. (2) Experience Injection Pattern: Our analysis reveals that step-wise injection significantly outperforms global injection by aligning experience with intermediate decision states, a property that is critical for long-horizon tool use. (3) Internalization Regime: We demonstrate that off-policy context-distillation on high-quality teacher trajectories provides a substantially more stable training signal than on-policy context-distillation, which is inherently limited by local corrections on student-induced flawed states. Together, these insights yield a simple yet robust recipe for stable and sustainable experience internalization, providing concrete guidance for engineering self-evolving and continually learning LLMs.

</details>

---

### [[20_Research/Papers/大模型/SMADE-IE_Sparse_Multi-Agent_Framework_with_Evidence-Driven_Debate_for_Zero-Shot_Information_Extraction|SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction]]

![[assets/2606.04691_figure.png|800]]

- **arXiv**: [2606.04691](https://arxiv.org/abs/2606.04691)
- **PDF**: https://arxiv.org/pdf/2606.04691
- **详细分析**: [[20_Research/Papers/大模型/SMADE-IE_Sparse_Multi-Agent_Framework_with_Evidence-Driven_Debate_for_Zero-Shot_Information_Extraction|SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction]]
- **作者**: Kenfeng Huang, Yi Cai, Xin Wu, Zikun Deng, Li Yuan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《SMADE-IE: Sparse Multi-Agent Framework with Evidence-Driven Debate for Zero-Shot Information Extraction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot information extraction (IE) with large language models (LLMs) has attracted increasing attention due to its flexibility in adapting to new schemas and domains without task-specific training. Existing approaches mainly rely on monolithic prompting, each-type prompting, or multi-agent debate. However, monolithic prompting often suffers from boundary and type errors, while each-type prompting and multi-agent debate introduce cross-type conflicts, redundant agent interactions, and substantial token overhead. To address these challenges, we propose SMADE-IE, a sparse and evidence-driven multi-agent framework for zero-shot IE. SMADE-IE first employs an Adaptive Mode Selector to dynamically route inputs into either a lightweight Global Extraction Mode or a Type-Centric Extraction Mode, reducing unnecessary type selection and reasoning noise. For conflicting predictions, we further introduce an Evidence-Driven Debate mechanism that structures arguments into Toulmin-style components and performs confidence aggregation through external evidence scoring and Bayesian updates. Experimental results on 9 benchmark datasets across NER, RE, and JERE tasks show that SMADE-IE consistently outperforms existing zero-shot IE baselines while also improving token efficiency through sparse agent selection and early-stopping debate.

</details>

---

### [[20_Research/Papers/强化学习/Read_the_Trace,_Steer_the_Path_Trajectory-Aware_Reinforcement_Learning_for_Diffusion_Language_Models|Read the Trace, Steer the Path: Trajectory-Aware Reinforcement Learning for Diffusion Language Models]]

![[assets/2606.04396_first_page.png|800]]

- **arXiv**: [2606.04396](https://arxiv.org/abs/2606.04396)
- **PDF**: https://arxiv.org/pdf/2606.04396
- **详细分析**: [[20_Research/Papers/强化学习/Read_the_Trace,_Steer_the_Path_Trajectory-Aware_Reinforcement_Learning_for_Diffusion_Language_Models|Read the Trace, Steer the Path: Trajectory-Aware Reinforcement Learning for Diffusion Language Models]]
- **作者**: Anant Khandelwal, Manish Gupta
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Read the Trace, Steer the Path: Trajectory-Aware Reinforcement Learning for Diffusion Language Models》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion large language models (dLLMs) generate responses by iteratively unmasking and revising many positions in parallel. This process leaves a rich denoising trace depicting which tokens become confident, which remain unstable, and when commitments form. Existing dLLM reinforcement learning methods use this signal only weakly. Flat rollouts are cheap, but assign a single outcome reward to the whole trajectory. Tree rollouts provide finer, verifiable training signals by branching partial trajectories and propagating leaf rewards upward, but are compute intensive. We ask whether the denoising trace itself can provide tree-like supervision without tree-level compute. We introduce CAPR (Cached-Amortized Path Refinement), a dLLM-RL algorithm that summarizes the denoising trace into a compact path state, uses cached trajectory states to generate cheap sibling continuations, and trains a block-level value head for local block-wise supervision. Under a block-wise unmasking schedule, CAPR records path-state and block-progress features, then redistributes the final outcome reward across blocks according to the tokens revealed in each block. This trains the value head to convert one sparse reward into block-level PPO weights. CAPR therefore recovers much of the granularity of tree search while avoiding full tree expansion, reducing rollout-generation cost to roughly 0.75x that of flat rollouts and 0.6x that of tree rollouts (under standard settings). Across 4x4 Sudoku, Countdown, GSM8K, and Math500, on dense and mixture-of-experts LLaDA backbones, CAPR sets a new state of the art for RL-tuned dLLMs at 256- and 512-token budgets. On Sudoku, it matches the strongest tree-structured baseline at less than one third of the per-step compute.

</details>

---

### [[20_Research/Papers/大模型/LazyAttention_Efficient_Retrieval-Augmented_Generation_with_Deferred_Positional_Encoding|LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding]]

![[assets/2606.04302_first_page.png|800]]

- **arXiv**: [2606.04302](https://arxiv.org/abs/2606.04302)
- **PDF**: https://arxiv.org/pdf/2606.04302
- **详细分析**: [[20_Research/Papers/大模型/LazyAttention_Efficient_Retrieval-Augmented_Generation_with_Deferred_Positional_Encoding|LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding]]
- **作者**: Haocheng Xia, Mihir Pamnani, Hanxi Fang, Supawit Chockchowwat, Yongjoo Park
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Systems

#### 研究背景与动机

《LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Key-value (KV) caching accelerates inference of large language models (LLMs) by reusing past computations for generated tokens. Its importance becomes even greater in long-context applications such as retrieval-augmented generation (RAG) and in-context learning (ICL). However, conventional KV caching embeds positional information directly into the cache, limiting its reusability. Existing solutions either restrict reuse to prefixes or require expensive memory materialization for positional re-encoding. We introduce LazyAttention, a novel attention mechanism that kernelizes deferred positional encoding to enable zero-copy, position-agnostic KV reuse. By adjusting positional encoding within attention kernels on-the-fly, LazyAttention resolves the materialization bottleneck, allowing a single physical KV copy to serve multiple logical requests at arbitrary positions. Leveraging attention kernels tailored for prefilling and decoding, our system achieves significant efficiency improvements: under skewed document distributions, it reduces time-to-first-token (TTFT) by 1.37$\times$ and increases inference throughput by 1.40$\times$ compared to the state-of-the-art Block-Attention, while maintaining comparable output quality.

</details>

---

### [[20_Research/Papers/大模型/Exploring_the_Topology_and_Memory_of_Consensus_How_LLM_Agents_Agree,_Fragment,_or_Settle_When_Forming_Conventions|Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions]]

![[assets/2606.04197_figure.png|800]]

- **arXiv**: [2606.04197](https://arxiv.org/abs/2606.04197)
- **PDF**: https://arxiv.org/pdf/2606.04197
- **详细分析**: [[20_Research/Papers/大模型/Exploring_the_Topology_and_Memory_of_Consensus_How_LLM_Agents_Agree,_Fragment,_or_Settle_When_Forming_Conventions|Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions]]
- **作者**: Aliakbar Mehdizadeh, Martin Hilbert
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How much should an LLM agent remember, and how should multi-agent systems be connected when trying to reach consensus? We show these two design choices interact in a way that flips the sign of memory's effect on coordination. Across 432 simulation runs of a networked Naming Game on eight fixed 16-agent topologies, we vary memory depth and network structure. Longer memory slows the time to reach steady state in decentralized networks but accelerates it in centralized ones; the same parameter pushes the system in opposite directions depending on topology. Critically, "faster settling" in centralized networks means locking in to a fragmented plateau more quickly, not reaching system-wide consensus, which can be used to generate diverging opinions. We further document a memory-mediated speed-unity trade-off: centralized networks consistently preserve more competing conventions than decentralized networks, but their settling speed depends sharply on memory. At the agent level, within-network analyses show that high-betweenness bridges suffer a brokerage penalty while agents in locally clustered neighborhoods achieve higher coordination success. Finally, in search of analytically tractable generative mechanisms, we find that agents' choices are well captured by Fictitious Play, indicating belief-based rather than reward-based adaptation. The practical implication: memory depth and communication topology should be co-designed, not optimized in isolation.

</details>

---

### [[20_Research/Papers/大模型/When_Retrieval_Doesn't_Help_A_Large-Scale_Study_of_Biomedical_RAG|When Retrieval Doesn't Help: A Large-Scale Study of Biomedical RAG]]

![[assets/2606.04127_first_page.png|800]]

- **arXiv**: [2606.04127](https://arxiv.org/abs/2606.04127)
- **PDF**: https://arxiv.org/pdf/2606.04127
- **详细分析**: [[20_Research/Papers/大模型/When_Retrieval_Doesn't_Help_A_Large-Scale_Study_of_Biomedical_RAG|When Retrieval Doesn't Help: A Large-Scale Study of Biomedical RAG]]
- **作者**: Erfan Nourbakhsh, Rocky Slavin, Ke Yang, Anthony Rios
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.CL

#### 研究背景与动机

《When Retrieval Doesn't Help: A Large-Scale Study of Biomedical RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MASH-QA, MashQA, MedMCQA, MedQA, MedRedQA, MedicationQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical question answering is a high-stakes setting where factual errors can have serious consequences. Retrieval-augmented generation (RAG) is widely viewed as a promising solution, and prior work has reported substantial gains for large medical QA models. We revisit this assumption across a broad range of open-weight instruction-tuned models spanning 7B to 72B parameters. Across five models, ten biomedical QA datasets, four retrieval methods, and four retrieval corpora, we find that retrieval yields only small and inconsistent improvements over a no-retrieval baseline, typically within 1-2 points. In contrast, the choice of backbone model has a much larger effect than the choice of retriever or corpus, and expert and layman retrieval sources perform similarly in most settings. These results suggest that the main bottleneck is not retrieval quality alone, but the model's limited ability to use retrieved evidence effectively.

</details>

---
