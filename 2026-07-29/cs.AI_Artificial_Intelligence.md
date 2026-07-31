# cs.AI | Artificial Intelligence | 2026-07-29

#arxiv #ComputerScience

**论文数**: 49

### [[20_Research/Papers/大模型/CHARM_A_Multimodal_Graph_Foundation_Model_with_Hierarchical_Context_Modeling_for_Zero-Shot_Transfer|CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer]]

![[assets/2607.26023_figure.png|800]]

- **arXiv**: [2607.26023](https://arxiv.org/abs/2607.26023)
- **PDF**: https://arxiv.org/pdf/2607.26023
- **详细分析**: [[20_Research/Papers/大模型/CHARM_A_Multimodal_Graph_Foundation_Model_with_Hierarchical_Context_Modeling_for_Zero-Shot_Transfer|CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer]]
- **作者**: Ankang Yang, Jitao Zhao, Di Jin, Yuxiao Huang, Dongxiao He
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored. Existing GNN-based graph foundation models typically require downstream adaptation, whereas LLM-based graph methods mainly address unimodal graphs or tasks within a single domain. This setting presents two key challenges. First, models must generalize knowledge from individual modalities while capturing transferable cross-modal relations. Second, without target-domain fine-tuning, node representations remain entangled with domain-specific structures and modality-specific characteristics, obscuring shared concepts in unseen domains. To address these challenges, we propose CHARM, a multimodal graph foundation model with hierarchical context modeling for zero-shot transfer. CHARM replaces isolated raw nodes with hierarchical graph contexts that capture multimodal semantics and cross-modal relations. These contexts map domain-specific node patterns to shared high-level concepts, reducing reliance on target-domain supervision or adaptation. A modality-aware graph context encoder integrates multimodal information with graph structure and converts the resulting representations into graph tokens for a large language model . Experiments show consistent improvements on zero-shot multimodal graph tasks.

</details>

---

### [[20_Research/Papers/大模型/MemLens_A_Value-Aware_Memory_Management_System_with_Interactive_Analytics_for_LLM-based_Agents|MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents]]

![[assets/2607.25992_figure.png|800]]

- **arXiv**: [2607.25992](https://arxiv.org/abs/2607.25992)
- **PDF**: https://arxiv.org/pdf/2607.25992
- **详细分析**: [[20_Research/Papers/大模型/MemLens_A_Value-Aware_Memory_Management_System_with_Interactive_Analytics_for_LLM-based_Agents|MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents]]
- **作者**: Shuyue Wei, Chang Liu, Zimu Zhou, Yongxin Tong, Lizhen Cui
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EduMemBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse. However, existing LLM memory systems typically adopt a coarse-grained (utility-agnostic) manner that treats heterogeneous user-LLM interaction records uniformly, leading to redundant and low-impact records persisting in the memory repository. To address this challenge, we present MemLens, a value-aware memory management system that takes memory records as first-class data objects. MemLens provides an end-to-end interactive analytics dashboard that exposes the complete memory lifecycle, including Shapley-style memory evaluation, value-aware storage, and memory-assisted response. Through a study-copilot application, the system enables users to inspect memory values, visualize hierarchical memory structures, and compare various memory management strategies in terms of response quality, retrieval latency, and token consumption. Therefore, our MemLens can serve as an efficient, interpretable, and personalized long-term memory management system for LLM-based agents.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Code_Optimization|Reinforcement Learning for Code Optimization]]

![[assets/2607.25970_first_page.png|800]]

- **arXiv**: [2607.25970](https://arxiv.org/abs/2607.25970)
- **PDF**: https://arxiv.org/pdf/2607.25970
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Code_Optimization|Reinforcement Learning for Code Optimization]]
- **作者**: Pierre Chambon, Kunhao Zheng, Juliette Decugis, Benoit Sagot, Gabriel Synnaeve
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning for Code Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforward: just add execution time to the reward. But in practice, once timing drives the reward, small problems in measurement noise, reward sparsity, or GRPO instability overwhelm the signal and make RL fail: generated solutions are barely faster, and more of them can fail. We make execution time learnable through three stages: (1) how code is tested, by building DMC-Optim with large optimization tests and a calibrated sandbox; (2) how speed is turned into reward, by composing correctness and speed in the RL environment and using an offline simulator to predict the most promising configurations; and (3) how the model learns from that reward, by adapting GRPO and evaluation to the sparser, noisier timed-execution setting. On DMC-Optim, the strongest optimization-aware configurations improve strict top-50% pass@1 from 18.0% to 31.3% on Qwen 2.5 7B and from 30.7% to 50.4% on CWM 32B. These gains further increase at stricter percentiles such as top-30%, with 125% relative improvement for CWM 32B, while preserving pure-correctness scores. When the timing sandbox is degraded, robust optimization RL reaches 100% to 200% improvement over standard RLVR, depending on the evaluation criterion. On LCB, CWM 32B wins up to 83% of median-sample speed comparisons against standard RLVR. Relative to the fastest correct human submissions per problem, it reaches about half the human rate of complexity-class improvements (14% vs. 28%).

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_for_Operations_Research_Formulation_Selection_in_Multi-Warehouse_Inventory_Allocation|Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation]]

![[assets/2607.25956_figure.png|800]]

- **arXiv**: [2607.25956](https://arxiv.org/abs/2607.25956)
- **PDF**: https://arxiv.org/pdf/2607.25956
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_for_Operations_Research_Formulation_Selection_in_Multi-Warehouse_Inventory_Allocation|Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation]]
- **作者**: Jintao Xu, Yingzheng Ma, Jiong Dong, Yongzhi Qi, Jianshen Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.9，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-warehouse inventory allocation is typically formulated as a mixed-integer programming (MIP) problem, yet no single formulation consistently matches heterogeneous instance-level regimes induced by demand concentration, inventory imbalance, replenishment scale, service constraints, and forecast volatility. We study this issue as instance-wise operations research (OR) formulation selection, where each allocation instance is assigned to a solver-executable formulation from a candidate OR expert library. We propose a solver-guided large language model (LLM) framework for OR formulation selection, in which each OR expert corresponds to a MIP formulation encoding a distinct allocation priority. To train the selector, the framework first constructs balanced expert-conditioned supervised fine-tuning (SFT) records for schema learning, and then uses MIP solver evaluation on historical instances to convert solver-evaluated allocation-quality gaps into margin-weighted identity preference optimization (IPO) preferences and per-instance expert-score metadata for reward lookup during group relative policy optimization (GRPO) to assign rewards to sampled responses. Experiments on multi-warehouse inventory allocation instances from JD$\mathord{.}$com, one of China's largest e-retailers, demonstrate that GRPO substantially improves expert-selection accuracy relative to the SFT+IPO selector and, more importantly, produces higher realized allocation quality than both the preference-trained selector and the best fixed formulation. With GRPO, Hit Ratio@1 and Hit Ratio@2 increase from 21.45% to 50.42% and from 70.47% to 82.31%. The resulting selector achieves an allocation accuracy gain of 12.57 percentage points over the incumbent baseline, outperforming both the SFT+IPO selector and the best fixed OR expert, and reduces the gap to the ex-post oracle to 4.85 percentage points.

</details>

---

### [[20_Research/Papers/大模型/A_Cost-Effective_Multimodal_LLM_Reasoning_Framework_for_Question_Answering_over_Irregular_Clinical_Time_Series|A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series]]

![[assets/2607.25947_figure.png|800]]

