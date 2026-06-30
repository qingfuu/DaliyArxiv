# cs.AI | Artificial Intelligence | 2026-06-29

#arxiv #ComputerScience

**论文数**: 41

### [[20_Research/Papers/强化学习/DexCompose_Reusing_Dexterous_Policies_for_Multi-Task_Manipulation_with_a_Single_Hand|DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand]]

![[assets/2606.28323_figure.png|800]]

- **arXiv**: [2606.28323](https://arxiv.org/abs/2606.28323)
- **PDF**: https://arxiv.org/pdf/2606.28323
- **详细分析**: [[20_Research/Papers/强化学习/DexCompose_Reusing_Dexterous_Policies_for_Multi-Task_Manipulation_with_a_Single_Hand|DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand]]
- **作者**: Dihong Huang, Zhenyu Wei, Zhuxiu Xu, Yunchao Yao, Sikai Li, Mingyu Ding
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DexGraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation policies can solve individual skills, but composing them to perform multiple tasks with a single hand remains challenging. Adding a new task on top of an existing manipulation skill often imposes conflicting demands on overlapping fingers and contact modes, causing destructive interference between preserving an existing manipulation outcome and executing a new one. We propose DexCompose, a role-aware residual composition framework that reuses pretrained dexterous policies for multi-task manipulation through explicit finger-level action ownership. Given two pretrained full-hand policies, DexCompose first collects successful post-task states from the first skill and performs release tests over candidate finger masks to identify which fingers are necessary for maintaining the established skill state. It then trains two asymmetric residual modules: a bounded residual stabilizer for task preservation, and a context-aware residual that adapts the frozen downstream policy only within the action subspace assigned to the new task. We evaluate the framework on 16 composite dexterous manipulation tasks spanning four object-retention skills and four downstream interactions. DexCompose achieves a 77.4% average composite success rate, demonstrating that structural action ownership with dual residuals offers a promising direction for composing dexterous skills beyond conventional policy chaining.

</details>

---

### [[20_Research/Papers/其他/Agent-Native_Immune_System_Architecture,_Taxonomy,_and_Engineering|Agent-Native Immune System: Architecture, Taxonomy, and Engineering]]

![[assets/2606.28270_first_page.png|800]]

- **arXiv**: [2606.28270](https://arxiv.org/abs/2606.28270)
- **PDF**: https://arxiv.org/pdf/2606.28270
- **详细分析**: [[20_Research/Papers/其他/Agent-Native_Immune_System_Architecture,_Taxonomy,_and_Engineering|Agent-Native Immune System: Architecture, Taxonomy, and Engineering]]
- **作者**: Bo Shen, Lifeng Chang, Tianyuan Wei, Yunpeng Li, Feng Shi, Yichen Han, Peijie Gao, Shiyi Kuang, Xin Chang, Dehui Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Robotics, Security

#### 研究背景与动机

《Agent-Native Immune System: Architecture, Taxonomy, and Engineering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape. Current defense mechanisms, such as perimeter security and training-time alignment, remain external to the agent's active reasoning loop. Consequently, they fall short: a fully aligned agent remains highly vulnerable to runtime hijacking via memory poisoning, tool-chain manipulation, or multi-agent protocol attacks. To address this critical gap, we introduce the Agent-Native Immune System (ANIS), the first biologically inspired, endogenous defense architecture embedded directly within the agent's cognitive loop. Our framework presents four primary contributions. First, we design a six-layer Immune Tower (L0-L5), distinctly incorporating Barrier Immunity (L1) as a non-cognitive, physical-and-logical isolation layer. Second, we establish a unified taxonomy of Agent Viruses and Agent Vaccines, formalizing the critical distinction between superficial non-parametric defenses and robust parametric vaccines. Third, we conceptualize the Harness Triad--Meta, Self, and Auto--a self-monitoring, meta-cognitive automation backbone that drives Continual Immune Learning (CIL), enabling vaccines to dynamically adapt to novel threats. Finally, we establish a rigorous theoretical demarcation between model alignment and agent immunity: while alignment provides a static "constitutional" value foundation during training, ANIS serves as the dynamic "law enforcement" mechanism during runtime. We conclude by framing open challenges for the field, including immune protocol standardization, novel evaluation metrics such as the Autoimmunity Rate (false-positive intervention rate), and the co-evolutionary dynamics between pathogens and vaccines within collective intelligence ecosystems.

</details>

---

### [[20_Research/Papers/其他/Govern_the_Repository,_Not_the_Agent_Measuring_Ecosystem-Level_Risk_in_AI-Native_Software|Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software]]

![[assets/2606.28235_figure.png|800]]

- **arXiv**: [2606.28235](https://arxiv.org/abs/2606.28235)
- **PDF**: https://arxiv.org/pdf/2606.28235
- **详细分析**: [[20_Research/Papers/其他/Govern_the_Repository,_Not_the_Agent_Measuring_Ecosystem-Level_Risk_in_AI-Native_Software|Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software]]
- **作者**: Daniel Russo
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for. We ask whether this problem belongs to the individual agent or to the repository where it accumulates. We study integration friction, the cost of integrating a contribution into a codebase that other contributors are concurrently changing. Across more than 930,000 agent-authored pull requests, we measure how much of the variation in friction stays with the repository after the contribution, its author, its size, and its agent are accounted for. About half does, and it survives full controls. In the same repositories, agent-authored contributions concentrate this repository-level friction roughly twice as much as human ones (intraclass correlation 0.30 versus 0.16), a gap that holds after controlling for codebase size, age, task shape, process maturity, and merge path. The risk is a property of the ecosystem, not the agent. AI-native software is therefore better measured and governed at the ecosystem level than one agent at a time.

</details>

---

### [[20_Research/Papers/具身智能/HAT-4D_Lifting_Monocular_Video_for_4D_Multi-Object_Interactions_via_Human-Agent_Collaboration|HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration]]

![[assets/2606.28215_figure.png|800]]

- **arXiv**: [2606.28215](https://arxiv.org/abs/2606.28215)
- **PDF**: https://arxiv.org/pdf/2606.28215
- **详细分析**: [[20_Research/Papers/具身智能/HAT-4D_Lifting_Monocular_Video_for_4D_Multi-Object_Interactions_via_Human-Agent_Collaboration|HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration]]
- **作者**: Jiaxin Li, Yuxiang Wu, Zhenkai Zhang, Xinrui Shi, Haoyuan Wang, Yichen Zhao, Su Linxiang, Chenyang Yu, Mingyu Zhang, Yifan Ding, Boran Wen, Li Zhang...
- **cs 子类**: cs.AI, cs.CV, cs.GR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at https://lijiaxin0111.github.io/HAT4D/

</details>

---

### [[20_Research/Papers/大模型/Cognitive_Episodes_in_LLM_Reasoning_Traces_Enable_Interpretable_Human_Item_Difficulty_Prediction|Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction]]

![[assets/2606.28186_first_page.png|800]]

- **arXiv**: [2606.28186](https://arxiv.org/abs/2606.28186)
- **PDF**: https://arxiv.org/pdf/2606.28186
- **详细分析**: [[20_Research/Papers/大模型/Cognitive_Episodes_in_LLM_Reasoning_Traces_Enable_Interpretable_Human_Item_Difficulty_Prediction|Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction]]
- **作者**: Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou
- **cs 子类**: cs.AI, cs.CL, cs.CY, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting human item difficulty is central to educational assessment, where reliable estimates support fairness and effective test construction. Existing methods often depend on costly human calibration or item-level textual representations, providing limited evidence about the cognitive processes that make items difficult. We argue that difficulty should be viewed not only as a property of item text, but also as an observable consequence of the problem-solving burden an item induces. Large Reasoning Models (LRMs) offer scalable process evidence through reasoning traces, but such evidence must be structured to support interpretable modeling. To this end, we introduce Epi2Diff (Episode to Difficulty), a framework that maps LRM reasoning traces into cognitively grounded episode sequences. These episodes group trace segments into functional problem-solving states, enabling difficulty to be modeled through reasoning scale, effort allocation, and state transitions. Epi2Diff extracts compact episode-dynamic features and combines them with semantic item representations for human difficulty prediction. Experiments on four real-world human difficulty datasets show that Epi2Diff consistently outperforms strong baselines, including fine-tuned small language models, LLM in-context learning, and supervised LLM adaptation. On SAT-derived classification benchmarks, Epi2Diff achieves an 8.1% average relative gain over supervised LLM fine-tuning baselines. Further analyses show that harder items induce more effortful, iterative, and implementation-centered episode dynamics, rather than merely longer responses. These results demonstrate that cognitive episodes in LRM reasoning traces provide a predictive and interpretable process representation for human item difficulty, offering a new lens for educational measurement with reasoning models.

</details>

---

### [[20_Research/Papers/具身智能/LLawCo_Learning_Laws_of_Cooperation_for_Modeling_Embodied_Multi-Agent_Behavior|LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior]]

![[assets/2606.28182_figure.png|800]]

- **arXiv**: [2606.28182](https://arxiv.org/abs/2606.28182)
- **PDF**: https://arxiv.org/pdf/2606.28182
- **详细分析**: [[20_Research/Papers/具身智能/LLawCo_Learning_Laws_of_Cooperation_for_Modeling_Embodied_Multi-Agent_Behavior|LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior]]
- **作者**: Qinhong Zhou, Chuang Gan, Anoop Cherian
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.8，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents operating in decentralized and partially observable environments have attracted growing attention in recent years. However, existing large language model (LLM)-based agents often exhibit behaviors that are misaligned with their partners or inconsistent with the environment state, leading to inefficient cooperation and poor task success. To address this challenge, we propose a novel framework, Learning Laws of Cooperation (LLawCo), that enables embodied agents to autonomously align with both their partners and task objectives. Our framework allows agents to reflect on past failures to extract misaligned behavioral patterns, which are used to derive high-level behavioral laws, such as "Talk when necessary" and "Wait for partner." These laws are explicitly incorporated into the agents' chains of thought via supervised fine-tuning, aligning their reasoning with task requirements and the behavior of other agents. To evaluate our approach, we introduce PARTNR-Dialog, a large-scale multi-agent communicative and cooperative planning benchmark built on the PARTNR environment. Experiments on existing tasks and our new benchmark demonstrate significant improvements in cooperative efficiency and task success rates. Across four backbone LLMs, our method achieves average success rate improvements of 4.5% on the PARTNR-Dialog benchmark and 6.8% on the TDW-MAT benchmark over state-of-the-art open-source communicative agent frameworks. See the LLawCo project page for details: https://www.merl.com/research/highlights/LLawCo

</details>

---

### [[20_Research/Papers/强化学习/Tandem_Reinforcement_Learning_with_Verifiable_Rewards|Tandem Reinforcement Learning with Verifiable Rewards]]

![[assets/2606.28166_figure.png|800]]

- **arXiv**: [2606.28166](https://arxiv.org/abs/2606.28166)
- **PDF**: https://arxiv.org/pdf/2606.28166
- **详细分析**: [[20_Research/Papers/强化学习/Tandem_Reinforcement_Learning_with_Verifiable_Rewards|Tandem Reinforcement Learning with Verifiable Rewards]]
- **作者**: Difan Jiao, Raghav Singhal, Robert West, Ashton Anderson
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Tandem Reinforcement Learning with Verifiable Rewards》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capability of large language models, reaching expert or even superhuman performance in domains such as competition math. However, whether weaker agents and humans can actually harness this capability is far less certain, with RLVR documented to drift reasoning toward idiosyncratic patterns such as poor readability and language mixing. Tandem training is a recently introduced paradigm that targets this compatibility problem: a trained, stronger senior co-generates each rollout with a frozen, weaker junior, and the two are rewarded as a team, so the senior is pushed to reason in ways the junior can follow. Yet this paradigm has so far been demonstrated only in proof-of-concept settings, leaving open whether it scales to the long chains of thought of the modern RLVR pipeline. In this work, we propose Tandem Reinforcement Learning (TRL), which carries the tandem training paradigm into RLVR. In TRL, the senior and a frozen junior alternate stochastically to co-generate the reasoning, the resulting generation is rewarded, and the standard GRPO loss is applied to the senior. Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. Our results demonstrate a promising route for RLVR with practical payoffs in multi-model communication and human compatibility.

</details>

---

### [[20_Research/Papers/具身智能/PhysisForcing_Physics_Reinforced_World_Simulator_for_Robotic_Manipulation|PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation]]

![[assets/2606.28128_figure.png|800]]

- **arXiv**: [2606.28128](https://arxiv.org/abs/2606.28128)
- **PDF**: https://arxiv.org/pdf/2606.28128
- **详细分析**: [[20_Research/Papers/具身智能/PhysisForcing_Physics_Reinforced_World_Simulator_for_Robotic_Manipulation|PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation]]
- **作者**: Peiwen Zhang, Yufan Deng, Shangkun Sun, Juncheng Ma, Duomin Wang, Jonas Du, Zilin Pan, Ye Huang, Hao Liang, Songyan Huang, Ruihua Zhang, Enze Xie...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.3（加权：具身智能 1.8，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ABot-PhysWorld, CTRL-World, EZS-Bench, PAI-Bench, R-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. Through extensive experiments, we find that such physical instability mainly arises from two factors: deformation of moving objects and implausible spatio-temporal correlations among interacting entities, particularly during contact. Building on this observation, we propose PhysisForcing, a scalable training framework that strengthens physical consistency by focusing supervision on physics-informative regions through joint optimization of pixel-level and semantic-level features. The framework consists of a pixel-level trajectory alignment loss, which supervises DiT features using reference point trajectories, and a semantic-level relational alignment loss, which aligns DiT features with inter-region relations extracted from a frozen video understanding encoder. Extensive experiments on R-Bench, PAI-Bench, and EZS-Bench show that PhysisForcing consistently improves embodied video generation over strong baselines, improving the Wan2.2-I2V-A14B and Cosmos3-Nano base models on R-Bench by 22.3\% and 9.2\% (7.1\% and 3.7\% over vanilla finetuning), with the Cosmos3-Nano variant attaining the best overall score. Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation.

</details>

---

### [[20_Research/Papers/大模型/From_Tokens_to_States_LLMs_as_a_Special_Case_of_World_Models_and_the_Continuous_Path_Beyond|From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond]]

![[assets/2606.28127_first_page.png|800]]

- **arXiv**: [2606.28127](https://arxiv.org/abs/2606.28127)
- **PDF**: https://arxiv.org/pdf/2606.28127
- **详细分析**: [[20_Research/Papers/大模型/From_Tokens_to_States_LLMs_as_a_Special_Case_of_World_Models_and_the_Continuous_Path_Beyond|From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond]]
- **作者**: Paul Dubois
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM

#### 研究背景与动机

《From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The AI community has framed the relationship between large language models (LLMs) and world models as a dichotomy: LLMs predict tokens; world models simulate reality. Yann LeCun argues in 2022 that reaching general intelligence requires abandoning autoregressive token prediction in favour of latent-space architectures. This framing is unnecessarily binary. Two claims will be defended. First, LLMs are a degenerate special case of world models: the state space is the set of all token sequences, the only action is appending one token, and world models are therefore a strict generalisation of LLMs, not a replacement. Second, there is a natural continuous spectrum from NTP to JEPA, with multi-token prediction, future-summary prediction, and next-latent prediction as intermediate stations already populated by current research. Moving along this spectrum relaxes the LLM constraints one by one. It also progressively surrenders the two practical advantages that make LLMs trainable at scale: internet-scale self-supervised data, and a transformer architecture co-designed for discrete token prediction. Both are examined as open research questions: the data question (the cliff from self-supervised text to instrumented action-labelled environments) and the architecture question (whether the transformer generalises to continuous-state prediction, or whether a new primitive is needed).

</details>

---

### [[20_Research/Papers/大模型/JD_Oxygen_AI_Item_Center_(Oxygen_AIIC)_V1_An_Industrial-Scale_LLM_VLM-Centric_Solution_for_Item_Understanding,_Management,_and_Applications|JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications]]

![[assets/2606.28070_figure.png|800]]

- **arXiv**: [2606.28070](https://arxiv.org/abs/2606.28070)
- **PDF**: https://arxiv.org/pdf/2606.28070
- **详细分析**: [[20_Research/Papers/大模型/JD_Oxygen_AI_Item_Center_(Oxygen_AIIC)_V1_An_Industrial-Scale_LLM_VLM-Centric_Solution_for_Item_Understanding,_Management,_and_Applications|JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications]]
- **作者**: Oxygen AIIC, Chan Long, Chao Liu, Chaofan Chen, Chaohui Dong, Chunyuan Guo, Danping Liu, Debin Liu, Deping Xiang, Fulai Xu, Guangyue Liu, Hao Li...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

JD.com, one of the world's largest e-commerce platforms, serves over 700 million active users and millions of merchants, with a catalog of tens of billions of SKUs. At this scale, high-quality, structured item knowledge underpins a better consumer experience, lower management costs, and higher operational efficiency-yet producing and serving it poses three industrial-scale challenges: fast-emerging concepts, high-quality knowledge production for massive SKUs, and diverse downstream requirements. To address these challenges, we present the JD Oxygen AI Item Center (Oxygen AIIC), an industrial-scale platform built on LLMs/VLMs for item-knowledge production and service. Oxygen AIIC is built around four core pillars: (i) ontology engineering driven by efficient human-AI collaboration, which supports the dynamic evolution and agile expansion of an ontology with millions of entries; (ii) a "Semantic Search then Discrimination"(S2D) knowledge identification architecture that, combined with throughput improvement strategies, enables scalable, extensible, and high-throughput AI Item Library production for tens of billions of SKUs; (iii) self-evolving item-understanding LLMs/VLMs that improve in a stable and controllable manner, enabling knowledge production with 94.2% precision and 82.8% recall; and (iv) a unified item tunnel that serves as the data and service hub. Oxygen AIIC now covers tens of thousands of JD categories and processes hundreds of millions of item updates per day on Huawei Ascend NPUs. It has accumulated hundreds of billions of item-knowledge assets. Deployed across core business scenarios-including search, recommendation, operations, category planning-Oxygen AIIC has delivered measurable gains at scale. Search-traffic coverage reaches 80.4%, item-information quality issues drop by 37%, the automated fill rate of core attributes during item listing exceeds 80%.

</details>

---

### [[20_Research/Papers/大模型/ToolPrivacyBench_Benchmarking_Purpose-Bound_Privacy_in_Tool-Using_LLM_Agents|ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents]]

![[assets/2606.28061_figure.png|800]]

- **arXiv**: [2606.28061](https://arxiv.org/abs/2606.28061)
- **PDF**: https://arxiv.org/pdf/2606.28061
- **详细分析**: [[20_Research/Papers/大模型/ToolPrivacyBench_Benchmarking_Purpose-Bound_Privacy_in_Tool-Using_LLM_Agents|ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents]]
- **作者**: Shijing Hu, Liang Liu, Zhu Meng, Zhicheng Zhao
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, AgentBench, AppWorld, PrivLM-Bench, TRAJECT-Bench, ToolPrivacyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. Neither perspective captures purpose-bound information flow across an executed multi-tool trajectory. Motivated by this limitation in current agent evaluation, ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks, thereby evaluating both task completion and privacy over-disclosure during tool use. The benchmark contains 2,150 cases, including 1,150 fully synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks. Each case is represented by a policy knowledge base. After an agent executes against mock business backends, the evaluator compares recorded tool arguments and backend audit logs with this policy knowledge base. The evaluation covers nine widely used agents to characterize purpose-bound privacy over-disclosure. The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.

</details>

---

### [[20_Research/Papers/大模型/Dialogue_to_Detection_A_Multimodal_Hybrid_NLP_Pipeline_for_Insurance_Fraud_Detection|Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection]]

![[assets/2606.28002_figure.png|800]]

- **arXiv**: [2606.28002](https://arxiv.org/abs/2606.28002)
- **PDF**: https://arxiv.org/pdf/2606.28002
- **详细分析**: [[20_Research/Papers/大模型/Dialogue_to_Detection_A_Multimodal_Hybrid_NLP_Pipeline_for_Insurance_Fraud_Detection|Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection]]
- **作者**: Muhammad Shakeel Akram, Amal Htait, Abdul Hamid Sadka, Emma Meisingseth, Karishma Jaitly
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：XLNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Insurance fraud imposes substantial financial losses and operational inefficiencies, raising premiums and impacting trust among legitimate policyholders. Early detection at FNOL remains a persistent challenge. Existing approaches rely largely on private, text-only datasets, limiting progress on multimodal methods that integrate linguistic, behavioural, and speaker-based indicators. We introduce a synthetic multimodal framework that replicates FNOL conditions. It generates agent-customer dialogue transcripts and two-speaker audios, performs ASR and diarisation. Downstream modules combine NER, regex-based feature extraction, LLM-RAG retrieval, and speaker embeddings in a rule-based risk score to flag narrative reuse, structural inconsistencies, and cross-case voice repetition while balancing sensitivity and false positives. Dataset validation and component-level evaluations show stability and transfer potential, offering a reproducible baseline beyond text-only fraud detection.

</details>

---

### [[20_Research/Papers/大模型/ProMSA_Progressive_Multimodal_Search_Agents_for_Knowledge-Based_Visual_Question_Answering|ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering]]

![[assets/2606.27974_figure.png|800]]

- **arXiv**: [2606.27974](https://arxiv.org/abs/2606.27974)
- **PDF**: https://arxiv.org/pdf/2606.27974
- **详细分析**: [[20_Research/Papers/大模型/ProMSA_Progressive_Multimodal_Search_Agents_for_Knowledge-Based_Visual_Question_Answering|ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering]]
- **作者**: ZhengXian Wu, Hangrui Xu, Kai Shi, Zhuohong Chen, Yunyao Yu, Chuanrui Zhang, Zirui Liao, Jun Yang, Zhenyu Yang, Haonan Lu, Haoqian Wang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CC-VQA, E-VQA, KB-VQA, QKVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge-based Visual Question Answering (KB-VQA) requires models to combine image understanding with external knowledge. Most prior methods use a fixed retrieve-then-generate pipeline with a pre-selected retriever and a static top-k setting, which is not adaptive during reasoning. We propose ProMSA, a progressive multimodal search agent for KB-VQA. Given an image-question pair, the agent iteratively chooses image search, text search, or stop, under explicit tool-call budgets and with deduplication to avoid redundant retrieval. For training, we first use rejection-sampling SFT to learn valid tool-use formats, then optimize the agent with TN-GSPO, a sequence-level RL objective that normalizes updates by both generation length and tool-interaction depth. Experiments on E-VQA and InfoSeek show consistent gains over strong RAG and agent baselines, and improved retrieval and end-to-end accuracy. The code is available at https://github.com/DingWu1021/Promsa.

</details>

---

### [[20_Research/Papers/强化学习/Two-Stage_Fine-Tuning_for_Protein_Sequence_Generation_with_Targeted_Amino-Acid_Composition|Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition]]

![[assets/2606.27939_figure.png|800]]

- **arXiv**: [2606.27939](https://arxiv.org/abs/2606.27939)
- **PDF**: https://arxiv.org/pdf/2606.27939
- **详细分析**: [[20_Research/Papers/强化学习/Two-Stage_Fine-Tuning_for_Protein_Sequence_Generation_with_Targeted_Amino-Acid_Composition|Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition]]
- **作者**: Violeta Basten-Romero, Rubén Muñoz-Tafalla, Anna María Díaz-Rovira, Bertran Miquel-Oliver, Isaac Filella-Merce, Víctor Guallar
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Protein language models are standard priors for biological sequence generation, but steering them toward explicit distributional design targets remains largely unexplored. We study a constrained protein generation problem in which sequences must match a desired amino-acid (AA) composition profile while preserving plausible sequence statistics and diversity. The motivating application is synthetic feed protein design, where the AA composition of dietary proteins directly determines their nutritional value. We propose a two-stage pipeline in which domain-adaptive fine-tuning (FT) on an in-domain protein dataset is followed by iterative reward-weighted FT via reinforcement learning (RL) anchored against the FT model as a frozen reference. We evaluate the pipeline on two AA compositions and find that FT brings the average composition close to the target, while the subsequent RL enforces specific sequence constraints that FT alone cannot satisfy. We additionally evaluate the design choices of the proposed composition reward term against two baselines and an ablated variant, isolate the contribution of each training stage, and verify that AA composition alignment is achieved without degrading sequence quality.

</details>

---

### [[20_Research/Papers/大模型/Verifiable_Geometry_Problem_Solving_Solver-Driven_Autoformalization_and_Theorem_Proposing|Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem Proposing]]

![[assets/2606.27926_figure.png|800]]

- **arXiv**: [2606.27926](https://arxiv.org/abs/2606.27926)
- **PDF**: https://arxiv.org/pdf/2606.27926
- **详细分析**: [[20_Research/Papers/大模型/Verifiable_Geometry_Problem_Solving_Solver-Driven_Autoformalization_and_Theorem_Proposing|Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem Proposing]]
- **作者**: Can Li, Ting Zhang, Junbo Zhao, Hua Huang
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem Proposing》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GeoDRL, SG-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometry Problem Solving have increasingly adopt the neuro-symbolic paradigm, combining neural intuition with symbolic rigor. However, current frameworks suffer from severe bottlenecks in two core stages: autoformalization, which treats multimodal translation as a static task decoupled from downstream solver compatibility, and theorem prediction, where solvers frequently hit a deductive impasse due to fixed rule libraries. To address these, we propose SD-GPS, a solver-driven framework that treats the symbolic solver as an execution oracle throughout both formalization and deduction. First, Solver-Driven Autoformalization unifies supervised formal-language adaptation and solvability-guided reinforcement learning into a single module built on QwenVL3-2B, making executability the central training signal. Second, Verified Theorem Proposing introduces an impasse-aware agent that proposes local auxiliary lemmas from current proof states, ensuring soundness by filtering all proposals through symbolic verification. Empirical evaluations on Geometry3K and PGPS9K demonstrate that SD-GPS consistently outperforms existing MLLM, neural, and neuro-symbolic methods across standard completion, multiple-choice, and cross-modal reference regimes, proving that closing the loop between multimodal perception and symbolic execution significantly improves geometric reasoning, offering profound insights into how neural agents can be grounded by formal systems to achieve verifiable problem-solving capabilities.

</details>

---

### [[20_Research/Papers/具身智能/SpatialUAV_Benchmarking_Spatial_Intelligence_for_Low-Altitude_UAV_Perception,_Collaboration,_and_Motion|SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion]]

![[assets/2606.27876_figure.png|800]]

- **arXiv**: [2606.27876](https://arxiv.org/abs/2606.27876)
- **PDF**: https://arxiv.org/pdf/2606.27876
- **详细分析**: [[20_Research/Papers/具身智能/SpatialUAV_Benchmarking_Spatial_Intelligence_for_Low-Altitude_UAV_Perception,_Collaboration,_and_Motion|SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion]]
- **作者**: Haoyu Zhang, Meng Liu, Qianlong Xiang, Kun Wang, Yaowei Wang, Liqiang Nie
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirCopBench, CityEQA, ESI-Bench, MM-UAVBench, MMSI-Video-Bench, Open3D-VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial intelligence is essential for low-altitude unmanned aerial vehicle (UAV) perception, collaboration, and navigation. However, existing UAV benchmarks often emphasize image-level recognition, single-view understanding, or narrow answer formats, leaving 3D spatial inference, multi-view collaboration, scene dynamics, and diverse task formulations insufficiently evaluated. To address these gaps, we introduce SpatialUAV, a real low-altitude UAV benchmark comprising 4,331 curated instances across 14 fine-grained task types, covering semantic discrimination, spatial relation, aerial--aerial collaboration, aerial--ground collaboration, and motion understanding. SpatialUAV organizes all samples into a unified visual-input--question--answer schema, while supporting seven input configurations and nine answer formats, including option labels, region identifiers, geometric values, cross-view correspondences, and free-form motion descriptions. To ensure reliable and grounded evaluation, our data construction pipeline integrates detector-assisted regions, depth supervision, metadata-derived rules, extensive manual annotation, blind filtering, and multi-turn human validation, together with task-specific metrics for heterogeneous outputs. Evaluating representative vision-language models across three categories, we show that current models remain far from human-level performance, with pronounced bottlenecks in cross-view association, structured grounding, geometric reasoning, and temporal viewpoint understanding. These results offer empirical guidance for advancing low-altitude UAV spatial intelligence. Code and data are available at https://github.com/Hyu-Zhang/SpatialUAV.

</details>

---

### [[20_Research/Papers/具身智能/S$^2$-VLA_State-Space_Guided_Vision-Language-Action_Models_for_Long-Horizon_Manipulation|S$^2$-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation]]

![[assets/2606.27872_figure.png|800]]

- **arXiv**: [2606.27872](https://arxiv.org/abs/2606.27872)
- **PDF**: https://arxiv.org/pdf/2606.27872
- **详细分析**: [[20_Research/Papers/具身智能/S$^2$-VLA_State-Space_Guided_Vision-Language-Action_Models_for_Long-Horizon_Manipulation|S$^2$-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation]]
- **作者**: Zhipeng Xie, Zongyi Han, Xiangyi Wei, Shiliang Sun, Yang Li, Jing Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《S$^2$-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, CronusVLA, FlowVLA, MemoryVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation, but their performance degrades significantly in long-horizon tasks due to cumulative error propagation. This limitation largely arises from static feature fusion mechanisms that rely on fixed weights to combine visual, language, and action representations, preventing the model from adapting to different phases of task execution. To address this limitation, we propose S$^2$-VLA, a framework that introduces a State-Space Guided Adaptive Attention (SSGAA) mechanism. SSGAA maintains a belief state that tracks task progression and generates dynamic gating weights to adaptively fuse information from three complementary sources visual features for spatial perception, task intents for high-level task planning, and temporal action sequences for execution consistency. This adaptive fusion allows the model to shift its focus throughout task execution, aligning with the evolving requirements of different task stages. Despite its compact 2B parameter size, S$^2$-VLA consistently outperforms larger 7B-scale models and achieves state-of-the-art performance on long-horizon manipulation benchmarks, including LIBERO and SimplerEnv. highlighting the importance of adaptive feature fusion for long-horizon robotic manipulation.

</details>

---

### [[20_Research/Papers/具身智能/NormAct_A_Benchmark_for_Hidden_Social_Norm_Compliance_in_Embodied_Planning|NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning]]

![[assets/2606.27826_figure.png|800]]

- **arXiv**: [2606.27826](https://arxiv.org/abs/2606.27826)
- **PDF**: https://arxiv.org/pdf/2606.27826
- **详细分析**: [[20_Research/Papers/具身智能/NormAct_A_Benchmark_for_Hidden_Social_Norm_Compliance_in_Embodied_Planning|NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning]]
- **作者**: Shiyun Zhao, Xinwei Song, Tianyu Guo, Xiaomeng Gao, Mingyuan Liu, Xu Han, Yuanyuan Zhang, Zhenliang Zhang, Xue Feng, Bo Dai
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 1.2，大模型 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeliveryBench, EmbodiedBench, SimWorld, TongSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) are increasingly deployed as embodied planners in egocentric environments, where task success requires not only achieving instructed goals but also acting in socially appropriate ways. While explicit goals may render certain actions optimal, implicit social norms often impose hidden constraints. Existing evaluations typically focus on explicit goal achievement or direct norm knowledge, seldom assessing whether planners can infer and apply these hidden constraints within action sequences. We introduce NormAct, a benchmark for embodied social-norm interactions that evaluates plans on Goal Achievement, Norm Compliance, and overall Task Success. NormAct uniquely embeds hidden norms within ordinary tasks, testing whether models can realize them without explicit instruction. Experiments with state-of-the-art MLLMs (GPT-5.4, Claude Opus 4.7, Gemini 3 Pro) reveal a significant gap: models achieve explicit goals in 67.3\% of cases, but comply with hidden norms in only 26.4\%. Cue-condition experiments indicate that this gap stems not from a lack of general social knowledge, but from challenges in activating and grounding relevant norms in context. To address this, we propose NormPerceptor, a context-conditioned cue generator that infers scene-relevant norms prior to planning, increasing Task Success from 24.2\% to 46.7\%. Our results underscore the importance of enabling embodied agents to proactively detect hidden norms, ground them in visual evidence, and integrate them as action-planning constraints. Our benchmark is publicly available at https://huggingface.co/datasets/Caleb196x/NormAct.

</details>

---

### [[20_Research/Papers/强化学习/ATOD_Annealed_Turn-aware_On-policy_Distillation_for_Multi-turn_Autonomous_Agents|ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents]]

![[assets/2606.27814_figure.png|800]]

- **arXiv**: [2606.27814](https://arxiv.org/abs/2606.27814)
- **PDF**: https://arxiv.org/pdf/2606.27814
- **详细分析**: [[20_Research/Papers/强化学习/ATOD_Annealed_Turn-aware_On-policy_Distillation_for_Multi-turn_Autonomous_Agents|ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents]]
- **作者**: Qitai Tan, Zefang Zong, Yang Li, Peng Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, OPD-RL, Search-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. Reinforcement learning (RL) directly optimizes environment rewards and encourages exploratory improvement toward a higher reward-defined ceiling, but sparse and delayed feedback makes early-stage learning much less efficient than OPD. In this paper, we propose ATOD (Annealed Turn-aware On-policy Distillation), a hybrid online distillation algorithm that explicitly exploits this complementarity. (1) ATOD uses an annealed OPD-RL schedule: OPD dominates early training to approach teacher-level behavior, while RL is gradually strengthened to drive reward-based exploration. (2) ATOD introduces Turn-level Disagreement-Uncertainty Reweighting (T-DUR), which softly amplifies high-utility turns and improves dense supervision in long trajectories. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 3.03 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.

</details>

---

### [[20_Research/Papers/大模型/Grounded_Iterative_Language_Planning_How_Parameterized_World_Models_Reduce_Hallucination_Propagation_in_LLM_Agents|Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents]]

![[assets/2606.27806_figure.png|800]]

- **arXiv**: [2606.27806](https://arxiv.org/abs/2606.27806)
- **PDF**: https://arxiv.org/pdf/2606.27806
- **详细分析**: [[20_Research/Papers/大模型/Grounded_Iterative_Language_Planning_How_Parameterized_World_Models_Reduce_Hallucination_Propagation_in_LLM_Agents|Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents]]
- **作者**: Xinyuan Song, Zekun Cai
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.9（加权：大模型 0.9，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the agent-based case. The comparison motivates \textbf{Grounded Iterative Language Planning} (GILP), which trains only a small parameterized backbone and combines it with API-based agent reasoning. The backbone supplies valid actions, predicted state deltas, risk, and value; the LLM drafts an action and imagined delta; and a consistency gate asks for revision when the two disagree. On real GPT-4o-mini calls, GILP reduces hallucinated-state rate from 0.176 to 0.035. In calibrated simulator ablations, it raises success from 0.668 to 0.838 while adding only ~22% extra LLM calls.

</details>

---

### [[20_Research/Papers/大模型/SHIFT_Gate-Modulated_Activation_Steering_for_Knowledge_Conflict_Mitigation_in_Retrieval-Augmented_Generation|SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation]]

![[assets/2606.27786_figure.png|800]]

- **arXiv**: [2606.27786](https://arxiv.org/abs/2606.27786)
- **PDF**: https://arxiv.org/pdf/2606.27786
- **详细分析**: [[20_Research/Papers/大模型/SHIFT_Gate-Modulated_Activation_Steering_for_Knowledge_Conflict_Mitigation_in_Retrieval-Augmented_Generation|SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation]]
- **作者**: Ruochang Li, Pengcheng Huang, Zhenghao Liu, Yukun Yan, Huiyuan Xie, Yu Gu, Ge Yu, Maosong Sun
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.AI

#### 研究背景与动机

《SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：HotpotQA, NewsQA, SearchQA, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) enhances LLMs by incorporating external knowledge to support response generation. However, conflicts between retrieved context and parametric knowledge have emerged as a critical challenge in RAG systems. To mitigate such conflicts, numerous studies have attempted to identify and edit knowledge-related internal neurons, aiming to improve the ability of LLMs to rely on contextual evidence during generation. However, these neuron-level approaches may introduce unintended cascading effects that compromise the general capabilities of LLMs, as the modified neurons are often entangled with broader model behaviors and functionalities. In this paper, we introduce SHIFT, a novel framework that reformulates neuron-level modification as learnable gate modulation, allowing LLMs to adaptively regulate internal activations for knowledge conflict resolution. Technically, our SHIFT equips LLMs with a lightweight gate module and optimizes fewer than 0.01% trainable parameters while keeping the backbone model frozen. During generation, the gate module adjusts the model's internal representations to adaptively leverage contextual and parametric knowledge. Extensive experiments on six datasets validate the effectiveness of our SHIFT in comparison with various competing baselines. All datasets and code are available at https://github.com/OpenBMB/SHIFT.

</details>

---

### [[20_Research/Papers/大模型/Output-Space_Allocation_Costs_for_Calibration-Guided_LLM_Compression_An_Empirical_Study|Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical Study]]

![[assets/2606.27785_figure.jpeg|800]]

- **arXiv**: [2606.27785](https://arxiv.org/abs/2606.27785)
- **PDF**: https://arxiv.org/pdf/2606.27785
- **详细分析**: [[20_Research/Papers/大模型/Output-Space_Allocation_Costs_for_Calibration-Guided_LLM_Compression_An_Empirical_Study|Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical Study]]
- **作者**: Qiong Tang, Xiangkun Hu, Xiangyang Liu, Yiran Chen, Yunfan Shao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM

#### 研究背景与动机

《Output-Space Allocation Costs for Calibration-Guided LLM Compression: An Empirical Study》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PIQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training-free compression methods for large language models (LLMs) often use calibration data to guide compression decisions. ROCKET, a recent method combining sparse-dictionary factorization with multi-choice knapsack problem (MCKP) allocation, derives its per-layer factorization from an output reconstruction objective but uses weight-space Frobenius error as the MCKP allocation cost. We investigate whether aligning the allocation cost with the output-space objective improves compressed model fidelity. On Qwen3-8B at 50\% compression, our ROCKET-ActCost achieves +0.8 percentage points higher average accuracy across 8 zero-shot benchmarks (53.1\% vs 52.3\%), but increases WikiText perplexity by 16\% (61.46 vs 52.98). This accuracy-perplexity tradeoff reveals that different allocation objectives favor different downstream metrics. The high correlation ($&gt;$0.99) between weight-space and output-space errors limits allocation divergence, explaining the modest effect size. On Llama-3.2-1B at 20\% compression, the two methods produce near-identical results (53.3\% vs 53.5\% accuracy, 14.45 vs 14.66 PPL), suggesting that the effect of the cost function is minor at lower compression ratios.

</details>

---

### [[20_Research/Papers/世界模型/Understanding_Rollout_Error_in_Graph_World_Models|Understanding Rollout Error in Graph World Models]]

![[assets/2606.27780_figure.png|800]]

- **arXiv**: [2606.27780](https://arxiv.org/abs/2606.27780)
- **PDF**: https://arxiv.org/pdf/2606.27780
- **详细分析**: [[20_Research/Papers/世界模型/Understanding_Rollout_Error_in_Graph_World_Models|Understanding Rollout Error in Graph World Models]]
- **作者**: Xinyuan Song, Zekun Cai
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，世界模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《Understanding Rollout Error in Graph World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are often used for planning by rolling learned dynamics forward. Many planning environments, however, are not vectors or images; they are graphs of agents, tools, skills, routes, and dependencies. In these settings, a local prediction error may stay local or spread through the graph, and the failure mode changes again when edges are predicted rather than fixed. This paper studies long-horizon rollout error in Graph World Models (GWMs). We formulate a unified fixed-edge and dynamic-edge GWM framework with action nodes for node-, edge-, and graph-level decisions. We develop graph-valued rollout bounds that separate topology-induced amplification from model-induced amplification, and we introduce a joint node-edge operator for dynamic-edge rollouts. Guided by the analysis, we propose Error-Aware GWM, which combines spectral regularization, rollout consistency, and critical-node weighting. Across synthetic topologies and heterogeneous agent-graph testbeds, rollout error and planning regret grow with horizon, dynamic-edge training is needed when structure evolves, and Error-Aware GWM prevents long-horizon divergence while preserving prediction accuracy. Real-world graph benchmarks clarify the scope of GWMs: they are most useful for dynamic graph rollout and agent planning, while specialized graph models remain strong on static or sparse prediction tasks.

</details>

---

### [[20_Research/Papers/具身智能/RS-Diffuser_Risk-Sensitive_Diffusion_Planning_with_Distributional_Value_Guidance|RS-Diffuser: Risk-Sensitive Diffusion Planning with Distributional Value Guidance]]

![[assets/2606.27766_figure.png|800]]

- **arXiv**: [2606.27766](https://arxiv.org/abs/2606.27766)
- **PDF**: https://arxiv.org/pdf/2606.27766
- **详细分析**: [[20_Research/Papers/具身智能/RS-Diffuser_Risk-Sensitive_Diffusion_Planning_with_Distributional_Value_Guidance|RS-Diffuser: Risk-Sensitive Diffusion Planning with Distributional Value Guidance]]
- **作者**: Shiqiang Gong
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.12（加权：具身智能 0.6，大模型 0.1，强化学习 0.56，世界模型 0.36，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RS-Diffuser: Risk-Sensitive Diffusion Planning with Distributional Value Guidance》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, ICRL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning enables policy learning from fixed datasets without additional environment interaction, making it appealing for safety-critical applications where online exploration is costly or unsafe. Diffusion-based decision-making methods have recently achieved strong performance in offline RL by modeling rich, multimodal trajectory distributions. However, existing diffusion planners are typically risk-neutral and therefore may overlook rare but catastrophic outcomes that are crucial in real-world deployment. In this work, we propose RS-Diffuser, a risk-sensitive offline diffusion planning framework that combines diffusion-based trajectory generation with distributional value critics. RS-Diffuser learns a diffusion planner over future state trajectories, a separate inverse dynamics model for action decoding, and a Monte Carlo distributional critic that estimates the full return distribution of candidate plans through quantile regression. At sampling time, we incorporate a risk-sensitive guidance signal into the denoising process, using gradients computed from tail-aware objectives such as Conditional Value at Risk to steer generation toward desired risk profiles. As a result, a single trained model can flexibly produce risk-averse, risk-neutral, or risk-seeking behaviors by changing only the inference-time risk parameter. Extensive experiments on risk-sensitive D4RL and risky robot navigation benchmarks demonstrate that RS-Diffuser achieves state-of-the-art performance, improving both overall return and worst-case robustness while reducing safety violations.

</details>

---

### [[20_Research/Papers/大模型/Towards_Reliable_and_Robust_LLM_Planning_Symbolic_Feedback-Driven_Iterative_Self-Refinement_Framework|Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework]]

![[assets/2606.27757_figure.png|800]]

- **arXiv**: [2606.27757](https://arxiv.org/abs/2606.27757)
- **PDF**: https://arxiv.org/pdf/2606.27757
- **详细分析**: [[20_Research/Papers/大模型/Towards_Reliable_and_Robust_LLM_Planning_Symbolic_Feedback-Driven_Iterative_Self-Refinement_Framework|Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework]]
- **作者**: Jiajing Zhang, Jiamei Jiang, Chenyang Zhang, Feifei Mo, Linjing Li, Daniel Zeng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have attracted widespread attention from academia and industry, yet their deployment raises critical security concerns regarding robustness and reliability. Planning, a core component of intelligent behavior, remains challenging for LLMs, which often produce infeasible or incorrect solutions in long-horizon decision-making tasks due to inherent complexity. In this paper, we propose a symbolic feedback-driven iterative self-refinement framework to enhance the robustness and reliability of LLMs in long-horizon planning. Specifically, a natural language prompting mechanism is introduced to map logical symbols into natural language descriptions, enabling LLMs to better capture task constraints and semantics. We further design a symbolic verifier that identifies errors and converts them into corrective instructions interpretable by the LLM, thereby guiding self-refinement. In addition, we leverage a plan recognizer to infer goal reachability, facilitating more effective guidance toward desired goals. Empirical results demonstrate that the proposed framework consistently improves both feasibility and correctness in long-horizon planning tasks. This highlights its effectiveness in enhancing the reliability of LLM-based planning and potential to enable more trustworthy AI systems.

</details>

---

### [[20_Research/Papers/具身智能/Drop-Then-Recovery_How_Redundant_Are_Vision-Language-Action_Models|Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?]]

![[assets/2606.27755_figure.png|800]]

- **arXiv**: [2606.27755](https://arxiv.org/abs/2606.27755)
- **PDF**: https://arxiv.org/pdf/2606.27755
- **详细分析**: [[20_Research/Papers/具身智能/Drop-Then-Recovery_How_Redundant_Are_Vision-Language-Action_Models|Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?]]
- **作者**: Guoheng Sun, Kaixi Feng, Shwai He, Xiaochuan Gong, Yexiao He, Ziyao Wang, Zheyu Shen, Wanghao Ye, Ramana Rao Kompella, Gaowen Liu, Ang Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Lingbot-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable instruction-driven robotic manipulation, but they inherit oversized language backbones from pretrained VLMs whose capacity far exceeds what is needed for short robotic instructions. This raises a basic question: how much of a VLA model is actually necessary for closed-loop control? In this work, we study architectural redundancy in VLA models by using transformer block removal as a controlled intervention. We introduce \textbf{Drop-Then-Recovery (DTR)}, an analysis protocol that removes selected blocks from a pretrained VLA model and then fine-tunes the resulting model to measure whether the removed capacity was necessary for downstream control. To make this intervention reliable, we propose \textbf{GateProbe}, a one-shot virtual-gate sensitivity metric that ranks blocks by their contribution to the downstream action loss. Across multiple VLA architectures, manipulation benchmarks and even real-robot industrial scenarios, we find a strong asymmetry in post-removal recoverability: \ul{\textit{language backbones are highly redundant for standard robotic manipulation tasks, whereas vision and action pathways are substantially less tolerant to removal}}. On LIBERO, removing half of the LLM blocks even improves OpenVLA-OFT from 95.0% to 98.3% under the same downstream fine-tuning budget, and retaining only two language blocks still recovers baseline-level performance. These results suggest that current VLA benchmarks may exert limited pressure on deep language grounding and compositional instruction understanding, and that future VLA architectures should allocate capacity more deliberately across language, vision, and action components. The code is available at https://github.com/s1ghhh/VLADrop.

</details>

---

### [[20_Research/Papers/大模型/Low-Agreeableness_Persona_Conditioning_for_Safe_LLM_Fine-Tuning|Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning]]

![[assets/2606.27709_figure.png|800]]

- **arXiv**: [2606.27709](https://arxiv.org/abs/2606.27709)
- **PDF**: https://arxiv.org/pdf/2606.27709
- **详细分析**: [[20_Research/Papers/大模型/Low-Agreeableness_Persona_Conditioning_for_Safe_LLM_Fine-Tuning|Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning]]
- **作者**: Austin MY Cheung, Yi Yang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We investigate a related but distinct failure mode: warmth fine-tuning also weakens adversarial safety, making models more susceptible to jailbreaks and harmful output generation. We examine whether this reflects an inherent consequence of empathetic adaptation or an artifact of data construction. To address this, we introduce a persona-driven rewriting pipeline that conditions user turns on low agreeableness and pairs this with warm, de-escalating assistant responses. Across three experiments on four models, our approach reduces jailbreak susceptibility and harmful output rates relative to generic warmth fine-tuning baselines, while preserving conversational warmth. Representational probing provides suggestive evidence that this conditioning reduces the geometric alignment between warmth and compliance directions in latent space. These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.

</details>

---

### [[20_Research/Papers/大模型/Mitigating_LLM-based_p-Hacking_by_Preregistering_for_the_Next_LLM|Mitigating LLM-based p-Hacking by Preregistering for the Next LLM]]

![[assets/2606.27687_first_page.png|800]]

- **arXiv**: [2606.27687](https://arxiv.org/abs/2606.27687)
- **PDF**: https://arxiv.org/pdf/2606.27687
- **详细分析**: [[20_Research/Papers/大模型/Mitigating_LLM-based_p-Hacking_by_Preregistering_for_the_Next_LLM|Mitigating LLM-based p-Hacking by Preregistering for the Next LLM]]
- **作者**: Maria Thomas, Kristina Gligoric, Nihar B. Shah
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Mitigating LLM-based p-Hacking by Preregistering for the Next LLM》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used to generate, classify, and annotate data whose outputs feed downstream hypothesis tests. However, LLM-based research is easy to p-hack: a researcher can tune the prompts, decoding parameters, or output format until a desired result is reached. We propose a protocol to mitigate p-hacking in LLM-based research: preregistering the experiment and eligible models, and then running it on the first eligible LLM that is released after the preregistration. The researcher finalizes the procedure on current models, preregisters the analysis plan together with a set of eligible future models, and runs the confirmatory analysis on the first eligible model released afterward. Because this model does not exist at commitment time, it cannot be hacked against; furthermore, configurations that hack one model frequently do not transfer to the next. We evaluate the protocol on two tasks whose true values are known. Across 20 models from four providers and 11 LLM-analysis configurations, the protocol would have blocked successful transfer of the p-hack in 73.9% and 72.7% of cases in the two tasks. Additional analyses reveal that mitigation remains substantial under several stress tests. Finally, putting money where our mouth is, we followed our own protocol and preregistered our experiment. The preregistered experiment confirmed the protocol's effectiveness: out of the 7 configurations that hacked the prior model, the hacking failed to carry over in 6 configurations on the first eligible model released afterward.

</details>

---

### [[20_Research/Papers/大模型/MER-R1_Multimodal_Emotion_Reasoning_via_Slow-Fast_Thinking_Synergy|MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy]]

![[assets/2606.27652_figure.png|800]]

- **arXiv**: [2606.27652](https://arxiv.org/abs/2606.27652)
- **PDF**: https://arxiv.org/pdf/2606.27652
- **详细分析**: [[20_Research/Papers/大模型/MER-R1_Multimodal_Emotion_Reasoning_via_Slow-Fast_Thinking_Synergy|MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy]]
- **作者**: Zhiyuan Han, Beier Zhu, Wenwen Tong, Chengwei Qin, Xinyi Wang, Jiayu Zhang, Jiangnan Chen, Hewei Guo, Dongchuan Ran, Lewei Lu, Xun Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MER-UniBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We find that explicit reasoning does not necessarily translate into better multimodal emotion recognition (MER) accuracy, even though it makes predictions more interpretable. Specifically, for reasoning-based MLLMs, fast thinking by triggering direct answers often outperforms slow thinking after deliberative reasoning. Our empirical analyses show that fast thinking improves recall with broader and more confident predictions, whereas slow thinking favors precision through conservative filtering of incorrect categories. Building on these insights, we propose MER-R1, a reinforcement learning framework that turns slow-fast complementarity into explicit optimization. Dual-objective disentanglement separates recall and precision into two optimization signals, allowing them to be jointly optimized rather than traded off against each other. Slow-fast confidence calibration further aligns the final slow-thinking answer with fast-thinking intuition, strengthening correct emotions while suppressing incorrect ones. In this way, MER-R1 unifies the recall-oriented intuition of fast thinking with the precision-oriented selectivity of slow thinking. We further provide theoretical justification for this synergy, showing that it mitigates variance-induced interference during optimization. Extensive experiments on MER-UniBench and MME-Emotion show that MER-R1 achieves state-of-the-art performance and makes reasoning genuinely benefit emotion recognition.

</details>

---

### [[20_Research/Papers/大模型/DysLexLens_A_Low-Resource_LLM_Framework_for_Analysing_Dyslexic_Learners_Insights_from_Online_Forums|DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners Insights from Online Forums]]

![[assets/2606.27619_figure.png|800]]

- **arXiv**: [2606.27619](https://arxiv.org/abs/2606.27619)
- **PDF**: https://arxiv.org/pdf/2606.27619
- **详细分析**: [[20_Research/Papers/大模型/DysLexLens_A_Low-Resource_LLM_Framework_for_Analysing_Dyslexic_Learners_Insights_from_Online_Forums|DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners Insights from Online Forums]]
- **作者**: Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang
- **cs 子类**: cs.AI, cs.CL, cs.HC, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners Insights from Online Forums》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dyslexic learners increasingly use artificial intelligence (AI) tools to support reading, writing, organisation, and study-related tasks. However, their lived experiences with these tools remain largely underexamined. This paper proposes DysLexLens, a low-resource LLM framework, designed to analyse dyslexic learners experience with AI through online forum discussions. DysLexLens is designed as an end-to-end, evidence-traceable architecture which transforms noisy social media posts into a dictionary-driven corpora, provides knowledge-graph (KG)-based question reasoning, generates verifiable query responses, and enables response evaluation through quantitative and human-grounded assessment. DysLexLens has four key features. First, it employs a dictionary-driven filtering method to construct a more focused Reddit corpus on dyslexia and AI, filtering out noisy and weakly related posts to improve the relevance of data collected from low-resource forum contexts. Second, it integrates LLM-assisted semantic analysis with KG-based query reasoning to uncover meaningful patterns. Third, it has quantitative evaluation metrics (RAGAS and Query Robustness) to measure LLM-generated response performance. Fourth, it provides structured qualitative validation guidelines for assessing response quality, with a specific focus on hallucination and evidence alignment. We demonstrate the effectiveness of DysLexLens using dyslexia-related Reddit forum data and 30 questions. The results show its potential generalisability to other low-resource forum data contexts. DysLexLens, sample data, questions and evaluation results are available at Github to support reproducibility.

</details>

---

### [[20_Research/Papers/具身智能/SceneBot_Contact-Prompted_General_Humanoid_Whole_Body_Tracking_with_Scene-Interaction|SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction]]

![[assets/2606.27581_figure.png|800]]

- **arXiv**: [2606.27581](https://arxiv.org/abs/2606.27581)
- **PDF**: https://arxiv.org/pdf/2606.27581
- **详细分析**: [[20_Research/Papers/具身智能/SceneBot_Contact-Prompted_General_Humanoid_Whole_Body_Tracking_with_Scene-Interaction|SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction]]
- **作者**: Sirui Chen, Shibo Zhao, Zhen Wu, Jiaman Li, Guanya Shi, C. Karen Liu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current humanoid reinforcement-learning policies excel at free-space motions but struggle with contact-rich tasks, as pure kinematic tracking cannot resolve the physical ambiguities of interacting with objects and uneven terrain. To address this, we introduce SceneBot, a unified motion-tracking framework capable of handling freespace locomotion, terrain traversal, and whole-body manipulation. SceneBot conditions a single policy on both reference motions and per-link contact labels, explicitly defining expected environmental interactions. To overcome the lack of annotated interaction data, we propose a hindsight scene reconstruction approach that infers scene-interaction graphs from retargeted human motion. Trained on 7.5 hours of this reconstructed, contact-rich data, SceneBot successfully generalizes to unseen motions and environments. Our results demonstrate that SceneBot is the first general framework to seamlessly unify free-space and contact-rich behaviors executing complex, long-horizon tasks like carrying a box upstairs and establishing contact conditioning as a powerful interface for humanoid control. All code and data will be open-sourced. More demos and information are available at: https://ericcsr.github.io/scenebot/

</details>

---

### [[20_Research/Papers/强化学习/Retroactive_Advantage_Correction_Closed-Form_V-Trace_Bias_Correction_for_Delay-Aware_RLHF|Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF]]

![[assets/2606.27580_figure.png|800]]

- **arXiv**: [2606.27580](https://arxiv.org/abs/2606.27580)
- **PDF**: https://arxiv.org/pdf/2606.27580
- **详细分析**: [[20_Research/Papers/强化学习/Retroactive_Advantage_Correction_Closed-Form_V-Trace_Bias_Correction_for_Delay-Aware_RLHF|Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF]]
- **作者**: Arnav Raj
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：SORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from human feedback (RLHF) in production does not always have a synchronous reward signal. Code-execution verifiers, slow judge ensembles, and queued human review can return several gradient steps after the rollout that produced them, breaking the synchronous-reward assumption underlying standard PPO. We address this gap with Retroactive Advantage Correction (RAC): each pending slow completion is queued, aged through a non-negative kernel, and reinjected as a clipped residual into the next optimiser step's advantage. We prove that under an unbiased clipped importance ratio, the cumulative RAC correction is exactly unbiased when the effective delay kernel reinjects all of its mass, and carries a bias linear in the unreinjected fraction otherwise; at the no-delay identity kernel it reduces to V-trace. On a tabular Markov decision process (MDP) proof-of-concept, RAC reduces the closed-form policy bias by up to 47.9x at the two-slow-channel configuration, beating wait-for-slow at lower wall-clock cost. RAC integrates with PPO and GRPO through a two-line reward-manager patch.

</details>

---

### [[20_Research/Papers/强化学习/PEBS_Per-rater_Empirical-Bayes_Shrinkage_for_RLHF_Reward-Model_Calibration|PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration]]

![[assets/2606.27578_figure.png|800]]

- **arXiv**: [2606.27578](https://arxiv.org/abs/2606.27578)
- **PDF**: https://arxiv.org/pdf/2606.27578
- **详细分析**: [[20_Research/Papers/强化学习/PEBS_Per-rater_Empirical-Bayes_Shrinkage_for_RLHF_Reward-Model_Calibration|PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration]]
- **作者**: Arnav Raj
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward models for Reinforcement Learning from Human Feedback (RLHF) pool preferences across thousands of annotators and fit one global affine calibrator, collapsing raters with systematically different rating-scale offsets and slopes into a single average-rater fit that does not match any individual annotator. PEBS is a per-rater empirical-Bayes shrinkage estimator: it fits per-rater affine calibrators on a held-out slice of each annotator's ratings and applies Morris-James-Stein empirical-Bayes shrinkage toward the population mean, in closed form and without retraining the reward model. On PRISM, PEBS reduces within-user held-out RMSE by 8.58% over the pooled population-slope baseline. The procedure replicates on PluriHarms harm ratings (Qwen-2.5 base, in-family) with a +9.66% RMSE reduction over the same population-slope baseline. PEBS is a closed-form post-hoc estimator for annotator-specific affine calibration in RLHF reward modeling; it leaves the reward base model unchanged and estimates only the rater-level map used at inference time for new ratings.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_Teaches_Visual_Students_Cross-Modality_Transfer_of_Fine-Grained_Conceptual_Knowledge|Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge]]

![[assets/2606.27527_figure.png|800]]

- **arXiv**: [2606.27527](https://arxiv.org/abs/2606.27527)
- **PDF**: https://arxiv.org/pdf/2606.27527
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_Teaches_Visual_Students_Cross-Modality_Transfer_of_Fine-Grained_Conceptual_Knowledge|Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge]]
- **作者**: Thomas Shih-Chao Liang, Zhuoran Yu, Yong Jae Lee
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Grained Conceptual Knowledge》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) possess broad conceptual knowledge acquired through large-scale text pretraining, yet their potential to supervise models in other modalities remains underexplored. In this work, we propose LaViD--Language-to-Visual Knowledge Distillation--a simple and effective framework for transferring high-level semantic knowledge from a language-only teacher to a vision-only student model. Instead of relying on paired multimodal data, LaViD elicits conceptual signals from an LLM by prompting it to generate multiple-choice questions (MCQs) that probe semantic distinctions between visual classes. Each class is mapped to a soft label distribution over these MCQs, forming a rich conceptual signature that guides the student through an auxiliary distillation loss. Notably, despite using a language-only teacher without access to image data, LaViD consistently outperforms recent methods like MaKD that distill from vision-language models across multiple fine-grained benchmarks. It also achieves competitive or superior performance compared to state-of-the-art visual distillation methods such as DKD and MLKD, with further gains when combined with logit standardization. On the Waterbirds dataset, LaViD substantially improves worst-group accuracy, demonstrating enhanced robustness to spurious correlations with distillation. Code is available at https://github.com/lliangthomas/lavid.

</details>

---

### [[20_Research/Papers/大模型/DMV-Bench_Diagnosing_Long-Horizon_Multimodal_Agents'_Visual_Memory_with_Incidental_Cue_Injection|DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection]]

![[assets/2606.27499_figure.png|800]]

- **arXiv**: [2606.27499](https://arxiv.org/abs/2606.27499)
- **PDF**: https://arxiv.org/pdf/2606.27499
- **详细分析**: [[20_Research/Papers/大模型/DMV-Bench_Diagnosing_Long-Horizon_Multimodal_Agents'_Visual_Memory_with_Incidental_Cue_Injection|DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection]]
- **作者**: Yujin Tang, Chenming Shang, Ruize Xu, Nikhil Singh
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《DMV-Bench: Diagnosing Long-Horizon Multimodal Agents' Visual Memory with Incidental Cue Injection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DMV-Bench, EMemBench, LongMemEval, M3-Bench, MemGUI-Bench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Research on agent memory has matured rapidly, but almost entirely on the text side: few existing benchmarks ask, in an interactive environment, when an agent genuinely needs to remember what it saw rather than what it could write down. We introduce DMV-Bench (Code: https://github.com/yyyujintang/DMV-Bench), the first interactive benchmark for multimodal-agent visual memory. DMV-Bench is built on a controlled home-furnishing e-commerce catalogue of 1,000 product variants in which a text-leakage contract keeps the discriminative signal of each task in the pixels alone. Across a chain of autonomous shopping sessions, every visited product image carries a unique, pre-rendered incidental cue, and the agent is later asked to recall a particular cued product and navigate to its URL. Inspired by dual-coding theory, we propose DualMem, a memory architecture that maintains a visual and a verbal code in parallel. On DMV-Bench, DualMem outperforms a caption baseline and three recent multimodal agent-memory systems at every chain length J in {5, 10, 15, 50} on both Gemini 2.5 Flash and Qwen2.5-VL-7B, with the lead surviving controls for memory-bank size and encoding-position bias, and an asymmetric dual-coding regime in which vision carries the cue end-to-end while the verbal channel plays a smaller query-grounding role.

</details>

---

### [[20_Research/Papers/大模型/Internalizing_the_Future_A_Unified_Agentic_Training_Paradigm_for_World_Model_Planning|Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning]]

![[assets/2606.27483_first_page.png|800]]

- **arXiv**: [2606.27483](https://arxiv.org/abs/2606.27483)
- **PDF**: https://arxiv.org/pdf/2606.27483
- **详细分析**: [[20_Research/Papers/大模型/Internalizing_the_Future_A_Unified_Agentic_Training_Paradigm_for_World_Model_Planning|Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning]]
- **作者**: Xuan Zhang, Zhijian Zhou, Lingfeng Qiao, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 0.2，世界模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FC-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.

</details>

---

### [[20_Research/Papers/大模型/Supersede_Diagnosing_and_Training_the_Memory-Update_Gap_in_LLM_Agents|Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents]]

![[assets/2606.27472_figure.png|800]]

- **arXiv**: [2606.27472](https://arxiv.org/abs/2606.27472)
- **PDF**: https://arxiv.org/pdf/2606.27472
- **详细分析**: [[20_Research/Papers/大模型/Supersede_Diagnosing_and_Training_the_Memory-Update_Gap_in_LLM_Agents|Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents]]
- **作者**: Vedant Patel
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemBench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents operate over long, multi-session interactions in which facts change: a user moves, a price updates, a plan is revised. Acting correctly requires using the current value of a fact and discarding values that have been superseded. We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. On the knowledge-update subset of LongMemEval, replacing an agent's full context with a bounded, self-maintained memory drops accuracy from 92% to 77% even on a frontier model (gpt-5.4), a gap that is statistically significant (paired McNemar p&lt;0.005) and persists across model scale while full-context accuracy saturates near 92%. The bottleneck is therefore memory maintenance, not comprehension, and is not closed by a stronger model. We then ask whether this is merely an undersized memory, and find it is not: as the conversation grows 24x, accuracy falls further (from 68% to 28%), and granting the agent proportionally more memory yields no detectable recovery (28% to 28%, n=25). The failure scales with the length of the conversation, not the compression ratio. We release Supersede, an open reinforcement-learning environment (on the verifiers / prime-rl stack) that turns this measurement into a training signal: agents are rewarded for answering from the current value and penalized for stale ones. Finally, we close the loop and show the gap is trainable: GRPO fine-tuning a small open model (Qwen2.5-3B) on this environment nearly doubles its held-out supersession accuracy on real, unseen conversations (9.0% to 16.7%, a single run), along a monotonic checkpoint curve indicating the learned policy, not the harness, carries the gain. To our knowledge this is the first trainable environment whose reward targets temporal fact-currency, and the first evidence the supersession gap can be trained down, not only measured.

</details>

---

### [[20_Research/Papers/大模型/When_Does_Personality_Composition_Matter_for_Multi-Agent_LLM_Teams|When Does Personality Composition Matter for Multi-Agent LLM Teams?]]

![[assets/2606.27443_figure.png|800]]

- **arXiv**: [2606.27443](https://arxiv.org/abs/2606.27443)
- **PDF**: https://arxiv.org/pdf/2606.27443
- **详细分析**: [[20_Research/Papers/大模型/When_Does_Personality_Composition_Matter_for_Multi-Agent_LLM_Teams|When Does Personality Composition Matter for Multi-Agent LLM Teams?]]
- **作者**: Aryan Keluskar, Amrita Bhattacharjee, Huan Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《When Does Personality Composition Matter for Multi-Agent LLM Teams?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HiddenBench, HumanEval, MultiAgentBench, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personality prompting shapes how large language models communicate, yet whether these behavioral shifts affect objective task outcomes remains under-explored. Prior work shows that agents prompted with low agreeableness produce adversarial language, while those prompted with high agreeableness become cooperative, but the relationship between communication style and task performance has not been systematically examined across multiple domains. In this work, we investigate whether personality composition matters for multi-agent team performance by manipulating personality traits across frontier LLMs on three task domains: structured coding, open-ended research collaboration, and competitive bargaining. We find that personality effects depend critically on task structure. In coding tasks, low agreeableness leads to large communication shifts that have little effect on milestone completion. In open-ended collaboration and bargaining, the same manipulation substantially degrades performance. We discuss implications for multi-agent system design and the limits of personality manipulation.

</details>

---

### [[20_Research/Papers/世界模型/Towards_Evaluation_of_Implicit_Software_World_Models_in_Coding_LLMs|Towards Evaluation of Implicit Software World Models in Coding LLMs]]

![[assets/2606.27406_first_page.png|800]]

- **arXiv**: [2606.27406](https://arxiv.org/abs/2606.27406)
- **PDF**: https://arxiv.org/pdf/2606.27406
- **详细分析**: [[20_Research/Papers/世界模型/Towards_Evaluation_of_Implicit_Software_World_Models_in_Coding_LLMs|Towards Evaluation of Implicit Software World Models in Coding LLMs]]
- **作者**: Egor Bogomolov, Yaroslav Zharov
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Towards Evaluation of Implicit Software World Models in Coding LLMs》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRUXEval, HumanEval, RE2-Bench, REval, SWE-Bench, ThrowBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. We use SWE-bench Verified as the source of data to hold the test close to real-world software engineering tasks. All tested models, frontier ones included, show modest performance and brittle behaviour, suggesting a notable lack of understanding of how software is executed, as opposed to how its source code is written.

</details>

---

### [[20_Research/Papers/大模型/SidConArena_An_Environment_Evaluating_Agents_in_Open-Ended,Positive-Sum_Bargaining_Game|SidConArena: An Environment Evaluating Agents in Open-Ended,Positive-Sum Bargaining Game]]

![[assets/2606.27397_figure.png|800]]

- **arXiv**: [2606.27397](https://arxiv.org/abs/2606.27397)
- **PDF**: https://arxiv.org/pdf/2606.27397
- **详细分析**: [[20_Research/Papers/大模型/SidConArena_An_Environment_Evaluating_Agents_in_Open-Ended,Positive-Sum_Bargaining_Game|SidConArena: An Environment Evaluating Agents in Open-Ended,Positive-Sum Bargaining Game]]
- **作者**: Yeqi Feng, Yuxin Chen, Tianxing He
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SidConArena: An Environment Evaluating Agents in Open-Ended,Positive-Sum Bargaining Game》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AvalonBench, GameBench, MultiAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating LLM agents requires dynamic environments that go beyond static reasoning and zero-sum games. Real-world economic interaction is often open-ended and mixed-motive: agents must negotiate, create positive-sum surplus, compete for scarce assets, and plan under delayed returns. We introduce SidConArena, a new benchmark framework for evaluating LLM agents in open-ended, positive-sum bargaining. SidConArena formalizes a multi-player economy as a finite-horizon partially observable stochastic game with three coupled phases: natural-language negotiation with binding trades, deterministic converter-based production, and sealed-bid auctions for long-term assets. The framework combines structured observations, phase-aware agent dispatching, a neural-symbolic action interface, and asynchronous execution, enabling free-form interaction while preserving rule-grounded evaluation. Across homogeneous and heterogeneous tournaments, stronger frontier models achieve higher economic outcomes, yet agents still misvalue resources, bargain passively, and remain limited in long-horizon investment planning.

</details>

---

### [[20_Research/Papers/强化学习/OverFlowLight_Real-Time_Gridlock_Prevention_and_Traffic_Signal_Optimization_for_Urban_Intersections|OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections]]

![[assets/2606.27381_figure.png|800]]

- **arXiv**: [2606.27381](https://arxiv.org/abs/2606.27381)
- **PDF**: https://arxiv.org/pdf/2606.27381
- **详细分析**: [[20_Research/Papers/强化学习/OverFlowLight_Real-Time_Gridlock_Prevention_and_Traffic_Signal_Optimization_for_Urban_Intersections|OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections]]
- **作者**: Mingyuan Li, Boyang Huang, Tianqi Jiang, Chenpu Li, Chunyu Liu, Yang Li, Ruimin Li, Qiang Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Queue overflow, a severe consequence of urban traffic congestion, occurs when vehicle queues exceed intersection capacity, obstructing upstream traffic and triggering cascading gridlocks. Prevailing traffic signal control (TSC) algorithms, primarily optimized for throughput, often fail to address overflow during peak hours, exacerbating congestion and creating safety hazards. We propose OverFlowLight, a real-time framework designed to preemptively resolve overflow and enhance overall TSC performance. It first introduces a mechanism to accurately detect overflow in real-time by leveraging multi-modal sensing from cameras and radars. Upon detection, it dynamically generates and inserts dedicated overflow phases into the signal cycle to clear the blocking queues. This is orchestrated by a hybrid control design that combines rapid rule-based overflow intervention with controller back ends such as reinforcement learning (RL) for longer-horizon efficiency. We conducted extensive real-world deployments of OverFlowLight across 43 intersections in three major cities. The framework demonstrates seamless integration with existing RL-based TSC agents, highlighting its modularity and practical applicability. Empirical results show that OverFlowLight reduces overflow incidents by 60.4% and increases network throughput by 18.2% compared to deployed baselines. Furthermore, it substantially diminishes the need for manual intervention common with expert-tuned signal plans. This work presents the first practical, scalable, and data-driven framework for actively preventing traffic gridlock, offering a crucial component for building resilient and efficient urban transportation systems. Our demonstration videos, codes and datasets are available at the anonymous URL, https://anonymous.4open.science/r/OverFlowLight-FBF9.

</details>

---
