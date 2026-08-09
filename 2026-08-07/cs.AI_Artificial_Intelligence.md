# cs.AI | Artificial Intelligence | 2026-08-07

#arxiv #ComputerScience

**论文数**: 46

### [[20_Research/Papers/大模型/AV-AIVAT_74x_Cheaper_Agent_Evaluation_with_Certified_Anytime-Valid_Stopping_in_Imperfect-Information_Games|AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games]]

![[assets/2608.06362_figure.png|800]]

- **arXiv**: [2608.06362](https://arxiv.org/abs/2608.06362)
- **PDF**: https://arxiv.org/pdf/2608.06362
- **详细分析**: [[20_Research/Papers/大模型/AV-AIVAT_74x_Cheaper_Agent_Evaluation_with_Certified_Anytime-Valid_Stopping_in_Imperfect-Information_Games|AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games]]
- **作者**: Boning Li, Yu Chen, Longbo Huang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PokerBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact. The Action-Informed Value Assessment Tool (AIVAT) reduces variance in imperfect-information games through conditional mean-zero corrections, by a median $54\times$ across 15 LLM agent configurations spanning 71,439 paired Heads-Up No-Limit Hold'em (HUNL) hands, but does not say when to stop. We combine AIVAT with continuously monitored Confidence Sequences (CSs) into anytime-valid AIVAT (AV-AIVAT), whose online value model learns only from past games so that no game scores its own correction. At the nominal 95\% level and a target precision of $\pm1$ Big Blind, raw outcomes need a median $74\times$ as many hands as AIVAT-corrected outcomes to stop under the Asymptotic CS (AsympCS). Exact finite-sample certification uses the Empirical-Bernstein CS (EB-CS), which needs an independently justified bound on corrected payoffs. We establish such a bound structurally for Leduc hold'em and characterize a width floor set by the CS's bet cap and that bound, which governs how much of a variance gain becomes earlier stopping; the descriptive HUNL EB-CS runs show a median $1.37\times$ stopping-time ratio. AV-AIVAT turns variance reduction into efficient, auditable early stopping while separating asymptotic screening from exact certification, so an evaluation can stop the moment its evidence suffices and hand a third party everything needed to recheck the verdict at that very stopping time.

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_the_Benchmarks_Evaluating_Benchmarks_for_Conversational_Agents|Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents]]

![[assets/2608.06329_first_page.png|800]]

- **arXiv**: [2608.06329](https://arxiv.org/abs/2608.06329)
- **PDF**: https://arxiv.org/pdf/2608.06329
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_the_Benchmarks_Evaluating_Benchmarks_for_Conversational_Agents|Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents]]
- **作者**: Noam Koren, Roy Bar-Haim, Abigail Goldsteen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations. We introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage, while providing actionable diagnostics of weaknesses. We validate the framework by demonstrating agreement with independent human annotations and by evaluating benchmarks generated by LLMs of varying capabilities, as well as benchmarks subjected to controlled quality-degrading perturbations. Across domains and judge models, the proposed metrics consistently distinguish between benchmark quality levels. We further demonstrate the framework's applicability to manually curated benchmarks. Our framework offers a practical approach for evaluating synthetic and manually curated conversational-agent benchmarks.

</details>

---

### [[20_Research/Papers/世界模型/From_Passive_Mirrors_to_Active_Agents_Holonic_Digital_Twins_for_Physical_AI_over_Networks|From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks]]

![[assets/2608.06227_figure.jpg|800]]

