# cs.CL | Computation and Language | 2026-10-19

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/大模型/Enhancing_RAG-based_Medical_VQA_with_Gated_Multimodal_Representations|Enhancing RAG-based Medical VQA with Gated Multimodal Representations]]

![[assets/2610.23588_figure.png|800]]

- **arXiv**: [2610.23588](https://arxiv.org/abs/2610.23588)
- **PDF**: https://arxiv.org/pdf/2610.23588
- **详细分析**: [[20_Research/Papers/大模型/Enhancing_RAG-based_Medical_VQA_with_Gated_Multimodal_Representations|Enhancing RAG-based Medical VQA with Gated Multimodal Representations]]
- **作者**: Daniela Jimenez-Pano, Hugo Jair Escalante, Delia Irazú Hernández-Farías
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Enhancing RAG-based Medical VQA with Gated Multimodal Representations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MM-RAG-MedVQA, MVQA, PhysioNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical Vision-Language Models (Med-LVLMs) have shown strong performance in Medical Visual Question Answering (MVQA), yet they may still produce factually inconsistent responses. Retrieval-Augmented Generation (RAG) can mitigate this issue by incorporating external clinical evidence; however, retrieval is often guided by a single modality, potentially overlooking the joint semantics of medical images and clinical questions. We introduce a multimodal RAG framework that learns a joint query representation through a Gated Multimodal Unit, enabling evidence retrieval to leverage information from both modalities while keeping the underlying Med-LVLM frozen. We evaluate the proposed approach on benchmark datasets. Results show that the multimodal query representation consistently outperforms a reference Med-LVLM and remains competitive with state-of-the-art methods. Our findings demonstrate the potential of multimodal query representations for more effective evidence retrieval in Medical VQA.

</details>

---

### [[20_Research/Papers/世界模型/Execution_Before_Memory_Diagnosing_Memory_Failures_in_Video_World_Models|Execution Before Memory: Diagnosing Memory Failures in Video World Models]]

![[assets/2610.23542_figure.png|800]]

- **arXiv**: [2610.23542](https://arxiv.org/abs/2610.23542)
- **PDF**: https://arxiv.org/pdf/2610.23542
- **详细分析**: [[20_Research/Papers/世界模型/Execution_Before_Memory_Diagnosing_Memory_Failures_in_Video_World_Models|Execution Before Memory: Diagnosing Memory Failures in Video World Models]]
- **作者**: Weiyang Jin, Jiwen Yu, Sihan Xu, Yuwei Niu, Xihui Liu
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，世界模型 0.8）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Execution Before Memory: Diagnosing Memory Failures in Video World Models》归入 世界模型、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MBench, MemoBench, StEvo-Bench, VQQA, WRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the scene while the change stays hidden, and only later is asked to show it, with leakage before that point kept under control. This separation locates the bottleneck: the model sets the scene but does not carry out the instructed change. The same gap appears in general memory evaluations. On that basis we propose M3-Agent (Make the Missing Move), which recursively revises the details of the input instruction so that the model successfully carries out the requested instruction. Relative to the baseline, it more than triples the MIST reveal score. On the benchmarks, WRBench's score T rises by 26.1% and MBench-T's score U by 52.7%. The method meets the problem from the execution side: it shows what the frozen model can do once the move is stated, and it sets a stricter baseline.

</details>

---

### [[20_Research/Papers/大模型/MultiAgent-OPD_End-to-End_Training_of_Hierarchical_Multi-Agent_Systems_with_On-Policy_Distillation|MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation]]

![[assets/2610.23234_first_page.png|800]]

- **arXiv**: [2610.23234](https://arxiv.org/abs/2610.23234)
- **PDF**: https://arxiv.org/pdf/2610.23234
- **详细分析**: [[20_Research/Papers/大模型/MultiAgent-OPD_End-to-End_Training_of_Hierarchical_Multi-Agent_Systems_with_On-Policy_Distillation|MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation]]
- **作者**: Yuhan Sun, Jiaxin Zhao, Yongdong Luo, Yibo Hu, Meiguang Jin, Junfeng Ma, Weixun Wang, Weihang Pan, Zhongan Bi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MAPoRL, PARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search and summary tokens to provide local process supervision for the Searchers, while the Leader learns from team success and the Answerer from candidate correctness. Across seven datasets, the trained system reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL, the trained cascaded multiagent system, by 2.61 percentage points. The team also solves more questions within four attempts.

</details>

---

### [[20_Research/Papers/大模型/Before_Retrieval_Begins_Safety_and_Tool-Use_Decisions_in_LLM_Agents|Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents]]

![[assets/2610.23071_figure.png|800]]

- **arXiv**: [2610.23071](https://arxiv.org/abs/2610.23071)
- **PDF**: https://arxiv.org/pdf/2610.23071
- **详细分析**: [[20_Research/Papers/大模型/Before_Retrieval_Begins_Safety_and_Tool-Use_Decisions_in_LLM_Agents|Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents]]
- **作者**: Aditya Nawal, Manit Baser, Mohan Gurusamy
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, HarmBench, HarmURLBench, SafeToolBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models increasingly act as agents that call external tools, yet most tool-safety research examines only what follows a tool call. The prior decision of whether to call the tool remains largely unexamined and can influence downstream safety. Across the seven open-weight models, the unweighted model-average harm rate after admitted harmful requests is 74.5%. To identify what governs this decision, we apply a factorial intervention to the input request. Within our generated construction, neutralizing the requested-operation component produces the largest admission contrast (19 pp). A linear direction estimated from this contrast influences held-out admission in four of seven models; effects on operation-neutralized requests in some models show that it is not an operation-specific mechanism. We then test whether written refusal is behaviorally and representationally coupled to the same decision. Written refusal accompanies 33.6% of admitted harmful calls. Plain-text refusal training reduces unsafe admission in models that retain benign tool use, showing that response-level safety training can transfer to the call decision. Together, these results establish a partial, model-dependent relation between written refusal and tool admission. They motivate direct evaluation and supervision of tool admission rather than treating text refusal as its proxy.

</details>

---

### [[20_Research/Papers/大模型/ParetoChat_An_LLM-Based_Interface_for_Interactive_Multi-Objective_Optimization|ParetoChat: An LLM-Based Interface for Interactive Multi-Objective Optimization]]

![[assets/2610.23062_figure.png|800]]

- **arXiv**: [2610.23062](https://arxiv.org/abs/2610.23062)
- **PDF**: https://arxiv.org/pdf/2610.23062
- **详细分析**: [[20_Research/Papers/大模型/ParetoChat_An_LLM-Based_Interface_for_Interactive_Multi-Objective_Optimization|ParetoChat: An LLM-Based Interface for Interactive Multi-Objective Optimization]]
- **作者**: Gokhan Ceyhan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ParetoChat: An LLM-Based Interface for Interactive Multi-Objective Optimization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-objective optimization models are often deployed in settings where decision makers (DMs) must balance some conflicting criteria. In practice, however, stakeholders must translate their qualitative preferences between different criteria into numerical weights, priorities, or reference points required by optimization methods, which can be difficult to specify and interpret. This paper proposes \emph{ParetoChat}, an LLM (large language model)-based expert-agent interface for interactive multi-objective optimization. The agent translates natural-language user input into structured scalarization parameters, invokes an optimization system, presents candidate solutions, and iteratively elicits feedback. We describe a multi-agent architecture that separates input processing, multi-criteria decision-making (MCDM) expertise, solution presentation, and feedback processing. We then present a simulation study using an LLM-based DM agent and benchmark ParetoChat against interactive methods implemented in DESDEO, including reference-point and NIMBUS methods. The computational experiments on multi-objective binary knapsack and set-partitioning instances show that ParetoChat can guide the search efficiently toward solutions that match the DM's preferences. An application to historical courier-order assignment instances illustrates how users can explore objective extremes and intermediate trade-offs through natural-language requests. The results indicate that LLM agents may provide a practical interaction layer between business stakeholders and optimization tools.

</details>

---

### [[20_Research/Papers/大模型/Self-Evolving_Agents_Can_Repair_Failures_but_Struggle_to_Generalize_from_Them|Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them]]

![[assets/2610.22984_first_page.png|800]]

- **arXiv**: [2610.22984](https://arxiv.org/abs/2610.22984)
- **PDF**: https://arxiv.org/pdf/2610.22984
- **详细分析**: [[20_Research/Papers/大模型/Self-Evolving_Agents_Can_Repair_Failures_but_Struggle_to_Generalize_from_Them|Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them]]
- **作者**: Weixiang Zhao, Yichen Zhang, Yanyan Zhao, Jinming Bai, Bin Liang, Ruifeng Xu, Bing Qin, Ting Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experience-driven self-evolution offers a promising path for large language model (LLM) agents to continually improve through interaction. Yet existing approaches often rely on successful trajectories or external evaluation signals, leaving unclear whether agents can evolve when such positive anchors are unavailable. We study this question through Cold-Start Failure-Only Evolution (CFOE), where agents start without accumulated experience and learn only from failed interactions without privileged guidance. Across three self-evolving paradigms, multiple LLM backbones, and four interactive environments, we uncover a consistent repair-generalization gap: failure-derived experience can help repair previously failed tasks, but rarely yields sustained improvements on unseen tasks. Further analysis shows that agents often misinterpret failures, while even verified-correct experience remains difficult to transfer. Relaxing CFOE reveals that verifier feedback and additional interaction provide limited gains, whereas successful trajectories substantially improve transfer. These findings suggest that current self-evolving agents are better at repairing observed failures than building generalizable capabilities from failure.

</details>

---

### [[20_Research/Papers/大模型/KiranaBench_Can_a_Language_Model_Run_a_Neighbourhood_Shop|KiranaBench: Can a Language Model Run a Neighbourhood Shop?]]

![[assets/2610.22980_first_page.png|800]]

- **arXiv**: [2610.22980](https://arxiv.org/abs/2610.22980)
- **PDF**: https://arxiv.org/pdf/2610.22980
- **详细分析**: [[20_Research/Papers/大模型/KiranaBench_Can_a_Language_Model_Run_a_Neighbourhood_Shop|KiranaBench: Can a Language Model Run a Neighbourhood Shop?]]
- **作者**: Bhuvan Arora, Ankita Karmakar, Chaitanya Jain, Dilesh Churiwal, Harshit Jain, Shivansh Manish Dubey, Manish Prasad, Raja Piyush, Kshitij Tayal, Dhruv Kumar, Jagat Sesh Challa, Raunak Manekar...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《KiranaBench: Can a Language Model Run a Neighbourhood Shop?》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BazaarBench, BhashaBench, ERPBench, IndicGenBench, KiranaBench, MerchantBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly evaluated on long-horizon tasks, including autonomously running a business. Existing benchmarks for this setting are almost exclusively English-language, Western in retail context, and single-agent, with the agent observing the business directly. We study how these results transfer to a multi-agent Indic setting. We introduce KiranaBench, a simulated Indian general store in which four roles (manager, cashier, helper, and bookkeeper) are each played by a separate LLM agent. Interactions with customers and suppliers occur in English, Hindi, or Hinglish, and product demand is calibrated to India's national Household Consumption Expenditure Survey. Evaluating four open-weight LLMs, we find that all fall far short of a fixed-rule shopkeeper baseline: the best model earns only one-eighth of the baseline's profit, and two models finish below an unmanaged shop. Performance is also consistently lower for Hindi and Hinglish than for English supplier communication. KiranaBench offers evidence that current LLM agents are not yet reliable for autonomously operating small businesses in India, and provides a testbed for developing agents suited to settings that are long-horizon, collaborative, and multilingual.

</details>

---

### [[20_Research/Papers/具身智能/Multimodal_Filesystem_Memory_For_Long-Horizon_Embodied_Agents|Multimodal Filesystem Memory For Long-Horizon Embodied Agents]]

![[assets/2610.22686_figure.png|800]]

- **arXiv**: [2610.22686](https://arxiv.org/abs/2610.22686)
- **PDF**: https://arxiv.org/pdf/2610.22686
- **详细分析**: [[20_Research/Papers/具身智能/Multimodal_Filesystem_Memory_For_Long-Horizon_Embodied_Agents|Multimodal Filesystem Memory For Long-Horizon Embodied Agents]]
- **作者**: Chloe Su, Jiahan Li, Zhenting Qi, Chaoran Cheng, Haoyu Chen, Sejoon Jun, Weirui Ye, Yilun Du
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.95（加权：具身智能 0.9，大模型 1.05）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Multimodal Filesystem Memory For Long-Horizon Embodied Agents》归入 大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CUABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents operating over long horizons need an effective memory that allows them to reuse their experience throughout long interactions. If the entire history of an interaction is retained, it becomes difficult to find the relevant experience, while compressing it into summaries may result in the loss of visual and spatial details that are required later on. We present \textbf{MFM}, a multimodal filesystem memory architecture that keeps complementary types of agent memory. \textbf{Episodic memory} stores the observations, actions, and outcomes, and \textbf{spatial memory} associates experiences with locations. \textbf{Semantic and procedural memory} build up general knowledge and reusable methods of acting, and \textbf{working memory} holds the current plans. MFM makes use of searchable textual records to connect these different representations to the underlying multimodal episodes. The agents are able to find previous experiences by means of contextual cues and to examine the original observations in order to recover details that are missing from their textual descriptions. Through consolidation, the agents convert experience into higher-level knowledge and procedures while still keeping references to the original episodes. In the case of long-horizon Minecraft and computer-use tasks, MFM leads to improved performance with three base models. With GPT-6-Astra, MFM completes \emph{Mine Diamond from Scratch} and reaches 16 out of 24 milestones on the \emph{Ender Dragon} task, as against 12.7 for the best baseline. On CUABench-KiCad it attains a mean reward of 0.440, as compared to 0.400 for the best baseline and 0.267 in the case of no persistent memory.

</details>

---

### [[20_Research/Papers/大模型/RealCLI_Toward_a_Unified_Evaluation_of_Human-Agent_Collaboration_for_CLI_Agents|RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents]]

![[assets/2610.22507_figure.png|800]]

- **arXiv**: [2610.22507](https://arxiv.org/abs/2610.22507)
- **PDF**: https://arxiv.org/pdf/2610.22507
- **详细分析**: [[20_Research/Papers/大模型/RealCLI_Toward_a_Unified_Evaluation_of_Human-Agent_Collaboration_for_CLI_Agents|RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents]]
- **作者**: Yunqi Liu, Peiyu Wang, Bingli Wang, Leo Luo, Xuanwu Song, Xudong Ma, Hongxin Li, Yaxin Du, Weicheng Gu, Fanglin Xu, Yi Xing, XiangLong Liu...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent

#### 研究背景与动机

《RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ICAE-Bench, Long-Horizon-Terminal-Bench, LongCLI-Bench, SWE-Bench, Terminal-Bench, UnderSpecBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchmark that unifies the evaluation of task execution and human-agent collaboration quality on realistic CLI tasks. To comprehensively measure collaboration, REALCLI builds a five-dimensional framework, operationalized into 22 sub-dimensions and 51 interaction scenario templates. REALCLI provides two modes for paired comparison: REALCLI-EXEC supplies complete specifications upfront, whereas REALCLI-COLLAB introduces a scripted user that delivers progressive information, corrections, constraint revisions, and authorization decisions. Evaluations reveal profound capability gaps in frontier agents: the best configuration attains an average score of only 49.2%, and when evaluated by the joint collaboration score ($J_{\mathrm{collab}}$), the peak performance reaches merely 37.6%. These results show that task effectiveness diverges sharply from collaboration quality, with models consistently struggling in steerability, trust calibration, and safety boundary management. REALCLI provides a rigorous, reproducible foundation for measuring and advancing collaborative CLI agents.

</details>

---
