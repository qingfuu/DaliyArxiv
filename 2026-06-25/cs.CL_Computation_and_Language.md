# cs.CL | Computation and Language | 2026-06-25

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/强化学习/Why_Multi-Step_Tool-Use_Reinforcement_Learning_Collapses_and_How_Supervisory_Signals_Fix_It|Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It]]

![[assets/2606.26027_figure.png|800]]

- **arXiv**: [2606.26027](https://arxiv.org/abs/2606.26027)
- **PDF**: https://arxiv.org/pdf/2606.26027
- **详细分析**: [[20_Research/Papers/强化学习/Why_Multi-Step_Tool-Use_Reinforcement_Learning_Collapses_and_How_Supervisory_Signals_Fix_It|Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It]]
- **作者**: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Tool-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.

</details>

---

### [[20_Research/Papers/大模型/OPERA_Aligning_Open-Ended_Reasoning_via_Objective_Perplexity-based_Reinforcement_Learning|OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning]]

![[assets/2606.25757_figure.png|800]]

- **arXiv**: [2606.25757](https://arxiv.org/abs/2606.25757)
- **PDF**: https://arxiv.org/pdf/2606.25757
- **详细分析**: [[20_Research/Papers/大模型/OPERA_Aligning_Open-Ended_Reasoning_via_Objective_Perplexity-based_Reinforcement_Learning|OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning]]
- **作者**: Wenxuan Jiang, Zining Fan, Zijian Zhang, Xuecheng Wu, Hongming Tan, Haoyang Dai, Xiaoyu Li, Xuezhi Cao, Ninghao Liu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：WritingBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has enabled LLMs to excel in objective reasoning tasks such as mathematics and code generation. However, applying RL to open-ended tasks, such as creative writing, remains challenging because LLM-as-a-judge reward models often exhibit stylistic biases and positional inconsistencies, leading to unstable supervision. To address this, we propose OPERA (Objective Perplexity-based Reflective Alignment), which replaces unreliable external judges with intrinsic rewards derived from perplexity dynamics. Specifically, we derive an intrinsic reward signal from perplexity dynamics, quantifying uncertainty reduction at critical reflective states. During the cold-start phase, we introduce a data synthesis method that leverages carefully designed guiding words to generate diverse reasoning traces, along with perplexity-prioritized rollouts that utilize internal log-probabilities to identify logically consistent reasoning branches. This pipeline yields a large-scale dataset comprising 20,000 high-quality reasoning trajectories. Empirical evaluations consistently demonstrate the scalability and efficacy of our approach in alignment for open-ended tasks. Implementing OPERA on Qwen3-8B establishes a new state-of-the-art among open-source models, achieving parity with or surpassing proprietary models like Gemini2.5 and MiniMax-M2.5 in some open-ended tasks. The code is available at https://github.com/pangpang-xuan/OPERA.

</details>

---

### [[20_Research/Papers/大模型/Riazi-8B_An_Urdu_Large_Language_Model_for_Mathematical_Reasoning|Riazi-8B: An Urdu Large Language Model for Mathematical Reasoning]]

![[assets/2606.25568_figure.png|800]]

- **arXiv**: [2606.25568](https://arxiv.org/abs/2606.25568)
- **PDF**: https://arxiv.org/pdf/2606.25568
- **详细分析**: [[20_Research/Papers/大模型/Riazi-8B_An_Urdu_Large_Language_Model_for_Mathematical_Reasoning|Riazi-8B: An Urdu Large Language Model for Mathematical Reasoning]]
- **作者**: Azher Ali, Ibtsam Haider, Raja Khurram Shahzad, Seemab Latif, Mehwish Fatima
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《Riazi-8B: An Urdu Large Language Model for Mathematical Reasoning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent LLMs demonstrate strong mathematical reasoning capabilities, but existing gains rely heavily on English-centric training resources and benchmarks. As a result, reasoning performance degrades substantially in low-resource languages such as Urdu, where reasoning-oriented datasets and adapted models remain scarce. Urdu lacks both reasoning-oriented resources and models adapted for multi-step mathematical problem solving, limiting the applicability of recent progress to Urdu-speaking users. We address this gap through Riazi-8B, an Urdu mathematical reasoning model developed through a two-step adaptation process comprising continued pre-training on Urdu Wikipedia and supervised fine-tuning on Urdu Chain-of-Thought data derived from GSM8K. We evaluate Riazi-8B on MGSM-Urdu against existing Urdu instruction-tuned models. Our results show consistent improvements in answer correctness, reasoning quality, response completeness, and Urdu generation. Our findings demonstrate that combining Urdu language adaptation with reasoning-focused fine-tuning is an effective strategy for extending mathematical reasoning capabilities to low-resource languages.

</details>

---

### [[20_Research/Papers/大模型/The_Interplay_of_Harness_Design_and_Post-Training_in_LLM_Agents|The Interplay of Harness Design and Post-Training in LLM Agents]]

![[assets/2606.25447_figure.png|800]]

- **arXiv**: [2606.25447](https://arxiv.org/abs/2606.25447)
- **PDF**: https://arxiv.org/pdf/2606.25447
- **详细分析**: [[20_Research/Papers/大模型/The_Interplay_of_Harness_Design_and_Post-Training_in_LLM_Agents|The Interplay of Harness Design and Post-Training in LLM Agents]]
- **作者**: Kyungmin Kim, Youngbin Choi, Seoyeon Lee, Suhyeon Jun, Dongwoo Kim, Sangdon Park
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Interplay of Harness Design and Post-Training in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation. While agents are routinely post-trained, this scaffolding is typically treated as a fixed engineering detail, with design effort limited to the training-free regime. Moreover, existing post-training algorithms assume a static environment, even though tool environments and tasks often shift upon deployment. To address this gap, we extend $\texttt{ALFWorld}$ (i) to treat the harness as a controllable design dimension and (ii) to support evaluation under task and tool environment shifts. Building on this, we systematically analyze how the harness design influences post-training in both in-distribution and out-of-distribution (OOD) settings. We empirically show that harness-aware post-training not only improves in-distribution performance but also enables agents to robustly adapt to OOD settings. Under a harness with minimal design effort, post-training suffers a drastic performance drop under stronger tool environment shifts, further highlighting the importance of harness-aware post-training under such shifts.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Next-Observation_Prediction_Agent-Authored_World_Modeling_for_Sequential_Decision_Making|Beyond Next-Observation Prediction: Agent-Authored World Modeling for Sequential Decision Making]]

![[assets/2606.25421_figure.png|800]]

- **arXiv**: [2606.25421](https://arxiv.org/abs/2606.25421)
- **PDF**: https://arxiv.org/pdf/2606.25421
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Next-Observation_Prediction_Agent-Authored_World_Modeling_for_Sequential_Decision_Making|Beyond Next-Observation Prediction: Agent-Authored World Modeling for Sequential Decision Making]]
- **作者**: Guangfeng Cai, Kaibing Yang, Shuo He, Yu Li, Shengtian Yang, Jiaqi Lv, Lei Feng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Beyond Next-Observation Prediction: Agent-Authored World Modeling for Sequential Decision Making》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies on world modeling for Large Language Model (LLM) agents typically formulate the learning objective as next-observation prediction. However, this objective ties supervision to what a transition happens to reveal, which may omit the dynamics most relevant to the agent's current decision. To bridge this gap, we propose Agent-Authored World Modeling (AAWM), a training procedure that constructs supervision from the policy's own decision needs. Specifically, at each state, the agent identifies what it needs to understand about the environment before acting. These needs drive the retrieval of relevant transition evidence across trajectories, which is then synthesized into training targets that capture decision-oriented dynamics instead of reconstructing the next observation. This aligns the training objective with the dynamics the policy needs before acting, not with the contents of the next observation. Experimental results validate the effectiveness of AAWM across multiple environments and training settings. These results show that decision-aware world-model targets provide a more effective learning signal than next-observation prediction.

</details>

---

### [[20_Research/Papers/强化学习/Digital_Twin-Driven_Adaptive_Sim-to-Real_Alignment_via_Reinforcement_Learning_for_Vibration-Based_Bearing_Health_Monitoring_Under_Data_Scarc|Digital Twin-Driven Adaptive Sim-to-Real Alignment via Reinforcement Learning for Vibration-Based Bearing Health Monitoring Under Data Scarcity]]

![[assets/2606.24954_first_page.png|800]]

- **arXiv**: [2606.24954](https://arxiv.org/abs/2606.24954)
- **PDF**: https://arxiv.org/pdf/2606.24954
- **详细分析**: [[20_Research/Papers/强化学习/Digital_Twin-Driven_Adaptive_Sim-to-Real_Alignment_via_Reinforcement_Learning_for_Vibration-Based_Bearing_Health_Monitoring_Under_Data_Scarc|Digital Twin-Driven Adaptive Sim-to-Real Alignment via Reinforcement Learning for Vibration-Based Bearing Health Monitoring Under Data Scarcity]]
- **作者**: Jinghan Wang, Yanjun Chen, Wei Zhang, Wentao Wu, Tianchen Liu, Gaoliang Peng
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.52（加权：具身智能 1.2，强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Digital Twin-Driven Adaptive Sim-to-Real Alignment via Reinforcement Learning for Vibration-Based Bearing Health Monitoring Under Data Scarcity》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vibration-based health monitoring of rotating machinery requires reliable fault diagnosis under operational data constraints, yet condition assessment remains challenged by structural scarcity of fault events and heterogeneous sim-to-real gaps in digital twin-generated signals. Each fault type generates impulses with distinct periodicity, amplitude modulation, and spectral character, making feature-space discrepancies fundamentally heterogeneous across fault classes. Existing domain adaptation methods apply a class-agnostic global transformation that cannot close all fault-specific gaps without distorting inter-class separability, while uniform source-target mixing introduces distributional noise into the data-abundant Normal class. These limitations stem from treating a sequential, state-dependent alignment problem as a one-shot optimization. Each corrective transformation simultaneously reshapes all class distributions, creating state dependencies that static gradient descent cannot resolve. We formulate feature alignment as a continuous-action Markov decision process solved via Proximal Policy Optimization, where the learned policy issues fault-type-specific affine corrections responsive to the current feature-space configuration, with a dual-objective reward balancing gap minimization against separability preservation. An asymmetry-aware strategy reserves real data for the Normal class while augmenting fault classes with policy-aligned simulated samples. Validation across XJTU-SY, CWRU, and a self-built slewing bearing testbed confirms the dominant gain from reinforcement learning-driven alignment, and cross-equipment linear probing achieves 92.8% without encoder retraining, demonstrating transferable monitoring capability.

</details>

---