- **arXiv**: [2607.25947](https://arxiv.org/abs/2607.25947)
- **PDF**: https://arxiv.org/pdf/2607.25947
- **详细分析**: [[20_Research/Papers/大模型/A_Cost-Effective_Multimodal_LLM_Reasoning_Framework_for_Question_Answering_over_Irregular_Clinical_Time_Series|A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series]]
- **作者**: Frank Nie, Ethan B Liu, Yuan Zhu, Wei Fan, Jindong Han
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Question answering (QA) over irregular clinical time series (ICTS) plays a pivotal role in a wide range of healthcare applications. Although recent multimodal time-series large language models (LLMs) have shown considerable promise in general-purpose time-series QA, they remain poorly equipped to model the sparsity, asynchrony, and irregular sampling patterns of clinical observations. To fill this gap, we propose ClinPRISM, a cost-effective multimodal LLM reasoning framework for question answering over ICTS data. First, we devise an irregularity-aware multi-scale encoder to capture sparse clinical evidence at diverse temporal scales. Then, we propose a temporal evidence distiller to integrate representations across these scales and compress them into a small number of LLM-compatible tokens. Moreover, we introduce a progressive alignment strategy that sequentially aligns the irregular trajectories with the LLM's textual embedding space. To facilitate training, we construct 30,000 clinical time series paired with multi-scale descriptions, together with 41,000 instruction-tuning instances spanning 11 tasks. Using a 4-billion-parameter LLM backbone, ClinPRISM achieves state-of-the-art performance on the held-out evaluation benchmark while using only 16 time-series tokens and achieving an average inference latency of 0.15 seconds per question.

</details>

---

### [[20_Research/Papers/具身智能/SAM3D-Guided_Object-Centric_Representation_Alignment_for_Vision-Language-Action_Models|SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models]]

![[assets/2607.25912_figure.png|800]]

- **arXiv**: [2607.25912](https://arxiv.org/abs/2607.25912)
- **PDF**: https://arxiv.org/pdf/2607.25912
- **详细分析**: [[20_Research/Papers/具身智能/SAM3D-Guided_Object-Centric_Representation_Alignment_for_Vision-Language-Action_Models|SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models]]
- **作者**: Zonghe Liu, Shanyuan Jie, Xiaoquan Sun, Chen Cao, Zetian Xu, Zongsheng Liu, Jiayu Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BridgeVLA, SAM3D-VLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training. Specifically, we localize task-relevant objects with object recognition models, generate corresponding object masks, and use SAM3D to extract dense object-level 3D representations, which are aligned with intermediate visual features of $π_0$. This enables the policy to internalize target-object 3D information while preserving the original RGB-language-to-action inference pipeline without requiring depth, point clouds, masks, SAM3D, or additional 3D modules at test time. Simulation experiments show consistent improvements, achieving 99.1\% on LIBERO and an average length of 4.11 on CALVIN. Real-world experiments further demonstrate that our method is particularly effective in long-horizon manipulation scenarios where the robot must focus on different target objects across multiple subtasks.

</details>

---

### [[20_Research/Papers/强化学习/Interactive_Reward_Agent_GUI_Task_Evaluation_via_Environment-State_Verification|Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification]]

![[assets/2607.25904_figure.png|800]]

- **arXiv**: [2607.25904](https://arxiv.org/abs/2607.25904)
- **PDF**: https://arxiv.org/pdf/2607.25904
- **详细分析**: [[20_Research/Papers/强化学习/Interactive_Reward_Agent_GUI_Task_Evaluation_via_Environment-State_Verification|Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification]]
- **作者**: Chenrui Shi, Yuwei Wu, Yang Liu, Ruining Feng, Zirui Shang, Zhi Gao, Lifeng Fan, Che Sun
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GUI-RewardBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because the evaluation results can serve as reward signals for both test-time scaling and post-training. However, reliable GUI task evaluation remains challenging because the judgments often require access to environment states, such as system configurations, file data, and application settings, beyond the screenshots of execution trajectories. In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment. Given a task instruction and a GUI environment after the GUI agent execution, IRA first proposes the task completion conditions and then verifies them by invoking system tools, application tools, and GUI tools. This design combines evidence from both visible interfaces and the environment state in an interactive process. We further introduce GUI-RewardBench, a benchmark of 321 GUI task trajectories spanning 10 Ubuntu desktop application categories. Experiments show that IRA achieves 86.9% accuracy on GUI-RewardBench, outperforming existing evaluator baselines. We further apply IRA to reinforcement learning of GUI agents, achieving a 34.0% OSWorld success rate, which demonstrates that IRA can provide effective reward signals for training GUI agents.

</details>

---

### [[20_Research/Papers/大模型/Runtime_Uncertainty_Monitoring_for_LLM-Based_Multi-Agent_Systems_Using_Bayesian_Networks|Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks]]

![[assets/2607.25877_figure.png|800]]

- **arXiv**: [2607.25877](https://arxiv.org/abs/2607.25877)
- **PDF**: https://arxiv.org/pdf/2607.25877
- **详细分析**: [[20_Research/Papers/大模型/Runtime_Uncertainty_Monitoring_for_LLM-Based_Multi-Agent_Systems_Using_Bayesian_Networks|Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks]]
- **作者**: Bart Custers, Koorosh Aslansefat
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

</details>

---

### [[20_Research/Papers/大模型/HiSkill_Empowering_LLM_Agents_with_Hierarchical_Skill_Graphs|HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs]]

![[assets/2607.25853_figure.png|800]]

- **arXiv**: [2607.25853](https://arxiv.org/abs/2607.25853)
- **PDF**: https://arxiv.org/pdf/2607.25853
- **详细分析**: [[20_Research/Papers/大模型/HiSkill_Empowering_LLM_Agents_with_Hierarchical_Skill_Graphs|HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs]]
- **作者**: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld, SkillNet, SkillRL, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at https://github.com/BUPT-GAMMA/HiSkill.

</details>

---

### [[20_Research/Papers/大模型/Speculate_While_You_Reason_Teaching_Agents_to_Predict_Their_Next_Tool_Call_via_Joint_Agent-Speculator_RL|Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL]]

![[assets/2607.25816_figure.png|800]]

- **arXiv**: [2607.25816](https://arxiv.org/abs/2607.25816)
- **PDF**: https://arxiv.org/pdf/2607.25816
- **详细分析**: [[20_Research/Papers/大模型/Speculate_While_You_Reason_Teaching_Agents_to_Predict_Their_Next_Tool_Call_via_Joint_Agent-Speculator_RL|Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL]]
- **作者**: Jiabao Ji, Yujian Liu, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.2（加权：大模型 1，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SearchQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. We identify this speculator-agent gap and show that the target agent itself is a strong next-call speculator. This points to a simpler design: unifying the agent and speculator within the same model. In this paper, we introduce the self-speculating agent, a single model that both solves tasks in agent mode and predicts its next tool call from partial trajectories in speculator mode, fully reusing prefix KV cache. To enable this dual-mode agent without degrading performance, we propose a joint agent-speculator reinforcement learning method, which derives speculation targets from the agent's own rollouts and alternates agent and speculator updates. Across agentic search QA and conversational tool-use agentic tasks, our method improves average next tool-call Hit@1 from 44.1 to 61.2 for Qwen3-4B and from 48.9 to 66.3 for Qwen3.5-4B, while preserving agent task success.

</details>

---

### [[20_Research/Papers/具身智能/Shared_Voxel-Map-Based_Cooperative_Indoor_UAV_Guidance_with_a_Multi-Agent_Soft_Actor-Critic_Controller|Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller]]

![[assets/2607.25728_figure.png|800]]

- **arXiv**: [2607.25728](https://arxiv.org/abs/2607.25728)
- **PDF**: https://arxiv.org/pdf/2607.25728
- **详细分析**: [[20_Research/Papers/具身智能/Shared_Voxel-Map-Based_Cooperative_Indoor_UAV_Guidance_with_a_Multi-Agent_Soft_Actor-Critic_Controller|Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller]]
- **作者**: Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型, 世界模型
- **相关性评分**: 3.42（加权：具身智能 0.6，大模型 0.4，强化学习 0.96，世界模型 0.36，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a cooperative indoor UAV guidance framework that combines a shared voxel-map world model with a multi-agent Soft Actor-Critic (MASAC) controller. Multiple drones fuse 360 LiDAR observations into a common world-frame occupancy map, which is converted into a compact bird's-eye-view (BEV) representation and provided to each agent as an ego-aligned local crop. This integrate-in-world, act-in- ego design enables consistent multi-UAV spatial fusion whilst retaining decentralised continuous control. The policy combines BEV map features, near-field obstacle observations, and compact goal and peer-state information within a centralised-training, decentralised-execution framework. In simulation, the learned controller achieves a 90.3% success rate in corridor navigation, outperforming Astar planning, an artificial potential field controller, and a prior guidance method. To address residual sim-to-real mismatch, the simulation-trained policy is further adapted using offline imitation fine-tuning from real-world data. Real-world experiments in GNSS-denied indoor environments demonstrate stable two-UAV cooperative operation across increasingly chal- lenging obstacle layouts. The results show that shared voxel-map representations provide an effective and scalable spatial substrate for learned cooperative indoor UAV guidance.

</details>

---

### [[20_Research/Papers/大模型/Tools_Are_Not_Islands_Set-Level_Tool_Retrieval_for_LLM_Agents_via_Query-Conditioned_Hyperedge_Prediction|Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction]]

![[assets/2607.25718_figure.png|800]]

- **arXiv**: [2607.25718](https://arxiv.org/abs/2607.25718)
- **PDF**: https://arxiv.org/pdf/2607.25718
- **详细分析**: [[20_Research/Papers/大模型/Tools_Are_Not_Islands_Set-Level_Tool_Retrieval_for_LLM_Agents_via_Query-Conditioned_Hyperedge_Prediction|Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction]]
- **作者**: Xinyi Hong, Pinjun Dong, Xinyang Yu, Binyan Jiang
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET, short for HYperedge-based SEt-level Tool retrieval. Our contributions are threefold: (i) we formulate tool retrieval as query-conditioned hyperedge prediction on a tool co-invocation hypergraph, under which the tool set itself becomes the unit of scoring and most existing retrieval paradigms reduce to restricted instances; (ii) we capture size-dependent tool compatibility through cardinality-specific interactions; and (iii) we design HYSET as a pre-selection module requiring no modification to the downstream agent. Experiments on ToolBench demonstrate that HYSET consistently outperforms state-of-the-art baselines in both tool retrieval performance and end-to-end task success. Beyond the in-domain setting, HYSET further supports zero-shot/few-shot transfer, generalizing to held-out tools/categories and unseen domains with minimal supervision.

</details>

---

### [[20_Research/Papers/大模型/CoRT_Counterfactual_Replay_for_Token-Level_Rubric-Guided_Policy_Optimization|CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization]]

![[assets/2607.25659_figure.png|800]]

- **arXiv**: [2607.25659](https://arxiv.org/abs/2607.25659)
- **PDF**: https://arxiv.org/pdf/2607.25659
- **详细分析**: [[20_Research/Papers/大模型/CoRT_Counterfactual_Replay_for_Token-Level_Rubric-Guided_Policy_Optimization|CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization]]
- **作者**: Bo-Wen Zhang, Junwei He, Wen Wang, Song-Lin Lv, Wentao Ma, Rongyi Lin, Shuhan Zhong, Lan-Zhe Guo
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria. Yet in GRPO-style pipelines, these structured judgments are reduced to a scalar response-level reward and converted into a response-level advantage, which is broadcast uniformly to all generated tokens. This leaves no explicit mechanism for allocating credit within a response, even when different criteria are grounded in different spans, formatting decisions, or semantic choices. We propose CoRT, a token-level credit weighting method for rubric-conditioned GRPO. Instead of training an auxiliary token scoring model, CoRT uses counterfactual replay to rescore the same sampled response under the original rubric-conditioned prompt and a matched criteria-free prompt. The resulting tokenwise log-likelihood contrasts serve as a proxy for dependence on the rubric context. CoRT maps these contrasts to bounded, response-normalized weights and uses them to redistribute the signed GRPO advantage across tokens, without introducing an auxiliary scorer or changing the response-level reward. Experiments across instruction-tuned models and reward granularities show that CoRT improves over matched response-level GRPO in the vast majority of comparisons, with an average gain of 4.4 percentage points. The method remains competitive with learned token-level credit baselines while avoiding a separate relevance-learning stage. These results suggest that policy-internal counterfactual likelihood contrasts provide an effective training signal for within-response credit allocation while retaining the simplicity and stability of GRPO.

</details>

---

### [[20_Research/Papers/大模型/A_Human-in-the-Loop_Corpus_for_LLM-Based_Simplification_of_Scientific_Summaries|A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries]]

![[assets/2607.25630_figure.png|800]]

- **arXiv**: [2607.25630](https://arxiv.org/abs/2607.25630)
- **PDF**: https://arxiv.org/pdf/2607.25630
- **详细分析**: [[20_Research/Papers/大模型/A_Human-in-the-Loop_Corpus_for_LLM-Based_Simplification_of_Scientific_Summaries|A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries]]
- **作者**: Kyuri Im, Michael Färber
- **cs 子类**: cs.AI, cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SciSummNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interdisciplinary research is accelerating, yet scientific papers remain difficult to understand outside their home fields. We study large language model (LLM)-based simplification of scientific texts and present a human-in-the-loop workflow that transforms expert summaries into more accessible versions for non-specialists. Using SciSummNet as the source corpus, we first generate baseline simplifications with GPT-4o-mini. In Phase 1, readers from STEM fields outside computer science identify difficult sentences and phrases and compare the original and GPT-simplified summaries in terms of comprehensibility, naturalness, and simplicity. In Phase 2, computer science experts use this feedback to create expert-edited reference simplifications. We release the resulting corpus together with human judgments and automatic evaluation results. The Phase 1 judgments show a clear preference for the GPT-generated summaries in terms of comprehensibility and simplicity, while qualitative analysis of the Phase 2 edits highlights the importance of preserving domain-specific terminology and the strength of scientific claims. The resulting resource supports the training and benchmarking of simplification systems for cross-disciplinary scientific communication.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Epistemia_Epistemic_Schizologia_and_Large_Language_Models_as_Techno-Semiotic_Machines|Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines]]

![[assets/2607.25620_first_page.png|800]]

- **arXiv**: [2607.25620](https://arxiv.org/abs/2607.25620)
- **PDF**: https://arxiv.org/pdf/2607.25620
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Epistemia_Epistemic_Schizologia_and_Large_Language_Models_as_Techno-Semiotic_Machines|Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines]]
- **作者**: Federico Cabitza, Gianluca Colombo
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.7（加权：具身智能 0.3，大模型 0.4）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quattrociocchi and colleagues warn that the fluent outputs of large language models may allow linguistic plausibility to substitute for epistemic evaluation, producing the condition they call *Epistemia*: the experience of possessing knowledge without undertaking the practices through which judgment would ordinarily be warranted. This article accepts that diagnosis but challenges its explanatory framework, which compares an embodied, socially situated human knower with an isolated generative model thereby locating epistemic legitimacy in capacities internal to autonomous agents. Drawing on Carlo Sini's philosophy of practices, writing, signs, and technics, we propose instead to understand a large language model (LLM) as a *techno-semiotic machine* that automates a phase of written semiosis by producing plausible linguistic configurations from the sedimented archive of human writing. From this perspective, *Epistemia* is one consequence of a broader phenomenon that we call *epistemic schizologia*: the socio-technical cleavage between signs as linguistically accomplished expressions and signs as moments within socially embedded circuits of interpretation, evidence, criticism, verification, and responsibility. This cleavage is reinforced by *eikotic closure*, through which a plausible continuation is presented with the finality of an epistemic result, and by algorithmic authority and epistemic self-misrecognition. The relevant unit is therefore not the model alone but the complete practice in which generated inscriptions are prompted, interpreted, verified, contested, used, and made consequential. This reframing preserves the distinction between linguistic production and responsible understanding while grounding a design programme centred on inspectable genealogy, contestability, distributed responsibility, epistemic agency, and the evaluation of hybrid human--AIpractices.

</details>

---

### [[20_Research/Papers/机器人/ReLATE_Reliability-Guided_Evidence_Fusion_for_Robust_UAV--Satellite_cross-view_Geo-Localization|ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization]]

![[assets/2607.25524_figure.png|800]]

- **arXiv**: [2607.25524](https://arxiv.org/abs/2607.25524)
- **PDF**: https://arxiv.org/pdf/2607.25524
- **详细分析**: [[20_Research/Papers/机器人/ReLATE_Reliability-Guided_Evidence_Fusion_for_Robust_UAV--Satellite_cross-view_Geo-Localization|ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization]]
- **作者**: Haochen Jiang, Jialei Pan, Yuzhe Sun, Zhe Dong, Lecheng Ren, Yanfeng Gu, Tianzhu Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, MuSe-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV)-satellite cross-view geo-localization matches UAV images against satellite imagery and has achieved impressive accuracy on clean (non-degraded) image benchmarks. In real-world flights, however, UAV observations are frequently affected by adverse weather, illumination changes, platform motion, sensor noise, and compression, while the robustness of existing methods under such degradations remains largely unexamined. In this paper, we present UAVSat-Deg, a large-scale robustness benchmark for degraded UAV-satellite geo-localization, comprising University-1652-Deg and SUES-200-Deg. UAVSat-Deg covers 27 corruption types, including 19 core and 8 compound corruptions, at three severity levels, supports bidirectional drone-to-satellite and satellite-to-drone retrieval as well as multi-height UAV acquisition, and contains more than 11.7 million pre-generated corrupted test images. Benchmarking representative methods under this protocol reveals substantial robustness gaps, particularly under severe and compound corruptions. To address this problem, we propose ReLATE, a Reliable Evidence Learning framework with Adaptive Token Evidence Regulation, which realizes reliability-adaptive feature fusion during descriptor construction. ReLATE estimates a structure-smoothed reliability field over visual tokens, aggregates trustworthy local evidence, and adaptively integrates it into query-derived representations; the regulated query representations are then combined with the CLS-token and GeM-pooled branches to form the final cross-view descriptor. Across both test sets and retrieval directions, ReLATE achieves the best average corrupted-test performance among the compared methods while maintaining competitive accuracy on clean images. The code and dataset will be available at https://github.com/JHC626/ReLATE.

</details>

---

### [[20_Research/Papers/具身智能/CoTinyVLA_Chain-of-Thought_Distillation_for_a_Sub-Billion-Parameter_Vision-Language-Action_Model|CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model]]

![[assets/2607.25487_figure.png|800]]

- **arXiv**: [2607.25487](https://arxiv.org/abs/2607.25487)
- **PDF**: https://arxiv.org/pdf/2607.25487
- **详细分析**: [[20_Research/Papers/具身智能/CoTinyVLA_Chain-of-Thought_Distillation_for_a_Sub-Billion-Parameter_Vision-Language-Action_Model|CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model]]
- **作者**: Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi, Donghwan Hwang, Donghun Ryu, Seokhyun Kim
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.5，机器人 0.4）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoTinyVLA, CronusVLA, OpenVLA, RIPT-VLA, SmolVLA, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. Three components target different axes of the problem: dual-view temporal input of 16 history frames per step with textual camera and time markers; hierarchical chain-of-thought (CoT) distillation from a 35B teacher into an episode-level Plan and a chunk-level Think span over task phase, gripper state and next subaction; and paraphrase augmentation expanding 40 base commands into 800 variants. On LIBERO-Plus, spanning 10,030 perturbed tasks across seven perturbation dimensions, CoTinyVLA reaches 90.8% on Spatial, 87.3% on Object, 86.6% on Goal and 80.7% on Long, leading the strongest 7B baseline on all four suites by 4.7, 2.8, 15.9 and 3.0 points, with every margin interval excluding zero. The gains concentrate on the hardest axes of the benchmark: across the eleven published baselines none exceeds 53.2% on Robot Initial States in any suite, whereas CoTinyVLA reaches 73.6% on Goal against 39.9% for the strongest baseline. Ablations show the three components to be separable by perturbation axis, and at a matched image budget how frames are divided between the two cameras and across time accounts for 8.6 points on its own. Closed-loop inference peaks at 2.25 GiB of allocated GPU memory, and paired interventions show the episode Plan to be load-bearing: replacing it with an empty or contradictory span costs 40 to 45 points of success. Structured supervision thus lets a 0.9B backbone exceed all of them. Code: https://github.com/BrainJellyPie/CoTinyVLA

</details>

---

### [[20_Research/Papers/大模型/PatientAgentBench_A_Benchmark_Framework_for_Evaluating_Patient-Facing_Health_AI_Agents|PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents]]

![[assets/2607.25485_figure.png|800]]

- **arXiv**: [2607.25485](https://arxiv.org/abs/2607.25485)
- **PDF**: https://arxiv.org/pdf/2607.25485
- **详细分析**: [[20_Research/Papers/大模型/PatientAgentBench_A_Benchmark_Framework_for_Evaluating_Patient-Facing_Health_AI_Agents|PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents]]
- **作者**: Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou, Mohammad Abuzar Hashemi, Prasad Kasu, Deepak Bansal, Daniel Lopez-Martinez, Anchal Nema, Ramya Ganesan, Will Kimbrough, Alex Woody, Yadunandana Rao...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ClinicalBench, FHIR-AgentBench, GMAI-MMBench, HealthAgentBench, HealthBench, MedAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation model, wrapped in an agent with a sandbox of healthcare tools, conversing with a simulated patient. Each conversation is scored by an LLM-as-a-Jury across six dimensions via over a hundred conversation-agnostic, clinician-grounded criteria. To validate alignment, licensed clinicians annotated shared conversations, yielding 79-93% adjacent agreement between jury and expert raters, on par with or exceeding clinician inter-rater agreement. We benchmarked 10 models across four families on the same 1,200 scenarios and found clinical gaps. Triage quality is the most discriminating dimension: pass rates rise from 32% for the weakest models to 88% for the strongest, with agents often acting on administrative requests without clinical screening. Clinical safety and workflow accuracy follow the same pattern: the weakest models fail often, fabricating unexecuted actions, while frontier models fail on only 1-3% of cases, from unverified tool outputs and omitted crisis resources in an emergency. More capable models narrow these gaps but do not close them; the strongest scores only 4.25 of 5 overall. These failures surface only in sustained, tool-using conversations against realistic patient records, confirming that static benchmarks are insufficient as healthcare agentic systems gain autonomy. We release the framework as a reproducible, clinician-validated evaluation standard to help the field close this gap.

</details>

---

### [[20_Research/Papers/大模型/Architectural_Backdoors_in_Vision-Language_Model_Supply_Chains_via_Representation_Steering|Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering]]

![[assets/2607.25479_figure.png|800]]

- **arXiv**: [2607.25479](https://arxiv.org/abs/2607.25479)
- **PDF**: https://arxiv.org/pdf/2607.25479
- **详细分析**: [[20_Research/Papers/大模型/Architectural_Backdoors_in_Vision-Language_Model_Supply_Chains_via_Representation_Steering|Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering]]
- **作者**: Maria Rosaria Briglia, Igor Maljkovic, Antonio Emanuele Cinà, Luca Oneto, Iacopo Masi, Fabio Roli
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TrojVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. In this paper, we show that a malicious provider can exploit this trust boundary by embedding architectural backdoors into VLM supply chains through representation steering. Our attack introduces dormant steering logic into the model architecture through a trigger-gated additive modification of an intermediate representation, without poisoning training data, controlling downstream fine-tuning, or modifying prompts at deployment time. When the trigger is absent, the modification reduces to zero and the model follows its normal computation, preserving clean utility. When the trigger is present, a steering direction shifts the internal representation toward an attacker-defined objective. We evaluate the attack across multiple VLM families and downstream tasks, including visual question answering, text-to-image generation, retrieval, and semantic response biasing. The results show that the proposed architectural steering backdoor compromises integrity, safety enforcement, and ranking fairness while preserving normal behavior on clean inputs. We further show that shared VLM artifacts can carry dormant steering logic against downstream services, and we propose an auditing defense that inspects the executable logic distributed with model artifacts rather than only their learned weights.

</details>

---

### [[20_Research/Papers/大模型/Toward_an_Organizational_Science_of_Multi-Agent_LLM_Systems_Decoupling_Who,_How,_and_Which_Algorithm|Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm]]

![[assets/2607.25446_figure.png|800]]

- **arXiv**: [2607.25446](https://arxiv.org/abs/2607.25446)
- **PDF**: https://arxiv.org/pdf/2607.25446
- **详细分析**: [[20_Research/Papers/大模型/Toward_an_Organizational_Science_of_Multi-Agent_LLM_Systems_Decoupling_Who,_How,_and_Which_Algorithm|Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm]]
- **作者**: Huan Chen, Xiang Song, Jian Jin, Pan Ren, Liang-Jie Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentsNet, MultiAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configuration, and the framework places six published collaboration algorithms behind a common interface while exposing roles, coordination, and accountability as independently configurable factors. We use this separation to conduct controlled comparisons in which organizational assignments vary while the collaboration protocol is held fixed. It also turns protocol choice into a variable that can be learned: Adaptive Org Routing, a contextual-bandit meta-protocol, selects a protocol per task under an explicit quality-cost tradeoff, outperforms every fixed protocol in a controlled study, and trains online on real benchmark and LLM-judge rewards. The ablations expose a mechanism. Accountability placement changes outcomes exactly when the protocol routes the deliverable through the accountable agent, and the winning placement flips across model families, so organizational design cannot be hard-coded; it must be revalidated, or learned, for each model binding.

</details>

---

### [[20_Research/Papers/大模型/A_Control_System,_a_Dataset,_and_a_Recipe_for_Making_Frozen_LLM_Agents_Learn_a_Domain|A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain]]

![[assets/2607.25415_figure.png|800]]

- **arXiv**: [2607.25415](https://arxiv.org/abs/2607.25415)
- **PDF**: https://arxiv.org/pdf/2607.25415
- **详细分析**: [[20_Research/Papers/大模型/A_Control_System,_a_Dataset,_and_a_Recipe_for_Making_Frozen_LLM_Agents_Learn_a_Domain|A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain]]
- **作者**: Debjyoti Paul
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HotpotQA, HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy. Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API. We take a narrower, more constrained position: treat the harness as a small, fixed, human-legible action space and learn a policy over it online with classic sample-efficient reinforcement learning (an $ε$-greedy contextual bandit and REINFORCE), scored against a multi-objective reward (task success, verifier score, policy compliance, cost, latency, and an unsupported-claim penalty). We instantiate this control system with DSPy (Khattab et al., 2024) as both the context assembler and the source of the strongest non-adaptive baseline (a DSPy BootstrapFewShot static prompt), and evaluate it across three verifiable task domains -- tool-use workflows, code generation (HumanEval), and multi-hop retrieval QA (HotpotQA) -- and two model providers (a local Ollama model and AWS Bedrock). We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup.

</details>

---

### [[20_Research/Papers/大模型/Context_Assembly_as_the_Controlled_Variable_A_Control-Theoretic_View_of_Harness_Policies_for_Frozen_LLM_Agents|Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents]]

![[assets/2607.25408_figure.png|800]]

- **arXiv**: [2607.25408](https://arxiv.org/abs/2607.25408)
- **PDF**: https://arxiv.org/pdf/2607.25408
- **详细分析**: [[20_Research/Papers/大模型/Context_Assembly_as_the_Controlled_Variable_A_Control-Theoretic_View_of_Harness_Policies_for_Frozen_LLM_Agents|Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents]]
- **作者**: Debjyoti Paul
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). We do not claim to introduce control theory to LLM agents -- that ship has sailed. Our narrower claim is about what the controlled variable is. Prior work controls tool selection, inter-agent message routing, or the agent's raw action stream. We instead treat context assembly itself -- which prompt template, which few-shot demonstrations, how much retrieved context, how many planning/verification passes -- as the controlled variable, learned online by a contextual bandit or REINFORCE policy sitting outside a frozen model. This paper develops the formal decomposition (inner frozen policy $π_θ$, outer context policy $π_φ$), gives a stability argument for the online controller in the sense used by Zhang et al. (2026) (non-decreasing expected reward under bounded policy change), and reports an uncertainty-calibration analysis of the controller's own confidence against realized task outcomes. The applied counterpart to this paper instantiates the same controller across three domains and two model providers and releases the dataset, trajectory logs, and a deployment recipe; here we focus on the formal framing and the stability/uncertainty evidence a control-theoretic claim requires.

</details>

---

### [[20_Research/Papers/大模型/COVENANT_Natural-Language_Workflow_Compilation_for_Aligned_Agent_Execution|COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution]]

![[assets/2607.25400_figure.png|800]]

- **arXiv**: [2607.25400](https://arxiv.org/abs/2607.25400)
- **PDF**: https://arxiv.org/pdf/2607.25400
- **详细分析**: [[20_Research/Papers/大模型/COVENANT_Natural-Language_Workflow_Compilation_for_Aligned_Agent_Execution|COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution]]
- **作者**: Jincheng Wang, Min Zheng, Tao Wei
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. As interactions accumulate, an agent can skip required steps, take unsupported branches, or execute a valid step with unsupported arguments or effects--a failure mode we call workflow misalignment. In this work, we propose COVENANT, a compiler-and-interpreter architecture for workflow-aligned agent execution. Our key insight is to treat workflow instructions as source programs rather than prompts. COVENANT converts the instructions into a workflow abstract syntax tree (WAST) and lowers it to a workflow control-flow graph (WCFG). At runtime, a controller interprets the WCFG one node at a time, checks each proposal against requirements extracted from the instructions before committing controller state or advancing the graph, and returns diagnostic feedback for repair. To evaluate COVENANT, we use 120 cases from three existing benchmarks, spanning seven workflow scenarios. Compared with state-of-the-art LLM agents, COVENANT improves benchmark success from 50.00% to 83.33% and reduces the workflow-misalignment failure rate from 42.50% to 15.83% (62.75% relative). These results show that COVENANT substantially mitigates workflow misalignment, moving LLM-agent alignment beyond isolated prompt following toward reliable execution of complex and multi-step workflows.

</details>

---

### [[20_Research/Papers/强化学习/ODYSSE_Episode-wise_Policy_Optimization_for_Personalized_Agentic_Reasoning|ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning]]

![[assets/2607.25369_figure.png|800]]

- **arXiv**: [2607.25369](https://arxiv.org/abs/2607.25369)
- **PDF**: https://arxiv.org/pdf/2607.25369
- **详细分析**: [[20_Research/Papers/强化学习/ODYSSE_Episode-wise_Policy_Optimization_for_Personalized_Agentic_Reasoning|ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning]]
- **作者**: Jiaqi Zhang, Tong Chen, Junliang Yu, Quoc Viet Hung Nguyen, Hongzhi Yin
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenClaw-RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users. However, unlike natural-world tasks that assume well-defined instructions, human-centered scenarios are characterized by ambiguous requests that lead to large, open-ended solution spaces. Decoding users' personalized preferences is therefore essential for narrowing the candidate solution space. This introduces a new challenge, personalized agentic reasoning, which requires agents to jointly interact with both users and environments to deliver personalized services. In this paper, we present ODYSSE, a Reinforced Fine-Tuning (RFT) framework for personalized agentic reasoning. At its core, ODYSSE proposes Episode-wise GRPO (ESPO), a novel extension of Group Relative Policy Optimization (GRPO) designed to address long action horizons and strong cross-step dependencies in personalized agentic reasoning. Rather than optimizing individual steps independently, ESPO introduces an episode-level reward mechanism together with episodic advantage estimation, enabling upstream evidence to effectively guide downstream personalized decisions and allowing agents to progressively resolve ambiguous user requests across multiple interaction steps. We further propose an episodic batch sampler that groups actions from the same episode into unified training batches, facilitating coherent optimization under ESPO. We evaluate ODYSSE on realistic long-horizon personalized GUI reasoning tasks. Experimental results demonstrate that ODYSSE consistently outperforms both specialist and general-purpose LVLMs, highlighting its effectiveness for personalized agentic reasoning.

</details>

---

### [[20_Research/Papers/大模型/CAST_Game_Solvers_as_Turn-Level_Teachers_for_LLM_Agents|CAST: Game Solvers as Turn-Level Teachers for LLM Agents]]

![[assets/2607.25308_figure.png|800]]

- **arXiv**: [2607.25308](https://arxiv.org/abs/2607.25308)
- **PDF**: https://arxiv.org/pdf/2607.25308
- **详细分析**: [[20_Research/Papers/大模型/CAST_Game_Solvers_as_Turn-Level_Teachers_for_LLM_Agents|CAST: Game Solvers as Turn-Level Teachers for LLM Agents]]
- **作者**: Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, Qi Gu, Xunliang Cai, Lan-Zhe Guo, Han-Jia Ye, Fuli Feng
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.95（加权：大模型 0.75，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CAST: Game Solvers as Turn-Level Teachers for LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training large language models (LLMs) to act in long-horizon games is a promising step toward generalist decision-making, yet reinforcement learning with verifiable rewards (RLVR) relies on sparse final rewards that reveal little about which decisions determine success. Denser process signals could supply this missing turn-level credit, but existing sources are hard to keep both cheap and accurate. We observe that changes in a game solver's state value reveal whether an action advances the state toward success. Building on this insight, we propose CAST (Credit Assignment from Solver Teachers), which converts these value changes into solver advantages and injects them into RLVR as turn-level signals. We further show that, under a soft-optimal solver assumption, maximizing the solver advantage is equivalent to on-policy distillation from the solver, requiring only scalar values rather than teacher logits. Across Sokoban, Minesweeper, and Rush Hour, CAST outperforms all trained baselines on every game under both in-domain and unseen-difficulty evaluation and achieves the highest average zero-shot performance on ALFWorld and WebShop. Our code is available at https://github.com/Wloner0809/CAST.

</details>

---

### [[20_Research/Papers/大模型/Hybrid_Analysis_for_Secure_MCP_Tool_Use_in_LLM_Agents|Hybrid Analysis for Secure MCP Tool Use in LLM Agents]]

![[assets/2607.25297_figure.png|800]]

- **arXiv**: [2607.25297](https://arxiv.org/abs/2607.25297)
- **PDF**: https://arxiv.org/pdf/2607.25297
- **详细分析**: [[20_Research/Papers/大模型/Hybrid_Analysis_for_Secure_MCP_Tool_Use_in_LLM_Agents|Hybrid Analysis for Secure MCP Tool Use in LLM Agents]]
- **作者**: Ping He, Yuexiang Xie, Yaliang Li, Shouling Ji
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Hybrid Analysis for Secure MCP Tool Use in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MCP-SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. However, the use of MCP tools also introduces new safety risks, as LLM agents can be induced to perform malicious or unauthorized actions. Although prior work has proposed defenses for securing tool use in LLM agents, most methods rely on static analysis, i.e., inspecting prompts and generated outputs, which limits the defense effectiveness and robustness. To address these limitations, we propose MTGuard, a hybrid analysis-based defense framework designed to safeguard the use of MCP tools in LLM agents by leveraging lifecycle-aware static-dynamic co-analysis. Extensive evaluation demonstrates that MTGuard effectively mitigates multiple categories of harmful tool use across different LLM agents while maintaining performance on benign user tasks.

</details>

---

### [[20_Research/Papers/强化学习/Structure-aware_Relative_Policy_Optimization_for_Ranking|Structure-aware Relative Policy Optimization for Ranking]]

![[assets/2607.25268_figure.png|800]]

- **arXiv**: [2607.25268](https://arxiv.org/abs/2607.25268)
- **PDF**: https://arxiv.org/pdf/2607.25268
- **详细分析**: [[20_Research/Papers/强化学习/Structure-aware_Relative_Policy_Optimization_for_Ranking|Structure-aware Relative Policy Optimization for Ranking]]
- **作者**: Yiteng Tu, Weihang Su, Zitao Su, Yiqun Liu, Min Zhang, Qingyao Ai
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Structure-aware Relative Policy Optimization for Ranking》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ranking is a fundamental component of modern information access systems. Reinforcement learning (RL) provides a flexible framework for directly optimizing coarse-grained feedback and system-level objectives defined over the complete ranking list. However, existing RL-based ranking methods typically treat each sampled permutation as an atomic output and evaluate it primarily through a scalar reward, overlooking the structural relationships among different ranking lists. Consequently, permutations with similar rewards but substantially different permutation patterns may receive comparable optimization signals, potentially leading to inaccurate credit assignment and overly aggressive policy updates. To address this limitation, we propose SRPO, a \textbf{S}tructure-aware \textbf{R}elative \textbf{P}olicy \textbf{O}ptimization framework for listwise ranking. SRPO measures the discrepancy between sampled permutations using a top-weighted Kendall-tau distance and normalizes their pairwise reward differences by the corresponding distances. It quantifies the reward improvement per unit of ranking change, thereby emphasizing efficient local refinements, particularly those involving top-ranked positions. Experimental results across two ranking scenarios demonstrate that explicitly modeling permutation-level differences improves the effectiveness and stability of listwise ranking, with particularly favorable performance in limited-feedback and complex list-level optimization settings.

</details>

---

### [[20_Research/Papers/大模型/When_Do_Agent_Loops_Mistake_Stagnation_for_Progress_Self-Evaluation_Bias_and_Externally_Grounded_Verification_in_Long-Running_Autonomous_LLM|When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops]]

![[assets/2607.25152_first_page.png|800]]

- **arXiv**: [2607.25152](https://arxiv.org/abs/2607.25152)
- **PDF**: https://arxiv.org/pdf/2607.25152
- **详细分析**: [[20_Research/Papers/大模型/When_Do_Agent_Loops_Mistake_Stagnation_for_Progress_Self-Evaluation_Bias_and_Externally_Grounded_Verification_in_Long-Running_Autonomous_LLM|When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops]]
- **作者**: Hyundoo Park, Byungho Choi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. We name this failure mode the progress mirage and show, with controlled measurement, that it is a question of what the evaluator is grounded in. We built a testbed that holds the agent and its tool surface fixed and manipulates only the information-channel type of the evaluator that gates the loop. A world-state oracle, unfakeable in principle, is enforced by container and network isolation and verified at every run. Across 54 cycles a frontier agent claimed improvement every time, yet 56 percent had a measured delta of zero or below. Self-report was thus uninformative, and the self-verdict gate degenerated into accept-all, eroding the best deployed state it had reached by 19 percent. Even the strongest in-band judge, reading the full artifact text, the change diff, and its own verdict history, accepted cycles of which 44 percent were real-world regressions and rejected 38 percent of real improvements; the preregistered adversarial hypothesis that a strong judge closes the gap was rejected. On a boundary task whose success specification is verifiable from the artifact itself, the same judge's mirage vanished to zero and the gap collapsed within the registered threshold, showing that the gap depends on where the success signal resides. A sign-only variant returning only the acceptance verdict kept real-world output similar to full feedback (110.0 versus 113.0), locating the benefit in the gate's grounding rather than in feedback content. For open-ended objectives whose success signal lives outside the transcript, scaling up the judge is not enough; out-of-band evaluation with real-world access is a structural requirement.

</details>

---

### [[20_Research/Papers/具身智能/How_Affect_Propagates_among_LLM_Agents_Emergent_Emotional_Contagion_in_Crowd_Simulation|How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation]]

![[assets/2607.25140_figure.png|800]]

- **arXiv**: [2607.25140](https://arxiv.org/abs/2607.25140)
- **PDF**: https://arxiv.org/pdf/2607.25140
- **详细分析**: [[20_Research/Papers/具身智能/How_Affect_Propagates_among_LLM_Agents_Emergent_Emotional_Contagion_in_Crowd_Simulation|How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation]]
- **作者**: Funda Durupinar
- **cs 子类**: cs.AI, cs.CL, cs.GR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EmoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outward expression. The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception-appraisal-expression loop. The agent representation draws on the Big Five personality model and Russell's circumplex model of affect. To limit latency, low-level steering and navigation are handled by a conventional crowd simulator operating independently of the LLM-based cognitive layer. We evaluate the architecture across five scenario environments spanning alarming, joyful, and neutral situations in different spatial layouts. The results show that the system produces emotional contagion dynamics with spatial, temporal, and personality-dependent structure in sparse, small crowds. Alarm spreads from seeded agents as a traveling front, the mean alarmed fraction settles at a nonzero plateau, and the distribution of prompted personality profiles determines whether an ambiguous alarm ignites panic and whether a provocation is interpreted as anger or fear. We further evaluate the appraisal step through controlled experiments across prompt variants, sampling temperatures, and four model backends, showing that the dynamics are backend-dependent.

</details>

---

### [[20_Research/Papers/大模型/Towards_Robust_Reinforcement_Learning_for_Small-Scale_Language_Model_Agents|Towards Robust Reinforcement Learning for Small-Scale Language Model Agents]]

![[assets/2607.25091_figure.png|800]]

- **arXiv**: [2607.25091](https://arxiv.org/abs/2607.25091)
- **PDF**: https://arxiv.org/pdf/2607.25091
- **详细分析**: [[20_Research/Papers/大模型/Towards_Robust_Reinforcement_Learning_for_Small-Scale_Language_Model_Agents|Towards Robust Reinforcement Learning for Small-Scale Language Model Agents]]
- **作者**: Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.07（加权：大模型 0.75，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Towards Robust Reinforcement Learning for Small-Scale Language Model Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SLM-RL, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). The experiments included Pythia-70M, 160M, 410M and SmolLM2-135M, 360M on the TinyStories, CNN/DailyMail, and Wikitext-103 corpora. Three reproducible failure modes were identified in small-scale language models: silent LoRA parameter freezing in standard PEFT/TRL pipelines, numerical overflow in importance ratios when using bfloat16, and catastrophic policy collapse due to reward-model error. These issues were addressed using a merge-and-reinitialize adapter technique, float32 precision during PPO updates, and a three-layer safety mechanism comprising reward whitening, importance-ratio guarding, and weight rollback. In this paper, a capacity-headroom hypothesis is proposed, which states that PPO performance at the SLM scale depends on both a fluent supervised model ($\text{PPL}&lt;20$) and a discriminative reward signal, rather than on the number of model parameters. The proposed system converged stably in all experiments and improved preference win rate over the SFT baseline in configurations with a fluent prior and an informative reward signal. Furthermore, it outperformed instruction-tuned baselines while requiring significantly less training data. All checkpoints, preference datasets, and training scripts are publicly released$^§$.

</details>

---

### [[20_Research/Papers/大模型/Matryoshka_Agent_Unfolding_Sub-Agents_for_Long-Horizon_Machine_Learning_Engineering|Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering]]

![[assets/2607.25090_figure.png|800]]

- **arXiv**: [2607.25090](https://arxiv.org/abs/2607.25090)
- **PDF**: https://arxiv.org/pdf/2607.25090
- **详细分析**: [[20_Research/Papers/大模型/Matryoshka_Agent_Unfolding_Sub-Agents_for_Long-Horizon_Machine_Learning_Engineering|Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering]]
- **作者**: Rushi Qiang, Changhao Li, Haotian Sun, Yuchen Zhuang, Chao Zhang, Bo Dai
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions. Developing and training a monolithic agent for such tasks is fundamentally challenging, as it must simultaneously manage extremely long and noisy contexts, explore vast solution spaces, and remain effective under limited model capacity and computational budgets. To address these challenges, we propose Matryoshka Agent, a unified hierarchical agent framework for complex long-horizon tasks. Matryoshka Agent decomposes agentic problem solving into a coordinated hierarchy of decision making and execution: a high-level Orchestrator maintains compact, long-horizon exploration states and issues strategic instructions, while lower-level Sub-Agents execute concrete solution attempts through direct environment interaction, mediated by standardized Tool interface. This design decouples strategic exploration from costly execution, substantially reducing the burden of long-context reasoning and enabling efficient iterative refinement. We further develop an efficient training paradigm for Matryoshka Agent. Experimental results on a broad range of MLE tasks with diverse model types and scales demonstrate that Matryoshka Agent is an effective and scalable paradigm for long-horizon MLE tasks and complex agentic problem solving. Notably, Matryoshka Agent enables Qwen3-4B-Instruct to reach Orchestrator performance comparable to o4-mini. Applying Matryoshka Agent to Qwen3-30B-Coder results in at most 36.7% relative performance gain.

</details>

---

### [[20_Research/Papers/强化学习/PLATO_Pointer_Learner_for_Agent_and_Task_Openness|PLATO: Pointer Learner for Agent and Task Openness]]

![[assets/2607.25082_figure.png|800]]

- **arXiv**: [2607.25082](https://arxiv.org/abs/2607.25082)
- **PDF**: https://arxiv.org/pdf/2607.25082
- **详细分析**: [[20_Research/Papers/强化学习/PLATO_Pointer_Learner_for_Agent_and_Task_Openness|PLATO: Pointer Learner for Agent and Task Openness]]
- **作者**: Alireza Saleh Abadi, Leen-Kiat Soh, Daniel Alan Redder, Adam Eck, Prashant Doshi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.5，强化学习 0.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《PLATO: Pointer Learner for Agent and Task Openness》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open agent systems (OASYS) are increasingly prevalent in real-world domains where the sets of agents and tasks change unpredictably over time. Such openness, including agent openness (AO) and task openness (TO), poses a fundamental challenge to multi-agent reinforcement learning (MARL), which typically assumes fixed state and action spaces. Existing methods address openness only partially: padding and masking approaches introduce artificial bounds, while recent graph-based or hypergraph methods handle one dimension of openness but still depend on restrictive assumptions. In this paper, we introduce Pointer Learner for Agent and Task Openness (PLATO), a pointer-network-based actor combined with a centralized graph neural network (GNN) critic, trained with multi-agent proximal policy optimization under a centralized training and decentralized execution paradigm. Our pointer-based actor outputs distributions directly over the current task set. This directly supports changing action spaces without masking or retraining. Our GNN critic encodes agent-task interactions as a graph that changes shape with task and agent composition. Together, these components consider AO and TO without the boundedness of existing approaches. We formalize PLATO in a Task-and-Agent-Open Markov Game (TaAgO-MG), extending prior task-open formulations, and prove it is well-defined over the resulting unbounded state and action spaces. We evaluate PLATO with the Methods for Open Agent Systems Evaluation Initiative (MOASEI) wildfire suppression domain, an environment designed for open multi-agent system evaluation, and we demonstrate strong performance and more consistent zero-shot generalization than state-of-the-art baselines in OASYS.

</details>

---

### [[20_Research/Papers/大模型/DS@GT_ARC_at_CheckThat!_2026_LLM-Based_Trace_Ranking_and_Grouped_Reward_Modeling_for_Multilingual_Numerical_Claim_Verification|DS@GT ARC at CheckThat! 2026: LLM-Based Trace Ranking and Grouped Reward Modeling for Multilingual Numerical Claim Verification]]

![[assets/2607.25069_figure.jpg|800]]

- **arXiv**: [2607.25069](https://arxiv.org/abs/2607.25069)
- **PDF**: https://arxiv.org/pdf/2607.25069
- **详细分析**: [[20_Research/Papers/大模型/DS@GT_ARC_at_CheckThat!_2026_LLM-Based_Trace_Ranking_and_Grouped_Reward_Modeling_for_Multilingual_Numerical_Claim_Verification|DS@GT ARC at CheckThat! 2026: LLM-Based Trace Ranking and Grouped Reward Modeling for Multilingual Numerical Claim Verification]]
- **作者**: Sagnik Sinha, Shreyas Shrestha
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《DS@GT ARC at CheckThat! 2026: LLM-Based Trace Ranking and Grouped Reward Modeling for Multilingual Numerical Claim Verification》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated verification of numerical claims is a challenging problem, as it requires both language understanding and quantitative reasoning. This paper describes our system for CLEF 2026 CheckThat! Task 2, which focuses on ranking reasoning traces generated by large language models (LLMs) and predicting a final verdict for numerical claims in English and Arabic. We explore two approaches. The first approach fine-tunes an LLM-based verifier using LoRA to score each reasoning trace independently as a binary classification problem, and selects the final verdict using Best-of-N selection. We further experiment with adaptive sub-claim decomposition to break complex claims into simpler parts before verification. The second approach uses a lightweight TF-IDF reward model with handcrafted numeric and temporal overlap features to score traces, and aggregates scores by verdict group to determine the final prediction. For Arabic, we compare a general multilingual model against AraBERT, a language-specific model pretrained on Arabic text. Our results show that the LLM-based approach outperforms the lightweight reward model on most metrics, particularly Recall@5, while the reward-based approach shows stronger performance on the Conflicting class. Sub-claim decomposition did not improve performance, suggesting that claim splitting introduces noise rather than aiding reasoning. For Arabic, AraBERT outperforms the multilingual baseline across most metrics.

</details>

---

### [[20_Research/Papers/大模型/Addressable_Recall_Compaction_for_Long_Context-Window_Control_in_AI_Agents|Addressable Recall Compaction for Long Context-Window Control in AI Agents]]

![[assets/2607.25066_figure.png|800]]

- **arXiv**: [2607.25066](https://arxiv.org/abs/2607.25066)
- **PDF**: https://arxiv.org/pdf/2607.25066
- **详细分析**: [[20_Research/Papers/大模型/Addressable_Recall_Compaction_for_Long_Context-Window_Control_in_AI_Agents|Addressable Recall Compaction for Long Context-Window Control in AI Agents]]
- **作者**: Thang Dang, Yuma Ichikawa, Sakina Fatima, Koichi Shirahata
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Addressable Recall Compaction for Long Context-Window Control in AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window. Existing compaction methods address this limitation by discarding, summarizing, or retrieving earlier information, but they may remove task-critical details or fail to recover them reliably. We propose ARC (Addressable Recall Compaction), a context-management framework that separates archival storage from active-context presentation. ARC stores tool observations in an append-only, ID-addressable log and replaces older observations with compact citations when compaction is required. The agent can subsequently use these identifiers to request stored content without re-executing the corresponding tools or depending solely on similarity-based retrieval. We evaluate ARC using Qwen3-8B with a 16k context window and Qwen3-32B with a 32k context window. On the Needle-in-a-Haystack evaluation, ARC achieves an average exact-answer accuracy of 99.40%, compared with 88.12% for the best-performing baseline in our evaluation. ARC also reduces estimated serving time and HBM traffic under our hardware-cost model. On the LongBench-v2 Hard subset, ARC obtains an average accuracy of 29.97%, compared with 28.25% for the best-performing baseline. These results indicate that explicit, address-based recall can improve information retention and serving efficiency relative to the evaluated context-management baselines under the tested settings.

</details>

---

### [[20_Research/Papers/大模型/Extended_Reality_as_a_Mediation_Layer_for_Situated_Human_Control_in_Human-Robot_Teaming|Extended Reality as a Mediation Layer for Situated Human Control in Human-Robot Teaming]]

![[assets/2607.25047_figure.jpg|800]]

- **arXiv**: [2607.25047](https://arxiv.org/abs/2607.25047)
- **PDF**: https://arxiv.org/pdf/2607.25047
- **详细分析**: [[20_Research/Papers/大模型/Extended_Reality_as_a_Mediation_Layer_for_Situated_Human_Control_in_Human-Robot_Teaming|Extended Reality as a Mediation Layer for Situated Human Control in Human-Robot Teaming]]
- **作者**: Jens Grubert, John Dudley, Eyal Ofek, Per Ola Kristensson
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Extended Reality as a Mediation Layer for Situated Human Control in Human-Robot Teaming》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Extended Reality (XR) is increasingly used in human-robot interaction to communicate robot intent, planned motion, reachability, and state. We argue that XR should also be understood as a mediation layer for situated human control in human-robot teaming. Situated human control denotes the human collaborator's ability to understand, shape, authorize, and interrupt robot action within the concrete physical, social, and temporal context in which that action unfolds. We ground this perspective in scenarios from robot-assisted bedside nursing, multi-arm supervisory control, and collaborative assembly under divided attention. Across these scenarios, robot autonomy must remain inspectable and adjustable as people move, goals change, sensing is incomplete, control roles shift, and plans become invalid. We identify four mediation functions connecting human intent and robot autonomy, robot plans and human judgment, levels of shared control, and team roles, handover, and recovery. Building on these functions, we derive six design dimensions: joint action possibilities, socio-physical constraints, uncertainty and plan validity, multimodal control and correction, roles, handover, and accountability, and anticipatory recovery. The paper outlines a research agenda for XR systems that make robot autonomy more actionable and accountable in dynamic shared environments.

</details>

---

### [[20_Research/Papers/大模型/Authoring_Agent_Skills_A_Software-Engineering_Approach|Authoring Agent Skills: A Software-Engineering Approach]]

![[assets/2607.25032_first_page.png|800]]

- **arXiv**: [2607.25032](https://arxiv.org/abs/2607.25032)
- **PDF**: https://arxiv.org/pdf/2607.25032
- **详细分析**: [[20_Research/Papers/大模型/Authoring_Agent_Skills_A_Software-Engineering_Approach|Authoring Agent Skills: A Software-Engineering Approach]]
- **作者**: Giuseppe Destefanis
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Authoring Agent Skills: A Software-Engineering Approach》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent Skills are an emerging way to extend large language model agents with reusable procedural knowledge that the agent loads on demand. Anthropic introduced Agent Skills and published the format as an open specification supported across several agent tools. This note argues that a skill is a software artefact and that its construction should follow software-engineering principles, with qualifications: single responsibility, separation of interface from implementation, low coupling, and economy in a shared token budget, together with behavioural evaluation in place of deterministic testing. Using Claude Code as the reference implementation, it describes how a skill is structured, how its contents are loaded in stages, and how to write the description on which selection depends. It places skills against the other mechanisms a developer can use to shape agent behaviour, like project memory files, slash commands, subagents, external tool connections, and hooks, and gives a rule for choosing between them based on who decides that a mechanism runs and what guarantee it provides. It then sets out an evaluation-driven authoring process, a set of patterns and faults commonly encountered in authoring, and the trust question raised by using skills from third parties. We illustrate the comparison drawn in UML class style, the loading model, the anatomy of a skill, the relative position of each mechanism, and the points at which skills and hooks act during a session.

</details>

---

### [[20_Research/Papers/强化学习/Calibrated_Partial_Resets_Preventing_Policy_Collapse_in_Continual_Reinforcement_Learning|Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning]]

![[assets/2607.24996_figure.png|800]]

- **arXiv**: [2607.24996](https://arxiv.org/abs/2607.24996)
- **PDF**: https://arxiv.org/pdf/2607.24996
- **详细分析**: [[20_Research/Papers/强化学习/Calibrated_Partial_Resets_Preventing_Policy_Collapse_in_Continual_Reinforcement_Learning|Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning]]
- **作者**: Luc McCutcheon, Evangelos Chatzaroulas, Saber Fallah
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neural networks are hindered by accumulating dormant neurons and loss of expressivity throughout training, particularly in non-stationary data settings, such as continual supervised and reinforcement learning. Recently, neuron resets have been used to maintain gradient flow and restore plasticity. However, full unit reinitialization often sacrifices peak performance and can destabilize training, leading to policy collapse. To preserve plasticity without destabilizing training, we propose Calibrated Partial Resets (CPR), an optimizer that periodically pulls low-utility neurons toward their initialization, with pull strength scaled by each neuron's utility. Unlike binary reset methods, partial resets avoid brittleness; unlike uniform decay, calibrated utility-scaling concentrates adjustment on the units that need it most. Among compared methods, only CPR avoids policy collapse over 400M training steps in SlipperyAnt, and it outperforms prior decay and reset-based methods on Continual MetaWorld and Continual MinAtar benchmarks. Ablations reveal a tunable trade-off between plasticity and peak performance, highlighting utility-scaled reinitialization as a promising direction for continual learning.

</details>

---

### [[20_Research/Papers/大模型/Early_Detection_of_Distributed_Backdoors_in_Multi-Agent_LLM_Systems_A_Characterization_Study|Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study]]

![[assets/2607.24893_figure.png|800]]

- **arXiv**: [2607.24893](https://arxiv.org/abs/2607.24893)
- **PDF**: https://arxiv.org/pdf/2607.24893
- **详细分析**: [[20_Research/Papers/大模型/Early_Detection_of_Distributed_Backdoors_in_Multi-Agent_LLM_Systems_A_Characterization_Study|Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study]]
- **作者**: Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang, Yibo Hu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ATBench, HINTBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught once its most obvious cues are stripped away. We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed. Detection is a race against assembly. Before the first fragment is injected, attacked and benign runs are indistinguishable; once injection begins, a prefix detector flags $99.3\%$ of successful attacks with a median of five steps remaining and a $10.3\%$ safe-run false-positive rate. Because assembly occurs only after the run, these alarms arrive in time to abort nearly every successful attack. We then measure how much of that warning rests on removable surface cues of the attack rather than on its distributed structure. Generic zero-shot and behavior-trained detectors provide almost no warning at all; the detectors that do work lean in part on removable surface cues, chiefly the ciphertext's length and entropy, and once the entropy cue is removed from the payload and the length features from the detector, detection arrives later and transfers poorly across domains, though a fine-tuned model recovers some of the loss.

</details>

---

### [[20_Research/Papers/大模型/Beyond_What_to_Retrieve_Uncertainty_in_Retrieval-Augmented_Code_Generation|Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation]]

![[assets/2607.24884_figure.png|800]]

- **arXiv**: [2607.24884](https://arxiv.org/abs/2607.24884)
- **PDF**: https://arxiv.org/pdf/2607.24884
- **详细分析**: [[20_Research/Papers/大模型/Beyond_What_to_Retrieve_Uncertainty_in_Retrieval-Augmented_Code_Generation|Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation]]
- **作者**: Chandan Kumar Sah, Xiaoli Lian, Li Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoderEval, ExecRepoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repository-level code generation relies on heterogeneous evidence whose relevance, compatibility, and completeness are inherently uncertain. Similar-code examples, repository context, and project-specific APIs may provide complementary information, but can also introduce noisy, redundant, or conflicting signals. Existing retrieval-augmented approaches primarily optimize retrieval relevance without explicitly modeling how uncertainty in retrieved evidence affects downstream generation. We introduce OpenCoder, an uncertainty-aware framework that estimates source-specific uncertainty, uses it to filter and rank heterogeneous evidence, and guides generation, verification, and repair. A factorial analysis over API knowledge, repository context, and similar-code evidence reveals no universal additive source ranking; instead, significant cross-source interactions depend on the accompanying evidence and LLM backend. On an expanded 32-task RepoExec-inline evaluation, OpenCoder improves GPT selected-output correctness over Baseline RAG from 56.25\% to 78.13\%. However, it matches a verification-and-repair control, and the corresponding Gemini improvement is not statistically supported, indicating backend-dependent benefits. Target-aware API refinement also substantially improves API-set retrieval. These findings support treating uncertainty as an actionable control signal for repository-level retrieval, verification, and repair.

</details>

---

### [[20_Research/Papers/大模型/Agent_Retrieval_Bench_Evaluating_Repository_Context_Retrieval_for_Coding_Agents|Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents]]

![[assets/2607.24882_first_page.png|800]]

- **arXiv**: [2607.24882](https://arxiv.org/abs/2607.24882)
- **PDF**: https://arxiv.org/pdf/2607.24882
- **详细分析**: [[20_Research/Papers/大模型/Agent_Retrieval_Bench_Evaluating_Repository_Context_Retrieval_for_Coding_Agents|Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents]]
- **作者**: Bowen Qin, Yi Xie
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent

#### 研究背景与动机

《Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CORE-Bench, CodeSearchNet, RepoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern coding agents are usually evaluated by whether they eventually produce a correct patch, but patch generation depends on an earlier context-acquisition stage: finding the repository files needed for the task. We introduce Agent Retrieval Bench, a file-level benchmark for this upstream retrieval problem. Samples are built from real coding-workflow signals and evaluated against frozen base-commit repositories, with relevance defined by what an agent needs next rather than direct query-file semantic similarity. The benchmark covers four positive-retrieval tasks: code2test, comment2context, trace2code, and edit2ripple; a fifth subset evaluates selective retrieval using natural evidence-backed no-gold cases and counterfactual wrong-repository controls. Agent Retrieval Bench contains 427 samples across 25 repositories: 345 positive examples, 50 natural no-gold examples, and 32 counterfactual controls. The corpus includes 308 base-commit snapshots, 392,000 files, and 7.9 million chunks. We evaluate lexical retrieval, RepoMap, open-source embeddings, selective abstention, and logged agent context selection. No single retrieval family dominates: Qwen3-Embedding-4B has the best sample-weighted MRR on positive samples, Qwen3-Embedding-8B the best Recall@20, and RepoMap the best budgeted context yield at 8K tokens, with task-level winners differing substantially. Selective thresholds calibrated with counterfactual controls do not improve selective success on natural no-gold cases, revealing a calibration gap. Logged trajectories also miss every gold file on 27-35 percent of samples. A controlled seed-intervention pilot finds that retrieval-derived initial context yields higher file F1 with less post-seed exploration than random non-gold context, while oracle gold context shows substantial remaining headroom.

</details>

---

### [[20_Research/Papers/大模型/HVM-GraphRAG_Holistic-View_Multimodal_Graph_Retrieval-Augmented_Generation_on_Complex_Document|HVM-GraphRAG: Holistic-View Multimodal Graph Retrieval-Augmented Generation on Complex Document]]

![[assets/2607.24861_figure.png|800]]

- **arXiv**: [2607.24861](https://arxiv.org/abs/2607.24861)
- **PDF**: https://arxiv.org/pdf/2607.24861
- **详细分析**: [[20_Research/Papers/大模型/HVM-GraphRAG_Holistic-View_Multimodal_Graph_Retrieval-Augmented_Generation_on_Complex_Document|HVM-GraphRAG: Holistic-View Multimodal Graph Retrieval-Augmented Generation on Complex Document]]
- **作者**: Xin He, Yili Wang, Wenqi Fan, Qing Li, Qinggang Zhang, Yi Chang, Xin Wang
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《HVM-GraphRAG: Holistic-View Multimodal Graph Retrieval-Augmented Generation on Complex Document》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Question answering (QA) over complex documents requires models to retrieve and integrate evidence distributed across distant document regions and modalities. Multimodal GraphRAG provides a promising direction by organizing document evidence with graph structures. However, existing methods often suffer from unreliable cross-modal evidence indexing and expensive graph traversal. To address these issues, we propose HVM-GraphRAG, a holistic-view multimodal GraphRAG framework on complex document. HVM-GraphRAG uses a holistic view to guide graph construction, thereby reducing noisy and conflicting graph updates and building reliable indices between concept-level graph nodes and supporting multimodal chunks. During retrieval, HVM-GraphRAG searches over a compact concept-level graph and directly accesses supporting evidence through the constructed index, avoiding costly traversal over dense entity-level graphs. After obtaining the retrieved evidence, HVM-GraphRAG further reorganizes chunks into modality-specific groups, enabling the answering model to better integrate heterogeneous evidence. Experiments on three datasets show that HVM-GraphRAG achieves the best answer performance in most evaluated settings while substantially improving online retrieval efficiency over representative graph-based baselines.

</details>

---

### [[20_Research/Papers/大模型/DisasterTD_Disaster_Toponym_Disambiguation_Using_Multimodal_LLMs_and_Cross-View_Geolocalization|DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization]]

![[assets/2607.24856_figure.png|800]]

- **arXiv**: [2607.24856](https://arxiv.org/abs/2607.24856)
- **PDF**: https://arxiv.org/pdf/2607.24856
- **详细分析**: [[20_Research/Papers/大模型/DisasterTD_Disaster_Toponym_Disambiguation_Using_Multimodal_LLMs_and_Cross-View_Geolocalization|DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization]]
- **作者**: Wenping Yin, Ziqi Liu, Naixia Mou, Weijia Li, Danfeng Hong, Hao Li
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social media imagery (SMI) provides timely and fine-grained ground perspectives that are valuable for situational awareness and emergency response. Unlike satellite or aerial imagery, SMI can capture disaster impacts and ground-level conditions in a timely manner. However, geographic references in SMI are often vague or ambiguous, making accurate geolocalization challenging. To address this issue, we propose DisasterTD, a disaster toponym disambiguation framework that integrates multimodal large language model (MLLMs)-based semantic reasoning with cross-view geolocalization. First, MLLMs extract toponyms and generate candidate geolocations from noisy textual inputs. Then, cross-view matching between SMI, remote sensing imagery (RSI), and optionally street-view imagery (SVI) is used to verify and refine these candidate results. We evaluate DisasterTD on the Hurricane Harvey dataset, where SMI is augmented with collected RSI and SVI to construct a cross-view benchmark for disaster geolocalization. The dataset is divided into four categories based on toponym clarity and ambiguity, allowing a fine-grained performance analysis across scenarios. Results show that DisasterTD consistently outperforms MLLM-only and cross-view-only baselines without disambiguation, achieving geolocalization accuracies of 71.62% within 1000 m, 62.36% within 500 m, 57.99% within 250 m, 52.09% within 100 m, and 47.01% within 50 m, while reducing the mean and median errors to 11.33 km and 0.68 km, respectively. The largest improvements appear in ambiguous toponyms, where semantic reasoning with cross-view evidence reduces candidate dispersion and errors. These findings demonstrate the effectiveness of integrating MLLM-based candidate generation with cross-view verification for fine-grained disaster geolocalization.

</details>

---

### [[20_Research/Papers/强化学习/AdaKP_Online_Adaptive_Knowledge-Point_Selection_for_Reasoning-Oriented_Reinforcement_Learning|AdaKP: Online Adaptive Knowledge-Point Selection for Reasoning-Oriented Reinforcement Learning]]

![[assets/2607.24833_first_page.png|800]]

- **arXiv**: [2607.24833](https://arxiv.org/abs/2607.24833)
- **PDF**: https://arxiv.org/pdf/2607.24833
- **详细分析**: [[20_Research/Papers/强化学习/AdaKP_Online_Adaptive_Knowledge-Point_Selection_for_Reasoning-Oriented_Reinforcement_Learning|AdaKP: Online Adaptive Knowledge-Point Selection for Reasoning-Oriented Reinforcement Learning]]
- **作者**: Zibin Meng, Zhenyu Zhao, Chunqiang Run
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《AdaKP: Online Adaptive Knowledge-Point Selection for Reasoning-Oriented Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：KnowRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards is a powerful paradigm for eliciting reasoning in large language models, yet it suffers from severe reward sparsity on competition-level mathematics. A common remedy injects atomic knowledge points (KPs) - short natural-language hints distilled from gold solutions - into the prompt. Existing methods, however, either fix this selection once offline or merely scale the monolithic quantity of injected text, leaving untouched the most informative axis of choice: which subset of atomic KPs to inject, and when. We introduce AdaKP, an online selector that re-chooses each problem's KP subset over the course of RL training. At its core is an entropy proxy that scores a KP by the reduction in next-token entropy it induces - a single inexpensive forward pass, with a provable bound on its truncation bias - in place of expensive rollout-based estimation. Three lightweight mechanisms make this signal usable online: a momentum smoother that absorbs per-step noise, a retirement-and-revival manager that prunes weak KPs while preserving exploration, and an adaptive scheduler that front-loads re-evaluations into early training. AdaKP further contributes a pre-flight validation gate that certifies the proxy against a leave-one-out ground truth before any expensive run is launched, turning method-level risk into a falsifiable check. Realized as a fully additive fork of a standard DAPO+GRPO trainer with no optimizer changes, AdaKP improves over a strong static-selection baseline on all eight competition-mathematics benchmarks at negligible added cost, positioning online, validated KP-subset selection as a practical and as-yet under-explored axis for reasoning-oriented reinforcement learning.

</details>

---

### [[20_Research/Papers/大模型/Retrieval-Augmented_Generation_in_LLMs_for_Mental_Health_Quantifying_the_Incremental_Contribution_of_Retrieval_Within_a_Layered_Safety_Archi|Retrieval-Augmented Generation in LLMs for Mental Health: Quantifying the Incremental Contribution of Retrieval Within a Layered Safety Architecture]]

![[assets/2607.24817_first_page.png|800]]

- **arXiv**: [2607.24817](https://arxiv.org/abs/2607.24817)
- **PDF**: https://arxiv.org/pdf/2607.24817
- **详细分析**: [[20_Research/Papers/大模型/Retrieval-Augmented_Generation_in_LLMs_for_Mental_Health_Quantifying_the_Incremental_Contribution_of_Retrieval_Within_a_Layered_Safety_Archi|Retrieval-Augmented Generation in LLMs for Mental Health: Quantifying the Incremental Contribution of Retrieval Within a Layered Safety Architecture]]
- **作者**: Anand Gupta, Akshat Surolia, Shubham Mishra, Shakil Imtiaz, Chaitali Sinha
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Retrieval-Augmented Generation in LLMs for Mental Health: Quantifying the Incremental Contribution of Retrieval Within a Layered Safety Architecture》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Digital mental health interventions (DMHIs) offer scalable support, but ensuring they accurately detect users' intent during volatile situations can be challenging. Pure parametric Large Language models (LLMs) do not contain specific safety critical architecture, and can miss critical cues, or hallucinate, undermining reliability. Retrieval Augmented Generation (RAG), which supplements an LLM with retrieved context, could enhance intent detection during volatile situations. Commercially available DMHIs typically combine multiple independent safety layers like rule-based filters, symbolic escalation protocols, and neural classification. The incremental contribution of any single layer, however, remains unquantified. This paper evaluates six LLM models within a DMHI called Wysa, via a controlled comparison of RAG-enabled versus RAG-disabled modes. Anonymized real and synthetic user-chatbot exchanges were annotated by a qualified clinical team against multi-class intent categories (e.g. self-harm, abuse, panic). The study computed classification accuracy, recall, precision and F1 scores against ground truth labels and tested differences for statistical significance. Performance was also examined by risk category and inter-model agreement. While RAG caused a rise in false alarms, the trade-off is consistent with safety-critical design principles that prioritize sensitivity, where flagged cases are routed to additional review rather than acted on directly. Overall, these findings support RAG as a promising approach to improve the accuracy, consistency and safety of LLM-driven DMHIs. Keywords: Digital Mental Health Intervention, Large Language Model, Retrieval Augmented Generation, Accuracy, Recall, Precision

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Hybrid_Retrieval-Augmented_Generation_for_Scientific_Document_Understanding_using_Open-Source_SLMs|Multimodal Hybrid Retrieval-Augmented Generation for Scientific Document Understanding using Open-Source SLMs]]

![[assets/2607.24799_figure.png|800]]

- **arXiv**: [2607.24799](https://arxiv.org/abs/2607.24799)
- **PDF**: https://arxiv.org/pdf/2607.24799
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Hybrid_Retrieval-Augmented_Generation_for_Scientific_Document_Understanding_using_Open-Source_SLMs|Multimodal Hybrid Retrieval-Augmented Generation for Scientific Document Understanding using Open-Source SLMs]]
- **作者**: Alexandru-Andrei Saucă, Ana-Luiza Rusnac
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《Multimodal Hybrid Retrieval-Augmented Generation for Scientific Document Understanding using Open-Source SLMs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DeepEval, MMLongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models tend to hallucinate when answering domain-specific ques tions from scientific documents without prior fine-tuning. Currently, methods such as Retrieval-Augmented Generation partially solve this problem but face different challenges: limited context knowledge, difference between sparse and dense retrieval, and retrieval noise. This paper presents an Advanced Multimodal Retrieval-Augmented Generation system that aims to solve those challenges and im prove the accuracy of information extraction. The proposed architecture introduces a multimodal ingestion pipeline that leverages an open-source Vision-Language Model (Qwen2-VL-2B-Instruct) to generate textual summaries of tables and fig ures. The retrieval phase integrates HNSW-based semantic search with GIN-based lexical search, unified through Reciprocal Rank Fusion and refined using Cross Encoder reranking to minimize retrieval noise. To ensure conversational coherence across multi-turn interactions, a Query Condenser module is employed. Evaluation is conducted by independently assessing the ingestion, retrieval and generation stages using the MMLongBench benchmark, a BeIR-format synthetic dataset and the DeepEval framework. Moreover, results demonstrate a 157% improvement in retrieval quality over a Naive-RAG baseline, with only 50 ms additional la tency, while Qwen2-VL-2B-Instruct achieved results comparable to cloud-based models in BERTScore. These findings validate that open-source optimized SLMs, paired with advanced retrieval strategies, can provide competitive performance for document understanding without relying on cloud-based models.

</details>

---

### [[20_Research/Papers/大模型/From_Naive_RAG_to_Deep_Agentic_Retrieval_An_Evolving_Context_Engineering_Pipeline_for_Regulatory_Compliance|From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance]]

![[assets/2607.24791_first_page.png|800]]

- **arXiv**: [2607.24791](https://arxiv.org/abs/2607.24791)
- **PDF**: https://arxiv.org/pdf/2607.24791
- **详细分析**: [[20_Research/Papers/大模型/From_Naive_RAG_to_Deep_Agentic_Retrieval_An_Evolving_Context_Engineering_Pipeline_for_Regulatory_Compliance|From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance]]
- **作者**: Mishca de Costa, Muhammad Saleh Anwar, Dave Mercier, Issam Hammad
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《From Naive RAG to Deep Agentic Retrieval: An Evolving Context Engineering Pipeline for Regulatory Compliance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) is the dominant paradigm for applying large language models (LLMs) to enterprise document corpora, yet naive implementations encounter hard limits as corpus scale and query complexity grow. This paper traces the evolution of a production retrieval pipeline at Ontario Power Generation (OPG) for regulatory compliance and rate case analysis under Ontario Energy Board (OEB) reporting requirements. We examine successive stages: naive RAG, hybrid retrieval with re-ranking, agentic function-calling retrieval, and a deep multi-agent architecture with code-based tool synthesis and explicit planning, and identify the failure modes and tradeoffs that motivated each transition. We formalize the mature architecture as Progressive Evidence Acquisition with Cost-Aware Escalation (PEA-CAE): begin with low-cost, high-precision retrieval and escalate to full-document reads only when the expected evidence gain justifies latency and cost. Our findings show that context engineering is a more tractable and economically viable path than domain-specific fine-tuning for large, evolving regulatory corpora. More broadly, the progression toward deep agentic retrieval mirrors classical information retrieval ideas, introducing adaptive query reformulation, progressive document discovery, and hierarchical subagent summarization as practical system primitives. Operational traces further support the search-based nature of modern retrieval systems, where iterative evidence acquisition and adaptive planning increasingly replace single-pass retrieval as the foundation for enterprise-scale question answering.

</details>

---

### [[20_Research/Papers/大模型/HOBA_Hierarchical_On-Policy_Bidding_Agents_for_Adaptive_Online_Advertising|HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising]]

![[assets/2607.24779_figure.png|800]]

- **arXiv**: [2607.24779](https://arxiv.org/abs/2607.24779)
- **PDF**: https://arxiv.org/pdf/2607.24779
- **详细分析**: [[20_Research/Papers/大模型/HOBA_Hierarchical_On-Policy_Bidding_Agents_for_Adaptive_Online_Advertising|HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising]]
- **作者**: Ji Wu, Yunshan Peng, Wentao Bai, Yunke Bai, Wenzheng Shu, Jinan Pang, Yanxiang Zeng, Xialong Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.7，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《HOBA: Hierarchical On-Policy Bidding Agents for Adaptive Online Advertising》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AuctionNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online advertising bidding systems typically deploy multiple offline-trained expert models (e.g., PID controllers, model predictive control, offline RL policies) but face two critical limitations: lack of online adaptability to non-stationary auction markets, and reliance on costly manual tuning of hyperparameters such as bid bounds and budget pacing constraints. We propose HOBA (Hierarchical On-policy Bidding Agents), a hierarchical reinforcement learning framework that decouples strategic reasoning, model selection, and bid execution across three time scales. At the high level, a large language model infers hyperparameters from contextual signals through a Think-Act-Observe-Reflect loop with historical experience retrieval. At the mid level, a SARSA agent dynamically selects among expert models, incorporating causal adjustment to eliminate selection bias. At the low level, a dynamic expert pool (PID, MPC, IQL, Decision Transformer) executes bids under high-level constraints. This design confines online learning to discrete expert selection rather than continuous bid optimization, significantly reducing exploration risk while maintaining adaptability. Experiments on the AuctionNet benchmark and a large-scale A/B test demonstrate consistent improvements over state-of-the-art baselines. In a large-scale online deployment, HOBA delivered substantial business value, achieving a +3.6\% increase in target cost, proving the effectiveness of our hierarchical multi-agent bidding paradigm.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Memory_A_Templated_Substrate_for_Heterogeneous_Collaborative_Knowledge_Work_with_LLM_Agents|Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents]]

![[assets/2607.24759_first_page.png|800]]

- **arXiv**: [2607.24759](https://arxiv.org/abs/2607.24759)
- **PDF**: https://arxiv.org/pdf/2607.24759
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Memory_A_Templated_Substrate_for_Heterogeneous_Collaborative_Knowledge_Work_with_LLM_Agents|Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents]]
- **作者**: Priscila Saboia Moreira, Christopher R. Sweet
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Research projects, educational efforts, and adjacent knowledge work accumulate findings, decisions, and reasoning that future collaborators rarely recover. The parts most useful to that work, including dead ends and walked-back claims, are routinely excluded from publications and shared code; future researchers re-attempt the same failures because no record survives. LLM coding agents are common participants but hold no persistent memory across sessions, and retrieval-augmented generation over raw sources does not compound. The llm-wiki pattern (Karpathy, 2026; tonbi, 2026) addresses this by inserting an LLM-maintained, interlinked wiki between raw sources and the agent. We present llm-wiki-memory-template, a reusable, agent-aware instantiation, and argue it is a substrate for heterogeneous collaborative knowledge work along three axes (multi-human, multi-AI-agent, multi-domain) with each axis supported by a distinct architectural element of the template (§4). The wiki is append-only by convention, which preserves what did not work alongside what did, addressing a negative-result loss problem that publications and code-sharing structurally cannot solve. Three deployed case studies and one design report cover the axes individually: a solo research lineage that preserves abandoned iterations; a two-author project whose retroactive audit revised two prior experiments' claimed 20-of-20 coverage down to 14 and 12 evidence-based answers, then to 18 and 18 after a fix, with the failure path preserved across the artifact; an in-progress multi-agent deployment reported as a design; and a cross-domain educational variant. We name failure-path preservation, agent honesty, and appropriation as cross-cutting sociotechnical properties of the artifact, not only of its technical mechanisms.

</details>

---

### [[20_Research/Papers/大模型/VLD-RAG_Agentic_Vision-Language_Retrieval-Augmented_Generation_for_Long,_Visually-Rich_Multi-Page_Documents|VLD-RAG: Agentic Vision-Language Retrieval-Augmented Generation for Long, Visually-Rich Multi-Page Documents]]

![[assets/2607.24748_figure.png|800]]

- **arXiv**: [2607.24748](https://arxiv.org/abs/2607.24748)
- **PDF**: https://arxiv.org/pdf/2607.24748
- **详细分析**: [[20_Research/Papers/大模型/VLD-RAG_Agentic_Vision-Language_Retrieval-Augmented_Generation_for_Long,_Visually-Rich_Multi-Page_Documents|VLD-RAG: Agentic Vision-Language Retrieval-Augmented Generation for Long, Visually-Rich Multi-Page Documents]]
- **作者**: Seonok Kim
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《VLD-RAG: Agentic Vision-Language Retrieval-Augmented Generation for Long, Visually-Rich Multi-Page Documents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FinRAGBench, LongDocURL, MMLongBench, MRAG-Bench, SK-VQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visually-rich documents such as reports, slides, and manuals often distribute the evidence needed to answer a question across multiple pages, mixing text with layout cues, tables, charts, and figures. This work studies multimodal retrieval-augmented generation for question answering over such visually-rich long documents, where retrieval must select evidence pages that include both textual and visual signals. We present VLD-RAG, an agentic multimodal RAG framework for multi-page evidence retrieval and cross-page reasoning over long documents. VLD-RAG builds a page-preserving multimodal index that stores parsed text, page-level metadata, and dense visual representations, and uses a hybrid retrieval strategy that combines keyword-based sparse search with dense semantic queries to identify candidate sources and evidence pages. A verifier-guided agent workflow coordinates a Retrieval Agent, Answer Agent, and Validation Agent to broaden evidence coverage, detect missing citations, and refine retrieval requests when needed. We evaluate retrieval with Top-1 and Top-5 evidence-page accuracy and generation with generalized accuracy, and show that VLD-RAG improves both evidence-page retrieval and end-task question answering on visually-rich long-document benchmarks, including LongDocURL and MMLongBench-Doc, outperforming previous vision-based retrieval baselines. These findings highlight that coordinated agent verification and multimodal hybrid retrieval are crucial for reliable grounding when correct answers depend on evidence scattered across pages.

</details>

---