- **arXiv**: [2608.06227](https://arxiv.org/abs/2608.06227)
- **PDF**: https://arxiv.org/pdf/2608.06227
- **详细分析**: [[20_Research/Papers/世界模型/From_Passive_Mirrors_to_Active_Agents_Holonic_Digital_Twins_for_Physical_AI_over_Networks|From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks]]
- **作者**: Christo Kurisummoottil Thomas, Omar Hashash, Walid Saad
- **cs 子类**: cs.AI, cs.IT, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 0.7（加权：大模型 0.5，世界模型 0.2）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HDT-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite advances in artificial intelligence (AI) across multiple sectors, today's AI tools, including deep learning and generative AI, still fail when embedded into physical systems, such as robots and vehicles operating under real-world physical laws. This stems from their inability to maintain reliable world models for long-horizon planning under uncertainty and generalize to unseen scenarios. In this context, wireless networks, through pervasive sensing and communication, can orchestrate physical intelligence. However, current architectures optimize throughput, latency, and reliability and cannot support real-time physical AI coordination, requiring agents to maintain shared spatiotemporal context. To address these challenges, a network of holonic digital twins (HDT-Nets) framework is proposed to deliver real-time physical AI inference through holonic agents that actively reason about their environment rather than passively mirror physical assets. Each HDT is realized as a hierarchical structure spanning the physical agent and network edge, reasoning autonomously at the local level while cooperating with neighboring HDTs to form collectively intelligent units. In HDT-Net, causal Markov blankets spanning sensing, communication, and control determine which agents must coordinate and enable counterfactual reasoning over multi-domain interventions. Active inference within these boundaries unifies perception, action, and learning by minimizing expected free energy while deciding which beliefs to transmit based on their cognitive value to the receiver. Category theory ensures that transmitted beliefs preserve semantic structure across heterogeneous agents with incompatible representations. Finally, integrated information theory quantifies when collective intelligence exceeds independent operation and how network intelligence evolves through coordinated learning and information exchange.

</details>

---

### [[20_Research/Papers/大模型/EnvACE_Internalizing_Environment_Dynamics_via_World_Rehearsal_for_Agentic_Reinforcement_Learning|EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning]]

![[assets/2608.06197_figure.png|800]]

- **arXiv**: [2608.06197](https://arxiv.org/abs/2608.06197)
- **PDF**: https://arxiv.org/pdf/2608.06197
- **详细分析**: [[20_Research/Papers/大模型/EnvACE_Internalizing_Environment_Dynamics_via_World_Rehearsal_for_Agentic_Reinforcement_Learning|EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning]]
- **作者**: Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, Jinyang Huang, Yan Xu, Yasheng Wang, Weinan Zhang, Xingshan Zeng, Weiwen Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 0.8，世界模型 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FinMCP-Bench, VitaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that replaces external environment interaction during training with world rehearsal. The policy alternates between acting and rehearsal: it first generates a tool call, then plays the role of the environment to produce the response induced by that action, and conditions subsequent decisions on the rehearsed response. Both roles are jointly optimized end-to-end using task-success rewards. Through world rehearsal, the policy internalizes the relationship between actions and their environment responses in its parameters, yielding an agent world model that directly supports decision making. Across BFCL-v4, tau^2-Bench, VitaBench, and FinMCP-Bench, EnvACE achieves strong and transferable performance, outperforming environment-scaling baselines in the overall evaluation. Controlled studies further show that world rehearsal consistently improves policy learning across model scales. At test time, the internalized world model enables private rehearsal before committed execution, yielding further gains under a moderate rehearsal budget without additional external interaction. Our findings establish world rehearsal as a new path toward scaling LLM agent training beyond the constraints of external environments. Our code is publicly available at https://github.com/Within-yao/EnvACE.

</details>

---

### [[20_Research/Papers/具身智能/iARCS_Iterative_Agentic_RL_for_Controllable_3D_Scene_Generation|iARCS: Iterative Agentic RL for Controllable 3D Scene Generation]]

![[assets/2608.06161_figure.png|800]]

- **arXiv**: [2608.06161](https://arxiv.org/abs/2608.06161)
- **PDF**: https://arxiv.org/pdf/2608.06161
- **详细分析**: [[20_Research/Papers/具身智能/iARCS_Iterative_Agentic_RL_for_Controllable_3D_Scene_Generation|iARCS: Iterative Agentic RL for Controllable 3D Scene Generation]]
- **作者**: Saugat Adhikari, Ashok Prasad Neupane, Pramish Paudel, Ajad Chhatkuli, Danda Pani Paudel
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.1，强化学习 0.2）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《iARCS: Iterative Agentic RL for Controllable 3D Scene Generation》归入 具身智能、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synthetic 3D scene generation is increasingly used as a data source for computer vision and embodied AI, but existing generators often optimize perceptual realism without reliably satisfying task-critical functional constraints. This mismatch limits the usefulness of synthetic data for downstream training, where accessibility, traversability, and spatial rule compliance are often essential. We present iARCS, an iterative agentic reinforcement learning framework that adapts a pretrained scene generator to natural-language task requirements. iARCS uses a two-stage strategy: universal-reward pretraining to improve physical plausibility and layout quality, followed by task-specific fine-tuning with LLM-generated reward programs that are iteratively refined from training feedback. Experiments show improved constraint fidelity on walkability, reachability, and clearance-focused tasks, effective task-specific constraint optimization, and competitive scene diversity. We further show that data generated by iARCS improves a base generator, supporting its value as a practical synthetic data generation tool rather than only a controllable scene editing method.

</details>

---

### [[20_Research/Papers/大模型/Learning_Globally_Reusable_Skills_for_Coding_Agents|Learning Globally Reusable Skills for Coding Agents]]

![[assets/2608.06153_figure.png|800]]

- **arXiv**: [2608.06153](https://arxiv.org/abs/2608.06153)
- **PDF**: https://arxiv.org/pdf/2608.06153
- **详细分析**: [[20_Research/Papers/大模型/Learning_Globally_Reusable_Skills_for_Coding_Agents|Learning Globally Reusable Skills for Coding Agents]]
- **作者**: Chen Yang, Jiashuo Tian, Ziqi Wang, Xinyin Liu, Meiru Ye, Junjie Chen
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Learning Globally Reusable Skills for Coding Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Multi-SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated skill evolution enables Large Language Model (LLM) agents to continuously improve without expensive retraining. However, existing approaches typically treat skill evolution as a sequence of local updates, overlooking relationships among skills and often producing overfitted skill updates that fail to generalize across tasks. We propose GSE, a globalized skill evolution framework that jointly optimizes skill compatibility and skill generalization. To preserve consistency across the skill bank, GSE maintains a Skill Relation Graph (SRG) that explicitly models and co-evolves inter-skill relationships. To improve generalization, GSE performs cluster-based skill consolidation to abstract reusable capabilities from local updates and employs replay-driven verification to prevent overfitting and behavioral regressions. We evaluate GSE on two representative software engineering tasks: bug-revealing test generation and false-positive bug report filtering. Across two state-of-the-art coding agents, OpenHands and mini-SWE-agent, GSE consistently achieves the best precision, recall, and F1-score. Compared with existing evolution techniques, GSE improves precision and recall by 6.1%~34.1% and 31.8%~180.0% for test generation, and by 15.4%~96.4% and 13.1%~19.8% for false-positive filtering. Deployment on an internal industrial agent further yields a 61.4% improvement in F1-score, demonstrating the effectiveness and generalizability of GSE for evolving effective skills.

</details>

---

### [[20_Research/Papers/强化学习/Contextual_Information_Policy_Optimization_for_Search_Agents|Contextual Information Policy Optimization for Search Agents]]

![[assets/2608.06128_figure.png|800]]

- **arXiv**: [2608.06128](https://arxiv.org/abs/2608.06128)
- **PDF**: https://arxiv.org/pdf/2608.06128
- **详细分析**: [[20_Research/Papers/强化学习/Contextual_Information_Policy_Optimization_for_Search_Agents|Contextual Information Policy Optimization for Search Agents]]
- **作者**: Xingyu Guo, Wei Chen, Linlin Yang, Baochang Zhang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.6（加权：大模型 0.4，强化学习 1.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Contextual Information Policy Optimization for Search Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Search agents extend large language models beyond static parametric memory by enabling them to acquire and use ex ternal evidence during multi-step reasoning. For knowledge intensive tasks involving complex or evolving information, their reliability depends not only on retrieving relevant ev idence but also on using it to guide subsequent reasoning. However, existing methods primarily reward final-answer cor rectness or intermediate progress, without directly assessing whether post-retrieval actions are grounded in the retrieved evidence. This misalignment encourages prior-driven reason ing: agents form conclusions based on internal knowledge and use retrieval mainly to confirm them, resulting in confirma tion bias and inefficient evidenceuse.Toaddressthisissue, we propose Contextual Information Policy Optimization (CIPO), an evidence-oriented reinforcement learning framework that explicitly aligns policy optimization with external evidence use. CIPO assigns dense, turn-level credit to reasoning ac tions influenced by retrieved information, while combining this evidence-use signal with a global outcome reward to pre serveanswercorrectness.Withthismanner,CIPOdiscourages evidence-detached guesses and promotes reasoning trajecto ries in which retrieved facts can guide or revise subsequent reasoning. Importantly, CIPO requires neither human process annotations nor an additional reward model. Extensive exper iments on seven in-domain and out-of-domain benchmarks show that CIPO reduces the prevalence of prior-driven rea soning and achieves excellent performance on most tasks.

</details>

---

### [[20_Research/Papers/大模型/Poli-Bias_Understanding_and_Measuring_Large_Language_Model_Biases_in_International_Political_Conflicts|Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts]]

![[assets/2608.06123_figure.png|800]]

- **arXiv**: [2608.06123](https://arxiv.org/abs/2608.06123)
- **PDF**: https://arxiv.org/pdf/2608.06123
- **详细分析**: [[20_Research/Papers/大模型/Poli-Bias_Understanding_and_Measuring_Large_Language_Model_Biases_in_International_Political_Conflicts|Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts]]
- **作者**: Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio, Holger Boche
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GermanPartiesQA, OpinionQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically swapped across diverse geopolitical relationships, legal violations, and reasoning tasks. Rather than reducing bias to a single judgment, our framework decomposes response disparities into five interpretable dimensions, revealing how and where unequal treatment manifests. Across 13 contemporary LLMs spanning diverse model families and sizes, we find that country identities and user affiliations can systematically affect how equivalent actions are described, evaluated, and defended under international law. Our results thus establish Poli-Bias as a fine-grained framework for auditing political even-handedness and sycophancy in LLMs.

</details>

---

### [[20_Research/Papers/具身智能/Does_Latent_Context_Help_A_Controlled_Evaluation_of_Inverse_Reinforcement_Learning_in_Arctic_Shipping|Does Latent Context Help? A Controlled Evaluation of Inverse Reinforcement Learning in Arctic Shipping]]

![[assets/2608.06105_figure.png|800]]

- **arXiv**: [2608.06105](https://arxiv.org/abs/2608.06105)
- **PDF**: https://arxiv.org/pdf/2608.06105
- **详细分析**: [[20_Research/Papers/具身智能/Does_Latent_Context_Help_A_Controlled_Evaluation_of_Inverse_Reinforcement_Learning_in_Arctic_Shipping|Does Latent Context Help? A Controlled Evaluation of Inverse Reinforcement Learning in Arctic Shipping]]
- **作者**: Vaishnav Vaidheeswaran, Dilith Jayakody, Biruk Ambaw, Jaswanth Kumar, Md Mahbub Alam, Gabriel Spadon
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Does Latent Context Help? A Controlled Evaluation of Inverse Reinforcement Learning in Arctic Shipping》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AIRL, IRL, MCE-IRL, Meta-IRL, PEMIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial Intelligence (AI)-assisted navigation can help Arctic shipping adapt to rapidly changing sea-ice conditions, but reliable deployment requires reward models that are interpretable and robust to changing environments. Inverse reinforcement learning (IRL) provides a framework for recovering such rewards from vessel trajectories, while recent meta-IRL methods introduce latent context variables to capture behavioral heterogeneity. However, it remains unclear whether these latent representations recover genuinely hidden preferences or simply re-encode information already available in the observed state. We conduct a controlled evaluation on 3,186 AIS-derived voyages from 202 vessels across nine Arctic shipping seasons, comparing a linear shared reward, a nonlinear shared reward, and a latent-context model built on the same nonlinear architecture. The nonlinear reward improves held-out likelihood by 50.9% over the linear baseline, whereas adding vessel-specific latent context reduces performance by 16.5%. Behavioral analysis, context probes, and a pre-registered feature-hiding ablation show that apparent vessel-level variation is largely explained by observable route and environmental conditions rather than hidden vessel-specific factors. Moreover, predictive accuracy, route fidelity, and reward transfer yield different model rankings, demonstrating that no single metric is sufficient to evaluate learned rewards. These findings motivate testing whether the observed route, environmental, and vessel features already explain behavioral variation before adding per-vessel latent context. This supports more trustworthy AI deployment in safety-critical domains.

</details>

---

### [[20_Research/Papers/大模型/From_Economic_Agents_to_Agentic_Economies_A_Systems_Blueprint_for_Economic_World_Models|From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models]]

![[assets/2608.06020_figure.png|800]]

- **arXiv**: [2608.06020](https://arxiv.org/abs/2608.06020)
- **PDF**: https://arxiv.org/pdf/2608.06020
- **详细分析**: [[20_Research/Papers/大模型/From_Economic_Agents_to_Agentic_Economies_A_Systems_Blueprint_for_Economic_World_Models|From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models]]
- **作者**: Jiale Han, Xiang Li, Jing Qian, Wenyuan Gu, Pin Gao, Ye Luo, Hongyuan Zha, Dacheng Tao, Benyou Wang, Lin William Cong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 具身智能, 强化学习
- **相关性评分**: 2.02（加权：具身智能 0.3，大模型 0.6，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models》归入 世界模型、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Awesome-Economic-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic dynamics from the inside. We organize EWM systems into a six-level capability ladder, from fixed rule-based agent worlds to adaptive and LLM-based agent worlds, self-evolving agents, evolving institutional worlds, and sim-to-real economic twins aligned with real observations. A systematic literature survey across these levels reveals that existing work remains concentrated in lower-level agent and simulation environments, while systems with self-evolving agents, endogenous institutions, persistent empirical alignment, and validated economic mechanisms remain rare. By translating the EWM agenda into an implementation blueprint, this paper aims to accelerate the development of the next generation of economic simulation environments that can serve as high-fidelity sandboxes for human decision-makers and as training, planning, evaluation, and safety substrates for AI agents. We release a curated paper list and related resources to support future research.

</details>

---

### [[20_Research/Papers/大模型/ProDVI_Programmatic_Dynamics_Priors_for_Value_Network_Initialization|ProDVI: Programmatic Dynamics Priors for Value Network Initialization]]

![[assets/2608.06015_figure.png|800]]

- **arXiv**: [2608.06015](https://arxiv.org/abs/2608.06015)
- **PDF**: https://arxiv.org/pdf/2608.06015
- **详细分析**: [[20_Research/Papers/大模型/ProDVI_Programmatic_Dynamics_Priors_for_Value_Network_Initialization|ProDVI: Programmatic Dynamics Priors for Value Network Initialization]]
- **作者**: Xinwei Liu, Junyuan Liang, Jianting Zhang, Wuhui Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ProDVI: Programmatic Dynamics Priors for Value Network Initialization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Gen2Sim, GenSim, Meta-RL, OFENet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Reinforcement Learning (RL) is notoriously sample inefficient. One contributing factor is that RL agents are typically initialized from scratch, forcing them to acquire task-relevant knowledge through online interaction. Existing approaches obtain informative initializations through pre-collected datasets, high-fidelity simulators, or meta-learning over related tasks, but these prerequisites may be difficult to access or even unavailable. In this paper, we propose Programmatic Dynamics Priors for Value Network Initialization (ProDVI), a framework that leverages the commonsense and domain knowledge encoded in large language models to initialize RL agents without relying on these resources. Specifically, ProDVI prompts a code-generating language model to produce executable Python functions that encode coarse hypotheses about environment dynamics. These functions are then used to generate synthetic transitions. Based on these transitions, we construct an auxiliary dynamics prediction objective to pretrain the state-action encoder of the value network in an actor-critic framework. The learned representation provides dynamics-aware inductive biases before online RL begins. Importantly, the generated programs are used only for representation pretraining and are not required to faithfully simulate the target environment. While the generated programs may be inaccurate, their induced initialization can be corrected through online learning from real transitions and rewards. Experiments on OpenAI Gym and DeepMind Control Suite tasks show that ProDVI can effectively improve the sample efficiency of model-free RL algorithms.

</details>

---

### [[20_Research/Papers/强化学习/AgentOPSD_Recursive_Self-Distillation_for_Agentic_Reinforcement_Learning|AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning]]

![[assets/2608.05987_figure.png|800]]

- **arXiv**: [2608.05987](https://arxiv.org/abs/2608.05987)
- **PDF**: https://arxiv.org/pdf/2608.05987
- **详细分析**: [[20_Research/Papers/强化学习/AgentOPSD_Recursive_Self-Distillation_for_Agentic_Reinforcement_Learning|AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning]]
- **作者**: Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Search-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. We propose AgentOPSD, a critic-free, recursive method for turn-level credit assignment in agentic reinforcement learning. AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space. This yields a principled reweighting scheme that converts sparse outcome supervision into turn-level credit signals and identifies pivotal turns through the marginal belief revision between consecutive states. The method is fully compatible with standard policy optimization and requires neither an additional critic nor extra rollouts. We evaluate AgentOPSD on ALFWorld, WebShop, and Search-QA using Qwen2.5 models at two scales (3B and 7B). AgentOPSD outperforms GRPO and strong self-distillation baselines, achieving 89.1% success on ALFWorld with Qwen2.5-7B. Ablation studies attribute the gains to turn-level aggregation and history-dependent recursive belief updates.

</details>

---

### [[20_Research/Papers/强化学习/TRACE_Learned_Proprioceptive_Odometry_for_Legged_Robots_under_Unreliable_Contact_Conditions|TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions]]

![[assets/2608.05975_figure.png|800]]

- **arXiv**: [2608.05975](https://arxiv.org/abs/2608.05975)
- **PDF**: https://arxiv.org/pdf/2608.05975
- **详细分析**: [[20_Research/Papers/强化学习/TRACE_Learned_Proprioceptive_Odometry_for_Legged_Robots_under_Unreliable_Contact_Conditions|TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions]]
- **作者**: Taehyeon Kong, Woojin Kim, Jemin Hwangbo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: RL

#### 研究背景与动机

《TRACE: Learned Proprioceptive Odometry for Legged Robots under Unreliable Contact Conditions》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we present TRACE (Tokenized Robust Attention for Contact-Aware Estimation), an end-to-end learned proprioceptive odometry estimator for legged robots under unreliable contact conditions. The proposed estimator directly predicts relative displacement, relative rotation, and body-frame velocity from a recent history of onboard inertial and joint measurements. To improve robustness under unreliable contact conditions, we introduce a foot-aware cross-attention module that adaptively weights IMU and leg-wise kinematic tokens without relying on manually defined contact or slip thresholds. The estimator is trained with direct supervision and two physics-inspired auxiliary losses that promote kinematic consistency and reliable use of leg information. To reduce policy-specific overfitting and consequently improve sim-to-real transfer, simulation training incorporates policy randomization, followed by partial real-world fine-tuning of the temporal encoder and prediction head. Experiments across diverse indoor and outdoor terrains demonstrate consistent reductions in position drift compared with classical filtering-based, hybrid, and purely learning-based baselines. Ablation studies further validate the contributions of the proposed training objectives, policy randomization, and real-world fine-tuning, particularly under unreliable contacts and sim-to-real mismatch.

</details>

---

### [[20_Research/Papers/具身智能/SkillMemo_Expert-guided_Skill_Memory_Framework_for_Compositional_Embodied_Manipulation|SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation]]

![[assets/2608.05970_figure.png|800]]

- **arXiv**: [2608.05970](https://arxiv.org/abs/2608.05970)
- **PDF**: https://arxiv.org/pdf/2608.05970
- **详细分析**: [[20_Research/Papers/具身智能/SkillMemo_Expert-guided_Skill_Memory_Framework_for_Compositional_Embodied_Manipulation|SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation]]
- **作者**: Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 2.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MemoryVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with limited capability to capture reusable skill structures. To address this limitation, we propose Skill-Based Memory (SkillMemo) framework that implicitly decomposes long-horizon demonstrations into latent atomic skills and integrates skill-level features into a dynamic episodic memory bank for solving compositional tasks. Specifically, we first introduce an expert-guided trajectory segmentation module built upon a Mixture-of-Experts (MoE) architecture, which implicitly partitions trajectories into distinct skill primitives represented by learned gating coefficients. We further design a skill-level episodic memory architecture that stores compact skill representations as retrievable key-value pairs. During inference, the memory bank retrieves the most relevant skill primitives which are subsequently fused with the model's current gating distribution, providing a robust contextual prior to refine action predictions. Extensive experiments on the simulation benchmark and real-world manipulation tasks demonstrate that SkillMemo consistently enhances both DP and VLA backbones, achieving state-of-the-art performance and outperforming $π_{0.5}$, while exhibiting strong compositional generalization to unseen task configurations.

</details>

---

### [[20_Research/Papers/强化学习/Training_a_Conditioned_Video_Game_Agent_on_a_VLM_Annotated_Dataset|Training a Conditioned Video Game Agent on a VLM Annotated Dataset]]

![[assets/2608.05954_figure.png|800]]

- **arXiv**: [2608.05954](https://arxiv.org/abs/2608.05954)
- **PDF**: https://arxiv.org/pdf/2608.05954
- **详细分析**: [[20_Research/Papers/强化学习/Training_a_Conditioned_Video_Game_Agent_on_a_VLM_Annotated_Dataset|Training a Conditioned Video Game Agent on a VLM Annotated Dataset]]
- **作者**: Katrin Schmid, Iuri Frosio
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.7，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Training a Conditioned Video Game Agent on a VLM Annotated Dataset》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) is a powerful but far from easy-to-use technique for policy learning. In the specific case of video games, access to the game engine is required to get rewards for training (e.g. to collect rewards from the environment). Furthermore, the proper identification and weighting of the rewards generally requires a difficult trial-and-error approach. Lastly, rewards are often sparse and understanding how they eventually affect the learned policy is a non-trivial exercise. To ease these issues we propose annotating a video game dataset with Vision Language Models (VLMs) instructed to extract human defined rewards. We show that offline RL can then be used to train a conditioned agent that responds accordingly to the desired returns and we discuss the difficulties and limitations that emerged in our early experiments.

</details>

---

### [[20_Research/Papers/强化学习/VLMs_for_Videogame_Data_Annotation|VLMs for Videogame Data Annotation]]

![[assets/2608.05949_figure.jpg|800]]

- **arXiv**: [2608.05949](https://arxiv.org/abs/2608.05949)
- **PDF**: https://arxiv.org/pdf/2608.05949
- **详细分析**: [[20_Research/Papers/强化学习/VLMs_for_Videogame_Data_Annotation|VLMs for Videogame Data Annotation]]
- **作者**: Katrin Schmid, Iuri Frosio
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《VLMs for Videogame Data Annotation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Language Models (VLMs) and Artificial Intelligence (AI) agents have revolutionized how engineers approach complex problems in real-world applications. Their adoption in video games is on the other hand limited by the extreme variability of the synthetic scenarios and their poor compliance with real-world physics. Here we investigate the use of VLMs for annotating video game frame sequences with reward signals, a task with several potential applications including, among others, conditioned training and offline reinforcement learning. We show that VLMs often struggle to answer basic questions on racing video games (although we observed a similar behavior on other game genres) and discuss countermeasures such as VLM output mixing and prompt optimization. We also show how input sequence length, resolution, and question batching affect the annotation quality and its token consumption.

</details>

---

### [[20_Research/Papers/具身智能/GAUGE_A_Measurement-Grounded_Benchmark_for_Physical_Fidelity_in_Simulation_Engines_and_Video_World_Models|GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models]]

![[assets/2608.05948_figure.png|800]]

- **arXiv**: [2608.05948](https://arxiv.org/abs/2608.05948)
- **PDF**: https://arxiv.org/pdf/2608.05948
- **详细分析**: [[20_Research/Papers/具身智能/GAUGE_A_Measurement-Grounded_Benchmark_for_Physical_Fidelity_in_Simulation_Engines_and_Video_World_Models|GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models]]
- **作者**: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.6，世界模型 0.8，机器人 0.3）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FysicsEval, IsaacSim, PhyGenBench, PhyWorldBench, RGBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physics engines facilitate large-scale training and evaluation for embodied intelligence, while generative video world models are emerging as implicit simulators of future states and interactions. However, existing evaluations of physical fidelity are often conducted in isolation and rely heavily on perceptual similarity or human judgments, providing limited insight into which physical principles or parameters are violated. We introduce GAUGE, a real-world-grounded diagnostic benchmark for jointly evaluating how numerical simulators and generative video world models reproduce or deviate from real-world physics. It comprises 22 controlled task families covering rigid bodies, flexible cables, textiles, and volumetric deformable objects. Grounded in real-world trajectories and paired with calibrated physical metadata, uncertainty annotations, and task-specific observables, these tasks cover fundamental physical processes including collision, friction, momentum transfer, oscillation, self-contact, and deformation across diverse materials and conditions. We benchmark Isaac Sim, Genesis, and Newton on 14 task families using generalized trajectory errors, and evaluate 6 image-to-video models on 5 rigid-body tasks by testing physical-law consistency and the temporal stability of inferred parameters. Our results reveal no uniformly faithful physics engine, with the largest discrepancies arising in impulsive contact, rapid textile motion, and volumetric deformation. We further find that video world models can produce trajectories with the expected equation form while recovering incorrect accelerations, momentum transfer, and oscillation timing. GAUGE lays the groundwork for developing more physically faithful simulators and world models for embodied intelligence.

</details>

---

### [[20_Research/Papers/大模型/BALANCE_Hybrid_Autoregressive-Speculative_LLM_Inference_in_Wireless_Edge_Networks|BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks]]

![[assets/2608.05926_figure.png|800]]

- **arXiv**: [2608.05926](https://arxiv.org/abs/2608.05926)
- **PDF**: https://arxiv.org/pdf/2608.05926
- **详细分析**: [[20_Research/Papers/大模型/BALANCE_Hybrid_Autoregressive-Speculative_LLM_Inference_in_Wireless_Edge_Networks|BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks]]
- **作者**: Guanqiao Qu, Shuo Chen, Qian Chen, Kin K. Leung, Xianhao Chen
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《BALANCE: Hybrid Autoregressive-Speculative LLM Inference in Wireless Edge Networks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Edge inference is a promising paradigm to provide large language model (LLM) inference services in next-generation mobile networks. LLM inference mainly relies on two approaches: Autoregressive decoding (AD) generates output tokens sequentially, resulting in long latency; Speculative decoding (SD) accelerates inference by using a small language model (SLM) to generate multiple draft tokens for LLM verification, but incurs extra memory costs. Due to this latency-memory tradeoff, neither approach alone can efficiently serve users with heterogeneous demands under limited edge computing resources. To address this challenge, we propose a hybrid autoregressive-speculative inference (BALANCE) framework for edge LLM inference. In BALANCE, an edge server hosts both an SLM and an LLM, assigns each user to AD or SD, and performs the two modes simultaneously. To maximize the number of served users, we formulate a task throughput maximization problem to jointly determine user scheduling and computing resource allocation between AD and SD under user latency requirements and server memory constraints. Since the problem is NP-hard, we develop a polynomial-time algorithm that transforms the original problem into two sub-problems and obtains a sub-optimal solution with a constant approximation guarantee. Experiments demonstrate that BALANCE consistently outperforms conventional AD and SD and significantly improves task throughput.

</details>

---

### [[20_Research/Papers/强化学习/AppDeltaWorld_Transition-Grounded_Delta_Code_World_Model_for_Mobile_GUI_Agents|AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents]]

![[assets/2608.05891_figure.png|800]]

- **arXiv**: [2608.05891](https://arxiv.org/abs/2608.05891)
- **PDF**: https://arxiv.org/pdf/2608.05891
- **详细分析**: [[20_Research/Papers/强化学习/AppDeltaWorld_Transition-Grounded_Delta_Code_World_Model_for_Mobile_GUI_Agents|AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents]]
- **作者**: Weikai Xu, Yunren Feng, Haoxiang Lei, Kun Huang, Yuxuan Liu, Kang Zhao, Xiaolin Hu, Shuo Shang, Bo An
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.75（加权：大模型 0.55，强化学习 0.2，世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppDeltaWorld, CMGUIBench, Code2World, MobileGym, MobileWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile GUI agents can operate apps through pixel perception and touch actions, making them a promising interface for collecting and improving long-horizon mobile interaction policies. However, real trajectories are difficult to obtain for sensitive apps and privacy-critical operations. At the same time, existing simulated environments are costly to scale up, and GUI world models still suffer from unstable generation, limited modality coverage, and inconsistent action-transition logic. To address these limitations, we propose AppDeltaWorld, a transition-grounded delta code world model that predicts the next GUI as a reachable code update rather than as an unconstrained image or text description. AppDeltaWorld retrieves app-specific Level-1 HTML references under an action-transition constraint, generates Level-2 executable HTML conditioned on the current screen, action, predicted next-screen text, and retrieved structure, and inserts generated visual assets into image slots before browser rendering. As a world model, AppDeltaWorld achieves the highest fidelity on CMGUIBench-500 under Code2World evaluation, with clear gains in structural layout and UI element reconstruction over image-only and code-only baselines. As a training environment, AppDeltaWorld supports filtered closed-loop SFT data construction that, when combined with public supervision, enables AppDeltaAgent to achieve state-of-the-art performance on AndroidLens and consistent gains on MobileGym and MobileWorld. Moreover, world-model-based test-time reinforcement learning enables policy adaptation and shows further improvements without additional interaction with real apps.

</details>

---

### [[20_Research/Papers/大模型/CodeGrep_An_RL-Trained_Retrieval_Agent_for_LLM_Coding_Agents|CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents]]

![[assets/2608.05886_figure.png|800]]

- **arXiv**: [2608.05886](https://arxiv.org/abs/2608.05886)
- **PDF**: https://arxiv.org/pdf/2608.05886
- **详细分析**: [[20_Research/Papers/大模型/CodeGrep_An_RL-Trained_Retrieval_Agent_for_LLM_Coding_Agents|CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents]]
- **作者**: Wuya Chen, Yihao yang, Yang Cao, Yue Lin
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWE-Bench, ToRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern LLM coding agents such as Claude Code and OpenHands share a common inefficiency: they spend much of their token budget finding the file to patch, rather than patching it. On SWE-Bench Verified, a 30B OpenHands agent averages 23 rounds and 631K tokens per resolved issue, with many calls spent on grep, glob, and view_file during repository exploration. We introduce CodeGrep, a 14B retrieval agent trained end-to-end with GRPO to issue multi-turn parallel grep, glob, and read tool calls and return candidate files to a frozen downstream coding agent. On all 500 SWE-Bench Verified instances, CodeGrep preserves resolve rate while substantially improving efficiency: 27.0% versus 25.8% for the no-retrieval baseline, with 15% fewer rounds and 19% fewer tokens on resolved instances. Across retrievers, downstream utility follows a precision threshold: BM25 with precision 0.375 degrades the agent, Jina with precision 0.445 is neutral, and CodeGrep with precision 0.677 crosses the threshold at which retrieval begins to reduce rollout cost. To enable this study, we mine supervision from 67K open-source agent trajectories using CATM and build a Git-worktree environment for multi-turn agent RL. In our setting, applying the efficiency signal at the advantage layer rather than the reward layer reduces KL drift and translates cleanly into downstream efficiency. We will release the model, training pipeline, RL environment, and evaluation harnesses.

</details>

---

### [[20_Research/Papers/大模型/ViSR-KGC_Visual_Subgraph_Reasoning_with_Vision-Language_Models_for_Multimodal_Knowledge_Graph_Completion|ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion]]

![[assets/2608.05833_figure.png|800]]

- **arXiv**: [2608.05833](https://arxiv.org/abs/2608.05833)
- **PDF**: https://arxiv.org/pdf/2608.05833
- **详细分析**: [[20_Research/Papers/大模型/ViSR-KGC_Visual_Subgraph_Reasoning_with_Vision-Language_Models_for_Multimodal_Knowledge_Graph_Completion|ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion]]
- **作者**: Jiafan Li, Mengxue Yang, Jiaqi Zhu, Liang Chang, Ying Li, Hongan Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《ViSR-KGC: Visual Subgraph Reasoning with Vision-Language Models for Multimodal Knowledge Graph Completion》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge graph completion (KGC) aims to infer missing entities or relations from incomplete graph structures, and has evolved into multimodal knowledge graph completion (MMKGC), where entities are associated with multiple modalities such as text and images. Traditional representation learning approaches follow the embedding-based paradigm and may struggle when relation-specific evidence is limited. Meanwhile, LLM-based reasoning methods typically linearize graph structures into textual prompts, which obscures structural topology and neglects vital visual information. While vision-language models (VLMs) excel at multimodal reasoning, they cannot natively interpret structured graph topology, particularly when it comes to knowledge graphs where nodes and edges carry complex semantics. To bridge this gap, we propose ViSR-KGC, a visual subgraph reasoning approach for KGC. It integrates three complementary capabilities to capture semantic correlations: identifying global topology dependencies via representation learning, analyzing local multimodal evidence using VLMs, and providing necessary commonsense knowledge inherent in pre-trained models. Based on learned multimodal embeddings, our framework first extracts a compact and query-aware subgraph from the MMKG. Then, this subgraph is transformed into a visually interpretable image using a layout strategy selected through empirical comparison.Finally, the visualized subgraph, entity images, textual descriptions, and candidate answers are combined into a unified prompt, enabling the VLM to infer the missing entity.

</details>

---

### [[20_Research/Papers/大模型/When_Self-Evolution_Backfires_Pre-Commit_Gating_against_Skill_Contamination_in_LLM_Agents|When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents]]

![[assets/2608.05810_figure.png|800]]

- **arXiv**: [2608.05810](https://arxiv.org/abs/2608.05810)
- **PDF**: https://arxiv.org/pdf/2608.05810
- **详细分析**: [[20_Research/Papers/大模型/When_Self-Evolution_Backfires_Pre-Commit_Gating_against_Skill_Contamination_in_LLM_Agents|When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents]]
- **作者**: Linfang Shang, Ming Xu, Yiding Sun, Tianle Xia, Lingxiang Hu, Lan Xu, Ning Zheng
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We further show the contamination is structurally irreversible: removing a source skill after the fact cannot erase the flawed reasoning its descendants have already inherited, so post-hoc rollback recovers only a small fraction of the lost performance. This makes skill admission a pre-commit necessity rather than a post-hoc fix, and motivates Verifier-as-Gatekeeper (VaG): a progressive trust hierarchy whose three heterogeneous critics - structural validity, behavioral harmlessness, and semantic consistency - filter each skill individually, coupled with a marginal-gain subset selection that removes combinatorial contamination at the top tier before skills reach the runtime context. On Terminal-Bench 2, unconditional accumulation rises to a peak and then degrades, giving back most of its gains as the pool keeps growing, and post-hoc removal of the culprit skills recovers only a small part of the drop - the empirical signature of irreversibility. In contrast, VaG improves every round, reaching 72% pass@1 with a pool roughly 5x smaller, and its frozen skill pool transfers positively to four other backbones and a second benchmark without re-evolution. Ablations confirm the three critics are complementary and mutually non-substitutable, each intercepting a largely disjoint class of harmful skills.

</details>

---

### [[20_Research/Papers/大模型/When_Agentic_AI_Meets_Integrated_Sensing_and_Communication|When Agentic AI Meets Integrated Sensing and Communication]]

![[assets/2608.05792_figure.png|800]]

- **arXiv**: [2608.05792](https://arxiv.org/abs/2608.05792)
- **PDF**: https://arxiv.org/pdf/2608.05792
- **详细分析**: [[20_Research/Papers/大模型/When_Agentic_AI_Meets_Integrated_Sensing_and_Communication|When Agentic AI Meets Integrated Sensing and Communication]]
- **作者**: Kai Li, Conggai Li, Sarah Ali Siddiqui, Syed Sohail Ahmed, Xin Yuan, Shenghong Li, Wei Ni
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型, 机器人
- **相关性评分**: 0.8（加权：大模型 0.2，强化学习 0.2，世界模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《When Agentic AI Meets Integrated Sensing and Communication》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent surfaces (RIS), edge intelligence, multi-agent coordination, and resilient networking has developed largely in isolation. This survey unifies the literature within a six-stage closed-loop framework comprising observation, contextualization, reasoning and prediction, planning and orchestration, execution and collaboration, and feedback and resilience. It also introduces five levels of agentic maturity, ranging from physical-layer primitives to fully closed-loop agentic ISAC. We use this framework to review advances in multimodal intelligence, large language models, reinforcement learning, federated learning, RIS-assisted control, Unmanned Aerial Vehicle (UAV) and vehicular networks, and AI-native network management, and analyze privacy, security, resilience, and sustainability as cross-cutting requirements of the full perception-reasoning-action loop. An audit of representative studies against nine agentic-specific evaluation criteria shows that no system reports more than one or two of them, exposing a gap between claimed and demonstrated agentic maturity. We identify open challenges in physical-to-semantic grounding, predictive world models, real-time agent-PHY interaction, safe tool use, heterogeneous multi-agent collaboration, benchmarking, and resource-efficient autonomy.

</details>

---

### [[20_Research/Papers/大模型/A_Two-Tier_Perspective_on_Inference-Time_Parallelism_in_Multi-Agent_LLM_Systems|A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems]]

![[assets/2608.05791_figure.png|800]]

- **arXiv**: [2608.05791](https://arxiv.org/abs/2608.05791)
- **PDF**: https://arxiv.org/pdf/2608.05791
- **详细分析**: [[20_Research/Papers/大模型/A_Two-Tier_Perspective_on_Inference-Time_Parallelism_in_Multi-Agent_LLM_Systems|A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems]]
- **作者**: Zihan Xu, Haolin Tian, Hai Jiang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-driven multi-agent systems typically require multiple model invocations and complex coordination during inference, and their execution strategies directly affect system accuracy, latency, and computational cost. Parallel execution provides a means to improve inference-time efficiency. From the perspective of inference-time execution, this paper models parallelism in multi-agent systems as two distinct levels of decision processes: Replica Parallelism, which explores multiple complete solution paths at the task level, and Structural Parallelism, which enables concurrent execution within a single solution path through task decomposition. However, the roles of different forms of parallelism and their interrelationships still lack systematic study in terms of unified organization and coordination. We therefore propose TIPEX, a controllable execution framework that unifies these two levels of parallelism and coordinates their roles within the inference process under a unified execution semantics while supporting systematic combinations and analyses of different parallel strategies and parameter configurations. Systematic experiments on the GAIA benchmark demonstrate that inference-time parallelism can significantly improve accuracy and reduce end-to-end latency at the cost of increased token consumption. Further analysis shows that Replica and Structural Parallelism exhibit complementary effects across task complexities, with tasks of intermediate difficulty benefiting most from their coordination, while overly aggressive parallel strategies do not necessarily yield better performance.

</details>

---

### [[20_Research/Papers/大模型/ChainClaw_A_Layered_Agent_Framework_for_Reliable_On-Chain_Execution|ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution]]

![[assets/2608.05790_figure.png|800]]

- **arXiv**: [2608.05790](https://arxiv.org/abs/2608.05790)
- **PDF**: https://arxiv.org/pdf/2608.05790
- **详细分析**: [[20_Research/Papers/大模型/ChainClaw_A_Layered_Agent_Framework_for_Reliable_On-Chain_Execution|ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution]]
- **作者**: Jiacheng Wei, Zhaoxin Fan, Xin Wen, Yuqin Lan, Dongrun Li, Wenjun Wu, Faguo Wu, Xiao Zhang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose large language model agents have achieved strong performance on tool-augmented tasks, yet they rely on assumptions break down in blockchain environments. On-chain execution is stateful, adversarial, and economically irreversible, exposing three fundamental gaps: Reactivity, Irreversibility, and Observability. We propose ChainClaw, a blockchain-native agent framework built on OpenClaw, that addresses all three gaps through a layered architecture comprising an event-driven orchestration layer, a simulation-based safety intelligence layer, and an on-chain monitoring runtime layer, unified by a cross-layer memory subsystem. ChainClaw closes the Reactivity gap via event ingestion and simulation feedback, the Irreversibility gap via a pre-execution safety pipeline with transaction simulation and action guard, and the Observability gap via an on-chain read adapter and transaction monitor. We evaluate ChainClaw on a purpose-built benchmark covering seven tasks across four categories and five dimensions. ChainClaw consistently outperforms representative baselines on both safety and task completion.

</details>

---

### [[20_Research/Papers/大模型/Unified_Agent_Managing_Interactions_across_Devices|Unified Agent: Managing Interactions across Devices]]

![[assets/2608.05729_figure.png|800]]

- **arXiv**: [2608.05729](https://arxiv.org/abs/2608.05729)
- **PDF**: https://arxiv.org/pdf/2608.05729
- **详细分析**: [[20_Research/Papers/大模型/Unified_Agent_Managing_Interactions_across_Devices|Unified Agent: Managing Interactions across Devices]]
- **作者**: Xinshuang Liu, Runfa Blark Li, Shaoxiu Wei, Xin Lin, Truong Nguyen
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Unified Agent: Managing Interactions across Devices》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As capabilities rapidly increase, AI agents can move from running inside one app to acting across a user's devices over time. Yet existing agent systems still fall short in this scenario. This is because observations are scattered across devices and moments, but mainstream systems are not designed around this fact: a single agent that treats devices as tools lacks effective state management for all devices across time, and multi-agent systems coordinate across agents but do not maintain the compact carried state a cross-device, cross-time request needs. We argue that the agent should maintain an effectively designed state that organizes engagement evidence, stated facts, and the standing request in a compact, action-ready form for deciding its action given the current observation. To compare state designs, we construct a benchmark of user-agent interaction across devices and time. We instantiate this principle in Unified Agent, a stateful agent that carries interaction evidence across devices and moments and uses it with the current observation to act. In the default setting, it significantly outperforms our adaptations of four published designs. Across changes in multimodal large language model (MLLM) family, capability, and reasoning effort, it remains ahead of all compared systems, demonstrating that the state-design advantage is robust across MLLM settings. Our code and data will be publicly available on GitHub.

</details>

---

### [[20_Research/Papers/机器人/Hijacking_Robots_with_a_Piece_of_Paper_A_Systematic_Study_of_Physical_Prompt_Injection_in_VLM-Controlled_Robots|Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots]]

![[assets/2608.05715_figure.png|800]]

- **arXiv**: [2608.05715](https://arxiv.org/abs/2608.05715)
- **PDF**: https://arxiv.org/pdf/2608.05715
- **详细分析**: [[20_Research/Papers/机器人/Hijacking_Robots_with_a_Piece_of_Paper_A_Systematic_Study_of_Physical_Prompt_Injection_in_VLM-Controlled_Robots|Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots]]
- **作者**: S. M . Bhagya P. Samarakoon, M. A. Viraj J. Muthugala, W. K. R. Sachinthana, Mohan Rajesh Elara
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《Hijacking Robots with a Piece of Paper: A Systematic Study of Physical Prompt Injection in VLM-Controlled Robots》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MM-SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Models (VLMs) are increasingly deployed as planners in robotic systems, where they translate natural-language commands into executable actions grounded in visual scene understanding. This tight coupling between perception and instruction-following introduces a new attack surface: adversarial text placed within the robot's visual field can act as an indirect prompt injection into the VLM's reasoning stack. We present a systematic study of physical prompt injection attacks against VLM-controlled sorting, introducing a four-category taxonomy, indirect signage, task redefinition, authority impersonation, and conflict injection, instantiated as a benchmark of 20 attack prompts evaluated across three physical scene layouts and three command formulations that vary in destination specificity and rule explicitness. Across 5,670 trials on three frontier VLMs (GPT-4o, Gemini 2.5 Flash, Qwen3-VL-32B), attacks succeed at 27.0%, 29.4%, and 5.0% respectively, with authority-impersonating and negation attacks transferring across all three models. Analysis of reasoning traces reveals that successful compromise is nearly always conscious (99.9% acknowledgment rate), and that models defend through structurally different mechanisms, explicit rejection for Gemini, perceptual inattention for GPT-4o. We evaluate three simple mitigations: prompt-based defense (75-100% effective, model-dependent), two-stage verification (85-100%), and pre-processing text masking (100%). Our findings show that VLM-controlled manipulation is meaningfully vulnerable to human-readable physical signage, and that simple defenses substantially reduce risk, though defense choice involves trade-offs. The defenses preserve general task capabilities in our benchmark, but they may impair tasks that require reading in-scene labels.

</details>

---

### [[20_Research/Papers/大模型/DreamGuard_Efficient_Runtime_Guardrail_for_LLM_Agents_via_Risk-Aware_World_Model|DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model]]

![[assets/2608.05695_figure.png|800]]

- **arXiv**: [2608.05695](https://arxiv.org/abs/2608.05695)
- **PDF**: https://arxiv.org/pdf/2608.05695
- **详细分析**: [[20_Research/Papers/大模型/DreamGuard_Efficient_Runtime_Guardrail_for_LLM_Agents_via_Risk-Aware_World_Model|DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model]]
- **作者**: Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 2.05（加权：大模型 1.25，世界模型 0.8）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a critical blind spot for long-horizon risks, where individually benign-looking actions can gradually drift the agent toward hazardous states. In response, we propose DreamGuard, a proactive guardrail for LLM agents built around a risk-aware world model. The world model maintains a compact recurrent latent state over the trajectory and predicts future latent states from which DreamGuard derives immediate-hazard and prefix-risk evidence. It then fuses these multi-horizon signals into intervention decisions before execution. Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to-end latency of 25 ms per call.

</details>

---

### [[20_Research/Papers/大模型/Nonvisual_Classification_of_Ground-Condition_by_Artificial_Proprioception_in_an_Amoeba-Inspired_Autonomous_Walking_Robot|Nonvisual Classification of Ground-Condition by Artificial Proprioception in an Amoeba-Inspired Autonomous Walking Robot]]

![[assets/2608.05684_first_page.png|800]]

- **arXiv**: [2608.05684](https://arxiv.org/abs/2608.05684)
- **PDF**: https://arxiv.org/pdf/2608.05684
- **详细分析**: [[20_Research/Papers/大模型/Nonvisual_Classification_of_Ground-Condition_by_Artificial_Proprioception_in_an_Amoeba-Inspired_Autonomous_Walking_Robot|Nonvisual Classification of Ground-Condition by Artificial Proprioception in an Amoeba-Inspired Autonomous Walking Robot]]
- **作者**: Hyoto Yamaguchi, Zenji Yatabe, Seiya Kasai
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Nonvisual Classification of Ground-Condition by Artificial Proprioception in an Amoeba-Inspired Autonomous Walking Robot》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nonvisual classification of ground condition based on a multimodal sensing approach was investigated for an amoeba-inspired autonomous walking robot. To classify ground condition without image sensing and processing, we implemented artificial proprioception by integrating a three-axis accelerometer, eight foot pressure sensors, and reservoir computing (RC). Even when large fluctuations in the sensor outputs are caused by dynamic motions of a four-legged robot in walking, our system can classify the ground condition, flat or rough, with high accuracy. We demonstrate on-site switching of walking gait depending on ground condition in the robot. We also discuss the contribution of each sensor to ground condition classification.

</details>

---

### [[20_Research/Papers/大模型/F$^2$Agent_Financial_Fusion_of_Agentic_Intelligence_for_Multimodal_Trading|F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading]]

![[assets/2608.05668_figure.png|800]]

- **arXiv**: [2608.05668](https://arxiv.org/abs/2608.05668)
- **PDF**: https://arxiv.org/pdf/2608.05668
- **详细分析**: [[20_Research/Papers/大模型/F$^2$Agent_Financial_Fusion_of_Agentic_Intelligence_for_Multimodal_Trading|F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading]]
- **作者**: Changshuo Liu, Yanzheng Jin, Shangfeng Cai, Peng Fang, Xiaokui Xiao, Beng Chin Ooi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《F$^2$Agent: Financial Fusion of Agentic Intelligence for Multimodal Trading》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With increasingly diverse and heterogeneous information sources, effectively leveraging multimodal data is becoming pivotal for high-quality financial trading. Although recent advancements in Large Language Model (LLM)-based agents have enabled the ingestion of multimodal inputs, existing methods fail to capture nuanced cross-modal dependencies and remain vulnerable to market noise, due to limited multimodal modeling, ineffective fusion mechanisms, and inadequate robustness. To address these challenges, we propose F$^2$Agent, a novel multimodal agentic paradigm driven by the Financial Fusion of Agentic Intelligence. F$^2$Agent first deploys a hierarchy of specialized agents to comprehensively extract modality-specific signals. It further introduces a modality-aware adaptive fusion mechanism coupled with noise-robust consistency regularization to dynamically capture fine-grained inter-modality dependencies and generate noise-resilient trading signals. Extensive experiments on six stocks and cryptocurrency assets demonstrate that F$^2$Agent consistently outperforms 16 competitive baselines across multiple trading metrics, with over 20% relative improvement in annualized return on average. Notably, F$^2$Agent delivers returns of 120.48% on GOOG and 148.41% on TSLA, demonstrating its efficacy and robustness in varying market dynamics.

</details>

---

### [[20_Research/Papers/大模型/Relay,_Don't_Route_Adaptive_Population_Handoff_for_Cost-Efficient_LLM-Driven_Evolution|Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution]]

![[assets/2608.05651_figure.png|800]]

- **arXiv**: [2608.05651](https://arxiv.org/abs/2608.05651)
- **PDF**: https://arxiv.org/pdf/2608.05651
- **详细分析**: [[20_Research/Papers/大模型/Relay,_Don't_Route_Adaptive_Population_Handoff_for_Cost-Efficient_LLM-Driven_Evolution|Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution]]
- **作者**: Sichun Luo, Yi Huang, Guanzhi Deng, Haibo Wang, Haochen Luo, Lei Li, Zefa Hu, Junlan Feng, Qi Liu
- **cs 子类**: cs.AI, cs.CL, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Relay, Don't Route: Adaptive Population Handoff for Cost-Efficient LLM-Driven Evolution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-driven evolution has shown promise for program search and algorithm discovery, but relying on strong models throughout long evolutionary runs is costly. A natural alternative is to combine cheap and strong models under a fixed inference budget. However, existing approaches typically allocate models at the level of individual queries or mutation steps, overlooking that evolutionary search is \textit{stateful}: each generated candidate changes the population from which subsequent mutations are produced. We empirically analyze LLM-driven evolutionary trajectories and find that search progress is strongly front-loaded, early trajectory performance is informative but noisy, and cheap models recover much of the early progress achieved by strong models at lower cost. Motivated by these findings, we propose \textbf{\model}, a training-free framework that shifts budget allocation from individual calls to evolving populations through adaptive \textit{population handoff}. A cheap model explores multiple trajectories in short blocks allocated by a bandit scheduler. Relay Gain, defined as the marginal improvement of a compact, quality-diverse candidate bank constructed for handoff, serves as the scheduler reward and determines when to hand off. The curated candidates initialize a shared strong model population for refinement. Across four benchmarks and three budgets, \model achieves the highest mean score in 11 of 12 settings, outperforming competitive baselines. Our results suggest that in stateful search, budget allocation should be organized around the population, not the individual call.

</details>

---

### [[20_Research/Papers/大模型/Refining_Over_Resampling_Test-Time_Self-Correction_for_LLM_Reasoning|Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning]]

![[assets/2608.05643_figure.png|800]]

- **arXiv**: [2608.05643](https://arxiv.org/abs/2608.05643)
- **PDF**: https://arxiv.org/pdf/2608.05643
- **详细分析**: [[20_Research/Papers/大模型/Refining_Over_Resampling_Test-Time_Self-Correction_for_LLM_Reasoning|Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning]]
- **作者**: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Lena Trigg, Ali Subhan, Muhammad Ali, Dean F. Hougen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OlyBench, OlympiadBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time scaling improves LLM reasoning by using additional inference compute, but wider sampling alone can suffer from diminishing returns: new rollouts often repeat existing answer patterns instead of adding useful reasoning diversity. Verifier-based selection offers an alternative, but its performance depends on the calibration of an external reward model. We propose a verifier-free breadth--depth refinement framework that uses test-time compute to both explore and improve candidate solutions. The method samples multiple independent reasoning rollouts, refines each rollout through iterative self-critique and self-correction, and aggregates the refined answers by majority voting. Breadth preserves diverse initial attempts, while depth repairs local reasoning errors before aggregation. Across AIME24, AIME25, AMC, OlympiadBench, and MATH500, our method consistently improves over greedy decoding, majority voting, verifier-based best-of-$N$, beam search, and lookahead decoding across multiple open-weight models. For instance, with Qwen2.5-1.5B, accuracy increases from the strongest verifier-based baseline to $58.0\%$ on MATH500, and from $25.0\%$ to $32.5\%$ on AMC. These results show that test-time compute can be more effective when used to refine sampled trajectories rather than only to sample more candidates or rely on verifier-guided selection.

</details>

---

### [[20_Research/Papers/具身智能/SkillZip_Contract-Preserving_Graph_Compression_for_Scalable_Agent_Skill_Libraries|SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries]]

![[assets/2608.05604_figure.png|800]]

- **arXiv**: [2608.05604](https://arxiv.org/abs/2608.05604)
- **PDF**: https://arxiv.org/pdf/2608.05604
- **详细分析**: [[20_Research/Papers/具身智能/SkillZip_Contract-Preserving_Graph_Compression_for_Scalable_Agent_Skill_Libraries|SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries]]
- **作者**: Xingyu Tan, Xiaoyang Wang, Qing Liu, Xiwei Xu, Xin Yuan, Liming Zhu, Wenjie Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.95（加权：具身智能 0.3，大模型 0.65）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) increasingly act as agents whose procedural knowledge is stored in reusable skill packages and loaded at inference time. As skill libraries grow, a central challenge is to expose the smallest sufficient executable context under a limited context budget. Existing systems struggle to reuse routines below the whole-skill level, preserve procedural contracts during compression, keep compressed routines executable and expandable, and update the compressed library as skills evolve. These challenges reveal a unit mismatch: skills are retrieved as packages, compressed as text, and converted into execution graphs only after retrieval, whereas reliable reuse requires a contract-bearing procedural unit. We propose SkillZip, an execution-aware procedural abstraction framework that performs contract-preserving compression over section-level graphs. SkillZip rewrites recurring contract-valid motifs into reversible ported macros while preserving boundary signatures, dependency closure, verifier reachability, and source-level expansion. At inference time, it hydrates a compact, dependency-closed context and expands macros only when required. ReZip further integrates new skills and revises risky macros using execution evidence. Comprehensive experiments1 on technical and embodied agent benchmarks show SkillZip consistently outperforms the strongest baseline by up to 12.2 points, while achieving a 3.46x compression ratio with 99.2% dependency preservation and 98.7% verifier reachability. Scaling analyses further confirm robust retrieval across skill libraries ranging from 200 to 100K skills.

</details>

---

### [[20_Research/Papers/强化学习/LC-GRPO_Bridging_Train-Inference_Gap_for_Flow-Based_GRPO_with_Langevin_Correction|LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction]]

![[assets/2608.05600_figure.png|800]]

- **arXiv**: [2608.05600](https://arxiv.org/abs/2608.05600)
- **PDF**: https://arxiv.org/pdf/2608.05600
- **详细分析**: [[20_Research/Papers/强化学习/LC-GRPO_Bridging_Train-Inference_Gap_for_Flow-Based_GRPO_with_Langevin_Correction|LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction]]
- **作者**: Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DrawBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based generative models are typically sampled by solving a deterministic ordinary differential equation (ODE), whereas online reinforcement learning requires stochastic rollouts for policy exploration and optimization. Existing GRPO methods for flow models therefore replace the inference-time ODE with a stochastic differential equation (SDE) during training. Although the ODE and SDE share the same marginal distributions in continuous time, their finite-step discretizations can differ substantially. In particular, SDE rollouts often become blurry as the exploration noise increases, creating a mismatch between the samples used for reinforcement learning and those generated by the test-time ODE sampler. We introduce LC-GRPO, a flow-based GRPO framework with Langevin correction. Each rollout transition first takes an inference-aligned ODE Euler step and then applies a stochastic Langevin correction targeting the marginal distribution at the resulting timestep. The required score is recovered directly from the flow velocity, requiring no additional score model, while the resulting transition remains an isotropic Gaussian with a tractable likelihood for policy optimization. We theoretically show that, under suitable conditions, one Langevin correction step reduces the Wasserstein error of an imperfect ODE Euler step. At a matched randomness level, we further show that the proposed transition can be more accurate than the standard Euler--Maruyama discretization of the reverse SDE. Experiments on SD3.5-Medium, FLUX.1-Dev, and HunyuanVideo demonstrate that LC-GRPO consistently improves reward optimization across text-to-image and text-to-video tasks, preserves generation quality, and substantially narrows the gap between stochastic training rollouts and deterministic test-time ODE inference.

</details>

---

### [[20_Research/Papers/强化学习/Search-Aided_Joint_Agent-Environment_Reinforcement_Learning_for_Robust_Lifelong_Multi-Agent_Path_Finding_with_Rotations|Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations]]

![[assets/2608.05588_figure.png|800]]

- **arXiv**: [2608.05588](https://arxiv.org/abs/2608.05588)
- **PDF**: https://arxiv.org/pdf/2608.05588
- **详细分析**: [[20_Research/Papers/强化学习/Search-Aided_Joint_Agent-Environment_Reinforcement_Learning_for_Robust_Lifelong_Multi-Agent_Path_Finding_with_Rotations|Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations]]
- **作者**: He Jiang, Jingtian Yan, Yulun Zhang, Yimin Tang, Tanishq Duhan, Rishi Veerapaneni, Guillaume Sartoretti, Jiaoyang Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NORL, SARL, SERL, SJRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free paths for agents that continuously receive new goals upon reaching their current ones. While many learning-based planners have been proposed for LMAPF, most rely on oversimplified kinematic assumptions that may overlook motion constraints critical to real-world performance. In this work, we study a more realistic LMAPF model derived from many real-world automated warehouse systems, termed LMAPF-R2, which incorporates robust safety constraints and in-place rotation constraints. These constraints substantially increase coordination difficulty, particularly in highly constrained spaces. To address these challenges, we propose Search-Aided Joint Reinforcement Learning (SJRL). We first augment neural policies with Causal PIBT, a single-step search-based planner that resolves agents' collisions and propagates their intentions. We then introduce a unified RL formulation that jointly optimizes agent and environment policies, where the environment policy learns graph edge costs to provide global movement guidance via backward Dijkstra search. Experiments demonstrate that SJRL achieves significant improvements over the strong search-based planner, Causal-PIBT, across multiple high-density maps. We further validate SJRL in a challenging mixed-reality warehouse environment with 8 physical robots and 248 virtual robots.

</details>

---

### [[20_Research/Papers/大模型/EcoAgent-Bench_Evaluating_Economic_Decision-Making_in_Budget-Constrained_LLM_Agents|EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents]]

![[assets/2608.05519_figure.png|800]]

- **arXiv**: [2608.05519](https://arxiv.org/abs/2608.05519)
- **PDF**: https://arxiv.org/pdf/2608.05519
- **详细分析**: [[20_Research/Papers/大模型/EcoAgent-Bench_Evaluating_Economic_Decision-Making_in_Budget-Constrained_LLM_Agents|EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents]]
- **作者**: Jie Wu, Ming Gong, Feixiang Cheng, Qinqin Zhao
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, CostBench, EcoAgent-Bench, HotpotQA, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent benchmarks usually measure task completion and treat resource use as an auxiliary statistic. In deployment, however, the choice among a local lookup, broad search, composite research tool, stronger model, or human escalation is part of the task itself. We introduce EcoAgent-Bench, in which every task specifies priced actions and an explicit budget. Its 304 real-derived tasks span five families adapted from GAIA, HotpotQA, and MuSiQue, and test four decisions: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. We evaluate seven LLM agents in tool-API and workspace-CLI settings, together with four oracle scripted controls. Micro-averaged accuracy rewards one-sided policies: always-escalate controls achieve high micro success while failing save-oriented tasks. We therefore also report an economic-consistency score (the worse of accuracy on upgrade-oriented and save-oriented family groups) which exposes this failure. Tool-API agents attain only 3.9-24.0% micro strict success (at most 7.3% economic consistency), often either stopping before warranted escalation or overspending on cheap tasks. A threshold-crossing budget sweep changes GPT-5.4's escalation rate from 0% to only 3%. These results show that completion under a budget and economical action selection are distinct properties. We release the task bundle, transformation pipeline, frozen evaluation environments, and integrity-bound result artifacts needed to study both.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Online_Traffic_Scheduling_in_Time-Sensitive_Application|Multi-Agent Reinforcement Learning for Online Traffic Scheduling in Time-Sensitive Application]]

![[assets/2608.05346_figure.png|800]]

- **arXiv**: [2608.05346](https://arxiv.org/abs/2608.05346)
- **PDF**: https://arxiv.org/pdf/2608.05346
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Online_Traffic_Scheduling_in_Time-Sensitive_Application|Multi-Agent Reinforcement Learning for Online Traffic Scheduling in Time-Sensitive Application]]
- **作者**: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-Agent Reinforcement Learning for Online Traffic Scheduling in Time-Sensitive Application》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL, TSN-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time-sensitive networking (TSN) is increasingly integrated into mobile edge computing (MEC) to support applications with stringent latency requirements, such as extended reality (XR). However, existing TSN scheduling solutions predominantly rely on static optimization techniques or centralized learning models that are based on fixed traffic patterns, limiting their effectiveness in dynamic environments. In practice, MEC environments often host multiple co-located XR traffic flows whose characteristics evolve over time, creating complex inter-queue dependencies that current schedulers fail to capture. Addressing these challenges requires adaptive, decentralized scheduling mechanisms capable of coordinating multiple TSN queues under varying traffic conditions. To this end, this paper proposes a multi-agent reinforcement learning (MARL) framework for TSN scheduling, where each TSN queue is modeled as an autonomous agent. The Heterogeneous-Agent Proximal Policy Optimization (HAPPO) algorithm is employed to explicitly model inter-agent dependencies and jointly optimize service delivery across queues. The simulation results demonstrate that the proposed approach reduces average frame waiting times by up to 26.8% and worst-case delays by approximately 16.8%, highlighting its effectiveness in dynamic XR-driven MEC scenarios.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Transformer_for_Queue-Level_XR_Traffic_Scheduling_in_TSN_Networks|Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks]]

![[assets/2608.05340_figure.png|800]]

- **arXiv**: [2608.05340](https://arxiv.org/abs/2608.05340)
- **PDF**: https://arxiv.org/pdf/2608.05340
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Transformer_for_Queue-Level_XR_Traffic_Scheduling_in_TSN_Networks|Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks]]
- **作者**: Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time-Sensitive Networking (TSN) and Mobile Edge Computing (MEC) hold strong potential for enabling ultra-reliable low-latency communication for time-sensitive applications, such as eXtended Reality (XR). However, the widespread adoption of XR introduces significant challenges due to co-located services in MEC environments, leading to contention for shared network resources. Moreover, XR traffic types have distinct characteristics and criticality in terms of timing requirements, further increasing the complexity and dynamics of such environments. Although reinforcement learning has shown promise for TSN scheduling optimization in dynamic network scenarios, existing approaches rely on centralized or high-level multi-agent designs and are typically tailored to periodic and predictable industrial traffic, limiting their applicability to XR workloads. As a result, these approaches suffer from (i) limited ability to capture inter-queue dependencies due to coarse-grained control, and (ii) poor adaptability to highly dynamic and heterogeneous XR traffic. To address these gaps, we propose a multi-agent reinforcement learning approach for queue-level XR traffic scheduling. We adopt the multi-agent transformer (MAT) to model inter-queue dependencies via attention over agents' observations and actions, enabling implicit coordination across heterogeneous co-located XR applications. Our simulation results show that the proposed method outperforms baselines, achieving up to 71.42% latency reduction and up to 83.2% reduction in failure rate, while consistently achieving high reliability across all queues.

</details>

---

### [[20_Research/Papers/机器人/Failing_Gracefully_Mitigating_Impact_of_Inevitable_Robot_Failures|Failing Gracefully: Mitigating Impact of Inevitable Robot Failures]]

![[assets/2608.05313_figure.jpg|800]]

- **arXiv**: [2608.05313](https://arxiv.org/abs/2608.05313)
- **PDF**: https://arxiv.org/pdf/2608.05313
- **详细分析**: [[20_Research/Papers/机器人/Failing_Gracefully_Mitigating_Impact_of_Inevitable_Robot_Failures|Failing Gracefully: Mitigating Impact of Inevitable Robot Failures]]
- **作者**: Duc M. Nguyen, Saad A. Ghani, Andrew Marshall, Allison Andreyev, Gregory J. Stein, Xuesu Xiao
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Failing Gracefully: Mitigating Impact of Inevitable Robot Failures》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FailBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Service robots operate in household environments shared with humans, pets, and everyday objects, where they are highly susceptible to failures such as software crashes, hardware degradation, or unpredictable interactions. While roboticists strive to minimize failures, some remain inevitable, making it critical to mitigate their potential consequences for safe and reliable deployment. This paper introduces a novel safety formulation that evaluates both the probability of impactful interactions between robots and surrounding entities during failures, and the severity of their outcomes. By quantifying the impact of failures on different entities, our approach enables robots to make informed planning decisions that balance safety with task efficiency. To support systematic evaluation, we also present FailBench, a MuJoCo-based simulation framework for studying robot-environment interactions under diverse failure modes, including sensing issues and actuator malfunctions. Together, our safety formulation and FailBench provide a foundation for developing safer and more robust motion plans and learned policies in real-world household environments.

</details>

---

### [[20_Research/Papers/大模型/Agentic_self-driving_microscopy_benchmarks_support_qualification_but_do_not_necessarily_generalize_to_unseen_tasks|Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks]]

![[assets/2608.05266_figure.png|800]]

- **arXiv**: [2608.05266](https://arxiv.org/abs/2608.05266)
- **PDF**: https://arxiv.org/pdf/2608.05266
- **详细分析**: [[20_Research/Papers/大模型/Agentic_self-driving_microscopy_benchmarks_support_qualification_but_do_not_necessarily_generalize_to_unseen_tasks|Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks]]
- **作者**: Nathan S Johnson, Ian Abshire
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agentic self-driving microscopy benchmarks support qualification but do not necessarily generalize to unseen tasks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents are increasingly being developed to control a wide range of scientific characterization tools including microscopes and synchrotron beamlines. Research into agentic control of physical infrastructure is nascent and there are few well-established paradigms for how to engineer an agentic system. There are many choices to make when designing a microscopy agent, including the choice of LLM, the number of agents to use, agent responsibilities and delegation rules, retrieval-augmented generation parameters, and more. When designing and optimizing an agentic microscope controller, researchers not only want to ensure that the agent can correctly perform known tasks but also that the agent can generalize to new tasks that it has not encountered before. In this study, we develop a benchmark and trace-logging framework that reveals a) how different choices of agent architecture impact performance at microscopy tasks and b) the limitations of benchmarks for predicting if a particular agent will perform well on unseen microscopy tasks. The framework was used to evaluate one-, two-, and three-agent graph topologies, five LLMs, RAG and context parameters, and operational constraints across 53 microscopy benchmark tests. In total, 105 agent configurations, 1,949 individual test runs, and 49,109 RAG retrievals were recorded. Direct comparisons showed clear differences in latency, token use, cost, and failure mode between configurations. However, surrogate models trained on agent architecture and test results did not reliably predict an agent's performance on new, unseen tasks. These results show that these benchmarks are useful for qualification, regression testing, diagnosis, and direct comparison, but the current heterogeneous test suite does not support a task-independent global configuration model.

</details>

---

### [[20_Research/Papers/大模型/An_Emerging_Retail_Portfolio_Management_Application_Personalized,_Tax-Aware_Reinforcement_Learning_with_Natural_Language_Goals|An Emerging Retail Portfolio Management Application: Personalized, Tax-Aware Reinforcement Learning with Natural Language Goals]]

![[assets/2608.05255_figure.png|800]]

- **arXiv**: [2608.05255](https://arxiv.org/abs/2608.05255)
- **PDF**: https://arxiv.org/pdf/2608.05255
- **详细分析**: [[20_Research/Papers/大模型/An_Emerging_Retail_Portfolio_Management_Application_Personalized,_Tax-Aware_Reinforcement_Learning_with_Natural_Language_Goals|An Emerging Retail Portfolio Management Application: Personalized, Tax-Aware Reinforcement Learning with Natural Language Goals]]
- **作者**: Ramin Pishehvar
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《An Emerging Retail Portfolio Management Application: Personalized, Tax-Aware Reinforcement Learning with Natural Language Goals》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retail investors lack access to the kind of personalized, tax-aware portfolio management that institutional clients take for granted -- existing robo-advisors use static, rule-based allocation, and institutional-grade systems require account minimums and technology stacks unavailable to individual investors. We present a fully built, integration-tested application that closes this gap: a FastAPI backend and web dashboard that let a user describe an investment goal in plain language (e.g. "I want steady growth but need to sell some shares next month for a down payment"), routes that goal to one of six investment mandates, and produces a live, broker-integrated portfolio recommendation from athree-phase reinforcement learning system -- a self-supervised cross-asset encoder, a Mixture-of-Experts (MoE) allocation policy with a learned intent router, and a lightweight LoRA adapter that personalizes recommendations from an individual's revealed brokerage behavior without retraining the shared model. The system is functionally complete and integration-tested end-to-end against a live brokerage API (Alpaca, paper-trading mode), including multi-user authentication, a trust first preview-before-apply confirmation flow, daily email digests, and an auditable action-integrity chain, but has not yet been opened to real end-users; we report this honestly as an emerging, pre-deployment application with a concrete path to full deployment, alongside 14-day walk-forward backtests (bootstrapped confidence intervals included) as preliminary, pre-deployment validation rather than production performance. We also report several practical engineering lessons -- silently-inactive integration paths, hanging third-party API calls, and the value of end-to-end empirical verification over trusting checkpoint metadata -- that we believe generalize to other applied RL systems built on external, live data sources.

</details>

---

### [[20_Research/Papers/大模型/Search2Skill_Skill_Distillation_Beyond_Knowledge_Boundaries_Via_Rubric-Based_Reinforcement_Learning|Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning]]

![[assets/2608.05245_figure.png|800]]

- **arXiv**: [2608.05245](https://arxiv.org/abs/2608.05245)
- **PDF**: https://arxiv.org/pdf/2608.05245
- **详细分析**: [[20_Research/Papers/大模型/Search2Skill_Skill_Distillation_Beyond_Knowledge_Boundaries_Via_Rubric-Based_Reinforcement_Learning|Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning]]
- **作者**: Muyang Ye, Tian Lan, Feihu Jiang, Yongshi Ye, Wuyunsiqin, Bin Zhu, Qianghuai Jia, Zhao Xu, Weihua Luo, Ye Wang, Jinyang Zhang, Longyue Wang...
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EvoAgentBench, SuperGPQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reusable skills, which encapsulate the procedural knowledge required to solve real-world professional tasks, offer LLM-based agents a path toward self-evolution in expert domains. Existing self-evolving skill methods construct skills internally from the model's parametric knowledge or trajectories, and are therefore bounded by what the model already knows. However, the domain conventions and standard procedures underlying professional skills often lie beyond this boundary and are hard to elicit from the agent alone. To address this issue, we therefore propose a novel framework, Search2Skill, that automatically identifies the agent's capability gaps, searches external sources to address them, and distills the retrieved evidence into structured, reusable skills. Specifically, Search2Skill is optimized by a rubric-based reinforcement learning scheme that jointly improves when to search, how to search, and how to generate skills. Experiments on eight expert-level domains from three benchmarks show that Search2Skill consistently outperforms both search-augmented and trajectory-based skill-learning baselines under both streaming and held-out evaluation protocols. Further analyses show that the gains arise from skill abstraction rather than raw retrieved evidence, and that the acquired skills transfer across model scales.

</details>

---

### [[20_Research/Papers/大模型/SkillTrace_Multi-Trace_Provenance_Auditing_for_LLM-Agent_Skill_Reuse|SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse]]

![[assets/2608.05204_figure.png|800]]

- **arXiv**: [2608.05204](https://arxiv.org/abs/2608.05204)
- **PDF**: https://arxiv.org/pdf/2608.05204
- **详细分析**: [[20_Research/Papers/大模型/SkillTrace_Multi-Trace_Provenance_Auditing_for_LLM-Agent_Skill_Reuse|SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse]]
- **作者**: Jialuo Chen, Minghe Wang, Lingqi Jiang, Jianan Ma, Xinhao Deng, Xiaohu Du, Ruixiao Lin, Yunhao Feng, Linkang Du, Jingyi Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillTrace-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-agent ecosystems are rapidly growing around reusable skills: mixed-modality packages of metadata, natural-language instructions, code, tools, references, and operational workflows. As skills become marketplace artifacts, auditing their reuse is no longer the same problem as ordinary code clone detection. Existing detectors target single-modality source code or whole-package similarity, yet skill reuse evidence is distributed across authored text, implementation fragments, and operational structure. As a result, they can miss reuse that preserves only one part of a skill. We present SKILLTRACE, a multi-trace provenance auditing framework for LLM-agent skill reuse. SKILLTRACE extracts three provenance traces: Expression, Implementation, and Operational. It represents the Operational Trace as a Skill Operational Graph (SOG) that captures activation, procedure, and resource-flow structure. An LLM assists only the Operational-trace extraction, once at ingestion; at audit time SKILLTRACE compares cached traces deterministically, calibrates each trace against same-function strict negatives, and reports which trace supports a reuse decision. On SKILLTRACE-BENCH, with 820 transformed reuse positives over 100 marketplace anchors and 751 negative controls, SKILLTRACE achieves AUROC 0.938 and F1 0.898. A 36,446-skill wild audit further shows that trace-attributed evidence surfaces actionable reuse review queues beyond repository-level baselines.

</details>

---

### [[20_Research/Papers/大模型/Post-Hoc_Trajectory-Risk_Certification_for_Modular_LLM-Based_Security_Agents|Post-Hoc Trajectory-Risk Certification for Modular LLM-Based Security Agents]]

![[assets/2608.05199_first_page.png|800]]

- **arXiv**: [2608.05199](https://arxiv.org/abs/2608.05199)
- **PDF**: https://arxiv.org/pdf/2608.05199
- **详细分析**: [[20_Research/Papers/大模型/Post-Hoc_Trajectory-Risk_Certification_for_Modular_LLM-Based_Security_Agents|Post-Hoc Trajectory-Risk Certification for Modular LLM-Based Security Agents]]
- **作者**: Zhenpeng Li
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Post-Hoc Trajectory-Risk Certification for Modular LLM-Based Security Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous security agents operate as staged pipelines, such as classifying network traffic and then attributing attacks to a specific technique. Split conformal prediction gives each stage finite-sample coverage, but deployment requires a trajectory-level guarantee across the full chain. These guarantees do not compose automatically when stages are independently trained and calibrated. Bonferroni allocation is distribution-free but conservative under correlated errors. We show that a natural pairwise-correlation extension to three or more stages is invalid because it gives a lower rather than an upper bound, and derive a valid spanning-tree alternative. We distinguish whether stages are dependent from whether an audit sample is large enough to certify that dependence, and give matching upper and information-theoretic lower sample-complexity bounds. We also show that coarse-to-fine label selection can create near-perfect measured correlation without learned dependence. On a two-stage intrusion-detection pipeline across 6 open LLMs and 2 datasets, removing this artifact reduces measured correlation from near 1 to 0-0.78. A direct audit of trajectory failure becomes 13.7% tighter than Bonferroni once the audit reaches the required sample size, but is worse when undersized. A modular certificate using per-stage certificates and a pairwise overlap bound yields a positive average gain of 0.6%, quantifying the cost of lacking joint access. Same-model, cross-model, and permuted-pairing tests show that residual dependence reflects shared sample difficulty, not shared model representations. Average trajectory coverage across 12 configurations is 92.7% +/- 2.4% at alpha = 0.10. Under cross-dataset deployment, single-step miscoverage reaches 100% even when accuracy remains 78%, showing that distribution shift destroys calibrated confidence before raw accuracy.

</details>

---

### [[20_Research/Papers/大模型/Autonomous_Research_Agents_A_Survey_of_AI_Scientists_and_the_Verification_Gap|Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap]]

![[assets/2608.05179_figure.png|800]]

- **arXiv**: [2608.05179](https://arxiv.org/abs/2608.05179)
- **PDF**: https://arxiv.org/pdf/2608.05179
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_Research_Agents_A_Survey_of_AI_Scientists_and_the_Verification_Gap|Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap]]
- **作者**: Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly used across the scientific research lifecycle: ideation, literature search, experiment design and execution, analysis, manuscript drafting, and review. End-to-end AI scientist systems can now produce paper-like manuscripts, but their claims are often harder to verify than their code is to run. This survey studies that gap in computational AI/ML research, where code, benchmarks, experiments, and write-ups are most visible. We screen 125 candidate works and include 35, with full-text coding of 26 entries: 24 runnable systems and two study or position papers. We code seven audit dimensions: lifecycle stage, autonomy level, evaluation method, released artifacts, human-in-the-loop points, novelty verification, and result-selection disclosure. The main pattern is that code release is now common, but reproducibility-grade and claim-verification artifacts remain much less common. In the 24 runnable systems, 83 percent release code, while 38 percent release seeds or execution traces and 38 percent report any novelty-verification method. Among nine closed-loop L4 systems, seven are mechanical reruns and one is author-claimed without an external check; no LLM-era system in the corpus demonstrates an externally validated in-loop oracle under our coding rule. We contribute a coded corpus, a lifecycle-by-autonomy map, an auditability-gap analysis, and a reviewer-facing reporting checklist. The survey argues that the field's central bottleneck is no longer only whether agents can complete research tasks, but whether reviewers can verify the claims those agents produce.

</details>

---

### [[20_Research/Papers/大模型/Universal_Pathologies,_Conditional_Consequences_A_Triple-Robustness_Analysis_of_RAG_for_Multi-Hop_Traceability|Universal Pathologies, Conditional Consequences: A Triple-Robustness Analysis of RAG for Multi-Hop Traceability]]

![[assets/2608.05153_figure.png|800]]

- **arXiv**: [2608.05153](https://arxiv.org/abs/2608.05153)
- **PDF**: https://arxiv.org/pdf/2608.05153
- **详细分析**: [[20_Research/Papers/大模型/Universal_Pathologies,_Conditional_Consequences_A_Triple-Robustness_Analysis_of_RAG_for_Multi-Hop_Traceability|Universal Pathologies, Conditional Consequences: A Triple-Robustness Analysis of RAG for Multi-Hop Traceability]]
- **作者**: Meftun Akarsu, Burak Ozdemir
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《Universal Pathologies, Conditional Consequences: A Triple-Robustness Analysis of RAG for Multi-Hop Traceability》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GraphRAG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

GraphRAG underperforms vector RAG on citation precision in many reports, but where and why have remained corpus-bound. We present a triple-robustness analysis that holds the retrieval architecture fixed and varies three orthogonal axes embedder (local e5-small -&gt; Azure text-embedding-3-small), corpus (DO-178C typed-edge requirements -&gt; Wikipedia paragraph chains via MuSiQue), and judge (paired GPT-5.4 x GPT-4.1) across 4,440 main-matrix runs, 600 cross-corpus runs, and 1,200 paired faithfulness judgments. (C2a) Over-citation is architecturally universal: GraphRAG emits 11-15 IDs per answer at citation precision 0.12-0.23 and retrieval recall 0.68-0.87 across all three settings. (C2b) Its faithfulness consequence is corpus-conditional: in typed-edge DO-178C, GraphRAG faithfulness collapses 74%-&gt;40% across hops; on Wikipedia chains the same pipeline rises 42%-&gt;58% because over-cited paragraphs remain topically supporting. (C1) Stratum-conditional winners are corpus-conditional but embedder-robust: vanilla wins 2-hop on DO-178C, GraphRAG wins 2-hop on MuSiQue, identical under either embedder. (C3) Single-judge LLM faithfulness is fragile to retrieval state: same-judge self-kappa across embedders is 0.137 for GPT-5.4 (verdict change on 41% of items). A learned router on dense embeddings alone reaches macro-F1 0.86 on hop classification (C4). We argue triple-robustness is the minimum bar for trustworthy RAG architecture claims.

</details>

---
